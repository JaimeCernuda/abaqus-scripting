#!/bin/bash
#PBS -A gpu_hack
#PBS -q gpu_hack
#PBS -l walltime=01:00:00
#PBS -l filesystems=home:flare
#PBS -N plato-in718
#PBS -j oe

# Plato IN718 fatigue specimen — multi-objective topology optimization on Aurora (CPU build)
# Submit examples:
#   qsub -l select=1 -v NODES=1 run-aurora.sh        # single-node baseline
#   qsub -l select=2:place=scatter -v NODES=2 run-aurora.sh   # 2-node scaling
#   qsub -l select=4:place=scatter -v NODES=4 run-aurora.sh   # 4-node scaling

set -uo pipefail
WORKDIR=/home/jcernuda/plato-runs/in718-specimen
NODES=${NODES:-1}
RUNDIR="$WORKDIR/run-N${NODES}"
LOG="$WORKDIR/run-N${NODES}.log"
exec > "$LOG" 2>&1

echo "=========================================="
echo "  IN718 SPECIMEN — TOPOLOGY OPTIMIZATION"
echo "  Multi-objective (3 load cases), $NODES node(s)"
echo "  Started: $(date)"
echo "  Host(s):"; cat $PBS_NODEFILE 2>/dev/null | sort -u
echo "=========================================="

cd "$WORKDIR"

# === Step 1: Mesh generation ===
echo ""
echo "=== Step 1: Mesh Generation ==="
unset PYTHONPATH
source /usr/share/lmod/lmod/init/bash 2>/dev/null
module load python/3.12.12
rm -rf "$RUNDIR" && mkdir -p "$RUNDIR" && cd "$RUNDIR"
time python "$WORKDIR/generate_mesh.py"
cp "$WORKDIR"/{analyze_lc1.xml,analyze_lc2.xml,analyze_lc3.xml,analyze_volume.xml,input.i} .
ls -la mesh.exo
[ -f mesh.exo ] || { echo "ERROR: mesh.exo missing"; exit 1; }

# === Step 2: Activate Plato ===
echo ""
echo "=== Step 2: Load Plato (CPU+OpenMP build) ==="
module unload python/3.12.12 || true
module load oneapi/release/2025.3.1 mpich/opt/5.0.0.aurora_test.3c70a61 libfabric/1.22.0 cmake
source /home/jcernuda/plato/spack/share/spack/setup-env.sh
spack env activate /home/jcernuda/plato
spack load platoanalyze platoengine

# OMP threading — 3 ranks, distribute remaining cores per node to OMP
TOTAL_CORES=$(nproc)
RANKS=3                                # 1 per load case
PER_NODE=$(( (RANKS + NODES - 1) / NODES ))
export OMP_NUM_THREADS=$(( TOTAL_CORES / PER_NODE ))
export OMP_PROC_BIND=spread
export OMP_PLACES=threads
echo "ranks=$RANKS  nodes=$NODES  ranks/node=$PER_NODE  OMP_NUM_THREADS=$OMP_NUM_THREADS"
echo "plato: $(which plato)"

# === Step 3: Run optimization ===
echo ""
echo "=== Step 3: Multi-objective Topology Optimization (3 load cases × 50 iter) ==="
SECONDS=0
mpiexec -n $RANKS -ppn $PER_NODE plato input.i 2>&1
OPT_RC=$?
ELAPSED=$SECONDS
echo "plato exit: $OPT_RC"
echo "elapsed: ${ELAPSED}s ($((ELAPSED/60))m$((ELAPSED%60))s)"
ls -la *.exo 2>/dev/null

# === Step 4: Extract results ===
echo ""
echo "=== Step 4: Results Extraction ==="
unset PYTHONPATH
module load python/3.12.12
python "$WORKDIR/extract_results.py" 2>&1 | head -60 || echo "extract failed"

# === Step 5: ParaView render ===
echo ""
echo "=== Step 5: ParaView 3D Render ==="
module unload python/3.12.12 || true
module use /soft/modulefiles
module load paraview/paraview-6.0.0

cat > "$RUNDIR/render_pv.py" << 'PYEOF'
from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()
import sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

result = ExodusIIReader(FileName=["result.exo"])
result.UpdatePipeline()
GetAnimationScene().GoToLast()
field = "density"

view = GetActiveViewOrCreate('RenderView')
view.ViewSize = [1920, 1080]
view.Background = [1, 1, 1]

# Render 1: density field (full geometry)
disp = Show(result, view)
disp.Representation = 'Surface'
ColorBy(disp, ('POINTS', field))
ctf = GetColorTransferFunction(field); ctf.RescaleTransferFunction(0, 1)
ctf.ApplyPreset('Cool to Warm', True)
bar = GetScalarBar(ctf, view); bar.Title = 'Density'; bar.Visibility = 1
view.ResetCamera()
cam = view.GetActiveCamera(); cam.Elevation(15); cam.Azimuth(25); view.ResetCamera()
SaveScreenshot("in718_density_3d.png", view, ImageResolution=[1920, 1080])
print("Saved: in718_density_3d.png")

# Render 2: thresholded shape (density > 0.3)
Hide(result, view); bar.Visibility = 0
thresh = Threshold(Input=result)
thresh.Scalars = ['POINTS', field]
thresh.LowerThreshold = 0.3; thresh.UpperThreshold = 1.0
thresh.UpdatePipeline()
disp2 = Show(thresh, view); ColorBy(disp2, None)
disp2.AmbientColor = [0.65, 0.7, 0.85]; disp2.DiffuseColor = [0.65, 0.7, 0.85]
view.ResetCamera()
cam = view.GetActiveCamera(); cam.Elevation(15); cam.Azimuth(25); view.ResetCamera()
SaveScreenshot("in718_shape_iso.png", view, ImageResolution=[1920, 1080])
print("Saved: in718_shape_iso.png")

# Render 3: front view of thresholded shape
cam.SetPosition(0, 70, 400); cam.SetFocalPoint(0, 70, 12.5); cam.SetViewUp(0, 1, 0)
view.ResetCamera()
SaveScreenshot("in718_shape_front.png", view, ImageResolution=[1920, 1080])
print("Saved: in718_shape_front.png")

# Render 4: midplane density slice
Hide(thresh, view)
slc = Slice(Input=result); slc.SliceType = 'Plane'
slc.SliceType.Origin = [0, 70, 12.5]; slc.SliceType.Normal = [0, 0, 1]
slcDisp = Show(slc, view); ColorBy(slcDisp, ('POINTS', field))
ctf = GetColorTransferFunction(field); ctf.RescaleTransferFunction(0, 1)
bar = GetScalarBar(ctf, view); bar.Title = 'Density'; bar.Visibility = 1
view.ResetCamera()
cam = view.GetActiveCamera(); cam.SetPosition(0, 70, 400); cam.SetFocalPoint(0, 70, 0)
view.ResetCamera()
SaveScreenshot("in718_midclip.png", view, ImageResolution=[1920, 1080])
print("Saved: in718_midclip.png")
print("ParaView renders complete.")
PYEOF

pvbatch --force-offscreen-rendering "$RUNDIR/render_pv.py" 2>&1 || echo "pvbatch failed"
ls -la *.png 2>/dev/null

# === Wrap up ===
echo ""
echo "=========================================="
echo "  COMPLETE at $(date)"
echo "  Plato exit: $OPT_RC"
echo "  Optimization wall time: ${ELAPSED}s"
echo "  Nodes: $NODES, Ranks: $RANKS"
echo "=========================================="
