# Abaqus LOAD Module API Reference

> Source: [https://hailin.wang/abqpy/en/2025/reference/mdb/model/load.html](https://hailin.wang/abqpy/en/2025/reference/mdb/model/load.html)
> Downloaded for offline use by Claude Code skills.

---

# Load[¶](#load "Permalink to this heading")

A specific type of load object and a specific type of load state object are designed for each type of load. A load object stores the nonpropagating data of a load as well as a number of instances of the corresponding load state object, each of which stores the propagating data of the load in a single step. Instances of the load state object are created and deleted internally by its corresponding load object.

Load Case commands are used for configuring load cases in specific types of steps that may use them.

## Load[¶](#id1 "Permalink to this heading")

The Load object is the abstract base type for other Load objects. The Load object has no explicit constructor. The methods and members of the Load object are common to all objects derived from Load.

### Create loads[¶](#create-loads "Permalink to this heading")

*class* LoadModel(*[name](#abaqus.Load.LoadModel.LoadModel "abaqus.Load.LoadModel.LoadModel.__init__.name (Python parameter)")*, *[description](#abaqus.Load.LoadModel.LoadModel "abaqus.Load.LoadModel.LoadModel.__init__.description (Python parameter)")=`''`*, *[stefanBoltzmann](#abaqus.Load.LoadModel.LoadModel "abaqus.Load.LoadModel.LoadModel.__init__.stefanBoltzmann (Python parameter)")=`None`*, *[absoluteZero](#abaqus.Load.LoadModel.LoadModel "abaqus.Load.LoadModel.LoadModel.__init__.absoluteZero (Python parameter)")=`None`*, *[waveFormulation](#abaqus.Load.LoadModel.LoadModel "abaqus.Load.LoadModel.LoadModel.__init__.waveFormulation (Python parameter)")=`abaqusConstants.NOT_SET`*, *[modelType](#abaqus.Load.LoadModel.LoadModel "abaqus.Load.LoadModel.LoadModel.__init__.modelType (Python parameter)")=`abaqusConstants.STANDARD_EXPLICIT`*, *[universalGas](#abaqus.Load.LoadModel.LoadModel "abaqus.Load.LoadModel.LoadModel.__init__.universalGas (Python parameter)")=`None`*, *[copyConstraints](#abaqus.Load.LoadModel.LoadModel "abaqus.Load.LoadModel.LoadModel.__init__.copyConstraints (Python parameter)")=`1`*, *[copyConnectors](#abaqus.Load.LoadModel.LoadModel "abaqus.Load.LoadModel.LoadModel.__init__.copyConnectors (Python parameter)")=`1`*, *[copyInteractions](#abaqus.Load.LoadModel.LoadModel "abaqus.Load.LoadModel.LoadModel.__init__.copyInteractions (Python parameter)")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L62-L2302)[¶](#abaqus.Load.LoadModel.LoadModel "Permalink to this definition")
:   Bases: [`ModelBase`](index.html#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase (Python class) — Bases: object")

    Abaqus creates a Model object named Model-1 when a session is started.

    Note

    This object can be accessed by:

    ```python
    mdb.models[name]
    ```

    Note

    Check [LoadModel on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?contextscope=all).

    Public Data Attributes:

    Inherited from [`ModelBase`](index.html#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | [`name`](index.html#abaqus.Model.ModelBase.ModelBase.name "abaqus.Model.ModelBase.ModelBase.name (Python attribute) — A String specifying the repository key.") | A String specifying the repository key. |
    | [`stefanBoltzmann`](index.html#abaqus.Model.ModelBase.ModelBase.stefanBoltzmann "abaqus.Model.ModelBase.ModelBase.stefanBoltzmann (Python attribute) — None or a Float specifying the Stefan-Boltzmann constant. The default value is None.") | None or a Float specifying the Stefan-Boltzmann constant. |
    | [`absoluteZero`](index.html#abaqus.Model.ModelBase.ModelBase.absoluteZero "abaqus.Model.ModelBase.ModelBase.absoluteZero (Python attribute) — None or a Float specifying the absolute zero constant. The default value is None.") | None or a Float specifying the absolute zero constant. |
    | [`waveFormulation`](index.html#abaqus.Model.ModelBase.ModelBase.waveFormulation "abaqus.Model.ModelBase.ModelBase.waveFormulation (Python attribute) — A SymbolicConstant specifying the type of incident wave formulation to be used in acoustic problems. Possible values are NOT_SET, SCATTERED, and TOTAL. The default value is NOT_SET.") | A SymbolicConstant specifying the type of incident wave formulation to be used in acoustic problems. |
    | [`universalGas`](index.html#abaqus.Model.ModelBase.ModelBase.universalGas "abaqus.Model.ModelBase.ModelBase.universalGas (Python attribute) — None or a Float specifying the universal gas constant. The default value is None.") | None or a Float specifying the universal gas constant. |
    | [`noPartsInputFile`](index.html#abaqus.Model.ModelBase.ModelBase.noPartsInputFile "abaqus.Model.ModelBase.ModelBase.noPartsInputFile (Python attribute) — A Boolean specifying whether an input file should be written without parts and assemblies. The default value is OFF.") | A Boolean specifying whether an input file should be written without parts and assemblies. |
    | [`endRestartStep`](index.html#abaqus.Model.ModelBase.ModelBase.endRestartStep "abaqus.Model.ModelBase.ModelBase.endRestartStep (Python attribute) — A Boolean specifying that the step specified by restartStep should be terminated at the increment specified by restartIncrement.") | A Boolean specifying that the step specified by **restartStep** should be terminated at the increment specified by **restartIncrement**. |
    | [`shellToSolid`](index.html#abaqus.Model.ModelBase.ModelBase.shellToSolid "abaqus.Model.ModelBase.ModelBase.shellToSolid (Python attribute) — A Boolean specifying that a shell global model drives a solid submodel.") | A Boolean specifying that a shell global model drives a solid submodel. |
    | [`lastChangedCount`](index.html#abaqus.Model.ModelBase.ModelBase.lastChangedCount "abaqus.Model.ModelBase.ModelBase.lastChangedCount (Python attribute) — A Float specifying the time stamp that indicates when the model was last changed.") | A Float specifying the time stamp that indicates when the model was last changed. |
    | [`description`](index.html#abaqus.Model.ModelBase.ModelBase.description "abaqus.Model.ModelBase.ModelBase.description (Python attribute) — A String specifying the purpose and contents of the Model object. The default value is an empty string.") | A String specifying the purpose and contents of the Model object. |
    | [`restartJob`](index.html#abaqus.Model.ModelBase.ModelBase.restartJob "abaqus.Model.ModelBase.ModelBase.restartJob (Python attribute) — A String specifying the name of the job that generated the restart data.") | A String specifying the name of the job that generated the restart data. |
    | [`restartStep`](index.html#abaqus.Model.ModelBase.ModelBase.restartStep "abaqus.Model.ModelBase.ModelBase.restartStep (Python attribute) — A String specifying the name of the step where the restart analysis will start.") | A String specifying the name of the step where the restart analysis will start. |
    | [`globalJob`](index.html#abaqus.Model.ModelBase.ModelBase.globalJob "abaqus.Model.ModelBase.ModelBase.globalJob (Python attribute) — A String specifying the name of the job that generated the results for the global model.") | A String specifying the name of the job that generated the results for the global model. |
    | [`copyConstraints`](index.html#abaqus.Model.ModelBase.ModelBase.copyConstraints "abaqus.Model.ModelBase.ModelBase.copyConstraints (Python attribute) — A boolean specifying the status of constraints created in a model, in the model which instances this model.") | A boolean specifying the status of constraints created in a model, in the model which instances this model. |
    | [`copyConnectors`](index.html#abaqus.Model.ModelBase.ModelBase.copyConnectors "abaqus.Model.ModelBase.ModelBase.copyConnectors (Python attribute) — A boolean specifying the status of connectors created in a model, in the model which instances this model.") | A boolean specifying the status of connectors created in a model, in the model which instances this model. |
    | [`copyInteractions`](index.html#abaqus.Model.ModelBase.ModelBase.copyInteractions "abaqus.Model.ModelBase.ModelBase.copyInteractions (Python attribute) — A boolean specifying the status of interactions created in a model, in the model which instances this model.") | A boolean specifying the status of interactions created in a model, in the model which instances this model. |
    | [`keywordBlock`](index.html#abaqus.Model.ModelBase.ModelBase.keywordBlock "abaqus.Model.ModelBase.ModelBase.keywordBlock (Python attribute) — A KeywordBlock object.") | A KeywordBlock object. |
    | [`amplitudes`](index.html#abaqus.Model.ModelBase.ModelBase.amplitudes "abaqus.Model.ModelBase.ModelBase.amplitudes (Python attribute) — A repository of Amplitude objects.") | A repository of Amplitude objects. |
    | [`profiles`](index.html#abaqus.Model.ModelBase.ModelBase.profiles "abaqus.Model.ModelBase.ModelBase.profiles (Python attribute) — A repository of Profile objects.") | A repository of Profile objects. |
    | [`boundaryConditions`](index.html#abaqus.Model.ModelBase.ModelBase.boundaryConditions "abaqus.Model.ModelBase.ModelBase.boundaryConditions (Python attribute) — A repository of BoundaryCondition objects.") | A repository of BoundaryCondition objects. |
    | [`constraints`](index.html#abaqus.Model.ModelBase.ModelBase.constraints "abaqus.Model.ModelBase.ModelBase.constraints (Python attribute) — A repository of ConstrainedSketchConstraint objects.") | A repository of ConstrainedSketchConstraint objects. |
    | [`analyticalFields`](index.html#abaqus.Model.ModelBase.ModelBase.analyticalFields "abaqus.Model.ModelBase.ModelBase.analyticalFields (Python attribute) — A repository of AnalyticalField objects.") | A repository of AnalyticalField objects. |
    | [`discreteFields`](index.html#abaqus.Model.ModelBase.ModelBase.discreteFields "abaqus.Model.ModelBase.ModelBase.discreteFields (Python attribute) — A repository of DiscreteField objects.") | A repository of DiscreteField objects. |
    | [`predefinedFields`](index.html#abaqus.Model.ModelBase.ModelBase.predefinedFields "abaqus.Model.ModelBase.ModelBase.predefinedFields (Python attribute) — A repository of PredefinedField objects.") | A repository of PredefinedField objects. |
    | [`interactions`](index.html#abaqus.Model.ModelBase.ModelBase.interactions "abaqus.Model.ModelBase.ModelBase.interactions (Python attribute) — A repository of Interaction objects.") | A repository of Interaction objects. |
    | [`interactionProperties`](index.html#abaqus.Model.ModelBase.ModelBase.interactionProperties "abaqus.Model.ModelBase.ModelBase.interactionProperties (Python attribute) — A repository of InteractionProperty objects.") | A repository of InteractionProperty objects. |
    | [`contactControls`](index.html#abaqus.Model.ModelBase.ModelBase.contactControls "abaqus.Model.ModelBase.ModelBase.contactControls (Python attribute) — A repository of ContactControl objects.") | A repository of ContactControl objects. |
    | [`contactInitializations`](index.html#abaqus.Model.ModelBase.ModelBase.contactInitializations "abaqus.Model.ModelBase.ModelBase.contactInitializations (Python attribute) — A repository of ContactInitialization objects.") | A repository of ContactInitialization objects. |
    | [`contactStabilizations`](index.html#abaqus.Model.ModelBase.ModelBase.contactStabilizations "abaqus.Model.ModelBase.ModelBase.contactStabilizations (Python attribute) — A repository of ContactStabilization objects.") | A repository of ContactStabilization objects. |
    | [`linkedInstances`](index.html#abaqus.Model.ModelBase.ModelBase.linkedInstances "abaqus.Model.ModelBase.ModelBase.linkedInstances (Python attribute) — A tuple of tuples of Strings specifying the linked child PartInstance name in the current model to the corresponding parent PartInstance name in a different model.") | A tuple of tuples of Strings specifying the linked child PartInstance name in the current model to the corresponding parent PartInstance name in a different model. |
    | [`linkedParts`](index.html#abaqus.Model.ModelBase.ModelBase.linkedParts "abaqus.Model.ModelBase.ModelBase.linkedParts (Python attribute) — A tuple of tuples of Strings specifying the linked child Part name in the current model to the corresponding parent Part name in a different model.") | A tuple of tuples of Strings specifying the linked child Part name in the current model to the corresponding parent Part name in a different model. |
    | [`loads`](index.html#abaqus.Model.ModelBase.ModelBase.loads "abaqus.Model.ModelBase.ModelBase.loads (Python attribute) — A repository of Load objects.") | A repository of Load objects. |
    | [`materials`](index.html#abaqus.Model.ModelBase.ModelBase.materials "abaqus.Model.ModelBase.ModelBase.materials (Python attribute) — A repository of Material objects.") | A repository of Material objects. |
    | [`calibrations`](index.html#abaqus.Model.ModelBase.ModelBase.calibrations "abaqus.Model.ModelBase.ModelBase.calibrations (Python attribute) — A repository of Calibration objects.") | A repository of Calibration objects. |
    | [`sections`](index.html#abaqus.Model.ModelBase.ModelBase.sections "abaqus.Model.ModelBase.ModelBase.sections (Python attribute) — A repository of Section objects.") | A repository of Section objects. |
    | [`remeshingRules`](index.html#abaqus.Model.ModelBase.ModelBase.remeshingRules "abaqus.Model.ModelBase.ModelBase.remeshingRules (Python attribute) — A repository of RemeshingRule objects.") | A repository of RemeshingRule objects. |
    | [`sketches`](index.html#abaqus.Model.ModelBase.ModelBase.sketches "abaqus.Model.ModelBase.ModelBase.sketches (Python attribute) — A repository of ConstrainedSketch objects.") | A repository of ConstrainedSketch objects. |
    | [`parts`](index.html#abaqus.Model.ModelBase.ModelBase.parts "abaqus.Model.ModelBase.ModelBase.parts (Python attribute) — A repository of Part objects.") | A repository of Part objects. |
    | [`steps`](index.html#abaqus.Model.ModelBase.ModelBase.steps "abaqus.Model.ModelBase.ModelBase.steps (Python attribute) — A repository of Step objects.") | A repository of Step objects. |
    | [`featureOptions`](index.html#abaqus.Model.ModelBase.ModelBase.featureOptions "abaqus.Model.ModelBase.ModelBase.featureOptions (Python attribute) — A FeatureOptions object.") | A FeatureOptions object. |
    | [`adaptiveMeshConstraints`](index.html#abaqus.Model.ModelBase.ModelBase.adaptiveMeshConstraints "abaqus.Model.ModelBase.ModelBase.adaptiveMeshConstraints (Python attribute) — A repository of AdaptiveMeshConstraint objects.") | A repository of AdaptiveMeshConstraint objects. |
    | [`adaptiveMeshControls`](index.html#abaqus.Model.ModelBase.ModelBase.adaptiveMeshControls "abaqus.Model.ModelBase.ModelBase.adaptiveMeshControls (Python attribute) — A repository of AdaptiveMeshControl objects.") | A repository of AdaptiveMeshControl objects. |
    | [`timePoints`](index.html#abaqus.Model.ModelBase.ModelBase.timePoints "abaqus.Model.ModelBase.ModelBase.timePoints (Python attribute) — A repository of TimePoint objects.") | A repository of TimePoint objects. |
    | [`filters`](index.html#abaqus.Model.ModelBase.ModelBase.filters "abaqus.Model.ModelBase.ModelBase.filters (Python attribute) — A repository of Filter objects.") | A repository of Filter objects. |
    | [`integratedOutputSections`](index.html#abaqus.Model.ModelBase.ModelBase.integratedOutputSections "abaqus.Model.ModelBase.ModelBase.integratedOutputSections (Python attribute) — A repository of IntegratedOutputSection objects.") | A repository of IntegratedOutputSection objects. |
    | [`fieldOutputRequests`](index.html#abaqus.Model.ModelBase.ModelBase.fieldOutputRequests "abaqus.Model.ModelBase.ModelBase.fieldOutputRequests (Python attribute) — A repository of FieldOutputRequest objects.") | A repository of FieldOutputRequest objects. |
    | [`historyOutputRequests`](index.html#abaqus.Model.ModelBase.ModelBase.historyOutputRequests "abaqus.Model.ModelBase.ModelBase.historyOutputRequests (Python attribute) — A repository of HistoryOutputRequest objects.") | A repository of HistoryOutputRequest objects. |
    | [`optimizationTasks`](index.html#abaqus.Model.ModelBase.ModelBase.optimizationTasks "abaqus.Model.ModelBase.ModelBase.optimizationTasks (Python attribute) — A repository of OptimizationTask objects.") | A repository of OptimizationTask objects. |
    | [`tableCollections`](index.html#abaqus.Model.ModelBase.ModelBase.tableCollections "abaqus.Model.ModelBase.ModelBase.tableCollections (Python attribute) — A repository of TableCollection objects.") | A repository of TableCollection objects. |
    | [`eventSeriesTypes`](index.html#abaqus.Model.ModelBase.ModelBase.eventSeriesTypes "abaqus.Model.ModelBase.ModelBase.eventSeriesTypes (Python attribute) — A repository of EventSeriesType objects.") | A repository of EventSeriesType objects. |
    | [`eventSeriesDatas`](index.html#abaqus.Model.ModelBase.ModelBase.eventSeriesDatas "abaqus.Model.ModelBase.ModelBase.eventSeriesDatas (Python attribute) — A repository of EventSeriesData objects.") | A repository of EventSeriesData objects. |
    | [`restartIncrement`](index.html#abaqus.Model.ModelBase.ModelBase.restartIncrement "abaqus.Model.ModelBase.ModelBase.restartIncrement (Python attribute) — An Int specifying the increment, interval, iteration or cycle where the restart analysis will start. To select the end of the step use the SymbolicConstant STEP_END.") | An Int specifying the increment, interval, iteration or cycle where the restart analysis will start. |
    | [`rootAssembly`](index.html#abaqus.Model.ModelBase.ModelBase.rootAssembly "abaqus.Model.ModelBase.ModelBase.rootAssembly (Python attribute) — An Assembly object.") | An Assembly object. |

    Public Methods:

    |  |  |
    | --- | --- |
    | [`BodyCharge`](#abaqus.Load.LoadModel.LoadModel.BodyCharge "abaqus.Load.LoadModel.LoadModel.BodyCharge (Python method) — This method creates a BodyCharge object.")(name, createStepName, region, ...) | This method creates a BodyCharge object. |
    | [`BodyConcentrationFlux`](#abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux "abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux (Python method) — This method creates a BodyConcentrationFlux object.")(name, createStepName, ...) | This method creates a BodyConcentrationFlux object. |
    | [`BodyCurrent`](#abaqus.Load.LoadModel.LoadModel.BodyCurrent "abaqus.Load.LoadModel.LoadModel.BodyCurrent (Python method) — This method creates a BodyCurrent object.")(name, createStepName, region, ...) | This method creates a BodyCurrent object. |
    | [`BodyCurrentDensity`](#abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity "abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity (Python method) — This method creates a BodyCurrentDensity object.")(name, createStepName, ...) | This method creates a BodyCurrentDensity object. |
    | [`BodyForce`](#abaqus.Load.LoadModel.LoadModel.BodyForce "abaqus.Load.LoadModel.LoadModel.BodyForce (Python method) — This method creates a BodyForce object.")(name, createStepName, region[, ...]) | This method creates a BodyForce object. |
    | [`BodyHeatFlux`](#abaqus.Load.LoadModel.LoadModel.BodyHeatFlux "abaqus.Load.LoadModel.LoadModel.BodyHeatFlux (Python method) — This method creates a BodyHeatFlux object.")(name, createStepName, region, ...) | This method creates a BodyHeatFlux object. |
    | [`BoltLoad`](#abaqus.Load.LoadModel.LoadModel.BoltLoad "abaqus.Load.LoadModel.LoadModel.BoltLoad (Python method) — This method creates a BoltLoad object.")(name, createStepName, region, ...) | This method creates a BoltLoad object. |
    | [`ConcCharge`](#abaqus.Load.LoadModel.LoadModel.ConcCharge "abaqus.Load.LoadModel.LoadModel.ConcCharge (Python method) — This method creates a ConcCharge object.")(name, createStepName, region, ...) | This method creates a ConcCharge object. |
    | [`ConcConcFlux`](#abaqus.Load.LoadModel.LoadModel.ConcConcFlux "abaqus.Load.LoadModel.LoadModel.ConcConcFlux (Python method) — This method creates a ConcConcFlux object.")(name, createStepName, region, ...) | This method creates a ConcConcFlux object. |
    | [`ConcCurrent`](#abaqus.Load.LoadModel.LoadModel.ConcCurrent "abaqus.Load.LoadModel.LoadModel.ConcCurrent (Python method) — This method creates a ConcCurrent object.")(name, createStepName, region, ...) | This method creates a ConcCurrent object. |
    | [`ConcentratedForce`](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce "abaqus.Load.LoadModel.LoadModel.ConcentratedForce (Python method) — This method creates a ConcentratedForce object.")(name, createStepName, region) | This method creates a ConcentratedForce object. |
    | [`ConcentratedHeatFlux`](#abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux "abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux (Python method) — This method creates a ConcentratedHeatFlux object.")(name, createStepName, ...) | This method creates a ConcentratedHeatFlux object. |
    | [`ConcPoreFluid`](#abaqus.Load.LoadModel.LoadModel.ConcPoreFluid "abaqus.Load.LoadModel.LoadModel.ConcPoreFluid (Python method) — This method creates a ConcPoreFluid object.")(name, createStepName, region, ...) | This method creates a ConcPoreFluid object. |
    | [`ConnectorForce`](#abaqus.Load.LoadModel.LoadModel.ConnectorForce "abaqus.Load.LoadModel.LoadModel.ConnectorForce (Python method) — This method creates a ConnectorForce object on a wire region. Alternatively, the load may also be applied to a wire set referenced from an assembled fastener template model.")(name, createStepName[, ...]) | This method creates a ConnectorForce object on a wire region. |
    | [`ConnectorMoment`](#abaqus.Load.LoadModel.LoadModel.ConnectorMoment "abaqus.Load.LoadModel.LoadModel.ConnectorMoment (Python method) — This method creates a ConnectorMoment object on a wire region. Alternatively, the load may also be applied to a wire set referenced from an assembled fastener template model.")(name, createStepName[, ...]) | This method creates a ConnectorMoment object on a wire region. |
    | [`CoriolisForce`](#abaqus.Load.LoadModel.LoadModel.CoriolisForce "abaqus.Load.LoadModel.LoadModel.CoriolisForce (Python method) — This method creates a CoriolisForce object.")(name, createStepName, region, ...) | This method creates a CoriolisForce object. |
    | [`Gravity`](#abaqus.Load.LoadModel.LoadModel.Gravity "abaqus.Load.LoadModel.LoadModel.Gravity (Python method) — This method creates a Gravity object.")(name, createStepName[, ...]) | This method creates a Gravity object. |
    | [`InertiaRelief`](#abaqus.Load.LoadModel.LoadModel.InertiaRelief "abaqus.Load.LoadModel.LoadModel.InertiaRelief (Python method) — This method creates an InertiaRelief object.")(name, createStepName[, u1, ...]) | This method creates an InertiaRelief object. |
    | [`InwardVolAccel`](#abaqus.Load.LoadModel.LoadModel.InwardVolAccel "abaqus.Load.LoadModel.LoadModel.InwardVolAccel (Python method) — This method creates a InwardVolAccel object.")(name, createStepName, region, ...) | This method creates a InwardVolAccel object. |
    | [`LineLoad`](#abaqus.Load.LoadModel.LoadModel.LineLoad "abaqus.Load.LoadModel.LoadModel.LineLoad (Python method) — This method creates a LineLoad object.")(name, createStepName, region[, ...]) | This method creates a LineLoad object. |
    | [`Moment`](#abaqus.Load.LoadModel.LoadModel.Moment "abaqus.Load.LoadModel.LoadModel.Moment (Python method) — This method creates a Moment object.")(name, createStepName, region[, cm1, ...]) | This method creates a Moment object. |
    | [`PEGLoad`](#abaqus.Load.LoadModel.LoadModel.PEGLoad "abaqus.Load.LoadModel.LoadModel.PEGLoad (Python method) — This method creates a PEGLoad object.")(name, createStepName, region[, ...]) | This method creates a PEGLoad object. |
    | [`PipePressure`](#abaqus.Load.LoadModel.LoadModel.PipePressure "abaqus.Load.LoadModel.LoadModel.PipePressure (Python method) — This method creates a Pressure object.")(name, createStepName, region, ...) | This method creates a Pressure object. |
    | [`Pressure`](#abaqus.Load.LoadModel.LoadModel.Pressure "abaqus.Load.LoadModel.LoadModel.Pressure (Python method) — This method creates a Pressure object.")(name, createStepName, region[, ...]) | This method creates a Pressure object. |
    | [`RotationalBodyForce`](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce "abaqus.Load.LoadModel.LoadModel.RotationalBodyForce (Python method) — This method creates a RotationalBodyForce object.")(name, createStepName, ...) | This method creates a RotationalBodyForce object. |
    | [`ShellEdgeLoad`](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad "abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad (Python method) — This method creates a ShellEdgeLoad object.")(name, createStepName, region, ...) | This method creates a ShellEdgeLoad object. |
    | [`SubmodelSB`](#abaqus.Load.LoadModel.LoadModel.SubmodelSB "abaqus.Load.LoadModel.LoadModel.SubmodelSB (Python method) — This method creates a SubmodelSB object.")(name, createStepName, region, ...) | This method creates a SubmodelSB object. |
    | [`SubstructureLoad`](#abaqus.Load.LoadModel.LoadModel.SubstructureLoad "abaqus.Load.LoadModel.LoadModel.SubstructureLoad (Python method) — This method creates a SubstructureLoad object.")(name, createStepName, ...) | This method creates a SubstructureLoad object. |
    | [`SurfaceCharge`](#abaqus.Load.LoadModel.LoadModel.SurfaceCharge "abaqus.Load.LoadModel.LoadModel.SurfaceCharge (Python method) — This method creates a SurfaceCharge object.")(name, createStepName, region, ...) | This method creates a SurfaceCharge object. |
    | [`SurfaceConcentrationFlux`](#abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux "abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux (Python method) — This method creates a SurfaceConcentrationFlux object.")(name, ...[, field, ...]) | This method creates a SurfaceConcentrationFlux object. |
    | [`SurfaceCurrent`](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrent "abaqus.Load.LoadModel.LoadModel.SurfaceCurrent (Python method) — This method creates a SurfaceCurrent object.")(name, createStepName, region, ...) | This method creates a SurfaceCurrent object. |
    | [`SurfaceCurrentDensity`](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity "abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity (Python method) — This method creates a SurfaceCurrentDensity object.")(name, createStepName, ...) | This method creates a SurfaceCurrentDensity object. |
    | [`SurfaceHeatFlux`](#abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux "abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux (Python method) — This method creates a SurfaceHeatFlux object.")(name, createStepName, ...[, ...]) | This method creates a SurfaceHeatFlux object. |
    | [`SurfacePoreFluid`](#abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid "abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid (Python method) — This method creates a SurfacePoreFluid object.")(name, createStepName, ...) | This method creates a SurfacePoreFluid object. |
    | [`SurfaceTraction`](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction "abaqus.Load.LoadModel.LoadModel.SurfaceTraction (Python method) — This method creates a SurfaceTraction object.")(name, createStepName, ...[, ...]) | This method creates a SurfaceTraction object. |

    Inherited from [`ModelBase`](index.html#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | `__init__`(name[, description, ...]) | This method creates a Model object. |
    | [`setValues`](index.html#abaqus.Model.ModelBase.ModelBase.setValues "abaqus.Model.ModelBase.ModelBase.setValues (Python method) — This method modifies the Model object.")([description, noPartsInputFile, ...]) | This method modifies the Model object. |

    ---

    Member Details:

    BodyCharge(*[name](#abaqus.Load.LoadModel.LoadModel.BodyCharge.name "abaqus.Load.LoadModel.LoadModel.BodyCharge.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.BodyCharge.createStepName "abaqus.Load.LoadModel.LoadModel.BodyCharge.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.BodyCharge.region "abaqus.Load.LoadModel.LoadModel.BodyCharge.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[magnitude](#abaqus.Load.LoadModel.LoadModel.BodyCharge.magnitude "abaqus.Load.LoadModel.LoadModel.BodyCharge.magnitude (Python parameter) — A Float specifying the load magnitude.")*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.BodyCharge.amplitude "abaqus.Load.LoadModel.LoadModel.BodyCharge.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.BodyCharge.distributionType "abaqus.Load.LoadModel.LoadModel.BodyCharge.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.LoadModel.BodyCharge.field "abaqus.Load.LoadModel.LoadModel.BodyCharge.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L72-L121)[¶](#abaqus.Load.LoadModel.LoadModel.BodyCharge "Permalink to this definition")
    :   This method creates a BodyCharge object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].BodyCharge
        ```

        Note

        Check [BodyCharge on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodychargepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.BodyCharge-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.BodyCharge.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.BodyCharge.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created. This must be the
                first analysis step name.

            region[¶](#abaqus.Load.LoadModel.LoadModel.BodyCharge.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            magnitude[¶](#abaqus.Load.LoadModel.LoadModel.BodyCharge.magnitude "Permalink to this definition")
            :   A Float specifying the load magnitude.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.BodyCharge.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.BodyCharge.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.BodyCharge.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.BodyCharge-returns "Permalink to this headline")
        :   A BodyCharge object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.BodyCharge-return-type "Permalink to this headline")
        :   [`BodyCharge`](#abaqus.Load.LoadModel.BodyCharge "abaqus.Load.LoadModel.BodyCharge (Python class) — Bases: Load")

    BodyConcentrationFlux(*[name](#abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux.name "abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux.createStepName "abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux.region "abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[magnitude](#abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux.magnitude "abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux.magnitude (Python parameter) — A Float specifying the body concentration flux magnitude.")*, *[field](#abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux.field "abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux.distributionType "abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux.distributionType (Python parameter) — A SymbolicConstant specifying how the body concentration flux is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD.")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux.amplitude "abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L123-L172)[¶](#abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux "Permalink to this definition")
    :   This method creates a BodyConcentrationFlux object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].BodyConcentrationFlux
        ```

        Note

        Check [BodyConcentrationFlux on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodyconcentrationfluxpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created.

            region[¶](#abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            magnitude[¶](#abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux.magnitude "Permalink to this definition")
            :   A Float specifying the body concentration flux magnitude. **magnitude** is optional if
                **distributionType** = USER\_DEFINED.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the body concentration flux is distributed spatially.
                Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux-returns "Permalink to this headline")
        :   A BodyConcentrationFlux object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux-return-type "Permalink to this headline")
        :   [`BodyConcentrationFlux`](#abaqus.Load.LoadModel.BodyConcentrationFlux "abaqus.Load.LoadModel.BodyConcentrationFlux (Python class) — Bases: Load")

    BodyCurrent(*[name](#abaqus.Load.LoadModel.LoadModel.BodyCurrent.name "abaqus.Load.LoadModel.LoadModel.BodyCurrent.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.BodyCurrent.createStepName "abaqus.Load.LoadModel.LoadModel.BodyCurrent.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.BodyCurrent.region "abaqus.Load.LoadModel.LoadModel.BodyCurrent.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[magnitude](#abaqus.Load.LoadModel.LoadModel.BodyCurrent.magnitude "abaqus.Load.LoadModel.LoadModel.BodyCurrent.magnitude (Python parameter) — A Float specifying the load magnitude.")*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.BodyCurrent.amplitude "abaqus.Load.LoadModel.LoadModel.BodyCurrent.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.BodyCurrent.distributionType "abaqus.Load.LoadModel.LoadModel.BodyCurrent.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.LoadModel.BodyCurrent.field "abaqus.Load.LoadModel.LoadModel.BodyCurrent.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L174-L223)[¶](#abaqus.Load.LoadModel.LoadModel.BodyCurrent "Permalink to this definition")
    :   This method creates a BodyCurrent object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].BodyCurrent
        ```

        Note

        Check [BodyCurrent on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodycurrentpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.BodyCurrent-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.BodyCurrent.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.BodyCurrent.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created. This must be the
                first analysis step name.

            region[¶](#abaqus.Load.LoadModel.LoadModel.BodyCurrent.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            magnitude[¶](#abaqus.Load.LoadModel.LoadModel.BodyCurrent.magnitude "Permalink to this definition")
            :   A Float specifying the load magnitude.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.BodyCurrent.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.BodyCurrent.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.BodyCurrent.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.BodyCurrent-returns "Permalink to this headline")
        :   A BodyCurrent object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.BodyCurrent-return-type "Permalink to this headline")
        :   [`BodyCurrent`](#abaqus.Load.LoadModel.BodyCurrent "abaqus.Load.LoadModel.BodyCurrent (Python class) — Bases: Load")

    BodyCurrentDensity(*[name](#abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity.name "abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity.createStepName "abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity.region "abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[comp1](#abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity.comp1 "abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity.comp1 (Python parameter) — A Complex specifying the first component of the load.")*, *[comp2](#abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity.comp2 "abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity.comp2 (Python parameter) — A Complex specifying the second component of the load.")*, *[comp3](#abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity.comp3 "abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity.comp3 (Python parameter) — A Complex specifying the third component of the load.")*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity.amplitude "abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity.distributionType "abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L225-L282)[¶](#abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity "Permalink to this definition")
    :   This method creates a BodyCurrentDensity object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].BodyCurrentDensity
        ```

        Note

        Check [BodyCurrentDensity on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodycurrentdensitypyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created. This must be the
                first analysis step name.

            region[¶](#abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            comp1[¶](#abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity.comp1 "Permalink to this definition")
            :   A Complex specifying the first component of the load.

            comp2[¶](#abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity.comp2 "Permalink to this definition")
            :   A Complex specifying the second component of the load.

            comp3[¶](#abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity.comp3 "Permalink to this definition")
            :   A Complex specifying the third component of the load.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and USER\_DEFINED. The default value is UNIFORM.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity-returns "Permalink to this headline")
        :   A BodyCurrentDensity object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity-return-type "Permalink to this headline")
        :   [`BodyCurrentDensity`](#abaqus.Load.LoadModel.BodyCurrentDensity "abaqus.Load.LoadModel.BodyCurrentDensity (Python class) — Bases: Load")

    BodyForce(*[name](#abaqus.Load.LoadModel.LoadModel.BodyForce.name "abaqus.Load.LoadModel.LoadModel.BodyForce.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.BodyForce.createStepName "abaqus.Load.LoadModel.LoadModel.BodyForce.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.BodyForce.region "abaqus.Load.LoadModel.LoadModel.BodyForce.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[field](#abaqus.Load.LoadModel.LoadModel.BodyForce.field "abaqus.Load.LoadModel.LoadModel.BodyForce.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.BodyForce.distributionType "abaqus.Load.LoadModel.LoadModel.BodyForce.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[comp1](#abaqus.Load.LoadModel.LoadModel.BodyForce.comp1 "abaqus.Load.LoadModel.LoadModel.BodyForce.comp1 (Python parameter) — A Float or a Complex specifying the body force component in the 1-direction.")=`None`*, *[comp2](#abaqus.Load.LoadModel.LoadModel.BodyForce.comp2 "abaqus.Load.LoadModel.LoadModel.BodyForce.comp2 (Python parameter) — A Float or a Complex specifying the body force component in the 2-direction.")=`None`*, *[comp3](#abaqus.Load.LoadModel.LoadModel.BodyForce.comp3 "abaqus.Load.LoadModel.LoadModel.BodyForce.comp3 (Python parameter) — A Float or a Complex specifying the body force component in the 3-direction.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.BodyForce.amplitude "abaqus.Load.LoadModel.LoadModel.BodyForce.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L284-L348)[¶](#abaqus.Load.LoadModel.LoadModel.BodyForce "Permalink to this definition")
    :   This method creates a BodyForce object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].BodyForce
        ```

        Note

        Check [BodyForce on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodyforcepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.BodyForce-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.BodyForce.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.BodyForce.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created.

            region[¶](#abaqus.Load.LoadModel.LoadModel.BodyForce.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.BodyForce.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.BodyForce.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            comp1=`None`[¶](#abaqus.Load.LoadModel.LoadModel.BodyForce.comp1 "Permalink to this definition")
            :   A Float or a Complex specifying the body force component in the
                1-direction. Note: Although **comp1**, **comp2**, and **comp3** are optional arguments, at least
                one of them must be nonzero unless **distributionType** = USER\_DEFINED.

            comp2=`None`[¶](#abaqus.Load.LoadModel.LoadModel.BodyForce.comp2 "Permalink to this definition")
            :   A Float or a Complex specifying the body force component in the 2-direction.

            comp3=`None`[¶](#abaqus.Load.LoadModel.LoadModel.BodyForce.comp3 "Permalink to this definition")
            :   A Float or a Complex specifying the body force component in the 3-direction.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.BodyForce.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.BodyForce-returns "Permalink to this headline")
        :   A BodyForce object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.BodyForce-return-type "Permalink to this headline")
        :   [`BodyForce`](#abaqus.Load.LoadModel.BodyForce "abaqus.Load.LoadModel.BodyForce (Python class) — Bases: Load")

    BodyHeatFlux(*[name](#abaqus.Load.LoadModel.LoadModel.BodyHeatFlux.name "abaqus.Load.LoadModel.LoadModel.BodyHeatFlux.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.BodyHeatFlux.createStepName "abaqus.Load.LoadModel.LoadModel.BodyHeatFlux.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.BodyHeatFlux.region "abaqus.Load.LoadModel.LoadModel.BodyHeatFlux.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[magnitude](#abaqus.Load.LoadModel.LoadModel.BodyHeatFlux.magnitude "abaqus.Load.LoadModel.LoadModel.BodyHeatFlux.magnitude (Python parameter) — A Float specifying the body heat flux magnitude.")*, *[field](#abaqus.Load.LoadModel.LoadModel.BodyHeatFlux.field "abaqus.Load.LoadModel.LoadModel.BodyHeatFlux.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.BodyHeatFlux.distributionType "abaqus.Load.LoadModel.LoadModel.BodyHeatFlux.distributionType (Python parameter) — A SymbolicConstant specifying how the body heat flux is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.BodyHeatFlux.amplitude "abaqus.Load.LoadModel.LoadModel.BodyHeatFlux.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L350-L399)[¶](#abaqus.Load.LoadModel.LoadModel.BodyHeatFlux "Permalink to this definition")
    :   This method creates a BodyHeatFlux object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].BodyHeatFlux
        ```

        Note

        Check [BodyHeatFlux on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodyheatfluxpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.BodyHeatFlux-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.BodyHeatFlux.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.BodyHeatFlux.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created.

            region[¶](#abaqus.Load.LoadModel.LoadModel.BodyHeatFlux.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            magnitude[¶](#abaqus.Load.LoadModel.LoadModel.BodyHeatFlux.magnitude "Permalink to this definition")
            :   A Float specifying the body heat flux magnitude. **magnitude** is optional if
                **distributionType** = USER\_DEFINED.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.BodyHeatFlux.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.BodyHeatFlux.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the body heat flux is distributed spatially. Possible
                values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.BodyHeatFlux.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.BodyHeatFlux-returns "Permalink to this headline")
        :   A BodyHeatFlux object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.BodyHeatFlux-return-type "Permalink to this headline")
        :   [`BodyHeatFlux`](#abaqus.Load.LoadModel.BodyHeatFlux "abaqus.Load.LoadModel.BodyHeatFlux (Python class) — Bases: Load")

    BoltLoad(*[name](#abaqus.Load.LoadModel.LoadModel.BoltLoad.name "abaqus.Load.LoadModel.LoadModel.BoltLoad.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.BoltLoad.createStepName "abaqus.Load.LoadModel.LoadModel.BoltLoad.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.BoltLoad.region "abaqus.Load.LoadModel.LoadModel.BoltLoad.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[magnitude](#abaqus.Load.LoadModel.LoadModel.BoltLoad.magnitude "abaqus.Load.LoadModel.LoadModel.BoltLoad.magnitude (Python parameter) — A Float specifying the bolt load magnitude.")*, *[datumAxis](#abaqus.Load.LoadModel.LoadModel.BoltLoad.datumAxis "abaqus.Load.LoadModel.LoadModel.BoltLoad.datumAxis (Python parameter) — A DatumAxis object specifying the orientation of the pre-tension section normal.")*, *[boltMethod](#abaqus.Load.LoadModel.LoadModel.BoltLoad.boltMethod "abaqus.Load.LoadModel.LoadModel.BoltLoad.boltMethod (Python parameter) — A SymbolicConstant specifying the method of applying the bolt load.")=`abaqusConstants.APPLY_FORCE`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.BoltLoad.amplitude "abaqus.Load.LoadModel.LoadModel.BoltLoad.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*, *[preTenSecPartLevel](#abaqus.Load.LoadModel.LoadModel.BoltLoad.preTenSecPartLevel "abaqus.Load.LoadModel.LoadModel.BoltLoad.preTenSecPartLevel (Python parameter) — A Boolean specifying whether the pre-tension section is to be defined at the part level. The default value is False.")=`False`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L401-L463)[¶](#abaqus.Load.LoadModel.LoadModel.BoltLoad "Permalink to this definition")
    :   This method creates a BoltLoad object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].BoltLoad
        ```

        Note

        Check [BoltLoad on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boltloadpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.BoltLoad-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.BoltLoad.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.BoltLoad.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created. This must be the
                first analysis step name.

            region[¶](#abaqus.Load.LoadModel.LoadModel.BoltLoad.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            magnitude[¶](#abaqus.Load.LoadModel.LoadModel.BoltLoad.magnitude "Permalink to this definition")
            :   A Float specifying the bolt load magnitude.

            datumAxis[¶](#abaqus.Load.LoadModel.LoadModel.BoltLoad.datumAxis "Permalink to this definition")
            :   A DatumAxis object specifying the orientation of the pre-tension section normal. Note:
                **datumAxis** is applicable only for Solid and Shell regions; it has no meaning for Wire
                regions.

            boltMethod=`abaqusConstants.APPLY_FORCE`[¶](#abaqus.Load.LoadModel.LoadModel.BoltLoad.boltMethod "Permalink to this definition")
            :   A SymbolicConstant specifying the method of applying the bolt load. Possible values are
                APPLY\_FORCE and ADJUST\_LENGTH. The default value is APPLY\_FORCE.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.BoltLoad.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

            preTenSecPartLevel=`False`[¶](#abaqus.Load.LoadModel.LoadModel.BoltLoad.preTenSecPartLevel "Permalink to this definition")
            :   A Boolean specifying whether the pre-tension section is to be defined at the part level.
                The default value is False. You should provide the **preTenSecPartLevel** argument only if
                the selected region belongs to a dependent part instance. A pre-tension section cannot
                be defined at the part level for independent and model instances.

                New in version 2018: The `preTenSecPartLevel` argument was added.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.BoltLoad-returns "Permalink to this headline")
        :   A BoltLoad object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.BoltLoad-return-type "Permalink to this headline")
        :   [`BoltLoad`](#abaqus.Load.LoadModel.BoltLoad "abaqus.Load.LoadModel.BoltLoad (Python class) — Bases: Load")

        Raises:[¶](#abaqus.Load.LoadModel.LoadModel.BoltLoad-raises "Permalink to this headline")
        :   **TextError** –

    ConcCharge(*[name](#abaqus.Load.LoadModel.LoadModel.ConcCharge.name "abaqus.Load.LoadModel.LoadModel.ConcCharge.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.ConcCharge.createStepName "abaqus.Load.LoadModel.LoadModel.ConcCharge.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.ConcCharge.region "abaqus.Load.LoadModel.LoadModel.ConcCharge.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[magnitude](#abaqus.Load.LoadModel.LoadModel.ConcCharge.magnitude "abaqus.Load.LoadModel.LoadModel.ConcCharge.magnitude (Python parameter) — A Float specifying the load magnitude.")*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.ConcCharge.distributionType "abaqus.Load.LoadModel.LoadModel.ConcCharge.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.LoadModel.ConcCharge.field "abaqus.Load.LoadModel.LoadModel.ConcCharge.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.ConcCharge.amplitude "abaqus.Load.LoadModel.LoadModel.ConcCharge.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L465-L514)[¶](#abaqus.Load.LoadModel.LoadModel.ConcCharge "Permalink to this definition")
    :   This method creates a ConcCharge object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ConcCharge
        ```

        Note

        Check [ConcCharge on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concchargepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.ConcCharge-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.ConcCharge.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.ConcCharge.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created. This must be the
                first analysis step name.

            region[¶](#abaqus.Load.LoadModel.LoadModel.ConcCharge.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            magnitude[¶](#abaqus.Load.LoadModel.LoadModel.ConcCharge.magnitude "Permalink to this definition")
            :   A Float specifying the load magnitude.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.ConcCharge.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.ConcCharge.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.ConcCharge.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.ConcCharge-returns "Permalink to this headline")
        :   A ConcCharge object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.ConcCharge-return-type "Permalink to this headline")
        :   [`ConcCharge`](#abaqus.Load.LoadModel.ConcCharge "abaqus.Load.LoadModel.ConcCharge (Python class) — Bases: Load")

    ConcConcFlux(*[name](#abaqus.Load.LoadModel.LoadModel.ConcConcFlux.name "abaqus.Load.LoadModel.LoadModel.ConcConcFlux.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.ConcConcFlux.createStepName "abaqus.Load.LoadModel.LoadModel.ConcConcFlux.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.ConcConcFlux.region "abaqus.Load.LoadModel.LoadModel.ConcConcFlux.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[magnitude](#abaqus.Load.LoadModel.LoadModel.ConcConcFlux.magnitude "abaqus.Load.LoadModel.LoadModel.ConcConcFlux.magnitude (Python parameter) — A Float specifying the load magnitude.")*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.ConcConcFlux.distributionType "abaqus.Load.LoadModel.LoadModel.ConcConcFlux.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.LoadModel.ConcConcFlux.field "abaqus.Load.LoadModel.LoadModel.ConcConcFlux.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.ConcConcFlux.amplitude "abaqus.Load.LoadModel.LoadModel.ConcConcFlux.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L516-L565)[¶](#abaqus.Load.LoadModel.LoadModel.ConcConcFlux "Permalink to this definition")
    :   This method creates a ConcConcFlux object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ConcConcFlux
        ```

        Note

        Check [ConcConcFlux on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concconcfluxpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.ConcConcFlux-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.ConcConcFlux.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.ConcConcFlux.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created. This must be the
                first analysis step name.

            region[¶](#abaqus.Load.LoadModel.LoadModel.ConcConcFlux.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            magnitude[¶](#abaqus.Load.LoadModel.LoadModel.ConcConcFlux.magnitude "Permalink to this definition")
            :   A Float specifying the load magnitude.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.ConcConcFlux.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.ConcConcFlux.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.ConcConcFlux.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.ConcConcFlux-returns "Permalink to this headline")
        :   A ConcConcFlux object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.ConcConcFlux-return-type "Permalink to this headline")
        :   [`ConcConcFlux`](#abaqus.Load.LoadModel.ConcConcFlux "abaqus.Load.LoadModel.ConcConcFlux (Python class) — Bases: Load")

    ConcCurrent(*[name](#abaqus.Load.LoadModel.LoadModel.ConcCurrent.name "abaqus.Load.LoadModel.LoadModel.ConcCurrent.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.ConcCurrent.createStepName "abaqus.Load.LoadModel.LoadModel.ConcCurrent.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.ConcCurrent.region "abaqus.Load.LoadModel.LoadModel.ConcCurrent.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[magnitude](#abaqus.Load.LoadModel.LoadModel.ConcCurrent.magnitude "abaqus.Load.LoadModel.LoadModel.ConcCurrent.magnitude (Python parameter) — A Float specifying the load magnitude.")*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.ConcCurrent.distributionType "abaqus.Load.LoadModel.LoadModel.ConcCurrent.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.LoadModel.ConcCurrent.field "abaqus.Load.LoadModel.LoadModel.ConcCurrent.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.ConcCurrent.amplitude "abaqus.Load.LoadModel.LoadModel.ConcCurrent.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L567-L616)[¶](#abaqus.Load.LoadModel.LoadModel.ConcCurrent "Permalink to this definition")
    :   This method creates a ConcCurrent object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ConcCurrent
        ```

        Note

        Check [ConcCurrent on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-conccurrentpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.ConcCurrent-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.ConcCurrent.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.ConcCurrent.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created. This must be the
                first analysis step name.

            region[¶](#abaqus.Load.LoadModel.LoadModel.ConcCurrent.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            magnitude[¶](#abaqus.Load.LoadModel.LoadModel.ConcCurrent.magnitude "Permalink to this definition")
            :   A Float specifying the load magnitude.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.ConcCurrent.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.ConcCurrent.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.ConcCurrent.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.ConcCurrent-returns "Permalink to this headline")
        :   A ConcCurrent object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.ConcCurrent-return-type "Permalink to this headline")
        :   [`ConcCurrent`](#abaqus.Load.LoadModel.ConcCurrent "abaqus.Load.LoadModel.ConcCurrent (Python class) — Bases: Load")

    ConcPoreFluid(*[name](#abaqus.Load.LoadModel.LoadModel.ConcPoreFluid.name "abaqus.Load.LoadModel.LoadModel.ConcPoreFluid.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.ConcPoreFluid.createStepName "abaqus.Load.LoadModel.LoadModel.ConcPoreFluid.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.ConcPoreFluid.region "abaqus.Load.LoadModel.LoadModel.ConcPoreFluid.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[magnitude](#abaqus.Load.LoadModel.LoadModel.ConcPoreFluid.magnitude "abaqus.Load.LoadModel.LoadModel.ConcPoreFluid.magnitude (Python parameter) — A Float specifying the load magnitude.")*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.ConcPoreFluid.distributionType "abaqus.Load.LoadModel.LoadModel.ConcPoreFluid.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.LoadModel.ConcPoreFluid.field "abaqus.Load.LoadModel.LoadModel.ConcPoreFluid.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.ConcPoreFluid.amplitude "abaqus.Load.LoadModel.LoadModel.ConcPoreFluid.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L759-L808)[¶](#abaqus.Load.LoadModel.LoadModel.ConcPoreFluid "Permalink to this definition")
    :   This method creates a ConcPoreFluid object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ConcPoreFluid
        ```

        Note

        Check [ConcPoreFluid on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concporefluidpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.ConcPoreFluid-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.ConcPoreFluid.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.ConcPoreFluid.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created. This must be the
                first analysis step name.

            region[¶](#abaqus.Load.LoadModel.LoadModel.ConcPoreFluid.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            magnitude[¶](#abaqus.Load.LoadModel.LoadModel.ConcPoreFluid.magnitude "Permalink to this definition")
            :   A Float specifying the load magnitude.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.ConcPoreFluid.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.ConcPoreFluid.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.ConcPoreFluid.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.ConcPoreFluid-returns "Permalink to this headline")
        :   A ConcPoreFluid object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.ConcPoreFluid-return-type "Permalink to this headline")
        :   [`ConcPoreFluid`](#abaqus.Load.LoadModel.ConcPoreFluid "abaqus.Load.LoadModel.ConcPoreFluid (Python class) — Bases: Load")

    ConcentratedForce(*[name](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce.name "abaqus.Load.LoadModel.LoadModel.ConcentratedForce.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce.createStepName "abaqus.Load.LoadModel.LoadModel.ConcentratedForce.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce.region "abaqus.Load.LoadModel.LoadModel.ConcentratedForce.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce.distributionType "abaqus.Load.LoadModel.LoadModel.ConcentratedForce.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce.field "abaqus.Load.LoadModel.LoadModel.ConcentratedForce.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[cf1](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce.cf1 "abaqus.Load.LoadModel.LoadModel.ConcentratedForce.cf1 (Python parameter) — A Float or a Complex specifying the concentrated force component in the 1-direction. Although cf1, cf2, and cf3 are optional arguments, at least one of them must be nonzero.")=`None`*, *[cf2](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce.cf2 "abaqus.Load.LoadModel.LoadModel.ConcentratedForce.cf2 (Python parameter) — A Float or a Complex specifying the concentrated force component in the 2-direction.")=`None`*, *[cf3](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce.cf3 "abaqus.Load.LoadModel.LoadModel.ConcentratedForce.cf3 (Python parameter) — A Float or a Complex specifying the concentrated force component in the 3-direction.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce.amplitude "abaqus.Load.LoadModel.LoadModel.ConcentratedForce.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*, *[follower](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce.follower "abaqus.Load.LoadModel.LoadModel.ConcentratedForce.follower (Python parameter) — A Boolean specifying whether the direction of the force rotates with the rotation at each node of the region.")=`0`*, *[localCsys](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce.localCsys "abaqus.Load.LoadModel.LoadModel.ConcentratedForce.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the load's degrees of freedom.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L618-L695)[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce "Permalink to this definition")
    :   This method creates a ConcentratedForce object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ConcentratedForce
        ```

        Note

        Check [ConcentratedForce on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concentratedforcepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created.

            region[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            cf1=`None`[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce.cf1 "Permalink to this definition")
            :   A Float or a Complex specifying the concentrated force component in the 1-direction.
                Although **cf1**, **cf2**, and **cf3** are optional arguments, at least one of them must be
                nonzero.

            cf2=`None`[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce.cf2 "Permalink to this definition")
            :   A Float or a Complex specifying the concentrated force component in the 2-direction.

            cf3=`None`[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce.cf3 "Permalink to this definition")
            :   A Float or a Complex specifying the concentrated force component in the 3-direction.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

            follower=`0`[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce.follower "Permalink to this definition")
            :   A Boolean specifying whether the direction of the force rotates with the rotation at
                each node of the region. You should provide the **follower** argument only if it is valid
                for the specified step. The default value is OFF.

            localCsys=`None`[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the load’s degrees
                of freedom. If **localCsys** = None, the degrees of freedom are defined in the global
                coordinate system. When this member is queried, it returns an Int. The default value is
                None.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce-returns "Permalink to this headline")
        :   A ConcentratedForce object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedForce-return-type "Permalink to this headline")
        :   [`ConcentratedForce`](#abaqus.Load.LoadModel.ConcentratedForce "abaqus.Load.LoadModel.ConcentratedForce (Python class) — Bases: Load")

    ConcentratedHeatFlux(*[name](#abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux.name "abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux.createStepName "abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux.region "abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[magnitude](#abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux.magnitude "abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux.magnitude (Python parameter) — A Float specifying the load magnitude.")*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux.distributionType "abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux.field "abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux.amplitude "abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*, *[dof](#abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux.dof "abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux.dof (Python parameter) — An Int specifying the degree of freedom of the node, to which the concentrated heat flux should be applied.")=`11`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L697-L757)[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux "Permalink to this definition")
    :   This method creates a ConcentratedHeatFlux object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ConcentratedHeatFlux
        ```

        Note

        Check [ConcentratedHeatFlux on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concentratedheatfluxpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created. This must be the
                first analysis step name.

            region[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            magnitude[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux.magnitude "Permalink to this definition")
            :   A Float specifying the load magnitude.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

            dof=`11`[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux.dof "Permalink to this definition")
            :   An Int specifying the degree of freedom of the node, to which the concentrated heat flux
                should be applied. The default value is 11.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux-returns "Permalink to this headline")
        :   A ConcentratedHeatFlux object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux-return-type "Permalink to this headline")
        :   [`ConcentratedHeatFlux`](#abaqus.Load.LoadModel.ConcentratedHeatFlux "abaqus.Load.LoadModel.ConcentratedHeatFlux (Python class) — Bases: Load")

    ConnectorForce(*[name](#abaqus.Load.LoadModel.LoadModel.ConnectorForce.name "abaqus.Load.LoadModel.LoadModel.ConnectorForce.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.ConnectorForce.createStepName "abaqus.Load.LoadModel.LoadModel.ConnectorForce.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.ConnectorForce.region "abaqus.Load.LoadModel.LoadModel.ConnectorForce.region (Python parameter) — The wire region to which the load is applied.")=`''`*, *[fastenerName](#abaqus.Load.LoadModel.LoadModel.ConnectorForce.fastenerName "abaqus.Load.LoadModel.LoadModel.ConnectorForce.fastenerName (Python parameter) — A String specifying the name of the assembled fastener to which the load will be applied.")=`''`*, *[fastenerSetName](#abaqus.Load.LoadModel.LoadModel.ConnectorForce.fastenerSetName "abaqus.Load.LoadModel.LoadModel.ConnectorForce.fastenerSetName (Python parameter) — A String specifying the assembled fastener template model set to which the load will be applied.")=`''`*, *[f1](#abaqus.Load.LoadModel.LoadModel.ConnectorForce.f1 "abaqus.Load.LoadModel.LoadModel.ConnectorForce.f1 (Python parameter) — A Float or a Complex specifying the connector force component in the connector's local 1-direction.")=`None`*, *[f2](#abaqus.Load.LoadModel.LoadModel.ConnectorForce.f2 "abaqus.Load.LoadModel.LoadModel.ConnectorForce.f2 (Python parameter) — A Float or a Complex specifying the connector force component in the connector's local 2-direction.")=`None`*, *[f3](#abaqus.Load.LoadModel.LoadModel.ConnectorForce.f3 "abaqus.Load.LoadModel.LoadModel.ConnectorForce.f3 (Python parameter) — A Float or a Complex specifying the connector force component in the connector's local 3-direction.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.ConnectorForce.amplitude "abaqus.Load.LoadModel.LoadModel.ConnectorForce.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L810-L880)[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorForce "Permalink to this definition")
    :   This method creates a ConnectorForce object on a wire region. Alternatively, the load may also be
        applied to a wire set referenced from an assembled fastener template model.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ConnectorForce
        ```

        Note

        Check [ConnectorForce on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorforcepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorForce-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorForce.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorForce.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created.

            region=`''`[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorForce.region "Permalink to this definition")
            :   The wire region to which the load is applied. This argument is not valid when
                **fastenerName** and **fastenerSetName** are specified.

            fastenerName=`''`[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorForce.fastenerName "Permalink to this definition")
            :   A String specifying the name of the assembled fastener to which the load will be
                applied. This argument is not valid when **region** is specified. When this argument is
                specified, **fastenerSetName** must also be specified. The default value is an empty
                string.

            fastenerSetName=`''`[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorForce.fastenerSetName "Permalink to this definition")
            :   A String specifying the assembled fastener template model set to which the load will be
                applied. This argument is not valid when **region** is specified. When this argument is
                specified, **fastenerName** must also be specified. The default value is an empty string.

            f1=`None`[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorForce.f1 "Permalink to this definition")
            :   A Float or a Complex specifying the connector force component in the connector’s local
                1-direction. Note: Although **f1**, **f2**, and **f3** are optional arguments, at least one of
                them must be nonzero.

            f2=`None`[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorForce.f2 "Permalink to this definition")
            :   A Float or a Complex specifying the connector force component in the connector’s local
                2-direction.

            f3=`None`[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorForce.f3 "Permalink to this definition")
            :   A Float or a Complex specifying the connector force component in the connector’s local
                3-direction.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorForce.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorForce-returns "Permalink to this headline")
        :   A ConnectorForce object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorForce-return-type "Permalink to this headline")
        :   [`ConnectorForce`](#abaqus.Load.LoadModel.ConnectorForce "abaqus.Load.LoadModel.ConnectorForce (Python class) — Bases: Load")

    ConnectorMoment(*[name](#abaqus.Load.LoadModel.LoadModel.ConnectorMoment.name "abaqus.Load.LoadModel.LoadModel.ConnectorMoment.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.ConnectorMoment.createStepName "abaqus.Load.LoadModel.LoadModel.ConnectorMoment.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.ConnectorMoment.region "abaqus.Load.LoadModel.LoadModel.ConnectorMoment.region (Python parameter) — The wire region to which the load is applied.")=`''`*, *[fastenerName](#abaqus.Load.LoadModel.LoadModel.ConnectorMoment.fastenerName "abaqus.Load.LoadModel.LoadModel.ConnectorMoment.fastenerName (Python parameter) — A String specifying the name of the assembled fastener to which the load will be applied.")=`''`*, *[fastenerSetName](#abaqus.Load.LoadModel.LoadModel.ConnectorMoment.fastenerSetName "abaqus.Load.LoadModel.LoadModel.ConnectorMoment.fastenerSetName (Python parameter) — A String specifying the assembled fastener template model set to which the load will be applied.")=`''`*, *[m1](#abaqus.Load.LoadModel.LoadModel.ConnectorMoment.m1 "abaqus.Load.LoadModel.LoadModel.ConnectorMoment.m1 (Python parameter) — A Float or a Complex specifying the moment component in the connector's local 4-direction.")=`None`*, *[m2](#abaqus.Load.LoadModel.LoadModel.ConnectorMoment.m2 "abaqus.Load.LoadModel.LoadModel.ConnectorMoment.m2 (Python parameter) — A Float or a Complex specifying the moment component in the connector's local 5-direction.")=`None`*, *[m3](#abaqus.Load.LoadModel.LoadModel.ConnectorMoment.m3 "abaqus.Load.LoadModel.LoadModel.ConnectorMoment.m3 (Python parameter) — A Float or a Complex specifying the moment component in the connector's local 6-direction.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.ConnectorMoment.amplitude "abaqus.Load.LoadModel.LoadModel.ConnectorMoment.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L882-L951)[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorMoment "Permalink to this definition")
    :   This method creates a ConnectorMoment object on a wire region. Alternatively, the load may also be
        applied to a wire set referenced from an assembled fastener template model.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ConnectorMoment
        ```

        Note

        Check [ConnectorMoment on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectormomentpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorMoment-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorMoment.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorMoment.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created.

            region=`''`[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorMoment.region "Permalink to this definition")
            :   The wire region to which the load is applied. This argument is not valid when
                **fastenerName** and **fastenerSetName** are specified.

            fastenerName=`''`[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorMoment.fastenerName "Permalink to this definition")
            :   A String specifying the name of the assembled fastener to which the load will be
                applied. This argument is not valid when **region** is specified. When this argument is
                specified, **fastenerSetName** must also be specified. The default value is an empty
                string.

            fastenerSetName=`''`[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorMoment.fastenerSetName "Permalink to this definition")
            :   A String specifying the assembled fastener template model set to which the load will be
                applied. This argument is not valid when **region** is specified. When this argument is
                specified, **fastenerName** must also be specified. The default value is an empty string.

            m1=`None`[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorMoment.m1 "Permalink to this definition")
            :   A Float or a Complex specifying the moment component in the connector’s local
                4-direction.

            m2=`None`[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorMoment.m2 "Permalink to this definition")
            :   A Float or a Complex specifying the moment component in the connector’s local
                5-direction.

            m3=`None`[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorMoment.m3 "Permalink to this definition")
            :   A Float or a Complex specifying the moment component in the connector’s local
                6-direction.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorMoment.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorMoment-returns "Permalink to this headline")
        :   A ConnectorMoment object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.ConnectorMoment-return-type "Permalink to this headline")
        :   [`ConnectorMoment`](#abaqus.Load.LoadModel.ConnectorMoment "abaqus.Load.LoadModel.ConnectorMoment (Python class) — Bases: Load")

    CoriolisForce(*[name](#abaqus.Load.LoadModel.LoadModel.CoriolisForce.name "abaqus.Load.LoadModel.LoadModel.CoriolisForce.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.CoriolisForce.createStepName "abaqus.Load.LoadModel.LoadModel.CoriolisForce.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.CoriolisForce.region "abaqus.Load.LoadModel.LoadModel.CoriolisForce.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[magnitude](#abaqus.Load.LoadModel.LoadModel.CoriolisForce.magnitude "abaqus.Load.LoadModel.LoadModel.CoriolisForce.magnitude (Python parameter) — A Float specifying the load magnitude.")*, *[point1](#abaqus.Load.LoadModel.LoadModel.CoriolisForce.point1 "abaqus.Load.LoadModel.LoadModel.CoriolisForce.point1 (Python parameter) — A sequence of Floats specifying the first point on the axis of rotation for the load.")*, *[point2](#abaqus.Load.LoadModel.LoadModel.CoriolisForce.point2 "abaqus.Load.LoadModel.LoadModel.CoriolisForce.point2 (Python parameter) — A sequence of Floats specifying the second point on the axis of rotation for the load.")*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.CoriolisForce.amplitude "abaqus.Load.LoadModel.LoadModel.CoriolisForce.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.CoriolisForce.distributionType "abaqus.Load.LoadModel.LoadModel.CoriolisForce.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.LoadModel.CoriolisForce.field "abaqus.Load.LoadModel.LoadModel.CoriolisForce.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L953-L1016)[¶](#abaqus.Load.LoadModel.LoadModel.CoriolisForce "Permalink to this definition")
    :   This method creates a CoriolisForce object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].CoriolisForce
        ```

        Note

        Check [CoriolisForce on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-coriolisforcepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.CoriolisForce-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.CoriolisForce.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.CoriolisForce.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created. This must be the
                first analysis step name.

            region[¶](#abaqus.Load.LoadModel.LoadModel.CoriolisForce.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            magnitude[¶](#abaqus.Load.LoadModel.LoadModel.CoriolisForce.magnitude "Permalink to this definition")
            :   A Float specifying the load magnitude.

            point1[¶](#abaqus.Load.LoadModel.LoadModel.CoriolisForce.point1 "Permalink to this definition")
            :   A sequence of Floats specifying the first point on the axis of rotation for the load.

            point2[¶](#abaqus.Load.LoadModel.LoadModel.CoriolisForce.point2 "Permalink to this definition")
            :   A sequence of Floats specifying the second point on the axis of rotation for the load.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.CoriolisForce.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.CoriolisForce.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.CoriolisForce.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.CoriolisForce-returns "Permalink to this headline")
        :   A CoriolisForce object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.CoriolisForce-return-type "Permalink to this headline")
        :   [`CoriolisForce`](#abaqus.Load.LoadModel.CoriolisForce "abaqus.Load.LoadModel.CoriolisForce (Python class) — Bases: Load")

    Gravity(*[name](#abaqus.Load.LoadModel.LoadModel.Gravity.name "abaqus.Load.LoadModel.LoadModel.Gravity.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.Gravity.createStepName "abaqus.Load.LoadModel.LoadModel.Gravity.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.Gravity.distributionType "abaqus.Load.LoadModel.LoadModel.Gravity.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.LoadModel.Gravity.field "abaqus.Load.LoadModel.LoadModel.Gravity.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[region](#abaqus.Load.LoadModel.LoadModel.Gravity.region "abaqus.Load.LoadModel.LoadModel.Gravity.region (Python parameter) — A Region object specifying the region to which the load is applied.")=`None`*, *[comp1](#abaqus.Load.LoadModel.LoadModel.Gravity.comp1 "abaqus.Load.LoadModel.LoadModel.Gravity.comp1 (Python parameter) — A Float or a Complex specifying the component of the load in the 1-direction.")=`None`*, *[comp2](#abaqus.Load.LoadModel.LoadModel.Gravity.comp2 "abaqus.Load.LoadModel.LoadModel.Gravity.comp2 (Python parameter) — A Float or a Complex specifying the component of the load in the 2-direction.")=`None`*, *[comp3](#abaqus.Load.LoadModel.LoadModel.Gravity.comp3 "abaqus.Load.LoadModel.LoadModel.Gravity.comp3 (Python parameter) — A Float or a Complex specifying the component of the load in the 3-direction.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.Gravity.amplitude "abaqus.Load.LoadModel.LoadModel.Gravity.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L1018-L1082)[¶](#abaqus.Load.LoadModel.LoadModel.Gravity "Permalink to this definition")
    :   This method creates a Gravity object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].Gravity
        ```

        Note

        Check [Gravity on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gravitypyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.Gravity-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.Gravity.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.Gravity.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.Gravity.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.Gravity.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            region=`None`[¶](#abaqus.Load.LoadModel.LoadModel.Gravity.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            comp1=`None`[¶](#abaqus.Load.LoadModel.LoadModel.Gravity.comp1 "Permalink to this definition")
            :   A Float or a Complex specifying the component of the load in the
                1-direction. Note: Although **comp1**, **comp2**, and **comp3** are optional arguments, at least
                one of them must be nonzero.

            comp2=`None`[¶](#abaqus.Load.LoadModel.LoadModel.Gravity.comp2 "Permalink to this definition")
            :   A Float or a Complex specifying the component of the load in the 2-direction.

            comp3=`None`[¶](#abaqus.Load.LoadModel.LoadModel.Gravity.comp3 "Permalink to this definition")
            :   A Float or a Complex specifying the component of the load in the 3-direction.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.Gravity.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.Gravity-returns "Permalink to this headline")
        :   A Gravity object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.Gravity-return-type "Permalink to this headline")
        :   [`Gravity`](#abaqus.Load.LoadModel.Gravity "abaqus.Load.LoadModel.Gravity (Python class) — Bases: Load")

    InertiaRelief(*[name](#abaqus.Load.LoadModel.LoadModel.InertiaRelief.name "abaqus.Load.LoadModel.LoadModel.InertiaRelief.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.InertiaRelief.createStepName "abaqus.Load.LoadModel.LoadModel.InertiaRelief.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[u1](#abaqus.Load.LoadModel.LoadModel.InertiaRelief.u1 "abaqus.Load.LoadModel.LoadModel.InertiaRelief.u1 (Python parameter) — A Boolean specifying the 1-direction as a free direction.")=`0`*, *[u2](#abaqus.Load.LoadModel.LoadModel.InertiaRelief.u2 "abaqus.Load.LoadModel.LoadModel.InertiaRelief.u2 (Python parameter) — A Boolean specifying the 2-direction as a free direction.")=`0`*, *[u3](#abaqus.Load.LoadModel.LoadModel.InertiaRelief.u3 "abaqus.Load.LoadModel.LoadModel.InertiaRelief.u3 (Python parameter) — A Boolean specifying the 3-direction as a free direction.")=`0`*, *[ur1](#abaqus.Load.LoadModel.LoadModel.InertiaRelief.ur1 "abaqus.Load.LoadModel.LoadModel.InertiaRelief.ur1 (Python parameter) — A Boolean specifying the rotation about the 1-direction as a free direction.")=`0`*, *[ur2](#abaqus.Load.LoadModel.LoadModel.InertiaRelief.ur2 "abaqus.Load.LoadModel.LoadModel.InertiaRelief.ur2 (Python parameter) — A Boolean specifying the rotation about the 2-direction as a free direction.")=`0`*, *[ur3](#abaqus.Load.LoadModel.LoadModel.InertiaRelief.ur3 "abaqus.Load.LoadModel.LoadModel.InertiaRelief.ur3 (Python parameter) — A Boolean specifying the rotation about the 3-direction as a free direction.")=`0`*, *[referencePoint](#abaqus.Load.LoadModel.LoadModel.InertiaRelief.referencePoint "abaqus.Load.LoadModel.LoadModel.InertiaRelief.referencePoint (Python parameter) — A sequence of Floats specifying the X, Y and Z coordinates of a fixed rotation point or a point on the rotation axis or a point on the symmetry line, about which rotations are defined.")=`()`*, *[localCoordinates](#abaqus.Load.LoadModel.LoadModel.InertiaRelief.localCoordinates "abaqus.Load.LoadModel.LoadModel.InertiaRelief.localCoordinates (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the rigid body degrees of freedom for the inertia relief load.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L1084-L1154)[¶](#abaqus.Load.LoadModel.LoadModel.InertiaRelief "Permalink to this definition")
    :   This method creates an InertiaRelief object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].InertiaRelief
        ```

        Note

        Check [InertiaRelief on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-inertiareliefpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.InertiaRelief-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.InertiaRelief.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.InertiaRelief.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created.

            u1=`0`[¶](#abaqus.Load.LoadModel.LoadModel.InertiaRelief.u1 "Permalink to this definition")
            :   A Boolean specifying the 1-direction as a free direction. Note: Although **u1**, **u2**, **u3**,
                **ur1**, **ur2**, and **ur3** are optional arguments, at least one of them must be specified.
                Further, any specified set of free directions cannot include only two rotational degrees
                of freedom.

            u2=`0`[¶](#abaqus.Load.LoadModel.LoadModel.InertiaRelief.u2 "Permalink to this definition")
            :   A Boolean specifying the 2-direction as a free direction.

            u3=`0`[¶](#abaqus.Load.LoadModel.LoadModel.InertiaRelief.u3 "Permalink to this definition")
            :   A Boolean specifying the 3-direction as a free direction.

            ur1=`0`[¶](#abaqus.Load.LoadModel.LoadModel.InertiaRelief.ur1 "Permalink to this definition")
            :   A Boolean specifying the rotation about the 1-direction as a free direction.

            ur2=`0`[¶](#abaqus.Load.LoadModel.LoadModel.InertiaRelief.ur2 "Permalink to this definition")
            :   A Boolean specifying the rotation about the 2-direction as a free direction.

            ur3=`0`[¶](#abaqus.Load.LoadModel.LoadModel.InertiaRelief.ur3 "Permalink to this definition")
            :   A Boolean specifying the rotation about the 3-direction as a free direction.

            referencePoint=`()`[¶](#abaqus.Load.LoadModel.LoadModel.InertiaRelief.referencePoint "Permalink to this definition")
            :   A sequence of Floats specifying the **X**, **Y** and **Z** coordinates of a fixed rotation
                point or a point on the rotation axis or a point on the symmetry line, about which
                rotations are defined. Such a point must be specified only for certain combinations of
                free directions.

            localCoordinates=`None`[¶](#abaqus.Load.LoadModel.LoadModel.InertiaRelief.localCoordinates "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the rigid body
                degrees of freedom for the inertia relief load. If **localCoordinates** = None, the free
                directions are defined in the global coordinate system. When this member is queried, it
                returns an Int. The default value is None.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.InertiaRelief-returns "Permalink to this headline")
        :   An InertiaRelief object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.InertiaRelief-return-type "Permalink to this headline")
        :   [`InertiaRelief`](#abaqus.Load.LoadModel.InertiaRelief "abaqus.Load.LoadModel.InertiaRelief (Python class) — Bases: Load")

    InwardVolAccel(*[name](#abaqus.Load.LoadModel.LoadModel.InwardVolAccel.name "abaqus.Load.LoadModel.LoadModel.InwardVolAccel.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.InwardVolAccel.createStepName "abaqus.Load.LoadModel.LoadModel.InwardVolAccel.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.InwardVolAccel.region "abaqus.Load.LoadModel.LoadModel.InwardVolAccel.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[magnitude](#abaqus.Load.LoadModel.LoadModel.InwardVolAccel.magnitude "abaqus.Load.LoadModel.LoadModel.InwardVolAccel.magnitude (Python parameter) — A Float specifying the load magnitude.")*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.InwardVolAccel.distributionType "abaqus.Load.LoadModel.LoadModel.InwardVolAccel.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.LoadModel.InwardVolAccel.field "abaqus.Load.LoadModel.LoadModel.InwardVolAccel.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.InwardVolAccel.amplitude "abaqus.Load.LoadModel.LoadModel.InwardVolAccel.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L1156-L1205)[¶](#abaqus.Load.LoadModel.LoadModel.InwardVolAccel "Permalink to this definition")
    :   This method creates a InwardVolAccel object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].InwardVolAccel
        ```

        Note

        Check [InwardVolAccel on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-inwardvolaccelpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.InwardVolAccel-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.InwardVolAccel.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.InwardVolAccel.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created. This must be the
                name of the first analysis step.

            region[¶](#abaqus.Load.LoadModel.LoadModel.InwardVolAccel.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            magnitude[¶](#abaqus.Load.LoadModel.LoadModel.InwardVolAccel.magnitude "Permalink to this definition")
            :   A Float specifying the load magnitude.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.InwardVolAccel.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.InwardVolAccel.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.InwardVolAccel.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.InwardVolAccel-returns "Permalink to this headline")
        :   An InwardVolAccel object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.InwardVolAccel-return-type "Permalink to this headline")
        :   [`InwardVolAccel`](#abaqus.Load.LoadModel.InwardVolAccel "abaqus.Load.LoadModel.InwardVolAccel (Python class) — Bases: Load")

    LineLoad(*[name](#abaqus.Load.LoadModel.LoadModel.LineLoad.name "abaqus.Load.LoadModel.LoadModel.LineLoad.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.LineLoad.createStepName "abaqus.Load.LoadModel.LoadModel.LineLoad.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.LineLoad.region "abaqus.Load.LoadModel.LoadModel.LineLoad.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.LineLoad.distributionType "abaqus.Load.LoadModel.LoadModel.LineLoad.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.LoadModel.LineLoad.field "abaqus.Load.LoadModel.LoadModel.LineLoad.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[comp1](#abaqus.Load.LoadModel.LoadModel.LineLoad.comp1 "abaqus.Load.LoadModel.LoadModel.LineLoad.comp1 (Python parameter) — A Float or a Complex specifying the component of the load in the global or the beam local 1-direction.")=`None`*, *[comp2](#abaqus.Load.LoadModel.LoadModel.LineLoad.comp2 "abaqus.Load.LoadModel.LoadModel.LineLoad.comp2 (Python parameter) — A Float or a Complex specifying the component of the load in the global or the beam local 2-direction.")=`None`*, *[comp3](#abaqus.Load.LoadModel.LoadModel.LineLoad.comp3 "abaqus.Load.LoadModel.LoadModel.LineLoad.comp3 (Python parameter) — A Float or a Complex specifying the component of the load in the global 3-direction.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.LineLoad.amplitude "abaqus.Load.LoadModel.LoadModel.LineLoad.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*, *[system](#abaqus.Load.LoadModel.LoadModel.LineLoad.system "abaqus.Load.LoadModel.LoadModel.LineLoad.system (Python parameter) — A SymbolicConstant specifying whether the load is applied in a global or the beam local frame of reference.")=`abaqusConstants.GLOBAL`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L1207-L1277)[¶](#abaqus.Load.LoadModel.LoadModel.LineLoad "Permalink to this definition")
    :   This method creates a LineLoad object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].LineLoad
        ```

        Note

        Check [LineLoad on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-lineloadpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.LineLoad-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.LineLoad.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.LineLoad.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created.

            region[¶](#abaqus.Load.LoadModel.LoadModel.LineLoad.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.LineLoad.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.LineLoad.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            comp1=`None`[¶](#abaqus.Load.LoadModel.LoadModel.LineLoad.comp1 "Permalink to this definition")
            :   A Float or a Complex specifying the component of the load in the global or the beam
                local 1-direction. Note: Although **comp1**, **comp2**, and **comp3** are optional arguments, at
                least one of them must be nonzero unless **distributionType** = USER\_DEFINED.

            comp2=`None`[¶](#abaqus.Load.LoadModel.LoadModel.LineLoad.comp2 "Permalink to this definition")
            :   A Float or a Complex specifying the component of the load in the global or the beam
                local 2-direction.

            comp3=`None`[¶](#abaqus.Load.LoadModel.LoadModel.LineLoad.comp3 "Permalink to this definition")
            :   A Float or a Complex specifying the component of the load in the global 3-direction.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.LineLoad.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

            system=`abaqusConstants.GLOBAL`[¶](#abaqus.Load.LoadModel.LoadModel.LineLoad.system "Permalink to this definition")
            :   A SymbolicConstant specifying whether the load is applied in a global or the beam local
                frame of reference. Possible values are GLOBAL and LOCAL. The default value is GLOBAL.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.LineLoad-returns "Permalink to this headline")
        :   A LineLoad object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.LineLoad-return-type "Permalink to this headline")
        :   [`LineLoad`](#abaqus.Load.LoadModel.LineLoad "abaqus.Load.LoadModel.LineLoad (Python class) — Bases: Load")

    Moment(*[name](#abaqus.Load.LoadModel.LoadModel.Moment.name "abaqus.Load.LoadModel.LoadModel.Moment.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.Moment.createStepName "abaqus.Load.LoadModel.LoadModel.Moment.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.Moment.region "abaqus.Load.LoadModel.LoadModel.Moment.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[cm1](#abaqus.Load.LoadModel.LoadModel.Moment.cm1 "abaqus.Load.LoadModel.LoadModel.Moment.cm1 (Python parameter) — A Float or a Complex specifying the load component in the 4-direction.")=`None`*, *[cm2](#abaqus.Load.LoadModel.LoadModel.Moment.cm2 "abaqus.Load.LoadModel.LoadModel.Moment.cm2 (Python parameter) — A Float or a Complex specifying the load component in the 5- direction.")=`None`*, *[cm3](#abaqus.Load.LoadModel.LoadModel.Moment.cm3 "abaqus.Load.LoadModel.LoadModel.Moment.cm3 (Python parameter) — A Float or a Complex specifying the load component in the 6-direction.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.Moment.amplitude "abaqus.Load.LoadModel.LoadModel.Moment.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*, *[follower](#abaqus.Load.LoadModel.LoadModel.Moment.follower "abaqus.Load.LoadModel.LoadModel.Moment.follower (Python parameter) — A Boolean specifying whether the direction of the force rotates with the rotation of the node.")=`0`*, *[localCsys](#abaqus.Load.LoadModel.LoadModel.Moment.localCsys "abaqus.Load.LoadModel.LoadModel.Moment.localCsys (Python parameter) — None or a DatumCsys object specifying the ID of the Datum coordinate system used as the local coordinate system of the load.")=`None`*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.Moment.distributionType "abaqus.Load.LoadModel.LoadModel.Moment.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.LoadModel.Moment.field "abaqus.Load.LoadModel.LoadModel.Moment.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L1279-L1356)[¶](#abaqus.Load.LoadModel.LoadModel.Moment "Permalink to this definition")
    :   This method creates a Moment object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].Moment
        ```

        Note

        Check [Moment on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-momentpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.Moment-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.Moment.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.Moment.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created.

            region[¶](#abaqus.Load.LoadModel.LoadModel.Moment.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            cm1=`None`[¶](#abaqus.Load.LoadModel.LoadModel.Moment.cm1 "Permalink to this definition")
            :   A Float or a Complex specifying the load component in the 4-direction. Note: Although
                **comp1**, **comp2**, and **comp3** are optional arguments, at least one of them must be
                nonzero.

            cm2=`None`[¶](#abaqus.Load.LoadModel.LoadModel.Moment.cm2 "Permalink to this definition")
            :   A Float or a Complex specifying the load component in the 5- direction.

            cm3=`None`[¶](#abaqus.Load.LoadModel.LoadModel.Moment.cm3 "Permalink to this definition")
            :   A Float or a Complex specifying the load component in the 6-direction.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.Moment.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

            follower=`0`[¶](#abaqus.Load.LoadModel.LoadModel.Moment.follower "Permalink to this definition")
            :   A Boolean specifying whether the direction of the force rotates with the rotation of the
                node. You should provide the **follower** argument only if it is valid for the specified
                step. The default value is OFF.

            localCsys=`None`[¶](#abaqus.Load.LoadModel.LoadModel.Moment.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the ID of the Datum coordinate system used as the
                local coordinate system of the load. If **localCsys** = None, the load is defined in the
                global coordinate system. When this member is queried, it returns an Int. The default
                value is None.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.Moment.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.Moment.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.Moment-returns "Permalink to this headline")
        :   A Moment object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.Moment-return-type "Permalink to this headline")
        :   [`Moment`](#abaqus.Load.LoadModel.LoadModel.Moment "abaqus.Load.LoadModel.LoadModel.Moment (Python method) — This method creates a Moment object.")

    PEGLoad(*[name](#abaqus.Load.LoadModel.LoadModel.PEGLoad.name "abaqus.Load.LoadModel.LoadModel.PEGLoad.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.PEGLoad.createStepName "abaqus.Load.LoadModel.LoadModel.PEGLoad.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.PEGLoad.region "abaqus.Load.LoadModel.LoadModel.PEGLoad.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.PEGLoad.distributionType "abaqus.Load.LoadModel.LoadModel.PEGLoad.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.LoadModel.PEGLoad.field "abaqus.Load.LoadModel.LoadModel.PEGLoad.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[comp1](#abaqus.Load.LoadModel.LoadModel.PEGLoad.comp1 "abaqus.Load.LoadModel.LoadModel.PEGLoad.comp1 (Python parameter) — A Float or a Complex specifying the load component at dof 1 of reference node 1.")=`None`*, *[comp2](#abaqus.Load.LoadModel.LoadModel.PEGLoad.comp2 "abaqus.Load.LoadModel.LoadModel.PEGLoad.comp2 (Python parameter) — A Float or a Complex specifying the load component at dof 1 of reference node 2.")=`None`*, *[comp3](#abaqus.Load.LoadModel.LoadModel.PEGLoad.comp3 "abaqus.Load.LoadModel.LoadModel.PEGLoad.comp3 (Python parameter) — A Float or a Complex specifying the load component at dof 2 of reference node 2.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.PEGLoad.amplitude "abaqus.Load.LoadModel.LoadModel.PEGLoad.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L1358-L1422)[¶](#abaqus.Load.LoadModel.LoadModel.PEGLoad "Permalink to this definition")
    :   This method creates a PEGLoad object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].PEGLoad
        ```

        Note

        Check [PEGLoad on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pegloadpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.PEGLoad-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.PEGLoad.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.PEGLoad.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created.

            region[¶](#abaqus.Load.LoadModel.LoadModel.PEGLoad.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.PEGLoad.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.PEGLoad.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            comp1=`None`[¶](#abaqus.Load.LoadModel.LoadModel.PEGLoad.comp1 "Permalink to this definition")
            :   A Float or a Complex specifying the load component at dof 1 of reference node
                1. Note: Although **comp1**, **comp2**, and **comp3** are optional arguments, at least one of
                them must be nonzero.

            comp2=`None`[¶](#abaqus.Load.LoadModel.LoadModel.PEGLoad.comp2 "Permalink to this definition")
            :   A Float or a Complex specifying the load component at dof 1 of reference node 2.

            comp3=`None`[¶](#abaqus.Load.LoadModel.LoadModel.PEGLoad.comp3 "Permalink to this definition")
            :   A Float or a Complex specifying the load component at dof 2 of reference node 2.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.PEGLoad.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.PEGLoad-returns "Permalink to this headline")
        :   A PEGLoad object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.PEGLoad-return-type "Permalink to this headline")
        :   [`PEGLoad`](#abaqus.Load.LoadModel.LoadModel.PEGLoad "abaqus.Load.LoadModel.LoadModel.PEGLoad (Python method) — This method creates a PEGLoad object.")

    PipePressure(*[name](#abaqus.Load.LoadModel.LoadModel.PipePressure.name "abaqus.Load.LoadModel.LoadModel.PipePressure.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.PipePressure.createStepName "abaqus.Load.LoadModel.LoadModel.PipePressure.createStepName (Python parameter) — A String specifying the name of the step in which the pressure is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.PipePressure.region "abaqus.Load.LoadModel.LoadModel.PipePressure.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[magnitude](#abaqus.Load.LoadModel.LoadModel.PipePressure.magnitude "abaqus.Load.LoadModel.LoadModel.PipePressure.magnitude (Python parameter) — A Float specifying the pressure magnitude.")*, *[diameter](#abaqus.Load.LoadModel.LoadModel.PipePressure.diameter "abaqus.Load.LoadModel.LoadModel.PipePressure.diameter (Python parameter) — A Float specifying the effective inner or outer diameter.")*, *[hZero](#abaqus.Load.LoadModel.LoadModel.PipePressure.hZero "abaqus.Load.LoadModel.LoadModel.PipePressure.hZero (Python parameter) — A Float specifying the height of the zero pressure level when distributionType = HYDROSTATIC.")*, *[hReference](#abaqus.Load.LoadModel.LoadModel.PipePressure.hReference "abaqus.Load.LoadModel.LoadModel.PipePressure.hReference (Python parameter) — A Float specifying the height of the reference pressure level when distributionType = HYDROSTATIC.")*, *[field](#abaqus.Load.LoadModel.LoadModel.PipePressure.field "abaqus.Load.LoadModel.LoadModel.PipePressure.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.PipePressure.amplitude "abaqus.Load.LoadModel.LoadModel.PipePressure.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.PipePressure.distributionType "abaqus.Load.LoadModel.LoadModel.PipePressure.distributionType (Python parameter) — A SymbolicConstant specifying whether the load is uniform.")=`abaqusConstants.UNIFORM`*, *[side](#abaqus.Load.LoadModel.LoadModel.PipePressure.side "abaqus.Load.LoadModel.LoadModel.PipePressure.side (Python parameter) — A SymbolicConstant specifying whether the pressure is applied internally or externally. Possible values are INTERNAL and EXTERNAL.")=`abaqusConstants.INTERNAL`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L1424-L1498)[¶](#abaqus.Load.LoadModel.LoadModel.PipePressure "Permalink to this definition")
    :   This method creates a Pressure object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].PipePressure
        ```

        Note

        Check [PipePressure on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pipepressurepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.PipePressure-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.PipePressure.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.PipePressure.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the pressure is created.

            region[¶](#abaqus.Load.LoadModel.LoadModel.PipePressure.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            magnitude[¶](#abaqus.Load.LoadModel.LoadModel.PipePressure.magnitude "Permalink to this definition")
            :   A Float specifying the pressure magnitude. Note: *magnitude* is optional if
                **distributionType** = USER\_DEFINED.

            diameter[¶](#abaqus.Load.LoadModel.LoadModel.PipePressure.diameter "Permalink to this definition")
            :   A Float specifying the effective inner or outer diameter.

            hZero[¶](#abaqus.Load.LoadModel.LoadModel.PipePressure.hZero "Permalink to this definition")
            :   A Float specifying the height of the zero pressure level when
                **distributionType** = HYDROSTATIC.

            hReference[¶](#abaqus.Load.LoadModel.LoadModel.PipePressure.hReference "Permalink to this definition")
            :   A Float specifying the height of the reference pressure level when
                **distributionType** = HYDROSTATIC.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.PipePressure.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.PipePressure.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.PipePressure.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM,
                HYDROSTATIC, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            side=`abaqusConstants.INTERNAL`[¶](#abaqus.Load.LoadModel.LoadModel.PipePressure.side "Permalink to this definition")
            :   A SymbolicConstant specifying whether the pressure is applied internally or externally.
                Possible values are INTERNAL and EXTERNAL. The default value is INTERNAL.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.PipePressure-returns "Permalink to this headline")
        :   A PipePressure object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.PipePressure-return-type "Permalink to this headline")
        :   [`PipePressure`](#abaqus.Load.LoadModel.LoadModel.PipePressure "abaqus.Load.LoadModel.LoadModel.PipePressure (Python method) — This method creates a Pressure object.")

    Pressure(*[name](#abaqus.Load.LoadModel.LoadModel.Pressure.name "abaqus.Load.LoadModel.LoadModel.Pressure.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.Pressure.createStepName "abaqus.Load.LoadModel.LoadModel.Pressure.createStepName (Python parameter) — A String specifying the name of the step in which the pressure is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.Pressure.region "abaqus.Load.LoadModel.LoadModel.Pressure.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[magnitude](#abaqus.Load.LoadModel.LoadModel.Pressure.magnitude "abaqus.Load.LoadModel.LoadModel.Pressure.magnitude (Python parameter) — A Float or a Complex specifying the pressure magnitude.")=`0.0`*, *[hZero](#abaqus.Load.LoadModel.LoadModel.Pressure.hZero "abaqus.Load.LoadModel.LoadModel.Pressure.hZero (Python parameter) — A Float specifying the height of the zero pressure level when distributionType = HYDROSTATIC.")=`0.0`*, *[hReference](#abaqus.Load.LoadModel.LoadModel.Pressure.hReference "abaqus.Load.LoadModel.LoadModel.Pressure.hReference (Python parameter) — A Float specifying the height of the reference pressure level when distributionType = HYDROSTATIC.")=`0.0`*, *[field](#abaqus.Load.LoadModel.LoadModel.Pressure.field "abaqus.Load.LoadModel.LoadModel.Pressure.field (Python parameter) — A String specifying the name of the AnalyticalField or DiscreteField object associated with this load.")=`''`*, *[refPoint](#abaqus.Load.LoadModel.LoadModel.Pressure.refPoint "abaqus.Load.LoadModel.LoadModel.Pressure.refPoint (Python parameter) — A Region specifying the reference point from which the relative velocity is determined when distributionType = STAGNATION or VISCOUS.")=`''`*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.Pressure.distributionType "abaqus.Load.LoadModel.LoadModel.Pressure.distributionType (Python parameter) — A SymbolicConstant specifying how the pressure is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.Pressure.amplitude "abaqus.Load.LoadModel.LoadModel.Pressure.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L1500-L1573)[¶](#abaqus.Load.LoadModel.LoadModel.Pressure "Permalink to this definition")
    :   This method creates a Pressure object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].Pressure
        ```

        Note

        Check [Pressure on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pressurepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.Pressure-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.Pressure.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.Pressure.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the pressure is created.

            region[¶](#abaqus.Load.LoadModel.LoadModel.Pressure.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            magnitude=`0.0`[¶](#abaqus.Load.LoadModel.LoadModel.Pressure.magnitude "Permalink to this definition")
            :   A Float or a Complex specifying the pressure magnitude. Note: *magnitude* is optional if
                **distributionType** = USER\_DEFINED.

            hZero=`0.0`[¶](#abaqus.Load.LoadModel.LoadModel.Pressure.hZero "Permalink to this definition")
            :   A Float specifying the height of the zero pressure level when
                **distributionType** = HYDROSTATIC.

            hReference=`0.0`[¶](#abaqus.Load.LoadModel.LoadModel.Pressure.hReference "Permalink to this definition")
            :   A Float specifying the height of the reference pressure level when
                **distributionType** = HYDROSTATIC.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.Pressure.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField or DiscreteField object associated
                with this load. The **field** argument applies only when **distributionType** = FIELD or
                **distributionType** = DISCRETE\_FIELD. The default value is an empty string.

            refPoint=`''`[¶](#abaqus.Load.LoadModel.LoadModel.Pressure.refPoint "Permalink to this definition")
            :   A Region specifying the reference point from which the relative velocity is determined
                when **distributionType** = STAGNATION or VISCOUS.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.Pressure.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the pressure is distributed spatially. Possible values
                are UNIFORM, USER\_DEFINED, FIELD, HYDROSTATIC, STAGNATION, VISCOUS, TOTAL\_FORCE, and
                DISCRETE\_FIELD. The default value is UNIFORM.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.Pressure.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.Pressure-returns "Permalink to this headline")
        :   A Pressure object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.Pressure-return-type "Permalink to this headline")
        :   [`Pressure`](#abaqus.Load.LoadModel.LoadModel.Pressure "abaqus.Load.LoadModel.LoadModel.Pressure (Python method) — This method creates a Pressure object.")

    RotationalBodyForce(*[name](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.name "abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.createStepName "abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.region "abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[magnitude](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.magnitude "abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.magnitude (Python parameter) — A Float specifying the load magnitude.")*, *[point1](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.point1 "abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.point1 (Python parameter) — A sequence of Floats specifying the first point on the axis of rotation for the load.")*, *[point2](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.point2 "abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.point2 (Python parameter) — A sequence of Floats specifying the second point on the axis of rotation for the load.")*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.distributionType "abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.field "abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[centrifugal](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.centrifugal "abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.centrifugal (Python parameter) — A Boolean specifying whether or not the effect of the load is centrifugal.")=`0`*, *[rotaryAcceleration](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.rotaryAcceleration "abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.rotaryAcceleration (Python parameter) — A Boolean specifying whether or not the effect of the load is rotary acceleration.")=`0`*, *[rotorDynamicloads](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.rotorDynamicloads "abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.rotorDynamicloads (Python parameter) — A Boolean specifying whether or not the effect of the load is rotordynamic.")=`0`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.amplitude "abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L1575-L1665)[¶](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce "Permalink to this definition")
    :   This method creates a RotationalBodyForce object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].RotationalBodyForce
        ```

        Note

        Check [RotationalBodyForce on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rotationalbodyforcepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created. This must be the
                first analysis step name.

            region[¶](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            magnitude[¶](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.magnitude "Permalink to this definition")
            :   A Float specifying the load magnitude.

            point1[¶](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.point1 "Permalink to this definition")
            :   A sequence of Floats specifying the first point on the axis of rotation for the load.

            point2[¶](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.point2 "Permalink to this definition")
            :   A sequence of Floats specifying the second point on the axis of rotation for the load.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            centrifugal=`0`[¶](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.centrifugal "Permalink to this definition")
            :   A Boolean specifying whether or not the effect of the load is centrifugal. The default
                value is OFF. Note: At least one of **centrifugal** or **rotaryAcceleration** or
                **rotorDynamicloads** must be specified and only one must have the value ON.

                Changed in version 2025: The `rotorDynamicloads` argument was added.

            rotaryAcceleration=`0`[¶](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.rotaryAcceleration "Permalink to this definition")
            :   A Boolean specifying whether or not the effect of the load is rotary acceleration. The
                default value is OFF. Note: At least one of **centrifugal** or **rotaryAcceleration** or
                **rotorDynamicloads** must be specified and only one must have the value ON.

                Changed in version 2025: The `rotorDynamicloads` argument was added.

            rotorDynamicloads=`0`[¶](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.rotorDynamicloads "Permalink to this definition")
            :   A Boolean specifying whether or not the effect of the load is rotordynamic. The default
                value is OFF. Note: At least one of **centrifugal** or **rotaryAcceleration** or
                **rotorDynamicloads** must be specified and only one must have the value ON.

                New in version 2025: The `rotorDynamicloads` argument was added.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce-returns "Permalink to this headline")
        :   A RotationalBodyForce object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce-return-type "Permalink to this headline")
        :   [`RotationalBodyForce`](#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce "abaqus.Load.LoadModel.LoadModel.RotationalBodyForce (Python method) — This method creates a RotationalBodyForce object.")

    ShellEdgeLoad(*[name](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.name "abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.createStepName "abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.region "abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[magnitude](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.magnitude "abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.magnitude (Python parameter) — A Float or Complex specifying the load magnitude.")*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.distributionType "abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.distributionType (Python parameter) — A SymbolicConstant specifying how the shell edge load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.field "abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.amplitude "abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*, *[angle](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.angle "abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.angle (Python parameter) — A Float specifying an additional rotation of directionVector about an axis.")=`0`*, *[axis](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.axis "abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.axis (Python parameter) — A SymbolicConstant specifying the axis about which to apply an additional rotation of directionVector.")=`abaqusConstants.AXIS_1`*, *[localCsys](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.localCsys "abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.localCsys (Python parameter) — A DatumCsys object specifying the local coordinate system of the load's degrees of freedom.")=`abaqusConstants.GENERAL`*, *[userCsys](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.userCsys "abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.userCsys (Python parameter) — A String specifying a CSYS defined by a user-subroutine.")=`abaqusConstants.GENERAL`*, *[directionVector](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.directionVector "abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.directionVector (Python parameter) — A tuple of two points specifying the direction of the load.")=`()`*, *[follower](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.follower "abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.follower (Python parameter) — A Boolean specifying whether the direction of the force changes with rotation.")=`1`*, *[resultant](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.resultant "abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.resultant (Python parameter) — A Boolean specifying whether to maintain a constant resultant force by defining traction per unit undeformed area.")=`0`*, *[traction](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.traction "abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.traction (Python parameter) — A SymbolicConstant specifying how to apply surface traction.")=`abaqusConstants.NORMAL`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L1667-L1773)[¶](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad "Permalink to this definition")
    :   This method creates a ShellEdgeLoad object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ShellEdgeLoad
        ```

        Note

        Check [ShellEdgeLoad on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shelledgeloadpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created.

            region[¶](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            magnitude[¶](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.magnitude "Permalink to this definition")
            :   A Float or Complex specifying the load magnitude. **magnitude** is optional if
                **distributionType** = USER\_DEFINED

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the shell edge load is distributed spatially. Possible
                values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

            angle=`0`[¶](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.angle "Permalink to this definition")
            :   A Float specifying an additional rotation of **directionVector** about an axis. The
                default value is 0.This parameter is available only if **traction** is GENERAL.

            axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the axis about which to apply an additional rotation of
                **directionVector**. Possible values are AXIS\_1, AXIS\_2, AXIS\_3. The default value is
                AXIS\_1.This parameter is available only if **traction** is GENERAL.

            localCsys=`abaqusConstants.GENERAL`[¶](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.localCsys "Permalink to this definition")
            :   A DatumCsys object specifying the local coordinate system of the load’s degrees of
                freedom. The default value is None, indicating that the degrees of freedom are defined
                in the global coordinate system or by the **userCsys** parameter if defined. This
                parameter is available only if **traction** is GENERAL. When this member is queried, it
                returns an Int.

            userCsys=`abaqusConstants.GENERAL`[¶](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.userCsys "Permalink to this definition")
            :   A String specifying a CSYS defined by a user-subroutine. The default value is None,
                indicating that the degrees of freedom are defined in the global coordinate system or by
                the **localCsys** parameter if defined. This parameter is available only if **traction** is
                GENERAL.

            directionVector=`()`[¶](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.directionVector "Permalink to this definition")
            :   A tuple of two points specifying the direction of the load. Each point is specified as a
                point region or a tuple of coordinates. If **traction** is SHEAR, then **directionVector**
                will be projected onto the region surface. This parameter is available only if
                **traction** is GENERAL.

            follower=`1`[¶](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.follower "Permalink to this definition")
            :   A Boolean specifying whether the direction of the force changes with rotation. The
                default value is ON. This parameter may be modified only if **traction** is GENERAL. You
                should provide the **follower** argument only if it is valid for the specified step.

            resultant=`0`[¶](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.resultant "Permalink to this definition")
            :   A Boolean specifying whether to maintain a constant resultant force by defining traction
                per unit undeformed area. If **resultant** is OFF, traction is defined per unit deformed
                area. The default value is OFF. You should provide the **resultant** argument only if it
                is valid for the specified step.

            traction=`abaqusConstants.NORMAL`[¶](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad.traction "Permalink to this definition")
            :   A SymbolicConstant specifying how to apply surface traction. Possible values are NORMAL,
                TRANSVERSE, SHEAR, MOMENT and GENERAL. The default value is NORMAL.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad-returns "Permalink to this headline")
        :   A ShellEdgeLoad object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad-return-type "Permalink to this headline")
        :   [`ShellEdgeLoad`](#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad "abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad (Python method) — This method creates a ShellEdgeLoad object.")

    SubmodelSB(*[name](#abaqus.Load.LoadModel.LoadModel.SubmodelSB.name "abaqus.Load.LoadModel.LoadModel.SubmodelSB.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.SubmodelSB.createStepName "abaqus.Load.LoadModel.LoadModel.SubmodelSB.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.SubmodelSB.region "abaqus.Load.LoadModel.LoadModel.SubmodelSB.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[globalStep](#abaqus.Load.LoadModel.LoadModel.SubmodelSB.globalStep "abaqus.Load.LoadModel.LoadModel.SubmodelSB.globalStep (Python parameter) — A String specifying the step in the global model from which Abaqus reads the values of the variables that will drive the submodel analysis.")*, *[globalDrivingRegion](#abaqus.Load.LoadModel.LoadModel.SubmodelSB.globalDrivingRegion "abaqus.Load.LoadModel.LoadModel.SubmodelSB.globalDrivingRegion (Python parameter) — A String specifying the element set in the global model that will be searched for elements whose responses will be used to drive the submodel.")=`''`*, *[absoluteExteriorTolerance](#abaqus.Load.LoadModel.LoadModel.SubmodelSB.absoluteExteriorTolerance "abaqus.Load.LoadModel.LoadModel.SubmodelSB.absoluteExteriorTolerance (Python parameter) — None or a Float specifying the absolute value by which a driven node of the submodel can lie outside the region of the elements of the global model.")=`None`*, *[exteriorTolerance](#abaqus.Load.LoadModel.LoadModel.SubmodelSB.exteriorTolerance "abaqus.Load.LoadModel.LoadModel.SubmodelSB.exteriorTolerance (Python parameter) — None or a Float specifying the fraction of the average element size in the global model by which a driven node of the submodel can lie outside the region of the elements of the global model.")=`0`*, *[globalIncrement](#abaqus.Load.LoadModel.LoadModel.SubmodelSB.globalIncrement "abaqus.Load.LoadModel.LoadModel.SubmodelSB.globalIncrement (Python parameter) — An Int specifying the increment number in the global model step from which the solution will be used to specify the values of the driven variables.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L1775-L1839)[¶](#abaqus.Load.LoadModel.LoadModel.SubmodelSB "Permalink to this definition")
    :   This method creates a SubmodelSB object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].SubmodelSB
        ```

        Note

        Check [SubmodelSB on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-submodelsbpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.SubmodelSB-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.SubmodelSB.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.SubmodelSB.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created.

            region[¶](#abaqus.Load.LoadModel.LoadModel.SubmodelSB.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            globalStep[¶](#abaqus.Load.LoadModel.LoadModel.SubmodelSB.globalStep "Permalink to this definition")
            :   A String specifying the step in the global model from which Abaqus reads the values of
                the variables that will drive the submodel analysis. The String indicates the position
                of the step in the sequence of analysis steps. For example, **globalStep** = ‘1’ indicates
                the first step.

            globalDrivingRegion=`''`[¶](#abaqus.Load.LoadModel.LoadModel.SubmodelSB.globalDrivingRegion "Permalink to this definition")
            :   A String specifying the element set in the global model that will be searched for
                elements whose responses will be used to drive the submodel. An empty string indicates
                that the entire global model will be searched. The default value is an empty string.

            absoluteExteriorTolerance=`None`[¶](#abaqus.Load.LoadModel.LoadModel.SubmodelSB.absoluteExteriorTolerance "Permalink to this definition")
            :   None or a Float specifying the absolute value by which a driven node of the submodel can
                lie outside the region of the elements of the global model. The default value is None.

            exteriorTolerance=`0`[¶](#abaqus.Load.LoadModel.LoadModel.SubmodelSB.exteriorTolerance "Permalink to this definition")
            :   None or a Float specifying the fraction of the average element size in the global model
                by which a driven node of the submodel can lie outside the region of the elements of the
                global model. The default value is 0.05.

            globalIncrement=`0`[¶](#abaqus.Load.LoadModel.LoadModel.SubmodelSB.globalIncrement "Permalink to this definition")
            :   An Int specifying the increment number in the global model step from which the solution
                will be used to specify the values of the driven variables. If **globalIncrement** = 0, the
                solution from the last increment will be used. The **globalIncrement** argument is
                applicable only for linear perturbation steps. The default value is 0.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.SubmodelSB-returns "Permalink to this headline")
        :   A SubmodelSB object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.SubmodelSB-return-type "Permalink to this headline")
        :   [`SubmodelSB`](#abaqus.Load.LoadModel.LoadModel.SubmodelSB "abaqus.Load.LoadModel.LoadModel.SubmodelSB (Python method) — This method creates a SubmodelSB object.")

    SubstructureLoad(*[name](#abaqus.Load.LoadModel.LoadModel.SubstructureLoad.name "abaqus.Load.LoadModel.LoadModel.SubstructureLoad.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.SubstructureLoad.createStepName "abaqus.Load.LoadModel.LoadModel.SubstructureLoad.createStepName (Python parameter) — A String specifying the name of the step in which the substructure load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.SubstructureLoad.region "abaqus.Load.LoadModel.LoadModel.SubstructureLoad.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[loadCaseNames](#abaqus.Load.LoadModel.LoadModel.SubstructureLoad.loadCaseNames "abaqus.Load.LoadModel.LoadModel.SubstructureLoad.loadCaseNames (Python parameter) — A list of names of the load cases that should be activated by this substructure load.")*, *[magnitude](#abaqus.Load.LoadModel.LoadModel.SubstructureLoad.magnitude "abaqus.Load.LoadModel.LoadModel.SubstructureLoad.magnitude (Python parameter) — A Float specifying the multiplier for the load case magnitude.")*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.SubstructureLoad.amplitude "abaqus.Load.LoadModel.LoadModel.SubstructureLoad.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L1841-L1881)[¶](#abaqus.Load.LoadModel.LoadModel.SubstructureLoad "Permalink to this definition")
    :   This method creates a SubstructureLoad object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].SubstructureLoad
        ```

        Note

        Check [SubstructureLoad on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-substructureloadpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.SubstructureLoad-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.SubstructureLoad.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.SubstructureLoad.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the substructure load is created.

            region[¶](#abaqus.Load.LoadModel.LoadModel.SubstructureLoad.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            loadCaseNames[¶](#abaqus.Load.LoadModel.LoadModel.SubstructureLoad.loadCaseNames "Permalink to this definition")
            :   A list of names of the load cases that should be activated by this substructure load.

            magnitude[¶](#abaqus.Load.LoadModel.LoadModel.SubstructureLoad.magnitude "Permalink to this definition")
            :   A Float specifying the multiplier for the load case magnitude.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.SubstructureLoad.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.SubstructureLoad-returns "Permalink to this headline")
        :   A SubstructureLoad object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.SubstructureLoad-return-type "Permalink to this headline")
        :   [`SubstructureLoad`](#abaqus.Load.LoadModel.LoadModel.SubstructureLoad "abaqus.Load.LoadModel.LoadModel.SubstructureLoad (Python method) — This method creates a SubstructureLoad object.")

    SurfaceCharge(*[name](#abaqus.Load.LoadModel.LoadModel.SurfaceCharge.name "abaqus.Load.LoadModel.LoadModel.SurfaceCharge.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.SurfaceCharge.createStepName "abaqus.Load.LoadModel.LoadModel.SurfaceCharge.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.SurfaceCharge.region "abaqus.Load.LoadModel.LoadModel.SurfaceCharge.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[magnitude](#abaqus.Load.LoadModel.LoadModel.SurfaceCharge.magnitude "abaqus.Load.LoadModel.LoadModel.SurfaceCharge.magnitude (Python parameter) — A Float specifying the load magnitude.")*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.SurfaceCharge.distributionType "abaqus.Load.LoadModel.LoadModel.SurfaceCharge.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.LoadModel.SurfaceCharge.field "abaqus.Load.LoadModel.LoadModel.SurfaceCharge.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.SurfaceCharge.amplitude "abaqus.Load.LoadModel.LoadModel.SurfaceCharge.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L1883-L1932)[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCharge "Permalink to this definition")
    :   This method creates a SurfaceCharge object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].SurfaceCharge
        ```

        Note

        Check [SurfaceCharge on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacechargepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCharge-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCharge.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCharge.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created. This must be the
                first analysis step name.

            region[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCharge.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            magnitude[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCharge.magnitude "Permalink to this definition")
            :   A Float specifying the load magnitude.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCharge.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCharge.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCharge.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCharge-returns "Permalink to this headline")
        :   A SurfaceCharge object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCharge-return-type "Permalink to this headline")
        :   [`SurfaceCharge`](#abaqus.Load.LoadModel.LoadModel.SurfaceCharge "abaqus.Load.LoadModel.LoadModel.SurfaceCharge (Python method) — This method creates a SurfaceCharge object.")

    SurfaceConcentrationFlux(*[name](#abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux.name "abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux.createStepName "abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux.region "abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[magnitude](#abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux.magnitude "abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux.magnitude (Python parameter) — A Float specifying the surface concentration flux magnitude.")*, *[field](#abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux.field "abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux.distributionType "abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux.distributionType (Python parameter) — A SymbolicConstant specifying how the surface concentration flux is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux.amplitude "abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L1934-L1984)[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux "Permalink to this definition")
    :   This method creates a SurfaceConcentrationFlux object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].SurfaceConcentrationFlux
        ```

        Note

        Check [SurfaceConcentrationFlux on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfaceconcentrationfluxpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created.

            region[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            magnitude[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux.magnitude "Permalink to this definition")
            :   A Float specifying the surface concentration flux magnitude. **magnitude** is optional if
                **distributionType** = USER\_DEFINED.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the surface concentration flux is distributed
                spatially. Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is
                UNIFORM.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux-returns "Permalink to this headline")
        :   A SurfaceConcentrationFlux object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux-return-type "Permalink to this headline")
        :   [`SurfaceConcentrationFlux`](#abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux "abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux (Python method) — This method creates a SurfaceConcentrationFlux object.")

    SurfaceCurrent(*[name](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrent.name "abaqus.Load.LoadModel.LoadModel.SurfaceCurrent.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrent.createStepName "abaqus.Load.LoadModel.LoadModel.SurfaceCurrent.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrent.region "abaqus.Load.LoadModel.LoadModel.SurfaceCurrent.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[magnitude](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrent.magnitude "abaqus.Load.LoadModel.LoadModel.SurfaceCurrent.magnitude (Python parameter) — A Float specifying the load magnitude.")*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrent.distributionType "abaqus.Load.LoadModel.LoadModel.SurfaceCurrent.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrent.field "abaqus.Load.LoadModel.LoadModel.SurfaceCurrent.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrent.amplitude "abaqus.Load.LoadModel.LoadModel.SurfaceCurrent.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L1986-L2035)[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrent "Permalink to this definition")
    :   This method creates a SurfaceCurrent object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].SurfaceCurrent
        ```

        Note

        Check [SurfaceCurrent on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacecurrentpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrent-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrent.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrent.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created. This must be the
                first analysis step name.

            region[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrent.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            magnitude[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrent.magnitude "Permalink to this definition")
            :   A Float specifying the load magnitude.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrent.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrent.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrent.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrent-returns "Permalink to this headline")
        :   A SurfaceCurrent object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrent-return-type "Permalink to this headline")
        :   [`SurfaceCurrent`](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrent "abaqus.Load.LoadModel.LoadModel.SurfaceCurrent (Python method) — This method creates a SurfaceCurrent object.")

    SurfaceCurrentDensity(*[name](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity.name "abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity.createStepName "abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity.region "abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[comp1](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity.comp1 "abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity.comp1 (Python parameter) — A Complex specifying the first component of the load.")*, *[comp2](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity.comp2 "abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity.comp2 (Python parameter) — A Complex specifying the second component of the load.")*, *[comp3](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity.comp3 "abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity.comp3 (Python parameter) — A Complex specifying the third component of the load.")*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity.distributionType "abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity.amplitude "abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L2037-L2094)[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity "Permalink to this definition")
    :   This method creates a SurfaceCurrentDensity object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].SurfaceCurrentDensity
        ```

        Note

        Check [SurfaceCurrentDensity on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacecurrentdensitypyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created. This must be the
                first analysis step name.

            region[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            comp1[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity.comp1 "Permalink to this definition")
            :   A Complex specifying the first component of the load.

            comp2[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity.comp2 "Permalink to this definition")
            :   A Complex specifying the second component of the load.

            comp3[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity.comp3 "Permalink to this definition")
            :   A Complex specifying the third component of the load.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and USER\_DEFINED. The default value is UNIFORM.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity-returns "Permalink to this headline")
        :   A SurfaceCurrentDensity object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity-return-type "Permalink to this headline")
        :   [`SurfaceCurrentDensity`](#abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity "abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity (Python method) — This method creates a SurfaceCurrentDensity object.")

    SurfaceHeatFlux(*[name](#abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux.name "abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux.createStepName "abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux.region "abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[magnitude](#abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux.magnitude "abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux.magnitude (Python parameter) — A Float specifying the surface heat flux magnitude.")*, *[field](#abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux.field "abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux.distributionType "abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux.distributionType (Python parameter) — A SymbolicConstant specifying how the surface heat flux is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD.")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux.amplitude "abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L2096-L2145)[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux "Permalink to this definition")
    :   This method creates a SurfaceHeatFlux object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].SurfaceHeatFlux
        ```

        Note

        Check [SurfaceHeatFlux on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfaceheatfluxpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created.

            region[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            magnitude[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux.magnitude "Permalink to this definition")
            :   A Float specifying the surface heat flux magnitude. **magnitude** is optional if
                **distributionType** = USER\_DEFINED.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the surface heat flux is distributed spatially.
                Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux-returns "Permalink to this headline")
        :   A SurfaceHeatFlux object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux-return-type "Permalink to this headline")
        :   [`SurfaceHeatFlux`](#abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux "abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux (Python method) — This method creates a SurfaceHeatFlux object.")

    SurfacePoreFluid(*[name](#abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid.name "abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid.createStepName "abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid.region "abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[magnitude](#abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid.magnitude "abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid.magnitude (Python parameter) — A Float specifying the surface pore fluid flow magnitude.")*, *[field](#abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid.field "abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid.distributionType "abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid.distributionType (Python parameter) — A SymbolicConstant specifying whether the load is uniform.")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid.amplitude "abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L2147-L2196)[¶](#abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid "Permalink to this definition")
    :   This method creates a SurfacePoreFluid object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].SurfacePoreFluid
        ```

        Note

        Check [SurfacePoreFluid on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfaceporefluidpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created.

            region[¶](#abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            magnitude[¶](#abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid.magnitude "Permalink to this definition")
            :   A Float specifying the surface pore fluid flow magnitude. **magnitude** is optional if
                **distributionType** = USER\_DEFINED.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM,
                USER\_DEFINED, and FIELD. The default value is UNIFORM.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid-returns "Permalink to this headline")
        :   A SurfacePoreFluid object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid-return-type "Permalink to this headline")
        :   [`SurfacePoreFluid`](#abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid "abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid (Python method) — This method creates a SurfacePoreFluid object.")

    SurfaceTraction(*[name](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.name "abaqus.Load.LoadModel.LoadModel.SurfaceTraction.name (Python parameter) — A String specifying the load repository key.")*, *[createStepName](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.createStepName "abaqus.Load.LoadModel.LoadModel.SurfaceTraction.createStepName (Python parameter) — A String specifying the name of the step in which the load is created.")*, *[region](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.region "abaqus.Load.LoadModel.LoadModel.SurfaceTraction.region (Python parameter) — A Region object specifying the region to which the load is applied.")*, *[magnitude](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.magnitude "abaqus.Load.LoadModel.LoadModel.SurfaceTraction.magnitude (Python parameter) — A Float or Complex specifying the load magnitude.")*, *[distributionType](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.distributionType "abaqus.Load.LoadModel.LoadModel.SurfaceTraction.distributionType (Python parameter) — A SymbolicConstant specifying how the surface traction is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.field "abaqus.Load.LoadModel.LoadModel.SurfaceTraction.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[amplitude](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.amplitude "abaqus.Load.LoadModel.LoadModel.SurfaceTraction.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*, *[angle](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.angle "abaqus.Load.LoadModel.LoadModel.SurfaceTraction.angle (Python parameter) — A Float specifying an additional rotation of directionVector about an axis.")=`0`*, *[axis](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.axis "abaqus.Load.LoadModel.LoadModel.SurfaceTraction.axis (Python parameter) — A SymbolicConstant specifying the axis about which to apply an additional rotation of directionVector.")=`abaqusConstants.AXIS_1`*, *[localCsys](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.localCsys "abaqus.Load.LoadModel.LoadModel.SurfaceTraction.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the load's degrees of freedom.")=`None`*, *[userCsys](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.userCsys "abaqus.Load.LoadModel.LoadModel.SurfaceTraction.userCsys (Python parameter) — A String specifying a CSYS defined by a user-subroutine.")=`''`*, *[directionVector](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.directionVector "abaqus.Load.LoadModel.LoadModel.SurfaceTraction.directionVector (Python parameter) — A VertexArray object of length 2 specifying the direction of the load.")=`()`*, *[follower](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.follower "abaqus.Load.LoadModel.LoadModel.SurfaceTraction.follower (Python parameter) — A Boolean specifying whether the direction of the force changes with rotation.")=`1`*, *[resultant](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.resultant "abaqus.Load.LoadModel.LoadModel.SurfaceTraction.resultant (Python parameter) — A Boolean specifying whether the to maintain a constant resultant force by defining traction per unit undeformed area.")=`0`*, *[traction](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.traction "abaqus.Load.LoadModel.LoadModel.SurfaceTraction.traction (Python parameter) — A SymbolicConstant specifying how to apply surface traction.")=`abaqusConstants.SHEAR`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L2198-L2302)[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction "Permalink to this definition")
    :   This method creates a SurfaceTraction object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].SurfaceTraction
        ```

        Note

        Check [SurfaceTraction on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacetractionpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.name "Permalink to this definition")
            :   A String specifying the load repository key.

            createStepName[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is created.

            region[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            magnitude[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.magnitude "Permalink to this definition")
            :   A Float or Complex specifying the load magnitude. **magnitude** is optional if
                **distributionType** = USER\_DEFINED.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the surface traction is distributed spatially.
                Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

            angle=`0`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.angle "Permalink to this definition")
            :   A Float specifying an additional rotation of **directionVector** about an axis. The
                default value is 0.0.

            axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the axis about which to apply an additional rotation of
                **directionVector**. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default value is
                AXIS\_1.

            localCsys=`None`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the load’s degrees
                of freedom. If **localCsys** = None, the degrees of freedom are defined in the global
                coordinate system or by the **userCsys** parameter if defined. When this member is
                queried, it returns an Int. The default value is None.

            userCsys=`''`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.userCsys "Permalink to this definition")
            :   A String specifying a CSYS defined by a user-subroutine. If **userCsys** = None, the degrees
                of freedom are defined in the global coordinate system or by the **localCsys** parameter
                if defined. The default value is “None”.

            directionVector=`()`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.directionVector "Permalink to this definition")
            :   A VertexArray object of length 2 specifying the direction of the load. Instead of
                through a ConstrainedSketchVertex, each point may be specified through a tuple of coordinates. If
                **traction** is SHEAR, then **directionVector** will be projected onto the region surface.
                This parameter is available only if **traction** is GENERAL or SHEAR.

            follower=`1`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.follower "Permalink to this definition")
            :   A Boolean specifying whether the direction of the force changes with rotation. The
                default value is ON.This parameter may be modified only if **traction** is GENERAL. You
                should provide the **follower** argument only if it is valid for the specified step.

            resultant=`0`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.resultant "Permalink to this definition")
            :   A Boolean specifying whether the to maintain a constant resultant force by defining
                traction per unit undeformed area. If **resultant** is OFF, traction is defined per unit
                deformed area. The default value is OFF.You should provide the **resultant** argument only
                if it is valid for the specified step.

            traction=`abaqusConstants.SHEAR`[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction.traction "Permalink to this definition")
            :   A SymbolicConstant specifying how to apply surface traction. Possible values are SHEAR
                and GENERAL. The default value is SHEAR.

        Returns:[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction-returns "Permalink to this headline")
        :   A SurfaceTraction object.

        Return type:[¶](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction-return-type "Permalink to this headline")
        :   [`SurfaceTraction`](#abaqus.Load.LoadModel.LoadModel.SurfaceTraction "abaqus.Load.LoadModel.LoadModel.SurfaceTraction (Python method) — This method creates a SurfaceTraction object.")

### Other Classes[¶](#other-classes "Permalink to this heading")

*class* BodyCharge(*[name](#abaqus.Load.LoadModel.BodyCharge "abaqus.Load.LoadModel.BodyCharge.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.LoadModel.BodyCharge "abaqus.Load.LoadModel.BodyCharge.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.LoadModel.BodyCharge "abaqus.Load.LoadModel.BodyCharge.__init__.region (Python parameter)")*, *[magnitude](#abaqus.Load.LoadModel.BodyCharge "abaqus.Load.LoadModel.BodyCharge.__init__.magnitude (Python parameter)")*, *[amplitude](#abaqus.Load.LoadModel.BodyCharge "abaqus.Load.LoadModel.BodyCharge.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.Load.LoadModel.BodyCharge "abaqus.Load.LoadModel.BodyCharge.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.BodyCharge "abaqus.Load.LoadModel.BodyCharge.__init__.field (Python parameter)")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L13-L130)[¶](#abaqus.Load.LoadModel.BodyCharge "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The BodyCharge object stores the data for a body charge. The BodyCharge object is derived from the Load
    object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [BodyCharge on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodychargepyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L28-L30)[¶](#abaqus.Load.LoadModel.BodyCharge.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
        UNIFORM and FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L32-L35)[¶](#abaqus.Load.LoadModel.BodyCharge.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L25-L26)[¶](#abaqus.Load.LoadModel.BodyCharge.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L37-L38)[¶](#abaqus.Load.LoadModel.BodyCharge.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[amplitude](#abaqus.Load.LoadModel.BodyCharge.setValues.amplitude "abaqus.Load.LoadModel.BodyCharge.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.Load.LoadModel.BodyCharge.setValues.distributionType "abaqus.Load.LoadModel.BodyCharge.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.BodyCharge.setValues.field "abaqus.Load.LoadModel.BodyCharge.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L88-L111)[¶](#abaqus.Load.LoadModel.BodyCharge.setValues "Permalink to this definition")
    :   This method modifies the data for an existing BodyCharge object in the step where it is created.

        Note

        Check [BodyCharge.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodychargepyc.htm?contextscope=all#simaker-bodychargesetvaluespyc).

        Parameters:[¶](#abaqus.Load.LoadModel.BodyCharge.setValues-parameters "Permalink to this headline")
        :   amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.BodyCharge.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.BodyCharge.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.BodyCharge.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

    setValuesInStep(*[stepName](#abaqus.Load.LoadModel.BodyCharge.setValuesInStep.stepName "abaqus.Load.LoadModel.BodyCharge.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[magnitude](#abaqus.Load.LoadModel.BodyCharge.setValuesInStep.magnitude "abaqus.Load.LoadModel.BodyCharge.setValuesInStep.magnitude (Python parameter) — A Float specifying the load magnitude.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.BodyCharge.setValuesInStep.amplitude "abaqus.Load.LoadModel.BodyCharge.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L113-L130)[¶](#abaqus.Load.LoadModel.BodyCharge.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing BodyCharge object in the specified step.

        Note

        Check [BodyCharge.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodychargepyc.htm?contextscope=all#simaker-bodychargesetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.LoadModel.BodyCharge.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.LoadModel.BodyCharge.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            magnitude=`None`[¶](#abaqus.Load.LoadModel.BodyCharge.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float specifying the load magnitude.

            amplitude=`''`[¶](#abaqus.Load.LoadModel.BodyCharge.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous static analysis step. FREED should be used if
                the load is changed to have no amplitude reference. You should provide the **amplitude**
                argument only if it is valid for the specified step.

*class* Load[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTraction.py#L8-L81)[¶](#abaqus.Load.SurfaceTraction.Load "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The Load object is the abstract base type for other Load objects. The Load object has no explicit
    constructor. The methods and members of the Load object are common to all objects derived from Load.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [Load on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadpyc.htm?contextscope=all).

    Member Details:

    deactivate(*[stepName](#abaqus.Load.SurfaceTraction.Load.deactivate.stepName "abaqus.Load.SurfaceTraction.Load.deactivate.stepName (Python parameter) — A String specifying the name of the step in which the load is deactivated.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTraction.py#L26-L35)[¶](#abaqus.Load.SurfaceTraction.Load.deactivate "Permalink to this definition")
    :   This method deactivates the load in the specified step and all its subsequent steps.

        Note

        Check [Load.deactivate on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadpyc.htm?contextscope=all#simaker-loaddeactivatepyc).

        Parameters:[¶](#abaqus.Load.SurfaceTraction.Load.deactivate-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.SurfaceTraction.Load.deactivate.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is deactivated.

    delete(*[indices](#abaqus.Load.SurfaceTraction.Load.delete.indices "abaqus.Load.SurfaceTraction.Load.delete.indices (Python parameter) — A sequence of Ints specifying the index of each load to delete.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTraction.py#L72-L81)[¶](#abaqus.Load.SurfaceTraction.Load.delete "Permalink to this definition")
    :   This method allows you to delete existing loads.

        Note

        Check [Load.delete on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadpyc.htm?contextscope=all#simaker-loaddeletepyc).

        Parameters:[¶](#abaqus.Load.SurfaceTraction.Load.delete-parameters "Permalink to this headline")
        :   indices[¶](#abaqus.Load.SurfaceTraction.Load.delete.indices "Permalink to this definition")
            :   A sequence of Ints specifying the index of each load to delete.

    move(*[fromStepName](#abaqus.Load.SurfaceTraction.Load.move.fromStepName "abaqus.Load.SurfaceTraction.Load.move.fromStepName (Python parameter) — A String specifying the name of the step from which the load state is moved.")*, *[toStepName](#abaqus.Load.SurfaceTraction.Load.move.toStepName "abaqus.Load.SurfaceTraction.Load.move.toStepName (Python parameter) — A String specifying the name of the step to which the load state is moved.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTraction.py#L37-L48)[¶](#abaqus.Load.SurfaceTraction.Load.move "Permalink to this definition")
    :   This method moves the load state object from one step to a different step.

        Note

        Check [Load.move on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadpyc.htm?contextscope=all#simaker-loadmovepyc).

        Parameters:[¶](#abaqus.Load.SurfaceTraction.Load.move-parameters "Permalink to this headline")
        :   fromStepName[¶](#abaqus.Load.SurfaceTraction.Load.move.fromStepName "Permalink to this definition")
            :   A String specifying the name of the step from which the load state is moved.

            toStepName[¶](#abaqus.Load.SurfaceTraction.Load.move.toStepName "Permalink to this definition")
            :   A String specifying the name of the step to which the load state is moved.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTraction.py#L20-L21)[¶](#abaqus.Load.SurfaceTraction.Load.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTraction.py#L23-L24)[¶](#abaqus.Load.SurfaceTraction.Load.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    reset(*[stepName](#abaqus.Load.SurfaceTraction.Load.reset.stepName "abaqus.Load.SurfaceTraction.Load.reset.stepName (Python parameter) — A String specifying the name of the step in which the load state is reset.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTraction.py#L50-L60)[¶](#abaqus.Load.SurfaceTraction.Load.reset "Permalink to this definition")
    :   This method resets the load state of the specified step to the state of the previous general analysis
        step.

        Note

        Check [Load.reset on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadpyc.htm?contextscope=all#simaker-loadresetpyc).

        Parameters:[¶](#abaqus.Load.SurfaceTraction.Load.reset-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.SurfaceTraction.Load.reset.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load state is reset.

    resume()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTraction.py#L62-L65)[¶](#abaqus.Load.SurfaceTraction.Load.resume "Permalink to this definition")
    :   This method resumes the load that was previously suppressed.

    suppress()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTraction.py#L67-L70)[¶](#abaqus.Load.SurfaceTraction.Load.suppress "Permalink to this definition")
    :   This method suppresses the load.

*class* BodyChargeState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyChargeState.py#L9-L54)[¶](#abaqus.Load.BodyChargeState.BodyChargeState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The BodyChargeState object stores the propagating data of a body charge in a step. One instance of this
    object is created internally by the BodyCharge object for each step. The instance is also deleted internally
    by the BodyCharge object. The BodyChargeState object has no constructor or methods. The BodyChargeState
    object is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * DECHARGE

    Note

    Check [BodyChargeState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodychargestatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyChargeState.py#L9-L54)[¶](#abaqus.Load.BodyChargeState.BodyChargeState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyChargeState.py)[¶](#abaqus.Load.BodyChargeState.BodyChargeState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyChargeState.py#L27-L28)[¶](#abaqus.Load.BodyChargeState.BodyChargeState.magnitude "Permalink to this definition")
    :   A Float specifying the load magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyChargeState.py)[¶](#abaqus.Load.BodyChargeState.BodyChargeState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load magnitude. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyChargeState.py)[¶](#abaqus.Load.BodyChargeState.BodyChargeState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* LoadState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTractionState.py#L8-L41)[¶](#abaqus.Load.SurfaceTractionState.LoadState "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The LoadState object is the abstract base type for other LoadState objects. The LoadState object has no
    explicit constructor or methods. The members of the LoadState object are common to all objects derived from
    LoadState.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    Note

    Check [LoadState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTractionState.py#L8-L41)[¶](#abaqus.Load.SurfaceTractionState.LoadState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTractionState.py)[¶](#abaqus.Load.SurfaceTractionState.LoadState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTractionState.py)[¶](#abaqus.Load.SurfaceTractionState.LoadState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* BodyConcentrationFlux(*[name](#abaqus.Load.LoadModel.BodyConcentrationFlux "abaqus.Load.LoadModel.BodyConcentrationFlux.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.LoadModel.BodyConcentrationFlux "abaqus.Load.LoadModel.BodyConcentrationFlux.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.LoadModel.BodyConcentrationFlux "abaqus.Load.LoadModel.BodyConcentrationFlux.__init__.region (Python parameter)")*, *[magnitude](#abaqus.Load.LoadModel.BodyConcentrationFlux "abaqus.Load.LoadModel.BodyConcentrationFlux.__init__.magnitude (Python parameter)")*, *[field](#abaqus.Load.LoadModel.BodyConcentrationFlux "abaqus.Load.LoadModel.BodyConcentrationFlux.__init__.field (Python parameter)")=`''`*, *[distributionType](#abaqus.Load.LoadModel.BodyConcentrationFlux "abaqus.Load.LoadModel.BodyConcentrationFlux.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.Load.LoadModel.BodyConcentrationFlux "abaqus.Load.LoadModel.BodyConcentrationFlux.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L13-L132)[¶](#abaqus.Load.LoadModel.BodyConcentrationFlux "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The BodyConcentrationFlux object defines body concentration flux from a region or into a region. The
    BodyConcentrationFlux object is derived from the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [BodyConcentrationFlux on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodyconcentrationfluxpyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L28-L30)[¶](#abaqus.Load.LoadModel.BodyConcentrationFlux.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the body concentration flux is distributed spatially.
        Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L32-L35)[¶](#abaqus.Load.LoadModel.BodyConcentrationFlux.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L25-L26)[¶](#abaqus.Load.LoadModel.BodyConcentrationFlux.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L37-L38)[¶](#abaqus.Load.LoadModel.BodyConcentrationFlux.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[field](#abaqus.Load.LoadModel.BodyConcentrationFlux.setValues.field "abaqus.Load.LoadModel.BodyConcentrationFlux.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[distributionType](#abaqus.Load.LoadModel.BodyConcentrationFlux.setValues.distributionType "abaqus.Load.LoadModel.BodyConcentrationFlux.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the body concentration flux is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD.")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.Load.LoadModel.BodyConcentrationFlux.setValues.amplitude "abaqus.Load.LoadModel.BodyConcentrationFlux.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L88-L112)[¶](#abaqus.Load.LoadModel.BodyConcentrationFlux.setValues "Permalink to this definition")
    :   This method modifies the data for an existing BodyConcentrationFlux object in the step where it is
        created.

        Note

        Check [BodyConcentrationFlux.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodyconcentrationfluxpyc.htm?contextscope=all#simaker-bodyconcentrationfluxsetvaluespyc).

        Parameters:[¶](#abaqus.Load.LoadModel.BodyConcentrationFlux.setValues-parameters "Permalink to this headline")
        :   field=`''`[¶](#abaqus.Load.LoadModel.BodyConcentrationFlux.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.BodyConcentrationFlux.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the body concentration flux is distributed spatially.
                Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.BodyConcentrationFlux.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

    setValuesInStep(*[stepName](#abaqus.Load.LoadModel.BodyConcentrationFlux.setValuesInStep.stepName "abaqus.Load.LoadModel.BodyConcentrationFlux.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the Body heat flux is modified.")*, *[magnitude](#abaqus.Load.LoadModel.BodyConcentrationFlux.setValuesInStep.magnitude "abaqus.Load.LoadModel.BodyConcentrationFlux.setValuesInStep.magnitude (Python parameter) — A Float specifying the Body concentration flux magnitude.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.BodyConcentrationFlux.setValuesInStep.amplitude "abaqus.Load.LoadModel.BodyConcentrationFlux.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L114-L132)[¶](#abaqus.Load.LoadModel.BodyConcentrationFlux.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing BodyConcentrationFlux object in the
        specified step.

        Note

        Check [BodyConcentrationFlux.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodyconcentrationfluxpyc.htm?contextscope=all#simaker-bodyconcentrationfluxsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.LoadModel.BodyConcentrationFlux.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.LoadModel.BodyConcentrationFlux.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the Body heat flux is modified.

            magnitude=`None`[¶](#abaqus.Load.LoadModel.BodyConcentrationFlux.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float specifying the Body concentration flux magnitude.

            amplitude=`''`[¶](#abaqus.Load.LoadModel.BodyConcentrationFlux.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                load has no amplitude reference. You should provide the **amplitude** argument only if it
                is valid for the specified step.

*class* BodyConcentrationFluxState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyConcentrationFluxState.py#L9-L55)[¶](#abaqus.Load.BodyConcentrationFluxState.BodyConcentrationFluxState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The BodyConcentrationFluxState object stores the propagating data for a BodyConcentrationFlux object in a
    step. One instance of this object is created internally by the BodyConcentrationFlux object for each step.
    The instance is also deleted internally by the BodyConcentrationFlux object. The BodyConcentrationFluxState
    object has no constructor or methods. The BodyConcentrationFluxState object is derived from the LoadState
    object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * CFLUX

    Note

    Check [BodyConcentrationFluxState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodyconcentrationfluxstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyConcentrationFluxState.py#L9-L55)[¶](#abaqus.Load.BodyConcentrationFluxState.BodyConcentrationFluxState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyConcentrationFluxState.py)[¶](#abaqus.Load.BodyConcentrationFluxState.BodyConcentrationFluxState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyConcentrationFluxState.py#L28-L29)[¶](#abaqus.Load.BodyConcentrationFluxState.BodyConcentrationFluxState.magnitude "Permalink to this definition")
    :   A Float specifying the body concentration flux magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyConcentrationFluxState.py)[¶](#abaqus.Load.BodyConcentrationFluxState.BodyConcentrationFluxState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the body concentration flux
        magnitude. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyConcentrationFluxState.py)[¶](#abaqus.Load.BodyConcentrationFluxState.BodyConcentrationFluxState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* BodyCurrent(*[name](#abaqus.Load.LoadModel.BodyCurrent "abaqus.Load.LoadModel.BodyCurrent.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.LoadModel.BodyCurrent "abaqus.Load.LoadModel.BodyCurrent.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.LoadModel.BodyCurrent "abaqus.Load.LoadModel.BodyCurrent.__init__.region (Python parameter)")*, *[magnitude](#abaqus.Load.LoadModel.BodyCurrent "abaqus.Load.LoadModel.BodyCurrent.__init__.magnitude (Python parameter)")*, *[amplitude](#abaqus.Load.LoadModel.BodyCurrent "abaqus.Load.LoadModel.BodyCurrent.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.Load.LoadModel.BodyCurrent "abaqus.Load.LoadModel.BodyCurrent.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.BodyCurrent "abaqus.Load.LoadModel.BodyCurrent.__init__.field (Python parameter)")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L13-L130)[¶](#abaqus.Load.LoadModel.BodyCurrent "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The BodyCurrent object stores the data for a body current. The BodyCurrent object is derived from the
    Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [BodyCurrent on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodycurrentpyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L28-L30)[¶](#abaqus.Load.LoadModel.BodyCurrent.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
        UNIFORM and FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L32-L35)[¶](#abaqus.Load.LoadModel.BodyCurrent.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L25-L26)[¶](#abaqus.Load.LoadModel.BodyCurrent.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L37-L38)[¶](#abaqus.Load.LoadModel.BodyCurrent.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[amplitude](#abaqus.Load.LoadModel.BodyCurrent.setValues.amplitude "abaqus.Load.LoadModel.BodyCurrent.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.Load.LoadModel.BodyCurrent.setValues.distributionType "abaqus.Load.LoadModel.BodyCurrent.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.BodyCurrent.setValues.field "abaqus.Load.LoadModel.BodyCurrent.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L88-L111)[¶](#abaqus.Load.LoadModel.BodyCurrent.setValues "Permalink to this definition")
    :   This method modifies the data for an existing BodyCurrent object in the step where it is created.

        Note

        Check [BodyCurrent.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodycurrentpyc.htm?contextscope=all#simaker-bodycurrentsetvaluespyc).

        Parameters:[¶](#abaqus.Load.LoadModel.BodyCurrent.setValues-parameters "Permalink to this headline")
        :   amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.BodyCurrent.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.BodyCurrent.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.BodyCurrent.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

    setValuesInStep(*[stepName](#abaqus.Load.LoadModel.BodyCurrent.setValuesInStep.stepName "abaqus.Load.LoadModel.BodyCurrent.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[magnitude](#abaqus.Load.LoadModel.BodyCurrent.setValuesInStep.magnitude "abaqus.Load.LoadModel.BodyCurrent.setValuesInStep.magnitude (Python parameter) — A Float specifying the load magnitude.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.BodyCurrent.setValuesInStep.amplitude "abaqus.Load.LoadModel.BodyCurrent.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L113-L130)[¶](#abaqus.Load.LoadModel.BodyCurrent.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing BodyCurrent object in the specified step.

        Note

        Check [BodyCurrent.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodycurrentpyc.htm?contextscope=all#simaker-bodycurrentsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.LoadModel.BodyCurrent.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.LoadModel.BodyCurrent.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            magnitude=`None`[¶](#abaqus.Load.LoadModel.BodyCurrent.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float specifying the load magnitude.

            amplitude=`''`[¶](#abaqus.Load.LoadModel.BodyCurrent.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous static analysis step. FREED should be used if
                the load is changed to have no amplitude reference. You should provide the **amplitude**
                argument only if it is valid for the specified step.

*class* BodyCurrentDensity(*[name](#abaqus.Load.LoadModel.BodyCurrentDensity "abaqus.Load.LoadModel.BodyCurrentDensity.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.LoadModel.BodyCurrentDensity "abaqus.Load.LoadModel.BodyCurrentDensity.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.LoadModel.BodyCurrentDensity "abaqus.Load.LoadModel.BodyCurrentDensity.__init__.region (Python parameter)")*, *[comp1](#abaqus.Load.LoadModel.BodyCurrentDensity "abaqus.Load.LoadModel.BodyCurrentDensity.__init__.comp1 (Python parameter)")*, *[comp2](#abaqus.Load.LoadModel.BodyCurrentDensity "abaqus.Load.LoadModel.BodyCurrentDensity.__init__.comp2 (Python parameter)")*, *[comp3](#abaqus.Load.LoadModel.BodyCurrentDensity "abaqus.Load.LoadModel.BodyCurrentDensity.__init__.comp3 (Python parameter)")*, *[amplitude](#abaqus.Load.LoadModel.BodyCurrentDensity "abaqus.Load.LoadModel.BodyCurrentDensity.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.Load.LoadModel.BodyCurrentDensity "abaqus.Load.LoadModel.BodyCurrentDensity.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L13-L130)[¶](#abaqus.Load.LoadModel.BodyCurrentDensity "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The BodyCurrentDensity object stores the data for a body current. The BodyCurrentDensity object is
    derived from the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [BodyCurrentDensity on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodycurrentdensitypyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L28-L30)[¶](#abaqus.Load.LoadModel.BodyCurrentDensity.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
        UNIFORM and USER\_DEFINED. The default value is UNIFORM.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L25-L26)[¶](#abaqus.Load.LoadModel.BodyCurrentDensity.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L32-L33)[¶](#abaqus.Load.LoadModel.BodyCurrentDensity.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[amplitude](#abaqus.Load.LoadModel.BodyCurrentDensity.setValues.amplitude "abaqus.Load.LoadModel.BodyCurrentDensity.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.Load.LoadModel.BodyCurrentDensity.setValues.distributionType "abaqus.Load.LoadModel.BodyCurrentDensity.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L84-L99)[¶](#abaqus.Load.LoadModel.BodyCurrentDensity.setValues "Permalink to this definition")
    :   This method modifies the data for an existing BodyCurrentDensity object in the step where it is
        created.

        Note

        Check [BodyCurrentDensity.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodycurrentdensitypyc.htm?contextscope=all#simaker-bodycurrentdensitysetvaluespyc).

        Parameters:[¶](#abaqus.Load.LoadModel.BodyCurrentDensity.setValues-parameters "Permalink to this headline")
        :   amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.BodyCurrentDensity.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.BodyCurrentDensity.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and USER\_DEFINED. The default value is UNIFORM.

    setValuesInStep(*[stepName](#abaqus.Load.LoadModel.BodyCurrentDensity.setValuesInStep.stepName "abaqus.Load.LoadModel.BodyCurrentDensity.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[comp1](#abaqus.Load.LoadModel.BodyCurrentDensity.setValuesInStep.comp1 "abaqus.Load.LoadModel.BodyCurrentDensity.setValuesInStep.comp1 (Python parameter) — A Complex specifying the first component of the load.")=`''`*, *[comp2](#abaqus.Load.LoadModel.BodyCurrentDensity.setValuesInStep.comp2 "abaqus.Load.LoadModel.BodyCurrentDensity.setValuesInStep.comp2 (Python parameter) — A Complex specifying the second component of the load.")=`''`*, *[comp3](#abaqus.Load.LoadModel.BodyCurrentDensity.setValuesInStep.comp3 "abaqus.Load.LoadModel.BodyCurrentDensity.setValuesInStep.comp3 (Python parameter) — A Complex specifying the third component of the load.")=`''`*, *[amplitude](#abaqus.Load.LoadModel.BodyCurrentDensity.setValuesInStep.amplitude "abaqus.Load.LoadModel.BodyCurrentDensity.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L101-L130)[¶](#abaqus.Load.LoadModel.BodyCurrentDensity.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing BodyCurrentDensity object in the specified
        step.

        Note

        Check [BodyCurrentDensity.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodycurrentdensitypyc.htm?contextscope=all#simaker-bodycurrentdensitysetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.LoadModel.BodyCurrentDensity.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.LoadModel.BodyCurrentDensity.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            comp1=`''`[¶](#abaqus.Load.LoadModel.BodyCurrentDensity.setValuesInStep.comp1 "Permalink to this definition")
            :   A Complex specifying the first component of the load.

            comp2=`''`[¶](#abaqus.Load.LoadModel.BodyCurrentDensity.setValuesInStep.comp2 "Permalink to this definition")
            :   A Complex specifying the second component of the load.

            comp3=`''`[¶](#abaqus.Load.LoadModel.BodyCurrentDensity.setValuesInStep.comp3 "Permalink to this definition")
            :   A Complex specifying the third component of the load.

            amplitude=`''`[¶](#abaqus.Load.LoadModel.BodyCurrentDensity.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous static analysis step. FREED should be used if
                the load is changed to have no amplitude reference. You should provide the **amplitude**
                argument only if it is valid for the specified step.

*class* BodyCurrentState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyCurrentState.py#L9-L54)[¶](#abaqus.Load.BodyCurrentState.BodyCurrentState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The BodyCurrentState object stores the propagating data of a body current in a step. One instance of this
    object is created internally by the BodyCurrent object for each step. The instance is also deleted
    internally by the BodyCurrent object. The BodyCurrentState object has no constructor or methods. The
    BodyCurrentState object is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * DECURRENT

    Note

    Check [BodyCurrentState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodycurrentstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyCurrentState.py#L9-L54)[¶](#abaqus.Load.BodyCurrentState.BodyCurrentState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyCurrentState.py)[¶](#abaqus.Load.BodyCurrentState.BodyCurrentState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyCurrentState.py#L27-L28)[¶](#abaqus.Load.BodyCurrentState.BodyCurrentState.magnitude "Permalink to this definition")
    :   A Float specifying the load magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyCurrentState.py)[¶](#abaqus.Load.BodyCurrentState.BodyCurrentState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load magnitude. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyCurrentState.py)[¶](#abaqus.Load.BodyCurrentState.BodyCurrentState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* BodyForce(*[name](#abaqus.Load.LoadModel.BodyForce "abaqus.Load.LoadModel.BodyForce.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.LoadModel.BodyForce "abaqus.Load.LoadModel.BodyForce.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.LoadModel.BodyForce "abaqus.Load.LoadModel.BodyForce.__init__.region (Python parameter)")*, *[field](#abaqus.Load.LoadModel.BodyForce "abaqus.Load.LoadModel.BodyForce.__init__.field (Python parameter)")=`''`*, *[distributionType](#abaqus.Load.LoadModel.BodyForce "abaqus.Load.LoadModel.BodyForce.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[comp1](#abaqus.Load.LoadModel.BodyForce "abaqus.Load.LoadModel.BodyForce.__init__.comp1 (Python parameter)")=`None`*, *[comp2](#abaqus.Load.LoadModel.BodyForce "abaqus.Load.LoadModel.BodyForce.__init__.comp2 (Python parameter)")=`None`*, *[comp3](#abaqus.Load.LoadModel.BodyForce "abaqus.Load.LoadModel.BodyForce.__init__.comp3 (Python parameter)")=`None`*, *[amplitude](#abaqus.Load.LoadModel.BodyForce "abaqus.Load.LoadModel.BodyForce.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L15-L170)[¶](#abaqus.Load.LoadModel.BodyForce "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The BodyForce object defines a distributed load. The BodyForce object is derived from the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    The corresponding analysis keywords are:

    * DLOAD

    Note

    Check [BodyForce on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodyforcepyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L33-L35)[¶](#abaqus.Load.LoadModel.BodyForce.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
        UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L37-L40)[¶](#abaqus.Load.LoadModel.BodyForce.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L30-L31)[¶](#abaqus.Load.LoadModel.BodyForce.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L42-L43)[¶](#abaqus.Load.LoadModel.BodyForce.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[field](#abaqus.Load.LoadModel.BodyForce.setValues.field "abaqus.Load.LoadModel.BodyForce.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[distributionType](#abaqus.Load.LoadModel.BodyForce.setValues.distributionType "abaqus.Load.LoadModel.BodyForce.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[comp1](#abaqus.Load.LoadModel.BodyForce.setValues.comp1 "abaqus.Load.LoadModel.BodyForce.setValues.comp1 (Python parameter) — A Float or a Complex specifying the body force component in the 1-direction.")=`None`*, *[comp2](#abaqus.Load.LoadModel.BodyForce.setValues.comp2 "abaqus.Load.LoadModel.BodyForce.setValues.comp2 (Python parameter) — A Float or a Complex specifying the body force component in the 2-direction.")=`None`*, *[comp3](#abaqus.Load.LoadModel.BodyForce.setValues.comp3 "abaqus.Load.LoadModel.BodyForce.setValues.comp3 (Python parameter) — A Float or a Complex specifying the body force component in the 3-direction.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.BodyForce.setValues.amplitude "abaqus.Load.LoadModel.BodyForce.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L100-L134)[¶](#abaqus.Load.LoadModel.BodyForce.setValues "Permalink to this definition")
    :   This method modifies the data for an existing BodyForce object in the step where it is created.

        Note

        Check [BodyForce.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodyforcepyc.htm?contextscope=all#simaker-bodyforcesetvaluespyc).

        Parameters:[¶](#abaqus.Load.LoadModel.BodyForce.setValues-parameters "Permalink to this headline")
        :   field=`''`[¶](#abaqus.Load.LoadModel.BodyForce.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.BodyForce.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            comp1=`None`[¶](#abaqus.Load.LoadModel.BodyForce.setValues.comp1 "Permalink to this definition")
            :   A Float or a Complex specifying the body force component in the
                1-direction. Note: Although **comp1**, **comp2**, and **comp3** are optional arguments, at least
                one of them must be nonzero unless **distributionType** = USER\_DEFINED.

            comp2=`None`[¶](#abaqus.Load.LoadModel.BodyForce.setValues.comp2 "Permalink to this definition")
            :   A Float or a Complex specifying the body force component in the 2-direction.

            comp3=`None`[¶](#abaqus.Load.LoadModel.BodyForce.setValues.comp3 "Permalink to this definition")
            :   A Float or a Complex specifying the body force component in the 3-direction.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.BodyForce.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

    setValuesInStep(*[stepName](#abaqus.Load.LoadModel.BodyForce.setValuesInStep.stepName "abaqus.Load.LoadModel.BodyForce.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[comp1](#abaqus.Load.LoadModel.BodyForce.setValuesInStep.comp1 "abaqus.Load.LoadModel.BodyForce.setValuesInStep.comp1 (Python parameter) — A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the body force component in the 1-direction.")=`Ellipsis`*, *[comp2](#abaqus.Load.LoadModel.BodyForce.setValuesInStep.comp2 "abaqus.Load.LoadModel.BodyForce.setValuesInStep.comp2 (Python parameter) — A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the body force component in the 2-direction.")=`Ellipsis`*, *[comp3](#abaqus.Load.LoadModel.BodyForce.setValuesInStep.comp3 "abaqus.Load.LoadModel.BodyForce.setValuesInStep.comp3 (Python parameter) — A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the body force component in the 3-direction.")=`Ellipsis`*, *[amplitude](#abaqus.Load.LoadModel.BodyForce.setValuesInStep.amplitude "abaqus.Load.LoadModel.BodyForce.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L136-L170)[¶](#abaqus.Load.LoadModel.BodyForce.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing BodyForce object in the specified step.

        Note

        Check [BodyForce.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodyforcepyc.htm?contextscope=all#simaker-bodyforcesetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.LoadModel.BodyForce.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.LoadModel.BodyForce.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            comp1=`Ellipsis`[¶](#abaqus.Load.LoadModel.BodyForce.setValuesInStep.comp1 "Permalink to this definition")
            :   A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the body force
                component in the 1-direction. UNCHANGED should be used if the body force component is
                propagated from the previous analysis step.

            comp2=`Ellipsis`[¶](#abaqus.Load.LoadModel.BodyForce.setValuesInStep.comp2 "Permalink to this definition")
            :   A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the body force
                component in the 2-direction. UNCHANGED should be used if the body force component is
                propagated from the previous analysis step.

            comp3=`Ellipsis`[¶](#abaqus.Load.LoadModel.BodyForce.setValuesInStep.comp3 "Permalink to this definition")
            :   A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the body force
                component in the 3-direction. UNCHANGED should be used if the body force component is
                propagated from the previous analysis step.

            amplitude=`''`[¶](#abaqus.Load.LoadModel.BodyForce.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                load is changed to have no amplitude reference. You should provide the **amplitude**
                argument only if it is valid for the specified step.

*class* BodyForceState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyForceState.py#L9-L68)[¶](#abaqus.Load.BodyForceState.BodyForceState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The BodyForceState object stores the propagating data of a body force in a step. One instance of this
    object is created internally by the BodyForce object for each step. The instance is also deleted internally
    by the BodyForce object. The BodyForceState object has no constructor or methods. The BodyForceState object
    is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * DLOAD

    Note

    Check [BodyForceState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodyforcestatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyForceState.py#L9-L68)[¶](#abaqus.Load.BodyForceState.BodyForceState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyForceState.py)[¶](#abaqus.Load.BodyForceState.BodyForceState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    comp1 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyForceState.py#L27-L28)[¶](#abaqus.Load.BodyForceState.BodyForceState.comp1 "Permalink to this definition")
    :   A Float or a Complex specifying the body force component in the 1-direction.

    comp1State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyForceState.py)[¶](#abaqus.Load.BodyForceState.BodyForceState.comp1State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the body force component in the
        1-direction. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

    comp2 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyForceState.py#L30-L31)[¶](#abaqus.Load.BodyForceState.BodyForceState.comp2 "Permalink to this definition")
    :   A Float or a Complex specifying the body force component in the 2-direction.

    comp2State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyForceState.py)[¶](#abaqus.Load.BodyForceState.BodyForceState.comp2State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the body force component in the
        2-direction. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

    comp3 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyForceState.py#L33-L34)[¶](#abaqus.Load.BodyForceState.BodyForceState.comp3 "Permalink to this definition")
    :   A Float or a Complex specifying the body force component in the 3-direction.

    comp3State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyForceState.py)[¶](#abaqus.Load.BodyForceState.BodyForceState.comp3State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the body force component in the
        3-direction. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyForceState.py)[¶](#abaqus.Load.BodyForceState.BodyForceState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* BodyHeatFlux(*[name](#abaqus.Load.LoadModel.BodyHeatFlux "abaqus.Load.LoadModel.BodyHeatFlux.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.LoadModel.BodyHeatFlux "abaqus.Load.LoadModel.BodyHeatFlux.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.LoadModel.BodyHeatFlux "abaqus.Load.LoadModel.BodyHeatFlux.__init__.region (Python parameter)")*, *[magnitude](#abaqus.Load.LoadModel.BodyHeatFlux "abaqus.Load.LoadModel.BodyHeatFlux.__init__.magnitude (Python parameter)")*, *[field](#abaqus.Load.LoadModel.BodyHeatFlux "abaqus.Load.LoadModel.BodyHeatFlux.__init__.field (Python parameter)")=`''`*, *[distributionType](#abaqus.Load.LoadModel.BodyHeatFlux "abaqus.Load.LoadModel.BodyHeatFlux.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.Load.LoadModel.BodyHeatFlux "abaqus.Load.LoadModel.BodyHeatFlux.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L13-L130)[¶](#abaqus.Load.LoadModel.BodyHeatFlux "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The BodyHeatFlux object defines body heat flux from a region or into a region. The BodyHeatFlux object is
    derived from the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [BodyHeatFlux on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodyheatfluxpyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L28-L30)[¶](#abaqus.Load.LoadModel.BodyHeatFlux.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the body heat flux is distributed spatially. Possible
        values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L32-L35)[¶](#abaqus.Load.LoadModel.BodyHeatFlux.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L25-L26)[¶](#abaqus.Load.LoadModel.BodyHeatFlux.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L37-L38)[¶](#abaqus.Load.LoadModel.BodyHeatFlux.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[field](#abaqus.Load.LoadModel.BodyHeatFlux.setValues.field "abaqus.Load.LoadModel.BodyHeatFlux.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[distributionType](#abaqus.Load.LoadModel.BodyHeatFlux.setValues.distributionType "abaqus.Load.LoadModel.BodyHeatFlux.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the body heat flux is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.Load.LoadModel.BodyHeatFlux.setValues.amplitude "abaqus.Load.LoadModel.BodyHeatFlux.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L88-L111)[¶](#abaqus.Load.LoadModel.BodyHeatFlux.setValues "Permalink to this definition")
    :   This method modifies the data for an existing BodyHeatFlux object in the step where it is created.

        Note

        Check [BodyHeatFlux.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodyheatfluxpyc.htm?contextscope=all#simaker-bodyheatfluxsetvaluespyc).

        Parameters:[¶](#abaqus.Load.LoadModel.BodyHeatFlux.setValues-parameters "Permalink to this headline")
        :   field=`''`[¶](#abaqus.Load.LoadModel.BodyHeatFlux.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.BodyHeatFlux.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the body heat flux is distributed spatially. Possible
                values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.BodyHeatFlux.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

    setValuesInStep(*[stepName](#abaqus.Load.LoadModel.BodyHeatFlux.setValuesInStep.stepName "abaqus.Load.LoadModel.BodyHeatFlux.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the body heat flux is modified.")*, *[magnitude](#abaqus.Load.LoadModel.BodyHeatFlux.setValuesInStep.magnitude "abaqus.Load.LoadModel.BodyHeatFlux.setValuesInStep.magnitude (Python parameter) — A Float specifying the body heat flux magnitude.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.BodyHeatFlux.setValuesInStep.amplitude "abaqus.Load.LoadModel.BodyHeatFlux.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L113-L130)[¶](#abaqus.Load.LoadModel.BodyHeatFlux.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing BodyHeatFlux object in the specified step.

        Note

        Check [BodyHeatFlux.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodyheatfluxpyc.htm?contextscope=all#simaker-bodyheatfluxsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.LoadModel.BodyHeatFlux.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.LoadModel.BodyHeatFlux.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the body heat flux is modified.

            magnitude=`None`[¶](#abaqus.Load.LoadModel.BodyHeatFlux.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float specifying the body heat flux magnitude.

            amplitude=`''`[¶](#abaqus.Load.LoadModel.BodyHeatFlux.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                load has no amplitude reference. You should provide the **amplitude** argument only if it
                is valid for the specified step.

*class* BodyHeatFluxState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyHeatFluxState.py#L9-L54)[¶](#abaqus.Load.BodyHeatFluxState.BodyHeatFluxState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The BodyHeatFluxState object stores the propagating data for a Body BodyHeatFlux object in a step. One
    instance of this object is created internally by the BodyHeatFlux object for each step. The instance is also
    deleted internally by the BodyHeatFlux object. The BodyHeatFluxState object has no constructor or methods.
    The BodyHeatFluxState object is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * DFLUX

    Note

    Check [BodyHeatFluxState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-bodyheatfluxstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyHeatFluxState.py#L9-L54)[¶](#abaqus.Load.BodyHeatFluxState.BodyHeatFluxState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyHeatFluxState.py)[¶](#abaqus.Load.BodyHeatFluxState.BodyHeatFluxState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyHeatFluxState.py#L27-L28)[¶](#abaqus.Load.BodyHeatFluxState.BodyHeatFluxState.magnitude "Permalink to this definition")
    :   A Float specifying the Body heat flux magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyHeatFluxState.py)[¶](#abaqus.Load.BodyHeatFluxState.BodyHeatFluxState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the Body heat flux magnitude.
        Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BodyHeatFluxState.py)[¶](#abaqus.Load.BodyHeatFluxState.BodyHeatFluxState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* BoltLoad(*[name](#abaqus.Load.LoadModel.BoltLoad "abaqus.Load.LoadModel.BoltLoad.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.LoadModel.BoltLoad "abaqus.Load.LoadModel.BoltLoad.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.LoadModel.BoltLoad "abaqus.Load.LoadModel.BoltLoad.__init__.region (Python parameter)")*, *[magnitude](#abaqus.Load.LoadModel.BoltLoad "abaqus.Load.LoadModel.BoltLoad.__init__.magnitude (Python parameter)")*, *[datumAxis](#abaqus.Load.LoadModel.BoltLoad "abaqus.Load.LoadModel.BoltLoad.__init__.datumAxis (Python parameter)")*, *[boltMethod](#abaqus.Load.LoadModel.BoltLoad "abaqus.Load.LoadModel.BoltLoad.__init__.boltMethod (Python parameter)")=`abaqusConstants.APPLY_FORCE`*, *[amplitude](#abaqus.Load.LoadModel.BoltLoad "abaqus.Load.LoadModel.BoltLoad.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[preTenSecPartLevel](#abaqus.Load.LoadModel.BoltLoad "abaqus.Load.LoadModel.BoltLoad.__init__.preTenSecPartLevel (Python parameter)")=`False`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L14-L160)[¶](#abaqus.Load.LoadModel.BoltLoad "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The BoltLoad object defines a bolt load. The BoltLoad object is derived from the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    The corresponding analysis keywords are:

    * PRE-TENSION SECTION
      :   + NODE
    * NSET

    Note

    Check [BoltLoad on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boltloadpyc.htm?contextscope=all).

    Member Details:

    datumAxis : --is-rst--:py:class:`~abaqus.Datum.DatumAxis.DatumAxis` = `<abaqus.Datum.DatumAxis.DatumAxis object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L34-L37)[¶](#abaqus.Load.LoadModel.BoltLoad.datumAxis "Permalink to this definition")
    :   A DatumAxis object specifying the orientation of the pre-tension section
        normal. Note: *datumAxis* is required only for Solid and Shell regions; it has no meaning
        for Wire regions.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L31-L32)[¶](#abaqus.Load.LoadModel.BoltLoad.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L39-L40)[¶](#abaqus.Load.LoadModel.BoltLoad.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[boltMethod](#abaqus.Load.LoadModel.BoltLoad.setValues.boltMethod "abaqus.Load.LoadModel.BoltLoad.setValues.boltMethod (Python parameter) — A SymbolicConstant specifying the method of applying the bolt load.")=`abaqusConstants.APPLY_FORCE`*, *[datumAxis](#abaqus.Load.LoadModel.BoltLoad.setValues.datumAxis "abaqus.Load.LoadModel.BoltLoad.setValues.datumAxis (Python parameter) — A DatumAxis object specifying the orientation of the pre-tension section normal.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.BoltLoad.setValues.amplitude "abaqus.Load.LoadModel.BoltLoad.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*, *[preTenSecPartLevel](#abaqus.Load.LoadModel.BoltLoad.setValues.preTenSecPartLevel "abaqus.Load.LoadModel.BoltLoad.setValues.preTenSecPartLevel (Python parameter) — A Boolean specifying whether the pre-tension section is to be defined at the part level. The default value is False.")=`False`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L103-L132)[¶](#abaqus.Load.LoadModel.BoltLoad.setValues "Permalink to this definition")
    :   This method modifies the data for an existing BoltLoad object in the step where it is created.

        Note

        Check [BoltLoad.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boltloadpyc.htm?contextscope=all#simaker-boltloadsetvaluespyc).

        Parameters:[¶](#abaqus.Load.LoadModel.BoltLoad.setValues-parameters "Permalink to this headline")
        :   boltMethod=`abaqusConstants.APPLY_FORCE`[¶](#abaqus.Load.LoadModel.BoltLoad.setValues.boltMethod "Permalink to this definition")
            :   A SymbolicConstant specifying the method of applying the bolt load. Possible values are
                APPLY\_FORCE and ADJUST\_LENGTH. The default value is APPLY\_FORCE.

            datumAxis=`None`[¶](#abaqus.Load.LoadModel.BoltLoad.setValues.datumAxis "Permalink to this definition")
            :   A DatumAxis object specifying the orientation of the pre-tension section normal. Note:
                **datumAxis** is applicable only for Solid and Shell regions; it has no meaning for Wire
                regions.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.BoltLoad.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

            preTenSecPartLevel=`False`[¶](#abaqus.Load.LoadModel.BoltLoad.setValues.preTenSecPartLevel "Permalink to this definition")
            :   A Boolean specifying whether the pre-tension section is to be defined at the part level.
                The default value is False. You should provide the **preTenSecPartLevel** argument only if
                the selected region belongs to a dependent part instance. A pre-tension section cannot
                be defined at the part level for independent and model instances.

    setValuesInStep(*[stepName](#abaqus.Load.LoadModel.BoltLoad.setValuesInStep.stepName "abaqus.Load.LoadModel.BoltLoad.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[boltMethod](#abaqus.Load.LoadModel.BoltLoad.setValuesInStep.boltMethod "abaqus.Load.LoadModel.BoltLoad.setValuesInStep.boltMethod (Python parameter) — A SymbolicConstant specifying the type of bolt load.")=`abaqusConstants.APPLY_FORCE`*, *[magnitude](#abaqus.Load.LoadModel.BoltLoad.setValuesInStep.magnitude "abaqus.Load.LoadModel.BoltLoad.setValuesInStep.magnitude (Python parameter) — A Float specifying the bolt load magnitude.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.BoltLoad.setValuesInStep.amplitude "abaqus.Load.LoadModel.BoltLoad.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L134-L160)[¶](#abaqus.Load.LoadModel.BoltLoad.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing BoltLoad object in the specified step.

        Note

        Check [BoltLoad.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boltloadpyc.htm?contextscope=all#simaker-boltloadsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.LoadModel.BoltLoad.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.LoadModel.BoltLoad.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            boltMethod=`abaqusConstants.APPLY_FORCE`[¶](#abaqus.Load.LoadModel.BoltLoad.setValuesInStep.boltMethod "Permalink to this definition")
            :   A SymbolicConstant specifying the type of bolt load. Possible values are APPLY\_FORCE,
                ADJUST\_LENGTH, and FIX\_LENGTH. The default is APPLY\_FORCE.

            magnitude=`None`[¶](#abaqus.Load.LoadModel.BoltLoad.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float specifying the bolt load magnitude.

            amplitude=`''`[¶](#abaqus.Load.LoadModel.BoltLoad.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                load is changed to have no amplitude reference. You should provide the **amplitude**
                argument only if it is valid for the specified step.

*class* BoltLoadState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BoltLoadState.py#L9-L63)[¶](#abaqus.Load.BoltLoadState.BoltLoadState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The BoltLoadState object stores the propagating data of a bolt load in a step. One instance of this
    object is created internally by the BoltLoad object for each step. The instance is also deleted internally
    by the BoltLoad object. The BoltLoadState object has no constructor or methods. The BoltLoadState object is
    derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * CLOAD
    * BOUNDARY

    Note

    Check [BoltLoadState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boltloadstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BoltLoadState.py#L9-L63)[¶](#abaqus.Load.BoltLoadState.BoltLoadState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BoltLoadState.py)[¶](#abaqus.Load.BoltLoadState.BoltLoadState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    boltMethod : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BoltLoadState.py)[¶](#abaqus.Load.BoltLoadState.BoltLoadState.boltMethod "Permalink to this definition")
    :   A SymbolicConstant specifying the type of bolt load. Possible values are APPLY\_FORCE,
        ADJUST\_LENGTH, and FIX\_LENGTH.

    boltMethodState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BoltLoadState.py)[¶](#abaqus.Load.BoltLoadState.BoltLoadState.boltMethodState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the bolt load type. Possible
        values are UNSET, SET, UNCHANGED, and MODIFIED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BoltLoadState.py#L36-L37)[¶](#abaqus.Load.BoltLoadState.BoltLoadState.magnitude "Permalink to this definition")
    :   A Float specifying the bolt load magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BoltLoadState.py)[¶](#abaqus.Load.BoltLoadState.BoltLoadState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the bolt load magnitude. Possible
        values are UNSET, SET, UNCHANGED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/BoltLoadState.py)[¶](#abaqus.Load.BoltLoadState.BoltLoadState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* ConcCharge(*[name](#abaqus.Load.LoadModel.ConcCharge "abaqus.Load.LoadModel.ConcCharge.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.LoadModel.ConcCharge "abaqus.Load.LoadModel.ConcCharge.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.LoadModel.ConcCharge "abaqus.Load.LoadModel.ConcCharge.__init__.region (Python parameter)")*, *[magnitude](#abaqus.Load.LoadModel.ConcCharge "abaqus.Load.LoadModel.ConcCharge.__init__.magnitude (Python parameter)")*, *[distributionType](#abaqus.Load.LoadModel.ConcCharge "abaqus.Load.LoadModel.ConcCharge.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.ConcCharge "abaqus.Load.LoadModel.ConcCharge.__init__.field (Python parameter)")=`''`*, *[amplitude](#abaqus.Load.LoadModel.ConcCharge "abaqus.Load.LoadModel.ConcCharge.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L13-L130)[¶](#abaqus.Load.LoadModel.ConcCharge "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The ConcCharge object stores the data for a concentrated charge. The ConcCharge object is derived from
    the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [ConcCharge on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concchargepyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L28-L30)[¶](#abaqus.Load.LoadModel.ConcCharge.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
        UNIFORM and FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L32-L35)[¶](#abaqus.Load.LoadModel.ConcCharge.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L25-L26)[¶](#abaqus.Load.LoadModel.ConcCharge.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L37-L38)[¶](#abaqus.Load.LoadModel.ConcCharge.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[distributionType](#abaqus.Load.LoadModel.ConcCharge.setValues.distributionType "abaqus.Load.LoadModel.ConcCharge.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.ConcCharge.setValues.field "abaqus.Load.LoadModel.ConcCharge.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[amplitude](#abaqus.Load.LoadModel.ConcCharge.setValues.amplitude "abaqus.Load.LoadModel.ConcCharge.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L88-L111)[¶](#abaqus.Load.LoadModel.ConcCharge.setValues "Permalink to this definition")
    :   This method modifies the data for an existing ConcCharge object in the step where it is created.

        Note

        Check [ConcCharge.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concchargepyc.htm?contextscope=all#simaker-concchargesetvaluespyc).

        Parameters:[¶](#abaqus.Load.LoadModel.ConcCharge.setValues-parameters "Permalink to this headline")
        :   distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.ConcCharge.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.ConcCharge.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.ConcCharge.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

    setValuesInStep(*[stepName](#abaqus.Load.LoadModel.ConcCharge.setValuesInStep.stepName "abaqus.Load.LoadModel.ConcCharge.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[magnitude](#abaqus.Load.LoadModel.ConcCharge.setValuesInStep.magnitude "abaqus.Load.LoadModel.ConcCharge.setValuesInStep.magnitude (Python parameter) — A Float specifying the load magnitude.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.ConcCharge.setValuesInStep.amplitude "abaqus.Load.LoadModel.ConcCharge.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L113-L130)[¶](#abaqus.Load.LoadModel.ConcCharge.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing ConcCharge object in the specified step.

        Note

        Check [ConcCharge.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concchargepyc.htm?contextscope=all#simaker-concchargesetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.LoadModel.ConcCharge.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.LoadModel.ConcCharge.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            magnitude=`None`[¶](#abaqus.Load.LoadModel.ConcCharge.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float specifying the load magnitude.

            amplitude=`''`[¶](#abaqus.Load.LoadModel.ConcCharge.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous static analysis step. FREED should be used if
                the load is changed to have no amplitude reference. You should provide the **amplitude**
                argument only if it is valid for the specified step.

*class* ConcConcFlux(*[name](#abaqus.Load.LoadModel.ConcConcFlux "abaqus.Load.LoadModel.ConcConcFlux.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.LoadModel.ConcConcFlux "abaqus.Load.LoadModel.ConcConcFlux.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.LoadModel.ConcConcFlux "abaqus.Load.LoadModel.ConcConcFlux.__init__.region (Python parameter)")*, *[magnitude](#abaqus.Load.LoadModel.ConcConcFlux "abaqus.Load.LoadModel.ConcConcFlux.__init__.magnitude (Python parameter)")*, *[distributionType](#abaqus.Load.LoadModel.ConcConcFlux "abaqus.Load.LoadModel.ConcConcFlux.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.ConcConcFlux "abaqus.Load.LoadModel.ConcConcFlux.__init__.field (Python parameter)")=`''`*, *[amplitude](#abaqus.Load.LoadModel.ConcConcFlux "abaqus.Load.LoadModel.ConcConcFlux.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L13-L130)[¶](#abaqus.Load.LoadModel.ConcConcFlux "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The ConcConcFlux object stores the data for a concentrated concentration flux. The ConcConcFlux object is
    derived from the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [ConcConcFlux on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concconcfluxpyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L28-L30)[¶](#abaqus.Load.LoadModel.ConcConcFlux.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
        UNIFORM and FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L32-L35)[¶](#abaqus.Load.LoadModel.ConcConcFlux.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L25-L26)[¶](#abaqus.Load.LoadModel.ConcConcFlux.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L37-L38)[¶](#abaqus.Load.LoadModel.ConcConcFlux.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[distributionType](#abaqus.Load.LoadModel.ConcConcFlux.setValues.distributionType "abaqus.Load.LoadModel.ConcConcFlux.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.ConcConcFlux.setValues.field "abaqus.Load.LoadModel.ConcConcFlux.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[amplitude](#abaqus.Load.LoadModel.ConcConcFlux.setValues.amplitude "abaqus.Load.LoadModel.ConcConcFlux.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L88-L111)[¶](#abaqus.Load.LoadModel.ConcConcFlux.setValues "Permalink to this definition")
    :   This method modifies the data for an existing ConcConcFlux object in the step where it is created.

        Note

        Check [ConcConcFlux.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concconcfluxpyc.htm?contextscope=all#simaker-concconcfluxsetvaluespyc).

        Parameters:[¶](#abaqus.Load.LoadModel.ConcConcFlux.setValues-parameters "Permalink to this headline")
        :   distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.ConcConcFlux.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.ConcConcFlux.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.ConcConcFlux.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

    setValuesInStep(*[stepName](#abaqus.Load.LoadModel.ConcConcFlux.setValuesInStep.stepName "abaqus.Load.LoadModel.ConcConcFlux.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[magnitude](#abaqus.Load.LoadModel.ConcConcFlux.setValuesInStep.magnitude "abaqus.Load.LoadModel.ConcConcFlux.setValuesInStep.magnitude (Python parameter) — A Float specifying the load magnitude.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.ConcConcFlux.setValuesInStep.amplitude "abaqus.Load.LoadModel.ConcConcFlux.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L113-L130)[¶](#abaqus.Load.LoadModel.ConcConcFlux.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing ConcConcFlux object in the specified step.

        Note

        Check [ConcConcFlux.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concconcfluxpyc.htm?contextscope=all#simaker-concconcfluxsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.LoadModel.ConcConcFlux.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.LoadModel.ConcConcFlux.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            magnitude=`None`[¶](#abaqus.Load.LoadModel.ConcConcFlux.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float specifying the load magnitude.

            amplitude=`''`[¶](#abaqus.Load.LoadModel.ConcConcFlux.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous static analysis step. FREED should be used if
                the load is changed to have no amplitude reference. You should provide the **amplitude**
                argument only if it is valid for the specified step.

*class* ConcCurrent(*[name](#abaqus.Load.LoadModel.ConcCurrent "abaqus.Load.LoadModel.ConcCurrent.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.LoadModel.ConcCurrent "abaqus.Load.LoadModel.ConcCurrent.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.LoadModel.ConcCurrent "abaqus.Load.LoadModel.ConcCurrent.__init__.region (Python parameter)")*, *[magnitude](#abaqus.Load.LoadModel.ConcCurrent "abaqus.Load.LoadModel.ConcCurrent.__init__.magnitude (Python parameter)")*, *[distributionType](#abaqus.Load.LoadModel.ConcCurrent "abaqus.Load.LoadModel.ConcCurrent.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.ConcCurrent "abaqus.Load.LoadModel.ConcCurrent.__init__.field (Python parameter)")=`''`*, *[amplitude](#abaqus.Load.LoadModel.ConcCurrent "abaqus.Load.LoadModel.ConcCurrent.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L13-L130)[¶](#abaqus.Load.LoadModel.ConcCurrent "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The ConcCurrent object stores the data for a concentrated current. The ConcCurrent object is derived from
    the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [ConcCurrent on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-conccurrentpyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L28-L30)[¶](#abaqus.Load.LoadModel.ConcCurrent.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
        UNIFORM and FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L32-L35)[¶](#abaqus.Load.LoadModel.ConcCurrent.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L25-L26)[¶](#abaqus.Load.LoadModel.ConcCurrent.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L37-L38)[¶](#abaqus.Load.LoadModel.ConcCurrent.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[distributionType](#abaqus.Load.LoadModel.ConcCurrent.setValues.distributionType "abaqus.Load.LoadModel.ConcCurrent.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.ConcCurrent.setValues.field "abaqus.Load.LoadModel.ConcCurrent.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[amplitude](#abaqus.Load.LoadModel.ConcCurrent.setValues.amplitude "abaqus.Load.LoadModel.ConcCurrent.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L88-L111)[¶](#abaqus.Load.LoadModel.ConcCurrent.setValues "Permalink to this definition")
    :   This method modifies the data for an existing ConcCurrent object in the step where it is created.

        Note

        Check [ConcCurrent.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-conccurrentpyc.htm?contextscope=all#simaker-conccurrentsetvaluespyc).

        Parameters:[¶](#abaqus.Load.LoadModel.ConcCurrent.setValues-parameters "Permalink to this headline")
        :   distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.ConcCurrent.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.ConcCurrent.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.ConcCurrent.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

    setValuesInStep(*[stepName](#abaqus.Load.LoadModel.ConcCurrent.setValuesInStep.stepName "abaqus.Load.LoadModel.ConcCurrent.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[magnitude](#abaqus.Load.LoadModel.ConcCurrent.setValuesInStep.magnitude "abaqus.Load.LoadModel.ConcCurrent.setValuesInStep.magnitude (Python parameter) — A Float specifying the load magnitude.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.ConcCurrent.setValuesInStep.amplitude "abaqus.Load.LoadModel.ConcCurrent.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L113-L130)[¶](#abaqus.Load.LoadModel.ConcCurrent.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing ConcCurrent object in the specified step.

        Note

        Check [ConcCurrent.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-conccurrentpyc.htm?contextscope=all#simaker-conccurrentsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.LoadModel.ConcCurrent.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.LoadModel.ConcCurrent.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            magnitude=`None`[¶](#abaqus.Load.LoadModel.ConcCurrent.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float specifying the load magnitude.

            amplitude=`''`[¶](#abaqus.Load.LoadModel.ConcCurrent.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous static analysis step. FREED should be used if
                the load is changed to have no amplitude reference. You should provide the **amplitude**
                argument only if it is valid for the specified step.

*class* ConcCurrentState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcCurrentState.py#L9-L54)[¶](#abaqus.Load.ConcCurrentState.ConcCurrentState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The ConcCurrentState object stores the propagating data of a concentrated current in a step. One instance
    of this object is created internally by the ConcCurrent object for each step. The instance is also deleted
    internally by the ConcCurrent object. The ConcCurrentState object has no constructor or methods. The
    ConcCurrentState object is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * CECURRENT

    Note

    Check [ConcCurrentState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-conccurrentstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcCurrentState.py#L9-L54)[¶](#abaqus.Load.ConcCurrentState.ConcCurrentState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcCurrentState.py)[¶](#abaqus.Load.ConcCurrentState.ConcCurrentState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcCurrentState.py#L27-L28)[¶](#abaqus.Load.ConcCurrentState.ConcCurrentState.magnitude "Permalink to this definition")
    :   A Float specifying the load magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcCurrentState.py)[¶](#abaqus.Load.ConcCurrentState.ConcCurrentState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load magnitude. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcCurrentState.py)[¶](#abaqus.Load.ConcCurrentState.ConcCurrentState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* ConcPoreFluid(*[name](#abaqus.Load.LoadModel.ConcPoreFluid "abaqus.Load.LoadModel.ConcPoreFluid.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.LoadModel.ConcPoreFluid "abaqus.Load.LoadModel.ConcPoreFluid.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.LoadModel.ConcPoreFluid "abaqus.Load.LoadModel.ConcPoreFluid.__init__.region (Python parameter)")*, *[magnitude](#abaqus.Load.LoadModel.ConcPoreFluid "abaqus.Load.LoadModel.ConcPoreFluid.__init__.magnitude (Python parameter)")*, *[distributionType](#abaqus.Load.LoadModel.ConcPoreFluid "abaqus.Load.LoadModel.ConcPoreFluid.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.ConcPoreFluid "abaqus.Load.LoadModel.ConcPoreFluid.__init__.field (Python parameter)")=`''`*, *[amplitude](#abaqus.Load.LoadModel.ConcPoreFluid "abaqus.Load.LoadModel.ConcPoreFluid.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L13-L130)[¶](#abaqus.Load.LoadModel.ConcPoreFluid "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The ConcPoreFluid object stores the data for a concentrated pore fluid flow load. The ConcPoreFluid
    object is derived from the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [ConcPoreFluid on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concporefluidpyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L28-L30)[¶](#abaqus.Load.LoadModel.ConcPoreFluid.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
        UNIFORM and FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L32-L35)[¶](#abaqus.Load.LoadModel.ConcPoreFluid.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L25-L26)[¶](#abaqus.Load.LoadModel.ConcPoreFluid.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L37-L38)[¶](#abaqus.Load.LoadModel.ConcPoreFluid.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[distributionType](#abaqus.Load.LoadModel.ConcPoreFluid.setValues.distributionType "abaqus.Load.LoadModel.ConcPoreFluid.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.ConcPoreFluid.setValues.field "abaqus.Load.LoadModel.ConcPoreFluid.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[amplitude](#abaqus.Load.LoadModel.ConcPoreFluid.setValues.amplitude "abaqus.Load.LoadModel.ConcPoreFluid.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L88-L111)[¶](#abaqus.Load.LoadModel.ConcPoreFluid.setValues "Permalink to this definition")
    :   This method modifies the data for an existing ConcPoreFluid object in the step where it is created.

        Note

        Check [ConcPoreFluid.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concporefluidpyc.htm?contextscope=all#simaker-concporefluidsetvaluespyc).

        Parameters:[¶](#abaqus.Load.LoadModel.ConcPoreFluid.setValues-parameters "Permalink to this headline")
        :   distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.ConcPoreFluid.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.ConcPoreFluid.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.ConcPoreFluid.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

    setValuesInStep(*[stepName](#abaqus.Load.LoadModel.ConcPoreFluid.setValuesInStep.stepName "abaqus.Load.LoadModel.ConcPoreFluid.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[magnitude](#abaqus.Load.LoadModel.ConcPoreFluid.setValuesInStep.magnitude "abaqus.Load.LoadModel.ConcPoreFluid.setValuesInStep.magnitude (Python parameter) — A Float specifying the load magnitude.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.ConcPoreFluid.setValuesInStep.amplitude "abaqus.Load.LoadModel.ConcPoreFluid.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L113-L130)[¶](#abaqus.Load.LoadModel.ConcPoreFluid.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing ConcPoreFluid object in the specified step.

        Note

        Check [ConcPoreFluid.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concporefluidpyc.htm?contextscope=all#simaker-concporefluidsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.LoadModel.ConcPoreFluid.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.LoadModel.ConcPoreFluid.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            magnitude=`None`[¶](#abaqus.Load.LoadModel.ConcPoreFluid.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float specifying the load magnitude.

            amplitude=`''`[¶](#abaqus.Load.LoadModel.ConcPoreFluid.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous static analysis step. FREED should be used if
                the load is changed to have no amplitude reference. You should provide the **amplitude**
                argument only if it is valid for the specified step.

*class* ConcentratedChargeState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedChargeState.py#L9-L54)[¶](#abaqus.Load.ConcentratedChargeState.ConcentratedChargeState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The ConcentratedChargeState object stores the propagating data of a concentrated charge in a step. One
    instance of this object is created internally by the ConcCharge object for each step. The instance is also
    deleted internally by the ConcCharge object. The ConcentratedChargeState object has no constructor or
    methods. The ConcentratedChargeState object is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * CECHARGE

    Note

    Check [ConcentratedChargeState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concentratedchargestatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedChargeState.py#L9-L54)[¶](#abaqus.Load.ConcentratedChargeState.ConcentratedChargeState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedChargeState.py)[¶](#abaqus.Load.ConcentratedChargeState.ConcentratedChargeState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedChargeState.py#L27-L28)[¶](#abaqus.Load.ConcentratedChargeState.ConcentratedChargeState.magnitude "Permalink to this definition")
    :   A Float specifying the load magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedChargeState.py)[¶](#abaqus.Load.ConcentratedChargeState.ConcentratedChargeState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load magnitude. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedChargeState.py)[¶](#abaqus.Load.ConcentratedChargeState.ConcentratedChargeState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* ConcentratedConcentrationFluxState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedConcentrationFluxState.py#L9-L55)[¶](#abaqus.Load.ConcentratedConcentrationFluxState.ConcentratedConcentrationFluxState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The ConcentratedConcentrationFluxState object stores the propagating data of a concentrated concentration
    flux in a step. One instance of this object is created internally by the ConcConcFlux object for each step.
    The instance is also deleted internally by the ConcConcFlux object. The ConcentratedConcentrationFluxState
    object has no constructor or methods. The ConcentratedConcentrationFluxState object is derived from the
    LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * CFLUX

    Note

    Check [ConcentratedConcentrationFluxState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concentratedconcentrationfluxstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedConcentrationFluxState.py#L9-L55)[¶](#abaqus.Load.ConcentratedConcentrationFluxState.ConcentratedConcentrationFluxState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedConcentrationFluxState.py)[¶](#abaqus.Load.ConcentratedConcentrationFluxState.ConcentratedConcentrationFluxState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedConcentrationFluxState.py#L28-L29)[¶](#abaqus.Load.ConcentratedConcentrationFluxState.ConcentratedConcentrationFluxState.magnitude "Permalink to this definition")
    :   A Float specifying the load magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedConcentrationFluxState.py)[¶](#abaqus.Load.ConcentratedConcentrationFluxState.ConcentratedConcentrationFluxState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load magnitude. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedConcentrationFluxState.py)[¶](#abaqus.Load.ConcentratedConcentrationFluxState.ConcentratedConcentrationFluxState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* ConcentratedForce(*[name](#abaqus.Load.LoadModel.ConcentratedForce "abaqus.Load.LoadModel.ConcentratedForce.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.LoadModel.ConcentratedForce "abaqus.Load.LoadModel.ConcentratedForce.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.LoadModel.ConcentratedForce "abaqus.Load.LoadModel.ConcentratedForce.__init__.region (Python parameter)")*, *[distributionType](#abaqus.Load.LoadModel.ConcentratedForce "abaqus.Load.LoadModel.ConcentratedForce.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.ConcentratedForce "abaqus.Load.LoadModel.ConcentratedForce.__init__.field (Python parameter)")=`''`*, *[cf1](#abaqus.Load.LoadModel.ConcentratedForce "abaqus.Load.LoadModel.ConcentratedForce.__init__.cf1 (Python parameter)")=`None`*, *[cf2](#abaqus.Load.LoadModel.ConcentratedForce "abaqus.Load.LoadModel.ConcentratedForce.__init__.cf2 (Python parameter)")=`None`*, *[cf3](#abaqus.Load.LoadModel.ConcentratedForce "abaqus.Load.LoadModel.ConcentratedForce.__init__.cf3 (Python parameter)")=`None`*, *[amplitude](#abaqus.Load.LoadModel.ConcentratedForce "abaqus.Load.LoadModel.ConcentratedForce.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[follower](#abaqus.Load.LoadModel.ConcentratedForce "abaqus.Load.LoadModel.ConcentratedForce.__init__.follower (Python parameter)")=`0`*, *[localCsys](#abaqus.Load.LoadModel.ConcentratedForce "abaqus.Load.LoadModel.ConcentratedForce.__init__.localCsys (Python parameter)")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L21-L208)[¶](#abaqus.Load.LoadModel.ConcentratedForce "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The ConcentratedForce object defines a concentrated force. The ConcentratedForce object is derived from
    the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [ConcentratedForce on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concentratedforcepyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L36-L38)[¶](#abaqus.Load.LoadModel.ConcentratedForce.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
        UNIFORM and FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L51-L54)[¶](#abaqus.Load.LoadModel.ConcentratedForce.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    follower : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L40-L43)[¶](#abaqus.Load.LoadModel.ConcentratedForce.follower "Permalink to this definition")
    :   A Boolean specifying whether the direction of the force rotates with the rotation at
        each node of the region. You should provide the **follower** argument only if it is valid
        for the specified step. The default value is OFF.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L45-L49)[¶](#abaqus.Load.LoadModel.ConcentratedForce.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the load’s degrees
        of freedom. If **localCsys** = None, the degrees of freedom are defined in the global
        coordinate system. When this member is queried, it returns an Int. The default value is
        None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L33-L34)[¶](#abaqus.Load.LoadModel.ConcentratedForce.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L56-L57)[¶](#abaqus.Load.LoadModel.ConcentratedForce.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[distributionType](#abaqus.Load.LoadModel.ConcentratedForce.setValues.distributionType "abaqus.Load.LoadModel.ConcentratedForce.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.ConcentratedForce.setValues.field "abaqus.Load.LoadModel.ConcentratedForce.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[cf1](#abaqus.Load.LoadModel.ConcentratedForce.setValues.cf1 "abaqus.Load.LoadModel.ConcentratedForce.setValues.cf1 (Python parameter) — A Float or a Complex specifying the concentrated force component in the 1-direction. Although cf1, cf2, and cf3 are optional arguments, at least one of them must be nonzero.")=`None`*, *[cf2](#abaqus.Load.LoadModel.ConcentratedForce.setValues.cf2 "abaqus.Load.LoadModel.ConcentratedForce.setValues.cf2 (Python parameter) — A Float or a Complex specifying the concentrated force component in the 2-direction.")=`None`*, *[cf3](#abaqus.Load.LoadModel.ConcentratedForce.setValues.cf3 "abaqus.Load.LoadModel.ConcentratedForce.setValues.cf3 (Python parameter) — A Float or a Complex specifying the concentrated force component in the 3-direction.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.ConcentratedForce.setValues.amplitude "abaqus.Load.LoadModel.ConcentratedForce.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*, *[follower](#abaqus.Load.LoadModel.ConcentratedForce.setValues.follower "abaqus.Load.LoadModel.ConcentratedForce.setValues.follower (Python parameter) — A Boolean specifying whether the direction of the force rotates with the rotation at each node of the region.")=`0`*, *[localCsys](#abaqus.Load.LoadModel.ConcentratedForce.setValues.localCsys "abaqus.Load.LoadModel.ConcentratedForce.setValues.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the load's degrees of freedom.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L125-L171)[¶](#abaqus.Load.LoadModel.ConcentratedForce.setValues "Permalink to this definition")
    :   This method modifies the data for an existing ConcentratedForce object in the step where it is
        created.

        Note

        Check [ConcentratedForce.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concentratedforcepyc.htm?contextscope=all#simaker-concentratedforcesetvaluespyc).

        Parameters:[¶](#abaqus.Load.LoadModel.ConcentratedForce.setValues-parameters "Permalink to this headline")
        :   distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.ConcentratedForce.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.ConcentratedForce.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            cf1=`None`[¶](#abaqus.Load.LoadModel.ConcentratedForce.setValues.cf1 "Permalink to this definition")
            :   A Float or a Complex specifying the concentrated force component in the 1-direction.
                Although **cf1**, **cf2**, and **cf3** are optional arguments, at least one of them must be
                nonzero.

            cf2=`None`[¶](#abaqus.Load.LoadModel.ConcentratedForce.setValues.cf2 "Permalink to this definition")
            :   A Float or a Complex specifying the concentrated force component in the 2-direction.

            cf3=`None`[¶](#abaqus.Load.LoadModel.ConcentratedForce.setValues.cf3 "Permalink to this definition")
            :   A Float or a Complex specifying the concentrated force component in the 3-direction.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.ConcentratedForce.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

            follower=`0`[¶](#abaqus.Load.LoadModel.ConcentratedForce.setValues.follower "Permalink to this definition")
            :   A Boolean specifying whether the direction of the force rotates with the rotation at
                each node of the region. You should provide the **follower** argument only if it is valid
                for the specified step. The default value is OFF.

            localCsys=`None`[¶](#abaqus.Load.LoadModel.ConcentratedForce.setValues.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the load’s degrees
                of freedom. If **localCsys** = None, the degrees of freedom are defined in the global
                coordinate system. When this member is queried, it returns an Int. The default value is
                None.

    setValuesInStep(*[stepName](#abaqus.Load.LoadModel.ConcentratedForce.setValuesInStep.stepName "abaqus.Load.LoadModel.ConcentratedForce.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[cf1](#abaqus.Load.LoadModel.ConcentratedForce.setValuesInStep.cf1 "abaqus.Load.LoadModel.ConcentratedForce.setValuesInStep.cf1 (Python parameter) — A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the concentrated force component in the 1-direction.")=`Ellipsis`*, *[cf2](#abaqus.Load.LoadModel.ConcentratedForce.setValuesInStep.cf2 "abaqus.Load.LoadModel.ConcentratedForce.setValuesInStep.cf2 (Python parameter) — A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the concentrated force component in the 2-direction.")=`Ellipsis`*, *[cf3](#abaqus.Load.LoadModel.ConcentratedForce.setValuesInStep.cf3 "abaqus.Load.LoadModel.ConcentratedForce.setValuesInStep.cf3 (Python parameter) — A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the concentrated force component in the 3-direction.")=`Ellipsis`*, *[amplitude](#abaqus.Load.LoadModel.ConcentratedForce.setValuesInStep.amplitude "abaqus.Load.LoadModel.ConcentratedForce.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L173-L208)[¶](#abaqus.Load.LoadModel.ConcentratedForce.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing ConcentratedForce object in the specified
        step.

        Note

        Check [ConcentratedForce.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concentratedforcepyc.htm?contextscope=all#simaker-concentratedforcesetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.LoadModel.ConcentratedForce.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.LoadModel.ConcentratedForce.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            cf1=`Ellipsis`[¶](#abaqus.Load.LoadModel.ConcentratedForce.setValuesInStep.cf1 "Permalink to this definition")
            :   A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the concentrated force
                component in the 1-direction. UNCHANGED should be used if the concentrated force
                component is propagated from the previous analysis step.

            cf2=`Ellipsis`[¶](#abaqus.Load.LoadModel.ConcentratedForce.setValuesInStep.cf2 "Permalink to this definition")
            :   A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the concentrated force
                component in the 2-direction. UNCHANGED should be used if the concentrated force
                component is propagated from the previous analysis step.

            cf3=`Ellipsis`[¶](#abaqus.Load.LoadModel.ConcentratedForce.setValuesInStep.cf3 "Permalink to this definition")
            :   A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the concentrated force
                component in the 3-direction. UNCHANGED should be used if the concentrated force
                component is propagated from the previous analysis step.

            amplitude=`''`[¶](#abaqus.Load.LoadModel.ConcentratedForce.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                load is changed to have no amplitude reference. You should provide the **amplitude**
                argument only if it is valid for the specified step.

*class* ConcentratedForceState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedForceState.py#L9-L69)[¶](#abaqus.Load.ConcentratedForceState.ConcentratedForceState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The ConcentratedForceState object stores the propagating data for a concentrated force in a step. One
    instance of this object is created internally by the ConcentratedForce object for each step. The instance is
    also deleted internally by the ConcentratedForce object. The ConcentratedForceState object has no
    constructor or methods. The ConcentratedForceState object is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * CLOAD

    Note

    Check [ConcentratedForceState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concentratedforcestatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedForceState.py#L9-L69)[¶](#abaqus.Load.ConcentratedForceState.ConcentratedForceState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.
        - NOT\_YET\_ACTIVE
        - CREATED
        - PROPAGATED
        - MODIFIED
        - DEACTIVATED
        - NO\_LONGER\_ACTIVE
        - TYPE\_NOT\_APPLICABLE
        - INSTANCE\_NOT\_APPLICABLE
        - BUILT\_INTO\_BASE\_STATE

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedForceState.py)[¶](#abaqus.Load.ConcentratedForceState.ConcentratedForceState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    cf1 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedForceState.py#L27-L30)[¶](#abaqus.Load.ConcentratedForceState.ConcentratedForceState.cf1 "Permalink to this definition")
    :   A Float or a Complex specifying the concentrated force component in the 1-direction.
        Although **cf1**, **cf2**, and **cf3** are optional arguments, at least one of them must be
        nonzero.

    cf1State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedForceState.py)[¶](#abaqus.Load.ConcentratedForceState.ConcentratedForceState.cf1State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the concentrated force component
        in the 1-direction. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

    cf2 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedForceState.py#L32-L33)[¶](#abaqus.Load.ConcentratedForceState.ConcentratedForceState.cf2 "Permalink to this definition")
    :   A Float or a Complex specifying the concentrated force component in the 2-direction.

    cf2State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedForceState.py)[¶](#abaqus.Load.ConcentratedForceState.ConcentratedForceState.cf2State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the concentrated force component
        in the 2-direction. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

    cf3 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedForceState.py#L35-L36)[¶](#abaqus.Load.ConcentratedForceState.ConcentratedForceState.cf3 "Permalink to this definition")
    :   A Float or a Complex specifying the concentrated force component in the 3-direction.

    cf3State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedForceState.py)[¶](#abaqus.Load.ConcentratedForceState.ConcentratedForceState.cf3State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the concentrated force component
        in the 3-direction. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedForceState.py)[¶](#abaqus.Load.ConcentratedForceState.ConcentratedForceState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

*class* ConcentratedHeatFlux(*[name](#abaqus.Load.LoadModel.ConcentratedHeatFlux "abaqus.Load.LoadModel.ConcentratedHeatFlux.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.LoadModel.ConcentratedHeatFlux "abaqus.Load.LoadModel.ConcentratedHeatFlux.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.LoadModel.ConcentratedHeatFlux "abaqus.Load.LoadModel.ConcentratedHeatFlux.__init__.region (Python parameter)")*, *[magnitude](#abaqus.Load.LoadModel.ConcentratedHeatFlux "abaqus.Load.LoadModel.ConcentratedHeatFlux.__init__.magnitude (Python parameter)")*, *[distributionType](#abaqus.Load.LoadModel.ConcentratedHeatFlux "abaqus.Load.LoadModel.ConcentratedHeatFlux.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.ConcentratedHeatFlux "abaqus.Load.LoadModel.ConcentratedHeatFlux.__init__.field (Python parameter)")=`''`*, *[amplitude](#abaqus.Load.LoadModel.ConcentratedHeatFlux "abaqus.Load.LoadModel.ConcentratedHeatFlux.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[dof](#abaqus.Load.LoadModel.ConcentratedHeatFlux "abaqus.Load.LoadModel.ConcentratedHeatFlux.__init__.dof (Python parameter)")=`11`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L13-L144)[¶](#abaqus.Load.LoadModel.ConcentratedHeatFlux "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The ConcentratedHeatFlux object stores the data for a concentrated heat flux load. The
    ConcentratedHeatFlux object is derived from the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [ConcentratedHeatFlux on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concentratedheatfluxpyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L28-L30)[¶](#abaqus.Load.LoadModel.ConcentratedHeatFlux.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
        UNIFORM and FIELD. The default value is UNIFORM.

    dof : --is-rst--:py:class:`int` = `11`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L32-L34)[¶](#abaqus.Load.LoadModel.ConcentratedHeatFlux.dof "Permalink to this definition")
    :   An Int specifying the degree of freedom of the node, to which the concentrated heat flux
        should be applied. The default value is 11.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L36-L39)[¶](#abaqus.Load.LoadModel.ConcentratedHeatFlux.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L25-L26)[¶](#abaqus.Load.LoadModel.ConcentratedHeatFlux.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L41-L42)[¶](#abaqus.Load.LoadModel.ConcentratedHeatFlux.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[distributionType](#abaqus.Load.LoadModel.ConcentratedHeatFlux.setValues.distributionType "abaqus.Load.LoadModel.ConcentratedHeatFlux.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.ConcentratedHeatFlux.setValues.field "abaqus.Load.LoadModel.ConcentratedHeatFlux.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[amplitude](#abaqus.Load.LoadModel.ConcentratedHeatFlux.setValues.amplitude "abaqus.Load.LoadModel.ConcentratedHeatFlux.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*, *[dof](#abaqus.Load.LoadModel.ConcentratedHeatFlux.setValues.dof "abaqus.Load.LoadModel.ConcentratedHeatFlux.setValues.dof (Python parameter) — An Int specifying the degree of freedom of the node, to which the concentrated heat flux should be applied.")=`11`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L96-L124)[¶](#abaqus.Load.LoadModel.ConcentratedHeatFlux.setValues "Permalink to this definition")
    :   This method modifies the data for an existing ConcentratedHeatFlux object in the step where it is
        created.

        Note

        Check [ConcentratedHeatFlux.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concentratedheatfluxpyc.htm?contextscope=all#simaker-concentratedheatfluxsetvaluespyc).

        Parameters:[¶](#abaqus.Load.LoadModel.ConcentratedHeatFlux.setValues-parameters "Permalink to this headline")
        :   distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.ConcentratedHeatFlux.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.ConcentratedHeatFlux.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.ConcentratedHeatFlux.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

            dof=`11`[¶](#abaqus.Load.LoadModel.ConcentratedHeatFlux.setValues.dof "Permalink to this definition")
            :   An Int specifying the degree of freedom of the node, to which the concentrated heat flux
                should be applied. The default value is 11.

    setValuesInStep(*[stepName](#abaqus.Load.LoadModel.ConcentratedHeatFlux.setValuesInStep.stepName "abaqus.Load.LoadModel.ConcentratedHeatFlux.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[magnitude](#abaqus.Load.LoadModel.ConcentratedHeatFlux.setValuesInStep.magnitude "abaqus.Load.LoadModel.ConcentratedHeatFlux.setValuesInStep.magnitude (Python parameter) — A Float specifying the load magnitude.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.ConcentratedHeatFlux.setValuesInStep.amplitude "abaqus.Load.LoadModel.ConcentratedHeatFlux.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L126-L144)[¶](#abaqus.Load.LoadModel.ConcentratedHeatFlux.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing ConcentratedHeatFlux object in the
        specified step.

        Note

        Check [ConcentratedHeatFlux.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concentratedheatfluxpyc.htm?contextscope=all#simaker-concentratedheatfluxsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.LoadModel.ConcentratedHeatFlux.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.LoadModel.ConcentratedHeatFlux.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            magnitude=`None`[¶](#abaqus.Load.LoadModel.ConcentratedHeatFlux.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float specifying the load magnitude.

            amplitude=`''`[¶](#abaqus.Load.LoadModel.ConcentratedHeatFlux.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous static analysis step. FREED should be used if
                the load is changed to have no amplitude reference. You should provide the **amplitude**
                argument only if it is valid for the specified step.

*class* ConcentratedHeatFluxState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedHeatFluxState.py#L9-L55)[¶](#abaqus.Load.ConcentratedHeatFluxState.ConcentratedHeatFluxState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The ConcentratedHeatFluxState object stores the propagating data of a concentrated heat flux load in a
    step. One instance of this object is created internally by the ConcentratedHeatFlux object for each step.
    The instance is also deleted internally by the ConcentratedHeatFlux object. The ConcentratedHeatFluxState
    object has no constructor or methods. The ConcentratedHeatFluxState object is derived from the LoadState
    object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * CFLUX

    Note

    Check [ConcentratedHeatFluxState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concentratedheatfluxstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedHeatFluxState.py#L9-L55)[¶](#abaqus.Load.ConcentratedHeatFluxState.ConcentratedHeatFluxState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedHeatFluxState.py)[¶](#abaqus.Load.ConcentratedHeatFluxState.ConcentratedHeatFluxState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedHeatFluxState.py#L28-L29)[¶](#abaqus.Load.ConcentratedHeatFluxState.ConcentratedHeatFluxState.magnitude "Permalink to this definition")
    :   A Float specifying the load magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedHeatFluxState.py)[¶](#abaqus.Load.ConcentratedHeatFluxState.ConcentratedHeatFluxState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load magnitude. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedHeatFluxState.py)[¶](#abaqus.Load.ConcentratedHeatFluxState.ConcentratedHeatFluxState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* ConcentratedPoreFluidState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedPoreFluidState.py#L9-L54)[¶](#abaqus.Load.ConcentratedPoreFluidState.ConcentratedPoreFluidState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The ConcentratedPoreFluidState object stores the propagating data of a concentrated pore fluid flow load
    in a step. One instance of this object is created internally by the ConcPoreFluid object for each step. The
    instance is also deleted internally by the ConcPoreFluid object. The ConcentratedPoreFluidState object has
    no constructor or methods. The ConcentratedPoreFluidState object is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * CLOAD

    Note

    Check [ConcentratedPoreFluidState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concentratedporefluidstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedPoreFluidState.py#L9-L54)[¶](#abaqus.Load.ConcentratedPoreFluidState.ConcentratedPoreFluidState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedPoreFluidState.py)[¶](#abaqus.Load.ConcentratedPoreFluidState.ConcentratedPoreFluidState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedPoreFluidState.py#L27-L28)[¶](#abaqus.Load.ConcentratedPoreFluidState.ConcentratedPoreFluidState.magnitude "Permalink to this definition")
    :   A Float specifying the load magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedPoreFluidState.py)[¶](#abaqus.Load.ConcentratedPoreFluidState.ConcentratedPoreFluidState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load magnitude. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConcentratedPoreFluidState.py)[¶](#abaqus.Load.ConcentratedPoreFluidState.ConcentratedPoreFluidState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* ConnectorForce(*[name](#abaqus.Load.LoadModel.ConnectorForce "abaqus.Load.LoadModel.ConnectorForce.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.LoadModel.ConnectorForce "abaqus.Load.LoadModel.ConnectorForce.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.LoadModel.ConnectorForce "abaqus.Load.LoadModel.ConnectorForce.__init__.region (Python parameter)")=`''`*, *[fastenerName](#abaqus.Load.LoadModel.ConnectorForce "abaqus.Load.LoadModel.ConnectorForce.__init__.fastenerName (Python parameter)")=`''`*, *[fastenerSetName](#abaqus.Load.LoadModel.ConnectorForce "abaqus.Load.LoadModel.ConnectorForce.__init__.fastenerSetName (Python parameter)")=`''`*, *[f1](#abaqus.Load.LoadModel.ConnectorForce "abaqus.Load.LoadModel.ConnectorForce.__init__.f1 (Python parameter)")=`None`*, *[f2](#abaqus.Load.LoadModel.ConnectorForce "abaqus.Load.LoadModel.ConnectorForce.__init__.f2 (Python parameter)")=`None`*, *[f3](#abaqus.Load.LoadModel.ConnectorForce "abaqus.Load.LoadModel.ConnectorForce.__init__.f3 (Python parameter)")=`None`*, *[amplitude](#abaqus.Load.LoadModel.ConnectorForce "abaqus.Load.LoadModel.ConnectorForce.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L15-L184)[¶](#abaqus.Load.LoadModel.ConnectorForce "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The ConnectorForce object defines a connector force. The ConnectorForce object is derived from the Load
    object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [ConnectorForce on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorforcepyc.htm?contextscope=all).

    Member Details:

    fastenerName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L30-L34)[¶](#abaqus.Load.LoadModel.ConnectorForce.fastenerName "Permalink to this definition")
    :   A String specifying the name of the assembled fastener to which the load will be
        applied. This argument is not valid when **region** is specified. When this argument is
        specified, **fastenerSetName** must also be specified. The default value is an empty
        string.

    fastenerSetName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L36-L39)[¶](#abaqus.Load.LoadModel.ConnectorForce.fastenerSetName "Permalink to this definition")
    :   A String specifying the assembled fastener template model set to which the load will be
        applied. This argument is not valid when **region** is specified. When this argument is
        specified, **fastenerName** must also be specified. The default value is an empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L27-L28)[¶](#abaqus.Load.LoadModel.ConnectorForce.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L41-L42)[¶](#abaqus.Load.LoadModel.ConnectorForce.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[region](#abaqus.Load.LoadModel.ConnectorForce.setValues.region "abaqus.Load.LoadModel.ConnectorForce.setValues.region (Python parameter) — The wire region to which the load is applied.")=`''`*, *[fastenerName](#abaqus.Load.LoadModel.ConnectorForce.setValues.fastenerName "abaqus.Load.LoadModel.ConnectorForce.setValues.fastenerName (Python parameter) — A String specifying the name of the assembled fastener to which the load will be applied.")=`''`*, *[fastenerSetName](#abaqus.Load.LoadModel.ConnectorForce.setValues.fastenerSetName "abaqus.Load.LoadModel.ConnectorForce.setValues.fastenerSetName (Python parameter) — A String specifying the assembled fastener template model set to which the load will be applied.")=`''`*, *[f1](#abaqus.Load.LoadModel.ConnectorForce.setValues.f1 "abaqus.Load.LoadModel.ConnectorForce.setValues.f1 (Python parameter) — A Float or a Complex specifying the connector force component in the connector's local 1-direction.")=`None`*, *[f2](#abaqus.Load.LoadModel.ConnectorForce.setValues.f2 "abaqus.Load.LoadModel.ConnectorForce.setValues.f2 (Python parameter) — A Float or a Complex specifying the connector force component in the connector's local 2-direction.")=`None`*, *[f3](#abaqus.Load.LoadModel.ConnectorForce.setValues.f3 "abaqus.Load.LoadModel.ConnectorForce.setValues.f3 (Python parameter) — A Float or a Complex specifying the connector force component in the connector's local 3-direction.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.ConnectorForce.setValues.amplitude "abaqus.Load.LoadModel.ConnectorForce.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L105-L147)[¶](#abaqus.Load.LoadModel.ConnectorForce.setValues "Permalink to this definition")
    :   This method modifies the data for an existing ConnectorForce object in the step where it is created.

        Note

        Check [ConnectorForce.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorforcepyc.htm?contextscope=all#simaker-connectorforcesetvaluespyc).

        Parameters:[¶](#abaqus.Load.LoadModel.ConnectorForce.setValues-parameters "Permalink to this headline")
        :   region=`''`[¶](#abaqus.Load.LoadModel.ConnectorForce.setValues.region "Permalink to this definition")
            :   The wire region to which the load is applied. This argument is not valid when
                **fastenerName** and **fastenerSetName** are specified.

            fastenerName=`''`[¶](#abaqus.Load.LoadModel.ConnectorForce.setValues.fastenerName "Permalink to this definition")
            :   A String specifying the name of the assembled fastener to which the load will be
                applied. This argument is not valid when **region** is specified. When this argument is
                specified, **fastenerSetName** must also be specified. The default value is an empty
                string.

            fastenerSetName=`''`[¶](#abaqus.Load.LoadModel.ConnectorForce.setValues.fastenerSetName "Permalink to this definition")
            :   A String specifying the assembled fastener template model set to which the load will be
                applied. This argument is not valid when **region** is specified. When this argument is
                specified, **fastenerName** must also be specified. The default value is an empty string.

            f1=`None`[¶](#abaqus.Load.LoadModel.ConnectorForce.setValues.f1 "Permalink to this definition")
            :   A Float or a Complex specifying the connector force component in the connector’s local
                1-direction. Note: Although **f1**, **f2**, and **f3** are optional arguments, at least one of
                them must be nonzero.

            f2=`None`[¶](#abaqus.Load.LoadModel.ConnectorForce.setValues.f2 "Permalink to this definition")
            :   A Float or a Complex specifying the connector force component in the connector’s local
                2-direction.

            f3=`None`[¶](#abaqus.Load.LoadModel.ConnectorForce.setValues.f3 "Permalink to this definition")
            :   A Float or a Complex specifying the connector force component in the connector’s local
                3-direction.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.ConnectorForce.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

    setValuesInStep(*[stepName](#abaqus.Load.LoadModel.ConnectorForce.setValuesInStep.stepName "abaqus.Load.LoadModel.ConnectorForce.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[f1](#abaqus.Load.LoadModel.ConnectorForce.setValuesInStep.f1 "abaqus.Load.LoadModel.ConnectorForce.setValuesInStep.f1 (Python parameter) — A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the connector force component in the connector's local 1-direction.")=`Ellipsis`*, *[f2](#abaqus.Load.LoadModel.ConnectorForce.setValuesInStep.f2 "abaqus.Load.LoadModel.ConnectorForce.setValuesInStep.f2 (Python parameter) — A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the connector force component in the connector's local 2-direction.")=`Ellipsis`*, *[f3](#abaqus.Load.LoadModel.ConnectorForce.setValuesInStep.f3 "abaqus.Load.LoadModel.ConnectorForce.setValuesInStep.f3 (Python parameter) — A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the connector force component in the connector's local 3-direction.")=`Ellipsis`*, *[amplitude](#abaqus.Load.LoadModel.ConnectorForce.setValuesInStep.amplitude "abaqus.Load.LoadModel.ConnectorForce.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L149-L184)[¶](#abaqus.Load.LoadModel.ConnectorForce.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing ConnectorForce object in the specified
        step.

        Note

        Check [ConnectorForce.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorforcepyc.htm?contextscope=all#simaker-connectorforcesetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.LoadModel.ConnectorForce.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.LoadModel.ConnectorForce.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            f1=`Ellipsis`[¶](#abaqus.Load.LoadModel.ConnectorForce.setValuesInStep.f1 "Permalink to this definition")
            :   A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the connector force
                component in the connector’s local 1-direction. UNCHANGED should be used if the
                connector force component is propagated from the previous analysis step.

            f2=`Ellipsis`[¶](#abaqus.Load.LoadModel.ConnectorForce.setValuesInStep.f2 "Permalink to this definition")
            :   A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the connector force
                component in the connector’s local 2-direction. UNCHANGED should be used if the
                connector force component is propagated from the previous analysis step.

            f3=`Ellipsis`[¶](#abaqus.Load.LoadModel.ConnectorForce.setValuesInStep.f3 "Permalink to this definition")
            :   A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the connector force
                component in the connector’s local 3-direction. UNCHANGED should be used if the
                connector force component is propagated from the previous analysis step.

            amplitude=`''`[¶](#abaqus.Load.LoadModel.ConnectorForce.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                load is changed to have no amplitude reference. You should provide the **amplitude**
                argument only if it is valid for the specified step.

*class* ConnectorForceState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConnectorForceState.py#L9-L74)[¶](#abaqus.Load.ConnectorForceState.ConnectorForceState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The ConnectorForceState object stores the propagating data for a connector force in a step. One instance
    of this object is created internally by the ConnectorForce object for each step. The instance is also
    deleted internally by the ConnectorForce object. The ConnectorForceState object has no constructor or
    methods. The ConnectorForceState object is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * CONNECTOR LOAD

    Note

    Check [ConnectorForceState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectorforcestatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConnectorForceState.py#L9-L74)[¶](#abaqus.Load.ConnectorForceState.ConnectorForceState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConnectorForceState.py)[¶](#abaqus.Load.ConnectorForceState.ConnectorForceState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    f1 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConnectorForceState.py#L27-L29)[¶](#abaqus.Load.ConnectorForceState.ConnectorForceState.f1 "Permalink to this definition")
    :   A Float or a Complex specifying the connector force component in the connector’s local
        1-direction.

    f1State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConnectorForceState.py)[¶](#abaqus.Load.ConnectorForceState.ConnectorForceState.f1State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the connector force component in
        the connector’s local 1-direction. Possible values are UNSET, SET, UNCHANGED, and
        MODIFIED.

    f2 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConnectorForceState.py#L27-L29)[¶](#abaqus.Load.ConnectorForceState.ConnectorForceState.f2 "Permalink to this definition")
    :   A Float or a Complex specifying the connector force component in the connector’s local
        2-direction.

    f2State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConnectorForceState.py)[¶](#abaqus.Load.ConnectorForceState.ConnectorForceState.f2State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the connector force component in
        the connector’s local 2-direction. Possible values are UNSET, SET, UNCHANGED, and
        MODIFIED.

    f3 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConnectorForceState.py#L27-L29)[¶](#abaqus.Load.ConnectorForceState.ConnectorForceState.f3 "Permalink to this definition")
    :   A Float or a Complex specifying the connector force component in the connector’s local
        3-direction.

    f3State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConnectorForceState.py)[¶](#abaqus.Load.ConnectorForceState.ConnectorForceState.f3State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the connector force component in
        the connector’s local 3-direction. Possible values are UNSET, SET, UNCHANGED, and
        MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConnectorForceState.py)[¶](#abaqus.Load.ConnectorForceState.ConnectorForceState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* ConnectorMoment(*[name](#abaqus.Load.LoadModel.ConnectorMoment "abaqus.Load.LoadModel.ConnectorMoment.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.LoadModel.ConnectorMoment "abaqus.Load.LoadModel.ConnectorMoment.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.LoadModel.ConnectorMoment "abaqus.Load.LoadModel.ConnectorMoment.__init__.region (Python parameter)")=`''`*, *[fastenerName](#abaqus.Load.LoadModel.ConnectorMoment "abaqus.Load.LoadModel.ConnectorMoment.__init__.fastenerName (Python parameter)")=`''`*, *[fastenerSetName](#abaqus.Load.LoadModel.ConnectorMoment "abaqus.Load.LoadModel.ConnectorMoment.__init__.fastenerSetName (Python parameter)")=`''`*, *[m1](#abaqus.Load.LoadModel.ConnectorMoment "abaqus.Load.LoadModel.ConnectorMoment.__init__.m1 (Python parameter)")=`None`*, *[m2](#abaqus.Load.LoadModel.ConnectorMoment "abaqus.Load.LoadModel.ConnectorMoment.__init__.m2 (Python parameter)")=`None`*, *[m3](#abaqus.Load.LoadModel.ConnectorMoment "abaqus.Load.LoadModel.ConnectorMoment.__init__.m3 (Python parameter)")=`None`*, *[amplitude](#abaqus.Load.LoadModel.ConnectorMoment "abaqus.Load.LoadModel.ConnectorMoment.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L15-L185)[¶](#abaqus.Load.LoadModel.ConnectorMoment "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The ConnectorMoment object stores the data for a connector moment. The ConnectorMoment object is derived
    from the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [ConnectorMoment on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectormomentpyc.htm?contextscope=all).

    Member Details:

    fastenerName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L30-L34)[¶](#abaqus.Load.LoadModel.ConnectorMoment.fastenerName "Permalink to this definition")
    :   A String specifying the name of the assembled fastener to which the load will be
        applied. This argument is not valid when **region** is specified. When this argument is
        specified, **fastenerSetName** must also be specified. The default value is an empty
        string.

    fastenerSetName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L36-L39)[¶](#abaqus.Load.LoadModel.ConnectorMoment.fastenerSetName "Permalink to this definition")
    :   A String specifying the assembled fastener template model set to which the load will be
        applied. This argument is not valid when **region** is specified. When this argument is
        specified, **fastenerName** must also be specified. The default value is an empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L27-L28)[¶](#abaqus.Load.LoadModel.ConnectorMoment.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L41-L42)[¶](#abaqus.Load.LoadModel.ConnectorMoment.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[region](#abaqus.Load.LoadModel.ConnectorMoment.setValues.region "abaqus.Load.LoadModel.ConnectorMoment.setValues.region (Python parameter) — The wire region to which the load is applied.")=`''`*, *[fastenerName](#abaqus.Load.LoadModel.ConnectorMoment.setValues.fastenerName "abaqus.Load.LoadModel.ConnectorMoment.setValues.fastenerName (Python parameter) — A String specifying the name of the assembled fastener to which the load will be applied.")=`''`*, *[fastenerSetName](#abaqus.Load.LoadModel.ConnectorMoment.setValues.fastenerSetName "abaqus.Load.LoadModel.ConnectorMoment.setValues.fastenerSetName (Python parameter) — A String specifying the assembled fastener template model set to which the load will be applied.")=`''`*, *[m1](#abaqus.Load.LoadModel.ConnectorMoment.setValues.m1 "abaqus.Load.LoadModel.ConnectorMoment.setValues.m1 (Python parameter) — A Float or a Complex specifying the moment component in the connector's local 4-direction.")=`None`*, *[m2](#abaqus.Load.LoadModel.ConnectorMoment.setValues.m2 "abaqus.Load.LoadModel.ConnectorMoment.setValues.m2 (Python parameter) — A Float or a Complex specifying the moment component in the connector's local 5-direction.")=`None`*, *[m3](#abaqus.Load.LoadModel.ConnectorMoment.setValues.m3 "abaqus.Load.LoadModel.ConnectorMoment.setValues.m3 (Python parameter) — A Float or a Complex specifying the moment component in the connector's local 6-direction.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.ConnectorMoment.setValues.amplitude "abaqus.Load.LoadModel.ConnectorMoment.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L104-L145)[¶](#abaqus.Load.LoadModel.ConnectorMoment.setValues "Permalink to this definition")
    :   This method modifies the data for an existing ConnectorMoment object in the step where it is created.

        Note

        Check [ConnectorMoment.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectormomentpyc.htm?contextscope=all#simaker-connectormomentsetvaluespyc).

        Parameters:[¶](#abaqus.Load.LoadModel.ConnectorMoment.setValues-parameters "Permalink to this headline")
        :   region=`''`[¶](#abaqus.Load.LoadModel.ConnectorMoment.setValues.region "Permalink to this definition")
            :   The wire region to which the load is applied. This argument is not valid when
                **fastenerName** and **fastenerSetName** are specified.

            fastenerName=`''`[¶](#abaqus.Load.LoadModel.ConnectorMoment.setValues.fastenerName "Permalink to this definition")
            :   A String specifying the name of the assembled fastener to which the load will be
                applied. This argument is not valid when **region** is specified. When this argument is
                specified, **fastenerSetName** must also be specified. The default value is an empty
                string.

            fastenerSetName=`''`[¶](#abaqus.Load.LoadModel.ConnectorMoment.setValues.fastenerSetName "Permalink to this definition")
            :   A String specifying the assembled fastener template model set to which the load will be
                applied. This argument is not valid when **region** is specified. When this argument is
                specified, **fastenerName** must also be specified. The default value is an empty string.

            m1=`None`[¶](#abaqus.Load.LoadModel.ConnectorMoment.setValues.m1 "Permalink to this definition")
            :   A Float or a Complex specifying the moment component in the connector’s local
                4-direction.

            m2=`None`[¶](#abaqus.Load.LoadModel.ConnectorMoment.setValues.m2 "Permalink to this definition")
            :   A Float or a Complex specifying the moment component in the connector’s local
                5-direction.

            m3=`None`[¶](#abaqus.Load.LoadModel.ConnectorMoment.setValues.m3 "Permalink to this definition")
            :   A Float or a Complex specifying the moment component in the connector’s local
                6-direction.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.ConnectorMoment.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

    setValuesInStep(*[stepName](#abaqus.Load.LoadModel.ConnectorMoment.setValuesInStep.stepName "abaqus.Load.LoadModel.ConnectorMoment.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[m1](#abaqus.Load.LoadModel.ConnectorMoment.setValuesInStep.m1 "abaqus.Load.LoadModel.ConnectorMoment.setValuesInStep.m1 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the moment component in the connector's local 4-direction.")=`Ellipsis`*, *[m2](#abaqus.Load.LoadModel.ConnectorMoment.setValuesInStep.m2 "abaqus.Load.LoadModel.ConnectorMoment.setValuesInStep.m2 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the moment component in the connector's local 5-direction.")=`Ellipsis`*, *[m3](#abaqus.Load.LoadModel.ConnectorMoment.setValuesInStep.m3 "abaqus.Load.LoadModel.ConnectorMoment.setValuesInStep.m3 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the moment component in the connector's local 6-direction.")=`Ellipsis`*, *[amplitude](#abaqus.Load.LoadModel.ConnectorMoment.setValuesInStep.amplitude "abaqus.Load.LoadModel.ConnectorMoment.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L147-L185)[¶](#abaqus.Load.LoadModel.ConnectorMoment.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing ConnectorMoment object in the specified
        step.

        Note

        Check [ConnectorMoment.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectormomentpyc.htm?contextscope=all#simaker-connectormomentsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.LoadModel.ConnectorMoment.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.LoadModel.ConnectorMoment.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            m1=`Ellipsis`[¶](#abaqus.Load.LoadModel.ConnectorMoment.setValuesInStep.m1 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the moment component in the
                connector’s local 4-direction. Possible values for the SymbolicConstant are UNCHANGED
                and FREED. UNCHANGED should be used if the load component is propagated from the
                previous static analysis step. Use FREED to remove a previously defined load component.

            m2=`Ellipsis`[¶](#abaqus.Load.LoadModel.ConnectorMoment.setValuesInStep.m2 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the moment component in the
                connector’s local 5-direction. Possible values for the SymbolicConstant are UNCHANGED
                and FREED. UNCHANGED should be used if the load component is propagated from the
                previous static analysis step. Use FREED to remove a previously defined load component.

            m3=`Ellipsis`[¶](#abaqus.Load.LoadModel.ConnectorMoment.setValuesInStep.m3 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the moment component in the
                connector’s local 6-direction. Possible values for the SymbolicConstant are UNCHANGED
                and FREED. UNCHANGED should be used if the load component is propagated from the
                previous static analysis step. Use FREED to remove a previously defined load component.

            amplitude=`''`[¶](#abaqus.Load.LoadModel.ConnectorMoment.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous static analysis step. FREED should be used if
                the load is changed to have no amplitude reference. You should provide the **amplitude**
                argument only if it is valid for the specified step.

*class* ConnectorMomentState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConnectorMomentState.py#L9-L72)[¶](#abaqus.Load.ConnectorMomentState.ConnectorMomentState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The ConnectorMomentState object stores the propagating data for a connector moment in a step. One
    instance of this object is created internally by the ConnectorMoment object for each step. The instance is
    also deleted internally by the ConnectorMoment object. The ConnectorMomentState object has no constructor or
    methods. The ConnectorMomentState object is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * CONNECTOR LOAD

    Note

    Check [ConnectorMomentState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectormomentstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConnectorMomentState.py#L9-L72)[¶](#abaqus.Load.ConnectorMomentState.ConnectorMomentState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConnectorMomentState.py)[¶](#abaqus.Load.ConnectorMomentState.ConnectorMomentState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    m1 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConnectorMomentState.py#L27-L30)[¶](#abaqus.Load.ConnectorMomentState.ConnectorMomentState.m1 "Permalink to this definition")
    :   A Float or a Complex specifying the connector moment component in the connector’s local
        4-direction. Although **m1**, **m2**, and **m3** are optional arguments, at least one of them
        must be nonzero.

    m1State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConnectorMomentState.py)[¶](#abaqus.Load.ConnectorMomentState.ConnectorMomentState.m1State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load component in the
        connector’s local 4-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.

    m2 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConnectorMomentState.py#L27-L29)[¶](#abaqus.Load.ConnectorMomentState.ConnectorMomentState.m2 "Permalink to this definition")
    :   A Float or a Complex specifying the connector moment component in the connector’s local
        5direction.

    m2State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConnectorMomentState.py)[¶](#abaqus.Load.ConnectorMomentState.ConnectorMomentState.m2State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load component in the
        connector’s local 5-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.

    m3 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConnectorMomentState.py#L27-L29)[¶](#abaqus.Load.ConnectorMomentState.ConnectorMomentState.m3 "Permalink to this definition")
    :   A Float or a Complex specifying the connector moment component in the connector’s local
        6-direction.

    m3State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConnectorMomentState.py)[¶](#abaqus.Load.ConnectorMomentState.ConnectorMomentState.m3State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load component in the
        connector’s local 6-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ConnectorMomentState.py)[¶](#abaqus.Load.ConnectorMomentState.ConnectorMomentState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* CoriolisForce(*[name](#abaqus.Load.LoadModel.CoriolisForce "abaqus.Load.LoadModel.CoriolisForce.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.LoadModel.CoriolisForce "abaqus.Load.LoadModel.CoriolisForce.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.LoadModel.CoriolisForce "abaqus.Load.LoadModel.CoriolisForce.__init__.region (Python parameter)")*, *[magnitude](#abaqus.Load.LoadModel.CoriolisForce "abaqus.Load.LoadModel.CoriolisForce.__init__.magnitude (Python parameter)")*, *[point1](#abaqus.Load.LoadModel.CoriolisForce "abaqus.Load.LoadModel.CoriolisForce.__init__.point1 (Python parameter)")*, *[point2](#abaqus.Load.LoadModel.CoriolisForce "abaqus.Load.LoadModel.CoriolisForce.__init__.point2 (Python parameter)")*, *[amplitude](#abaqus.Load.LoadModel.CoriolisForce "abaqus.Load.LoadModel.CoriolisForce.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.Load.LoadModel.CoriolisForce "abaqus.Load.LoadModel.CoriolisForce.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.CoriolisForce "abaqus.Load.LoadModel.CoriolisForce.__init__.field (Python parameter)")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L13-L142)[¶](#abaqus.Load.LoadModel.CoriolisForce "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The CoriolisForce object stores the data for a coriolis force. The CoriolisForce object is derived from
    the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [CoriolisForce on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-coriolisforcepyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L28-L30)[¶](#abaqus.Load.LoadModel.CoriolisForce.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
        UNIFORM and FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L38-L41)[¶](#abaqus.Load.LoadModel.CoriolisForce.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L25-L26)[¶](#abaqus.Load.LoadModel.CoriolisForce.name "Permalink to this definition")
    :   A String specifying the load repository key.

    point1 : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L32-L33)[¶](#abaqus.Load.LoadModel.CoriolisForce.point1 "Permalink to this definition")
    :   A tuple of Floats specifying the first point on the axis of rotation for the load.

    point2 : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L35-L36)[¶](#abaqus.Load.LoadModel.CoriolisForce.point2 "Permalink to this definition")
    :   A tuple of Floats specifying the second point on the axis of rotation for the load.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L43-L44)[¶](#abaqus.Load.LoadModel.CoriolisForce.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[amplitude](#abaqus.Load.LoadModel.CoriolisForce.setValues.amplitude "abaqus.Load.LoadModel.CoriolisForce.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.Load.LoadModel.CoriolisForce.setValues.distributionType "abaqus.Load.LoadModel.CoriolisForce.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.CoriolisForce.setValues.field "abaqus.Load.LoadModel.CoriolisForce.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L100-L123)[¶](#abaqus.Load.LoadModel.CoriolisForce.setValues "Permalink to this definition")
    :   This method modifies the data for an existing CoriolisForce object in the step where it is created.

        Note

        Check [CoriolisForce.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-coriolisforcepyc.htm?contextscope=all#simaker-coriolisforcesetvaluespyc).

        Parameters:[¶](#abaqus.Load.LoadModel.CoriolisForce.setValues-parameters "Permalink to this headline")
        :   amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.CoriolisForce.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.CoriolisForce.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.CoriolisForce.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

    setValuesInStep(*[stepName](#abaqus.Load.LoadModel.CoriolisForce.setValuesInStep.stepName "abaqus.Load.LoadModel.CoriolisForce.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[magnitude](#abaqus.Load.LoadModel.CoriolisForce.setValuesInStep.magnitude "abaqus.Load.LoadModel.CoriolisForce.setValuesInStep.magnitude (Python parameter) — A Float specifying the load magnitude.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.CoriolisForce.setValuesInStep.amplitude "abaqus.Load.LoadModel.CoriolisForce.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L125-L142)[¶](#abaqus.Load.LoadModel.CoriolisForce.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing CoriolisForce object in the specified step.

        Note

        Check [CoriolisForce.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-coriolisforcepyc.htm?contextscope=all#simaker-coriolisforcesetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.LoadModel.CoriolisForce.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.LoadModel.CoriolisForce.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            magnitude=`None`[¶](#abaqus.Load.LoadModel.CoriolisForce.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float specifying the load magnitude.

            amplitude=`''`[¶](#abaqus.Load.LoadModel.CoriolisForce.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous static analysis step. FREED should be used if
                the load is changed to have no amplitude reference. You should provide the **amplitude**
                argument only if it is valid for the specified step.

*class* CoriolisForceState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/CoriolisForceState.py#L9-L54)[¶](#abaqus.Load.CoriolisForceState.CoriolisForceState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The CoriolisForceState object stores the propagating data of a coriolis force in a step. One instance of
    this object is created internally by the CoriolisForce object for each step. The instance is also deleted
    internally by the CoriolisForce object. The CoriolisForceState object has no constructor or methods. The
    CoriolisForceState object is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * DLOAD

    Note

    Check [CoriolisForceState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-coriolisforcestatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/CoriolisForceState.py#L9-L54)[¶](#abaqus.Load.CoriolisForceState.CoriolisForceState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/CoriolisForceState.py)[¶](#abaqus.Load.CoriolisForceState.CoriolisForceState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/CoriolisForceState.py#L27-L28)[¶](#abaqus.Load.CoriolisForceState.CoriolisForceState.magnitude "Permalink to this definition")
    :   A Float specifying the load magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/CoriolisForceState.py)[¶](#abaqus.Load.CoriolisForceState.CoriolisForceState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load magnitude. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/CoriolisForceState.py)[¶](#abaqus.Load.CoriolisForceState.CoriolisForceState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* Gravity(*[name](#abaqus.Load.LoadModel.Gravity "abaqus.Load.LoadModel.Gravity.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.LoadModel.Gravity "abaqus.Load.LoadModel.Gravity.__init__.createStepName (Python parameter)")*, *[distributionType](#abaqus.Load.LoadModel.Gravity "abaqus.Load.LoadModel.Gravity.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.Gravity "abaqus.Load.LoadModel.Gravity.__init__.field (Python parameter)")=`''`*, *[region](#abaqus.Load.LoadModel.Gravity "abaqus.Load.LoadModel.Gravity.__init__.region (Python parameter)")=`None`*, *[comp1](#abaqus.Load.LoadModel.Gravity "abaqus.Load.LoadModel.Gravity.__init__.comp1 (Python parameter)")=`None`*, *[comp2](#abaqus.Load.LoadModel.Gravity "abaqus.Load.LoadModel.Gravity.__init__.comp2 (Python parameter)")=`None`*, *[comp3](#abaqus.Load.LoadModel.Gravity "abaqus.Load.LoadModel.Gravity.__init__.comp3 (Python parameter)")=`None`*, *[amplitude](#abaqus.Load.LoadModel.Gravity "abaqus.Load.LoadModel.Gravity.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L15-L168)[¶](#abaqus.Load.LoadModel.Gravity "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The Gravity object stores the data of a gravity load. The Gravity object is derived from the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [Gravity on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gravitypyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L29-L31)[¶](#abaqus.Load.LoadModel.Gravity.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
        UNIFORM and FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L33-L36)[¶](#abaqus.Load.LoadModel.Gravity.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L26-L27)[¶](#abaqus.Load.LoadModel.Gravity.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L38-L39)[¶](#abaqus.Load.LoadModel.Gravity.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[distributionType](#abaqus.Load.LoadModel.Gravity.setValues.distributionType "abaqus.Load.LoadModel.Gravity.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.Gravity.setValues.field "abaqus.Load.LoadModel.Gravity.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[region](#abaqus.Load.LoadModel.Gravity.setValues.region "abaqus.Load.LoadModel.Gravity.setValues.region (Python parameter) — A Region object specifying the region to which the load is applied.")=`None`*, *[comp1](#abaqus.Load.LoadModel.Gravity.setValues.comp1 "abaqus.Load.LoadModel.Gravity.setValues.comp1 (Python parameter) — A Float or a Complex specifying the component of the load in the 1-direction.")=`None`*, *[comp2](#abaqus.Load.LoadModel.Gravity.setValues.comp2 "abaqus.Load.LoadModel.Gravity.setValues.comp2 (Python parameter) — A Float or a Complex specifying the component of the load in the 2-direction.")=`None`*, *[comp3](#abaqus.Load.LoadModel.Gravity.setValues.comp3 "abaqus.Load.LoadModel.Gravity.setValues.comp3 (Python parameter) — A Float or a Complex specifying the component of the load in the 3-direction.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.Gravity.setValues.amplitude "abaqus.Load.LoadModel.Gravity.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L96-L133)[¶](#abaqus.Load.LoadModel.Gravity.setValues "Permalink to this definition")
    :   This method modifies the data for an existing Gravity object in the step where it is created.

        Note

        Check [Gravity.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gravitypyc.htm?contextscope=all#simaker-gravitysetvaluespyc).

        Parameters:[¶](#abaqus.Load.LoadModel.Gravity.setValues-parameters "Permalink to this headline")
        :   distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.Gravity.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.Gravity.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            region=`None`[¶](#abaqus.Load.LoadModel.Gravity.setValues.region "Permalink to this definition")
            :   A Region object specifying the region to which the load is applied.

            comp1=`None`[¶](#abaqus.Load.LoadModel.Gravity.setValues.comp1 "Permalink to this definition")
            :   A Float or a Complex specifying the component of the load in the
                1-direction. Note: Although **comp1**, **comp2**, and **comp3** are optional arguments, at least
                one of them must be nonzero.

            comp2=`None`[¶](#abaqus.Load.LoadModel.Gravity.setValues.comp2 "Permalink to this definition")
            :   A Float or a Complex specifying the component of the load in the 2-direction.

            comp3=`None`[¶](#abaqus.Load.LoadModel.Gravity.setValues.comp3 "Permalink to this definition")
            :   A Float or a Complex specifying the component of the load in the 3-direction.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.Gravity.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

    setValuesInStep(*[stepName](#abaqus.Load.LoadModel.Gravity.setValuesInStep.stepName "abaqus.Load.LoadModel.Gravity.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[comp1](#abaqus.Load.LoadModel.Gravity.setValuesInStep.comp1 "abaqus.Load.LoadModel.Gravity.setValuesInStep.comp1 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the load component in the 1-direction.")=`Ellipsis`*, *[comp2](#abaqus.Load.LoadModel.Gravity.setValuesInStep.comp2 "abaqus.Load.LoadModel.Gravity.setValuesInStep.comp2 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the load component in the 2-direction.")=`Ellipsis`*, *[comp3](#abaqus.Load.LoadModel.Gravity.setValuesInStep.comp3 "abaqus.Load.LoadModel.Gravity.setValuesInStep.comp3 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the load component in the 3-direction.")=`Ellipsis`*, *[amplitude](#abaqus.Load.LoadModel.Gravity.setValuesInStep.amplitude "abaqus.Load.LoadModel.Gravity.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L135-L168)[¶](#abaqus.Load.LoadModel.Gravity.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing Gravity object in the specified step.

        Note

        Check [Gravity.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gravitypyc.htm?contextscope=all#simaker-gravitysetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.LoadModel.Gravity.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.LoadModel.Gravity.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            comp1=`Ellipsis`[¶](#abaqus.Load.LoadModel.Gravity.setValuesInStep.comp1 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the load component in the
                1-direction. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED
                should be used if the load component is propagated from the previous static analysis
                step. Use FREED to remove a previously defined load component.

            comp2=`Ellipsis`[¶](#abaqus.Load.LoadModel.Gravity.setValuesInStep.comp2 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the load component in the
                2-direction. For details see **comp1**.

            comp3=`Ellipsis`[¶](#abaqus.Load.LoadModel.Gravity.setValuesInStep.comp3 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the load component in the
                3-direction. For details see **comp1**.

            amplitude=`''`[¶](#abaqus.Load.LoadModel.Gravity.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous static analysis step. FREED should be used if
                the load is changed to have no amplitude reference. You should provide the **amplitude**
                argument only if it is valid for the specified step.

*class* GravityState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/GravityState.py#L9-L68)[¶](#abaqus.Load.GravityState.GravityState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The GravityState object stores the propagating data for a gravity load in a step. One instance of this
    object is created internally by the Gravity object for each step. The instance is also deleted internally by
    the Gravity object. The GravityState object has no constructor or methods. The GravityState object is
    derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * DLOAD

    Note

    Check [GravityState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-gravitystatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/GravityState.py#L9-L68)[¶](#abaqus.Load.GravityState.GravityState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/GravityState.py)[¶](#abaqus.Load.GravityState.GravityState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    comp1 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/GravityState.py#L27-L28)[¶](#abaqus.Load.GravityState.GravityState.comp1 "Permalink to this definition")
    :   A Float or a Complex specifying the load component in the 1-direction.

    comp1State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/GravityState.py)[¶](#abaqus.Load.GravityState.GravityState.comp1State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load component in the
        1-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.

    comp2 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/GravityState.py#L30-L31)[¶](#abaqus.Load.GravityState.GravityState.comp2 "Permalink to this definition")
    :   A Float or a Complex specifying the load component in the 2-direction.

    comp2State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/GravityState.py)[¶](#abaqus.Load.GravityState.GravityState.comp2State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load component in the
        2-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.

    comp3 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/GravityState.py#L33-L34)[¶](#abaqus.Load.GravityState.GravityState.comp3 "Permalink to this definition")
    :   A Float or a Complex specifying the load component in the 3-direction.

    comp3State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/GravityState.py)[¶](#abaqus.Load.GravityState.GravityState.comp3State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load component in the
        3-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/GravityState.py)[¶](#abaqus.Load.GravityState.GravityState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* HydrostaticFluidFlowState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/HydrostaticFluidFlowState.py#L9-L55)[¶](#abaqus.Load.HydrostaticFluidFlowState.HydrostaticFluidFlowState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The HydrostaticFluidFlowState object stores the propagating data for a concentrated HydrostaticFluidFlow
    object in a step. One instance of this object is created internally by the HydrostaticFluidFlow object for
    each step. The instance is also deleted internally by the HydrostaticFluidFlow object. The
    HydrostaticFluidFlowState object has no constructor or methods. The HydrostaticFluidFlowState object is
    derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * FLUID FLUX

    Note

    Check [HydrostaticFluidFlowState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-hydrostaticfluidflowstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/HydrostaticFluidFlowState.py#L9-L55)[¶](#abaqus.Load.HydrostaticFluidFlowState.HydrostaticFluidFlowState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/HydrostaticFluidFlowState.py)[¶](#abaqus.Load.HydrostaticFluidFlowState.HydrostaticFluidFlowState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/HydrostaticFluidFlowState.py#L28-L29)[¶](#abaqus.Load.HydrostaticFluidFlowState.HydrostaticFluidFlowState.magnitude "Permalink to this definition")
    :   A Float specifying the load magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/HydrostaticFluidFlowState.py)[¶](#abaqus.Load.HydrostaticFluidFlowState.HydrostaticFluidFlowState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load magnitude. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/HydrostaticFluidFlowState.py)[¶](#abaqus.Load.HydrostaticFluidFlowState.HydrostaticFluidFlowState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* InertiaRelief(*[name](#abaqus.Load.LoadModel.InertiaRelief "abaqus.Load.LoadModel.InertiaRelief.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.LoadModel.InertiaRelief "abaqus.Load.LoadModel.InertiaRelief.__init__.createStepName (Python parameter)")*, *[u1](#abaqus.Load.LoadModel.InertiaRelief "abaqus.Load.LoadModel.InertiaRelief.__init__.u1 (Python parameter)")=`0`*, *[u2](#abaqus.Load.LoadModel.InertiaRelief "abaqus.Load.LoadModel.InertiaRelief.__init__.u2 (Python parameter)")=`0`*, *[u3](#abaqus.Load.LoadModel.InertiaRelief "abaqus.Load.LoadModel.InertiaRelief.__init__.u3 (Python parameter)")=`0`*, *[ur1](#abaqus.Load.LoadModel.InertiaRelief "abaqus.Load.LoadModel.InertiaRelief.__init__.ur1 (Python parameter)")=`0`*, *[ur2](#abaqus.Load.LoadModel.InertiaRelief "abaqus.Load.LoadModel.InertiaRelief.__init__.ur2 (Python parameter)")=`0`*, *[ur3](#abaqus.Load.LoadModel.InertiaRelief "abaqus.Load.LoadModel.InertiaRelief.__init__.ur3 (Python parameter)")=`0`*, *[referencePoint](#abaqus.Load.LoadModel.InertiaRelief "abaqus.Load.LoadModel.InertiaRelief.__init__.referencePoint (Python parameter)")=`()`*, *[localCoordinates](#abaqus.Load.LoadModel.InertiaRelief "abaqus.Load.LoadModel.InertiaRelief.__init__.localCoordinates (Python parameter)")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L10-L181)[¶](#abaqus.Load.LoadModel.InertiaRelief "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The InertiaRelief object defines an inertia relief load. The InertiaRelief object is derived from the
    Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [InertiaRelief on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-inertiareliefpyc.htm?contextscope=all).

    Member Details:

    localCoordinates : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L25-L29)[¶](#abaqus.Load.LoadModel.InertiaRelief.localCoordinates "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the rigid body
        degrees of freedom for the inertia relief load. If **localCoordinates** = None, the free
        directions are defined in the global coordinate system. When this member is queried, it
        returns an Int. The default value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L22-L23)[¶](#abaqus.Load.LoadModel.InertiaRelief.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L31-L32)[¶](#abaqus.Load.LoadModel.InertiaRelief.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[u1](#abaqus.Load.LoadModel.InertiaRelief.setValues.u1 "abaqus.Load.LoadModel.InertiaRelief.setValues.u1 (Python parameter) — A Boolean specifying the 1-direction as a free direction.")=`0`*, *[u2](#abaqus.Load.LoadModel.InertiaRelief.setValues.u2 "abaqus.Load.LoadModel.InertiaRelief.setValues.u2 (Python parameter) — A Boolean specifying the 2-direction as a free direction.")=`0`*, *[u3](#abaqus.Load.LoadModel.InertiaRelief.setValues.u3 "abaqus.Load.LoadModel.InertiaRelief.setValues.u3 (Python parameter) — A Boolean specifying the 3-direction as a free direction.")=`0`*, *[ur1](#abaqus.Load.LoadModel.InertiaRelief.setValues.ur1 "abaqus.Load.LoadModel.InertiaRelief.setValues.ur1 (Python parameter) — A Boolean specifying the rotation about the 1-direction as a free direction.")=`0`*, *[ur2](#abaqus.Load.LoadModel.InertiaRelief.setValues.ur2 "abaqus.Load.LoadModel.InertiaRelief.setValues.ur2 (Python parameter) — A Boolean specifying the rotation about the 2-direction as a free direction.")=`0`*, *[ur3](#abaqus.Load.LoadModel.InertiaRelief.setValues.ur3 "abaqus.Load.LoadModel.InertiaRelief.setValues.ur3 (Python parameter) — A Boolean specifying the rotation about the 3-direction as a free direction.")=`0`*, *[referencePoint](#abaqus.Load.LoadModel.InertiaRelief.setValues.referencePoint "abaqus.Load.LoadModel.InertiaRelief.setValues.referencePoint (Python parameter) — A sequence of Floats specifying the X, Y and Z coordinates of a fixed rotation point or a point on the rotation axis or a point on the symmetry line, about which rotations are defined.")=`()`*, *[localCoordinates](#abaqus.Load.LoadModel.InertiaRelief.setValues.localCoordinates "abaqus.Load.LoadModel.InertiaRelief.setValues.localCoordinates (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the rigid body degrees of freedom for the inertia relief load.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L94-L136)[¶](#abaqus.Load.LoadModel.InertiaRelief.setValues "Permalink to this definition")
    :   This method modifies the data for an existing InertiaRelief object in the step where it is created.

        Note

        Check [InertiaRelief.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-inertiareliefpyc.htm?contextscope=all#simaker-inertiareliefsetvaluespyc).

        Parameters:[¶](#abaqus.Load.LoadModel.InertiaRelief.setValues-parameters "Permalink to this headline")
        :   u1=`0`[¶](#abaqus.Load.LoadModel.InertiaRelief.setValues.u1 "Permalink to this definition")
            :   A Boolean specifying the 1-direction as a free direction. Note: Although **u1**, **u2**, **u3**,
                **ur1**, **ur2**, and **ur3** are optional arguments, at least one of them must be specified.
                Further, any specified set of free directions cannot include only two rotational degrees
                of freedom.

            u2=`0`[¶](#abaqus.Load.LoadModel.InertiaRelief.setValues.u2 "Permalink to this definition")
            :   A Boolean specifying the 2-direction as a free direction.

            u3=`0`[¶](#abaqus.Load.LoadModel.InertiaRelief.setValues.u3 "Permalink to this definition")
            :   A Boolean specifying the 3-direction as a free direction.

            ur1=`0`[¶](#abaqus.Load.LoadModel.InertiaRelief.setValues.ur1 "Permalink to this definition")
            :   A Boolean specifying the rotation about the 1-direction as a free direction.

            ur2=`0`[¶](#abaqus.Load.LoadModel.InertiaRelief.setValues.ur2 "Permalink to this definition")
            :   A Boolean specifying the rotation about the 2-direction as a free direction.

            ur3=`0`[¶](#abaqus.Load.LoadModel.InertiaRelief.setValues.ur3 "Permalink to this definition")
            :   A Boolean specifying the rotation about the 3-direction as a free direction.

            referencePoint=`()`[¶](#abaqus.Load.LoadModel.InertiaRelief.setValues.referencePoint "Permalink to this definition")
            :   A sequence of Floats specifying the **X**, **Y** and **Z** coordinates of a fixed rotation
                point or a point on the rotation axis or a point on the symmetry line, about which
                rotations are defined. Such a point must be specified only for certain combinations of
                free directions.

            localCoordinates=`None`[¶](#abaqus.Load.LoadModel.InertiaRelief.setValues.localCoordinates "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the rigid body
                degrees of freedom for the inertia relief load. If **localCoordinates** = None, the free
                directions are defined in the global coordinate system. When this member is queried, it
                returns an Int. The default value is None.

    setValuesInStep(*[stepName](#abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.stepName "abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[u1](#abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.u1 "abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.u1 (Python parameter) — A Boolean specifying the 1-direction as a free direction.")=`0`*, *[u2](#abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.u2 "abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.u2 (Python parameter) — A Boolean specifying the 2-direction as a free direction.")=`0`*, *[u3](#abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.u3 "abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.u3 (Python parameter) — A Boolean specifying the 3-direction as a free direction.")=`0`*, *[ur1](#abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.ur1 "abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.ur1 (Python parameter) — A Boolean specifying the rotation about the 1-direction as a free direction.")=`0`*, *[ur2](#abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.ur2 "abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.ur2 (Python parameter) — A Boolean specifying the rotation about the 2-direction as a free direction.")=`0`*, *[ur3](#abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.ur3 "abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.ur3 (Python parameter) — A Boolean specifying the rotation about the 3-direction as a free direction.")=`0`*, *[referencePoint](#abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.referencePoint "abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.referencePoint (Python parameter) — A sequence of Floats specifying the point about which rotations are defined.")=`()`*, *[fixed](#abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.fixed "abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.fixed (Python parameter) — A Boolean specifying whether the inertia relief loading should remain fixed at the current loading at the start of the step.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L138-L181)[¶](#abaqus.Load.LoadModel.InertiaRelief.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing InertiaRelief object in the specified step.

        Note

        Check [InertiaRelief.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-inertiareliefpyc.htm?contextscope=all#simaker-inertiareliefsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.LoadModel.InertiaRelief.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            u1=`0`[¶](#abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.u1 "Permalink to this definition")
            :   A Boolean specifying the 1-direction as a free direction.

            u2=`0`[¶](#abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.u2 "Permalink to this definition")
            :   A Boolean specifying the 2-direction as a free direction.

            u3=`0`[¶](#abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.u3 "Permalink to this definition")
            :   A Boolean specifying the 3-direction as a free direction.

            ur1=`0`[¶](#abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.ur1 "Permalink to this definition")
            :   A Boolean specifying the rotation about the 1-direction as a free direction.

            ur2=`0`[¶](#abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.ur2 "Permalink to this definition")
            :   A Boolean specifying the rotation about the 2-direction as a free direction.

            ur3=`0`[¶](#abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.ur3 "Permalink to this definition")
            :   A Boolean specifying the rotation about the 3-direction as a free direction.

            referencePoint=`()`[¶](#abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.referencePoint "Permalink to this definition")
            :   A sequence of Floats specifying the point about which rotations are defined. The point
                can be specified only for certain combinations of free directions. The **referencePoint**
                argument can be one of the following:

                * The **X**, **Y** and **Z** coordinates of a fixed rotation point.
                * A point on the rotation axis.
                * A point on the symmetry line.

            fixed=`0`[¶](#abaqus.Load.LoadModel.InertiaRelief.setValuesInStep.fixed "Permalink to this definition")
            :   A Boolean specifying whether the inertia relief loading should remain fixed at the
                current loading at the start of the step. The default value is OFF.

*class* InertiaReliefState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InertiaReliefState.py#L9-L117)[¶](#abaqus.Load.InertiaReliefState.InertiaReliefState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The InertiaReliefState object stores the propagating data for an inertia relief load in a step. One
    instance of this object is created internally by the InertiaRelief object for each step. The instance is
    also deleted internally by the InertiaRelief object. The InertiaReliefState object has no constructor or
    methods. The InertiaReliefState object is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * INERTIA RELIEF

    Note

    Check [InertiaReliefState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-inertiareliefstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InertiaReliefState.py#L9-L117)[¶](#abaqus.Load.InertiaReliefState.InertiaReliefState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InertiaReliefState.py)[¶](#abaqus.Load.InertiaReliefState.InertiaReliefState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    fixed : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InertiaReliefState.py#L75-L77)[¶](#abaqus.Load.InertiaReliefState.InertiaReliefState.fixed "Permalink to this definition")
    :   A Boolean specifying whether the inertia relief loading should remain fixed at the
        current loading at the start of the step. The default value is OFF.

    fixedState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InertiaReliefState.py)[¶](#abaqus.Load.InertiaReliefState.InertiaReliefState.fixedState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the Boolean that identifies
        whether the inertia relief load should remain fixed at current level at the start of the
        step. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

    referencePoint : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InertiaReliefState.py#L92-L95)[¶](#abaqus.Load.InertiaReliefState.InertiaReliefState.referencePoint "Permalink to this definition")
    :   A tuple of Floats specifying the point about which rotations are defined. The point can
        be specified only for certain combinations of free directions. The **referencePoint**
        argument can be one of the following:

        * The **X**, **Y** and **Z** coordinates of a fixed rotation point.
        * A point on the rotation axis.
        * A point on the symmetry line.

    referencePointState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InertiaReliefState.py)[¶](#abaqus.Load.InertiaReliefState.InertiaReliefState.referencePointState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the reference point of the
        inertia relief load. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InertiaReliefState.py)[¶](#abaqus.Load.InertiaReliefState.InertiaReliefState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

    u1 : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InertiaReliefState.py#L27-L28)[¶](#abaqus.Load.InertiaReliefState.InertiaReliefState.u1 "Permalink to this definition")
    :   A Boolean specifying the 1-direction as a free direction.

    u1State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InertiaReliefState.py)[¶](#abaqus.Load.InertiaReliefState.InertiaReliefState.u1State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the Boolean that identifies the
        local 1-direction as a free direction. Possible values are UNSET, SET, UNCHANGED, and
        MODIFIED.

    u2 : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InertiaReliefState.py#L30-L31)[¶](#abaqus.Load.InertiaReliefState.InertiaReliefState.u2 "Permalink to this definition")
    :   A Boolean specifying the 2-direction as a free direction.

    u2State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InertiaReliefState.py)[¶](#abaqus.Load.InertiaReliefState.InertiaReliefState.u2State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the Boolean that identifies the
        local 2-direction as a free direction. Possible values are UNSET, SET, UNCHANGED, and
        MODIFIED.

    u3 : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InertiaReliefState.py#L33-L34)[¶](#abaqus.Load.InertiaReliefState.InertiaReliefState.u3 "Permalink to this definition")
    :   A Boolean specifying the 3-direction as a free direction.

    u3State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InertiaReliefState.py)[¶](#abaqus.Load.InertiaReliefState.InertiaReliefState.u3State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the Boolean that identifies the
        local the 3-direction as a free direction. Possible values are UNSET, SET, UNCHANGED,
        and MODIFIED.

    ur1 : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InertiaReliefState.py#L36-L37)[¶](#abaqus.Load.InertiaReliefState.InertiaReliefState.ur1 "Permalink to this definition")
    :   A Boolean specifying the rotation about the 1-direction as a free direction.

    ur1State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InertiaReliefState.py)[¶](#abaqus.Load.InertiaReliefState.InertiaReliefState.ur1State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the Boolean that identifies
        rotation about the local 1-direction as a free direction. Possible values are UNSET,
        SET, UNCHANGED, and MODIFIED.

    ur2 : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InertiaReliefState.py#L39-L40)[¶](#abaqus.Load.InertiaReliefState.InertiaReliefState.ur2 "Permalink to this definition")
    :   A Boolean specifying the rotation about the 2-direction as a free direction.

    ur2State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InertiaReliefState.py)[¶](#abaqus.Load.InertiaReliefState.InertiaReliefState.ur2State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the Boolean that identifies the
        rotation about the local the 2-direction as a free direction. Possible values are UNSET,
        SET, UNCHANGED, and MODIFIED.

    ur3 : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InertiaReliefState.py#L42-L43)[¶](#abaqus.Load.InertiaReliefState.InertiaReliefState.ur3 "Permalink to this definition")
    :   A Boolean specifying the rotation about the 3-direction as a free direction.

    ur3State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InertiaReliefState.py)[¶](#abaqus.Load.InertiaReliefState.InertiaReliefState.ur3State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the Boolean that identifies the
        rotation about the local the 3-direction as a free direction. Possible values are UNSET,
        SET, UNCHANGED, and MODIFIED.

*class* InwardVolAccel(*[name](#abaqus.Load.LoadModel.InwardVolAccel "abaqus.Load.LoadModel.InwardVolAccel.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.LoadModel.InwardVolAccel "abaqus.Load.LoadModel.InwardVolAccel.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.LoadModel.InwardVolAccel "abaqus.Load.LoadModel.InwardVolAccel.__init__.region (Python parameter)")*, *[magnitude](#abaqus.Load.LoadModel.InwardVolAccel "abaqus.Load.LoadModel.InwardVolAccel.__init__.magnitude (Python parameter)")*, *[distributionType](#abaqus.Load.LoadModel.InwardVolAccel "abaqus.Load.LoadModel.InwardVolAccel.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.InwardVolAccel "abaqus.Load.LoadModel.InwardVolAccel.__init__.field (Python parameter)")=`''`*, *[amplitude](#abaqus.Load.LoadModel.InwardVolAccel "abaqus.Load.LoadModel.InwardVolAccel.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L13-L131)[¶](#abaqus.Load.LoadModel.InwardVolAccel "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The InwardVolAccel object stores the data for an inward volume acceleration acoustic load. The
    InwardVolAccel object is derived from the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [InwardVolAccel on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-inwardvolaccelpyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L28-L30)[¶](#abaqus.Load.LoadModel.InwardVolAccel.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
        UNIFORM and FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L32-L35)[¶](#abaqus.Load.LoadModel.InwardVolAccel.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L25-L26)[¶](#abaqus.Load.LoadModel.InwardVolAccel.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L37-L38)[¶](#abaqus.Load.LoadModel.InwardVolAccel.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[distributionType](#abaqus.Load.LoadModel.InwardVolAccel.setValues.distributionType "abaqus.Load.LoadModel.InwardVolAccel.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.InwardVolAccel.setValues.field "abaqus.Load.LoadModel.InwardVolAccel.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[amplitude](#abaqus.Load.LoadModel.InwardVolAccel.setValues.amplitude "abaqus.Load.LoadModel.InwardVolAccel.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L88-L111)[¶](#abaqus.Load.LoadModel.InwardVolAccel.setValues "Permalink to this definition")
    :   This method modifies the data for an existing InwardVolAccel object in the step where it is created.

        Note

        Check [InwardVolAccel.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-inwardvolaccelpyc.htm?contextscope=all#simaker-inwardvolaccelsetvaluespyc).

        Parameters:[¶](#abaqus.Load.LoadModel.InwardVolAccel.setValues-parameters "Permalink to this headline")
        :   distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.InwardVolAccel.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.InwardVolAccel.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.InwardVolAccel.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

    setValuesInStep(*[stepName](#abaqus.Load.LoadModel.InwardVolAccel.setValuesInStep.stepName "abaqus.Load.LoadModel.InwardVolAccel.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[magnitude](#abaqus.Load.LoadModel.InwardVolAccel.setValuesInStep.magnitude "abaqus.Load.LoadModel.InwardVolAccel.setValuesInStep.magnitude (Python parameter) — A Float specifying the load magnitude.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.InwardVolAccel.setValuesInStep.amplitude "abaqus.Load.LoadModel.InwardVolAccel.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L113-L131)[¶](#abaqus.Load.LoadModel.InwardVolAccel.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing InwardVolAccel object in the specified
        step.

        Note

        Check [InwardVolAccel.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-inwardvolaccelpyc.htm?contextscope=all#simaker-inwardvolaccelsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.LoadModel.InwardVolAccel.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.LoadModel.InwardVolAccel.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            magnitude=`None`[¶](#abaqus.Load.LoadModel.InwardVolAccel.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float specifying the load magnitude.

            amplitude=`''`[¶](#abaqus.Load.LoadModel.InwardVolAccel.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous static analysis step. FREED should be used if
                the load is changed to have no amplitude reference. You should provide the **amplitude**
                argument only if it is valid for the specified step.

*class* InwardVolAccelState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InwardVolAccelState.py#L9-L54)[¶](#abaqus.Load.InwardVolAccelState.InwardVolAccelState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The InwardVolAccelState object stores the propagating data of an inward volume acceleration acoustic load
    in a step. One instance of this object is created internally by the InwardVolAccel object for each step. The
    instance is also deleted internally by the InwardVolAccel object. The InwardVolAccelState object has no
    constructor or methods. The InwardVolAccelState object is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * CLOAD

    Note

    Check [InwardVolAccelState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-inwardvolaccelstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InwardVolAccelState.py#L9-L54)[¶](#abaqus.Load.InwardVolAccelState.InwardVolAccelState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InwardVolAccelState.py)[¶](#abaqus.Load.InwardVolAccelState.InwardVolAccelState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InwardVolAccelState.py#L27-L28)[¶](#abaqus.Load.InwardVolAccelState.InwardVolAccelState.magnitude "Permalink to this definition")
    :   A Float specifying the load magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InwardVolAccelState.py)[¶](#abaqus.Load.InwardVolAccelState.InwardVolAccelState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load magnitude. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/InwardVolAccelState.py)[¶](#abaqus.Load.InwardVolAccelState.InwardVolAccelState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* LineLoad(*[name](#abaqus.Load.LoadModel.LineLoad "abaqus.Load.LoadModel.LineLoad.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.LoadModel.LineLoad "abaqus.Load.LoadModel.LineLoad.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.LoadModel.LineLoad "abaqus.Load.LoadModel.LineLoad.__init__.region (Python parameter)")*, *[distributionType](#abaqus.Load.LoadModel.LineLoad "abaqus.Load.LoadModel.LineLoad.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.LineLoad "abaqus.Load.LoadModel.LineLoad.__init__.field (Python parameter)")=`''`*, *[comp1](#abaqus.Load.LoadModel.LineLoad "abaqus.Load.LoadModel.LineLoad.__init__.comp1 (Python parameter)")=`None`*, *[comp2](#abaqus.Load.LoadModel.LineLoad "abaqus.Load.LoadModel.LineLoad.__init__.comp2 (Python parameter)")=`None`*, *[comp3](#abaqus.Load.LoadModel.LineLoad "abaqus.Load.LoadModel.LineLoad.__init__.comp3 (Python parameter)")=`None`*, *[amplitude](#abaqus.Load.LoadModel.LineLoad "abaqus.Load.LoadModel.LineLoad.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[system](#abaqus.Load.LoadModel.LineLoad "abaqus.Load.LoadModel.LineLoad.__init__.system (Python parameter)")=`abaqusConstants.GLOBAL`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L15-L180)[¶](#abaqus.Load.LoadModel.LineLoad "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The LineLoad object stores the data of an applied line load. The LineLoad object is derived from the Load
    object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [LineLoad on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-lineloadpyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L30-L32)[¶](#abaqus.Load.LoadModel.LineLoad.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
        UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L38-L41)[¶](#abaqus.Load.LoadModel.LineLoad.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L27-L28)[¶](#abaqus.Load.LoadModel.LineLoad.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L43-L44)[¶](#abaqus.Load.LoadModel.LineLoad.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[distributionType](#abaqus.Load.LoadModel.LineLoad.setValues.distributionType "abaqus.Load.LoadModel.LineLoad.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.LoadModel.LineLoad.setValues.field "abaqus.Load.LoadModel.LineLoad.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[comp1](#abaqus.Load.LoadModel.LineLoad.setValues.comp1 "abaqus.Load.LoadModel.LineLoad.setValues.comp1 (Python parameter) — A Float or a Complex specifying the component of the load in the global or the beam local 1-direction.")=`None`*, *[comp2](#abaqus.Load.LoadModel.LineLoad.setValues.comp2 "abaqus.Load.LoadModel.LineLoad.setValues.comp2 (Python parameter) — A Float or a Complex specifying the component of the load in the global or the beam local 2-direction.")=`None`*, *[comp3](#abaqus.Load.LoadModel.LineLoad.setValues.comp3 "abaqus.Load.LoadModel.LineLoad.setValues.comp3 (Python parameter) — A Float or a Complex specifying the component of the load in the global 3-direction.")=`None`*, *[amplitude](#abaqus.Load.LoadModel.LineLoad.setValues.amplitude "abaqus.Load.LoadModel.LineLoad.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*, *[system](#abaqus.Load.LoadModel.LineLoad.setValues.system "abaqus.Load.LoadModel.LineLoad.setValues.system (Python parameter) — A SymbolicConstant specifying whether the load is applied in a global or the beam local frame of reference.")=`abaqusConstants.GLOBAL`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L106-L145)[¶](#abaqus.Load.LoadModel.LineLoad.setValues "Permalink to this definition")
    :   This method modifies the data for an existing LineLoad object in the step where it is created.

        Note

        Check [LineLoad.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-lineloadpyc.htm?contextscope=all#simaker-lineloadsetvaluespyc).

        Parameters:[¶](#abaqus.Load.LoadModel.LineLoad.setValues-parameters "Permalink to this headline")
        :   distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.LoadModel.LineLoad.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.LoadModel.LineLoad.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            comp1=`None`[¶](#abaqus.Load.LoadModel.LineLoad.setValues.comp1 "Permalink to this definition")
            :   A Float or a Complex specifying the component of the load in the global or the beam
                local 1-direction. Note: Although **comp1**, **comp2**, and **comp3** are optional arguments, at
                least one of them must be nonzero unless **distributionType** = USER\_DEFINED.

            comp2=`None`[¶](#abaqus.Load.LoadModel.LineLoad.setValues.comp2 "Permalink to this definition")
            :   A Float or a Complex specifying the component of the load in the global or the beam
                local 2-direction.

            comp3=`None`[¶](#abaqus.Load.LoadModel.LineLoad.setValues.comp3 "Permalink to this definition")
            :   A Float or a Complex specifying the component of the load in the global 3-direction.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.LoadModel.LineLoad.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

            system=`abaqusConstants.GLOBAL`[¶](#abaqus.Load.LoadModel.LineLoad.setValues.system "Permalink to this definition")
            :   A SymbolicConstant specifying whether the load is applied in a global or the beam local
                frame of reference. Possible values are GLOBAL and LOCAL. The default value is GLOBAL.

    setValuesInStep(*[stepName](#abaqus.Load.LoadModel.LineLoad.setValuesInStep.stepName "abaqus.Load.LoadModel.LineLoad.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[comp1](#abaqus.Load.LoadModel.LineLoad.setValuesInStep.comp1 "abaqus.Load.LoadModel.LineLoad.setValuesInStep.comp1 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the load component in the global or the beam local 1-direction.")=`Ellipsis`*, *[comp2](#abaqus.Load.LoadModel.LineLoad.setValuesInStep.comp2 "abaqus.Load.LoadModel.LineLoad.setValuesInStep.comp2 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the load component in the global or the beam local 2-direction.")=`Ellipsis`*, *[comp3](#abaqus.Load.LoadModel.LineLoad.setValuesInStep.comp3 "abaqus.Load.LoadModel.LineLoad.setValuesInStep.comp3 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the load component in the global 3-direction.")=`Ellipsis`*, *[amplitude](#abaqus.Load.LoadModel.LineLoad.setValuesInStep.amplitude "abaqus.Load.LoadModel.LineLoad.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L147-L180)[¶](#abaqus.Load.LoadModel.LineLoad.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing LineLoad object in the specified step.

        Note

        Check [LineLoad.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-lineloadpyc.htm?contextscope=all#simaker-lineloadsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.LoadModel.LineLoad.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.LoadModel.LineLoad.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            comp1=`Ellipsis`[¶](#abaqus.Load.LoadModel.LineLoad.setValuesInStep.comp1 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the load component in the global or
                the beam local 1-direction. Possible values for the SymbolicConstant are UNCHANGED and
                FREED. UNCHANGED should be used if the load component is propagated from the previous
                static analysis step. Use FREED to remove a previously defined load component.

            comp2=`Ellipsis`[¶](#abaqus.Load.LoadModel.LineLoad.setValuesInStep.comp2 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the load component in the global or
                the beam local 2-direction. For details see **comp1**.

            comp3=`Ellipsis`[¶](#abaqus.Load.LoadModel.LineLoad.setValuesInStep.comp3 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the load component in the global
                3-direction. For details see **comp1**.

            amplitude=`''`[¶](#abaqus.Load.LoadModel.LineLoad.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous static analysis step. FREED should be used if
                the load is changed to have no amplitude reference. You should provide the **amplitude**
                argument only if it is valid for the specified step.

    system : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'GLOBAL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadModel.py#L34-L36)[¶](#abaqus.Load.LoadModel.LineLoad.system "Permalink to this definition")
    :   A SymbolicConstant specifying whether the load is applied in a global or the beam local
        frame of reference. Possible values are GLOBAL and LOCAL. The default value is GLOBAL.

*class* LineLoadState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LineLoadState.py#L9-L70)[¶](#abaqus.Load.LineLoadState.LineLoadState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The LineLoadState object stores the propagating data of a line load in a step. One instance of this
    object is created internally by the LineLoad object for each step. The instance is also deleted internally
    by the LineLoad object. The LineLoadState object has no constructor or methods. The LineLoadState object is
    derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * DLOAD

    Note

    Check [LineLoadState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-lineloadstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LineLoadState.py#L9-L70)[¶](#abaqus.Load.LineLoadState.LineLoadState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LineLoadState.py)[¶](#abaqus.Load.LineLoadState.LineLoadState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    comp1 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LineLoadState.py#L27-L29)[¶](#abaqus.Load.LineLoadState.LineLoadState.comp1 "Permalink to this definition")
    :   A Float or a Complex specifying the load component in the global or the beam local
        1-direction.

    comp1State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LineLoadState.py)[¶](#abaqus.Load.LineLoadState.LineLoadState.comp1State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load component in the global
        or the beam local 1-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.

    comp2 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LineLoadState.py#L27-L29)[¶](#abaqus.Load.LineLoadState.LineLoadState.comp2 "Permalink to this definition")
    :   A Float or a Complex specifying the load component in the global or the beam local
        2-direction.

    comp2State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LineLoadState.py)[¶](#abaqus.Load.LineLoadState.LineLoadState.comp2State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load component in the global
        or the beam local 2-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.

    comp3 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LineLoadState.py#L35-L36)[¶](#abaqus.Load.LineLoadState.LineLoadState.comp3 "Permalink to this definition")
    :   A Float or a Complex specifying the load component in the global 3-direction.

    comp3State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LineLoadState.py)[¶](#abaqus.Load.LineLoadState.LineLoadState.comp3State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load component in the global
        3-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LineLoadState.py)[¶](#abaqus.Load.LineLoadState.LineLoadState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* LoadCase(*[name](#abaqus.Load.LoadStep.LoadCase "abaqus.Load.LoadStep.LoadCase.__init__.name (Python parameter)")*, *[boundaryConditions](#abaqus.Load.LoadStep.LoadCase "abaqus.Load.LoadStep.LoadCase.__init__.boundaryConditions (Python parameter)")=`()`*, *[loads](#abaqus.Load.LoadStep.LoadCase "abaqus.Load.LoadStep.LoadCase.__init__.loads (Python parameter)")=`()`*, *[includeActiveBaseStateBC](#abaqus.Load.LoadStep.LoadCase "abaqus.Load.LoadStep.LoadCase.__init__.includeActiveBaseStateBC (Python parameter)")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadStep.py#L8-L91)[¶](#abaqus.Load.LoadStep.LoadCase "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The LoadCase object is used to define the loads and constraints comprising a particular loading condition
    and the linear response of a structure subjected to that loading condition.

    Note

    This object can be accessed by:

    ```python
    import step
    mdb.models[name].steps[name].loadCases[name]
    ```

    Note

    Check [LoadCase on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadcasepyc.htm?contextscope=all).

    Member Details:

    resume()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadStep.py#L60-L63)[¶](#abaqus.Load.LoadStep.LoadCase.resume "Permalink to this definition")
    :   This method resumes the load case that was previously suppressed.

    setValues(*[boundaryConditions](#abaqus.Load.LoadStep.LoadCase.setValues.boundaryConditions "abaqus.Load.LoadStep.LoadCase.setValues.boundaryConditions (Python parameter) — A sequence of (String, Float) sequences specifying the name of a BoundaryCondition followed by a nonzero Float scaling factor.")=`()`*, *[loads](#abaqus.Load.LoadStep.LoadCase.setValues.loads "abaqus.Load.LoadStep.LoadCase.setValues.loads (Python parameter) — A sequence of (String, Float) sequences specifying the name of a Load followed by a nonzero Float specifying a scale factor.")=`()`*, *[includeActiveBaseStateBC](#abaqus.Load.LoadStep.LoadCase.setValues.includeActiveBaseStateBC "abaqus.Load.LoadStep.LoadCase.setValues.includeActiveBaseStateBC (Python parameter) — A Boolean specifying whether to include all active boundary conditions propagated or modified from the base state.")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadStep.py#L70-L91)[¶](#abaqus.Load.LoadStep.LoadCase.setValues "Permalink to this definition")
    :   This method modifies the LoadCase object.

        Note

        Check [LoadCase.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadcasepyc.htm?contextscope=all#simaker-loadcasesetvaluespyc).

        Parameters:[¶](#abaqus.Load.LoadStep.LoadCase.setValues-parameters "Permalink to this headline")
        :   boundaryConditions=`()`[¶](#abaqus.Load.LoadStep.LoadCase.setValues.boundaryConditions "Permalink to this definition")
            :   A sequence of (String, Float) sequences specifying the name of a BoundaryCondition
                followed by a nonzero Float scaling factor. The default value is an empty sequence.

            loads=`()`[¶](#abaqus.Load.LoadStep.LoadCase.setValues.loads "Permalink to this definition")
            :   A sequence of (String, Float) sequences specifying the name of a Load followed by a
                nonzero Float specifying a scale factor. The default value is an empty sequence.

            includeActiveBaseStateBC=`1`[¶](#abaqus.Load.LoadStep.LoadCase.setValues.includeActiveBaseStateBC "Permalink to this definition")
            :   A Boolean specifying whether to include all active boundary conditions propagated or
                modified from the base state. The default value is ON.

    suppress()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadStep.py#L65-L68)[¶](#abaqus.Load.LoadStep.LoadCase.suppress "Permalink to this definition")
    :   This method suppresses the load case.

    suppressed : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadStep.py#L20-L22)[¶](#abaqus.Load.LoadStep.LoadCase.suppressed "Permalink to this definition")
    :   A Boolean specifying whether the load case is suppressed or not. The default value is
        OFF.

*class* Moment(*[name](#abaqus.Load.Moment.Moment "abaqus.Load.Moment.Moment.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.Moment.Moment "abaqus.Load.Moment.Moment.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.Moment.Moment "abaqus.Load.Moment.Moment.__init__.region (Python parameter)")*, *[cm1](#abaqus.Load.Moment.Moment "abaqus.Load.Moment.Moment.__init__.cm1 (Python parameter)")=`None`*, *[cm2](#abaqus.Load.Moment.Moment "abaqus.Load.Moment.Moment.__init__.cm2 (Python parameter)")=`None`*, *[cm3](#abaqus.Load.Moment.Moment "abaqus.Load.Moment.Moment.__init__.cm3 (Python parameter)")=`None`*, *[amplitude](#abaqus.Load.Moment.Moment "abaqus.Load.Moment.Moment.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[follower](#abaqus.Load.Moment.Moment "abaqus.Load.Moment.Moment.__init__.follower (Python parameter)")=`0`*, *[localCsys](#abaqus.Load.Moment.Moment "abaqus.Load.Moment.Moment.__init__.localCsys (Python parameter)")=`None`*, *[distributionType](#abaqus.Load.Moment.Moment "abaqus.Load.Moment.Moment.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.Moment.Moment "abaqus.Load.Moment.Moment.__init__.field (Python parameter)")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/Moment.py#L21-L204)[¶](#abaqus.Load.Moment.Moment "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The Moment object stores the data for a moment. The Moment object is derived from the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [Moment on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-momentpyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/Moment.py#L35-L37)[¶](#abaqus.Load.Moment.Moment.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
        UNIFORM and FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/Moment.py#L50-L53)[¶](#abaqus.Load.Moment.Moment.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    follower : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/Moment.py#L39-L42)[¶](#abaqus.Load.Moment.Moment.follower "Permalink to this definition")
    :   A Boolean specifying whether the direction of the force rotates with the rotation of the
        node. You should provide the **follower** argument only if it is valid for the specified
        step. The default value is OFF.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/Moment.py#L44-L48)[¶](#abaqus.Load.Moment.Moment.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the ID of the Datum coordinate system used as the
        local coordinate system of the load. If **localCsys** = None, the load is defined in the
        global coordinate system. When this member is queried, it returns an Int. The default
        value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/Moment.py#L32-L33)[¶](#abaqus.Load.Moment.Moment.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/Moment.py#L55-L56)[¶](#abaqus.Load.Moment.Moment.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[cm1](#abaqus.Load.Moment.Moment.setValues.cm1 "abaqus.Load.Moment.Moment.setValues.cm1 (Python parameter) — A Float or a Complex specifying the load component in the 4-direction.")=`None`*, *[cm2](#abaqus.Load.Moment.Moment.setValues.cm2 "abaqus.Load.Moment.Moment.setValues.cm2 (Python parameter) — A Float or a Complex specifying the load component in the 5- direction.")=`None`*, *[cm3](#abaqus.Load.Moment.Moment.setValues.cm3 "abaqus.Load.Moment.Moment.setValues.cm3 (Python parameter) — A Float or a Complex specifying the load component in the 6-direction.")=`None`*, *[amplitude](#abaqus.Load.Moment.Moment.setValues.amplitude "abaqus.Load.Moment.Moment.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*, *[follower](#abaqus.Load.Moment.Moment.setValues.follower "abaqus.Load.Moment.Moment.setValues.follower (Python parameter) — A Boolean specifying whether the direction of the force rotates with the rotation of the node.")=`0`*, *[localCsys](#abaqus.Load.Moment.Moment.setValues.localCsys "abaqus.Load.Moment.Moment.setValues.localCsys (Python parameter) — None or a DatumCsys object specifying the ID of the Datum coordinate system used as the local coordinate system of the load.")=`None`*, *[distributionType](#abaqus.Load.Moment.Moment.setValues.distributionType "abaqus.Load.Moment.Moment.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.Moment.Moment.setValues.field "abaqus.Load.Moment.Moment.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/Moment.py#L124-L169)[¶](#abaqus.Load.Moment.Moment.setValues "Permalink to this definition")
    :   This method modifies the data for an existing Moment object in the step where it is created.

        Note

        Check [Moment.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-momentpyc.htm?contextscope=all#simaker-momentsetvaluespyc).

        Parameters:[¶](#abaqus.Load.Moment.Moment.setValues-parameters "Permalink to this headline")
        :   cm1=`None`[¶](#abaqus.Load.Moment.Moment.setValues.cm1 "Permalink to this definition")
            :   A Float or a Complex specifying the load component in the 4-direction. Note: Although
                **comp1**, **comp2**, and **comp3** are optional arguments, at least one of them must be
                nonzero.

            cm2=`None`[¶](#abaqus.Load.Moment.Moment.setValues.cm2 "Permalink to this definition")
            :   A Float or a Complex specifying the load component in the 5- direction.

            cm3=`None`[¶](#abaqus.Load.Moment.Moment.setValues.cm3 "Permalink to this definition")
            :   A Float or a Complex specifying the load component in the 6-direction.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.Moment.Moment.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

            follower=`0`[¶](#abaqus.Load.Moment.Moment.setValues.follower "Permalink to this definition")
            :   A Boolean specifying whether the direction of the force rotates with the rotation of the
                node. You should provide the **follower** argument only if it is valid for the specified
                step. The default value is OFF.

            localCsys=`None`[¶](#abaqus.Load.Moment.Moment.setValues.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the ID of the Datum coordinate system used as the
                local coordinate system of the load. If **localCsys** = None, the load is defined in the
                global coordinate system. When this member is queried, it returns an Int. The default
                value is None.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.Moment.Moment.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.Moment.Moment.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

    setValuesInStep(*[stepName](#abaqus.Load.Moment.Moment.setValuesInStep.stepName "abaqus.Load.Moment.Moment.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[comp1](#abaqus.Load.Moment.Moment.setValuesInStep.comp1 "abaqus.Load.Moment.Moment.setValuesInStep.comp1 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the load component in the 4-direction.")=`Ellipsis`*, *[comp2](#abaqus.Load.Moment.Moment.setValuesInStep.comp2 "abaqus.Load.Moment.Moment.setValuesInStep.comp2 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the load component in the 5-direction.")=`Ellipsis`*, *[comp3](#abaqus.Load.Moment.Moment.setValuesInStep.comp3 "abaqus.Load.Moment.Moment.setValuesInStep.comp3 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the load component in the 6-direction.")=`Ellipsis`*, *[amplitude](#abaqus.Load.Moment.Moment.setValuesInStep.amplitude "abaqus.Load.Moment.Moment.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/Moment.py#L171-L204)[¶](#abaqus.Load.Moment.Moment.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing Moment object in the specified step.

        Note

        Check [Moment.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-momentpyc.htm?contextscope=all#simaker-momentsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.Moment.Moment.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.Moment.Moment.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            comp1=`Ellipsis`[¶](#abaqus.Load.Moment.Moment.setValuesInStep.comp1 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the load component in the
                4-direction. Possible values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED
                should be used if the load component is propagated from the previous static analysis
                step. Use FREED to remove a previously defined load component.

            comp2=`Ellipsis`[¶](#abaqus.Load.Moment.Moment.setValuesInStep.comp2 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the load component in the
                5-direction. For details see **comp1**.

            comp3=`Ellipsis`[¶](#abaqus.Load.Moment.Moment.setValuesInStep.comp3 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the load component in the
                6-direction. For details see **comp1**.

            amplitude=`''`[¶](#abaqus.Load.Moment.Moment.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous static analysis step. FREED should be used if
                the load is changed to have no amplitude reference. You should provide the **amplitude**
                argument only if it is valid for the specified step.

*class* PEGLoad(*[name](#abaqus.Load.PEGLoad.PEGLoad "abaqus.Load.PEGLoad.PEGLoad.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.PEGLoad.PEGLoad "abaqus.Load.PEGLoad.PEGLoad.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.PEGLoad.PEGLoad "abaqus.Load.PEGLoad.PEGLoad.__init__.region (Python parameter)")*, *[distributionType](#abaqus.Load.PEGLoad.PEGLoad "abaqus.Load.PEGLoad.PEGLoad.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.PEGLoad.PEGLoad "abaqus.Load.PEGLoad.PEGLoad.__init__.field (Python parameter)")=`''`*, *[comp1](#abaqus.Load.PEGLoad.PEGLoad "abaqus.Load.PEGLoad.PEGLoad.__init__.comp1 (Python parameter)")=`None`*, *[comp2](#abaqus.Load.PEGLoad.PEGLoad "abaqus.Load.PEGLoad.PEGLoad.__init__.comp2 (Python parameter)")=`None`*, *[comp3](#abaqus.Load.PEGLoad.PEGLoad "abaqus.Load.PEGLoad.PEGLoad.__init__.comp3 (Python parameter)")=`None`*, *[amplitude](#abaqus.Load.PEGLoad.PEGLoad "abaqus.Load.PEGLoad.PEGLoad.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PEGLoad.py#L15-L165)[¶](#abaqus.Load.PEGLoad.PEGLoad "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The PEGLoad object stores the data for a PEG load. The PEGLoad object is derived from the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [PEGLoad on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pegloadpyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PEGLoad.py#L29-L31)[¶](#abaqus.Load.PEGLoad.PEGLoad.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
        UNIFORM and FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PEGLoad.py#L33-L36)[¶](#abaqus.Load.PEGLoad.PEGLoad.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PEGLoad.py#L26-L27)[¶](#abaqus.Load.PEGLoad.PEGLoad.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PEGLoad.py#L38-L39)[¶](#abaqus.Load.PEGLoad.PEGLoad.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[distributionType](#abaqus.Load.PEGLoad.PEGLoad.setValues.distributionType "abaqus.Load.PEGLoad.PEGLoad.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.PEGLoad.PEGLoad.setValues.field "abaqus.Load.PEGLoad.PEGLoad.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[comp1](#abaqus.Load.PEGLoad.PEGLoad.setValues.comp1 "abaqus.Load.PEGLoad.PEGLoad.setValues.comp1 (Python parameter) — A Float or a Complex specifying the load component at dof 1 of reference node 1.")=`None`*, *[comp2](#abaqus.Load.PEGLoad.PEGLoad.setValues.comp2 "abaqus.Load.PEGLoad.PEGLoad.setValues.comp2 (Python parameter) — A Float or a Complex specifying the load component at dof 1 of reference node 2.")=`None`*, *[comp3](#abaqus.Load.PEGLoad.PEGLoad.setValues.comp3 "abaqus.Load.PEGLoad.PEGLoad.setValues.comp3 (Python parameter) — A Float or a Complex specifying the load component at dof 2 of reference node 2.")=`None`*, *[amplitude](#abaqus.Load.PEGLoad.PEGLoad.setValues.amplitude "abaqus.Load.PEGLoad.PEGLoad.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PEGLoad.py#L96-L130)[¶](#abaqus.Load.PEGLoad.PEGLoad.setValues "Permalink to this definition")
    :   This method modifies the data for an existing PEGLoad object in the step where it is created.

        Note

        Check [PEGLoad.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pegloadpyc.htm?contextscope=all#simaker-pegloadsetvaluespyc).

        Parameters:[¶](#abaqus.Load.PEGLoad.PEGLoad.setValues-parameters "Permalink to this headline")
        :   distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.PEGLoad.PEGLoad.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.PEGLoad.PEGLoad.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            comp1=`None`[¶](#abaqus.Load.PEGLoad.PEGLoad.setValues.comp1 "Permalink to this definition")
            :   A Float or a Complex specifying the load component at dof 1 of reference node
                1. Note: Although **comp1**, **comp2**, and **comp3** are optional arguments, at least one of
                them must be nonzero.

            comp2=`None`[¶](#abaqus.Load.PEGLoad.PEGLoad.setValues.comp2 "Permalink to this definition")
            :   A Float or a Complex specifying the load component at dof 1 of reference node 2.

            comp3=`None`[¶](#abaqus.Load.PEGLoad.PEGLoad.setValues.comp3 "Permalink to this definition")
            :   A Float or a Complex specifying the load component at dof 2 of reference node 2.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.PEGLoad.PEGLoad.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

    setValuesInStep(*[stepName](#abaqus.Load.PEGLoad.PEGLoad.setValuesInStep.stepName "abaqus.Load.PEGLoad.PEGLoad.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[comp1](#abaqus.Load.PEGLoad.PEGLoad.setValuesInStep.comp1 "abaqus.Load.PEGLoad.PEGLoad.setValuesInStep.comp1 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the load component at dof 1 of reference node 1.")=`Ellipsis`*, *[comp2](#abaqus.Load.PEGLoad.PEGLoad.setValuesInStep.comp2 "abaqus.Load.PEGLoad.PEGLoad.setValuesInStep.comp2 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the load component at dof 1 of reference node 2.")=`Ellipsis`*, *[comp3](#abaqus.Load.PEGLoad.PEGLoad.setValuesInStep.comp3 "abaqus.Load.PEGLoad.PEGLoad.setValuesInStep.comp3 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the load component at dof 2 of reference node 2.")=`Ellipsis`*, *[amplitude](#abaqus.Load.PEGLoad.PEGLoad.setValuesInStep.amplitude "abaqus.Load.PEGLoad.PEGLoad.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PEGLoad.py#L132-L165)[¶](#abaqus.Load.PEGLoad.PEGLoad.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing PEGLoad object in the specified step.

        Note

        Check [PEGLoad.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pegloadpyc.htm?contextscope=all#simaker-pegloadsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.PEGLoad.PEGLoad.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.PEGLoad.PEGLoad.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            comp1=`Ellipsis`[¶](#abaqus.Load.PEGLoad.PEGLoad.setValuesInStep.comp1 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the load component at dof 1 of
                reference node 1. Possible values for the SymbolicConstant are UNCHANGED and FREED.
                UNCHANGED should be used if the load component is propagated from the previous static
                analysis step. Use FREED to remove a previously defined load component.

            comp2=`Ellipsis`[¶](#abaqus.Load.PEGLoad.PEGLoad.setValuesInStep.comp2 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the load component at dof 1 of
                reference node 2. For details see **comp1**.

            comp3=`Ellipsis`[¶](#abaqus.Load.PEGLoad.PEGLoad.setValuesInStep.comp3 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the load component at dof 2 of
                reference node 2. For details see **comp1**.

            amplitude=`''`[¶](#abaqus.Load.PEGLoad.PEGLoad.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous static analysis step. FREED should be used if
                the load is changed to have no amplitude reference. You should provide the **amplitude**
                argument only if it is valid for the specified step.

*class* PipePressure(*[name](#abaqus.Load.PipePressure.PipePressure "abaqus.Load.PipePressure.PipePressure.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.PipePressure.PipePressure "abaqus.Load.PipePressure.PipePressure.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.PipePressure.PipePressure "abaqus.Load.PipePressure.PipePressure.__init__.region (Python parameter)")*, *[magnitude](#abaqus.Load.PipePressure.PipePressure "abaqus.Load.PipePressure.PipePressure.__init__.magnitude (Python parameter)")*, *[diameter](#abaqus.Load.PipePressure.PipePressure "abaqus.Load.PipePressure.PipePressure.__init__.diameter (Python parameter)")*, *[hZero](#abaqus.Load.PipePressure.PipePressure "abaqus.Load.PipePressure.PipePressure.__init__.hZero (Python parameter)")*, *[hReference](#abaqus.Load.PipePressure.PipePressure "abaqus.Load.PipePressure.PipePressure.__init__.hReference (Python parameter)")*, *[field](#abaqus.Load.PipePressure.PipePressure "abaqus.Load.PipePressure.PipePressure.__init__.field (Python parameter)")=`''`*, *[amplitude](#abaqus.Load.PipePressure.PipePressure "abaqus.Load.PipePressure.PipePressure.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.Load.PipePressure.PipePressure "abaqus.Load.PipePressure.PipePressure.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[side](#abaqus.Load.PipePressure.PipePressure "abaqus.Load.PipePressure.PipePressure.__init__.side (Python parameter)")=`abaqusConstants.INTERNAL`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PipePressure.py#L13-L169)[¶](#abaqus.Load.PipePressure.PipePressure "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The PipePressure object stores the data for a pressure applied to pipe or elbow elements. The
    PipePressure object is derived from the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [PipePressure on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pipepressurepyc.htm?contextscope=all).

    Member Details:

    diameter : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PipePressure.py#L36-L37)[¶](#abaqus.Load.PipePressure.PipePressure.diameter "Permalink to this definition")
    :   A Float specifying the effective inner or outer diameter.

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PipePressure.py#L28-L30)[¶](#abaqus.Load.PipePressure.PipePressure.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM,
        HYDROSTATIC, USER\_DEFINED, and FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PipePressure.py#L39-L42)[¶](#abaqus.Load.PipePressure.PipePressure.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PipePressure.py#L25-L26)[¶](#abaqus.Load.PipePressure.PipePressure.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PipePressure.py#L44-L45)[¶](#abaqus.Load.PipePressure.PipePressure.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[field](#abaqus.Load.PipePressure.PipePressure.setValues.field "abaqus.Load.PipePressure.PipePressure.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[amplitude](#abaqus.Load.PipePressure.PipePressure.setValues.amplitude "abaqus.Load.PipePressure.PipePressure.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.Load.PipePressure.PipePressure.setValues.distributionType "abaqus.Load.PipePressure.PipePressure.setValues.distributionType (Python parameter) — A SymbolicConstant specifying whether the load is uniform.")=`abaqusConstants.UNIFORM`*, *[side](#abaqus.Load.PipePressure.PipePressure.setValues.side "abaqus.Load.PipePressure.PipePressure.setValues.side (Python parameter) — A SymbolicConstant specifying whether the pressure is applied internally or externally. Possible values are INTERNAL and EXTERNAL.")=`abaqusConstants.INTERNAL`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PipePressure.py#L110-L137)[¶](#abaqus.Load.PipePressure.PipePressure.setValues "Permalink to this definition")
    :   This method modifies the data for an existing PipePressure object in the step where it is created.

        Note

        Check [PipePressure.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pipepressurepyc.htm?contextscope=all#simaker-pipepressuresetvaluespyc).

        Parameters:[¶](#abaqus.Load.PipePressure.PipePressure.setValues-parameters "Permalink to this headline")
        :   field=`''`[¶](#abaqus.Load.PipePressure.PipePressure.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.PipePressure.PipePressure.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.PipePressure.PipePressure.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM,
                HYDROSTATIC, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            side=`abaqusConstants.INTERNAL`[¶](#abaqus.Load.PipePressure.PipePressure.setValues.side "Permalink to this definition")
            :   A SymbolicConstant specifying whether the pressure is applied internally or externally.
                Possible values are INTERNAL and EXTERNAL. The default value is INTERNAL.

    setValuesInStep(*[stepName](#abaqus.Load.PipePressure.PipePressure.setValuesInStep.stepName "abaqus.Load.PipePressure.PipePressure.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[magnitude](#abaqus.Load.PipePressure.PipePressure.setValuesInStep.magnitude "abaqus.Load.PipePressure.PipePressure.setValuesInStep.magnitude (Python parameter) — A Float specifying the pressure magnitude.")=`None`*, *[hZero](#abaqus.Load.PipePressure.PipePressure.setValuesInStep.hZero "abaqus.Load.PipePressure.PipePressure.setValuesInStep.hZero (Python parameter) — A Float specifying the height of the zero pressure level when distributionType = HYDROSTATIC.")=`None`*, *[hReference](#abaqus.Load.PipePressure.PipePressure.setValuesInStep.hReference "abaqus.Load.PipePressure.PipePressure.setValuesInStep.hReference (Python parameter) — A Float specifying the height of the reference pressure level when distributionType = HYDROSTATIC.")=`None`*, *[amplitude](#abaqus.Load.PipePressure.PipePressure.setValuesInStep.amplitude "abaqus.Load.PipePressure.PipePressure.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PipePressure.py#L139-L169)[¶](#abaqus.Load.PipePressure.PipePressure.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing PipePressure object in the specified step.

        Note

        Check [PipePressure.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pipepressurepyc.htm?contextscope=all#simaker-pipepressuresetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.PipePressure.PipePressure.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.PipePressure.PipePressure.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            magnitude=`None`[¶](#abaqus.Load.PipePressure.PipePressure.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float specifying the pressure magnitude.

            hZero=`None`[¶](#abaqus.Load.PipePressure.PipePressure.setValuesInStep.hZero "Permalink to this definition")
            :   A Float specifying the height of the zero pressure level when
                **distributionType** = HYDROSTATIC.

            hReference=`None`[¶](#abaqus.Load.PipePressure.PipePressure.setValuesInStep.hReference "Permalink to this definition")
            :   A Float specifying the height of the reference pressure level when
                **distributionType** = HYDROSTATIC.

            amplitude=`''`[¶](#abaqus.Load.PipePressure.PipePressure.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous static analysis step. FREED should be used if
                the load has no amplitude reference. You should provide the **amplitude** argument only if
                it is valid for the specified step.

    side : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'INTERNAL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PipePressure.py#L32-L34)[¶](#abaqus.Load.PipePressure.PipePressure.side "Permalink to this definition")
    :   A SymbolicConstant specifying whether the pressure is applied internally or externally.
        Possible values are INTERNAL and EXTERNAL. The default value is INTERNAL.

*class* Pressure(*[name](#abaqus.Load.Pressure.Pressure "abaqus.Load.Pressure.Pressure.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.Pressure.Pressure "abaqus.Load.Pressure.Pressure.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.Pressure.Pressure "abaqus.Load.Pressure.Pressure.__init__.region (Python parameter)")*, *[magnitude](#abaqus.Load.Pressure.Pressure "abaqus.Load.Pressure.Pressure.__init__.magnitude (Python parameter)")=`0.0`*, *[hZero](#abaqus.Load.Pressure.Pressure "abaqus.Load.Pressure.Pressure.__init__.hZero (Python parameter)")=`0.0`*, *[hReference](#abaqus.Load.Pressure.Pressure "abaqus.Load.Pressure.Pressure.__init__.hReference (Python parameter)")=`0.0`*, *[field](#abaqus.Load.Pressure.Pressure "abaqus.Load.Pressure.Pressure.__init__.field (Python parameter)")=`''`*, *[refPoint](#abaqus.Load.Pressure.Pressure "abaqus.Load.Pressure.Pressure.__init__.refPoint (Python parameter)")=`''`*, *[distributionType](#abaqus.Load.Pressure.Pressure "abaqus.Load.Pressure.Pressure.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.Load.Pressure.Pressure "abaqus.Load.Pressure.Pressure.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/Pressure.py#L13-L165)[¶](#abaqus.Load.Pressure.Pressure "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The Pressure object defines a pressure load. The Pressure object is derived from the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [Pressure on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pressurepyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/Pressure.py#L27-L30)[¶](#abaqus.Load.Pressure.Pressure.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the pressure is distributed spatially. Possible values
        are UNIFORM, USER\_DEFINED, FIELD, HYDROSTATIC, STAGNATION, VISCOUS, TOTAL\_FORCE, and
        DISCRETE\_FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/Pressure.py#L32-L35)[¶](#abaqus.Load.Pressure.Pressure.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField or DiscreteField object associated
        with this load. The **field** argument applies only when **distributionType** = FIELD or
        **distributionType** = DISCRETE\_FIELD. The default value is an empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/Pressure.py#L24-L25)[¶](#abaqus.Load.Pressure.Pressure.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/Pressure.py#L37-L38)[¶](#abaqus.Load.Pressure.Pressure.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[field](#abaqus.Load.Pressure.Pressure.setValues.field "abaqus.Load.Pressure.Pressure.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField or DiscreteField object associated with this load.")=`''`*, *[refPoint](#abaqus.Load.Pressure.Pressure.setValues.refPoint "abaqus.Load.Pressure.Pressure.setValues.refPoint (Python parameter) — A Region specifying the reference point from which the relative velocity is determined when distributionType = STAGNATION or VISCOUS.")=`''`*, *[distributionType](#abaqus.Load.Pressure.Pressure.setValues.distributionType "abaqus.Load.Pressure.Pressure.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the pressure is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.Load.Pressure.Pressure.setValues.amplitude "abaqus.Load.Pressure.Pressure.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/Pressure.py#L103-L133)[¶](#abaqus.Load.Pressure.Pressure.setValues "Permalink to this definition")
    :   This method modifies the data for an existing Pressure object in the step where it is created.

        Note

        Check [Pressure.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pressurepyc.htm?contextscope=all#simaker-pressuresetvaluespyc).

        Parameters:[¶](#abaqus.Load.Pressure.Pressure.setValues-parameters "Permalink to this headline")
        :   field=`''`[¶](#abaqus.Load.Pressure.Pressure.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField or DiscreteField object associated
                with this load. The **field** argument applies only when **distributionType** = FIELD or
                **distributionType** = DISCRETE\_FIELD. The default value is an empty string.

            refPoint=`''`[¶](#abaqus.Load.Pressure.Pressure.setValues.refPoint "Permalink to this definition")
            :   A Region specifying the reference point from which the relative velocity is determined
                when **distributionType** = STAGNATION or VISCOUS.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.Pressure.Pressure.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the pressure is distributed spatially. Possible values
                are UNIFORM, USER\_DEFINED, FIELD, HYDROSTATIC, STAGNATION, VISCOUS, TOTAL\_FORCE, and
                DISCRETE\_FIELD. The default value is UNIFORM.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.Pressure.Pressure.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

    setValuesInStep(*[stepName](#abaqus.Load.Pressure.Pressure.setValuesInStep.stepName "abaqus.Load.Pressure.Pressure.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[magnitude](#abaqus.Load.Pressure.Pressure.setValuesInStep.magnitude "abaqus.Load.Pressure.Pressure.setValuesInStep.magnitude (Python parameter) — A Float or a Complex specifying the pressure magnitude.")=`None`*, *[hZero](#abaqus.Load.Pressure.Pressure.setValuesInStep.hZero "abaqus.Load.Pressure.Pressure.setValuesInStep.hZero (Python parameter) — A Float specifying the height of the zero pressure level when distributionType = HYDROSTATIC.")=`None`*, *[hReference](#abaqus.Load.Pressure.Pressure.setValuesInStep.hReference "abaqus.Load.Pressure.Pressure.setValuesInStep.hReference (Python parameter) — A Float specifying the height of the reference pressure level when distributionType = HYDROSTATIC.")=`None`*, *[amplitude](#abaqus.Load.Pressure.Pressure.setValuesInStep.amplitude "abaqus.Load.Pressure.Pressure.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/Pressure.py#L135-L165)[¶](#abaqus.Load.Pressure.Pressure.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing Pressure object in the specified step.

        Note

        Check [Pressure.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pressurepyc.htm?contextscope=all#simaker-pressuresetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.Pressure.Pressure.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.Pressure.Pressure.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            magnitude=`None`[¶](#abaqus.Load.Pressure.Pressure.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float or a Complex specifying the pressure magnitude.

            hZero=`None`[¶](#abaqus.Load.Pressure.Pressure.setValuesInStep.hZero "Permalink to this definition")
            :   A Float specifying the height of the zero pressure level when
                **distributionType** = HYDROSTATIC.

            hReference=`None`[¶](#abaqus.Load.Pressure.Pressure.setValuesInStep.hReference "Permalink to this definition")
            :   A Float specifying the height of the reference pressure level when
                **distributionType** = HYDROSTATIC.

            amplitude=`''`[¶](#abaqus.Load.Pressure.Pressure.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                load has no amplitude reference. You should provide the **amplitude** argument only if it
                is valid for the specified step.

*class* RotationalBodyForce(*[name](#abaqus.Load.RotationalBodyForce.RotationalBodyForce "abaqus.Load.RotationalBodyForce.RotationalBodyForce.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.RotationalBodyForce.RotationalBodyForce "abaqus.Load.RotationalBodyForce.RotationalBodyForce.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.RotationalBodyForce.RotationalBodyForce "abaqus.Load.RotationalBodyForce.RotationalBodyForce.__init__.region (Python parameter)")*, *[magnitude](#abaqus.Load.RotationalBodyForce.RotationalBodyForce "abaqus.Load.RotationalBodyForce.RotationalBodyForce.__init__.magnitude (Python parameter)")*, *[point1](#abaqus.Load.RotationalBodyForce.RotationalBodyForce "abaqus.Load.RotationalBodyForce.RotationalBodyForce.__init__.point1 (Python parameter)")*, *[point2](#abaqus.Load.RotationalBodyForce.RotationalBodyForce "abaqus.Load.RotationalBodyForce.RotationalBodyForce.__init__.point2 (Python parameter)")*, *[distributionType](#abaqus.Load.RotationalBodyForce.RotationalBodyForce "abaqus.Load.RotationalBodyForce.RotationalBodyForce.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.RotationalBodyForce.RotationalBodyForce "abaqus.Load.RotationalBodyForce.RotationalBodyForce.__init__.field (Python parameter)")=`''`*, *[centrifugal](#abaqus.Load.RotationalBodyForce.RotationalBodyForce "abaqus.Load.RotationalBodyForce.RotationalBodyForce.__init__.centrifugal (Python parameter)")=`0`*, *[rotaryAcceleration](#abaqus.Load.RotationalBodyForce.RotationalBodyForce "abaqus.Load.RotationalBodyForce.RotationalBodyForce.__init__.rotaryAcceleration (Python parameter)")=`0`*, *[rotorDynamicloads](#abaqus.Load.RotationalBodyForce.RotationalBodyForce "abaqus.Load.RotationalBodyForce.RotationalBodyForce.__init__.rotorDynamicloads (Python parameter)")=`0`*, *[amplitude](#abaqus.Load.RotationalBodyForce.RotationalBodyForce "abaqus.Load.RotationalBodyForce.RotationalBodyForce.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/RotationalBodyForce.py#L19-L222)[¶](#abaqus.Load.RotationalBodyForce.RotationalBodyForce "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The RotationalBodyForce object stores the data for a rotational body force. The RotationalBodyForce
    object is derived from the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [RotationalBodyForce on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rotationalbodyforcepyc.htm?contextscope=all).

    Member Details:

    centrifugal : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/RotationalBodyForce.py#L42-L44)[¶](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.centrifugal "Permalink to this definition")
    :   A Boolean specifying whether or not the effect of the load is centrifugal. The default
        value is OFF. Note: At least one of **centrifugal** or **rotaryAcceleration** or
        **rotorDynamicloadsmust** must be specified and only one must have the value ON.

        Changed in version 2025: The `rotorDynamicloadsmust` argument was added.

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/RotationalBodyForce.py#L34-L36)[¶](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
        UNIFORM and FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/RotationalBodyForce.py#L68-L71)[¶](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/RotationalBodyForce.py#L31-L32)[¶](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.name "Permalink to this definition")
    :   A String specifying the load repository key.

    point1 : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/RotationalBodyForce.py#L62-L63)[¶](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.point1 "Permalink to this definition")
    :   A tuple of Floats specifying the first point on the axis of rotation for the load.

    point2 : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/RotationalBodyForce.py#L65-L66)[¶](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.point2 "Permalink to this definition")
    :   A tuple of Floats specifying the second point on the axis of rotation for the load.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/RotationalBodyForce.py#L73-L74)[¶](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    rotaryAcceleration : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/RotationalBodyForce.py#L42-L44)[¶](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.rotaryAcceleration "Permalink to this definition")
    :   A Boolean specifying whether or not the effect of the load is rotary acceleration. The
        default value is OFF. Note: At least one of **centrifugal** or **rotaryAcceleration** or
        **rotaryAcceleration** must be specified and only one must have the value ON.

        Changed in version 2025: The `rotorDynamicloadsmust` argument was added.

    rotorDynamicloads : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/RotationalBodyForce.py#L58-L60)[¶](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.rotorDynamicloads "Permalink to this definition")
    :   A Boolean specifying whether or not the effect of the load is rotordynamic. The default
        value is OFF. Note: At least one of **centrifugal** or **rotaryAcceleration** or
        **rotorDynamicloads** must be specified and only one must have the value ON.

        New in version 2025: The `rotorDynamicloadsmust` argument was added.

    setValues(*[distributionType](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValues.distributionType "abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValues.field "abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[centrifugal](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValues.centrifugal "abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValues.centrifugal (Python parameter) — A Boolean specifying whether or not the effect of the load is centrifugal.")=`0`*, *[rotaryAcceleration](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValues.rotaryAcceleration "abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValues.rotaryAcceleration (Python parameter) — A Boolean specifying whether or not the effect of the load is rotary acceleration.")=`0`*, *[rotorDynamicloads](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValues.rotorDynamicloads "abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValues.rotorDynamicloads (Python parameter) — A Boolean specifying whether or not the effect of the load is rotordynamic.")=`0`*, *[amplitude](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValues.amplitude "abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/RotationalBodyForce.py#L154-L202)[¶](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValues "Permalink to this definition")
    :   This method modifies the data for an existing RotationalBodyForce object in the step where it is
        created.

        Note

        Check [RotationalBodyForce.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rotationalbodyforcepyc.htm?contextscope=all#simaker-rotationalbodyforcesetvaluespyc).

        Parameters:[¶](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValues-parameters "Permalink to this headline")
        :   distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            centrifugal=`0`[¶](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValues.centrifugal "Permalink to this definition")
            :   A Boolean specifying whether or not the effect of the load is centrifugal. The default
                value is OFF. Note: At least one of **centrifugal** or **rotaryAcceleration** or
                **rotorDynamicloads** must be specified and only one must have the value ON.

                Changed in version 2025: The `rotorDynamicloads` argument was added.

            rotaryAcceleration=`0`[¶](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValues.rotaryAcceleration "Permalink to this definition")
            :   A Boolean specifying whether or not the effect of the load is rotary acceleration. The
                default value is OFF. Note: At least one of **centrifugal** or **rotaryAcceleration** or
                **rotorDynamicloads** must be specified and only one must have the value ON.

                Changed in version 2025: The `rotorDynamicloads` argument was added.

            rotorDynamicloads=`0`[¶](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValues.rotorDynamicloads "Permalink to this definition")
            :   A Boolean specifying whether or not the effect of the load is rotordynamic. The default
                value is OFF. Note: At least one of **centrifugal** or **rotaryAcceleration** or
                **rotorDynamicloads** must be specified and only one must have the value ON.

                New in version 2025: The `rotorDynamicloads` argument was added.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

    setValuesInStep(*[stepName](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValuesInStep.stepName "abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[magnitude](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValuesInStep.magnitude "abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValuesInStep.magnitude (Python parameter) — A Float specifying the load magnitude.")=`None`*, *[amplitude](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValuesInStep.amplitude "abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/RotationalBodyForce.py#L204-L222)[¶](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing RotationalBodyForce object in the specified
        step.

        Note

        Check [RotationalBodyForce.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rotationalbodyforcepyc.htm?contextscope=all#simaker-rotationalbodyforcesetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            magnitude=`None`[¶](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float specifying the load magnitude.

            amplitude=`''`[¶](#abaqus.Load.RotationalBodyForce.RotationalBodyForce.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous static analysis step. FREED should be used if
                the load is changed to have no amplitude reference. You should provide the **amplitude**
                argument only if it is valid for the specified step.

*class* ShellEdgeLoad(*[name](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.__init__.region (Python parameter)")*, *[magnitude](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.__init__.magnitude (Python parameter)")*, *[distributionType](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.__init__.field (Python parameter)")=`''`*, *[amplitude](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[angle](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.__init__.angle (Python parameter)")=`0`*, *[axis](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.__init__.axis (Python parameter)")=`abaqusConstants.AXIS_1`*, *[localCsys](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.__init__.localCsys (Python parameter)")=`abaqusConstants.GENERAL`*, *[userCsys](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.__init__.userCsys (Python parameter)")=`abaqusConstants.GENERAL`*, *[directionVector](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.__init__.directionVector (Python parameter)")=`()`*, *[follower](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.__init__.follower (Python parameter)")=`1`*, *[resultant](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.__init__.resultant (Python parameter)")=`0`*, *[traction](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.__init__.traction (Python parameter)")=`abaqusConstants.NORMAL`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ShellEdgeLoad.py#L25-L235)[¶](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The ShellEdgeLoad object defines shell edge loads on a region. The ShellEdgeLoad object is derived from
    the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [ShellEdgeLoad on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shelledgeloadpyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ShellEdgeLoad.py#L40-L42)[¶](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the shell edge load is distributed spatially. Possible
        values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ShellEdgeLoad.py#L44-L47)[¶](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ShellEdgeLoad.py#L37-L38)[¶](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ShellEdgeLoad.py#L49-L50)[¶](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[distributionType](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.distributionType "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the shell edge load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.field "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[amplitude](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.amplitude "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*, *[angle](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.angle "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.angle (Python parameter) — A Float specifying an additional rotation of directionVector about an axis.")=`0`*, *[axis](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.axis "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.axis (Python parameter) — A SymbolicConstant specifying the axis about which to apply an additional rotation of directionVector.")=`abaqusConstants.AXIS_1`*, *[localCsys](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.localCsys "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.localCsys (Python parameter) — A DatumCsys object specifying the local coordinate system of the load's degrees of freedom.")=`abaqusConstants.GENERAL`*, *[userCsys](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.userCsys "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.userCsys (Python parameter) — A String specifying a CSYS defined by a user-subroutine.")=`abaqusConstants.GENERAL`*, *[directionVector](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.directionVector "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.directionVector (Python parameter) — A tuple of two points specifying the direction of the load.")=`()`*, *[follower](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.follower "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.follower (Python parameter) — A Boolean specifying whether the direction of the force changes with rotation.")=`1`*, *[resultant](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.resultant "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.resultant (Python parameter) — A Boolean specifying whether to maintain a constant resultant force by defining traction per unit undeformed area.")=`0`*, *[traction](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.traction "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.traction (Python parameter) — A SymbolicConstant specifying how to apply surface traction.")=`abaqusConstants.NORMAL`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ShellEdgeLoad.py#L143-L209)[¶](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues "Permalink to this definition")
    :   This method modifies the data for an existing ShellEdgeLoad object in the step where it is created.

        Note

        Check [ShellEdgeLoad.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shelledgeloadpyc.htm?contextscope=all#simaker-shelledgeloadsetvaluespyc).

        Parameters:[¶](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues-parameters "Permalink to this headline")
        :   distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the shell edge load is distributed spatially. Possible
                values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

            angle=`0`[¶](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.angle "Permalink to this definition")
            :   A Float specifying an additional rotation of **directionVector** about an axis. The
                default value is 0.This parameter is available only if **traction** is GENERAL.

            axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the axis about which to apply an additional rotation of
                **directionVector**. Possible values are AXIS\_1, AXIS\_2, AXIS\_3. The default value is
                AXIS\_1.This parameter is available only if **traction** is GENERAL.

            localCsys=`abaqusConstants.GENERAL`[¶](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.localCsys "Permalink to this definition")
            :   A DatumCsys object specifying the local coordinate system of the load’s degrees of
                freedom. The default value is None, indicating that the degrees of freedom are defined
                in the global coordinate system or by the **userCsys** parameter if defined. This
                parameter is available only if **traction** is GENERAL. When this member is queried, it
                returns an Int.

            userCsys=`abaqusConstants.GENERAL`[¶](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.userCsys "Permalink to this definition")
            :   A String specifying a CSYS defined by a user-subroutine. The default value is None,
                indicating that the degrees of freedom are defined in the global coordinate system or by
                the **localCsys** parameter if defined. This parameter is available only if **traction** is
                GENERAL.

            directionVector=`()`[¶](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.directionVector "Permalink to this definition")
            :   A tuple of two points specifying the direction of the load. Each point is specified as a
                point region or a tuple of coordinates. If **traction** is SHEAR, then **directionVector**
                will be projected onto the region surface. This parameter is available only if
                **traction** is GENERAL.

            follower=`1`[¶](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.follower "Permalink to this definition")
            :   A Boolean specifying whether the direction of the force changes with rotation. The
                default value is ON. This parameter may be modified only if **traction** is GENERAL. You
                should provide the **follower** argument only if it is valid for the specified step.

            resultant=`0`[¶](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.resultant "Permalink to this definition")
            :   A Boolean specifying whether to maintain a constant resultant force by defining traction
                per unit undeformed area. If **resultant** is OFF, traction is defined per unit deformed
                area. The default value is OFF. You should provide the **resultant** argument only if it
                is valid for the specified step.

            traction=`abaqusConstants.NORMAL`[¶](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValues.traction "Permalink to this definition")
            :   A SymbolicConstant specifying how to apply surface traction. Possible values are NORMAL,
                TRANSVERSE, SHEAR, MOMENT and GENERAL. The default value is NORMAL.

    setValuesInStep(*[stepName](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValuesInStep.stepName "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the surface pore fluid flow is modified.")*, *[magnitude](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValuesInStep.magnitude "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValuesInStep.magnitude (Python parameter) — A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the load magnitude. UNCHANGED should be used if the magnitude is propagated from the previous analysis step.")=`Ellipsis`*, *[amplitude](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValuesInStep.amplitude "abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ShellEdgeLoad.py#L211-L235)[¶](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing ShellEdgeLoad object in the specified step.

        Note

        Check [ShellEdgeLoad.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shelledgeloadpyc.htm?contextscope=all#simaker-shelledgeloadsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the surface pore fluid flow is
                modified.

            magnitude=`Ellipsis`[¶](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the load magnitude.
                UNCHANGED should be used if the magnitude is propagated from the previous analysis step.

            amplitude=`''`[¶](#abaqus.Load.ShellEdgeLoad.ShellEdgeLoad.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                load has no amplitude reference. You should provide the **amplitude** argument only if it
                is valid for the specified step.

*class* SubmodelSB(*[name](#abaqus.Load.SubmodelSB.SubmodelSB "abaqus.Load.SubmodelSB.SubmodelSB.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.SubmodelSB.SubmodelSB "abaqus.Load.SubmodelSB.SubmodelSB.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.SubmodelSB.SubmodelSB "abaqus.Load.SubmodelSB.SubmodelSB.__init__.region (Python parameter)")*, *[globalStep](#abaqus.Load.SubmodelSB.SubmodelSB "abaqus.Load.SubmodelSB.SubmodelSB.__init__.globalStep (Python parameter)")*, *[globalDrivingRegion](#abaqus.Load.SubmodelSB.SubmodelSB "abaqus.Load.SubmodelSB.SubmodelSB.__init__.globalDrivingRegion (Python parameter)")=`''`*, *[absoluteExteriorTolerance](#abaqus.Load.SubmodelSB.SubmodelSB "abaqus.Load.SubmodelSB.SubmodelSB.__init__.absoluteExteriorTolerance (Python parameter)")=`None`*, *[exteriorTolerance](#abaqus.Load.SubmodelSB.SubmodelSB "abaqus.Load.SubmodelSB.SubmodelSB.__init__.exteriorTolerance (Python parameter)")=`0`*, *[globalIncrement](#abaqus.Load.SubmodelSB.SubmodelSB "abaqus.Load.SubmodelSB.SubmodelSB.__init__.globalIncrement (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubmodelSB.py#L10-L158)[¶](#abaqus.Load.SubmodelSB.SubmodelSB "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The SubmodelSB object stores the data for a submodel surface based load. The SubmodelSB object is derived
    from the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [SubmodelSB on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-submodelsbpyc.htm?contextscope=all).

    Member Details:

    absoluteExteriorTolerance : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubmodelSB.py#L25-L27)[¶](#abaqus.Load.SubmodelSB.SubmodelSB.absoluteExteriorTolerance "Permalink to this definition")
    :   None or a Float specifying the absolute value by which a driven node of the submodel can
        lie outside the region of the elements of the global model. The default value is None.

    exteriorTolerance : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubmodelSB.py#L29-L32)[¶](#abaqus.Load.SubmodelSB.SubmodelSB.exteriorTolerance "Permalink to this definition")
    :   None or a Float specifying the fraction of the average element size in the global model
        by which a driven node of the submodel can lie outside the region of the elements of the
        global model. The default value is 0.05.

    globalDrivingRegion : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubmodelSB.py#L34-L37)[¶](#abaqus.Load.SubmodelSB.SubmodelSB.globalDrivingRegion "Permalink to this definition")
    :   A String specifying the element set in the global model that will be searched for
        elements whose responses will be used to drive the submodel. An empty string indicates
        that the entire global model will be searched. The default value is an empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubmodelSB.py#L22-L23)[¶](#abaqus.Load.SubmodelSB.SubmodelSB.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubmodelSB.py#L39-L40)[¶](#abaqus.Load.SubmodelSB.SubmodelSB.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[globalDrivingRegion](#abaqus.Load.SubmodelSB.SubmodelSB.setValues.globalDrivingRegion "abaqus.Load.SubmodelSB.SubmodelSB.setValues.globalDrivingRegion (Python parameter) — A String specifying the element set in the global model that will be searched for elements whose responses will be used to drive the submodel.")=`''`*, *[absoluteExteriorTolerance](#abaqus.Load.SubmodelSB.SubmodelSB.setValues.absoluteExteriorTolerance "abaqus.Load.SubmodelSB.SubmodelSB.setValues.absoluteExteriorTolerance (Python parameter) — None or a Float specifying the absolute value by which a driven node of the submodel can lie outside the region of the elements of the global model.")=`None`*, *[exteriorTolerance](#abaqus.Load.SubmodelSB.SubmodelSB.setValues.exteriorTolerance "abaqus.Load.SubmodelSB.SubmodelSB.setValues.exteriorTolerance (Python parameter) — None or a Float specifying the fraction of the average element size in the global model by which a driven node of the submodel can lie outside the region of the elements of the global model.")=`0`*, *[globalIncrement](#abaqus.Load.SubmodelSB.SubmodelSB.setValues.globalIncrement "abaqus.Load.SubmodelSB.SubmodelSB.setValues.globalIncrement (Python parameter) — An Int specifying the increment number in the global model step from which the solution will be used to specify the values of the driven variables.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubmodelSB.py#L98-L127)[¶](#abaqus.Load.SubmodelSB.SubmodelSB.setValues "Permalink to this definition")
    :   This method modifies the data for an existing SubmodelSB object in the step where it is created.

        Note

        Check [SubmodelSB.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-submodelsbpyc.htm?contextscope=all#simaker-submodelsbsetvaluespyc).

        Parameters:[¶](#abaqus.Load.SubmodelSB.SubmodelSB.setValues-parameters "Permalink to this headline")
        :   globalDrivingRegion=`''`[¶](#abaqus.Load.SubmodelSB.SubmodelSB.setValues.globalDrivingRegion "Permalink to this definition")
            :   A String specifying the element set in the global model that will be searched for
                elements whose responses will be used to drive the submodel. An empty string indicates
                that the entire global model will be searched. The default value is an empty string.

            absoluteExteriorTolerance=`None`[¶](#abaqus.Load.SubmodelSB.SubmodelSB.setValues.absoluteExteriorTolerance "Permalink to this definition")
            :   None or a Float specifying the absolute value by which a driven node of the submodel can
                lie outside the region of the elements of the global model. The default value is None.

            exteriorTolerance=`0`[¶](#abaqus.Load.SubmodelSB.SubmodelSB.setValues.exteriorTolerance "Permalink to this definition")
            :   None or a Float specifying the fraction of the average element size in the global model
                by which a driven node of the submodel can lie outside the region of the elements of the
                global model. The default value is 0.05.

            globalIncrement=`0`[¶](#abaqus.Load.SubmodelSB.SubmodelSB.setValues.globalIncrement "Permalink to this definition")
            :   An Int specifying the increment number in the global model step from which the solution
                will be used to specify the values of the driven variables. If **globalIncrement** = 0, the
                solution from the last increment will be used. The **globalIncrement** argument is
                applicable only for linear perturbation steps. The default value is 0.

    setValuesInStep(*[stepName](#abaqus.Load.SubmodelSB.SubmodelSB.setValuesInStep.stepName "abaqus.Load.SubmodelSB.SubmodelSB.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[fixed](#abaqus.Load.SubmodelSB.SubmodelSB.setValuesInStep.fixed "abaqus.Load.SubmodelSB.SubmodelSB.setValuesInStep.fixed (Python parameter) — A Boolean specifying whether the load should remain fixed at the current values at the start of the step.")=`1`*, *[globalStep](#abaqus.Load.SubmodelSB.SubmodelSB.setValuesInStep.globalStep "abaqus.Load.SubmodelSB.SubmodelSB.setValuesInStep.globalStep (Python parameter) — A String specifying the step in the global model from which Abaqus reads the values of the variables that will drive the submodel analysis.")=`''`*, *[globalIncrement](#abaqus.Load.SubmodelSB.SubmodelSB.setValuesInStep.globalIncrement "abaqus.Load.SubmodelSB.SubmodelSB.setValuesInStep.globalIncrement (Python parameter) — An Int specifying the increment number in the global model step at which the solution will be used to specify the values of the driven variables.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubmodelSB.py#L129-L158)[¶](#abaqus.Load.SubmodelSB.SubmodelSB.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing SubmodelSB object in the specified step.

        Note

        Check [SubmodelSB.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-submodelsbpyc.htm?contextscope=all#simaker-submodelsbsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.SubmodelSB.SubmodelSB.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.SubmodelSB.SubmodelSB.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            fixed=`1`[¶](#abaqus.Load.SubmodelSB.SubmodelSB.setValuesInStep.fixed "Permalink to this definition")
            :   A Boolean specifying whether the load should remain fixed at the current values at the
                start of the step. The default value is ON.

            globalStep=`''`[¶](#abaqus.Load.SubmodelSB.SubmodelSB.setValuesInStep.globalStep "Permalink to this definition")
            :   A String specifying the step in the global model from which Abaqus reads the values of
                the variables that will drive the submodel analysis. The String indicates the position
                of the step in the sequence of analysis steps. For example, **globalStep** = ‘1’ indicates
                the first step. The **globalStep** argument is applicable only if **fixed** = OFF.

            globalIncrement=`0`[¶](#abaqus.Load.SubmodelSB.SubmodelSB.setValuesInStep.globalIncrement "Permalink to this definition")
            :   An Int specifying the increment number in the global model step at which the solution
                will be used to specify the values of the driven variables. If **globalIncrement** = 0, the
                solution from the last increment will be used. The **globalIncrement** argument is
                applicable only for linear perturbation steps and if **fixed** = OFF. The default value is
                0.

*class* SubstructureLoad(*[name](#abaqus.Load.SubstructureLoad.SubstructureLoad "abaqus.Load.SubstructureLoad.SubstructureLoad.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.SubstructureLoad.SubstructureLoad "abaqus.Load.SubstructureLoad.SubstructureLoad.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.SubstructureLoad.SubstructureLoad "abaqus.Load.SubstructureLoad.SubstructureLoad.__init__.region (Python parameter)")*, *[loadCaseNames](#abaqus.Load.SubstructureLoad.SubstructureLoad "abaqus.Load.SubstructureLoad.SubstructureLoad.__init__.loadCaseNames (Python parameter)")*, *[magnitude](#abaqus.Load.SubstructureLoad.SubstructureLoad "abaqus.Load.SubstructureLoad.SubstructureLoad.__init__.magnitude (Python parameter)")*, *[amplitude](#abaqus.Load.SubstructureLoad.SubstructureLoad "abaqus.Load.SubstructureLoad.SubstructureLoad.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubstructureLoad.py#L10-L109)[¶](#abaqus.Load.SubstructureLoad.SubstructureLoad "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The SubstructureLoad object defines a substructure load. The SubstructureLoad object is derived from the
    Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [SubstructureLoad on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-substructureloadpyc.htm?contextscope=all).

    Member Details:

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubstructureLoad.py#L22-L23)[¶](#abaqus.Load.SubstructureLoad.SubstructureLoad.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubstructureLoad.py#L25-L26)[¶](#abaqus.Load.SubstructureLoad.SubstructureLoad.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[amplitude](#abaqus.Load.SubstructureLoad.SubstructureLoad.setValues.amplitude "abaqus.Load.SubstructureLoad.SubstructureLoad.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubstructureLoad.py#L69-L81)[¶](#abaqus.Load.SubstructureLoad.SubstructureLoad.setValues "Permalink to this definition")
    :   This method modifies the data for an existing SubstructureLoad object in the step where it is
        created.

        Note

        Check [SubstructureLoad.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-substructureloadpyc.htm?contextscope=all#simaker-substructureloadsetvaluespyc).

        Parameters:[¶](#abaqus.Load.SubstructureLoad.SubstructureLoad.setValues-parameters "Permalink to this headline")
        :   amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.SubstructureLoad.SubstructureLoad.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

    setValuesInStep(*[stepName](#abaqus.Load.SubstructureLoad.SubstructureLoad.setValuesInStep.stepName "abaqus.Load.SubstructureLoad.SubstructureLoad.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[loadCaseNames](#abaqus.Load.SubstructureLoad.SubstructureLoad.setValuesInStep.loadCaseNames "abaqus.Load.SubstructureLoad.SubstructureLoad.setValuesInStep.loadCaseNames (Python parameter) — A list of names of the load cases that should be activated by this substructure load.")=`''`*, *[magnitude](#abaqus.Load.SubstructureLoad.SubstructureLoad.setValuesInStep.magnitude "abaqus.Load.SubstructureLoad.SubstructureLoad.setValuesInStep.magnitude (Python parameter) — A Float specifying the multiplier for the load case magnitude.")=`None`*, *[amplitude](#abaqus.Load.SubstructureLoad.SubstructureLoad.setValuesInStep.amplitude "abaqus.Load.SubstructureLoad.SubstructureLoad.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubstructureLoad.py#L83-L109)[¶](#abaqus.Load.SubstructureLoad.SubstructureLoad.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing SubstructureLoad object in the specified
        step.

        Note

        Check [SubstructureLoad.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-substructureloadpyc.htm?contextscope=all#simaker-substructureloadsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.SubstructureLoad.SubstructureLoad.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.SubstructureLoad.SubstructureLoad.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            loadCaseNames=`''`[¶](#abaqus.Load.SubstructureLoad.SubstructureLoad.setValuesInStep.loadCaseNames "Permalink to this definition")
            :   A list of names of the load cases that should be activated by this substructure load.

            magnitude=`None`[¶](#abaqus.Load.SubstructureLoad.SubstructureLoad.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float specifying the multiplier for the load case magnitude.

            amplitude=`''`[¶](#abaqus.Load.SubstructureLoad.SubstructureLoad.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                load has no amplitude reference. You should provide the **amplitude** argument only if it
                is valid for the specified step.

*class* SurfaceCharge(*[name](#abaqus.Load.SurfaceCharge.SurfaceCharge "abaqus.Load.SurfaceCharge.SurfaceCharge.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.SurfaceCharge.SurfaceCharge "abaqus.Load.SurfaceCharge.SurfaceCharge.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.SurfaceCharge.SurfaceCharge "abaqus.Load.SurfaceCharge.SurfaceCharge.__init__.region (Python parameter)")*, *[magnitude](#abaqus.Load.SurfaceCharge.SurfaceCharge "abaqus.Load.SurfaceCharge.SurfaceCharge.__init__.magnitude (Python parameter)")*, *[distributionType](#abaqus.Load.SurfaceCharge.SurfaceCharge "abaqus.Load.SurfaceCharge.SurfaceCharge.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.SurfaceCharge.SurfaceCharge "abaqus.Load.SurfaceCharge.SurfaceCharge.__init__.field (Python parameter)")=`''`*, *[amplitude](#abaqus.Load.SurfaceCharge.SurfaceCharge "abaqus.Load.SurfaceCharge.SurfaceCharge.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCharge.py#L13-L130)[¶](#abaqus.Load.SurfaceCharge.SurfaceCharge "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The SurfaceCharge object stores the data for a surface charge. The SurfaceCharge object is derived from
    the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [SurfaceCharge on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacechargepyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCharge.py#L28-L30)[¶](#abaqus.Load.SurfaceCharge.SurfaceCharge.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
        UNIFORM and FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCharge.py#L32-L35)[¶](#abaqus.Load.SurfaceCharge.SurfaceCharge.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCharge.py#L25-L26)[¶](#abaqus.Load.SurfaceCharge.SurfaceCharge.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCharge.py#L37-L38)[¶](#abaqus.Load.SurfaceCharge.SurfaceCharge.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[distributionType](#abaqus.Load.SurfaceCharge.SurfaceCharge.setValues.distributionType "abaqus.Load.SurfaceCharge.SurfaceCharge.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.SurfaceCharge.SurfaceCharge.setValues.field "abaqus.Load.SurfaceCharge.SurfaceCharge.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[amplitude](#abaqus.Load.SurfaceCharge.SurfaceCharge.setValues.amplitude "abaqus.Load.SurfaceCharge.SurfaceCharge.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCharge.py#L88-L111)[¶](#abaqus.Load.SurfaceCharge.SurfaceCharge.setValues "Permalink to this definition")
    :   This method modifies the data for an existing SurfaceCharge object in the step where it is created.

        Note

        Check [SurfaceCharge.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacechargepyc.htm?contextscope=all#simaker-surfacechargesetvaluespyc).

        Parameters:[¶](#abaqus.Load.SurfaceCharge.SurfaceCharge.setValues-parameters "Permalink to this headline")
        :   distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.SurfaceCharge.SurfaceCharge.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.SurfaceCharge.SurfaceCharge.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.SurfaceCharge.SurfaceCharge.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

    setValuesInStep(*[stepName](#abaqus.Load.SurfaceCharge.SurfaceCharge.setValuesInStep.stepName "abaqus.Load.SurfaceCharge.SurfaceCharge.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[magnitude](#abaqus.Load.SurfaceCharge.SurfaceCharge.setValuesInStep.magnitude "abaqus.Load.SurfaceCharge.SurfaceCharge.setValuesInStep.magnitude (Python parameter) — A Float specifying the load magnitude.")=`None`*, *[amplitude](#abaqus.Load.SurfaceCharge.SurfaceCharge.setValuesInStep.amplitude "abaqus.Load.SurfaceCharge.SurfaceCharge.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCharge.py#L113-L130)[¶](#abaqus.Load.SurfaceCharge.SurfaceCharge.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing SurfaceCharge object in the specified step.

        Note

        Check [SurfaceCharge.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacechargepyc.htm?contextscope=all#simaker-surfacechargesetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.SurfaceCharge.SurfaceCharge.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.SurfaceCharge.SurfaceCharge.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            magnitude=`None`[¶](#abaqus.Load.SurfaceCharge.SurfaceCharge.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float specifying the load magnitude.

            amplitude=`''`[¶](#abaqus.Load.SurfaceCharge.SurfaceCharge.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous static analysis step. FREED should be used if
                the load is changed to have no amplitude reference. You should provide the **amplitude**
                argument only if it is valid for the specified step.

*class* SurfaceConcentrationFlux(*[name](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux "abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux "abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux "abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.__init__.region (Python parameter)")*, *[magnitude](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux "abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.__init__.magnitude (Python parameter)")*, *[field](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux "abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.__init__.field (Python parameter)")=`''`*, *[distributionType](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux "abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux "abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceConcentrationFlux.py#L13-L136)[¶](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The SurfaceConcentrationFlux object defines surface concentration flux from a region or into a region.
    The SurfaceConcentrationFlux object is derived from the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [SurfaceConcentrationFlux on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfaceconcentrationfluxpyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceConcentrationFlux.py#L28-L31)[¶](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the surface concentration flux is distributed
        spatially. Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is
        UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceConcentrationFlux.py#L33-L36)[¶](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceConcentrationFlux.py#L25-L26)[¶](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceConcentrationFlux.py#L38-L39)[¶](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[field](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.setValues.field "abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[distributionType](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.setValues.distributionType "abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the surface concentration flux is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.setValues.amplitude "abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceConcentrationFlux.py#L90-L115)[¶](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.setValues "Permalink to this definition")
    :   This method modifies the data for an existing SurfaceConcentrationFlux object in the step where it is
        created.

        Note

        Check [SurfaceConcentrationFlux.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfaceconcentrationfluxpyc.htm?contextscope=all#simaker-surfaceconcentrationfluxsetvaluespyc).

        Parameters:[¶](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.setValues-parameters "Permalink to this headline")
        :   field=`''`[¶](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the surface concentration flux is distributed
                spatially. Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is
                UNIFORM.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

    setValuesInStep(*[stepName](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.setValuesInStep.stepName "abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the surface concentration flux is modified.")*, *[magnitude](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.setValuesInStep.magnitude "abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.setValuesInStep.magnitude (Python parameter) — A Float specifying the surface concentration flux magnitude.")=`None`*, *[amplitude](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.setValuesInStep.amplitude "abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceConcentrationFlux.py#L117-L136)[¶](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing SurfaceConcentrationFlux object in the
        specified step.

        Note

        Check [SurfaceConcentrationFlux.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfaceconcentrationfluxpyc.htm?contextscope=all#simaker-surfaceconcentrationfluxsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the surface concentration flux is
                modified.

            magnitude=`None`[¶](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float specifying the surface concentration flux magnitude.

            amplitude=`''`[¶](#abaqus.Load.SurfaceConcentrationFlux.SurfaceConcentrationFlux.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                load has no amplitude reference. You should provide the **amplitude** argument only if it
                is valid for the specified step.

*class* SurfaceCurrent(*[name](#abaqus.Load.SurfaceCurrent.SurfaceCurrent "abaqus.Load.SurfaceCurrent.SurfaceCurrent.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.SurfaceCurrent.SurfaceCurrent "abaqus.Load.SurfaceCurrent.SurfaceCurrent.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.SurfaceCurrent.SurfaceCurrent "abaqus.Load.SurfaceCurrent.SurfaceCurrent.__init__.region (Python parameter)")*, *[magnitude](#abaqus.Load.SurfaceCurrent.SurfaceCurrent "abaqus.Load.SurfaceCurrent.SurfaceCurrent.__init__.magnitude (Python parameter)")*, *[distributionType](#abaqus.Load.SurfaceCurrent.SurfaceCurrent "abaqus.Load.SurfaceCurrent.SurfaceCurrent.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.SurfaceCurrent.SurfaceCurrent "abaqus.Load.SurfaceCurrent.SurfaceCurrent.__init__.field (Python parameter)")=`''`*, *[amplitude](#abaqus.Load.SurfaceCurrent.SurfaceCurrent "abaqus.Load.SurfaceCurrent.SurfaceCurrent.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCurrent.py#L13-L131)[¶](#abaqus.Load.SurfaceCurrent.SurfaceCurrent "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The SurfaceCurrent object stores the data for a surface current. The SurfaceCurrent object is derived
    from the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [SurfaceCurrent on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacecurrentpyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCurrent.py#L28-L30)[¶](#abaqus.Load.SurfaceCurrent.SurfaceCurrent.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
        UNIFORM and FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCurrent.py#L32-L35)[¶](#abaqus.Load.SurfaceCurrent.SurfaceCurrent.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCurrent.py#L25-L26)[¶](#abaqus.Load.SurfaceCurrent.SurfaceCurrent.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCurrent.py#L37-L38)[¶](#abaqus.Load.SurfaceCurrent.SurfaceCurrent.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[distributionType](#abaqus.Load.SurfaceCurrent.SurfaceCurrent.setValues.distributionType "abaqus.Load.SurfaceCurrent.SurfaceCurrent.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.SurfaceCurrent.SurfaceCurrent.setValues.field "abaqus.Load.SurfaceCurrent.SurfaceCurrent.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[amplitude](#abaqus.Load.SurfaceCurrent.SurfaceCurrent.setValues.amplitude "abaqus.Load.SurfaceCurrent.SurfaceCurrent.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCurrent.py#L88-L111)[¶](#abaqus.Load.SurfaceCurrent.SurfaceCurrent.setValues "Permalink to this definition")
    :   This method modifies the data for an existing SurfaceCurrent object in the step where it is created.

        Note

        Check [SurfaceCurrent.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacecurrentpyc.htm?contextscope=all#simaker-surfacecurrentsetvaluespyc).

        Parameters:[¶](#abaqus.Load.SurfaceCurrent.SurfaceCurrent.setValues-parameters "Permalink to this headline")
        :   distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.SurfaceCurrent.SurfaceCurrent.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.SurfaceCurrent.SurfaceCurrent.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.SurfaceCurrent.SurfaceCurrent.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

    setValuesInStep(*[stepName](#abaqus.Load.SurfaceCurrent.SurfaceCurrent.setValuesInStep.stepName "abaqus.Load.SurfaceCurrent.SurfaceCurrent.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[magnitude](#abaqus.Load.SurfaceCurrent.SurfaceCurrent.setValuesInStep.magnitude "abaqus.Load.SurfaceCurrent.SurfaceCurrent.setValuesInStep.magnitude (Python parameter) — A Float specifying the load magnitude.")=`None`*, *[amplitude](#abaqus.Load.SurfaceCurrent.SurfaceCurrent.setValuesInStep.amplitude "abaqus.Load.SurfaceCurrent.SurfaceCurrent.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCurrent.py#L113-L131)[¶](#abaqus.Load.SurfaceCurrent.SurfaceCurrent.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing SurfaceCurrent object in the specified
        step.

        Note

        Check [SurfaceCurrent.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacecurrentpyc.htm?contextscope=all#simaker-surfacecurrentsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.SurfaceCurrent.SurfaceCurrent.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.SurfaceCurrent.SurfaceCurrent.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            magnitude=`None`[¶](#abaqus.Load.SurfaceCurrent.SurfaceCurrent.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float specifying the load magnitude.

            amplitude=`''`[¶](#abaqus.Load.SurfaceCurrent.SurfaceCurrent.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous static analysis step. FREED should be used if
                the load is changed to have no amplitude reference. You should provide the **amplitude**
                argument only if it is valid for the specified step.

*class* SurfaceCurrentDensity(*[name](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity "abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity "abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity "abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.__init__.region (Python parameter)")*, *[comp1](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity "abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.__init__.comp1 (Python parameter)")*, *[comp2](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity "abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.__init__.comp2 (Python parameter)")*, *[comp3](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity "abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.__init__.comp3 (Python parameter)")*, *[distributionType](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity "abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity "abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCurrentDensity.py#L13-L130)[¶](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The SurfaceCurrentDensity object stores the data for a surface current. The SurfaceCurrentDensity object
    is derived from the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [SurfaceCurrentDensity on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacecurrentdensitypyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCurrentDensity.py#L28-L30)[¶](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
        UNIFORM and USER\_DEFINED. The default value is UNIFORM.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCurrentDensity.py#L25-L26)[¶](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCurrentDensity.py#L32-L33)[¶](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[distributionType](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValues.distributionType "abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the load is distributed spatially.")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValues.amplitude "abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCurrentDensity.py#L84-L99)[¶](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValues "Permalink to this definition")
    :   This method modifies the data for an existing SurfaceCurrentDensity object in the step where it is
        created.

        Note

        Check [SurfaceCurrentDensity.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacecurrentdensitypyc.htm?contextscope=all#simaker-surfacecurrentdensitysetvaluespyc).

        Parameters:[¶](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValues-parameters "Permalink to this headline")
        :   distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the load is distributed spatially. Possible values are
                UNIFORM and USER\_DEFINED. The default value is UNIFORM.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

    setValuesInStep(*[stepName](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValuesInStep.stepName "abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[comp1](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValuesInStep.comp1 "abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValuesInStep.comp1 (Python parameter) — A Complex specifying the first component of the load.")=`''`*, *[comp2](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValuesInStep.comp2 "abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValuesInStep.comp2 (Python parameter) — A Complex specifying the second component of the load.")=`''`*, *[comp3](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValuesInStep.comp3 "abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValuesInStep.comp3 (Python parameter) — A Complex specifying the third component of the load.")=`''`*, *[amplitude](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValuesInStep.amplitude "abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCurrentDensity.py#L101-L130)[¶](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing SurfaceCurrentDensity object in the
        specified step.

        Note

        Check [SurfaceCurrentDensity.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacecurrentdensitypyc.htm?contextscope=all#simaker-surfacecurrentdensitysetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            comp1=`''`[¶](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValuesInStep.comp1 "Permalink to this definition")
            :   A Complex specifying the first component of the load.

            comp2=`''`[¶](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValuesInStep.comp2 "Permalink to this definition")
            :   A Complex specifying the second component of the load.

            comp3=`''`[¶](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValuesInStep.comp3 "Permalink to this definition")
            :   A Complex specifying the third component of the load.

            amplitude=`''`[¶](#abaqus.Load.SurfaceCurrentDensity.SurfaceCurrentDensity.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous static analysis step. FREED should be used if
                the load is changed to have no amplitude reference. You should provide the **amplitude**
                argument only if it is valid for the specified step.

*class* SurfaceHeatFlux(*[name](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux "abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux "abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux "abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.__init__.region (Python parameter)")*, *[magnitude](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux "abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.__init__.magnitude (Python parameter)")*, *[field](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux "abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.__init__.field (Python parameter)")=`''`*, *[distributionType](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux "abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux "abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceHeatFlux.py#L13-L131)[¶](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The SurfaceHeatFlux object defines surface heat flux from a region or into a region. The SurfaceHeatFlux
    object is derived from the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [SurfaceHeatFlux on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfaceheatfluxpyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceHeatFlux.py#L28-L30)[¶](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the surface heat flux is distributed spatially.
        Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceHeatFlux.py#L32-L35)[¶](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceHeatFlux.py#L25-L26)[¶](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceHeatFlux.py#L37-L38)[¶](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[field](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.setValues.field "abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[distributionType](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.setValues.distributionType "abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the surface heat flux is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD.")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.setValues.amplitude "abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceHeatFlux.py#L88-L111)[¶](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.setValues "Permalink to this definition")
    :   This method modifies the data for an existing SurfaceHeatFlux object in the step where it is created.

        Note

        Check [SurfaceHeatFlux.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfaceheatfluxpyc.htm?contextscope=all#simaker-surfaceheatfluxsetvaluespyc).

        Parameters:[¶](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.setValues-parameters "Permalink to this headline")
        :   field=`''`[¶](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the surface heat flux is distributed spatially.
                Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

    setValuesInStep(*[stepName](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.setValuesInStep.stepName "abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the surface heat flux is modified.")*, *[magnitude](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.setValuesInStep.magnitude "abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.setValuesInStep.magnitude (Python parameter) — A Float specifying the surface heat flux magnitude.")=`None`*, *[amplitude](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.setValuesInStep.amplitude "abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceHeatFlux.py#L113-L131)[¶](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing SurfaceHeatFlux object in the specified
        step.

        Note

        Check [SurfaceHeatFlux.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfaceheatfluxpyc.htm?contextscope=all#simaker-surfaceheatfluxsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the surface heat flux is modified.

            magnitude=`None`[¶](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float specifying the surface heat flux magnitude.

            amplitude=`''`[¶](#abaqus.Load.SurfaceHeatFlux.SurfaceHeatFlux.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                load has no amplitude reference. You should provide the **amplitude** argument only if it
                is valid for the specified step.

*class* SurfacePoreFluid(*[name](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid "abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid "abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid "abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.__init__.region (Python parameter)")*, *[magnitude](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid "abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.__init__.magnitude (Python parameter)")*, *[field](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid "abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.__init__.field (Python parameter)")=`''`*, *[distributionType](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid "abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid "abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfacePoreFluid.py#L13-L133)[¶](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The SurfacePoreFluid object defines surface pore fluid flow from a region or into a region. The
    SurfacePoreFluid object is derived from the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [SurfacePoreFluid on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfaceporefluidpyc.htm?contextscope=all).

    Member Details:

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfacePoreFluid.py#L28-L30)[¶](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM,
        USER\_DEFINED, and FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfacePoreFluid.py#L32-L35)[¶](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfacePoreFluid.py#L25-L26)[¶](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfacePoreFluid.py#L37-L38)[¶](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    setValues(*[field](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.setValues.field "abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[distributionType](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.setValues.distributionType "abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.setValues.distributionType (Python parameter) — A SymbolicConstant specifying whether the load is uniform.")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.setValues.amplitude "abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfacePoreFluid.py#L88-L112)[¶](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.setValues "Permalink to this definition")
    :   This method modifies the data for an existing SurfacePoreFluid object in the step where it is
        created.

        Note

        Check [SurfacePoreFluid.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfaceporefluidpyc.htm?contextscope=all#simaker-surfaceporefluidsetvaluespyc).

        Parameters:[¶](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.setValues-parameters "Permalink to this headline")
        :   field=`''`[¶](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying whether the load is uniform. Possible values are UNIFORM,
                USER\_DEFINED, and FIELD. The default value is UNIFORM.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

    setValuesInStep(*[stepName](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.setValuesInStep.stepName "abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the surface pore fluid flow is modified.")*, *[magnitude](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.setValuesInStep.magnitude "abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.setValuesInStep.magnitude (Python parameter) — A Float specifying the surface pore fluid flow magnitude.")=`None`*, *[amplitude](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.setValuesInStep.amplitude "abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfacePoreFluid.py#L114-L133)[¶](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing SurfacePoreFluid object in the specified
        step.

        Note

        Check [SurfacePoreFluid.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfaceporefluidpyc.htm?contextscope=all#simaker-surfaceporefluidsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the surface pore fluid flow is
                modified.

            magnitude=`None`[¶](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float specifying the surface pore fluid flow magnitude.

            amplitude=`''`[¶](#abaqus.Load.SurfacePoreFluid.SurfacePoreFluid.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                load has no amplitude reference. You should provide the **amplitude** argument only if it
                is valid for the specified step.

*class* SurfaceTraction(*[name](#abaqus.Load.SurfaceTraction.SurfaceTraction "abaqus.Load.SurfaceTraction.SurfaceTraction.__init__.name (Python parameter)")*, *[createStepName](#abaqus.Load.SurfaceTraction.SurfaceTraction "abaqus.Load.SurfaceTraction.SurfaceTraction.__init__.createStepName (Python parameter)")*, *[region](#abaqus.Load.SurfaceTraction.SurfaceTraction "abaqus.Load.SurfaceTraction.SurfaceTraction.__init__.region (Python parameter)")*, *[magnitude](#abaqus.Load.SurfaceTraction.SurfaceTraction "abaqus.Load.SurfaceTraction.SurfaceTraction.__init__.magnitude (Python parameter)")*, *[distributionType](#abaqus.Load.SurfaceTraction.SurfaceTraction "abaqus.Load.SurfaceTraction.SurfaceTraction.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.SurfaceTraction.SurfaceTraction "abaqus.Load.SurfaceTraction.SurfaceTraction.__init__.field (Python parameter)")=`''`*, *[amplitude](#abaqus.Load.SurfaceTraction.SurfaceTraction "abaqus.Load.SurfaceTraction.SurfaceTraction.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[angle](#abaqus.Load.SurfaceTraction.SurfaceTraction "abaqus.Load.SurfaceTraction.SurfaceTraction.__init__.angle (Python parameter)")=`0`*, *[axis](#abaqus.Load.SurfaceTraction.SurfaceTraction "abaqus.Load.SurfaceTraction.SurfaceTraction.__init__.axis (Python parameter)")=`abaqusConstants.AXIS_1`*, *[localCsys](#abaqus.Load.SurfaceTraction.SurfaceTraction "abaqus.Load.SurfaceTraction.SurfaceTraction.__init__.localCsys (Python parameter)")=`None`*, *[userCsys](#abaqus.Load.SurfaceTraction.SurfaceTraction "abaqus.Load.SurfaceTraction.SurfaceTraction.__init__.userCsys (Python parameter)")=`''`*, *[directionVector](#abaqus.Load.SurfaceTraction.SurfaceTraction "abaqus.Load.SurfaceTraction.SurfaceTraction.__init__.directionVector (Python parameter)")=`()`*, *[follower](#abaqus.Load.SurfaceTraction.SurfaceTraction "abaqus.Load.SurfaceTraction.SurfaceTraction.__init__.follower (Python parameter)")=`1`*, *[resultant](#abaqus.Load.SurfaceTraction.SurfaceTraction "abaqus.Load.SurfaceTraction.SurfaceTraction.__init__.resultant (Python parameter)")=`0`*, *[traction](#abaqus.Load.SurfaceTraction.SurfaceTraction "abaqus.Load.SurfaceTraction.SurfaceTraction.__init__.traction (Python parameter)")=`abaqusConstants.SHEAR`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTraction.py#L24-L271)[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction "Permalink to this definition")
:   Bases: [`Load`](#abaqus.Load.SurfaceTraction.Load "abaqus.Load.Load.Load (Python class)")

    The SurfaceTraction object defines surface traction on a region. The SurfaceTraction object is derived
    from the Load object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].loads[name]
    ```

    Note

    Check [SurfaceTraction on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacetractionpyc.htm?contextscope=all).

    Member Details:

    angle : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTraction.py#L39-L41)[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.angle "Permalink to this definition")
    :   A Float specifying an additional rotation of **directionVector** about an axis. The
        default value is 0.0.

    axis : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'AXIS_1'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTraction.py#L43-L46)[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.axis "Permalink to this definition")
    :   A SymbolicConstant specifying the axis about which to apply an additional rotation of
        **directionVector**. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default value is
        AXIS\_1.

    directionVector : --is-rst--:py:class:`tuple` = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTraction.py#L83-L87)[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.directionVector "Permalink to this definition")
    :   A VertexArray object of length 2 specifying the direction of the load. Instead of
        through a ConstrainedSketchVertex, each point may be specified through a tuple of coordinates. If
        **traction** is SHEAR, then **directionVector** will be projected onto the region surface.
        This parameter is available only if **traction** is GENERAL or SHEAR.

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTraction.py#L63-L65)[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the surface traction is distributed spatially.
        Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

    field : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTraction.py#L67-L70)[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.field "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this load.
        The **field** argument applies only when **distributionType** = FIELD. The default value is an
        empty string.

    follower : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTraction.py#L48-L51)[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.follower "Permalink to this definition")
    :   A Boolean specifying whether the direction of the force changes with rotation. The
        default value is ON.This parameter may be modified only if **traction** is GENERAL. You
        should provide the **follower** argument only if it is valid for the specified step.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTraction.py#L77-L81)[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the load’s degrees
        of freedom. If **localCsys** = None, the degrees of freedom are defined in the global
        coordinate system or by the **userCsys** parameter if defined. When this member is
        queried, it returns an Int. The default value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTraction.py#L36-L37)[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.name "Permalink to this definition")
    :   A String specifying the load repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTraction.py#L89-L90)[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.region "Permalink to this definition")
    :   A Region object specifying the region to which the load is applied.

    resultant : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTraction.py#L53-L57)[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.resultant "Permalink to this definition")
    :   A Boolean specifying whether the to maintain a constant resultant force by defining
        traction per unit undeformed area. If **resultant** is OFF, traction is defined per unit
        deformed area. The default value is OFF.You should provide the **resultant** argument only
        if it is valid for the specified step.

    setValues(*[distributionType](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.distributionType "abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the surface traction is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD.")=`abaqusConstants.UNIFORM`*, *[field](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.field "abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.field (Python parameter) — A String specifying the name of the AnalyticalField object associated with this load. The field argument applies only when distributionType = FIELD.")=`''`*, *[amplitude](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.amplitude "abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the load has no amplitude reference.")=`abaqusConstants.UNSET`*, *[angle](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.angle "abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.angle (Python parameter) — A Float specifying an additional rotation of directionVector about an axis.")=`0`*, *[axis](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.axis "abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.axis (Python parameter) — A SymbolicConstant specifying the axis about which to apply an additional rotation of directionVector.")=`abaqusConstants.AXIS_1`*, *[localCsys](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.localCsys "abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the load's degrees of freedom.")=`None`*, *[userCsys](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.userCsys "abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.userCsys (Python parameter) — A String specifying a CSYS defined by a user-subroutine.")=`''`*, *[directionVector](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.directionVector "abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.directionVector (Python parameter) — A VertexArray object of length 2 specifying the direction of the load.")=`()`*, *[follower](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.follower "abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.follower (Python parameter) — A Boolean specifying whether the direction of the force changes with rotation.")=`1`*, *[resultant](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.resultant "abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.resultant (Python parameter) — A Boolean specifying whether the to maintain a constant resultant force by defining traction per unit undeformed area.")=`0`*, *[traction](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.traction "abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.traction (Python parameter) — A SymbolicConstant specifying how to apply surface traction.")=`abaqusConstants.SHEAR`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTraction.py#L181-L245)[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValues "Permalink to this definition")
    :   This method modifies the data for an existing SurfaceTraction object in the step where it is created.

        Note

        Check [SurfaceTraction.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacetractionpyc.htm?contextscope=all#simaker-surfacetractionsetvaluespyc).

        Parameters:[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValues-parameters "Permalink to this headline")
        :   distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the surface traction is distributed spatially.
                Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            field=`''`[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.field "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this load.
                The **field** argument applies only when **distributionType** = FIELD. The default value is an
                empty string.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the load has no amplitude reference. The default value is UNSET.
                You should provide the **amplitude** argument only if it is valid for the specified step.

            angle=`0`[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.angle "Permalink to this definition")
            :   A Float specifying an additional rotation of **directionVector** about an axis. The
                default value is 0.0.

            axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the axis about which to apply an additional rotation of
                **directionVector**. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default value is
                AXIS\_1.

            localCsys=`None`[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the load’s degrees
                of freedom. If **localCsys** = None, the degrees of freedom are defined in the global
                coordinate system or by the **userCsys** parameter if defined. When this member is
                queried, it returns an Int. The default value is None.

            userCsys=`''`[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.userCsys "Permalink to this definition")
            :   A String specifying a CSYS defined by a user-subroutine. If **userCsys** = None, the degrees
                of freedom are defined in the global coordinate system or by the **localCsys** parameter
                if defined. The default value is “None”.

            directionVector=`()`[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.directionVector "Permalink to this definition")
            :   A VertexArray object of length 2 specifying the direction of the load. Instead of
                through a ConstrainedSketchVertex, each point may be specified through a tuple of coordinates. If
                **traction** is SHEAR, then **directionVector** will be projected onto the region surface.
                This parameter is available only if **traction** is GENERAL or SHEAR.

            follower=`1`[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.follower "Permalink to this definition")
            :   A Boolean specifying whether the direction of the force changes with rotation. The
                default value is ON.This parameter may be modified only if **traction** is GENERAL. You
                should provide the **follower** argument only if it is valid for the specified step.

            resultant=`0`[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.resultant "Permalink to this definition")
            :   A Boolean specifying whether the to maintain a constant resultant force by defining
                traction per unit undeformed area. If **resultant** is OFF, traction is defined per unit
                deformed area. The default value is OFF.You should provide the **resultant** argument only
                if it is valid for the specified step.

            traction=`abaqusConstants.SHEAR`[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValues.traction "Permalink to this definition")
            :   A SymbolicConstant specifying how to apply surface traction. Possible values are SHEAR
                and GENERAL. The default value is SHEAR.

    setValuesInStep(*[stepName](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValuesInStep.stepName "abaqus.Load.SurfaceTraction.SurfaceTraction.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the load is modified.")*, *[magnitude](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValuesInStep.magnitude "abaqus.Load.SurfaceTraction.SurfaceTraction.setValuesInStep.magnitude (Python parameter) — A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the load magnitude. UNCHANGED should be used if the magnitude is propagated from the previous analysis step.")=`Ellipsis`*, *[amplitude](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValuesInStep.amplitude "abaqus.Load.SurfaceTraction.SurfaceTraction.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTraction.py#L247-L271)[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing SurfaceTraction object in the specified
        step.

        Note

        Check [SurfaceTraction.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacetractionpyc.htm?contextscope=all#simaker-surfacetractionsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the load is modified.

            magnitude=`Ellipsis`[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float, a Complex, or the SymbolicConstant UNCHANGED specifying the load magnitude.
                UNCHANGED should be used if the magnitude is propagated from the previous analysis step.

            amplitude=`''`[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                load has no amplitude reference. You should provide the **amplitude** argument only if it
                is valid for the specified step.

    traction : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'SHEAR'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTraction.py#L59-L61)[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.traction "Permalink to this definition")
    :   A SymbolicConstant specifying how to apply surface traction. Possible values are SHEAR
        and GENERAL. The default value is SHEAR.

    userCsys : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTraction.py#L72-L75)[¶](#abaqus.Load.SurfaceTraction.SurfaceTraction.userCsys "Permalink to this definition")
    :   A String specifying a CSYS defined by a user-subroutine. If **userCsys** = None, the degrees
        of freedom are defined in the global coordinate system or by the **localCsys** parameter
        if defined. The default value is “None”.

*class* LoadStep[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadStep.py#L10-L51)[¶](#abaqus.Load.LoadStep.LoadStep "Permalink to this definition")
:   Bases: [`StepBase`](step/index.html#abaqus.Step.StepBase.StepBase "abaqus.Step.StepBase.StepBase (Python class) — Bases: object")

    Member Details:

    LoadCase(*[name](#abaqus.Load.LoadStep.LoadStep.LoadCase.name "abaqus.Load.LoadStep.LoadStep.LoadCase.name (Python parameter) — A String specifying the name of the object.")*, *[boundaryConditions](#abaqus.Load.LoadStep.LoadStep.LoadCase.boundaryConditions "abaqus.Load.LoadStep.LoadStep.LoadCase.boundaryConditions (Python parameter) — A sequence of (String, Float) sequences specifying the name of a BoundaryCondition followed by a nonzero Float scaling factor.")=`()`*, *[loads](#abaqus.Load.LoadStep.LoadStep.LoadCase.loads "abaqus.Load.LoadStep.LoadStep.LoadCase.loads (Python parameter) — A sequence of (String, Float) sequences specifying the name of a Load followed by a nonzero Float specifying a scale factor.")=`()`*, *[includeActiveBaseStateBC](#abaqus.Load.LoadStep.LoadStep.LoadCase.includeActiveBaseStateBC "abaqus.Load.LoadStep.LoadStep.LoadCase.includeActiveBaseStateBC (Python parameter) — A Boolean specifying whether to include all active boundary conditions propagated or modified from the base state.")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/LoadStep.py#L12-L51)[¶](#abaqus.Load.LoadStep.LoadStep.LoadCase "Permalink to this definition")
    :   This method creates a load case in a step.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].steps[name].LoadCase
        ```

        Note

        Check [LoadCase on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-loadcasepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Load.LoadStep.LoadStep.LoadCase-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Load.LoadStep.LoadStep.LoadCase.name "Permalink to this definition")
            :   A String specifying the name of the object.

            boundaryConditions=`()`[¶](#abaqus.Load.LoadStep.LoadStep.LoadCase.boundaryConditions "Permalink to this definition")
            :   A sequence of (String, Float) sequences specifying the name of a BoundaryCondition
                followed by a nonzero Float scaling factor. The default value is an empty sequence.

            loads=`()`[¶](#abaqus.Load.LoadStep.LoadStep.LoadCase.loads "Permalink to this definition")
            :   A sequence of (String, Float) sequences specifying the name of a Load followed by a
                nonzero Float specifying a scale factor. The default value is an empty sequence.

            includeActiveBaseStateBC=`1`[¶](#abaqus.Load.LoadStep.LoadStep.LoadCase.includeActiveBaseStateBC "Permalink to this definition")
            :   A Boolean specifying whether to include all active boundary conditions propagated or
                modified from the base state. The default value is ON.

        Returns:[¶](#abaqus.Load.LoadStep.LoadStep.LoadCase-returns "Permalink to this headline")
        :   A LoadCase object.

        Return type:[¶](#abaqus.Load.LoadStep.LoadStep.LoadCase-return-type "Permalink to this headline")
        :   [`LoadCase`](#abaqus.Load.LoadStep.LoadCase "abaqus.Load.LoadStep.LoadCase (Python class) — Bases: object")

        Raises:[¶](#abaqus.Load.LoadStep.LoadStep.LoadCase-raises "Permalink to this headline")
        :   **RangeError** –

*class* MomentState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/MomentState.py#L9-L68)[¶](#abaqus.Load.MomentState.MomentState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The MomentState object stores the propagating data for a moment in a step. One instance of this object is
    created internally by the Moment object for each step. The instance is also deleted internally by the Moment
    object. The MomentState object has no constructor or methods. The MomentState object is derived from the
    LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * CLOAD

    Note

    Check [MomentState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-momentstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/MomentState.py#L9-L68)[¶](#abaqus.Load.MomentState.MomentState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/MomentState.py)[¶](#abaqus.Load.MomentState.MomentState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    cm1 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/MomentState.py#L27-L28)[¶](#abaqus.Load.MomentState.MomentState.cm1 "Permalink to this definition")
    :   A Float or a Complex specifying the load component in the 4-direction.

    cm1State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/MomentState.py)[¶](#abaqus.Load.MomentState.MomentState.cm1State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load component in the
        4-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.

    cm2 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/MomentState.py#L30-L31)[¶](#abaqus.Load.MomentState.MomentState.cm2 "Permalink to this definition")
    :   A Float or a Complex specifying the load component in the 5-direction.

    cm2State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/MomentState.py)[¶](#abaqus.Load.MomentState.MomentState.cm2State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load component in the
        5-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.

    cm3 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/MomentState.py#L33-L34)[¶](#abaqus.Load.MomentState.MomentState.cm3 "Permalink to this definition")
    :   A Float or a Complex specifying the load component in the 6-direction.

    cm3State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/MomentState.py)[¶](#abaqus.Load.MomentState.MomentState.cm3State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load component in the
        6-direction. Possible values are UNSET, SET, UNCHANGED, and FREED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/MomentState.py)[¶](#abaqus.Load.MomentState.MomentState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* PEGLoadState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PEGLoadState.py#L9-L68)[¶](#abaqus.Load.PEGLoadState.PEGLoadState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The PEGLoadState object stores the propagating data for a concentrated force in a step. One instance of
    this object is created internally by the PEGLoad object for each step. The instance is also deleted
    internally by the PEGLoad object. The PEGLoadState object has no constructor or methods. The PEGLoadState
    object is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * CLOAD

    Note

    Check [PEGLoadState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pegloadstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PEGLoadState.py#L9-L68)[¶](#abaqus.Load.PEGLoadState.PEGLoadState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PEGLoadState.py)[¶](#abaqus.Load.PEGLoadState.PEGLoadState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    comp1 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PEGLoadState.py#L27-L28)[¶](#abaqus.Load.PEGLoadState.PEGLoadState.comp1 "Permalink to this definition")
    :   A Float or a Complex specifying the load component at dof 1 of reference node 1.

    comp1State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PEGLoadState.py)[¶](#abaqus.Load.PEGLoadState.PEGLoadState.comp1State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load component at dof 1 of
        reference node 1. Possible values are UNSET, SET, UNCHANGED, and FREED.

    comp2 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PEGLoadState.py#L30-L31)[¶](#abaqus.Load.PEGLoadState.PEGLoadState.comp2 "Permalink to this definition")
    :   A Float or a Complex specifying the load component at dof 1 of reference node 2.

    comp2State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PEGLoadState.py)[¶](#abaqus.Load.PEGLoadState.PEGLoadState.comp2State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load component at dof 1 of
        reference node 2. Possible values are UNSET, SET, UNCHANGED, and FREED.

    comp3 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PEGLoadState.py#L33-L34)[¶](#abaqus.Load.PEGLoadState.PEGLoadState.comp3 "Permalink to this definition")
    :   A Float or a Complex specifying the load component at dof 2 of reference node 2.

    comp3State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PEGLoadState.py)[¶](#abaqus.Load.PEGLoadState.PEGLoadState.comp3State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load component at dof 2 of
        reference node 2. Possible values are UNSET, SET, UNCHANGED, and FREED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PEGLoadState.py)[¶](#abaqus.Load.PEGLoadState.PEGLoadState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* PipePressureState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PipePressureState.py#L9-L71)[¶](#abaqus.Load.PipePressureState.PipePressureState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The PipePressureState object stores the propagating data for a pipe pressure in a step. One instance of
    this object is created internally by the PipePressure object for each step. The instance is also deleted
    internally by the PipePressure object. The PipePressureState object has no constructor or methods. The
    PipePressureState object is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * DSLOAD
    * DLOAD

    Note

    Check [PipePressureState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pipepressurestatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PipePressureState.py#L9-L71)[¶](#abaqus.Load.PipePressureState.PipePressureState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PipePressureState.py)[¶](#abaqus.Load.PipePressureState.PipePressureState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    hReference : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PipePressureState.py#L43-L45)[¶](#abaqus.Load.PipePressureState.PipePressureState.hReference "Permalink to this definition")
    :   A Float specifying the height of the reference pressure level when the pipe pressure
        **distributionType** = HYDROSTATIC.

    hReferenceState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PipePressureState.py)[¶](#abaqus.Load.PipePressureState.PipePressureState.hReferenceState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of **hReference**. Possible values are
        UNSET, SET, UNCHANGED, and FREED.

    hZero : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PipePressureState.py#L35-L37)[¶](#abaqus.Load.PipePressureState.PipePressureState.hZero "Permalink to this definition")
    :   A Float specifying the height of the zero pressure level when the pipe pressure
        **distributionType** = HYDROSTATIC.

    hZeroState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PipePressureState.py)[¶](#abaqus.Load.PipePressureState.PipePressureState.hZeroState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of **hZero**. Possible values are
        UNSET, SET, UNCHANGED, and FREED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PipePressureState.py#L28-L29)[¶](#abaqus.Load.PipePressureState.PipePressureState.magnitude "Permalink to this definition")
    :   A Float or a Complex specifying the load magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PipePressureState.py)[¶](#abaqus.Load.PipePressureState.PipePressureState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load magnitude. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PipePressureState.py)[¶](#abaqus.Load.PipePressureState.PipePressureState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* PressureState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PressureState.py#L9-L71)[¶](#abaqus.Load.PressureState.PressureState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The PressureState object stores the propagating data for a pressure in a step. One instance of this
    object is created internally by the Pressure object for each step. The instance is also deleted internally
    by the Pressure object. The PressureState object has no constructor or methods. The PressureState object is
    derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * DSLOAD
    * DLOAD

    Note

    Check [PressureState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pressurestatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PressureState.py#L9-L71)[¶](#abaqus.Load.PressureState.PressureState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PressureState.py)[¶](#abaqus.Load.PressureState.PressureState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    hReference : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PressureState.py#L43-L45)[¶](#abaqus.Load.PressureState.PressureState.hReference "Permalink to this definition")
    :   A Float specifying the height of the reference pressure level when the pressure
        **distributionType** = HYDROSTATIC.

    hReferenceState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PressureState.py)[¶](#abaqus.Load.PressureState.PressureState.hReferenceState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of **hReference**. Possible values are
        UNSET, SET, UNCHANGED, and FREED.

    hZero : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PressureState.py#L35-L37)[¶](#abaqus.Load.PressureState.PressureState.hZero "Permalink to this definition")
    :   A Float specifying the height of the zero pressure level when the pressure
        **distributionType** = HYDROSTATIC.

    hZeroState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PressureState.py)[¶](#abaqus.Load.PressureState.PressureState.hZeroState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of **hZero**. Possible values are
        UNSET, SET, UNCHANGED, and FREED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PressureState.py#L28-L29)[¶](#abaqus.Load.PressureState.PressureState.magnitude "Permalink to this definition")
    :   A Float or a Complex specifying the pressure magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PressureState.py)[¶](#abaqus.Load.PressureState.PressureState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the pressure magnitude. Possible
        values are UNSET, SET, UNCHANGED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/PressureState.py)[¶](#abaqus.Load.PressureState.PressureState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* RotationalBodyForceState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/RotationalBodyForceState.py#L9-L54)[¶](#abaqus.Load.RotationalBodyForceState.RotationalBodyForceState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The RotationalBodyForceState object stores the propagating data of a rotational body force in a step. One
    instance of this object is created internally by the RotationalBodyForce object for each step. The instance
    is also deleted internally by the RotationalBodyForce object. The RotationalBodyForceState object has no
    constructor or methods. The RotationalBodyForceState object is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * DLOAD

    Note

    Check [RotationalBodyForceState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rotationalbodyforcestatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/RotationalBodyForceState.py#L9-L54)[¶](#abaqus.Load.RotationalBodyForceState.RotationalBodyForceState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/RotationalBodyForceState.py)[¶](#abaqus.Load.RotationalBodyForceState.RotationalBodyForceState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/RotationalBodyForceState.py#L27-L28)[¶](#abaqus.Load.RotationalBodyForceState.RotationalBodyForceState.magnitude "Permalink to this definition")
    :   A Float specifying the load magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/RotationalBodyForceState.py)[¶](#abaqus.Load.RotationalBodyForceState.RotationalBodyForceState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load magnitude. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/RotationalBodyForceState.py)[¶](#abaqus.Load.RotationalBodyForceState.RotationalBodyForceState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* ShellEdgeLoadState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ShellEdgeLoadState.py#L9-L55)[¶](#abaqus.Load.ShellEdgeLoadState.ShellEdgeLoadState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The ShellEdgeLoadState object stores the propagating data for a ShellEdgeLoad object in a step. One
    instance of this object is created internally by the ShellEdgeLoad object for each step. The instance is
    also deleted internally by the ShellEdgeLoad object. The ShellEdgeLoadState object has no constructor or
    methods. The ShellEdgeLoadState object is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * DSLOAD
    * DLOAD

    Note

    Check [ShellEdgeLoadState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shelledgeloadstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ShellEdgeLoadState.py#L9-L55)[¶](#abaqus.Load.ShellEdgeLoadState.ShellEdgeLoadState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ShellEdgeLoadState.py)[¶](#abaqus.Load.ShellEdgeLoadState.ShellEdgeLoadState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ShellEdgeLoadState.py#L28-L29)[¶](#abaqus.Load.ShellEdgeLoadState.ShellEdgeLoadState.magnitude "Permalink to this definition")
    :   A Float or a Complex specifying the load magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ShellEdgeLoadState.py)[¶](#abaqus.Load.ShellEdgeLoadState.ShellEdgeLoadState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load magnitude. Possible
        values are UNSET, SET, UNCHANGED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/ShellEdgeLoadState.py)[¶](#abaqus.Load.ShellEdgeLoadState.ShellEdgeLoadState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* SubmodelSBState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubmodelSBState.py#L9-L67)[¶](#abaqus.Load.SubmodelSBState.SubmodelSBState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The SubmodelSBState object stores the propagating data for a Submodel load in a step. One instance of
    this object is created internally by the SubmodelSB object for each step. The instance is also deleted
    internally by the SubmodelSB object. The SubmodelSBState object has no constructor or methods. The
    SubmodelSBState object is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * SUBMODEL
    * DSLOAD

    Note

    Check [SubmodelSBState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-submodelsbstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubmodelSBState.py#L9-L67)[¶](#abaqus.Load.SubmodelSBState.SubmodelSBState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubmodelSBState.py)[¶](#abaqus.Load.SubmodelSBState.SubmodelSBState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    globalIncrement : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubmodelSBState.py#L32-L35)[¶](#abaqus.Load.SubmodelSBState.SubmodelSBState.globalIncrement "Permalink to this definition")
    :   An Int specifying the increment number in the global model step at which the solution
        will be used to specify the values of the driven variables. This argument is applicable
        only for linear perturbation steps.

    globalIncrementState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubmodelSBState.py)[¶](#abaqus.Load.SubmodelSBState.SubmodelSBState.globalIncrementState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **globalIncrement** member.
        Possible values are SET and UNCHANGED.

    globalStep : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubmodelSBState.py#L41-L45)[¶](#abaqus.Load.SubmodelSBState.SubmodelSBState.globalStep "Permalink to this definition")
    :   A String specifying the step in the global model from which Abaqus reads the values of
        the variables that will drive the submodel analysis. The String indicates the position
        of the step in the sequence of analysis steps. For example, **globalStep** = ‘1’ indicates
        the first step.

    globalStepState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubmodelSBState.py)[¶](#abaqus.Load.SubmodelSBState.SubmodelSBState.globalStepState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **globalStep** member. Possible
        values are SET and UNCHANGED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubmodelSBState.py)[¶](#abaqus.Load.SubmodelSBState.SubmodelSBState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* SubstructureLoadState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubstructureLoadState.py#L9-L57)[¶](#abaqus.Load.SubstructureLoadState.SubstructureLoadState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The SubstructureLoadState object stores the propagating data for a substructure load in a step. One
    instance of this object is created internally by the SubstructureLoad object for each step. The instance is
    also deleted internally by the SubstructureLoad object. The SubstructureLoadState object has no constructor
    or methods. The SubstructureLoadState object is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * SLOAD

    Note

    Check [SubstructureLoadState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-substructureloadstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubstructureLoadState.py#L9-L57)[¶](#abaqus.Load.SubstructureLoadState.SubstructureLoadState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubstructureLoadState.py)[¶](#abaqus.Load.SubstructureLoadState.SubstructureLoadState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    loadCaseNames : --is-rst--:py:class:`tuple`\[:py:class:`str`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubstructureLoadState.py#L27-L28)[¶](#abaqus.Load.SubstructureLoadState.SubstructureLoadState.loadCaseNames "Permalink to this definition")
    :   A tuple of strings specifying the names of the load cases to be activated.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubstructureLoadState.py#L30-L31)[¶](#abaqus.Load.SubstructureLoadState.SubstructureLoadState.magnitude "Permalink to this definition")
    :   A Float or a Complex specifying the load magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubstructureLoadState.py)[¶](#abaqus.Load.SubstructureLoadState.SubstructureLoadState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load magnitude. Possible
        values are UNSET, SET, UNCHANGED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SubstructureLoadState.py)[¶](#abaqus.Load.SubstructureLoadState.SubstructureLoadState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* SurfaceChargeState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceChargeState.py#L9-L54)[¶](#abaqus.Load.SurfaceChargeState.SurfaceChargeState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The SurfaceChargeState object stores the propagating data of a surface charge in a step. One instance of
    this object is created internally by the SurfaceCharge object for each step. The instance is also deleted
    internally by the SurfaceCharge object. The SurfaceChargeState object has no constructor or methods. The
    SurfaceChargeState object is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * DSECHARGE

    Note

    Check [SurfaceChargeState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacechargestatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceChargeState.py#L9-L54)[¶](#abaqus.Load.SurfaceChargeState.SurfaceChargeState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceChargeState.py)[¶](#abaqus.Load.SurfaceChargeState.SurfaceChargeState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceChargeState.py#L27-L28)[¶](#abaqus.Load.SurfaceChargeState.SurfaceChargeState.magnitude "Permalink to this definition")
    :   A Float specifying the load magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceChargeState.py)[¶](#abaqus.Load.SurfaceChargeState.SurfaceChargeState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load magnitude. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceChargeState.py)[¶](#abaqus.Load.SurfaceChargeState.SurfaceChargeState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* SurfaceConcentrationFluxState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceConcentrationFluxState.py#L9-L55)[¶](#abaqus.Load.SurfaceConcentrationFluxState.SurfaceConcentrationFluxState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The SurfaceConcentrationFluxState object stores the propagating data for a SurfaceConcentrationFlux
    object in a step. One instance of this object is created internally by the SurfaceConcentrationFlux object
    for each step. The instance is also deleted internally by the SurfaceConcentrationFlux object. The
    SurfaceConcentrationFluxState object has no constructor or methods. The SurfaceConcentrationFluxState object
    is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * DSFLUX

    Note

    Check [SurfaceConcentrationFluxState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfaceconcentrationfluxstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceConcentrationFluxState.py#L9-L55)[¶](#abaqus.Load.SurfaceConcentrationFluxState.SurfaceConcentrationFluxState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceConcentrationFluxState.py)[¶](#abaqus.Load.SurfaceConcentrationFluxState.SurfaceConcentrationFluxState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceConcentrationFluxState.py#L28-L29)[¶](#abaqus.Load.SurfaceConcentrationFluxState.SurfaceConcentrationFluxState.magnitude "Permalink to this definition")
    :   A Float specifying the surface concentration flux magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceConcentrationFluxState.py)[¶](#abaqus.Load.SurfaceConcentrationFluxState.SurfaceConcentrationFluxState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the surface concentration flux
        magnitude. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceConcentrationFluxState.py)[¶](#abaqus.Load.SurfaceConcentrationFluxState.SurfaceConcentrationFluxState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* SurfaceCurrentState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCurrentState.py#L9-L54)[¶](#abaqus.Load.SurfaceCurrentState.SurfaceCurrentState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The SurfaceCurrentState object stores the propagating data of a surface current in a step. One instance
    of this object is created internally by the SurfaceCurrent object for each step. The instance is also
    deleted internally by the SurfaceCurrent object. The SurfaceCurrentState object has no constructor or
    methods. The SurfaceCurrentState object is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * DSECURRENT

    Note

    Check [SurfaceCurrentState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacecurrentstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCurrentState.py#L9-L54)[¶](#abaqus.Load.SurfaceCurrentState.SurfaceCurrentState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCurrentState.py)[¶](#abaqus.Load.SurfaceCurrentState.SurfaceCurrentState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCurrentState.py#L27-L28)[¶](#abaqus.Load.SurfaceCurrentState.SurfaceCurrentState.magnitude "Permalink to this definition")
    :   A Float specifying the load magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCurrentState.py)[¶](#abaqus.Load.SurfaceCurrentState.SurfaceCurrentState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load magnitude. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceCurrentState.py)[¶](#abaqus.Load.SurfaceCurrentState.SurfaceCurrentState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* SurfaceHeatFluxState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceHeatFluxState.py#L9-L54)[¶](#abaqus.Load.SurfaceHeatFluxState.SurfaceHeatFluxState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The SurfaceHeatFluxState object stores the propagating data for a surface SurfaceHeatFlux object in a
    step. One instance of this object is created internally by the SurfaceHeatFlux object for each step. The
    instance is also deleted internally by the SurfaceHeatFlux object. The SurfaceHeatFluxState object has no
    constructor or methods. The SurfaceHeatFluxState object is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * DSFLUX

    Note

    Check [SurfaceHeatFluxState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfaceheatfluxstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceHeatFluxState.py#L9-L54)[¶](#abaqus.Load.SurfaceHeatFluxState.SurfaceHeatFluxState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceHeatFluxState.py)[¶](#abaqus.Load.SurfaceHeatFluxState.SurfaceHeatFluxState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceHeatFluxState.py#L27-L28)[¶](#abaqus.Load.SurfaceHeatFluxState.SurfaceHeatFluxState.magnitude "Permalink to this definition")
    :   A Float specifying the surface heat flux magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceHeatFluxState.py)[¶](#abaqus.Load.SurfaceHeatFluxState.SurfaceHeatFluxState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the surface heat flux magnitude.
        Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceHeatFluxState.py)[¶](#abaqus.Load.SurfaceHeatFluxState.SurfaceHeatFluxState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* SurfacePoreFluidState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfacePoreFluidState.py#L9-L54)[¶](#abaqus.Load.SurfacePoreFluidState.SurfacePoreFluidState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The SurfacePoreFluidState object stores the propagating data for a SurfacePoreFluid object in a step. One
    instance of this object is created internally by the SurfacePoreFluid object for each step. The instance is
    also deleted internally by the SurfacePoreFluid object. The SurfacePoreFluidState object has no constructor
    or methods. The SurfacePoreFluidState object is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * DSFLOW

    Note

    Check [SurfacePoreFluidState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfaceporefluidstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfacePoreFluidState.py#L9-L54)[¶](#abaqus.Load.SurfacePoreFluidState.SurfacePoreFluidState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfacePoreFluidState.py)[¶](#abaqus.Load.SurfacePoreFluidState.SurfacePoreFluidState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfacePoreFluidState.py#L27-L28)[¶](#abaqus.Load.SurfacePoreFluidState.SurfacePoreFluidState.magnitude "Permalink to this definition")
    :   A Float specifying the surface pore fluid flow magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfacePoreFluidState.py)[¶](#abaqus.Load.SurfacePoreFluidState.SurfacePoreFluidState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the surface pore fluid flow
        magnitude. Possible values are UNSET, SET, UNCHANGED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfacePoreFluidState.py)[¶](#abaqus.Load.SurfacePoreFluidState.SurfacePoreFluidState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

*class* SurfaceTractionState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTractionState.py#L9-L55)[¶](#abaqus.Load.SurfaceTractionState.SurfaceTractionState "Permalink to this definition")
:   Bases: [`LoadState`](#abaqus.Load.SurfaceTractionState.LoadState "abaqus.Load.LoadState.LoadState (Python class)")

    The SurfaceTractionState object stores the propagating data for a SurfaceTraction object in a step. One
    instance of this object is created internally by the SurfaceTraction object for each step. The instance is
    also deleted internally by the SurfaceTraction object. The SurfaceTractionState object has no constructor or
    methods. The SurfaceTractionState object is derived from the LoadState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].loadStates[name]
    ```

    The corresponding analysis keywords are:

    * DSLOAD
    * DLOAD

    Note

    Check [SurfaceTractionState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-surfacetractionstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTractionState.py#L9-L55)[¶](#abaqus.Load.SurfaceTractionState.SurfaceTractionState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the load
        has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTractionState.py)[¶](#abaqus.Load.SurfaceTractionState.SurfaceTractionState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **amplitude** member. Possible
        values are UNSET, SET, UNCHANGED, and FREED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTractionState.py#L28-L29)[¶](#abaqus.Load.SurfaceTractionState.SurfaceTractionState.magnitude "Permalink to this definition")
    :   A Float or a Complex specifying the load magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTractionState.py)[¶](#abaqus.Load.SurfaceTractionState.SurfaceTractionState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the load magnitude. Possible
        values are UNSET, SET, UNCHANGED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Load/SurfaceTractionState.py)[¶](#abaqus.Load.SurfaceTractionState.SurfaceTractionState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the LoadState object. Possible
        values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * BUILT\_INTO\_BASE\_STATE

[Back to top](#)