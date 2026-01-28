# -*- coding: utf-8 -*-
"""
Export images from multiple views to definitively verify hole orientations.
Run with: abaqus cae noGUI=export_views.py
"""
import os
from abaqus import *
from abaqusConstants import *
from caeModules import *

os.chdir(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4')
openMdb(r'D:/Libraries/Documents/projects/Abaqus/paper_reproduction/experiment4/Experiment4_TO_Specimen_v19.cae')

model = mdb.models['Experiment4_TO_Specimen']
part = model.parts['TO_Specimen']

# Create a new viewport for image export
vp = session.viewports['Viewport: 1']
vp.setValues(displayedObject=part)
vp.partDisplay.setValues(renderStyle=WIREFRAME)

# Function to export view
def export_view(view_name, filename):
    vp.view.setValues(session.views[view_name])
    vp.view.fitView()
    session.printToFile(
        fileName='screenshots/{}'.format(filename),
        format=PNG,
        canvasObjects=(vp,)
    )
    print("Exported: {}".format(filename))

# Export multiple views
print("Exporting views...")

# Front view - looking down Z axis (X horizontal, Y vertical)
# X-direction holes will appear as rectangles
# Z-direction holes will appear as circles
export_view('Front', 'view_front.png')

# Left view - looking down X axis (Z horizontal, Y vertical)
# X-direction holes will appear as circles (looking down the hole axis)
# Z-direction holes will appear as rectangles
export_view('Left', 'view_left.png')

# Top view - looking down Y axis
export_view('Top', 'view_top.png')

# Isometric
export_view('Iso', 'view_iso.png')

print("")
print("=" * 60)
print("HOW TO INTERPRET THESE IMAGES:")
print("=" * 60)
print("")
print("view_front.png (Front view, looking down Z):")
print("  - X-direction holes appear as RECTANGLES")
print("  - Z-direction holes appear as CIRCLES")
print("")
print("view_left.png (Left view, looking down X):")
print("  - X-direction holes appear as CIRCLES")
print("  - Z-direction holes appear as RECTANGLES")
print("")
print("For CORRECT geometry (X-direction holes):")
print("  - Front view: holes are rectangles (slots)")
print("  - Left view: holes are circles")
print("=" * 60)

mdb.close()
