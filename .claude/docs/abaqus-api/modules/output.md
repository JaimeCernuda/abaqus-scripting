# Abaqus OUTPUT Module API Reference

> Source: [https://hailin.wang/abqpy/en/2025/reference/mdb/model/output.html](https://hailin.wang/abqpy/en/2025/reference/mdb/model/output.html)
> Downloaded for offline use by Claude Code skills.

---

# Output Request[¶](#output-request "Permalink to this heading")

Step output commands are used for configuring output requests, integrated output sections, diagnostic printing, monitoring, and restart.

## Create output requests for Model[¶](#create-output-requests-for-model "Permalink to this heading")

*class* OutputModel(*[name](#abaqus.StepOutput.OutputModel.OutputModel "abaqus.StepOutput.OutputModel.OutputModel.__init__.name (Python parameter)")*, *[description](#abaqus.StepOutput.OutputModel.OutputModel "abaqus.StepOutput.OutputModel.OutputModel.__init__.description (Python parameter)")=`''`*, *[stefanBoltzmann](#abaqus.StepOutput.OutputModel.OutputModel "abaqus.StepOutput.OutputModel.OutputModel.__init__.stefanBoltzmann (Python parameter)")=`None`*, *[absoluteZero](#abaqus.StepOutput.OutputModel.OutputModel "abaqus.StepOutput.OutputModel.OutputModel.__init__.absoluteZero (Python parameter)")=`None`*, *[waveFormulation](#abaqus.StepOutput.OutputModel.OutputModel "abaqus.StepOutput.OutputModel.OutputModel.__init__.waveFormulation (Python parameter)")=`abaqusConstants.NOT_SET`*, *[modelType](#abaqus.StepOutput.OutputModel.OutputModel "abaqus.StepOutput.OutputModel.OutputModel.__init__.modelType (Python parameter)")=`abaqusConstants.STANDARD_EXPLICIT`*, *[universalGas](#abaqus.StepOutput.OutputModel.OutputModel "abaqus.StepOutput.OutputModel.OutputModel.__init__.universalGas (Python parameter)")=`None`*, *[copyConstraints](#abaqus.StepOutput.OutputModel.OutputModel "abaqus.StepOutput.OutputModel.OutputModel.__init__.copyConstraints (Python parameter)")=`1`*, *[copyConnectors](#abaqus.StepOutput.OutputModel.OutputModel "abaqus.StepOutput.OutputModel.OutputModel.__init__.copyConnectors (Python parameter)")=`1`*, *[copyInteractions](#abaqus.StepOutput.OutputModel.OutputModel "abaqus.StepOutput.OutputModel.OutputModel.__init__.copyInteractions (Python parameter)")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L38-L448)[¶](#abaqus.StepOutput.OutputModel.OutputModel "Permalink to this definition")
:   Bases: [`ModelBase`](index.html#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase (Python class) — Bases: object")

    Abaqus creates a Model object named Model-1 when a session is started.

    Note

    This object can be accessed by:

    ```python
    mdb.models[name]
    ```

    Note

    Check [OutputModel on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?contextscope=all).

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
    | [`FieldOutputRequest`](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest (Python method) — This method creates a FieldOutputRequest object.")(name, createStepName[, ...]) | This method creates a FieldOutputRequest object. |
    | [`HistoryOutputRequest`](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest (Python method) — This method creates a HistoryOutputRequest object.")(name, createStepName[, ...]) | This method creates a HistoryOutputRequest object. |
    | [`IntegratedOutputSection`](#abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection "abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection (Python method) — This method creates an IntegratedOutputSection object.")(name, surface[, ...]) | This method creates an IntegratedOutputSection object. |
    | [`TimePoint`](#abaqus.StepOutput.OutputModel.OutputModel.TimePoint "abaqus.StepOutput.OutputModel.OutputModel.TimePoint (Python method) — This method creates a TimePoint object.")(name, points) | This method creates a TimePoint object. |

    Inherited from [`ModelBase`](index.html#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | `__init__`(name[, description, ...]) | This method creates a Model object. |
    | [`setValues`](index.html#abaqus.Model.ModelBase.ModelBase.setValues "abaqus.Model.ModelBase.ModelBase.setValues (Python method) — This method modifies the Model object.")([description, noPartsInputFile, ...]) | This method modifies the Model object. |

    ---

    Member Details:

    FieldOutputRequest(*[name](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.name "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.name (Python parameter) — A String specifying the repository key.")*, *[createStepName](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.createStepName "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.createStepName (Python parameter) — A String specifying the name of the step in which the object is created.")*, *[region](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.region "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.region (Python parameter) — The SymbolicConstant MODEL or a Region object specifying the region from which output is requested.")=`abaqusConstants.MODEL`*, *[variables](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.variables "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.variables (Python parameter) — A sequence of Strings specifying output request variable or component names, or the SymbolicConstant PRESELECT or ALL.")=`abaqusConstants.PRESELECT`*, *[frequency](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.frequency "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.frequency (Python parameter) — The SymbolicConstant LAST_INCREMENT or an Int specifying the output frequency in increments.")=`1`*, *[modes](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.modes "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.modes (Python parameter) — The SymbolicConstant ALL or a sequence of Ints specifying a list of eigenmodes for which output is desired.")=`abaqusConstants.ALL`*, *[timeInterval](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.timeInterval "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.timeInterval (Python parameter) — The SymbolicConstant EVERY_TIME_INCREMENT or a Float specifying the time interval at which the output states are to be written.")=`abaqusConstants.EVERY_TIME_INCREMENT`*, *[numIntervals](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.numIntervals "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.numIntervals (Python parameter) — An Int specifying the number of intervals during the step at which output database states are to be written.")=`20`*, *[timeMarks](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.timeMarks "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.timeMarks (Python parameter) — A Boolean specifying when to write results to the output database.")=`0`*, *[timePoint](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.timePoint "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.timePoint (Python parameter) — A String specifying the name of a time point object.")=`None`*, *[boltLoad](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.boltLoad "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.boltLoad (Python parameter) — A String specifying a bolt load from which output is requested.")=`''`*, *[sectionPoints](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.sectionPoints "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.sectionPoints (Python parameter) — The SymbolicConstant DEFAULT or a sequence of Ints specifying the section points for which output requested.")=`abaqusConstants.DEFAULT`*, *[interactions](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.interactions "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.interactions (Python parameter) — None or a sequence of Strings specifying the interaction names.")=`None`*, *[rebar](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.rebar "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.rebar (Python parameter) — A SymbolicConstant specifying whether output is requested for rebar.")=`abaqusConstants.EXCLUDE`*, *[filter](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.filter "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.filter (Python parameter) — The SymbolicConstant ANTIALIASING or a String specifying the name of an output filter object.")=`None`*, *[directions](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.directions "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.directions (Python parameter) — A Boolean specifying whether to output directions of the local material coordinate system.")=`1`*, *[fasteners](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.fasteners "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.fasteners (Python parameter) — A String specifying the fastener name.")=`''`*, *[assembledFastener](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.assembledFastener "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.assembledFastener (Python parameter) — A String specifying the assembled fastener name.")=`''`*, *[assembledFastenerSet](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.assembledFastenerSet "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.assembledFastenerSet (Python parameter) — A String specifying the set name from the model referenced by the assembled fastener, assembledFastener.")=`''`*, *[exteriorOnly](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.exteriorOnly "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.exteriorOnly (Python parameter) — A Boolean specifying whether the output domain is restricted to the exterior of the model.")=`0`*, *[layupNames](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.layupNames "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.layupNames (Python parameter) — A List of Composite Layer Names.")=`''`*, *[layupLocationMethod](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.layupLocationMethod "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.layupLocationMethod (Python parameter) — A Symbolic constant specifying the method used to indicate the output locations for composite layups.")=`abaqusConstants.SPECIFIED`*, *[outputAtPlyTop](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.outputAtPlyTop "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.outputAtPlyTop (Python parameter) — A Boolean specifying whether to output at the ply top section point.")=`False`*, *[outputAtPlyMid](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.outputAtPlyMid "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.outputAtPlyMid (Python parameter) — A Boolean specifying whether to output at the ply mid section point.")=`True`*, *[outputAtPlyBottom](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.outputAtPlyBottom "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.outputAtPlyBottom (Python parameter) — A Boolean specifying whether to output at the ply bottom section point.")=`False`*, *[position](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.position "abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.position (Python parameter) — A SymbolicConstant specifying the position on an element where output needs to be written.")=`abaqusConstants.INTEGRATION_POINTS`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L48-L201)[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest "Permalink to this definition")
    :   This method creates a FieldOutputRequest object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].FieldOutputRequest
        ```

        Note

        Check [FieldOutputRequest on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldoutputrequestpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest-parameters "Permalink to this headline")
        :   name[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.name "Permalink to this definition")
            :   A String specifying the repository key.

            createStepName[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the object is created.

            region=`abaqusConstants.MODEL`[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.region "Permalink to this definition")
            :   The SymbolicConstant MODEL or a Region object specifying the region from which output is
                requested. The SymbolicConstant MODEL represents the whole model. The default value is
                MODEL.

            variables=`abaqusConstants.PRESELECT`[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.variables "Permalink to this definition")
            :   A sequence of Strings specifying output request variable or component names, or the
                SymbolicConstant PRESELECT or ALL. PRESELECT represents all default output variables for
                the given step. ALL represents all valid output variables. The default value is
                PRESELECT.

            frequency=`1`[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.frequency "Permalink to this definition")
            :   The SymbolicConstant LAST\_INCREMENT or an Int specifying the output frequency in
                increments. The default value is 1.

            modes=`abaqusConstants.ALL`[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.modes "Permalink to this definition")
            :   The SymbolicConstant ALL or a sequence of Ints specifying a list of eigenmodes for which
                output is desired. The default value is ALL.

            timeInterval=`abaqusConstants.EVERY_TIME_INCREMENT`[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.timeInterval "Permalink to this definition")
            :   The SymbolicConstant EVERY\_TIME\_INCREMENT or a Float specifying the time interval at
                which the output states are to be written. The default value is EVERY\_TIME\_INCREMENT.

            numIntervals=`20`[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.numIntervals "Permalink to this definition")
            :   An Int specifying the number of intervals during the step at which output database
                states are to be written. The default value is 20.

            timeMarks=`0`[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.timeMarks "Permalink to this definition")
            :   A Boolean specifying when to write results to the output database. OFF indicates that
                output is written immediately after the time dictated by the specified number of
                intervals. ON indicates that output is written at the exact times dictated by the
                specified number of intervals. The default value is OFF.

            timePoint=`None`[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.timePoint "Permalink to this definition")
            :   A String specifying the name of a time point object. The default value is equal to
                the number of intervals during the step at which output database states are to be
                written. The default value is None.

            boltLoad=`''`[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.boltLoad "Permalink to this definition")
            :   A String specifying a bolt load from which output is requested.

            sectionPoints=`abaqusConstants.DEFAULT`[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.sectionPoints "Permalink to this definition")
            :   The SymbolicConstant DEFAULT or a sequence of Ints specifying the section points for
                which output requested. The default is DEFAULT.

            interactions=`None`[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.interactions "Permalink to this definition")
            :   None or a sequence of Strings specifying the interaction names. The default value is
                None.The sequence can contain only one String.

            rebar=`abaqusConstants.EXCLUDE`[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.rebar "Permalink to this definition")
            :   A SymbolicConstant specifying whether output is requested for rebar. Possible values are
                EXCLUDE, INCLUDE, and ONLY. The default value is EXCLUDE.

            filter=`None`[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.filter "Permalink to this definition")
            :   The SymbolicConstant ANTIALIASING or a String specifying the name of an output filter
                object. The default value is None.

            directions=`1`[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.directions "Permalink to this definition")
            :   A Boolean specifying whether to output directions of the local material coordinate
                system. The default value is ON.

            fasteners=`''`[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.fasteners "Permalink to this definition")
            :   A String specifying the fastener name. The default value is an empty string.

            assembledFastener=`''`[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.assembledFastener "Permalink to this definition")
            :   A String specifying the assembled fastener name. The default value is an empty string.

            assembledFastenerSet=`''`[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.assembledFastenerSet "Permalink to this definition")
            :   A String specifying the set name from the model referenced by the assembled fastener,
                **assembledFastener**. The default value is an empty string.

            exteriorOnly=`0`[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.exteriorOnly "Permalink to this definition")
            :   A Boolean specifying whether the output domain is restricted to the exterior of the
                model. This argument is only valid if **region** = MODEL. The default value is OFF.

            layupNames=`''`[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.layupNames "Permalink to this definition")
            :   A List of Composite Layer Names.

            layupLocationMethod=`abaqusConstants.SPECIFIED`[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.layupLocationMethod "Permalink to this definition")
            :   A Symbolic constant specifying the method used to indicate the output locations for
                composite layups. Possible values are ALL\_LOCATIONS, SPECIFIED and TYPED\_IN. The default
                value is SPECIFIED.

            outputAtPlyTop=`False`[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.outputAtPlyTop "Permalink to this definition")
            :   A Boolean specifying whether to output at the ply top section point. The default value
                is False.

            outputAtPlyMid=`True`[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.outputAtPlyMid "Permalink to this definition")
            :   A Boolean specifying whether to output at the ply mid section point. The default value
                is True.

            outputAtPlyBottom=`False`[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.outputAtPlyBottom "Permalink to this definition")
            :   A Boolean specifying whether to output at the ply bottom section point. The default
                value is False.

            position=`abaqusConstants.INTEGRATION_POINTS`[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest.position "Permalink to this definition")
            :   A SymbolicConstant specifying the position on an element where output needs to be
                written. Possible values are INTEGRATION\_POINTS, AVERAGED\_AT\_NODES, CENTROIDAL, and
                NODES. The default value is INTEGRATION\_POINTS.

        Returns:[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest-returns "Permalink to this headline")
        :   A FieldOutputRequest object.

        Return type:[¶](#abaqus.StepOutput.OutputModel.OutputModel.FieldOutputRequest-return-type "Permalink to this headline")
        :   [`FieldOutputRequest`](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest (Python class) — Bases: object")

    HistoryOutputRequest(*[name](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.name "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.name (Python parameter) — A String specifying the repository key.")*, *[createStepName](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.createStepName "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.createStepName (Python parameter) — A String specifying the name of the step in which the object is created.")*, *[region](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.region "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.region (Python parameter) — The SymbolicConstant MODEL or a Region object specifying the region from which output is requested.")=`abaqusConstants.MODEL`*, *[variables](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.variables "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.variables (Python parameter) — A sequence of Strings specifying output request variable or component names, or the SymbolicConstant PRESELECT or ALL.")=`abaqusConstants.PRESELECT`*, *[frequency](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.frequency "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.frequency (Python parameter) — The SymbolicConstant LAST_INCREMENT or an Int specifying the output frequency in increments.")=`1`*, *[modes](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.modes "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.modes (Python parameter) — The SymbolicConstant ALL or a sequence of Ints specifying a list of eigenmodes for which output is desired.")=`abaqusConstants.ALL`*, *[timeInterval](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.timeInterval "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.timeInterval (Python parameter) — The SymbolicConstant EVERY_TIME_INCREMENT or a Float specifying the time interval at which the output states are to be written.")=`abaqusConstants.EVERY_TIME_INCREMENT`*, *[numIntervals](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.numIntervals "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.numIntervals (Python parameter) — An Int specifying the number of intervals during the step at which output database states are to be written.")=`20`*, *[boltLoad](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.boltLoad "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.boltLoad (Python parameter) — A String specifying a bolt load from which output is requested.")=`''`*, *[sectionPoints](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.sectionPoints "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.sectionPoints (Python parameter) — The SymbolicConstant DEFAULT or a sequence of Ints specifying the section points for which output is requested.")=`abaqusConstants.DEFAULT`*, *[stepName](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.stepName "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.stepName (Python parameter) — A String specifying the name of the step.")=`''`*, *[interactions](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.interactions "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.interactions (Python parameter) — None or a sequence of Strings specifying the interaction names.")=`None`*, *[contourIntegral](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.contourIntegral "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.contourIntegral (Python parameter) — A String specifying the contour integral name.")=`None`*, *[numberOfContours](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.numberOfContours "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.numberOfContours (Python parameter) — An Int specifying the number of contour integrals to output for the contour integral object.")=`0`*, *[stressInitializationStep](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.stressInitializationStep "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.stressInitializationStep (Python parameter) — A String specifying the name of the stress initialization step.")=`None`*, *[contourType](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.contourType "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.contourType (Python parameter) — A SymbolicConstant specifying the type of contour integral.")=`abaqusConstants.J_INTEGRAL`*, *[kFactorDirection](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.kFactorDirection "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.kFactorDirection (Python parameter) — A SymbolicConstant specifying the stress intensity factor direction.")=`abaqusConstants.MTS`*, *[rebar](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.rebar "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.rebar (Python parameter) — A SymbolicConstant specifying whether output is requested for rebar.")=`abaqusConstants.EXCLUDE`*, *[integratedOutputSection](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.integratedOutputSection "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.integratedOutputSection (Python parameter) — A String specifying the integrated output section.")=`''`*, *[springs](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.springs "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.springs (Python parameter) — A sequence of Strings specifying the springs/dashpots names.")=`None`*, *[filter](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.filter "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.filter (Python parameter) — The SymbolicConstant ANTIALIASING or a String specifying the name of an output filter object.")=`None`*, *[fasteners](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.fasteners "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.fasteners (Python parameter) — A String specifying the fastener name.")=`''`*, *[assembledFastener](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.assembledFastener "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.assembledFastener (Python parameter) — A String specifying the assembled fastener name.")=`''`*, *[assembledFastenerSet](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.assembledFastenerSet "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.assembledFastenerSet (Python parameter) — A String specifying the set name from the model referenced by the assembled fastener, assembledFastener.")=`''`*, *[sensor](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.sensor "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.sensor (Python parameter) — A Boolean specifying whether to associate the output request with a sensor definition. The default value is OFF.")=`0`*, *[useGlobal](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.useGlobal "abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.useGlobal (Python parameter) — A Boolean specifying whether to output vector-valued nodal variables in the global directions.")=`True`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L203-L352)[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest "Permalink to this definition")
    :   This method creates a HistoryOutputRequest object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].HistoryOutputRequest
        ```

        Note

        Check [HistoryOutputRequest on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyoutputrequestpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest-parameters "Permalink to this headline")
        :   name[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.name "Permalink to this definition")
            :   A String specifying the repository key.

            createStepName[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.createStepName "Permalink to this definition")
            :   A String specifying the name of the step in which the object is created.

            region=`abaqusConstants.MODEL`[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.region "Permalink to this definition")
            :   The SymbolicConstant MODEL or a Region object specifying the region from which output is
                requested. The SymbolicConstant MODEL represents the whole model. The default value is
                MODEL. If the region is a surface region, the surface must lie within the general contact
                surface domain.

            variables=`abaqusConstants.PRESELECT`[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.variables "Permalink to this definition")
            :   A sequence of Strings specifying output request variable or component names, or the
                SymbolicConstant PRESELECT or ALL. PRESELECT represents all default output variables for
                the given step. ALL represents all valid output variables. The default value is
                PRESELECT.

            frequency=`1`[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.frequency "Permalink to this definition")
            :   The SymbolicConstant LAST\_INCREMENT or an Int specifying the output frequency in
                increments. The default value is 1.

            modes=`abaqusConstants.ALL`[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.modes "Permalink to this definition")
            :   The SymbolicConstant ALL or a sequence of Ints specifying a list of eigenmodes for which
                output is desired. The default value is ALL.

            timeInterval=`abaqusConstants.EVERY_TIME_INCREMENT`[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.timeInterval "Permalink to this definition")
            :   The SymbolicConstant EVERY\_TIME\_INCREMENT or a Float specifying the time interval at
                which the output states are to be written. The default value is EVERY\_TIME\_INCREMENT.

            numIntervals=`20`[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.numIntervals "Permalink to this definition")
            :   An Int specifying the number of intervals during the step at which output database
                states are to be written. The default value is 20.

            boltLoad=`''`[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.boltLoad "Permalink to this definition")
            :   A String specifying a bolt load from which output is requested. The default value is an
                empty string.

            sectionPoints=`abaqusConstants.DEFAULT`[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.sectionPoints "Permalink to this definition")
            :   The SymbolicConstant DEFAULT or a sequence of Ints specifying the section points for
                which output is requested. The default value is DEFAULT.

            stepName=`''`[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.stepName "Permalink to this definition")
            :   A String specifying the name of the step. The default value is an empty string.

            interactions=`None`[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.interactions "Permalink to this definition")
            :   None or a sequence of Strings specifying the interaction names. The default value is
                None.The sequence can contain only one String.

            contourIntegral=`None`[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.contourIntegral "Permalink to this definition")
            :   A String specifying the contour integral name. The default value is None.

            numberOfContours=`0`[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.numberOfContours "Permalink to this definition")
            :   An Int specifying the number of contour integrals to output for the contour integral
                object. The default value is 0.

            stressInitializationStep=`None`[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.stressInitializationStep "Permalink to this definition")
            :   A String specifying the name of the stress initialization step. The default value is
                None.

            contourType=`abaqusConstants.J_INTEGRAL`[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.contourType "Permalink to this definition")
            :   A SymbolicConstant specifying the type of contour integral. Possible values are
                J\_INTEGRAL, C\_INTEGRAL, T\_STRESS, and K\_FACTORS. The default value is J\_INTEGRAL.

            kFactorDirection=`abaqusConstants.MTS`[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.kFactorDirection "Permalink to this definition")
            :   A SymbolicConstant specifying the stress intensity factor direction. Possible values are
                MTS, MERR, and K110. The **kFactorDirection** argument is valid only if
                **contourType** = K\_FACTORS. The default value is MTS.

            rebar=`abaqusConstants.EXCLUDE`[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.rebar "Permalink to this definition")
            :   A SymbolicConstant specifying whether output is requested for rebar. Possible values are
                EXCLUDE, INCLUDE, and ONLY. The default value is EXCLUDE.

            integratedOutputSection=`''`[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.integratedOutputSection "Permalink to this definition")
            :   A String specifying the integrated output section. The default value is an empty string.

            springs=`None`[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.springs "Permalink to this definition")
            :   A sequence of Strings specifying the springs/dashpots names. The default value is None.
                The sequence can contain only one String.

            filter=`None`[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.filter "Permalink to this definition")
            :   The SymbolicConstant ANTIALIASING or a String specifying the name of an output filter
                object. The default value is None.

            fasteners=`''`[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.fasteners "Permalink to this definition")
            :   A String specifying the fastener name. The default value is an empty string.

            assembledFastener=`''`[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.assembledFastener "Permalink to this definition")
            :   A String specifying the assembled fastener name. The default value is an empty string.

            assembledFastenerSet=`''`[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.assembledFastenerSet "Permalink to this definition")
            :   A String specifying the set name from the model referenced by the assembled fastener,
                **assembledFastener**. The default value is an empty string.

            sensor=`0`[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.sensor "Permalink to this definition")
            :   A Boolean specifying whether to associate the output request with a sensor definition.
                The default value is OFF.

            useGlobal=`True`[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest.useGlobal "Permalink to this definition")
            :   A Boolean specifying whether to output vector-valued nodal variables in the global
                directions. The default value is True.

        Returns:[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest-returns "Permalink to this headline")
        :   A HistoryOutputRequest object.

        Return type:[¶](#abaqus.StepOutput.OutputModel.OutputModel.HistoryOutputRequest-return-type "Permalink to this headline")
        :   [`HistoryOutputRequest`](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest (Python class) — Bases: object")

    IntegratedOutputSection(*[name](#abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection.name "abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection.name (Python parameter) — A String specifying the repository key.")*, *[surface](#abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection.surface "abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection.surface (Python parameter) — A Region object specifying the surface over which the output is based.")*, *[refPoint](#abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection.refPoint "abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection.refPoint (Python parameter) — None or a Region object specifying the anchor point about which the integrated moment over the output region is computed or the SymbolicConstant None representing the global origin.")=`None`*, *[refPointAtCenter](#abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection.refPointAtCenter "abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection.refPointAtCenter (Python parameter) — A Boolean specifying that the refPoint be adjusted so that it coincides with the center of the output region in the initial configuration.")=`0`*, *[refPointMotion](#abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection.refPointMotion "abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection.refPointMotion (Python parameter) — A SymbolicConstant specifying how to relate the motion of refPoint to the average motion of the output region.")=`abaqusConstants.INDEPENDENT`*, *[localCsys](#abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection.localCsys "abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system used to express vector output.")=`None`*, *[projectOrientation](#abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection.projectOrientation "abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection.projectOrientation (Python parameter) — A Boolean specifying that the coordinate system be projected onto the surface such that the 1-axis is normal to the surface.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L354-L418)[¶](#abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection "Permalink to this definition")
    :   This method creates an IntegratedOutputSection object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].IntegratedOutputSection
        ```

        Note

        Check [IntegratedOutputSection on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-integratedoutputsectionpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection-parameters "Permalink to this headline")
        :   name[¶](#abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection.name "Permalink to this definition")
            :   A String specifying the repository key.

            surface[¶](#abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection.surface "Permalink to this definition")
            :   A Region object specifying the surface over which the output is based.

            refPoint=`None`[¶](#abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection.refPoint "Permalink to this definition")
            :   None or a Region object specifying the anchor point about which the integrated moment
                over the output region is computed or the SymbolicConstant None representing the global
                origin. The default value is None.

            refPointAtCenter=`0`[¶](#abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection.refPointAtCenter "Permalink to this definition")
            :   A Boolean specifying that the **refPoint** be adjusted so that it coincides with the
                center of the output region in the initial configuration. This argument is valid only
                when you include the **refPoint** argument. The default value is OFF.

            refPointMotion=`abaqusConstants.INDEPENDENT`[¶](#abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection.refPointMotion "Permalink to this definition")
            :   A SymbolicConstant specifying how to relate the motion of **refPoint** to the average
                motion of the output region. A value of INDEPENDENT will allow the **refPoint** to move
                independent of the output region. A value of AVERAGE\_TRANSLATION will set the
                displacement of the **refPoint** equal to the average translation of the output region. A
                value of AVERAGE will set the displacement and rotation of the **refPoint** equal to the
                average translation of the output region. The default value is INDEPENDENT.This argument
                is valid only when you include the **refPoint** argument.

            localCsys=`None`[¶](#abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system used to express vector
                output. If **localCsys** = None, the degrees of freedom are defined in the global coordinate
                system. The default value is None.

            projectOrientation=`0`[¶](#abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection.projectOrientation "Permalink to this definition")
            :   A Boolean specifying that the coordinate system be projected onto the **surface** such
                that the 1-axis is normal to the **surface**. Projection onto a planar **surface** is such
                that the 1-axis is normal to the surface, and a projection onto a nonplanar **surface** is
                such that a least-squares fit surface will be used. The default value is OFF.

        Returns:[¶](#abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection-returns "Permalink to this headline")
        :   An IntegratedOutputSection object.

        Return type:[¶](#abaqus.StepOutput.OutputModel.OutputModel.IntegratedOutputSection-return-type "Permalink to this headline")
        :   [`IntegratedOutputSection`](#abaqus.StepOutput.OutputModel.IntegratedOutputSection "abaqus.StepOutput.OutputModel.IntegratedOutputSection (Python class) — Bases: object")

    TimePoint(*[name](#abaqus.StepOutput.OutputModel.OutputModel.TimePoint.name "abaqus.StepOutput.OutputModel.OutputModel.TimePoint.name (Python parameter) — A String specifying the repository key.")*, *[points](#abaqus.StepOutput.OutputModel.OutputModel.TimePoint.points "abaqus.StepOutput.OutputModel.OutputModel.TimePoint.points (Python parameter) — A sequence of sequences of Floats specifying time points at which data are written to the output database or restart files.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L420-L448)[¶](#abaqus.StepOutput.OutputModel.OutputModel.TimePoint "Permalink to this definition")
    :   This method creates a TimePoint object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].TimePoint
        ```

        Note

        Check [TimePoint on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-timepointpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.StepOutput.OutputModel.OutputModel.TimePoint-parameters "Permalink to this headline")
        :   name[¶](#abaqus.StepOutput.OutputModel.OutputModel.TimePoint.name "Permalink to this definition")
            :   A String specifying the repository key.

            points[¶](#abaqus.StepOutput.OutputModel.OutputModel.TimePoint.points "Permalink to this definition")
            :   A sequence of sequences of Floats specifying time points at which data are written to
                the output database or restart files.

        Returns:[¶](#abaqus.StepOutput.OutputModel.OutputModel.TimePoint-returns "Permalink to this headline")
        :   A TimePoint object.

        Return type:[¶](#abaqus.StepOutput.OutputModel.OutputModel.TimePoint-return-type "Permalink to this headline")
        :   [`TimePoint`](#abaqus.StepOutput.OutputModel.OutputModel.TimePoint "abaqus.StepOutput.OutputModel.OutputModel.TimePoint (Python method) — This method creates a TimePoint object.")

        Raises:[¶](#abaqus.StepOutput.OutputModel.OutputModel.TimePoint-raises "Permalink to this headline")
        :   * **InvalidNameError** –
            * **RangeError** –

## Create DiagnosticPrint, Monitor and Restart information for Step[¶](#create-diagnosticprint-monitor-and-restart-information-for-step "Permalink to this heading")

*class* OutputStep[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputStep.py#L15-L223)[¶](#abaqus.StepOutput.OutputStep.OutputStep "Permalink to this definition")
:   Bases: [`StepBase`](step/index.html#abaqus.Step.StepBase.StepBase "abaqus.Step.StepBase.StepBase (Python class) — Bases: object")

    The Step object stores the parameters that determine the context of the step. The Step object is the
    abstract base type for other Step objects. The Step object has no explicit constructor. The methods and
    members of the Step object are common to all objects derived from the Step.

    Note

    This object can be accessed by:

    ```python
    import step
    mdb.models[name].steps[name]
    ```

    Note

    Check [OutputStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-steppyc.htm?contextscope=all).

    Public Data Attributes:

    Inherited from [`StepBase`](step/index.html#abaqus.Step.StepBase.StepBase "abaqus.Step.StepBase.StepBase (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | [`name`](step/index.html#abaqus.Step.StepBase.StepBase.name "abaqus.Step.StepBase.StepBase.name (Python attribute) — A String specifying the repository key.") | A String specifying the repository key. |
    | [`perturbation`](step/index.html#abaqus.Step.StepBase.StepBase.perturbation "abaqus.Step.StepBase.StepBase.perturbation (Python attribute) — A Boolean specifying whether the step has a perturbation procedure type.") | A Boolean specifying whether the step has a perturbation procedure type. |
    | [`nonmechanical`](step/index.html#abaqus.Step.StepBase.StepBase.nonmechanical "abaqus.Step.StepBase.StepBase.nonmechanical (Python attribute) — A Boolean specifying whether the step has a mechanical procedure type.") | A Boolean specifying whether the step has a mechanical procedure type. |
    | [`suppressed`](step/index.html#abaqus.Step.StepBase.StepBase.suppressed "abaqus.Step.StepBase.StepBase.suppressed (Python attribute) — A Boolean specifying whether the step is suppressed or not. The default value is OFF.") | A Boolean specifying whether the step is suppressed or not. |
    | [`fieldOutputRequestState`](step/index.html#abaqus.Step.StepBase.StepBase.fieldOutputRequestState "abaqus.Step.StepBase.StepBase.fieldOutputRequestState (Python attribute) — A repository of FieldOutputRequestState objects.") | A repository of FieldOutputRequestState objects. |
    | [`historyOutputRequestState`](step/index.html#abaqus.Step.StepBase.StepBase.historyOutputRequestState "abaqus.Step.StepBase.StepBase.historyOutputRequestState (Python attribute) — A repository of HistoryOutputRequestState objects.") | A repository of HistoryOutputRequestState objects. |
    | [`diagnosticPrint`](step/index.html#abaqus.Step.StepBase.StepBase.diagnosticPrint "abaqus.Step.StepBase.StepBase.diagnosticPrint (Python attribute) — A DiagnosticPrint object.") | A DiagnosticPrint object. |
    | [`monitor`](step/index.html#abaqus.Step.StepBase.StepBase.monitor "abaqus.Step.StepBase.StepBase.monitor (Python attribute) — A Monitor object.") | A Monitor object. |
    | [`restart`](step/index.html#abaqus.Step.StepBase.StepBase.restart "abaqus.Step.StepBase.StepBase.restart (Python attribute) — A Restart object.") | A Restart object. |
    | [`adaptiveMeshConstraintStates`](step/index.html#abaqus.Step.StepBase.StepBase.adaptiveMeshConstraintStates "abaqus.Step.StepBase.StepBase.adaptiveMeshConstraintStates (Python attribute) — A repository of AdaptiveMeshConstraintState objects.") | A repository of AdaptiveMeshConstraintState objects. |
    | [`adaptiveMeshDomains`](step/index.html#abaqus.Step.StepBase.StepBase.adaptiveMeshDomains "abaqus.Step.StepBase.StepBase.adaptiveMeshDomains (Python attribute) — A repository of AdaptiveMeshDomain objects.") | A repository of AdaptiveMeshDomain objects. |
    | [`control`](step/index.html#abaqus.Step.StepBase.StepBase.control "abaqus.Step.StepBase.StepBase.control (Python attribute) — A Control object.") | A Control object. |
    | [`solverControl`](step/index.html#abaqus.Step.StepBase.StepBase.solverControl "abaqus.Step.StepBase.StepBase.solverControl (Python attribute) — A SolverControl object.") | A SolverControl object. |
    | [`boundaryConditionStates`](step/index.html#abaqus.Step.StepBase.StepBase.boundaryConditionStates "abaqus.Step.StepBase.StepBase.boundaryConditionStates (Python attribute) — A repository of BoundaryConditionState objects.") | A repository of BoundaryConditionState objects. |
    | [`interactionStates`](step/index.html#abaqus.Step.StepBase.StepBase.interactionStates "abaqus.Step.StepBase.StepBase.interactionStates (Python attribute) — A repository of InteractionState objects.") | A repository of InteractionState objects. |
    | [`loadStates`](step/index.html#abaqus.Step.StepBase.StepBase.loadStates "abaqus.Step.StepBase.StepBase.loadStates (Python attribute) — A repository of LoadState objects.") | A repository of LoadState objects. |
    | [`loadCases`](step/index.html#abaqus.Step.StepBase.StepBase.loadCases "abaqus.Step.StepBase.StepBase.loadCases (Python attribute) — A repository of LoadCase objects.") | A repository of LoadCase objects. |
    | [`predefinedFieldStates`](step/index.html#abaqus.Step.StepBase.StepBase.predefinedFieldStates "abaqus.Step.StepBase.StepBase.predefinedFieldStates (Python attribute) — A repository of PredefinedFieldState objects.") | A repository of PredefinedFieldState objects. |
    | [`activateElements`](step/index.html#abaqus.Step.StepBase.StepBase.activateElements "abaqus.Step.StepBase.StepBase.activateElements (Python attribute) — A repository of ActivateElements objects.") | A repository of ActivateElements objects. |
    | [`explicit`](step/index.html#abaqus.Step.StepBase.StepBase.explicit "abaqus.Step.StepBase.StepBase.explicit (Python attribute) — A SymbolicConstant specifying whether the step has an explicit procedure type (procedureType = ANNEAL, DYNAMIC_EXPLICIT, or DYNAMIC_TEMP_DISPLACEMENT).") | A SymbolicConstant specifying whether the step has an explicit procedure type (*procedureType* = ANNEAL, DYNAMIC\_EXPLICIT, or DYNAMIC\_TEMP\_DISPLACEMENT). |
    | [`procedureType`](step/index.html#abaqus.Step.StepBase.StepBase.procedureType "abaqus.Step.StepBase.StepBase.procedureType (Python attribute) — A SymbolicConstant specifying the Abaqus procedure. Possible values are:") | A SymbolicConstant specifying the Abaqus procedure. |

    Public Methods:

    |  |  |
    | --- | --- |
    | [`DiagnosticPrint`](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint "abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint (Python method) — This method creates a DiagnosticPrint object.")([allke, criticalElement, ...]) | This method creates a DiagnosticPrint object. |
    | [`Monitor`](#abaqus.StepOutput.OutputStep.OutputStep.Monitor "abaqus.StepOutput.OutputStep.OutputStep.Monitor (Python method) — This method creates a request for a degree of freedom to be monitored in a general or modal procedure.")(node, dof, frequency) | This method creates a request for a degree of freedom to be monitored in a general or modal procedure. |
    | [`Restart`](#abaqus.StepOutput.OutputStep.OutputStep.Restart "abaqus.StepOutput.OutputStep.OutputStep.Restart (Python method) — This method creates a restart request.")([numberIntervals, timeMarks, ...]) | This method creates a restart request. |

    Inherited from [`StepBase`](step/index.html#abaqus.Step.StepBase.StepBase "abaqus.Step.StepBase.StepBase (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | [`resume`](step/index.html#abaqus.Step.StepBase.StepBase.resume "abaqus.Step.StepBase.StepBase.resume (Python method) — This method resumes the step that was previously suppressed.")() | This method resumes the step that was previously suppressed. |
    | [`suppress`](step/index.html#abaqus.Step.StepBase.StepBase.suppress "abaqus.Step.StepBase.StepBase.suppress (Python method) — This method suppresses the step.")() | This method suppresses the step. |

    ---

    Member Details:

    DiagnosticPrint(*[allke](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.allke "abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.allke (Python parameter) — A Boolean specifying a request for a column containing the total kinetic energy.")=`1`*, *[criticalElement](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.criticalElement "abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.criticalElement (Python parameter) — A Boolean specifying a request for a column containing the element that has the smallest stable time increment and a column listing the value.")=`1`*, *[dmass](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.dmass "abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.dmass (Python parameter) — A Boolean specifying a request for a column containing the percent change in total mass of the model as a result of mass scaling.")=`0`*, *[etotal](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.etotal "abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.etotal (Python parameter) — A Boolean specifying a request for a column containing the energy balance of the model. This argument is valid only for an Abaqus/Explicit analysis.")=`0`*, *[contact](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.contact "abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.contact (Python parameter) — A Boolean specifying a request for detailed output of points that are contacting or separating in interface and gap problems.")=`1`*, *[modelChange](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.modelChange "abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.modelChange (Python parameter) — A Boolean specifying a request for detailed output of which elements are being removed or reactivated in the step.")=`0`*, *[plasticity](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.plasticity "abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.plasticity (Python parameter) — A Boolean specifying a request for detailed output of element and integration point numbers for which the plasticity algorithms have failed to converge in the material routines.")=`0`*, *[residual](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.residual "abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.residual (Python parameter) — A Boolean specifying a request for output of equilibrium residuals during the equilibrium iterations.")=`1`*, *[frequency](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.frequency "abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.frequency (Python parameter) — An Int specifying the frequency of output, in increments.")=`1`*, *[solve](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.solve "abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.solve (Python parameter) — A Boolean specifying a request for information regarding the actual number of equations and the wavefront in each iteration.")=`1`*, *[mass](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.mass "abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.mass (Python parameter) — A Boolean specifying a request for a column containing the total mass of the model as a result of mass scaling.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputStep.py#L28-L113)[¶](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint "Permalink to this definition")
    :   This method creates a DiagnosticPrint object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].steps[name].DiagnosticPrint
        ```

        Note

        Check [DiagnosticPrint on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-diagnosticprintpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint-parameters "Permalink to this headline")
        :   allke=`1`[¶](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.allke "Permalink to this definition")
            :   A Boolean specifying a request for a column containing the total kinetic energy. This
                argument is valid only for an Abaqus/Explicit analysis. The default value is ON.

            criticalElement=`1`[¶](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.criticalElement "Permalink to this definition")
            :   A Boolean specifying a request for a column containing the element that has the smallest
                stable time increment and a column listing the value. This argument is valid only for an
                Abaqus/Explicit analysis. The default value is ON.

            dmass=`0`[¶](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.dmass "Permalink to this definition")
            :   A Boolean specifying a request for a column containing the percent change in total mass
                of the model as a result of mass scaling. This argument is valid only for an
                Abaqus/Explicit analysis. The default value is OFF unless mass scaling is present in the
                model.

            etotal=`0`[¶](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.etotal "Permalink to this definition")
            :   A Boolean specifying a request for a column containing the energy balance of the model.
                This argument is valid only for an Abaqus/Explicit analysis. The default value is OFF.

            contact=`1`[¶](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.contact "Permalink to this definition")
            :   A Boolean specifying a request for detailed output of points that are contacting or
                separating in interface and gap problems. This argument is valid only for an
                Abaqus/Standard analysis. The default value is ON.

            modelChange=`0`[¶](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.modelChange "Permalink to this definition")
            :   A Boolean specifying a request for detailed output of which elements are being removed
                or reactivated in the step. This argument is valid only for an Abaqus/Standard analysis.
                The default value is OFF.

            plasticity=`0`[¶](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.plasticity "Permalink to this definition")
            :   A Boolean specifying a request for detailed output of element and integration point
                numbers for which the plasticity algorithms have failed to converge in the material
                routines. This argument is valid only for an Abaqus/Standard analysis. The default value
                is OFF.

            residual=`1`[¶](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.residual "Permalink to this definition")
            :   A Boolean specifying a request for output of equilibrium residuals during the
                equilibrium iterations. This argument is valid only for an Abaqus/Standard analysis. The
                default value is ON.

            frequency=`1`[¶](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.frequency "Permalink to this definition")
            :   An Int specifying the frequency of output, in increments. The default value is 1.

            solve=`1`[¶](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.solve "Permalink to this definition")
            :   A Boolean specifying a request for information regarding the actual number of equations
                and the wavefront in each iteration. This argument is valid only for an Abaqus/Standard
                analysis. The default value is ON.

            mass=`0`[¶](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint.mass "Permalink to this definition")
            :   A Boolean specifying a request for a column containing the total mass of the model as a
                result of mass scaling. This argument is valid only for an Abaqus/Explicit analysis. The
                default value is OFF.

        Returns:[¶](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint-returns "Permalink to this headline")
        :   **diagnosticPrint** – A DiagnosticPrint object

        Return type:[¶](#abaqus.StepOutput.OutputStep.OutputStep.DiagnosticPrint-return-type "Permalink to this headline")
        :   [`DiagnosticPrint`](#abaqus.StepOutput.OutputStep.DiagnosticPrint "abaqus.StepOutput.OutputStep.DiagnosticPrint (Python class) — Bases: object")

    Monitor(*[node](#abaqus.StepOutput.OutputStep.OutputStep.Monitor.node "abaqus.StepOutput.OutputStep.OutputStep.Monitor.node (Python parameter) — A String specifying the name of the region to be monitored.")*, *[dof](#abaqus.StepOutput.OutputStep.OutputStep.Monitor.dof "abaqus.StepOutput.OutputStep.OutputStep.Monitor.dof (Python parameter) — A SymbolicConstant specifying the degree of freedom to be monitored at the node. Possible values are:")*, *[frequency](#abaqus.StepOutput.OutputStep.OutputStep.Monitor.frequency "abaqus.StepOutput.OutputStep.OutputStep.Monitor.frequency (Python parameter) — An Int specifying the output frequency in increments.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputStep.py#L115-L179)[¶](#abaqus.StepOutput.OutputStep.OutputStep.Monitor "Permalink to this definition")
    :   This method creates a request for a degree of freedom to be monitored in a general or modal
        procedure.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].steps[name].Monitor
        ```

        Note

        Check [Monitor on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-monitorpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.StepOutput.OutputStep.OutputStep.Monitor-parameters "Permalink to this headline")
        :   node[¶](#abaqus.StepOutput.OutputStep.OutputStep.Monitor.node "Permalink to this definition")
            :   A String specifying the name of the region to be monitored.

            dof[¶](#abaqus.StepOutput.OutputStep.OutputStep.Monitor.dof "Permalink to this definition")
            :   A SymbolicConstant specifying the degree of freedom to be monitored at the node.
                Possible values are:

                * U1
                * U2
                * U3
                * UR1
                * UR2
                * UR3
                * WARP
                * FLUID\_PRESSURE
                * ELECTRICAL\_POTENTIAL
                * NT11
                * NT30
                * NN11
                * NN30

                The NT identifiers are not available for mass diffusion. The NN identifiers are
                available only for mass diffusion.

            frequency[¶](#abaqus.StepOutput.OutputStep.OutputStep.Monitor.frequency "Permalink to this definition")
            :   An Int specifying the output frequency in increments. This argument is valid only for an
                Abaqus/Standard analysis.

        Returns:[¶](#abaqus.StepOutput.OutputStep.OutputStep.Monitor-returns "Permalink to this headline")
        :   **monitor** – A Monitor object

        Return type:[¶](#abaqus.StepOutput.OutputStep.OutputStep.Monitor-return-type "Permalink to this headline")
        :   [`Monitor`](#abaqus.StepOutput.OutputStep.Monitor "abaqus.StepOutput.OutputStep.Monitor (Python class) — Bases: object")

    Restart(*[numberIntervals](#abaqus.StepOutput.OutputStep.OutputStep.Restart.numberIntervals "abaqus.StepOutput.OutputStep.OutputStep.Restart.numberIntervals (Python parameter) — An Int specifying the number of intervals during the step at which restart information will be written.")=`0`*, *[timeMarks](#abaqus.StepOutput.OutputStep.OutputStep.Restart.timeMarks "abaqus.StepOutput.OutputStep.OutputStep.Restart.timeMarks (Python parameter) — A Boolean specifying whether to use exact time marks for writing during an analysis.")=`0`*, *[overlay](#abaqus.StepOutput.OutputStep.OutputStep.Restart.overlay "abaqus.StepOutput.OutputStep.OutputStep.Restart.overlay (Python parameter) — A Boolean specifying that only one increment per step should be retained on the restart file, thus minimizing the size of the restart file.")=`0`*, *[frequency](#abaqus.StepOutput.OutputStep.OutputStep.Restart.frequency "abaqus.StepOutput.OutputStep.OutputStep.Restart.frequency (Python parameter) — An Int specifying the increments at which restart information will be written.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputStep.py#L181-L223)[¶](#abaqus.StepOutput.OutputStep.OutputStep.Restart "Permalink to this definition")
    :   This method creates a restart request.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].steps[name].Restart
        ```

        Note

        Check [Restart on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-restartpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.StepOutput.OutputStep.OutputStep.Restart-parameters "Permalink to this headline")
        :   numberIntervals=`0`[¶](#abaqus.StepOutput.OutputStep.OutputStep.Restart.numberIntervals "Permalink to this definition")
            :   An Int specifying the number of intervals during the step at which restart information
                will be written. The default value is 0. The default value is 1.

            timeMarks=`0`[¶](#abaqus.StepOutput.OutputStep.OutputStep.Restart.timeMarks "Permalink to this definition")
            :   A Boolean specifying whether to use exact time marks for writing during an analysis. The
                default value is OFF. The default value is OFF.

            overlay=`0`[¶](#abaqus.StepOutput.OutputStep.OutputStep.Restart.overlay "Permalink to this definition")
            :   A Boolean specifying that only one increment per step should be retained on the restart
                file, thus minimizing the size of the restart file. The default value is OFF. The
                default value is ON.

            frequency=`0`[¶](#abaqus.StepOutput.OutputStep.OutputStep.Restart.frequency "Permalink to this definition")
            :   An Int specifying the increments at which restart information will be written. The
                default value is 0. The default value is 0.This argument applies only to Abaqus/Standard
                analyses.

        Returns:[¶](#abaqus.StepOutput.OutputStep.OutputStep.Restart-returns "Permalink to this headline")
        :   **restart** – A Restart object

        Return type:[¶](#abaqus.StepOutput.OutputStep.OutputStep.Restart-return-type "Permalink to this headline")
        :   [`Restart`](#abaqus.StepOutput.OutputStep.OutputStep.Restart "abaqus.StepOutput.OutputStep.OutputStep.Restart (Python method) — This method creates a restart request.")

        Raises:[¶](#abaqus.StepOutput.OutputStep.OutputStep.Restart-raises "Permalink to this headline")
        :   **RangeError** –

## Other Classes[¶](#other-classes "Permalink to this heading")

*class* DiagnosticPrint(*[allke](#abaqus.StepOutput.OutputStep.DiagnosticPrint "abaqus.StepOutput.OutputStep.DiagnosticPrint.__init__.allke (Python parameter)")=`1`*, *[criticalElement](#abaqus.StepOutput.OutputStep.DiagnosticPrint "abaqus.StepOutput.OutputStep.DiagnosticPrint.__init__.criticalElement (Python parameter)")=`1`*, *[dmass](#abaqus.StepOutput.OutputStep.DiagnosticPrint "abaqus.StepOutput.OutputStep.DiagnosticPrint.__init__.dmass (Python parameter)")=`0`*, *[etotal](#abaqus.StepOutput.OutputStep.DiagnosticPrint "abaqus.StepOutput.OutputStep.DiagnosticPrint.__init__.etotal (Python parameter)")=`0`*, *[contact](#abaqus.StepOutput.OutputStep.DiagnosticPrint "abaqus.StepOutput.OutputStep.DiagnosticPrint.__init__.contact (Python parameter)")=`1`*, *[modelChange](#abaqus.StepOutput.OutputStep.DiagnosticPrint "abaqus.StepOutput.OutputStep.DiagnosticPrint.__init__.modelChange (Python parameter)")=`0`*, *[plasticity](#abaqus.StepOutput.OutputStep.DiagnosticPrint "abaqus.StepOutput.OutputStep.DiagnosticPrint.__init__.plasticity (Python parameter)")=`0`*, *[residual](#abaqus.StepOutput.OutputStep.DiagnosticPrint "abaqus.StepOutput.OutputStep.DiagnosticPrint.__init__.residual (Python parameter)")=`1`*, *[frequency](#abaqus.StepOutput.OutputStep.DiagnosticPrint "abaqus.StepOutput.OutputStep.DiagnosticPrint.__init__.frequency (Python parameter)")=`1`*, *[solve](#abaqus.StepOutput.OutputStep.DiagnosticPrint "abaqus.StepOutput.OutputStep.DiagnosticPrint.__init__.solve (Python parameter)")=`1`*, *[mass](#abaqus.StepOutput.OutputStep.DiagnosticPrint "abaqus.StepOutput.OutputStep.DiagnosticPrint.__init__.mass (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputStep.py#L8-L153)[¶](#abaqus.StepOutput.OutputStep.DiagnosticPrint "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The DiagnosticPrint object is used to request detailed diagnostic output or to disable specific
    diagnostic checks.

    Note

    This object can be accessed by:

    ```python
    import step
    mdb.models[name].steps[name].diagnosticPrint
    ```

    The corresponding analysis keywords are:

    * DIAGNOSTICS

    Note

    Check [DiagnosticPrint on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-diagnosticprintpyc.htm?contextscope=all).

    Member Details:

    allke : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputStep.py#L24-L26)[¶](#abaqus.StepOutput.OutputStep.DiagnosticPrint.allke "Permalink to this definition")
    :   A Boolean specifying a request for a column containing the total kinetic energy. This
        argument is valid only for an Abaqus/Explicit analysis. The default value is ON.

    contact : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputStep.py#L43-L46)[¶](#abaqus.StepOutput.OutputStep.DiagnosticPrint.contact "Permalink to this definition")
    :   A Boolean specifying a request for detailed output of points that are contacting or
        separating in interface and gap problems. This argument is valid only for an
        Abaqus/Standard analysis. The default value is ON.

    criticalElement : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputStep.py#L28-L31)[¶](#abaqus.StepOutput.OutputStep.DiagnosticPrint.criticalElement "Permalink to this definition")
    :   A Boolean specifying a request for a column containing the element that has the smallest
        stable time increment and a column listing the value. This argument is valid only for an
        Abaqus/Explicit analysis. The default value is ON.

    dmass : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputStep.py#L33-L37)[¶](#abaqus.StepOutput.OutputStep.DiagnosticPrint.dmass "Permalink to this definition")
    :   A Boolean specifying a request for a column containing the percent change in total mass
        of the model as a result of mass scaling. This argument is valid only for an
        Abaqus/Explicit analysis. The default value is OFF unless mass scaling is present in the
        model.

    etotal : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputStep.py#L39-L41)[¶](#abaqus.StepOutput.OutputStep.DiagnosticPrint.etotal "Permalink to this definition")
    :   A Boolean specifying a request for a column containing the energy balance of the model.
        This argument is valid only for an Abaqus/Explicit analysis. The default value is OFF.

    frequency : --is-rst--:py:class:`int` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputStep.py#L64-L65)[¶](#abaqus.StepOutput.OutputStep.DiagnosticPrint.frequency "Permalink to this definition")
    :   An Int specifying the frequency of output, in increments. The default value is 1.

    mass : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputStep.py#L71-L74)[¶](#abaqus.StepOutput.OutputStep.DiagnosticPrint.mass "Permalink to this definition")
    :   A Boolean specifying a request for a column containing the total mass of the model as a
        result of mass scaling. This argument is valid only for an Abaqus/Explicit analysis. The
        default value is OFF.

    modelChange : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputStep.py#L48-L51)[¶](#abaqus.StepOutput.OutputStep.DiagnosticPrint.modelChange "Permalink to this definition")
    :   A Boolean specifying a request for detailed output of which elements are being removed
        or reactivated in the step. This argument is valid only for an Abaqus/Standard analysis.
        The default value is OFF.

    plasticity : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputStep.py#L53-L57)[¶](#abaqus.StepOutput.OutputStep.DiagnosticPrint.plasticity "Permalink to this definition")
    :   A Boolean specifying a request for detailed output of element and integration point
        numbers for which the plasticity algorithms have failed to converge in the material
        routines. This argument is valid only for an Abaqus/Standard analysis. The default value
        is OFF.

    residual : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputStep.py#L59-L62)[¶](#abaqus.StepOutput.OutputStep.DiagnosticPrint.residual "Permalink to this definition")
    :   A Boolean specifying a request for output of equilibrium residuals during the
        equilibrium iterations. This argument is valid only for an Abaqus/Standard analysis. The
        default value is ON.

    setValues(*\*[args](#abaqus.StepOutput.OutputStep.DiagnosticPrint.setValues "abaqus.StepOutput.OutputStep.DiagnosticPrint.setValues.args (Python parameter)")*, *\*\*[kwargs](#abaqus.StepOutput.OutputStep.DiagnosticPrint.setValues "abaqus.StepOutput.OutputStep.DiagnosticPrint.setValues.kwargs (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputStep.py#L150-L153)[¶](#abaqus.StepOutput.OutputStep.DiagnosticPrint.setValues "Permalink to this definition")
    :   This method modifies the DiagnosticPrint object.

*class* FieldOutputRequest(*[name](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.name (Python parameter)")*, *[createStepName](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.createStepName (Python parameter)")*, *[region](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.region (Python parameter)")=`abaqusConstants.MODEL`*, *[variables](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.variables (Python parameter)")=`abaqusConstants.PRESELECT`*, *[frequency](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.frequency (Python parameter)")=`1`*, *[modes](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.modes (Python parameter)")=`abaqusConstants.ALL`*, *[timeInterval](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.timeInterval (Python parameter)")=`abaqusConstants.EVERY_TIME_INCREMENT`*, *[numIntervals](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.numIntervals (Python parameter)")=`20`*, *[timeMarks](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.timeMarks (Python parameter)")=`0`*, *[timePoint](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.timePoint (Python parameter)")=`None`*, *[boltLoad](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.boltLoad (Python parameter)")=`''`*, *[sectionPoints](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.sectionPoints (Python parameter)")=`abaqusConstants.DEFAULT`*, *[interactions](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.interactions (Python parameter)")=`None`*, *[rebar](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.rebar (Python parameter)")=`abaqusConstants.EXCLUDE`*, *[filter](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.filter (Python parameter)")=`None`*, *[directions](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.directions (Python parameter)")=`1`*, *[fasteners](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.fasteners (Python parameter)")=`''`*, *[assembledFastener](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.assembledFastener (Python parameter)")=`''`*, *[assembledFastenerSet](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.assembledFastenerSet (Python parameter)")=`''`*, *[exteriorOnly](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.exteriorOnly (Python parameter)")=`0`*, *[layupNames](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.layupNames (Python parameter)")=`''`*, *[layupLocationMethod](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.layupLocationMethod (Python parameter)")=`abaqusConstants.SPECIFIED`*, *[outputAtPlyTop](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.outputAtPlyTop (Python parameter)")=`False`*, *[outputAtPlyMid](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.outputAtPlyMid (Python parameter)")=`True`*, *[outputAtPlyBottom](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.outputAtPlyBottom (Python parameter)")=`False`*, *[position](#abaqus.StepOutput.OutputModel.FieldOutputRequest "abaqus.StepOutput.OutputModel.FieldOutputRequest.__init__.position (Python parameter)")=`abaqusConstants.INTEGRATION_POINTS`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L26-L388)[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The FieldOutputRequest object defines a field output request.

    Note

    This object can be accessed by:

    ```python
    import step
    mdb.models[name].fieldOutputRequests[name]
    ```

    The corresponding analysis keywords are:

    * CONTACT OUTPUT
    * ELEMENT OUTPUT
    * ENERGY OUTPUT
    * CONTACT OUTPUT
    * ELEMENT OUTPUT
    * ENERGY OUTPUT
    * MODAL OUTPUT
    * CONTACT OUTPUT
    * ELEMENT OUTPUT
    * OUTPUT
    * RADIATION OUTPUT

    Note

    Check [FieldOutputRequest on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldoutputrequestpyc.htm?contextscope=all).

    Member Details:

    boltLoad : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L51-L52)[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.boltLoad "Permalink to this definition")
    :   A String specifying a bolt load from which output is requested.

    deactivate(*[stepName](#abaqus.StepOutput.OutputModel.FieldOutputRequest.deactivate.stepName "abaqus.StepOutput.OutputModel.FieldOutputRequest.deactivate.stepName (Python parameter) — A String specifying the name of the step in which the field output request is deactivated.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L185-L195)[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.deactivate "Permalink to this definition")
    :   This method deactivates the field output request in the specified step and all its subsequent steps.

        Note

        Check [FieldOutputRequest.deactivate on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldoutputrequestpyc.htm?contextscope=all#simaker-fieldoutputrequestdeactivatepyc).

        Parameters:[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.deactivate-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.deactivate.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the field output request is
                deactivated.

    interactions : --is-rst--:py:data:`~typing.Optional`\[:py:class:`tuple`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L59-L61)[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.interactions "Permalink to this definition")
    :   None or a tuple of Strings specifying the interaction names. The default value is
        None.The sequence can contain only one String.

    move(*[fromStepName](#abaqus.StepOutput.OutputModel.FieldOutputRequest.move.fromStepName "abaqus.StepOutput.OutputModel.FieldOutputRequest.move.fromStepName (Python parameter) — A String specifying the name of the step from which the field output request state is moved.")*, *[toStepName](#abaqus.StepOutput.OutputModel.FieldOutputRequest.move.toStepName "abaqus.StepOutput.OutputModel.FieldOutputRequest.move.toStepName (Python parameter) — A String specifying the name of the step to which the field output request state is moved.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L197-L210)[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.move "Permalink to this definition")
    :   This method moves the field output request state object from one step to a different step.

        Note

        Check [FieldOutputRequest.move on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldoutputrequestpyc.htm?contextscope=all#simaker-fieldoutputrequestmovepyc).

        Parameters:[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.move-parameters "Permalink to this headline")
        :   fromStepName[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.move.fromStepName "Permalink to this definition")
            :   A String specifying the name of the step from which the field output request state is
                moved.

            toStepName[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.move.toStepName "Permalink to this definition")
            :   A String specifying the name of the step to which the field output request state is
                moved.

    region : --is-rst--:py:data:`~typing.Union`\[:py:data:`~typing.Literal`\[``MODEL``], :py:class:`~abaqus.Region.Region.Region`] = `'MODEL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L54-L57)[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.region "Permalink to this definition")
    :   The SymbolicConstant MODEL or a Region object specifying the region from which output is
        requested. The SymbolicConstant MODEL represents the whole model. The default value is
        MODEL.

    reset(*[stepName](#abaqus.StepOutput.OutputModel.FieldOutputRequest.reset.stepName "abaqus.StepOutput.OutputModel.FieldOutputRequest.reset.stepName (Python parameter) — A String specifying the name of the step in which the field output request state is reset.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L212-L223)[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.reset "Permalink to this definition")
    :   This method resets the field output request state of the specified step to the state of the previous
        step.

        Note

        Check [FieldOutputRequest.reset on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldoutputrequestpyc.htm?contextscope=all#simaker-fieldoutputrequestresetpyc).

        Parameters:[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.reset-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.reset.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the field output request state is
                reset.

    resume()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L225-L228)[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.resume "Permalink to this definition")
    :   This method resumes the field output request that was previously suppressed.

    setValues(*[region](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.region "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.region (Python parameter) — The SymbolicConstant MODEL or a Region object specifying the region from which output is requested.")=`abaqusConstants.MODEL`*, *[variables](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.variables "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.variables (Python parameter) — A sequence of Strings specifying output request variable or component names, or the SymbolicConstant PRESELECT or ALL.")=`abaqusConstants.PRESELECT`*, *[frequency](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.frequency "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.frequency (Python parameter) — The SymbolicConstant LAST_INCREMENT or an Int specifying the output frequency in increments.")=`1`*, *[modes](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.modes "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.modes (Python parameter) — The SymbolicConstant ALL or a sequence of Ints specifying a list of eigenmodes for which output is desired.")=`abaqusConstants.ALL`*, *[timeInterval](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.timeInterval "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.timeInterval (Python parameter) — The SymbolicConstant EVERY_TIME_INCREMENT or a Float specifying the time interval at which the output states are to be written.")=`abaqusConstants.EVERY_TIME_INCREMENT`*, *[numIntervals](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.numIntervals "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.numIntervals (Python parameter) — An Int specifying the number of intervals during the step at which output database states are to be written.")=`20`*, *[timeMarks](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.timeMarks "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.timeMarks (Python parameter) — A Boolean specifying when to write results to the output database.")=`0`*, *[boltLoad](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.boltLoad "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.boltLoad (Python parameter) — A String specifying a bolt load from which output is requested.")=`''`*, *[sectionPoints](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.sectionPoints "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.sectionPoints (Python parameter) — The SymbolicConstant DEFAULT or a sequence of Ints specifying the section points for which output requested.")=`abaqusConstants.DEFAULT`*, *[interactions](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.interactions "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.interactions (Python parameter) — None or a sequence of Strings specifying the interaction names.")=`None`*, *[rebar](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.rebar "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.rebar (Python parameter) — A SymbolicConstant specifying whether output is requested for rebar.")=`abaqusConstants.EXCLUDE`*, *[filter](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.filter "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.filter (Python parameter) — The SymbolicConstant ANTIALIASING or a String specifying the name of an output filter object.")=`None`*, *[directions](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.directions "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.directions (Python parameter) — A Boolean specifying whether to output directions of the local material coordinate system.")=`1`*, *[fasteners](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.fasteners "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.fasteners (Python parameter) — A String specifying the fastener name.")=`''`*, *[assembledFastener](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.assembledFastener "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.assembledFastener (Python parameter) — A String specifying the assembled fastener name.")=`''`*, *[assembledFastenerSet](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.assembledFastenerSet "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.assembledFastenerSet (Python parameter) — A String specifying the set name from the model referenced by the assembled fastener, assembledFastener.")=`''`*, *[exteriorOnly](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.exteriorOnly "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.exteriorOnly (Python parameter) — A Boolean specifying whether the output domain is restricted to the exterior of the model.")=`0`*, *[layupNames](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.layupNames "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.layupNames (Python parameter) — A List of Composite Layer Names.")=`''`*, *[layupLocationMethod](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.layupLocationMethod "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.layupLocationMethod (Python parameter) — A Symbolic constant specifying the method used to indicate the output locations for composite layups.")=`abaqusConstants.SPECIFIED`*, *[outputAtPlyTop](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.outputAtPlyTop "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.outputAtPlyTop (Python parameter) — A Boolean specifying whether to output at the ply top section point.")=`False`*, *[outputAtPlyMid](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.outputAtPlyMid "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.outputAtPlyMid (Python parameter) — A Boolean specifying whether to output at the ply mid section point.")=`True`*, *[outputAtPlyBottom](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.outputAtPlyBottom "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.outputAtPlyBottom (Python parameter) — A Boolean specifying whether to output at the ply bottom section point.")=`False`*, *[position](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.position "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.position (Python parameter) — A SymbolicConstant specifying the position on an element where output needs to be written.")=`abaqusConstants.INTEGRATION_POINTS`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L235-L340)[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues "Permalink to this definition")
    :   This method modifies the data for an existing FieldOutputRequest object in the step where it is
        created.

        Note

        Check [FieldOutputRequest.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldoutputrequestpyc.htm?contextscope=all#simaker-fieldoutputrequestsetvaluespyc).

        Parameters:[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues-parameters "Permalink to this headline")
        :   region=`abaqusConstants.MODEL`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.region "Permalink to this definition")
            :   The SymbolicConstant MODEL or a Region object specifying the region from which output is
                requested. The SymbolicConstant MODEL represents the whole model. The default value is
                MODEL.

            variables=`abaqusConstants.PRESELECT`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.variables "Permalink to this definition")
            :   A sequence of Strings specifying output request variable or component names, or the
                SymbolicConstant PRESELECT or ALL. PRESELECT represents all default output variables for
                the given step. ALL represents all valid output variables. The default value is
                PRESELECT.

            frequency=`1`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.frequency "Permalink to this definition")
            :   The SymbolicConstant LAST\_INCREMENT or an Int specifying the output frequency in
                increments. The default value is 1.

            modes=`abaqusConstants.ALL`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.modes "Permalink to this definition")
            :   The SymbolicConstant ALL or a sequence of Ints specifying a list of eigenmodes for which
                output is desired. The default value is ALL.

            timeInterval=`abaqusConstants.EVERY_TIME_INCREMENT`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.timeInterval "Permalink to this definition")
            :   The SymbolicConstant EVERY\_TIME\_INCREMENT or a Float specifying the time interval at
                which the output states are to be written. The default value is EVERY\_TIME\_INCREMENT.

            numIntervals=`20`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.numIntervals "Permalink to this definition")
            :   An Int specifying the number of intervals during the step at which output database
                states are to be written. The default value is 20.

            timeMarks=`0`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.timeMarks "Permalink to this definition")
            :   A Boolean specifying when to write results to the output database. OFF indicates that
                output is written immediately after the time dictated by the specified number of
                intervals. ON indicates that output is written at the exact times dictated by the
                specified number of intervals. The default value is OFF.

            boltLoad=`''`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.boltLoad "Permalink to this definition")
            :   A String specifying a bolt load from which output is requested.

            sectionPoints=`abaqusConstants.DEFAULT`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.sectionPoints "Permalink to this definition")
            :   The SymbolicConstant DEFAULT or a sequence of Ints specifying the section points for
                which output requested. The default is DEFAULT.

            interactions=`None`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.interactions "Permalink to this definition")
            :   None or a sequence of Strings specifying the interaction names. The default value is
                None.The sequence can contain only one String.

            rebar=`abaqusConstants.EXCLUDE`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.rebar "Permalink to this definition")
            :   A SymbolicConstant specifying whether output is requested for rebar. Possible values are
                EXCLUDE, INCLUDE, and ONLY. The default value is EXCLUDE.

            filter=`None`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.filter "Permalink to this definition")
            :   The SymbolicConstant ANTIALIASING or a String specifying the name of an output filter
                object. The default value is None.

            directions=`1`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.directions "Permalink to this definition")
            :   A Boolean specifying whether to output directions of the local material coordinate
                system. The default value is ON.

            fasteners=`''`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.fasteners "Permalink to this definition")
            :   A String specifying the fastener name. The default value is an empty string.

            assembledFastener=`''`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.assembledFastener "Permalink to this definition")
            :   A String specifying the assembled fastener name. The default value is an empty string.

            assembledFastenerSet=`''`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.assembledFastenerSet "Permalink to this definition")
            :   A String specifying the set name from the model referenced by the assembled fastener,
                **assembledFastener**. The default value is an empty string.

            exteriorOnly=`0`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.exteriorOnly "Permalink to this definition")
            :   A Boolean specifying whether the output domain is restricted to the exterior of the
                model. This argument is only valid if **region** = MODEL. The default value is OFF.

            layupNames=`''`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.layupNames "Permalink to this definition")
            :   A List of Composite Layer Names.

            layupLocationMethod=`abaqusConstants.SPECIFIED`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.layupLocationMethod "Permalink to this definition")
            :   A Symbolic constant specifying the method used to indicate the output locations for
                composite layups. Possible values are ALL\_LOCATIONS, SPECIFIED and TYPED\_IN. The default
                value is SPECIFIED.

            outputAtPlyTop=`False`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.outputAtPlyTop "Permalink to this definition")
            :   A Boolean specifying whether to output at the ply top section point. The default value
                is False.

            outputAtPlyMid=`True`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.outputAtPlyMid "Permalink to this definition")
            :   A Boolean specifying whether to output at the ply mid section point. The default value
                is True.

            outputAtPlyBottom=`False`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.outputAtPlyBottom "Permalink to this definition")
            :   A Boolean specifying whether to output at the ply bottom section point. The default
                value is False.

            position=`abaqusConstants.INTEGRATION_POINTS`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValues.position "Permalink to this definition")
            :   A SymbolicConstant specifying the position on an element where output needs to be
                written. Possible values are INTEGRATION\_POINTS, AVERAGED\_AT\_NODES, CENTROIDAL, and
                NODES. The default value is INTEGRATION\_POINTS.

    setValuesInStep(*[stepName](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep.stepName "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the field output request is modified.")*, *[variables](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep.variables "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep.variables (Python parameter) — A sequence of Strings specifying output request variable or component names, or the SymbolicConstant PRESELECT or ALL.")=`None`*, *[frequency](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep.frequency "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep.frequency (Python parameter) — The SymbolicConstant LAST_INCREMENT or an Int specifying the output frequency in increments.")=`1`*, *[modes](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep.modes "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep.modes (Python parameter) — The SymbolicConstant ALL or a sequence of Ints specifying a list of eigenmodes for which output is desired.")=`abaqusConstants.ALL`*, *[timeInterval](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep.timeInterval "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep.timeInterval (Python parameter) — The SymbolicConstant EVERY_TIME_INCREMENT or a Float specifying the time interval at which the output states are to be written.")=`abaqusConstants.EVERY_TIME_INCREMENT`*, *[numIntervals](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep.numIntervals "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep.numIntervals (Python parameter) — An Int equal to the number of intervals during the step at which output database states are to be written.")=`20`*, *[timePoint](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep.timePoint "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep.timePoint (Python parameter) — A String specifying the name of a time point object.")=`None`*, *[timeMarks](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep.timeMarks "abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep.timeMarks (Python parameter) — A Boolean specifying when to write results to the output database.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L342-L388)[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing FieldOutputRequest object in the specified
        step.

        Note

        Check [FieldOutputRequest.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldoutputrequestpyc.htm?contextscope=all#simaker-fieldoutputrequestsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the field output request is modified.

            variables=`None`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep.variables "Permalink to this definition")
            :   A sequence of Strings specifying output request variable or component names, or the
                SymbolicConstant PRESELECT or ALL. PRESELECT represents all default output variables for
                the given step. ALL represents all valid output variables.

            frequency=`1`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep.frequency "Permalink to this definition")
            :   The SymbolicConstant LAST\_INCREMENT or an Int specifying the output frequency in
                increments. The default value is 1.

            modes=`abaqusConstants.ALL`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep.modes "Permalink to this definition")
            :   The SymbolicConstant ALL or a sequence of Ints specifying a list of eigenmodes for which
                output is desired. The default value is ALL.

            timeInterval=`abaqusConstants.EVERY_TIME_INCREMENT`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep.timeInterval "Permalink to this definition")
            :   The SymbolicConstant EVERY\_TIME\_INCREMENT or a Float specifying the time interval at
                which the output states are to be written. The default value is EVERY\_TIME\_INCREMENT.

            numIntervals=`20`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep.numIntervals "Permalink to this definition")
            :   An Int equal to the number of intervals during the step at which output database states
                are to be written. The default value is 20.

            timePoint=`None`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep.timePoint "Permalink to this definition")
            :   A String specifying the name of a time point object. The default value is equal to the
                number of intervals during the step at which output database states are to be written.
                The default value is None.

                Changed in version 2022: The argument `timePoints` was renamed to `timePoint`.

            timeMarks=`0`[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.setValuesInStep.timeMarks "Permalink to this definition")
            :   A Boolean specifying when to write results to the output database. The default value is
                OFF.

    suppress()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L230-L233)[¶](#abaqus.StepOutput.OutputModel.FieldOutputRequest.suppress "Permalink to this definition")
    :   This method suppresses the field output request.

*class* FieldOutputRequestState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/FieldOutputRequestState.py#L16-L96)[¶](#abaqus.StepOutput.FieldOutputRequestState.FieldOutputRequestState "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The FieldOutputRequestState object stores the propagating data of a field output request current in a
    step. One instance of this object is created internally by the FieldOutputRequest object for each step. The
    instance is also deleted internally by the FieldOutputRequest object. The FieldOutputRequestState object has
    no constructor or methods.

    Note

    This object can be accessed by:

    ```python
    import step
    mdb.models[name].steps[name].fieldOutputRequestState[name]
    ```

    Note

    Check [FieldOutputRequestState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldoutputrequeststatepyc.htm?contextscope=all).

    Member Details:

    frequency : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` | :py:class:`int` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/FieldOutputRequestState.py#L34-L36)[¶](#abaqus.StepOutput.FieldOutputRequestState.FieldOutputRequestState.frequency "Permalink to this definition")
    :   The SymbolicConstant LAST\_INCREMENT or an Int specifying the output frequency in
        increments. The default value is 1.

    frequencyState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/FieldOutputRequestState.py)[¶](#abaqus.StepOutput.FieldOutputRequestState.FieldOutputRequestState.frequencyState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the field output request
        frequency. Possible values are UNSET, SET, and UNCHANGED.

    frequencyType : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/FieldOutputRequestState.py#L16-L96)[¶](#abaqus.StepOutput.FieldOutputRequestState.FieldOutputRequestState.frequencyType "Permalink to this definition")
    :   A String specifying a read-only SymbolicConstant describing which type of frequency of
        output is used. Possible values areFREQUENCY, NUMBER\_INTERVALS, TIME\_INTERVAL,
        TIME\_POINT and MODES. The default value depends on the procedure. The default value is
        an empty string.

    modes : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'ALL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/FieldOutputRequestState.py#L84-L86)[¶](#abaqus.StepOutput.FieldOutputRequestState.FieldOutputRequestState.modes "Permalink to this definition")
    :   The SymbolicConstant ALL or a tuple of Ints specifying a list of eigenmodes for which
        output is desired. The default value is ALL.

    modesState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/FieldOutputRequestState.py)[¶](#abaqus.StepOutput.FieldOutputRequestState.FieldOutputRequestState.modesState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the field output request modes.
        Possible values are UNSET, SET, and UNCHANGED.

    numIntervals : --is-rst--:py:class:`int` = `20`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/FieldOutputRequestState.py#L54-L56)[¶](#abaqus.StepOutput.FieldOutputRequestState.FieldOutputRequestState.numIntervals "Permalink to this definition")
    :   An Int specifying the number of intervals during the step at which output database
        states are to be written. The default value is 20.

    numIntervalsState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/FieldOutputRequestState.py)[¶](#abaqus.StepOutput.FieldOutputRequestState.FieldOutputRequestState.numIntervalsState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the field output request.
        Possible values are UNSET, SET, and UNCHANGED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/FieldOutputRequestState.py)[¶](#abaqus.StepOutput.FieldOutputRequestState.FieldOutputRequestState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the FieldOutputRequestState
        object. Possible values are NOT\_YET\_ACTIVE, CREATED, PROPAGATED, MODIFIED, DEACTIVATED,
        NO\_LONGER\_ACTIVE, TYPE\_NOT\_APPLICABLE, and INSTANCE\_NOT\_APPLICABLE.

    timeInterval : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`, :py:class:`float`] = `'EVERY_TIME_INCREMENT'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/FieldOutputRequestState.py#L46-L48)[¶](#abaqus.StepOutput.FieldOutputRequestState.FieldOutputRequestState.timeInterval "Permalink to this definition")
    :   The SymbolicConstant EVERY\_TIME\_INCREMENT or a Float specifying the time interval at
        which the output states are to be written. The default value is EVERY\_TIME\_INCREMENT.

    timeIntervalState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/FieldOutputRequestState.py)[¶](#abaqus.StepOutput.FieldOutputRequestState.FieldOutputRequestState.timeIntervalState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the field output request time
        interval. Possible values are UNSET, SET, and UNCHANGED.

    timeMarks : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/FieldOutputRequestState.py#L62-L64)[¶](#abaqus.StepOutput.FieldOutputRequestState.FieldOutputRequestState.timeMarks "Permalink to this definition")
    :   A Boolean specifying when to write results to the output database. The default value is
        OFF.

    timeMarksState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/FieldOutputRequestState.py)[¶](#abaqus.StepOutput.FieldOutputRequestState.FieldOutputRequestState.timeMarksState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the field output request.
        Possible values are UNSET, SET, and UNCHANGED.

    timePoint : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/FieldOutputRequestState.py#L88-L90)[¶](#abaqus.StepOutput.FieldOutputRequestState.FieldOutputRequestState.timePoint "Permalink to this definition")
    :   A String specifying the name of a time point object used to determine which output
        database states are to be written. The default value is an empty string.

    timePointState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/FieldOutputRequestState.py)[¶](#abaqus.StepOutput.FieldOutputRequestState.FieldOutputRequestState.timePointState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the field output request.
        Possible values are UNSET, SET, and UNCHANGED.

    variables : --is-rst--:py:class:`tuple`\[:py:class:`str`, :py:data:`...<Ellipsis>`] | :py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/FieldOutputRequestState.py#L79-L82)[¶](#abaqus.StepOutput.FieldOutputRequestState.FieldOutputRequestState.variables "Permalink to this definition")
    :   A tuple of Strings specifying output request variable or component names, or the
        SymbolicConstant PRESELECT or ALL. PRESELECT represents all default output variables for
        the given step. ALL represents all valid output variables.

    variablesState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/FieldOutputRequestState.py)[¶](#abaqus.StepOutput.FieldOutputRequestState.FieldOutputRequestState.variablesState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the field output request
        variables. Possible values are UNSET, SET, and UNCHANGED.

*class* HistoryOutputRequest(*[name](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.name (Python parameter)")*, *[createStepName](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.createStepName (Python parameter)")*, *[region](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.region (Python parameter)")=`abaqusConstants.MODEL`*, *[variables](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.variables (Python parameter)")=`abaqusConstants.PRESELECT`*, *[frequency](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.frequency (Python parameter)")=`1`*, *[modes](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.modes (Python parameter)")=`abaqusConstants.ALL`*, *[timeInterval](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.timeInterval (Python parameter)")=`abaqusConstants.EVERY_TIME_INCREMENT`*, *[numIntervals](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.numIntervals (Python parameter)")=`20`*, *[boltLoad](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.boltLoad (Python parameter)")=`''`*, *[sectionPoints](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.sectionPoints (Python parameter)")=`abaqusConstants.DEFAULT`*, *[stepName](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.stepName (Python parameter)")=`''`*, *[interactions](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.interactions (Python parameter)")=`None`*, *[contourIntegral](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.contourIntegral (Python parameter)")=`None`*, *[numberOfContours](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.numberOfContours (Python parameter)")=`0`*, *[stressInitializationStep](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.stressInitializationStep (Python parameter)")=`None`*, *[contourType](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.contourType (Python parameter)")=`abaqusConstants.J_INTEGRAL`*, *[kFactorDirection](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.kFactorDirection (Python parameter)")=`abaqusConstants.MTS`*, *[rebar](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.rebar (Python parameter)")=`abaqusConstants.EXCLUDE`*, *[integratedOutputSection](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.integratedOutputSection (Python parameter)")=`''`*, *[springs](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.springs (Python parameter)")=`None`*, *[filter](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.filter (Python parameter)")=`None`*, *[fasteners](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.fasteners (Python parameter)")=`''`*, *[assembledFastener](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.assembledFastener (Python parameter)")=`''`*, *[assembledFastenerSet](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.assembledFastenerSet (Python parameter)")=`''`*, *[sensor](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.sensor (Python parameter)")=`0`*, *[useGlobal](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "abaqus.StepOutput.OutputModel.HistoryOutputRequest.__init__.useGlobal (Python parameter)")=`True`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L25-L384)[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The HistoryOutputRequest object defines a history output request.

    Note

    This object can be accessed by:

    ```python
    import step
    mdb.models[name].historyOutputRequests[name]
    ```

    The corresponding analysis keywords are:

    * CONTACT OUTPUT
    * ELEMENT OUTPUT
    * ENERGY OUTPUT
    * CONTACT OUTPUT
    * ELEMENT OUTPUT
    * ENERGY OUTPUT
    * MODAL OUTPUT
    * CONTACT OUTPUT
    * ELEMENT OUTPUT
    * OUTPUT
    * RADIATION OUTPUT

    Note

    Check [HistoryOutputRequest on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyoutputrequestpyc.htm?contextscope=all).

    Member Details:

    boltLoad : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L50-L52)[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.boltLoad "Permalink to this definition")
    :   A String specifying a bolt load from which output is requested. The default value is an
        empty string.

    deactivate(*[stepName](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.deactivate.stepName "abaqus.StepOutput.OutputModel.HistoryOutputRequest.deactivate.stepName (Python parameter) — A String specifying the name of the step in which the history output request is deactivated.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L186-L196)[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.deactivate "Permalink to this definition")
    :   This method deactivates the history output request in the specified step and all subsequent steps.

        Note

        Check [HistoryOutputRequest.deactivate on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyoutputrequestpyc.htm?contextscope=all#simaker-historyoutputrequestdeactivatepyc).

        Parameters:[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.deactivate-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.deactivate.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the history output request is
                deactivated.

    interactions : --is-rst--:py:data:`~typing.Optional`\[:py:class:`tuple`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L64-L66)[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.interactions "Permalink to this definition")
    :   None or a tuple of Strings specifying the interaction names. The default value is
        None.The sequence can contain only one String.

    move(*[fromStepName](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.move.fromStepName "abaqus.StepOutput.OutputModel.HistoryOutputRequest.move.fromStepName (Python parameter) — A String specifying the name of the step from which the history output request state is moved.")*, *[toStepName](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.move.toStepName "abaqus.StepOutput.OutputModel.HistoryOutputRequest.move.toStepName (Python parameter) — A String specifying the name of the step to which the history output request state is moved.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L198-L211)[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.move "Permalink to this definition")
    :   This method moves the history output request state object from one step to a different step.

        Note

        Check [HistoryOutputRequest.move on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyoutputrequestpyc.htm?contextscope=all#simaker-historyoutputrequestmovepyc).

        Parameters:[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.move-parameters "Permalink to this headline")
        :   fromStepName[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.move.fromStepName "Permalink to this definition")
            :   A String specifying the name of the step from which the history output request state is
                moved.

            toStepName[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.move.toStepName "Permalink to this definition")
            :   A String specifying the name of the step to which the history output request state is
                moved.

    region : --is-rst--:py:data:`~typing.Union`\[:py:data:`~typing.Literal`\[``MODEL``], :py:class:`~abaqus.Region.Region.Region`] = `'MODEL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L54-L58)[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.region "Permalink to this definition")
    :   The SymbolicConstant MODEL or a Region object specifying the region from which output is
        requested. The SymbolicConstant MODEL represents the whole model. The default value is
        MODEL.If the region is a surface region, the surface must lie within the general contact
        surface domain.

    reset(*[stepName](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.reset.stepName "abaqus.StepOutput.OutputModel.HistoryOutputRequest.reset.stepName (Python parameter) — A String specifying the name of the step in which the history output request state is reset.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L213-L224)[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.reset "Permalink to this definition")
    :   This method resets the history output request state of the specified step to the state of the
        previous step.

        Note

        Check [HistoryOutputRequest.reset on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyoutputrequestpyc.htm?contextscope=all#simaker-historyoutputrequestresetpyc).

        Parameters:[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.reset-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.reset.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the history output request state is
                reset.

    resume()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L226-L229)[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.resume "Permalink to this definition")
    :   This method resumes the history output request that was previously suppressed.

    sectionPoints : --is-rst--:py:data:`~typing.Union`\[:py:data:`~typing.Literal`\[``DEFAULT``], :py:class:`~typing.Sequence`\[:py:class:`int`]] = `'DEFAULT'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L60-L62)[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.sectionPoints "Permalink to this definition")
    :   The SymbolicConstant DEFAULT or a tuple of Ints specifying the section points for which
        output is requested. The default value is DEFAULT.

    setValues(*[region](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.region "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.region (Python parameter) — The SymbolicConstant MODEL or a Region object specifying the region from which output is requested.")=`abaqusConstants.MODEL`*, *[variables](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.variables "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.variables (Python parameter) — A sequence of Strings specifying output request variable or component names, or the SymbolicConstant PRESELECT or ALL.")=`abaqusConstants.PRESELECT`*, *[frequency](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.frequency "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.frequency (Python parameter) — The SymbolicConstant LAST_INCREMENT or an Int specifying the output frequency in increments.")=`1`*, *[modes](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.modes "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.modes (Python parameter) — The SymbolicConstant ALL or a sequence of Ints specifying a list of eigenmodes for which output is desired.")=`abaqusConstants.ALL`*, *[timeInterval](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.timeInterval "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.timeInterval (Python parameter) — The SymbolicConstant EVERY_TIME_INCREMENT or a Float specifying the time interval at which the output states are to be written.")=`abaqusConstants.EVERY_TIME_INCREMENT`*, *[numIntervals](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.numIntervals "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.numIntervals (Python parameter) — An Int specifying the number of intervals during the step at which output database states are to be written.")=`20`*, *[boltLoad](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.boltLoad "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.boltLoad (Python parameter) — A String specifying a bolt load from which output is requested.")=`''`*, *[sectionPoints](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.sectionPoints "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.sectionPoints (Python parameter) — The SymbolicConstant DEFAULT or a sequence of Ints specifying the section points for which output is requested.")=`abaqusConstants.DEFAULT`*, *[stepName](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.stepName "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.stepName (Python parameter) — A String specifying the name of the step.")=`''`*, *[interactions](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.interactions "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.interactions (Python parameter) — None or a sequence of Strings specifying the interaction names.")=`None`*, *[contourIntegral](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.contourIntegral "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.contourIntegral (Python parameter) — A String specifying the contour integral name.")=`None`*, *[numberOfContours](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.numberOfContours "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.numberOfContours (Python parameter) — An Int specifying the number of contour integrals to output for the contour integral object.")=`0`*, *[stressInitializationStep](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.stressInitializationStep "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.stressInitializationStep (Python parameter) — A String specifying the name of the stress initialization step.")=`None`*, *[contourType](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.contourType "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.contourType (Python parameter) — A SymbolicConstant specifying the type of contour integral.")=`abaqusConstants.J_INTEGRAL`*, *[kFactorDirection](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.kFactorDirection "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.kFactorDirection (Python parameter) — A SymbolicConstant specifying the stress intensity factor direction.")=`abaqusConstants.MTS`*, *[rebar](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.rebar "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.rebar (Python parameter) — A SymbolicConstant specifying whether output is requested for rebar.")=`abaqusConstants.EXCLUDE`*, *[integratedOutputSection](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.integratedOutputSection "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.integratedOutputSection (Python parameter) — A String specifying the integrated output section.")=`''`*, *[springs](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.springs "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.springs (Python parameter) — A sequence of Strings specifying the springs/dashpots names.")=`None`*, *[filter](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.filter "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.filter (Python parameter) — The SymbolicConstant ANTIALIASING or a String specifying the name of an output filter object.")=`None`*, *[fasteners](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.fasteners "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.fasteners (Python parameter) — A String specifying the fastener name.")=`''`*, *[assembledFastener](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.assembledFastener "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.assembledFastener (Python parameter) — A String specifying the assembled fastener name.")=`''`*, *[assembledFastenerSet](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.assembledFastenerSet "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.assembledFastenerSet (Python parameter) — A String specifying the set name from the model referenced by the assembled fastener, assembledFastener.")=`''`*, *[sensor](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.sensor "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.sensor (Python parameter) — A Boolean specifying whether to associate the output request with a sensor definition. The default value is OFF.")=`0`*, *[useGlobal](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.useGlobal "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.useGlobal (Python parameter) — A Boolean specifying whether to output vector-valued nodal variables in the global directions.")=`True`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L236-L342)[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues "Permalink to this definition")
    :   This method modifies the data for an existing HistoryOutputRequest object in the step where it is
        created.

        Note

        Check [HistoryOutputRequest.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyoutputrequestpyc.htm?contextscope=all#simaker-historyoutputrequestsetvaluespyc).

        Parameters:[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues-parameters "Permalink to this headline")
        :   region=`abaqusConstants.MODEL`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.region "Permalink to this definition")
            :   The SymbolicConstant MODEL or a Region object specifying the region from which output is
                requested. The SymbolicConstant MODEL represents the whole model. The default value is
                MODEL.If the region is a surface region, the surface must lie within the general contact
                surface domain.

            variables=`abaqusConstants.PRESELECT`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.variables "Permalink to this definition")
            :   A sequence of Strings specifying output request variable or component names, or the
                SymbolicConstant PRESELECT or ALL. PRESELECT represents all default output variables for
                the given step. ALL represents all valid output variables. The default value is
                PRESELECT.

            frequency=`1`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.frequency "Permalink to this definition")
            :   The SymbolicConstant LAST\_INCREMENT or an Int specifying the output frequency in
                increments. The default value is 1.

            modes=`abaqusConstants.ALL`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.modes "Permalink to this definition")
            :   The SymbolicConstant ALL or a sequence of Ints specifying a list of eigenmodes for which
                output is desired. The default value is ALL.

            timeInterval=`abaqusConstants.EVERY_TIME_INCREMENT`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.timeInterval "Permalink to this definition")
            :   The SymbolicConstant EVERY\_TIME\_INCREMENT or a Float specifying the time interval at
                which the output states are to be written. The default value is EVERY\_TIME\_INCREMENT.

            numIntervals=`20`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.numIntervals "Permalink to this definition")
            :   An Int specifying the number of intervals during the step at which output database
                states are to be written. The default value is 20.

            boltLoad=`''`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.boltLoad "Permalink to this definition")
            :   A String specifying a bolt load from which output is requested. The default value is an
                empty string.

            sectionPoints=`abaqusConstants.DEFAULT`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.sectionPoints "Permalink to this definition")
            :   The SymbolicConstant DEFAULT or a sequence of Ints specifying the section points for
                which output is requested. The default value is DEFAULT.

            stepName=`''`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.stepName "Permalink to this definition")
            :   A String specifying the name of the step. The default value is an empty string.

            interactions=`None`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.interactions "Permalink to this definition")
            :   None or a sequence of Strings specifying the interaction names. The default value is
                None.The sequence can contain only one String.

            contourIntegral=`None`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.contourIntegral "Permalink to this definition")
            :   A String specifying the contour integral name. The default value is None.

            numberOfContours=`0`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.numberOfContours "Permalink to this definition")
            :   An Int specifying the number of contour integrals to output for the contour integral
                object. The default value is 0.

            stressInitializationStep=`None`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.stressInitializationStep "Permalink to this definition")
            :   A String specifying the name of the stress initialization step. The default value is
                None.

            contourType=`abaqusConstants.J_INTEGRAL`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.contourType "Permalink to this definition")
            :   A SymbolicConstant specifying the type of contour integral. Possible values are
                J\_INTEGRAL, C\_INTEGRAL, T\_STRESS, and K\_FACTORS. The default value is J\_INTEGRAL.

            kFactorDirection=`abaqusConstants.MTS`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.kFactorDirection "Permalink to this definition")
            :   A SymbolicConstant specifying the stress intensity factor direction. Possible values are
                MTS, MERR, and K110. The **kFactorDirection** argument is valid only if
                **contourType** = K\_FACTORS. The default value is MTS.

            rebar=`abaqusConstants.EXCLUDE`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.rebar "Permalink to this definition")
            :   A SymbolicConstant specifying whether output is requested for rebar. Possible values are
                EXCLUDE, INCLUDE, and ONLY. The default value is EXCLUDE.

            integratedOutputSection=`''`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.integratedOutputSection "Permalink to this definition")
            :   A String specifying the integrated output section. The default value is an empty string.

            springs=`None`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.springs "Permalink to this definition")
            :   A sequence of Strings specifying the springs/dashpots names. The default value is None.
                The sequence can contain only one String.

            filter=`None`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.filter "Permalink to this definition")
            :   The SymbolicConstant ANTIALIASING or a String specifying the name of an output filter
                object. The default value is None.

            fasteners=`''`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.fasteners "Permalink to this definition")
            :   A String specifying the fastener name. The default value is an empty string.

            assembledFastener=`''`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.assembledFastener "Permalink to this definition")
            :   A String specifying the assembled fastener name. The default value is an empty string.

            assembledFastenerSet=`''`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.assembledFastenerSet "Permalink to this definition")
            :   A String specifying the set name from the model referenced by the assembled fastener,
                **assembledFastener**. The default value is an empty string.

            sensor=`0`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.sensor "Permalink to this definition")
            :   A Boolean specifying whether to associate the output request with a sensor definition.
                The default value is OFF.

            useGlobal=`True`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValues.useGlobal "Permalink to this definition")
            :   A Boolean specifying whether to output vector-valued nodal variables in the global
                directions. The default value is True.

    setValuesInStep(*[stepName](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValuesInStep.stepName "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValuesInStep.stepName (Python parameter) — A String specifying the name of the step in which the history output request is modified.")*, *[variables](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValuesInStep.variables "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValuesInStep.variables (Python parameter) — A sequence of Strings specifying output request variable or component names or the SymbolicConstant PRESELECT or ALL.")=`Ellipsis`*, *[frequency](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValuesInStep.frequency "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValuesInStep.frequency (Python parameter) — The SymbolicConstant LAST_INCREMENT or an Int specifying the output frequency in increments.")=`1`*, *[modes](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValuesInStep.modes "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValuesInStep.modes (Python parameter) — The SymbolicConstant ALL or a sequence of Ints specifying a list of eigenmodes for which output is desired.")=`abaqusConstants.ALL`*, *[timeInterval](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValuesInStep.timeInterval "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValuesInStep.timeInterval (Python parameter) — The SymbolicConstant EVERY_TIME_INCREMENT or a Float specifying the time interval at which the output states are to be written.")=`abaqusConstants.EVERY_TIME_INCREMENT`*, *[numIntervals](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValuesInStep.numIntervals "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValuesInStep.numIntervals (Python parameter) — An Int specifying the number of intervals during the step at which output database states are to be written.")=`20`*, *[timePoints](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValuesInStep.timePoints "abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValuesInStep.timePoints (Python parameter) — A String specifying the name of a time point object.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L344-L384)[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValuesInStep "Permalink to this definition")
    :   This method modifies the propagating data for an existing HistoryOutputRequest object in the
        specified step.

        Note

        Check [HistoryOutputRequest.setValuesInStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyoutputrequestpyc.htm?contextscope=all#simaker-historyoutputrequestsetvaluesinsteppyc).

        Parameters:[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValuesInStep-parameters "Permalink to this headline")
        :   stepName[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValuesInStep.stepName "Permalink to this definition")
            :   A String specifying the name of the step in which the history output request is
                modified.

            variables=`Ellipsis`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValuesInStep.variables "Permalink to this definition")
            :   A sequence of Strings specifying output request variable or component names or the
                SymbolicConstant PRESELECT or ALL. PRESELECT represents all default output variables for
                the given step. ALL represents all valid output variables.

            frequency=`1`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValuesInStep.frequency "Permalink to this definition")
            :   The SymbolicConstant LAST\_INCREMENT or an Int specifying the output frequency in
                increments. The default value is 1.

            modes=`abaqusConstants.ALL`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValuesInStep.modes "Permalink to this definition")
            :   The SymbolicConstant ALL or a sequence of Ints specifying a list of eigenmodes for which
                output is desired. The default value is ALL.

            timeInterval=`abaqusConstants.EVERY_TIME_INCREMENT`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValuesInStep.timeInterval "Permalink to this definition")
            :   The SymbolicConstant EVERY\_TIME\_INCREMENT or a Float specifying the time interval at
                which the output states are to be written. The default value is EVERY\_TIME\_INCREMENT.

            numIntervals=`20`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValuesInStep.numIntervals "Permalink to this definition")
            :   An Int specifying the number of intervals during the step at which output database
                states are to be written. The default value is 20.

            timePoints=`None`[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.setValuesInStep.timePoints "Permalink to this definition")
            :   A String specifying the name of a time point object. The default value is equal to the
                number of intervals during the step at which output database states are to be written.
                The default value is None.

    suppress()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L231-L234)[¶](#abaqus.StepOutput.OutputModel.HistoryOutputRequest.suppress "Permalink to this definition")
    :   This method suppresses the history output request.

*class* HistoryOutputRequestState[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/HistoryOutputRequestState.py#L10-L83)[¶](#abaqus.StepOutput.HistoryOutputRequestState.HistoryOutputRequestState "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The HistoryOutputRequestState object stores the propagating data of a History output request current in a
    step. One instance of this object is created internally by the HistoryOutputRequest object for each step.
    The instance is also deleted internally by the HistoryOutputRequest object. The HistoryOutputRequestState
    object has no constructor or methods.

    Note

    This object can be accessed by:

    ```python
    import step
    mdb.models[name].steps[name].historyOutputRequestState[name]
    ```

    Note

    Check [HistoryOutputRequestState on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyoutputrequeststatepyc.htm?contextscope=all).

    Member Details:

    frequency : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` | :py:class:`int` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/HistoryOutputRequestState.py#L28-L30)[¶](#abaqus.StepOutput.HistoryOutputRequestState.HistoryOutputRequestState.frequency "Permalink to this definition")
    :   The SymbolicConstant LAST\_INCREMENT or an Int specifying the output frequency in
        increments. The default value is 1.

    frequencyState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/HistoryOutputRequestState.py)[¶](#abaqus.StepOutput.HistoryOutputRequestState.HistoryOutputRequestState.frequencyState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the history output request
        frequency. Possible values are UNSET, SET, and UNCHANGED.

    frequencyType : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/HistoryOutputRequestState.py#L10-L83)[¶](#abaqus.StepOutput.HistoryOutputRequestState.HistoryOutputRequestState.frequencyType "Permalink to this definition")
    :   A String specifying a read-only SymbolicConstant describing which type of frequency of
        output is used. Possible values areFREQUENCY, NUMBER\_INTERVALS, TIME\_INTERVAL,
        TIME\_POINT and MODES. The default value depends on the procedure. The default value is
        an empty string.

    modes : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'ALL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/HistoryOutputRequestState.py#L70-L72)[¶](#abaqus.StepOutput.HistoryOutputRequestState.HistoryOutputRequestState.modes "Permalink to this definition")
    :   The SymbolicConstant ALL or a tuple of Ints specifying a list of eigenmodes for which
        output is desired. The default value is ALL.

    modesState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/HistoryOutputRequestState.py)[¶](#abaqus.StepOutput.HistoryOutputRequestState.HistoryOutputRequestState.modesState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the history output request modes.
        Possible values are UNSET, SET, and UNCHANGED.

    numIntervals : --is-rst--:py:class:`int` = `20`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/HistoryOutputRequestState.py#L48-L50)[¶](#abaqus.StepOutput.HistoryOutputRequestState.HistoryOutputRequestState.numIntervals "Permalink to this definition")
    :   An Int specifying the number of intervals during the step at which output database
        states are to be written. The default value is 20.

    numIntervalsState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/HistoryOutputRequestState.py)[¶](#abaqus.StepOutput.HistoryOutputRequestState.HistoryOutputRequestState.numIntervalsState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the history output request.
        Possible values are UNSET, SET, and UNCHANGED.

    status : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/HistoryOutputRequestState.py)[¶](#abaqus.StepOutput.HistoryOutputRequestState.HistoryOutputRequestState.status "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the HistoryOutputRequestState
        object. Possible values are NOT\_YET\_ACTIVE, CREATED, PROPAGATED, MODIFIED, DEACTIVATED,
        NO\_LONGER\_ACTIVE, TYPE\_NOT\_APPLICABLE, and INSTANCE\_NOT\_APPLICABLE.

    timeInterval : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`, :py:class:`float`] = `'EVERY_TIME_INCREMENT'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/HistoryOutputRequestState.py#L40-L42)[¶](#abaqus.StepOutput.HistoryOutputRequestState.HistoryOutputRequestState.timeInterval "Permalink to this definition")
    :   The SymbolicConstant EVERY\_TIME\_INCREMENT or a Float specifying the time interval at
        which the output states are to be written. The default value is EVERY\_TIME\_INCREMENT.

    timeIntervalState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/HistoryOutputRequestState.py)[¶](#abaqus.StepOutput.HistoryOutputRequestState.HistoryOutputRequestState.timeIntervalState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the history output request time
        interval. Possible values are UNSET, SET, and UNCHANGED.

    timePoint : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/HistoryOutputRequestState.py#L74-L77)[¶](#abaqus.StepOutput.HistoryOutputRequestState.HistoryOutputRequestState.timePoint "Permalink to this definition")
    :   A String specifying the name of a time point object used to determine at which points in
        the time period data is written to the output database. The default value is an empty
        string.

    timePointState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/HistoryOutputRequestState.py)[¶](#abaqus.StepOutput.HistoryOutputRequestState.HistoryOutputRequestState.timePointState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the history output request.
        Possible values are UNSET, SET, and UNCHANGED.

    variables : --is-rst--:py:class:`tuple`\[:py:class:`str`, :py:data:`...<Ellipsis>`] | :py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/HistoryOutputRequestState.py#L65-L68)[¶](#abaqus.StepOutput.HistoryOutputRequestState.HistoryOutputRequestState.variables "Permalink to this definition")
    :   A tuple of Strings specifying output request variable or component names, or the
        SymbolicConstant PRESELECT or ALL. PRESELECT represents all default output variables for
        the given step. ALL represents all valid output variables.

    variablesState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/HistoryOutputRequestState.py)[¶](#abaqus.StepOutput.HistoryOutputRequestState.HistoryOutputRequestState.variablesState "Permalink to this definition")
    :   A SymbolicConstant specifying the propagation state of the history output request
        variables. Possible values are UNSET, SET, and UNCHANGED.

*class* IntegratedOutputSection(*[name](#abaqus.StepOutput.OutputModel.IntegratedOutputSection "abaqus.StepOutput.OutputModel.IntegratedOutputSection.__init__.name (Python parameter)")*, *[surface](#abaqus.StepOutput.OutputModel.IntegratedOutputSection "abaqus.StepOutput.OutputModel.IntegratedOutputSection.__init__.surface (Python parameter)")*, *[refPoint](#abaqus.StepOutput.OutputModel.IntegratedOutputSection "abaqus.StepOutput.OutputModel.IntegratedOutputSection.__init__.refPoint (Python parameter)")=`None`*, *[refPointAtCenter](#abaqus.StepOutput.OutputModel.IntegratedOutputSection "abaqus.StepOutput.OutputModel.IntegratedOutputSection.__init__.refPointAtCenter (Python parameter)")=`0`*, *[refPointMotion](#abaqus.StepOutput.OutputModel.IntegratedOutputSection "abaqus.StepOutput.OutputModel.IntegratedOutputSection.__init__.refPointMotion (Python parameter)")=`abaqusConstants.INDEPENDENT`*, *[localCsys](#abaqus.StepOutput.OutputModel.IntegratedOutputSection "abaqus.StepOutput.OutputModel.IntegratedOutputSection.__init__.localCsys (Python parameter)")=`None`*, *[projectOrientation](#abaqus.StepOutput.OutputModel.IntegratedOutputSection "abaqus.StepOutput.OutputModel.IntegratedOutputSection.__init__.projectOrientation (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L12-L158)[¶](#abaqus.StepOutput.OutputModel.IntegratedOutputSection "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The IntegratedOutputSection object specifies parameters used for integrated output.

    Note

    This object can be accessed by:

    ```python
    import step
    mdb.models[name].integratedOutputSections[name]
    ```

    Note

    Check [IntegratedOutputSection on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-integratedoutputsectionpyc.htm?contextscope=all).

    Member Details:

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L48-L51)[¶](#abaqus.StepOutput.OutputModel.IntegratedOutputSection.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system used to express vector
        output. If **localCsys** = None, the degrees of freedom are defined in the global coordinate
        system. The default value is None.

    name : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py)[¶](#abaqus.StepOutput.OutputModel.IntegratedOutputSection.name "Permalink to this definition")
    :   A String specifying the repository key.

    projectOrientation : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L53-L57)[¶](#abaqus.StepOutput.OutputModel.IntegratedOutputSection.projectOrientation "Permalink to this definition")
    :   A Boolean specifying that the coordinate system be projected onto the **surface** such
        that the 1-axis is normal to the **surface**. Projection onto a planar **surface** is such
        that the 1-axis is normal to the surface, and a projection onto a nonplanar **surface** is
        such that a least-squares fit surface will be used. The default value is OFF.

    refPoint : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py)[¶](#abaqus.StepOutput.OutputModel.IntegratedOutputSection.refPoint "Permalink to this definition")
    :   None or a Region object specifying the anchor point about which the integrated moment
        over the output region is computed or the SymbolicConstant None representing the global
        origin. The default value is None.

    refPointAtCenter : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L34-L37)[¶](#abaqus.StepOutput.OutputModel.IntegratedOutputSection.refPointAtCenter "Permalink to this definition")
    :   A Boolean specifying that the **refPoint** be adjusted so that it coincides with the
        center of the output region in the initial configuration. This argument is valid only
        when you include the **refPoint** argument. The default value is OFF.

    refPointMotion : --is-rst--:py:data:`~typing.Literal`\[``AVERAGE\_TRANSLATION``, ``AVERAGE``, ``INDEPENDENT``] = `'INDEPENDENT'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L39-L46)[¶](#abaqus.StepOutput.OutputModel.IntegratedOutputSection.refPointMotion "Permalink to this definition")
    :   A SymbolicConstant specifying how to relate the motion of **refPoint** to the average
        motion of the output region. A value of INDEPENDENT will allow the **refPoint** to move
        independent of the output region. A value of AVERAGE\_TRANSLATION will set the
        displacement of the **refPoint** equal to the average translation of the output region. A
        value of AVERAGE will set the displacement and rotation of the **refPoint** equal to the
        average translation of the output region. The default value is INDEPENDENT.This argument
        is valid only when you include the **refPoint** argument.

    setValues(*[surface](#abaqus.StepOutput.OutputModel.IntegratedOutputSection.setValues.surface "abaqus.StepOutput.OutputModel.IntegratedOutputSection.setValues.surface (Python parameter) — A Region object specifying the surface over which the output is based.")*, *[refPoint](#abaqus.StepOutput.OutputModel.IntegratedOutputSection.setValues.refPoint "abaqus.StepOutput.OutputModel.IntegratedOutputSection.setValues.refPoint (Python parameter) — None or a Region object specifying the anchor point about which the integrated moment over the output region is computed or the SymbolicConstant None representing the global origin.")=`None`*, *[refPointAtCenter](#abaqus.StepOutput.OutputModel.IntegratedOutputSection.setValues.refPointAtCenter "abaqus.StepOutput.OutputModel.IntegratedOutputSection.setValues.refPointAtCenter (Python parameter) — A Boolean specifying that the refPoint be adjusted so that it coincides with the center of the output region in the initial configuration.")=`0`*, *[refPointMotion](#abaqus.StepOutput.OutputModel.IntegratedOutputSection.setValues.refPointMotion "abaqus.StepOutput.OutputModel.IntegratedOutputSection.setValues.refPointMotion (Python parameter) — A SymbolicConstant specifying how to relate the motion of refPoint to the average motion of the output region.")=`abaqusConstants.INDEPENDENT`*, *[localCsys](#abaqus.StepOutput.OutputModel.IntegratedOutputSection.setValues.localCsys "abaqus.StepOutput.OutputModel.IntegratedOutputSection.setValues.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system used to express vector output.")=`None`*, *[projectOrientation](#abaqus.StepOutput.OutputModel.IntegratedOutputSection.setValues.projectOrientation "abaqus.StepOutput.OutputModel.IntegratedOutputSection.setValues.projectOrientation (Python parameter) — A Boolean specifying that the coordinate system be projected onto the surface such that the 1-axis is normal to the surface.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py#L116-L158)[¶](#abaqus.StepOutput.OutputModel.IntegratedOutputSection.setValues "Permalink to this definition")
    :   This method modifies the IntegratedOutputSection object.

        Note

        Check [IntegratedOutputSection.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-integratedoutputsectionpyc.htm?contextscope=all#simaker-integratedoutputsectionsetvaluespyc).

        Parameters:[¶](#abaqus.StepOutput.OutputModel.IntegratedOutputSection.setValues-parameters "Permalink to this headline")
        :   surface[¶](#abaqus.StepOutput.OutputModel.IntegratedOutputSection.setValues.surface "Permalink to this definition")
            :   A Region object specifying the surface over which the output is based.

            refPoint=`None`[¶](#abaqus.StepOutput.OutputModel.IntegratedOutputSection.setValues.refPoint "Permalink to this definition")
            :   None or a Region object specifying the anchor point about which the integrated moment
                over the output region is computed or the SymbolicConstant None representing the global
                origin. The default value is None.

            refPointAtCenter=`0`[¶](#abaqus.StepOutput.OutputModel.IntegratedOutputSection.setValues.refPointAtCenter "Permalink to this definition")
            :   A Boolean specifying that the **refPoint** be adjusted so that it coincides with the
                center of the output region in the initial configuration. This argument is valid only
                when you include the **refPoint** argument. The default value is OFF.

            refPointMotion=`abaqusConstants.INDEPENDENT`[¶](#abaqus.StepOutput.OutputModel.IntegratedOutputSection.setValues.refPointMotion "Permalink to this definition")
            :   A SymbolicConstant specifying how to relate the motion of **refPoint** to the average
                motion of the output region. A value of INDEPENDENT will allow the **refPoint** to move
                independent of the output region. A value of AVERAGE\_TRANSLATION will set the
                displacement of the **refPoint** equal to the average translation of the output region. A
                value of AVERAGE will set the displacement and rotation of the **refPoint** equal to the
                average translation of the output region. The default value is INDEPENDENT.This argument
                is valid only when you include the **refPoint** argument.

            localCsys=`None`[¶](#abaqus.StepOutput.OutputModel.IntegratedOutputSection.setValues.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system used to express vector
                output. If **localCsys** = None, the degrees of freedom are defined in the global coordinate
                system. The default value is None.

            projectOrientation=`0`[¶](#abaqus.StepOutput.OutputModel.IntegratedOutputSection.setValues.projectOrientation "Permalink to this definition")
            :   A Boolean specifying that the coordinate system be projected onto the **surface** such
                that the 1-axis is normal to the **surface**. Projection onto a planar **surface** is such
                that the 1-axis is normal to the surface, and a projection onto a nonplanar **surface** is
                such that a least-squares fit surface will be used. The default value is OFF.

    surface : --is-rst--:py:class:`~abaqus.Region.Region.Region`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputModel.py)[¶](#abaqus.StepOutput.OutputModel.IntegratedOutputSection.surface "Permalink to this definition")
    :   A Region object specifying the surface over which the output is based.

*class* Monitor(*[node](#abaqus.StepOutput.OutputStep.Monitor "abaqus.StepOutput.OutputStep.Monitor.__init__.node (Python parameter)")*, *[dof](#abaqus.StepOutput.OutputStep.Monitor "abaqus.StepOutput.OutputStep.Monitor.__init__.dof (Python parameter)")*, *[frequency](#abaqus.StepOutput.OutputStep.Monitor "abaqus.StepOutput.OutputStep.Monitor.__init__.frequency (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputStep.py#L11-L131)[¶](#abaqus.StepOutput.OutputStep.Monitor "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The Monitor object defines a degree of freedom to monitor.

    Note

    This object can be accessed by:

    ```python
    import step
    mdb.models[name].steps[name].monitor
    ```

    The corresponding analysis keywords are:

    * MONITOR

    Note

    Check [Monitor on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-monitorpyc.htm?contextscope=all).

    Member Details:

    dof : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputStep.py)[¶](#abaqus.StepOutput.OutputStep.Monitor.dof "Permalink to this definition")
    :   A SymbolicConstant specifying the degree of freedom to be monitored at the node.
        Possible values are:

        * U1
        * U2
        * U3
        * UR1
        * UR2
        * UR3
        * WARP
        * FLUID\_PRESSURE
        * ELECTRICAL\_POTENTIAL
        * NT11
        * NT30
        * NN11
        * NN30

        The NT identifiers are not available for mass diffusion. The NN identifiers are
        available only for mass diffusion.

    frequency : --is-rst--:py:class:`int`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputStep.py)[¶](#abaqus.StepOutput.OutputStep.Monitor.frequency "Permalink to this definition")
    :   An Int specifying the output frequency in increments. This argument is valid only for an
        Abaqus/Standard analysis.

    node : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputStep.py)[¶](#abaqus.StepOutput.OutputStep.Monitor.node "Permalink to this definition")
    :   A String specifying the name of the region to be monitored.

    setValues(*\*[args](#abaqus.StepOutput.OutputStep.Monitor.setValues "abaqus.StepOutput.OutputStep.Monitor.setValues.args (Python parameter)")*, *\*\*[kwargs](#abaqus.StepOutput.OutputStep.Monitor.setValues "abaqus.StepOutput.OutputStep.Monitor.setValues.kwargs (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/OutputStep.py#L123-L131)[¶](#abaqus.StepOutput.OutputStep.Monitor.setValues "Permalink to this definition")
    :   This method modifies the Monitor object.

        Raises:[¶](#abaqus.StepOutput.OutputStep.Monitor.setValues-raises "Permalink to this headline")
        :   **RangeError** –

*class* TimePoint(*[name](#abaqus.StepOutput.TimePoint.TimePoint "abaqus.StepOutput.TimePoint.TimePoint.__init__.name (Python parameter)")*, *[points](#abaqus.StepOutput.TimePoint.TimePoint "abaqus.StepOutput.TimePoint.TimePoint.__init__.points (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/TimePoint.py#L6-L66)[¶](#abaqus.StepOutput.TimePoint.TimePoint "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The TimePoint object defines time points at which data are written to the output database or restart
    files.

    Note

    This object can be accessed by:

    ```python
    import step
    mdb.models[name].timePoints[name]
    ```

    The corresponding analysis keywords are:

    * TIME POINTS

    Note

    Check [TimePoint on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-timepointpyc.htm?contextscope=all).

    Member Details:

    name : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/TimePoint.py)[¶](#abaqus.StepOutput.TimePoint.TimePoint.name "Permalink to this definition")
    :   A String specifying the repository key.

    points : --is-rst--:py:class:`tuple`\[:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`], :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/TimePoint.py#L25-L27)[¶](#abaqus.StepOutput.TimePoint.TimePoint.points "Permalink to this definition")
    :   A sequence of sequences of Floats specifying time points at which data are written to
        the output database or restart files.

    setValues(*\*[args](#abaqus.StepOutput.TimePoint.TimePoint.setValues "abaqus.StepOutput.TimePoint.TimePoint.setValues.args (Python parameter)")*, *\*\*[kwargs](#abaqus.StepOutput.TimePoint.TimePoint.setValues "abaqus.StepOutput.TimePoint.TimePoint.setValues.kwargs (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/TimePoint.py#L58-L66)[¶](#abaqus.StepOutput.TimePoint.TimePoint.setValues "Permalink to this definition")
    :   This method modifies the TimePoint object.

        Raises:[¶](#abaqus.StepOutput.TimePoint.TimePoint.setValues-raises "Permalink to this headline")
        :   **RangeError** –

*class* Restart(*[numberIntervals](#abaqus.StepOutput.Restart.Restart "abaqus.StepOutput.Restart.Restart.__init__.numberIntervals (Python parameter)")=`0`*, *[timeMarks](#abaqus.StepOutput.Restart.Restart "abaqus.StepOutput.Restart.Restart.__init__.timeMarks (Python parameter)")=`0`*, *[overlay](#abaqus.StepOutput.Restart.Restart "abaqus.StepOutput.Restart.Restart.__init__.overlay (Python parameter)")=`0`*, *[frequency](#abaqus.StepOutput.Restart.Restart "abaqus.StepOutput.Restart.Restart.__init__.frequency (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/Restart.py#L8-L92)[¶](#abaqus.StepOutput.Restart.Restart "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The Restart object defines a restart request.

    Note

    This object can be accessed by:

    ```python
    import step
    mdb.models[name].steps[name].restart
    ```

    The corresponding analysis keywords are:

    * RESTART

    Note

    Check [Restart on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-restartpyc.htm?contextscope=all).

    Member Details:

    frequency : --is-rst--:py:class:`int` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/Restart.py#L36-L39)[¶](#abaqus.StepOutput.Restart.Restart.frequency "Permalink to this definition")
    :   An Int specifying the increments at which restart information will be written. The
        default value is 0. The default value is 0.This argument applies only to Abaqus/Standard
        analyses.

    numberIntervals : --is-rst--:py:class:`int` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/Restart.py#L23-L25)[¶](#abaqus.StepOutput.Restart.Restart.numberIntervals "Permalink to this definition")
    :   An Int specifying the number of intervals during the step at which restart information
        will be written. The default value is 0. The default value is 1.

    overlay : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/Restart.py#L31-L34)[¶](#abaqus.StepOutput.Restart.Restart.overlay "Permalink to this definition")
    :   A Boolean specifying that only one increment per step should be retained on the restart
        file, thus minimizing the size of the restart file. The default value is OFF. The
        default value is ON.

    setValues(*\*[args](#abaqus.StepOutput.Restart.Restart.setValues "abaqus.StepOutput.Restart.Restart.setValues.args (Python parameter)")*, *\*\*[kwargs](#abaqus.StepOutput.Restart.Restart.setValues "abaqus.StepOutput.Restart.Restart.setValues.kwargs (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/Restart.py#L84-L92)[¶](#abaqus.StepOutput.Restart.Restart.setValues "Permalink to this definition")
    :   This method modifies the Restart object.

        Raises:[¶](#abaqus.StepOutput.Restart.Restart.setValues-raises "Permalink to this headline")
        :   **RangeError** –

    timeMarks : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/StepOutput/Restart.py#L27-L29)[¶](#abaqus.StepOutput.Restart.Restart.timeMarks "Permalink to this definition")
    :   A Boolean specifying whether to use exact time marks for writing during an analysis. The
        default value is OFF. The default value is OFF.

[Back to top](#)