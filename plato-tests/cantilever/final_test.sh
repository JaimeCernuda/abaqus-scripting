#!/bin/bash
#SBATCH --job-name=plato-final
#SBATCH --account=bekn-delta-cpu
#SBATCH --partition=cpu
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=32g
#SBATCH --time=01:00:00
#SBATCH --output=plato-final-%j.out
#SBATCH --error=plato-final-%j.err

set -uo pipefail
WORKDIR=/projects/bekn/jcernuda/plato-tests/cantilever
cd $WORKDIR

echo "=========================================="
echo "  PLATO CANTILEVER TOPOLOGY OPTIMIZATION"
echo "  $(date)"
echo "=========================================="

# ============================================
# Step 1: Generate mesh (system python, before spack)
# ============================================
echo ""
echo "=== Step 1: Mesh Generation ==="
rm -rf run && mkdir -p run && cd run
/usr/bin/python3 $WORKDIR/generate_mesh_simple.py
cp $WORKDIR/analyze_compliance.xml $WORKDIR/analyze_volume.xml $WORKDIR/input.i .
echo "Mesh ready."

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
# Step 3: Run optimization (50 iterations)
# ============================================
echo ""
echo "=== Step 3: Topology Optimization (50 iter) ==="
time srun -n 1 plato input.i 2>&1
echo "Exit: $?"
echo "Output files:"
ls -la *.exo 2>/dev/null

# ============================================
# Step 4: Extract results
# ============================================
echo ""
echo "=== Step 4: Results ==="
PYTHONPATH="" /usr/bin/python3 $WORKDIR/extract_results.py 2>&1

# ============================================
# Step 5: Render images with ParaView
# ============================================
echo ""
echo "=== Step 5: Render Images ==="
module load paraview/6.0.1-prebuilt 2>/dev/null

if [ -f result.exo ] && command -v pvpython &> /dev/null; then
    echo "Using pvpython: $(which pvpython)"
    # Use pvpython with offscreen rendering
    pvpython --force-offscreen-rendering $WORKDIR/render_results.py 2>&1 || {
        echo "pvpython failed, trying without --force-offscreen-rendering..."
        pvpython $WORKDIR/render_results.py 2>&1 || echo "Rendering failed."
    }
    echo "Images:"
    ls -la *.png 2>/dev/null
    cp *.png $WORKDIR/ 2>/dev/null
else
    echo "Skipped (result.exo: $(ls result.exo 2>&1))"
fi

echo ""
echo "=========================================="
echo "  COMPLETE at $(date)"
echo "=========================================="
