#!/bin/bash
#SBATCH --job-name=test_par_gen
#SBATCH --account=hochhalter
#SBATCH --partition=kingspeak
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --time=2:00:00
#SBATCH --mem=8G
#SBATCH -o test_par_gen_%j.out
#SBATCH -e test_par_gen_%j.err

# ============================================================================
# Test: Full Tosca pipeline via CLI with flat .inp
#
# 1) create_design_space.py — geometry + mesh (Abaqus CAE)
# 2) setup_optimization.py — BCs, loads, opt task, write .inp (Abaqus CAE)
# 3) flatten_inp.py         — convert assembly .inp to flat format (Python)
# 4) generate_par_file.py   — write .par file (Python)
# 5) abaqus optimization    — run Tosca (CLI)
#
# Pass: TOSCA_POST/ with .odb files
# ============================================================================

unset SLURM_GTIDS
export I_MPI_HYDRA_TOPOLIB=ipl

source /uufs/chpc.utah.edu/sys/installdir/abaqus/setup_ab_slurm.sh

export ABAQUS_MESH_SIZE=3.0
export ABAQUS_NUM_CPUS=$SLURM_NTASKS
export ABAQUS_MAX_CYCLES=3

cd $HOME/Abaqus/paper_reproduction/experiment5

echo "============================================"
echo "Test: Flat .inp + .par + Tosca CLI"
echo "Started: $(date)"
echo "Tasks: $SLURM_NTASKS, Max cycles: $ABAQUS_MAX_CYCLES"
echo "============================================"

# Clean up
echo ""
echo "Cleaning up..."
rm -rf Experiment5_Optimization Experiment5_TO Experiment5_FEA
rm -f Experiment5_TO.{cae,inp,par,log,sta,dat,msg,com,prt,sim,023,mdl,stt,odb,res,lck}
rm -f Experiment5_FEA.{inp,log,sta,dat,msg,com,prt,sim,023,mdl,stt,odb,res,lck}
rm -f Experiment5_FEA_flat.inp
rm -f *.par abaqus.rpy abaqus.rpy.* *.jnl *.rec authorization.log

# Step 1: Create design space
echo ""
echo "[1/5] Creating design space..."
abaqus cae noGUI=scripts/create_design_space.py
if [ $? -ne 0 ]; then
    echo "FAILED: Design space creation"
    exit 1
fi

# Step 2: Setup optimization + write .inp
echo ""
echo "[2/5] Setting up optimization..."
abaqus cae noGUI=scripts/setup_optimization.py
if [ $? -ne 0 ]; then
    echo "FAILED: Optimization setup"
    exit 1
fi

# Verify .inp exists
if [ ! -f Experiment5_FEA.inp ]; then
    echo "FAILED: Experiment5_FEA.inp not found"
    ls -la *.inp 2>/dev/null
    exit 1
fi
echo "  .inp file: $(wc -l < Experiment5_FEA.inp) lines"

# Step 3: Flatten .inp (remove assembly structure for Tosca)
echo ""
echo "[3/5] Flattening .inp file..."
python3 scripts/flatten_inp.py
if [ ! -f Experiment5_FEA_flat.inp ]; then
    echo "FAILED: Flat .inp not generated"
    exit 1
fi
echo "  Flat .inp: $(wc -l < Experiment5_FEA_flat.inp) lines"

# Quick sanity check: flat file should NOT contain *Part or *Assembly
if grep -q '^\*Part,' Experiment5_FEA_flat.inp; then
    echo "WARNING: Flat .inp still contains *Part"
fi
if grep -q '^\*Assembly,' Experiment5_FEA_flat.inp; then
    echo "WARNING: Flat .inp still contains *Assembly"
fi

# Show structure of flat file (keyword lines only)
echo "  Keyword structure:"
grep '^\*[A-Za-z]' Experiment5_FEA_flat.inp | head -30

# Step 4: Generate .par file
echo ""
echo "[4/5] Generating .par file..."
python3 scripts/generate_par_file.py
if [ ! -f Experiment5_TO.par ]; then
    echo "FAILED: .par file not generated"
    exit 1
fi
echo "  .par contents:"
cat Experiment5_TO.par

# Step 5: Run Tosca via CLI
echo ""
echo "[5/5] Running Tosca optimization..."
cat > abaqus_v6.env << 'ENVEOF'
import os
cpus = int(os.environ.get('SLURM_NTASKS', '1'))
ENVEOF

echo "  Command: abaqus optimization task=Experiment5_TO.par job=Experiment5_TO interactive"
abaqus optimization task=Experiment5_TO.par job=Experiment5_TO interactive 2>&1
OPT_EXIT=$?
echo "  Tosca exit code: $OPT_EXIT"

# Check results
echo ""
echo "Checking results..."
if [ -f Experiment5_TO/TOSCA.OUT ]; then
    echo "  TOSCA.OUT (last 30 lines):"
    tail -30 Experiment5_TO/TOSCA.OUT
fi

TOSCA_FOUND=0
for dir in . Experiment5_TO; do
    if [ -d "${dir}/TOSCA_POST" ]; then
        ODB_COUNT=$(ls ${dir}/TOSCA_POST/*.odb 2>/dev/null | wc -l)
        echo ""
        echo "PASSED: Tosca ran — ${ODB_COUNT} design cycle ODB(s) in ${dir}/TOSCA_POST"
        ls -la ${dir}/TOSCA_POST/ 2>/dev/null | head -20
        TOSCA_FOUND=1
        break
    fi
done

if [ $TOSCA_FOUND -eq 0 ]; then
    echo "FAILED: No TOSCA_POST directory"
    echo ""
    echo "Diagnostics:"
    find . -name "TOSCA_POST" -type d 2>/dev/null || echo "  No TOSCA_POST anywhere"
    find . -name "TOSCA.OUT" 2>/dev/null
    echo ""
    if [ -d Experiment5_TO ]; then
        echo "  Experiment5_TO/ contents:"
        ls -la Experiment5_TO/
        if [ -d Experiment5_TO/DB_ERROR ]; then
            echo ""
            echo "  DB_ERROR/ contents:"
            ls -la Experiment5_TO/DB_ERROR/
            cat Experiment5_TO/DB_ERROR/*.json 2>/dev/null
        fi
    fi
fi

echo ""
echo "============================================"
echo "Test Complete: $(date)"
echo "============================================"
