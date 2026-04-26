#!/bin/bash
#SBATCH --job-name=in718-plato
#SBATCH --account=bekn-delta-cpu
#SBATCH --partition=cpu
#SBATCH --nodes=2
#SBATCH --ntasks=3
#SBATCH --cpus-per-task=16
#SBATCH --mem=64g
#SBATCH --time=02:00:00
#SBATCH --output=in718-plato-%j.out
#SBATCH --error=in718-plato-%j.err

set -uo pipefail
WORKDIR=/projects/bekn/jcernuda/plato-tests/in718_specimen
cd $WORKDIR

echo "=========================================="
echo "  IN718 SPECIMEN TOPOLOGY OPTIMIZATION"
echo "  Multi-load-case (3 objectives, 2 nodes)"
echo "  $(date)"
echo "=========================================="
echo "  Nodes: $SLURM_NNODES"
echo "  Tasks: $SLURM_NTASKS"
echo "  CPUs/task: $SLURM_CPUS_PER_TASK"
echo "  Host: $(hostname)"

# ============================================
# Step 1: Generate mesh (system python, before spack)
# ============================================
echo ""
echo "=== Step 1: Mesh Generation ==="
rm -rf run && mkdir -p run && cd run
/usr/bin/python3 $WORKDIR/generate_mesh.py
cp $WORKDIR/analyze_lc1.xml $WORKDIR/analyze_lc2.xml $WORKDIR/analyze_lc3.xml \
   $WORKDIR/analyze_volume.xml $WORKDIR/input.i .
echo "Mesh ready."

# Verify mesh
if [ ! -f mesh.exo ]; then
    echo "ERROR: mesh.exo not generated!"
    exit 1
fi
echo "mesh.exo: $(ls -la mesh.exo)"

# ============================================
# Step 2: Load Plato
# ============================================
echo ""
echo "=== Step 2: Load Plato ==="
source /projects/bekn/jcernuda/plato/spack/share/spack/setup-env.sh
spack env activate /projects/bekn/jcernuda/plato
spack load platoanalyze
export LD_LIBRARY_PATH="/opt/cray/pe/mpich/8.1.32/ofi/gnu/11.2/lib:/opt/cray/libfabric/1.22.0/lib64:/opt/cray/pe/lib64:${LD_LIBRARY_PATH:-}"
export OMP_PROC_BIND=spread
export OMP_PLACES=threads
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK:-16}
echo "Plato: $(which plato)"
echo "OMP_NUM_THREADS: $OMP_NUM_THREADS"

# ============================================
# Step 3: Run optimization (3 ranks, 50 iterations)
# ============================================
echo ""
echo "=== Step 3: Topology Optimization (50 iter, 3 load cases) ==="
echo "Running with srun -n 3 (1 rank per load case objective)..."
time srun -n 3 plato input.i 2>&1
OPT_EXIT=$?
echo "Exit: $OPT_EXIT"
echo ""
echo "Output files:"
ls -la *.exo 2>/dev/null

# ============================================
# Step 4: Extract results
# ============================================
echo ""
echo "=== Step 4: Results ==="
if [ -f result.exo ]; then
    echo "result.exo exists ($(stat -c%s result.exo) bytes)"
else
    echo "WARNING: result.exo not found"
    # Check for restart
    ls -la restart_result.exo 2>/dev/null
fi

# ============================================
# Step 5: Render images with matplotlib (headless)
# ============================================
echo ""
echo "=== Step 5: Render Images ==="
if [ -f result.exo ]; then
    PYTHONPATH="" /usr/bin/python3 $WORKDIR/render_matplotlib.py 2>&1
    echo "Images:"
    ls -la *.png 2>/dev/null
    cp *.png $WORKDIR/ 2>/dev/null
else
    echo "Skipped (no result.exo)"
fi

# ============================================
# Summary
# ============================================
echo ""
echo "=========================================="
echo "  COMPLETE at $(date)"
echo "  Optimization exit code: $OPT_EXIT"
echo "=========================================="
echo ""
echo "Files in run directory:"
ls -la
