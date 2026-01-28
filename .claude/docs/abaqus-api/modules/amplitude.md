# Abaqus AMPLITUDE Module API Reference

> Source: [https://hailin.wang/abqpy/en/2025/reference/mdb/model/amplitude.html](https://hailin.wang/abqpy/en/2025/reference/mdb/model/amplitude.html)
> Downloaded for offline use by Claude Code skills.

---

# Amplitude[¶](#amplitude "Permalink to this heading")

Amplitude commands are used to create arbitrary time or frequency variations of load, displacement, and some interaction attributes throughout a step using step time or throughout an analysis using total time.

## Create amplitudes[¶](#create-amplitudes "Permalink to this heading")

### In Mdb[¶](#in-mdb "Permalink to this heading")

*class* AmplitudeModel(*[name](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.__init__.name (Python parameter)")*, *[description](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.__init__.description (Python parameter)")=`''`*, *[stefanBoltzmann](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.__init__.stefanBoltzmann (Python parameter)")=`None`*, *[absoluteZero](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.__init__.absoluteZero (Python parameter)")=`None`*, *[waveFormulation](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.__init__.waveFormulation (Python parameter)")=`abaqusConstants.NOT_SET`*, *[modelType](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.__init__.modelType (Python parameter)")=`abaqusConstants.STANDARD_EXPLICIT`*, *[universalGas](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.__init__.universalGas (Python parameter)")=`None`*, *[copyConstraints](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.__init__.copyConstraints (Python parameter)")=`1`*, *[copyConnectors](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.__init__.copyConnectors (Python parameter)")=`1`*, *[copyInteractions](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.__init__.copyInteractions (Python parameter)")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeModel.py#L36-L566)[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel "Permalink to this definition")
:   Bases: [`ModelBase`](index.html#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase (Python class) — Bases: object")

    Abaqus creates a Model object named Model-1 when a session is started.

    Note

    This object can be accessed by:

    ```python
    mdb.models[name]
    ```

    Note

    Check [AmplitudeModel on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?contextscope=all).

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
    | [`ActuatorAmplitude`](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ActuatorAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ActuatorAmplitude (Python method) — This method creates a ActuatorAmplitude object.")(name[, timeSpan]) | This method creates a ActuatorAmplitude object. |
    | [`DecayAmplitude`](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude (Python method) — This method creates a DecayAmplitude object.")(name, initial, maximum, ...) | This method creates a DecayAmplitude object. |
    | [`EquallySpacedAmplitude`](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude (Python method) — This method creates an EquallySpacedAmplitude object.")(name, fixedInterval, data) | This method creates an EquallySpacedAmplitude object. |
    | [`ModulatedAmplitude`](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude (Python method) — This method creates a ModulatedAmplitude object.")(name, initial, magnitude, ...) | This method creates a ModulatedAmplitude object. |
    | [`PeriodicAmplitude`](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude (Python method) — This method creates a PeriodicAmplitude object.")(name, frequency, start, ...) | This method creates a PeriodicAmplitude object. |
    | [`PsdDefinition`](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition (Python method) — This method creates a PsdDefinition object.")(name, data[, unitType, ...]) | This method creates a PsdDefinition object. |
    | [`SmoothStepAmplitude`](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SmoothStepAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SmoothStepAmplitude (Python method) — This method creates a SmoothStepAmplitude object.")(name, data[, timeSpan]) | This method creates a SmoothStepAmplitude object. |
    | [`SolutionDependentAmplitude`](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude (Python method) — This method creates a SolutionDependentAmplitude object.")(name[, initial, ...]) | This method creates a SolutionDependentAmplitude object. |
    | [`SpectrumAmplitude`](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude (Python method) — This method creates a SpectrumAmplitude object.")(name, method, data[, ...]) | This method creates a SpectrumAmplitude object. |
    | [`TabularAmplitude`](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.TabularAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.TabularAmplitude (Python method) — This method creates a TabularAmplitude object.")(name, data[, smooth, timeSpan]) | This method creates a TabularAmplitude object. |

    Inherited from [`ModelBase`](index.html#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | `__init__`(name[, description, ...]) | This method creates a Model object. |
    | [`setValues`](index.html#abaqus.Model.ModelBase.ModelBase.setValues "abaqus.Model.ModelBase.ModelBase.setValues (Python method) — This method modifies the Model object.")([description, noPartsInputFile, ...]) | This method modifies the Model object. |

    ---

    Member Details:

    ActuatorAmplitude(*[name](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ActuatorAmplitude.name "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ActuatorAmplitude.name (Python parameter) — A String specifying the repository key.")*, *[timeSpan](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ActuatorAmplitude.timeSpan "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ActuatorAmplitude.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeModel.py#L46-L75)[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ActuatorAmplitude "Permalink to this definition")
    :   This method creates a ActuatorAmplitude object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ActuatorAmplitude
        session.odbs[name].ActuatorAmplitude
        ```

        Note

        Check [ActuatorAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-actuatoramplitudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ActuatorAmplitude-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ActuatorAmplitude.name "Permalink to this definition")
            :   A String specifying the repository key.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ActuatorAmplitude.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

        Returns:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ActuatorAmplitude-returns "Permalink to this headline")
        :   An ActuatorAmplitude object.

        Return type:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ActuatorAmplitude-return-type "Permalink to this headline")
        :   [`ActuatorAmplitude`](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ActuatorAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ActuatorAmplitude (Python method) — This method creates a ActuatorAmplitude object.")

        Raises:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ActuatorAmplitude-raises "Permalink to this headline")
        :   * **InvalidNameError** –
            * **RangeError** –

    DecayAmplitude(*[name](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude.name "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude.name (Python parameter) — A String specifying the repository key.")*, *[initial](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude.initial "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude.initial (Python parameter) — A Float specifying the constant A0A0.")*, *[maximum](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude.maximum "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude.maximum (Python parameter) — A Float specifying the coefficient AA.")*, *[start](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude.start "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude.start (Python parameter) — A Float specifying the starting time t0t0.")*, *[decayTime](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude.decayTime "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude.decayTime (Python parameter) — A Float specifying the decay time tdtd.")*, *[timeSpan](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude.timeSpan "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeModel.py#L77-L122)[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude "Permalink to this definition")
    :   This method creates a DecayAmplitude object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].DecayAmplitude
        session.odbs[name].DecayAmplitude
        ```

        Note

        Check [DecayAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-decayamplitudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude.name "Permalink to this definition")
            :   A String specifying the repository key.

            initial[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude.initial "Permalink to this definition")
            :   A Float specifying the constant A0A0.

            maximum[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude.maximum "Permalink to this definition")
            :   A Float specifying the coefficient AA.

            start[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude.start "Permalink to this definition")
            :   A Float specifying the starting time t0t0. Possible values are non-negative numbers.

            decayTime[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude.decayTime "Permalink to this definition")
            :   A Float specifying the decay time tdtd. Possible values are non-negative numbers.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

        Returns:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude-returns "Permalink to this headline")
        :   A DecayAmplitude object.

        Return type:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude-return-type "Permalink to this headline")
        :   [`DecayAmplitude`](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude (Python method) — This method creates a DecayAmplitude object.")

        Raises:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.DecayAmplitude-raises "Permalink to this headline")
        :   * **InvalidNameError** –
            * **RangeError** –

    EquallySpacedAmplitude(*[name](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude.name "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude.name (Python parameter) — A String specifying the repository key.")*, *[fixedInterval](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude.fixedInterval "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude.fixedInterval (Python parameter) — A Float specifying the fixed time interval at which the amplitude data are given. Possible values are positive numbers.")*, *[data](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude.data "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude.data (Python parameter) — A sequence of Floats specifying the amplitude values.")*, *[begin](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude.begin "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude.begin (Python parameter) — A Float specifying the time at which the first amplitude data are given.")=`0`*, *[smooth](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude.smooth "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude.smooth (Python parameter) — The SymbolicConstant SOLVER_DEFAULT or a Float specifying the degree of smoothing. Possible float values are 0 ≤ smoothing ≤ 0.5.")=`abaqusConstants.SOLVER_DEFAULT`*, *[timeSpan](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude.timeSpan "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeModel.py#L124-L174)[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude "Permalink to this definition")
    :   This method creates an EquallySpacedAmplitude object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].EquallySpacedAmplitude
        session.odbs[name].EquallySpacedAmplitude
        ```

        Note

        Check [EquallySpacedAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-equallyspacedamplitudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude.name "Permalink to this definition")
            :   A String specifying the repository key.

            fixedInterval[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude.fixedInterval "Permalink to this definition")
            :   A Float specifying the fixed time interval at which the amplitude data are given.
                Possible values are positive numbers.

            data[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude.data "Permalink to this definition")
            :   A sequence of Floats specifying the amplitude values.

            begin=`0`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude.begin "Permalink to this definition")
            :   A Float specifying the time at which the first amplitude data are given. Possible values
                are non-negative numbers. The default value is 0.0.

            smooth=`abaqusConstants.SOLVER_DEFAULT`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude.smooth "Permalink to this definition")
            :   The SymbolicConstant SOLVER\_DEFAULT or a Float specifying the degree of smoothing.
                Possible float values are 0 ≤ **smoothing** ≤ 0.5. If **smooth** = SOLVER\_DEFAULT, the
                default degree of smoothing will be determined by the solver. The default value is
                SOLVER\_DEFAULT.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

        Returns:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude-returns "Permalink to this headline")
        :   An EquallySpacedAmplitude object.

        Return type:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude-return-type "Permalink to this headline")
        :   [`EquallySpacedAmplitude`](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude (Python method) — This method creates an EquallySpacedAmplitude object.")

        Raises:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.EquallySpacedAmplitude-raises "Permalink to this headline")
        :   * **InvalidNameError** –
            * **RangeError** –

    ModulatedAmplitude(*[name](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude.name "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude.name (Python parameter) — A String specifying the repository key.")*, *[initial](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude.initial "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude.initial (Python parameter) — A Float specifying the constant A0A0.")*, *[magnitude](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude.magnitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude.magnitude (Python parameter) — A Float specifying the coefficient AA.")*, *[start](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude.start "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude.start (Python parameter) — A Float specifying the starting time t0t0.")*, *[frequency1](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude.frequency1 "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude.frequency1 (Python parameter) — A Float specifying the circular frequency 1 (ω1ω1).")*, *[frequency2](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude.frequency2 "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude.frequency2 (Python parameter) — A Float specifying the circular frequency 2 (ω2ω2).")*, *[timeSpan](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude.timeSpan "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeModel.py#L176-L228)[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude "Permalink to this definition")
    :   This method creates a ModulatedAmplitude object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ModulatedAmplitude
        session.odbs[name].ModulatedAmplitude
        ```

        Note

        Check [ModulatedAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modulatedamplitudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude.name "Permalink to this definition")
            :   A String specifying the repository key.

            initial[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude.initial "Permalink to this definition")
            :   A Float specifying the constant A0A0.

            magnitude[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude.magnitude "Permalink to this definition")
            :   A Float specifying the coefficient AA.

            start[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude.start "Permalink to this definition")
            :   A Float specifying the starting time t0t0. Possible values are non-negative numbers.

            frequency1[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude.frequency1 "Permalink to this definition")
            :   A Float specifying the circular frequency 1 (ω1ω1). Possible values are positive
                numbers.

            frequency2[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude.frequency2 "Permalink to this definition")
            :   A Float specifying the circular frequency 2 (ω2ω2). Possible values are positive
                numbers.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

        Returns:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude-returns "Permalink to this headline")
        :   A ModulatedAmplitude object.

        Return type:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude-return-type "Permalink to this headline")
        :   [`ModulatedAmplitude`](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude (Python method) — This method creates a ModulatedAmplitude object.")

        Raises:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.ModulatedAmplitude-raises "Permalink to this headline")
        :   * **InvalidNameError** –
            * **RangeError** –

    PeriodicAmplitude(*[name](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude.name "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude.name (Python parameter) — A String specifying the repository key.")*, *[frequency](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude.frequency "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude.frequency (Python parameter) — A Float specifying the circular frequency ωω.")*, *[start](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude.start "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude.start (Python parameter) — A Float specifying the starting time t0t0.")*, *[a\_0](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude.a_0 "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude.a_0 (Python parameter) — A Float specifying the constant A0A0.")*, *[data](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude.data "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude.data (Python parameter) — A sequence of pairs of Floats specifying AiAi and BiBi pairs.")*, *[timeSpan](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude.timeSpan "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeModel.py#L230-L275)[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude "Permalink to this definition")
    :   This method creates a PeriodicAmplitude object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].PeriodicAmplitude
        session.odbs[name].PeriodicAmplitude
        ```

        Note

        Check [PeriodicAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-periodicamplitudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude.name "Permalink to this definition")
            :   A String specifying the repository key.

            frequency[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude.frequency "Permalink to this definition")
            :   A Float specifying the circular frequency ωω. Possible values are positive numbers.

            start[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude.start "Permalink to this definition")
            :   A Float specifying the starting time t0t0. Possible values are positive numbers.

            a\_0[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude.a_0 "Permalink to this definition")
            :   A Float specifying the constant A0A0.

            data[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude.data "Permalink to this definition")
            :   A sequence of pairs of Floats specifying AiAi and BiBi pairs.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

        Returns:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude-returns "Permalink to this headline")
        :   A PeriodicAmplitude object.

        Return type:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude-return-type "Permalink to this headline")
        :   [`PeriodicAmplitude`](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude (Python method) — This method creates a PeriodicAmplitude object.")

        Raises:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PeriodicAmplitude-raises "Permalink to this headline")
        :   * **InvalidNameError** –
            * **RangeError** –

    PsdDefinition(*[name](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition.name "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition.name (Python parameter) — A String specifying the repository key.")*, *[data](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition.data "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition.data (Python parameter) — A sequence of sequences of Floats specifying the real part of the frequency function, the imaginary part of the frequency function, and the frequency or frequency band number values, depending on the value of unitType.")*, *[unitType](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition.unitType "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition.unitType (Python parameter) — A SymbolicConstant specifying the type of units for specifying the frequency function. FORCE implies power units.")=`abaqusConstants.FORCE`*, *[referenceGravityAcceleration](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition.referenceGravityAcceleration "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition.referenceGravityAcceleration (Python parameter) — A Float specifying the reference gravity acceleration.")=`1`*, *[referenecePower](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition.referenecePower "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition.referenecePower (Python parameter) — A Float specifying the reference power value, in load units squared.")=`0`*, *[user](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition.user "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition.user (Python parameter) — A Boolean specifying whether the frequency function is defined in user subroutine UPSD. If specified, then data is not applicable, and the unitType value must not be DB. The default value is OFF.")=`0`*, *[timeSpan](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition.timeSpan "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*, *[amplitude](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition.amplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition.amplitude (Python parameter) — A String specifying the name of the amplitude that describes the dynamic event used to define the cross-spectral density frequency function.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeModel.py#L277-L347)[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition "Permalink to this definition")
    :   This method creates a PsdDefinition object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].PsdDefinition
        session.odbs[name].PsdDefinition
        ```

        Note

        Check [PsdDefinition on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-psddefinitionpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition.name "Permalink to this definition")
            :   A String specifying the repository key.

            data[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition.data "Permalink to this definition")
            :   A sequence of sequences of Floats specifying the real part of the frequency function,
                the imaginary part of the frequency function, and the frequency or frequency band number
                values, depending on the value of **unitType**.

            unitType=`abaqusConstants.FORCE`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition.unitType "Permalink to this definition")
            :   A SymbolicConstant specifying the type of units for specifying the frequency function.
                FORCE implies power units. BASE implies gravity used to define base motion. DB implies
                decibel units. Possible values are FORCE, BASE, and DB. The default value is FORCE.

            referenceGravityAcceleration=`1`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition.referenceGravityAcceleration "Permalink to this definition")
            :   A Float specifying the reference gravity acceleration. This argument applies when
                **unitType** = BASE. The default value is 1.0.

            referenecePower=`0`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition.referenecePower "Permalink to this definition")
            :   A Float specifying the reference power value, in load units squared. This argument
                applies when **unitType** = DB. The default value is 0.0.

            user=`0`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition.user "Permalink to this definition")
            :   A Boolean specifying whether the frequency function is defined in user subroutine UPSD.
                If specified, then **data** is not applicable, and the **unitType** value must not be DB.
                The default value is OFF.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

            amplitude=`''`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition.amplitude "Permalink to this definition")
            :   A String specifying the name of the amplitude that describes the dynamic event used to
                define the cross-spectral density frequency function. The default value is an empty
                string.

        Returns:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition-returns "Permalink to this headline")
        :   A PsdDefinition object.

        Return type:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition-return-type "Permalink to this headline")
        :   [`PsdDefinition`](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition (Python method) — This method creates a PsdDefinition object.")

        Raises:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.PsdDefinition-raises "Permalink to this headline")
        :   * **InvalidNameError** –
            * **RangeError** –

    SmoothStepAmplitude(*[name](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SmoothStepAmplitude.name "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SmoothStepAmplitude.name (Python parameter) — A String specifying the repository key.")*, *[data](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SmoothStepAmplitude.data "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SmoothStepAmplitude.data (Python parameter) — A sequence of pairs of Floats specifying time/frequency and amplitude pairs.")*, *[timeSpan](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SmoothStepAmplitude.timeSpan "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SmoothStepAmplitude.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeModel.py#L349-L383)[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SmoothStepAmplitude "Permalink to this definition")
    :   This method creates a SmoothStepAmplitude object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].SmoothStepAmplitude
        session.odbs[name].SmoothStepAmplitude
        ```

        Note

        Check [SmoothStepAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-smoothstepamplitudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SmoothStepAmplitude-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SmoothStepAmplitude.name "Permalink to this definition")
            :   A String specifying the repository key.

            data[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SmoothStepAmplitude.data "Permalink to this definition")
            :   A sequence of pairs of Floats specifying time/frequency and amplitude pairs. Possible
                values for time/frequency are positive numbers.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SmoothStepAmplitude.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

        Returns:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SmoothStepAmplitude-returns "Permalink to this headline")
        :   A SmoothStepAmplitude object.

        Return type:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SmoothStepAmplitude-return-type "Permalink to this headline")
        :   [`SmoothStepAmplitude`](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SmoothStepAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SmoothStepAmplitude (Python method) — This method creates a SmoothStepAmplitude object.")

        Raises:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SmoothStepAmplitude-raises "Permalink to this headline")
        :   * **InvalidNameError** –
            * **RangeError** –

    SolutionDependentAmplitude(*[name](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude.name "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude.name (Python parameter) — A String specifying the repository key.")*, *[initial](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude.initial "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude.initial (Python parameter) — A Float specifying the initial amplitude value.")=`1`*, *[minimum](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude.minimum "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude.minimum (Python parameter) — A Float specifying the minimum amplitude value.")=`0`*, *[maximum](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude.maximum "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude.maximum (Python parameter) — A Float specifying the maximum amplitude value.")=`1000`*, *[timeSpan](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude.timeSpan "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeModel.py#L385-L430)[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude "Permalink to this definition")
    :   This method creates a SolutionDependentAmplitude object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].SolutionDependentAmplitude
        session.odbs[name].SolutionDependentAmplitude
        ```

        Note

        Check [SolutionDependentAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-solutiondependentamplitudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude.name "Permalink to this definition")
            :   A String specifying the repository key.

            initial=`1`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude.initial "Permalink to this definition")
            :   A Float specifying the initial amplitude value. Possible values are those between
                **minimum** and **maximum**. The default value is 1.0.

            minimum=`0`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude.minimum "Permalink to this definition")
            :   A Float specifying the minimum amplitude value. Possible values are those smaller than
                **maximum** and **initial**. The default value is 0.1.

            maximum=`1000`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude.maximum "Permalink to this definition")
            :   A Float specifying the maximum amplitude value. Possible values are those larger than
                **minimum** and **initial**. The default value is 1000.0.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

        Returns:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude-returns "Permalink to this headline")
        :   A SolutionDependentAmplitude object.

        Return type:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude-return-type "Permalink to this headline")
        :   [`SolutionDependentAmplitude`](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude (Python method) — This method creates a SolutionDependentAmplitude object.")

        Raises:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SolutionDependentAmplitude-raises "Permalink to this headline")
        :   * **InvalidNameError** –
            * **RangeError** –

    SpectrumAmplitude(*[name](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.name "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.name (Python parameter) — A String specifying the repository key.")*, *[method](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.method "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.method (Python parameter) — A SymbolicConstant specifying the method for specifying the spectrum.")*, *[data](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.data "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.data (Python parameter) — A sequence of sequences of Floats specifying the magnitude, frequency, and damping values.")*, *[specificationUnits](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.specificationUnits "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.specificationUnits (Python parameter) — A SymbolicConstant specifying the units used for specifying the spectrum.")=`abaqusConstants.ACCELERATION`*, *[eventUnits](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.eventUnits "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.eventUnits (Python parameter) — A SymbolicConstant specifying the units used to describe the dynamic event in the amplitude used for the calculation.")=`abaqusConstants.EVENT_ACCELERATION`*, *[solution](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.solution "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.solution (Python parameter) — A SymbolicConstant specifying the solution method for the dynamic equations.")=`abaqusConstants.ABSOLUTE_VALUE`*, *[timeIncrement](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.timeIncrement "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.timeIncrement (Python parameter) — A Float specifying the implicit time increment used to calculate the spectrum.")=`0`*, *[gravity](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.gravity "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.gravity (Python parameter) — A Float specifying the acceleration due to gravity.")=`1`*, *[criticalDamping](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.criticalDamping "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.criticalDamping (Python parameter) — A Boolean specifying whether to calculate the spectrum for only the specified range of critical damping values or a list of values.")=`0`*, *[timeSpan](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.timeSpan "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*, *[amplitude](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.amplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.amplitude (Python parameter) — A String specifying the name of the amplitude that describes the dynamic event used to calculate the spectrum.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeModel.py#L432-L521)[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude "Permalink to this definition")
    :   This method creates a SpectrumAmplitude object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].SpectrumAmplitude
        session.odbs[name].SpectrumAmplitude
        ```

        Note

        Check [SpectrumAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-spectrumamplitudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.name "Permalink to this definition")
            :   A String specifying the repository key.

            method[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.method "Permalink to this definition")
            :   A SymbolicConstant specifying the method for specifying the spectrum. Possible values
                are DEFINE and CALCULATE.

            data[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.data "Permalink to this definition")
            :   A sequence of sequences of Floats specifying the magnitude, frequency, and damping
                values.

            specificationUnits=`abaqusConstants.ACCELERATION`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.specificationUnits "Permalink to this definition")
            :   A SymbolicConstant specifying the units used for specifying the spectrum. Possible
                values are DISPLACEMENT, VELOCITY, ACCELERATION, and GRAVITY. The default value is
                ACCELERATION.

            eventUnits=`abaqusConstants.EVENT_ACCELERATION`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.eventUnits "Permalink to this definition")
            :   A SymbolicConstant specifying the units used to describe the dynamic event in the
                amplitude used for the calculation. Possible values are EVENT\_DISPLACEMENT,
                EVENT\_VELOCITY, EVENT\_ACCELERATION, and EVENT\_GRAVITY. The default value is
                EVENT\_ACCELERATION.

            solution=`abaqusConstants.ABSOLUTE_VALUE`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.solution "Permalink to this definition")
            :   A SymbolicConstant specifying the solution method for the dynamic equations. Possible
                values are ABSOLUTE\_VALUE and RELATIVE\_VALUE. The default value is ABSOLUTE\_VALUE.

            timeIncrement=`0`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.timeIncrement "Permalink to this definition")
            :   A Float specifying the implicit time increment used to calculate the spectrum. This
                argument is required when the **method** = CALCULATE. The default value is 0.0.

            gravity=`1`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.gravity "Permalink to this definition")
            :   A Float specifying the acceleration due to gravity. This argument applies only when
                **specificationUnits** = GRAVITY or\*eventUnits\* = GRAVITY. The default value is 1.0.

            criticalDamping=`0`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.criticalDamping "Permalink to this definition")
            :   A Boolean specifying whether to calculate the spectrum for only the specified range of
                critical damping values or a list of values. If **criticalDamping** = ON, the spectrum is
                calculated only for the specified range of critical damping values. If **criticalDamping**
                = OFF, the spectrum is calculated for a list of damping values. The default value is
                OFF.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

            amplitude=`''`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude.amplitude "Permalink to this definition")
            :   A String specifying the name of the amplitude that describes the dynamic event used to
                calculate the spectrum. The default value is an empty string.

        Returns:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude-returns "Permalink to this headline")
        :   A SpectrumAmplitude object.

        Return type:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude-return-type "Permalink to this headline")
        :   [`SpectrumAmplitude`](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude (Python method) — This method creates a SpectrumAmplitude object.")

        Raises:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.SpectrumAmplitude-raises "Permalink to this headline")
        :   * **InvalidNameError** –
            * **RangeError** –

    TabularAmplitude(*[name](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.TabularAmplitude.name "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.TabularAmplitude.name (Python parameter) — A String specifying the repository key.")*, *[data](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.TabularAmplitude.data "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.TabularAmplitude.data (Python parameter) — A sequence of pairs of Floats specifying time/frequency and amplitude pairs.")*, *[smooth](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.TabularAmplitude.smooth "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.TabularAmplitude.smooth (Python parameter) — The SymbolicConstant SOLVER_DEFAULT or a Float specifying the degree of smoothing. Possible float values are between 0 and 0.5.")=`abaqusConstants.SOLVER_DEFAULT`*, *[timeSpan](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.TabularAmplitude.timeSpan "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.TabularAmplitude.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeModel.py#L523-L566)[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.TabularAmplitude "Permalink to this definition")
    :   This method creates a TabularAmplitude object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].TabularAmplitude
        session.odbs[name].TabularAmplitude
        ```

        Note

        Check [TabularAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tabularamplitudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.TabularAmplitude-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.TabularAmplitude.name "Permalink to this definition")
            :   A String specifying the repository key.

            data[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.TabularAmplitude.data "Permalink to this definition")
            :   A sequence of pairs of Floats specifying time/frequency and amplitude pairs. Possible
                values for time/frequency are positive numbers.

            smooth=`abaqusConstants.SOLVER_DEFAULT`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.TabularAmplitude.smooth "Permalink to this definition")
            :   The SymbolicConstant SOLVER\_DEFAULT or a Float specifying the degree of smoothing.
                Possible float values are between 0 and 0.5. If **smooth** = SOLVER\_DEFAULT, the default
                degree of smoothing will be determined by the solver. The default value is
                SOLVER\_DEFAULT.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.TabularAmplitude.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

        Returns:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.TabularAmplitude-returns "Permalink to this headline")
        :   A TabularAmplitude object.

        Return type:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.TabularAmplitude-return-type "Permalink to this headline")
        :   [`TabularAmplitude`](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.TabularAmplitude "abaqus.Amplitude.AmplitudeModel.AmplitudeModel.TabularAmplitude (Python method) — This method creates a TabularAmplitude object.")

        Raises:[¶](#abaqus.Amplitude.AmplitudeModel.AmplitudeModel.TabularAmplitude-raises "Permalink to this headline")
        :   * **InvalidNameError** –
            * **RangeError** –

### In Odb[¶](#in-odb "Permalink to this heading")

*class* AmplitudeOdb(*[name](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.__init__.name (Python parameter)")*, *[analysisTitle](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.__init__.analysisTitle (Python parameter)")=`''`*, *[description](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.__init__.description (Python parameter)")=`''`*, *[path](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.__init__.path (Python parameter)")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeOdb.py#L33-L564)[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb "Permalink to this definition")
:   Bases: [`OdbBase`](../../odb.html#abaqus.Odb.OdbBase.OdbBase "abaqus.Odb.OdbBase.OdbBase (Python class) — Bases: object")

    The Odb object is the in-memory representation of an output database (ODB) file.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name]
    ```

    Note

    Check [AmplitudeOdb on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbpyc.htm?contextscope=all).

    Public Data Attributes:

    Inherited from [`OdbBase`](../../odb.html#abaqus.Odb.OdbBase.OdbBase "abaqus.Odb.OdbBase.OdbBase (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | [`isReadOnly`](../../odb.html#abaqus.Odb.OdbBase.OdbBase.isReadOnly "abaqus.Odb.OdbBase.OdbBase.isReadOnly (Python attribute) — A Boolean specifying whether the output database was opened with read-only access.") | A Boolean specifying whether the output database was opened with read-only access. |
    | [`amplitudes`](../../odb.html#abaqus.Odb.OdbBase.OdbBase.amplitudes "abaqus.Odb.OdbBase.OdbBase.amplitudes (Python attribute) — A repository of Amplitude objects.") | A repository of Amplitude objects. |
    | [`filters`](../../odb.html#abaqus.Odb.OdbBase.OdbBase.filters "abaqus.Odb.OdbBase.OdbBase.filters (Python attribute) — A repository of Filter objects.") | A repository of Filter objects. |
    | [`rootAssembly`](../../odb.html#abaqus.Odb.OdbBase.OdbBase.rootAssembly "abaqus.Odb.OdbBase.OdbBase.rootAssembly (Python attribute) — An OdbAssembly object.") | An OdbAssembly object. |
    | [`jobData`](../../odb.html#abaqus.Odb.OdbBase.OdbBase.jobData "abaqus.Odb.OdbBase.OdbBase.jobData (Python attribute) — A JobData object.") | A JobData object. |
    | [`parts`](../../odb.html#abaqus.Odb.OdbBase.OdbBase.parts "abaqus.Odb.OdbBase.OdbBase.parts (Python attribute) — A repository of OdbPart objects.") | A repository of OdbPart objects. |
    | [`materials`](../../odb.html#abaqus.Odb.OdbBase.OdbBase.materials "abaqus.Odb.OdbBase.OdbBase.materials (Python attribute) — A repository of Material objects.") | A repository of Material objects. |
    | [`steps`](../../odb.html#abaqus.Odb.OdbBase.OdbBase.steps "abaqus.Odb.OdbBase.OdbBase.steps (Python attribute) — A repository of OdbStep objects.") | A repository of OdbStep objects. |
    | [`sections`](../../odb.html#abaqus.Odb.OdbBase.OdbBase.sections "abaqus.Odb.OdbBase.OdbBase.sections (Python attribute) — A repository of Section objects.") | A repository of Section objects. |
    | [`sectionCategories`](../../odb.html#abaqus.Odb.OdbBase.OdbBase.sectionCategories "abaqus.Odb.OdbBase.OdbBase.sectionCategories (Python attribute) — A repository of SectionCategory objects.") | A repository of SectionCategory objects. |
    | [`sectorDefinition`](../../odb.html#abaqus.Odb.OdbBase.OdbBase.sectorDefinition "abaqus.Odb.OdbBase.OdbBase.sectorDefinition (Python attribute) — A SectorDefinition object.") | A SectorDefinition object. |
    | [`userData`](../../odb.html#abaqus.Odb.OdbBase.OdbBase.userData "abaqus.Odb.OdbBase.OdbBase.userData (Python attribute) — A UserData object.") | A UserData object. |
    | [`customData`](../../odb.html#abaqus.Odb.OdbBase.OdbBase.customData "abaqus.Odb.OdbBase.OdbBase.customData (Python attribute) — A RepositorySupport object.") | A RepositorySupport object. |
    | [`profiles`](../../odb.html#abaqus.Odb.OdbBase.OdbBase.profiles "abaqus.Odb.OdbBase.OdbBase.profiles (Python attribute) — A repository of Profile objects.") | A repository of Profile objects. |

    Public Methods:

    |  |  |
    | --- | --- |
    | [`ActuatorAmplitude`](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ActuatorAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ActuatorAmplitude (Python method) — This method creates a ActuatorAmplitude object.")(name[, timeSpan]) | This method creates a ActuatorAmplitude object. |
    | [`DecayAmplitude`](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude (Python method) — This method creates a DecayAmplitude object.")(name, initial, maximum, ...) | This method creates a DecayAmplitude object. |
    | [`EquallySpacedAmplitude`](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude (Python method) — This method creates an EquallySpacedAmplitude object.")(name, fixedInterval, data) | This method creates an EquallySpacedAmplitude object. |
    | [`ModulatedAmplitude`](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude (Python method) — This method creates a ModulatedAmplitude object.")(name, initial, magnitude, ...) | This method creates a ModulatedAmplitude object. |
    | [`PeriodicAmplitude`](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude (Python method) — This method creates a PeriodicAmplitude object.")(name, frequency, start, ...) | This method creates a PeriodicAmplitude object. |
    | [`PsdDefinition`](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition (Python method) — This method creates a PsdDefinition object.")(name, data[, unitType, ...]) | This method creates a PsdDefinition object. |
    | [`SmoothStepAmplitude`](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SmoothStepAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SmoothStepAmplitude (Python method) — This method creates a SmoothStepAmplitude object.")(name, data[, timeSpan]) | This method creates a SmoothStepAmplitude object. |
    | [`SolutionDependentAmplitude`](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude (Python method) — This method creates a SolutionDependentAmplitude object.")(name[, initial, ...]) | This method creates a SolutionDependentAmplitude object. |
    | [`SpectrumAmplitude`](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude (Python method) — This method creates a SpectrumAmplitude object.")(name, method, data[, ...]) | This method creates a SpectrumAmplitude object. |
    | [`TabularAmplitude`](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.TabularAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.TabularAmplitude (Python method) — This method creates a TabularAmplitude object.")(name, data[, smooth, timeSpan]) | This method creates a TabularAmplitude object. |

    Inherited from [`OdbBase`](../../odb.html#abaqus.Odb.OdbBase.OdbBase "abaqus.Odb.OdbBase.OdbBase (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | `__init__`(name[, analysisTitle, description, ...]) | This method creates a new Odb object. |
    | [`close`](../../odb.html#abaqus.Odb.OdbBase.OdbBase.close "abaqus.Odb.OdbBase.OdbBase.close (Python method) — This method closes an output database.")() | This method closes an output database. |
    | [`getFrame`](../../odb.html#abaqus.Odb.OdbBase.OdbBase.getFrame "abaqus.Odb.OdbBase.OdbBase.getFrame (Python method) — This method returns the frame at the specified time, frequency, or mode. It will not interpolate values between frames. The method is not applicable to an Odb object containing steps with different domains or to an Odb object containing a step with load case specific data.")(frameValue[, match]) | This method returns the frame at the specified time, frequency, or mode. |
    | [`save`](../../odb.html#abaqus.Odb.OdbBase.OdbBase.save "abaqus.Odb.OdbBase.OdbBase.save (Python method) — This method saves output to an output database (.odb ) file.")() | This method saves output to an output database (.odb ) file. |
    | [`update`](../../odb.html#abaqus.Odb.OdbBase.OdbBase.update "abaqus.Odb.OdbBase.OdbBase.update (Python method) — This method is used to update an Odb object in memory while an Abaqus analysis writes data to the associated output database. update checks if additional steps have been written to the output database since it was opened or last updated. If additional steps have been written to the output database, update adds them to the Odb object.")() | This method is used to update an Odb object in memory while an Abaqus analysis writes data to the associated output database. |

    ---

    Member Details:

    ActuatorAmplitude(*[name](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ActuatorAmplitude.name "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ActuatorAmplitude.name (Python parameter) — A String specifying the repository key.")*, *[timeSpan](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ActuatorAmplitude.timeSpan "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ActuatorAmplitude.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeOdb.py#L44-L73)[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ActuatorAmplitude "Permalink to this definition")
    :   This method creates a ActuatorAmplitude object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ActuatorAmplitude
        session.odbs[name].ActuatorAmplitude
        ```

        Note

        Check [ActuatorAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-actuatoramplitudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ActuatorAmplitude-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ActuatorAmplitude.name "Permalink to this definition")
            :   A String specifying the repository key.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ActuatorAmplitude.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

        Returns:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ActuatorAmplitude-returns "Permalink to this headline")
        :   An ActuatorAmplitude object.

        Return type:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ActuatorAmplitude-return-type "Permalink to this headline")
        :   [`ActuatorAmplitude`](#abaqus.Amplitude.AmplitudeOdb.ActuatorAmplitude "abaqus.Amplitude.AmplitudeOdb.ActuatorAmplitude (Python class) — Bases: Amplitude")

        Raises:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ActuatorAmplitude-raises "Permalink to this headline")
        :   * **InvalidNameError** –
            * **RangeError** –

    DecayAmplitude(*[name](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude.name "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude.name (Python parameter) — A String specifying the repository key.")*, *[initial](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude.initial "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude.initial (Python parameter) — A Float specifying the constant A0A0.")*, *[maximum](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude.maximum "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude.maximum (Python parameter) — A Float specifying the coefficient AA.")*, *[start](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude.start "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude.start (Python parameter) — A Float specifying the starting time t0t0.")*, *[decayTime](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude.decayTime "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude.decayTime (Python parameter) — A Float specifying the decay time tdtd.")*, *[timeSpan](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude.timeSpan "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeOdb.py#L75-L120)[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude "Permalink to this definition")
    :   This method creates a DecayAmplitude object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].DecayAmplitude
        session.odbs[name].DecayAmplitude
        ```

        Note

        Check [DecayAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-decayamplitudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude.name "Permalink to this definition")
            :   A String specifying the repository key.

            initial[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude.initial "Permalink to this definition")
            :   A Float specifying the constant A0A0.

            maximum[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude.maximum "Permalink to this definition")
            :   A Float specifying the coefficient AA.

            start[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude.start "Permalink to this definition")
            :   A Float specifying the starting time t0t0. Possible values are non-negative numbers.

            decayTime[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude.decayTime "Permalink to this definition")
            :   A Float specifying the decay time tdtd. Possible values are non-negative numbers.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

        Returns:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude-returns "Permalink to this headline")
        :   A DecayAmplitude object.

        Return type:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude-return-type "Permalink to this headline")
        :   [`DecayAmplitude`](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude (Python method) — This method creates a DecayAmplitude object.")

        Raises:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude-raises "Permalink to this headline")
        :   * **InvalidNameError** –
            * **RangeError** –

    EquallySpacedAmplitude(*[name](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude.name "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude.name (Python parameter) — A String specifying the repository key.")*, *[fixedInterval](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude.fixedInterval "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude.fixedInterval (Python parameter) — A Float specifying the fixed time interval at which the amplitude data are given. Possible values are positive numbers.")*, *[data](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude.data "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude.data (Python parameter) — A sequence of Floats specifying the amplitude values.")*, *[begin](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude.begin "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude.begin (Python parameter) — A Float specifying the time at which the first amplitude data are given.")=`0`*, *[smooth](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude.smooth "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude.smooth (Python parameter) — The SymbolicConstant SOLVER_DEFAULT or a Float specifying the degree of smoothing. Possible float values are 0 ≤ smoothing ≤ 0.5.")=`abaqusConstants.SOLVER_DEFAULT`*, *[timeSpan](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude.timeSpan "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeOdb.py#L122-L172)[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude "Permalink to this definition")
    :   This method creates an EquallySpacedAmplitude object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].EquallySpacedAmplitude
        session.odbs[name].EquallySpacedAmplitude
        ```

        Note

        Check [EquallySpacedAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-equallyspacedamplitudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude.name "Permalink to this definition")
            :   A String specifying the repository key.

            fixedInterval[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude.fixedInterval "Permalink to this definition")
            :   A Float specifying the fixed time interval at which the amplitude data are given.
                Possible values are positive numbers.

            data[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude.data "Permalink to this definition")
            :   A sequence of Floats specifying the amplitude values.

            begin=`0`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude.begin "Permalink to this definition")
            :   A Float specifying the time at which the first amplitude data are given. Possible values
                are non-negative numbers. The default value is 0.0.

            smooth=`abaqusConstants.SOLVER_DEFAULT`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude.smooth "Permalink to this definition")
            :   The SymbolicConstant SOLVER\_DEFAULT or a Float specifying the degree of smoothing.
                Possible float values are 0 ≤ **smoothing** ≤ 0.5. If **smooth** = SOLVER\_DEFAULT, the
                default degree of smoothing will be determined by the solver. The default value is
                SOLVER\_DEFAULT.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

        Returns:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude-returns "Permalink to this headline")
        :   An EquallySpacedAmplitude object.

        Return type:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude-return-type "Permalink to this headline")
        :   [`EquallySpacedAmplitude`](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude (Python method) — This method creates an EquallySpacedAmplitude object.")

        Raises:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude-raises "Permalink to this headline")
        :   * **InvalidNameError** –
            * **RangeError** –

    ModulatedAmplitude(*[name](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude.name "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude.name (Python parameter) — A String specifying the repository key.")*, *[initial](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude.initial "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude.initial (Python parameter) — A Float specifying the constant A0A0.")*, *[magnitude](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude.magnitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude.magnitude (Python parameter) — A Float specifying the coefficient AA.")*, *[start](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude.start "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude.start (Python parameter) — A Float specifying the starting time t0t0.")*, *[frequency1](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude.frequency1 "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude.frequency1 (Python parameter) — A Float specifying the circular frequency 1 (ω1ω1).")*, *[frequency2](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude.frequency2 "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude.frequency2 (Python parameter) — A Float specifying the circular frequency 2 (ω2ω2).")*, *[timeSpan](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude.timeSpan "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeOdb.py#L174-L226)[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude "Permalink to this definition")
    :   This method creates a ModulatedAmplitude object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ModulatedAmplitude
        session.odbs[name].ModulatedAmplitude
        ```

        Note

        Check [ModulatedAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modulatedamplitudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude.name "Permalink to this definition")
            :   A String specifying the repository key.

            initial[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude.initial "Permalink to this definition")
            :   A Float specifying the constant A0A0.

            magnitude[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude.magnitude "Permalink to this definition")
            :   A Float specifying the coefficient AA.

            start[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude.start "Permalink to this definition")
            :   A Float specifying the starting time t0t0. Possible values are non-negative numbers.

            frequency1[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude.frequency1 "Permalink to this definition")
            :   A Float specifying the circular frequency 1 (ω1ω1). Possible values are positive
                numbers.

            frequency2[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude.frequency2 "Permalink to this definition")
            :   A Float specifying the circular frequency 2 (ω2ω2). Possible values are positive
                numbers.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

        Returns:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude-returns "Permalink to this headline")
        :   A ModulatedAmplitude object.

        Return type:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude-return-type "Permalink to this headline")
        :   [`ModulatedAmplitude`](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude (Python method) — This method creates a ModulatedAmplitude object.")

        Raises:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude-raises "Permalink to this headline")
        :   * **InvalidNameError** –
            * **RangeError** –

    PeriodicAmplitude(*[name](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude.name "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude.name (Python parameter) — A String specifying the repository key.")*, *[frequency](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude.frequency "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude.frequency (Python parameter) — A Float specifying the circular frequency ωω.")*, *[start](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude.start "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude.start (Python parameter) — A Float specifying the starting time t0t0.")*, *[a\_0](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude.a_0 "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude.a_0 (Python parameter) — A Float specifying the constant A0A0.")*, *[data](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude.data "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude.data (Python parameter) — A sequence of pairs of Floats specifying AiAi and BiBi pairs.")*, *[timeSpan](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude.timeSpan "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeOdb.py#L228-L273)[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude "Permalink to this definition")
    :   This method creates a PeriodicAmplitude object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].PeriodicAmplitude
        session.odbs[name].PeriodicAmplitude
        ```

        Note

        Check [PeriodicAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-periodicamplitudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude.name "Permalink to this definition")
            :   A String specifying the repository key.

            frequency[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude.frequency "Permalink to this definition")
            :   A Float specifying the circular frequency ωω. Possible values are positive numbers.

            start[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude.start "Permalink to this definition")
            :   A Float specifying the starting time t0t0. Possible values are positive numbers.

            a\_0[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude.a_0 "Permalink to this definition")
            :   A Float specifying the constant A0A0.

            data[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude.data "Permalink to this definition")
            :   A sequence of pairs of Floats specifying AiAi and BiBi pairs.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

        Returns:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude-returns "Permalink to this headline")
        :   A PeriodicAmplitude object.

        Return type:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude-return-type "Permalink to this headline")
        :   [`PeriodicAmplitude`](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude (Python method) — This method creates a PeriodicAmplitude object.")

        Raises:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude-raises "Permalink to this headline")
        :   * **InvalidNameError** –
            * **RangeError** –

    PsdDefinition(*[name](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition.name "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition.name (Python parameter) — A String specifying the repository key.")*, *[data](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition.data "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition.data (Python parameter) — A sequence of sequences of Floats specifying the real part of the frequency function, the imaginary part of the frequency function, and the frequency or frequency band number values, depending on the value of unitType.")*, *[unitType](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition.unitType "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition.unitType (Python parameter) — A SymbolicConstant specifying the type of units for specifying the frequency function. FORCE implies power units.")=`abaqusConstants.FORCE`*, *[referenceGravityAcceleration](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition.referenceGravityAcceleration "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition.referenceGravityAcceleration (Python parameter) — A Float specifying the reference gravity acceleration.")=`1`*, *[referenecePower](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition.referenecePower "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition.referenecePower (Python parameter) — A Float specifying the reference power value, in load units squared.")=`0`*, *[user](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition.user "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition.user (Python parameter) — A Boolean specifying whether the frequency function is defined in user subroutine UPSD. If specified, then data is not applicable, and the unitType value must not be DB. The default value is OFF.")=`0`*, *[timeSpan](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition.timeSpan "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*, *[amplitude](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition.amplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition.amplitude (Python parameter) — A String specifying the name of the amplitude that describes the dynamic event used to define the cross-spectral density frequency function.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeOdb.py#L275-L345)[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition "Permalink to this definition")
    :   This method creates a PsdDefinition object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].PsdDefinition
        session.odbs[name].PsdDefinition
        ```

        Note

        Check [PsdDefinition on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-psddefinitionpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition.name "Permalink to this definition")
            :   A String specifying the repository key.

            data[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition.data "Permalink to this definition")
            :   A sequence of sequences of Floats specifying the real part of the frequency function,
                the imaginary part of the frequency function, and the frequency or frequency band number
                values, depending on the value of **unitType**.

            unitType=`abaqusConstants.FORCE`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition.unitType "Permalink to this definition")
            :   A SymbolicConstant specifying the type of units for specifying the frequency function.
                FORCE implies power units. BASE implies gravity used to define base motion. DB implies
                decibel units. Possible values are FORCE, BASE, and DB. The default value is FORCE.

            referenceGravityAcceleration=`1`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition.referenceGravityAcceleration "Permalink to this definition")
            :   A Float specifying the reference gravity acceleration. This argument applies when
                **unitType** = BASE. The default value is 1.0.

            referenecePower=`0`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition.referenecePower "Permalink to this definition")
            :   A Float specifying the reference power value, in load units squared. This argument
                applies when **unitType** = DB. The default value is 0.0.

            user=`0`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition.user "Permalink to this definition")
            :   A Boolean specifying whether the frequency function is defined in user subroutine UPSD.
                If specified, then **data** is not applicable, and the **unitType** value must not be DB.
                The default value is OFF.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

            amplitude=`''`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition.amplitude "Permalink to this definition")
            :   A String specifying the name of the amplitude that describes the dynamic event used to
                define the cross-spectral density frequency function. The default value is an empty
                string.

        Returns:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition-returns "Permalink to this headline")
        :   A PsdDefinition object.

        Return type:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition-return-type "Permalink to this headline")
        :   [`PsdDefinition`](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition (Python method) — This method creates a PsdDefinition object.")

        Raises:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition-raises "Permalink to this headline")
        :   * **InvalidNameError** –
            * **RangeError** –

    SmoothStepAmplitude(*[name](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SmoothStepAmplitude.name "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SmoothStepAmplitude.name (Python parameter) — A String specifying the repository key.")*, *[data](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SmoothStepAmplitude.data "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SmoothStepAmplitude.data (Python parameter) — A sequence of pairs of Floats specifying time/frequency and amplitude pairs.")*, *[timeSpan](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SmoothStepAmplitude.timeSpan "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SmoothStepAmplitude.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeOdb.py#L347-L381)[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SmoothStepAmplitude "Permalink to this definition")
    :   This method creates a SmoothStepAmplitude object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].SmoothStepAmplitude
        session.odbs[name].SmoothStepAmplitude
        ```

        Note

        Check [SmoothStepAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-smoothstepamplitudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SmoothStepAmplitude-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SmoothStepAmplitude.name "Permalink to this definition")
            :   A String specifying the repository key.

            data[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SmoothStepAmplitude.data "Permalink to this definition")
            :   A sequence of pairs of Floats specifying time/frequency and amplitude pairs. Possible
                values for time/frequency are positive numbers.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SmoothStepAmplitude.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

        Returns:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SmoothStepAmplitude-returns "Permalink to this headline")
        :   A SmoothStepAmplitude object.

        Return type:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SmoothStepAmplitude-return-type "Permalink to this headline")
        :   [`SmoothStepAmplitude`](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SmoothStepAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SmoothStepAmplitude (Python method) — This method creates a SmoothStepAmplitude object.")

        Raises:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SmoothStepAmplitude-raises "Permalink to this headline")
        :   * **InvalidNameError** –
            * **RangeError** –

    SolutionDependentAmplitude(*[name](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude.name "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude.name (Python parameter) — A String specifying the repository key.")*, *[initial](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude.initial "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude.initial (Python parameter) — A Float specifying the initial amplitude value.")=`1`*, *[minimum](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude.minimum "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude.minimum (Python parameter) — A Float specifying the minimum amplitude value.")=`0`*, *[maximum](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude.maximum "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude.maximum (Python parameter) — A Float specifying the maximum amplitude value.")=`1000`*, *[timeSpan](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude.timeSpan "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeOdb.py#L383-L428)[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude "Permalink to this definition")
    :   This method creates a SolutionDependentAmplitude object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].SolutionDependentAmplitude
        session.odbs[name].SolutionDependentAmplitude
        ```

        Note

        Check [SolutionDependentAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-solutiondependentamplitudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude.name "Permalink to this definition")
            :   A String specifying the repository key.

            initial=`1`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude.initial "Permalink to this definition")
            :   A Float specifying the initial amplitude value. Possible values are those between
                **minimum** and **maximum**. The default value is 1.0.

            minimum=`0`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude.minimum "Permalink to this definition")
            :   A Float specifying the minimum amplitude value. Possible values are those smaller than
                **maximum** and **initial**. The default value is 0.1.

            maximum=`1000`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude.maximum "Permalink to this definition")
            :   A Float specifying the maximum amplitude value. Possible values are those larger than
                **minimum** and **initial**. The default value is 1000.0.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

        Returns:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude-returns "Permalink to this headline")
        :   A SolutionDependentAmplitude object.

        Return type:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude-return-type "Permalink to this headline")
        :   [`SolutionDependentAmplitude`](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude (Python method) — This method creates a SolutionDependentAmplitude object.")

        Raises:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude-raises "Permalink to this headline")
        :   * **InvalidNameError** –
            * **RangeError** –

    SpectrumAmplitude(*[name](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.name "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.name (Python parameter) — A String specifying the repository key.")*, *[method](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.method "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.method (Python parameter) — A SymbolicConstant specifying the method for specifying the spectrum.")*, *[data](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.data "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.data (Python parameter) — A sequence of sequences of Floats specifying the magnitude, frequency, and damping values.")*, *[specificationUnits](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.specificationUnits "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.specificationUnits (Python parameter) — A SymbolicConstant specifying the units used for specifying the spectrum.")=`abaqusConstants.ACCELERATION`*, *[eventUnits](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.eventUnits "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.eventUnits (Python parameter) — A SymbolicConstant specifying the units used to describe the dynamic event in the amplitude used for the calculation.")=`abaqusConstants.EVENT_ACCELERATION`*, *[solution](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.solution "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.solution (Python parameter) — A SymbolicConstant specifying the solution method for the dynamic equations.")=`abaqusConstants.ABSOLUTE_VALUE`*, *[timeIncrement](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.timeIncrement "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.timeIncrement (Python parameter) — A Float specifying the implicit time increment used to calculate the spectrum.")=`0`*, *[gravity](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.gravity "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.gravity (Python parameter) — A Float specifying the acceleration due to gravity.")=`1`*, *[criticalDamping](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.criticalDamping "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.criticalDamping (Python parameter) — A Boolean specifying whether to calculate the spectrum for only the specified range of critical damping values or a list of values.")=`0`*, *[timeSpan](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.timeSpan "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*, *[amplitude](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.amplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.amplitude (Python parameter) — A String specifying the name of the amplitude that describes the dynamic event used to calculate the spectrum.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeOdb.py#L430-L519)[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude "Permalink to this definition")
    :   This method creates a SpectrumAmplitude object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].SpectrumAmplitude
        session.odbs[name].SpectrumAmplitude
        ```

        Note

        Check [SpectrumAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-spectrumamplitudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.name "Permalink to this definition")
            :   A String specifying the repository key.

            method[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.method "Permalink to this definition")
            :   A SymbolicConstant specifying the method for specifying the spectrum. Possible values
                are DEFINE and CALCULATE.

            data[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.data "Permalink to this definition")
            :   A sequence of sequences of Floats specifying the magnitude, frequency, and damping
                values.

            specificationUnits=`abaqusConstants.ACCELERATION`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.specificationUnits "Permalink to this definition")
            :   A SymbolicConstant specifying the units used for specifying the spectrum. Possible
                values are DISPLACEMENT, VELOCITY, ACCELERATION, and GRAVITY. The default value is
                ACCELERATION.

            eventUnits=`abaqusConstants.EVENT_ACCELERATION`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.eventUnits "Permalink to this definition")
            :   A SymbolicConstant specifying the units used to describe the dynamic event in the
                amplitude used for the calculation. Possible values are EVENT\_DISPLACEMENT,
                EVENT\_VELOCITY, EVENT\_ACCELERATION, and EVENT\_GRAVITY. The default value is
                EVENT\_ACCELERATION.

            solution=`abaqusConstants.ABSOLUTE_VALUE`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.solution "Permalink to this definition")
            :   A SymbolicConstant specifying the solution method for the dynamic equations. Possible
                values are ABSOLUTE\_VALUE and RELATIVE\_VALUE. The default value is ABSOLUTE\_VALUE.

            timeIncrement=`0`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.timeIncrement "Permalink to this definition")
            :   A Float specifying the implicit time increment used to calculate the spectrum. This
                argument is required when the **method** = CALCULATE. The default value is 0.0.

            gravity=`1`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.gravity "Permalink to this definition")
            :   A Float specifying the acceleration due to gravity. This argument applies only when
                **specificationUnits** = GRAVITY or\*eventUnits\* = GRAVITY. The default value is 1.0.

            criticalDamping=`0`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.criticalDamping "Permalink to this definition")
            :   A Boolean specifying whether to calculate the spectrum for only the specified range of
                critical damping values or a list of values. If **criticalDamping** = ON, the spectrum is
                calculated only for the specified range of critical damping values. If **criticalDamping**
                = OFF, the spectrum is calculated for a list of damping values. The default value is
                OFF.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

            amplitude=`''`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude.amplitude "Permalink to this definition")
            :   A String specifying the name of the amplitude that describes the dynamic event used to
                calculate the spectrum. The default value is an empty string.

        Returns:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude-returns "Permalink to this headline")
        :   A SpectrumAmplitude object.

        Return type:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude-return-type "Permalink to this headline")
        :   [`SpectrumAmplitude`](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude (Python method) — This method creates a SpectrumAmplitude object.")

        Raises:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude-raises "Permalink to this headline")
        :   * **InvalidNameError** –
            * **RangeError** –

    TabularAmplitude(*[name](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.TabularAmplitude.name "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.TabularAmplitude.name (Python parameter) — A String specifying the repository key.")*, *[data](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.TabularAmplitude.data "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.TabularAmplitude.data (Python parameter) — A sequence of pairs of Floats specifying time/frequency and amplitude pairs.")*, *[smooth](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.TabularAmplitude.smooth "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.TabularAmplitude.smooth (Python parameter) — The SymbolicConstant SOLVER_DEFAULT or a Float specifying the degree of smoothing. Possible float values are between 0 and 0.5.")=`abaqusConstants.SOLVER_DEFAULT`*, *[timeSpan](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.TabularAmplitude.timeSpan "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.TabularAmplitude.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeOdb.py#L521-L564)[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.TabularAmplitude "Permalink to this definition")
    :   This method creates a TabularAmplitude object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].TabularAmplitude
        session.odbs[name].TabularAmplitude
        ```

        Note

        Check [TabularAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tabularamplitudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.TabularAmplitude-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.TabularAmplitude.name "Permalink to this definition")
            :   A String specifying the repository key.

            data[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.TabularAmplitude.data "Permalink to this definition")
            :   A sequence of pairs of Floats specifying time/frequency and amplitude pairs. Possible
                values for time/frequency are positive numbers.

            smooth=`abaqusConstants.SOLVER_DEFAULT`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.TabularAmplitude.smooth "Permalink to this definition")
            :   The SymbolicConstant SOLVER\_DEFAULT or a Float specifying the degree of smoothing.
                Possible float values are between 0 and 0.5. If **smooth** = SOLVER\_DEFAULT, the default
                degree of smoothing will be determined by the solver. The default value is
                SOLVER\_DEFAULT.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.TabularAmplitude.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

        Returns:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.TabularAmplitude-returns "Permalink to this headline")
        :   A TabularAmplitude object.

        Return type:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.TabularAmplitude-return-type "Permalink to this headline")
        :   [`TabularAmplitude`](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.TabularAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.TabularAmplitude (Python method) — This method creates a TabularAmplitude object.")

        Raises:[¶](#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.TabularAmplitude-raises "Permalink to this headline")
        :   * **InvalidNameError** –
            * **RangeError** –

## Other Classes[¶](#other-classes "Permalink to this heading")

*class* ActuatorAmplitude(*[name](#abaqus.Amplitude.AmplitudeOdb.ActuatorAmplitude "abaqus.Amplitude.AmplitudeOdb.ActuatorAmplitude.__init__.name (Python parameter)")*, *[timeSpan](#abaqus.Amplitude.AmplitudeOdb.ActuatorAmplitude "abaqus.Amplitude.AmplitudeOdb.ActuatorAmplitude.__init__.timeSpan (Python parameter)")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeOdb.py#L12-L81)[¶](#abaqus.Amplitude.AmplitudeOdb.ActuatorAmplitude "Permalink to this definition")
:   Bases: [`Amplitude`](#abaqus.Amplitude.TabularAmplitude.Amplitude "abaqus.Amplitude.Amplitude.Amplitude (Python class)")

    The ActuatorAmplitude object defines an actuator amplitude curve. The ActuatorAmplitude object is derived
    from the Amplitude object.

    Note

    This object can be accessed by:

    ```python
    import amplitude
    mdb.models[name].amplitudes[name]
    import odbAmplitude
    session.odbs[name].amplitudes[name]
    ```

    The corresponding analysis keywords are:

    * AMPLITUDE

    Note

    Check [ActuatorAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-actuatoramplitudepyc.htm?contextscope=all).

    Member Details:

    setValues(*[timeSpan](#abaqus.Amplitude.AmplitudeOdb.ActuatorAmplitude.setValues.timeSpan "abaqus.Amplitude.AmplitudeOdb.ActuatorAmplitude.setValues.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeOdb.py#L67-L81)[¶](#abaqus.Amplitude.AmplitudeOdb.ActuatorAmplitude.setValues "Permalink to this definition")
    :   This method modifies the ActuatorAmplitude object.

        Note

        Check [ActuatorAmplitude.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-actuatoramplitudepyc.htm?contextscope=all#simaker-actuatoramplitudesetvaluespyc).

        Parameters:[¶](#abaqus.Amplitude.AmplitudeOdb.ActuatorAmplitude.setValues-parameters "Permalink to this headline")
        :   timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.AmplitudeOdb.ActuatorAmplitude.setValues.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

        Raises:[¶](#abaqus.Amplitude.AmplitudeOdb.ActuatorAmplitude.setValues-raises "Permalink to this headline")
        :   **RangeError** –

    timeSpan : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'STEP'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/AmplitudeOdb.py#L33-L35)[¶](#abaqus.Amplitude.AmplitudeOdb.ActuatorAmplitude.timeSpan "Permalink to this definition")
    :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
        and TOTAL. The default value is STEP.

*class* Amplitude[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/TabularAmplitude.py#L8-L28)[¶](#abaqus.Amplitude.TabularAmplitude.Amplitude "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The Amplitude object is the abstract base type for other Amplitude objects. The Amplitude object has no
    explicit constructor. The methods and members of the Amplitude object are common to all objects derived from
    the Amplitude.

    Note

    This object can be accessed by:

    ```python
    import amplitude
    mdb.models[name].amplitudes[name]
    import odbAmplitude
    session.odbs[name].amplitudes[name]
    ```

    Note

    Check [Amplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-amplitudepyc.htm?contextscope=all).

    Member Details:

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/TabularAmplitude.py#L23-L24)[¶](#abaqus.Amplitude.TabularAmplitude.Amplitude.name "Permalink to this definition")
    :   A String specifying the repository key.

    timeSpan : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'STEP'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/TabularAmplitude.py#L8-L28)[¶](#abaqus.Amplitude.TabularAmplitude.Amplitude.timeSpan "Permalink to this definition")
    :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
        and TOTAL. The default value is STEP.

*class* DecayAmplitude(*[name](#abaqus.Amplitude.DecayAmplitude.DecayAmplitude "abaqus.Amplitude.DecayAmplitude.DecayAmplitude.__init__.name (Python parameter)")*, *[initial](#abaqus.Amplitude.DecayAmplitude.DecayAmplitude "abaqus.Amplitude.DecayAmplitude.DecayAmplitude.__init__.initial (Python parameter)")*, *[maximum](#abaqus.Amplitude.DecayAmplitude.DecayAmplitude "abaqus.Amplitude.DecayAmplitude.DecayAmplitude.__init__.maximum (Python parameter)")*, *[start](#abaqus.Amplitude.DecayAmplitude.DecayAmplitude "abaqus.Amplitude.DecayAmplitude.DecayAmplitude.__init__.start (Python parameter)")*, *[decayTime](#abaqus.Amplitude.DecayAmplitude.DecayAmplitude "abaqus.Amplitude.DecayAmplitude.DecayAmplitude.__init__.decayTime (Python parameter)")*, *[timeSpan](#abaqus.Amplitude.DecayAmplitude.DecayAmplitude "abaqus.Amplitude.DecayAmplitude.DecayAmplitude.__init__.timeSpan (Python parameter)")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/DecayAmplitude.py#L12-L109)[¶](#abaqus.Amplitude.DecayAmplitude.DecayAmplitude "Permalink to this definition")
:   Bases: [`Amplitude`](#abaqus.Amplitude.TabularAmplitude.Amplitude "abaqus.Amplitude.Amplitude.Amplitude (Python class)")

    The DecayAmplitude object defines an amplitude curve using an exponential decay. The DecayAmplitude
    object is derived from the Amplitude object.

    Note

    This object can be accessed by:

    ```python
    import amplitude
    mdb.models[name].amplitudes[name]
    import odbAmplitude
    session.odbs[name].amplitudes[name]
    ```

    The corresponding analysis keywords are:

    * AMPLITUDE

    Note

    Check [DecayAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-decayamplitudepyc.htm?contextscope=all).

    Member Details:

    decayTime : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/DecayAmplitude.py)[¶](#abaqus.Amplitude.DecayAmplitude.DecayAmplitude.decayTime "Permalink to this definition")
    :   A Float specifying the decay time tdtd. Possible values are non-negative numbers.

    initial : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/DecayAmplitude.py)[¶](#abaqus.Amplitude.DecayAmplitude.DecayAmplitude.initial "Permalink to this definition")
    :   A Float specifying the constant A0A0.

    maximum : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/DecayAmplitude.py)[¶](#abaqus.Amplitude.DecayAmplitude.DecayAmplitude.maximum "Permalink to this definition")
    :   A Float specifying the coefficient AA.

    setValues(*[timeSpan](#abaqus.Amplitude.DecayAmplitude.DecayAmplitude.setValues.timeSpan "abaqus.Amplitude.DecayAmplitude.DecayAmplitude.setValues.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/DecayAmplitude.py#L95-L109)[¶](#abaqus.Amplitude.DecayAmplitude.DecayAmplitude.setValues "Permalink to this definition")
    :   This method modifies the DecayAmplitude object.

        Note

        Check [DecayAmplitude.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-decayamplitudepyc.htm?contextscope=all#simaker-decayamplitudesetvaluespyc).

        Parameters:[¶](#abaqus.Amplitude.DecayAmplitude.DecayAmplitude.setValues-parameters "Permalink to this headline")
        :   timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.DecayAmplitude.DecayAmplitude.setValues.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

        Raises:[¶](#abaqus.Amplitude.DecayAmplitude.DecayAmplitude.setValues-raises "Permalink to this headline")
        :   **RangeError** –

    start : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/DecayAmplitude.py)[¶](#abaqus.Amplitude.DecayAmplitude.DecayAmplitude.start "Permalink to this definition")
    :   A Float specifying the starting time t0t0. Possible values are non-negative numbers.

    timeSpan : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'STEP'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/DecayAmplitude.py#L45-L47)[¶](#abaqus.Amplitude.DecayAmplitude.DecayAmplitude.timeSpan "Permalink to this definition")
    :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
        and TOTAL. The default value is STEP.

*class* EquallySpacedAmplitude(*[name](#abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude "abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude.__init__.name (Python parameter)")*, *[fixedInterval](#abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude "abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude.__init__.fixedInterval (Python parameter)")*, *[data](#abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude "abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude.__init__.data (Python parameter)")*, *[begin](#abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude "abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude.__init__.begin (Python parameter)")=`0`*, *[smooth](#abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude "abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude.__init__.smooth (Python parameter)")=`abaqusConstants.SOLVER_DEFAULT`*, *[timeSpan](#abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude "abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude.__init__.timeSpan (Python parameter)")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/EquallySpacedAmplitude.py#L15-L138)[¶](#abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude "Permalink to this definition")
:   Bases: [`Amplitude`](#abaqus.Amplitude.TabularAmplitude.Amplitude "abaqus.Amplitude.Amplitude.Amplitude (Python class)")

    The EquallySpacedAmplitude object defines a list of amplitude values at fixed time intervals beginning at
    a specified value of time. The EquallySpacedAmplitude object is derived from the Amplitude object.

    Note

    This object can be accessed by:

    ```python
    import amplitude
    mdb.models[name].amplitudes[name]
    import odbAmplitude
    session.odbs[name].amplitudes[name]
    ```

    The corresponding analysis keywords are:

    * AMPLITUDE

    Note

    Check [EquallySpacedAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-equallyspacedamplitudepyc.htm?contextscope=all).

    Member Details:

    baselineCorrection : --is-rst--:py:class:`~abaqus.Amplitude.BaselineCorrection.BaselineCorrection` = `<abaqus.Amplitude.BaselineCorrection.BaselineCorrection object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/EquallySpacedAmplitude.py#L33-L34)[¶](#abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude.baselineCorrection "Permalink to this definition")
    :   A BaselineCorrection object.

    begin : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/EquallySpacedAmplitude.py#L46-L48)[¶](#abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude.begin "Permalink to this definition")
    :   A Float specifying the time at which the first amplitude data are given. Possible values
        are non-negative numbers. The default value is 0.0.

    data : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/EquallySpacedAmplitude.py#L43-L44)[¶](#abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude.data "Permalink to this definition")
    :   A sequence of Floats specifying the amplitude values.

    fixedInterval : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/EquallySpacedAmplitude.py)[¶](#abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude.fixedInterval "Permalink to this definition")
    :   A Float specifying the fixed time interval at which the amplitude data are given.
        Possible values are positive numbers.

    setValues(*[begin](#abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude.setValues.begin "abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude.setValues.begin (Python parameter) — A Float specifying the time at which the first amplitude data are given.")=`0`*, *[smooth](#abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude.setValues.smooth "abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude.setValues.smooth (Python parameter) — The SymbolicConstant SOLVER_DEFAULT or a Float specifying the degree of smoothing. Possible float values are 0 ≤ smoothing ≤ 0.5.")=`abaqusConstants.SOLVER_DEFAULT`*, *[timeSpan](#abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude.setValues.timeSpan "abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude.setValues.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/EquallySpacedAmplitude.py#L111-L138)[¶](#abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude.setValues "Permalink to this definition")
    :   This method modifies the EquallySpacedAmplitude object.

        Note

        Check [EquallySpacedAmplitude.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-equallyspacedamplitudepyc.htm?contextscope=all#simaker-equallyspacedamplitudesetvaluespyc).

        Parameters:[¶](#abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude.setValues-parameters "Permalink to this headline")
        :   begin=`0`[¶](#abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude.setValues.begin "Permalink to this definition")
            :   A Float specifying the time at which the first amplitude data are given. Possible values
                are non-negative numbers. The default value is 0.0.

            smooth=`abaqusConstants.SOLVER_DEFAULT`[¶](#abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude.setValues.smooth "Permalink to this definition")
            :   The SymbolicConstant SOLVER\_DEFAULT or a Float specifying the degree of smoothing.
                Possible float values are 0 ≤ **smoothing** ≤ 0.5. If **smooth** = SOLVER\_DEFAULT, the
                default degree of smoothing will be determined by the solver. The default value is
                SOLVER\_DEFAULT.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude.setValues.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

        Raises:[¶](#abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude.setValues-raises "Permalink to this headline")
        :   **RangeError** –

    smooth : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`, :py:class:`float`] = `'SOLVER_DEFAULT'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/EquallySpacedAmplitude.py#L50-L54)[¶](#abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude.smooth "Permalink to this definition")
    :   The SymbolicConstant SOLVER\_DEFAULT or a Float specifying the degree of smoothing.
        Possible float values are 0 ≤ **smoothing** ≤ 0.5. If **smooth** = SOLVER\_DEFAULT, the
        default degree of smoothing will be determined by the solver. The default value is
        SOLVER\_DEFAULT.

    timeSpan : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'STEP'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/EquallySpacedAmplitude.py#L56-L58)[¶](#abaqus.Amplitude.EquallySpacedAmplitude.EquallySpacedAmplitude.timeSpan "Permalink to this definition")
    :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
        and TOTAL. The default value is STEP.

*class* ModulatedAmplitude(*[name](#abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude "abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude.__init__.name (Python parameter)")*, *[initial](#abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude "abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude.__init__.initial (Python parameter)")*, *[magnitude](#abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude "abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude.__init__.magnitude (Python parameter)")*, *[start](#abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude "abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude.__init__.start (Python parameter)")*, *[frequency1](#abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude "abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude.__init__.frequency1 (Python parameter)")*, *[frequency2](#abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude "abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude.__init__.frequency2 (Python parameter)")*, *[timeSpan](#abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude "abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude.__init__.timeSpan (Python parameter)")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/ModulatedAmplitude.py#L12-L119)[¶](#abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude "Permalink to this definition")
:   Bases: [`Amplitude`](#abaqus.Amplitude.TabularAmplitude.Amplitude "abaqus.Amplitude.Amplitude.Amplitude (Python class)")

    The ModulatedAmplitude object defines a modulated amplitude curve. The ModulatedAmplitude object is
    derived from the Amplitude object.

    Note

    This object can be accessed by:

    ```python
    import amplitude
    mdb.models[name].amplitudes[name]
    import odbAmplitude
    session.odbs[name].amplitudes[name]
    ```

    The corresponding analysis keywords are:

    * AMPLITUDE

    Note

    Check [ModulatedAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modulatedamplitudepyc.htm?contextscope=all).

    Member Details:

    frequency1 : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/ModulatedAmplitude.py)[¶](#abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude.frequency1 "Permalink to this definition")
    :   A Float specifying the circular frequency 1 (ω1ω1). Possible values are positive
        numbers.

    frequency2 : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/ModulatedAmplitude.py)[¶](#abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude.frequency2 "Permalink to this definition")
    :   A Float specifying the circular frequency 2 (ω2ω2). Possible values are positive
        numbers.

    initial : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/ModulatedAmplitude.py)[¶](#abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude.initial "Permalink to this definition")
    :   A Float specifying the constant A0A0.

    magnitude : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/ModulatedAmplitude.py)[¶](#abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude.magnitude "Permalink to this definition")
    :   A Float specifying the coefficient AA.

    setValues(*[timeSpan](#abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude.setValues.timeSpan "abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude.setValues.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/ModulatedAmplitude.py#L105-L119)[¶](#abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude.setValues "Permalink to this definition")
    :   This method modifies the ModulatedAmplitude object.

        Note

        Check [ModulatedAmplitude.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modulatedamplitudepyc.htm?contextscope=all#simaker-modulatedamplitudesetvaluespyc).

        Parameters:[¶](#abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude.setValues-parameters "Permalink to this headline")
        :   timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude.setValues.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

        Raises:[¶](#abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude.setValues-raises "Permalink to this headline")
        :   **RangeError** –

    start : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/ModulatedAmplitude.py)[¶](#abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude.start "Permalink to this definition")
    :   A Float specifying the starting time t0t0. Possible values are non-negative numbers.

    timeSpan : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'STEP'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/ModulatedAmplitude.py#L50-L52)[¶](#abaqus.Amplitude.ModulatedAmplitude.ModulatedAmplitude.timeSpan "Permalink to this definition")
    :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
        and TOTAL. The default value is STEP.

*class* PeriodicAmplitude(*[name](#abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude "abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude.__init__.name (Python parameter)")*, *[frequency](#abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude "abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude.__init__.frequency (Python parameter)")*, *[start](#abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude "abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude.__init__.start (Python parameter)")*, *[a\_0](#abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude "abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude.__init__.a_0 (Python parameter)")*, *[data](#abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude "abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude.__init__.data (Python parameter)")*, *[timeSpan](#abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude "abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude.__init__.timeSpan (Python parameter)")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/PeriodicAmplitude.py#L12-L109)[¶](#abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude "Permalink to this definition")
:   Bases: [`Amplitude`](#abaqus.Amplitude.TabularAmplitude.Amplitude "abaqus.Amplitude.Amplitude.Amplitude (Python class)")

    The PeriodicAmplitude object defines an amplitude curve using a Fourier series. The PeriodicAmplitude
    object is derived from the Amplitude object.

    Note

    This object can be accessed by:

    ```python
    import amplitude
    mdb.models[name].amplitudes[name]
    import odbAmplitude
    session.odbs[name].amplitudes[name]
    ```

    The corresponding analysis keywords are:

    * AMPLITUDE

    Note

    Check [PeriodicAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-periodicamplitudepyc.htm?contextscope=all).

    Member Details:

    a\_0 : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/PeriodicAmplitude.py)[¶](#abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude.a_0 "Permalink to this definition")
    :   A Float specifying the constant A0A0.

    data : --is-rst--:py:class:`tuple`\[:py:class:`tuple`\[:py:class:`float`, :py:class:`float`], :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/PeriodicAmplitude.py#L42-L43)[¶](#abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude.data "Permalink to this definition")
    :   A sequence of pairs of Floats specifying AiAi and BiBi pairs.

    frequency : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/PeriodicAmplitude.py)[¶](#abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude.frequency "Permalink to this definition")
    :   A Float specifying the circular frequency ωω. Possible values are positive numbers.

    setValues(*[timeSpan](#abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude.setValues.timeSpan "abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude.setValues.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/PeriodicAmplitude.py#L95-L109)[¶](#abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude.setValues "Permalink to this definition")
    :   This method modifies the PeriodicAmplitude object.

        Note

        Check [PeriodicAmplitude.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-periodicamplitudepyc.htm?contextscope=all#simaker-periodicamplitudesetvaluespyc).

        Parameters:[¶](#abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude.setValues-parameters "Permalink to this headline")
        :   timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude.setValues.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

        Raises:[¶](#abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude.setValues-raises "Permalink to this headline")
        :   **RangeError** –

    start : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/PeriodicAmplitude.py)[¶](#abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude.start "Permalink to this definition")
    :   A Float specifying the starting time t0t0. Possible values are positive numbers.

    timeSpan : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'STEP'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/PeriodicAmplitude.py#L45-L47)[¶](#abaqus.Amplitude.PeriodicAmplitude.PeriodicAmplitude.timeSpan "Permalink to this definition")
    :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
        and TOTAL. The default value is STEP.

*class* PsdDefinition(*[name](#abaqus.Amplitude.PsdDefinition.PsdDefinition "abaqus.Amplitude.PsdDefinition.PsdDefinition.__init__.name (Python parameter)")*, *[data](#abaqus.Amplitude.PsdDefinition.PsdDefinition "abaqus.Amplitude.PsdDefinition.PsdDefinition.__init__.data (Python parameter)")*, *[unitType](#abaqus.Amplitude.PsdDefinition.PsdDefinition "abaqus.Amplitude.PsdDefinition.PsdDefinition.__init__.unitType (Python parameter)")=`abaqusConstants.FORCE`*, *[referenceGravityAcceleration](#abaqus.Amplitude.PsdDefinition.PsdDefinition "abaqus.Amplitude.PsdDefinition.PsdDefinition.__init__.referenceGravityAcceleration (Python parameter)")=`1`*, *[referenecePower](#abaqus.Amplitude.PsdDefinition.PsdDefinition "abaqus.Amplitude.PsdDefinition.PsdDefinition.__init__.referenecePower (Python parameter)")=`0`*, *[user](#abaqus.Amplitude.PsdDefinition.PsdDefinition "abaqus.Amplitude.PsdDefinition.PsdDefinition.__init__.user (Python parameter)")=`0`*, *[timeSpan](#abaqus.Amplitude.PsdDefinition.PsdDefinition "abaqus.Amplitude.PsdDefinition.PsdDefinition.__init__.timeSpan (Python parameter)")=`abaqusConstants.STEP`*, *[amplitude](#abaqus.Amplitude.PsdDefinition.PsdDefinition "abaqus.Amplitude.PsdDefinition.PsdDefinition.__init__.amplitude (Python parameter)")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/PsdDefinition.py#L12-L167)[¶](#abaqus.Amplitude.PsdDefinition.PsdDefinition "Permalink to this definition")
:   Bases: [`Amplitude`](#abaqus.Amplitude.TabularAmplitude.Amplitude "abaqus.Amplitude.Amplitude.Amplitude (Python class)")

    The PsdDefinition object defines the cross-spectral density frequency function for random response
    loading. The PsdDefinition object is derived from the Amplitude object.

    Note

    This object can be accessed by:

    ```python
    import amplitude
    mdb.models[name].amplitudes[name]
    import odbAmplitude
    session.odbs[name].amplitudes[name]
    ```

    The corresponding analysis keywords are:

    * PSD-DEFINITION

    Note

    Check [PsdDefinition on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-psddefinitionpyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/PsdDefinition.py#L60-L63)[¶](#abaqus.Amplitude.PsdDefinition.PsdDefinition.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude that describes the dynamic event used to
        define the cross-spectral density frequency function. The default value is an empty
        string.

    data : --is-rst--:py:class:`tuple`\[:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`], :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/PsdDefinition.py#L33-L36)[¶](#abaqus.Amplitude.PsdDefinition.PsdDefinition.data "Permalink to this definition")
    :   A sequence of sequences of Floats specifying the real part of the frequency function,
        the imaginary part of the frequency function, and the frequency or frequency band number
        values, depending on the value of **unitType**.

    referenceGravityAcceleration : --is-rst--:py:class:`float` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/PsdDefinition.py#L43-L45)[¶](#abaqus.Amplitude.PsdDefinition.PsdDefinition.referenceGravityAcceleration "Permalink to this definition")
    :   A Float specifying the reference gravity acceleration. This argument applies when
        **unitType** = BASE. The default value is 1.0.

    referenecePower : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/PsdDefinition.py#L47-L49)[¶](#abaqus.Amplitude.PsdDefinition.PsdDefinition.referenecePower "Permalink to this definition")
    :   A Float specifying the reference power value, in load units squared. This argument
        applies when **unitType** = DB. The default value is 0.0.

    setValues(*[unitType](#abaqus.Amplitude.PsdDefinition.PsdDefinition.setValues.unitType "abaqus.Amplitude.PsdDefinition.PsdDefinition.setValues.unitType (Python parameter) — A SymbolicConstant specifying the type of units for specifying the frequency function. FORCE implies power units.")=`abaqusConstants.FORCE`*, *[referenceGravityAcceleration](#abaqus.Amplitude.PsdDefinition.PsdDefinition.setValues.referenceGravityAcceleration "abaqus.Amplitude.PsdDefinition.PsdDefinition.setValues.referenceGravityAcceleration (Python parameter) — A Float specifying the reference gravity acceleration.")=`1`*, *[referenecePower](#abaqus.Amplitude.PsdDefinition.PsdDefinition.setValues.referenecePower "abaqus.Amplitude.PsdDefinition.PsdDefinition.setValues.referenecePower (Python parameter) — A Float specifying the reference power value, in load units squared.")=`0`*, *[user](#abaqus.Amplitude.PsdDefinition.PsdDefinition.setValues.user "abaqus.Amplitude.PsdDefinition.PsdDefinition.setValues.user (Python parameter) — A Boolean specifying whether the frequency function is defined in user subroutine UPSD. If specified, then data is not applicable, and the unitType value must not be DB. The default value is OFF.")=`0`*, *[timeSpan](#abaqus.Amplitude.PsdDefinition.PsdDefinition.setValues.timeSpan "abaqus.Amplitude.PsdDefinition.PsdDefinition.setValues.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*, *[amplitude](#abaqus.Amplitude.PsdDefinition.PsdDefinition.setValues.amplitude "abaqus.Amplitude.PsdDefinition.PsdDefinition.setValues.amplitude (Python parameter) — A String specifying the name of the amplitude that describes the dynamic event used to define the cross-spectral density frequency function.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/PsdDefinition.py#L127-L167)[¶](#abaqus.Amplitude.PsdDefinition.PsdDefinition.setValues "Permalink to this definition")
    :   This method modifies the PsdDefinition object.

        Note

        Check [PsdDefinition.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-psddefinitionpyc.htm?contextscope=all#simaker-psddefinitionsetvaluespyc).

        Parameters:[¶](#abaqus.Amplitude.PsdDefinition.PsdDefinition.setValues-parameters "Permalink to this headline")
        :   unitType=`abaqusConstants.FORCE`[¶](#abaqus.Amplitude.PsdDefinition.PsdDefinition.setValues.unitType "Permalink to this definition")
            :   A SymbolicConstant specifying the type of units for specifying the frequency function.
                FORCE implies power units. BASE implies gravity used to define base motion. DB implies
                decibel units. Possible values are FORCE, BASE, and DB. The default value is FORCE.

            referenceGravityAcceleration=`1`[¶](#abaqus.Amplitude.PsdDefinition.PsdDefinition.setValues.referenceGravityAcceleration "Permalink to this definition")
            :   A Float specifying the reference gravity acceleration. This argument applies when
                **unitType** = BASE. The default value is 1.0.

            referenecePower=`0`[¶](#abaqus.Amplitude.PsdDefinition.PsdDefinition.setValues.referenecePower "Permalink to this definition")
            :   A Float specifying the reference power value, in load units squared. This argument
                applies when **unitType** = DB. The default value is 0.0.

            user=`0`[¶](#abaqus.Amplitude.PsdDefinition.PsdDefinition.setValues.user "Permalink to this definition")
            :   A Boolean specifying whether the frequency function is defined in user subroutine UPSD.
                If specified, then **data** is not applicable, and the **unitType** value must not be DB.
                The default value is OFF.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.PsdDefinition.PsdDefinition.setValues.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

            amplitude=`''`[¶](#abaqus.Amplitude.PsdDefinition.PsdDefinition.setValues.amplitude "Permalink to this definition")
            :   A String specifying the name of the amplitude that describes the dynamic event used to
                define the cross-spectral density frequency function. The default value is an empty
                string.

        Raises:[¶](#abaqus.Amplitude.PsdDefinition.PsdDefinition.setValues-raises "Permalink to this headline")
        :   **RangeError** –

    timeSpan : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'STEP'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/PsdDefinition.py#L56-L58)[¶](#abaqus.Amplitude.PsdDefinition.PsdDefinition.timeSpan "Permalink to this definition")
    :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
        and TOTAL. The default value is STEP.

    unitType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FORCE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/PsdDefinition.py#L38-L41)[¶](#abaqus.Amplitude.PsdDefinition.PsdDefinition.unitType "Permalink to this definition")
    :   A SymbolicConstant specifying the type of units for specifying the frequency function.
        FORCE implies power units. BASE implies gravity used to define base motion. DB implies
        decibel units. Possible values are FORCE, BASE, and DB. The default value is FORCE.

    user : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/PsdDefinition.py#L51-L54)[¶](#abaqus.Amplitude.PsdDefinition.PsdDefinition.user "Permalink to this definition")
    :   A Boolean specifying whether the frequency function is defined in user subroutine UPSD.
        If specified, then **data** is not applicable, and the **unitType** value must not be DB.
        The default value is OFF.

*class* SmoothStepAmplitude(*[name](#abaqus.Amplitude.SmoothStepAmplitude.SmoothStepAmplitude "abaqus.Amplitude.SmoothStepAmplitude.SmoothStepAmplitude.__init__.name (Python parameter)")*, *[data](#abaqus.Amplitude.SmoothStepAmplitude.SmoothStepAmplitude "abaqus.Amplitude.SmoothStepAmplitude.SmoothStepAmplitude.__init__.data (Python parameter)")*, *[timeSpan](#abaqus.Amplitude.SmoothStepAmplitude.SmoothStepAmplitude "abaqus.Amplitude.SmoothStepAmplitude.SmoothStepAmplitude.__init__.timeSpan (Python parameter)")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/SmoothStepAmplitude.py#L12-L88)[¶](#abaqus.Amplitude.SmoothStepAmplitude.SmoothStepAmplitude "Permalink to this definition")
:   Bases: [`Amplitude`](#abaqus.Amplitude.TabularAmplitude.Amplitude "abaqus.Amplitude.Amplitude.Amplitude (Python class)")

    The SmoothStepAmplitude object defines an amplitude that ramps up or down smoothly from one data point to
    another. The SmoothStepAmplitude object is derived from the Amplitude object.

    Note

    This object can be accessed by:

    ```python
    import amplitude
    mdb.models[name].amplitudes[name]
    import odbAmplitude
    session.odbs[name].amplitudes[name]
    ```

    The corresponding analysis keywords are:

    * AMPLITUDE

    Note

    Check [SmoothStepAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-smoothstepamplitudepyc.htm?contextscope=all).

    Member Details:

    data : --is-rst--:py:class:`tuple`\[:py:class:`tuple`\[:py:class:`float`, :py:class:`float`], :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/SmoothStepAmplitude.py#L33-L35)[¶](#abaqus.Amplitude.SmoothStepAmplitude.SmoothStepAmplitude.data "Permalink to this definition")
    :   A sequence of pairs of Floats specifying time/frequency and amplitude pairs. Possible
        values for time/frequency are positive numbers.

    setValues(*[timeSpan](#abaqus.Amplitude.SmoothStepAmplitude.SmoothStepAmplitude.setValues.timeSpan "abaqus.Amplitude.SmoothStepAmplitude.SmoothStepAmplitude.setValues.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/SmoothStepAmplitude.py#L74-L88)[¶](#abaqus.Amplitude.SmoothStepAmplitude.SmoothStepAmplitude.setValues "Permalink to this definition")
    :   This method modifies the SmoothStepAmplitude object.

        Note

        Check [SmoothStepAmplitude.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-smoothstepamplitudepyc.htm?contextscope=all#simaker-smoothstepamplitudesetvaluespyc).

        Parameters:[¶](#abaqus.Amplitude.SmoothStepAmplitude.SmoothStepAmplitude.setValues-parameters "Permalink to this headline")
        :   timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.SmoothStepAmplitude.SmoothStepAmplitude.setValues.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

        Raises:[¶](#abaqus.Amplitude.SmoothStepAmplitude.SmoothStepAmplitude.setValues-raises "Permalink to this headline")
        :   **RangeError** –

    timeSpan : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'STEP'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/SmoothStepAmplitude.py#L37-L39)[¶](#abaqus.Amplitude.SmoothStepAmplitude.SmoothStepAmplitude.timeSpan "Permalink to this definition")
    :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
        and TOTAL. The default value is STEP.

*class* SolutionDependentAmplitude(*[name](#abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude "abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude.__init__.name (Python parameter)")*, *[initial](#abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude "abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude.__init__.initial (Python parameter)")=`1`*, *[minimum](#abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude "abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude.__init__.minimum (Python parameter)")=`0`*, *[maximum](#abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude "abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude.__init__.maximum (Python parameter)")=`1000`*, *[timeSpan](#abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude "abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude.__init__.timeSpan (Python parameter)")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/SolutionDependentAmplitude.py#L12-L124)[¶](#abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude "Permalink to this definition")
:   Bases: [`Amplitude`](#abaqus.Amplitude.TabularAmplitude.Amplitude "abaqus.Amplitude.Amplitude.Amplitude (Python class)")

    The SolutionDependentAmplitude object defines a solution-dependent amplitude for superplastic forming
    analysis. The SolutionDependentAmplitude object is derived from the Amplitude object.

    Note

    This object can be accessed by:

    ```python
    import amplitude
    mdb.models[name].amplitudes[name]
    import odbAmplitude
    session.odbs[name].amplitudes[name]
    ```

    The corresponding analysis keywords are:

    * AMPLITUDE

    Note

    Check [SolutionDependentAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-solutiondependentamplitudepyc.htm?contextscope=all).

    Member Details:

    initial : --is-rst--:py:class:`float` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/SolutionDependentAmplitude.py#L33-L35)[¶](#abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude.initial "Permalink to this definition")
    :   A Float specifying the initial amplitude value. Possible values are those between
        **minimum** and **maximum**. The default value is 1.0.

    maximum : --is-rst--:py:class:`float` = `1000`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/SolutionDependentAmplitude.py#L41-L43)[¶](#abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude.maximum "Permalink to this definition")
    :   A Float specifying the maximum amplitude value. Possible values are those larger than
        **minimum** and **initial**. The default value is 1000.0.

    minimum : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/SolutionDependentAmplitude.py#L37-L39)[¶](#abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude.minimum "Permalink to this definition")
    :   A Float specifying the minimum amplitude value. Possible values are those smaller than
        **maximum** and **initial**. The default value is 0.1.

    setValues(*[initial](#abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude.setValues.initial "abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude.setValues.initial (Python parameter) — A Float specifying the initial amplitude value.")=`1`*, *[minimum](#abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude.setValues.minimum "abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude.setValues.minimum (Python parameter) — A Float specifying the minimum amplitude value.")=`0`*, *[maximum](#abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude.setValues.maximum "abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude.setValues.maximum (Python parameter) — A Float specifying the maximum amplitude value.")=`1000`*, *[timeSpan](#abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude.setValues.timeSpan "abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude.setValues.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/SolutionDependentAmplitude.py#L95-L124)[¶](#abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude.setValues "Permalink to this definition")
    :   This method modifies the SolutionDependentAmplitude object.

        Note

        Check [SolutionDependentAmplitude.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-solutiondependentamplitudepyc.htm?contextscope=all#simaker-solutiondependentamplitudesetvaluespyc).

        Parameters:[¶](#abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude.setValues-parameters "Permalink to this headline")
        :   initial=`1`[¶](#abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude.setValues.initial "Permalink to this definition")
            :   A Float specifying the initial amplitude value. Possible values are those between
                **minimum** and **maximum**. The default value is 1.0.

            minimum=`0`[¶](#abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude.setValues.minimum "Permalink to this definition")
            :   A Float specifying the minimum amplitude value. Possible values are those smaller than
                **maximum** and **initial**. The default value is 0.1.

            maximum=`1000`[¶](#abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude.setValues.maximum "Permalink to this definition")
            :   A Float specifying the maximum amplitude value. Possible values are those larger than
                **minimum** and **initial**. The default value is 1000.0.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude.setValues.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

        Raises:[¶](#abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude.setValues-raises "Permalink to this headline")
        :   **RangeError** –

    timeSpan : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'STEP'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/SolutionDependentAmplitude.py#L45-L47)[¶](#abaqus.Amplitude.SolutionDependentAmplitude.SolutionDependentAmplitude.timeSpan "Permalink to this definition")
    :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
        and TOTAL. The default value is STEP.

*class* SpectrumAmplitude(*[name](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude "abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.__init__.name (Python parameter)")*, *[method](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude "abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.__init__.method (Python parameter)")*, *[data](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude "abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.__init__.data (Python parameter)")*, *[specificationUnits](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude "abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.__init__.specificationUnits (Python parameter)")=`abaqusConstants.ACCELERATION`*, *[eventUnits](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude "abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.__init__.eventUnits (Python parameter)")=`abaqusConstants.EVENT_ACCELERATION`*, *[solution](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude "abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.__init__.solution (Python parameter)")=`abaqusConstants.ABSOLUTE_VALUE`*, *[timeIncrement](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude "abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.__init__.timeIncrement (Python parameter)")=`0`*, *[gravity](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude "abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.__init__.gravity (Python parameter)")=`1`*, *[criticalDamping](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude "abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.__init__.criticalDamping (Python parameter)")=`0`*, *[timeSpan](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude "abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.__init__.timeSpan (Python parameter)")=`abaqusConstants.STEP`*, *[amplitude](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude "abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.__init__.amplitude (Python parameter)")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/SpectrumAmplitude.py#L20-L219)[¶](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude "Permalink to this definition")
:   Bases: [`Amplitude`](#abaqus.Amplitude.TabularAmplitude.Amplitude "abaqus.Amplitude.Amplitude.Amplitude (Python class)")

    The SpectrumAmplitude object defines the spectrum of responses for displacement, velocity, or
    acceleration to be used in a response spectrum analysis. The SpectrumAmplitude object is derived from the
    Amplitude object.

    Note

    This object can be accessed by:

    ```python
    import amplitude
    mdb.models[name].amplitudes[name]
    import odbAmplitude
    session.odbs[name].amplitudes[name]
    ```

    The corresponding analysis keywords are:

    * SPECTRUM

    Note

    Check [SpectrumAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-spectrumamplitudepyc.htm?contextscope=all).

    Member Details:

    amplitude : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/SpectrumAmplitude.py#L84-L86)[¶](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.amplitude "Permalink to this definition")
    :   A String specifying the name of the amplitude that describes the dynamic event used to
        calculate the spectrum. The default value is an empty string.

    criticalDamping : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/SpectrumAmplitude.py#L73-L78)[¶](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.criticalDamping "Permalink to this definition")
    :   A Boolean specifying whether to calculate the spectrum for only the specified range of
        critical damping values or a list of values. If **criticalDamping** = ON, the spectrum is
        calculated only for the specified range of critical damping values. If **criticalDamping**
        = OFF, the spectrum is calculated for a list of damping values. The default value is
        OFF.

    data : --is-rst--:py:class:`tuple`\[:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`], :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/SpectrumAmplitude.py#L46-L48)[¶](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.data "Permalink to this definition")
    :   A sequence of sequences of Floats specifying the magnitude, frequency, and damping
        values.

    eventUnits : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'EVENT_ACCELERATION'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/SpectrumAmplitude.py#L55-L59)[¶](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.eventUnits "Permalink to this definition")
    :   A SymbolicConstant specifying the units used to describe the dynamic event in the
        amplitude used for the calculation. Possible values are EVENT\_DISPLACEMENT,
        EVENT\_VELOCITY, EVENT\_ACCELERATION, and EVENT\_GRAVITY. The default value is
        EVENT\_ACCELERATION.

    gravity : --is-rst--:py:class:`float` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/SpectrumAmplitude.py#L69-L71)[¶](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.gravity "Permalink to this definition")
    :   A Float specifying the acceleration due to gravity. This argument applies only when
        **specificationUnits** = GRAVITY or\*eventUnits\* = GRAVITY. The default value is 1.0.

    method : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/SpectrumAmplitude.py)[¶](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.method "Permalink to this definition")
    :   A SymbolicConstant specifying the method for specifying the spectrum. Possible values
        are DEFINE and CALCULATE.

    setValues(*[specificationUnits](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues.specificationUnits "abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues.specificationUnits (Python parameter) — A SymbolicConstant specifying the units used for specifying the spectrum.")=`abaqusConstants.ACCELERATION`*, *[eventUnits](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues.eventUnits "abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues.eventUnits (Python parameter) — A SymbolicConstant specifying the units used to describe the dynamic event in the amplitude used for the calculation.")=`abaqusConstants.EVENT_ACCELERATION`*, *[solution](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues.solution "abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues.solution (Python parameter) — A SymbolicConstant specifying the solution method for the dynamic equations.")=`abaqusConstants.ABSOLUTE_VALUE`*, *[timeIncrement](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues.timeIncrement "abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues.timeIncrement (Python parameter) — A Float specifying the implicit time increment used to calculate the spectrum.")=`0`*, *[gravity](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues.gravity "abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues.gravity (Python parameter) — A Float specifying the acceleration due to gravity.")=`1`*, *[criticalDamping](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues.criticalDamping "abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues.criticalDamping (Python parameter) — A Boolean specifying whether to calculate the spectrum for only the specified range of critical damping values or a list of values.")=`0`*, *[timeSpan](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues.timeSpan "abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*, *[amplitude](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues.amplitude "abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues.amplitude (Python parameter) — A String specifying the name of the amplitude that describes the dynamic event used to calculate the spectrum.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/SpectrumAmplitude.py#L166-L219)[¶](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues "Permalink to this definition")
    :   This method modifies the SpectrumAmplitude object.

        Note

        Check [SpectrumAmplitude.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-spectrumamplitudepyc.htm?contextscope=all#simaker-spectrumamplitudesetvaluespyc).

        Parameters:[¶](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues-parameters "Permalink to this headline")
        :   specificationUnits=`abaqusConstants.ACCELERATION`[¶](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues.specificationUnits "Permalink to this definition")
            :   A SymbolicConstant specifying the units used for specifying the spectrum. Possible
                values are DISPLACEMENT, VELOCITY, ACCELERATION, and GRAVITY. The default value is
                ACCELERATION.

            eventUnits=`abaqusConstants.EVENT_ACCELERATION`[¶](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues.eventUnits "Permalink to this definition")
            :   A SymbolicConstant specifying the units used to describe the dynamic event in the
                amplitude used for the calculation. Possible values are EVENT\_DISPLACEMENT,
                EVENT\_VELOCITY, EVENT\_ACCELERATION, and EVENT\_GRAVITY. The default value is
                EVENT\_ACCELERATION.

            solution=`abaqusConstants.ABSOLUTE_VALUE`[¶](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues.solution "Permalink to this definition")
            :   A SymbolicConstant specifying the solution method for the dynamic equations. Possible
                values are ABSOLUTE\_VALUE and RELATIVE\_VALUE. The default value is ABSOLUTE\_VALUE.

            timeIncrement=`0`[¶](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues.timeIncrement "Permalink to this definition")
            :   A Float specifying the implicit time increment used to calculate the spectrum. This
                argument is required when the **method** = CALCULATE. The default value is 0.0.

            gravity=`1`[¶](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues.gravity "Permalink to this definition")
            :   A Float specifying the acceleration due to gravity. This argument applies only when
                **specificationUnits** = GRAVITY or\*eventUnits\* = GRAVITY. The default value is 1.0.

            criticalDamping=`0`[¶](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues.criticalDamping "Permalink to this definition")
            :   A Boolean specifying whether to calculate the spectrum for only the specified range of
                critical damping values or a list of values. If **criticalDamping** = ON, the spectrum is
                calculated only for the specified range of critical damping values. If **criticalDamping**
                = OFF, the spectrum is calculated for a list of damping values. The default value is
                OFF.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

            amplitude=`''`[¶](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues.amplitude "Permalink to this definition")
            :   A String specifying the name of the amplitude that describes the dynamic event used to
                calculate the spectrum. The default value is an empty string.

        Raises:[¶](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.setValues-raises "Permalink to this headline")
        :   **RangeError** –

    solution : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'ABSOLUTE_VALUE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/SpectrumAmplitude.py#L61-L63)[¶](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.solution "Permalink to this definition")
    :   A SymbolicConstant specifying the solution method for the dynamic equations. Possible
        values are ABSOLUTE\_VALUE and RELATIVE\_VALUE. The default value is ABSOLUTE\_VALUE.

    specificationUnits : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'ACCELERATION'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/SpectrumAmplitude.py#L50-L53)[¶](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.specificationUnits "Permalink to this definition")
    :   A SymbolicConstant specifying the units used for specifying the spectrum. Possible
        values are DISPLACEMENT, VELOCITY, ACCELERATION, and GRAVITY. The default value is
        ACCELERATION.

    timeIncrement : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/SpectrumAmplitude.py#L65-L67)[¶](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.timeIncrement "Permalink to this definition")
    :   A Float specifying the implicit time increment used to calculate the spectrum. This
        argument is required when the **method** = CALCULATE. The default value is 0.0.

    timeSpan : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'STEP'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/SpectrumAmplitude.py#L80-L82)[¶](#abaqus.Amplitude.SpectrumAmplitude.SpectrumAmplitude.timeSpan "Permalink to this definition")
    :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
        and TOTAL. The default value is STEP.

*class* TabularAmplitude(*[name](#abaqus.Amplitude.TabularAmplitude.TabularAmplitude "abaqus.Amplitude.TabularAmplitude.TabularAmplitude.__init__.name (Python parameter)")*, *[data](#abaqus.Amplitude.TabularAmplitude.TabularAmplitude "abaqus.Amplitude.TabularAmplitude.TabularAmplitude.__init__.data (Python parameter)")*, *[smooth](#abaqus.Amplitude.TabularAmplitude.TabularAmplitude "abaqus.Amplitude.TabularAmplitude.TabularAmplitude.__init__.smooth (Python parameter)")=`abaqusConstants.SOLVER_DEFAULT`*, *[timeSpan](#abaqus.Amplitude.TabularAmplitude.TabularAmplitude "abaqus.Amplitude.TabularAmplitude.TabularAmplitude.__init__.timeSpan (Python parameter)")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/TabularAmplitude.py#L15-L120)[¶](#abaqus.Amplitude.TabularAmplitude.TabularAmplitude "Permalink to this definition")
:   Bases: [`Amplitude`](#abaqus.Amplitude.TabularAmplitude.Amplitude "abaqus.Amplitude.Amplitude.Amplitude (Python class)")

    The TabularAmplitude object defines an amplitude curve as a table of values at convenient points on the
    time scale. The TabularAmplitude object is derived from the Amplitude object.

    Note

    This object can be accessed by:

    ```python
    import amplitude
    mdb.models[name].amplitudes[name]
    import odbAmplitude
    session.odbs[name].amplitudes[name]
    ```

    The corresponding analysis keywords are:

    * AMPLITUDE

    Note

    Check [TabularAmplitude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tabularamplitudepyc.htm?contextscope=all).

    Member Details:

    baselineCorrection : --is-rst--:py:class:`~abaqus.Amplitude.BaselineCorrection.BaselineCorrection` = `<abaqus.Amplitude.BaselineCorrection.BaselineCorrection object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/TabularAmplitude.py#L33-L34)[¶](#abaqus.Amplitude.TabularAmplitude.TabularAmplitude.baselineCorrection "Permalink to this definition")
    :   A BaselineCorrection object.

    data : --is-rst--:py:class:`tuple`\[:py:class:`tuple`\[:py:class:`float`, :py:class:`float`], :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/TabularAmplitude.py#L39-L41)[¶](#abaqus.Amplitude.TabularAmplitude.TabularAmplitude.data "Permalink to this definition")
    :   A sequence of pairs of Floats specifying time/frequency and amplitude pairs. Possible
        values for time/frequency are positive numbers.

    setValues(*[smooth](#abaqus.Amplitude.TabularAmplitude.TabularAmplitude.setValues.smooth "abaqus.Amplitude.TabularAmplitude.TabularAmplitude.setValues.smooth (Python parameter) — The SymbolicConstant SOLVER_DEFAULT or a Float specifying the degree of smoothing. Possible float values are between 0 and 0.5.")=`abaqusConstants.SOLVER_DEFAULT`*, *[timeSpan](#abaqus.Amplitude.TabularAmplitude.TabularAmplitude.setValues.timeSpan "abaqus.Amplitude.TabularAmplitude.TabularAmplitude.setValues.timeSpan (Python parameter) — A SymbolicConstant specifying the time span of the amplitude.")=`abaqusConstants.STEP`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/TabularAmplitude.py#L97-L120)[¶](#abaqus.Amplitude.TabularAmplitude.TabularAmplitude.setValues "Permalink to this definition")
    :   This method modifies the TabularAmplitude object.

        Note

        Check [TabularAmplitude.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tabularamplitudepyc.htm?contextscope=all#simaker-tabularamplitudesetvaluespyc).

        Parameters:[¶](#abaqus.Amplitude.TabularAmplitude.TabularAmplitude.setValues-parameters "Permalink to this headline")
        :   smooth=`abaqusConstants.SOLVER_DEFAULT`[¶](#abaqus.Amplitude.TabularAmplitude.TabularAmplitude.setValues.smooth "Permalink to this definition")
            :   The SymbolicConstant SOLVER\_DEFAULT or a Float specifying the degree of smoothing.
                Possible float values are between 0 and 0.5. If **smooth** = SOLVER\_DEFAULT, the default
                degree of smoothing will be determined by the solver. The default value is
                SOLVER\_DEFAULT.

            timeSpan=`abaqusConstants.STEP`[¶](#abaqus.Amplitude.TabularAmplitude.TabularAmplitude.setValues.timeSpan "Permalink to this definition")
            :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
                and TOTAL. The default value is STEP.

        Raises:[¶](#abaqus.Amplitude.TabularAmplitude.TabularAmplitude.setValues-raises "Permalink to this headline")
        :   **RangeError** –

    smooth : --is-rst--:py:data:`~typing.Union`\[:py:data:`~typing.Literal`\[``SOLVER\_DEFAULT``], :py:class:`float`] = `'SOLVER_DEFAULT'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/TabularAmplitude.py#L43-L47)[¶](#abaqus.Amplitude.TabularAmplitude.TabularAmplitude.smooth "Permalink to this definition")
    :   The SymbolicConstant SOLVER\_DEFAULT or a Float specifying the degree of smoothing.
        Possible float values are between 0 and 0.5. If **smooth** = SOLVER\_DEFAULT, the default
        degree of smoothing will be determined by the solver. The default value is
        SOLVER\_DEFAULT.

    timeSpan : --is-rst--:py:data:`~typing.Literal`\[``STEP``, ``TOTAL``] = `'STEP'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/TabularAmplitude.py#L49-L51)[¶](#abaqus.Amplitude.TabularAmplitude.TabularAmplitude.timeSpan "Permalink to this definition")
    :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
        and TOTAL. The default value is STEP.

*class* BaselineCorrection(*[intervals](#abaqus.Amplitude.TabularAmplitude.BaselineCorrection "abaqus.Amplitude.TabularAmplitude.BaselineCorrection.__init__.intervals (Python parameter)")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/TabularAmplitude.py#L6-L65)[¶](#abaqus.Amplitude.TabularAmplitude.BaselineCorrection "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The BaselineCorrection object modifies an acceleration history to minimize the overall drift of the
    displacement obtained from the time integration of the given acceleration.

    Note

    This object can be accessed by:

    ```python
    import amplitude
    mdb.models[name].amplitudes[name].baselineCorrection
    import odbAmplitude
    session.odbs[name].amplitudes[name].baselineCorrection
    ```

    The corresponding analysis keywords are:

    * BASELINE CORRECTION

    Note

    Check [BaselineCorrection on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-baselinecorrectionpyc.htm?contextscope=all).

    Member Details:

    intervals : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/TabularAmplitude.py#L24-L27)[¶](#abaqus.Amplitude.TabularAmplitude.BaselineCorrection.intervals "Permalink to this definition")
    :   A sequence of Floats specifying the correction time interval end points. Possible values
        are positive and monotonically increasing Floats. The default value is an empty
        sequence.

    setValues(*\*[args](#abaqus.Amplitude.TabularAmplitude.BaselineCorrection.setValues "abaqus.Amplitude.TabularAmplitude.BaselineCorrection.setValues.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Amplitude.TabularAmplitude.BaselineCorrection.setValues "abaqus.Amplitude.TabularAmplitude.BaselineCorrection.setValues.kwargs (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/TabularAmplitude.py#L57-L65)[¶](#abaqus.Amplitude.TabularAmplitude.BaselineCorrection.setValues "Permalink to this definition")
    :   This method modifies the BaselineCorrection object.

        Raises:[¶](#abaqus.Amplitude.TabularAmplitude.BaselineCorrection.setValues-raises "Permalink to this headline")
        :   **RangeError** –

*class* Correlation[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/Correlation.py#L9-L36)[¶](#abaqus.Amplitude.Correlation.Correlation "Permalink to this definition")
:   Bases: [`Amplitude`](#abaqus.Amplitude.TabularAmplitude.Amplitude "abaqus.Amplitude.Amplitude.Amplitude (Python class)")

    A Correlation is an object used to define the cross-correlation as part of the definition of random
    loading. The Correlation object is derived from the Amplitude object.

    Note

    This object can be accessed by:

    ```python
    import load
    mdb.models[name].boundaryConditions[name].correlation[i]
    ```

    Note

    Check [Correlation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-correlationpyc.htm?contextscope=all).

    Member Details:

    approach : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'CORRELATED'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/Correlation.py#L24-L27)[¶](#abaqus.Amplitude.Correlation.Correlation.approach "Permalink to this definition")
    :   A SymbolicConstant specifying the approach used in the correlation data representation.
        Possible values are CORRELATED, MOVING\_NOISE, UNCORRELATED, and USER. The default value
        is CORRELATED.

    data : --is-rst--:py:class:`tuple`\[:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`], :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/Correlation.py#L29-L32)[¶](#abaqus.Amplitude.Correlation.Correlation.data "Permalink to this definition")
    :   A tuple of tuples of Floats specifying the real and imaginary part of the scaling
        factor. If **approach** = MOVING\_NOISE, then **data** represents the noise velocity components
        1, 2, and 3.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/Correlation.py#L21-L22)[¶](#abaqus.Amplitude.Correlation.Correlation.name "Permalink to this definition")
    :   A String specifying the repository key.

    timeSpan : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'STEP'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Amplitude/Correlation.py#L9-L36)[¶](#abaqus.Amplitude.Correlation.Correlation.timeSpan "Permalink to this definition")
    :   A SymbolicConstant specifying the time span of the amplitude. Possible values are STEP
        and TOTAL. The default value is STEP.

[Back to top](#)