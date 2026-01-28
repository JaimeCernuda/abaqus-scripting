# Set viewport to wireframe view
from abaqus import *
from abaqusConstants import *

session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    renderStyle=WIREFRAME
)
