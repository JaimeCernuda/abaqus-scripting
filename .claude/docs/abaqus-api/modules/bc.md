# Abaqus BC Module API Reference

> Source: [https://hailin.wang/abqpy/en/2025/reference/mdb/model/bc.html](https://hailin.wang/abqpy/en/2025/reference/mdb/model/bc.html)
> Downloaded for offline use by Claude Code skills.

---

# Boundary Condition[¶](#boundary-condition "Permalink to this heading")

A specific type of boundary condition object and a specific type of boundary condition state object are designed for each type of boundary condition. A BoundaryCondition object stores the non-propagating data of a boundary condition as well as a number of instances of the corresponding BoundaryConditionState object, each of which stores the propagating data of the boundary condition in a single step. Instances of the BoundaryConditionState object are created and deleted internally by its corresponding BoundaryCondition object.

## Create boundary conditions[¶](#create-boundary-conditions "Permalink to this heading")

*class* BoundaryConditionModel(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.__init__.name (Python parameter)")*, *[description](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.__init__.description (Python parameter)")=`''`*, *[stefanBoltzmann](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.__init__.stefanBoltzmann (Python parameter)")=`None`*, *[absoluteZero](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.__init__.absoluteZero (Python parameter)")=`None`*, *[waveFormulation](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.__init__.waveFormulation (Python parameter)")=`abaqusConstants.NOT_SET`*, *[modelType](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.__init__.modelType (Python parameter)")=`abaqusConstants.STANDARD_EXPLICIT`*, *[universalGas](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.__init__.universalGas (Python parameter)")=`None`*, *[copyConstraints](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.__init__.copyConstraints (Python parameter)")=`1`*, *[copyConnectors](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.__init__.copyConnectors (Python parameter)")=`1`*, *[copyInteractions](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.__init__.copyInteractions (Python parameter)")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L70-L2194)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel "Permalink to this definition")
:   Bases: [`ModelBase`](index.html#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase (Python class) — Bases: object")

    Abaqus creates a Model object named Model-1 when a session is started.

    Note

    This object can be accessed by:

    ```python
    mdb.models[name]
    ```

    Note

    Check [BoundaryConditionModel on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?contextscope=all).

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
    | [`AccelerationBaseMotionBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC (Python method) — This method creates a AccelerationBaseMotionBC object.")(name, ...[, ...]) | This method creates a AccelerationBaseMotionBC object. |
    | [`AccelerationBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC (Python method) — This method creates an AccelerationBC object.")(name, createStepName, region) | This method creates an AccelerationBC object. |
    | [`AcousticPressureBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC (Python method) — This method creates a AcousticPressureBC object.")(name, createStepName, region) | This method creates a AcousticPressureBC object. |
    | [`ConcentrationBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC (Python method) — This method creates a ConcentrationBC object.")(name, createStepName, region) | This method creates a ConcentrationBC object. |
    | [`ConnAccelerationBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC (Python method) — This method creates an ConnAccelerationBC object on a wire region. Alternatively, the boundary condition may also be applied to a wire set referenced from an assembled fastener template model.")(name, createStepName[, ...]) | This method creates an ConnAccelerationBC object on a wire region. |
    | [`ConnDisplacementBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC (Python method) — This method creates a ConnDisplacementBC object on a wire region. Alternatively, the boundary condition may also be applied to a wire set referenced from an assembled fastener template model.")(name, createStepName[, ...]) | This method creates a ConnDisplacementBC object on a wire region. |
    | [`ConnVelocityBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC (Python method) — This method creates a ConnVelocityBC object on a wire region. Alternatively, the boundary condition may also be applied to a wire set referenced from an assembled fastener template model.")(name, createStepName[, ...]) | This method creates a ConnVelocityBC object on a wire region. |
    | [`DisplacementBaseMotionBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC (Python method) — This method creates a DisplacementBaseMotionBC object.")(name, ...[, ...]) | This method creates a DisplacementBaseMotionBC object. |
    | [`DisplacementBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC (Python method) — This method creates a DisplacementBC object.")(name, createStepName, region) | This method creates a DisplacementBC object. |
    | [`ElectricPotentialBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC (Python method) — This method creates an ElectricPotentialBC object.")(name, createStepName, region) | This method creates an ElectricPotentialBC object. |
    | [`EulerianBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC (Python method) — This method creates a EulerianBC object.")(name, createStepName, region[, ...]) | This method creates a EulerianBC object. |
    | [`EulerianMotionBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC (Python method) — This method creates an EulerianMotionBC object.")(name, createStepName, ...) | This method creates an EulerianMotionBC object. |
    | [`FluidCavityPressureBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC (Python method) — This method creates a FluidCavityPressureBC object.")(name, createStepName, ...) | This method creates a FluidCavityPressureBC object. |
    | [`MagneticVectorPotentialBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC (Python method) — This method creates a MagneticVectorPotentialBC object.")(name, ...[, ...]) | This method creates a MagneticVectorPotentialBC object. |
    | [`MaterialFlowBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC (Python method) — This method creates a MaterialFlowBC object.")(name, createStepName, region) | This method creates a MaterialFlowBC object. |
    | [`PorePressureBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC (Python method) — This method creates a PorePressureBC object.")(name, createStepName, region) | This method creates a PorePressureBC object. |
    | [`RetainedNodalDofsBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC (Python method) — This method creates a RetainedNodalDofsBC object.")(name, createStepName, region) | This method creates a RetainedNodalDofsBC object. |
    | [`SecondaryBaseBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SecondaryBaseBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SecondaryBaseBC (Python method) — This method creates a SecondaryBaseBC object.")(name, createStepName, ...) | This method creates a SecondaryBaseBC object. |
    | [`SubmodelBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC (Python method) — This method creates a SubmodelBC object.")(name, createStepName, region, ...) | This method creates a SubmodelBC object. |
    | [`TemperatureBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC (Python method) — This method creates a TemperatureBC object.")(name, createStepName, region) | This method creates a TemperatureBC object. |
    | [`VelocityBaseMotionBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC (Python method) — This method creates a VelocityBaseMotionBC object.")(name, createStepName, dof) | This method creates a VelocityBaseMotionBC object. |
    | [`VelocityBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC (Python method) — This method creates a VelocityBC object.")(name, createStepName, region[, ...]) | This method creates a VelocityBC object. |
    | [`EncastreBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EncastreBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EncastreBC (Python method) — This method creates an encastre TypeBC object.")(name, createStepName, region[, ...]) | This method creates an encastre TypeBC object. |
    | [`PinnedBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PinnedBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PinnedBC (Python method) — This method creates a pinned TypeBC object.")(name, createStepName, region[, ...]) | This method creates a pinned TypeBC object. |
    | [`XsymmBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XsymmBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XsymmBC (Python method) — This method creates a TypeBC object that specifies symmetry about the X axis.")(name, createStepName, region[, ...]) | This method creates a TypeBC object that specifies symmetry about the **X** axis. |
    | [`YsymmBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YsymmBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YsymmBC (Python method) — This method creates a TypeBC object that specifies symmetry about the Y axis.")(name, createStepName, region[, ...]) | This method creates a TypeBC object that specifies symmetry about the **Y** axis. |
    | [`ZsymmBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZsymmBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZsymmBC (Python method) — This method creates a TypeBC object that specifies symmetry about the Z axis.")(name, createStepName, region[, ...]) | This method creates a TypeBC object that specifies symmetry about the **Z** axis. |
    | [`XasymmBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XasymmBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XasymmBC (Python method) — This method creates a TypeBC object that specifies antisymmetry about the X axis.")(name, createStepName, region[, ...]) | This method creates a TypeBC object that specifies antisymmetry about the **X** axis. |
    | [`YasymmBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YasymmBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YasymmBC (Python method) — This method creates a TypeBC object that specifies antisymmetry about the Y axis.")(name, createStepName, region[, ...]) | This method creates a TypeBC object that specifies antisymmetry about the **Y** axis. |
    | [`ZasymmBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZasymmBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZasymmBC (Python method) — This method creates a TypeBC object that specifies antisymmetry about the Z axis.")(name, createStepName, region[, ...]) | This method creates a TypeBC object that specifies antisymmetry about the **Z** axis. |

    Inherited from [`ModelBase`](index.html#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | `__init__`(name[, description, ...]) | This method creates a Model object. |
    | [`setValues`](index.html#abaqus.Model.ModelBase.ModelBase.setValues "abaqus.Model.ModelBase.ModelBase.setValues (Python method) — This method modifies the Model object.")([description, noPartsInputFile, ...]) | This method modifies the Model object. |

    ---

    Member Details:

    AccelerationBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[fieldName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.fieldName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.fieldName (Python parameter) — A String specifying the name of the AnalyticalField object associated with this boundary condition.")=`''`*, *[a1](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.a1 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.a1 (Python parameter) — A Float or a SymbolicConstant specifying the acceleration component in the 1-direction. Possible values for the SymbolicConstant are UNSET and SET.")=`abaqusConstants.UNSET`*, *[a2](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.a2 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.a2 (Python parameter) — A Float or a SymbolicConstant specifying the acceleration component in the 2-direction. Possible values for the SymbolicConstant are UNSET and SET.")=`abaqusConstants.UNSET`*, *[a3](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.a3 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.a3 (Python parameter) — A Float or a SymbolicConstant specifying the acceleration component in the 3-direction. Possible values for the SymbolicConstant are UNSET and SET.")=`abaqusConstants.UNSET`*, *[ar1](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.ar1 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.ar1 (Python parameter) — A Float or a SymbolicConstant specifying the rotational acceleration component about the 1-direction.")=`abaqusConstants.UNSET`*, *[ar2](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.ar2 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.ar2 (Python parameter) — A Float or a SymbolicConstant specifying the rotational acceleration component about the 2-direction.")=`abaqusConstants.UNSET`*, *[ar3](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.ar3 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.ar3 (Python parameter) — A Float or a SymbolicConstant specifying the rotational acceleration component about the 3-direction.")=`abaqusConstants.UNSET`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.amplitude "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[localCsys](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.localCsys "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*, *[distributionType](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.distributionType "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD.")=`abaqusConstants.UNIFORM`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L147-L240)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC "Permalink to this definition")
    :   This method creates an AccelerationBC object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].AccelerationBC
        ```

        Note

        Check [AccelerationBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-accelerationbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            fieldName=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.fieldName "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this boundary
                condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
                default value is an empty string.

            a1=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.a1 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the acceleration component in the 1-direction.
                Possible values for the SymbolicConstant are UNSET and SET. The default value is
                UNSET. Note: Although **a1**, **a2**, **a3**, **ar1**, **ar2**, and **ar3** are optional arguments, at
                least one of them must be specified.

            a2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.a2 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the acceleration component in the 2-direction.
                Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

            a3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.a3 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the acceleration component in the 3-direction.
                Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

            ar1=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.ar1 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational acceleration component about the
                1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET.

            ar2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.ar2 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational acceleration component about the
                2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET.

            ar3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.ar3 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational acceleration component about the
                3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC-returns "Permalink to this headline")
        :   **bc** – An AccelerationBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC-return-type "Permalink to this headline")
        :   [`AccelerationBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC (Python class) — Bases: BoundaryCondition")

    AccelerationBaseMotionBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[dof](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.dof "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.dof (Python parameter) — A SymbolicConstant specifying the constrained degree-of-freedom.")*, *[amplitudeScaleFactor](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.amplitudeScaleFactor "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.amplitudeScaleFactor (Python parameter) — A Float specifying the scale factor for the amplitude curve.")=`1`*, *[centerOfRotation](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.centerOfRotation "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.centerOfRotation (Python parameter) — A ModelDot object specifying a tuple containing one center of rotation.")=`()`*, *[correlation](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.correlation "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.correlation (Python parameter) — A Correlation object.")=`None`*, *[secondaryBase](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.secondaryBase "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.secondaryBase (Python parameter) — A String specifying the name of the SecondaryBaseBC object associated with this boundary condition.")=`''`*, *[useComplex](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.useComplex "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.useComplex (Python parameter) — A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base motion record given by amplitude definition.")=`0`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.amplitude "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L80-L145)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC "Permalink to this definition")
    :   This method creates a AccelerationBaseMotionBC object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].AccelerationBaseMotionBC
        ```

        Note

        Check [AccelerationBaseMotionBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-accelerationbasemotionbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            dof[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.dof "Permalink to this definition")
            :   A SymbolicConstant specifying the constrained degree-of-freedom. Possible values for the
                SymbolicConstant are U1, U2, U3, UR1, UR2, UR3. The default value is U1.

            amplitudeScaleFactor=`1`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.amplitudeScaleFactor "Permalink to this definition")
            :   A Float specifying the scale factor for the amplitude curve. The default value is 1.0.

            centerOfRotation=`()`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.centerOfRotation "Permalink to this definition")
            :   A ModelDot object specifying a tuple containing one center of rotation. The default
                value is the global origin. This argument applies only when **dof** = UR1, UR2, or UR3.

            correlation=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.correlation "Permalink to this definition")
            :   A Correlation object.

            secondaryBase=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.secondaryBase "Permalink to this definition")
            :   A String specifying the name of the SecondaryBaseBC object associated with this boundary
                condition. The default value is an empty string.

            useComplex=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.useComplex "Permalink to this definition")
            :   A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base
                motion record given by amplitude definition. The default value is OFF.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC-returns "Permalink to this headline")
        :   **bc** – An AccelerationBaseMotionBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC-return-type "Permalink to this headline")
        :   [`AccelerationBaseMotionBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC (Python class) — Bases: BoundaryCondition")

    AcousticPressureBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[fieldName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC.fieldName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC.fieldName (Python parameter) — A String specifying the name of the AnalyticalField object associated with this boundary condition.")=`''`*, *[magnitude](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC.magnitude "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC.magnitude (Python parameter) — A Float specifying the acoustic pressure magnitude.")=`0`*, *[distributionType](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC.distributionType "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD.")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC.amplitude "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[fixed](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC.fixed "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC.fixed (Python parameter) — A Boolean specifying whether the boundary condition should remain fixed at the current values at the start of the step.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L242-L304)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC "Permalink to this definition")
    :   This method creates a AcousticPressureBC object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].AcousticPressureBC
        ```

        Note

        Check [AcousticPressureBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acousticpressurebcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            fieldName=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC.fieldName "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this boundary
                condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
                default value is an empty string.

            magnitude=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC.magnitude "Permalink to this definition")
            :   A Float specifying the acoustic pressure magnitude. The default value is 0. The
                **magnitude** argument is optional if **distributionType** = USER\_DEFINED.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            fixed=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC.fixed "Permalink to this definition")
            :   A Boolean specifying whether the boundary condition should remain fixed at the current
                values at the start of the step. The default value is OFF.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC-returns "Permalink to this headline")
        :   **bc** – An AcousticPressureBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC-return-type "Permalink to this headline")
        :   [`AcousticPressureBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC "abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC (Python class) — Bases: BoundaryCondition")

    ConcentrationBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[fieldName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC.fieldName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC.fieldName (Python parameter) — A String specifying the name of the AnalyticalField object associated with this boundary condition.")=`''`*, *[magnitude](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC.magnitude "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC.magnitude (Python parameter) — A Float specifying the concentration magnitude.")=`0`*, *[distributionType](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC.distributionType "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD.")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC.amplitude "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[fixed](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC.fixed "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC.fixed (Python parameter) — A Boolean specifying whether the boundary condition should remain fixed at the current values at the start of the step.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L306-L368)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC "Permalink to this definition")
    :   This method creates a ConcentrationBC object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ConcentrationBC
        ```

        Note

        Check [ConcentrationBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concentrationbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            fieldName=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC.fieldName "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this boundary
                condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
                default value is an empty string.

            magnitude=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC.magnitude "Permalink to this definition")
            :   A Float specifying the concentration magnitude. The default value is 0. The **magnitude**
                argument is optional if **distributionType** = USER\_DEFINED.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            fixed=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC.fixed "Permalink to this definition")
            :   A Boolean specifying whether the boundary condition should remain fixed at the current
                values at the start of the step. The default value is OFF.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC-returns "Permalink to this headline")
        :   **bc** – A ConcentrationBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC-return-type "Permalink to this headline")
        :   [`ConcentrationBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC (Python method) — This method creates a ConcentrationBC object.")

    ConnAccelerationBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.region (Python parameter) — The wire region to which the boundary condition is applied.")=`''`*, *[fastenerName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.fastenerName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.fastenerName (Python parameter) — A String specifying the name of the assembled fastener to which the boundary condition will be applied.")=`''`*, *[fastenerSetName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.fastenerSetName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.fastenerSetName (Python parameter) — A String specifying the assembled fastener template model set to which the boundary condition will be applied.")=`''`*, *[a1](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.a1 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.a1 (Python parameter) — A Float or a SymbolicConstant specifying the acceleration component in the connector's local 1-direction.")=`abaqusConstants.UNSET`*, *[a2](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.a2 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.a2 (Python parameter) — A Float or a SymbolicConstant specifying the acceleration component in the connector's local 2-direction.")=`abaqusConstants.UNSET`*, *[a3](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.a3 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.a3 (Python parameter) — A Float or a SymbolicConstant specifying the acceleration component in the connector's local 3-direction.")=`abaqusConstants.UNSET`*, *[ar1](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.ar1 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.ar1 (Python parameter) — A Float or a SymbolicConstant specifying the rotational acceleration component in the connector's local 4-direction.")=`abaqusConstants.UNSET`*, *[ar2](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.ar2 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.ar2 (Python parameter) — A Float or a SymbolicConstant specifying the rotational acceleration component in the connector's local 5-direction.")=`abaqusConstants.UNSET`*, *[ar3](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.ar3 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.ar3 (Python parameter) — A Float or a SymbolicConstant specifying the rotational acceleration component in the connector's local 6-direction.")=`abaqusConstants.UNSET`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.amplitude "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.distributionType "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM and USER_DEFINED.")=`abaqusConstants.UNIFORM`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L370-L469)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC "Permalink to this definition")
    :   This method creates an ConnAccelerationBC object on a wire region. Alternatively, the boundary
        condition may also be applied to a wire set referenced from an assembled fastener template model.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ConnAccelerationBC
        ```

        Note

        Check [ConnAccelerationBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connaccelerationbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.region "Permalink to this definition")
            :   The wire region to which the boundary condition is applied. This argument is not valid
                when **fastenerName** and **fastenerSetName** are specified.

            fastenerName=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.fastenerName "Permalink to this definition")
            :   A String specifying the name of the assembled fastener to which the boundary condition
                will be applied. This argument is not valid when **region** is specified. When this
                argument is specified, **fastenerSetName** must also be specified. The default value is an
                empty string.

            fastenerSetName=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.fastenerSetName "Permalink to this definition")
            :   A String specifying the assembled fastener template model set to which the boundary
                condition will be applied. This argument is not valid when **region** is specified. When
                this argument is specified, **fastenerName** must also be specified. The default value is
                an empty string.

            a1=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.a1 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the acceleration component in the connector’s
                local 1-direction. Possible values for the SymbolicConstant are UNSET and SET. The
                default value is UNSET. Note: Although **a1**, **a2**, **a3**, **ar1**, **ar2**, and **ar3** are
                optional arguments, at least one of them must be specified.

            a2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.a2 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the acceleration component in the connector’s
                local 2-direction. Possible values for the SymbolicConstant are UNSET and SET. The
                default value is UNSET.

            a3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.a3 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the acceleration component in the connector’s
                local 3-direction. Possible values for the SymbolicConstant are UNSET and SET. The
                default value is UNSET.

            ar1=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.ar1 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational acceleration component in the
                connector’s local 4-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            ar2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.ar2 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational acceleration component in the
                connector’s local 5-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            ar3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.ar3 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational acceleration component in the
                connector’s local 6-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM and USER\_DEFINED. The default value is UNIFORM.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC-returns "Permalink to this headline")
        :   **bc** – A ConnAccelerationBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC-return-type "Permalink to this headline")
        :   [`ConnAccelerationBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC (Python method) — This method creates an ConnAccelerationBC object on a wire region. Alternatively, the boundary condition may also be applied to a wire set referenced from an assembled fastener template model.")

    ConnDisplacementBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.region (Python parameter) — The wire region to which the boundary condition is applied.")=`''`*, *[fastenerName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.fastenerName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.fastenerName (Python parameter) — A String specifying the name of the assembled fastener to which the boundary condition will be applied.")=`''`*, *[fastenerSetName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.fastenerSetName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.fastenerSetName (Python parameter) — A String specifying the assembled fastener template model set to which the boundary condition will be applied.")=`''`*, *[u1](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.u1 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.u1 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the displacement component in the connector's local 1-direction.")=`abaqusConstants.UNSET`*, *[u2](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.u2 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.u2 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the displacement component in the connector's local 2-direction.")=`abaqusConstants.UNSET`*, *[u3](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.u3 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.u3 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the displacement component in the connector's local 3-direction.")=`abaqusConstants.UNSET`*, *[ur1](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.ur1 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.ur1 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the rotational component in the connector's local 4-direction.")=`abaqusConstants.UNSET`*, *[ur2](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.ur2 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.ur2 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the rotational component in the connector's local 5-direction.")=`abaqusConstants.UNSET`*, *[ur3](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.ur3 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.ur3 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the rotational component in the connector's local 6-direction.")=`abaqusConstants.UNSET`*, *[fixed](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.fixed "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.fixed (Python parameter) — A Boolean specifying whether the boundary condition should remain fixed at the current values at the start of the step.")=`0`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.amplitude "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.distributionType "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM and USER_DEFINED.")=`abaqusConstants.UNIFORM`*, *[buckleCase](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.buckleCase "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.buckleCase (Python parameter) — A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE analysis.")=`abaqusConstants.NOT_APPLICABLE`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L471-L583)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC "Permalink to this definition")
    :   This method creates a ConnDisplacementBC object on a wire region. Alternatively, the boundary
        condition may also be applied to a wire set referenced from an assembled fastener template model.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ConnDisplacementBC
        ```

        Note

        Check [ConnDisplacementBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-conndisplacementbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.region "Permalink to this definition")
            :   The wire region to which the boundary condition is applied. This argument is not valid
                when **fastenerName** and **fastenerSetName** are specified.

            fastenerName=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.fastenerName "Permalink to this definition")
            :   A String specifying the name of the assembled fastener to which the boundary condition
                will be applied. This argument is not valid when **region** is specified. When this
                argument is specified, **fastenerSetName** must also be specified. The default value is an
                empty string.

            fastenerSetName=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.fastenerSetName "Permalink to this definition")
            :   A String specifying the assembled fastener template model set to which the boundary
                condition will be applied. This argument is not valid when **region** is specified. When
                this argument is specified, **fastenerName** must also be specified. The default value is
                an empty string.

            u1=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.u1 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
                connector’s local 1-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET. Note: Although **u1**, **u2**, **u3**, **ur1**, **ur2**, and **ur3**
                are optional arguments, at least one of them must be specified.

            u2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.u2 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
                connector’s local 2-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            u3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.u3 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
                connector’s local 3-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            ur1=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.ur1 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the rotational component in the
                connector’s local 4-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            ur2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.ur2 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the rotational component in the
                connector’s local 5-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            ur3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.ur3 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the rotational component in the
                connector’s local 6-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            fixed=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.fixed "Permalink to this definition")
            :   A Boolean specifying whether the boundary condition should remain fixed at the current
                values at the start of the step. The default value is OFF.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM and USER\_DEFINED. The default value is UNIFORM.

            buckleCase=`abaqusConstants.NOT_APPLICABLE`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC.buckleCase "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
                analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
                PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC-returns "Permalink to this headline")
        :   **bc** – A ConnDisplacementBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC-return-type "Permalink to this headline")
        :   [`ConnDisplacementBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC (Python method) — This method creates a ConnDisplacementBC object on a wire region. Alternatively, the boundary condition may also be applied to a wire set referenced from an assembled fastener template model.")

    ConnVelocityBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.region (Python parameter) — The wire region to which the boundary condition is applied.")=`''`*, *[fastenerName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.fastenerName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.fastenerName (Python parameter) — A String specifying the name of the assembled fastener to which the boundary condition will be applied.")=`''`*, *[fastenerSetName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.fastenerSetName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.fastenerSetName (Python parameter) — A String specifying the assembled fastener template model set to which the boundary condition will be applied.")=`''`*, *[v1](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.v1 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.v1 (Python parameter) — A Float or a SymbolicConstant specifying the velocity component in the connector's local 1-direction.")=`abaqusConstants.UNSET`*, *[v2](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.v2 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.v2 (Python parameter) — A Float or a SymbolicConstant specifying the velocity component in the connector's local 2-direction.")=`abaqusConstants.UNSET`*, *[v3](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.v3 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.v3 (Python parameter) — A Float or a SymbolicConstant specifying the velocity component in the connector's local 3-direction.")=`abaqusConstants.UNSET`*, *[vr1](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.vr1 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.vr1 (Python parameter) — A Float or a SymbolicConstant specifying the rotational velocity component in the connector's local 4-direction.")=`abaqusConstants.UNSET`*, *[vr2](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.vr2 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.vr2 (Python parameter) — A Float or a SymbolicConstant specifying the rotational velocity component in the connector's local 5-direction.")=`abaqusConstants.UNSET`*, *[vr3](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.vr3 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.vr3 (Python parameter) — A Float or a SymbolicConstant specifying the rotational velocity component in the connector's local 6-direction.")=`abaqusConstants.UNSET`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.amplitude "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.distributionType "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM and USER_DEFINED.")=`abaqusConstants.UNIFORM`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L585-L684)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC "Permalink to this definition")
    :   This method creates a ConnVelocityBC object on a wire region. Alternatively, the boundary condition
        may also be applied to a wire set referenced from an assembled fastener template model.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ConnVelocityBC
        ```

        Note

        Check [ConnVelocityBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connvelocitybcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.region "Permalink to this definition")
            :   The wire region to which the boundary condition is applied. This argument is not valid
                when **fastenerName** and **fastenerSetName** are specified.

            fastenerName=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.fastenerName "Permalink to this definition")
            :   A String specifying the name of the assembled fastener to which the boundary condition
                will be applied. This argument is not valid when **region** is specified. When this
                argument is specified, **fastenerSetName** must also be specified. The default value is an
                empty string.

            fastenerSetName=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.fastenerSetName "Permalink to this definition")
            :   A String specifying the assembled fastener template model set to which the boundary
                condition will be applied. This argument is not valid when **region** is specified. When
                this argument is specified, **fastenerName** must also be specified. The default value is
                an empty string.

            v1=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.v1 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the velocity component in the connector’s local
                1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET. Note: Although **v1**, **v2**, **v3**, **vr1**, **vr2**, and **vr3** are optional
                arguments, at least one of them must be specified.

            v2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.v2 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the velocity component in the connector’s local
                2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET.

            v3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.v3 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the velocity component in the connector’s local
                3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET.

            vr1=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.vr1 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational velocity component in the
                connector’s local 4-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            vr2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.vr2 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational velocity component in the
                connector’s local 5-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            vr3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.vr3 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational velocity component in the
                connector’s local 6-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM and USER\_DEFINED. The default value is UNIFORM.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC-returns "Permalink to this headline")
        :   **bc** – A ConnVelocityBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC-return-type "Permalink to this headline")
        :   [`ConnVelocityBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC (Python method) — This method creates a ConnVelocityBC object on a wire region. Alternatively, the boundary condition may also be applied to a wire set referenced from an assembled fastener template model.")

    DisplacementBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[fieldName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.fieldName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.fieldName (Python parameter) — A String specifying the name of the AnalyticalField or DiscreteField object associated with this boundary condition.")=`''`*, *[u1](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.u1 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.u1 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the displacement component in the 1-direction.")=`abaqusConstants.UNSET`*, *[u2](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.u2 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.u2 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the displacement component in the 2-direction.")=`abaqusConstants.UNSET`*, *[u3](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.u3 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.u3 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the displacement component in the 3-direction.")=`abaqusConstants.UNSET`*, *[ur1](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.ur1 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.ur1 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the rotational displacement component about the 1-direction.")=`abaqusConstants.UNSET`*, *[ur2](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.ur2 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.ur2 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the rotational displacement component about the 2-direction.")=`abaqusConstants.UNSET`*, *[ur3](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.ur3 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.ur3 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the rotational displacement component about the 3-direction.")=`abaqusConstants.UNSET`*, *[fixed](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.fixed "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.fixed (Python parameter) — A Boolean specifying whether the boundary condition should remain fixed at the current values at the start of the step.")=`0`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.amplitude "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.distributionType "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM, USER_DEFINED, FIELD, and DISCRETE_FIELD.")=`abaqusConstants.UNIFORM`*, *[localCsys](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.localCsys "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*, *[buckleCase](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.buckleCase "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.buckleCase (Python parameter) — A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE analysis.")=`abaqusConstants.NOT_APPLICABLE`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L753-L863)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC "Permalink to this definition")
    :   This method creates a DisplacementBC object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].DisplacementBC
        ```

        Note

        Check [DisplacementBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displacementbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            fieldName=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.fieldName "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField or DiscreteField object associated
                with this boundary condition. The **fieldName** argument applies only when
                **distributionType** = FIELD or **distributionType** = DISCRETE\_FIELD. The default value is an
                empty string.

            u1=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.u1 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
                1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET. Note: Although **u1**, **u2**, **u3**, **ur1**, **ur2**, and **ur3** are optional
                arguments, at least one of them must be specified.

            u2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.u2 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
                2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET.

            u3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.u3 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
                3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET.

            ur1=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.ur1 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the rotational displacement
                component about the 1-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            ur2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.ur2 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the rotational displacement
                component about the 2-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            ur3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.ur3 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the rotational displacement
                component about the 3-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            fixed=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.fixed "Permalink to this definition")
            :   A Boolean specifying whether the boundary condition should remain fixed at the current
                values at the start of the step. The default value is OFF.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM, USER\_DEFINED, FIELD, and DISCRETE\_FIELD. The default value
                is UNIFORM.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

            buckleCase=`abaqusConstants.NOT_APPLICABLE`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC.buckleCase "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
                analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
                PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC-returns "Permalink to this headline")
        :   **bc** – A DisplacementBC object

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC-return-type "Permalink to this headline")
        :   [`DisplacementBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC (Python method) — This method creates a DisplacementBC object.")

    DisplacementBaseMotionBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[dof](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.dof "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.dof (Python parameter) — A SymbolicConstant specifying the constrained degree-of-freedom.")*, *[amplitudeScaleFactor](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.amplitudeScaleFactor "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.amplitudeScaleFactor (Python parameter) — A Float specifying the scale factor for the amplitude curve.")=`1`*, *[centerOfRotation](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.centerOfRotation "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.centerOfRotation (Python parameter) — A ModelDot object specifying a tuple containing one center of rotation.")=`()`*, *[correlation](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.correlation "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.correlation (Python parameter) — A Correlation object.")=`None`*, *[secondaryBase](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.secondaryBase "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.secondaryBase (Python parameter) — A String specifying the name of the SecondaryBaseBC object associated with this boundary condition.")=`''`*, *[useComplex](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.useComplex "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.useComplex (Python parameter) — A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base motion record given by amplitude definition.")=`0`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.amplitude "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L686-L751)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC "Permalink to this definition")
    :   This method creates a DisplacementBaseMotionBC object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].DisplacementBaseMotionBC
        ```

        Note

        Check [DisplacementBaseMotionBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displacementbasemotionbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            dof[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.dof "Permalink to this definition")
            :   A SymbolicConstant specifying the constrained degree-of-freedom. Possible values for the
                SymbolicConstant are U1, U2, U3, UR1, UR2, UR3. The default value is U1.

            amplitudeScaleFactor=`1`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.amplitudeScaleFactor "Permalink to this definition")
            :   A Float specifying the scale factor for the amplitude curve. The default value is 1.0.

            centerOfRotation=`()`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.centerOfRotation "Permalink to this definition")
            :   A ModelDot object specifying a tuple containing one center of rotation. The default
                value is the global origin. This argument applies only when **dof** = UR1, UR2, or UR3.

            correlation=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.correlation "Permalink to this definition")
            :   A Correlation object.

            secondaryBase=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.secondaryBase "Permalink to this definition")
            :   A String specifying the name of the SecondaryBaseBC object associated with this boundary
                condition. The default value is an empty string.

            useComplex=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.useComplex "Permalink to this definition")
            :   A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base
                motion record given by amplitude definition. The default value is OFF.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC-returns "Permalink to this headline")
        :   **bc** – A DisplacementBaseMotionBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC-return-type "Permalink to this headline")
        :   [`DisplacementBaseMotionBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC (Python method) — This method creates a DisplacementBaseMotionBC object.")

    ElectricPotentialBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[fieldName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC.fieldName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC.fieldName (Python parameter) — A String specifying the name of the AnalyticalField object associated with this boundary condition.")=`''`*, *[magnitude](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC.magnitude "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC.magnitude (Python parameter) — A Float specifying the electrical potential magnitude.")=`0`*, *[distributionType](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC.distributionType "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD.")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC.amplitude "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[fixed](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC.fixed "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC.fixed (Python parameter) — A Boolean specifying whether the boundary condition should remain fixed at the current values at the start of the step.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L865-L927)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC "Permalink to this definition")
    :   This method creates an ElectricPotentialBC object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ElectricPotentialBC
        ```

        Note

        Check [ElectricPotentialBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-electricpotentialbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            fieldName=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC.fieldName "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this boundary
                condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
                default value is an empty string.

            magnitude=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC.magnitude "Permalink to this definition")
            :   A Float specifying the electrical potential magnitude. The default value is 0. The
                **magnitude** argument is optional if **distributionType** = USER\_DEFINED.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            fixed=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC.fixed "Permalink to this definition")
            :   A Boolean specifying whether the boundary condition should remain fixed at the current
                values at the start of the step. The default value is OFF.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC-returns "Permalink to this headline")
        :   **bc** – An ElectricPotentialBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC-return-type "Permalink to this headline")
        :   [`ElectricPotentialBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC (Python method) — This method creates an ElectricPotentialBC object.")

    EncastreBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EncastreBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EncastreBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EncastreBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EncastreBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EncastreBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EncastreBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[buckleCase](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EncastreBC.buckleCase "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EncastreBC.buckleCase (Python parameter) — A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE analysis.")=`abaqusConstants.NOT_APPLICABLE`*, *[localCsys](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EncastreBC.localCsys "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EncastreBC.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L1804-L1851)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EncastreBC "Permalink to this definition")
    :   This method creates an encastre TypeBC object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].EncastreBC
        ```

        Note

        Check [EncastreBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-encastrebcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EncastreBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EncastreBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EncastreBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EncastreBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            buckleCase=`abaqusConstants.NOT_APPLICABLE`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EncastreBC.buckleCase "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
                analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
                PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EncastreBC.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EncastreBC-returns "Permalink to this headline")
        :   A TypeBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EncastreBC-return-type "Permalink to this headline")
        :   `TypeBC`

    EulerianBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[definition](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC.definition "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC.definition (Python parameter) — A SymbolicConstant specifying the flow conditions to be defined.")=`abaqusConstants.INFLOW`*, *[inflowType](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC.inflowType "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC.inflowType (Python parameter) — A SymbolicConstant specifying the control of material flow into the Eulerian domain. Possible values are FREE, NONE, and VOID.")=`abaqusConstants.FREE`*, *[outflowType](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC.outflowType "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC.outflowType (Python parameter) — A SymbolicConstant specifying the control of flow of material out of the Eulerian domain.")=`abaqusConstants.ZERO_PRESSURE`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L929-L974)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC "Permalink to this definition")
    :   This method creates a EulerianBC object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].EulerianBC
        ```

        Note

        Check [EulerianBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-eulerianbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            definition=`abaqusConstants.INFLOW`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC.definition "Permalink to this definition")
            :   A SymbolicConstant specifying the flow conditions to be defined. Possible values are
                INFLOW, OUTFLOW, and BOTH. The default value is INFLOW.

            inflowType=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC.inflowType "Permalink to this definition")
            :   A SymbolicConstant specifying the control of material flow into the Eulerian domain.
                Possible values are FREE, NONE, and VOID. The default value is FREE.

            outflowType=`abaqusConstants.ZERO_PRESSURE`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC.outflowType "Permalink to this definition")
            :   A SymbolicConstant specifying the control of flow of material out of the Eulerian
                domain. Possible values are ZERO\_PRESSURE, FREE, NON\_REFLECTING, and EQUILIBRIUM. The
                default value is ZERO\_PRESSURE.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC-returns "Permalink to this headline")
        :   **bc** – An EulerianBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC-return-type "Permalink to this headline")
        :   [`EulerianBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC (Python method) — This method creates a EulerianBC object.")

    EulerianMotionBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[instanceName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.instanceName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.instanceName (Python parameter) — A String specifying the name of the Eulerian part instance.")*, *[followRegion](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.followRegion "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.followRegion (Python parameter) — A Boolean specifying whether the mesh will follow a regular surface region or an Eulerian surface.")=`1`*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")=`None`*, *[materialName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.materialName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.materialName (Python parameter) — A String specifying the name of the Eulerian surface to follow.")=`''`*, *[ctrPosition1](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.ctrPosition1 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.ctrPosition1 (Python parameter) — A SymbolicConstant specifying the 1-direction translational constraint on the center of the Eulerian mesh.")=`abaqusConstants.FREE`*, *[posPosition1](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.posPosition1 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.posPosition1 (Python parameter) — A SymbolicConstant specifying the translational constraint on the positive (maximum) bounds of the mesh in the 1 direction.")=`abaqusConstants.FREE`*, *[negPosition1](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.negPosition1 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.negPosition1 (Python parameter) — A SymbolicConstant specifying the translational constraint on the negative (minimum) bounds of the mesh in the 1 direction.")=`abaqusConstants.FREE`*, *[expansionRatio1](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.expansionRatio1 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.expansionRatio1 (Python parameter) — None or a Float specifying the upper bounds on the allowable scaling of the mesh in the 1 direction.")=`None`*, *[contractRatio1](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.contractRatio1 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.contractRatio1 (Python parameter) — A Float specifying the lower bounds on the allowable scaling of the mesh in the 1 direction.")=`0`*, *[ctrPosition2](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.ctrPosition2 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.ctrPosition2 (Python parameter) — A SymbolicConstant specifying the 2-direction translational constraint on the center of the Eulerian mesh.")=`abaqusConstants.FREE`*, *[posPosition2](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.posPosition2 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.posPosition2 (Python parameter) — A SymbolicConstant specifying the translational constraint on the positive (maximum) bounds of the mesh in the 2 direction.")=`abaqusConstants.FREE`*, *[negPosition2](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.negPosition2 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.negPosition2 (Python parameter) — A SymbolicConstant specifying the translational constraint on the negative (minimum) bounds of the mesh in the 2 direction.")=`abaqusConstants.FREE`*, *[expansionRatio2](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.expansionRatio2 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.expansionRatio2 (Python parameter) — None or a Float specifying the upper bounds on the allowable scaling of the mesh in the 2 direction.")=`None`*, *[contractRatio2](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.contractRatio2 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.contractRatio2 (Python parameter) — A Float specifying the lower bounds on the allowable scaling of the mesh in the 2 direction.")=`0`*, *[ctrPosition3](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.ctrPosition3 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.ctrPosition3 (Python parameter) — A SymbolicConstant specifying the 3-direction translational constraint on the center of the Eulerian mesh.")=`abaqusConstants.FREE`*, *[posPosition3](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.posPosition3 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.posPosition3 (Python parameter) — A SymbolicConstant specifying the translational constraint on the positive (maximum) bounds of the mesh in the 3 direction.")=`abaqusConstants.FREE`*, *[negPosition3](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.negPosition3 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.negPosition3 (Python parameter) — A SymbolicConstant specifying the translational constraint on the negative (minimum) bounds of the mesh in the 3 direction.")=`abaqusConstants.FREE`*, *[expansionRatio3](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.expansionRatio3 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.expansionRatio3 (Python parameter) — None or a Float specifying the upper bounds on the allowable scaling of the mesh in the 3 direction.")=`None`*, *[contractRatio3](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.contractRatio3 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.contractRatio3 (Python parameter) — A Float specifying the lower bounds on the allowable scaling of the mesh in the 3 direction.")=`0`*, *[allowContraction](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.allowContraction "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.allowContraction (Python parameter) — A Boolean specifying whether the mesh is allowed to contract .")=`1`*, *[aspectLimit](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.aspectLimit "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.aspectLimit (Python parameter) — A Float specifying the maximum change in allowed aspect ratio (for any of the three mesh aspects, 1-2, 2-3, 3-1).")=`10`*, *[vmaxFactor](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.vmaxFactor "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.vmaxFactor (Python parameter) — A Float specifying the multiplier for the mesh nodal velocity limit.")=`1`*, *[volThreshold](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.volThreshold "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.volThreshold (Python parameter) — A Float specifying the lower bounds on the volume fraction when determining which nodes to include in the surface bounding box calculation for an Eulerian material surface. This argument applies only when followRegion = False.")=`0`*, *[bufferSize](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.bufferSize "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.bufferSize (Python parameter) — None or a Float specifying the buffer between the surface box and the Eulerian section mesh bounding box.")=`2`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L976-L1133)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC "Permalink to this definition")
    :   This method creates an EulerianMotionBC object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].EulerianMotionBC
        ```

        Note

        Check [EulerianMotionBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-eulerianmotionbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            instanceName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.instanceName "Permalink to this definition")
            :   A String specifying the name of the Eulerian part instance.

            followRegion=`1`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.followRegion "Permalink to this definition")
            :   A Boolean specifying whether the mesh will follow a regular surface region or an
                Eulerian surface. The default value is ON.

            region=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            materialName=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.materialName "Permalink to this definition")
            :   A String specifying the name of the Eulerian surface to follow. This argument applies
                only when **followRegion** = False.

            ctrPosition1=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.ctrPosition1 "Permalink to this definition")
            :   A SymbolicConstant specifying the 1-direction translational constraint on the center of
                the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

            posPosition1=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.posPosition1 "Permalink to this definition")
            :   A SymbolicConstant specifying the translational constraint on the positive (maximum)
                bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default
                value is FREE.

            negPosition1=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.negPosition1 "Permalink to this definition")
            :   A SymbolicConstant specifying the translational constraint on the negative (minimum)
                bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default
                value is FREE.

            expansionRatio1=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.expansionRatio1 "Permalink to this definition")
            :   None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
                1 direction. If **expansionRatio1** = None, then there is no upper limit. The default value
                is None.

            contractRatio1=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.contractRatio1 "Permalink to this definition")
            :   A Float specifying the lower bounds on the allowable scaling of the mesh in the 1
                direction. The default value is 0.0.

            ctrPosition2=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.ctrPosition2 "Permalink to this definition")
            :   A SymbolicConstant specifying the 2-direction translational constraint on the center of
                the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

            posPosition2=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.posPosition2 "Permalink to this definition")
            :   A SymbolicConstant specifying the translational constraint on the positive (maximum)
                bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default
                value is FREE.

            negPosition2=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.negPosition2 "Permalink to this definition")
            :   A SymbolicConstant specifying the translational constraint on the negative (minimum)
                bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default
                value is FREE.

            expansionRatio2=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.expansionRatio2 "Permalink to this definition")
            :   None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
                2 direction. If **expansionRatio2** = None, then there is no upper limit. The default value
                is None.

            contractRatio2=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.contractRatio2 "Permalink to this definition")
            :   A Float specifying the lower bounds on the allowable scaling of the mesh in the 2
                direction. The default value is 0.0.

            ctrPosition3=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.ctrPosition3 "Permalink to this definition")
            :   A SymbolicConstant specifying the 3-direction translational constraint on the center of
                the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

            posPosition3=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.posPosition3 "Permalink to this definition")
            :   A SymbolicConstant specifying the translational constraint on the positive (maximum)
                bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default
                value is FREE.

            negPosition3=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.negPosition3 "Permalink to this definition")
            :   A SymbolicConstant specifying the translational constraint on the negative (minimum)
                bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default
                value is FREE.

            expansionRatio3=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.expansionRatio3 "Permalink to this definition")
            :   None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
                3 direction. If **expansionRatio3** = None, then there is no upper limit. The default value
                is None.

            contractRatio3=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.contractRatio3 "Permalink to this definition")
            :   A Float specifying the lower bounds on the allowable scaling of the mesh in the 3
                direction. The default value is 0.0.

            allowContraction=`1`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.allowContraction "Permalink to this definition")
            :   A Boolean specifying whether the mesh is allowed to contract . The default value is ON.

            aspectLimit=`10`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.aspectLimit "Permalink to this definition")
            :   A Float specifying the maximum change in allowed aspect ratio (for any of the three mesh
                aspects, 1-2, 2-3, 3-1). The default value is 10.0.

            vmaxFactor=`1`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.vmaxFactor "Permalink to this definition")
            :   A Float specifying the multiplier for the mesh nodal velocity limit. The default value
                is 1.01.

            volThreshold=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.volThreshold "Permalink to this definition")
            :   A Float specifying the lower bounds on the volume fraction when determining which nodes
                to include in the surface bounding box calculation for an Eulerian material surface.
                This argument applies only when **followRegion** = False. The default value is 0.5.

            bufferSize=`2`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC.bufferSize "Permalink to this definition")
            :   None or a Float specifying the buffer between the surface box and the Eulerian section
                mesh bounding box. The default value is 2.0.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC-returns "Permalink to this headline")
        :   **bc** – An EulerianMotionBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC-return-type "Permalink to this headline")
        :   [`EulerianMotionBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC (Python method) — This method creates an EulerianMotionBC object.")

    FluidCavityPressureBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[fluidCavity](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC.fluidCavity "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC.fluidCavity (Python parameter) — A String specifying the name of a Fluid Cavity Interaction.")*, *[magnitude](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC.magnitude "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC.magnitude (Python parameter) — A Float specifying the fluid cavity pressure magnitude.")=`0`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC.amplitude "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[fixed](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC.fixed "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC.fixed (Python parameter) — A Boolean specifying whether the boundary condition should remain fixed at the current values at the start of the step.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L1135-L1180)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC "Permalink to this definition")
    :   This method creates a FluidCavityPressureBC object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].FluidCavityPressureBC
        ```

        Note

        Check [FluidCavityPressureBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidcavitypressurebcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            fluidCavity[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC.fluidCavity "Permalink to this definition")
            :   A String specifying the name of a Fluid Cavity Interaction.

            magnitude=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC.magnitude "Permalink to this definition")
            :   A Float specifying the fluid cavity pressure magnitude. The default value is 0.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            fixed=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC.fixed "Permalink to this definition")
            :   A Boolean specifying whether the boundary condition should remain fixed at the current
                values at the start of the step. The default value is OFF.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC-returns "Permalink to this headline")
        :   **bc** – A FluidCavityPressureBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC-return-type "Permalink to this headline")
        :   [`FluidCavityPressureBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC (Python method) — This method creates a FluidCavityPressureBC object.")

    MagneticVectorPotentialBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[component1](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.component1 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.component1 (Python parameter) — A Complex, or a SymbolicConstant specifying the magnetic vector potential component in the 1-direction.")=`None`*, *[component2](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.component2 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.component2 (Python parameter) — A Complex, or a SymbolicConstant specifying the magnetic vector potential component in the 2-direction.")=`abaqusConstants.UNSET`*, *[component3](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.component3 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.component3 (Python parameter) — A Complex, or a SymbolicConstant specifying the magnetic vector potential component in the 3-direction.")=`abaqusConstants.UNSET`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.amplitude "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.distributionType "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM and USER_DEFINED.")=`abaqusConstants.UNIFORM`*, *[localCsys](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.localCsys "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L1182-L1251)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC "Permalink to this definition")
    :   This method creates a MagneticVectorPotentialBC object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].MagneticVectorPotentialBC
        ```

        Note

        Check [MagneticVectorPotentialBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-magneticvectorpotentialbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            component1=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.component1 "Permalink to this definition")
            :   A Complex, or a SymbolicConstant specifying the magnetic vector potential component in
                the 1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET

            component2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.component2 "Permalink to this definition")
            :   A Complex, or a SymbolicConstant specifying the magnetic vector potential component in
                the 2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET.

            component3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.component3 "Permalink to this definition")
            :   A Complex, or a SymbolicConstant specifying the magnetic vector potential component in
                the 3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM and USER\_DEFINED. The default value is UNIFORM.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC-returns "Permalink to this headline")
        :   **bc** – A MagneticVectorPotentialBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC-return-type "Permalink to this headline")
        :   [`MagneticVectorPotentialBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC (Python method) — This method creates a MagneticVectorPotentialBC object.")

    MaterialFlowBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[fieldName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC.fieldName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC.fieldName (Python parameter) — A String specifying the name of the AnalyticalField object associated with this boundary condition.")=`''`*, *[magnitude](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC.magnitude "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC.magnitude (Python parameter) — A Float specifying the material flow magnitude.")=`0`*, *[distributionType](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC.distributionType "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD.")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC.amplitude "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[fixed](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC.fixed "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC.fixed (Python parameter) — A Boolean specifying whether the boundary condition should remain fixed at the current values at the start of the step.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L1253-L1315)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC "Permalink to this definition")
    :   This method creates a MaterialFlowBC object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].MaterialFlowBC
        ```

        Note

        Check [MaterialFlowBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-materialflowbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            fieldName=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC.fieldName "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this boundary
                condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
                default value is an empty string.

            magnitude=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC.magnitude "Permalink to this definition")
            :   A Float specifying the material flow magnitude. The default value is 0. The **magnitude**
                argument is optional if **distributionType** = USER\_DEFINED.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            fixed=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC.fixed "Permalink to this definition")
            :   A Boolean specifying whether the boundary condition should remain fixed at the current
                values at the start of the step. The default value is OFF.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC-returns "Permalink to this headline")
        :   **bc** – A MaterialFlowBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC-return-type "Permalink to this headline")
        :   [`MaterialFlowBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC (Python method) — This method creates a MaterialFlowBC object.")

    PinnedBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PinnedBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PinnedBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PinnedBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PinnedBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PinnedBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PinnedBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[buckleCase](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PinnedBC.buckleCase "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PinnedBC.buckleCase (Python parameter) — A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE analysis.")=`abaqusConstants.NOT_APPLICABLE`*, *[localCsys](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PinnedBC.localCsys "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PinnedBC.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L1853-L1900)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PinnedBC "Permalink to this definition")
    :   This method creates a pinned TypeBC object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].PinnedBC
        ```

        Note

        Check [PinnedBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pinnedbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PinnedBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PinnedBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PinnedBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PinnedBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            buckleCase=`abaqusConstants.NOT_APPLICABLE`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PinnedBC.buckleCase "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
                analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
                PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PinnedBC.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PinnedBC-returns "Permalink to this headline")
        :   A TypeBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PinnedBC-return-type "Permalink to this headline")
        :   `TypeBC`

    PorePressureBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[fieldName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC.fieldName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC.fieldName (Python parameter) — A String specifying the name of the AnalyticalField object associated with this boundary condition.")=`''`*, *[magnitude](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC.magnitude "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC.magnitude (Python parameter) — A Float specifying the pore pressure magnitude.")=`0`*, *[distributionType](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC.distributionType "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD.")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC.amplitude "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[fixed](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC.fixed "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC.fixed (Python parameter) — A Boolean specifying whether the boundary condition should remain fixed at the current values at the start of the step.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L1317-L1379)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC "Permalink to this definition")
    :   This method creates a PorePressureBC object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].PorePressureBC
        ```

        Note

        Check [PorePressureBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-porepressurebcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            fieldName=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC.fieldName "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this boundary
                condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
                default value is an empty string.

            magnitude=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC.magnitude "Permalink to this definition")
            :   A Float specifying the pore pressure magnitude. The default value is 0. The **magnitude**
                argument is optional if **distributionType** = USER\_DEFINED.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            fixed=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC.fixed "Permalink to this definition")
            :   A Boolean specifying whether the boundary condition should remain fixed at the current
                values at the start of the step. The default value is OFF.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC-returns "Permalink to this headline")
        :   **bc** – A PorePressureBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC-return-type "Permalink to this headline")
        :   [`PorePressureBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC (Python method) — This method creates a PorePressureBC object.")

    RetainedNodalDofsBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[u1](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.u1 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.u1 (Python parameter) — A Boolean specifying whether to retain the degree of freedom in the 1-direction.")=`0`*, *[u2](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.u2 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.u2 (Python parameter) — A Boolean specifying whether to retain the degree of freedom in the 2-direction.")=`0`*, *[u3](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.u3 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.u3 (Python parameter) — A Boolean specifying whether to retain the degree of freedom in the 3-direction.")=`0`*, *[ur1](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.ur1 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.ur1 (Python parameter) — A Boolean specifying whether to retain the rotational degree of freedom about the 1-direction.")=`0`*, *[ur2](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.ur2 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.ur2 (Python parameter) — A Boolean specifying whether to retain the rotational degree of freedom about the 2-direction.")=`0`*, *[ur3](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.ur3 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.ur3 (Python parameter) — A Boolean specifying whether to retain the rotational degree of freedom about the 3-direction.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L1381-L1439)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC "Permalink to this definition")
    :   This method creates a RetainedNodalDofsBC object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].RetainedNodalDofsBC
        ```

        Note

        Check [RetainedNodalDofsBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-retainednodaldofsbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            u1=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.u1 "Permalink to this definition")
            :   A Boolean specifying whether to retain the degree of freedom in the 1-direction. The
                default value is OFF indicating that the degree of freedom is not retained.

            u2=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.u2 "Permalink to this definition")
            :   A Boolean specifying whether to retain the degree of freedom in the 2-direction. The
                default value is OFF indicating that the degree of freedom is not retained.

            u3=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.u3 "Permalink to this definition")
            :   A Boolean specifying whether to retain the degree of freedom in the 3-direction. The
                default value is OFF indicating that the degree of freedom is not retained.

            ur1=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.ur1 "Permalink to this definition")
            :   A Boolean specifying whether to retain the rotational degree of freedom about the
                1-direction. The default value is OFF indicating that the degree of freedom is not
                retained.

            ur2=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.ur2 "Permalink to this definition")
            :   A Boolean specifying whether to retain the rotational degree of freedom about the
                2-direction. The default value is OFF indicating that the degree of freedom is not
                retained.

            ur3=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC.ur3 "Permalink to this definition")
            :   A Boolean specifying whether to retain the rotational degree of freedom about the
                3-direction. The default value is OFF indicating that the degree of freedom is not
                retained.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC-returns "Permalink to this headline")
        :   **bc** – A RetainedNodalDofsBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC-return-type "Permalink to this headline")
        :   [`RetainedNodalDofsBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC (Python method) — This method creates a RetainedNodalDofsBC object.")

    SecondaryBaseBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SecondaryBaseBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SecondaryBaseBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SecondaryBaseBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SecondaryBaseBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[regions](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SecondaryBaseBC.regions "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SecondaryBaseBC.regions (Python parameter) — A RegionArray object specifying the region to which the boundary condition is applied. Note that the usual region is ignored.")*, *[dofs](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SecondaryBaseBC.dofs "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SecondaryBaseBC.dofs (Python parameter) — A sequence of sequences of Ints specifying the constrained degrees-of-freedom.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L1441-L1469)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SecondaryBaseBC "Permalink to this definition")
    :   This method creates a SecondaryBaseBC object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].SecondaryBaseBC
        ```

        Note

        Check [SecondaryBaseBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-secondarybasebcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SecondaryBaseBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SecondaryBaseBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SecondaryBaseBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            regions[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SecondaryBaseBC.regions "Permalink to this definition")
            :   A RegionArray object specifying the region to which the boundary condition is applied.
                Note that the usual **region** is ignored. The default value is MODEL.

            dofs[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SecondaryBaseBC.dofs "Permalink to this definition")
            :   A sequence of sequences of Ints specifying the constrained degrees-of-freedom.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SecondaryBaseBC-returns "Permalink to this headline")
        :   **bc** – A SecondaryBaseBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SecondaryBaseBC-return-type "Permalink to this headline")
        :   [`SecondaryBaseBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SecondaryBaseBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SecondaryBaseBC (Python method) — This method creates a SecondaryBaseBC object.")

    SubmodelBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[dof](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.dof "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.dof (Python parameter) — A sequence of Ints specifying the degrees of freedom to which the boundary condition is applied.")*, *[globalStep](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.globalStep "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.globalStep (Python parameter) — A String specifying the step in the global model from which Abaqus reads the values of the variables that will drive the submodel analysis.")*, *[timeScale](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.timeScale "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.timeScale (Python parameter) — A Boolean specifying whether to scale the time variable for the driven nodes' amplitude functions to match the submodel analysis step time.")*, *[shellThickness](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.shellThickness "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.shellThickness (Python parameter) — A Float specifying the thickness of the shell in the global model.")*, *[globalDrivingRegion](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.globalDrivingRegion "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.globalDrivingRegion (Python parameter) — A String specifying the element set in the global model that will be searched for elements whose responses will be used to drive the submodel.")=`''`*, *[absoluteExteriorTolerance](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.absoluteExteriorTolerance "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.absoluteExteriorTolerance (Python parameter) — None or a Float specifying the absolute value by which a driven node of the submodel can lie outside the region of the elements of the global model.")=`None`*, *[exteriorTolerance](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.exteriorTolerance "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.exteriorTolerance (Python parameter) — None or a Float specifying the fraction of the average element size in the global model by which a driven node of the submodel can lie outside the region of the elements of the global model.")=`0`*, *[localCsys](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.localCsys "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*, *[globalIncrement](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.globalIncrement "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.globalIncrement (Python parameter) — An Int specifying the increment number in the global model step from which the solution will be used to specify the values of the driven variables.")=`0`*, *[centerZoneSize](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.centerZoneSize "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.centerZoneSize (Python parameter) — A Float specifying the thickness of the center zone size around the shell midsurface. The default value is None.")=`None`*, *[intersectionOnly](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.intersectionOnly "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.intersectionOnly (Python parameter) — A Boolean specifying whether to ignore driven nodes that lie outside the region of elements of the global model after accounting for the exterior search tolerance.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L1471-L1572)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC "Permalink to this definition")
    :   This method creates a SubmodelBC object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].SubmodelBC
        ```

        Note

        Check [SubmodelBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-submodelbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            dof[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.dof "Permalink to this definition")
            :   A sequence of Ints specifying the degrees of freedom to which the boundary condition is
                applied.

            globalStep[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.globalStep "Permalink to this definition")
            :   A String specifying the step in the global model from which Abaqus reads the values of
                the variables that will drive the submodel analysis. The String indicates the position
                of the step in the sequence of analysis steps. For example, **globalStep** = ‘1’ indicates
                the first step.

            timeScale[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.timeScale "Permalink to this definition")
            :   A Boolean specifying whether to scale the time variable for the driven nodes’ amplitude
                functions to match the submodel analysis step time. The default value is OFF.

            shellThickness[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.shellThickness "Permalink to this definition")
            :   A Float specifying the thickness of the shell in the global model. This argument is
                required for shell-to-solid submodeling and is not applicable to other submodels. The
                default value is 0.0.

            globalDrivingRegion=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.globalDrivingRegion "Permalink to this definition")
            :   A String specifying the element set in the global model that will be searched for
                elements whose responses will be used to drive the submodel. An empty string indicates
                that the entire global model will be searched. The default value is an empty string.

            absoluteExteriorTolerance=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.absoluteExteriorTolerance "Permalink to this definition")
            :   None or a Float specifying the absolute value by which a driven node of the submodel can
                lie outside the region of the elements of the global model. The default value is None.

            exteriorTolerance=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.exteriorTolerance "Permalink to this definition")
            :   None or a Float specifying the fraction of the average element size in the global model
                by which a driven node of the submodel can lie outside the region of the elements of the
                global model. The default value is 0.05.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

            globalIncrement=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.globalIncrement "Permalink to this definition")
            :   An Int specifying the increment number in the global model step from which the solution
                will be used to specify the values of the driven variables. If **globalIncrement** = 0, the
                solution from the last increment will be used. The **globalIncrement** argument is
                applicable only for linear perturbation steps. The default value is 0.

            centerZoneSize=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.centerZoneSize "Permalink to this definition")
            :   A Float specifying the thickness of the center zone size around the shell midsurface.
                The default value is None.

            intersectionOnly=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC.intersectionOnly "Permalink to this definition")
            :   A Boolean specifying whether to ignore driven nodes that lie outside the region of
                elements of the global model after accounting for the exterior search tolerance. The
                default value is OFF.

                New in version 2021: The `intersectionOnly` argument was added.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC-returns "Permalink to this headline")
        :   **bc** – A SubmodelBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC-return-type "Permalink to this headline")
        :   [`SubmodelBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC (Python method) — This method creates a SubmodelBC object.")

    TemperatureBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[fieldName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.fieldName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.fieldName (Python parameter) — A String specifying the name of the AnalyticalField object associated with this boundary condition.")=`''`*, *[magnitude](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.magnitude "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.magnitude (Python parameter) — A Float specifying the temperature magnitude.")=`0`*, *[dof](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.dof "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.dof (Python parameter) — A sequence of Ints specifying the degrees of freedom to which the boundary condition is applied.")=`()`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.amplitude "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.distributionType "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD.")=`abaqusConstants.UNIFORM`*, *[fixed](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.fixed "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.fixed (Python parameter) — A Boolean specifying whether the boundary condition should remain fixed at the current values at the start of the step.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L1574-L1640)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC "Permalink to this definition")
    :   This method creates a TemperatureBC object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].TemperatureBC
        ```

        Note

        Check [TemperatureBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-temperaturebcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            fieldName=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.fieldName "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this boundary
                condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
                default value is an empty string.

            magnitude=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.magnitude "Permalink to this definition")
            :   A Float specifying the temperature magnitude. The default value is 0.

            dof=`()`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.dof "Permalink to this definition")
            :   A sequence of Ints specifying the degrees of freedom to which the boundary condition is
                applied. The default value is (11,).

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            fixed=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC.fixed "Permalink to this definition")
            :   A Boolean specifying whether the boundary condition should remain fixed at the current
                values at the start of the step. The default value is OFF.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC-returns "Permalink to this headline")
        :   **bc** – A TemperatureBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC-return-type "Permalink to this headline")
        :   [`TemperatureBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC (Python method) — This method creates a TemperatureBC object.")

    VelocityBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[fieldName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.fieldName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.fieldName (Python parameter) — A String specifying the name of the AnalyticalField object associated with this boundary condition.")=`''`*, *[v1](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.v1 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.v1 (Python parameter) — A Float or a SymbolicConstant specifying the velocity component in the 1-direction. Possible values for the SymbolicConstant are UNSET and SET.")=`abaqusConstants.UNSET`*, *[v2](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.v2 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.v2 (Python parameter) — A Float or a SymbolicConstant specifying the velocity component in the 2-direction. Possible values for the SymbolicConstant are UNSET and SET.")=`abaqusConstants.UNSET`*, *[v3](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.v3 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.v3 (Python parameter) — A Float or a SymbolicConstant specifying the velocity component in the 3-direction. Possible values for the SymbolicConstant are UNSET and SET.")=`abaqusConstants.UNSET`*, *[vr1](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.vr1 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.vr1 (Python parameter) — A Float or a SymbolicConstant specifying the rotational velocity component about the 1-direction.")=`abaqusConstants.UNSET`*, *[vr2](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.vr2 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.vr2 (Python parameter) — A Float or a SymbolicConstant specifying the rotational velocity component about the 2-direction.")=`abaqusConstants.UNSET`*, *[vr3](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.vr3 "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.vr3 (Python parameter) — A Float or a SymbolicConstant specifying the rotational velocity component about the 3-direction.")=`abaqusConstants.UNSET`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.amplitude "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[localCsys](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.localCsys "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*, *[distributionType](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.distributionType "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD.")=`abaqusConstants.UNIFORM`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L1709-L1802)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC "Permalink to this definition")
    :   This method creates a VelocityBC object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].VelocityBC
        ```

        Note

        Check [VelocityBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-velocitybcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            fieldName=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.fieldName "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this boundary
                condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
                default value is an empty string.

            v1=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.v1 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the velocity component in the 1-direction.
                Possible values for the SymbolicConstant are UNSET and SET. The default value is
                UNSET. Note: Although **v1**, **v2**, **v3**, **vr1**, **vr2**, and **vr3** are optional arguments, at
                least one of them must be specified.

            v2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.v2 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the velocity component in the 2-direction.
                Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

            v3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.v3 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the velocity component in the 3-direction.
                Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

            vr1=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.vr1 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational velocity component about the
                1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET.

            vr2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.vr2 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational velocity component about the
                2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET.

            vr3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.vr3 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational velocity component about the
                3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC-returns "Permalink to this headline")
        :   **bc** – A VelocityBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC-return-type "Permalink to this headline")
        :   [`VelocityBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC (Python method) — This method creates a VelocityBC object.")

    VelocityBaseMotionBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[dof](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.dof "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.dof (Python parameter) — A SymbolicConstant specifying the constrained degree-of-freedom.")*, *[amplitudeScaleFactor](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.amplitudeScaleFactor "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.amplitudeScaleFactor (Python parameter) — A Float specifying the scale factor for the amplitude curve.")=`1`*, *[centerOfRotation](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.centerOfRotation "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.centerOfRotation (Python parameter) — A ModelDot object specifying a tuple containing one center of rotation.")=`()`*, *[correlation](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.correlation "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.correlation (Python parameter) — A Correlation object.")=`None`*, *[secondaryBase](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.secondaryBase "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.secondaryBase (Python parameter) — A String specifying the name of the SecondaryBaseBC object associated with this boundary condition.")=`''`*, *[useComplex](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.useComplex "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.useComplex (Python parameter) — A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base motion record given by amplitude definition.")=`0`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.amplitude "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L1642-L1707)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC "Permalink to this definition")
    :   This method creates a VelocityBaseMotionBC object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].VelocityBaseMotionBC
        ```

        Note

        Check [VelocityBaseMotionBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-velocitybasemotionbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            dof[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.dof "Permalink to this definition")
            :   A SymbolicConstant specifying the constrained degree-of-freedom. Possible values for the
                SymbolicConstant are U1, U2, U3, UR1, UR2, UR3. The default value is U1.

            amplitudeScaleFactor=`1`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.amplitudeScaleFactor "Permalink to this definition")
            :   A Float specifying the scale factor for the amplitude curve. The default value is 1.0.

            centerOfRotation=`()`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.centerOfRotation "Permalink to this definition")
            :   A ModelDot object specifying a tuple containing one center of rotation. The default
                value is the global origin. This argument applies only when **dof** = UR1, UR2, or UR3.

            correlation=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.correlation "Permalink to this definition")
            :   A Correlation object.

            secondaryBase=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.secondaryBase "Permalink to this definition")
            :   A String specifying the name of the SecondaryBaseBC object associated with this boundary
                condition. The default value is an empty string.

            useComplex=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.useComplex "Permalink to this definition")
            :   A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base
                motion record given by amplitude definition. The default value is OFF.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC-returns "Permalink to this headline")
        :   **bc** – A VelocityBaseMotionBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC-return-type "Permalink to this headline")
        :   [`VelocityBaseMotionBC`](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC (Python method) — This method creates a VelocityBaseMotionBC object.")

    XasymmBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XasymmBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XasymmBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XasymmBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XasymmBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XasymmBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XasymmBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[buckleCase](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XasymmBC.buckleCase "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XasymmBC.buckleCase (Python parameter) — A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE analysis.")=`abaqusConstants.NOT_APPLICABLE`*, *[localCsys](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XasymmBC.localCsys "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XasymmBC.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L2049-L2096)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XasymmBC "Permalink to this definition")
    :   This method creates a TypeBC object that specifies antisymmetry about the **X** axis.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].XasymmBC
        ```

        Note

        Check [XasymmBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xasymmbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XasymmBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XasymmBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XasymmBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XasymmBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            buckleCase=`abaqusConstants.NOT_APPLICABLE`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XasymmBC.buckleCase "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
                analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
                PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XasymmBC.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XasymmBC-returns "Permalink to this headline")
        :   A TypeBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XasymmBC-return-type "Permalink to this headline")
        :   `TypeBC`

    XsymmBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XsymmBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XsymmBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XsymmBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XsymmBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XsymmBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XsymmBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[buckleCase](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XsymmBC.buckleCase "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XsymmBC.buckleCase (Python parameter) — A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE analysis.")=`abaqusConstants.NOT_APPLICABLE`*, *[localCsys](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XsymmBC.localCsys "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XsymmBC.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L1902-L1949)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XsymmBC "Permalink to this definition")
    :   This method creates a TypeBC object that specifies symmetry about the **X** axis.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].XsymmBC
        ```

        Note

        Check [XsymmBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xsymmbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XsymmBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XsymmBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XsymmBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XsymmBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            buckleCase=`abaqusConstants.NOT_APPLICABLE`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XsymmBC.buckleCase "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
                analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
                PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XsymmBC.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XsymmBC-returns "Permalink to this headline")
        :   A TypeBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XsymmBC-return-type "Permalink to this headline")
        :   `TypeBC`

    YasymmBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YasymmBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YasymmBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YasymmBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YasymmBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YasymmBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YasymmBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[buckleCase](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YasymmBC.buckleCase "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YasymmBC.buckleCase (Python parameter) — A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE analysis.")=`abaqusConstants.NOT_APPLICABLE`*, *[localCsys](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YasymmBC.localCsys "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YasymmBC.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L2098-L2145)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YasymmBC "Permalink to this definition")
    :   This method creates a TypeBC object that specifies antisymmetry about the **Y** axis.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].YasymmBC
        ```

        Note

        Check [YasymmBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-yasymmbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YasymmBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YasymmBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YasymmBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YasymmBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            buckleCase=`abaqusConstants.NOT_APPLICABLE`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YasymmBC.buckleCase "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
                analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
                PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YasymmBC.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YasymmBC-returns "Permalink to this headline")
        :   A TypeBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YasymmBC-return-type "Permalink to this headline")
        :   `TypeBC`

    YsymmBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YsymmBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YsymmBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YsymmBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YsymmBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YsymmBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YsymmBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[buckleCase](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YsymmBC.buckleCase "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YsymmBC.buckleCase (Python parameter) — A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE analysis.")=`abaqusConstants.NOT_APPLICABLE`*, *[localCsys](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YsymmBC.localCsys "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YsymmBC.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L1951-L1998)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YsymmBC "Permalink to this definition")
    :   This method creates a TypeBC object that specifies symmetry about the **Y** axis.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].YsymmBC
        ```

        Note

        Check [YsymmBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ysymmbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YsymmBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YsymmBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YsymmBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YsymmBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            buckleCase=`abaqusConstants.NOT_APPLICABLE`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YsymmBC.buckleCase "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
                analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
                PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YsymmBC.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YsymmBC-returns "Permalink to this headline")
        :   A TypeBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YsymmBC-return-type "Permalink to this headline")
        :   `TypeBC`

    ZasymmBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZasymmBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZasymmBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZasymmBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZasymmBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZasymmBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZasymmBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[buckleCase](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZasymmBC.buckleCase "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZasymmBC.buckleCase (Python parameter) — A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE analysis.")=`abaqusConstants.NOT_APPLICABLE`*, *[localCsys](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZasymmBC.localCsys "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZasymmBC.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L2147-L2194)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZasymmBC "Permalink to this definition")
    :   This method creates a TypeBC object that specifies antisymmetry about the **Z** axis.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ZasymmBC
        ```

        Note

        Check [ZasymmBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-zasymmbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZasymmBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZasymmBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZasymmBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZasymmBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            buckleCase=`abaqusConstants.NOT_APPLICABLE`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZasymmBC.buckleCase "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
                analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
                PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZasymmBC.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZasymmBC-returns "Permalink to this headline")
        :   A TypeBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZasymmBC-return-type "Permalink to this headline")
        :   `TypeBC`

    ZsymmBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZsymmBC.name "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZsymmBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZsymmBC.createStepName "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZsymmBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZsymmBC.region "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZsymmBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[buckleCase](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZsymmBC.buckleCase "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZsymmBC.buckleCase (Python parameter) — A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE analysis.")=`abaqusConstants.NOT_APPLICABLE`*, *[localCsys](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZsymmBC.localCsys "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZsymmBC.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L2000-L2047)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZsymmBC "Permalink to this definition")
    :   This method creates a TypeBC object that specifies symmetry about the **Z** axis.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ZsymmBC
        ```

        Note

        Check [ZsymmBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-zsymmbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZsymmBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZsymmBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZsymmBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZsymmBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            buckleCase=`abaqusConstants.NOT_APPLICABLE`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZsymmBC.buckleCase "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
                analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
                PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZsymmBC.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

        Returns:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZsymmBC-returns "Permalink to this headline")
        :   A TypeBC object.

        Return type:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZsymmBC-return-type "Permalink to this headline")
        :   `TypeBC`

## Other Classes[¶](#other-classes "Permalink to this heading")

*class* AccelerationBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.__init__.name (Python parameter)")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.__init__.createStepName (Python parameter)")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.__init__.region (Python parameter)")*, *[fieldName](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.__init__.fieldName (Python parameter)")=`''`*, *[a1](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.__init__.a1 (Python parameter)")=`abaqusConstants.UNSET`*, *[a2](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.__init__.a2 (Python parameter)")=`abaqusConstants.UNSET`*, *[a3](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.__init__.a3 (Python parameter)")=`abaqusConstants.UNSET`*, *[ar1](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.__init__.ar1 (Python parameter)")=`abaqusConstants.UNSET`*, *[ar2](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.__init__.ar2 (Python parameter)")=`abaqusConstants.UNSET`*, *[ar3](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.__init__.ar3 (Python parameter)")=`abaqusConstants.UNSET`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[localCsys](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.__init__.localCsys (Python parameter)")=`None`*, *[distributionType](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L15-L234)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC "Permalink to this definition")
:   Bases: [`BoundaryCondition`](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition "abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition (Python class)")

    The AccelerationBC object stores the data for an acceleration boundary condition. The AccelerationBC
    object is derived from the BoundaryCondition object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name]
    ```

    Note

    Check [AccelerationBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-accelerationbcpyc.htm?contextscope=all).

    Member Details:

    category : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.category "Permalink to this definition")
    :   A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L30-L32)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
        Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

    fieldName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L34-L37)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.fieldName "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this boundary
        condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
        default value is an empty string.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L46-L49)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the boundary
        condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L27-L28)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.name "Permalink to this definition")
    :   A String specifying the boundary condition repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L43-L44)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.region "Permalink to this definition")
    :   A Region object specifying the region to which the boundary condition is applied.

    setValues(*[fieldName](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.fieldName "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.fieldName (Python parameter) — A String specifying the name of the AnalyticalField object associated with this boundary condition.")=`''`*, *[a1](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.a1 "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.a1 (Python parameter) — A Float or a SymbolicConstant specifying the acceleration component in the 1-direction. Possible values for the SymbolicConstant are UNSET and SET.")=`abaqusConstants.UNSET`*, *[a2](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.a2 "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.a2 (Python parameter) — A Float or a SymbolicConstant specifying the acceleration component in the 2-direction. Possible values for the SymbolicConstant are UNSET and SET.")=`abaqusConstants.UNSET`*, *[a3](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.a3 "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.a3 (Python parameter) — A Float or a SymbolicConstant specifying the acceleration component in the 3-direction. Possible values for the SymbolicConstant are UNSET and SET.")=`abaqusConstants.UNSET`*, *[ar1](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.ar1 "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.ar1 (Python parameter) — A Float or a SymbolicConstant specifying the rotational acceleration component about the 1-direction.")=`abaqusConstants.UNSET`*, *[ar2](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.ar2 "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.ar2 (Python parameter) — A Float or a SymbolicConstant specifying the rotational acceleration component about the 2-direction.")=`abaqusConstants.UNSET`*, *[ar3](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.ar3 "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.ar3 (Python parameter) — A Float or a SymbolicConstant specifying the rotational acceleration component about the 3-direction.")=`abaqusConstants.UNSET`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.amplitude "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[localCsys](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.localCsys "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*, *[distributionType](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.distributionType "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD.")=`abaqusConstants.UNIFORM`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L130-L188)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues "Permalink to this definition")
    :   This method modifies the data for an existing AccelerationBC object in the step where it is created.

        Note

        Check [AccelerationBC.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-accelerationbcpyc.htm?contextscope=all#simaker-accelerationbcsetvaluespyc).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues-parameters "Permalink to this headline")
        :   fieldName=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.fieldName "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this boundary
                condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
                default value is an empty string.

            a1=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.a1 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the acceleration component in the 1-direction.
                Possible values for the SymbolicConstant are UNSET and SET. The default value is
                UNSET. Note: Although **a1**, **a2**, **a3**, **ar1**, **ar2**, and **ar3** are optional arguments, at
                least one of them must be specified.

            a2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.a2 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the acceleration component in the 2-direction.
                Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

            a3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.a3 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the acceleration component in the 3-direction.
                Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

            ar1=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.ar1 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational acceleration component about the
                1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET.

            ar2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.ar2 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational acceleration component about the
                2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET.

            ar3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.ar3 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational acceleration component about the
                3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

    setValuesInStep(*[stepName](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep.stepName "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition is modified.")*, *[a1](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep.a1 "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep.a1 (Python parameter) — A Float or a SymbolicConstant specifying the acceleration component in the 1-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.")=`abaqusConstants.SET`*, *[a2](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep.a2 "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep.a2 (Python parameter) — A Float or a SymbolicConstant specifying the acceleration component in the 2-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.")=`abaqusConstants.SET`*, *[a3](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep.a3 "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep.a3 (Python parameter) — A Float or a SymbolicConstant specifying the acceleration component in the 3-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.")=`abaqusConstants.SET`*, *[ar1](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep.ar1 "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep.ar1 (Python parameter) — A Float or a SymbolicConstant specifying the rotational acceleration component about the 1-direction.")=`abaqusConstants.SET`*, *[ar2](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep.ar2 "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep.ar2 (Python parameter) — A Float or a SymbolicConstant specifying the rotational acceleration component about the 2-direction.")=`abaqusConstants.SET`*, *[ar3](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep.ar3 "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep.ar3 (Python parameter) — A Float or a SymbolicConstant specifying the rotational acceleration component about the 3-direction.")=`abaqusConstants.SET`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep.amplitude "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L190-L234)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing AccelerationBC object in the specified
        step.

        Note

        Check [AccelerationBC.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-accelerationbcpyc.htm?contextscope=all#simaker-accelerationbcsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is modified.

            a1=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep.a1 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the acceleration component in the 1-direction.
                Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.

            a2=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep.a2 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the acceleration component in the 2-direction.
                Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.

            a3=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep.a3 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the acceleration component in the 3-direction.
                Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.

            ar1=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep.ar1 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational acceleration component about the
                1-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.

            ar2=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep.ar2 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational acceleration component about the
                2-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.

            ar3=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep.ar3 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational acceleration component about the
                3-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.

            amplitude=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBC.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                boundary condition is changed to have no amplitude reference. You should provide the
                **amplitude** argument only if it is valid for the specified step.

*class* BoundaryCondition[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py#L9-L97)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The BoundaryCondition object is the abstract base type for other BoundaryCondition objects. The
    BoundaryCondition object has no explicit constructor. The methods and members of the BoundaryCondition
    object are common to all objects derived from the BoundaryCondition.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name]
    ```

    Note

    Check [BoundaryCondition on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionpyc.htm?contextscope=all).

    Member Details:

    category : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.category "Permalink to this definition")
    :   A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.

    deactivate(*[stepName](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.deactivate.stepName "abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.deactivate.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition is deactivated.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py#L37-L46)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.deactivate "Permalink to this definition")
    :   This method deactivates the boundary condition in the specified step and all subsequent steps.

        Note

        Check [BoundaryCondition.deactivate on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionpyc.htm?contextscope=all#simaker-boundaryconditiondeactivatepyc).

        Parameters:[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.deactivate-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.deactivate.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is deactivated.

    delete(*[indices](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.delete.indices "abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.delete.indices (Python parameter) — A sequence of Ints specifying the index of each boundary condition to delete.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py#L84-L93)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.delete "Permalink to this definition")
    :   This method allows you to delete existing boundary conditions.

        Note

        Check [BoundaryCondition.delete on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionpyc.htm?contextscope=all#simaker-boundaryconditiondeletepyc).

        Parameters:[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.delete-parameters "Permalink to this headline")
        :   indices[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.delete.indices "Permalink to this definition")
            :   A sequence of Ints specifying the index of each boundary condition to delete.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py#L32-L35)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the boundary
        condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    move(*[fromStepName](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.move.fromStepName "abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.move.fromStepName (Python parameter) — A String specifying the name of the step from which the boundary condition state is moved.")*, *[toStepName](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.move.toStepName "abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.move.toStepName (Python parameter) — A String specifying the name of the step to which the boundary condition state is moved.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py#L48-L60)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.move "Permalink to this definition")
    :   This method moves the boundary condition state from one step to a different step.

        Note

        Check [BoundaryCondition.move on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionpyc.htm?contextscope=all#simaker-boundaryconditionmovepyc).

        Parameters:[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.move-parameters "Permalink to this headline")
        :   fromStepName[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.move.fromStepName "Permalink to this definition")
            :   A String specifying the name of the step from which the boundary condition state is
                moved.

            toStepName[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.move.toStepName "Permalink to this definition")
            :   A String specifying the name of the step to which the boundary condition state is moved.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py#L22-L23)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.name "Permalink to this definition")
    :   A String specifying the boundary condition repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py#L29-L30)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.region "Permalink to this definition")
    :   A Region object specifying the region to which the boundary condition is applied.

    reset(*[stepName](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.reset.stepName "abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.reset.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition state is reset.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py#L62-L72)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.reset "Permalink to this definition")
    :   This method resets the boundary condition state of the specified step to the state of the previous
        analysis step.

        Note

        Check [BoundaryCondition.reset on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionpyc.htm?contextscope=all#simaker-boundaryconditionresetpyc).

        Parameters:[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.reset-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.reset.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition state is reset.

    resume()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py#L74-L77)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.resume "Permalink to this definition")
    :   This method resumes the boundary condition that was previously suppressed.

    setValues(*\*[args](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.setValues "abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.setValues.args (Python parameter)")*, *\*\*[kwargs](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.setValues "abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.setValues.kwargs (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py#L95-L95)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.setValues "Permalink to this definition")

    setValuesInStep(*\*[args](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.setValuesInStep "abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.setValuesInStep.args (Python parameter)")*, *\*\*[kwargs](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.setValuesInStep "abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.setValuesInStep.kwargs (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py#L97-L97)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.setValuesInStep "Permalink to this definition")

    suppress()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py#L79-L82)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition.suppress "Permalink to this definition")
    :   This method suppresses the boundary condition.

*class* AccelerationBCState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L9-L94)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBCState "Permalink to this definition")
:   Bases: [`BoundaryConditionState`](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState "abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState (Python class)")

    The AccelerationBCState object stores the propagating data of an acceleration boundary condition in a
    step. One instance of this object is created internally by the AccelerationBC object for each step. The
    instance is also deleted internally by the AccelerationBC object. The AccelerationBCState object has no
    constructor or methods. The AccelerationBCState object is derived from the BoundaryConditionState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].boundaryConditionStates[name]
    ```

    The corresponding analysis keywords are:

    * BOUNDARY

    Note

    Check [AccelerationBCState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-accelerationbcstatepyc.htm?contextscope=all).

    Member Details:

    a1 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L27-L28)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBCState.a1 "Permalink to this definition")
    :   A Float specifying the acceleration component in the 1-direction.

    a1State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBCState.a1State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the acceleration component in the
        1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    a2 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L30-L31)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBCState.a2 "Permalink to this definition")
    :   A Float specifying the acceleration component in the 2-direction.

    a2State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBCState.a2State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the acceleration component in the
        2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    a3 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L33-L34)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBCState.a3 "Permalink to this definition")
    :   A Float specifying the acceleration component in the 3-direction.

    a3State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBCState.a3State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the acceleration component in the
        3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L9-L94)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBCState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the
        boundary condition has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBCState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    ar1 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L36-L37)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBCState.ar1 "Permalink to this definition")
    :   A Float specifying the rotational acceleration component about the 1-direction.

    ar1State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBCState.ar1State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the rotational acceleration
        component about the 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
        MODIFIED.

    ar2 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L39-L40)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBCState.ar2 "Permalink to this definition")
    :   A Float specifying the rotational acceleration component about the 2-direction.

    ar2State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBCState.ar2State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the rotational acceleration
        component about the 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
        MODIFIED.

    ar3 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L42-L43)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBCState.ar3 "Permalink to this definition")
    :   A Float specifying the rotational acceleration component about the 3-direction.

    ar3State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBCState.ar3State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the rotational acceleration
        component about the 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
        MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBCState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * PROPAGATED\_FROM\_BASE\_STATE
        * MODIFIED\_FROM\_BASE\_STATE
        * DEACTIVATED\_FROM\_BASE\_STATE
        * BUILT\_INTO\_MODES

*class* BoundaryConditionState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBCState.py#L8-L43)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The BoundaryConditionState object is the abstract base type for other BoundaryConditionState objects. The
    BoundaryConditionState object has no explicit constructor or methods. The members of the
    BoundaryConditionState object are common to all objects derived from the BoundaryConditionState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].boundaryConditionStates[name]
    ```

    Note

    Check [BoundaryConditionState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-boundaryconditionstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBCState.py#L8-L43)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the
        boundary condition has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBCState.py)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBCState.py)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * PROPAGATED\_FROM\_BASE\_STATE
        * MODIFIED\_FROM\_BASE\_STATE
        * DEACTIVATED\_FROM\_BASE\_STATE
        * BUILT\_INTO\_MODES

*class* AccelerationBaseMotionBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.__init__.name (Python parameter)")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.__init__.createStepName (Python parameter)")*, *[dof](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.__init__.dof (Python parameter)")*, *[amplitudeScaleFactor](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.__init__.amplitudeScaleFactor (Python parameter)")=`1`*, *[centerOfRotation](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.__init__.centerOfRotation (Python parameter)")=`()`*, *[correlation](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.__init__.correlation (Python parameter)")=`None`*, *[secondaryBase](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.__init__.secondaryBase (Python parameter)")=`''`*, *[useComplex](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.__init__.useComplex (Python parameter)")=`0`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L14-L166)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC "Permalink to this definition")
:   Bases: [`BoundaryCondition`](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition "abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition (Python class)")

    The AccelerationBaseMotionBC object stores the data for an acceleration base motion boundary condition.
    The AccelerationBaseMotionBC object is derived from the BoundaryCondition object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name]
    ```

    Note

    Check [AccelerationBaseMotionBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-accelerationbasemotionbcpyc.htm?contextscope=all).

    Member Details:

    amplitudeScaleFactor : --is-rst--:py:class:`float` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L29-L30)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.amplitudeScaleFactor "Permalink to this definition")
    :   A Float specifying the scale factor for the amplitude curve. The default value is 1.0.

    category : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.category "Permalink to this definition")
    :   A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.

    centerOfRotation : --is-rst--:py:class:`tuple` = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L36-L38)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.centerOfRotation "Permalink to this definition")
    :   A ModelDot object specifying a tuple containing one center of rotation. The default
        value is the global origin. This argument applies only when **dof** = UR1, UR2, or UR3.

    correlation : --is-rst--:py:class:`~abaqus.Amplitude.Correlation.Correlation` = `<abaqus.Amplitude.Correlation.Correlation object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L40-L41)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.correlation "Permalink to this definition")
    :   A Correlation object.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L54-L57)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the boundary
        condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L26-L27)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.name "Permalink to this definition")
    :   A String specifying the boundary condition repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L51-L52)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.region "Permalink to this definition")
    :   A Region object specifying the region to which the boundary condition is applied.

    secondaryBase : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L43-L45)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.secondaryBase "Permalink to this definition")
    :   A String specifying the name of the SecondaryBaseBC object associated with this boundary
        condition. The default value is an empty string.

    setValues(*[amplitudeScaleFactor](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValues.amplitudeScaleFactor "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValues.amplitudeScaleFactor (Python parameter) — A Float specifying the scale factor for the amplitude curve.")=`1`*, *[centerOfRotation](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValues.centerOfRotation "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValues.centerOfRotation (Python parameter) — A ModelDot object specifying a tuple containing one center of rotation.")=`()`*, *[correlation](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValues.correlation "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValues.correlation (Python parameter) — A Correlation object.")=`None`*, *[secondaryBase](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValues.secondaryBase "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValues.secondaryBase (Python parameter) — A String specifying the name of the SecondaryBaseBC object associated with this boundary condition.")=`''`*, *[useComplex](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValues.useComplex "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValues.useComplex (Python parameter) — A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base motion record given by amplitude definition.")=`0`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValues.amplitude "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L114-L148)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValues "Permalink to this definition")
    :   This method modifies the data for an existing AccelerationBaseMotionBC object in the step where it is
        created.

        Note

        Check [AccelerationBaseMotionBC.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-accelerationbasemotionbcpyc.htm?contextscope=all#simaker-accelerationbasemotionbcsetvaluespyc).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValues-parameters "Permalink to this headline")
        :   amplitudeScaleFactor=`1`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValues.amplitudeScaleFactor "Permalink to this definition")
            :   A Float specifying the scale factor for the amplitude curve. The default value is 1.0.

            centerOfRotation=`()`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValues.centerOfRotation "Permalink to this definition")
            :   A ModelDot object specifying a tuple containing one center of rotation. The default
                value is the global origin. This argument applies only when **dof** = UR1, UR2, or UR3.

            correlation=`None`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValues.correlation "Permalink to this definition")
            :   A Correlation object.

            secondaryBase=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValues.secondaryBase "Permalink to this definition")
            :   A String specifying the name of the SecondaryBaseBC object associated with this boundary
                condition. The default value is an empty string.

            useComplex=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValues.useComplex "Permalink to this definition")
            :   A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base
                motion record given by amplitude definition. The default value is OFF.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

    setValuesInStep(*[stepName](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValuesInStep.stepName "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition is modified.")*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValuesInStep.amplitude "abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L150-L166)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing AccelerationBaseMotionBC object in the
        specified step.

        Note

        Check [AccelerationBaseMotionBC.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-accelerationbasemotionbcpyc.htm?contextscope=all#simaker-accelerationbasemotionbcsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is modified.

            amplitude=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                boundary condition is changed to have no amplitude reference. You should provide the
                **amplitude** argument only if it is valid for the specified step.

    useComplex : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L32-L34)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBC.useComplex "Permalink to this definition")
    :   A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base
        motion record given by amplitude definition. The default value is OFF.

*class* AccelerationBaseMotionBCState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L9-L50)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBCState "Permalink to this definition")
:   Bases: [`BoundaryConditionState`](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState "abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState (Python class)")

    The AccelerationBaseMotionBCState object stores the propagating data for a velocity base motion boundary
    condition in a step. One instance of this object is created internally by the AccelerationBaseMotionBC
    object for each step. The instance is also deleted internally by the AccelerationBaseMotionBC object. The
    AccelerationBaseMotionBCState object has no constructor or methods. The AccelerationBaseMotionBCState object
    is derived from the BoundaryConditionState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].boundaryConditionStates[name]
    ```

    The corresponding analysis keywords are:

    * BASE MOTION

    Note

    Check [AccelerationBaseMotionBCState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-accelerationbasemotionbcstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L9-L50)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBCState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the
        boundary condition has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBCState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AccelerationBaseMotionBCState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * PROPAGATED\_FROM\_BASE\_STATE
        * MODIFIED\_FROM\_BASE\_STATE
        * DEACTIVATED\_FROM\_BASE\_STATE
        * BUILT\_INTO\_MODES

*class* AcousticPressureBC(*[name](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC "abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.__init__.name (Python parameter)")*, *[createStepName](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC "abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.__init__.createStepName (Python parameter)")*, *[region](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC "abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.__init__.region (Python parameter)")*, *[fieldName](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC "abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.__init__.fieldName (Python parameter)")=`''`*, *[magnitude](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC "abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.__init__.magnitude (Python parameter)")=`0`*, *[distributionType](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC "abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC "abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[fixed](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC "abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.__init__.fixed (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L22-L169)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC "Permalink to this definition")
:   Bases: [`BoundaryCondition`](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition "abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition (Python class)")

    The AcousticPressureBC object stores the data for an acoustic pressure boundary condition. The
    AcousticPressureBC object is derived from the BoundaryCondition object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name]
    ```

    Note

    Check [AcousticPressureBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acousticpressurebcpyc.htm?contextscope=all).

    Member Details:

    category : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.category "Permalink to this definition")
    :   A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L37-L39)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
        Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

    fieldName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L41-L44)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.fieldName "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this boundary
        condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
        default value is an empty string.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L53-L56)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the boundary
        condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L34-L35)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.name "Permalink to this definition")
    :   A String specifying the boundary condition repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L50-L51)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.region "Permalink to this definition")
    :   A Region object specifying the region to which the boundary condition is applied.

    setValues(*[fieldName](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValues.fieldName "abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValues.fieldName (Python parameter) — A String specifying the name of the AnalyticalField object associated with this boundary condition.")=`''`*, *[magnitude](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValues.magnitude "abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValues.magnitude (Python parameter) — A Float specifying the acoustic pressure magnitude.")=`0`*, *[distributionType](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValues.distributionType "abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD.")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValues.amplitude "abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[fixed](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValues.fixed "abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValues.fixed (Python parameter) — A Boolean specifying whether the boundary condition should remain fixed at the current values at the start of the step.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L111-L144)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValues "Permalink to this definition")
    :   This method modifies the data for an existing AcousticPressureBC object in the step where it is
        created.

        Note

        Check [AcousticPressureBC.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acousticpressurebcpyc.htm?contextscope=all#simaker-acousticpressurebcsetvaluespyc).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValues-parameters "Permalink to this headline")
        :   fieldName=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValues.fieldName "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this boundary
                condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
                default value is an empty string.

            magnitude=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValues.magnitude "Permalink to this definition")
            :   A Float specifying the acoustic pressure magnitude. The default value is 0. The
                **magnitude** argument is optional if **distributionType** = USER\_DEFINED.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            fixed=`0`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValues.fixed "Permalink to this definition")
            :   A Boolean specifying whether the boundary condition should remain fixed at the current
                values at the start of the step. The default value is OFF.

    setValuesInStep(*[stepName](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValuesInStep.stepName "abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition is modified.")*, *[magnitude](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValuesInStep.magnitude "abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValuesInStep.magnitude (Python parameter) — A Float or the SymbolicConstant FREED specifying the acoustic pressure magnitude.")=`abaqusConstants.UNCHANGED`*, *[amplitude](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValuesInStep.amplitude "abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L146-L169)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing AcousticPressureBC object in the specified
        step.

        Note

        Check [AcousticPressureBC.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acousticpressurebcpyc.htm?contextscope=all#simaker-acousticpressurebcsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is modified.

            magnitude=`abaqusConstants.UNCHANGED`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float or the SymbolicConstant FREED specifying the acoustic pressure magnitude.

            amplitude=`''`[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBC.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                boundary condition is changed to have no amplitude reference. You should provide the
                **amplitude** argument only if it is valid for the specified step.

*class* AcousticPressureBCState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L9-L57)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBCState "Permalink to this definition")
:   Bases: [`BoundaryConditionState`](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState "abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState (Python class)")

    The AcousticPressureBCState object stores the propagating data for an acoustic pressure boundary
    condition in a step. One instance of this object is created internally by the AcousticPressureBC object for
    each step. The instance is also deleted internally by the AcousticPressureBC object. The
    AcousticPressureBCState object has no constructor or methods. The AcousticPressureBCState object is derived
    from the BoundaryConditionState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].boundaryConditionStates[name]
    ```

    The corresponding analysis keywords are:

    * BOUNDARY

    Note

    Check [AcousticPressureBCState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acousticpressurebcstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L9-L57)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBCState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the
        boundary condition has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBCState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py#L28-L29)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBCState.magnitude "Permalink to this definition")
    :   A Float specifying the acoustic pressure magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBCState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the acoustic pressure magnitude.
        Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/BoundaryConditionModel.py)[¶](#abaqus.BoundaryCondition.BoundaryConditionModel.AcousticPressureBCState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * PROPAGATED\_FROM\_BASE\_STATE
        * MODIFIED\_FROM\_BASE\_STATE
        * DEACTIVATED\_FROM\_BASE\_STATE
        * BUILT\_INTO\_MODES

*class* ConcentrationBC(*[name](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC "abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.__init__.name (Python parameter)")*, *[createStepName](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC "abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.__init__.createStepName (Python parameter)")*, *[region](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC "abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.__init__.region (Python parameter)")*, *[fieldName](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC "abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.__init__.fieldName (Python parameter)")=`''`*, *[magnitude](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC "abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.__init__.magnitude (Python parameter)")=`0`*, *[distributionType](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC "abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC "abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[fixed](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC "abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.__init__.fixed (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConcentrationBC.py#L22-L168)[¶](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC "Permalink to this definition")
:   Bases: [`BoundaryCondition`](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition "abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition (Python class)")

    The ConcentrationBC object stores the data for a concentration boundary condition. The ConcentrationBC
    object is derived from the BoundaryCondition object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name]
    ```

    Note

    Check [ConcentrationBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concentrationbcpyc.htm?contextscope=all).

    Member Details:

    category : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConcentrationBC.py)[¶](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.category "Permalink to this definition")
    :   A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConcentrationBC.py#L37-L39)[¶](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
        Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

    fieldName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConcentrationBC.py#L41-L44)[¶](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.fieldName "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this boundary
        condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
        default value is an empty string.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConcentrationBC.py#L53-L56)[¶](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the boundary
        condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConcentrationBC.py#L34-L35)[¶](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.name "Permalink to this definition")
    :   A String specifying the boundary condition repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConcentrationBC.py#L50-L51)[¶](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.region "Permalink to this definition")
    :   A Region object specifying the region to which the boundary condition is applied.

    setValues(*[fieldName](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValues.fieldName "abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValues.fieldName (Python parameter) — A String specifying the name of the AnalyticalField object associated with this boundary condition.")=`''`*, *[magnitude](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValues.magnitude "abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValues.magnitude (Python parameter) — A Float specifying the concentration magnitude.")=`0`*, *[distributionType](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValues.distributionType "abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD.")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValues.amplitude "abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[fixed](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValues.fixed "abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValues.fixed (Python parameter) — A Boolean specifying whether the boundary condition should remain fixed at the current values at the start of the step.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConcentrationBC.py#L111-L143)[¶](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValues "Permalink to this definition")
    :   This method modifies the data for an existing ConcentrationBC object in the step where it is created.

        Note

        Check [ConcentrationBC.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concentrationbcpyc.htm?contextscope=all#simaker-concentrationbcsetvaluespyc).

        Parameters:[¶](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValues-parameters "Permalink to this headline")
        :   fieldName=`''`[¶](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValues.fieldName "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this boundary
                condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
                default value is an empty string.

            magnitude=`0`[¶](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValues.magnitude "Permalink to this definition")
            :   A Float specifying the concentration magnitude. The default value is 0. The **magnitude**
                argument is optional if **distributionType** = USER\_DEFINED.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            fixed=`0`[¶](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValues.fixed "Permalink to this definition")
            :   A Boolean specifying whether the boundary condition should remain fixed at the current
                values at the start of the step. The default value is OFF.

    setValuesInStep(*[stepName](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValuesInStep.stepName "abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition is modified.")*, *[magnitude](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValuesInStep.magnitude "abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValuesInStep.magnitude (Python parameter) — A Float or the SymbolicConstant FREED specifying the concentration magnitude.")=`abaqusConstants.UNCHANGED`*, *[amplitude](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValuesInStep.amplitude "abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConcentrationBC.py#L145-L168)[¶](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing ConcentrationBC object in the specified
        step.

        Note

        Check [ConcentrationBC.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concentrationbcpyc.htm?contextscope=all#simaker-concentrationbcsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is modified.

            magnitude=`abaqusConstants.UNCHANGED`[¶](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float or the SymbolicConstant FREED specifying the concentration magnitude.

            amplitude=`''`[¶](#abaqus.BoundaryCondition.ConcentrationBC.ConcentrationBC.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                boundary condition is changed to have no amplitude reference. You should provide the
                **amplitude** argument only if it is valid for the specified step.

*class* ConcentrationBCState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConcentrationBCState.py#L9-L56)[¶](#abaqus.BoundaryCondition.ConcentrationBCState.ConcentrationBCState "Permalink to this definition")
:   Bases: [`BoundaryConditionState`](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState "abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState (Python class)")

    The ConcentrationBCState object stores the propagating data for a concentration boundary condition in a
    step. One instance of this object is created internally by the ConcentrationBC object for each step. The
    instance is also deleted internally by the ConcentrationBC object. The ConcentrationBCState object has no
    constructor or methods. The ConcentrationBCState object is derived from the BoundaryConditionState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].boundaryConditionStates[name]
    ```

    The corresponding analysis keywords are:

    * BOUNDARY

    Note

    Check [ConcentrationBCState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concentrationbcstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConcentrationBCState.py#L9-L56)[¶](#abaqus.BoundaryCondition.ConcentrationBCState.ConcentrationBCState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the
        boundary condition has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConcentrationBCState.py)[¶](#abaqus.BoundaryCondition.ConcentrationBCState.ConcentrationBCState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConcentrationBCState.py#L27-L28)[¶](#abaqus.BoundaryCondition.ConcentrationBCState.ConcentrationBCState.magnitude "Permalink to this definition")
    :   A Float specifying the concentration magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConcentrationBCState.py)[¶](#abaqus.BoundaryCondition.ConcentrationBCState.ConcentrationBCState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the concentration magnitude.
        Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConcentrationBCState.py)[¶](#abaqus.BoundaryCondition.ConcentrationBCState.ConcentrationBCState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * PROPAGATED\_FROM\_BASE\_STATE
        * MODIFIED\_FROM\_BASE\_STATE
        * DEACTIVATED\_FROM\_BASE\_STATE
        * BUILT\_INTO\_MODES

*class* ConnAccelerationBC(*[name](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.__init__.name (Python parameter)")*, *[createStepName](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.__init__.createStepName (Python parameter)")*, *[region](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.__init__.region (Python parameter)")=`''`*, *[fastenerName](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.__init__.fastenerName (Python parameter)")=`''`*, *[fastenerSetName](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.__init__.fastenerSetName (Python parameter)")=`''`*, *[a1](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.__init__.a1 (Python parameter)")=`abaqusConstants.UNSET`*, *[a2](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.__init__.a2 (Python parameter)")=`abaqusConstants.UNSET`*, *[a3](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.__init__.a3 (Python parameter)")=`abaqusConstants.UNSET`*, *[ar1](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.__init__.ar1 (Python parameter)")=`abaqusConstants.UNSET`*, *[ar2](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.__init__.ar2 (Python parameter)")=`abaqusConstants.UNSET`*, *[ar3](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.__init__.ar3 (Python parameter)")=`abaqusConstants.UNSET`*, *[amplitude](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBC.py#L15-L262)[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC "Permalink to this definition")
:   Bases: [`BoundaryCondition`](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition "abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition (Python class)")

    The ConnAccelerationBC object stores the data for a connector acceleration boundary condition. The
    ConnAccelerationBC object is derived from the BoundaryCondition object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name]
    ```

    Note

    Check [ConnAccelerationBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connaccelerationbcpyc.htm?contextscope=all).

    Member Details:

    category : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBC.py)[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.category "Permalink to this definition")
    :   A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBC.py#L30-L32)[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
        Possible values are UNIFORM and USER\_DEFINED. The default value is UNIFORM.

    fastenerName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBC.py#L34-L38)[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.fastenerName "Permalink to this definition")
    :   A String specifying the name of the assembled fastener to which the boundary condition
        will be applied. This argument is not valid when **region** is specified. When this
        argument is specified, **fastenerSetName** must also be specified. The default value is an
        empty string.

    fastenerSetName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBC.py#L40-L44)[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.fastenerSetName "Permalink to this definition")
    :   A String specifying the assembled fastener template model set to which the boundary
        condition will be applied. This argument is not valid when **region** is specified. When
        this argument is specified, **fastenerName** must also be specified. The default value is
        an empty string.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBC.py#L53-L56)[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the boundary
        condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBC.py#L27-L28)[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.name "Permalink to this definition")
    :   A String specifying the boundary condition repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBC.py#L50-L51)[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.region "Permalink to this definition")
    :   A Region object specifying the region to which the boundary condition is applied.

    setValues(*[region](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.region "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.region (Python parameter) — The wire region to which the boundary condition is applied.")=`''`*, *[fastenerName](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.fastenerName "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.fastenerName (Python parameter) — A String specifying the name of the assembled fastener to which the boundary condition will be applied.")=`''`*, *[fastenerSetName](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.fastenerSetName "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.fastenerSetName (Python parameter) — A String specifying the assembled fastener template model set to which the boundary condition will be applied.")=`''`*, *[a1](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.a1 "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.a1 (Python parameter) — A Float or a SymbolicConstant specifying the acceleration component in the connector's local 1-direction.")=`abaqusConstants.UNSET`*, *[a2](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.a2 "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.a2 (Python parameter) — A Float or a SymbolicConstant specifying the acceleration component in the connector's local 2-direction.")=`abaqusConstants.UNSET`*, *[a3](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.a3 "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.a3 (Python parameter) — A Float or a SymbolicConstant specifying the acceleration component in the connector's local 3-direction.")=`abaqusConstants.UNSET`*, *[ar1](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.ar1 "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.ar1 (Python parameter) — A Float or a SymbolicConstant specifying the rotational acceleration component in the connector's local 4-direction.")=`abaqusConstants.UNSET`*, *[ar2](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.ar2 "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.ar2 (Python parameter) — A Float or a SymbolicConstant specifying the rotational acceleration component in the connector's local 5-direction.")=`abaqusConstants.UNSET`*, *[ar3](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.ar3 "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.ar3 (Python parameter) — A Float or a SymbolicConstant specifying the rotational acceleration component in the connector's local 6-direction.")=`abaqusConstants.UNSET`*, *[amplitude](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.amplitude "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.distributionType "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM and USER_DEFINED.")=`abaqusConstants.UNIFORM`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBC.py#L143-L210)[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues "Permalink to this definition")
    :   This method modifies the data for an existing ConnAccelerationBC object in the step where it is
        created.

        Note

        Check [ConnAccelerationBC.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connaccelerationbcpyc.htm?contextscope=all#simaker-connaccelerationbcsetvaluespyc).

        Parameters:[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues-parameters "Permalink to this headline")
        :   region=`''`[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.region "Permalink to this definition")
            :   The wire region to which the boundary condition is applied. This argument is not valid
                when **fastenerName** and **fastenerSetName** are specified.

            fastenerName=`''`[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.fastenerName "Permalink to this definition")
            :   A String specifying the name of the assembled fastener to which the boundary condition
                will be applied. This argument is not valid when **region** is specified. When this
                argument is specified, **fastenerSetName** must also be specified. The default value is an
                empty string.

            fastenerSetName=`''`[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.fastenerSetName "Permalink to this definition")
            :   A String specifying the assembled fastener template model set to which the boundary
                condition will be applied. This argument is not valid when **region** is specified. When
                this argument is specified, **fastenerName** must also be specified. The default value is
                an empty string.

            a1=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.a1 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the acceleration component in the connector’s
                local 1-direction. Possible values for the SymbolicConstant are UNSET and SET. The
                default value is UNSET. Note: Although **a1**, **a2**, **a3**, **ar1**, **ar2**, and **ar3** are
                optional arguments, at least one of them must be specified.

            a2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.a2 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the acceleration component in the connector’s
                local 2-direction. Possible values for the SymbolicConstant are UNSET and SET. The
                default value is UNSET.

            a3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.a3 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the acceleration component in the connector’s
                local 3-direction. Possible values for the SymbolicConstant are UNSET and SET. The
                default value is UNSET.

            ar1=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.ar1 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational acceleration component in the
                connector’s local 4-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            ar2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.ar2 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational acceleration component in the
                connector’s local 5-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            ar3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.ar3 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational acceleration component in the
                connector’s local 6-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM and USER\_DEFINED. The default value is UNIFORM.

    setValuesInStep(*[stepName](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep.stepName "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition is modified.")*, *[a1](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep.a1 "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep.a1 (Python parameter) — A Float or a SymbolicConstant specifying the connector acceleration component in the connector's local 1-direction.")=`abaqusConstants.SET`*, *[a2](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep.a2 "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep.a2 (Python parameter) — A Float or a SymbolicConstant specifying the connector acceleration component in the connector's local 2-direction.")=`abaqusConstants.SET`*, *[a3](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep.a3 "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep.a3 (Python parameter) — A Float or a SymbolicConstant specifying the connector acceleration component in the connector's local 3-direction.")=`abaqusConstants.SET`*, *[ar1](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep.ar1 "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep.ar1 (Python parameter) — A Float or a SymbolicConstant specifying the connector acceleration component in the connector's local 4-direction.")=`abaqusConstants.SET`*, *[ar2](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep.ar2 "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep.ar2 (Python parameter) — A Float or a SymbolicConstant specifying the connector acceleration component in the connector's local 5-direction.")=`abaqusConstants.SET`*, *[ar3](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep.ar3 "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep.ar3 (Python parameter) — A Float or a SymbolicConstant specifying the connector acceleration component in the connector's local 6-direction.")=`abaqusConstants.SET`*, *[amplitude](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep.amplitude "abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBC.py#L212-L262)[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing ConnAccelerationBC object in the specified
        step.

        Note

        Check [ConnAccelerationBC.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connaccelerationbcpyc.htm?contextscope=all#simaker-connaccelerationbcsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is modified.

            a1=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep.a1 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the connector acceleration component in the
                connector’s local 1-direction. Possible values for the SymbolicConstant are SET,
                UNCHANGED, and FREED.

            a2=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep.a2 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the connector acceleration component in the
                connector’s local 2-direction. Possible values for the SymbolicConstant are SET,
                UNCHANGED, and FREED.

            a3=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep.a3 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the connector acceleration component in the
                connector’s local 3-direction. Possible values for the SymbolicConstant are SET,
                UNCHANGED, and FREED.

            ar1=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep.ar1 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the connector acceleration component in the
                connector’s local 4-direction. Possible values for the SymbolicConstant are SET,
                UNCHANGED, and FREED.

            ar2=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep.ar2 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the connector acceleration component in the
                connector’s local 5-direction. Possible values for the SymbolicConstant are SET,
                UNCHANGED, and FREED.

            ar3=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep.ar3 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the connector acceleration component in the
                connector’s local 6-direction. Possible values for the SymbolicConstant are SET,
                UNCHANGED, and FREED.

            amplitude=`''`[¶](#abaqus.BoundaryCondition.ConnAccelerationBC.ConnAccelerationBC.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                boundary condition is changed to have no amplitude reference. You should provide the
                **amplitude** argument only if it is valid for the specified step.

*class* ConnAccelerationBCState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBCState.py#L9-L104)[¶](#abaqus.BoundaryCondition.ConnAccelerationBCState.ConnAccelerationBCState "Permalink to this definition")
:   Bases: [`BoundaryConditionState`](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState "abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState (Python class)")

    The ConnAccelerationBCState object stores the propagating data of a connector acceleration boundary
    condition in a step. One instance of this object is created internally by the ConnAccelerationBC object for
    each step. The instance is also deleted internally by the ConnAccelerationBC object. The
    ConnAccelerationBCState object has no constructor or methods. The ConnAccelerationBCState object is derived
    from the BoundaryConditionState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].boundaryConditionStates[name]
    ```

    The corresponding analysis keywords are:

    * CONNECTOR MOTION

    Note

    Check [ConnAccelerationBCState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connaccelerationbcstatepyc.htm?contextscope=all).

    Member Details:

    a1 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBCState.py#L28-L30)[¶](#abaqus.BoundaryCondition.ConnAccelerationBCState.ConnAccelerationBCState.a1 "Permalink to this definition")
    :   A Float specifying the connector acceleration component in the connector’s local
        1-direction.

    a1State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBCState.py)[¶](#abaqus.BoundaryCondition.ConnAccelerationBCState.ConnAccelerationBCState.a1State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the connector acceleration
        component in the connector’s local 1-direction. Possible values are UNSET, SET,
        UNCHANGED, FREED, and MODIFIED.

    a2 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBCState.py#L28-L30)[¶](#abaqus.BoundaryCondition.ConnAccelerationBCState.ConnAccelerationBCState.a2 "Permalink to this definition")
    :   A Float specifying the connector acceleration component in the connector’s local
        2-direction.

    a2State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBCState.py)[¶](#abaqus.BoundaryCondition.ConnAccelerationBCState.ConnAccelerationBCState.a2State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the connector acceleration
        component in the connector’s local 2-direction. Possible values are UNSET, SET,
        UNCHANGED, FREED, and MODIFIED.

    a3 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBCState.py#L28-L30)[¶](#abaqus.BoundaryCondition.ConnAccelerationBCState.ConnAccelerationBCState.a3 "Permalink to this definition")
    :   A Float specifying the connector acceleration component in the connector’s local
        3-direction.

    a3State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBCState.py)[¶](#abaqus.BoundaryCondition.ConnAccelerationBCState.ConnAccelerationBCState.a3State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the connector acceleration
        component in the connector’s local 3-direction. Possible values are UNSET, SET,
        UNCHANGED, FREED, and MODIFIED.

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBCState.py#L9-L104)[¶](#abaqus.BoundaryCondition.ConnAccelerationBCState.ConnAccelerationBCState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the
        boundary condition has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBCState.py)[¶](#abaqus.BoundaryCondition.ConnAccelerationBCState.ConnAccelerationBCState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    ar1 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBCState.py#L28-L30)[¶](#abaqus.BoundaryCondition.ConnAccelerationBCState.ConnAccelerationBCState.ar1 "Permalink to this definition")
    :   A Float specifying the connector acceleration component in the connector’s local
        4-direction.

    ar1State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBCState.py)[¶](#abaqus.BoundaryCondition.ConnAccelerationBCState.ConnAccelerationBCState.ar1State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the connector acceleration
        component in the connector’s local 4-direction. Possible values are UNSET, SET,
        UNCHANGED, FREED, and MODIFIED.

    ar2 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBCState.py#L28-L30)[¶](#abaqus.BoundaryCondition.ConnAccelerationBCState.ConnAccelerationBCState.ar2 "Permalink to this definition")
    :   A Float specifying the connector acceleration component in the connector’s local
        5-direction.

    ar2State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBCState.py)[¶](#abaqus.BoundaryCondition.ConnAccelerationBCState.ConnAccelerationBCState.ar2State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the connector acceleration
        component in the connector’s local 5-direction. Possible values are UNSET, SET,
        UNCHANGED, FREED, and MODIFIED.

    ar3 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBCState.py#L28-L30)[¶](#abaqus.BoundaryCondition.ConnAccelerationBCState.ConnAccelerationBCState.ar3 "Permalink to this definition")
    :   A Float specifying the connector acceleration component in the connector’s local
        6-direction.

    ar3State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBCState.py)[¶](#abaqus.BoundaryCondition.ConnAccelerationBCState.ConnAccelerationBCState.ar3State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the connector acceleration
        component in the connector’s local 6-direction. Possible values are UNSET, SET,
        UNCHANGED, FREED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnAccelerationBCState.py)[¶](#abaqus.BoundaryCondition.ConnAccelerationBCState.ConnAccelerationBCState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * PROPAGATED\_FROM\_BASE\_STATE
        * MODIFIED\_FROM\_BASE\_STATE
        * DEACTIVATED\_FROM\_BASE\_STATE
        * BUILT\_INTO\_MODES

*class* ConnDisplacementBC(*[name](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.__init__.name (Python parameter)")*, *[createStepName](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.__init__.createStepName (Python parameter)")*, *[region](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.__init__.region (Python parameter)")=`''`*, *[fastenerName](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.__init__.fastenerName (Python parameter)")=`''`*, *[fastenerSetName](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.__init__.fastenerSetName (Python parameter)")=`''`*, *[u1](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.__init__.u1 (Python parameter)")=`abaqusConstants.UNSET`*, *[u2](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.__init__.u2 (Python parameter)")=`abaqusConstants.UNSET`*, *[u3](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.__init__.u3 (Python parameter)")=`abaqusConstants.UNSET`*, *[ur1](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.__init__.ur1 (Python parameter)")=`abaqusConstants.UNSET`*, *[ur2](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.__init__.ur2 (Python parameter)")=`abaqusConstants.UNSET`*, *[ur3](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.__init__.ur3 (Python parameter)")=`abaqusConstants.UNSET`*, *[fixed](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.__init__.fixed (Python parameter)")=`0`*, *[amplitude](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[buckleCase](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.__init__.buckleCase (Python parameter)")=`abaqusConstants.NOT_APPLICABLE`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBC.py#L23-L308)[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC "Permalink to this definition")
:   Bases: [`BoundaryCondition`](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition "abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition (Python class)")

    The ConnDisplacementBC object stores the data for a connector displacement/rotation boundary condition.
    The ConnDisplacementBC object is derived from the BoundaryCondition object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name]
    ```

    Note

    Check [ConnDisplacementBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-conndisplacementbcpyc.htm?contextscope=all).

    Member Details:

    buckleCase : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'NOT_APPLICABLE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBC.py#L42-L45)[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.buckleCase "Permalink to this definition")
    :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
        analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
        PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

    category : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBC.py)[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.category "Permalink to this definition")
    :   A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBC.py#L47-L49)[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
        Possible values are UNIFORM and USER\_DEFINED. The default value is UNIFORM.

    fastenerName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBC.py#L51-L55)[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.fastenerName "Permalink to this definition")
    :   A String specifying the name of the assembled fastener to which the boundary condition
        will be applied. This argument is not valid when **region** is specified. When this
        argument is specified, **fastenerSetName** must also be specified. The default value is an
        empty string.

    fastenerSetName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBC.py#L57-L61)[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.fastenerSetName "Permalink to this definition")
    :   A String specifying the assembled fastener template model set to which the boundary
        condition will be applied. This argument is not valid when **region** is specified. When
        this argument is specified, **fastenerName** must also be specified. The default value is
        an empty string.

    fixed : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBC.py#L38-L40)[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.fixed "Permalink to this definition")
    :   A Boolean specifying whether the boundary condition should remain fixed at the current
        values at the start of the step. The default value is OFF.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBC.py#L70-L73)[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the boundary
        condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBC.py#L35-L36)[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.name "Permalink to this definition")
    :   A String specifying the boundary condition repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBC.py#L67-L68)[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.region "Permalink to this definition")
    :   A Region object specifying the region to which the boundary condition is applied.

    setValues(*[region](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.region "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.region (Python parameter) — The wire region to which the boundary condition is applied.")=`''`*, *[fastenerName](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.fastenerName "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.fastenerName (Python parameter) — A String specifying the name of the assembled fastener to which the boundary condition will be applied.")=`''`*, *[fastenerSetName](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.fastenerSetName "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.fastenerSetName (Python parameter) — A String specifying the assembled fastener template model set to which the boundary condition will be applied.")=`''`*, *[u1](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.u1 "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.u1 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the displacement component in the connector's local 1-direction.")=`abaqusConstants.UNSET`*, *[u2](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.u2 "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.u2 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the displacement component in the connector's local 2-direction.")=`abaqusConstants.UNSET`*, *[u3](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.u3 "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.u3 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the displacement component in the connector's local 3-direction.")=`abaqusConstants.UNSET`*, *[ur1](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.ur1 "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.ur1 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the rotational component in the connector's local 4-direction.")=`abaqusConstants.UNSET`*, *[ur2](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.ur2 "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.ur2 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the rotational component in the connector's local 5-direction.")=`abaqusConstants.UNSET`*, *[ur3](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.ur3 "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.ur3 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the rotational component in the connector's local 6-direction.")=`abaqusConstants.UNSET`*, *[fixed](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.fixed "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.fixed (Python parameter) — A Boolean specifying whether the boundary condition should remain fixed at the current values at the start of the step.")=`0`*, *[amplitude](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.amplitude "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.distributionType "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM and USER_DEFINED.")=`abaqusConstants.UNIFORM`*, *[buckleCase](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.buckleCase "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.buckleCase (Python parameter) — A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE analysis.")=`abaqusConstants.NOT_APPLICABLE`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBC.py#L171-L249)[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues "Permalink to this definition")
    :   This method modifies the data for an existing ConnDisplacementBC object in the step where it is
        created.

        Note

        Check [ConnDisplacementBC.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-conndisplacementbcpyc.htm?contextscope=all#simaker-conndisplacementbcsetvaluespyc).

        Parameters:[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues-parameters "Permalink to this headline")
        :   region=`''`[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.region "Permalink to this definition")
            :   The wire region to which the boundary condition is applied. This argument is not valid
                when **fastenerName** and **fastenerSetName** are specified.

            fastenerName=`''`[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.fastenerName "Permalink to this definition")
            :   A String specifying the name of the assembled fastener to which the boundary condition
                will be applied. This argument is not valid when **region** is specified. When this
                argument is specified, **fastenerSetName** must also be specified. The default value is an
                empty string.

            fastenerSetName=`''`[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.fastenerSetName "Permalink to this definition")
            :   A String specifying the assembled fastener template model set to which the boundary
                condition will be applied. This argument is not valid when **region** is specified. When
                this argument is specified, **fastenerName** must also be specified. The default value is
                an empty string.

            u1=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.u1 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
                connector’s local 1-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET. Note: Although **u1**, **u2**, **u3**, **ur1**, **ur2**, and **ur3**
                are optional arguments, at least one of them must be specified.

            u2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.u2 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
                connector’s local 2-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            u3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.u3 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
                connector’s local 3-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            ur1=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.ur1 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the rotational component in the
                connector’s local 4-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            ur2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.ur2 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the rotational component in the
                connector’s local 5-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            ur3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.ur3 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the rotational component in the
                connector’s local 6-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            fixed=`0`[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.fixed "Permalink to this definition")
            :   A Boolean specifying whether the boundary condition should remain fixed at the current
                values at the start of the step. The default value is OFF.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM and USER\_DEFINED. The default value is UNIFORM.

            buckleCase=`abaqusConstants.NOT_APPLICABLE`[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValues.buckleCase "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
                analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
                PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

    setValuesInStep(*[stepName](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.stepName "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition is modified.")*, *[u1](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.u1 "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.u1 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the displacement component in the connector's local 1-direction.")=`abaqusConstants.SET`*, *[u2](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.u2 "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.u2 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the displacement component in the connector's local 2-direction.")=`abaqusConstants.SET`*, *[u3](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.u3 "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.u3 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the displacement component in the connector's local 3-direction.")=`abaqusConstants.SET`*, *[ur1](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.ur1 "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.ur1 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the rotational component in the connector's local 4-direction.")=`abaqusConstants.SET`*, *[ur2](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.ur2 "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.ur2 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the rotational component in the connector's local 5-direction.")=`abaqusConstants.SET`*, *[ur3](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.ur3 "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.ur3 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the rotational component in the connector's local 6-direction.")=`abaqusConstants.SET`*, *[amplitude](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.amplitude "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*, *[buckleCase](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.buckleCase "abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.buckleCase (Python parameter) — A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE analysis.")=`abaqusConstants.NOT_APPLICABLE`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBC.py#L251-L308)[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing ConnDisplacementBC object in the specified
        step.

        Note

        Check [ConnDisplacementBC.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-conndisplacementbcpyc.htm?contextscope=all#simaker-conndisplacementbcsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is modified.

            u1=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.u1 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
                connector’s local 1-direction. Possible values for the SymbolicConstant are SET,
                UNCHANGED, and FREED.

            u2=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.u2 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
                connector’s local 2-direction. Possible values for the SymbolicConstant are SET,
                UNCHANGED, and FREED.

            u3=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.u3 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
                connector’s local 3-direction. Possible values for the SymbolicConstant are SET,
                UNCHANGED, and FREED.

            ur1=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.ur1 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the rotational component in the
                connector’s local 4-direction. Possible values for the SymbolicConstant are SET,
                UNCHANGED, and FREED.

            ur2=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.ur2 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the rotational component in the
                connector’s local 5-direction. Possible values for the SymbolicConstant are SET,
                UNCHANGED, and FREED.

            ur3=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.ur3 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the rotational component in the
                connector’s local 6-direction. Possible values for the SymbolicConstant are SET,
                UNCHANGED, and FREED.

            amplitude=`''`[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                boundary condition is changed to have no amplitude reference. You should provide the
                **amplitude** argument only if it is valid for the specified step.

            buckleCase=`abaqusConstants.NOT_APPLICABLE`[¶](#abaqus.BoundaryCondition.ConnDisplacementBC.ConnDisplacementBC.setValuesInStep.buckleCase "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
                analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
                PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

*class* ConnDisplacementBCState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBCState.py#L9-L104)[¶](#abaqus.BoundaryCondition.ConnDisplacementBCState.ConnDisplacementBCState "Permalink to this definition")
:   Bases: [`BoundaryConditionState`](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState "abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState (Python class)")

    The ConnDisplacementBCState object stores the propagating data for a connector displacement/rotation
    boundary condition in a step. One instance of this object is created internally by the ConnDisplacementBC
    object for each step. The instance is also deleted internally by the ConnDisplacementBC object. The
    ConnDisplacementBCState object has no constructor or methods. The ConnDisplacementBCState object is derived
    from the BoundaryConditionState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].boundaryConditionStates[name]
    ```

    The corresponding analysis keywords are:

    * CONNECTOR MOTION

    Note

    Check [ConnDisplacementBCState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-conndisplacementbcstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBCState.py#L9-L104)[¶](#abaqus.BoundaryCondition.ConnDisplacementBCState.ConnDisplacementBCState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the
        boundary condition has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBCState.py)[¶](#abaqus.BoundaryCondition.ConnDisplacementBCState.ConnDisplacementBCState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBCState.py)[¶](#abaqus.BoundaryCondition.ConnDisplacementBCState.ConnDisplacementBCState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * PROPAGATED\_FROM\_BASE\_STATE
        * MODIFIED\_FROM\_BASE\_STATE
        * DEACTIVATED\_FROM\_BASE\_STATE
        * BUILT\_INTO\_MODES

    u1 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBCState.py#L28-L30)[¶](#abaqus.BoundaryCondition.ConnDisplacementBCState.ConnDisplacementBCState.u1 "Permalink to this definition")
    :   A Float or a Complex specifying the displacement component in the connector’s local
        1-direction.

    u1State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBCState.py)[¶](#abaqus.BoundaryCondition.ConnDisplacementBCState.ConnDisplacementBCState.u1State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the displacement component in the
        connector’s local 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
        MODIFIED.

    u2 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBCState.py#L28-L30)[¶](#abaqus.BoundaryCondition.ConnDisplacementBCState.ConnDisplacementBCState.u2 "Permalink to this definition")
    :   A Float or a Complex specifying the displacement component in the connector’s local
        2-direction.

    u2State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBCState.py)[¶](#abaqus.BoundaryCondition.ConnDisplacementBCState.ConnDisplacementBCState.u2State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the displacement component in the
        connector’s local 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
        MODIFIED.

    u3 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBCState.py#L28-L30)[¶](#abaqus.BoundaryCondition.ConnDisplacementBCState.ConnDisplacementBCState.u3 "Permalink to this definition")
    :   A Float or a Complex specifying the displacement component in the connector’s local
        3-direction.

    u3State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBCState.py)[¶](#abaqus.BoundaryCondition.ConnDisplacementBCState.ConnDisplacementBCState.u3State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the displacement component in the
        connector’s local 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
        MODIFIED.

    ur1 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBCState.py#L40-L42)[¶](#abaqus.BoundaryCondition.ConnDisplacementBCState.ConnDisplacementBCState.ur1 "Permalink to this definition")
    :   A Float or a Complex specifying the rotational component in the connector’s local
        4-direction.

    ur1State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBCState.py)[¶](#abaqus.BoundaryCondition.ConnDisplacementBCState.ConnDisplacementBCState.ur1State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the rotational component in the
        connector’s local 4-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
        MODIFIED.

    ur2 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBCState.py#L40-L42)[¶](#abaqus.BoundaryCondition.ConnDisplacementBCState.ConnDisplacementBCState.ur2 "Permalink to this definition")
    :   A Float or a Complex specifying the rotational component in the connector’s local
        5-direction.

    ur2State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBCState.py)[¶](#abaqus.BoundaryCondition.ConnDisplacementBCState.ConnDisplacementBCState.ur2State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the rotational component in the
        connector’s local 5-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
        MODIFIED.

    ur3 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBCState.py#L40-L42)[¶](#abaqus.BoundaryCondition.ConnDisplacementBCState.ConnDisplacementBCState.ur3 "Permalink to this definition")
    :   A Float or a Complex specifying the rotational component in the connector’s local
        6-direction.

    ur3State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnDisplacementBCState.py)[¶](#abaqus.BoundaryCondition.ConnDisplacementBCState.ConnDisplacementBCState.ur3State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the rotational component in the
        connector’s local 6-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
        MODIFIED.

*class* ConnVelocityBC(*[name](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.__init__.name (Python parameter)")*, *[createStepName](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.__init__.createStepName (Python parameter)")*, *[region](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.__init__.region (Python parameter)")=`''`*, *[fastenerName](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.__init__.fastenerName (Python parameter)")=`''`*, *[fastenerSetName](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.__init__.fastenerSetName (Python parameter)")=`''`*, *[v1](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.__init__.v1 (Python parameter)")=`abaqusConstants.UNSET`*, *[v2](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.__init__.v2 (Python parameter)")=`abaqusConstants.UNSET`*, *[v3](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.__init__.v3 (Python parameter)")=`abaqusConstants.UNSET`*, *[vr1](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.__init__.vr1 (Python parameter)")=`abaqusConstants.UNSET`*, *[vr2](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.__init__.vr2 (Python parameter)")=`abaqusConstants.UNSET`*, *[vr3](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.__init__.vr3 (Python parameter)")=`abaqusConstants.UNSET`*, *[amplitude](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBC.py#L15-L258)[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC "Permalink to this definition")
:   Bases: [`BoundaryCondition`](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition "abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition (Python class)")

    The ConnVelocityBC object stores the data for a connector velocity boundary condition. The ConnVelocityBC
    object is derived from the BoundaryCondition object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name]
    ```

    Note

    Check [ConnVelocityBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connvelocitybcpyc.htm?contextscope=all).

    Member Details:

    category : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBC.py)[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.category "Permalink to this definition")
    :   A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBC.py#L30-L32)[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
        Possible values are UNIFORM and USER\_DEFINED. The default value is UNIFORM.

    fastenerName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBC.py#L34-L38)[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.fastenerName "Permalink to this definition")
    :   A String specifying the name of the assembled fastener to which the boundary condition
        will be applied. This argument is not valid when **region** is specified. When this
        argument is specified, **fastenerSetName** must also be specified. The default value is an
        empty string.

    fastenerSetName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBC.py#L40-L44)[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.fastenerSetName "Permalink to this definition")
    :   A String specifying the assembled fastener template model set to which the boundary
        condition will be applied. This argument is not valid when **region** is specified. When
        this argument is specified, **fastenerName** must also be specified. The default value is
        an empty string.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBC.py#L53-L56)[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the boundary
        condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBC.py#L27-L28)[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.name "Permalink to this definition")
    :   A String specifying the boundary condition repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBC.py#L50-L51)[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.region "Permalink to this definition")
    :   A Region object specifying the region to which the boundary condition is applied.

    setValues(*[region](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.region "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.region (Python parameter) — The wire region to which the boundary condition is applied.")=`''`*, *[fastenerName](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.fastenerName "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.fastenerName (Python parameter) — A String specifying the name of the assembled fastener to which the boundary condition will be applied.")=`''`*, *[fastenerSetName](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.fastenerSetName "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.fastenerSetName (Python parameter) — A String specifying the assembled fastener template model set to which the boundary condition will be applied.")=`''`*, *[v1](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.v1 "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.v1 (Python parameter) — A Float or a SymbolicConstant specifying the velocity component in the connector's local 1-direction.")=`abaqusConstants.UNSET`*, *[v2](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.v2 "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.v2 (Python parameter) — A Float or a SymbolicConstant specifying the velocity component in the connector's local 2-direction.")=`abaqusConstants.UNSET`*, *[v3](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.v3 "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.v3 (Python parameter) — A Float or a SymbolicConstant specifying the velocity component in the connector's local 3-direction.")=`abaqusConstants.UNSET`*, *[vr1](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.vr1 "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.vr1 (Python parameter) — A Float or a SymbolicConstant specifying the rotational velocity component in the connector's local 4-direction.")=`abaqusConstants.UNSET`*, *[vr2](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.vr2 "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.vr2 (Python parameter) — A Float or a SymbolicConstant specifying the rotational velocity component in the connector's local 5-direction.")=`abaqusConstants.UNSET`*, *[vr3](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.vr3 "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.vr3 (Python parameter) — A Float or a SymbolicConstant specifying the rotational velocity component in the connector's local 6-direction.")=`abaqusConstants.UNSET`*, *[amplitude](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.amplitude "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.distributionType "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM and USER_DEFINED.")=`abaqusConstants.UNIFORM`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBC.py#L143-L209)[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues "Permalink to this definition")
    :   This method modifies the data for an existing ConnVelocityBC object in the step where it is created.

        Note

        Check [ConnVelocityBC.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connvelocitybcpyc.htm?contextscope=all#simaker-connvelocitybcsetvaluespyc).

        Parameters:[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues-parameters "Permalink to this headline")
        :   region=`''`[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.region "Permalink to this definition")
            :   The wire region to which the boundary condition is applied. This argument is not valid
                when **fastenerName** and **fastenerSetName** are specified.

            fastenerName=`''`[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.fastenerName "Permalink to this definition")
            :   A String specifying the name of the assembled fastener to which the boundary condition
                will be applied. This argument is not valid when **region** is specified. When this
                argument is specified, **fastenerSetName** must also be specified. The default value is an
                empty string.

            fastenerSetName=`''`[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.fastenerSetName "Permalink to this definition")
            :   A String specifying the assembled fastener template model set to which the boundary
                condition will be applied. This argument is not valid when **region** is specified. When
                this argument is specified, **fastenerName** must also be specified. The default value is
                an empty string.

            v1=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.v1 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the velocity component in the connector’s local
                1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET. Note: Although **v1**, **v2**, **v3**, **vr1**, **vr2**, and **vr3** are optional
                arguments, at least one of them must be specified.

            v2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.v2 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the velocity component in the connector’s local
                2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET.

            v3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.v3 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the velocity component in the connector’s local
                3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET.

            vr1=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.vr1 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational velocity component in the
                connector’s local 4-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            vr2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.vr2 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational velocity component in the
                connector’s local 5-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            vr3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.vr3 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational velocity component in the
                connector’s local 6-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM and USER\_DEFINED. The default value is UNIFORM.

    setValuesInStep(*[stepName](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep.stepName "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition is modified.")*, *[v1](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep.v1 "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep.v1 (Python parameter) — A Float or a SymbolicConstant specifying the velocity component in the connector's local 1-direction.")=`abaqusConstants.SET`*, *[v2](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep.v2 "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep.v2 (Python parameter) — A Float or a SymbolicConstant specifying the velocity component in the connector's local 2-direction.")=`abaqusConstants.SET`*, *[v3](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep.v3 "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep.v3 (Python parameter) — A Float or a SymbolicConstant specifying the velocity component in the connector's local 3-direction.")=`abaqusConstants.SET`*, *[vr1](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep.vr1 "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep.vr1 (Python parameter) — A Float or a SymbolicConstant specifying the rotational velocity component in the connector's local 4-direction.")=`abaqusConstants.SET`*, *[vr2](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep.vr2 "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep.vr2 (Python parameter) — A Float or a SymbolicConstant specifying the rotational velocity component in the connector's local 5-direction.")=`abaqusConstants.SET`*, *[vr3](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep.vr3 "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep.vr3 (Python parameter) — A Float or a SymbolicConstant specifying the rotational velocity component in the connector's local 6-direction.")=`abaqusConstants.SET`*, *[amplitude](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep.amplitude "abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBC.py#L211-L258)[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing ConnVelocityBC object in the specified
        step.

        Note

        Check [ConnVelocityBC.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connvelocitybcpyc.htm?contextscope=all#simaker-connvelocitybcsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is modified.

            v1=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep.v1 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the velocity component in the connector’s local
                1-direction. Possible values for the SymbolicConstant are SET and FREED.

            v2=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep.v2 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the velocity component in the connector’s local
                2-direction. Possible values for the SymbolicConstant are SET and FREED.

            v3=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep.v3 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the velocity component in the connector’s local
                3-direction. Possible values for the SymbolicConstant are SET and FREED.

            vr1=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep.vr1 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational velocity component in the
                connector’s local 4-direction. Possible values for the SymbolicConstant are SET and
                FREED.

            vr2=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep.vr2 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational velocity component in the
                connector’s local 5-direction. Possible values for the SymbolicConstant are SET and
                FREED.

            vr3=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep.vr3 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational velocity component in the
                connector’s local 6-direction. Possible values for the SymbolicConstant are SET and
                FREED.

            amplitude=`''`[¶](#abaqus.BoundaryCondition.ConnVelocityBC.ConnVelocityBC.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                boundary condition is changed to have no amplitude reference. You should provide the
                **amplitude** argument only if it is valid for the specified step.

*class* ConnVelocityBCState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBCState.py#L9-L100)[¶](#abaqus.BoundaryCondition.ConnVelocityBCState.ConnVelocityBCState "Permalink to this definition")
:   Bases: [`BoundaryConditionState`](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState "abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState (Python class)")

    The ConnVelocityBCState object stores the propagating data for a velocity boundary condition in a step.
    One instance of this object is created internally by the ConnVelocityBC object for each step. The instance
    is also deleted internally by the ConnVelocityBC object. The ConnVelocityBCState object has no constructor
    or methods. The ConnVelocityBCState object is derived from the BoundaryConditionState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].boundaryConditionStates[name]
    ```

    The corresponding analysis keywords are:

    * CONNECTOR MOTION

    Note

    Check [ConnVelocityBCState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connvelocitybcstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBCState.py#L9-L100)[¶](#abaqus.BoundaryCondition.ConnVelocityBCState.ConnVelocityBCState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the
        boundary condition has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBCState.py)[¶](#abaqus.BoundaryCondition.ConnVelocityBCState.ConnVelocityBCState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBCState.py)[¶](#abaqus.BoundaryCondition.ConnVelocityBCState.ConnVelocityBCState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * PROPAGATED\_FROM\_BASE\_STATE
        * MODIFIED\_FROM\_BASE\_STATE
        * DEACTIVATED\_FROM\_BASE\_STATE
        * BUILT\_INTO\_MODES

    v1 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBCState.py#L27-L28)[¶](#abaqus.BoundaryCondition.ConnVelocityBCState.ConnVelocityBCState.v1 "Permalink to this definition")
    :   A Float specifying the velocity component in the connector’s local 1-direction.

    v1State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBCState.py)[¶](#abaqus.BoundaryCondition.ConnVelocityBCState.ConnVelocityBCState.v1State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the velocity component in the
        connector’s local 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
        MODIFIED.

    v2 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBCState.py#L30-L31)[¶](#abaqus.BoundaryCondition.ConnVelocityBCState.ConnVelocityBCState.v2 "Permalink to this definition")
    :   A Float specifying the velocity component in the connector’s local 2-direction.

    v2State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBCState.py)[¶](#abaqus.BoundaryCondition.ConnVelocityBCState.ConnVelocityBCState.v2State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the velocity component in the
        connector’s local 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
        MODIFIED.

    v3 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBCState.py#L33-L34)[¶](#abaqus.BoundaryCondition.ConnVelocityBCState.ConnVelocityBCState.v3 "Permalink to this definition")
    :   A Float specifying the velocity component in the connector’s local 3-direction.

    v3State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBCState.py)[¶](#abaqus.BoundaryCondition.ConnVelocityBCState.ConnVelocityBCState.v3State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the velocity component in the
        connector’s local 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
        MODIFIED.

    vr1 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBCState.py#L36-L38)[¶](#abaqus.BoundaryCondition.ConnVelocityBCState.ConnVelocityBCState.vr1 "Permalink to this definition")
    :   A Float specifying the rotational velocity component in the connector’s local
        4-direction.

    vr1State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBCState.py)[¶](#abaqus.BoundaryCondition.ConnVelocityBCState.ConnVelocityBCState.vr1State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the rotational velocity component
        in the connector’s local 4-direction. Possible values are UNSET, SET, UNCHANGED, FREED,
        and MODIFIED.

    vr2 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBCState.py#L36-L38)[¶](#abaqus.BoundaryCondition.ConnVelocityBCState.ConnVelocityBCState.vr2 "Permalink to this definition")
    :   A Float specifying the rotational velocity component in the connector’s local
        5-direction.

    vr2State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBCState.py)[¶](#abaqus.BoundaryCondition.ConnVelocityBCState.ConnVelocityBCState.vr2State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the rotational velocity component
        in the connector’s local 5-direction. Possible values are UNSET, SET, UNCHANGED, FREED,
        and MODIFIED.

    vr3 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBCState.py#L36-L38)[¶](#abaqus.BoundaryCondition.ConnVelocityBCState.ConnVelocityBCState.vr3 "Permalink to this definition")
    :   A Float specifying the rotational velocity component in the connector’s local
        6-direction.

    vr3State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ConnVelocityBCState.py)[¶](#abaqus.BoundaryCondition.ConnVelocityBCState.ConnVelocityBCState.vr3State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the rotational velocity component
        in the connector’s local 6-direction. Possible values are UNSET, SET, UNCHANGED, FREED,
        and MODIFIED.

*class* DisplacementBC(*[name](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.__init__.name (Python parameter)")*, *[createStepName](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.__init__.createStepName (Python parameter)")*, *[region](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.__init__.region (Python parameter)")*, *[fieldName](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.__init__.fieldName (Python parameter)")=`''`*, *[u1](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.__init__.u1 (Python parameter)")=`abaqusConstants.UNSET`*, *[u2](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.__init__.u2 (Python parameter)")=`abaqusConstants.UNSET`*, *[u3](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.__init__.u3 (Python parameter)")=`abaqusConstants.UNSET`*, *[ur1](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.__init__.ur1 (Python parameter)")=`abaqusConstants.UNSET`*, *[ur2](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.__init__.ur2 (Python parameter)")=`abaqusConstants.UNSET`*, *[ur3](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.__init__.ur3 (Python parameter)")=`abaqusConstants.UNSET`*, *[fixed](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.__init__.fixed (Python parameter)")=`0`*, *[amplitude](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[localCsys](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.__init__.localCsys (Python parameter)")=`None`*, *[buckleCase](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.__init__.buckleCase (Python parameter)")=`abaqusConstants.NOT_APPLICABLE`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBC.py#L23-L293)[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC "Permalink to this definition")
:   Bases: [`BoundaryCondition`](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition "abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition (Python class)")

    The DisplacementBC object stores the data for a displacement/rotation boundary condition. The
    DisplacementBC object is derived from the BoundaryCondition object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name]
    ```

    Note

    Check [DisplacementBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displacementbcpyc.htm?contextscope=all).

    Member Details:

    buckleCase : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'NOT_APPLICABLE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBC.py#L47-L50)[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.buckleCase "Permalink to this definition")
    :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
        analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
        PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

    category : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBC.py)[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.category "Permalink to this definition")
    :   A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBC.py#L38-L41)[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
        Possible values are UNIFORM, USER\_DEFINED, FIELD, and DISCRETE\_FIELD. The default value
        is UNIFORM.

    fieldName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBC.py#L52-L56)[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.fieldName "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField or DiscreteField object associated
        with this boundary condition. The **fieldName** argument applies only when
        **distributionType** = FIELD or **distributionType** = DISCRETE\_FIELD. The default value is an
        empty string.

    fixed : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBC.py#L43-L45)[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.fixed "Permalink to this definition")
    :   A Boolean specifying whether the boundary condition should remain fixed at the current
        values at the start of the step. The default value is OFF.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBC.py#L65-L68)[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the boundary
        condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBC.py#L35-L36)[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.name "Permalink to this definition")
    :   A String specifying the boundary condition repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBC.py#L62-L63)[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.region "Permalink to this definition")
    :   A Region object specifying the region to which the boundary condition is applied.

    setValues(*[fieldName](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.fieldName "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.fieldName (Python parameter) — A String specifying the name of the AnalyticalField or DiscreteField object associated with this boundary condition.")=`''`*, *[u1](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.u1 "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.u1 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the displacement component in the 1-direction.")=`abaqusConstants.UNSET`*, *[u2](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.u2 "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.u2 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the displacement component in the 2-direction.")=`abaqusConstants.UNSET`*, *[u3](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.u3 "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.u3 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the displacement component in the 3-direction.")=`abaqusConstants.UNSET`*, *[ur1](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.ur1 "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.ur1 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the rotational displacement component about the 1-direction.")=`abaqusConstants.UNSET`*, *[ur2](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.ur2 "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.ur2 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the rotational displacement component about the 2-direction.")=`abaqusConstants.UNSET`*, *[ur3](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.ur3 "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.ur3 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the rotational displacement component about the 3-direction.")=`abaqusConstants.UNSET`*, *[fixed](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.fixed "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.fixed (Python parameter) — A Boolean specifying whether the boundary condition should remain fixed at the current values at the start of the step.")=`0`*, *[amplitude](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.amplitude "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.distributionType "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM, USER_DEFINED, FIELD, and DISCRETE_FIELD.")=`abaqusConstants.UNIFORM`*, *[localCsys](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.localCsys "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*, *[buckleCase](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.buckleCase "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.buckleCase (Python parameter) — A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE analysis.")=`abaqusConstants.NOT_APPLICABLE`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBC.py#L164-L237)[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues "Permalink to this definition")
    :   This method modifies the data for an existing DisplacementBC object in the step where it is created.

        Note

        Check [DisplacementBC.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displacementbcpyc.htm?contextscope=all#simaker-displacementbcsetvaluespyc).

        Parameters:[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues-parameters "Permalink to this headline")
        :   fieldName=`''`[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.fieldName "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField or DiscreteField object associated
                with this boundary condition. The **fieldName** argument applies only when
                **distributionType** = FIELD or **distributionType** = DISCRETE\_FIELD. The default value is an
                empty string.

            u1=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.u1 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
                1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET. Note: Although **u1**, **u2**, **u3**, **ur1**, **ur2**, and **ur3** are optional
                arguments, at least one of them must be specified.

            u2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.u2 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
                2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET.

            u3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.u3 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
                3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET.

            ur1=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.ur1 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the rotational displacement
                component about the 1-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            ur2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.ur2 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the rotational displacement
                component about the 2-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            ur3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.ur3 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the rotational displacement
                component about the 3-direction. Possible values for the SymbolicConstant are UNSET and
                SET. The default value is UNSET.

            fixed=`0`[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.fixed "Permalink to this definition")
            :   A Boolean specifying whether the boundary condition should remain fixed at the current
                values at the start of the step. The default value is OFF.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM, USER\_DEFINED, FIELD, and DISCRETE\_FIELD. The default value
                is UNIFORM.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

            buckleCase=`abaqusConstants.NOT_APPLICABLE`[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValues.buckleCase "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
                analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
                PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

    setValuesInStep(*[stepName](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.stepName "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition is modified.")*, *[u1](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.u1 "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.u1 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the displacement component in the 1-direction.")=`abaqusConstants.SET`*, *[u2](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.u2 "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.u2 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the displacement component in the 2-direction.")=`abaqusConstants.SET`*, *[u3](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.u3 "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.u3 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the displacement component in the 3-direction.")=`abaqusConstants.SET`*, *[ur1](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.ur1 "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.ur1 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the rotational displacement component about the 1-direction.")=`abaqusConstants.SET`*, *[ur2](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.ur2 "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.ur2 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the rotational displacement component about the 2-direction.")=`abaqusConstants.SET`*, *[ur3](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.ur3 "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.ur3 (Python parameter) — A Float, a Complex, or a SymbolicConstant specifying the rotational displacement component about the 3-direction.")=`abaqusConstants.SET`*, *[amplitude](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.amplitude "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*, *[buckleCase](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.buckleCase "abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.buckleCase (Python parameter) — A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE analysis.")=`abaqusConstants.NOT_APPLICABLE`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBC.py#L239-L293)[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing DisplacementBC object in the specified
        step.

        Note

        Check [DisplacementBC.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displacementbcpyc.htm?contextscope=all#simaker-displacementbcsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is modified.

            u1=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.u1 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
                1-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.

            u2=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.u2 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
                2-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.

            u3=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.u3 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the displacement component in the
                3-direction. Possible values for the SymbolicConstant are SET, UNCHANGED, and FREED.

            ur1=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.ur1 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the rotational displacement
                component about the 1-direction. Possible values for the SymbolicConstant are SET,
                UNCHANGED, and FREED.

            ur2=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.ur2 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the rotational displacement
                component about the 2-direction. Possible values for the SymbolicConstant are SET,
                UNCHANGED, and FREED.

            ur3=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.ur3 "Permalink to this definition")
            :   A Float, a Complex, or a SymbolicConstant specifying the rotational displacement
                component about the 3-direction. Possible values for the SymbolicConstant are SET,
                UNCHANGED, and FREED.

            amplitude=`''`[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                boundary condition is changed to have no amplitude reference. You should provide the
                **amplitude** argument only if it is valid for the specified step.

            buckleCase=`abaqusConstants.NOT_APPLICABLE`[¶](#abaqus.BoundaryCondition.DisplacementBC.DisplacementBC.setValuesInStep.buckleCase "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
                analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
                PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

*class* DisplacementBCState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBCState.py#L9-L97)[¶](#abaqus.BoundaryCondition.DisplacementBCState.DisplacementBCState "Permalink to this definition")
:   Bases: [`BoundaryConditionState`](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState "abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState (Python class)")

    The DisplacementBCState object stores the propagating data for a displacement/rotation boundary condition
    in a step. One instance of this object is created internally by the DisplacementBC object for each step. The
    instance is also deleted internally by the DisplacementBC object. The DisplacementBCState object has no
    constructor or methods. The DisplacementBCState object is derived from the BoundaryConditionState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].boundaryConditionStates[name]
    ```

    The corresponding analysis keywords are:

    * BOUNDARY

    Note

    Check [DisplacementBCState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displacementbcstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBCState.py#L9-L97)[¶](#abaqus.BoundaryCondition.DisplacementBCState.DisplacementBCState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the
        boundary condition has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBCState.py)[¶](#abaqus.BoundaryCondition.DisplacementBCState.DisplacementBCState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBCState.py)[¶](#abaqus.BoundaryCondition.DisplacementBCState.DisplacementBCState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * PROPAGATED\_FROM\_BASE\_STATE
        * MODIFIED\_FROM\_BASE\_STATE
        * DEACTIVATED\_FROM\_BASE\_STATE
        * BUILT\_INTO\_MODES

    u1 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBCState.py#L27-L28)[¶](#abaqus.BoundaryCondition.DisplacementBCState.DisplacementBCState.u1 "Permalink to this definition")
    :   A Float or a Complex specifying the displacement component in the 1-direction.

    u1State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBCState.py)[¶](#abaqus.BoundaryCondition.DisplacementBCState.DisplacementBCState.u1State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the displacement component in the
        1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    u2 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBCState.py#L30-L31)[¶](#abaqus.BoundaryCondition.DisplacementBCState.DisplacementBCState.u2 "Permalink to this definition")
    :   A Float or a Complex specifying the displacement component in the 2-direction.

    u2State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBCState.py)[¶](#abaqus.BoundaryCondition.DisplacementBCState.DisplacementBCState.u2State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the displacement component in the
        2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    u3 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBCState.py#L33-L34)[¶](#abaqus.BoundaryCondition.DisplacementBCState.DisplacementBCState.u3 "Permalink to this definition")
    :   A Float or a Complex specifying the displacement component in the 3-direction.

    u3State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBCState.py)[¶](#abaqus.BoundaryCondition.DisplacementBCState.DisplacementBCState.u3State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the displacement component in the
        3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    ur1 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBCState.py#L36-L38)[¶](#abaqus.BoundaryCondition.DisplacementBCState.DisplacementBCState.ur1 "Permalink to this definition")
    :   A Float or a Complex specifying the rotational displacement component about the
        1-direction.

    ur1State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBCState.py)[¶](#abaqus.BoundaryCondition.DisplacementBCState.DisplacementBCState.ur1State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the rotational displacement
        component about the 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
        MODIFIED.

    ur2 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBCState.py#L36-L38)[¶](#abaqus.BoundaryCondition.DisplacementBCState.DisplacementBCState.ur2 "Permalink to this definition")
    :   A Float or a Complex specifying the rotational displacement component about the
        2-direction.

    ur2State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBCState.py)[¶](#abaqus.BoundaryCondition.DisplacementBCState.DisplacementBCState.ur2State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the rotational displacement
        component about the 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
        MODIFIED.

    ur3 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBCState.py#L36-L38)[¶](#abaqus.BoundaryCondition.DisplacementBCState.DisplacementBCState.ur3 "Permalink to this definition")
    :   A Float or a Complex specifying the rotational displacement component about the
        3-direction.

    ur3State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBCState.py)[¶](#abaqus.BoundaryCondition.DisplacementBCState.DisplacementBCState.ur3State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the rotational displacement
        component about the 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and
        MODIFIED.

*class* DisplacementBaseMotionBC(*[name](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC "abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.__init__.name (Python parameter)")*, *[createStepName](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC "abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.__init__.createStepName (Python parameter)")*, *[dof](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC "abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.__init__.dof (Python parameter)")*, *[amplitudeScaleFactor](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC "abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.__init__.amplitudeScaleFactor (Python parameter)")=`1`*, *[centerOfRotation](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC "abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.__init__.centerOfRotation (Python parameter)")=`()`*, *[correlation](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC "abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.__init__.correlation (Python parameter)")=`None`*, *[secondaryBase](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC "abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.__init__.secondaryBase (Python parameter)")=`''`*, *[useComplex](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC "abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.__init__.useComplex (Python parameter)")=`0`*, *[amplitude](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC "abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBaseMotionBC.py#L14-L166)[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC "Permalink to this definition")
:   Bases: [`BoundaryCondition`](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition "abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition (Python class)")

    The DisplacementBaseMotionBC object stores the data for a displacement base motion boundary condition.
    The DisplacementBaseMotionBC object is derived from the BoundaryCondition object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name]
    ```

    Note

    Check [DisplacementBaseMotionBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displacementbasemotionbcpyc.htm?contextscope=all).

    Member Details:

    amplitudeScaleFactor : --is-rst--:py:class:`float` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBaseMotionBC.py#L29-L30)[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.amplitudeScaleFactor "Permalink to this definition")
    :   A Float specifying the scale factor for the amplitude curve. The default value is 1.0.

    category : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBaseMotionBC.py)[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.category "Permalink to this definition")
    :   A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.

    centerOfRotation : --is-rst--:py:class:`tuple` = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBaseMotionBC.py#L36-L38)[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.centerOfRotation "Permalink to this definition")
    :   A ModelDot object specifying a tuple containing one center of rotation. The default
        value is the global origin. This argument applies only when **dof** = UR1, UR2, or UR3.

    correlation : --is-rst--:py:class:`~abaqus.Amplitude.Correlation.Correlation` = `<abaqus.Amplitude.Correlation.Correlation object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBaseMotionBC.py#L40-L41)[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.correlation "Permalink to this definition")
    :   A Correlation object.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBaseMotionBC.py#L54-L57)[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the boundary
        condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBaseMotionBC.py#L26-L27)[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.name "Permalink to this definition")
    :   A String specifying the boundary condition repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBaseMotionBC.py#L51-L52)[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.region "Permalink to this definition")
    :   A Region object specifying the region to which the boundary condition is applied.

    secondaryBase : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBaseMotionBC.py#L43-L45)[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.secondaryBase "Permalink to this definition")
    :   A String specifying the name of the SecondaryBaseBC object associated with this boundary
        condition. The default value is an empty string.

    setValues(*[amplitudeScaleFactor](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValues.amplitudeScaleFactor "abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValues.amplitudeScaleFactor (Python parameter) — A Float specifying the scale factor for the amplitude curve.")=`1`*, *[centerOfRotation](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValues.centerOfRotation "abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValues.centerOfRotation (Python parameter) — A ModelDot object specifying a tuple containing one center of rotation.")=`()`*, *[correlation](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValues.correlation "abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValues.correlation (Python parameter) — A Correlation object.")=`None`*, *[secondaryBase](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValues.secondaryBase "abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValues.secondaryBase (Python parameter) — A String specifying the name of the SecondaryBaseBC object associated with this boundary condition.")=`''`*, *[useComplex](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValues.useComplex "abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValues.useComplex (Python parameter) — A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base motion record given by amplitude definition.")=`0`*, *[amplitude](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValues.amplitude "abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBaseMotionBC.py#L114-L148)[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValues "Permalink to this definition")
    :   This method modifies the data for an existing DisplacementBaseMotionBC object in the step where it is
        created.

        Note

        Check [DisplacementBaseMotionBC.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displacementbasemotionbcpyc.htm?contextscope=all#simaker-displacementbasemotionbcsetvaluespyc).

        Parameters:[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValues-parameters "Permalink to this headline")
        :   amplitudeScaleFactor=`1`[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValues.amplitudeScaleFactor "Permalink to this definition")
            :   A Float specifying the scale factor for the amplitude curve. The default value is 1.0.

            centerOfRotation=`()`[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValues.centerOfRotation "Permalink to this definition")
            :   A ModelDot object specifying a tuple containing one center of rotation. The default
                value is the global origin. This argument applies only when **dof** = UR1, UR2, or UR3.

            correlation=`None`[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValues.correlation "Permalink to this definition")
            :   A Correlation object.

            secondaryBase=`''`[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValues.secondaryBase "Permalink to this definition")
            :   A String specifying the name of the SecondaryBaseBC object associated with this boundary
                condition. The default value is an empty string.

            useComplex=`0`[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValues.useComplex "Permalink to this definition")
            :   A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base
                motion record given by amplitude definition. The default value is OFF.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

    setValuesInStep(*[stepName](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValuesInStep.stepName "abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition is modified.")*, *[amplitude](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValuesInStep.amplitude "abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBaseMotionBC.py#L150-L166)[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing DisplacementBaseMotionBC object in the
        specified step.

        Note

        Check [DisplacementBaseMotionBC.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displacementbasemotionbcpyc.htm?contextscope=all#simaker-displacementbasemotionbcsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is modified.

            amplitude=`''`[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                boundary condition is changed to have no amplitude reference. You should provide the
                **amplitude** argument only if it is valid for the specified step.

    useComplex : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBaseMotionBC.py#L32-L34)[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBC.DisplacementBaseMotionBC.useComplex "Permalink to this definition")
    :   A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base
        motion record given by amplitude definition. The default value is OFF.

*class* DisplacementBaseMotionBCState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBaseMotionBCState.py#L9-L50)[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBCState.DisplacementBaseMotionBCState "Permalink to this definition")
:   Bases: [`BoundaryConditionState`](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState "abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState (Python class)")

    The DisplacementBaseMotionBCState object stores the propagating data for a velocity base motion boundary
    condition in a step. One instance of this object is created internally by the DisplacementBaseMotionBC
    object for each step. The instance is also deleted internally by the DisplacementBaseMotionBC object. The
    DisplacementBaseMotionBCState object has no constructor or methods. The DisplacementBaseMotionBCState object
    is derived from the BoundaryConditionState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].boundaryConditionStates[name]
    ```

    The corresponding analysis keywords are:

    * BASE MOTION

    Note

    Check [DisplacementBaseMotionBCState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-displacementbasemotionbcstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBaseMotionBCState.py#L9-L50)[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBCState.DisplacementBaseMotionBCState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the
        boundary condition has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBaseMotionBCState.py)[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBCState.DisplacementBaseMotionBCState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/DisplacementBaseMotionBCState.py)[¶](#abaqus.BoundaryCondition.DisplacementBaseMotionBCState.DisplacementBaseMotionBCState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * PROPAGATED\_FROM\_BASE\_STATE
        * MODIFIED\_FROM\_BASE\_STATE
        * DEACTIVATED\_FROM\_BASE\_STATE
        * BUILT\_INTO\_MODES

*class* ElectricPotentialBC(*[name](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC "abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.__init__.name (Python parameter)")*, *[createStepName](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC "abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.__init__.createStepName (Python parameter)")*, *[region](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC "abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.__init__.region (Python parameter)")*, *[fieldName](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC "abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.__init__.fieldName (Python parameter)")=`''`*, *[magnitude](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC "abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.__init__.magnitude (Python parameter)")=`0`*, *[distributionType](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC "abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC "abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[fixed](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC "abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.__init__.fixed (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ElectricPotentialBC.py#L22-L169)[¶](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC "Permalink to this definition")
:   Bases: [`BoundaryCondition`](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition "abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition (Python class)")

    The ElectricPotentialBC object stores the data for an electrical potential boundary condition. The
    ElectricPotentialBC object is derived from the BoundaryCondition object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name]
    ```

    Note

    Check [ElectricPotentialBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-electricpotentialbcpyc.htm?contextscope=all).

    Member Details:

    category : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ElectricPotentialBC.py)[¶](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.category "Permalink to this definition")
    :   A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ElectricPotentialBC.py#L37-L39)[¶](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
        Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

    fieldName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ElectricPotentialBC.py#L41-L44)[¶](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.fieldName "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this boundary
        condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
        default value is an empty string.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ElectricPotentialBC.py#L53-L56)[¶](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the boundary
        condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ElectricPotentialBC.py#L34-L35)[¶](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.name "Permalink to this definition")
    :   A String specifying the boundary condition repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ElectricPotentialBC.py#L50-L51)[¶](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.region "Permalink to this definition")
    :   A Region object specifying the region to which the boundary condition is applied.

    setValues(*[fieldName](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValues.fieldName "abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValues.fieldName (Python parameter) — A String specifying the name of the AnalyticalField object associated with this boundary condition.")=`''`*, *[magnitude](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValues.magnitude "abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValues.magnitude (Python parameter) — A Float specifying the electrical potential magnitude.")=`0`*, *[distributionType](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValues.distributionType "abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD.")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValues.amplitude "abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[fixed](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValues.fixed "abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValues.fixed (Python parameter) — A Boolean specifying whether the boundary condition should remain fixed at the current values at the start of the step.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ElectricPotentialBC.py#L111-L144)[¶](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValues "Permalink to this definition")
    :   This method modifies the data for an existing ElectricPotentialBC object in the step where it is
        created.

        Note

        Check [ElectricPotentialBC.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-electricpotentialbcpyc.htm?contextscope=all#simaker-electricpotentialbcsetvaluespyc).

        Parameters:[¶](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValues-parameters "Permalink to this headline")
        :   fieldName=`''`[¶](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValues.fieldName "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this boundary
                condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
                default value is an empty string.

            magnitude=`0`[¶](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValues.magnitude "Permalink to this definition")
            :   A Float specifying the electrical potential magnitude. The default value is 0. The
                **magnitude** argument is optional if **distributionType** = USER\_DEFINED.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            fixed=`0`[¶](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValues.fixed "Permalink to this definition")
            :   A Boolean specifying whether the boundary condition should remain fixed at the current
                values at the start of the step. The default value is OFF.

    setValuesInStep(*[stepName](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValuesInStep.stepName "abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition is modified.")*, *[magnitude](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValuesInStep.magnitude "abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValuesInStep.magnitude (Python parameter) — A Float or the SymbolicConstant FREED specifying the electrical potential magnitude.")=`abaqusConstants.UNCHANGED`*, *[amplitude](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValuesInStep.amplitude "abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ElectricPotentialBC.py#L146-L169)[¶](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing ElectricPotentialBC object in the specified
        step.

        Note

        Check [ElectricPotentialBC.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-electricpotentialbcpyc.htm?contextscope=all#simaker-electricpotentialbcsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is modified.

            magnitude=`abaqusConstants.UNCHANGED`[¶](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float or the SymbolicConstant FREED specifying the electrical potential magnitude.

            amplitude=`''`[¶](#abaqus.BoundaryCondition.ElectricPotentialBC.ElectricPotentialBC.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                boundary condition is changed to have no amplitude reference. You should provide the
                **amplitude** argument only if it is valid for the specified step.

*class* ElectricPotentialBCState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ElectricPotentialBCState.py#L9-L57)[¶](#abaqus.BoundaryCondition.ElectricPotentialBCState.ElectricPotentialBCState "Permalink to this definition")
:   Bases: [`BoundaryConditionState`](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState "abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState (Python class)")

    The ElectricPotentialBCState object stores the propagating data for a electrical potential boundary
    condition in a step. One instance of this object is created internally by the ElectricPotentialBC object for
    each step. The instance is also deleted internally by the ElectricPotentialBC object. The
    ElectricPotentialBCState object has no constructor or methods. The ElectricPotentialBCState object is
    derived from the BoundaryConditionState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].boundaryConditionStates[name]
    ```

    The corresponding analysis keywords are:

    * BOUNDARY

    Note

    Check [ElectricPotentialBCState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-electricpotentialbcstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ElectricPotentialBCState.py#L9-L57)[¶](#abaqus.BoundaryCondition.ElectricPotentialBCState.ElectricPotentialBCState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the
        boundary condition has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ElectricPotentialBCState.py)[¶](#abaqus.BoundaryCondition.ElectricPotentialBCState.ElectricPotentialBCState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ElectricPotentialBCState.py#L28-L29)[¶](#abaqus.BoundaryCondition.ElectricPotentialBCState.ElectricPotentialBCState.magnitude "Permalink to this definition")
    :   A Float specifying the electrical potential magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ElectricPotentialBCState.py)[¶](#abaqus.BoundaryCondition.ElectricPotentialBCState.ElectricPotentialBCState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the electrical potential
        magnitude. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/ElectricPotentialBCState.py)[¶](#abaqus.BoundaryCondition.ElectricPotentialBCState.ElectricPotentialBCState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * PROPAGATED\_FROM\_BASE\_STATE
        * MODIFIED\_FROM\_BASE\_STATE
        * DEACTIVATED\_FROM\_BASE\_STATE
        * BUILT\_INTO\_MODES

*class* EulerianBC(*[name](#abaqus.BoundaryCondition.EulerianBC.EulerianBC "abaqus.BoundaryCondition.EulerianBC.EulerianBC.__init__.name (Python parameter)")*, *[createStepName](#abaqus.BoundaryCondition.EulerianBC.EulerianBC "abaqus.BoundaryCondition.EulerianBC.EulerianBC.__init__.createStepName (Python parameter)")*, *[region](#abaqus.BoundaryCondition.EulerianBC.EulerianBC "abaqus.BoundaryCondition.EulerianBC.EulerianBC.__init__.region (Python parameter)")*, *[definition](#abaqus.BoundaryCondition.EulerianBC.EulerianBC "abaqus.BoundaryCondition.EulerianBC.EulerianBC.__init__.definition (Python parameter)")=`abaqusConstants.INFLOW`*, *[inflowType](#abaqus.BoundaryCondition.EulerianBC.EulerianBC "abaqus.BoundaryCondition.EulerianBC.EulerianBC.__init__.inflowType (Python parameter)")=`abaqusConstants.FREE`*, *[outflowType](#abaqus.BoundaryCondition.EulerianBC.EulerianBC "abaqus.BoundaryCondition.EulerianBC.EulerianBC.__init__.outflowType (Python parameter)")=`abaqusConstants.ZERO_PRESSURE`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianBC.py#L18-L153)[¶](#abaqus.BoundaryCondition.EulerianBC.EulerianBC "Permalink to this definition")
:   Bases: [`BoundaryCondition`](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition "abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition (Python class)")

    The EulerianBC object stores the data for an Eulerian boundary condition. The EulerianBC object is
    derived from the BoundaryCondition object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name]
    ```

    Note

    Check [EulerianBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-eulerianbcpyc.htm?contextscope=all).

    Member Details:

    category : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianBC.py)[¶](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.category "Permalink to this definition")
    :   A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.

    definition : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'INFLOW'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianBC.py#L33-L35)[¶](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.definition "Permalink to this definition")
    :   A SymbolicConstant specifying the flow conditions to be defined. Possible values are
        INFLOW, OUTFLOW, and BOTH. The default value is INFLOW.

    inflowType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FREE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianBC.py#L37-L39)[¶](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.inflowType "Permalink to this definition")
    :   A SymbolicConstant specifying the control of material flow into the Eulerian domain.
        Possible values are FREE, NONE, and VOID. The default value is FREE.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianBC.py#L53-L56)[¶](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the boundary
        condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianBC.py#L30-L31)[¶](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.name "Permalink to this definition")
    :   A String specifying the boundary condition repository key.

    outflowType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'ZERO_PRESSURE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianBC.py#L41-L44)[¶](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.outflowType "Permalink to this definition")
    :   A SymbolicConstant specifying the control of flow of material out of the Eulerian
        domain. Possible values are ZERO\_PRESSURE, FREE, NON\_REFLECTING, and EQUILIBRIUM. The
        default value is ZERO\_PRESSURE.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianBC.py#L50-L51)[¶](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.region "Permalink to this definition")
    :   A Region object specifying the region to which the boundary condition is applied.

    setValues(*[region](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValues.region "abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValues.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[definition](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValues.definition "abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValues.definition (Python parameter) — A SymbolicConstant specifying the material flow conditions to be defined.")=`abaqusConstants.INFLOW`*, *[inflowType](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValues.inflowType "abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValues.inflowType (Python parameter) — A SymbolicConstant specifying the control of material flow into the Eulerian domain. Possible values are FREE, NONE, and VOID.")=`abaqusConstants.FREE`*, *[outflowType](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValues.outflowType "abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValues.outflowType (Python parameter) — A SymbolicConstant specifying the control of material flow out of the Eulerian domain. Possible values are ZERO_PRESSURE, FREE, NON_REFLECTING, and EQUILIBRIUM.")=`abaqusConstants.ZERO_PRESSURE`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianBC.py#L101-L126)[¶](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValues "Permalink to this definition")
    :   This method modifies the data for an existing EulerianBC object in the step where it is created.

        Note

        Check [EulerianBC.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-eulerianbcpyc.htm?contextscope=all#simaker-eulerianbcsetvaluespyc).

        Parameters:[¶](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValues-parameters "Permalink to this headline")
        :   region[¶](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValues.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            definition=`abaqusConstants.INFLOW`[¶](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValues.definition "Permalink to this definition")
            :   A SymbolicConstant specifying the material flow conditions to be defined. Possible
                values are INFLOW, OUTFLOW, and BOTH. The default value is INFLOW.

            inflowType=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValues.inflowType "Permalink to this definition")
            :   A SymbolicConstant specifying the control of material flow into the Eulerian domain.
                Possible values are FREE, NONE, and VOID. The default value is FREE.

            outflowType=`abaqusConstants.ZERO_PRESSURE`[¶](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValues.outflowType "Permalink to this definition")
            :   A SymbolicConstant specifying the control of material flow out of the Eulerian domain.
                Possible values are ZERO\_PRESSURE, FREE, NON\_REFLECTING, and EQUILIBRIUM. The default
                value is ZERO\_PRESSURE.

    setValuesInStep(*[stepName](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValuesInStep.stepName "abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition is modified.")*, *[definition](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValuesInStep.definition "abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValuesInStep.definition (Python parameter) — A SymbolicConstant specifying the material flow conditions to be defined.")=`abaqusConstants.INFLOW`*, *[inflowType](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValuesInStep.inflowType "abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValuesInStep.inflowType (Python parameter) — A SymbolicConstant specifying the control of material flow into the Eulerian domain. Possible values are FREE, NONE, and VOID.")=`abaqusConstants.FREE`*, *[outflowType](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValuesInStep.outflowType "abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValuesInStep.outflowType (Python parameter) — A SymbolicConstant specifying the control of material flow out of the Eulerian domain. Possible values are ZERO_PRESSURE, FREE, NON_REFLECTING, and EQUILIBRIUM.")=`abaqusConstants.ZERO_PRESSURE`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianBC.py#L128-L153)[¶](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing EulerianBC object in the specified step.

        Note

        Check [EulerianBC.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-eulerianbcpyc.htm?contextscope=all#simaker-eulerianbcsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is modified.

            definition=`abaqusConstants.INFLOW`[¶](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValuesInStep.definition "Permalink to this definition")
            :   A SymbolicConstant specifying the material flow conditions to be defined. Possible
                values are INFLOW, OUTFLOW, and BOTH. The default value is INFLOW.

            inflowType=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValuesInStep.inflowType "Permalink to this definition")
            :   A SymbolicConstant specifying the control of material flow into the Eulerian domain.
                Possible values are FREE, NONE, and VOID. The default value is FREE.

            outflowType=`abaqusConstants.ZERO_PRESSURE`[¶](#abaqus.BoundaryCondition.EulerianBC.EulerianBC.setValuesInStep.outflowType "Permalink to this definition")
            :   A SymbolicConstant specifying the control of material flow out of the Eulerian domain.
                Possible values are ZERO\_PRESSURE, FREE, NON\_REFLECTING, and EQUILIBRIUM. The default
                value is ZERO\_PRESSURE.

*class* EulerianBCState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianBCState.py#L14-L79)[¶](#abaqus.BoundaryCondition.EulerianBCState.EulerianBCState "Permalink to this definition")
:   Bases: [`BoundaryConditionState`](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState "abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState (Python class)")

    The EulerianBCState object stores the propagating data for an Eulerian boundary condition in a step. One
    instance of this object is created internally by the EulerianBC object for each step. The instance is also
    deleted internally by the EulerianBC object. The EulerianBCState object has no constructor or methods. The
    EulerianBCState object is derived from the BoundaryConditionState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].boundaryConditionStates[name]
    ```

    The corresponding analysis keywords are:

    * EULERIAN BOUNDARY

    Note

    Check [EulerianBCState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-eulerianbcstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianBCState.py#L14-L79)[¶](#abaqus.BoundaryCondition.EulerianBCState.EulerianBCState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the
        boundary condition has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianBCState.py)[¶](#abaqus.BoundaryCondition.EulerianBCState.EulerianBCState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    definition : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'INFLOW'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianBCState.py#L32-L34)[¶](#abaqus.BoundaryCondition.EulerianBCState.EulerianBCState.definition "Permalink to this definition")
    :   A SymbolicConstant specifying the material flow conditions to be defined. Possible
        values are INFLOW, OUTFLOW, and BOTH. The default value is INFLOW.

    definitionState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianBCState.py)[¶](#abaqus.BoundaryCondition.EulerianBCState.EulerianBCState.definitionState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the definition member. Possible
        values are UNSET, SET, and UNCHANGED.

    inflowType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FREE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianBCState.py#L32-L34)[¶](#abaqus.BoundaryCondition.EulerianBCState.EulerianBCState.inflowType "Permalink to this definition")
    :   A SymbolicConstant specifying the material flow conditions to be defined. Possible
        values are FREE, NONE, and VOID. The default value is FREE.

    inflowTypeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianBCState.py)[¶](#abaqus.BoundaryCondition.EulerianBCState.EulerianBCState.inflowTypeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the definition member. Possible
        values are UNSET, SET, and UNCHANGED.

    outflowType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'ZERO_PRESSURE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianBCState.py#L32-L35)[¶](#abaqus.BoundaryCondition.EulerianBCState.EulerianBCState.outflowType "Permalink to this definition")
    :   A SymbolicConstant specifying the material flow conditions to be defined. Possible
        values are ZERO\_PRESSURE, FREE, NON\_REFLECTING, and EQUILIBRIUM. The default value is
        ZERO\_PRESSURE.

    outflowTypeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianBCState.py)[¶](#abaqus.BoundaryCondition.EulerianBCState.EulerianBCState.outflowTypeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the definition member. Possible
        values are UNSET, SET, and UNCHANGED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianBCState.py)[¶](#abaqus.BoundaryCondition.EulerianBCState.EulerianBCState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * PROPAGATED\_FROM\_BASE\_STATE
        * MODIFIED\_FROM\_BASE\_STATE
        * DEACTIVATED\_FROM\_BASE\_STATE
        * BUILT\_INTO\_MODES

*class* EulerianMotionBC(*[name](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.name (Python parameter)")*, *[createStepName](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.createStepName (Python parameter)")*, *[instanceName](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.instanceName (Python parameter)")*, *[followRegion](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.followRegion (Python parameter)")=`1`*, *[region](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.region (Python parameter)")=`None`*, *[materialName](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.materialName (Python parameter)")=`''`*, *[ctrPosition1](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.ctrPosition1 (Python parameter)")=`abaqusConstants.FREE`*, *[posPosition1](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.posPosition1 (Python parameter)")=`abaqusConstants.FREE`*, *[negPosition1](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.negPosition1 (Python parameter)")=`abaqusConstants.FREE`*, *[expansionRatio1](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.expansionRatio1 (Python parameter)")=`None`*, *[contractRatio1](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.contractRatio1 (Python parameter)")=`0`*, *[ctrPosition2](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.ctrPosition2 (Python parameter)")=`abaqusConstants.FREE`*, *[posPosition2](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.posPosition2 (Python parameter)")=`abaqusConstants.FREE`*, *[negPosition2](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.negPosition2 (Python parameter)")=`abaqusConstants.FREE`*, *[expansionRatio2](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.expansionRatio2 (Python parameter)")=`None`*, *[contractRatio2](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.contractRatio2 (Python parameter)")=`0`*, *[ctrPosition3](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.ctrPosition3 (Python parameter)")=`abaqusConstants.FREE`*, *[posPosition3](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.posPosition3 (Python parameter)")=`abaqusConstants.FREE`*, *[negPosition3](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.negPosition3 (Python parameter)")=`abaqusConstants.FREE`*, *[expansionRatio3](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.expansionRatio3 (Python parameter)")=`None`*, *[contractRatio3](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.contractRatio3 (Python parameter)")=`0`*, *[allowContraction](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.allowContraction (Python parameter)")=`1`*, *[aspectLimit](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.aspectLimit (Python parameter)")=`10`*, *[vmaxFactor](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.vmaxFactor (Python parameter)")=`1`*, *[volThreshold](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.volThreshold (Python parameter)")=`0`*, *[bufferSize](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.__init__.bufferSize (Python parameter)")=`2`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L13-L487)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC "Permalink to this definition")
:   Bases: [`BoundaryCondition`](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition "abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition (Python class)")

    The EulerianMotionBC object stores the data for an Eulerian mesh motion boundary condition. The
    EulerianMotionBC object is derived from the BoundaryCondition object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name]
    ```

    Note

    Check [EulerianMotionBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-eulerianmotionbcpyc.htm?contextscope=all).

    Member Details:

    allowContraction : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L101-L102)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.allowContraction "Permalink to this definition")
    :   A Boolean specifying whether the mesh is allowed to contract . The default value is ON.

    aspectLimit : --is-rst--:py:class:`float` = `10`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L104-L106)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.aspectLimit "Permalink to this definition")
    :   A Float specifying the maximum change in allowed aspect ratio (for any of the three mesh
        aspects, 1-2, 2-3, 3-1). The default value is 10.0.

    bufferSize : --is-rst--:py:class:`float` = `2`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L117-L119)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.bufferSize "Permalink to this definition")
    :   None or a Float specifying the buffer between the surface box and the Eulerian section
        mesh bounding box. The default value is 2.0.

    category : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.category "Permalink to this definition")
    :   A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.

    contractRatio1 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L89-L91)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.contractRatio1 "Permalink to this definition")
    :   A Float specifying the lower bounds on the allowable scaling of the mesh in the 1
        direction. The default value is 0.0.

    contractRatio2 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L93-L95)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.contractRatio2 "Permalink to this definition")
    :   A Float specifying the lower bounds on the allowable scaling of the mesh in the 2
        direction. The default value is 0.0.

    contractRatio3 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L97-L99)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.contractRatio3 "Permalink to this definition")
    :   A Float specifying the lower bounds on the allowable scaling of the mesh in the 3
        direction. The default value is 0.0.

    ctrPosition1 : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FREE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L32-L34)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.ctrPosition1 "Permalink to this definition")
    :   A SymbolicConstant specifying the 1-direction translational constraint on the center of
        the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

    ctrPosition2 : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FREE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L36-L38)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.ctrPosition2 "Permalink to this definition")
    :   A SymbolicConstant specifying the 2-direction translational constraint on the center of
        the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

    ctrPosition3 : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FREE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L40-L42)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.ctrPosition3 "Permalink to this definition")
    :   A SymbolicConstant specifying the 3-direction translational constraint on the center of
        the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

    expansionRatio1 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L74-L77)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.expansionRatio1 "Permalink to this definition")
    :   None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
        1 direction. If **expansionRatio1** = None, then there is no upper limit. The default value
        is None.

    expansionRatio2 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L74-L77)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.expansionRatio2 "Permalink to this definition")
    :   None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
        2 direction. If **expansionRatio2** = None, then there is no upper limit. The default value
        is None.

    expansionRatio3 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L74-L77)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.expansionRatio3 "Permalink to this definition")
    :   None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
        3 direction. If **expansionRatio3** = None, then there is no upper limit. The default value
        is None.

    followRegion : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L28-L30)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.followRegion "Permalink to this definition")
    :   A Boolean specifying whether the mesh will follow a regular surface region or an
        Eulerian surface. The default value is ON.

    instanceName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L121-L122)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.instanceName "Permalink to this definition")
    :   A String specifying the name of the Eulerian part instance.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L135-L138)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the boundary
        condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    materialName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L124-L126)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.materialName "Permalink to this definition")
    :   A String specifying the name of the Eulerian surface to follow. This argument applies
        only when **followRegion** = False.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L25-L26)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.name "Permalink to this definition")
    :   A String specifying the boundary condition repository key.

    negPosition1 : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FREE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L59-L62)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.negPosition1 "Permalink to this definition")
    :   A SymbolicConstant specifying the translational constraint on the negative (minimum)
        bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default
        value is FREE.

    negPosition2 : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FREE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L59-L62)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.negPosition2 "Permalink to this definition")
    :   A SymbolicConstant specifying the translational constraint on the negative (minimum)
        bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default
        value is FREE.

    negPosition3 : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FREE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L59-L62)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.negPosition3 "Permalink to this definition")
    :   A SymbolicConstant specifying the translational constraint on the negative (minimum)
        bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default
        value is FREE.

    posPosition1 : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FREE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L44-L47)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.posPosition1 "Permalink to this definition")
    :   A SymbolicConstant specifying the translational constraint on the positive (maximum)
        bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default
        value is FREE.

    posPosition2 : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FREE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L44-L47)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.posPosition2 "Permalink to this definition")
    :   A SymbolicConstant specifying the translational constraint on the positive (maximum)
        bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default
        value is FREE.

    posPosition3 : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FREE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L44-L47)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.posPosition3 "Permalink to this definition")
    :   A SymbolicConstant specifying the translational constraint on the positive (maximum)
        bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default
        value is FREE.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L132-L133)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.region "Permalink to this definition")
    :   A Region object specifying the region to which the boundary condition is applied.

    setValues(*[instanceName](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.instanceName "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.instanceName (Python parameter) — A String specifying the name of the Eulerian part instance.")*, *[followRegion](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.followRegion "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.followRegion (Python parameter) — A Boolean specifying whether the mesh will follow a regular surface region or an Eulerian surface.")=`1`*, *[region](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.region "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")=`None`*, *[materialName](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.materialName "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.materialName (Python parameter) — A String specifying the name of the Eulerian surface to follow.")=`''`*, *[ctrPosition1](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.ctrPosition1 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.ctrPosition1 (Python parameter) — A SymbolicConstant specifying the 1-direction translational constraint on the center of the Eulerian mesh.")=`abaqusConstants.FREE`*, *[posPosition1](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.posPosition1 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.posPosition1 (Python parameter) — A SymbolicConstant specifying the translational constraint on the positive (maximum) bounds of the mesh in the 1 direction.")=`abaqusConstants.FREE`*, *[negPosition1](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.negPosition1 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.negPosition1 (Python parameter) — A SymbolicConstant specifying the translational constraint on the negative (minimum) bounds of the mesh in the 1 direction.")=`abaqusConstants.FREE`*, *[expansionRatio1](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.expansionRatio1 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.expansionRatio1 (Python parameter) — None or a Float specifying the upper bounds on the allowable scaling of the mesh in the 1 direction.")=`None`*, *[contractRatio1](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.contractRatio1 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.contractRatio1 (Python parameter) — A Float specifying the lower bounds on the allowable scaling of the mesh in the 1 direction.")=`0`*, *[ctrPosition2](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.ctrPosition2 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.ctrPosition2 (Python parameter) — A SymbolicConstant specifying the 2-direction translational constraint on the center of the Eulerian mesh.")=`abaqusConstants.FREE`*, *[posPosition2](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.posPosition2 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.posPosition2 (Python parameter) — A SymbolicConstant specifying the translational constraint on the positive (maximum) bounds of the mesh in the 2 direction.")=`abaqusConstants.FREE`*, *[negPosition2](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.negPosition2 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.negPosition2 (Python parameter) — A SymbolicConstant specifying the translational constraint on the negative (minimum) bounds of the mesh in the 2 direction.")=`abaqusConstants.FREE`*, *[expansionRatio2](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.expansionRatio2 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.expansionRatio2 (Python parameter) — None or a Float specifying the upper bounds on the allowable scaling of the mesh in the 2 direction.")=`None`*, *[contractRatio2](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.contractRatio2 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.contractRatio2 (Python parameter) — A Float specifying the lower bounds on the allowable scaling of the mesh in the 2 direction.")=`0`*, *[ctrPosition3](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.ctrPosition3 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.ctrPosition3 (Python parameter) — A SymbolicConstant specifying the 3-direction translational constraint on the center of the Eulerian mesh.")=`abaqusConstants.FREE`*, *[posPosition3](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.posPosition3 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.posPosition3 (Python parameter) — A SymbolicConstant specifying the translational constraint on the positive (maximum) bounds of the mesh in the 3 direction.")=`abaqusConstants.FREE`*, *[negPosition3](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.negPosition3 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.negPosition3 (Python parameter) — A SymbolicConstant specifying the translational constraint on the negative (minimum) bounds of the mesh in the 3 direction.")=`abaqusConstants.FREE`*, *[expansionRatio3](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.expansionRatio3 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.expansionRatio3 (Python parameter) — None or a Float specifying the upper bounds on the allowable scaling of the mesh in the 3 direction.")=`None`*, *[contractRatio3](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.contractRatio3 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.contractRatio3 (Python parameter) — A Float specifying the lower bounds on the allowable scaling of the mesh in the 3 direction.")=`0`*, *[allowContraction](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.allowContraction "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.allowContraction (Python parameter) — A Boolean specifying whether the mesh is allowed to contract .")=`1`*, *[aspectLimit](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.aspectLimit "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.aspectLimit (Python parameter) — A Float specifying the maximum change in allowed aspect ratio (for any of the three mesh aspects, 1-2, 2-3, 3-1).")=`10`*, *[vmaxFactor](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.vmaxFactor "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.vmaxFactor (Python parameter) — A Float specifying the multiplier for the mesh nodal velocity limit.")=`1`*, *[volThreshold](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.volThreshold "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.volThreshold (Python parameter) — A Float specifying the lower bounds on the volume fraction when determining which nodes to include in the surface bounding box calculation for an Eulerian material surface. This argument applies only when followRegion = False.")=`0`*, *[bufferSize](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.bufferSize "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.bufferSize (Python parameter) — None or a Float specifying the buffer between the surface box and the Eulerian section mesh bounding box.")=`2`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L270-L383)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues "Permalink to this definition")
    :   This method modifies the data for an existing EulerianMotionBC object in the step where it is
        created.

        Note

        Check [EulerianMotionBC.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-eulerianmotionbcpyc.htm?contextscope=all#simaker-eulerianmotionbcsetvaluespyc).

        Parameters:[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues-parameters "Permalink to this headline")
        :   instanceName[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.instanceName "Permalink to this definition")
            :   A String specifying the name of the Eulerian part instance.

            followRegion=`1`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.followRegion "Permalink to this definition")
            :   A Boolean specifying whether the mesh will follow a regular surface region or an
                Eulerian surface. The default value is ON.

            region=`None`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            materialName=`''`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.materialName "Permalink to this definition")
            :   A String specifying the name of the Eulerian surface to follow. This argument applies
                only when **followRegion** = False.

            ctrPosition1=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.ctrPosition1 "Permalink to this definition")
            :   A SymbolicConstant specifying the 1-direction translational constraint on the center of
                the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

            posPosition1=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.posPosition1 "Permalink to this definition")
            :   A SymbolicConstant specifying the translational constraint on the positive (maximum)
                bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default
                value is FREE.

            negPosition1=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.negPosition1 "Permalink to this definition")
            :   A SymbolicConstant specifying the translational constraint on the negative (minimum)
                bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default
                value is FREE.

            expansionRatio1=`None`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.expansionRatio1 "Permalink to this definition")
            :   None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
                1 direction. If **expansionRatio1** = None, then there is no upper limit. The default value
                is None.

            contractRatio1=`0`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.contractRatio1 "Permalink to this definition")
            :   A Float specifying the lower bounds on the allowable scaling of the mesh in the 1
                direction. The default value is 0.0.

            ctrPosition2=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.ctrPosition2 "Permalink to this definition")
            :   A SymbolicConstant specifying the 2-direction translational constraint on the center of
                the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

            posPosition2=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.posPosition2 "Permalink to this definition")
            :   A SymbolicConstant specifying the translational constraint on the positive (maximum)
                bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default
                value is FREE.

            negPosition2=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.negPosition2 "Permalink to this definition")
            :   A SymbolicConstant specifying the translational constraint on the negative (minimum)
                bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default
                value is FREE.

            expansionRatio2=`None`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.expansionRatio2 "Permalink to this definition")
            :   None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
                2 direction. If **expansionRatio2** = None, then there is no upper limit. The default value
                is None.

            contractRatio2=`0`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.contractRatio2 "Permalink to this definition")
            :   A Float specifying the lower bounds on the allowable scaling of the mesh in the 2
                direction. The default value is 0.0.

            ctrPosition3=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.ctrPosition3 "Permalink to this definition")
            :   A SymbolicConstant specifying the 3-direction translational constraint on the center of
                the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

            posPosition3=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.posPosition3 "Permalink to this definition")
            :   A SymbolicConstant specifying the translational constraint on the positive (maximum)
                bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default
                value is FREE.

            negPosition3=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.negPosition3 "Permalink to this definition")
            :   A SymbolicConstant specifying the translational constraint on the negative (minimum)
                bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default
                value is FREE.

            expansionRatio3=`None`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.expansionRatio3 "Permalink to this definition")
            :   None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
                3 direction. If **expansionRatio3** = None, then there is no upper limit. The default value
                is None.

            contractRatio3=`0`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.contractRatio3 "Permalink to this definition")
            :   A Float specifying the lower bounds on the allowable scaling of the mesh in the 3
                direction. The default value is 0.0.

            allowContraction=`1`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.allowContraction "Permalink to this definition")
            :   A Boolean specifying whether the mesh is allowed to contract . The default value is ON.

            aspectLimit=`10`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.aspectLimit "Permalink to this definition")
            :   A Float specifying the maximum change in allowed aspect ratio (for any of the three mesh
                aspects, 1-2, 2-3, 3-1). The default value is 10.0.

            vmaxFactor=`1`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.vmaxFactor "Permalink to this definition")
            :   A Float specifying the multiplier for the mesh nodal velocity limit. The default value
                is 1.01.

            volThreshold=`0`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.volThreshold "Permalink to this definition")
            :   A Float specifying the lower bounds on the volume fraction when determining which nodes
                to include in the surface bounding box calculation for an Eulerian material surface.
                This argument applies only when **followRegion** = False. The default value is 0.5.

            bufferSize=`2`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValues.bufferSize "Permalink to this definition")
            :   None or a Float specifying the buffer between the surface box and the Eulerian section
                mesh bounding box. The default value is 2.0.

    setValuesInStep(*[stepName](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.stepName "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition is modified.")*, *[ctrPosition1](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.ctrPosition1 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.ctrPosition1 (Python parameter) — A SymbolicConstant specifying the 1-direction translational constraint on the center of the Eulerian mesh.")=`abaqusConstants.FREE`*, *[posPosition1](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.posPosition1 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.posPosition1 (Python parameter) — A SymbolicConstant specifying the translational constraint on the positive (maximum) bounds of the mesh in the 1 direction.")=`abaqusConstants.FREE`*, *[negPosition1](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.negPosition1 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.negPosition1 (Python parameter) — A SymbolicConstant specifying the translational constraint on the negative (minimum) bounds of the mesh in the 1 direction.")=`abaqusConstants.FREE`*, *[expansionRatio1](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.expansionRatio1 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.expansionRatio1 (Python parameter) — None or a Float specifying the upper bounds on the allowable scaling of the mesh in the 1 direction.")=`None`*, *[contractRatio1](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.contractRatio1 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.contractRatio1 (Python parameter) — A Float specifying the lower bounds on the allowable scaling of the mesh in the 1 direction.")=`0`*, *[ctrPosition2](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.ctrPosition2 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.ctrPosition2 (Python parameter) — A SymbolicConstant specifying the 2-direction translational constraint on the center of the Eulerian mesh.")=`abaqusConstants.FREE`*, *[posPosition2](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.posPosition2 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.posPosition2 (Python parameter) — A SymbolicConstant specifying the translational constraint on the positive (maximum) bounds of the mesh in the 2 direction.")=`abaqusConstants.FREE`*, *[negPosition2](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.negPosition2 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.negPosition2 (Python parameter) — A SymbolicConstant specifying the translational constraint on the negative (minimum) bounds of the mesh in the 2 direction.")=`abaqusConstants.FREE`*, *[expansionRatio2](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.expansionRatio2 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.expansionRatio2 (Python parameter) — None or a Float specifying the upper bounds on the allowable scaling of the mesh in the 2 direction.")=`None`*, *[contractRatio2](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.contractRatio2 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.contractRatio2 (Python parameter) — A Float specifying the lower bounds on the allowable scaling of the mesh in the 2 direction.")=`0`*, *[ctrPosition3](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.ctrPosition3 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.ctrPosition3 (Python parameter) — A SymbolicConstant specifying the 3-direction translational constraint on the center of the Eulerian mesh.")=`abaqusConstants.FREE`*, *[posPosition3](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.posPosition3 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.posPosition3 (Python parameter) — A SymbolicConstant specifying the translational constraint on the positive (maximum) bounds of the mesh in the 3 direction.")=`abaqusConstants.FREE`*, *[negPosition3](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.negPosition3 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.negPosition3 (Python parameter) — A SymbolicConstant specifying the translational constraint on the negative (minimum) bounds of the mesh in the 3 direction.")=`abaqusConstants.FREE`*, *[expansionRatio3](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.expansionRatio3 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.expansionRatio3 (Python parameter) — None or a Float specifying the upper bounds on the allowable scaling of the mesh in the 3 direction.")=`None`*, *[contractRatio3](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.contractRatio3 "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.contractRatio3 (Python parameter) — A Float specifying the lower bounds on the allowable scaling of the mesh in the 3 direction.")=`0`*, *[allowContraction](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.allowContraction "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.allowContraction (Python parameter) — A Boolean specifying whether the mesh is allowed to contract .")=`1`*, *[aspectLimit](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.aspectLimit "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.aspectLimit (Python parameter) — A Float specifying the maximum change in allowed aspect ratio (for any of the three mesh aspects, 1-2, 2-3, 3-1).")=`10`*, *[vmaxFactor](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.vmaxFactor "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.vmaxFactor (Python parameter) — A Float specifying the multiplier for the mesh nodal velocity limit.")=`1`*, *[volThreshold](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.volThreshold "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.volThreshold (Python parameter) — A Float specifying the lower bounds on the volume fraction when determining which nodes to include in the surface bounding box calculation for an Eulerian material surface. This argument applies only when followRegion = False.")=`0`*, *[bufferSize](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.bufferSize "abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.bufferSize (Python parameter) — None or a Float specifying the buffer between the surface box and the Eulerian section mesh bounding box.")=`2`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L385-L487)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing EulerianMotionBC object in the specified
        step.

        Note

        Check [EulerianMotionBC.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-eulerianmotionbcpyc.htm?contextscope=all#simaker-eulerianmotionbcsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is modified.

            ctrPosition1=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.ctrPosition1 "Permalink to this definition")
            :   A SymbolicConstant specifying the 1-direction translational constraint on the center of
                the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

            posPosition1=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.posPosition1 "Permalink to this definition")
            :   A SymbolicConstant specifying the translational constraint on the positive (maximum)
                bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default
                value is FREE.

            negPosition1=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.negPosition1 "Permalink to this definition")
            :   A SymbolicConstant specifying the translational constraint on the negative (minimum)
                bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default
                value is FREE.

            expansionRatio1=`None`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.expansionRatio1 "Permalink to this definition")
            :   None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
                1 direction. If **expansionRatio1** = None, then there is no upper limit. The default value
                is None.

            contractRatio1=`0`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.contractRatio1 "Permalink to this definition")
            :   A Float specifying the lower bounds on the allowable scaling of the mesh in the 1
                direction. The default value is 0.0.

            ctrPosition2=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.ctrPosition2 "Permalink to this definition")
            :   A SymbolicConstant specifying the 2-direction translational constraint on the center of
                the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

            posPosition2=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.posPosition2 "Permalink to this definition")
            :   A SymbolicConstant specifying the translational constraint on the positive (maximum)
                bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default
                value is FREE.

            negPosition2=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.negPosition2 "Permalink to this definition")
            :   A SymbolicConstant specifying the translational constraint on the negative (minimum)
                bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default
                value is FREE.

            expansionRatio2=`None`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.expansionRatio2 "Permalink to this definition")
            :   None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
                2 direction. If **expansionRatio2** = None, then there is no upper limit. The default value
                is None.

            contractRatio2=`0`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.contractRatio2 "Permalink to this definition")
            :   A Float specifying the lower bounds on the allowable scaling of the mesh in the 2
                direction. The default value is 0.0.

            ctrPosition3=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.ctrPosition3 "Permalink to this definition")
            :   A SymbolicConstant specifying the 3-direction translational constraint on the center of
                the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

            posPosition3=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.posPosition3 "Permalink to this definition")
            :   A SymbolicConstant specifying the translational constraint on the positive (maximum)
                bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default
                value is FREE.

            negPosition3=`abaqusConstants.FREE`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.negPosition3 "Permalink to this definition")
            :   A SymbolicConstant specifying the translational constraint on the negative (minimum)
                bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default
                value is FREE.

            expansionRatio3=`None`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.expansionRatio3 "Permalink to this definition")
            :   None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
                3 direction. If **expansionRatio3** = None, then there is no upper limit. The default value
                is None.

            contractRatio3=`0`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.contractRatio3 "Permalink to this definition")
            :   A Float specifying the lower bounds on the allowable scaling of the mesh in the 3
                direction. The default value is 0.0.

            allowContraction=`1`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.allowContraction "Permalink to this definition")
            :   A Boolean specifying whether the mesh is allowed to contract . The default value is ON.

            aspectLimit=`10`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.aspectLimit "Permalink to this definition")
            :   A Float specifying the maximum change in allowed aspect ratio (for any of the three mesh
                aspects, 1-2, 2-3, 3-1). The default value is 10.0.

            vmaxFactor=`1`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.vmaxFactor "Permalink to this definition")
            :   A Float specifying the multiplier for the mesh nodal velocity limit. The default value
                is 1.01.

            volThreshold=`0`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.volThreshold "Permalink to this definition")
            :   A Float specifying the lower bounds on the volume fraction when determining which nodes
                to include in the surface bounding box calculation for an Eulerian material surface.
                This argument applies only when **followRegion** = False. The default value is 0.5.

            bufferSize=`2`[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.setValuesInStep.bufferSize "Permalink to this definition")
            :   None or a Float specifying the buffer between the surface box and the Eulerian section
                mesh bounding box. The default value is 2.0.

    vmaxFactor : --is-rst--:py:class:`float` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L108-L110)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.vmaxFactor "Permalink to this definition")
    :   A Float specifying the multiplier for the mesh nodal velocity limit. The default value
        is 1.01.

    volThreshold : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBC.py#L112-L115)[¶](#abaqus.BoundaryCondition.EulerianMotionBC.EulerianMotionBC.volThreshold "Permalink to this definition")
    :   A Float specifying the lower bounds on the volume fraction when determining which nodes
        to include in the surface bounding box calculation for an Eulerian material surface.
        This argument applies only when **followRegion** = False. The default value is 0.5.

*class* EulerianMotionBCState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBCState.py#L9-L139)[¶](#abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState "Permalink to this definition")
:   Bases: [`BoundaryConditionState`](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState "abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState (Python class)")

    The EulerianMotionBCState object stores the propagating data for an Eulerian mesh motion boundary
    condition in a step. One instance of this object is created internally by the EulerianMotionBC object for
    each step. The instance is also deleted internally by the EulerianMotionBC object. The EulerianMotionBCState
    object has no constructor or methods. The EulerianMotionBCState object is derived from the
    BoundaryConditionState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].boundaryConditionStates[name]
    ```

    The corresponding analysis keywords are:

    * EULERIAN MESH MOTION

    Note

    Check [EulerianMotionBCState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-eulerianmotionbcstatepyc.htm?contextscope=all).

    Member Details:

    allowContraction : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBCState.py#L97-L98)[¶](#abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState.allowContraction "Permalink to this definition")
    :   A Boolean specifying whether the mesh is allowed to contract . The default value is ON.

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBCState.py#L9-L139)[¶](#abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the
        boundary condition has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBCState.py)[¶](#abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    aspectLimit : --is-rst--:py:class:`float` = `10`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBCState.py#L100-L102)[¶](#abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState.aspectLimit "Permalink to this definition")
    :   A Float specifying the maximum change in allowed aspect ratio (for any of the three mesh
        aspects, 1-2, 2-3, 3-1). The default value is 10.0.

    bufferSize : --is-rst--:py:class:`float` = `2`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBCState.py#L113-L115)[¶](#abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState.bufferSize "Permalink to this definition")
    :   None or a Float specifying the buffer between the surface box and the Eulerian section
        mesh bounding box. The default value is 2.0.

    contractRatio1 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBCState.py#L85-L87)[¶](#abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState.contractRatio1 "Permalink to this definition")
    :   A Float specifying the lower bounds on the allowable scaling of the mesh in the 1
        direction. The default value is 0.0.

    contractRatio2 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBCState.py#L89-L91)[¶](#abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState.contractRatio2 "Permalink to this definition")
    :   A Float specifying the lower bounds on the allowable scaling of the mesh in the 2
        direction. The default value is 0.0.

    contractRatio3 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBCState.py#L93-L95)[¶](#abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState.contractRatio3 "Permalink to this definition")
    :   A Float specifying the lower bounds on the allowable scaling of the mesh in the 3
        direction. The default value is 0.0.

    ctrPosition1 : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FREE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBCState.py#L28-L30)[¶](#abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState.ctrPosition1 "Permalink to this definition")
    :   A SymbolicConstant specifying the 1-direction translational constraint on the center of
        the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

    ctrPosition2 : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FREE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBCState.py#L32-L34)[¶](#abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState.ctrPosition2 "Permalink to this definition")
    :   A SymbolicConstant specifying the 2-direction translational constraint on the center of
        the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

    ctrPosition3 : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FREE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBCState.py#L36-L38)[¶](#abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState.ctrPosition3 "Permalink to this definition")
    :   A SymbolicConstant specifying the 3-direction translational constraint on the center of
        the Eulerian mesh. Possible values are FREE and FIXED. The default value is FREE.

    expansionRatio1 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBCState.py#L70-L73)[¶](#abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState.expansionRatio1 "Permalink to this definition")
    :   None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
        1 direction. If **expansionRatio1** = None, then there is no upper limit. The default value
        is None.

    expansionRatio2 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBCState.py#L70-L73)[¶](#abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState.expansionRatio2 "Permalink to this definition")
    :   None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
        2 direction. If **expansionRatio2** = None, then there is no upper limit. The default value
        is None.

    expansionRatio3 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBCState.py#L70-L73)[¶](#abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState.expansionRatio3 "Permalink to this definition")
    :   None or a Float specifying the upper bounds on the allowable scaling of the mesh in the
        3 direction. If **expansionRatio3** = None, then there is no upper limit. The default value
        is None.

    negPosition1 : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FREE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBCState.py#L55-L58)[¶](#abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState.negPosition1 "Permalink to this definition")
    :   A SymbolicConstant specifying the translational constraint on the negative (minimum)
        bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default
        value is FREE.

    negPosition2 : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FREE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBCState.py#L55-L58)[¶](#abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState.negPosition2 "Permalink to this definition")
    :   A SymbolicConstant specifying the translational constraint on the negative (minimum)
        bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default
        value is FREE.

    negPosition3 : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FREE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBCState.py#L55-L58)[¶](#abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState.negPosition3 "Permalink to this definition")
    :   A SymbolicConstant specifying the translational constraint on the negative (minimum)
        bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default
        value is FREE.

    posPosition1 : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FREE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBCState.py#L40-L43)[¶](#abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState.posPosition1 "Permalink to this definition")
    :   A SymbolicConstant specifying the translational constraint on the positive (maximum)
        bounds of the mesh in the 1 direction. Possible values are FREE and FIXED. The default
        value is FREE.

    posPosition2 : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FREE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBCState.py#L40-L43)[¶](#abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState.posPosition2 "Permalink to this definition")
    :   A SymbolicConstant specifying the translational constraint on the positive (maximum)
        bounds of the mesh in the 2 direction. Possible values are FREE and FIXED. The default
        value is FREE.

    posPosition3 : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FREE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBCState.py#L40-L43)[¶](#abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState.posPosition3 "Permalink to this definition")
    :   A SymbolicConstant specifying the translational constraint on the positive (maximum)
        bounds of the mesh in the 3 direction. Possible values are FREE and FIXED. The default
        value is FREE.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBCState.py)[¶](#abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * PROPAGATED\_FROM\_BASE\_STATE
        * MODIFIED\_FROM\_BASE\_STATE
        * DEACTIVATED\_FROM\_BASE\_STATE
        * BUILT\_INTO\_MODES

    vmaxFactor : --is-rst--:py:class:`float` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBCState.py#L104-L106)[¶](#abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState.vmaxFactor "Permalink to this definition")
    :   A Float specifying the multiplier for the mesh nodal velocity limit. The default value
        is 1.01.

    volThreshold : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/EulerianMotionBCState.py#L108-L111)[¶](#abaqus.BoundaryCondition.EulerianMotionBCState.EulerianMotionBCState.volThreshold "Permalink to this definition")
    :   A Float specifying the lower bounds on the volume fraction when determining which nodes
        to include in the surface bounding box calculation for an Eulerian material surface.
        This argument applies only when **followRegion** = False. The default value is 0.5.

*class* FluidCavityPressureBC(*[name](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC "abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.__init__.name (Python parameter)")*, *[createStepName](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC "abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.__init__.createStepName (Python parameter)")*, *[fluidCavity](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC "abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.__init__.fluidCavity (Python parameter)")*, *[magnitude](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC "abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.__init__.magnitude (Python parameter)")=`0`*, *[amplitude](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC "abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[fixed](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC "abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.__init__.fixed (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/FluidCavityPressureBC.py#L21-L137)[¶](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC "Permalink to this definition")
:   Bases: [`BoundaryCondition`](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition "abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition (Python class)")

    The FluidCavityPressureBC object stores the data for a fluid cavity pressure boundary condition. The
    FluidCavityPressureBC object is derived from the BoundaryCondition object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name]
    ```

    Note

    Check [FluidCavityPressureBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidcavitypressurebcpyc.htm?contextscope=all).

    Member Details:

    category : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/FluidCavityPressureBC.py)[¶](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.category "Permalink to this definition")
    :   A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.

    fluidCavity : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/FluidCavityPressureBC.py#L36-L37)[¶](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.fluidCavity "Permalink to this definition")
    :   A String specifying the name of a Fluid Cavity Interaction.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/FluidCavityPressureBC.py#L46-L49)[¶](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the boundary
        condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/FluidCavityPressureBC.py#L33-L34)[¶](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.name "Permalink to this definition")
    :   A String specifying the boundary condition repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/FluidCavityPressureBC.py#L43-L44)[¶](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.region "Permalink to this definition")
    :   A Region object specifying the region to which the boundary condition is applied.

    setValues(*[magnitude](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.setValues.magnitude "abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.setValues.magnitude (Python parameter) — A Float specifying the fluid cavity pressure magnitude.")=`0`*, *[amplitude](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.setValues.amplitude "abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[fixed](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.setValues.fixed "abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.setValues.fixed (Python parameter) — A Boolean specifying whether the boundary condition should remain fixed at the current values at the start of the step.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/FluidCavityPressureBC.py#L94-L112)[¶](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.setValues "Permalink to this definition")
    :   This method modifies the data for an existing FluidCavityPressureBC object in the step where it is
        created.

        Note

        Check [FluidCavityPressureBC.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidcavitypressurebcpyc.htm?contextscope=all#simaker-fluidcavitypressurebcsetvaluespyc).

        Parameters:[¶](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.setValues-parameters "Permalink to this headline")
        :   magnitude=`0`[¶](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.setValues.magnitude "Permalink to this definition")
            :   A Float specifying the fluid cavity pressure magnitude. The default value is 0.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            fixed=`0`[¶](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.setValues.fixed "Permalink to this definition")
            :   A Boolean specifying whether the boundary condition should remain fixed at the current
                values at the start of the step. The default value is OFF.

    setValuesInStep(*[stepName](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.setValuesInStep.stepName "abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition is modified.")*, *[magnitude](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.setValuesInStep.magnitude "abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.setValuesInStep.magnitude (Python parameter) — A Float or the SymbolicConstant FREED specifying the fluid cavity pressure magnitude.")=`abaqusConstants.UNCHANGED`*, *[amplitude](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.setValuesInStep.amplitude "abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/FluidCavityPressureBC.py#L114-L137)[¶](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing FluidCavityPressureBC object in the
        specified step.

        Note

        Check [FluidCavityPressureBC.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidcavitypressurebcpyc.htm?contextscope=all#simaker-fluidcavitypressurebcsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is modified.

            magnitude=`abaqusConstants.UNCHANGED`[¶](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float or the SymbolicConstant FREED specifying the fluid cavity pressure magnitude.

            amplitude=`''`[¶](#abaqus.BoundaryCondition.FluidCavityPressureBC.FluidCavityPressureBC.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                boundary condition is changed to have no amplitude reference. You should provide the
                **amplitude** argument only if it is valid for the specified step.

*class* FluidCavityPressureBCState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/FluidCavityPressureBCState.py#L9-L57)[¶](#abaqus.BoundaryCondition.FluidCavityPressureBCState.FluidCavityPressureBCState "Permalink to this definition")
:   Bases: [`BoundaryConditionState`](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState "abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState (Python class)")

    The FluidCavityPressureBCState object stores the propagating data for a fluid cavity pressure boundary
    condition in a step. One instance of this object is created internally by the FluidCavityPressureBC object
    for each step. The instance is also deleted internally by the FluidCavityPressureBC object. The
    FluidCavityPressureBCState object has no constructor or methods. The FluidCavityPressureBCState object is
    derived from the BoundaryConditionState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].boundaryConditionStates[name]
    ```

    The corresponding analysis keywords are:

    * BOUNDARY

    Note

    Check [FluidCavityPressureBCState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fluidcavitypressurebcstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/FluidCavityPressureBCState.py#L9-L57)[¶](#abaqus.BoundaryCondition.FluidCavityPressureBCState.FluidCavityPressureBCState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the
        boundary condition has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/FluidCavityPressureBCState.py)[¶](#abaqus.BoundaryCondition.FluidCavityPressureBCState.FluidCavityPressureBCState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/FluidCavityPressureBCState.py#L28-L29)[¶](#abaqus.BoundaryCondition.FluidCavityPressureBCState.FluidCavityPressureBCState.magnitude "Permalink to this definition")
    :   A Float specifying the fluid cavity pressure magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/FluidCavityPressureBCState.py)[¶](#abaqus.BoundaryCondition.FluidCavityPressureBCState.FluidCavityPressureBCState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the fluid cavity pressure
        magnitude. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/FluidCavityPressureBCState.py)[¶](#abaqus.BoundaryCondition.FluidCavityPressureBCState.FluidCavityPressureBCState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * PROPAGATED\_FROM\_BASE\_STATE
        * MODIFIED\_FROM\_BASE\_STATE
        * DEACTIVATED\_FROM\_BASE\_STATE
        * BUILT\_INTO\_MODES

*class* MagneticVectorPotentialBC(*[name](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC "abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.__init__.name (Python parameter)")*, *[createStepName](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC "abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.__init__.createStepName (Python parameter)")*, *[region](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC "abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.__init__.region (Python parameter)")*, *[component1](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC "abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.__init__.component1 (Python parameter)")=`None`*, *[component2](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC "abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.__init__.component2 (Python parameter)")=`abaqusConstants.UNSET`*, *[component3](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC "abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.__init__.component3 (Python parameter)")=`abaqusConstants.UNSET`*, *[amplitude](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC "abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC "abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[localCsys](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC "abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.__init__.localCsys (Python parameter)")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/MagneticVectorPotentialBC.py#L13-L178)[¶](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC "Permalink to this definition")
:   Bases: [`BoundaryCondition`](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition "abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition (Python class)")

    The MagneticVectorPotentialBC object stores the data for a magnetic vector potential boundary condition.
    The MagneticVectorPotentialBC object is derived from the BoundaryCondition object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name]
    ```

    Note

    Check [MagneticVectorPotentialBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-magneticvectorpotentialbcpyc.htm?contextscope=all).

    Member Details:

    category : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/MagneticVectorPotentialBC.py)[¶](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.category "Permalink to this definition")
    :   A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/MagneticVectorPotentialBC.py#L28-L30)[¶](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
        Possible values are UNIFORM and USER\_DEFINED. The default value is UNIFORM.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/MagneticVectorPotentialBC.py#L39-L42)[¶](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the boundary
        condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/MagneticVectorPotentialBC.py#L25-L26)[¶](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.name "Permalink to this definition")
    :   A String specifying the boundary condition repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/MagneticVectorPotentialBC.py#L36-L37)[¶](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.region "Permalink to this definition")
    :   A Region object specifying the region to which the boundary condition is applied.

    setValues(*[component1](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValues.component1 "abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValues.component1 (Python parameter) — A Complex, or a SymbolicConstant specifying the magnetic vector potential component in the 1-direction.")=`None`*, *[component2](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValues.component2 "abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValues.component2 (Python parameter) — A Complex, or a SymbolicConstant specifying the magnetic vector potential component in the 2-direction.")=`abaqusConstants.UNSET`*, *[component3](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValues.component3 "abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValues.component3 (Python parameter) — A Complex, or a SymbolicConstant specifying the magnetic vector potential component in the 3-direction.")=`abaqusConstants.UNSET`*, *[amplitude](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValues.amplitude "abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValues.distributionType "abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM and USER_DEFINED.")=`abaqusConstants.UNIFORM`*, *[localCsys](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValues.localCsys "abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValues.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/MagneticVectorPotentialBC.py#L104-L144)[¶](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValues "Permalink to this definition")
    :   This method modifies the data for an existing MagneticVectorPotentialBC object in the step where it
        is created.

        Note

        Check [MagneticVectorPotentialBC.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-magneticvectorpotentialbcpyc.htm?contextscope=all#simaker-magneticvectorpotentialbcsetvaluespyc).

        Parameters:[¶](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValues-parameters "Permalink to this headline")
        :   component1=`None`[¶](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValues.component1 "Permalink to this definition")
            :   A Complex, or a SymbolicConstant specifying the magnetic vector potential component in
                the 1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET

            component2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValues.component2 "Permalink to this definition")
            :   A Complex, or a SymbolicConstant specifying the magnetic vector potential component in
                the 2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET.

            component3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValues.component3 "Permalink to this definition")
            :   A Complex, or a SymbolicConstant specifying the magnetic vector potential component in
                the 3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM and USER\_DEFINED. The default value is UNIFORM.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValues.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

    setValuesInStep(*[stepName](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValuesInStep.stepName "abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition is modified.")*, *[component1](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValuesInStep.component1 "abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValuesInStep.component1 (Python parameter) — A Complex, or a SymbolicConstant specifying the magnetic vector potential component in the 1-direction.")=`None`*, *[component2](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValuesInStep.component2 "abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValuesInStep.component2 (Python parameter) — A Complex, or a SymbolicConstant specifying the magnetic vector potential component in the 2-direction.")=`None`*, *[component3](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValuesInStep.component3 "abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValuesInStep.component3 (Python parameter) — A Complex, or a SymbolicConstant specifying the magnetic vector potential component in the 3-direction.")=`None`*, *[amplitude](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValuesInStep.amplitude "abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/MagneticVectorPotentialBC.py#L146-L178)[¶](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing MagneticVectorPotentialBC object in the
        specified step.

        Note

        Check [MagneticVectorPotentialBC.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-magneticvectorpotentialbcpyc.htm?contextscope=all#simaker-magneticvectorpotentialbcsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is modified.

            component1=`None`[¶](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValuesInStep.component1 "Permalink to this definition")
            :   A Complex, or a SymbolicConstant specifying the magnetic vector potential component in
                the 1-direction. Possible values for the SymbolicConstant are SET and UNCHANGED.

            component2=`None`[¶](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValuesInStep.component2 "Permalink to this definition")
            :   A Complex, or a SymbolicConstant specifying the magnetic vector potential component in
                the 2-direction. Possible values for the SymbolicConstant are SET and UNCHANGED.

            component3=`None`[¶](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValuesInStep.component3 "Permalink to this definition")
            :   A Complex, or a SymbolicConstant specifying the magnetic vector potential component in
                the 3-direction. Possible values for the SymbolicConstant areSET and UNCHANGED.

            amplitude=`''`[¶](#abaqus.BoundaryCondition.MagneticVectorPotentialBC.MagneticVectorPotentialBC.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                boundary condition is changed to have no amplitude reference. You should provide the
                **amplitude** argument only if it is valid for the specified step.

*class* MaterialFlowBC(*[name](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC "abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.__init__.name (Python parameter)")*, *[createStepName](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC "abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.__init__.createStepName (Python parameter)")*, *[region](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC "abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.__init__.region (Python parameter)")*, *[fieldName](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC "abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.__init__.fieldName (Python parameter)")=`''`*, *[magnitude](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC "abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.__init__.magnitude (Python parameter)")=`0`*, *[distributionType](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC "abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC "abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[fixed](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC "abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.__init__.fixed (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/MaterialFlowBC.py#L22-L168)[¶](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC "Permalink to this definition")
:   Bases: [`BoundaryCondition`](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition "abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition (Python class)")

    The MaterialFlowBC object stores the data for a connector material flow boundary condition. The
    MaterialFlowBC object is derived from the BoundaryCondition object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name]
    ```

    Note

    Check [MaterialFlowBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-materialflowbcpyc.htm?contextscope=all).

    Member Details:

    category : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/MaterialFlowBC.py)[¶](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.category "Permalink to this definition")
    :   A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/MaterialFlowBC.py#L37-L39)[¶](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
        Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

    fieldName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/MaterialFlowBC.py#L41-L44)[¶](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.fieldName "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this boundary
        condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
        default value is an empty string.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/MaterialFlowBC.py#L53-L56)[¶](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the boundary
        condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/MaterialFlowBC.py#L34-L35)[¶](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.name "Permalink to this definition")
    :   A String specifying the boundary condition repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/MaterialFlowBC.py#L50-L51)[¶](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.region "Permalink to this definition")
    :   A Region object specifying the region to which the boundary condition is applied.

    setValues(*[fieldName](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValues.fieldName "abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValues.fieldName (Python parameter) — A String specifying the name of the AnalyticalField object associated with this boundary condition.")=`''`*, *[magnitude](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValues.magnitude "abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValues.magnitude (Python parameter) — A Float specifying the material flow magnitude.")=`0`*, *[distributionType](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValues.distributionType "abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD.")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValues.amplitude "abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[fixed](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValues.fixed "abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValues.fixed (Python parameter) — A Boolean specifying whether the boundary condition should remain fixed at the current values at the start of the step.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/MaterialFlowBC.py#L111-L143)[¶](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValues "Permalink to this definition")
    :   This method modifies the data for an existing MaterialFlowBC object in the step where it is created.

        Note

        Check [MaterialFlowBC.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-materialflowbcpyc.htm?contextscope=all#simaker-materialflowbcsetvaluespyc).

        Parameters:[¶](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValues-parameters "Permalink to this headline")
        :   fieldName=`''`[¶](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValues.fieldName "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this boundary
                condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
                default value is an empty string.

            magnitude=`0`[¶](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValues.magnitude "Permalink to this definition")
            :   A Float specifying the material flow magnitude. The default value is 0. The **magnitude**
                argument is optional if **distributionType** = USER\_DEFINED.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            fixed=`0`[¶](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValues.fixed "Permalink to this definition")
            :   A Boolean specifying whether the boundary condition should remain fixed at the current
                values at the start of the step. The default value is OFF.

    setValuesInStep(*[stepName](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValuesInStep.stepName "abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition is modified.")*, *[magnitude](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValuesInStep.magnitude "abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValuesInStep.magnitude (Python parameter) — A Float or the SymbolicConstant FREED specifying the material flow magnitude.")=`abaqusConstants.UNCHANGED`*, *[amplitude](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValuesInStep.amplitude "abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/MaterialFlowBC.py#L145-L168)[¶](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing MaterialFlowBC object in the specified
        step.

        Note

        Check [MaterialFlowBC.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-materialflowbcpyc.htm?contextscope=all#simaker-materialflowbcsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is modified.

            magnitude=`abaqusConstants.UNCHANGED`[¶](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float or the SymbolicConstant FREED specifying the material flow magnitude.

            amplitude=`''`[¶](#abaqus.BoundaryCondition.MaterialFlowBC.MaterialFlowBC.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                boundary condition is changed to have no amplitude reference. You should provide the
                **amplitude** argument only if it is valid for the specified step.

*class* MaterialFlowBCState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/MaterialFlowBCState.py#L9-L57)[¶](#abaqus.BoundaryCondition.MaterialFlowBCState.MaterialFlowBCState "Permalink to this definition")
:   Bases: [`BoundaryConditionState`](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState "abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState (Python class)")

    The MaterialFlowBCState object stores the propagating data for a connector material flow boundary
    condition in a step. One instance of this object is created internally by the MaterialFlowBC object for each
    step. The instance is also deleted internally by the MaterialFlowBC object. The MaterialFlowBCState object
    has no constructor or methods. The MaterialFlowBCState object is derived from the BoundaryConditionState
    object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].boundaryConditionStates[name]
    ```

    The corresponding analysis keywords are:

    * BOUNDARY

    Note

    Check [MaterialFlowBCState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-materialflowbcstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/MaterialFlowBCState.py#L9-L57)[¶](#abaqus.BoundaryCondition.MaterialFlowBCState.MaterialFlowBCState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the
        boundary condition has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/MaterialFlowBCState.py)[¶](#abaqus.BoundaryCondition.MaterialFlowBCState.MaterialFlowBCState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/MaterialFlowBCState.py#L28-L29)[¶](#abaqus.BoundaryCondition.MaterialFlowBCState.MaterialFlowBCState.magnitude "Permalink to this definition")
    :   A Float specifying the material flow magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/MaterialFlowBCState.py)[¶](#abaqus.BoundaryCondition.MaterialFlowBCState.MaterialFlowBCState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the material flow magnitude.
        Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/MaterialFlowBCState.py)[¶](#abaqus.BoundaryCondition.MaterialFlowBCState.MaterialFlowBCState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * PROPAGATED\_FROM\_BASE\_STATE
        * MODIFIED\_FROM\_BASE\_STATE
        * DEACTIVATED\_FROM\_BASE\_STATE
        * BUILT\_INTO\_MODES

*class* PorePressureBC(*[name](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC "abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.__init__.name (Python parameter)")*, *[createStepName](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC "abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.__init__.createStepName (Python parameter)")*, *[region](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC "abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.__init__.region (Python parameter)")*, *[fieldName](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC "abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.__init__.fieldName (Python parameter)")=`''`*, *[magnitude](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC "abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.__init__.magnitude (Python parameter)")=`0`*, *[distributionType](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC "abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC "abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[fixed](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC "abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.__init__.fixed (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/PorePressureBC.py#L22-L168)[¶](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC "Permalink to this definition")
:   Bases: [`BoundaryCondition`](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition "abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition (Python class)")

    The PorePressureBC object stores the data for a pore pressure boundary condition. The PorePressureBC
    object is derived from the BoundaryCondition object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name]
    ```

    Note

    Check [PorePressureBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-porepressurebcpyc.htm?contextscope=all).

    Member Details:

    category : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/PorePressureBC.py)[¶](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.category "Permalink to this definition")
    :   A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/PorePressureBC.py#L37-L39)[¶](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
        Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

    fieldName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/PorePressureBC.py#L41-L44)[¶](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.fieldName "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this boundary
        condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
        default value is an empty string.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/PorePressureBC.py#L53-L56)[¶](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the boundary
        condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/PorePressureBC.py#L34-L35)[¶](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.name "Permalink to this definition")
    :   A String specifying the boundary condition repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/PorePressureBC.py#L50-L51)[¶](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.region "Permalink to this definition")
    :   A Region object specifying the region to which the boundary condition is applied.

    setValues(*[fieldName](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValues.fieldName "abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValues.fieldName (Python parameter) — A String specifying the name of the AnalyticalField object associated with this boundary condition.")=`''`*, *[magnitude](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValues.magnitude "abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValues.magnitude (Python parameter) — A Float specifying the pore pressure magnitude.")=`0`*, *[distributionType](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValues.distributionType "abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD.")=`abaqusConstants.UNIFORM`*, *[amplitude](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValues.amplitude "abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[fixed](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValues.fixed "abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValues.fixed (Python parameter) — A Boolean specifying whether the boundary condition should remain fixed at the current values at the start of the step.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/PorePressureBC.py#L111-L143)[¶](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValues "Permalink to this definition")
    :   This method modifies the data for an existing PorePressureBC object in the step where it is created.

        Note

        Check [PorePressureBC.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-porepressurebcpyc.htm?contextscope=all#simaker-porepressurebcsetvaluespyc).

        Parameters:[¶](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValues-parameters "Permalink to this headline")
        :   fieldName=`''`[¶](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValues.fieldName "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this boundary
                condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
                default value is an empty string.

            magnitude=`0`[¶](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValues.magnitude "Permalink to this definition")
            :   A Float specifying the pore pressure magnitude. The default value is 0. The **magnitude**
                argument is optional if **distributionType** = USER\_DEFINED.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            fixed=`0`[¶](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValues.fixed "Permalink to this definition")
            :   A Boolean specifying whether the boundary condition should remain fixed at the current
                values at the start of the step. The default value is OFF.

    setValuesInStep(*[stepName](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValuesInStep.stepName "abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition is modified.")*, *[magnitude](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValuesInStep.magnitude "abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValuesInStep.magnitude (Python parameter) — A Float or the SymbolicConstant FREED specifying the pore pressure magnitude.")=`abaqusConstants.UNCHANGED`*, *[amplitude](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValuesInStep.amplitude "abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/PorePressureBC.py#L145-L168)[¶](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing PorePressureBC object in the specified
        step.

        Note

        Check [PorePressureBC.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-porepressurebcpyc.htm?contextscope=all#simaker-porepressurebcsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is modified.

            magnitude=`abaqusConstants.UNCHANGED`[¶](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float or the SymbolicConstant FREED specifying the pore pressure magnitude.

            amplitude=`''`[¶](#abaqus.BoundaryCondition.PorePressureBC.PorePressureBC.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                boundary condition is changed to have no amplitude reference. You should provide the
                **amplitude** argument only if it is valid for the specified step.

*class* PorePressureBCState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/PorePressureBCState.py#L9-L56)[¶](#abaqus.BoundaryCondition.PorePressureBCState.PorePressureBCState "Permalink to this definition")
:   Bases: [`BoundaryConditionState`](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState "abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState (Python class)")

    The PorePressureBCState object stores the propagating data for a pore pressure boundary condition in a
    step. One instance of this object is created internally by the PorePressureBC object for each step. The
    instance is also deleted internally by the PorePressureBC object. The PorePressureBCState object has no
    constructor or methods. The PorePressureBCState object is derived from the BoundaryConditionState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].boundaryConditionStates[name]
    ```

    The corresponding analysis keywords are:

    * BOUNDARY

    Note

    Check [PorePressureBCState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-porepressurebcstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/PorePressureBCState.py#L9-L56)[¶](#abaqus.BoundaryCondition.PorePressureBCState.PorePressureBCState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the
        boundary condition has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/PorePressureBCState.py)[¶](#abaqus.BoundaryCondition.PorePressureBCState.PorePressureBCState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/PorePressureBCState.py#L27-L28)[¶](#abaqus.BoundaryCondition.PorePressureBCState.PorePressureBCState.magnitude "Permalink to this definition")
    :   A Float specifying the pore pressure magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/PorePressureBCState.py)[¶](#abaqus.BoundaryCondition.PorePressureBCState.PorePressureBCState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the pore pressure magnitude.
        Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/PorePressureBCState.py)[¶](#abaqus.BoundaryCondition.PorePressureBCState.PorePressureBCState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * PROPAGATED\_FROM\_BASE\_STATE
        * MODIFIED\_FROM\_BASE\_STATE
        * DEACTIVATED\_FROM\_BASE\_STATE
        * BUILT\_INTO\_MODES

*class* RetainedNodalDofsBC(*[name](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC "abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.__init__.name (Python parameter)")*, *[createStepName](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC "abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.__init__.createStepName (Python parameter)")*, *[region](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC "abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.__init__.region (Python parameter)")*, *[u1](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC "abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.__init__.u1 (Python parameter)")=`0`*, *[u2](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC "abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.__init__.u2 (Python parameter)")=`0`*, *[u3](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC "abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.__init__.u3 (Python parameter)")=`0`*, *[ur1](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC "abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.__init__.ur1 (Python parameter)")=`0`*, *[ur2](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC "abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.__init__.ur2 (Python parameter)")=`0`*, *[ur3](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC "abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.__init__.ur3 (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/RetainedNodalDofsBC.py#L10-L167)[¶](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC "Permalink to this definition")
:   Bases: [`BoundaryCondition`](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition "abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition (Python class)")

    The RetainedNodalDofsBC object stores the data for a retained nodal dofs boundary condition. The
    RetainedNodalDofsBC object is derived from the BoundaryCondition object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name]
    ```

    Note

    Check [RetainedNodalDofsBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-retainednodaldofsbcpyc.htm?contextscope=all).

    Member Details:

    category : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/RetainedNodalDofsBC.py)[¶](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.category "Permalink to this definition")
    :   A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/RetainedNodalDofsBC.py#L32-L35)[¶](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the boundary
        condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/RetainedNodalDofsBC.py#L22-L23)[¶](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.name "Permalink to this definition")
    :   A String specifying the boundary condition repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/RetainedNodalDofsBC.py#L29-L30)[¶](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.region "Permalink to this definition")
    :   A Region object specifying the region to which the boundary condition is applied.

    setValues(*[u1](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValues.u1 "abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValues.u1 (Python parameter) — A Boolean specifying whether to retain the degree of freedom in the 1-direction.")=`0`*, *[u2](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValues.u2 "abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValues.u2 (Python parameter) — A Boolean specifying whether to retain the degree of freedom in the 2-direction.")=`0`*, *[u3](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValues.u3 "abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValues.u3 (Python parameter) — A Boolean specifying whether to retain the degree of freedom in the 3-direction.")=`0`*, *[ur1](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValues.ur1 "abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValues.ur1 (Python parameter) — A Boolean specifying whether to retain the rotational degree of freedom about the 1-direction.")=`0`*, *[ur2](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValues.ur2 "abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValues.ur2 (Python parameter) — A Boolean specifying whether to retain the rotational degree of freedom about the 2-direction.")=`0`*, *[ur3](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValues.ur3 "abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValues.ur3 (Python parameter) — A Boolean specifying whether to retain the rotational degree of freedom about the 3-direction.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/RetainedNodalDofsBC.py#L94-L131)[¶](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValues "Permalink to this definition")
    :   This method modifies the data for an existing RetainedNodalDofsBC object in the step where it is
        created.

        Note

        Check [RetainedNodalDofsBC.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-retainednodaldofsbcpyc.htm?contextscope=all#simaker-retainednodaldofsbcsetvaluespyc).

        Parameters:[¶](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValues-parameters "Permalink to this headline")
        :   u1=`0`[¶](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValues.u1 "Permalink to this definition")
            :   A Boolean specifying whether to retain the degree of freedom in the 1-direction. The
                default value is OFF indicating that the degree of freedom is not retained.

            u2=`0`[¶](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValues.u2 "Permalink to this definition")
            :   A Boolean specifying whether to retain the degree of freedom in the 2-direction. The
                default value is OFF indicating that the degree of freedom is not retained.

            u3=`0`[¶](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValues.u3 "Permalink to this definition")
            :   A Boolean specifying whether to retain the degree of freedom in the 3-direction. The
                default value is OFF indicating that the degree of freedom is not retained.

            ur1=`0`[¶](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValues.ur1 "Permalink to this definition")
            :   A Boolean specifying whether to retain the rotational degree of freedom about the
                1-direction. The default value is OFF indicating that the degree of freedom is not
                retained.

            ur2=`0`[¶](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValues.ur2 "Permalink to this definition")
            :   A Boolean specifying whether to retain the rotational degree of freedom about the
                2-direction. The default value is OFF indicating that the degree of freedom is not
                retained.

            ur3=`0`[¶](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValues.ur3 "Permalink to this definition")
            :   A Boolean specifying whether to retain the rotational degree of freedom about the
                3-direction. The default value is OFF indicating that the degree of freedom is not
                retained.

    setValuesInStep(*[stepName](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValuesInStep.stepName "abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition is modified.")*, *[u1](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValuesInStep.u1 "abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValuesInStep.u1 (Python parameter) — A Boolean specifying whether to retain the degree of freedom in the 1-direction.")=`0`*, *[u2](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValuesInStep.u2 "abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValuesInStep.u2 (Python parameter) — A Boolean specifying whether to retain the degree of freedom in the 2-direction.")=`0`*, *[u3](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValuesInStep.u3 "abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValuesInStep.u3 (Python parameter) — A Boolean specifying whether to retain the degree of freedom in the 3-direction.")=`0`*, *[ur1](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValuesInStep.ur1 "abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValuesInStep.ur1 (Python parameter) — A Boolean specifying whether to retain the rotational degree of freedom about the 1-direction.")=`0`*, *[ur2](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValuesInStep.ur2 "abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValuesInStep.ur2 (Python parameter) — A Boolean specifying whether to retain the rotational degree of freedom about the 2-direction.")=`0`*, *[ur3](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValuesInStep.ur3 "abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValuesInStep.ur3 (Python parameter) — A Boolean specifying whether to retain the rotational degree of freedom about the 3-direction.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/RetainedNodalDofsBC.py#L133-L167)[¶](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing RetainedNodalDofsBC object in the specified
        step.

        Note

        Check [RetainedNodalDofsBC.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-retainednodaldofsbcpyc.htm?contextscope=all#simaker-retainednodaldofsbcsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is modified.

            u1=`0`[¶](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValuesInStep.u1 "Permalink to this definition")
            :   A Boolean specifying whether to retain the degree of freedom in the 1-direction.

            u2=`0`[¶](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValuesInStep.u2 "Permalink to this definition")
            :   A Boolean specifying whether to retain the degree of freedom in the 2-direction.

            u3=`0`[¶](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValuesInStep.u3 "Permalink to this definition")
            :   A Boolean specifying whether to retain the degree of freedom in the 3-direction.

            ur1=`0`[¶](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValuesInStep.ur1 "Permalink to this definition")
            :   A Boolean specifying whether to retain the rotational degree of freedom about the
                1-direction.

            ur2=`0`[¶](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValuesInStep.ur2 "Permalink to this definition")
            :   A Boolean specifying whether to retain the rotational degree of freedom about the
                2-direction.

            ur3=`0`[¶](#abaqus.BoundaryCondition.RetainedNodalDofsBC.RetainedNodalDofsBC.setValuesInStep.ur3 "Permalink to this definition")
            :   A Boolean specifying whether to retain the rotational degree of freedom about the
                3-direction.

*class* SecondaryBaseBC(*[name](#abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC "abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC.__init__.name (Python parameter)")*, *[createStepName](#abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC "abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC.__init__.createStepName (Python parameter)")*, *[regions](#abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC "abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC.__init__.regions (Python parameter)")*, *[dofs](#abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC "abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC.__init__.dofs (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SecondaryBaseBC.py#L11-L89)[¶](#abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC "Permalink to this definition")
:   Bases: [`BoundaryCondition`](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition "abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition (Python class)")

    The SecondaryBaseBC object stores the data for a secondary base boundary condition. The SecondaryBaseBC
    object is derived from the BoundaryCondition object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name]
    ```

    Note

    Check [SecondaryBaseBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-secondarybasebcpyc.htm?contextscope=all).

    Member Details:

    category : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SecondaryBaseBC.py)[¶](#abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC.category "Permalink to this definition")
    :   A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.

    dofs : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SecondaryBaseBC.py#L26-L27)[¶](#abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC.dofs "Permalink to this definition")
    :   A tuple of tuples of Ints specifying the constrained degrees-of-freedom.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SecondaryBaseBC.py#L40-L43)[¶](#abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the boundary
        condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SecondaryBaseBC.py#L23-L24)[¶](#abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC.name "Permalink to this definition")
    :   A String specifying the boundary condition repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SecondaryBaseBC.py#L37-L38)[¶](#abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC.region "Permalink to this definition")
    :   A Region object specifying the region to which the boundary condition is applied.

    regions : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Region.Region.Region`] = `'MODEL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SecondaryBaseBC.py#L29-L31)[¶](#abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC.regions "Permalink to this definition")
    :   A RegionArray object specifying the region to which the boundary condition is applied.
        Note that the usual **region** is ignored. The default value is MODEL.

    setValues(*\*[args](#abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC.setValues "abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC.setValues.args (Python parameter)")*, *\*\*[kwargs](#abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC.setValues "abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC.setValues.kwargs (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SecondaryBaseBC.py#L73-L77)[¶](#abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC.setValues "Permalink to this definition")
    :   This method modifies the data for an existing SecondaryBaseBC object in the step where it is
        created.

    setValuesInStep(*[stepName](#abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC.setValuesInStep.stepName "abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition is modified.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SecondaryBaseBC.py#L79-L89)[¶](#abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing SecondaryBaseBC object in the specified
        step.

        Note

        Check [SecondaryBaseBC.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-secondarybasebcpyc.htm?contextscope=all#simaker-secondarybasebcsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.SecondaryBaseBC.SecondaryBaseBC.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is modified.

*class* SecondaryBaseBCState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SecondaryBaseBCState.py#L9-L49)[¶](#abaqus.BoundaryCondition.SecondaryBaseBCState.SecondaryBaseBCState "Permalink to this definition")
:   Bases: [`BoundaryConditionState`](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState "abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState (Python class)")

    The SecondaryBaseBCState object stores the propagating data for a secondary base boundary condition in a
    step. One instance of this object is created internally by the SecondaryBaseBC object for each step. The
    instance is also deleted internally by the SecondaryBaseBC object. The SecondaryBaseBCState object has no
    constructor or methods. The SecondaryBaseBCState object is derived from the BoundaryConditionState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].boundaryConditionStates[name]
    ```

    The corresponding analysis keywords are:

    * BOUNDARY

    Note

    Check [SecondaryBaseBCState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-secondarybasebcstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SecondaryBaseBCState.py#L9-L49)[¶](#abaqus.BoundaryCondition.SecondaryBaseBCState.SecondaryBaseBCState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the
        boundary condition has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SecondaryBaseBCState.py)[¶](#abaqus.BoundaryCondition.SecondaryBaseBCState.SecondaryBaseBCState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SecondaryBaseBCState.py)[¶](#abaqus.BoundaryCondition.SecondaryBaseBCState.SecondaryBaseBCState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * PROPAGATED\_FROM\_BASE\_STATE
        * MODIFIED\_FROM\_BASE\_STATE
        * DEACTIVATED\_FROM\_BASE\_STATE
        * BUILT\_INTO\_MODES

*class* SubmodelBC(*[name](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.__init__.name (Python parameter)")*, *[createStepName](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.__init__.createStepName (Python parameter)")*, *[region](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.__init__.region (Python parameter)")*, *[dof](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.__init__.dof (Python parameter)")*, *[globalStep](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.__init__.globalStep (Python parameter)")*, *[timeScale](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.__init__.timeScale (Python parameter)")*, *[shellThickness](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.__init__.shellThickness (Python parameter)")*, *[globalDrivingRegion](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.__init__.globalDrivingRegion (Python parameter)")=`''`*, *[absoluteExteriorTolerance](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.__init__.absoluteExteriorTolerance (Python parameter)")=`None`*, *[exteriorTolerance](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.__init__.exteriorTolerance (Python parameter)")=`0`*, *[localCsys](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.__init__.localCsys (Python parameter)")=`None`*, *[globalIncrement](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.__init__.globalIncrement (Python parameter)")=`0`*, *[centerZoneSize](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.__init__.centerZoneSize (Python parameter)")=`None`*, *[intersectionOnly](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.__init__.intersectionOnly (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBC.py#L10-L220)[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC "Permalink to this definition")
:   Bases: [`BoundaryCondition`](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition "abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition (Python class)")

    The SubmodelBC object stores the data for a submodel boundary condition. The SubmodelBC object is derived
    from the BoundaryCondition object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name]
    ```

    Note

    Check [SubmodelBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-submodelbcpyc.htm?contextscope=all).

    Member Details:

    absoluteExteriorTolerance : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBC.py#L30-L32)[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.absoluteExteriorTolerance "Permalink to this definition")
    :   None or a Float specifying the absolute value by which a driven node of the submodel can
        lie outside the region of the elements of the global model. The default value is None.

    category : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBC.py)[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.category "Permalink to this definition")
    :   A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.

    exteriorTolerance : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBC.py#L34-L37)[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.exteriorTolerance "Permalink to this definition")
    :   None or a Float specifying the fraction of the average element size in the global model
        by which a driven node of the submodel can lie outside the region of the elements of the
        global model. The default value is 0.05.

    globalDrivingRegion : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBC.py#L39-L42)[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.globalDrivingRegion "Permalink to this definition")
    :   A String specifying the element set in the global model that will be searched for
        elements whose responses will be used to drive the submodel. An empty string indicates
        that the entire global model will be searched. The default value is an empty string.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBC.py#L51-L54)[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the boundary
        condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBC.py#L22-L23)[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.name "Permalink to this definition")
    :   A String specifying the boundary condition repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBC.py#L48-L49)[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.region "Permalink to this definition")
    :   A Region object specifying the region to which the boundary condition is applied.

    setValues(*[globalDrivingRegion](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValues.globalDrivingRegion "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValues.globalDrivingRegion (Python parameter) — A String specifying the element set in the global model that will be searched for elements whose responses will be used to drive the submodel.")=`''`*, *[absoluteExteriorTolerance](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValues.absoluteExteriorTolerance "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValues.absoluteExteriorTolerance (Python parameter) — None or a Float specifying the absolute value by which a driven node of the submodel can lie outside the region of the elements of the global model.")=`None`*, *[exteriorTolerance](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValues.exteriorTolerance "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValues.exteriorTolerance (Python parameter) — None or a Float specifying the fraction of the average element size in the global model by which a driven node of the submodel can lie outside the region of the elements of the global model.")=`0`*, *[localCsys](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValues.localCsys "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValues.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*, *[globalIncrement](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValues.globalIncrement "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValues.globalIncrement (Python parameter) — An Int specifying the increment number in the global model step from which the solution will be used to specify the values of the driven variables.")=`0`*, *[centerZoneSize](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValues.centerZoneSize "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValues.centerZoneSize (Python parameter) — A Float specifying the thickness of the center zone size around the shell midsurface. The default value is None.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBC.py#L142-L180)[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValues "Permalink to this definition")
    :   This method modifies the data for an existing SubmodelBC object in the step where it is created.

        Note

        Check [SubmodelBC.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-submodelbcpyc.htm?contextscope=all#simaker-submodelbcsetvaluespyc).

        Parameters:[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValues-parameters "Permalink to this headline")
        :   globalDrivingRegion=`''`[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValues.globalDrivingRegion "Permalink to this definition")
            :   A String specifying the element set in the global model that will be searched for
                elements whose responses will be used to drive the submodel. An empty string indicates
                that the entire global model will be searched. The default value is an empty string.

            absoluteExteriorTolerance=`None`[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValues.absoluteExteriorTolerance "Permalink to this definition")
            :   None or a Float specifying the absolute value by which a driven node of the submodel can
                lie outside the region of the elements of the global model. The default value is None.

            exteriorTolerance=`0`[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValues.exteriorTolerance "Permalink to this definition")
            :   None or a Float specifying the fraction of the average element size in the global model
                by which a driven node of the submodel can lie outside the region of the elements of the
                global model. The default value is 0.05.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValues.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

            globalIncrement=`0`[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValues.globalIncrement "Permalink to this definition")
            :   An Int specifying the increment number in the global model step from which the solution
                will be used to specify the values of the driven variables. If **globalIncrement** = 0, the
                solution from the last increment will be used. The **globalIncrement** argument is
                applicable only for linear perturbation steps. The default value is 0.

            centerZoneSize=`None`[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValues.centerZoneSize "Permalink to this definition")
            :   A Float specifying the thickness of the center zone size around the shell midsurface.
                The default value is None.

    setValuesInStep(*[stepName](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValuesInStep.stepName "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition is modified.")*, *[fixed](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValuesInStep.fixed "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValuesInStep.fixed (Python parameter) — A Boolean specifying whether the boundary condition should remain fixed at the current values at the start of the step.")=`1`*, *[dof](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValuesInStep.dof "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValuesInStep.dof (Python parameter) — A sequence of Ints specifying the degrees of freedom to which the boundary condition is applied.")=`()`*, *[globalStep](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValuesInStep.globalStep "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValuesInStep.globalStep (Python parameter) — A String specifying the step in the global model from which Abaqus reads the values of the variables that will drive the submodel analysis.")=`''`*, *[globalIncrement](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValuesInStep.globalIncrement "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValuesInStep.globalIncrement (Python parameter) — An Int specifying the increment number in the global model step at which the solution will be used to specify the values of the driven variables.")=`0`*, *[centerZoneSize](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValuesInStep.centerZoneSize "abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValuesInStep.centerZoneSize (Python parameter) — A Float specifying the thickness of the center zone size around the shell midsurface. The default value is None.The centerZoneSize argument is applicable only if fixed = OFF.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBC.py#L182-L220)[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing SubmodelBC object in the specified step.

        Note

        Check [SubmodelBC.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-submodelbcpyc.htm?contextscope=all#simaker-submodelbcsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is modified.

            fixed=`1`[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValuesInStep.fixed "Permalink to this definition")
            :   A Boolean specifying whether the boundary condition should remain fixed at the current
                values at the start of the step. The default value is ON.

            dof=`()`[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValuesInStep.dof "Permalink to this definition")
            :   A sequence of Ints specifying the degrees of freedom to which the boundary condition is
                applied. The **dof** argument is applicable only if **fixed** = OFF.

            globalStep=`''`[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValuesInStep.globalStep "Permalink to this definition")
            :   A String specifying the step in the global model from which Abaqus reads the values of
                the variables that will drive the submodel analysis. The String indicates the position
                of the step in the sequence of analysis steps. For example, **globalStep** = ‘1’ indicates
                the first step. The **globalStep** argument is applicable only if **fixed** = OFF.

            globalIncrement=`0`[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValuesInStep.globalIncrement "Permalink to this definition")
            :   An Int specifying the increment number in the global model step at which the solution
                will be used to specify the values of the driven variables. If **globalIncrement** = 0, the
                solution from the last increment will be used. The **globalIncrement** argument is
                applicable only for linear perturbation steps and if **fixed** = OFF. The default value is
                0.

            centerZoneSize=`None`[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.setValuesInStep.centerZoneSize "Permalink to this definition")
            :   A Float specifying the thickness of the center zone size around the shell midsurface.
                The default value is None.The **centerZoneSize** argument is applicable only if
                **fixed** = OFF.

    shellThickness : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBC.py#L25-L28)[¶](#abaqus.BoundaryCondition.SubmodelBC.SubmodelBC.shellThickness "Permalink to this definition")
    :   A Float specifying the thickness of the shell in the global model. This argument is
        required for shell-to-solid submodeling and is not applicable to other submodels. The
        default value is 0.0.

*class* SubmodelBCState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBCState.py#L9-L93)[¶](#abaqus.BoundaryCondition.SubmodelBCState.SubmodelBCState "Permalink to this definition")
:   Bases: [`BoundaryConditionState`](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState "abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState (Python class)")

    The SubmodelBCState object stores the propagating data for a Submodel boundary condition in a step. One
    instance of this object is created internally by the SubmodelBC object for each step. The instance is also
    deleted internally by the SubmodelBC object. The SubmodelBCState object has no constructor or methods. The
    SubmodelBCState object is derived from the BoundaryConditionState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].boundaryConditionStates[name]
    ```

    The corresponding analysis keywords are:

    * SUBMODEL
    * BOUNDARY

    Note

    Check [SubmodelBCState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-submodelbcstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBCState.py#L9-L93)[¶](#abaqus.BoundaryCondition.SubmodelBCState.SubmodelBCState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the
        boundary condition has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBCState.py)[¶](#abaqus.BoundaryCondition.SubmodelBCState.SubmodelBCState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    centerZoneSize : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBCState.py#L45-L47)[¶](#abaqus.BoundaryCondition.SubmodelBCState.SubmodelBCState.centerZoneSize "Permalink to this definition")
    :   None or a Float specifying the thickness of the center zone size around the shell
        midsurface. The default value is None.

    centerZoneSizefState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBCState.py)[¶](#abaqus.BoundaryCondition.SubmodelBCState.SubmodelBCState.centerZoneSizefState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **centerZoneSize** member.
        Possible values are SET and UNCHANGED.

    dof : --is-rst--:py:class:`tuple`\[:py:class:`int`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBCState.py#L67-L69)[¶](#abaqus.BoundaryCondition.SubmodelBCState.SubmodelBCState.dof "Permalink to this definition")
    :   A tuple of Ints specifying the degrees of freedom to which the boundary condition is
        applied.

    dofState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBCState.py)[¶](#abaqus.BoundaryCondition.SubmodelBCState.SubmodelBCState.dofState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **dof** member. Possible values
        are SET and UNCHANGED.

    globalIncrement : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBCState.py#L36-L39)[¶](#abaqus.BoundaryCondition.SubmodelBCState.SubmodelBCState.globalIncrement "Permalink to this definition")
    :   An Int specifying the increment number in the global model step at which the solution
        will be used to specify the values of the driven variables. This argument is applicable
        only for linear perturbation steps.

    globalIncrementState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBCState.py)[¶](#abaqus.BoundaryCondition.SubmodelBCState.SubmodelBCState.globalIncrementState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **globalIncrement** member.
        Possible values are SET and UNCHANGED.

    globalStep : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBCState.py#L61-L65)[¶](#abaqus.BoundaryCondition.SubmodelBCState.SubmodelBCState.globalStep "Permalink to this definition")
    :   A String specifying the step in the global model from which Abaqus reads the values of
        the variables that will drive the submodel analysis. The String indicates the position
        of the step in the sequence of analysis steps. For example, **globalStep** = ‘1’ indicates
        the first step.

    globalStepState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBCState.py)[¶](#abaqus.BoundaryCondition.SubmodelBCState.SubmodelBCState.globalStepState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **globalStep** member. Possible
        values are SET and UNCHANGED.

    scale : --is-rst--:py:class:`float` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBCState.py#L53-L55)[¶](#abaqus.BoundaryCondition.SubmodelBCState.SubmodelBCState.scale "Permalink to this definition")
    :   None or a Float specifying a scaling value applied to the applied displacements at the
        interface. The default value is 1.0.

    scaleState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBCState.py)[¶](#abaqus.BoundaryCondition.SubmodelBCState.SubmodelBCState.scaleState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **scale** member. Possible
        values are SET and UNCHANGED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/SubmodelBCState.py)[¶](#abaqus.BoundaryCondition.SubmodelBCState.SubmodelBCState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * PROPAGATED\_FROM\_BASE\_STATE
        * MODIFIED\_FROM\_BASE\_STATE
        * DEACTIVATED\_FROM\_BASE\_STATE
        * BUILT\_INTO\_MODES

*class* TemperatureBC(*[name](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC "abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.__init__.name (Python parameter)")*, *[createStepName](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC "abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.__init__.createStepName (Python parameter)")*, *[region](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC "abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.__init__.region (Python parameter)")*, *[fieldName](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC "abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.__init__.fieldName (Python parameter)")=`''`*, *[magnitude](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC "abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.__init__.magnitude (Python parameter)")=`0`*, *[dof](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC "abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.__init__.dof (Python parameter)")=`()`*, *[amplitude](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC "abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC "abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*, *[fixed](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC "abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.__init__.fixed (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TemperatureBC.py#L22-L177)[¶](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC "Permalink to this definition")
:   Bases: [`BoundaryCondition`](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition "abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition (Python class)")

    The TemperatureBC object stores the data for a temperature boundary condition. The TemperatureBC object
    is derived from the BoundaryCondition object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name]
    ```

    Note

    Check [TemperatureBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-temperaturebcpyc.htm?contextscope=all).

    Member Details:

    category : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TemperatureBC.py)[¶](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.category "Permalink to this definition")
    :   A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TemperatureBC.py#L37-L39)[¶](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
        Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

    fieldName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TemperatureBC.py#L41-L44)[¶](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.fieldName "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this boundary
        condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
        default value is an empty string.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TemperatureBC.py#L53-L56)[¶](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the boundary
        condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TemperatureBC.py#L34-L35)[¶](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.name "Permalink to this definition")
    :   A String specifying the boundary condition repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TemperatureBC.py#L50-L51)[¶](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.region "Permalink to this definition")
    :   A Region object specifying the region to which the boundary condition is applied.

    setValues(*[fieldName](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValues.fieldName "abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValues.fieldName (Python parameter) — A String specifying the name of the AnalyticalField object associated with this boundary condition.")=`''`*, *[magnitude](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValues.magnitude "abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValues.magnitude (Python parameter) — A Float specifying the temperature magnitude.")=`0`*, *[dof](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValues.dof "abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValues.dof (Python parameter) — A sequence of Ints specifying the degrees of freedom to which the boundary condition is applied.")=`()`*, *[amplitude](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValues.amplitude "abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[distributionType](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValues.distributionType "abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD.")=`abaqusConstants.UNIFORM`*, *[fixed](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValues.fixed "abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValues.fixed (Python parameter) — A Boolean specifying whether the boundary condition should remain fixed at the current values at the start of the step.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TemperatureBC.py#L114-L149)[¶](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValues "Permalink to this definition")
    :   This method modifies the data for an existing TemperatureBC object in the step where it is created.

        Note

        Check [TemperatureBC.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-temperaturebcpyc.htm?contextscope=all#simaker-temperaturebcsetvaluespyc).

        Parameters:[¶](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValues-parameters "Permalink to this headline")
        :   fieldName=`''`[¶](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValues.fieldName "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this boundary
                condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
                default value is an empty string.

            magnitude=`0`[¶](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValues.magnitude "Permalink to this definition")
            :   A Float specifying the temperature magnitude. The default value is 0.

            dof=`()`[¶](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValues.dof "Permalink to this definition")
            :   A sequence of Ints specifying the degrees of freedom to which the boundary condition is
                applied. The default value is (11,).

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

            fixed=`0`[¶](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValues.fixed "Permalink to this definition")
            :   A Boolean specifying whether the boundary condition should remain fixed at the current
                values at the start of the step. The default value is OFF.

    setValuesInStep(*[stepName](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValuesInStep.stepName "abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition is modified.")*, *[magnitude](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValuesInStep.magnitude "abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValuesInStep.magnitude (Python parameter) — A Float or the SymbolicConstant FREED specifying the temperature magnitude.")=`abaqusConstants.UNCHANGED`*, *[dof](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValuesInStep.dof "abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValuesInStep.dof (Python parameter) — A sequence of Ints specifying the degrees of freedom to which the boundary condition is applied.")=`()`*, *[amplitude](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValuesInStep.amplitude "abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TemperatureBC.py#L151-L177)[¶](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing TemperatureBC object in the specified step.

        Note

        Check [TemperatureBC.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-temperaturebcpyc.htm?contextscope=all#simaker-temperaturebcsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is modified.

            magnitude=`abaqusConstants.UNCHANGED`[¶](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValuesInStep.magnitude "Permalink to this definition")
            :   A Float or the SymbolicConstant FREED specifying the temperature magnitude.

            dof=`()`[¶](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValuesInStep.dof "Permalink to this definition")
            :   A sequence of Ints specifying the degrees of freedom to which the boundary condition is
                applied.

            amplitude=`''`[¶](#abaqus.BoundaryCondition.TemperatureBC.TemperatureBC.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                boundary condition is changed to have no amplitude reference. You should provide the
                **amplitude** argument only if it is valid for the specified step.

*class* TemperatureBCState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TemperatureBCState.py#L9-L64)[¶](#abaqus.BoundaryCondition.TemperatureBCState.TemperatureBCState "Permalink to this definition")
:   Bases: [`BoundaryConditionState`](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState "abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState (Python class)")

    The TemperatureBCState object stores the propagating data for a temperature boundary condition in a step.
    One instance of this object is created internally by the TemperatureBC object for each step. The instance is
    also deleted internally by the TemperatureBC object. The TemperatureBCState object has no constructor or
    methods. The TemperatureBCState object is derived from the BoundaryConditionState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].boundaryConditionStates[name]
    ```

    The corresponding analysis keywords are:

    * BOUNDARY

    Note

    Check [TemperatureBCState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-temperaturebcstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TemperatureBCState.py#L9-L64)[¶](#abaqus.BoundaryCondition.TemperatureBCState.TemperatureBCState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the
        boundary condition has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TemperatureBCState.py)[¶](#abaqus.BoundaryCondition.TemperatureBCState.TemperatureBCState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    dof : --is-rst--:py:class:`tuple`\[:py:class:`int`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TemperatureBCState.py#L38-L40)[¶](#abaqus.BoundaryCondition.TemperatureBCState.TemperatureBCState.dof "Permalink to this definition")
    :   A tuple of Ints specifying the degrees of freedom to which the boundary condition is
        applied.

    dofState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TemperatureBCState.py)[¶](#abaqus.BoundaryCondition.TemperatureBCState.TemperatureBCState.dofState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the **dof** member. Possible values
        are SET and UNCHANGED.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TemperatureBCState.py#L27-L28)[¶](#abaqus.BoundaryCondition.TemperatureBCState.TemperatureBCState.magnitude "Permalink to this definition")
    :   A Float specifying the temperature magnitude.

    magnitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TemperatureBCState.py)[¶](#abaqus.BoundaryCondition.TemperatureBCState.TemperatureBCState.magnitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the temperature magnitude.
        Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TemperatureBCState.py)[¶](#abaqus.BoundaryCondition.TemperatureBCState.TemperatureBCState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * PROPAGATED\_FROM\_BASE\_STATE
        * MODIFIED\_FROM\_BASE\_STATE
        * DEACTIVATED\_FROM\_BASE\_STATE
        * BUILT\_INTO\_MODES

*class* TypeBC(*[name](#abaqus.BoundaryCondition.TypeBC.TypeBC "abaqus.BoundaryCondition.TypeBC.TypeBC.__init__.name (Python parameter)")*, *[createStepName](#abaqus.BoundaryCondition.TypeBC.TypeBC "abaqus.BoundaryCondition.TypeBC.TypeBC.__init__.createStepName (Python parameter)")*, *[region](#abaqus.BoundaryCondition.TypeBC.TypeBC "abaqus.BoundaryCondition.TypeBC.TypeBC.__init__.region (Python parameter)")*, *[buckleCase](#abaqus.BoundaryCondition.TypeBC.TypeBC "abaqus.BoundaryCondition.TypeBC.TypeBC.__init__.buckleCase (Python parameter)")=`abaqusConstants.NOT_APPLICABLE`*, *[localCsys](#abaqus.BoundaryCondition.TypeBC.TypeBC "abaqus.BoundaryCondition.TypeBC.TypeBC.__init__.localCsys (Python parameter)")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TypeBC.py#L13-L465)[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC "Permalink to this definition")
:   Bases: [`BoundaryCondition`](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition "abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition (Python class)")

    The TypeBC object stores the data for several types of predefined boundary conditions that are commonly
    used in stress/displacement analyses. The TypeBC object is derived from the BoundaryCondition object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name]
    ```

    Note

    Check [TypeBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-typebcpyc.htm?contextscope=all).

    Member Details:

    *static* EncastreBC(*[name](#abaqus.BoundaryCondition.TypeBC.TypeBC.EncastreBC.name "abaqus.BoundaryCondition.TypeBC.TypeBC.EncastreBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.TypeBC.TypeBC.EncastreBC.createStepName "abaqus.BoundaryCondition.TypeBC.TypeBC.EncastreBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.TypeBC.TypeBC.EncastreBC.region "abaqus.BoundaryCondition.TypeBC.TypeBC.EncastreBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[buckleCase](#abaqus.BoundaryCondition.TypeBC.TypeBC.EncastreBC.buckleCase "abaqus.BoundaryCondition.TypeBC.TypeBC.EncastreBC.buckleCase (Python parameter) — A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE analysis.")=`abaqusConstants.NOT_APPLICABLE`*, *[localCsys](#abaqus.BoundaryCondition.TypeBC.TypeBC.EncastreBC.localCsys "abaqus.BoundaryCondition.TypeBC.TypeBC.EncastreBC.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TypeBC.py#L93-L131)[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.EncastreBC "Permalink to this definition")
    :   This method creates an encastre TypeBC object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].EncastreBC
        ```

        Note

        Check [EncastreBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-encastrebcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.EncastreBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.EncastreBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.EncastreBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.EncastreBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            buckleCase=`abaqusConstants.NOT_APPLICABLE`[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.EncastreBC.buckleCase "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
                analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
                PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.EncastreBC.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

        Returns:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.EncastreBC-returns "Permalink to this headline")
        :   A TypeBC object.

        Return type:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.EncastreBC-return-type "Permalink to this headline")
        :   [`TypeBC`](#abaqus.BoundaryCondition.TypeBC.TypeBC "abaqus.BoundaryCondition.TypeBC.TypeBC (Python class) — Bases: BoundaryCondition")

    *static* PinnedBC(*[name](#abaqus.BoundaryCondition.TypeBC.TypeBC.PinnedBC.name "abaqus.BoundaryCondition.TypeBC.TypeBC.PinnedBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.TypeBC.TypeBC.PinnedBC.createStepName "abaqus.BoundaryCondition.TypeBC.TypeBC.PinnedBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.TypeBC.TypeBC.PinnedBC.region "abaqus.BoundaryCondition.TypeBC.TypeBC.PinnedBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[buckleCase](#abaqus.BoundaryCondition.TypeBC.TypeBC.PinnedBC.buckleCase "abaqus.BoundaryCondition.TypeBC.TypeBC.PinnedBC.buckleCase (Python parameter) — A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE analysis.")=`abaqusConstants.NOT_APPLICABLE`*, *[localCsys](#abaqus.BoundaryCondition.TypeBC.TypeBC.PinnedBC.localCsys "abaqus.BoundaryCondition.TypeBC.TypeBC.PinnedBC.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TypeBC.py#L133-L171)[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.PinnedBC "Permalink to this definition")
    :   This method creates a pinned TypeBC object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].PinnedBC
        ```

        Note

        Check [PinnedBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-pinnedbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.PinnedBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.PinnedBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.PinnedBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.PinnedBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            buckleCase=`abaqusConstants.NOT_APPLICABLE`[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.PinnedBC.buckleCase "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
                analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
                PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.PinnedBC.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

        Returns:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.PinnedBC-returns "Permalink to this headline")
        :   A TypeBC object.

        Return type:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.PinnedBC-return-type "Permalink to this headline")
        :   [`TypeBC`](#abaqus.BoundaryCondition.TypeBC.TypeBC "abaqus.BoundaryCondition.TypeBC.TypeBC (Python class) — Bases: BoundaryCondition")

    *static* XasymmBC(*[name](#abaqus.BoundaryCondition.TypeBC.TypeBC.XasymmBC.name "abaqus.BoundaryCondition.TypeBC.TypeBC.XasymmBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.TypeBC.TypeBC.XasymmBC.createStepName "abaqus.BoundaryCondition.TypeBC.TypeBC.XasymmBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.TypeBC.TypeBC.XasymmBC.region "abaqus.BoundaryCondition.TypeBC.TypeBC.XasymmBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[buckleCase](#abaqus.BoundaryCondition.TypeBC.TypeBC.XasymmBC.buckleCase "abaqus.BoundaryCondition.TypeBC.TypeBC.XasymmBC.buckleCase (Python parameter) — A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE analysis.")=`abaqusConstants.NOT_APPLICABLE`*, *[localCsys](#abaqus.BoundaryCondition.TypeBC.TypeBC.XasymmBC.localCsys "abaqus.BoundaryCondition.TypeBC.TypeBC.XasymmBC.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TypeBC.py#L293-L331)[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.XasymmBC "Permalink to this definition")
    :   This method creates a TypeBC object that specifies antisymmetry about the **X** axis.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].XasymmBC
        ```

        Note

        Check [XasymmBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xasymmbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.XasymmBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.XasymmBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.XasymmBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.XasymmBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            buckleCase=`abaqusConstants.NOT_APPLICABLE`[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.XasymmBC.buckleCase "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
                analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
                PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.XasymmBC.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

        Returns:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.XasymmBC-returns "Permalink to this headline")
        :   A TypeBC object.

        Return type:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.XasymmBC-return-type "Permalink to this headline")
        :   [`TypeBC`](#abaqus.BoundaryCondition.TypeBC.TypeBC "abaqus.BoundaryCondition.TypeBC.TypeBC (Python class) — Bases: BoundaryCondition")

    *static* XsymmBC(*[name](#abaqus.BoundaryCondition.TypeBC.TypeBC.XsymmBC.name "abaqus.BoundaryCondition.TypeBC.TypeBC.XsymmBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.TypeBC.TypeBC.XsymmBC.createStepName "abaqus.BoundaryCondition.TypeBC.TypeBC.XsymmBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.TypeBC.TypeBC.XsymmBC.region "abaqus.BoundaryCondition.TypeBC.TypeBC.XsymmBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[buckleCase](#abaqus.BoundaryCondition.TypeBC.TypeBC.XsymmBC.buckleCase "abaqus.BoundaryCondition.TypeBC.TypeBC.XsymmBC.buckleCase (Python parameter) — A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE analysis.")=`abaqusConstants.NOT_APPLICABLE`*, *[localCsys](#abaqus.BoundaryCondition.TypeBC.TypeBC.XsymmBC.localCsys "abaqus.BoundaryCondition.TypeBC.TypeBC.XsymmBC.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TypeBC.py#L173-L211)[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.XsymmBC "Permalink to this definition")
    :   This method creates a TypeBC object that specifies symmetry about the **X** axis.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].XsymmBC
        ```

        Note

        Check [XsymmBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xsymmbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.XsymmBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.XsymmBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.XsymmBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.XsymmBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            buckleCase=`abaqusConstants.NOT_APPLICABLE`[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.XsymmBC.buckleCase "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
                analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
                PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.XsymmBC.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

        Returns:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.XsymmBC-returns "Permalink to this headline")
        :   A TypeBC object.

        Return type:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.XsymmBC-return-type "Permalink to this headline")
        :   [`TypeBC`](#abaqus.BoundaryCondition.TypeBC.TypeBC "abaqus.BoundaryCondition.TypeBC.TypeBC (Python class) — Bases: BoundaryCondition")

    *static* YasymmBC(*[name](#abaqus.BoundaryCondition.TypeBC.TypeBC.YasymmBC.name "abaqus.BoundaryCondition.TypeBC.TypeBC.YasymmBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.TypeBC.TypeBC.YasymmBC.createStepName "abaqus.BoundaryCondition.TypeBC.TypeBC.YasymmBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.TypeBC.TypeBC.YasymmBC.region "abaqus.BoundaryCondition.TypeBC.TypeBC.YasymmBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[buckleCase](#abaqus.BoundaryCondition.TypeBC.TypeBC.YasymmBC.buckleCase "abaqus.BoundaryCondition.TypeBC.TypeBC.YasymmBC.buckleCase (Python parameter) — A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE analysis.")=`abaqusConstants.NOT_APPLICABLE`*, *[localCsys](#abaqus.BoundaryCondition.TypeBC.TypeBC.YasymmBC.localCsys "abaqus.BoundaryCondition.TypeBC.TypeBC.YasymmBC.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TypeBC.py#L333-L371)[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.YasymmBC "Permalink to this definition")
    :   This method creates a TypeBC object that specifies antisymmetry about the **Y** axis.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].YasymmBC
        ```

        Note

        Check [YasymmBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-yasymmbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.YasymmBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.YasymmBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.YasymmBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.YasymmBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            buckleCase=`abaqusConstants.NOT_APPLICABLE`[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.YasymmBC.buckleCase "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
                analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
                PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.YasymmBC.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

        Returns:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.YasymmBC-returns "Permalink to this headline")
        :   A TypeBC object.

        Return type:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.YasymmBC-return-type "Permalink to this headline")
        :   [`TypeBC`](#abaqus.BoundaryCondition.TypeBC.TypeBC "abaqus.BoundaryCondition.TypeBC.TypeBC (Python class) — Bases: BoundaryCondition")

    *static* YsymmBC(*[name](#abaqus.BoundaryCondition.TypeBC.TypeBC.YsymmBC.name "abaqus.BoundaryCondition.TypeBC.TypeBC.YsymmBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.TypeBC.TypeBC.YsymmBC.createStepName "abaqus.BoundaryCondition.TypeBC.TypeBC.YsymmBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.TypeBC.TypeBC.YsymmBC.region "abaqus.BoundaryCondition.TypeBC.TypeBC.YsymmBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[buckleCase](#abaqus.BoundaryCondition.TypeBC.TypeBC.YsymmBC.buckleCase "abaqus.BoundaryCondition.TypeBC.TypeBC.YsymmBC.buckleCase (Python parameter) — A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE analysis.")=`abaqusConstants.NOT_APPLICABLE`*, *[localCsys](#abaqus.BoundaryCondition.TypeBC.TypeBC.YsymmBC.localCsys "abaqus.BoundaryCondition.TypeBC.TypeBC.YsymmBC.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TypeBC.py#L213-L251)[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.YsymmBC "Permalink to this definition")
    :   This method creates a TypeBC object that specifies symmetry about the **Y** axis.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].YsymmBC
        ```

        Note

        Check [YsymmBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ysymmbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.YsymmBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.YsymmBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.YsymmBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.YsymmBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            buckleCase=`abaqusConstants.NOT_APPLICABLE`[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.YsymmBC.buckleCase "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
                analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
                PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.YsymmBC.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

        Returns:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.YsymmBC-returns "Permalink to this headline")
        :   A TypeBC object.

        Return type:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.YsymmBC-return-type "Permalink to this headline")
        :   [`TypeBC`](#abaqus.BoundaryCondition.TypeBC.TypeBC "abaqus.BoundaryCondition.TypeBC.TypeBC (Python class) — Bases: BoundaryCondition")

    *static* ZasymmBC(*[name](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZasymmBC.name "abaqus.BoundaryCondition.TypeBC.TypeBC.ZasymmBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZasymmBC.createStepName "abaqus.BoundaryCondition.TypeBC.TypeBC.ZasymmBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZasymmBC.region "abaqus.BoundaryCondition.TypeBC.TypeBC.ZasymmBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[buckleCase](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZasymmBC.buckleCase "abaqus.BoundaryCondition.TypeBC.TypeBC.ZasymmBC.buckleCase (Python parameter) — A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE analysis.")=`abaqusConstants.NOT_APPLICABLE`*, *[localCsys](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZasymmBC.localCsys "abaqus.BoundaryCondition.TypeBC.TypeBC.ZasymmBC.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TypeBC.py#L373-L411)[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZasymmBC "Permalink to this definition")
    :   This method creates a TypeBC object that specifies antisymmetry about the **Z** axis.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ZasymmBC
        ```

        Note

        Check [ZasymmBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-zasymmbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZasymmBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZasymmBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZasymmBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZasymmBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            buckleCase=`abaqusConstants.NOT_APPLICABLE`[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZasymmBC.buckleCase "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
                analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
                PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZasymmBC.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

        Returns:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZasymmBC-returns "Permalink to this headline")
        :   A TypeBC object.

        Return type:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZasymmBC-return-type "Permalink to this headline")
        :   [`TypeBC`](#abaqus.BoundaryCondition.TypeBC.TypeBC "abaqus.BoundaryCondition.TypeBC.TypeBC (Python class) — Bases: BoundaryCondition")

    *static* ZsymmBC(*[name](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZsymmBC.name "abaqus.BoundaryCondition.TypeBC.TypeBC.ZsymmBC.name (Python parameter) — A String specifying the boundary condition repository key.")*, *[createStepName](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZsymmBC.createStepName "abaqus.BoundaryCondition.TypeBC.TypeBC.ZsymmBC.createStepName (Python parameter) — A String specifying the name of the step in which the boundary condition is created.")*, *[region](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZsymmBC.region "abaqus.BoundaryCondition.TypeBC.TypeBC.ZsymmBC.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[buckleCase](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZsymmBC.buckleCase "abaqus.BoundaryCondition.TypeBC.TypeBC.ZsymmBC.buckleCase (Python parameter) — A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE analysis.")=`abaqusConstants.NOT_APPLICABLE`*, *[localCsys](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZsymmBC.localCsys "abaqus.BoundaryCondition.TypeBC.TypeBC.ZsymmBC.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TypeBC.py#L253-L291)[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZsymmBC "Permalink to this definition")
    :   This method creates a TypeBC object that specifies symmetry about the **Z** axis.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ZsymmBC
        ```

        Note

        Check [ZsymmBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-zsymmbcpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZsymmBC-parameters "Permalink to this headline")
        :   name[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZsymmBC.name "Permalink to this definition")
            :   A String specifying the boundary condition repository key.

            createStepName[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZsymmBC.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is created.

            region[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZsymmBC.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            buckleCase=`abaqusConstants.NOT_APPLICABLE`[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZsymmBC.buckleCase "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
                analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
                PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZsymmBC.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

        Returns:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZsymmBC-returns "Permalink to this headline")
        :   A TypeBC object.

        Return type:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.ZsymmBC-return-type "Permalink to this headline")
        :   [`TypeBC`](#abaqus.BoundaryCondition.TypeBC.TypeBC "abaqus.BoundaryCondition.TypeBC.TypeBC (Python class) — Bases: BoundaryCondition")

    buckleCase : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'NOT_APPLICABLE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TypeBC.py#L28-L31)[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.buckleCase "Permalink to this definition")
    :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
        analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
        PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

    category : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TypeBC.py)[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.category "Permalink to this definition")
    :   A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TypeBC.py#L40-L43)[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the boundary
        condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TypeBC.py#L25-L26)[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.name "Permalink to this definition")
    :   A String specifying the boundary condition repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TypeBC.py#L37-L38)[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.region "Permalink to this definition")
    :   A Region object specifying the region to which the boundary condition is applied.

    setValues(*[region](#abaqus.BoundaryCondition.TypeBC.TypeBC.setValues.region "abaqus.BoundaryCondition.TypeBC.TypeBC.setValues.region (Python parameter) — A Region object specifying the region to which the boundary condition is applied.")*, *[typeName](#abaqus.BoundaryCondition.TypeBC.TypeBC.setValues.typeName "abaqus.BoundaryCondition.TypeBC.TypeBC.setValues.typeName (Python parameter) — A SymbolicConstant specifying the predefined boundary condition type.")=`None`*, *[buckleCase](#abaqus.BoundaryCondition.TypeBC.TypeBC.setValues.buckleCase "abaqus.BoundaryCondition.TypeBC.TypeBC.setValues.buckleCase (Python parameter) — A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE analysis.")=`abaqusConstants.NOT_APPLICABLE`*, *[localCsys](#abaqus.BoundaryCondition.TypeBC.TypeBC.setValues.localCsys "abaqus.BoundaryCondition.TypeBC.TypeBC.setValues.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TypeBC.py#L413-L441)[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.setValues "Permalink to this definition")
    :   This method modifies the data for an existing TypeBC object in the step where it is created.

        Note

        Check [TypeBC.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-typebcpyc.htm?contextscope=all#simaker-typebcsetvaluespyc).

        Parameters:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.setValues-parameters "Permalink to this headline")
        :   region[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.setValues.region "Permalink to this definition")
            :   A Region object specifying the region to which the boundary condition is applied.

            typeName=`None`[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.setValues.typeName "Permalink to this definition")
            :   A SymbolicConstant specifying the predefined boundary condition type. Possible values
                are XSYMM, YSYMM, ZSYMM, XASYMM, YASYMM, ZASYMM, PINNED, and ENCASTRE.

            buckleCase=`abaqusConstants.NOT_APPLICABLE`[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.setValues.buckleCase "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is defined in a BUCKLE
                analysis. Possible values are NOT\_APPLICABLE, STRESS\_PERTURBATION, BUCKLING\_MODES, and
                PERTURBATION\_AND\_BUCKLING. The default value is NOT\_APPLICABLE.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.setValues.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

    setValuesInStep(*[stepName](#abaqus.BoundaryCondition.TypeBC.TypeBC.setValuesInStep.stepName "abaqus.BoundaryCondition.TypeBC.TypeBC.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition is modified.")*, *[typeName](#abaqus.BoundaryCondition.TypeBC.TypeBC.setValuesInStep.typeName "abaqus.BoundaryCondition.TypeBC.TypeBC.setValuesInStep.typeName (Python parameter) — A SymbolicConstant specifying the predefined boundary condition type.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TypeBC.py#L443-L465)[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.setValuesInStep "Permalink to this definition")
    :   This method always returns a value error for a TypeBC; it is inherited from the BoundaryCondition
        object.

        Note

        Check [TypeBC.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-typebcpyc.htm?contextscope=all#simaker-typebcsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is modified.

            typeName=`None`[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.setValuesInStep.typeName "Permalink to this definition")
            :   A SymbolicConstant specifying the predefined boundary condition type. Possible values
                are XSYMM, YSYMM, ZSYMM, XASYMM, YASYMM, ZASYMM, PINNED, and ENCASTRE.

        Raises:[¶](#abaqus.BoundaryCondition.TypeBC.TypeBC.setValuesInStep-raises "Permalink to this headline")
        :   **Value Error** – A Symmetry/Antisymmetry/Encastre BC cannot be edited in a propagated step.

*class* VelocityBC(*[name](#abaqus.BoundaryCondition.VelocityBC.VelocityBC "abaqus.BoundaryCondition.VelocityBC.VelocityBC.__init__.name (Python parameter)")*, *[createStepName](#abaqus.BoundaryCondition.VelocityBC.VelocityBC "abaqus.BoundaryCondition.VelocityBC.VelocityBC.__init__.createStepName (Python parameter)")*, *[region](#abaqus.BoundaryCondition.VelocityBC.VelocityBC "abaqus.BoundaryCondition.VelocityBC.VelocityBC.__init__.region (Python parameter)")*, *[fieldName](#abaqus.BoundaryCondition.VelocityBC.VelocityBC "abaqus.BoundaryCondition.VelocityBC.VelocityBC.__init__.fieldName (Python parameter)")=`''`*, *[v1](#abaqus.BoundaryCondition.VelocityBC.VelocityBC "abaqus.BoundaryCondition.VelocityBC.VelocityBC.__init__.v1 (Python parameter)")=`abaqusConstants.UNSET`*, *[v2](#abaqus.BoundaryCondition.VelocityBC.VelocityBC "abaqus.BoundaryCondition.VelocityBC.VelocityBC.__init__.v2 (Python parameter)")=`abaqusConstants.UNSET`*, *[v3](#abaqus.BoundaryCondition.VelocityBC.VelocityBC "abaqus.BoundaryCondition.VelocityBC.VelocityBC.__init__.v3 (Python parameter)")=`abaqusConstants.UNSET`*, *[vr1](#abaqus.BoundaryCondition.VelocityBC.VelocityBC "abaqus.BoundaryCondition.VelocityBC.VelocityBC.__init__.vr1 (Python parameter)")=`abaqusConstants.UNSET`*, *[vr2](#abaqus.BoundaryCondition.VelocityBC.VelocityBC "abaqus.BoundaryCondition.VelocityBC.VelocityBC.__init__.vr2 (Python parameter)")=`abaqusConstants.UNSET`*, *[vr3](#abaqus.BoundaryCondition.VelocityBC.VelocityBC "abaqus.BoundaryCondition.VelocityBC.VelocityBC.__init__.vr3 (Python parameter)")=`abaqusConstants.UNSET`*, *[amplitude](#abaqus.BoundaryCondition.VelocityBC.VelocityBC "abaqus.BoundaryCondition.VelocityBC.VelocityBC.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*, *[localCsys](#abaqus.BoundaryCondition.VelocityBC.VelocityBC "abaqus.BoundaryCondition.VelocityBC.VelocityBC.__init__.localCsys (Python parameter)")=`None`*, *[distributionType](#abaqus.BoundaryCondition.VelocityBC.VelocityBC "abaqus.BoundaryCondition.VelocityBC.VelocityBC.__init__.distributionType (Python parameter)")=`abaqusConstants.UNIFORM`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBC.py#L15-L233)[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC "Permalink to this definition")
:   Bases: [`BoundaryCondition`](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition "abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition (Python class)")

    The VelocityBC object stores the data for a velocity boundary condition. The VelocityBC object is derived
    from the BoundaryCondition object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name]
    ```

    Note

    Check [VelocityBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-velocitybcpyc.htm?contextscope=all).

    Member Details:

    category : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBC.py)[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.category "Permalink to this definition")
    :   A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.

    distributionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNIFORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBC.py#L30-L32)[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.distributionType "Permalink to this definition")
    :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
        Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

    fieldName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBC.py#L34-L37)[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.fieldName "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField object associated with this boundary
        condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
        default value is an empty string.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBC.py#L46-L49)[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the boundary
        condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBC.py#L27-L28)[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.name "Permalink to this definition")
    :   A String specifying the boundary condition repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBC.py#L43-L44)[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.region "Permalink to this definition")
    :   A Region object specifying the region to which the boundary condition is applied.

    setValues(*[fieldName](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.fieldName "abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.fieldName (Python parameter) — A String specifying the name of the AnalyticalField object associated with this boundary condition.")=`''`*, *[v1](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.v1 "abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.v1 (Python parameter) — A Float or a SymbolicConstant specifying the velocity component in the 1-direction. Possible values for the SymbolicConstant are UNSET and SET.")=`abaqusConstants.UNSET`*, *[v2](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.v2 "abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.v2 (Python parameter) — A Float or a SymbolicConstant specifying the velocity component in the 2-direction. Possible values for the SymbolicConstant are UNSET and SET.")=`abaqusConstants.UNSET`*, *[v3](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.v3 "abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.v3 (Python parameter) — A Float or a SymbolicConstant specifying the velocity component in the 3-direction. Possible values for the SymbolicConstant are UNSET and SET.")=`abaqusConstants.UNSET`*, *[vr1](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.vr1 "abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.vr1 (Python parameter) — A Float or a SymbolicConstant specifying the rotational velocity component about the 1-direction.")=`abaqusConstants.UNSET`*, *[vr2](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.vr2 "abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.vr2 (Python parameter) — A Float or a SymbolicConstant specifying the rotational velocity component about the 2-direction.")=`abaqusConstants.UNSET`*, *[vr3](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.vr3 "abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.vr3 (Python parameter) — A Float or a SymbolicConstant specifying the rotational velocity component about the 3-direction.")=`abaqusConstants.UNSET`*, *[amplitude](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.amplitude "abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*, *[localCsys](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.localCsys "abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the boundary condition's degrees of freedom.")=`None`*, *[distributionType](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.distributionType "abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.distributionType (Python parameter) — A SymbolicConstant specifying how the boundary condition is distributed spatially. Possible values are UNIFORM, USER_DEFINED, and FIELD.")=`abaqusConstants.UNIFORM`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBC.py#L130-L188)[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues "Permalink to this definition")
    :   This method modifies the data for an existing VelocityBC object in the step where it is created.

        Note

        Check [VelocityBC.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-velocitybcpyc.htm?contextscope=all#simaker-velocitybcsetvaluespyc).

        Parameters:[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues-parameters "Permalink to this headline")
        :   fieldName=`''`[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.fieldName "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField object associated with this boundary
                condition. The **fieldName** argument applies only when **distributionType** = FIELD. The
                default value is an empty string.

            v1=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.v1 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the velocity component in the 1-direction.
                Possible values for the SymbolicConstant are UNSET and SET. The default value is
                UNSET. Note: Although **v1**, **v2**, **v3**, **vr1**, **vr2**, and **vr3** are optional arguments, at
                least one of them must be specified.

            v2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.v2 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the velocity component in the 2-direction.
                Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

            v3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.v3 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the velocity component in the 3-direction.
                Possible values for the SymbolicConstant are UNSET and SET. The default value is UNSET.

            vr1=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.vr1 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational velocity component about the
                1-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET.

            vr2=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.vr2 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational velocity component about the
                2-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET.

            vr3=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.vr3 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational velocity component about the
                3-direction. Possible values for the SymbolicConstant are UNSET and SET. The default
                value is UNSET.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

            localCsys=`None`[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the boundary
                condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
                in the global coordinate system. The default value is None.

            distributionType=`abaqusConstants.UNIFORM`[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValues.distributionType "Permalink to this definition")
            :   A SymbolicConstant specifying how the boundary condition is distributed spatially.
                Possible values are UNIFORM, USER\_DEFINED, and FIELD. The default value is UNIFORM.

    setValuesInStep(*[stepName](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep.stepName "abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition is modified.")*, *[v1](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep.v1 "abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep.v1 (Python parameter) — A Float or a SymbolicConstant specifying the velocity component in the 1-direction. Possible values for the SymbolicConstant are SET and FREED.")=`abaqusConstants.SET`*, *[v2](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep.v2 "abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep.v2 (Python parameter) — A Float or a SymbolicConstant specifying the velocity component in the 2-direction. Possible values for the SymbolicConstant are SET and FREED.")=`abaqusConstants.SET`*, *[v3](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep.v3 "abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep.v3 (Python parameter) — A Float or a SymbolicConstant specifying the velocity component in the 3-direction. Possible values for the SymbolicConstant are SET and FREED.")=`abaqusConstants.SET`*, *[vr1](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep.vr1 "abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep.vr1 (Python parameter) — A Float or a SymbolicConstant specifying the rotational velocity component about the 1-direction.")=`abaqusConstants.SET`*, *[vr2](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep.vr2 "abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep.vr2 (Python parameter) — A Float or a SymbolicConstant specifying the rotational velocity component about the 2-direction.")=`abaqusConstants.SET`*, *[vr3](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep.vr3 "abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep.vr3 (Python parameter) — A Float or a SymbolicConstant specifying the rotational velocity component about the 3-direction.")=`abaqusConstants.SET`*, *[amplitude](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep.amplitude "abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBC.py#L190-L233)[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing VelocityBC object in the specified step.

        Note

        Check [VelocityBC.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-velocitybcpyc.htm?contextscope=all#simaker-velocitybcsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is modified.

            v1=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep.v1 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the velocity component in the 1-direction.
                Possible values for the SymbolicConstant are SET and FREED.

            v2=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep.v2 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the velocity component in the 2-direction.
                Possible values for the SymbolicConstant are SET and FREED.

            v3=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep.v3 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the velocity component in the 3-direction.
                Possible values for the SymbolicConstant are SET and FREED.

            vr1=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep.vr1 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational velocity component about the
                1-direction. Possible values for the SymbolicConstant are SET and FREED.

            vr2=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep.vr2 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational velocity component about the
                2-direction. Possible values for the SymbolicConstant are SET and FREED.

            vr3=`abaqusConstants.SET`[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep.vr3 "Permalink to this definition")
            :   A Float or a SymbolicConstant specifying the rotational velocity component about the
                3-direction. Possible values for the SymbolicConstant are SET and FREED.

            amplitude=`''`[¶](#abaqus.BoundaryCondition.VelocityBC.VelocityBC.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                boundary condition is changed to have no amplitude reference. You should provide the
                **amplitude** argument only if it is valid for the specified step.

*class* VelocityBCState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBCState.py#L9-L91)[¶](#abaqus.BoundaryCondition.VelocityBCState.VelocityBCState "Permalink to this definition")
:   Bases: [`BoundaryConditionState`](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState "abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState (Python class)")

    The VelocityBCState object stores the propagating data for a velocity boundary condition in a step. One
    instance of this object is created internally by the VelocityBC object for each step. The instance is also
    deleted internally by the VelocityBC object. The VelocityBCState object has no constructor or methods. The
    VelocityBCState object is derived from the BoundaryConditionState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].boundaryConditionStates[name]
    ```

    The corresponding analysis keywords are:

    * BOUNDARY

    Note

    Check [VelocityBCState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-velocitybcstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBCState.py#L9-L91)[¶](#abaqus.BoundaryCondition.VelocityBCState.VelocityBCState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the
        boundary condition has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBCState.py)[¶](#abaqus.BoundaryCondition.VelocityBCState.VelocityBCState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBCState.py)[¶](#abaqus.BoundaryCondition.VelocityBCState.VelocityBCState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * PROPAGATED\_FROM\_BASE\_STATE
        * MODIFIED\_FROM\_BASE\_STATE
        * DEACTIVATED\_FROM\_BASE\_STATE
        * BUILT\_INTO\_MODES

    v1 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBCState.py#L27-L28)[¶](#abaqus.BoundaryCondition.VelocityBCState.VelocityBCState.v1 "Permalink to this definition")
    :   A Float specifying the velocity component in the 1-direction.

    v1State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBCState.py)[¶](#abaqus.BoundaryCondition.VelocityBCState.VelocityBCState.v1State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the velocity component in the
        1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    v2 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBCState.py#L30-L31)[¶](#abaqus.BoundaryCondition.VelocityBCState.VelocityBCState.v2 "Permalink to this definition")
    :   A Float specifying the velocity component in the 2-direction.

    v2State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBCState.py)[¶](#abaqus.BoundaryCondition.VelocityBCState.VelocityBCState.v2State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the velocity component in the
        2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    v3 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBCState.py#L33-L34)[¶](#abaqus.BoundaryCondition.VelocityBCState.VelocityBCState.v3 "Permalink to this definition")
    :   A Float specifying the velocity component in the 3-direction.

    v3State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBCState.py)[¶](#abaqus.BoundaryCondition.VelocityBCState.VelocityBCState.v3State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the velocity component in the
        3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    vr1 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBCState.py#L36-L37)[¶](#abaqus.BoundaryCondition.VelocityBCState.VelocityBCState.vr1 "Permalink to this definition")
    :   A Float specifying the rotational velocity component about the 1-direction.

    vr1State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBCState.py)[¶](#abaqus.BoundaryCondition.VelocityBCState.VelocityBCState.vr1State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the rotational velocity component
        about the 1-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    vr2 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBCState.py#L39-L40)[¶](#abaqus.BoundaryCondition.VelocityBCState.VelocityBCState.vr2 "Permalink to this definition")
    :   A Float specifying the rotational velocity component about the 2-direction.

    vr2State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBCState.py)[¶](#abaqus.BoundaryCondition.VelocityBCState.VelocityBCState.vr2State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the rotational velocity component
        about the 2-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    vr3 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBCState.py#L42-L43)[¶](#abaqus.BoundaryCondition.VelocityBCState.VelocityBCState.vr3 "Permalink to this definition")
    :   A Float specifying the rotational velocity component about the 3-direction.

    vr3State : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBCState.py)[¶](#abaqus.BoundaryCondition.VelocityBCState.VelocityBCState.vr3State "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the rotational velocity component
        about the 3-direction. Possible values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

*class* VelocityBaseMotionBC(*[name](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC "abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.__init__.name (Python parameter)")*, *[createStepName](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC "abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.__init__.createStepName (Python parameter)")*, *[dof](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC "abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.__init__.dof (Python parameter)")*, *[amplitudeScaleFactor](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC "abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.__init__.amplitudeScaleFactor (Python parameter)")=`1`*, *[centerOfRotation](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC "abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.__init__.centerOfRotation (Python parameter)")=`()`*, *[correlation](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC "abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.__init__.correlation (Python parameter)")=`None`*, *[secondaryBase](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC "abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.__init__.secondaryBase (Python parameter)")=`''`*, *[useComplex](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC "abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.__init__.useComplex (Python parameter)")=`0`*, *[amplitude](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC "abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.__init__.amplitude (Python parameter)")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py#L14-L166)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC "Permalink to this definition")
:   Bases: [`BoundaryCondition`](#abaqus.BoundaryCondition.VelocityBaseMotionBC.BoundaryCondition "abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition (Python class)")

    The VelocityBaseMotionBC object stores the data for a velocity base motion boundary condition. The
    VelocityBaseMotionBC object is derived from the BoundaryCondition object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name]
    ```

    Note

    Check [VelocityBaseMotionBC on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-velocitybasemotionbcpyc.htm?contextscope=all).

    Member Details:

    amplitudeScaleFactor : --is-rst--:py:class:`float` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py#L29-L30)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.amplitudeScaleFactor "Permalink to this definition")
    :   A Float specifying the scale factor for the amplitude curve. The default value is 1.0.

    category : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.category "Permalink to this definition")
    :   A SymbolicConstant specifying the category of the boundary condition. Possible values
        are MECHANICAL and THERMAL.

    centerOfRotation : --is-rst--:py:class:`tuple` = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py#L36-L38)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.centerOfRotation "Permalink to this definition")
    :   A ModelDot object specifying a tuple containing one center of rotation. The default
        value is the global origin. This argument applies only when **dof** = UR1, UR2, or UR3.

    correlation : --is-rst--:py:class:`~abaqus.Amplitude.Correlation.Correlation` = `<abaqus.Amplitude.Correlation.Correlation object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py#L40-L41)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.correlation "Permalink to this definition")
    :   A Correlation object.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py#L54-L57)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the boundary
        condition’s degrees of freedom. If **localCsys** = None, the degrees of freedom are defined
        in the global coordinate system. The default value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py#L26-L27)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.name "Permalink to this definition")
    :   A String specifying the boundary condition repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py#L51-L52)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.region "Permalink to this definition")
    :   A Region object specifying the region to which the boundary condition is applied.

    secondaryBase : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py#L43-L45)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.secondaryBase "Permalink to this definition")
    :   A String specifying the name of the SecondaryBaseBC object associated with this boundary
        condition. The default value is an empty string.

    setValues(*[amplitudeScaleFactor](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValues.amplitudeScaleFactor "abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValues.amplitudeScaleFactor (Python parameter) — A Float specifying the scale factor for the amplitude curve.")=`1`*, *[centerOfRotation](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValues.centerOfRotation "abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValues.centerOfRotation (Python parameter) — A ModelDot object specifying a tuple containing one center of rotation.")=`()`*, *[correlation](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValues.correlation "abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValues.correlation (Python parameter) — A Correlation object.")=`None`*, *[secondaryBase](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValues.secondaryBase "abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValues.secondaryBase (Python parameter) — A String specifying the name of the SecondaryBaseBC object associated with this boundary condition.")=`''`*, *[useComplex](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValues.useComplex "abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValues.useComplex (Python parameter) — A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base motion record given by amplitude definition.")=`0`*, *[amplitude](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValues.amplitude "abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValues.amplitude (Python parameter) — A String or the SymbolicConstant UNSET specifying the name of the amplitude reference. UNSET should be used if the boundary condition has no amplitude reference.")=`abaqusConstants.UNSET`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py#L114-L148)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValues "Permalink to this definition")
    :   This method modifies the data for an existing VelocityBaseMotionBC object in the step where it is
        created.

        Note

        Check [VelocityBaseMotionBC.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-velocitybasemotionbcpyc.htm?contextscope=all#simaker-velocitybasemotionbcsetvaluespyc).

        Parameters:[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValues-parameters "Permalink to this headline")
        :   amplitudeScaleFactor=`1`[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValues.amplitudeScaleFactor "Permalink to this definition")
            :   A Float specifying the scale factor for the amplitude curve. The default value is 1.0.

            centerOfRotation=`()`[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValues.centerOfRotation "Permalink to this definition")
            :   A ModelDot object specifying a tuple containing one center of rotation. The default
                value is the global origin. This argument applies only when **dof** = UR1, UR2, or UR3.

            correlation=`None`[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValues.correlation "Permalink to this definition")
            :   A Correlation object.

            secondaryBase=`''`[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValues.secondaryBase "Permalink to this definition")
            :   A String specifying the name of the SecondaryBaseBC object associated with this boundary
                condition. The default value is an empty string.

            useComplex=`0`[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValues.useComplex "Permalink to this definition")
            :   A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base
                motion record given by amplitude definition. The default value is OFF.

            amplitude=`abaqusConstants.UNSET`[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValues.amplitude "Permalink to this definition")
            :   A String or the SymbolicConstant UNSET specifying the name of the amplitude reference.
                UNSET should be used if the boundary condition has no amplitude reference. The default
                value is UNSET. You should provide the **amplitude** argument only if it is valid for the
                specified step.

    setValuesInStep(*[stepName](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValuesInStep.stepName "abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the boundary condition is modified.")*, *[amplitude](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValuesInStep.amplitude "abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValuesInStep.amplitude (Python parameter) — A String or a SymbolicConstant specifying the name of the amplitude reference.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py#L150-L166)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing VelocityBaseMotionBC object in the
        specified step.

        Note

        Check [VelocityBaseMotionBC.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-velocitybasemotionbcpyc.htm?contextscope=all#simaker-velocitybasemotionbcsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the boundary condition is modified.

            amplitude=`''`[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.setValuesInStep.amplitude "Permalink to this definition")
            :   A String or a SymbolicConstant specifying the name of the amplitude reference. Possible
                values for the SymbolicConstant are UNCHANGED and FREED. UNCHANGED should be used if the
                amplitude is propagated from the previous analysis step. FREED should be used if the
                boundary condition is changed to have no amplitude reference. You should provide the
                **amplitude** argument only if it is valid for the specified step.

    useComplex : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBC.py#L32-L34)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBC.VelocityBaseMotionBC.useComplex "Permalink to this definition")
    :   A Boolean specifying whether to define the imaginary (out-of-plane) portion of the base
        motion record given by amplitude definition. The default value is OFF.

*class* VelocityBaseMotionBCState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBCState.py#L9-L50)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.VelocityBaseMotionBCState "Permalink to this definition")
:   Bases: [`BoundaryConditionState`](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState "abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState (Python class)")

    The VelocityBaseMotionBCState object stores the propagating data for a velocity base motion boundary
    condition in a step. One instance of this object is created internally by the VelocityBaseMotionBC object
    for each step. The instance is also deleted internally by the VelocityBaseMotionBC object. The
    VelocityBaseMotionBCState object has no constructor or methods. The VelocityBaseMotionBCState object is
    derived from the BoundaryConditionState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].boundaryConditionStates[name]
    ```

    The corresponding analysis keywords are:

    * BASE MOTION

    Note

    Check [VelocityBaseMotionBCState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-velocitybasemotionbcstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBCState.py#L9-L50)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.VelocityBaseMotionBCState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the
        boundary condition has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBCState.py)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.VelocityBaseMotionBCState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/VelocityBaseMotionBCState.py)[¶](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.VelocityBaseMotionBCState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * PROPAGATED\_FROM\_BASE\_STATE
        * MODIFIED\_FROM\_BASE\_STATE
        * DEACTIVATED\_FROM\_BASE\_STATE
        * BUILT\_INTO\_MODES

*class* TypeBCState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TypeBCState.py#L9-L57)[¶](#abaqus.BoundaryCondition.TypeBCState.TypeBCState "Permalink to this definition")
:   Bases: [`BoundaryConditionState`](#abaqus.BoundaryCondition.VelocityBaseMotionBCState.BoundaryConditionState "abaqus.BoundaryCondition.BoundaryConditionState.BoundaryConditionState (Python class)")

    The TypeBCState object stores the propagating data for a predefined boundary condition in a step. One
    instance of this object is created internally by the TypeBC object for each step. The instance is also
    deleted internally by the TypeBC object. The TypeBCState object has no constructor or methods. The
    TypeBCState object is derived from the BoundaryConditionState object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].steps[name].boundaryConditionStates[name]
    ```

    The corresponding analysis keywords are:

    * BOUNDARY

    Note

    Check [TypeBCState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-typebcstatepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TypeBCState.py#L9-L57)[¶](#abaqus.BoundaryCondition.TypeBCState.TypeBCState.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude reference. The String is empty if the
        boundary condition has no amplitude reference.

    amplitudeState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TypeBCState.py)[¶](#abaqus.BoundaryCondition.TypeBCState.TypeBCState.amplitudeState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the amplitude reference. Possible
        values are UNSET, SET, UNCHANGED, FREED, and MODIFIED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TypeBCState.py)[¶](#abaqus.BoundaryCondition.TypeBCState.TypeBCState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the BoundaryConditionState object. Possible values are:

        * NOT\_YET\_ACTIVE
        * CREATED
        * PROPAGATED
        * MODIFIED
        * DEACTIVATED
        * NO\_LONGER\_ACTIVE
        * TYPE\_NOT\_APPLICABLE
        * INSTANCE\_NOT\_APPLICABLE
        * PROPAGATED\_FROM\_BASE\_STATE
        * MODIFIED\_FROM\_BASE\_STATE
        * DEACTIVATED\_FROM\_BASE\_STATE
        * BUILT\_INTO\_MODES

    typeName : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TypeBCState.py)[¶](#abaqus.BoundaryCondition.TypeBCState.TypeBCState.typeName "Permalink to this definition")
    :   A SymbolicConstant specifying the predefined boundary condition type. Possible values
        are XSYMM, YSYMM, ZSYMM, XASYMM, YASYMM, ZASYMM, PINNED, and ENCASTRE.

    typeNameState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/BoundaryCondition/TypeBCState.py)[¶](#abaqus.BoundaryCondition.TypeBCState.TypeBCState.typeNameState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the predefined boundary condition
        type. The only possible value is UNCHANGED.

[Back to top](#)