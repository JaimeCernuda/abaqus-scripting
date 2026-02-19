#!/bin/bash
#SBATCH --job-name=simple_to
#SBATCH --account=hochhalter
#SBATCH --partition=kingspeak
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=1:00:00
#SBATCH --mem=8G
#SBATCH -o simple_to_%j.out
#SBATCH -e simple_to_%j.err

# ============================================================================
# Experiment 6: Simplest possible topology optimization
#
# Block, fixed one end, pressure other end.
# Minimize strain energy, volume <= 50%.
# Single CPU to rule out MPI issues.
# ============================================================================

unset SLURM_GTIDS
export I_MPI_HYDRA_TOPOLIB=ipl

source /uufs/chpc.utah.edu/sys/installdir/abaqus/setup_ab_slurm.sh

export ABAQUS_NUM_CPUS=1
export ABAQUS_MAX_CYCLES=3

cd $HOME/Abaqus/paper_reproduction/experiment6

echo "============================================"
echo "Experiment 6: Simple TO Test"
echo "Started: $(date)"
echo "CPUs: 1, Max cycles: 3"
echo "============================================"

# Clean slate
rm -rf SimpleTO* abaqus.rpy* *.jnl *.rec *.log *.exception

# Set cpus as integer in env file
cat > abaqus_v6.env << 'EOF'
import os
cpus = int(os.environ.get('ABAQUS_NUM_CPUS', '1'))
EOF

# Run it
echo ""
echo "Running: abaqus cae noGUI=scripts/run_topology_optimization.py"
abaqus cae noGUI=scripts/run_topology_optimization.py 2>&1
EXIT_CODE=$?
echo ""
echo "Exit code: $EXIT_CODE"

# Check what happened
echo ""
echo "Files created:"
ls -la
echo ""

# Look for results
if [ -d SimpleTO_Opt ]; then
    echo "SimpleTO_Opt/ contents:"
    ls -la SimpleTO_Opt/
    if [ -d SimpleTO_Opt/TOSCA_POST ]; then
        echo ""
        echo "PASSED: TOSCA_POST exists"
        ls -la SimpleTO_Opt/TOSCA_POST/
    fi
    if [ -f SimpleTO_Opt/TOSCA.OUT ]; then
        echo ""
        echo "TOSCA.OUT:"
        cat SimpleTO_Opt/TOSCA.OUT
    fi
fi

# Check for crash
if ls *.exception 2>/dev/null; then
    echo ""
    echo "Exception files found:"
    for f in *.exception; do
        echo "--- $f ---"
        head -30 "$f"
    done
fi

echo ""
echo "============================================"
echo "Complete: $(date)"
echo "============================================"
