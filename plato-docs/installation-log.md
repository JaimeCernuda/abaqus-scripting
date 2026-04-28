# Plato Engine Installation Log

Reproducible installation guide for Plato Engine on HPC clusters.
Tested on: NCSA Delta (Red Hat 9, Cray PE, cray-mpich)

## What is Plato?

Plato is Sandia National Labs' open-source **topology optimization platform**.
It is NOT a general-purpose FEA tool — it uses FEA internally (via Plato Analyze)
to drive optimization-based design.

- **Repository**: https://github.com/sandialabs/platoengine
- **Super-project**: https://github.com/sandialabs/plato (bundles all components)
- **License**: BSD 3-Clause
- **Language**: C++ (C++20 required)

### Components

| Component | Repo | Purpose |
|---|---|---|
| `plato` | `sandialabs/plato` | Super-project (umbrella) |
| `platoengine` | `sandialabs/platoengine` | Core optimization engine (MPMD) |
| `platoanalyze` | `sandialabs/platoanalyze` | GPU-accelerated FE solver |
| `plato-spack-repo` | `sandialabs/plato-spack-repo` | Custom spack package definitions |
| `plato-integration-tests` | `sandialabs/plato-integration-tests` | Test suite |

---

## Prerequisites

### Compiler
- GCC >= 10 (needs C++20 support)
- Fortran compiler (gfortran)
- Tested with: gcc 13.3.1 (gcc-toolset-13 on RHEL9)

### MPI
- Any MPI implementation (OpenMPI, cray-mpich, MPICH)
- Tested with: cray-mpich 8.1.32

### Build Tools
- CMake >= 3.21
- Git (git-lfs recommended but not strictly required)
- Python 3.8+ (for regression tests)

### Key Dependencies (managed by spack)
- **Trilinos** 16.2.0 — the heaviest dep (~1-2 hour build)
  - ROL (optimizer), Tpetra (linear algebra), STK (mesh I/O), Krino (level set), Percept (refinement), Exodus (I/O)
- **Boost** — serialization, filesystem, mpi, log, program_options, regex
- **Kokkos** — performance portability (CPU OpenMP or CUDA)
- **OpenBLAS** — linear algebra
- **HDF5**, **NetCDF**, **CGNS** — mesh I/O (via Trilinos+exodus)

---

## Step 1: Clone the Super-Project

```bash
# Choose install location (use shared project space, not home)
PLATO_DIR=/projects/bekn/jcernuda/plato

# Clone with all submodules
git clone --recursive https://github.com/sandialabs/plato.git $PLATO_DIR
```

This clones ~5 repos:
- `plato/` (root)
- `plato/platoengine/`
- `plato/platoanalyze/`
- `plato/plato-spack-repo/`
- `plato/plato-integration-tests/`
- `plato/spack/` (bundled spack v1.1.0)

**Note**: The project bundles its own spack. This avoids version conflicts.

---

## Step 2: Initialize Spack Environment

```bash
cd $PLATO_DIR

# Set environment variables
export SUPER_PLATO_ROOT=$PLATO_DIR
export SPACK_DISABLE_LOCAL_CONFIG=true
mkdir -p "${PLATO_DIR}/cache"
export SPACK_USER_CACHE_PATH="${PLATO_DIR}/cache"

# Source the BUNDLED spack (not system spack!)
source ${PLATO_DIR}/spack/share/spack/setup-env.sh

# Create spack environment
spack env create --without-view -d .
spack env activate .

# Register Plato's custom package repo
spack repo add plato-spack-repo/plato
```

---

## Step 3: Discover System Libraries (CRITICAL)

Before configuring spack, you MUST identify the system-provided libraries and
their paths. Spack's compiler wrapper chain does NOT inherit the cluster's
module environment, so transitive dependencies (e.g., libfabric for cray-mpich)
must be explicitly provided.

### What to find

| Library | How to find | Why needed |
|---|---|---|
| **MPI** | `echo $CRAY_MPICH_DIR` or `which mpicc` | Core dependency |
| **MPI transitive deps** | `ldd $(which mpicc)` or `ldd $CRAY_MPICH_DIR/lib/libmpi*.so` | Linker needs these |
| **libfabric** | `pkg-config --libs libfabric` or check `/opt/cray/libfabric/` | Network transport for MPI |
| **PMI libs** | `ls /opt/cray/pe/lib64/libpmi*` | Process management for MPI |
| **CUDA** | `echo $CUDA_HOME` or `which nvcc` | GPU builds |
| **Compilers** | `which gcc g++ gfortran` and `gcc --version` | Must support C++20 |

### Discovery commands

```bash
# 1. Compiler paths and version
which gcc g++ gfortran
gcc --version | head -1

# 2. MPI location and version
echo $CRAY_MPICH_DIR            # Cray systems
mpicc -show                      # Shows underlying compiler + flags
mpicxx -show

# 3. MPI runtime dependencies (THE KEY STEP)
#    These libraries must be in the linker path during builds
ldd ${CRAY_MPICH_DIR}/lib/libmpi*.so | grep "=>"
#    Look for: libfabric, libpmi, libpmi2, libpals, libcxi
#    Note their directories — you'll need them in spack config

# 4. Cray PE libraries
ls /opt/cray/pe/lib64/           # libpmi.so, libpmi2.so
ls /opt/cray/libfabric/*/lib64/  # libfabric.so

# 5. CUDA (if GPU build)
echo $CUDA_HOME
nvcc --version

# 6. Verify mpicc actually works
echo 'int main(){return 0;}' | mpicc -x c - -o /tmp/test_mpi && echo "OK"
```

### Common pitfall: "C compiler cannot create executables"

On Cray PE systems, `mpicc` links against `libmpi_gnu_*.so`, which in turn
depends on `libfabric.so`, `libpmi.so`, etc. These are NOT in standard linker
paths. Spack's compiler wrapper rebuilds the link command and loses these paths.

**Fix**: Add the extra library directories to the compiler's `ldflags` and
`extra_rpaths` in `spack.yaml` (see Step 5 below).

---

## Step 4: Configure Compilers

```bash
# Auto-detect compilers
spack compiler find

# Verify
spack compiler list
```

---

## Step 5: Register External Packages

This is **cluster-specific**. The goal is to tell spack about system-provided
libraries so it doesn't build them from scratch.

**IMPORTANT**: Do NOT use `spack config add` for complex nested YAML (externals
with extra_attributes). It mangles the format. Write `spack.yaml` directly instead.

### Delta-specific externals (cray-mpich)

Write directly into `spack.yaml` packages section:

```yaml
packages:
  mpi:
    require: cray-mpich
  cray-mpich:
    buildable: false
    externals:
    - spec: cray-mpich@8.1.32
      prefix: /opt/cray/pe/mpich/8.1.32/ofi/gnu/11.2
      extra_attributes:
        compilers:
          c: /opt/cray/pe/mpich/8.1.32/ofi/gnu/11.2/bin/mpicc
          cxx: /opt/cray/pe/mpich/8.1.32/ofi/gnu/11.2/bin/mpicxx
          fortran: /opt/cray/pe/mpich/8.1.32/ofi/gnu/11.2/bin/mpif90
  libfabric:
    buildable: false
    externals:
    - spec: libfabric@1.22.0
      prefix: /opt/cray/libfabric/1.22.0
```

### Compiler config with Cray PE linker paths

The compiler section MUST include ldflags and extra_rpaths for the Cray PE
libraries that MPI depends on:

```yaml
compilers:
- compiler:
    spec: gcc@=13.3.1
    paths:
      cc: /opt/rh/gcc-toolset-13/root/usr/bin/gcc
      cxx: /opt/rh/gcc-toolset-13/root/usr/bin/g++
      f77: /opt/rh/gcc-toolset-13/root/usr/bin/gfortran
      fc: /opt/rh/gcc-toolset-13/root/usr/bin/gfortran
    flags:
      ldflags: -L/opt/cray/pe/mpich/8.1.32/ofi/gnu/11.2/lib -L/opt/cray/libfabric/1.22.0/lib64 -L/opt/cray/pe/lib64 -Wl,-rpath,/opt/cray/pe/mpich/8.1.32/ofi/gnu/11.2/lib -Wl,-rpath,/opt/cray/libfabric/1.22.0/lib64 -Wl,-rpath,/opt/cray/pe/lib64
    operating_system: rhel9
    target: x86_64
    modules: []
    environment:
      prepend_path:
        LD_LIBRARY_PATH: "/opt/cray/pe/mpich/8.1.32/ofi/gnu/11.2/lib:/opt/cray/libfabric/1.22.0/lib64:/opt/cray/pe/lib64"
        LIBRARY_PATH: "/opt/cray/pe/mpich/8.1.32/ofi/gnu/11.2/lib:/opt/cray/libfabric/1.22.0/lib64:/opt/cray/pe/lib64"
    extra_rpaths:
    - /opt/cray/pe/mpich/8.1.32/ofi/gnu/11.2/lib
    - /opt/cray/libfabric/1.22.0/lib64
    - /opt/cray/pe/lib64
```
spack config add "packages:libfabric:buildable: false"

# CUDA (if doing GPU build)
spack config add "packages:cuda:externals:
- spec: cuda@12.8
  prefix: /opt/nvidia/hpc_sdk/Linux_x86_64/25.3/cuda/12.8"
spack config add "packages:cuda:buildable: false"
```

### For other clusters (e.g., with OpenMPI)

If the cluster uses OpenMPI, you can either:
1. Let spack build OpenMPI (simpler, slower)
2. Register it as external:
```bash
spack config add "packages:openmpi:externals:
- spec: openmpi@4.1.6
  prefix: /path/to/openmpi"
```

---

## Step 5: Configure Build Spec

```bash
# Set up develop specs (build from local source checkout)
spack develop -p ${PLATO_DIR}/platoengine -b ${PLATO_DIR}/build/platoengine platoengine@develop
spack develop -p ${PLATO_DIR}/platoanalyze -b ${PLATO_DIR}/build/platoanalyze platoanalyze@develop

# CPU build (recommended first):
spack add platoanalyze@develop~amgx~cuda+tacho+umfpack+enginemesh+integration_tests+openmp \
  ^platoengine@develop~esp+regression+unit_testing~sierra_tests \
  ^openblas threads=openmp

# GPU build (after CPU works, for A100 = cuda_arch=80):
# spack add platoanalyze@develop+amgx+cuda+enginemesh+integration_tests+tacho+verificationtests \
#   ^amgx cuda_arch=80 ^trilinos cuda_arch=80 \
#   ^platoengine@develop~esp+regression+unit_testing~sierra_tests
```

### Variant Reference

**platoanalyze variants**:
| Variant | Default | Description |
|---|---|---|
| `cuda` | on | NVIDIA GPU support |
| `amgx` | on | NVIDIA algebraic multigrid (requires cuda) |
| `tacho` | off | Tacho direct solver from Trilinos |
| `umfpack` | off | UMFPACK sparse solver |
| `enginemesh` | on | Use engine mesh (vs omega-h) |
| `openmp` | off | OpenMP threading (conflicts with cuda) |
| `integration_tests` | on | Build integration tests |

**platoengine variants**:
| Variant | Default | Description |
|---|---|---|
| `esp` | off | Engineering Sketch Pad (CAD kernel) |
| `snopt` | off | SNOPT optimizer (commercial) |
| `regression` | on | Regression tests |
| `unit_testing` | on | Unit tests |
| `openmp` | off | OpenMP support |
| `python` | off | Python plugin support |

---

## Step 6: Concretize and Build

**IMPORTANT: Run on a compute node, not the login node!**

### Interactive build

```bash
# Get a compute node (adjust account/partition for your cluster)
srun --account=bekn-delta-cpu --partition=cpu --time=06:00:00 \
  --mem=128g --cpus-per-task=64 --pty bash

# Then run:
cd $PLATO_DIR
source spack/share/spack/setup-env.sh
spack env activate .
spack concretize --force
spack install --verbose
```

### Batch build (recommended)

See `build-delta.sh` for a complete SLURM batch script.

```bash
sbatch build-delta.sh
```

Expected build time: **2-6 hours** depending on core count. Trilinos is the bottleneck.

---

## Step 7: Verify Installation

```bash
source ${PLATO_DIR}/spack/share/spack/setup-env.sh
spack env activate ${PLATO_DIR}
source ${PLATO_DIR}/utilities/test-env.sh

# Check executables
which plato
which analyze_MPMD

# Run a simple test
cd ${PLATO_DIR}/plato-integration-tests
# (follow test instructions)
```

---

## Step 8: Create Module File (for shared access)

To make Plato available as an Lmod module for other users:

```bash
# Create module directory
mkdir -p /projects/bekn/modulefiles/plato

# Create module file
cat > /projects/bekn/modulefiles/plato/develop.lua << 'EOF'
-- Plato Engine (Topology Optimization Platform)
-- Built from: https://github.com/sandialabs/plato

help([[
Plato Engine - Platform for Topology Optimization
Sandia National Laboratories (open-source, BSD 3-Clause)
]])

whatis("Name: Plato Engine")
whatis("Version: develop")
whatis("Description: Topology optimization platform with GPU-accelerated FEA")

local plato_root = "/projects/bekn/jcernuda/plato"

-- Source spack environment
execute {
    cmd = "source " .. plato_root .. "/spack/share/spack/setup-env.sh && spack env activate " .. plato_root,
    modeA = {"load"}
}

-- Add binaries to PATH
prepend_path("PATH", plato_root .. "/build/platoengine/bin")
prepend_path("PATH", plato_root .. "/build/platoanalyze/bin")
prepend_path("LD_LIBRARY_PATH", plato_root .. "/build/platoengine/lib")
prepend_path("LD_LIBRARY_PATH", plato_root .. "/build/platoanalyze/lib")

setenv("PLATO_ROOT", plato_root)
EOF

# Tell Lmod where to find it
module use /projects/bekn/modulefiles
module avail plato
module load plato/develop
```

Add `module use /projects/bekn/modulefiles` to your `.bashrc` or team's shared setup.

---

## Troubleshooting

### Common Issues

1. **spack concretize fails with MPI conflicts**
   - Ensure `packages:mpi:require` matches your external MPI spec exactly
   - Check `spack config get packages` to verify

2. **Trilinos build fails**
   - Most common cause: incompatible HDF5 version (needs <= 1.14.2)
   - Check `concretize.log` for the resolved HDF5 version

3. **C++20 errors**
   - Ensure gcc >= 10 (ideally >= 13)
   - Check `spack compiler list` shows the right version

4. **Out of disk space during build**
   - Trilinos build artifacts are large (~10-20 GB)
   - Use project/scratch space, not home directory

5. **cray-mpich not found by spack**
   - The `extra_attributes.compilers` block is required for cray-mpich
   - Verify paths: `ls ${CRAY_MPICH_DIR}/bin/mpicc`

---

## File Locations (Delta)

| What | Path |
|---|---|
| Plato install | `/projects/bekn/jcernuda/plato` |
| Build output | `/projects/bekn/jcernuda/plato/build/` |
| Spack cache | `/projects/bekn/jcernuda/plato/cache/` |
| Build script | `/projects/bekn/jcernuda/plato/build-delta.sh` |
| Build logs | `/projects/bekn/jcernuda/plato/plato-build-*.out` |
| Module files | `/projects/bekn/modulefiles/plato/` |
| This documentation | `abaqus-scripting/plato-docs/` |

---

## Cluster Adaptation Checklist

When porting to a new cluster:

1. [ ] Clone super-project to shared storage
2. [ ] `spack compiler find` — verify gcc >= 10 with C++20
3. [ ] **Discover system libraries** — find MPI, libfabric, PMI, CUDA paths
4. [ ] **`ldd` the MPI library** — identify ALL transitive deps and their dirs
5. [ ] Register MPI as external (cray-mpich, OpenMPI, Intel MPI, etc.)
6. [ ] Register CUDA as external (if GPU build)
7. [ ] **Add MPI transitive dep paths to compiler ldflags + extra_rpaths**
8. [ ] Write `spack.yaml` directly (do NOT use `spack config add` for complex YAML)
9. [ ] Adjust SLURM directives in build script (account, partition, time)
10. [ ] `spack concretize --force` — check for conflicts
11. [ ] `spack install` on a compute node
12. [ ] Create Lmod module file for team access
13. [ ] Test with a simple optimization problem
