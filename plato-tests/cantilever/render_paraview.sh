#!/bin/bash
#SBATCH --job-name=plato-render3d
#SBATCH --account=bekn-delta-gpu
#SBATCH --partition=gpuA40x4-interactive
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --gpus-per-node=1
#SBATCH --time=00:15:00
#SBATCH --mem=16g
#SBATCH --output=plato-render3d-%j.out
#SBATCH --error=plato-render3d-%j.err

WORKDIR=/projects/bekn/jcernuda/plato-tests/cantilever
cd $WORKDIR/run

echo "=== ParaView 3D Rendering (GPU/EGL) ==="
module load paraview/6.0.1-prebuilt

cat > /tmp/render_pv.py << 'PYEOF'
from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

result = ExodusIIReader(FileName=["result.exo"])
result.UpdatePipeline()

# Go to last timestep
anim = GetAnimationScene()
anim.GoToLast()

# The field is called "density" (found in previous run)
field_name = "density"

# ---- View 1: Density field (isometric) ----
view = GetActiveViewOrCreate('RenderView')
view.ViewSize = [1920, 1080]
view.Background = [1, 1, 1]

display = Show(result, view)
display.Representation = 'Surface'
ColorBy(display, ('POINTS', field_name))

ctf = GetColorTransferFunction(field_name)
ctf.RescaleTransferFunction(0, 1)
ctf.ApplyPreset('Cool to Warm', True)

bar = GetScalarBar(ctf, view)
bar.Title = 'Density'
bar.Visibility = 1

view.ResetCamera()
cam = view.GetActiveCamera()
cam.Elevation(15)
cam.Azimuth(25)
view.ResetCamera()

SaveScreenshot("density_3d.png", view, ImageResolution=[1920, 1080])
print("Saved: density_3d.png")

# ---- View 2: Thresholded shape (solid only) ----
Hide(result, view)
bar.Visibility = 0

thresh = Threshold(Input=result)
thresh.Scalars = ['POINTS', field_name]
thresh.LowerThreshold = 0.3
thresh.UpperThreshold = 1.0
thresh.UpdatePipeline()

disp2 = Show(thresh, view)
ColorBy(disp2, None)
disp2.AmbientColor = [0.6, 0.65, 0.8]
disp2.DiffuseColor = [0.6, 0.65, 0.8]

view.ResetCamera()
cam = view.GetActiveCamera()
cam.Elevation(15)
cam.Azimuth(25)
view.ResetCamera()

SaveScreenshot("shape_3d.png", view, ImageResolution=[1920, 1080])
print("Saved: shape_3d.png")

# ---- View 3: Side view ----
cam.SetPosition(50, 10, 200)
cam.SetFocalPoint(50, 10, 5)
cam.SetViewUp(0, 1, 0)
view.ResetCamera()

SaveScreenshot("shape_side_3d.png", view, ImageResolution=[1920, 1080])
print("Saved: shape_side_3d.png")

print("All renders complete.")
PYEOF

pvpython --force-offscreen-rendering /tmp/render_pv.py 2>&1

echo ""
echo "=== Images ==="
ls -la *.png 2>/dev/null
cp density_3d.png shape_3d.png shape_side_3d.png $WORKDIR/ 2>/dev/null
echo "=== Done ==="
