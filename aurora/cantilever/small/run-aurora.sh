#!/bin/bash
#PBS -A gpu_hack
#PBS -q gpu_hack
#PBS -l select=1
#PBS -l walltime=00:30:00
#PBS -l filesystems=home:flare
#PBS -N plato-cantilever
#PBS -j oe
#PBS -o /home/jcernuda/plato-runs/cantilever/run.log

# Plato cantilever topology optimization smoke test on Aurora (CPU build)
# Submit:  qsub /home/jcernuda/plato-runs/cantilever/run-aurora.sh
# Monitor: tail -f /home/jcernuda/plato-runs/cantilever/run.log

set -uo pipefail
WORKDIR=/home/jcernuda/plato-runs/cantilever
cd "$WORKDIR"

echo "=========================================="
echo "  PLATO CANTILEVER TOPOLOGY OPTIMIZATION"
echo "  $(date)"
echo "  Host: $(hostname)"
echo "=========================================="

# === Step 1: Mesh generation (system python with user-installed gmsh) ===
echo ""
echo "=== Step 1: Mesh Generation ==="
source /usr/share/lmod/lmod/init/bash 2>/dev/null || true
module load python/3.12.12
rm -rf run && mkdir -p run && cd run
python "$WORKDIR/generate_mesh_simple.py"
cp "$WORKDIR"/{analyze_compliance.xml,analyze_volume.xml,input.i} .
echo "Mesh:"; ls -la mesh.exo

# === Step 2: Activate Plato spack env ===
echo ""
echo "=== Step 2: Load Plato ==="
module unload python/3.12.12 || true
module load oneapi/release/2025.3.1 mpich/opt/5.0.0.aurora_test.3c70a61 libfabric/1.22.0 cmake
source /home/jcernuda/plato/spack/share/spack/setup-env.sh
spack env activate /home/jcernuda/plato
spack load platoanalyze platoengine

# OpenMP threading for CPU+OpenMP build
export OMP_PROC_BIND=spread
export OMP_PLACES=threads
NCORES=$(nproc)
export OMP_NUM_THREADS=${OMP_NUM_THREADS:-$NCORES}

echo "plato: $(which plato)"
echo "analyze: $(which analyze)"
echo "OMP_NUM_THREADS=$OMP_NUM_THREADS"

# === Step 3: Run optimization ===
echo ""
echo "=== Step 3: Topology Optimization (50 iter) ==="
time mpiexec -n 1 plato input.i 2>&1
PLATO_RC=$?
echo "Plato exit code: $PLATO_RC"
echo "Output exodus files:"
ls -la *.exo 2>/dev/null

# === Step 4: Extract results ===
echo ""
echo "=== Step 4: Results Extraction ==="
module load python/3.12.12
python "$WORKDIR/extract_results.py" 2>&1 || echo "extract failed"

# === Step 5: Render ===
echo ""
echo "=== Step 5: Visualization (matplotlib) ==="
python "$WORKDIR/render_matplotlib.py" 2>&1 || echo "render failed"
echo "Rendered images:"
ls -la *.png 2>/dev/null

cp run/result.exo "$WORKDIR/" 2>/dev/null
cp run/*.png "$WORKDIR/" 2>/dev/null

echo ""
echo "=========================================="
echo "  COMPLETE at $(date)"
echo "=========================================="
