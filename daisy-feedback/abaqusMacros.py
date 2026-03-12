# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Macro1():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    import os
    os.chdir(
        r"/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken")
    openMdb(
        pathName='/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken/exp8c.cae')
    session.viewports['Viewport: 1'].setValues(displayedObject=None)
    p = mdb.models['Model-1'].parts['Block']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTask='TopOpt')
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    mdb.OptimizationProcess(name='Opt-Process-1', model='Model-1', task='TopOpt', 
        description='', prototypeJob='Opt-Process-1-Job', maxDesignCycle=20, 
        odbMergeFrequency=2, dataSaveFrequency=OPT_DATASAVE_SPECIFY_CYCLE, 
        saveInitial=False)
    mdb.optimizationProcesses['Opt-Process-1'].Job(name='Opt-Process-1-Job', 
        model='Model-1', atTime=None, waitMinutes=0, waitHours=0, 
        licenseType=DEFAULT, queue=None, memory=90, memoryUnits=PERCENTAGE, 
        getMemoryFromAnalysis=True, numCpus=1, numGPUs=0)
    mdb.optimizationProcesses['Opt-Process-1'].submit()
    mdb.CombineOptResults(
        optResultLocation='/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken/Opt-Process-1', 
        includeResultsFrom=LAST, optIter=LAST, models=ALL, steps=('LoadStep', 
        ), analysisFieldVariables=('S', 'U'))
    session.mdbData.summary()
    o6 = session.openOdb(
        name='/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o6)
    session.viewports['Viewport: 1'].makeCurrent()
    import caeXmlObjects.kernel.mainXML
    caeXmlObjects.kernel.mainXML.loadXMLRecords(
        fileName='/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb', 
        className='caeXmlObjects.displayGroups.dgXML.DGXML', silentMode=False, 
        outputType='ODB')
    caeXmlObjects.kernel.mainXML.loadXMLRecords(
        fileName='/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb', 
        className='caeXmlObjects.paths.pathXML.PathXML', silentMode=False, 
        outputType='ODB')
    caeXmlObjects.kernel.mainXML.loadXMLRecords(
        fileName='/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb', 
        className='caeXmlObjects.xyData.xyDataXML.XYDataXML', silentMode=False, 
        outputType='ODB')
    caeXmlObjects.kernel.mainXML.loadXMLRecords(
        fileName='/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb', 
        className='caeXmlObjects.viewCuts.viewCutXML.ViewCutXML', 
        silentMode=False, outputType='ODB')
    caeXmlObjects.kernel.mainXML.loadXMLRecords(
        fileName='/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb', 
        className='caeXmlObjects.freeBodies.fbXML.FBXML', silentMode=False, 
        outputType='ODB')
    caeXmlObjects.kernel.mainXML.loadXMLRecords(
        fileName='/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb', 
        className='caeXmlObjects.spectrum.spectrumXML.SpectrumXML', 
        silentMode=False, outputType='ODB')
    caeXmlObjects.kernel.mainXML.kernelCommand(
        fileName='/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb', 
        className='caeXmlObjects.viewerPlotOptions.odbDisplay.odbDisplayXML.OdbDisplayXML', 
        silentMode=False, recordName='ODB Display', outputType='ODB', isSave=0)
    caeXmlObjects.kernel.mainXML.kernelCommand(
        fileName='/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb', 
        className='caeXmlObjects.viewerPlotOptions.basicOptions.basicOptionsXML.BasicOptionsXML', 
        silentMode=False, recordName='Basic Options', outputType='ODB', 
        isSave=0)
    caeXmlObjects.kernel.mainXML.kernelCommand(
        fileName='/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb', 
        className='caeXmlObjects.customViews.customViewsXML.CustomViewsXML', 
        silentMode=False, recordName='Custom Views', outputType='ODB', 
        isSave=0)
    caeXmlObjects.kernel.mainXML.kernelCommand(
        fileName='/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb', 
        className='caeXmlObjects.views.ViewsXML.ViewsXML', silentMode=False, 
        recordName='Views', outputType='ODB', isSave=0)
    caeXmlObjects.kernel.mainXML.kernelCommand(
        fileName='/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb', 
        className='caeXmlObjects.viewerPlotOptions.commonOptions.commonOptionsXML.CommonOptionsXML', 
        silentMode=False, recordName='Common Options', outputType='ODB', 
        isSave=0)
    caeXmlObjects.kernel.mainXML.kernelCommand(
        fileName='/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb', 
        className='caeXmlObjects.viewerPlotOptions.contourOptions.contourOptionsXML.ContourOptionsXML', 
        silentMode=False, recordName='Contour Options', outputType='ODB', 
        isSave=0)
    caeXmlObjects.kernel.mainXML.kernelCommand(
        fileName='/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb', 
        className='caeXmlObjects.viewerPlotOptions.superimposeOptions.superimposeOptionsXML.SuperimposeOptionsXML', 
        silentMode=False, recordName='Superimpose Options', outputType='ODB', 
        isSave=0)
    caeXmlObjects.kernel.mainXML.kernelCommand(
        fileName='/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb', 
        className='caeXmlObjects.viewerPlotOptions.materialOrientationOptions.materialOrientationOptionsXML.MaterialOrientationOptionsXML', 
        silentMode=False, recordName='Material Orientation Options', 
        outputType='ODB', isSave=0)
    caeXmlObjects.kernel.mainXML.kernelCommand(
        fileName='/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb', 
        className='caeXmlObjects.viewerPlotOptions.plyStackPlotOptions.plyStackPlotOptionsXML.PlyStackPlotOptionsXML', 
        silentMode=False, recordName='Ply Stack Plot Options', 
        outputType='ODB', isSave=0)
    caeXmlObjects.kernel.mainXML.kernelCommand(
        fileName='/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb', 
        className='caeXmlObjects.viewerPlotOptions.symbolOptions.symbolOptionsXML.SymbolOptionsXML', 
        silentMode=False, recordName='Symbol Options', outputType='ODB', 
        isSave=0)
    caeXmlObjects.kernel.mainXML.kernelCommand(
        fileName='/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb', 
        className='caeXmlObjects.viewerPlotOptions.freeBodyOptions.freeBodyOptionsXML.FreeBodyOptionsXML', 
        silentMode=False, recordName='Free Body Options', outputType='ODB', 
        isSave=0)
    caeXmlObjects.kernel.mainXML.kernelCommand(
        fileName='/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb', 
        className='caeXmlObjects.viewerPlotOptions.viewCutOptions.viewCutOptionsXML.ViewCutOptionsXML', 
        silentMode=False, recordName='View Cut Options', outputType='ODB', 
        isSave=0)
    caeXmlObjects.kernel.mainXML.kernelCommand(
        fileName='/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb', 
        className='caeXmlObjects.viewerPlotOptions.xPlane.xPlaneXML.XPlaneXML', 
        silentMode=False, recordName='X Plane', outputType='ODB', isSave=0)
    caeXmlObjects.kernel.mainXML.kernelCommand(
        fileName='/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb', 
        className='caeXmlObjects.viewerPlotOptions.yPlane.yPlaneXML.YPlaneXML', 
        silentMode=False, recordName='Y Plane', outputType='ODB', isSave=0)
    caeXmlObjects.kernel.mainXML.kernelCommand(
        fileName='/uufs/chpc.utah.edu/common/home/u1282901/Documents/IOWarpDemos/jaimeTO_broken/Opt-Process-1/TOSCA_POST/Opt-Process-1-Job_post.odb', 
        className='caeXmlObjects.viewerPlotOptions.zPlane.zPlaneXML.ZPlaneXML', 
        silentMode=False, recordName='Z Plane', outputType='ODB', isSave=0)
    mdb.save()


