# -*- coding: utf-8 -*-
from abaqus import *
from abaqusConstants import *
from caeModules import *

# Set wireframe view
session.viewports['Viewport: 1'].setValues(displayedObject=
    mdb.models['Experiment4_TO_Specimen'].parts['TO_Specimen'])

# Set to wireframe
session.viewports['Viewport: 1'].partDisplay.setValues(renderStyle=WIREFRAME)

# Front view (XY plane)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.fitView()

