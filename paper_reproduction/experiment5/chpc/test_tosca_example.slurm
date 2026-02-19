#!/bin/bash
#SBATCH --job-name=test_tosca_ex
#SBATCH --account=hochhalter
#SBATCH --partition=kingspeak
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --time=1:00:00
#SBATCH --mem=8G
#SBATCH -o test_tosca_ex_%j.out
#SBATCH -e test_tosca_ex_%j.err

# ============================================================================
# Smoke test: run a built-in Tosca example to verify Tosca works at all
# ============================================================================

unset SLURM_GTIDS
export I_MPI_HYDRA_TOPOLIB=ipl

source /uufs/chpc.utah.edu/sys/installdir/abaqus/setup_ab_slurm.sh

# Create temp directory and copy example files
WORKDIR=$(mktemp -d $HOME/tosca_test_XXXXXX)
cd $WORKDIR

echo "============================================"
echo "Tosca Example Smoke Test"
echo "Started: $(date)"
echo "Working dir: $WORKDIR"
echo "============================================"

# Copy the airbeam_vol example (simple topology optimization)
EXAMPLE_DIR=/uufs/chpc.utah.edu/sys/installdir/abaqus/2025/linux_a64/SMATsoResources/abaqus/examples/topo/airbeam_vol
cp $EXAMPLE_DIR/airbeam_vol.par .
cp $EXAMPLE_DIR/airbeam_vol.inp .

# Limit to 2 iterations for speed
sed -i 's/ITER_MAX.*=.*80/ITER_MAX = 2/' airbeam_vol.par

echo ""
echo "Files:"
ls -la
echo ""
echo "Modified .par file:"
cat airbeam_vol.par

# Set cpus in env file to avoid str/int bug
cat > abaqus_v6.env << 'EOF'
import os
cpus = int(os.environ.get('SLURM_NTASKS', '1'))
EOF

echo ""
echo "Running: abaqus optimization task=airbeam_vol.par job=airbeam_test interactive"
abaqus optimization task=airbeam_vol.par job=airbeam_test interactive 2>&1
echo "Exit code: $?"

echo ""
echo "Results:"
ls -la airbeam_test/ 2>/dev/null || echo "No results directory"
ls -la airbeam_test/TOSCA_POST/ 2>/dev/null || echo "No TOSCA_POST"

if [ -f airbeam_test/TOSCA.OUT ]; then
    echo ""
    echo "TOSCA.OUT:"
    cat airbeam_test/TOSCA.OUT
fi

echo ""
echo "============================================"
echo "Complete: $(date)"
echo "============================================"

# Cleanup
rm -rf $WORKDIR
