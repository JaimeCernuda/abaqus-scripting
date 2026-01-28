# Set view to front (looking down Z axis)
from abaqus import *
from abaqusConstants import *

session.viewports['Viewport: 1'].view.setValues(
    session.views['Front']
)
session.viewports['Viewport: 1'].view.fitView()
