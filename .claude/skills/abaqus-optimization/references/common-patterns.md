# Tosca CLI Common Patterns

All code in this file is taken from working experiment scripts in this repository.

## Pattern 0: Generate Flat .inp with noPartsInputFile (Preferred)

The simplest way to produce a flat `.inp` for Tosca — no manual flattening needed:

```python
# Set model to write flat .inp (no *Part/*Instance/*Assembly hierarchy)
mdb.models['Model-1'].setValues(noPartsInputFile=ON)

# Write input file — produces flat .inp directly
mdb.Job(name=job_name, model='Model-1', numCpus=NUM_CPUS, numDomains=NUM_CPUS)
mdb.jobs[job_name].writeInput()
```

This replaces the manual flattening process in Patterns 1-2 below. Set names appear directly without `<assembly>_<instance>_` prefixes.

## Pattern 1: Flatten .inp for Tosca (Legacy)

**Note:** This is the legacy approach. Prefer `noPartsInputFile=ON` (Pattern 0) instead.

Abaqus CAE writes hierarchical `.inp` files with `*Part`/`*Instance`/`*Assembly` wrappers. Tosca cannot read this format. This code flattens the `.inp` by removing the hierarchy and stripping instance references.

Source: `paper_reproduction/experiment10/scripts/exp10_optimize.py` (Phase 7)

```python
import re

inp_file = 'Model_FEA.inp'
instance_name = 'PartName-1'  # The instance name used in the assembly

with open(inp_file, 'r') as f:
    inp_text = f.read()

inp_lines = inp_text.split('\n')

# --- Step 1: Find max mesh node ID and collect assembly RP node info ---
# Parse the file structure to identify Part vs Assembly sections
max_mesh_node = 0
rp_nodes = {}  # old_id -> coordinate line
section = None  # 'part', 'instance', 'assembly_post_instance', None
in_node_block = False

for line in inp_lines:
    stripped = line.strip()
    upper = stripped.upper()

    # Track sections
    if upper.startswith('*PART'):
        section = 'part'
        in_node_block = False
        continue
    if upper.startswith('*END PART'):
        section = None
        in_node_block = False
        continue
    if upper.startswith('*INSTANCE'):
        section = 'instance'
        continue
    if upper.startswith('*END INSTANCE'):
        section = 'assembly_post_instance'
        continue
    if upper.startswith('*END ASSEMBLY'):
        section = None
        continue

    # Inside *Part: find max node ID
    if section == 'part':
        if upper.startswith('*NODE'):
            in_node_block = True
            continue
        if in_node_block:
            if upper.startswith('*'):
                in_node_block = False
            else:
                parts_list = stripped.split(',')
                if parts_list and parts_list[0].strip().isdigit():
                    nid = int(parts_list[0].strip())
                    if nid > max_mesh_node:
                        max_mesh_node = nid

    # After *End Instance: collect RP nodes
    if section == 'assembly_post_instance':
        if upper.startswith('*NODE'):
            continue  # skip keyword, read data on next iteration
        if not upper.startswith('*') and not upper.startswith('**'):
            parts_list = stripped.split(',')
            if len(parts_list) >= 4 and parts_list[0].strip().isdigit():
                old_id = int(parts_list[0].strip())
                rp_nodes[old_id] = stripped

# --- Step 2: Build RP node renumbering map ---
rp_offset = max_mesh_node
rp_node_map = {}
for old_id in rp_nodes:
    rp_node_map[old_id] = old_id + rp_offset

print("Max mesh node ID: {}".format(max_mesh_node))
print("RP node remapping: {}".format(rp_node_map))

# --- Step 3: Flatten with renumbering ---
# (see Pattern 2 for the full flatten loop)
```

## Pattern 2: RP Node Renumbering in Flatten Loop (Legacy)

**Note:** This is the legacy approach. When using `noPartsInputFile=ON` (Pattern 0), RP nodes are already correctly numbered and no renumbering is needed.

Assembly-level reference point (RP) nodes are numbered 1, 2, 3, etc. -- which collide with mesh node IDs. This code renumbers them during flattening.

Source: `paper_reproduction/experiment10/scripts/exp10_optimize.py` (Phase 7, Step 2)

```python
rp_nset_names = {'UpperRP', 'LowerLeftRP', 'LowerRightRP'}  # Your RP set names
flat_lines = []
current_nset_is_rp = False
section = None
in_rp_node = False

for line in inp_lines:
    stripped = line.strip()
    upper = stripped.upper()

    # Skip wrapper lines
    if upper.startswith('*PART') and not upper.startswith('*PART,'):
        section = 'part'
        continue
    if upper.startswith('*PART,'):
        section = 'part'
        continue
    if upper.startswith('*END PART'):
        section = None
        continue
    if upper.startswith('*INSTANCE'):
        section = 'instance'
        continue
    if upper.startswith('*END INSTANCE'):
        section = 'assembly_post'
        in_rp_node = False
        continue
    if upper.startswith('*ASSEMBLY'):
        continue
    if upper.startswith('*END ASSEMBLY'):
        section = None
        continue

    # In assembly after instance: handle RP *Node blocks
    if section == 'assembly_post':
        if upper.startswith('*NODE'):
            in_rp_node = True
            flat_lines.append(line + '\n')
            continue
        if in_rp_node and not upper.startswith('*') and not upper.startswith('**') and stripped:
            # Renumber this RP node
            parts_list = stripped.split(',')
            if parts_list and parts_list[0].strip().isdigit():
                old_id = int(parts_list[0].strip())
                if old_id in rp_node_map:
                    parts_list[0] = '      ' + str(rp_node_map[old_id])
                    flat_lines.append(','.join(parts_list) + '\n')
                    continue
        if upper.startswith('*') and not upper.startswith('**'):
            in_rp_node = False
            section = 'assembly_sets'

    # Remove 'internal' from set definitions
    if upper.startswith('*ELSET') or upper.startswith('*NSET'):
        parts_list = line.split(',')
        parts_list = [p for p in parts_list if 'INTERNAL' not in p.upper()]
        line = ','.join(parts_list)
        stripped = line.strip()
        upper = stripped.upper()

    # Strip instance= from keyword lines
    line = re.sub(r',\s*instance=' + re.escape(instance_name), '', line,
                  flags=re.IGNORECASE)

    # Strip instance prefix from data lines
    line = line.replace(instance_name + '.', '')

    # Track if we're in an RP nset and renumber node IDs
    if upper.startswith('*NSET'):
        current_nset_is_rp = False
        for p in line.split(','):
            if 'NSET=' in p.upper():
                nset_name = p.split('=')[1].strip()
                if nset_name in rp_nset_names:
                    current_nset_is_rp = True
                break
        flat_lines.append(line + '\n' if not line.endswith('\n') else line)
        continue

    if current_nset_is_rp:
        if upper.startswith('*'):
            current_nset_is_rp = False
        elif stripped:
            tokens = stripped.rstrip(',').split(',')
            new_tokens = []
            for t in tokens:
                t = t.strip()
                if t.isdigit() and int(t) in rp_node_map:
                    new_tokens.append(str(rp_node_map[int(t)]))
                else:
                    new_tokens.append(t)
            flat_lines.append(' ' + ', '.join(new_tokens) + ',\n')
            continue

    flat_lines.append(line + '\n' if not line.endswith('\n') else line)

flat_inp = ''.join(flat_lines)
flat_name = 'Model_flat.inp'
with open(flat_name, 'w') as f:
    f.write(flat_inp)

# Verify RP nodes were renumbered
for old_id, new_id in rp_node_map.items():
    if str(new_id) in flat_inp:
        print("Verified: RP node {} -> {} found in flat .inp".format(old_id, new_id))
    else:
        print("WARNING: RP node {} -> {} NOT found in flat .inp!".format(old_id, new_id))
```

## Pattern 3: Full SLURM Submission Script for CHPC

Source: `paper_reproduction/experiment10/chpc/run_exp10_production.slurm`

```bash
#!/bin/bash
#SBATCH --job-name=topo_opt
#SBATCH --account=hochhalter
#SBATCH --partition=kingspeak
#SBATCH --qos=kingspeak
#SBATCH -M kingspeak
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --time=48:00:00
#SBATCH --mem=120G
#SBATCH -o opt_%j.out
#SBATCH -e opt_%j.err

# --- Module and environment setup ---
module load abaqus/2025
unset SLURM_GTIDS                    # Prevents Abaqus MPI issues
export I_MPI_HYDRA_TOPOLIB=ipl       # Intel MPI topology

# --- Configuration via environment variables ---
EXP_DIR=$HOME/Abaqus/paper_reproduction/experiment10
WORK_DIR=$EXP_DIR/run

export ABAQUS_MESH_SIZE=1.0
export ABAQUS_NUM_CPUS=8
export ABAQUS_MAX_CYCLES=75
export ABAQUS_STRESS_LIMIT=800.0

# --- Environment check ---
which abaqus 2>/dev/null && echo "abaqus: $(abaqus information=release 2>&1 | head -1)" || echo "abaqus: NOT found"
which tosca 2>/dev/null && echo "tosca: found" || echo "tosca: NOT found (will try 'abaqus tosca')"
which Xvfb 2>/dev/null && echo "Xvfb: found" || echo "Xvfb: NOT found (visualization skipped)"

# --- Clean and run ---
rm -rf $WORK_DIR
mkdir -p $WORK_DIR
cd $WORK_DIR

# STEP 1: Build model + flatten + generate .par + run Tosca (all in one script)
abaqus cae noGUI=$EXP_DIR/scripts/exp10_optimize.py 2>&1
STEP1_EXIT=$?

# STEP 2: Visualization (optional, requires Xvfb for headless rendering)
if command -v Xvfb &>/dev/null; then
    XDISPLAY=:$(( RANDOM % 900 + 100 ))
    Xvfb $XDISPLAY -screen 0 1024x768x24 &
    XVFB_PID=$!
    sleep 2
    export DISPLAY=$XDISPLAY
    timeout 300 abaqus cae script=$EXP_DIR/scripts/exp10_visualize.py 2>&1
    kill $XVFB_PID 2>/dev/null
    unset DISPLAY
fi

# --- Results summary ---
echo "--- Optimization convergence ---"
if [ -f $WORK_DIR/exp10_tosca/optimization_report.csv ]; then
    head -7 $WORK_DIR/exp10_tosca/optimization_report.csv
    echo "..."
    tail -5 $WORK_DIR/exp10_tosca/optimization_report.csv
fi
```

Key SLURM considerations:
- `unset SLURM_GTIDS` is **mandatory** -- without it, Abaqus MPI hangs.
- `module load abaqus/2025` loads both Abaqus and Tosca.
- Use `Xvfb` for headless visualization (ODB screenshots).
- Environment variables (`ABAQUS_MESH_SIZE`, etc.) let the Python script read configuration without hardcoding.

## Pattern 4: Post-Optimization FEA Validation

Tosca deletes per-cycle ODB files. To visualize stress/displacement on the optimized design, run Abaqus FEA on the last-cycle `.inp`.

Source: `paper_reproduction/experiment10/scripts/exp10_optimize.py` (Phase 9)

```python
import os
import subprocess

tosca_dir = os.path.join(WORK_DIR, 'exp10_tosca')
save_inp_dir = os.path.join(tosca_dir, 'SAVE.inp')

# Find the last cycle directory (highest numbered)
last_cycle = None
if os.path.isdir(save_inp_dir):
    cycle_dirs = [d for d in os.listdir(save_inp_dir)
                  if d.isdigit() and os.path.isdir(os.path.join(save_inp_dir, d))]
    if cycle_dirs:
        last_cycle = max(cycle_dirs, key=int)

if last_cycle:
    cycle_dir = os.path.join(save_inp_dir, last_cycle)
    cycle_inp = os.path.join(cycle_dir, flat_name)       # e.g., Model_flat.inp
    dist_file = os.path.join(cycle_dir, 'tosca_distribution.inp')

    if os.path.exists(cycle_inp) and os.path.exists(dist_file):
        print("Last cycle: {} (dir: {})".format(last_cycle, cycle_dir))

        # Run Abaqus FEA in the cycle directory
        # (so *INCLUDE finds tosca_distribution.inp in same directory)
        fea_job = 'Optimized_FEA'
        fea_cmd = ['abaqus', 'job=' + fea_job,
                   'input=' + cycle_inp,
                   'cpus=' + str(NUM_CPUS), 'interactive']

        fea_proc = subprocess.Popen(fea_cmd, cwd=cycle_dir,
                                    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        fea_out, _ = fea_proc.communicate()
        fea_output = fea_out.decode('utf-8', errors='replace')
        print("FEA exit code: {}".format(fea_proc.returncode))

        # Check for ODB
        odb_path = os.path.join(cycle_dir, fea_job + '.odb')
        if os.path.exists(odb_path):
            print("ODB created: {} ({} bytes)".format(odb_path, os.path.getsize(odb_path)))
```

The last-cycle `.inp` includes `*INCLUDE, INPUT=tosca_distribution.inp` which contains per-element density values (SIMP penalties). The `cwd=cycle_dir` argument is critical so Abaqus can find this include file.

## Pattern 5: Extracting Optimization Convergence from Report CSV

After optimization completes, `optimization_report.csv` in the Tosca output directory contains per-cycle metrics.

```bash
# Quick convergence check from command line
echo "First 5 and last 5 iterations:"
head -7 JOBNAME/optimization_report.csv
echo "..."
tail -5 JOBNAME/optimization_report.csv
```

From Python (for plotting or analysis):

```python
import csv
import os

report_path = os.path.join(tosca_dir, 'optimization_report.csv')
if os.path.exists(report_path):
    with open(report_path, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        print("Columns: {}".format(header))
        for row in reader:
            print("Cycle {}: {}".format(row[0], row))
```

## Pattern 6: STL Export from Smoothing Results

The `.par` file should include a `SMOOTH` block to configure STL output:

```
SMOOTH
  ID_NAME                = ISO_SMOOTHING
  TASK                   = iso
  ISO_VALUE              = 0.51
  SELF_INTERSECTION_CHECK = runtime
  SMOOTH_CYCLES          = 10
  REDUCTION_RATE         = 60
  REDUCTION_ANGLE        = 5.0
  FORMAT                 = stl
END_
```

After optimization, find the STL:

```python
import glob as globmod

# STL files can be in the job directory or subdirectories
stl_files = (globmod.glob('*.stl') +
             globmod.glob('JOBNAME/*.stl') +
             globmod.glob('JOBNAME/*/*.stl'))
if stl_files:
    print("STL files: {}".format(stl_files))
    for stl in stl_files:
        print("  {}: {} bytes".format(stl, os.path.getsize(stl)))
```

If smoothing was not included in the original `.par`, run it separately:

```bash
ToscaStructure --job JOBNAME --smooth
```

## Pattern 7: Full Pipeline Script (Build + Flatten + Optimize)

The complete pipeline in a single Abaqus noGUI script:

```python
# Phase 1-6: Build model with CAE API (geometry, material, mesh, BCs, loads)
# ... (standard Abaqus scripting) ...

# Phase 7a: Write flat .inp (noPartsInputFile=ON avoids manual flattening)
mdb.models[model_name].setValues(noPartsInputFile=ON)
mdb.Job(name=job_name, model=model_name, numCpus=NUM_CPUS, numDomains=NUM_CPUS)
mdb.jobs[job_name].writeInput()

# Phase 7c: Generate .par file (write string to file)
par_content = """FEM_INPUT
  ID_NAME  = FEA_MODEL
  FILE     = {flat_inp}
END_
...
""".format(flat_inp=flat_name)
with open(par_file, 'w') as f:
    f.write(par_content)

# Phase 8: Run Tosca CLI
import subprocess
cmd = ['tosca', 'optimize', '-j', 'job_tosca',
       '-p', par_file, '-s', 'abaqus', '-scpus', str(NUM_CPUS)]
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
stdout, _ = proc.communicate()
print("Tosca exit code: {}".format(proc.returncode))

# Phase 9: Validation FEA on last-cycle .inp (Pattern 4)
# ... (validation code) ...
```

This entire script runs with `abaqus cae noGUI=script.py`. The CAE API handles model building, then subprocess calls handle the Tosca CLI execution.
