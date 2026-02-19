#!/bin/bash
#SBATCH --job-name=exp6_diag
#SBATCH --account=notchpeak-shared-short
#SBATCH --partition=notchpeak-shared-short
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=1:00:00
#SBATCH --mem=8G
#SBATCH -o exp6_diag_%j.out
#SBATCH -e exp6_diag_%j.err

# ============================================================================
# Experiment 6 Diagnostic: Capture all generated files before submit()
# ============================================================================

module load abaqus/2025

unset SLURM_GTIDS
export I_MPI_HYDRA_TOPOLIB=ipl
export ABAQUS_NUM_CPUS=1
export ABAQUS_MAX_CYCLES=3

cd $HOME/Abaqus/paper_reproduction/experiment6

echo "============================================"
echo "Experiment 6: Diagnostic Run"
echo "Started: $(date)"
echo "Node: $(hostname)"
echo "============================================"

# Clean previous run
rm -rf SimpleTO* abaqus.rpy* *.jnl *.rec *.log *.exception *.inp *.par

# Set cpus as integer
cat > abaqus_v6.env << 'EOF'
import os
cpus = int(os.environ.get('ABAQUS_NUM_CPUS', '1'))
EOF

echo ""
echo "which abaqus: $(which abaqus)"
echo "which tosca: $(which tosca 2>/dev/null || echo 'not found')"
echo ""

# Run diagnostic script
abaqus cae noGUI=scripts/run_diagnostic.py 2>&1
EXIT_CODE=$?

echo ""
echo "============================================"
echo "Exit code: $EXIT_CODE"
echo "============================================"

# Capture everything
echo ""
echo "All files in working directory:"
find . -maxdepth 1 -type f -printf '%s\t%p\n' | sort -k2
echo ""
echo "All directories:"
find . -maxdepth 2 -type d | sort

# Show contents of any .par files
for f in $(find . -name "*.par" -type f 2>/dev/null); do
    echo ""
    echo "=== $f ==="
    cat "$f"
done

# Show first 50 lines of any .inp files
for f in $(find . -name "*.inp" -type f 2>/dev/null); do
    echo ""
    echo "=== $f (first 50 lines) ==="
    head -50 "$f"
    echo "... ($(wc -l < "$f") total lines)"
done

# Show exception files
for f in $(find . -name "*.exception" -type f 2>/dev/null); do
    echo ""
    echo "=== $f ==="
    cat "$f"
done

echo ""
echo "============================================"
echo "Complete: $(date)"
echo "============================================"
