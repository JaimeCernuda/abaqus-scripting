# Abaqus MDB_MODEL Module API Reference

> Source: [https://hailin.wang/abqpy/en/2025/reference/mdb/model/index.html](https://hailin.wang/abqpy/en/2025/reference/mdb/model/index.html)
> Downloaded for offline use by Claude Code skills.

---

# Model[¶](#model "Permalink to this heading")

Model commands are used to create Abaqus/CAE models. A finished model contains all the data that Abaqus/CAE needs to create and submit an analysis to Abaqus/Standard or Abaqus/Explicit. Models are stored in a model database.

Objects in Model

* [Adaptivity](adaptivity.html)
* [Amplitude](amplitude.html)
* [Boundary Condition](bc.html)
* [Calibration of Material](calibration.html)
* [Constraint](constraint.html)
* [Field](field.html)
* [Filter](filter.html)
* [Interaction](interaction.html)
* [Load](load.html)
* [Material](material.html)
* [Mesh](mesh.html)
* [Optimization](optimization.html)
* [Output Request](output.html)
* [Part and Assembly](part_assembly/index.html)
* [Predefined Field](predefined.html)
* [Beam Section Profile](profile.html)
* [Property](property.html)
* [Section](section/index.html)
* [Sketcher](sketcher.html)
* [Step](step/index.html)

## Classes[¶](#classes "Permalink to this heading")

### Model[¶](#id1 "Permalink to this heading")

*class* Model(*[name](#abaqus.Model.Model.Model "abaqus.Model.Model.Model.__init__.name (Python parameter)")*, *[description](#abaqus.Model.Model.Model "abaqus.Model.Model.Model.__init__.description (Python parameter)")=`''`*, *[stefanBoltzmann](#abaqus.Model.Model.Model "abaqus.Model.Model.Model.__init__.stefanBoltzmann (Python parameter)")=`None`*, *[absoluteZero](#abaqus.Model.Model.Model "abaqus.Model.Model.Model.__init__.absoluteZero (Python parameter)")=`None`*, *[waveFormulation](#abaqus.Model.Model.Model "abaqus.Model.Model.Model.__init__.waveFormulation (Python parameter)")=`abaqusConstants.NOT_SET`*, *[modelType](#abaqus.Model.Model.Model "abaqus.Model.Model.Model.__init__.modelType (Python parameter)")=`abaqusConstants.STANDARD_EXPLICIT`*, *[universalGas](#abaqus.Model.Model.Model "abaqus.Model.Model.Model.__init__.universalGas (Python parameter)")=`None`*, *[copyConstraints](#abaqus.Model.Model.Model "abaqus.Model.Model.Model.__init__.copyConstraints (Python parameter)")=`1`*, *[copyConnectors](#abaqus.Model.Model.Model "abaqus.Model.Model.Model.__init__.copyConnectors (Python parameter)")=`1`*, *[copyInteractions](#abaqus.Model.Model.Model "abaqus.Model.Model.Model.__init__.copyInteractions (Python parameter)")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/Model.py#L25-L58)[¶](#abaqus.Model.Model.Model "Permalink to this definition")
:   Bases: [`AdaptivityModel`](adaptivity.html#abaqus.Adaptivity.AdaptivityModel.AdaptivityModel "abaqus.Adaptivity.AdaptivityModel.AdaptivityModel (Python class) — Bases: ModelBase"), [`AmplitudeModel`](amplitude.html#abaqus.Amplitude.AmplitudeModel.AmplitudeModel "abaqus.Amplitude.AmplitudeModel.AmplitudeModel (Python class) — Bases: ModelBase"), [`AssemblyModel`](part_assembly/assembly.html#abaqus.Assembly.AssemblyModel.AssemblyModel "abaqus.Assembly.AssemblyModel.AssemblyModel (Python class) — Bases: ModelBase"), [`BoundaryConditionModel`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel (Python class) — Bases: ModelBase"), [`CalibrationModel`](calibration.html#abaqus.Calibration.CalibrationModel.CalibrationModel "abaqus.Calibration.CalibrationModel.CalibrationModel (Python class) — Bases: ModelBase"), [`ConstraintModel`](constraint.html#abaqus.Constraint.ConstraintModel.ConstraintModel "abaqus.Constraint.ConstraintModel.ConstraintModel (Python class) — Bases: ModelBase"), [`FilterModel`](filter.html#abaqus.Filter.FilterModel.FilterModel "abaqus.Filter.FilterModel.FilterModel (Python class) — Bases: ModelBase"), [`InteractionModel`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel "abaqus.Interaction.InteractionModel.InteractionModel (Python class) — Bases: InteractionContactControlModel, InteractionContactInitializationModel, InteractionContactStabilizationModel, InteractionPropertyModel"), [`LoadModel`](load.html#abaqus.Load.LoadModel.LoadModel "abaqus.Load.LoadModel.LoadModel (Python class) — Bases: ModelBase"), [`MaterialModel`](material.html#abaqus.Material.MaterialModel.MaterialModel "abaqus.Material.MaterialModel.MaterialModel (Python class) — Bases: ModelBase"), [`OptimizationTaskModel`](optimization.html#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel (Python class) — Bases: ModelBase"), [`PartModel`](part_assembly/part.html#abaqus.Part.PartModel.PartModel "abaqus.Part.PartModel.PartModel (Python class) — Bases: ModelBase"), [`PredefinedFieldModel`](predefined.html#abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel "abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel (Python class) — Bases: ModelBase"), [`BeamSectionProfileModel`](profile.html#abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel "abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel (Python class) — Bases: ModelBase"), [`OutputModel`](output.html#abaqus.StepOutput.OutputModel.OutputModel "abaqus.StepOutput.OutputModel.OutputModel (Python class) — Bases: ModelBase"), [`SectionModel`](section/index.html#abaqus.Section.SectionModel.SectionModel "abaqus.Section.SectionModel.SectionModel (Python class) — Bases: ModelBase"), [`SketchModel`](sketcher.html#abaqus.Sketcher.SketchModel.SketchModel "abaqus.Sketcher.SketchModel.SketchModel (Python class) — Bases: ModelBase"), [`StepModel`](step/index.html#abaqus.Step.StepModel.StepModel "abaqus.Step.StepModel.StepModel (Python class) — Bases: ModelBase")

    Abaqus creates a Model object named Model-1 when a session is started.

    Note

    This object can be accessed by:

    ```python
    mdb.models[name]
    ```

    The corresponding analysis keywords are:

    * PHYSICAL CONSTANTS

    Note

    Check [Model on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?contextscope=all).

    Public Data Attributes:

    Inherited from [`ModelBase`](#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | [`name`](#abaqus.Model.ModelBase.ModelBase.name "abaqus.Model.ModelBase.ModelBase.name (Python attribute) — A String specifying the repository key.") | A String specifying the repository key. |
    | [`stefanBoltzmann`](#abaqus.Model.ModelBase.ModelBase.stefanBoltzmann "abaqus.Model.ModelBase.ModelBase.stefanBoltzmann (Python attribute) — None or a Float specifying the Stefan-Boltzmann constant. The default value is None.") | None or a Float specifying the Stefan-Boltzmann constant. |
    | [`absoluteZero`](#abaqus.Model.ModelBase.ModelBase.absoluteZero "abaqus.Model.ModelBase.ModelBase.absoluteZero (Python attribute) — None or a Float specifying the absolute zero constant. The default value is None.") | None or a Float specifying the absolute zero constant. |
    | [`waveFormulation`](#abaqus.Model.ModelBase.ModelBase.waveFormulation "abaqus.Model.ModelBase.ModelBase.waveFormulation (Python attribute) — A SymbolicConstant specifying the type of incident wave formulation to be used in acoustic problems. Possible values are NOT_SET, SCATTERED, and TOTAL. The default value is NOT_SET.") | A SymbolicConstant specifying the type of incident wave formulation to be used in acoustic problems. |
    | [`universalGas`](#abaqus.Model.ModelBase.ModelBase.universalGas "abaqus.Model.ModelBase.ModelBase.universalGas (Python attribute) — None or a Float specifying the universal gas constant. The default value is None.") | None or a Float specifying the universal gas constant. |
    | [`noPartsInputFile`](#abaqus.Model.ModelBase.ModelBase.noPartsInputFile "abaqus.Model.ModelBase.ModelBase.noPartsInputFile (Python attribute) — A Boolean specifying whether an input file should be written without parts and assemblies. The default value is OFF.") | A Boolean specifying whether an input file should be written without parts and assemblies. |
    | [`endRestartStep`](#abaqus.Model.ModelBase.ModelBase.endRestartStep "abaqus.Model.ModelBase.ModelBase.endRestartStep (Python attribute) — A Boolean specifying that the step specified by restartStep should be terminated at the increment specified by restartIncrement.") | A Boolean specifying that the step specified by **restartStep** should be terminated at the increment specified by **restartIncrement**. |
    | [`shellToSolid`](#abaqus.Model.ModelBase.ModelBase.shellToSolid "abaqus.Model.ModelBase.ModelBase.shellToSolid (Python attribute) — A Boolean specifying that a shell global model drives a solid submodel.") | A Boolean specifying that a shell global model drives a solid submodel. |
    | [`lastChangedCount`](#abaqus.Model.ModelBase.ModelBase.lastChangedCount "abaqus.Model.ModelBase.ModelBase.lastChangedCount (Python attribute) — A Float specifying the time stamp that indicates when the model was last changed.") | A Float specifying the time stamp that indicates when the model was last changed. |
    | [`description`](#abaqus.Model.ModelBase.ModelBase.description "abaqus.Model.ModelBase.ModelBase.description (Python attribute) — A String specifying the purpose and contents of the Model object. The default value is an empty string.") | A String specifying the purpose and contents of the Model object. |
    | [`restartJob`](#abaqus.Model.ModelBase.ModelBase.restartJob "abaqus.Model.ModelBase.ModelBase.restartJob (Python attribute) — A String specifying the name of the job that generated the restart data.") | A String specifying the name of the job that generated the restart data. |
    | [`restartStep`](#abaqus.Model.ModelBase.ModelBase.restartStep "abaqus.Model.ModelBase.ModelBase.restartStep (Python attribute) — A String specifying the name of the step where the restart analysis will start.") | A String specifying the name of the step where the restart analysis will start. |
    | [`globalJob`](#abaqus.Model.ModelBase.ModelBase.globalJob "abaqus.Model.ModelBase.ModelBase.globalJob (Python attribute) — A String specifying the name of the job that generated the results for the global model.") | A String specifying the name of the job that generated the results for the global model. |
    | [`copyConstraints`](#abaqus.Model.ModelBase.ModelBase.copyConstraints "abaqus.Model.ModelBase.ModelBase.copyConstraints (Python attribute) — A boolean specifying the status of constraints created in a model, in the model which instances this model.") | A boolean specifying the status of constraints created in a model, in the model which instances this model. |
    | [`copyConnectors`](#abaqus.Model.ModelBase.ModelBase.copyConnectors "abaqus.Model.ModelBase.ModelBase.copyConnectors (Python attribute) — A boolean specifying the status of connectors created in a model, in the model which instances this model.") | A boolean specifying the status of connectors created in a model, in the model which instances this model. |
    | [`copyInteractions`](#abaqus.Model.ModelBase.ModelBase.copyInteractions "abaqus.Model.ModelBase.ModelBase.copyInteractions (Python attribute) — A boolean specifying the status of interactions created in a model, in the model which instances this model.") | A boolean specifying the status of interactions created in a model, in the model which instances this model. |
    | [`keywordBlock`](#abaqus.Model.ModelBase.ModelBase.keywordBlock "abaqus.Model.ModelBase.ModelBase.keywordBlock (Python attribute) — A KeywordBlock object.") | A KeywordBlock object. |
    | [`amplitudes`](#abaqus.Model.ModelBase.ModelBase.amplitudes "abaqus.Model.ModelBase.ModelBase.amplitudes (Python attribute) — A repository of Amplitude objects.") | A repository of Amplitude objects. |
    | [`profiles`](#abaqus.Model.ModelBase.ModelBase.profiles "abaqus.Model.ModelBase.ModelBase.profiles (Python attribute) — A repository of Profile objects.") | A repository of Profile objects. |
    | [`boundaryConditions`](#abaqus.Model.ModelBase.ModelBase.boundaryConditions "abaqus.Model.ModelBase.ModelBase.boundaryConditions (Python attribute) — A repository of BoundaryCondition objects.") | A repository of BoundaryCondition objects. |
    | [`constraints`](#abaqus.Model.ModelBase.ModelBase.constraints "abaqus.Model.ModelBase.ModelBase.constraints (Python attribute) — A repository of ConstrainedSketchConstraint objects.") | A repository of ConstrainedSketchConstraint objects. |
    | [`analyticalFields`](#abaqus.Model.ModelBase.ModelBase.analyticalFields "abaqus.Model.ModelBase.ModelBase.analyticalFields (Python attribute) — A repository of AnalyticalField objects.") | A repository of AnalyticalField objects. |
    | [`discreteFields`](#abaqus.Model.ModelBase.ModelBase.discreteFields "abaqus.Model.ModelBase.ModelBase.discreteFields (Python attribute) — A repository of DiscreteField objects.") | A repository of DiscreteField objects. |
    | [`predefinedFields`](#abaqus.Model.ModelBase.ModelBase.predefinedFields "abaqus.Model.ModelBase.ModelBase.predefinedFields (Python attribute) — A repository of PredefinedField objects.") | A repository of PredefinedField objects. |
    | [`interactions`](#abaqus.Model.ModelBase.ModelBase.interactions "abaqus.Model.ModelBase.ModelBase.interactions (Python attribute) — A repository of Interaction objects.") | A repository of Interaction objects. |
    | [`interactionProperties`](#abaqus.Model.ModelBase.ModelBase.interactionProperties "abaqus.Model.ModelBase.ModelBase.interactionProperties (Python attribute) — A repository of InteractionProperty objects.") | A repository of InteractionProperty objects. |
    | [`contactControls`](#abaqus.Model.ModelBase.ModelBase.contactControls "abaqus.Model.ModelBase.ModelBase.contactControls (Python attribute) — A repository of ContactControl objects.") | A repository of ContactControl objects. |
    | [`contactInitializations`](#abaqus.Model.ModelBase.ModelBase.contactInitializations "abaqus.Model.ModelBase.ModelBase.contactInitializations (Python attribute) — A repository of ContactInitialization objects.") | A repository of ContactInitialization objects. |
    | [`contactStabilizations`](#abaqus.Model.ModelBase.ModelBase.contactStabilizations "abaqus.Model.ModelBase.ModelBase.contactStabilizations (Python attribute) — A repository of ContactStabilization objects.") | A repository of ContactStabilization objects. |
    | [`linkedInstances`](#abaqus.Model.ModelBase.ModelBase.linkedInstances "abaqus.Model.ModelBase.ModelBase.linkedInstances (Python attribute) — A tuple of tuples of Strings specifying the linked child PartInstance name in the current model to the corresponding parent PartInstance name in a different model.") | A tuple of tuples of Strings specifying the linked child PartInstance name in the current model to the corresponding parent PartInstance name in a different model. |
    | [`linkedParts`](#abaqus.Model.ModelBase.ModelBase.linkedParts "abaqus.Model.ModelBase.ModelBase.linkedParts (Python attribute) — A tuple of tuples of Strings specifying the linked child Part name in the current model to the corresponding parent Part name in a different model.") | A tuple of tuples of Strings specifying the linked child Part name in the current model to the corresponding parent Part name in a different model. |
    | [`loads`](#abaqus.Model.ModelBase.ModelBase.loads "abaqus.Model.ModelBase.ModelBase.loads (Python attribute) — A repository of Load objects.") | A repository of Load objects. |
    | [`materials`](#abaqus.Model.ModelBase.ModelBase.materials "abaqus.Model.ModelBase.ModelBase.materials (Python attribute) — A repository of Material objects.") | A repository of Material objects. |
    | [`calibrations`](#abaqus.Model.ModelBase.ModelBase.calibrations "abaqus.Model.ModelBase.ModelBase.calibrations (Python attribute) — A repository of Calibration objects.") | A repository of Calibration objects. |
    | [`sections`](#abaqus.Model.ModelBase.ModelBase.sections "abaqus.Model.ModelBase.ModelBase.sections (Python attribute) — A repository of Section objects.") | A repository of Section objects. |
    | [`remeshingRules`](#abaqus.Model.ModelBase.ModelBase.remeshingRules "abaqus.Model.ModelBase.ModelBase.remeshingRules (Python attribute) — A repository of RemeshingRule objects.") | A repository of RemeshingRule objects. |
    | [`sketches`](#abaqus.Model.ModelBase.ModelBase.sketches "abaqus.Model.ModelBase.ModelBase.sketches (Python attribute) — A repository of ConstrainedSketch objects.") | A repository of ConstrainedSketch objects. |
    | [`parts`](#abaqus.Model.ModelBase.ModelBase.parts "abaqus.Model.ModelBase.ModelBase.parts (Python attribute) — A repository of Part objects.") | A repository of Part objects. |
    | [`steps`](#abaqus.Model.ModelBase.ModelBase.steps "abaqus.Model.ModelBase.ModelBase.steps (Python attribute) — A repository of Step objects.") | A repository of Step objects. |
    | [`featureOptions`](#abaqus.Model.ModelBase.ModelBase.featureOptions "abaqus.Model.ModelBase.ModelBase.featureOptions (Python attribute) — A FeatureOptions object.") | A FeatureOptions object. |
    | [`adaptiveMeshConstraints`](#abaqus.Model.ModelBase.ModelBase.adaptiveMeshConstraints "abaqus.Model.ModelBase.ModelBase.adaptiveMeshConstraints (Python attribute) — A repository of AdaptiveMeshConstraint objects.") | A repository of AdaptiveMeshConstraint objects. |
    | [`adaptiveMeshControls`](#abaqus.Model.ModelBase.ModelBase.adaptiveMeshControls "abaqus.Model.ModelBase.ModelBase.adaptiveMeshControls (Python attribute) — A repository of AdaptiveMeshControl objects.") | A repository of AdaptiveMeshControl objects. |
    | [`timePoints`](#abaqus.Model.ModelBase.ModelBase.timePoints "abaqus.Model.ModelBase.ModelBase.timePoints (Python attribute) — A repository of TimePoint objects.") | A repository of TimePoint objects. |
    | [`filters`](#abaqus.Model.ModelBase.ModelBase.filters "abaqus.Model.ModelBase.ModelBase.filters (Python attribute) — A repository of Filter objects.") | A repository of Filter objects. |
    | [`integratedOutputSections`](#abaqus.Model.ModelBase.ModelBase.integratedOutputSections "abaqus.Model.ModelBase.ModelBase.integratedOutputSections (Python attribute) — A repository of IntegratedOutputSection objects.") | A repository of IntegratedOutputSection objects. |
    | [`fieldOutputRequests`](#abaqus.Model.ModelBase.ModelBase.fieldOutputRequests "abaqus.Model.ModelBase.ModelBase.fieldOutputRequests (Python attribute) — A repository of FieldOutputRequest objects.") | A repository of FieldOutputRequest objects. |
    | [`historyOutputRequests`](#abaqus.Model.ModelBase.ModelBase.historyOutputRequests "abaqus.Model.ModelBase.ModelBase.historyOutputRequests (Python attribute) — A repository of HistoryOutputRequest objects.") | A repository of HistoryOutputRequest objects. |
    | [`optimizationTasks`](#abaqus.Model.ModelBase.ModelBase.optimizationTasks "abaqus.Model.ModelBase.ModelBase.optimizationTasks (Python attribute) — A repository of OptimizationTask objects.") | A repository of OptimizationTask objects. |
    | [`tableCollections`](#abaqus.Model.ModelBase.ModelBase.tableCollections "abaqus.Model.ModelBase.ModelBase.tableCollections (Python attribute) — A repository of TableCollection objects.") | A repository of TableCollection objects. |
    | [`eventSeriesTypes`](#abaqus.Model.ModelBase.ModelBase.eventSeriesTypes "abaqus.Model.ModelBase.ModelBase.eventSeriesTypes (Python attribute) — A repository of EventSeriesType objects.") | A repository of EventSeriesType objects. |
    | [`eventSeriesDatas`](#abaqus.Model.ModelBase.ModelBase.eventSeriesDatas "abaqus.Model.ModelBase.ModelBase.eventSeriesDatas (Python attribute) — A repository of EventSeriesData objects.") | A repository of EventSeriesData objects. |
    | [`restartIncrement`](#abaqus.Model.ModelBase.ModelBase.restartIncrement "abaqus.Model.ModelBase.ModelBase.restartIncrement (Python attribute) — An Int specifying the increment, interval, iteration or cycle where the restart analysis will start. To select the end of the step use the SymbolicConstant STEP_END.") | An Int specifying the increment, interval, iteration or cycle where the restart analysis will start. |
    | [`rootAssembly`](#abaqus.Model.ModelBase.ModelBase.rootAssembly "abaqus.Model.ModelBase.ModelBase.rootAssembly (Python attribute) — An Assembly object.") | An Assembly object. |

    Public Methods:

    Inherited from [`AdaptivityModel`](adaptivity.html#abaqus.Adaptivity.AdaptivityModel.AdaptivityModel "abaqus.Adaptivity.AdaptivityModel.AdaptivityModel (Python class) — Bases: ModelBase")

    |  |  |
    | --- | --- |
    | [`adaptiveRemesh`](adaptivity.html#abaqus.Adaptivity.AdaptivityModel.AdaptivityModel.adaptiveRemesh "abaqus.Adaptivity.AdaptivityModel.AdaptivityModel.adaptiveRemesh (Python method) — This method remeshes the model using the active remesh rules in the model and the error indicator results from a previous analysis.")(odb) | This method remeshes the model using the active remesh rules in the model and the error indicator results from a previous analysis. |
    | [`AdaptiveMeshConstraint`](adaptivity.html#abaqus.Adaptivity.AdaptivityModel.AdaptivityModel.AdaptiveMeshConstraint "abaqus.Adaptivity.AdaptivityModel.AdaptivityModel.AdaptiveMeshConstraint (Python method) — The AdaptiveMeshConstraint object is the abstract base type for other Arbitrary Lagrangian Eularian (ALE) style AdaptiveMeshConstraint objects. The AdaptiveMeshConstraint object has no explicit constructor. The methods and members of the AdaptiveMeshConstraint object are common to all objects derived from the AdaptiveMeshConstraint object.")(name, category, region) | The AdaptiveMeshConstraint object is the abstract base type for other Arbitrary Lagrangian Eularian (ALE) style AdaptiveMeshConstraint objects. |
    | [`AdaptiveMeshControl`](adaptivity.html#abaqus.Adaptivity.AdaptivityModel.AdaptivityModel.AdaptiveMeshControl "abaqus.Adaptivity.AdaptivityModel.AdaptivityModel.AdaptiveMeshControl (Python method) — This method creates an AdaptiveMeshControl object.")(name[, remapping, ...]) | This method creates an AdaptiveMeshControl object. |
    | [`DisplacementAdaptiveMeshConstraint`](adaptivity.html#abaqus.Adaptivity.AdaptivityModel.AdaptivityModel.DisplacementAdaptiveMeshConstraint "abaqus.Adaptivity.AdaptivityModel.AdaptivityModel.DisplacementAdaptiveMeshConstraint (Python method) — This method creates a DisplacementAdaptiveMeshConstraint object.")(name, ...) | This method creates a DisplacementAdaptiveMeshConstraint object. |
    | [`RemeshingRule`](adaptivity.html#abaqus.Adaptivity.AdaptivityModel.AdaptivityModel.RemeshingRule "abaqus.Adaptivity.AdaptivityModel.AdaptivityModel.RemeshingRule (Python method) — This method creates a RemeshingRule object.")(name, stepName, variables[, ...]) | This method creates a RemeshingRule object. |
    | [`VelocityAdaptiveMeshConstraint`](adaptivity.html#abaqus.Adaptivity.AdaptivityModel.AdaptivityModel.VelocityAdaptiveMeshConstraint "abaqus.Adaptivity.AdaptivityModel.AdaptivityModel.VelocityAdaptiveMeshConstraint (Python method) — This method creates a VelocityAdaptiveMeshConstraint object.")(name, ...[, ...]) | This method creates a VelocityAdaptiveMeshConstraint object. |

    Inherited from [`AmplitudeModel`](amplitude.html#abaqus.Amplitude.AmplitudeModel.AmplitudeModel "abaqus.Amplitude.AmplitudeModel.AmplitudeModel (Python class) — Bases: ModelBase")

    |  |  |
    | --- | --- |
    | [`ActuatorAmplitude`](amplitude.html#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ActuatorAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ActuatorAmplitude (Python method) — This method creates a ActuatorAmplitude object.")(name[, timeSpan]) | This method creates a ActuatorAmplitude object. |
    | [`DecayAmplitude`](amplitude.html#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude (Python method) — This method creates a DecayAmplitude object.")(name, initial, maximum, ...) | This method creates a DecayAmplitude object. |
    | [`EquallySpacedAmplitude`](amplitude.html#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude (Python method) — This method creates an EquallySpacedAmplitude object.")(name, fixedInterval, data) | This method creates an EquallySpacedAmplitude object. |
    | [`ModulatedAmplitude`](amplitude.html#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude (Python method) — This method creates a ModulatedAmplitude object.")(name, initial, magnitude, ...) | This method creates a ModulatedAmplitude object. |
    | [`PeriodicAmplitude`](amplitude.html#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude (Python method) — This method creates a PeriodicAmplitude object.")(name, frequency, start, ...) | This method creates a PeriodicAmplitude object. |
    | [`PsdDefinition`](amplitude.html#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition (Python method) — This method creates a PsdDefinition object.")(name, data[, unitType, ...]) | This method creates a PsdDefinition object. |
    | [`SmoothStepAmplitude`](amplitude.html#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SmoothStepAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SmoothStepAmplitude (Python method) — This method creates a SmoothStepAmplitude object.")(name, data[, timeSpan]) | This method creates a SmoothStepAmplitude object. |
    | [`SolutionDependentAmplitude`](amplitude.html#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude (Python method) — This method creates a SolutionDependentAmplitude object.")(name[, initial, ...]) | This method creates a SolutionDependentAmplitude object. |
    | [`SpectrumAmplitude`](amplitude.html#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude (Python method) — This method creates a SpectrumAmplitude object.")(name, method, data[, ...]) | This method creates a SpectrumAmplitude object. |
    | [`TabularAmplitude`](amplitude.html#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.TabularAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.TabularAmplitude (Python method) — This method creates a TabularAmplitude object.")(name, data[, smooth, timeSpan]) | This method creates a TabularAmplitude object. |

    Inherited from [`AssemblyModel`](part_assembly/assembly.html#abaqus.Assembly.AssemblyModel.AssemblyModel "abaqus.Assembly.AssemblyModel.AssemblyModel (Python class) — Bases: ModelBase")

    |  |  |
    | --- | --- |
    | [`Instance`](part_assembly/assembly.html#abaqus.Assembly.AssemblyModel.AssemblyModel.Instance "abaqus.Assembly.AssemblyModel.AssemblyModel.Instance (Python method) — This method copies a PartInstance object from the specified model and creates a new PartInstance object.")(name, objectToCopy) | This method copies a PartInstance object from the specified model and creates a new PartInstance object. |
    | [`convertAllSketches`](part_assembly/assembly.html#abaqus.Assembly.AssemblyModel.AssemblyModel.convertAllSketches "abaqus.Assembly.AssemblyModel.AssemblyModel.convertAllSketches (Python method) — This method converts all sketches from Abaqus 6.5 or earlier to the equivalent ConstrainedSketch objects.")([regenerate, ...]) | This method converts all sketches from Abaqus 6.5 or earlier to the equivalent ConstrainedSketch objects. |
    | [`linkInstances`](part_assembly/assembly.html#abaqus.Assembly.AssemblyModel.AssemblyModel.linkInstances "abaqus.Assembly.AssemblyModel.AssemblyModel.linkInstances (Python method) — This method links the selected PartInstance objects to the corresponding PartInstance objects from the specified models. If all instances of a Part are selected for linking, the Part will be linked as well. If not, a new linked child Part object will be created and added to the repository.")(instancesMap) | This method links the selected PartInstance objects to the corresponding PartInstance objects from the specified models. |

    Inherited from [`BoundaryConditionModel`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel (Python class) — Bases: ModelBase")

    |  |  |
    | --- | --- |
    | [`AccelerationBaseMotionBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBaseMotionBC (Python method) — This method creates a AccelerationBaseMotionBC object.")(name, ...[, ...]) | This method creates a AccelerationBaseMotionBC object. |
    | [`AccelerationBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AccelerationBC (Python method) — This method creates an AccelerationBC object.")(name, createStepName, region) | This method creates an AccelerationBC object. |
    | [`AcousticPressureBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.AcousticPressureBC (Python method) — This method creates a AcousticPressureBC object.")(name, createStepName, region) | This method creates a AcousticPressureBC object. |
    | [`ConcentrationBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConcentrationBC (Python method) — This method creates a ConcentrationBC object.")(name, createStepName, region) | This method creates a ConcentrationBC object. |
    | [`ConnAccelerationBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnAccelerationBC (Python method) — This method creates an ConnAccelerationBC object on a wire region. Alternatively, the boundary condition may also be applied to a wire set referenced from an assembled fastener template model.")(name, createStepName[, ...]) | This method creates an ConnAccelerationBC object on a wire region. |
    | [`ConnDisplacementBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnDisplacementBC (Python method) — This method creates a ConnDisplacementBC object on a wire region. Alternatively, the boundary condition may also be applied to a wire set referenced from an assembled fastener template model.")(name, createStepName[, ...]) | This method creates a ConnDisplacementBC object on a wire region. |
    | [`ConnVelocityBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ConnVelocityBC (Python method) — This method creates a ConnVelocityBC object on a wire region. Alternatively, the boundary condition may also be applied to a wire set referenced from an assembled fastener template model.")(name, createStepName[, ...]) | This method creates a ConnVelocityBC object on a wire region. |
    | [`DisplacementBaseMotionBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBaseMotionBC (Python method) — This method creates a DisplacementBaseMotionBC object.")(name, ...[, ...]) | This method creates a DisplacementBaseMotionBC object. |
    | [`DisplacementBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.DisplacementBC (Python method) — This method creates a DisplacementBC object.")(name, createStepName, region) | This method creates a DisplacementBC object. |
    | [`ElectricPotentialBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ElectricPotentialBC (Python method) — This method creates an ElectricPotentialBC object.")(name, createStepName, region) | This method creates an ElectricPotentialBC object. |
    | [`EulerianBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianBC (Python method) — This method creates a EulerianBC object.")(name, createStepName, region[, ...]) | This method creates a EulerianBC object. |
    | [`EulerianMotionBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EulerianMotionBC (Python method) — This method creates an EulerianMotionBC object.")(name, createStepName, ...) | This method creates an EulerianMotionBC object. |
    | [`FluidCavityPressureBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.FluidCavityPressureBC (Python method) — This method creates a FluidCavityPressureBC object.")(name, createStepName, ...) | This method creates a FluidCavityPressureBC object. |
    | [`MagneticVectorPotentialBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MagneticVectorPotentialBC (Python method) — This method creates a MagneticVectorPotentialBC object.")(name, ...[, ...]) | This method creates a MagneticVectorPotentialBC object. |
    | [`MaterialFlowBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.MaterialFlowBC (Python method) — This method creates a MaterialFlowBC object.")(name, createStepName, region) | This method creates a MaterialFlowBC object. |
    | [`PorePressureBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PorePressureBC (Python method) — This method creates a PorePressureBC object.")(name, createStepName, region) | This method creates a PorePressureBC object. |
    | [`RetainedNodalDofsBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.RetainedNodalDofsBC (Python method) — This method creates a RetainedNodalDofsBC object.")(name, createStepName, region) | This method creates a RetainedNodalDofsBC object. |
    | [`SecondaryBaseBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SecondaryBaseBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SecondaryBaseBC (Python method) — This method creates a SecondaryBaseBC object.")(name, createStepName, ...) | This method creates a SecondaryBaseBC object. |
    | [`SubmodelBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.SubmodelBC (Python method) — This method creates a SubmodelBC object.")(name, createStepName, region, ...) | This method creates a SubmodelBC object. |
    | [`TemperatureBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.TemperatureBC (Python method) — This method creates a TemperatureBC object.")(name, createStepName, region) | This method creates a TemperatureBC object. |
    | [`VelocityBaseMotionBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBaseMotionBC (Python method) — This method creates a VelocityBaseMotionBC object.")(name, createStepName, dof) | This method creates a VelocityBaseMotionBC object. |
    | [`VelocityBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.VelocityBC (Python method) — This method creates a VelocityBC object.")(name, createStepName, region[, ...]) | This method creates a VelocityBC object. |
    | [`EncastreBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EncastreBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.EncastreBC (Python method) — This method creates an encastre TypeBC object.")(name, createStepName, region[, ...]) | This method creates an encastre TypeBC object. |
    | [`PinnedBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PinnedBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.PinnedBC (Python method) — This method creates a pinned TypeBC object.")(name, createStepName, region[, ...]) | This method creates a pinned TypeBC object. |
    | [`XsymmBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XsymmBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XsymmBC (Python method) — This method creates a TypeBC object that specifies symmetry about the X axis.")(name, createStepName, region[, ...]) | This method creates a TypeBC object that specifies symmetry about the **X** axis. |
    | [`YsymmBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YsymmBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YsymmBC (Python method) — This method creates a TypeBC object that specifies symmetry about the Y axis.")(name, createStepName, region[, ...]) | This method creates a TypeBC object that specifies symmetry about the **Y** axis. |
    | [`ZsymmBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZsymmBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZsymmBC (Python method) — This method creates a TypeBC object that specifies symmetry about the Z axis.")(name, createStepName, region[, ...]) | This method creates a TypeBC object that specifies symmetry about the **Z** axis. |
    | [`XasymmBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XasymmBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.XasymmBC (Python method) — This method creates a TypeBC object that specifies antisymmetry about the X axis.")(name, createStepName, region[, ...]) | This method creates a TypeBC object that specifies antisymmetry about the **X** axis. |
    | [`YasymmBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YasymmBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.YasymmBC (Python method) — This method creates a TypeBC object that specifies antisymmetry about the Y axis.")(name, createStepName, region[, ...]) | This method creates a TypeBC object that specifies antisymmetry about the **Y** axis. |
    | [`ZasymmBC`](bc.html#abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZasymmBC "abaqus.BoundaryCondition.BoundaryConditionModel.BoundaryConditionModel.ZasymmBC (Python method) — This method creates a TypeBC object that specifies antisymmetry about the Z axis.")(name, createStepName, region[, ...]) | This method creates a TypeBC object that specifies antisymmetry about the **Z** axis. |

    Inherited from [`CalibrationModel`](calibration.html#abaqus.Calibration.CalibrationModel.CalibrationModel "abaqus.Calibration.CalibrationModel.CalibrationModel (Python class) — Bases: ModelBase")

    |  |  |
    | --- | --- |
    | [`Calibration`](calibration.html#abaqus.Calibration.CalibrationModel.CalibrationModel.Calibration "abaqus.Calibration.CalibrationModel.CalibrationModel.Calibration (Python method) — This method creates a Calibration object.")(name) | This method creates a Calibration object. |

    Inherited from [`ConstraintModel`](constraint.html#abaqus.Constraint.ConstraintModel.ConstraintModel "abaqus.Constraint.ConstraintModel.ConstraintModel (Python class) — Bases: ModelBase")

    |  |  |
    | --- | --- |
    | [`AdjustPoints`](constraint.html#abaqus.Constraint.ConstraintModel.ConstraintModel.AdjustPoints "abaqus.Constraint.ConstraintModel.ConstraintModel.AdjustPoints (Python method) — This method creates an AdjustPoints object.")(name, surface, controlPoints) | This method creates an AdjustPoints object. |
    | [`Coupling`](constraint.html#abaqus.Constraint.ConstraintModel.ConstraintModel.Coupling "abaqus.Constraint.ConstraintModel.ConstraintModel.Coupling (Python method) — This method creates a Coupling object.")(name, surface, controlPoint, ...[, ...]) | This method creates a Coupling object. |
    | [`DisplayBody`](constraint.html#abaqus.Constraint.ConstraintModel.ConstraintModel.DisplayBody "abaqus.Constraint.ConstraintModel.ConstraintModel.DisplayBody (Python method) — This method creates a DisplayBody object.")(name, instance, controlPoints) | This method creates a DisplayBody object. |
    | [`EmbeddedRegion`](constraint.html#abaqus.Constraint.ConstraintModel.ConstraintModel.EmbeddedRegion "abaqus.Constraint.ConstraintModel.ConstraintModel.EmbeddedRegion (Python method) — This method creates a EmbeddedRegion object.")(name, embeddedRegion, hostRegion) | This method creates a EmbeddedRegion object. |
    | [`Equation`](constraint.html#abaqus.Constraint.ConstraintModel.ConstraintModel.Equation "abaqus.Constraint.ConstraintModel.ConstraintModel.Equation (Python method) — This method creates an Equation object.")(name, terms) | This method creates an Equation object. |
    | [`MultipointConstraint`](constraint.html#abaqus.Constraint.ConstraintModel.ConstraintModel.MultipointConstraint "abaqus.Constraint.ConstraintModel.ConstraintModel.MultipointConstraint (Python method) — This method creates a MultipointConstraint object.")(name, surface, ...[, ...]) | This method creates a MultipointConstraint object. |
    | [`RigidBody`](constraint.html#abaqus.Constraint.ConstraintModel.ConstraintModel.RigidBody "abaqus.Constraint.ConstraintModel.ConstraintModel.RigidBody (Python method) — This method creates a RigidBody object.")(name, refPointRegion[, ...]) | This method creates a RigidBody object. |
    | [`ShellSolidCoupling`](constraint.html#abaqus.Constraint.ConstraintModel.ConstraintModel.ShellSolidCoupling "abaqus.Constraint.ConstraintModel.ConstraintModel.ShellSolidCoupling (Python method) — This method creates a ShellSolidCoupling object.")(name, shellEdge, solidFace) | This method creates a ShellSolidCoupling object. |
    | [`Tie`](constraint.html#abaqus.Constraint.ConstraintModel.ConstraintModel.Tie "abaqus.Constraint.ConstraintModel.ConstraintModel.Tie (Python method) — This method creates a Tie object.")(name, main, secondary[, adjust, ...]) | This method creates a Tie object. |

    Inherited from [`FilterModel`](filter.html#abaqus.Filter.FilterModel.FilterModel "abaqus.Filter.FilterModel.FilterModel (Python class) — Bases: ModelBase")

    |  |  |
    | --- | --- |
    | [`ButterworthFilter`](filter.html#abaqus.Filter.FilterModel.FilterModel.ButterworthFilter "abaqus.Filter.FilterModel.FilterModel.ButterworthFilter (Python method) — This method creates a ButterworthFilter object.")(name, cutoffFrequency[, ...]) | This method creates a ButterworthFilter object. |
    | [`Chebyshev1Filter`](filter.html#abaqus.Filter.FilterModel.FilterModel.Chebyshev1Filter "abaqus.Filter.FilterModel.FilterModel.Chebyshev1Filter (Python method) — This method creates a Chebyshev1Filter object.")(name, cutoffFrequency[, ...]) | This method creates a Chebyshev1Filter object. |
    | [`Chebyshev2Filter`](filter.html#abaqus.Filter.FilterModel.FilterModel.Chebyshev2Filter "abaqus.Filter.FilterModel.FilterModel.Chebyshev2Filter (Python method) — This method creates a Chebyshev2Filter object.")(name, cutoffFrequency[, ...]) | This method creates a Chebyshev2Filter object. |
    | [`OperatorFilter`](filter.html#abaqus.Filter.FilterModel.FilterModel.OperatorFilter "abaqus.Filter.FilterModel.FilterModel.OperatorFilter (Python method) — This method creates an OperatorFilter object.")(name, cutoffFrequency[, ...]) | This method creates an OperatorFilter object. |

    Inherited from [`InteractionModel`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel "abaqus.Interaction.InteractionModel.InteractionModel (Python class) — Bases: InteractionContactControlModel, InteractionContactInitializationModel, InteractionContactStabilizationModel, InteractionPropertyModel")

    |  |  |
    | --- | --- |
    | [`contactDetection`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.contactDetection "abaqus.Interaction.InteractionModel.InteractionModel.contactDetection (Python method) — This method uses contact detection to create SurfaceToSurfaceContactStd, SurfaceToSurfaceContactExp, and Tie objects.")([name, createStepName, ...]) | This method uses contact detection to create SurfaceToSurfaceContactStd, SurfaceToSurfaceContactExp, and Tie objects. |
    | [`getSurfaceSeparation`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.getSurfaceSeparation "abaqus.Interaction.InteractionModel.InteractionModel.getSurfaceSeparation (Python method) — This method returns a list of all possible contacts that can be created using the ContactDetection method.")() | This method returns a list of all possible contacts that can be created using the ContactDetection method. |
    | [`AcousticImpedance`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.AcousticImpedance "abaqus.Interaction.InteractionModel.InteractionModel.AcousticImpedance (Python method) — This method creates an AcousticImpedance object.")(name, createStepName, surface) | This method creates an AcousticImpedance object. |
    | [`ActuatorSensor`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.ActuatorSensor "abaqus.Interaction.InteractionModel.InteractionModel.ActuatorSensor (Python method) — This method creates an ActuatorSensor object.")(name, createStepName, point, ...) | This method creates an ActuatorSensor object. |
    | [`CavityRadiation`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.CavityRadiation "abaqus.Interaction.InteractionModel.InteractionModel.CavityRadiation (Python method) — This method creates a CavityRadiation object.")(name, createStepName, surfaces) | This method creates a CavityRadiation object. |
    | [`ConcentratedFilmCondition`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.ConcentratedFilmCondition "abaqus.Interaction.InteractionModel.InteractionModel.ConcentratedFilmCondition (Python method) — This method creates a ConcentratedFilmCondition object.")(name, ...[, ...]) | This method creates a ConcentratedFilmCondition object. |
    | [`ConcentratedRadiationToAmbient`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.ConcentratedRadiationToAmbient "abaqus.Interaction.InteractionModel.InteractionModel.ConcentratedRadiationToAmbient (Python method) — This method creates a ConcentratedRadiationToAmbient object.")(name, ...[, ...]) | This method creates a ConcentratedRadiationToAmbient object. |
    | [`ContactExp`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.ContactExp "abaqus.Interaction.InteractionModel.InteractionModel.ContactExp (Python method) — This method creates a ContactExp object.")(name, createStepName[, ...]) | This method creates a ContactExp object. |
    | [`ContactMassScalingExp`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.ContactMassScalingExp "abaqus.Interaction.InteractionModel.InteractionModel.ContactMassScalingExp (Python method) — This method creates an ContactMassScalingExp object.")(name, createStepName) | This method creates an ContactMassScalingExp object. |
    | [`ContactStd`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.ContactStd "abaqus.Interaction.InteractionModel.InteractionModel.ContactStd (Python method) — This method creates a ContactStd object.")(name, createStepName[, ...]) | This method creates a ContactStd object. |
    | [`CyclicSymmetry`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.CyclicSymmetry "abaqus.Interaction.InteractionModel.InteractionModel.CyclicSymmetry (Python method) — This method creates a CyclicSymmetry object.")(name, createStepName, main, ...) | This method creates a CyclicSymmetry object. |
    | [`ElasticFoundation`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.ElasticFoundation "abaqus.Interaction.InteractionModel.InteractionModel.ElasticFoundation (Python method) — This method creates an ElasticFoundation object.")(name, createStepName, ...) | This method creates an ElasticFoundation object. |
    | [`FilmCondition`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.FilmCondition "abaqus.Interaction.InteractionModel.InteractionModel.FilmCondition (Python method) — This method creates a FilmCondition object.")(name, createStepName, surface, ...) | This method creates a FilmCondition object. |
    | [`FluidCavity`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.FluidCavity "abaqus.Interaction.InteractionModel.InteractionModel.FluidCavity (Python method) — This method creates an FluidCavity object.")(name, createStepName, ...[, ...]) | This method creates an FluidCavity object. |
    | [`FluidExchange`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.FluidExchange "abaqus.Interaction.InteractionModel.InteractionModel.FluidExchange (Python method) — This method creates an FluidExchange object.")(name, createStepName, ...[, ...]) | This method creates an FluidExchange object. |
    | [`FluidExchangeActivation`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.FluidExchangeActivation "abaqus.Interaction.InteractionModel.InteractionModel.FluidExchangeActivation (Python method) — This method creates an FluidExchangeActivation object.")(name, ...[, ...]) | This method creates an FluidExchangeActivation object. |
    | [`FluidInflator`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.FluidInflator "abaqus.Interaction.InteractionModel.InteractionModel.FluidInflator (Python method) — This method creates a FluidInflator object.")(name, createStepName, cavity, ...) | This method creates a FluidInflator object. |
    | [`FluidInflatorActivation`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.FluidInflatorActivation "abaqus.Interaction.InteractionModel.InteractionModel.FluidInflatorActivation (Python method) — This method creates an FluidExchangeActivation object.")(name, ...[, ...]) | This method creates an FluidExchangeActivation object. |
    | [`IncidentWave`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.IncidentWave "abaqus.Interaction.InteractionModel.InteractionModel.IncidentWave (Python method) — This method creates an IncidentWave object.")(name, createStepName, ...[, ...]) | This method creates an IncidentWave object. |
    | [`ModelChange`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.ModelChange "abaqus.Interaction.InteractionModel.InteractionModel.ModelChange (Python method) — This method creates a ModelChange object.")(name, createStepName[, ...]) | This method creates a ModelChange object. |
    | [`PressurePenetration`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.PressurePenetration "abaqus.Interaction.InteractionModel.InteractionModel.PressurePenetration (Python method) — This method creates a PressurePenetration object.")(name, createStepName, ...) | This method creates a PressurePenetration object. |
    | [`RadiationToAmbient`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.RadiationToAmbient "abaqus.Interaction.InteractionModel.InteractionModel.RadiationToAmbient (Python method) — This method creates a RadiationToAmbient object.")(name, createStepName, ...) | This method creates a RadiationToAmbient object. |
    | [`SelfContactExp`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.SelfContactExp "abaqus.Interaction.InteractionModel.InteractionModel.SelfContactExp (Python method) — This method creates a SelfContactExp object.")(name, createStepName, ...[, ...]) | This method creates a SelfContactExp object. |
    | [`SelfContactStd`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.SelfContactStd "abaqus.Interaction.InteractionModel.InteractionModel.SelfContactStd (Python method) — This method creates a SelfContactStd object.")(name, createStepName, ...[, ...]) | This method creates a SelfContactStd object. |
    | [`StdXplCosimulation`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.StdXplCosimulation "abaqus.Interaction.InteractionModel.InteractionModel.StdXplCosimulation (Python method) — This method creates a StdXplCosimulation object.")(name, createStepName, region) | This method creates a StdXplCosimulation object. |
    | [`SurfaceToSurfaceContactExp`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.SurfaceToSurfaceContactExp "abaqus.Interaction.InteractionModel.InteractionModel.SurfaceToSurfaceContactExp (Python method) — This method creates a SurfaceToSurfaceContactExp object.")(name, ...[, ...]) | This method creates a SurfaceToSurfaceContactExp object. |
    | [`SurfaceToSurfaceContactStd`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.SurfaceToSurfaceContactStd "abaqus.Interaction.InteractionModel.InteractionModel.SurfaceToSurfaceContactStd (Python method) — This method creates a SurfaceToSurfaceContactStd object.")(name, ...[, ...]) | This method creates a SurfaceToSurfaceContactStd object. |
    | [`WearProperty`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.WearProperty "abaqus.Interaction.InteractionModel.InteractionModel.WearProperty (Python method) — This method creates an WearProperty object.")(name[, fricCoefDependency, ...]) | This method creates an WearProperty object. |
    | [`XFEMCrackGrowth`](interaction.html#abaqus.Interaction.InteractionModel.InteractionModel.XFEMCrackGrowth "abaqus.Interaction.InteractionModel.InteractionModel.XFEMCrackGrowth (Python method) — This method creates an XFEMCrackGrowth object.")(name, createStepName, crackName) | This method creates an XFEMCrackGrowth object. |

    Inherited from [`InteractionContactControlModel`](interaction.html#abaqus.Interaction.InteractionContactControlModel.InteractionContactControlModel "abaqus.Interaction.InteractionContactControlModel.InteractionContactControlModel (Python class) — Bases: ModelBase")

    |  |  |
    | --- | --- |
    | [`ExpContactControl`](interaction.html#abaqus.Interaction.InteractionContactControlModel.InteractionContactControlModel.ExpContactControl "abaqus.Interaction.InteractionContactControlModel.InteractionContactControlModel.ExpContactControl (Python method) — This method creates an ExpContactControl object.")(name[, globTrkChoice, ...]) | This method creates an ExpContactControl object. |
    | [`StdContactControl`](interaction.html#abaqus.Interaction.InteractionContactControlModel.InteractionContactControlModel.StdContactControl "abaqus.Interaction.InteractionContactControlModel.InteractionContactControlModel.StdContactControl (Python method) — This method creates an StdContactControl object.")(name[, ...]) | This method creates an StdContactControl object. |

    Inherited from [`InteractionContactInitializationModel`](interaction.html#abaqus.Interaction.InteractionContactInitializationModel.InteractionContactInitializationModel "abaqus.Interaction.InteractionContactInitializationModel.InteractionContactInitializationModel (Python class) — Bases: ModelBase")

    |  |  |
    | --- | --- |
    | [`ExpInitialization`](interaction.html#abaqus.Interaction.InteractionContactInitializationModel.InteractionContactInitializationModel.ExpInitialization "abaqus.Interaction.InteractionContactInitializationModel.InteractionContactInitializationModel.ExpInitialization (Python method) — This method creates an ExpInitialization object.")(name[, overclosureType, ...]) | This method creates an ExpInitialization object. |
    | [`StdInitialization`](interaction.html#abaqus.Interaction.InteractionContactInitializationModel.InteractionContactInitializationModel.StdInitialization "abaqus.Interaction.InteractionContactInitializationModel.InteractionContactInitializationModel.StdInitialization (Python method) — This method creates a StdInitialization object.")(name[, overclosureType, ...]) | This method creates a StdInitialization object. |

    Inherited from [`InteractionContactStabilizationModel`](interaction.html#abaqus.Interaction.InteractionContactStabilizationModel.InteractionContactStabilizationModel "abaqus.Interaction.InteractionContactStabilizationModel.InteractionContactStabilizationModel (Python class) — Bases: ModelBase")

    |  |  |
    | --- | --- |
    | [`StdStabilization`](interaction.html#abaqus.Interaction.InteractionContactStabilizationModel.InteractionContactStabilizationModel.StdStabilization "abaqus.Interaction.InteractionContactStabilizationModel.InteractionContactStabilizationModel.StdStabilization (Python method) — This method creates a StdStabilization object.")(name[, zeroDistance, ...]) | This method creates a StdStabilization object. |

    Inherited from [`InteractionPropertyModel`](interaction.html#abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel "abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel (Python class) — Bases: ModelBase")

    |  |  |
    | --- | --- |
    | [`AcousticImpedanceProp`](interaction.html#abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel.AcousticImpedanceProp "abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel.AcousticImpedanceProp (Python method) — This method creates an AcousticImpedanceProp object.")(name, tableType, table) | This method creates an AcousticImpedanceProp object. |
    | [`ActuatorSensorProp`](interaction.html#abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel.ActuatorSensorProp "abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel.ActuatorSensorProp (Python method) — This method creates an ActuatorSensorProp object.")(name[, realProperties, ...]) | This method creates an ActuatorSensorProp object. |
    | [`CavityRadiationProp`](interaction.html#abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel.CavityRadiationProp "abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel.CavityRadiationProp (Python method) — This method creates a CavityRadiationProp object.")(name[, ...]) | This method creates a CavityRadiationProp object. |
    | [`ContactProperty`](interaction.html#abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel.ContactProperty "abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel.ContactProperty (Python method) — This method creates a ContactProperty object.")(name) | This method creates a ContactProperty object. |
    | [`FilmConditionProp`](interaction.html#abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel.FilmConditionProp "abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel.FilmConditionProp (Python method) — This method creates a FilmConditionProp object.")(name[, ...]) | This method creates a FilmConditionProp object. |
    | [`FluidCavityProperty`](interaction.html#abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel.FluidCavityProperty "abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel.FluidCavityProperty (Python method) — This method creates a FluidCavityProperty object.")(name[, definition, ...]) | This method creates a FluidCavityProperty object. |
    | [`FluidExchangeProperty`](interaction.html#abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel.FluidExchangeProperty "abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel.FluidExchangeProperty (Python method) — This method creates a FluidExchangeProperty object.")(name, dataTable[, ...]) | This method creates a FluidExchangeProperty object. |
    | [`FluidInflatorProperty`](interaction.html#abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel.FluidInflatorProperty "abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel.FluidInflatorProperty (Python method) — This method creates a FluidInflatorProperty object.")(name, definition, ...) | This method creates a FluidInflatorProperty object. |
    | [`IncidentWaveProperty`](interaction.html#abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel.IncidentWaveProperty "abaqus.Interaction.InteractionPropertyModel.InteractionPropertyModel.IncidentWaveProperty (Python method) — This method creates an IncidentWaveProperty object.")(name[, definition, ...]) | This method creates an IncidentWaveProperty object. |

    Inherited from [`LoadModel`](load.html#abaqus.Load.LoadModel.LoadModel "abaqus.Load.LoadModel.LoadModel (Python class) — Bases: ModelBase")

    |  |  |
    | --- | --- |
    | [`BodyCharge`](load.html#abaqus.Load.LoadModel.LoadModel.BodyCharge "abaqus.Load.LoadModel.LoadModel.BodyCharge (Python method) — This method creates a BodyCharge object.")(name, createStepName, region, ...) | This method creates a BodyCharge object. |
    | [`BodyConcentrationFlux`](load.html#abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux "abaqus.Load.LoadModel.LoadModel.BodyConcentrationFlux (Python method) — This method creates a BodyConcentrationFlux object.")(name, createStepName, ...) | This method creates a BodyConcentrationFlux object. |
    | [`BodyCurrent`](load.html#abaqus.Load.LoadModel.LoadModel.BodyCurrent "abaqus.Load.LoadModel.LoadModel.BodyCurrent (Python method) — This method creates a BodyCurrent object.")(name, createStepName, region, ...) | This method creates a BodyCurrent object. |
    | [`BodyCurrentDensity`](load.html#abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity "abaqus.Load.LoadModel.LoadModel.BodyCurrentDensity (Python method) — This method creates a BodyCurrentDensity object.")(name, createStepName, ...) | This method creates a BodyCurrentDensity object. |
    | [`BodyForce`](load.html#abaqus.Load.LoadModel.LoadModel.BodyForce "abaqus.Load.LoadModel.LoadModel.BodyForce (Python method) — This method creates a BodyForce object.")(name, createStepName, region[, ...]) | This method creates a BodyForce object. |
    | [`BodyHeatFlux`](load.html#abaqus.Load.LoadModel.LoadModel.BodyHeatFlux "abaqus.Load.LoadModel.LoadModel.BodyHeatFlux (Python method) — This method creates a BodyHeatFlux object.")(name, createStepName, region, ...) | This method creates a BodyHeatFlux object. |
    | [`BoltLoad`](load.html#abaqus.Load.LoadModel.LoadModel.BoltLoad "abaqus.Load.LoadModel.LoadModel.BoltLoad (Python method) — This method creates a BoltLoad object.")(name, createStepName, region, ...) | This method creates a BoltLoad object. |
    | [`ConcCharge`](load.html#abaqus.Load.LoadModel.LoadModel.ConcCharge "abaqus.Load.LoadModel.LoadModel.ConcCharge (Python method) — This method creates a ConcCharge object.")(name, createStepName, region, ...) | This method creates a ConcCharge object. |
    | [`ConcConcFlux`](load.html#abaqus.Load.LoadModel.LoadModel.ConcConcFlux "abaqus.Load.LoadModel.LoadModel.ConcConcFlux (Python method) — This method creates a ConcConcFlux object.")(name, createStepName, region, ...) | This method creates a ConcConcFlux object. |
    | [`ConcCurrent`](load.html#abaqus.Load.LoadModel.LoadModel.ConcCurrent "abaqus.Load.LoadModel.LoadModel.ConcCurrent (Python method) — This method creates a ConcCurrent object.")(name, createStepName, region, ...) | This method creates a ConcCurrent object. |
    | [`ConcentratedForce`](load.html#abaqus.Load.LoadModel.LoadModel.ConcentratedForce "abaqus.Load.LoadModel.LoadModel.ConcentratedForce (Python method) — This method creates a ConcentratedForce object.")(name, createStepName, region) | This method creates a ConcentratedForce object. |
    | [`ConcentratedHeatFlux`](load.html#abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux "abaqus.Load.LoadModel.LoadModel.ConcentratedHeatFlux (Python method) — This method creates a ConcentratedHeatFlux object.")(name, createStepName, ...) | This method creates a ConcentratedHeatFlux object. |
    | [`ConcPoreFluid`](load.html#abaqus.Load.LoadModel.LoadModel.ConcPoreFluid "abaqus.Load.LoadModel.LoadModel.ConcPoreFluid (Python method) — This method creates a ConcPoreFluid object.")(name, createStepName, region, ...) | This method creates a ConcPoreFluid object. |
    | [`ConnectorForce`](load.html#abaqus.Load.LoadModel.LoadModel.ConnectorForce "abaqus.Load.LoadModel.LoadModel.ConnectorForce (Python method) — This method creates a ConnectorForce object on a wire region. Alternatively, the load may also be applied to a wire set referenced from an assembled fastener template model.")(name, createStepName[, ...]) | This method creates a ConnectorForce object on a wire region. |
    | [`ConnectorMoment`](load.html#abaqus.Load.LoadModel.LoadModel.ConnectorMoment "abaqus.Load.LoadModel.LoadModel.ConnectorMoment (Python method) — This method creates a ConnectorMoment object on a wire region. Alternatively, the load may also be applied to a wire set referenced from an assembled fastener template model.")(name, createStepName[, ...]) | This method creates a ConnectorMoment object on a wire region. |
    | [`CoriolisForce`](load.html#abaqus.Load.LoadModel.LoadModel.CoriolisForce "abaqus.Load.LoadModel.LoadModel.CoriolisForce (Python method) — This method creates a CoriolisForce object.")(name, createStepName, region, ...) | This method creates a CoriolisForce object. |
    | [`Gravity`](load.html#abaqus.Load.LoadModel.LoadModel.Gravity "abaqus.Load.LoadModel.LoadModel.Gravity (Python method) — This method creates a Gravity object.")(name, createStepName[, ...]) | This method creates a Gravity object. |
    | [`InertiaRelief`](load.html#abaqus.Load.LoadModel.LoadModel.InertiaRelief "abaqus.Load.LoadModel.LoadModel.InertiaRelief (Python method) — This method creates an InertiaRelief object.")(name, createStepName[, u1, ...]) | This method creates an InertiaRelief object. |
    | [`InwardVolAccel`](load.html#abaqus.Load.LoadModel.LoadModel.InwardVolAccel "abaqus.Load.LoadModel.LoadModel.InwardVolAccel (Python method) — This method creates a InwardVolAccel object.")(name, createStepName, region, ...) | This method creates a InwardVolAccel object. |
    | [`LineLoad`](load.html#abaqus.Load.LoadModel.LoadModel.LineLoad "abaqus.Load.LoadModel.LoadModel.LineLoad (Python method) — This method creates a LineLoad object.")(name, createStepName, region[, ...]) | This method creates a LineLoad object. |
    | [`Moment`](load.html#abaqus.Load.LoadModel.LoadModel.Moment "abaqus.Load.LoadModel.LoadModel.Moment (Python method) — This method creates a Moment object.")(name, createStepName, region[, cm1, ...]) | This method creates a Moment object. |
    | [`PEGLoad`](load.html#abaqus.Load.LoadModel.LoadModel.PEGLoad "abaqus.Load.LoadModel.LoadModel.PEGLoad (Python method) — This method creates a PEGLoad object.")(name, createStepName, region[, ...]) | This method creates a PEGLoad object. |
    | [`PipePressure`](load.html#abaqus.Load.LoadModel.LoadModel.PipePressure "abaqus.Load.LoadModel.LoadModel.PipePressure (Python method) — This method creates a Pressure object.")(name, createStepName, region, ...) | This method creates a Pressure object. |
    | [`Pressure`](load.html#abaqus.Load.LoadModel.LoadModel.Pressure "abaqus.Load.LoadModel.LoadModel.Pressure (Python method) — This method creates a Pressure object.")(name, createStepName, region[, ...]) | This method creates a Pressure object. |
    | [`RotationalBodyForce`](load.html#abaqus.Load.LoadModel.LoadModel.RotationalBodyForce "abaqus.Load.LoadModel.LoadModel.RotationalBodyForce (Python method) — This method creates a RotationalBodyForce object.")(name, createStepName, ...) | This method creates a RotationalBodyForce object. |
    | [`ShellEdgeLoad`](load.html#abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad "abaqus.Load.LoadModel.LoadModel.ShellEdgeLoad (Python method) — This method creates a ShellEdgeLoad object.")(name, createStepName, region, ...) | This method creates a ShellEdgeLoad object. |
    | [`SubmodelSB`](load.html#abaqus.Load.LoadModel.LoadModel.SubmodelSB "abaqus.Load.LoadModel.LoadModel.SubmodelSB (Python method) — This method creates a SubmodelSB object.")(name, createStepName, region, ...) | This method creates a SubmodelSB object. |
    | [`SubstructureLoad`](load.html#abaqus.Load.LoadModel.LoadModel.SubstructureLoad "abaqus.Load.LoadModel.LoadModel.SubstructureLoad (Python method) — This method creates a SubstructureLoad object.")(name, createStepName, ...) | This method creates a SubstructureLoad object. |
    | [`SurfaceCharge`](load.html#abaqus.Load.LoadModel.LoadModel.SurfaceCharge "abaqus.Load.LoadModel.LoadModel.SurfaceCharge (Python method) — This method creates a SurfaceCharge object.")(name, createStepName, region, ...) | This method creates a SurfaceCharge object. |
    | [`SurfaceConcentrationFlux`](load.html#abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux "abaqus.Load.LoadModel.LoadModel.SurfaceConcentrationFlux (Python method) — This method creates a SurfaceConcentrationFlux object.")(name, ...[, field, ...]) | This method creates a SurfaceConcentrationFlux object. |
    | [`SurfaceCurrent`](load.html#abaqus.Load.LoadModel.LoadModel.SurfaceCurrent "abaqus.Load.LoadModel.LoadModel.SurfaceCurrent (Python method) — This method creates a SurfaceCurrent object.")(name, createStepName, region, ...) | This method creates a SurfaceCurrent object. |
    | [`SurfaceCurrentDensity`](load.html#abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity "abaqus.Load.LoadModel.LoadModel.SurfaceCurrentDensity (Python method) — This method creates a SurfaceCurrentDensity object.")(name, createStepName, ...) | This method creates a SurfaceCurrentDensity object. |
    | [`SurfaceHeatFlux`](load.html#abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux "abaqus.Load.LoadModel.LoadModel.SurfaceHeatFlux (Python method) — This method creates a SurfaceHeatFlux object.")(name, createStepName, ...[, ...]) | This method creates a SurfaceHeatFlux object. |
    | [`SurfacePoreFluid`](load.html#abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid "abaqus.Load.LoadModel.LoadModel.SurfacePoreFluid (Python method) — This method creates a SurfacePoreFluid object.")(name, createStepName, ...) | This method creates a SurfacePoreFluid object. |
    | [`SurfaceTraction`](load.html#abaqus.Load.LoadModel.LoadModel.SurfaceTraction "abaqus.Load.LoadModel.LoadModel.SurfaceTraction (Python method) — This method creates a SurfaceTraction object.")(name, createStepName, ...[, ...]) | This method creates a SurfaceTraction object. |

    Inherited from [`MaterialModel`](material.html#abaqus.Material.MaterialModel.MaterialModel "abaqus.Material.MaterialModel.MaterialModel (Python class) — Bases: ModelBase")

    |  |  |
    | --- | --- |
    | [`Material`](material.html#abaqus.Material.MaterialModel.MaterialModel.Material "abaqus.Material.MaterialModel.MaterialModel.Material (Python method) — This method creates a Material object.")(name[, description, materialIdentifier]) | This method creates a Material object. |

    Inherited from [`OptimizationTaskModel`](optimization.html#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel (Python class) — Bases: ModelBase")

    |  |  |
    | --- | --- |
    | [`BeadTask`](optimization.html#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask (Python method) — This method creates a BeadTask object.")(name[, abaqusSensitivities, ...]) | This method creates a BeadTask object. |
    | [`ShapeTask`](optimization.html#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask (Python method) — This method creates a ShapeTask object.")(name[, abaqusSensitivities, ...]) | This method creates a ShapeTask object. |
    | [`SizingTask`](optimization.html#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask (Python method) — This method creates a SizingTask object.")(name[, abaqusSensitivities, ...]) | This method creates a SizingTask object. |
    | [`TopologyTask`](optimization.html#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask (Python method) — This method creates a TopologyTask object.")(name[, abaqusSensitivities, ...]) | This method creates a TopologyTask object. |

    Inherited from [`PartModel`](part_assembly/part.html#abaqus.Part.PartModel.PartModel "abaqus.Part.PartModel.PartModel (Python class) — Bases: ModelBase")

    |  |  |
    | --- | --- |
    | [`Part`](part_assembly/part.html#abaqus.Part.PartModel.PartModel.Part "abaqus.Part.PartModel.PartModel.Part (Python method) — This method creates a Part object and places it in the parts repository.")(name, dimensionality, type[, twist]) | This method creates a Part object and places it in the parts repository. |

    Inherited from [`PredefinedFieldModel`](predefined.html#abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel "abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel (Python class) — Bases: ModelBase")

    |  |  |
    | --- | --- |
    | [`FluidCavityPressure`](predefined.html#abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.FluidCavityPressure "abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.FluidCavityPressure (Python method) — This method creates a FluidCavityPressure object.")(name, fluidCavity, ...) | This method creates a FluidCavityPressure object. |
    | [`InitialState`](predefined.html#abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.InitialState "abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.InitialState (Python method) — This method creates an InitialState predefined field object.")(name, instances, fileName[, ...]) | This method creates an InitialState predefined field object. |
    | [`KinematicHardening`](predefined.html#abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.KinematicHardening "abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.KinematicHardening (Python method) — This method creates a KinematicHardening object.")(name, region[, ...]) | This method creates a KinematicHardening object. |
    | [`MaterialAssignment`](predefined.html#abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.MaterialAssignment "abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.MaterialAssignment (Python method) — This method creates a MaterialAssignment predefined field object.")(name, instanceList[, ...]) | This method creates a MaterialAssignment predefined field object. |
    | [`PorePressure`](predefined.html#abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.PorePressure "abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.PorePressure (Python method) — This method creates a PorePressure predefined field object.")(name, region[, ...]) | This method creates a PorePressure predefined field object. |
    | [`Temperature`](predefined.html#abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.Temperature "abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.Temperature (Python method) — This method creates a Temperature object.")(name, createStepName, region[, ...]) | This method creates a Temperature object. |
    | [`Velocity`](predefined.html#abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.Velocity "abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.Velocity (Python method) — This method creates a Velocity predefined field object.")(name, region, velocity1, velocity2, ...) | This method creates a Velocity predefined field object. |
    | [`Saturation`](predefined.html#abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.Saturation "abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.Saturation (Python method) — This method creates a Saturation predefined field object.")(name, region[, distributionType, ...]) | This method creates a Saturation predefined field object. |
    | [`Stress`](predefined.html#abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.Stress "abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.Stress (Python method) — This method creates a Stress predefined field object.")(name, region[, distributionType, ...]) | This method creates a Stress predefined field object. |
    | [`Field`](predefined.html#abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.Field "abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.Field (Python method) — This method creates a Field object.")(name, createStepName, region[, ...]) | This method creates a Field object. |
    | [`VoidsRatio`](predefined.html#abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.VoidsRatio "abaqus.PredefinedField.PredefinedFieldModel.PredefinedFieldModel.VoidsRatio (Python method) — This method creates a PorePressure predefined field object.")(name, region[, distributionType, ...]) | This method creates a PorePressure predefined field object. |

    Inherited from [`BeamSectionProfileModel`](profile.html#abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel "abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel (Python class) — Bases: ModelBase")

    |  |  |
    | --- | --- |
    | [`beamProfilesFromOdb`](profile.html#abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.beamProfilesFromOdb "abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.beamProfilesFromOdb (Python method) — This method creates Profile objects by reading an output database. The new profiles are placed in the profiles repository.")(fileName) | This method creates Profile objects by reading an output database. |
    | [`ArbitraryProfile`](profile.html#abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.ArbitraryProfile "abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.ArbitraryProfile (Python method) — This method creates a ArbitraryProfile object.")(name, table) | This method creates a ArbitraryProfile object. |
    | [`BoxProfile`](profile.html#abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.BoxProfile "abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.BoxProfile (Python method) — This method creates a BoxProfile object.")(name, a, b, uniformThickness, t1) | This method creates a BoxProfile object. |
    | [`ChannelProfile`](profile.html#abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.ChannelProfile "abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.ChannelProfile (Python method) — This method creates a ChannelProfile object.")(name, l, h, b1, b2, t1, t2, t3, o) | This method creates a ChannelProfile object. |
    | [`CircularProfile`](profile.html#abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.CircularProfile "abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.CircularProfile (Python method) — This method creates a CircularProfile object.")(name, r) | This method creates a CircularProfile object. |
    | [`GeneralizedProfile`](profile.html#abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.GeneralizedProfile "abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.GeneralizedProfile (Python method) — This method creates a GeneralizedProfile object.")(name, area, i11, i12, ...) | This method creates a GeneralizedProfile object. |
    | [`HatProfile`](profile.html#abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.HatProfile "abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.HatProfile (Python method) — This method creates a HatProfile object.")(name, l, h, b, b1, b2, t1, t2, t3) | This method creates a HatProfile object. |
    | [`HexagonalProfile`](profile.html#abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.HexagonalProfile "abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.HexagonalProfile (Python method) — This method creates a HexagonalProfile object.")(name, r, t) | This method creates a HexagonalProfile object. |
    | [`IProfile`](profile.html#abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.IProfile "abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.IProfile (Python method) — This method creates an IProfile object.")(name, l, h, b1, b2, t1, t2, t3) | This method creates an IProfile object. |
    | [`LProfile`](profile.html#abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.LProfile "abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.LProfile (Python method) — This method creates a LProfile object.")(name, a, b, t1, t2) | This method creates a LProfile object. |
    | [`PipeProfile`](profile.html#abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.PipeProfile "abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.PipeProfile (Python method) — This method creates a PipeProfile object.")(name, r, t) | This method creates a PipeProfile object. |
    | [`RectangularProfile`](profile.html#abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.RectangularProfile "abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.RectangularProfile (Python method) — This method creates a RectangularProfile object.")(name, a, b) | This method creates a RectangularProfile object. |
    | [`TProfile`](profile.html#abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.TProfile "abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.TProfile (Python method) — This method creates a TProfile object.")(name, b, h, l, tf, tw) | This method creates a TProfile object. |
    | [`TrapezoidalProfile`](profile.html#abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.TrapezoidalProfile "abaqus.BeamSectionProfile.BeamSectionProfileModel.BeamSectionProfileModel.TrapezoidalProfile (Python method) — This method creates a TrapezoidalProfile object.")(name, a, b, c, d) | This method creates a TrapezoidalProfile object. |

    Inherited from [`OutputModel`](output.html#abaqus.StepOutput.OutputModel.OutputModel "abaqus.StepOutput.OutputModel.OutputModel (Python class) — Bases: ModelBase")

    |  |  |
    | --- | --- |
    | [`FieldOutputRequest`](output.html#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest (Python method) — This method creates a FieldOutputRequest object.")(name, createStepName[, ...]) | This method creates a FieldOutputRequest object. |
    | [`HistoryOutputRequest`](output.html#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest (Python method) — This method creates a HistoryOutputRequest object.")(name, createStepName[, ...]) | This method creates a HistoryOutputRequest object. |
    | [`IntegratedOutputSection`](output.html#abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection "abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection (Python method) — This method creates an IntegratedOutputSection object.")(name, surface[, ...]) | This method creates an IntegratedOutputSection object. |
    | [`TimePoint`](output.html#abaqus.StepOutput.OutputModel.OutputModel.TimePoint "abaqus.StepOutput.OutputModel.OutputModel.TimePoint (Python method) — This method creates a TimePoint object.")(name, points) | This method creates a TimePoint object. |

    Inherited from [`SectionModel`](section/index.html#abaqus.Section.SectionModel.SectionModel "abaqus.Section.SectionModel.SectionModel (Python class) — Bases: ModelBase")

    |  |  |
    | --- | --- |
    | [`AcousticInfiniteSection`](section/index.html#abaqus.Section.SectionModel.SectionModel.AcousticInfiniteSection "abaqus.Section.SectionModel.SectionModel.AcousticInfiniteSection (Python method) — This method creates an AcousticInfiniteSection object.")(name, material[, ...]) | This method creates an AcousticInfiniteSection object. |
    | [`AcousticInterfaceSection`](section/index.html#abaqus.Section.SectionModel.SectionModel.AcousticInterfaceSection "abaqus.Section.SectionModel.SectionModel.AcousticInterfaceSection (Python method) — This method creates an AcousticInterfaceSection object.")(name[, thickness]) | This method creates an AcousticInterfaceSection object. |
    | [`BeamSection`](section/index.html#abaqus.Section.SectionModel.SectionModel.BeamSection "abaqus.Section.SectionModel.SectionModel.BeamSection (Python method) — This method creates a BeamSection object.")(name, integration, profile[, ...]) | This method creates a BeamSection object. |
    | [`CohesiveSection`](section/index.html#abaqus.Section.SectionModel.SectionModel.CohesiveSection "abaqus.Section.SectionModel.SectionModel.CohesiveSection (Python method) — This method creates a CohesiveSection object.")(name, response, material[, ...]) | This method creates a CohesiveSection object. |
    | [`CompositeShellSection`](section/index.html#abaqus.Section.SectionModel.SectionModel.CompositeShellSection "abaqus.Section.SectionModel.SectionModel.CompositeShellSection (Python method) — This method creates a CompositeShellSection object.")(name, layup[, ...]) | This method creates a CompositeShellSection object. |
    | [`CompositeSolidSection`](section/index.html#abaqus.Section.SectionModel.SectionModel.CompositeSolidSection "abaqus.Section.SectionModel.SectionModel.CompositeSolidSection (Python method) — This method creates a CompositeSolidSection object.")(name, layup[, ...]) | This method creates a CompositeSolidSection object. |
    | [`ConnectorSection`](section/index.html#abaqus.Section.SectionModel.SectionModel.ConnectorSection "abaqus.Section.SectionModel.SectionModel.ConnectorSection (Python method) — This method creates a ConnectorSection object.")(name[, assembledType, ...]) | This method creates a ConnectorSection object. |
    | [`EulerianSection`](section/index.html#abaqus.Section.SectionModel.SectionModel.EulerianSection "abaqus.Section.SectionModel.SectionModel.EulerianSection (Python method) — This method creates a EulerianSection object.")(name, data) | This method creates a EulerianSection object. |
    | [`GasketSection`](section/index.html#abaqus.Section.SectionModel.SectionModel.GasketSection "abaqus.Section.SectionModel.SectionModel.GasketSection (Python method) — This method creates a GasketSection object.")(name, material[, ...]) | This method creates a GasketSection object. |
    | [`GeneralStiffnessSection`](section/index.html#abaqus.Section.SectionModel.SectionModel.GeneralStiffnessSection "abaqus.Section.SectionModel.SectionModel.GeneralStiffnessSection (Python method) — This method creates a GeneralStiffnessSection object.")(name, stiffnessMatrix) | This method creates a GeneralStiffnessSection object. |
    | [`HomogeneousShellSection`](section/index.html#abaqus.Section.SectionModel.SectionModel.HomogeneousShellSection "abaqus.Section.SectionModel.SectionModel.HomogeneousShellSection (Python method) — This method creates a HomogeneousShellSection object.")(name, material[, ...]) | This method creates a HomogeneousShellSection object. |
    | [`HomogeneousSolidSection`](section/index.html#abaqus.Section.SectionModel.SectionModel.HomogeneousSolidSection "abaqus.Section.SectionModel.SectionModel.HomogeneousSolidSection (Python method) — This method creates a HomogeneousSolidSection object.")(name, material[, ...]) | This method creates a HomogeneousSolidSection object. |
    | [`MembraneSection`](section/index.html#abaqus.Section.SectionModel.SectionModel.MembraneSection "abaqus.Section.SectionModel.SectionModel.MembraneSection (Python method) — This method creates a MembraneSection object.")(name, material[, thickness, ...]) | This method creates a MembraneSection object. |
    | [`MPCSection`](section/index.html#abaqus.Section.SectionModel.SectionModel.MPCSection "abaqus.Section.SectionModel.SectionModel.MPCSection (Python method) — This method creates a MPCSection object.")(name, mpcType[, userMode, userType]) | This method creates a MPCSection object. |
    | [`PEGSection`](section/index.html#abaqus.Section.SectionModel.SectionModel.PEGSection "abaqus.Section.SectionModel.SectionModel.PEGSection (Python method) — This method creates a PEGSection object.")(name, material[, thickness, ...]) | This method creates a PEGSection object. |
    | [`SurfaceSection`](section/index.html#abaqus.Section.SectionModel.SectionModel.SurfaceSection "abaqus.Section.SectionModel.SectionModel.SurfaceSection (Python method) — This method creates a SurfaceSection object.")(name[, useDensity, density]) | This method creates a SurfaceSection object. |
    | [`TrussSection`](section/index.html#abaqus.Section.SectionModel.SectionModel.TrussSection "abaqus.Section.SectionModel.SectionModel.TrussSection (Python method) — This method creates a TrussSection object.")(name, material[, area]) | This method creates a TrussSection object. |

    Inherited from [`SketchModel`](sketcher.html#abaqus.Sketcher.SketchModel.SketchModel "abaqus.Sketcher.SketchModel.SketchModel (Python class) — Bases: ModelBase")

    |  |  |
    | --- | --- |
    | [`ConstrainedSketch`](sketcher.html#abaqus.Sketcher.SketchModel.SketchModel.ConstrainedSketch "abaqus.Sketcher.SketchModel.SketchModel.ConstrainedSketch (Python method) — This method creates a ConstrainedSketch object. If the sketch cannot be created, the method returns None.")(name, sheetSize[, ...]) | This method creates a ConstrainedSketch object. |

    Inherited from [`StepModel`](step/index.html#abaqus.Step.StepModel.StepModel "abaqus.Step.StepModel.StepModel (Python class) — Bases: ModelBase")

    |  |  |
    | --- | --- |
    | [`AnnealStep`](step/index.html#abaqus.Step.StepModel.StepModel.AnnealStep "abaqus.Step.StepModel.StepModel.AnnealStep (Python method) — This method creates an AnnealStep object.")(name, previous[, description, ...]) | This method creates an AnnealStep object. |
    | [`BuckleStep`](step/index.html#abaqus.Step.StepModel.StepModel.BuckleStep "abaqus.Step.StepModel.StepModel.BuckleStep (Python method) — This method creates a BuckleStep object.")(name, previous, numEigen[, ...]) | This method creates a BuckleStep object. |
    | [`ComplexFrequencyStep`](step/index.html#abaqus.Step.StepModel.StepModel.ComplexFrequencyStep "abaqus.Step.StepModel.StepModel.ComplexFrequencyStep (Python method) — This method creates a ComplexFrequencyStep object.")(name, previous[, ...]) | This method creates a ComplexFrequencyStep object. |
    | [`CoupledTempDisplacementStep`](step/index.html#abaqus.Step.StepModel.StepModel.CoupledTempDisplacementStep "abaqus.Step.StepModel.StepModel.CoupledTempDisplacementStep (Python method) — This method creates a CoupledTempDisplacementStep object.")(name, previous) | This method creates a CoupledTempDisplacementStep object. |
    | [`CoupledThermalElectricalStructuralStep`](step/index.html#abaqus.Step.StepModel.StepModel.CoupledThermalElectricalStructuralStep "abaqus.Step.StepModel.StepModel.CoupledThermalElectricalStructuralStep (Python method) — This method creates a CoupledThermalElectricalStructuralStep object.")(name, ...) | This method creates a CoupledThermalElectricalStructuralStep object. |
    | [`CoupledThermalElectricStep`](step/index.html#abaqus.Step.StepModel.StepModel.CoupledThermalElectricStep "abaqus.Step.StepModel.StepModel.CoupledThermalElectricStep (Python method) — This method creates a CoupledThermalElectricStep object.")(name, previous[, ...]) | This method creates a CoupledThermalElectricStep object. |
    | [`DirectCyclicStep`](step/index.html#abaqus.Step.StepModel.StepModel.DirectCyclicStep "abaqus.Step.StepModel.StepModel.DirectCyclicStep (Python method) — This method creates a DirectCyclicStep object.")(name, previous[, ...]) | This method creates a DirectCyclicStep object. |
    | [`EmagTimeHarmonicStep`](step/index.html#abaqus.Step.StepModel.StepModel.EmagTimeHarmonicStep "abaqus.Step.StepModel.StepModel.EmagTimeHarmonicStep (Python method) — This method creates a EmagTimeHarmonicStep object.")(name, previous, ...[, ...]) | This method creates a EmagTimeHarmonicStep object. |
    | [`ExplicitDynamicsStep`](step/index.html#abaqus.Step.StepModel.StepModel.ExplicitDynamicsStep "abaqus.Step.StepModel.StepModel.ExplicitDynamicsStep (Python method) — This method creates an ExplicitDynamicsStep object.")(name, previous[, ...]) | This method creates an ExplicitDynamicsStep object. |
    | [`FrequencyStep`](step/index.html#abaqus.Step.StepModel.StepModel.FrequencyStep "abaqus.Step.StepModel.StepModel.FrequencyStep (Python method) — This method creates a FrequencyStep object.")(name, previous, eigensolver[, ...]) | This method creates a FrequencyStep object. |
    | [`GeostaticStep`](step/index.html#abaqus.Step.StepModel.StepModel.GeostaticStep "abaqus.Step.StepModel.StepModel.GeostaticStep (Python method) — This method creates a GeostaticStep object.")(name, previous[, description, ...]) | This method creates a GeostaticStep object. |
    | [`HeatTransferStep`](step/index.html#abaqus.Step.StepModel.StepModel.HeatTransferStep "abaqus.Step.StepModel.StepModel.HeatTransferStep (Python method) — This method creates a HeatTransferStep object.")(name, previous[, ...]) | This method creates a HeatTransferStep object. |
    | [`ImplicitDynamicsStep`](step/index.html#abaqus.Step.StepModel.StepModel.ImplicitDynamicsStep "abaqus.Step.StepModel.StepModel.ImplicitDynamicsStep (Python method) — This method creates an ImplicitDynamicsStep object.")(name, previous[, ...]) | This method creates an ImplicitDynamicsStep object. |
    | [`MassDiffusionStep`](step/index.html#abaqus.Step.StepModel.StepModel.MassDiffusionStep "abaqus.Step.StepModel.StepModel.MassDiffusionStep (Python method) — This method creates a MassDiffusionStep object.")(name, previous[, ...]) | This method creates a MassDiffusionStep object. |
    | [`ModalDynamicsStep`](step/index.html#abaqus.Step.StepModel.StepModel.ModalDynamicsStep "abaqus.Step.StepModel.StepModel.ModalDynamicsStep (Python method) — This method creates a ModalDynamicsStep object.")(name, previous[, ...]) | This method creates a ModalDynamicsStep object. |
    | [`RandomResponseStep`](step/index.html#abaqus.Step.StepModel.StepModel.RandomResponseStep "abaqus.Step.StepModel.StepModel.RandomResponseStep (Python method) — This method creates a RandomResponseStep object.")(name, previous, freq[, ...]) | This method creates a RandomResponseStep object. |
    | [`ResponseSpectrumStep`](step/index.html#abaqus.Step.StepModel.StepModel.ResponseSpectrumStep "abaqus.Step.StepModel.StepModel.ResponseSpectrumStep (Python method) — This method creates a ResponseSpectrumStep object.")(name, previous, components) | This method creates a ResponseSpectrumStep object. |
    | [`SoilsStep`](step/index.html#abaqus.Step.StepModel.StepModel.SoilsStep "abaqus.Step.StepModel.StepModel.SoilsStep (Python method) — This method creates a SoilsStep object.")(name, previous[, description, ...]) | This method creates a SoilsStep object. |
    | [`StaticLinearPerturbationStep`](step/index.html#abaqus.Step.StepModel.StepModel.StaticLinearPerturbationStep "abaqus.Step.StepModel.StepModel.StaticLinearPerturbationStep (Python method) — This method creates a StaticLinearPerturbationStep object.")(name, previous) | This method creates a StaticLinearPerturbationStep object. |
    | [`StaticRiksStep`](step/index.html#abaqus.Step.StepModel.StepModel.StaticRiksStep "abaqus.Step.StepModel.StepModel.StaticRiksStep (Python method) — This method creates a StaticRiksStep object.")(name, previous[, ...]) | This method creates a StaticRiksStep object. |
    | [`StaticStep`](step/index.html#abaqus.Step.StepModel.StepModel.StaticStep "abaqus.Step.StepModel.StepModel.StaticStep (Python method) — This method creates a StaticStep object.")(name, previous[, description, ...]) | This method creates a StaticStep object. |
    | [`SteadyStateDirectStep`](step/index.html#abaqus.Step.StepModel.StepModel.SteadyStateDirectStep "abaqus.Step.StepModel.StepModel.SteadyStateDirectStep (Python method) — This method creates a SteadyStateDirectStep object.")(name, previous, ...[, ...]) | This method creates a SteadyStateDirectStep object. |
    | [`SteadyStateModalStep`](step/index.html#abaqus.Step.StepModel.StepModel.SteadyStateModalStep "abaqus.Step.StepModel.StepModel.SteadyStateModalStep (Python method) — This method creates a SteadyStateModalStep object.")(name, previous, ...[, ...]) | This method creates a SteadyStateModalStep object. |
    | [`SteadyStateSubspaceStep`](step/index.html#abaqus.Step.StepModel.StepModel.SteadyStateSubspaceStep "abaqus.Step.StepModel.StepModel.SteadyStateSubspaceStep (Python method) — This method creates a SteadyStateSubspaceStep object.")(name, previous, ...) | This method creates a SteadyStateSubspaceStep object. |
    | [`SubspaceDynamicsStep`](step/index.html#abaqus.Step.StepModel.StepModel.SubspaceDynamicsStep "abaqus.Step.StepModel.StepModel.SubspaceDynamicsStep (Python method) — This method creates a SubspaceDynamicsStep object.")(name, previous[, ...]) | This method creates a SubspaceDynamicsStep object. |
    | [`SubstructureGenerateStep`](step/index.html#abaqus.Step.StepModel.StepModel.SubstructureGenerateStep "abaqus.Step.StepModel.StepModel.SubstructureGenerateStep (Python method) — This method creates a SubstructureGenerateStep object.")(name, previous, ...) | This method creates a SubstructureGenerateStep object. |
    | [`TempDisplacementDynamicsStep`](step/index.html#abaqus.Step.StepModel.StepModel.TempDisplacementDynamicsStep "abaqus.Step.StepModel.StepModel.TempDisplacementDynamicsStep (Python method) — This method creates a TempDisplacementDynamicsStep object.")(name, previous) | This method creates a TempDisplacementDynamicsStep object. |
    | [`ViscoStep`](step/index.html#abaqus.Step.StepModel.StepModel.ViscoStep "abaqus.Step.StepModel.StepModel.ViscoStep (Python method) — This method creates a ViscoStep object.")(name, previous[, description, ...]) | This method creates a ViscoStep object. |

    Inherited from [`ModelBase`](#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | `__init__`(name[, description, ...]) | This method creates a Model object. |
    | [`setValues`](#abaqus.Model.ModelBase.ModelBase.setValues "abaqus.Model.ModelBase.ModelBase.setValues (Python method) — This method modifies the Model object.")([description, noPartsInputFile, ...]) | This method modifies the Model object. |

    ---

    Member Details:

### Other Classes[¶](#other-classes "Permalink to this heading")

*class* KeywordBlock[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L8-L119)[¶](#abaqus.Model.ModelBase.KeywordBlock "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The KeywordBlock object contains a representation of its model in the Abaqus input file format. You may
    edit the contents of the KeywordBlock to add solver functionality that is not supported by Abaqus/CAE. As a
    general rule, edits to the KeywordBlock object should be made as the last step prior to writing the actual
    Abaqus input file, thus avoiding possible conflicts with changes made using other MDB commands. The
    KeywordBlock object has no constructor. A KeywordBlock object is created when you create a model object. A
    model object contains only one KeywordBlock object.

    Note

    This object can be accessed by:

    ```python
    mdb.models[name].keywordBlock
    ```

    Note

    Check [KeywordBlock on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-keywordblockpyc.htm?contextscope=all).

    Member Details:

    edited : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L23-L24)[¶](#abaqus.Model.ModelBase.KeywordBlock.edited "Permalink to this definition")
    :   A Boolean specifying whether the Keywords Editor has been used to change the model.

    insert(*[position](#abaqus.Model.ModelBase.KeywordBlock.insert.position "abaqus.Model.ModelBase.KeywordBlock.insert.position (Python parameter) — An Int specifying the position in the sieBlocks member after which the new string will be inserted.")*, *[text](#abaqus.Model.ModelBase.KeywordBlock.insert.text "abaqus.Model.ModelBase.KeywordBlock.insert.text (Python parameter) — A String specifying the text to be inserted.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L54-L71)[¶](#abaqus.Model.ModelBase.KeywordBlock.insert "Permalink to this definition")
    :   This method inserts a String at a specified position in the **sieBlocks** member.

        Note

        Check [KeywordBlock.insert on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-keywordblockpyc.htm?contextscope=all#simaker-keywordblockinsertpyc).

        Parameters:[¶](#abaqus.Model.ModelBase.KeywordBlock.insert-parameters "Permalink to this headline")
        :   position[¶](#abaqus.Model.ModelBase.KeywordBlock.insert.position "Permalink to this definition")
            :   An Int specifying the position in the **sieBlocks** member after which the new string will
                be inserted.

            text[¶](#abaqus.Model.ModelBase.KeywordBlock.insert.text "Permalink to this definition")
            :   A String specifying the text to be inserted. The text represents an Abaqus input file
                keyword and its associated data

        Raises:[¶](#abaqus.Model.ModelBase.KeywordBlock.insert-raises "Permalink to this headline")
        :   [**IndexError**](https://docs.python.org/3/library/exceptions.html#IndexError "(in Python v3.13)") –

    lastSynchCount : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L26-L28)[¶](#abaqus.Model.ModelBase.KeywordBlock.lastSynchCount "Permalink to this definition")
    :   A Float specifying the value of the counter associated with the Mdb object at the most
        recent synchronization.

    replace(*[position](#abaqus.Model.ModelBase.KeywordBlock.replace.position "abaqus.Model.ModelBase.KeywordBlock.replace.position (Python parameter) — An Int specifying the position of the String to be replaced in the sieBlocks member.")*, *[text](#abaqus.Model.ModelBase.KeywordBlock.replace.text "abaqus.Model.ModelBase.KeywordBlock.replace.text (Python parameter) — A String specifying the text to be replaced.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L73-L89)[¶](#abaqus.Model.ModelBase.KeywordBlock.replace "Permalink to this definition")
    :   This method replaces a String at a specified position in the **sieBlocks** member.

        Note

        Check [KeywordBlock.replace on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-keywordblockpyc.htm?contextscope=all#simaker-keywordblockreplacepyc).

        Parameters:[¶](#abaqus.Model.ModelBase.KeywordBlock.replace-parameters "Permalink to this headline")
        :   position[¶](#abaqus.Model.ModelBase.KeywordBlock.replace.position "Permalink to this definition")
            :   An Int specifying the position of the String to be replaced in the **sieBlocks** member.

            text[¶](#abaqus.Model.ModelBase.KeywordBlock.replace.text "Permalink to this definition")
            :   A String specifying the text to be replaced. The text represents an Abaqus input file
                keyword and its associated data.

        Raises:[¶](#abaqus.Model.ModelBase.KeywordBlock.replace-raises "Permalink to this headline")
        :   [**IndexError**](https://docs.python.org/3/library/exceptions.html#IndexError "(in Python v3.13)") –

    setValues(*[edited](#abaqus.Model.ModelBase.KeywordBlock.setValues.edited "abaqus.Model.ModelBase.KeywordBlock.setValues.edited (Python parameter) — A Boolean specifying whether this objects sieBlocks member has been edited.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L41-L52)[¶](#abaqus.Model.ModelBase.KeywordBlock.setValues "Permalink to this definition")
    :   This method modifies the KeywordBlock object.

        Note

        Check [KeywordBlock.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-keywordblockpyc.htm?contextscope=all#simaker-keywordblocksetvaluespyc).

        Parameters:[¶](#abaqus.Model.ModelBase.KeywordBlock.setValues-parameters "Permalink to this headline")
        :   edited=`0`[¶](#abaqus.Model.ModelBase.KeywordBlock.setValues.edited "Permalink to this definition")
            :   A Boolean specifying whether this objects **sieBlocks** member has been edited. Setting
                edited=False will set the **sieBlocks** member to an empty tuple, thereby discarding all
                previous edits.

    sieBlocks : --is-rst--:py:class:`tuple`\[:py:class:`str`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L30-L39)[¶](#abaqus.Model.ModelBase.KeywordBlock.sieBlocks "Permalink to this definition")
    :   A tuple of Strings specifying a sequence of Strings that is identical to the information
        written to the Abaqus input file. Each String in the sequence represents an Abaqus input
        file keyword along with the parameters and data lines associated with the keyword. A
        String can also be a comment in the input file. You initialize this data member by
        calling synchVersions. After you initialize the data member, you use calls to replace
        and insert to record your edits in the correct location. If the last call to
        synchVersions used the argument **storeNodesAndElements** = False, the entry for the
        keywords NODE and ELEMENT will contain only the keyword and its parameters, not the data
        lines.

    synchVersions(*[storeNodesAndElements](#abaqus.Model.ModelBase.KeywordBlock.synchVersions.storeNodesAndElements "abaqus.Model.ModelBase.KeywordBlock.synchVersions.storeNodesAndElements (Python parameter) — A Boolean specifying whether the nodal coordinates and element connectivities (i.e.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L91-L119)[¶](#abaqus.Model.ModelBase.KeywordBlock.synchVersions "Permalink to this definition")
    :   This method synchronizes, or merges, the edits made in this object with those made in the model using
        other scripting commands or the user interface. The synchVersions method updates the **sieBlocks**
        member. The **sieBlocks** member is empty prior to the first call to synchVersions. As a side effect,
        synchVersions sets **lastSynchCount** to the current value of the counter associated with the Mdb
        object, which is used to determine if synchronization is necessary.

        Note

        Check [KeywordBlock.synchVersions on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-keywordblockpyc.htm?contextscope=all#simaker-keywordblocksynchversionspyc).

        Parameters:[¶](#abaqus.Model.ModelBase.KeywordBlock.synchVersions-parameters "Permalink to this headline")
        :   storeNodesAndElements[¶](#abaqus.Model.ModelBase.KeywordBlock.synchVersions.storeNodesAndElements "Permalink to this definition")
            :   A Boolean specifying whether the nodal coordinates and element connectivities (i.e. the
                data lines for the *NODE and \*ELEMENT keyword blocks) are to be stored in the
                \*\*sieBlocks\** member. All other keywords and their data lines are always stored. The
                default value is True. If **storeNodesAndElements** is True, the size of the keywordBlock
                data will be similar to that of the input file. Since the KeywordBlock is stored in the
                Abaqus/CAE database, this will result in a larger database. It will also result in a
                slower execution of the synchVersions command. If **storeNodesAndElements** is False, the
                data lines are not stored in **sieBlocks**. Consequently, only set
                **storeNodesAndElements** = True if you wish to make changes to the **NODE** or **ELEMENT** data
                lines themselves. If your task is limited to reading nodal coordinates and element
                connectivities (i.e. not editing this information) then it is generally better to access
                this information from other parts of the Mdb.

        Raises:[¶](#abaqus.Model.ModelBase.KeywordBlock.synchVersions-raises "Permalink to this headline")
        :   [**IndexError**](https://docs.python.org/3/library/exceptions.html#IndexError "(in Python v3.13)") –

*class* ModelBase(*[name](#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase.__init__.name (Python parameter)")*, *[description](#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase.__init__.description (Python parameter)")=`''`*, *[stefanBoltzmann](#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase.__init__.stefanBoltzmann (Python parameter)")=`None`*, *[absoluteZero](#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase.__init__.absoluteZero (Python parameter)")=`None`*, *[waveFormulation](#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase.__init__.waveFormulation (Python parameter)")=`abaqusConstants.NOT_SET`*, *[modelType](#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase.__init__.modelType (Python parameter)")=`abaqusConstants.STANDARD_EXPLICIT`*, *[universalGas](#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase.__init__.universalGas (Python parameter)")=`None`*, *[copyConstraints](#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase.__init__.copyConstraints (Python parameter)")=`1`*, *[copyConnectors](#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase.__init__.copyConnectors (Python parameter)")=`1`*, *[copyInteractions](#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase.__init__.copyInteractions (Python parameter)")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L57-L374)[¶](#abaqus.Model.ModelBase.ModelBase "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    Abaqus creates a Model object named Model-1 when a session is started.

    Note

    This object can be accessed by:

    ```python
    mdb.models[name]
    ```

    The corresponding analysis keywords are:

    * PHYSICAL CONSTANTS

    Note

    Check [ModelBase on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?contextscope=all).

    Member Details:

    absoluteZero : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L77-L78)[¶](#abaqus.Model.ModelBase.ModelBase.absoluteZero "Permalink to this definition")
    :   None or a Float specifying the absolute zero constant. The default value is None.

    adaptiveMeshConstraints : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Adaptivity.AdaptiveMeshConstraint.AdaptiveMeshConstraint`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L208-L209)[¶](#abaqus.Model.ModelBase.ModelBase.adaptiveMeshConstraints "Permalink to this definition")
    :   A repository of AdaptiveMeshConstraint objects.

    adaptiveMeshControls : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Adaptivity.AdaptiveMeshControl.AdaptiveMeshControl`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L211-L212)[¶](#abaqus.Model.ModelBase.ModelBase.adaptiveMeshControls "Permalink to this definition")
    :   A repository of AdaptiveMeshControl objects.

    amplitudes : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Amplitude.Amplitude.Amplitude`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L137-L138)[¶](#abaqus.Model.ModelBase.ModelBase.amplitudes "Permalink to this definition")
    :   A repository of Amplitude objects.

    analyticalFields : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Field.AnalyticalField.AnalyticalField`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L149-L150)[¶](#abaqus.Model.ModelBase.ModelBase.analyticalFields "Permalink to this definition")
    :   A repository of AnalyticalField objects.

    boundaryConditions : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.BoundaryCondition.BoundaryCondition.BoundaryCondition`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L143-L144)[¶](#abaqus.Model.ModelBase.ModelBase.boundaryConditions "Permalink to this definition")
    :   A repository of BoundaryCondition objects.

    calibrations : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Calibration.Calibration.Calibration`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L187-L188)[¶](#abaqus.Model.ModelBase.ModelBase.calibrations "Permalink to this definition")
    :   A repository of Calibration objects.

    constraints : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Constraint.Constraint.Constraint`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L146-L147)[¶](#abaqus.Model.ModelBase.ModelBase.constraints "Permalink to this definition")
    :   A repository of ConstrainedSketchConstraint objects.

    contactControls : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Interaction.ContactControl.ContactControl`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L164-L165)[¶](#abaqus.Model.ModelBase.ModelBase.contactControls "Permalink to this definition")
    :   A repository of ContactControl objects.

    contactInitializations : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Interaction.ContactInitialization.ContactInitialization`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L167-L168)[¶](#abaqus.Model.ModelBase.ModelBase.contactInitializations "Permalink to this definition")
    :   A repository of ContactInitialization objects.

    contactStabilizations : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Interaction.ContactStabilization.ContactStabilization`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L170-L171)[¶](#abaqus.Model.ModelBase.ModelBase.contactStabilizations "Permalink to this definition")
    :   A repository of ContactStabilization objects.

    copyConnectors : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L123-L125)[¶](#abaqus.Model.ModelBase.ModelBase.copyConnectors "Permalink to this definition")
    :   A boolean specifying the status of connectors created in a model, in the model which
        instances this model.

    copyConstraints : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L119-L121)[¶](#abaqus.Model.ModelBase.ModelBase.copyConstraints "Permalink to this definition")
    :   A boolean specifying the status of constraints created in a model, in the model which
        instances this model.

    copyInteractions : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L127-L129)[¶](#abaqus.Model.ModelBase.ModelBase.copyInteractions "Permalink to this definition")
    :   A boolean specifying the status of interactions created in a model, in the model which
        instances this model.

    description : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L106-L108)[¶](#abaqus.Model.ModelBase.ModelBase.description "Permalink to this definition")
    :   A String specifying the purpose and contents of the Model object. The default value is
        an empty string.

    discreteFields : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Field.DiscreteField.DiscreteField`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L152-L153)[¶](#abaqus.Model.ModelBase.ModelBase.discreteFields "Permalink to this definition")
    :   A repository of DiscreteField objects.

    endRestartStep : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L96-L98)[¶](#abaqus.Model.ModelBase.ModelBase.endRestartStep "Permalink to this definition")
    :   A Boolean specifying that the step specified by **restartStep** should be terminated at
        the increment specified by **restartIncrement**.

    eventSeriesDatas : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.TableCollection.EventSeriesData.EventSeriesData`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L234-L236)[¶](#abaqus.Model.ModelBase.ModelBase.eventSeriesDatas "Permalink to this definition")
    :   A repository of EventSeriesData objects.

        New in version 2020: The `eventSeriesDatas` attribute was added.

    eventSeriesTypes : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.TableCollection.EventSeriesType.EventSeriesType`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L234-L236)[¶](#abaqus.Model.ModelBase.ModelBase.eventSeriesTypes "Permalink to this definition")
    :   A repository of EventSeriesType objects.

        New in version 2020: The `eventSeriesTypes` attribute was added.

    featureOptions : --is-rst--:py:class:`~abaqus.Feature.FeatureOptions.FeatureOptions` = `<abaqus.Feature.FeatureOptions.FeatureOptions object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L205-L206)[¶](#abaqus.Model.ModelBase.ModelBase.featureOptions "Permalink to this definition")
    :   A FeatureOptions object.

    fieldOutputRequests : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.StepOutput.FieldOutputRequest.FieldOutputRequest`] = `{'F-Output-1': <abaqus.StepOutput.FieldOutputRequest.FieldOutputRequest object>}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L223-L224)[¶](#abaqus.Model.ModelBase.ModelBase.fieldOutputRequests "Permalink to this definition")
    :   A repository of FieldOutputRequest objects.

    filters : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Filter.Filter.Filter`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L217-L218)[¶](#abaqus.Model.ModelBase.ModelBase.filters "Permalink to this definition")
    :   A repository of Filter objects.

    globalJob : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L116-L117)[¶](#abaqus.Model.ModelBase.ModelBase.globalJob "Permalink to this definition")
    :   A String specifying the name of the job that generated the results for the global model.

    historyOutputRequests : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.StepOutput.HistoryOutputRequest.HistoryOutputRequest`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L226-L227)[¶](#abaqus.Model.ModelBase.ModelBase.historyOutputRequests "Permalink to this definition")
    :   A repository of HistoryOutputRequest objects.

    integratedOutputSections : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.StepOutput.IntegratedOutputSection.IntegratedOutputSection`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L220-L221)[¶](#abaqus.Model.ModelBase.ModelBase.integratedOutputSections "Permalink to this definition")
    :   A repository of IntegratedOutputSection objects.

    interactionProperties : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Interaction.ContactProperty.ContactProperty`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L161-L162)[¶](#abaqus.Model.ModelBase.ModelBase.interactionProperties "Permalink to this definition")
    :   A repository of InteractionProperty objects.

    interactions : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Interaction.Interaction.Interaction`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L158-L159)[¶](#abaqus.Model.ModelBase.ModelBase.interactions "Permalink to this definition")
    :   A repository of Interaction objects.

    keywordBlock : --is-rst--:py:class:`~abaqus.Model.KeywordBlock.KeywordBlock` = `<abaqus.Model.KeywordBlock.KeywordBlock object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L131-L132)[¶](#abaqus.Model.ModelBase.ModelBase.keywordBlock "Permalink to this definition")
    :   A KeywordBlock object.

    lastChangedCount : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L103-L104)[¶](#abaqus.Model.ModelBase.ModelBase.lastChangedCount "Permalink to this definition")
    :   A Float specifying the time stamp that indicates when the model was last changed.

    linkedInstances : --is-rst--:py:class:`tuple` = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L173-L175)[¶](#abaqus.Model.ModelBase.ModelBase.linkedInstances "Permalink to this definition")
    :   A tuple of tuples of Strings specifying the linked child PartInstance name in the
        current model to the corresponding parent PartInstance name in a different model.

    linkedParts : --is-rst--:py:class:`tuple` = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L177-L179)[¶](#abaqus.Model.ModelBase.ModelBase.linkedParts "Permalink to this definition")
    :   A tuple of tuples of Strings specifying the linked child Part name in the current model
        to the corresponding parent Part name in a different model.

    loads : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Load.Load.Load`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L181-L182)[¶](#abaqus.Model.ModelBase.ModelBase.loads "Permalink to this definition")
    :   A repository of Load objects.

    materials : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Material.Material.Material`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L184-L185)[¶](#abaqus.Model.ModelBase.ModelBase.materials "Permalink to this definition")
    :   A repository of Material objects.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L71-L72)[¶](#abaqus.Model.ModelBase.ModelBase.name "Permalink to this definition")
    :   A String specifying the repository key.

    noPartsInputFile : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L88-L90)[¶](#abaqus.Model.ModelBase.ModelBase.noPartsInputFile "Permalink to this definition")
    :   A Boolean specifying whether an input file should be written without parts and
        assemblies. The default value is OFF.

    optimizationTasks : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Optimization.OptimizationTask.OptimizationTask`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L229-L230)[¶](#abaqus.Model.ModelBase.ModelBase.optimizationTasks "Permalink to this definition")
    :   A repository of OptimizationTask objects.

    parts : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Part.Part.Part`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L199-L200)[¶](#abaqus.Model.ModelBase.ModelBase.parts "Permalink to this definition")
    :   A repository of Part objects.

    predefinedFields : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.PredefinedField.PredefinedField.PredefinedField`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L155-L156)[¶](#abaqus.Model.ModelBase.ModelBase.predefinedFields "Permalink to this definition")
    :   A repository of PredefinedField objects.

    profiles : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.BeamSectionProfile.Profile.Profile`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L140-L141)[¶](#abaqus.Model.ModelBase.ModelBase.profiles "Permalink to this definition")
    :   A repository of Profile objects.

    remeshingRules : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Adaptivity.RemeshingRule.RemeshingRule`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L193-L194)[¶](#abaqus.Model.ModelBase.ModelBase.remeshingRules "Permalink to this definition")
    :   A repository of RemeshingRule objects.

    restartIncrement : --is-rst--:py:class:`int` | :py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py)[¶](#abaqus.Model.ModelBase.ModelBase.restartIncrement "Permalink to this definition")
    :   An Int specifying the increment, interval, iteration or cycle where the restart analysis
        will start. To select the end of the step use the SymbolicConstant STEP\_END.

    restartJob : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L110-L111)[¶](#abaqus.Model.ModelBase.ModelBase.restartJob "Permalink to this definition")
    :   A String specifying the name of the job that generated the restart data.

    restartStep : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L113-L114)[¶](#abaqus.Model.ModelBase.ModelBase.restartStep "Permalink to this definition")
    :   A String specifying the name of the step where the restart analysis will start.

    rootAssembly : --is-rst--:py:class:`~abaqus.Assembly.Assembly.Assembly`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py)[¶](#abaqus.Model.ModelBase.ModelBase.rootAssembly "Permalink to this definition")
    :   An Assembly object.

    sections : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Section.Section.Section`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L190-L191)[¶](#abaqus.Model.ModelBase.ModelBase.sections "Permalink to this definition")
    :   A repository of Section objects.

    setValues(*[description](#abaqus.Model.ModelBase.ModelBase.setValues.description "abaqus.Model.ModelBase.ModelBase.setValues.description (Python parameter) — A String specifying the purpose and contents of the Model object.")=`''`*, *[noPartsInputFile](#abaqus.Model.ModelBase.ModelBase.setValues.noPartsInputFile "abaqus.Model.ModelBase.ModelBase.setValues.noPartsInputFile (Python parameter) — A Boolean specifying whether an input file should be written without parts and assemblies.")=`0`*, *[absoluteZero](#abaqus.Model.ModelBase.ModelBase.setValues.absoluteZero "abaqus.Model.ModelBase.ModelBase.setValues.absoluteZero (Python parameter) — None or a Float specifying the absolute zero constant.")=`None`*, *[stefanBoltzmann](#abaqus.Model.ModelBase.ModelBase.setValues.stefanBoltzmann "abaqus.Model.ModelBase.ModelBase.setValues.stefanBoltzmann (Python parameter) — None or a Float specifying the Stefan-Boltzmann constant.")=`None`*, *[waveFormulation](#abaqus.Model.ModelBase.ModelBase.setValues.waveFormulation "abaqus.Model.ModelBase.ModelBase.setValues.waveFormulation (Python parameter) — A SymbolicConstant specifying the type of incident wave formulation to be used in acoustic problems.")=`abaqusConstants.NOT_SET`*, *[universalGas](#abaqus.Model.ModelBase.ModelBase.setValues.universalGas "abaqus.Model.ModelBase.ModelBase.setValues.universalGas (Python parameter) — None or a Float specifying the universal gas constant.")=`None`*, *[restartJob](#abaqus.Model.ModelBase.ModelBase.setValues.restartJob "abaqus.Model.ModelBase.ModelBase.setValues.restartJob (Python parameter) — A String specifying the name of the job that generated the restart data.")=`''`*, *[restartStep](#abaqus.Model.ModelBase.ModelBase.setValues.restartStep "abaqus.Model.ModelBase.ModelBase.setValues.restartStep (Python parameter) — A String specifying the name of the step where the restart analysis will start.")=`''`*, *[restartIncrement](#abaqus.Model.ModelBase.ModelBase.setValues.restartIncrement "abaqus.Model.ModelBase.ModelBase.setValues.restartIncrement (Python parameter) — An Int specifying the increment, interval, iteration or cycle where the restart analysis will start.")=`None`*, *[endRestartStep](#abaqus.Model.ModelBase.ModelBase.setValues.endRestartStep "abaqus.Model.ModelBase.ModelBase.setValues.endRestartStep (Python parameter) — A Boolean specifying that the step specified by restartStep should be terminated at the increment specified by restartIncrement.")=`0`*, *[globalJob](#abaqus.Model.ModelBase.ModelBase.setValues.globalJob "abaqus.Model.ModelBase.ModelBase.setValues.globalJob (Python parameter) — A String specifying the name of the job that generated the results for the global model.")=`''`*, *[shellToSolid](#abaqus.Model.ModelBase.ModelBase.setValues.shellToSolid "abaqus.Model.ModelBase.ModelBase.setValues.shellToSolid (Python parameter) — A Boolean specifying that a shell global model drives a solid submodel.")=`0`*, *[copyConstraints](#abaqus.Model.ModelBase.ModelBase.setValues.copyConstraints "abaqus.Model.ModelBase.ModelBase.setValues.copyConstraints (Python parameter) — A Boolean specifying whether to copy the constraints created in the model to the model that instances this model.")=`0`*, *[copyConnectors](#abaqus.Model.ModelBase.ModelBase.setValues.copyConnectors "abaqus.Model.ModelBase.ModelBase.setValues.copyConnectors (Python parameter) — A Boolean specifying whether to copy the connectors created in the model to the model that instances this model")=`0`*, *[copyInteractions](#abaqus.Model.ModelBase.ModelBase.setValues.copyInteractions "abaqus.Model.ModelBase.ModelBase.setValues.copyInteractions (Python parameter) — A Boolean specifying whether to copy the interactions created in the model to the model that instances this model.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L311-L374)[¶](#abaqus.Model.ModelBase.ModelBase.setValues "Permalink to this definition")
    :   This method modifies the Model object.

        Note

        Check [ModelBase.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?contextscope=all#simaker-modelsetvaluespyc).

        Parameters:[¶](#abaqus.Model.ModelBase.ModelBase.setValues-parameters "Permalink to this headline")
        :   description=`''`[¶](#abaqus.Model.ModelBase.ModelBase.setValues.description "Permalink to this definition")
            :   A String specifying the purpose and contents of the Model object. The default value is
                an empty string.

            noPartsInputFile=`0`[¶](#abaqus.Model.ModelBase.ModelBase.setValues.noPartsInputFile "Permalink to this definition")
            :   A Boolean specifying whether an input file should be written without parts and
                assemblies. The default value is OFF.

            absoluteZero=`None`[¶](#abaqus.Model.ModelBase.ModelBase.setValues.absoluteZero "Permalink to this definition")
            :   None or a Float specifying the absolute zero constant. The default value is None.

            stefanBoltzmann=`None`[¶](#abaqus.Model.ModelBase.ModelBase.setValues.stefanBoltzmann "Permalink to this definition")
            :   None or a Float specifying the Stefan-Boltzmann constant. The default value is None.

            waveFormulation=`abaqusConstants.NOT_SET`[¶](#abaqus.Model.ModelBase.ModelBase.setValues.waveFormulation "Permalink to this definition")
            :   A SymbolicConstant specifying the type of incident wave formulation to be used in
                acoustic problems. Possible values are NOT\_SET, SCATTERED, and TOTAL. The default value
                is NOT\_SET.

            universalGas=`None`[¶](#abaqus.Model.ModelBase.ModelBase.setValues.universalGas "Permalink to this definition")
            :   None or a Float specifying the universal gas constant. The default value is None.

            restartJob=`''`[¶](#abaqus.Model.ModelBase.ModelBase.setValues.restartJob "Permalink to this definition")
            :   A String specifying the name of the job that generated the restart data.

            restartStep=`''`[¶](#abaqus.Model.ModelBase.ModelBase.setValues.restartStep "Permalink to this definition")
            :   A String specifying the name of the step where the restart analysis will start.

            restartIncrement=`None`[¶](#abaqus.Model.ModelBase.ModelBase.setValues.restartIncrement "Permalink to this definition")
            :   An Int specifying the increment, interval, iteration or cycle where the restart analysis
                will start. To select the end of the step use the SymbolicConstant STEP\_END.

            endRestartStep=`0`[¶](#abaqus.Model.ModelBase.ModelBase.setValues.endRestartStep "Permalink to this definition")
            :   A Boolean specifying that the step specified by **restartStep** should be terminated at
                the increment specified by **restartIncrement**.

            globalJob=`''`[¶](#abaqus.Model.ModelBase.ModelBase.setValues.globalJob "Permalink to this definition")
            :   A String specifying the name of the job that generated the results for the global model.

            shellToSolid=`0`[¶](#abaqus.Model.ModelBase.ModelBase.setValues.shellToSolid "Permalink to this definition")
            :   A Boolean specifying that a shell global model drives a solid submodel.

            copyConstraints=`0`[¶](#abaqus.Model.ModelBase.ModelBase.setValues.copyConstraints "Permalink to this definition")
            :   A Boolean specifying whether to copy the constraints created in the model to the model
                that instances this model.

            copyConnectors=`0`[¶](#abaqus.Model.ModelBase.ModelBase.setValues.copyConnectors "Permalink to this definition")
            :   A Boolean specifying whether to copy the connectors created in the model to the model
                that instances this model

            copyInteractions=`0`[¶](#abaqus.Model.ModelBase.ModelBase.setValues.copyInteractions "Permalink to this definition")
            :   A Boolean specifying whether to copy the interactions created in the model to the model
                that instances this model.

    shellToSolid : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L100-L101)[¶](#abaqus.Model.ModelBase.ModelBase.shellToSolid "Permalink to this definition")
    :   A Boolean specifying that a shell global model drives a solid submodel.

    sketches : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Sketcher.ConstrainedSketch.ConstrainedSketch`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L196-L197)[¶](#abaqus.Model.ModelBase.ModelBase.sketches "Permalink to this definition")
    :   A repository of ConstrainedSketch objects.

    stefanBoltzmann : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L74-L75)[¶](#abaqus.Model.ModelBase.ModelBase.stefanBoltzmann "Permalink to this definition")
    :   None or a Float specifying the Stefan-Boltzmann constant. The default value is None.

    steps : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Step.Step.Step`] = `{'Initial': <abaqus.Step.InitialStep.InitialStep object>}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L202-L203)[¶](#abaqus.Model.ModelBase.ModelBase.steps "Permalink to this definition")
    :   A repository of Step objects.

    tableCollections : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.TableCollection.TableCollection.TableCollection`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L234-L236)[¶](#abaqus.Model.ModelBase.ModelBase.tableCollections "Permalink to this definition")
    :   A repository of TableCollection objects.

        New in version 2020: The `tableCollections` attribute was added.

    timePoints : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.StepOutput.TimePoint.TimePoint`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L214-L215)[¶](#abaqus.Model.ModelBase.ModelBase.timePoints "Permalink to this definition")
    :   A repository of TimePoint objects.

    universalGas : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L85-L86)[¶](#abaqus.Model.ModelBase.ModelBase.universalGas "Permalink to this definition")
    :   None or a Float specifying the universal gas constant. The default value is None.

    waveFormulation : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'NOT_SET'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Model/ModelBase.py#L80-L83)[¶](#abaqus.Model.ModelBase.ModelBase.waveFormulation "Permalink to this definition")
    :   A SymbolicConstant specifying the type of incident wave formulation to be used in
        acoustic problems. Possible values are NOT\_SET, SCATTERED, and TOTAL. The default value
        is NOT\_SET.

[Back to top](#)