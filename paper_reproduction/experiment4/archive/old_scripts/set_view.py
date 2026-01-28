# -*- coding: utf-8 -*-
from abaqus import *
from abaqusConstants import *
from caeModules import *

vp = session.viewports['Viewport: 1']
vp.partDisplay.setValues(renderStyle=WIREFRAME)
vp.view.setValues(session.views['Right'])
vp.view.fitView()
