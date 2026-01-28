# Set wireframe display
from abaqus import *
from abaqusConstants import *

session.viewports['Viewport: 1'].assemblyDisplay.setValues(renderStyle=WIREFRAME)
session.viewports['Viewport: 1'].view.fitView()
