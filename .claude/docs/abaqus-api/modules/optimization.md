# Abaqus OPTIMIZATION Module API Reference

> Source: [https://hailin.wang/abqpy/en/2025/reference/mdb/model/optimization.html](https://hailin.wang/abqpy/en/2025/reference/mdb/model/optimization.html)
> Downloaded for offline use by Claude Code skills.

---

# Optimization[¶](#optimization "Permalink to this heading")

Optimization commands are used to perform topology, shape, or sizing optimization of your model given a set of objectives and a set of restrictions.

## Create optimization tasks[¶](#create-optimization-tasks "Permalink to this heading")

*class* OptimizationTaskModel(*[name](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.__init__.name (Python parameter)")*, *[description](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.__init__.description (Python parameter)")=`''`*, *[stefanBoltzmann](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.__init__.stefanBoltzmann (Python parameter)")=`None`*, *[absoluteZero](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.__init__.absoluteZero (Python parameter)")=`None`*, *[waveFormulation](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.__init__.waveFormulation (Python parameter)")=`abaqusConstants.NOT_SET`*, *[modelType](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.__init__.modelType (Python parameter)")=`abaqusConstants.STANDARD_EXPLICIT`*, *[universalGas](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.__init__.universalGas (Python parameter)")=`None`*, *[copyConstraints](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.__init__.copyConstraints (Python parameter)")=`1`*, *[copyConnectors](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.__init__.copyConnectors (Python parameter)")=`1`*, *[copyInteractions](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.__init__.copyInteractions (Python parameter)")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L38-L761)[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel "Permalink to this definition")
:   Bases: [`ModelBase`](index.html#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase (Python class) — Bases: object")

    Abaqus creates a Model object named Model-1 when a session is started.

    Note

    This object can be accessed by:

    ```python
    mdb.models[name]
    ```

    Note

    Check [OptimizationTaskModel on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?contextscope=all).

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
    | [`BeadTask`](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask (Python method) — This method creates a BeadTask object.")(name[, abaqusSensitivities, ...]) | This method creates a BeadTask object. |
    | [`ShapeTask`](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask (Python method) — This method creates a ShapeTask object.")(name[, abaqusSensitivities, ...]) | This method creates a ShapeTask object. |
    | [`SizingTask`](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask (Python method) — This method creates a SizingTask object.")(name[, abaqusSensitivities, ...]) | This method creates a SizingTask object. |
    | [`TopologyTask`](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask (Python method) — This method creates a TopologyTask object.")(name[, abaqusSensitivities, ...]) | This method creates a TopologyTask object. |

    Inherited from [`ModelBase`](index.html#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | `__init__`(name[, description, ...]) | This method creates a Model object. |
    | [`setValues`](index.html#abaqus.Model.ModelBase.ModelBase.setValues "abaqus.Model.ModelBase.ModelBase.setValues (Python method) — This method modifies the Model object.")([description, noPartsInputFile, ...]) | This method modifies the Model object. |

    ---

    Member Details:

    BeadTask(*[name](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.name "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.name (Python parameter) — A String specifying the optimization task repository key.")*, *[abaqusSensitivities](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.abaqusSensitivities "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.abaqusSensitivities (Python parameter) — A Boolean specifying whether to use Abaqus to compute the design responses and their sensitivities.")=`True`*, *[algorithm](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.algorithm "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.algorithm (Python parameter) — A SymbolicConstant specifying the optimization task algorithm.")=`abaqusConstants.GENERAL_OPTIMIZATION`*, *[areBCRegionsFrozen](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.areBCRegionsFrozen "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.areBCRegionsFrozen (Python parameter) — A Boolean specifying whether to exclude elements with boundary conditions from the optimization.")=`0`*, *[beadIter](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.beadIter "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.beadIter (Python parameter) — An int specifying the step size of the optimization.")=`1`*, *[beadMaxMembraneStress](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.beadMaxMembraneStress "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.beadMaxMembraneStress (Python parameter) — A float specifying maximum membrane/bending stress.")=`0`*, *[beadMinStress](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.beadMinStress "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.beadMinStress (Python parameter) — A float specifying minimum stress.")=`0`*, *[beadPerturbation](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.beadPerturbation "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.beadPerturbation (Python parameter) — A Sets perturbation size for finite differences.")=`0`*, *[beadWidth](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.beadWidth "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.beadWidth (Python parameter) — A SymbolicConstant specifying the Optimization product default or a float specifying the bead width.")=`abaqusConstants.DEFAULT`*, *[curveSmooth](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.curveSmooth "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.curveSmooth (Python parameter) — A float specifying relative value to the middle element edge length such that normals in this area do not cross each other.")=`5`*, *[filterRadius](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.filterRadius "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.filterRadius (Python parameter) — A float specifying the filter radius.")=`4`*, *[filterRadiusBy](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.filterRadiusBy "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.filterRadiusBy (Python parameter) — A SymbolicConstant specifying the method used to define filter radius.")=`abaqusConstants.VALUE`*, *[flipNormalDir](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.flipNormalDir "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.flipNormalDir (Python parameter) — A Boolean specifying whether the growth direction is along the normal direction of elements or opposite to the normal direction.")=`0`*, *[frozenBoundaryConditionRegion](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.frozenBoundaryConditionRegion "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.frozenBoundaryConditionRegion (Python parameter) — When nodes with boundary conditions are excluded from the optimization (frozenBoundaryConditionRegions = ON).")=`abaqusConstants.MODEL`*, *[isSensCalcOnlyOnDesignNodes](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.isSensCalcOnlyOnDesignNodes "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.isSensCalcOnlyOnDesignNodes (Python parameter) — A Boolean specifying whether to calculate the sensitivities only on design nodes or the whole model.")=`0`*, *[modeTrackingRegion](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.modeTrackingRegion "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.modeTrackingRegion (Python parameter) — The SymbolicConstant MODEL or a Region object specifying the region to use for mode tracking.")=`abaqusConstants.MODEL`*, *[nodalMoveLimit](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.nodalMoveLimit "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.nodalMoveLimit (Python parameter) — A Float specifying the maximum change in nodal displacement per design cycle.")=`0`*, *[nodeSmooth](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.nodeSmooth "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.nodeSmooth (Python parameter) — A SymbolicConstant specifying the Optimization product default or a float specifying the node smooth.")=`abaqusConstants.DEFAULT`*, *[nodeUpdateStrategy](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.nodeUpdateStrategy "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.nodeUpdateStrategy (Python parameter) — A SymbolicConstant specifying the strategy for how the nodal displacements are updated in the method of moving asymptotes.")=`abaqusConstants.CONSERVATIVE`*, *[numTrackedModes](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.numTrackedModes "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.numTrackedModes (Python parameter) — An Int specifying the number of modes included in mode tracking.")=`5`*, *[updateShapeBasisVectors](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.updateShapeBasisVectors "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.updateShapeBasisVectors (Python parameter) — A SymbolicConstant specifying whether to update shape basis vectors in the first design cycle or every design cycle.")=`abaqusConstants.EVERY_CYCLE`*, *[groupOperator](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.groupOperator "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.groupOperator (Python parameter) — A Boolean specifying whether the group in the design response will be evaluated using the existing algorithm or a new algorithm based on Abaqus sensitivities.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L48-L186)[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask "Permalink to this definition")
    :   This method creates a BeadTask object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].BeadTask
        ```

        Note

        Check [BeadTask on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadtaskpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.name "Permalink to this definition")
            :   A String specifying the optimization task repository key.

            abaqusSensitivities=`True`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.abaqusSensitivities "Permalink to this definition")
            :   A Boolean specifying whether to use Abaqus to compute the design responses and their
                sensitivities. The default value is True.

                New in version 2019: The `abaqusSensitivities` argument was added.

            algorithm=`abaqusConstants.GENERAL_OPTIMIZATION`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.algorithm "Permalink to this definition")
            :   A SymbolicConstant specifying the optimization task algorithm. Possible values are
                GENERAL\_OPTIMIZATION and CONDITION\_BASED\_OPTIMIZATION. The default value is
                GENERAL\_OPTIMIZATION.

            areBCRegionsFrozen=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.areBCRegionsFrozen "Permalink to this definition")
            :   A Boolean specifying whether to exclude elements with boundary conditions from the
                optimization. The default value is OFF.

            beadIter=`1`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.beadIter "Permalink to this definition")
            :   An int specifying the step size of the optimization. The default value is 1.

            beadMaxMembraneStress=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.beadMaxMembraneStress "Permalink to this definition")
            :   A float specifying maximum membrane/bending stress. The default value is 0.1.

            beadMinStress=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.beadMinStress "Permalink to this definition")
            :   A float specifying minimum stress. The default value is 0.001.

            beadPerturbation=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.beadPerturbation "Permalink to this definition")
            :   A Sets perturbation size for finite differences. The default value is 0.0001.

            beadWidth=`abaqusConstants.DEFAULT`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.beadWidth "Permalink to this definition")
            :   A SymbolicConstant specifying the Optimization product default or a float specifying the
                bead width. The default value is DEFAULT.

            curveSmooth=`5`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.curveSmooth "Permalink to this definition")
            :   A float specifying relative value to the middle element edge length such that normals in
                this area do not cross each other. The default value is 5.

            filterRadius=`4`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.filterRadius "Permalink to this definition")
            :   A float specifying the filter radius. The default value is 4.

            filterRadiusBy=`abaqusConstants.VALUE`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.filterRadiusBy "Permalink to this definition")
            :   A SymbolicConstant specifying the method used to define filter radius. Possible values
                are VALUE and REFERENCE. The default is VALUE.

            flipNormalDir=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.flipNormalDir "Permalink to this definition")
            :   A Boolean specifying whether the growth direction is along the normal direction of
                elements or opposite to the normal direction. The default value is OFF

            frozenBoundaryConditionRegion=`abaqusConstants.MODEL`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.frozenBoundaryConditionRegion "Permalink to this definition")
            :   When nodes with boundary conditions are excluded from the optimization
                (*frozenBoundaryConditionRegions* = ON). you can specify that this exclusion apply to
                nodes throughout the model or only to those nodes from a specific region. Set this
                parameter to the SymbolicConstant MODEL to apply the freeze to the entire model, or set
                this parameter to a Region object to specify an individual region over which nodes with
                boundary conditions should be frozen. The default value is MODEL.

            isSensCalcOnlyOnDesignNodes=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.isSensCalcOnlyOnDesignNodes "Permalink to this definition")
            :   A Boolean specifying whether to calculate the sensitivities only on design nodes or the
                whole model. The default value is ON

            modeTrackingRegion=`abaqusConstants.MODEL`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.modeTrackingRegion "Permalink to this definition")
            :   The SymbolicConstant MODEL or a Region object specifying the region to use for mode
                tracking. The default value is MODEL.

            nodalMoveLimit=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.nodalMoveLimit "Permalink to this definition")
            :   A Float specifying the maximum change in nodal displacement per design cycle. The
                default value is 0.1.

            nodeSmooth=`abaqusConstants.DEFAULT`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.nodeSmooth "Permalink to this definition")
            :   A SymbolicConstant specifying the Optimization product default or a float specifying the
                node smooth. The default value is DEFAULT.

            nodeUpdateStrategy=`abaqusConstants.CONSERVATIVE`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.nodeUpdateStrategy "Permalink to this definition")
            :   A SymbolicConstant specifying the strategy for how the nodal displacements are updated
                in the method of moving asymptotes. Possible values are NORMAL, CONSERVATIVE, and
                AGGRESSIVE. The default value is CONSERVATIVE.

            numTrackedModes=`5`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.numTrackedModes "Permalink to this definition")
            :   An Int specifying the number of modes included in mode tracking. The default value is 5.

            updateShapeBasisVectors=`abaqusConstants.EVERY_CYCLE`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.updateShapeBasisVectors "Permalink to this definition")
            :   A SymbolicConstant specifying whether to update shape basis vectors in the first design
                cycle or every design cycle. Possible values are EVERY\_CYCLE and FIRST\_CYCLE. The
                default value is EVERY\_CYCLE.

            groupOperator=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask.groupOperator "Permalink to this definition")
            :   A Boolean specifying whether the group in the design response will be evaluated using
                the existing algorithm or a new algorithm based on Abaqus sensitivities. The default
                value of False means that the existing algorithm will be used.

                New in version 2022: The `groupOperator` argument was added.

        Returns:[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask-returns "Permalink to this headline")
        :   A BeadTask object.

        Return type:[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.BeadTask-return-type "Permalink to this headline")
        :   [`BeadTask`](#abaqus.Optimization.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.BeadTask (Python class) — Bases: OptimizationTask")

    ShapeTask(*[name](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.name "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.name (Python parameter) — A String specifying the optimization task repository key.")*, *[abaqusSensitivities](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.abaqusSensitivities "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.abaqusSensitivities (Python parameter) — A Boolean specifying whether to use Abaqus to compute the design responses and their sensitivities.")=`True`*, *[absoluteStepSizeControl](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.absoluteStepSizeControl "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.absoluteStepSizeControl (Python parameter) — A SymbolicConstant specifying whether to control the permitted absolute step size by the average optimization displacement or minimum optimization displacement.")=`abaqusConstants.MINIMUM`*, *[activateDurability](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.activateDurability "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.activateDurability (Python parameter) — A boolean specifying whether or not the durability approach of optimization is turned on.")=`1`*, *[additionalDurabilityFiles](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.additionalDurabilityFiles "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.additionalDurabilityFiles (Python parameter) — A String specifying the path of additional files pertaining to durability optimization. Only valid if the activateDurability argument is ON.")=`''`*, *[constrainedLaplacianConvergenceLevel](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.constrainedLaplacianConvergenceLevel "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.constrainedLaplacianConvergenceLevel (Python parameter) — A SymbolicConstant specifying the constrained Laplacian convergence level.")=`abaqusConstants.NORMAL`*, *[curvatureSmoothingEdgeLength](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.curvatureSmoothingEdgeLength "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.curvatureSmoothingEdgeLength (Python parameter) — A Float specifying the edge length for the movement vector.")=`5`*, *[durabilityInputfile](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.durabilityInputfile "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.durabilityInputfile (Python parameter) — A string specifying the path of the input file.")=`''`*, *[durabilitySolver](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.durabilitySolver "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.durabilitySolver (Python parameter) — A String specifying the type of solver for durability optimization.")=`abaqusConstants.FE_SAFE`*, *[equalityConstraintTolerance](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.equalityConstraintTolerance "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.equalityConstraintTolerance (Python parameter) — A Float specifying the equality constraint tolerance.")=`None`*, *[featureRecognitionAngle](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.featureRecognitionAngle "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.featureRecognitionAngle (Python parameter) — A Float specifying the mesh smoothing feature recognition angle for edges and corners. The default value is 30.0.")=`30`*, *[filterExponent](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.filterExponent "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.filterExponent (Python parameter) — A Float specifying the weight depending on the radius, used when filterMaxRadius is specified.")=`1`*, *[filterMaxRadius](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.filterMaxRadius "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.filterMaxRadius (Python parameter) — None or a Float specifying the maximum influence radius for equivalent stress.")=`None`*, *[filterRadiusReduction](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.filterRadiusReduction "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.filterRadiusReduction (Python parameter) — None or a Float specifying the reduction of the radius depending on surface bending, used when filterMaxRadius is specified.")=`None`*, *[firstCycleDeletedVolumeTechnique](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.firstCycleDeletedVolumeTechnique "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.firstCycleDeletedVolumeTechnique (Python parameter) — A SymbolicConstant specifying the method of specifying volume that can be removed immediately in the first design cycle.")=`0`*, *[freezeBoundaryConditionRegions](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.freezeBoundaryConditionRegions "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.freezeBoundaryConditionRegions (Python parameter) — A Boolean specifying whether to exclude nodes with boundary conditions from the optimization.")=`0`*, *[frozenBoundaryConditionRegion](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.frozenBoundaryConditionRegion "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.frozenBoundaryConditionRegion (Python parameter) — The SymbolicConstant MODEL or a Region object specifying the region in which to freeze boundary condition regions, or the SymbolicConstant MODEL, used with freezeBoundaryConditionRegions.")=`abaqusConstants.MODEL`*, *[geometricRestrictionEvaluationFrequency](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.geometricRestrictionEvaluationFrequency "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.geometricRestrictionEvaluationFrequency (Python parameter) — A SymbolicConstant specifying the frequency of evaluating geometric restrictions during mesh smoothing.")=`abaqusConstants.LOW`*, *[growthScaleFactor](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.growthScaleFactor "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.growthScaleFactor (Python parameter) — A Float specifying the scale factor to apply to optimization displacements for nodes with growth.")=`1`*, *[haltUponViolation](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.haltUponViolation "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.haltUponViolation (Python parameter) — A Boolean specifying whether to halt the optimization if quality criteria are not satisified.")=`0`*, *[layerReferenceRegion](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.layerReferenceRegion "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.layerReferenceRegion (Python parameter) — None or a Region object specifying the region specifying the first node layer for mesh smoothing, used when meshSmoothingRegionMethod is TASK_REGION_LAYERS.")=`None`*, *[meshSmoothingRegionMethod](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.meshSmoothingRegionMethod "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.meshSmoothingRegionMethod (Python parameter) — A SymbolicConstant specifying the method used to determine the mesh smoothing region. The REGION value uses the smoothingRegion.")=`abaqusConstants.TASK_REGION_LAYERS`*, *[meshSmoothingStrategy](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.meshSmoothingStrategy "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.meshSmoothingStrategy (Python parameter) — A SymbolicConstant specifying the method smoothing strategy.")=`abaqusConstants.CONSTRAINED_LAPLACIAN`*, *[midsideInterpolation](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.midsideInterpolation "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.midsideInterpolation (Python parameter) — A SymbolicConstant specifying the approach used when treating midside node positions during optimization.")=`abaqusConstants.POSITIONS`*, *[numFreeNodeLayers](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.numFreeNodeLayers "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.numFreeNodeLayers (Python parameter) — The SymbolicConstant FIX_NONE or an Int specifying the number of node layers adjoining the task region to remain free during mesh smoothing.")=`0`*, *[numSmoothedElementLayers](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.numSmoothedElementLayers "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.numSmoothedElementLayers (Python parameter) — None or an Int specifying the number of layers for mesh smoothing when meshSmoothingRegionMethod is NUMBER_OF_LAYERS.")=`None`*, *[presumeFeasibleBCRegionAtStart](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.presumeFeasibleBCRegionAtStart "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.presumeFeasibleBCRegionAtStart (Python parameter) — A Boolean specifying whether to ignore automatically frozen boundary condition regions in the first design cycle.")=`1`*, *[quadMaxAngle](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.quadMaxAngle "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.quadMaxAngle (Python parameter) — A Float specifying the maximum angle for quad elements during mesh smoothing.")=`160`*, *[quadMinAngle](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.quadMinAngle "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.quadMinAngle (Python parameter) — A Float specifying the minimum angle for quad elements during mesh smoothing.")=`20`*, *[quadSkew](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.quadSkew "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.quadSkew (Python parameter) — A Float specifying the skew angle for quad elements during mesh smoothing, used with reportQualityViolation.")=`30`*, *[quadTaper](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.quadTaper "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.quadTaper (Python parameter) — A Float specifying the taper for quad elements during mesh smoothing, used with reportQualityViolation.")=`0`*, *[region](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.region "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.region (Python parameter) — The SymbolicConstant MODEL or a Region object specifying the region to which the optimization task is applied.")=`abaqusConstants.MODEL`*, *[reportPoorQualityElements](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.reportPoorQualityElements "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.reportPoorQualityElements (Python parameter) — A Boolean specifying whether to report poor quality elements during mesh smoothing.")=`0`*, *[reportQualityViolation](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.reportQualityViolation "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.reportQualityViolation (Python parameter) — A Boolean specifying whether to report a quality criteria violation during mesh smoothing.")=`0`*, *[shrinkScaleFactor](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.shrinkScaleFactor "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.shrinkScaleFactor (Python parameter) — A Float specifying the scale factor to apply to optimization displacements for nodes with shrinkage.")=`1`*, *[smoothingRegion](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.smoothingRegion "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.smoothingRegion (Python parameter) — None or a Region object specifying the mesh smoothing region, used when meshSmoothingRegionMethod is REGION.")=`None`*, *[targetMeshQuality](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.targetMeshQuality "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.targetMeshQuality (Python parameter) — A SymbolicConstant specifying the target mesh quality for mesh smoothing.")=`abaqusConstants.LOW`*, *[tetAspectRatio](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.tetAspectRatio "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.tetAspectRatio (Python parameter) — A Float specifying the tet element aspect ratio during mesh smoothing.")=`100`*, *[tetMaxAspect](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.tetMaxAspect "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.tetMaxAspect (Python parameter) — A Float specifying the maximum tet element aspect ratio during mesh smoothing.")=`8`*, *[tetMinAspect](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.tetMinAspect "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.tetMinAspect (Python parameter) — A Float specifying the minimum tet element aspect ratio during mesh smoothing.")=`0`*, *[tetSkew](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.tetSkew "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.tetSkew (Python parameter) — A Float specifying the tet element skew value during mesh smoothing.")=`100`*, *[triMaxAngle](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.triMaxAngle "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.triMaxAngle (Python parameter) — A Float specifying the tri element maximum angle during mesh smoothing.")=`140`*, *[triMinAngle](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.triMinAngle "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.triMinAngle (Python parameter) — A Float specifying the tri element maximum angle during mesh smoothing.")=`20`*, *[updateShapeBasisVectors](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.updateShapeBasisVectors "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.updateShapeBasisVectors (Python parameter) — A SymbolicConstant specifying whether to update shape basis vectors in the first design cycle or every design cycle.")=`abaqusConstants.EVERY_CYCLE`*, *[groupOperator](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.groupOperator "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.groupOperator (Python parameter) — A Boolean specifying whether the group in the design response will be evaluated using the existing algorithm or a new algorithm based on Abaqus sensitivities.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L188-L452)[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask "Permalink to this definition")
    :   This method creates a ShapeTask object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ShapeTask
        ```

        Note

        Check [ShapeTask on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapetaskpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.name "Permalink to this definition")
            :   A String specifying the optimization task repository key.

            abaqusSensitivities=`True`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.abaqusSensitivities "Permalink to this definition")
            :   A Boolean specifying whether to use Abaqus to compute the design responses and their
                sensitivities. The default value is True.

                New in version 2019: The `abaqusSensitivities` argument was added.

            absoluteStepSizeControl=`abaqusConstants.MINIMUM`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.absoluteStepSizeControl "Permalink to this definition")
            :   A SymbolicConstant specifying whether to control the permitted absolute step size by the
                average optimization displacement or minimum optimization displacement. Possible values
                are MINIMUM and AVERAGE. The default value is MINIMUM.

            activateDurability=`1`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.activateDurability "Permalink to this definition")
            :   A boolean specifying whether or not the durability approach of optimization is turned
                on. The default value is ON.

            additionalDurabilityFiles=`''`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.additionalDurabilityFiles "Permalink to this definition")
            :   A String specifying the path of additional files pertaining to durability optimization.
                Only valid if the **activateDurability** argument is ON.

            constrainedLaplacianConvergenceLevel=`abaqusConstants.NORMAL`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.constrainedLaplacianConvergenceLevel "Permalink to this definition")
            :   A SymbolicConstant specifying the constrained Laplacian convergence level. Possible
                values are NORMAL, CONSERVATIVE, and AGGRESSIVE. The default value is NORMAL.

            curvatureSmoothingEdgeLength=`5`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.curvatureSmoothingEdgeLength "Permalink to this definition")
            :   A Float specifying the edge length for the movement vector. The default value is 5.0.

            durabilityInputfile=`''`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.durabilityInputfile "Permalink to this definition")
            :   A string specifying the path of the input file. Only valid if the **activateDurability**
                argument is ON and is a required argument in that case.

            durabilitySolver=`abaqusConstants.FE_SAFE`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.durabilitySolver "Permalink to this definition")
            :   A String specifying the type of solver for durability optimization. Possible values are:
                FE\_SAFE, FEMFAT, FLANS, MSC\_FATIGUE, FE\_FATIGUE, DESIGN\_LIFE, CUSTOM, FEMSITE. The
                default value is FE\_SAFE. Only valid if the **activateDurability** argument is ON.

            equalityConstraintTolerance=`None`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.equalityConstraintTolerance "Permalink to this definition")
            :   A Float specifying the equality constraint tolerance. The default value is 10⁻³.

            featureRecognitionAngle=`30`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.featureRecognitionAngle "Permalink to this definition")
            :   A Float specifying the mesh smoothing feature recognition angle for edges and corners.
                The default value is 30.0.

            filterExponent=`1`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.filterExponent "Permalink to this definition")
            :   A Float specifying the weight depending on the radius, used when **filterMaxRadius** is
                specified. The default value is 1.0.

            filterMaxRadius=`None`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.filterMaxRadius "Permalink to this definition")
            :   None or a Float specifying the maximum influence radius for equivalent stress. The
                default value is None.

            filterRadiusReduction=`None`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.filterRadiusReduction "Permalink to this definition")
            :   None or a Float specifying the reduction of the radius depending on surface bending,
                used when **filterMaxRadius** is specified. The default value is None.

            firstCycleDeletedVolumeTechnique=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.firstCycleDeletedVolumeTechnique "Permalink to this definition")
            :   A SymbolicConstant specifying the method of specifying volume that can be removed
                immediately in the first design cycle. Possible values are OFF, PERCENTAGE, and
                ABSOLUTE. The default value is OFF.

            freezeBoundaryConditionRegions=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.freezeBoundaryConditionRegions "Permalink to this definition")
            :   A Boolean specifying whether to exclude nodes with boundary conditions from the
                optimization. The default value is OFF.

            frozenBoundaryConditionRegion=`abaqusConstants.MODEL`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.frozenBoundaryConditionRegion "Permalink to this definition")
            :   The SymbolicConstant MODEL or a Region object specifying the region in which to freeze
                boundary condition regions, or the SymbolicConstant MODEL, used with
                **freezeBoundaryConditionRegions**. The default value is MODEL.

            geometricRestrictionEvaluationFrequency=`abaqusConstants.LOW`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.geometricRestrictionEvaluationFrequency "Permalink to this definition")
            :   A SymbolicConstant specifying the frequency of evaluating geometric restrictions during
                mesh smoothing. Possible values are LOW, MEDIUM, and HIGH. The default value is LOW.

            growthScaleFactor=`1`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.growthScaleFactor "Permalink to this definition")
            :   A Float specifying the scale factor to apply to optimization displacements for nodes
                with growth. The default value is 1.0.

            haltUponViolation=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.haltUponViolation "Permalink to this definition")
            :   A Boolean specifying whether to halt the optimization if quality criteria are not
                satisified. The default value is OFF.

            layerReferenceRegion=`None`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.layerReferenceRegion "Permalink to this definition")
            :   None or a Region object specifying the region specifying the first node layer for mesh
                smoothing, used when **meshSmoothingRegionMethod** is TASK\_REGION\_LAYERS. The default
                value is None.

            meshSmoothingRegionMethod=`abaqusConstants.TASK_REGION_LAYERS`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.meshSmoothingRegionMethod "Permalink to this definition")
            :   A SymbolicConstant specifying the method used to determine the mesh smoothing region.
                The REGION value uses the **smoothingRegion**. The NUMBER\_OF\_LAYERS value uses the
                **layerReferenceRegion**. The TASK\_REGION\_LAYERS value will smooth six layers using the
                task region. Possible values are TASK\_REGION\_LAYERS, REGION, and NUMBER\_OF\_LAYERS. The
                default value is TASK\_REGION\_LAYERS.

            meshSmoothingStrategy=`abaqusConstants.CONSTRAINED_LAPLACIAN`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.meshSmoothingStrategy "Permalink to this definition")
            :   A SymbolicConstant specifying the method smoothing strategy. Possible values are
                CONSTRAINED\_LAPLACIAN and LOCAL\_GRADIENT. The default value is CONSTRAINED\_LAPLACIAN.

            midsideInterpolation=`abaqusConstants.POSITIONS`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.midsideInterpolation "Permalink to this definition")
            :   A SymbolicConstant specifying the approach used when treating midside node positions
                during optimization. POSITIONS indicates midside node positions are interpolated
                linearly by position. OPTIMIZATION\_DISPLACEMENT indicates they are interpolated by
                optimization displacement of corner nodes. Possible values are POSITIONS and
                OPTIMIZATION\_DISPLACEMENT. The default value is POSITIONS.

            numFreeNodeLayers=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.numFreeNodeLayers "Permalink to this definition")
            :   The SymbolicConstant FIX\_NONE or an Int specifying the number of node layers adjoining
                the task region to remain free during mesh smoothing. A value of 0 indicates that no
                layers are free and all layers are fixed. The default value is 0.

            numSmoothedElementLayers=`None`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.numSmoothedElementLayers "Permalink to this definition")
            :   None or an Int specifying the number of layers for mesh smoothing when
                **meshSmoothingRegionMethod** is NUMBER\_OF\_LAYERS. The default value is None.

            presumeFeasibleBCRegionAtStart=`1`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.presumeFeasibleBCRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore automatically frozen boundary condition regions
                in the first design cycle. This is used with **freezeBoundaryConditionRegions**. The
                default value is ON.

            quadMaxAngle=`160`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.quadMaxAngle "Permalink to this definition")
            :   A Float specifying the maximum angle for quad elements during mesh smoothing. The
                default value is 160.0.

            quadMinAngle=`20`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.quadMinAngle "Permalink to this definition")
            :   A Float specifying the minimum angle for quad elements during mesh smoothing. The
                default value is 20.0.

            quadSkew=`30`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.quadSkew "Permalink to this definition")
            :   A Float specifying the skew angle for quad elements during mesh smoothing, used with
                **reportQualityViolation**. The default value is 30.0.

            quadTaper=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.quadTaper "Permalink to this definition")
            :   A Float specifying the taper for quad elements during mesh smoothing, used with
                **reportQualityViolation**. The default value is 0.5.

            region=`abaqusConstants.MODEL`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.region "Permalink to this definition")
            :   The SymbolicConstant MODEL or a Region object specifying the region to which the
                optimization task is applied. The default value is MODEL.

            reportPoorQualityElements=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.reportPoorQualityElements "Permalink to this definition")
            :   A Boolean specifying whether to report poor quality elements during mesh smoothing. The
                default value is OFF.

            reportQualityViolation=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.reportQualityViolation "Permalink to this definition")
            :   A Boolean specifying whether to report a quality criteria violation during mesh
                smoothing. The default value is OFF.

            shrinkScaleFactor=`1`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.shrinkScaleFactor "Permalink to this definition")
            :   A Float specifying the scale factor to apply to optimization displacements for nodes
                with shrinkage. The default value is 1.0.

            smoothingRegion=`None`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.smoothingRegion "Permalink to this definition")
            :   None or a Region object specifying the mesh smoothing region, used when
                **meshSmoothingRegionMethod** is REGION. The default value is None.

            targetMeshQuality=`abaqusConstants.LOW`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.targetMeshQuality "Permalink to this definition")
            :   A SymbolicConstant specifying the target mesh quality for mesh smoothing. Possible
                values are NONE, LOW, MEDIUM, and HIGH. The default value is LOW.

            tetAspectRatio=`100`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.tetAspectRatio "Permalink to this definition")
            :   A Float specifying the tet element aspect ratio during mesh smoothing. The default value
                is 100.0.

            tetMaxAspect=`8`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.tetMaxAspect "Permalink to this definition")
            :   A Float specifying the maximum tet element aspect ratio during mesh smoothing. The
                default value is 8.0.

            tetMinAspect=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.tetMinAspect "Permalink to this definition")
            :   A Float specifying the minimum tet element aspect ratio during mesh smoothing. The
                default value is 0.222.

            tetSkew=`100`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.tetSkew "Permalink to this definition")
            :   A Float specifying the tet element skew value during mesh smoothing. The default value
                is 100.0.

            triMaxAngle=`140`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.triMaxAngle "Permalink to this definition")
            :   A Float specifying the tri element maximum angle during mesh smoothing. The default
                value is 140.0.

            triMinAngle=`20`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.triMinAngle "Permalink to this definition")
            :   A Float specifying the tri element maximum angle during mesh smoothing. The default
                value is 20.0.

            updateShapeBasisVectors=`abaqusConstants.EVERY_CYCLE`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.updateShapeBasisVectors "Permalink to this definition")
            :   A SymbolicConstant specifying whether to update shape basis vectors in the first design
                cycle or every design cycle. Possible values are EVERY\_CYCLE and FIRST\_CYCLE. The
                default value is EVERY\_CYCLE.

            groupOperator=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask.groupOperator "Permalink to this definition")
            :   A Boolean specifying whether the group in the design response will be evaluated using
                the existing algorithm or a new algorithm based on Abaqus sensitivities. The default
                value of False means that the existing algorithm will be used.

                New in version 2022: The `groupOperator` argument was added.

        Returns:[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask-returns "Permalink to this headline")
        :   A ShapeTask object.

        Return type:[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask-return-type "Permalink to this headline")
        :   [`ShapeTask`](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.ShapeTask (Python method) — This method creates a ShapeTask object.")

    SizingTask(*[name](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.name "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.name (Python parameter) — A String specifying the optimization task repository key.")*, *[abaqusSensitivities](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.abaqusSensitivities "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.abaqusSensitivities (Python parameter) — A Boolean specifying whether to use Abaqus to compute the design responses and their sensitivities.")=`True`*, *[elementThicknessDeltaStopCriteria](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.elementThicknessDeltaStopCriteria "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.elementThicknessDeltaStopCriteria (Python parameter) — A Float specifying the stop criteria based on the change in element thickness.")=`0`*, *[freezeBoundaryConditionRegions](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.freezeBoundaryConditionRegions "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.freezeBoundaryConditionRegions (Python parameter) — A Boolean specifying whether to exclude elements with boundary conditions from the optimization.")=`0`*, *[freezeLoadRegions](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.freezeLoadRegions "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.freezeLoadRegions (Python parameter) — A Boolean specifying whether to exclude elements with loads and elements with loaded nodes from the optimization.")=`1`*, *[modeTrackingRegion](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.modeTrackingRegion "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.modeTrackingRegion (Python parameter) — The SymbolicConstatnt MODEL or a Region object specifying the region to use for mode tracking.")=`abaqusConstants.MODEL`*, *[numFulfilledStopCriteria](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.numFulfilledStopCriteria "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.numFulfilledStopCriteria (Python parameter) — An Int specifying the number of stop criteria.")=`2`*, *[numTrackedModes](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.numTrackedModes "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.numTrackedModes (Python parameter) — An Int specifying the number of modes included in mode tracking.")=`5`*, *[objectiveFunctionDeltaStopCriteria](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.objectiveFunctionDeltaStopCriteria "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.objectiveFunctionDeltaStopCriteria (Python parameter) — A Float specifying the stop criteria based on the change in objective function.")=`0`*, *[stopCriteriaDesignCycle](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.stopCriteriaDesignCycle "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.stopCriteriaDesignCycle (Python parameter) — An Int specifying the first design cycle used to evaluate convergence criteria.")=`4`*, *[thicknessMoveLimit](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.thicknessMoveLimit "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.thicknessMoveLimit (Python parameter) — A Float specifying the maximum change in thickness per design cycle.")=`0`*, *[thicknessUpdateStrategy](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.thicknessUpdateStrategy "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.thicknessUpdateStrategy (Python parameter) — A SymbolicConstant specifying the strategy for how the thickness is updated in the method of moving asymptotes.")=`abaqusConstants.NORMAL`*, *[groupOperator](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.groupOperator "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.groupOperator (Python parameter) — A Boolean specifying whether the group in the design response will be evaluated using the existing algorithm or a new algorithm based on Abaqus sensitivities.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L454-L545)[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask "Permalink to this definition")
    :   This method creates a SizingTask object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].SizingTask
        ```

        Note

        Check [SizingTask on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingtaskpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.name "Permalink to this definition")
            :   A String specifying the optimization task repository key.

            abaqusSensitivities=`True`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.abaqusSensitivities "Permalink to this definition")
            :   A Boolean specifying whether to use Abaqus to compute the design responses and their
                sensitivities. The default value is True.

                New in version 2019: The `abaqusSensitivities` argument was added.

            elementThicknessDeltaStopCriteria=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.elementThicknessDeltaStopCriteria "Permalink to this definition")
            :   A Float specifying the stop criteria based on the change in element thickness. The
                default value is 0.5 x 10⁻².

            freezeBoundaryConditionRegions=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.freezeBoundaryConditionRegions "Permalink to this definition")
            :   A Boolean specifying whether to exclude elements with boundary conditions from the
                optimization. The default value is OFF.

            freezeLoadRegions=`1`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.freezeLoadRegions "Permalink to this definition")
            :   A Boolean specifying whether to exclude elements with loads and elements with loaded
                nodes from the optimization. The default value is ON.

            modeTrackingRegion=`abaqusConstants.MODEL`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.modeTrackingRegion "Permalink to this definition")
            :   The SymbolicConstatnt MODEL or a Region object specifying the region to use for mode
                tracking. The default value is MODEL.

            numFulfilledStopCriteria=`2`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.numFulfilledStopCriteria "Permalink to this definition")
            :   An Int specifying the number of stop criteria. The default value is 2.

            numTrackedModes=`5`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.numTrackedModes "Permalink to this definition")
            :   An Int specifying the number of modes included in mode tracking. The default value is 5.

            objectiveFunctionDeltaStopCriteria=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.objectiveFunctionDeltaStopCriteria "Permalink to this definition")
            :   A Float specifying the stop criteria based on the change in objective function. The
                default value is 0.001.

            stopCriteriaDesignCycle=`4`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.stopCriteriaDesignCycle "Permalink to this definition")
            :   An Int specifying the first design cycle used to evaluate convergence criteria. The
                default value is 4.

            thicknessMoveLimit=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.thicknessMoveLimit "Permalink to this definition")
            :   A Float specifying the maximum change in thickness per design cycle. The default value
                is 0.25.

            thicknessUpdateStrategy=`abaqusConstants.NORMAL`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.thicknessUpdateStrategy "Permalink to this definition")
            :   A SymbolicConstant specifying the strategy for how the thickness is updated in the
                method of moving asymptotes. Possible values are NORMAL, CONSERVATIVE, and AGGRESSIVE.
                The default value is NORMAL.

            groupOperator=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask.groupOperator "Permalink to this definition")
            :   A Boolean specifying whether the group in the design response will be evaluated using
                the existing algorithm or a new algorithm based on Abaqus sensitivities. The default
                value of False means that the existing algorithm will be used.

                New in version 2022: The `groupOperator` argument was added.

        Returns:[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask-returns "Permalink to this headline")
        :   A SizingTask object.

        Return type:[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask-return-type "Permalink to this headline")
        :   [`SizingTask`](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.SizingTask (Python method) — This method creates a SizingTask object.")

    TopologyTask(*[name](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.name "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.name (Python parameter) — A String specifying the optimization task repository key.")*, *[abaqusSensitivities](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.abaqusSensitivities "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.abaqusSensitivities (Python parameter) — A Boolean specifying whether to use Abaqus to compute the design responses and their sensitivities.")=`True`*, *[algorithm](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.algorithm "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.algorithm (Python parameter) — A SymbolicConstant specifying the optimization task algorithm.")=`abaqusConstants.GENERAL_OPTIMIZATION`*, *[densityMoveLimit](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.densityMoveLimit "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.densityMoveLimit (Python parameter) — A Float specifying the maximum density change per design cycle.")=`0`*, *[densityUpdateStrategy](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.densityUpdateStrategy "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.densityUpdateStrategy (Python parameter) — A SymbolicConstant specifying the strategy for how the densities are updated in the method of moving asymptotes.")=`abaqusConstants.NORMAL`*, *[elementDensityDeltaStopCriteria](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.elementDensityDeltaStopCriteria "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.elementDensityDeltaStopCriteria (Python parameter) — A Float specifying the stop criteria based upon the change in element densities.")=`0`*, *[filterRadius](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.filterRadius "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.filterRadius (Python parameter) — None or a Float specifying the mesh filter radius for mesh independence and minimum size.")=`None`*, *[firstCycleDeletedVolume](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.firstCycleDeletedVolume "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.firstCycleDeletedVolume (Python parameter) — A Float specifying the volume that can be removed immediately in the first design cycle. The default value is 5.0.")=`5`*, *[firstCycleDeletedVolumeTechnique](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.firstCycleDeletedVolumeTechnique "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.firstCycleDeletedVolumeTechnique (Python parameter) — A SymbolicConstant specifying the method of quantifying volume that can be removed immediately in the first design cycle.")=`0`*, *[freezeBoundaryConditionRegions](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.freezeBoundaryConditionRegions "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.freezeBoundaryConditionRegions (Python parameter) — A Boolean specifying whether to exclude elements with boundary conditions from the optimization.")=`0`*, *[freezeLoadRegions](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.freezeLoadRegions "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.freezeLoadRegions (Python parameter) — A Boolean specifying whether to exclude elements with loads and elements with loaded nodes from the optimization.")=`1`*, *[frequencySpectrumWeight](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.frequencySpectrumWeight "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.frequencySpectrumWeight (Python parameter) — A Float specifying the weighting factor for frequency spectrum peaks.")=`6`*, *[initialDensity](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.initialDensity "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.initialDensity (Python parameter) — A SymbolicConstant specifying the Optimization product default or a float specifying the initial density.")=`abaqusConstants.DEFAULT`*, *[materialInterpolationPenalty](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.materialInterpolationPenalty "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.materialInterpolationPenalty (Python parameter) — A Float specifying the penalty factor for the material interpolation technique.")=`3`*, *[materialInterpolationTechnique](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.materialInterpolationTechnique "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.materialInterpolationTechnique (Python parameter) — A SymbolicConstant specifying the material interpolation technique: optimization product default, solid isotropic material with penalization, or rational approximation of material properties.")=`abaqusConstants.DEFAULT`*, *[maxDensity](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.maxDensity "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.maxDensity (Python parameter) — A Float specifying the maximum density in the density update.")=`1`*, *[minDensity](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.minDensity "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.minDensity (Python parameter) — A Float specifying the minimum density in the density update.")=`None`*, *[modeTrackingRegion](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.modeTrackingRegion "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.modeTrackingRegion (Python parameter) — The SymbolicConstant MODEL or a Region object specifying the region to use for mode tracking.")=`abaqusConstants.MODEL`*, *[numDesignCycles](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.numDesignCycles "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.numDesignCycles (Python parameter) — An Int specifying the number of design cycles permitted when stepSize is DYNAMIC.")=`15`*, *[numFulfilledStopCriteria](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.numFulfilledStopCriteria "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.numFulfilledStopCriteria (Python parameter) — An Int specifying the number of stop criteria.")=`2`*, *[numTrackedModes](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.numTrackedModes "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.numTrackedModes (Python parameter) — An Int specifying the number of modes included in mode tracking.")=`5`*, *[objectiveFunctionDeltaStopCriteria](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.objectiveFunctionDeltaStopCriteria "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.objectiveFunctionDeltaStopCriteria (Python parameter) — A Float specifying the stop criteria based on the change in objective function.")=`None`*, *[region](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.region "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.region (Python parameter) — The SymbolicConstant MODEL or a Region object specifying the region to which the optimization task is applied.")=`abaqusConstants.MODEL`*, *[softDeletionMethod](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.softDeletionMethod "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.softDeletionMethod (Python parameter) — A SymbolicConstant specifying the method used when softDeletionRegion is specified. The STANDARD method avoids creating disconnected regions.")=`abaqusConstants.STANDARD`*, *[softDeletionRadius](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.softDeletionRadius "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.softDeletionRadius (Python parameter) — A Float specifying the radius to use when considering neighboring soft elements to delete.")=`0`*, *[softDeletionRegion](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.softDeletionRegion "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.softDeletionRegion (Python parameter) — None or a Region object specifying the region in which the soft elements should be deleted during optimization.")=`None`*, *[softDeletionThreshold](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.softDeletionThreshold "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.softDeletionThreshold (Python parameter) — A Float specifying the relative material density value used to identify soft elements. Those with values below the threshold are considered for removal.")=`None`*, *[stepSize](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.stepSize "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.stepSize (Python parameter) — A SymbolicConstant specifying the size of the increment for volume modification. Possible values are DYNAMIC, VERY_SMALL, SMALL, MODERATE, MEDIUM, and LARGE.")=`abaqusConstants.MEDIUM`*, *[stiffnessMassDamping](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.stiffnessMassDamping "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.stiffnessMassDamping (Python parameter) — The SymbolicConstant AVERAGE_EDGE_LENGTH or a Float specifying the stiffness mass damping for the task region.")=`abaqusConstants.AVERAGE_EDGE_LENGTH`*, *[stopCriteriaDesignCycle](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.stopCriteriaDesignCycle "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.stopCriteriaDesignCycle (Python parameter) — An Int specifying the first design cycle used to evaluate convergence criteria.")=`4`*, *[structuralMassDamping](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.structuralMassDamping "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.structuralMassDamping (Python parameter) — None or a Float specifying the structural mass damping for the task region.")=`None`*, *[viscousMassDamping](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.viscousMassDamping "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.viscousMassDamping (Python parameter) — None or a Float specifying the viscous mass damping for the task region.")=`None`*, *[viscousStiffnessDamping](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.viscousStiffnessDamping "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.viscousStiffnessDamping (Python parameter) — None or a Float specifying the viscous stiffness damping for the task region.")=`None`*, *[groupOperator](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.groupOperator "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.groupOperator (Python parameter) — A Boolean specifying whether the group in the design response will be evaluated using the existing algorithm or a new algorithm based on Abaqus sensitivities.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L547-L761)[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask "Permalink to this definition")
    :   This method creates a TopologyTask object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].TopologyTask
        ```

        Note

        Check [TopologyTask on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologytaskpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.name "Permalink to this definition")
            :   A String specifying the optimization task repository key.

            abaqusSensitivities=`True`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.abaqusSensitivities "Permalink to this definition")
            :   A Boolean specifying whether to use Abaqus to compute the design responses and their
                sensitivities. The default value is True.

                New in version 2019: The `abaqusSensitivities` argument was added.

            algorithm=`abaqusConstants.GENERAL_OPTIMIZATION`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.algorithm "Permalink to this definition")
            :   A SymbolicConstant specifying the optimization task algorithm. Possible values are
                GENERAL\_OPTIMIZATION and CONDITION\_BASED\_OPTIMIZATION. The default value is
                GENERAL\_OPTIMIZATION.

            densityMoveLimit=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.densityMoveLimit "Permalink to this definition")
            :   A Float specifying the maximum density change per design cycle. The default value is
                0.25.

            densityUpdateStrategy=`abaqusConstants.NORMAL`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.densityUpdateStrategy "Permalink to this definition")
            :   A SymbolicConstant specifying the strategy for how the densities are updated in the
                method of moving asymptotes. Possible values are NORMAL, CONSERVATIVE, and AGGRESSIVE.
                The default value is NORMAL.

            elementDensityDeltaStopCriteria=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.elementDensityDeltaStopCriteria "Permalink to this definition")
            :   A Float specifying the stop criteria based upon the change in element densities. The
                default value is 0.5x10⁻².

            filterRadius=`None`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.filterRadius "Permalink to this definition")
            :   None or a Float specifying the mesh filter radius for mesh independence and minimum
                size. The default value is None.

            firstCycleDeletedVolume=`5`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.firstCycleDeletedVolume "Permalink to this definition")
            :   A Float specifying the volume that can be removed immediately in the first design cycle.
                The default value is 5.0.

            firstCycleDeletedVolumeTechnique=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.firstCycleDeletedVolumeTechnique "Permalink to this definition")
            :   A SymbolicConstant specifying the method of quantifying volume that can be removed
                immediately in the first design cycle. Possible values are OFF, PERCENTAGE, and
                ABSOLUTE. The default value is OFF.

            freezeBoundaryConditionRegions=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.freezeBoundaryConditionRegions "Permalink to this definition")
            :   A Boolean specifying whether to exclude elements with boundary conditions from the
                optimization. The default value is OFF.

            freezeLoadRegions=`1`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.freezeLoadRegions "Permalink to this definition")
            :   A Boolean specifying whether to exclude elements with loads and elements with loaded
                nodes from the optimization. The default value is ON.

            frequencySpectrumWeight=`6`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.frequencySpectrumWeight "Permalink to this definition")
            :   A Float specifying the weighting factor for frequency spectrum peaks. The default value
                is 6.0.

            initialDensity=`abaqusConstants.DEFAULT`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.initialDensity "Permalink to this definition")
            :   A SymbolicConstant specifying the Optimization product default or a float specifying the
                initial density. The default value is DEFAULT.

            materialInterpolationPenalty=`3`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.materialInterpolationPenalty "Permalink to this definition")
            :   A Float specifying the penalty factor for the material interpolation technique. The
                default value is 3.0.

            materialInterpolationTechnique=`abaqusConstants.DEFAULT`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.materialInterpolationTechnique "Permalink to this definition")
            :   A SymbolicConstant specifying the material interpolation technique: optimization product
                default, solid isotropic material with penalization, or rational approximation of
                material properties. Possible values are DEFAULT, SIMP, and RAMP. The default value is
                DEFAULT.

            maxDensity=`1`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.maxDensity "Permalink to this definition")
            :   A Float specifying the maximum density in the density update. The default value is 1.0.

            minDensity=`None`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.minDensity "Permalink to this definition")
            :   A Float specifying the minimum density in the density update. The default value is 10⁻³.

            modeTrackingRegion=`abaqusConstants.MODEL`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.modeTrackingRegion "Permalink to this definition")
            :   The SymbolicConstant MODEL or a Region object specifying the region to use for mode
                tracking. The default value is MODEL.

            numDesignCycles=`15`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.numDesignCycles "Permalink to this definition")
            :   An Int specifying the number of design cycles permitted when **stepSize** is DYNAMIC. The
                default value is 15.

            numFulfilledStopCriteria=`2`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.numFulfilledStopCriteria "Permalink to this definition")
            :   An Int specifying the number of stop criteria. The default value is 2.

            numTrackedModes=`5`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.numTrackedModes "Permalink to this definition")
            :   An Int specifying the number of modes included in mode tracking. The default value is 5.

            objectiveFunctionDeltaStopCriteria=`None`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.objectiveFunctionDeltaStopCriteria "Permalink to this definition")
            :   A Float specifying the stop criteria based on the change in objective function. The
                default value is 10⁻³.

            region=`abaqusConstants.MODEL`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.region "Permalink to this definition")
            :   The SymbolicConstant MODEL or a Region object specifying the region to which the
                optimization task is applied. The default value is MODEL.

            softDeletionMethod=`abaqusConstants.STANDARD`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.softDeletionMethod "Permalink to this definition")
            :   A SymbolicConstant specifying the method used when **softDeletionRegion** is specified.
                The STANDARD method avoids creating disconnected regions. The AGGRESSIVE method only
                considers the **softDeletionThreshold**. The MAX\_SHEAR\_STRAIN, MAX\_ELASTOPLASTIC\_STRAIN
                and VOLUME\_COMPRESSION methods do not need the **softDeletionRadius**. Possible values are
                STANDARD, AGGRESSIVE, MAX\_SHEAR\_STRAIN, MIN\_PRINCIPAL\_STRAIN, MAX\_ELASTOPLASTIC\_STRAIN
                and VOLUME\_COMPRESSION. The default value is STANDARD.

            softDeletionRadius=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.softDeletionRadius "Permalink to this definition")
            :   A Float specifying the radius to use when considering neighboring soft elements to
                delete. The default value is 0.0.

            softDeletionRegion=`None`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.softDeletionRegion "Permalink to this definition")
            :   None or a Region object specifying the region in which the soft elements should be
                deleted during optimization. The default value is None.

            softDeletionThreshold=`None`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.softDeletionThreshold "Permalink to this definition")
            :   A Float specifying the relative material density value used to identify soft elements.
                Those with values below the threshold are considered for removal. For STANDARD and
                AGGRESSIVE methods positive values are accepted and the default value is 0.05. For
                MAX\_SHEAR\_STRAIN and MAX\_ELASTOPLASTIC\_STRAIN methods positive values are accepted
                whereas for MIN\_PRINCIPAL\_STRAIN and VOLUME\_COMPRESSION methods negative values are
                accepted.

            stepSize=`abaqusConstants.MEDIUM`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.stepSize "Permalink to this definition")
            :   A SymbolicConstant specifying the size of the increment for volume modification.
                Possible values are DYNAMIC, VERY\_SMALL, SMALL, MODERATE, MEDIUM, and LARGE. The default
                value is MEDIUM.

            stiffnessMassDamping=`abaqusConstants.AVERAGE_EDGE_LENGTH`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.stiffnessMassDamping "Permalink to this definition")
            :   The SymbolicConstant AVERAGE\_EDGE\_LENGTH or a Float specifying the stiffness mass
                damping for the task region. The default value is AVERAGE\_EDGE\_LENGTH.

            stopCriteriaDesignCycle=`4`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.stopCriteriaDesignCycle "Permalink to this definition")
            :   An Int specifying the first design cycle used to evaluate convergence criteria. The
                default value is 4.

            structuralMassDamping=`None`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.structuralMassDamping "Permalink to this definition")
            :   None or a Float specifying the structural mass damping for the task region. The default
                value is None.

            viscousMassDamping=`None`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.viscousMassDamping "Permalink to this definition")
            :   None or a Float specifying the viscous mass damping for the task region. The default
                value is None.

            viscousStiffnessDamping=`None`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.viscousStiffnessDamping "Permalink to this definition")
            :   None or a Float specifying the viscous stiffness damping for the task region. The
                default value is None.

            groupOperator=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask.groupOperator "Permalink to this definition")
            :   A Boolean specifying whether the group in the design response will be evaluated using
                the existing algorithm or a new algorithm based on Abaqus sensitivities. The default
                value of False means that the existing algorithm will be used.

                New in version 2022: The `groupOperator` argument was added.

        Returns:[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask-returns "Permalink to this headline")
        :   A TopologyTask object.

        Return type:[¶](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask-return-type "Permalink to this headline")
        :   [`TopologyTask`](#abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask "abaqus.Optimization.OptimizationTaskModel.OptimizationTaskModel.TopologyTask (Python method) — This method creates a TopologyTask object.")

## Assign features to optimization tasks[¶](#assign-features-to-optimization-tasks "Permalink to this heading")

*class* OptimizationTask[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L80-L2197)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask "Permalink to this definition")
:   Bases: [`OptimizationTaskBase`](#abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase "abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase (Python class) — Bases: object")

    Public Data Attributes:

    Inherited from [`OptimizationTaskBase`](#abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase "abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | [`name`](#abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase.name "abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase.name (Python attribute) — A String specifying the optimization task repository key.") | A String specifying the optimization task repository key. |
    | [`region`](#abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase.region "abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase.region (Python attribute) — The SymbolicConstant MODEL or a Region object specifying the region to which the optimization task is applied. The default value is MODEL.") | The SymbolicConstant MODEL or a Region object specifying the region to which the optimization task is applied. |
    | [`designResponses`](#abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase.designResponses "abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase.designResponses (Python attribute) — A repository of DesignResponse objects.") | A repository of DesignResponse objects. |
    | [`objectiveFunctions`](#abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase.objectiveFunctions "abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase.objectiveFunctions (Python attribute) — A repository of ObjectiveFunction objects.") | A repository of ObjectiveFunction objects. |
    | [`optimizationConstraints`](#abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase.optimizationConstraints "abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase.optimizationConstraints (Python attribute) — A repository of OptimizationConstraint objects.") | A repository of OptimizationConstraint objects. |
    | [`geometricRestrictions`](#abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase.geometricRestrictions "abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase.geometricRestrictions (Python attribute) — A repository of GeometricRestriction objects.") | A repository of GeometricRestriction objects. |
    | [`stopConditions`](#abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase.stopConditions "abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase.stopConditions (Python attribute) — A repository of StopCondition objects.") | A repository of StopCondition objects. |

    Public Methods:

    |  |  |
    | --- | --- |
    | [`SingleTermDesignResponse`](#abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse "abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse (Python method) — This method creates a SingleTermDesignResponse object.")(name, identifier[, ...]) | This method creates a SingleTermDesignResponse object. |
    | [`ObjectiveFunction`](#abaqus.Optimization.OptimizationTask.OptimizationTask.ObjectiveFunction "abaqus.Optimization.OptimizationTask.OptimizationTask.ObjectiveFunction (Python method) — This method creates an ObjectiveFunction object.")(name, objectives[, target]) | This method creates an ObjectiveFunction object. |
    | [`OptimizationConstraint`](#abaqus.Optimization.OptimizationTask.OptimizationTask.OptimizationConstraint "abaqus.Optimization.OptimizationTask.OptimizationTask.OptimizationConstraint (Python method) — This method creates an OptimizationConstraint object.")(name, designResponse, ...) | This method creates an OptimizationConstraint object. |
    | [`BeadFilter`](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFilter "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFilter (Python method) — This method creates a BeadFilter object.")(name, region[, radius, ...]) | This method creates a BeadFilter object. |
    | [`BeadFixedRegion`](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion (Python method) — This method creates a BeadFixedRegion object.")(name, region[, csys, u1, u2, u3]) | This method creates a BeadFixedRegion object. |
    | [`BeadGrowth`](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadGrowth "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadGrowth (Python method) — This method creates a BeadGrowth object.")(name, region[, beadGrowth, shrink]) | This method creates a BeadGrowth object. |
    | [`BeadPenetrationCheck`](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPenetrationCheck "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPenetrationCheck (Python method) — This method creates a BeadPenetrationCheck object.")(name, ...) | This method creates a BeadPenetrationCheck object. |
    | [`BeadPlanarSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPlanarSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPlanarSymmetry (Python method) — This method creates a BeadPlanarSymmetry object.")(name, region[, axis, csys]) | This method creates a BeadPlanarSymmetry object. |
    | [`BeadPointSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPointSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPointSymmetry (Python method) — This method creates a BeadPointSymmetry object.")(name, region[, csys]) | This method creates a BeadPointSymmetry object. |
    | [`BeadRotationalSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadRotationalSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadRotationalSymmetry (Python method) — This method creates a BeadRotationalSymmetry object.")(name, angle, region) | This method creates a BeadRotationalSymmetry object. |
    | [`DesignDirection`](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection "abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection (Python method) — This method creates a DesignDirection object.")(name, region[, csys, ...]) | This method creates a DesignDirection object. |
    | [`DrillControl`](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl "abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl (Python method) — This method creates a DrillControl object.")(name, clientDirection, region) | This method creates a DrillControl object. |
    | [`FixedRegion`](#abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion "abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion (Python method) — This method creates a FixedRegion object.")(name, region[, csys, ...]) | This method creates a FixedRegion object. |
    | [`FrozenArea`](#abaqus.Optimization.OptimizationTask.OptimizationTask.FrozenArea "abaqus.Optimization.OptimizationTask.OptimizationTask.FrozenArea (Python method) — This method creates a FrozenArea object.")(name[, region]) | This method creates a FrozenArea object. |
    | [`Growth`](#abaqus.Optimization.OptimizationTask.OptimizationTask.Growth "abaqus.Optimization.OptimizationTask.OptimizationTask.Growth (Python method) — This method creates a Growth object.")(name, region[, growth, ...]) | This method creates a Growth object. |
    | [`PenetrationCheck`](#abaqus.Optimization.OptimizationTask.OptimizationTask.PenetrationCheck "abaqus.Optimization.OptimizationTask.OptimizationTask.PenetrationCheck (Python method) — This method creates a PenetrationCheck object.")(name, ...[, ...]) | This method creates a PenetrationCheck object. |
    | [`ShapeDemoldControl`](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl (Python method) — This method creates a ShapeDemoldControl object.")(name, pullDirection, region) | This method creates a ShapeDemoldControl object. |
    | [`ShapeMemberSize`](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize (Python method) — This method creates a ShapeMemberSize object.")(name, region[, ...]) | This method creates a ShapeMemberSize object. |
    | [`ShapePlanarSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry (Python method) — This method creates a ShapePlanarSymmetry object.")(name, clientDirection, ...) | This method creates a ShapePlanarSymmetry object. |
    | [`ShapePointSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry (Python method) — This method creates a ShapePointSymmetry object.")(name, region[, csys, ...]) | This method creates a ShapePointSymmetry object. |
    | [`ShapeRotationalSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry (Python method) — This method creates a ShapeRotationalSymmetry object.")(name, ...[, ...]) | This method creates a ShapeRotationalSymmetry object. |
    | [`SizingClusterAreas`](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingClusterAreas "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingClusterAreas (Python method) — This method creates a SizingClusterAreas object.")(name, regions) | This method creates a SizingClusterAreas object. |
    | [`SizingCyclicSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry (Python method) — This method creates a SizingCyclicSymmetry object.")(name, region, translation) | This method creates a SizingCyclicSymmetry object. |
    | [`SizingFrozenArea`](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingFrozenArea "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingFrozenArea (Python method) — This method creates a SizingFrozenArea object.")(name, region) | This method creates a SizingFrozenArea object. |
    | [`SizingMemberSize`](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingMemberSize "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingMemberSize (Python method) — This method creates a SizingMemberSize object.")(name, region, minWidth) | This method creates a SizingMemberSize object. |
    | [`SizingPlanarSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPlanarSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPlanarSymmetry (Python method) — This method creates a SizingPlanarSymmetry object.")(name, region[, axis, ...]) | This method creates a SizingPlanarSymmetry object. |
    | [`SizingPointSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPointSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPointSymmetry (Python method) — This method creates a SizingPointSymmetry object.")(name, region[, csys, ...]) | This method creates a SizingPointSymmetry object. |
    | [`SizingRotationalSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry (Python method) — This method creates a SizingRotationalSymmetry object.")(name, angle, region) | This method creates a SizingRotationalSymmetry object. |
    | [`SlideRegionControl`](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl "abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl (Python method) — This method creates a SlideRegionControl object.")(name, clientDirection, region) | This method creates a SlideRegionControl object. |
    | [`StampControl`](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl "abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl (Python method) — This method creates a StampControl object.")(name, clientDirection, region) | This method creates a StampControl object. |
    | [`TopologyCyclicSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry (Python method) — This method creates a TopologyCyclicSymmetry object.")(name, region, translation) | This method creates a TopologyCyclicSymmetry object. |
    | [`TopologyDemoldControl`](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl (Python method) — This method creates a TopologyDemoldControl object.")(name, region[, csys, ...]) | This method creates a TopologyDemoldControl object. |
    | [`TopologyMemberSize`](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize (Python method) — This method creates a TopologyMemberSize object.")(name, region[, ...]) | This method creates a TopologyMemberSize object. |
    | [`TopologyMillingControl`](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl (Python method) — This method creates a TopologyMillingControl object.")(name, ...[, csys, ...]) | This method creates a TopologyMillingControl object. |
    | [`TopologyOverhangControl`](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl (Python method) — This method creates a TopologyOverhangControl object.")(name, pullDirection, ...) | This method creates a TopologyOverhangControl object. |
    | [`TopologyPlanarSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPlanarSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPlanarSymmetry (Python method) — This method creates a TopologyPlanarSymmetry object.")(name, region[, axis, ...]) | This method creates a TopologyPlanarSymmetry object. |
    | [`TopologyPointSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPointSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPointSymmetry (Python method) — This method creates a TopologyPointSymmetry object.")(name, region[, csys, ...]) | This method creates a TopologyPointSymmetry object. |
    | [`TopologyRibDesign`](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign (Python method) — This method creates a TopologyRibDesign object.")(name, ribDirection, ...[, ...]) | This method creates a TopologyRibDesign object. |
    | [`TopologyRotationalSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry (Python method) — This method creates a TopologyRotationalSymmetry object.")(name, angle, region) | This method creates a TopologyRotationalSymmetry object. |
    | [`TurnControl`](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl "abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl (Python method) — This method creates a TurnControl object.")(name, clientDirection, region[, ...]) | This method creates a TurnControl object. |

    ---

    Member Details:

    BeadFilter(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFilter.name "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFilter.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFilter.region "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFilter.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied.")*, *[radius](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFilter.radius "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFilter.radius (Python parameter) — A Float specifying the filter radius.")=`None`*, *[filterRadiusBy](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFilter.filterRadiusBy "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFilter.filterRadiusBy (Python parameter) — The SymbolicConstant defines whether the filter radius is in absolute or relative units.")=`abaqusConstants.ABSOLUTE_VALUE`*, *[filterCheckRegion](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFilter.filterCheckRegion "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFilter.filterCheckRegion (Python parameter) — The SymbolicConstant FILTER_REGION or a Region object specifying the filter check region.")=`abaqusConstants.FILTER_REGION`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L235-L280)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFilter "Permalink to this definition")
    :   This method creates a BeadFilter object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].BeadFilter
        ```

        New in version 2023.

        The `BeadFilter` method was added.

        Note

        Check [BeadFilter on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadfilterpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFilter-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFilter.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFilter.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.

            radius=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFilter.radius "Permalink to this definition")
            :   A Float specifying the filter radius. The default value is double the average edge length of the model.

            filterRadiusBy=`abaqusConstants.ABSOLUTE_VALUE`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFilter.filterRadiusBy "Permalink to this definition")
            :   The SymbolicConstant defines whether the filter radius is in absolute or relative units. For an absolute
                radius, the value is ABSOLUTE\_VALUE. For a relative radius, the value is RELATIVE. The default value is
                ABSOLUTE\_VALUE.

            filterCheckRegion=`abaqusConstants.FILTER_REGION`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFilter.filterCheckRegion "Permalink to this definition")
            :   The SymbolicConstant FILTER\_REGION or a Region object specifying the filter check region. If the value is
                FILTER\_REGION, the value of the region is used as both the filter region and the filter check region.
                The default value is FILTER\_REGION.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFilter-returns "Permalink to this headline")
        :   A BeadFilter object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFilter-return-type "Permalink to this headline")
        :   [`BeadFilter`](#abaqus.Optimization.OptimizationTask.BeadFilter "abaqus.Optimization.OptimizationTask.BeadFilter (Python class) — Bases: GeometricRestriction")

    BeadFixedRegion(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion.name "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion.region "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied.")*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[u1](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion.u1 "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion.u1 (Python parameter) — A Boolean specifying whether to fix the region in the 1-direction.")=`0`*, *[u2](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion.u2 "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion.u2 (Python parameter) — A Boolean specifying whether to fix the region in the 2-direction.")=`0`*, *[u3](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion.u3 "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion.u3 (Python parameter) — A Boolean specifying whether to fix the region in the 3-direction.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L282-L325)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion "Permalink to this definition")
    :   This method creates a BeadFixedRegion object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].BeadFixedRegion
        ```

        Note

        Check [BeadFixedRegion on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadfixedregionpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            u1=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion.u1 "Permalink to this definition")
            :   A Boolean specifying whether to fix the region in the 1-direction. The default value is
                OFF.

            u2=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion.u2 "Permalink to this definition")
            :   A Boolean specifying whether to fix the region in the 2-direction. The default value is
                OFF.

            u3=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion.u3 "Permalink to this definition")
            :   A Boolean specifying whether to fix the region in the 3-direction. The default value is
                OFF.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion-returns "Permalink to this headline")
        :   A BeadFixedRegion object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadFixedRegion-return-type "Permalink to this headline")
        :   [`BeadFixedRegion`](#abaqus.Optimization.OptimizationTask.BeadFixedRegion "abaqus.Optimization.OptimizationTask.BeadFixedRegion (Python class) — Bases: GeometricRestriction")

    BeadGrowth(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadGrowth.name "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadGrowth.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadGrowth.region "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadGrowth.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied.")*, *[beadGrowth](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadGrowth.beadGrowth "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadGrowth.beadGrowth (Python parameter) — A Float specifying the maximum optimization displacement in the growth direction.")=`0`*, *[shrink](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadGrowth.shrink "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadGrowth.shrink (Python parameter) — A Float specifying the maximum optimization displacement in the shrink direction.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L327-L355)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadGrowth "Permalink to this definition")
    :   This method creates a BeadGrowth object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].BeadGrowth
        ```

        Note

        Check [BeadGrowth on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadgrowthpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadGrowth-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadGrowth.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadGrowth.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.

            beadGrowth=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadGrowth.beadGrowth "Permalink to this definition")
            :   A Float specifying the maximum optimization displacement in the growth direction. Either
                **beadGrowth** or **shrink** or both must be specified. The default value is 0.0.

            shrink=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadGrowth.shrink "Permalink to this definition")
            :   A Float specifying the maximum optimization displacement in the shrink direction. Either
                **beadGrowth** or **shrink** or both must be specified The default value is 0.0.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadGrowth-returns "Permalink to this headline")
        :   A BeadGrowth object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadGrowth-return-type "Permalink to this headline")
        :   [`BeadGrowth`](#abaqus.Optimization.OptimizationTask.BeadGrowth "abaqus.Optimization.OptimizationTask.BeadGrowth (Python class) — Bases: GeometricRestriction")

    BeadPenetrationCheck(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPenetrationCheck.name "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPenetrationCheck.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[beadPenetrationCheckRegion](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPenetrationCheck.beadPenetrationCheckRegion "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPenetrationCheck.beadPenetrationCheckRegion (Python parameter) — A Region object specifying the penetration check region.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPenetrationCheck.region "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPenetrationCheck.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L357-L385)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPenetrationCheck "Permalink to this definition")
    :   This method creates a BeadPenetrationCheck object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].BeadPenetrationCheck
        ```

        Note

        Check [BeadPenetrationCheck on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadpenetrationcheckpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPenetrationCheck-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPenetrationCheck.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            beadPenetrationCheckRegion[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPenetrationCheck.beadPenetrationCheckRegion "Permalink to this definition")
            :   A Region object specifying the penetration check region.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPenetrationCheck.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPenetrationCheck-returns "Permalink to this headline")
        :   A BeadPenetrationCheck object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPenetrationCheck-return-type "Permalink to this headline")
        :   [`BeadPenetrationCheck`](#abaqus.Optimization.OptimizationTask.BeadPenetrationCheck "abaqus.Optimization.OptimizationTask.BeadPenetrationCheck (Python class) — Bases: GeometricRestriction")

    BeadPlanarSymmetry(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPlanarSymmetry.name "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPlanarSymmetry.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPlanarSymmetry.region "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPlanarSymmetry.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied.")*, *[axis](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPlanarSymmetry.axis "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPlanarSymmetry.axis (Python parameter) — A SymbolicConstant specifying the axis of symmetry.")=`abaqusConstants.AXIS_1`*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPlanarSymmetry.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPlanarSymmetry.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L387-L422)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPlanarSymmetry "Permalink to this definition")
    :   This method creates a BeadPlanarSymmetry object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].BeadPlanarSymmetry
        ```

        Note

        Check [BeadPlanarSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadplanarsymmetrypyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPlanarSymmetry-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPlanarSymmetry.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPlanarSymmetry.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.

            axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPlanarSymmetry.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS\_1, AXIS\_2,
                and AXIS\_3. The default value is AXIS\_1.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPlanarSymmetry.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPlanarSymmetry-returns "Permalink to this headline")
        :   A BeadPlanarSymmetry object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPlanarSymmetry-return-type "Permalink to this headline")
        :   [`BeadPlanarSymmetry`](#abaqus.Optimization.OptimizationTask.BeadPlanarSymmetry "abaqus.Optimization.OptimizationTask.BeadPlanarSymmetry (Python class) — Bases: GeometricRestriction")

    BeadPointSymmetry(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPointSymmetry.name "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPointSymmetry.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPointSymmetry.region "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPointSymmetry.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied.")*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPointSymmetry.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPointSymmetry.csys (Python parameter) — None or a DatumCsys object specifying the position of the symmetry point defined as the origin of a local coordinate system.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L424-L450)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPointSymmetry "Permalink to this definition")
    :   This method creates a BeadPointSymmetry object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].BeadPointSymmetry
        ```

        Note

        Check [BeadPointSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadpointsymmetrypyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPointSymmetry-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPointSymmetry.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPointSymmetry.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPointSymmetry.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the position of the symmetry point defined as the
                origin of a local coordinate system. If **csys** = None, the global coordinate system is
                used. When this member is queried, it returns an Int. The default value is None.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPointSymmetry-returns "Permalink to this headline")
        :   A BeadPointSymmetry object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadPointSymmetry-return-type "Permalink to this headline")
        :   [`BeadPointSymmetry`](#abaqus.Optimization.OptimizationTask.BeadPointSymmetry "abaqus.Optimization.OptimizationTask.BeadPointSymmetry (Python class) — Bases: GeometricRestriction")

    BeadRotationalSymmetry(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadRotationalSymmetry.name "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadRotationalSymmetry.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[angle](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadRotationalSymmetry.angle "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadRotationalSymmetry.angle (Python parameter) — A Float specifying the repeating segment size, an angle in degrees.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadRotationalSymmetry.region "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadRotationalSymmetry.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied.")*, *[axis](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadRotationalSymmetry.axis "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadRotationalSymmetry.axis (Python parameter) — A SymbolicConstant specifying the axis of symmetry.")=`abaqusConstants.AXIS_1`*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadRotationalSymmetry.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.BeadRotationalSymmetry.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L452-L492)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadRotationalSymmetry "Permalink to this definition")
    :   This method creates a BeadRotationalSymmetry object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].BeadRotationalSymmetry
        ```

        Note

        Check [BeadRotationalSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadrotationalsymmetrypyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadRotationalSymmetry-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadRotationalSymmetry.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            angle[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadRotationalSymmetry.angle "Permalink to this definition")
            :   A Float specifying the repeating segment size, an angle in degrees.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadRotationalSymmetry.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.

            axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadRotationalSymmetry.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS\_1, AXIS\_2,
                and AXIS\_3. The default value is AXIS\_1.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadRotationalSymmetry.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadRotationalSymmetry-returns "Permalink to this headline")
        :   A BeadRotationalSymmetry object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.BeadRotationalSymmetry-return-type "Permalink to this headline")
        :   [`BeadRotationalSymmetry`](#abaqus.Optimization.OptimizationTask.BeadRotationalSymmetry "abaqus.Optimization.OptimizationTask.BeadRotationalSymmetry (Python class) — Bases: GeometricRestriction")

    DesignDirection(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.name "abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.region "abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied. When used with a TopologyTask, there is no default value.")*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[mainPoint](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.mainPoint "abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.mainPoint (Python parameter) — None or a Region object specifying the main point used when mainPointDetermination is SPECIFY.")=`None`*, *[mainPointDetermination](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.mainPointDetermination "abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.mainPointDetermination (Python parameter) — A SymbolicConstant specifying the rule for assigning point priority.")=`abaqusConstants.MAXIMUM`*, *[movementRestriction](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.movementRestriction "abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.movementRestriction (Python parameter) — A SymbolicConstant specifying whether movement in the region should follow only the direction of the mainPoint, only the magnitude, or both the magnitude of the mainPoint and the directions specified by u1, u2 and u3.")=`abaqusConstants.VECTOR`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.presumeFeasibleRegionAtStart "abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.presumeFeasibleRegionAtStart (Python parameter) — A Boolean specifying whether to ignore the geometric restriction in the first design cycle.")=`1`*, *[u1](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.u1 "abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.u1 (Python parameter) — A Boolean specifying whether movement in the region should follow the masterPoint in the 1-direction.")=`1`*, *[u2](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.u2 "abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.u2 (Python parameter) — A Boolean specifying whether movement in the region should follow the masterPoint in the 2-direction.")=`1`*, *[u3](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.u3 "abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.u3 (Python parameter) — A Boolean specifying whether movement in the region should follow the masterPoint in the 3-direction.")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L494-L577)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection "Permalink to this definition")
    :   This method creates a DesignDirection object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].DesignDirection
        ```

        Note

        Check [DesignDirection on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-designdirectionpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.
                When used with a TopologyTask, there is no default value. When used with a ShapeTask,
                the default value is MODEL.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            mainPoint=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.mainPoint "Permalink to this definition")
            :   None or a Region object specifying the main point used when **mainPointDetermination** is
                SPECIFY. The default value is None.

                Changed in version 2022: The argument `masterPoint` was renamed to `mainPoint`.

            mainPointDetermination=`abaqusConstants.MAXIMUM`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.mainPointDetermination "Permalink to this definition")
            :   A SymbolicConstant specifying the rule for assigning point priority. Possible values are
                MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.

                Changed in version 2022: The argument `masterPointDetermination` was renamed to `mainPointDetermination`.

            movementRestriction=`abaqusConstants.VECTOR`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.movementRestriction "Permalink to this definition")
            :   A SymbolicConstant specifying whether movement in the region should follow only the
                direction of the **mainPoint**, only the magnitude, or both the magnitude of the
                **mainPoint** and the directions specified by **u1**, **u2** and **u3**. Possible values are
                DIRECTION, MAGNITUDE, and VECTOR. The default value is VECTOR.

            presumeFeasibleRegionAtStart=`1`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.presumeFeasibleRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore the geometric restriction in the first design
                cycle. The default value is ON.

            u1=`1`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.u1 "Permalink to this definition")
            :   A Boolean specifying whether movement in the region should follow the **masterPoint** in
                the 1-direction. This is used when **movementRestriction** is VECTOR. The default value is
                ON.

            u2=`1`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.u2 "Permalink to this definition")
            :   A Boolean specifying whether movement in the region should follow the **masterPoint** in
                the 2-direction. This is used when **movementRestriction** is VECTOR. The default value is
                ON.

            u3=`1`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection.u3 "Permalink to this definition")
            :   A Boolean specifying whether movement in the region should follow the **masterPoint** in
                the 3-direction. This is used when **movementRestriction** is VECTOR. The default value is
                ON.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection-returns "Permalink to this headline")
        :   A DesignDirection object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DesignDirection-return-type "Permalink to this headline")
        :   [`DesignDirection`](#abaqus.Optimization.OptimizationTask.DesignDirection "abaqus.Optimization.OptimizationTask.DesignDirection (Python class) — Bases: GeometricRestriction")

    DrillControl(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.name "abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[clientDirection](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.clientDirection "abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.clientDirection (Python parameter) — A VertexArray object of length 2 specifying the direction of the drill axis positioned at the csys origin.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.region "abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied. When used with a TopologyTask, there is no default value.")*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[drawAngle](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.drawAngle "abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.drawAngle (Python parameter) — A Float specifying the draw angle.")=`0`*, *[mainPoint](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.mainPoint "abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.mainPoint (Python parameter) — None or a Region object specifying the main point used when mainPointDetermination is SPECIFY.")=`None`*, *[mainPointDetermination](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.mainPointDetermination "abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.mainPointDetermination (Python parameter) — A SymbolicConstant specifying the rule for assigning point priority.")=`abaqusConstants.MAXIMUM`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.presumeFeasibleRegionAtStart "abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.presumeFeasibleRegionAtStart (Python parameter) — A Boolean specifying whether to ignore the geometric restriction in the first design cycle.")=`1`*, *[tolerance1](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.tolerance1 "abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.tolerance1 (Python parameter) — A Float specifying the geometric tolerance in the 1-direction.")=`0`*, *[tolerance2](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.tolerance2 "abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.tolerance2 (Python parameter) — A Float specifying the geometric tolerance in the 2-direction.")=`0`*, *[tolerance3](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.tolerance3 "abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.tolerance3 (Python parameter) — A Float specifying the geometric tolerance in the 3-direction.")=`0`*, *[undercutTolerance](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.undercutTolerance "abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.undercutTolerance (Python parameter) — A Float specifying the undercut tolerance.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L579-L666)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl "Permalink to this definition")
    :   This method creates a DrillControl object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].DrillControl
        ```

        Note

        Check [DrillControl on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-drillcontrolpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            clientDirection[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.clientDirection "Permalink to this definition")
            :   A VertexArray object of length 2 specifying the direction of the drill axis positioned
                at the **csys** origin. Instead of through a ConstrainedSketchVertex, each point may be specified through a
                tuple of coordinates.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.
                When used with a TopologyTask, there is no default value. When used with a ShapeTask,
                the default value is MODEL.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            drawAngle=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.drawAngle "Permalink to this definition")
            :   A Float specifying the draw angle. The default value is 0.0.

            mainPoint=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.mainPoint "Permalink to this definition")
            :   None or a Region object specifying the main point used when **mainPointDetermination** is
                SPECIFY. The default value is None.

                Changed in version 2022: The argument `masterPoint` was renamed to `mainPoint`.

            mainPointDetermination=`abaqusConstants.MAXIMUM`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.mainPointDetermination "Permalink to this definition")
            :   A SymbolicConstant specifying the rule for assigning point priority. Possible values are
                MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.

                Changed in version 2022: The argument `masterPointDetermination` was renamed to `mainPointDetermination`.

            presumeFeasibleRegionAtStart=`1`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.presumeFeasibleRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore the geometric restriction in the first design
                cycle. The default value is ON.

            tolerance1=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.tolerance1 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 1-direction. The default value is
                0.01.

            tolerance2=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.tolerance2 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 2-direction. The default value is
                0.01.

            tolerance3=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.tolerance3 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 3-direction. The default value is
                0.01.

            undercutTolerance=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl.undercutTolerance "Permalink to this definition")
            :   A Float specifying the undercut tolerance. The default value is 0.0.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl-returns "Permalink to this headline")
        :   A DrillControl object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.DrillControl-return-type "Permalink to this headline")
        :   [`DrillControl`](#abaqus.Optimization.OptimizationTask.DrillControl "abaqus.Optimization.OptimizationTask.DrillControl (Python class) — Bases: GeometricRestriction")

    FixedRegion(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion.name "abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion.region "abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied. When used with a TopologyTask, there is no default value.")*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion.presumeFeasibleRegionAtStart "abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion.presumeFeasibleRegionAtStart (Python parameter) — A Boolean specifying whether to ignore the geometric restriction in the first design cycle.")=`1`*, *[u1](#abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion.u1 "abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion.u1 (Python parameter) — A Boolean specifying whether to fix the region in the 1-direction.")=`0`*, *[u2](#abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion.u2 "abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion.u2 (Python parameter) — A Boolean specifying whether to fix the region in the 2-direction.")=`0`*, *[u3](#abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion.u3 "abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion.u3 (Python parameter) — A Boolean specifying whether to fix the region in the 3-direction.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L668-L719)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion "Permalink to this definition")
    :   This method creates a FixedRegion object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].FixedRegion
        ```

        Note

        Check [FixedRegion on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fixedregionpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.
                When used with a TopologyTask, there is no default value. When used with a ShapeTask,
                the default value is MODEL.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            presumeFeasibleRegionAtStart=`1`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion.presumeFeasibleRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore the geometric restriction in the first design
                cycle. The default value is ON.

            u1=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion.u1 "Permalink to this definition")
            :   A Boolean specifying whether to fix the region in the 1-direction. The default value is
                OFF.

            u2=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion.u2 "Permalink to this definition")
            :   A Boolean specifying whether to fix the region in the 2-direction. The default value is
                OFF.

            u3=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion.u3 "Permalink to this definition")
            :   A Boolean specifying whether to fix the region in the 3-direction. The default value is
                OFF.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion-returns "Permalink to this headline")
        :   A FixedRegion object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.FixedRegion-return-type "Permalink to this headline")
        :   [`FixedRegion`](#abaqus.Optimization.OptimizationTask.FixedRegion "abaqus.Optimization.OptimizationTask.FixedRegion (Python class) — Bases: GeometricRestriction")

    FrozenArea(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.FrozenArea.name "abaqus.Optimization.OptimizationTask.OptimizationTask.FrozenArea.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[region=<abaqus.Region.Region.Region object>](#abaqus.Optimization.OptimizationTask.OptimizationTask.FrozenArea "abaqus.Optimization.OptimizationTask.OptimizationTask.FrozenArea.region=<abaqus.Region.Region.Region object> (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L721-L745)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.FrozenArea "Permalink to this definition")
    :   This method creates a FrozenArea object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].FrozenArea
        ```

        Note

        Check [FrozenArea on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-frozenareapyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.FrozenArea-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.FrozenArea.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            region : [`Region`](part_assembly/region.html#abaqus.Region.Surface.Region "abaqus.Region.Region.Region (Python class)"), default: `<abaqus.Region.Region.Region object at 0x7f850cd6fed0>`
            :   A Region object specifying the region to which the geometric restriction is applied.
                When used with a TopologyTask, there is no default value. When used with a ShapeTask,
                the default value is MODEL.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.FrozenArea-returns "Permalink to this headline")
        :   A FrozenArea object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.FrozenArea-return-type "Permalink to this headline")
        :   [`FrozenArea`](#abaqus.Optimization.OptimizationTask.FrozenArea "abaqus.Optimization.OptimizationTask.FrozenArea (Python class) — Bases: GeometricRestriction")

    Growth(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.Growth.name "abaqus.Optimization.OptimizationTask.OptimizationTask.Growth.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.Growth.region "abaqus.Optimization.OptimizationTask.OptimizationTask.Growth.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied. When used with a TopologyTask, there is no default value.")*, *[growth](#abaqus.Optimization.OptimizationTask.OptimizationTask.Growth.growth "abaqus.Optimization.OptimizationTask.OptimizationTask.Growth.growth (Python parameter) — A Float specifying the maximum optimization displacement in the growth direction.")=`0`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.OptimizationTask.OptimizationTask.Growth.presumeFeasibleRegionAtStart "abaqus.Optimization.OptimizationTask.OptimizationTask.Growth.presumeFeasibleRegionAtStart (Python parameter) — A Boolean specifying whether to ignore the geometric restriction in the first design cycle.")=`1`*, *[shrink](#abaqus.Optimization.OptimizationTask.OptimizationTask.Growth.shrink "abaqus.Optimization.OptimizationTask.OptimizationTask.Growth.shrink (Python parameter) — A Float specifying the maximum optimization displacement in the shrink direction.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L747-L789)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.Growth "Permalink to this definition")
    :   This method creates a Growth object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].Growth
        ```

        Note

        Check [Growth on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-growthpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.Growth-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.Growth.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.Growth.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.
                When used with a TopologyTask, there is no default value. When used with a ShapeTask,
                the default value is MODEL.

            growth=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.Growth.growth "Permalink to this definition")
            :   A Float specifying the maximum optimization displacement in the growth direction. Either
                **growth** or **shrink** or both must be specified. The default value is 0.0.

            presumeFeasibleRegionAtStart=`1`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.Growth.presumeFeasibleRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore the geometric restriction in the first design
                cycle. The default value is ON.

            shrink=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.Growth.shrink "Permalink to this definition")
            :   A Float specifying the maximum optimization displacement in the shrink direction. Either
                **growth** or **shrink** or both must be specified The default value is 0.0.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.Growth-returns "Permalink to this headline")
        :   A Growth object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.Growth-return-type "Permalink to this headline")
        :   [`Growth`](#abaqus.Optimization.OptimizationTask.Growth "abaqus.Optimization.OptimizationTask.Growth (Python class) — Bases: GeometricRestriction")

    ObjectiveFunction(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.ObjectiveFunction.name "abaqus.Optimization.OptimizationTask.OptimizationTask.ObjectiveFunction.name (Python parameter) — A String specifying the objective function repository key.")*, *[objectives](#abaqus.Optimization.OptimizationTask.OptimizationTask.ObjectiveFunction.objectives "abaqus.Optimization.OptimizationTask.OptimizationTask.ObjectiveFunction.objectives (Python parameter) — An OptimizationObjectiveArray object.")*, *[target](#abaqus.Optimization.OptimizationTask.OptimizationTask.ObjectiveFunction.target "abaqus.Optimization.OptimizationTask.OptimizationTask.ObjectiveFunction.target (Python parameter) — A SymbolicConstant specifying the target of the objective function.")=`abaqusConstants.MINIMIZE`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L147-L182)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ObjectiveFunction "Permalink to this definition")
    :   This method creates an ObjectiveFunction object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].ObjectiveFunction
        ```

        Note

        Check [ObjectiveFunction on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-objectivefunctionpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ObjectiveFunction-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ObjectiveFunction.name "Permalink to this definition")
            :   A String specifying the objective function repository key.

            objectives[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ObjectiveFunction.objectives "Permalink to this definition")
            :   An OptimizationObjectiveArray object.

            target=`abaqusConstants.MINIMIZE`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ObjectiveFunction.target "Permalink to this definition")
            :   A SymbolicConstant specifying the target of the objective function. Possible values are
                MINIMIZE, MAXIMIZE, and MINIMIZE\_MAXIMUM. The default value is MINIMIZE.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ObjectiveFunction-returns "Permalink to this headline")
        :   An ObjectiveFunction object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ObjectiveFunction-return-type "Permalink to this headline")
        :   [`ObjectiveFunction`](#abaqus.Optimization.OptimizationTask.OptimizationTask.ObjectiveFunction "abaqus.Optimization.OptimizationTask.OptimizationTask.ObjectiveFunction (Python method) — This method creates an ObjectiveFunction object.")

        Raises:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ObjectiveFunction-raises "Permalink to this headline")
        :   * **InvalidNameError** –
            * **RangeError** –

    OptimizationConstraint(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.OptimizationConstraint.name "abaqus.Optimization.OptimizationTask.OptimizationTask.OptimizationConstraint.name (Python parameter) — A String specifying the optimization constraint repository key.")*, *[designResponse](#abaqus.Optimization.OptimizationTask.OptimizationTask.OptimizationConstraint.designResponse "abaqus.Optimization.OptimizationTask.OptimizationTask.OptimizationConstraint.designResponse (Python parameter) — A String specifying the name of the design response to constrain.")*, *[restrictionValue](#abaqus.Optimization.OptimizationTask.OptimizationTask.OptimizationConstraint.restrictionValue "abaqus.Optimization.OptimizationTask.OptimizationTask.OptimizationConstraint.restrictionValue (Python parameter) — A Float specifying the value to which the design response should be constrained.")*, *[restrictionMethod](#abaqus.Optimization.OptimizationTask.OptimizationTask.OptimizationConstraint.restrictionMethod "abaqus.Optimization.OptimizationTask.OptimizationTask.OptimizationConstraint.restrictionMethod (Python parameter) — A SymbolicConstant specifying the method used to constrain the design response.")=`abaqusConstants.ABSOLUTE_EQUAL`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L184-L233)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.OptimizationConstraint "Permalink to this definition")
    :   This method creates an OptimizationConstraint object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].OptimizationConstraint
        ```

        Note

        Check [OptimizationConstraint on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optimizationconstraintpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.OptimizationConstraint-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.OptimizationConstraint.name "Permalink to this definition")
            :   A String specifying the optimization constraint repository key.

            designResponse[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.OptimizationConstraint.designResponse "Permalink to this definition")
            :   A String specifying the name of the design response to constrain.

            restrictionValue[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.OptimizationConstraint.restrictionValue "Permalink to this definition")
            :   A Float specifying the value to which the design response should be constrained.

            restrictionMethod=`abaqusConstants.ABSOLUTE_EQUAL`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.OptimizationConstraint.restrictionMethod "Permalink to this definition")
            :   A SymbolicConstant specifying the method used to constrain the design response. Possible
                values are ABSOLUTE\_EQUAL, ABSOLUTE\_GREATER\_THAN\_EQUAL, ABSOLUTE\_LESS\_THAN\_EQUAL,
                RELATIVE\_EQUAL, RELATIVE\_GREATER\_THAN\_EQUAL, and RELATIVE\_LESS\_THAN\_EQUAL. The default
                value is ABSOLUTE\_EQUAL.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.OptimizationConstraint-returns "Permalink to this headline")
        :   An OptimizationConstraint object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.OptimizationConstraint-return-type "Permalink to this headline")
        :   [`OptimizationConstraint`](#abaqus.Optimization.OptimizationTask.OptimizationTask.OptimizationConstraint "abaqus.Optimization.OptimizationTask.OptimizationTask.OptimizationConstraint (Python method) — This method creates an OptimizationConstraint object.")

        Raises:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.OptimizationConstraint-raises "Permalink to this headline")
        :   * **InvalidNameError** –
            * **RangeError** –

    PenetrationCheck(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.PenetrationCheck.name "abaqus.Optimization.OptimizationTask.OptimizationTask.PenetrationCheck.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[penetrationCheckRegion](#abaqus.Optimization.OptimizationTask.OptimizationTask.PenetrationCheck.penetrationCheckRegion "abaqus.Optimization.OptimizationTask.OptimizationTask.PenetrationCheck.penetrationCheckRegion (Python parameter) — A Region object specifying the penetration check region.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.PenetrationCheck.region "abaqus.Optimization.OptimizationTask.OptimizationTask.PenetrationCheck.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied. When used with a TopologyTask, there is no default value.")*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.OptimizationTask.OptimizationTask.PenetrationCheck.presumeFeasibleRegionAtStart "abaqus.Optimization.OptimizationTask.OptimizationTask.PenetrationCheck.presumeFeasibleRegionAtStart (Python parameter) — A Boolean specifying whether to ignore the geometric restriction in the first design cycle.")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L791-L828)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.PenetrationCheck "Permalink to this definition")
    :   This method creates a PenetrationCheck object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].PenetrationCheck
        ```

        Note

        Check [PenetrationCheck on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-penetrationcheckpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.PenetrationCheck-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.PenetrationCheck.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            penetrationCheckRegion[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.PenetrationCheck.penetrationCheckRegion "Permalink to this definition")
            :   A Region object specifying the penetration check region.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.PenetrationCheck.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.
                When used with a TopologyTask, there is no default value. When used with a ShapeTask,
                the default value is MODEL.

            presumeFeasibleRegionAtStart=`1`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.PenetrationCheck.presumeFeasibleRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore the geometric restriction in the first design
                cycle. The default value is ON.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.PenetrationCheck-returns "Permalink to this headline")
        :   A PenetrationCheck object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.PenetrationCheck-return-type "Permalink to this headline")
        :   [`PenetrationCheck`](#abaqus.Optimization.OptimizationTask.OptimizationTask.PenetrationCheck "abaqus.Optimization.OptimizationTask.OptimizationTask.PenetrationCheck (Python method) — This method creates a PenetrationCheck object.")

    ShapeDemoldControl(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.name "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[pullDirection](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.pullDirection "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.pullDirection (Python parameter) — A VertexArray object of length 2 specifying the demold pull direction.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.region "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied. When used with a TopologyTask, there is no default value.")*, *[collisionCheckRegion](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.collisionCheckRegion "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.collisionCheckRegion (Python parameter) — The SymbolicConstant DEMOLD_REGION or a Region object specifying the collision check region.")=`abaqusConstants.DEMOLD_REGION`*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the pullDirection.")=`None`*, *[drawAngle](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.drawAngle "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.drawAngle (Python parameter) — A Float specifying the draw angle.")=`0`*, *[mainPointDetermination](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.mainPointDetermination "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.mainPointDetermination (Python parameter) — A SymbolicConstant specifying the rule for assigning point priority.")=`abaqusConstants.MAXIMUM`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.presumeFeasibleRegionAtStart "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.presumeFeasibleRegionAtStart (Python parameter) — A Boolean specifying whether to ignore the geometric restriction in the first design cycle.")=`1`*, *[tolerance1](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.tolerance1 "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.tolerance1 (Python parameter) — A Float specifying the geometric tolerance in the 1-direction.")=`0`*, *[tolerance2](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.tolerance2 "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.tolerance2 (Python parameter) — A Float specifying the geometric tolerance in the 2-direction.")=`0`*, *[tolerance3](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.tolerance3 "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.tolerance3 (Python parameter) — A Float specifying the geometric tolerance in the 3-direction.")=`0`*, *[undercutTolerance](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.undercutTolerance "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.undercutTolerance (Python parameter) — A Float specifying the undercut tolerance.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L830-L915)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl "Permalink to this definition")
    :   This method creates a ShapeDemoldControl object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].ShapeDemoldControl
        ```

        Note

        Check [ShapeDemoldControl on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapedemoldcontrolpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            pullDirection[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.pullDirection "Permalink to this definition")
            :   A VertexArray object of length 2 specifying the demold pull direction. Instead of
                through a ConstrainedSketchVertex, each point might be specified through a tuple of coordinates.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.
                When used with a TopologyTask, there is no default value. When used with a ShapeTask,
                the default value is MODEL.

            collisionCheckRegion=`abaqusConstants.DEMOLD_REGION`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.collisionCheckRegion "Permalink to this definition")
            :   The SymbolicConstant DEMOLD\_REGION or a Region object specifying the collision check
                region. If the value is DEMOLD\_REGION, then the value of **region** is used as both the
                demold region and the collision check region. The default value is DEMOLD\_REGION.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the
                **pullDirection**. If **csys** = None, the global coordinate system is used. When this member
                is queried, it returns an Int indicating the identifier of the DatumCsys. The default
                value is None.

            drawAngle=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.drawAngle "Permalink to this definition")
            :   A Float specifying the draw angle. The default value is 0.0.

            mainPointDetermination=`abaqusConstants.MAXIMUM`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.mainPointDetermination "Permalink to this definition")
            :   A SymbolicConstant specifying the rule for assigning point priority. Possible values are
                MAXIMUM and MINIMUM. The default value is MAXIMUM.

                Changed in version 2022: The argument `masterPointDetermination` was renamed to `mainPointDetermination`.

            presumeFeasibleRegionAtStart=`1`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.presumeFeasibleRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore the geometric restriction in the first design
                cycle. The default value is ON.

            tolerance1=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.tolerance1 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 1-direction. The default value is
                0.01.

            tolerance2=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.tolerance2 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 2-direction. The default value is
                0.01.

            tolerance3=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.tolerance3 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 3-direction. The default value is
                0.01.

            undercutTolerance=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl.undercutTolerance "Permalink to this definition")
            :   A Float specifying the undercut tolerance. The default value is 0.0.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl-returns "Permalink to this headline")
        :   A ShapeDemoldControl object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl-return-type "Permalink to this headline")
        :   [`ShapeDemoldControl`](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeDemoldControl (Python method) — This method creates a ShapeDemoldControl object.")

    ShapeMemberSize(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize.name "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize.region "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied. When used with a TopologyTask, there is no default value.")*, *[maxThickness](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize.maxThickness "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize.maxThickness (Python parameter) — A Float specifying the maximum thickness.")=`0`*, *[minThickness](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize.minThickness "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize.minThickness (Python parameter) — A Float specifying the minimum thickness.")=`0`*, *[sizeRestriction](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize.sizeRestriction "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize.sizeRestriction (Python parameter) — A SymbolicConstant specifying whether to restrict the minimum or maximum thickness. Possible values are MAXIMUM and MINIMUM.")=`abaqusConstants.MINIMUM`*, *[assignNodeGroupRegion](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize.assignNodeGroupRegion "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize.assignNodeGroupRegion (Python parameter) — A bool specifying whether to use the node group region.")=`0`*, *[nodeGroupRegion](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize.nodeGroupRegion "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize.nodeGroupRegion (Python parameter) — A Node Region object specifying the check node group.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L917-L975)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize "Permalink to this definition")
    :   This method creates a ShapeMemberSize object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].ShapeMemberSize
        ```

        Note

        Check [ShapeMemberSize on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapemembersizepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.
                When used with a TopologyTask, there is no default value. When used with a ShapeTask,
                the default value is MODEL.

            maxThickness=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize.maxThickness "Permalink to this definition")
            :   A Float specifying the maximum thickness. The default value is 0.0.

            minThickness=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize.minThickness "Permalink to this definition")
            :   A Float specifying the minimum thickness. The default value is 0.0.

            sizeRestriction=`abaqusConstants.MINIMUM`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize.sizeRestriction "Permalink to this definition")
            :   A SymbolicConstant specifying whether to restrict the minimum or maximum thickness.
                Possible values are MAXIMUM and MINIMUM. The default value is MINIMUM.

            assignNodeGroupRegion=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize.assignNodeGroupRegion "Permalink to this definition")
            :   A bool specifying whether to use the node group region. The default value is OFF.

                New in version 2022: The `assignNodeGroupRegion` argument was added.

            nodeGroupRegion=`''`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize.nodeGroupRegion "Permalink to this definition")
            :   A Node Region object specifying the check node group.

                New in version 2022: The `nodeGroupRegion` argument was added.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize-returns "Permalink to this headline")
        :   A ShapeMemberSize object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize-return-type "Permalink to this headline")
        :   [`ShapeMemberSize`](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeMemberSize (Python method) — This method creates a ShapeMemberSize object.")

    ShapePlanarSymmetry(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.name "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[clientDirection](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.clientDirection "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.clientDirection (Python parameter) — A VertexArray object of length 2 specifying the vector positioned at the csys origin that is normal to the symmetry plane.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.region "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied. When used with a TopologyTask, there is no default value.")*, *[allowNonSymmetricMesh](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.allowNonSymmetricMesh "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.allowNonSymmetricMesh (Python parameter) — A Boolean specifying whether to allow a nonsymmetric mesh for this geometric restriction.")=`True`*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[mainPointDetermination](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.mainPointDetermination "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.mainPointDetermination (Python parameter) — A SymbolicConstant specifying the rule for determining the main node.")=`abaqusConstants.MAXIMUM`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.presumeFeasibleRegionAtStart "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.presumeFeasibleRegionAtStart (Python parameter) — A Boolean specifying whether to ignore the geometric restriction in the first design cycle.")=`1`*, *[tolerance1](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.tolerance1 "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.tolerance1 (Python parameter) — A Float specifying the geometric tolerance in the 1-direction.")=`0`*, *[tolerance2](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.tolerance2 "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.tolerance2 (Python parameter) — A Float specifying the geometric tolerance in the 2-direction.")=`0`*, *[tolerance3](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.tolerance3 "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.tolerance3 (Python parameter) — A Float specifying the geometric tolerance in the 3-direction.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L977-L1056)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry "Permalink to this definition")
    :   This method creates a ShapePlanarSymmetry object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].ShapePlanarSymmetry
        ```

        Note

        Check [ShapePlanarSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapeplanarsymmetrypyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            clientDirection[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.clientDirection "Permalink to this definition")
            :   A VertexArray object of length 2 specifying the vector positioned at the **csys** origin
                that is normal to the symmetry plane. Instead of through a ConstrainedSketchVertex, each point may be
                specified through a tuple of coordinates.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.
                When used with a TopologyTask, there is no default value. When used with a ShapeTask,
                the default value is MODEL.

            allowNonSymmetricMesh=`True`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.allowNonSymmetricMesh "Permalink to this definition")
            :   A Boolean specifying whether to allow a nonsymmetric mesh for this geometric
                restriction. The default value is TRUE.

                New in version 2021: The `alloowNonSymmetricMesh` argument was added.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            mainPointDetermination=`abaqusConstants.MAXIMUM`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.mainPointDetermination "Permalink to this definition")
            :   A SymbolicConstant specifying the rule for determining the main node. Possible values
                are MAXIMUM and MINIMUM. The default value is MAXIMUM.

                Changed in version 2022: The argument `masterPointDetermination` was renamed to `mainPointDetermination`.

            presumeFeasibleRegionAtStart=`1`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.presumeFeasibleRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore the geometric restriction in the first design
                cycle. The default value is ON.

            tolerance1=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.tolerance1 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 1-direction. The default value is
                0.01.

            tolerance2=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.tolerance2 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 2-direction. The default value is
                0.01.

            tolerance3=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry.tolerance3 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 3-direction. The default value is
                0.01.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry-returns "Permalink to this headline")
        :   A ShapePlanarSymmetry object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry-return-type "Permalink to this headline")
        :   [`ShapePlanarSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePlanarSymmetry (Python method) — This method creates a ShapePlanarSymmetry object.")

    ShapePointSymmetry(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry.name "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry.region "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied. When used with a TopologyTask, there is no default value.")*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry.csys (Python parameter) — None or a DatumCsys object specifying the symmetry point represented as the origin of a local coordinate system.")=`None`*, *[mainPointDetermination](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry.mainPointDetermination "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry.mainPointDetermination (Python parameter) — A SymbolicConstant specifying the rule for determining the main node.")=`abaqusConstants.MAXIMUM`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry.presumeFeasibleRegionAtStart "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry.presumeFeasibleRegionAtStart (Python parameter) — A Boolean specifying whether to ignore the geometric restriction in the first design cycle.")=`1`*, *[tolerance1](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry.tolerance1 "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry.tolerance1 (Python parameter) — A Float specifying the geometric tolerance in the 1-direction.")=`0`*, *[tolerance2](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry.tolerance2 "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry.tolerance2 (Python parameter) — A Float specifying the geometric tolerance in the 2-direction.")=`0`*, *[tolerance3](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry.tolerance3 "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry.tolerance3 (Python parameter) — A Float specifying the geometric tolerance in the 3-direction.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L1058-L1123)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry "Permalink to this definition")
    :   This method creates a ShapePointSymmetry object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].ShapePointSymmetry
        ```

        Note

        Check [ShapePointSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapepointsymmetrypyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.
                When used with a TopologyTask, there is no default value. When used with a ShapeTask,
                the default value is MODEL.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the symmetry point represented as the origin of a
                local coordinate system. If **csys** = None, the global coordinate system is used. When this
                member is queried, it returns an Int. The default value is None.

            mainPointDetermination=`abaqusConstants.MAXIMUM`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry.mainPointDetermination "Permalink to this definition")
            :   A SymbolicConstant specifying the rule for determining the main node. Possible values
                are MAXIMUM and MINIMUM. The default value is MAXIMUM.

                Changed in version 2022: The argument `masterPointDetermination` was renamed to `mainPointDetermination`.

            presumeFeasibleRegionAtStart=`1`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry.presumeFeasibleRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore the geometric restriction in the first design
                cycle. The default value is ON.

            tolerance1=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry.tolerance1 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 1-direction. The default value is
                0.01.

            tolerance2=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry.tolerance2 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 2-direction. The default value is
                0.01.

            tolerance3=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry.tolerance3 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 3-direction. The default value is
                0.01.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry-returns "Permalink to this headline")
        :   A ShapePointSymmetry object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry-return-type "Permalink to this headline")
        :   [`ShapePointSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapePointSymmetry (Python method) — This method creates a ShapePointSymmetry object.")

    ShapeRotationalSymmetry(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.name "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[clientDirection](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.clientDirection "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.clientDirection (Python parameter) — A VertexArray object of length 2 specifying the vector positioned at the csys origin, used as the axis of symmetry.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.region "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied. When used with a TopologyTask, there is no default value.")*, *[allowNonSymmetricMesh](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.allowNonSymmetricMesh "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.allowNonSymmetricMesh (Python parameter) — A Boolean specifying whether to allow a nonsymmetric mesh for this geometric restriction.")=`True`*, *[angle](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.angle "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.angle (Python parameter) — A Float specifying the segment size of the repeating pattern in degrees.")=`0`*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[mainPoint](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.mainPoint "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.mainPoint (Python parameter) — None or a Region object specifying the main point used when mainPointDetermination is SPECIFY.")=`None`*, *[mainPointDetermination](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.mainPointDetermination "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.mainPointDetermination (Python parameter) — A SymbolicConstant specifying the rule for determining the main node.")=`abaqusConstants.MAXIMUM`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.presumeFeasibleRegionAtStart "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.presumeFeasibleRegionAtStart (Python parameter) — A Boolean specifying whether to ignore the geometric restriction in the first design cycle.")=`1`*, *[startPoint](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.startPoint "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.startPoint (Python parameter) — A tuple of Floats representing the coordinates of a start point of the rotational symmetry.")=`None`*, *[tolerance1](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.tolerance1 "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.tolerance1 (Python parameter) — A Float specifying the geometric tolerance in the 1-direction.")=`0`*, *[tolerance2](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.tolerance2 "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.tolerance2 (Python parameter) — A Float specifying the geometric tolerance in the 2-direction.")=`0`*, *[tolerance3](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.tolerance3 "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.tolerance3 (Python parameter) — A Float specifying the geometric tolerance in the 3-direction.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L1125-L1222)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry "Permalink to this definition")
    :   This method creates a ShapeRotationalSymmetry object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].ShapeRotationalSymmetry
        ```

        Note

        Check [ShapeRotationalSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shaperotationalsymmetrypyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            clientDirection[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.clientDirection "Permalink to this definition")
            :   A VertexArray object of length 2 specifying the vector positioned at the **csys** origin,
                used as the axis of symmetry. Instead of through a ConstrainedSketchVertex, each point might be specified
                through a tuple of coordinates.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.
                When used with a TopologyTask, there is no default value. When used with a ShapeTask,
                the default value is MODEL.

            allowNonSymmetricMesh=`True`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.allowNonSymmetricMesh "Permalink to this definition")
            :   A Boolean specifying whether to allow a nonsymmetric mesh for this geometric
                restriction. The default value is TRUE.

                New in version 2021: The `alloowNonSymmetricMesh` argument was added.

            angle=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.angle "Permalink to this definition")
            :   A Float specifying the segment size of the repeating pattern in degrees. If the **angle**
                value is 0, no repeating pattern is created. The default value is 0.0.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            mainPoint=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.mainPoint "Permalink to this definition")
            :   None or a Region object specifying the main point used when **mainPointDetermination** is
                SPECIFY. The default value is None.

                Changed in version 2022: The argument `masterPoint` was renamed to `mainPoint`.

            mainPointDetermination=`abaqusConstants.MAXIMUM`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.mainPointDetermination "Permalink to this definition")
            :   A SymbolicConstant specifying the rule for determining the main node. Possible values
                are MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.

                Changed in version 2022: The argument `masterPointDetermination` was renamed to `mainPointDetermination`.

            presumeFeasibleRegionAtStart=`1`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.presumeFeasibleRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore the geometric restriction in the first design
                cycle. The default value is ON.

            startPoint=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.startPoint "Permalink to this definition")
            :   A tuple of Floats representing the coordinates of a start point of the rotational
                symmetry.

            tolerance1=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.tolerance1 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 1-direction. The default value is
                0.01.

            tolerance2=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.tolerance2 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 2-direction. The default value is
                0.01.

            tolerance3=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry.tolerance3 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 3-direction. The default value is
                0.01.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry-returns "Permalink to this headline")
        :   A ShapeRotationalSymmetry object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry-return-type "Permalink to this headline")
        :   [`ShapeRotationalSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.ShapeRotationalSymmetry (Python method) — This method creates a ShapeRotationalSymmetry object.")

    SingleTermDesignResponse(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse.name "abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse.name (Python parameter) — A String specifying the design response repository key.")*, *[identifier](#abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse.identifier "abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse.identifier (Python parameter) — A String specifying the name of the variable identifier.")*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[drivingRegion](#abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse.drivingRegion "abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse.drivingRegion (Python parameter) — None or a sequence of Floats specifying the driving region used when identifier is an internal nodal variable.")=`None`*, *[operation](#abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse.operation "abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse.operation (Python parameter) — A SymbolicConstant specifying the operation used on values in the region.")=`abaqusConstants.SUM`*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse.region "abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse.region (Python parameter) — The SymbolicConstant MODEL or a Region object specifying the region of the design response variable.")=`abaqusConstants.MODEL`*, *[shellLayer](#abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse.shellLayer "abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse.shellLayer (Python parameter) — A SymbolicConstant specifying the location used for shell layer values.")=`abaqusConstants.MAXIMUM`*, *[stepOptions](#abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse.stepOptions "abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse.stepOptions (Python parameter) — A StepOptionArray object.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L82-L145)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse "Permalink to this definition")
    :   This method creates a SingleTermDesignResponse object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].SingleTermDesignResponse
        ```

        Changed in version 2024: The argument stepOperation was removed.

        Note

        Check [SingleTermDesignResponse on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-singletermdesignresponsepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse.name "Permalink to this definition")
            :   A String specifying the design response repository key.

            identifier[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse.identifier "Permalink to this definition")
            :   A String specifying the name of the variable identifier.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            drivingRegion=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse.drivingRegion "Permalink to this definition")
            :   None or a sequence of Floats specifying the driving region used when **identifier** is an
                internal nodal variable. The default value is None.

            operation=`abaqusConstants.SUM`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse.operation "Permalink to this definition")
            :   A SymbolicConstant specifying the operation used on values in the region. Possible
                values are MAXIMUM, MINIMUM, and SUM. The default value is SUM.

            region=`abaqusConstants.MODEL`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse.region "Permalink to this definition")
            :   The SymbolicConstant MODEL or a Region object specifying the region of the design
                response variable. The default value is MODEL.

            shellLayer=`abaqusConstants.MAXIMUM`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse.shellLayer "Permalink to this definition")
            :   A SymbolicConstant specifying the location used for shell layer values. Possible values
                are BOTTOM, MAXIMUM, MIDDLE, MINIMUM, and TOP. The default value is MAXIMUM.

            stepOptions=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse.stepOptions "Permalink to this definition")
            :   A StepOptionArray object.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse-returns "Permalink to this headline")
        :   A SingleTermDesignResponse object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse-return-type "Permalink to this headline")
        :   [`SingleTermDesignResponse`](#abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse "abaqus.Optimization.OptimizationTask.OptimizationTask.SingleTermDesignResponse (Python method) — This method creates a SingleTermDesignResponse object.")

    SizingClusterAreas(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingClusterAreas.name "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingClusterAreas.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[regions](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingClusterAreas.regions "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingClusterAreas.regions (Python parameter) — Tuple of Region objects specifying the regions to which the geometric restriction is applied.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L1224-L1247)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingClusterAreas "Permalink to this definition")
    :   This method creates a SizingClusterAreas object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].SizingClusterAreas
        ```

        Note

        Check [SizingClusterAreas on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingclusterareaspyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingClusterAreas-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingClusterAreas.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            regions[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingClusterAreas.regions "Permalink to this definition")
            :   Tuple of Region objects specifying the regions to which the geometric restriction is
                applied.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingClusterAreas-returns "Permalink to this headline")
        :   A SizingClusterAreas object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingClusterAreas-return-type "Permalink to this headline")
        :   [`SizingClusterAreas`](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingClusterAreas "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingClusterAreas (Python method) — This method creates a SizingClusterAreas object.")

    SizingCyclicSymmetry(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry.name "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry.region "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied.")*, *[translation](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry.translation "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry.translation (Python parameter) — A Float specifying the translation distance.")*, *[axis](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry.axis "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry.axis (Python parameter) — A SymbolicConstant specifying the translation direction defined along an axis positioned at the csys origin.")=`abaqusConstants.AXIS_1`*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[ignoreFrozenArea](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry.ignoreFrozenArea "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry.ignoreFrozenArea (Python parameter) — A Boolean specifying whether to ignore frozen areas.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L1249-L1293)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry "Permalink to this definition")
    :   This method creates a SizingCyclicSymmetry object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].SizingCyclicSymmetry
        ```

        Note

        Check [SizingCyclicSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingcyclicsymmetrypyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.

            translation[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry.translation "Permalink to this definition")
            :   A Float specifying the translation distance.

            axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the translation direction defined along an axis positioned
                at the **csys** origin. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default value
                is AXIS\_1.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            ignoreFrozenArea=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry.ignoreFrozenArea "Permalink to this definition")
            :   A Boolean specifying whether to ignore frozen areas. The default value is OFF.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry-returns "Permalink to this headline")
        :   A SizingCyclicSymmetry object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry-return-type "Permalink to this headline")
        :   [`SizingCyclicSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingCyclicSymmetry (Python method) — This method creates a SizingCyclicSymmetry object.")

    SizingFrozenArea(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingFrozenArea.name "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingFrozenArea.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingFrozenArea.region "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingFrozenArea.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L1295-L1317)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingFrozenArea "Permalink to this definition")
    :   This method creates a SizingFrozenArea object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].SizingFrozenArea
        ```

        Note

        Check [SizingFrozenArea on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingfrozenareapyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingFrozenArea-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingFrozenArea.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingFrozenArea.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingFrozenArea-returns "Permalink to this headline")
        :   A SizingFrozenArea object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingFrozenArea-return-type "Permalink to this headline")
        :   [`SizingFrozenArea`](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingFrozenArea "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingFrozenArea (Python method) — This method creates a SizingFrozenArea object.")

    SizingMemberSize(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingMemberSize.name "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingMemberSize.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingMemberSize.region "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingMemberSize.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied.")*, *[minWidth](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingMemberSize.minWidth "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingMemberSize.minWidth (Python parameter) — A Float specifying the min width.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L1319-L1344)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingMemberSize "Permalink to this definition")
    :   This method creates a SizingMemberSize object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].SizingMemberSize
        ```

        Note

        Check [SizingMemberSize on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingmembersizepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingMemberSize-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingMemberSize.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingMemberSize.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.

            minWidth[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingMemberSize.minWidth "Permalink to this definition")
            :   A Float specifying the min width.

    SizingPlanarSymmetry(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPlanarSymmetry.name "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPlanarSymmetry.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPlanarSymmetry.region "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPlanarSymmetry.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied.")*, *[axis](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPlanarSymmetry.axis "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPlanarSymmetry.axis (Python parameter) — A SymbolicConstant specifying the axis of symmetry.")=`abaqusConstants.AXIS_1`*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPlanarSymmetry.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPlanarSymmetry.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[ignoreFrozenArea](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPlanarSymmetry.ignoreFrozenArea "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPlanarSymmetry.ignoreFrozenArea (Python parameter) — A Boolean specifying whether to ignore frozen areas.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L1346-L1386)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPlanarSymmetry "Permalink to this definition")
    :   This method creates a SizingPlanarSymmetry object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].SizingPlanarSymmetry
        ```

        Note

        Check [SizingPlanarSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingplanarsymmetrypyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPlanarSymmetry-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPlanarSymmetry.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPlanarSymmetry.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.

            axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPlanarSymmetry.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS\_1, AXIS\_2,
                and AXIS\_3. The default value is AXIS\_1.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPlanarSymmetry.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            ignoreFrozenArea=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPlanarSymmetry.ignoreFrozenArea "Permalink to this definition")
            :   A Boolean specifying whether to ignore frozen areas. The default value is OFF.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPlanarSymmetry-returns "Permalink to this headline")
        :   A SizingPlanarSymmetry object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPlanarSymmetry-return-type "Permalink to this headline")
        :   [`SizingPlanarSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPlanarSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPlanarSymmetry (Python method) — This method creates a SizingPlanarSymmetry object.")

    SizingPointSymmetry(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPointSymmetry.name "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPointSymmetry.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPointSymmetry.region "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPointSymmetry.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied.")*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPointSymmetry.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPointSymmetry.csys (Python parameter) — None or a DatumCsys object specifying the position of the symmetry point defined as the origin of a local coordinate system.")=`None`*, *[ignoreFrozenArea](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPointSymmetry.ignoreFrozenArea "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPointSymmetry.ignoreFrozenArea (Python parameter) — A Boolean specifying whether to ignore frozen areas.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L1388-L1424)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPointSymmetry "Permalink to this definition")
    :   This method creates a SizingPointSymmetry object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].SizingPointSymmetry
        ```

        Note

        Check [SizingPointSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingpointsymmetrypyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPointSymmetry-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPointSymmetry.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPointSymmetry.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPointSymmetry.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the position of the symmetry point defined as the
                origin of a local coordinate system. If **csys** = None, the global coordinate system is
                used. When this member is queried, it returns an Int. The default value is None.

            ignoreFrozenArea=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPointSymmetry.ignoreFrozenArea "Permalink to this definition")
            :   A Boolean specifying whether to ignore frozen areas. The default value is OFF.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPointSymmetry-returns "Permalink to this headline")
        :   A SizingPointSymmetry object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPointSymmetry-return-type "Permalink to this headline")
        :   [`SizingPointSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPointSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingPointSymmetry (Python method) — This method creates a SizingPointSymmetry object.")

    SizingRotationalSymmetry(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry.name "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[angle](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry.angle "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry.angle (Python parameter) — A Float specifying the repeating segment size, an angle in degrees.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry.region "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied.")*, *[axis](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry.axis "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry.axis (Python parameter) — A SymbolicConstant specifying the axis of symmetry.")=`abaqusConstants.AXIS_1`*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[ignoreFrozenArea](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry.ignoreFrozenArea "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry.ignoreFrozenArea (Python parameter) — A Boolean specifying whether to ignore frozen areas.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L1426-L1469)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry "Permalink to this definition")
    :   This method creates a SizingRotationalSymmetry object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].SizingRotationalSymmetry
        ```

        Note

        Check [SizingRotationalSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingrotationalsymmetrypyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            angle[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry.angle "Permalink to this definition")
            :   A Float specifying the repeating segment size, an angle in degrees.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.

            axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS\_1, AXIS\_2,
                and AXIS\_3. The default value is AXIS\_1.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            ignoreFrozenArea=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry.ignoreFrozenArea "Permalink to this definition")
            :   A Boolean specifying whether to ignore frozen areas. The default value is OFF.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry-returns "Permalink to this headline")
        :   A SizingRotationalSymmetry object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry-return-type "Permalink to this headline")
        :   [`SizingRotationalSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.SizingRotationalSymmetry (Python method) — This method creates a SizingRotationalSymmetry object.")

    SlideRegionControl(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.name "abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[clientDirection](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.clientDirection "abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.clientDirection (Python parameter) — A VertexArray object of length 2 specifying the axis of revolution.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.region "abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied. When used with a TopologyTask, there is no default value.")*, *[approach](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.approach "abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.approach (Python parameter) — A SymbolicConstant specifying the restriction approach.")=`abaqusConstants.FREE_FORM`*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[freeFormRegion](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.freeFormRegion "abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.freeFormRegion (Python parameter) — None or a Region object specifying the free-form region.")=`None`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.presumeFeasibleRegionAtStart "abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.presumeFeasibleRegionAtStart (Python parameter) — A Boolean specifying whether to ignore the geometric restriction in the first design cycle.")=`1`*, *[revolvedRegion](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.revolvedRegion "abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.revolvedRegion (Python parameter) — None or a Region object specifying the region to revolve into a slide region.")=`None`*, *[tolerance1](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.tolerance1 "abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.tolerance1 (Python parameter) — A Float specifying the geometric tolerance in the 1-direction.")=`0`*, *[tolerance2](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.tolerance2 "abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.tolerance2 (Python parameter) — A Float specifying the geometric tolerance in the 2-direction.")=`0`*, *[tolerance3](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.tolerance3 "abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.tolerance3 (Python parameter) — A Float specifying the geometric tolerance in the 3-direction.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L1471-L1551)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl "Permalink to this definition")
    :   This method creates a SlideRegionControl object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].SlideRegionControl
        ```

        Note

        Check [SlideRegionControl on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-slideregioncontrolpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            clientDirection[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.clientDirection "Permalink to this definition")
            :   A VertexArray object of length 2 specifying the axis of revolution. Instead of through a
                ConstrainedSketchVertex, each point may be specified through a tuple of coordinates. This is used when
                **approach** is TURN.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.
                When used with a TopologyTask, there is no default value. When used with a ShapeTask,
                the default value is MODEL.

            approach=`abaqusConstants.FREE_FORM`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.approach "Permalink to this definition")
            :   A SymbolicConstant specifying the restriction approach. The SymbolicConstant FREE\_FORM
                indicates a free-form slide region, and the SymbolicConstant TURN indicates that the
                restriction should conserve a turnable surface. Possible values are FREE\_FORM and TURN.
                The default value is FREE\_FORM.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. This
                is used when **approach** is TURN. The default value is None.

            freeFormRegion=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.freeFormRegion "Permalink to this definition")
            :   None or a Region object specifying the free-form region. This is used when **approach** is
                FREE\_FORM. The default value is None.

            presumeFeasibleRegionAtStart=`1`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.presumeFeasibleRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore the geometric restriction in the first design
                cycle. The default value is ON.

            revolvedRegion=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.revolvedRegion "Permalink to this definition")
            :   None or a Region object specifying the region to revolve into a slide region. This is
                used when **approach** is TURN. The default value is None.

            tolerance1=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.tolerance1 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 1-direction. This is used when
                **approach** is TURN. The default value is 0.01.

            tolerance2=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.tolerance2 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 2-direction. This is used when
                **approach** is TURN. The default value is 0.01.

            tolerance3=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl.tolerance3 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 3-direction. This is used when
                **approach** is TURN. The default value is 0.01.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl-returns "Permalink to this headline")
        :   A SlideRegionControl object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl-return-type "Permalink to this headline")
        :   [`SlideRegionControl`](#abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl "abaqus.Optimization.OptimizationTask.OptimizationTask.SlideRegionControl (Python method) — This method creates a SlideRegionControl object.")

    StampControl(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.name "abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[clientDirection](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.clientDirection "abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.clientDirection (Python parameter) — A VertexArray object of length 2 specifying the stamping direction.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.region "abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied. When used with a TopologyTask, there is no default value.")*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[drawAngle](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.drawAngle "abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.drawAngle (Python parameter) — A Float specifying the draw angle.")=`0`*, *[mainPoint](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.mainPoint "abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.mainPoint (Python parameter) — None or a Region object specifying the main point used when mainPointDetermination is SPECIFY.")=`None`*, *[mainPointDetermination](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.mainPointDetermination "abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.mainPointDetermination (Python parameter) — A SymbolicConstant specifying the rule for assigning point priority.")=`abaqusConstants.MAXIMUM`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.presumeFeasibleRegionAtStart "abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.presumeFeasibleRegionAtStart (Python parameter) — A Boolean specifying whether to ignore the geometric restriction in the first design cycle.")=`1`*, *[tolerance1](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.tolerance1 "abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.tolerance1 (Python parameter) — A Float specifying the geometric tolerance in the 1-direction.")=`0`*, *[tolerance2](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.tolerance2 "abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.tolerance2 (Python parameter) — A Float specifying the geometric tolerance in the 2-direction.")=`0`*, *[tolerance3](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.tolerance3 "abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.tolerance3 (Python parameter) — A Float specifying the geometric tolerance in the 3-direction.")=`0`*, *[undercutTolerance](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.undercutTolerance "abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.undercutTolerance (Python parameter) — A Float specifying the undercut tolerance.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L1553-L1639)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl "Permalink to this definition")
    :   This method creates a StampControl object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].StampControl
        ```

        Note

        Check [StampControl on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stampcontrolpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            clientDirection[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.clientDirection "Permalink to this definition")
            :   A VertexArray object of length 2 specifying the stamping direction. Instead of through a
                ConstrainedSketchVertex, each point may be specified through a tuple of coordinates.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.
                When used with a TopologyTask, there is no default value. When used with a ShapeTask,
                the default value is MODEL.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            drawAngle=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.drawAngle "Permalink to this definition")
            :   A Float specifying the draw angle. The default value is 0.0.

            mainPoint=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.mainPoint "Permalink to this definition")
            :   None or a Region object specifying the main point used when **mainPointDetermination** is
                SPECIFY. The default value is None.

                Changed in version 2022: The argument `masterPoint` was renamed to `mainPoint`.

            mainPointDetermination=`abaqusConstants.MAXIMUM`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.mainPointDetermination "Permalink to this definition")
            :   A SymbolicConstant specifying the rule for assigning point priority. Possible values are
                MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.

                Changed in version 2022: The argument `masterPointDetermination` was renamed to `mainPointDetermination`.

            presumeFeasibleRegionAtStart=`1`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.presumeFeasibleRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore the geometric restriction in the first design
                cycle. The default value is ON.

            tolerance1=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.tolerance1 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 1-direction. The default value is
                0.01.

            tolerance2=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.tolerance2 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 2-direction. The default value is
                0.01.

            tolerance3=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.tolerance3 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 3-direction. The default value is
                0.01.

            undercutTolerance=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl.undercutTolerance "Permalink to this definition")
            :   A Float specifying the undercut tolerance. The default value is 0.0.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl-returns "Permalink to this headline")
        :   A StampControl object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl-return-type "Permalink to this headline")
        :   [`StampControl`](#abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl "abaqus.Optimization.OptimizationTask.OptimizationTask.StampControl (Python method) — This method creates a StampControl object.")

    TopologyCyclicSymmetry(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry.name "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry.region "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied. When used with a TopologyTask, there is no default value.")*, *[translation](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry.translation "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry.translation (Python parameter) — A Float specifying the translation distance.")*, *[axis](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry.axis "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry.axis (Python parameter) — A SymbolicConstant specifying the translation direction defined along an axis positioned at the csys origin.")=`abaqusConstants.AXIS_1`*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[ignoreFrozenArea](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry.ignoreFrozenArea "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry.ignoreFrozenArea (Python parameter) — A Boolean specifying whether to ignore frozen areas.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L1641-L1687)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry "Permalink to this definition")
    :   This method creates a TopologyCyclicSymmetry object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].TopologyCyclicSymmetry
        ```

        Note

        Check [TopologyCyclicSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologycyclicsymmetrypyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.
                When used with a TopologyTask, there is no default value. When used with a ShapeTask,
                the default value is MODEL.

            translation[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry.translation "Permalink to this definition")
            :   A Float specifying the translation distance.

            axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the translation direction defined along an axis positioned
                at the **csys** origin. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default value
                is AXIS\_1.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            ignoreFrozenArea=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry.ignoreFrozenArea "Permalink to this definition")
            :   A Boolean specifying whether to ignore frozen areas. The default value is OFF.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry-returns "Permalink to this headline")
        :   A TopologyCyclicSymmetry object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry-return-type "Permalink to this headline")
        :   [`TopologyCyclicSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyCyclicSymmetry (Python method) — This method creates a TopologyCyclicSymmetry object.")

    TopologyDemoldControl(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl.name "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl.region "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied. When used with a TopologyTask, there is no default value.")*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the pullDirection.")=`None`*, *[draftAngle](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl.draftAngle "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl.draftAngle (Python parameter) — A Float specifying the draft angle.")=`0`*, *[collisionCheckRegion](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl.collisionCheckRegion "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl.collisionCheckRegion (Python parameter) — The SymbolicConstant DEMOLD_REGION or a Region object specifying the collision check region.")=`abaqusConstants.DEMOLD_REGION`*, *[pointRegion](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl.pointRegion "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl.pointRegion (Python parameter) — A Region object specifying the point on a plane perpendicular to the pull direction, used to specify the central plane when technique is POINT.")=`None`*, *[pullDirection](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl.pullDirection "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl.pullDirection (Python parameter) — A VertexArray object of length 2 specifying the demold pull direction.")=`()`*, *[technique](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl.technique "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl.technique (Python parameter) — A SymbolicConstant specifying the demold technique.")=`abaqusConstants.AUTO`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L1689-L1752)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl "Permalink to this definition")
    :   This method creates a TopologyDemoldControl object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].TopologyDemoldControl
        ```

        Note

        Check [TopologyDemoldControl on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologydemoldcontrolpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.
                When used with a TopologyTask, there is no default value. When used with a ShapeTask,
                the default value is MODEL.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the
                **pullDirection**. If **csys** = None, the global coordinate system is used. When this member
                is queried, it returns an Int indicating the identifier of the DatumCsys. The default
                value is None.

            draftAngle=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl.draftAngle "Permalink to this definition")
            :   A Float specifying the draft angle. The default value is 0.0.

            collisionCheckRegion=`abaqusConstants.DEMOLD_REGION`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl.collisionCheckRegion "Permalink to this definition")
            :   The SymbolicConstant DEMOLD\_REGION or a Region object specifying the collision check
                region. If the value is DEMOLD\_REGION, then the value of **region** is used as both the
                demold region and the collision check region. The default value is DEMOLD\_REGION.

            pointRegion=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl.pointRegion "Permalink to this definition")
            :   A Region object specifying the point on a plane perpendicular to the pull direction,
                used to specify the central plane when **technique** is POINT.

            pullDirection=`()`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl.pullDirection "Permalink to this definition")
            :   A VertexArray object of length 2 specifying the demold pull direction. Instead of
                through a ConstrainedSketchVertex, each point may be specified through a tuple of coordinates.

            technique=`abaqusConstants.AUTO`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl.technique "Permalink to this definition")
            :   A SymbolicConstant specifying the demold technique. Possible values are AUTO,
                AUTO\_TIGHT, POINT, SURFACE, and STAMP. The default value is AUTO.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl-returns "Permalink to this headline")
        :   A TopologyDemoldControl object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl-return-type "Permalink to this headline")
        :   [`TopologyDemoldControl`](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyDemoldControl (Python method) — This method creates a TopologyDemoldControl object.")

    TopologyMemberSize(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize.name "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize.region "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied. When used with a TopologyTask, there is no default value.")*, *[maxThickness](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize.maxThickness "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize.maxThickness (Python parameter) — A Float specifying the maximum thickness.")=`0`*, *[minThickness](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize.minThickness "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize.minThickness (Python parameter) — A Float specifying the minimum thickness.")=`0`*, *[separation](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize.separation "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize.separation (Python parameter) — A Float specifying the minimum gap.")=`0`*, *[sizeRestriction](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize.sizeRestriction "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize.sizeRestriction (Python parameter) — A SymbolicConstant specifying whether to restrict the minimum or maximum thickness or an envelope of both.")=`abaqusConstants.MINIMUM`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L1754-L1798)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize "Permalink to this definition")
    :   This method creates a TopologyMemberSize object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].TopologyMemberSize
        ```

        Note

        Check [TopologyMemberSize on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologymembersizepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.
                When used with a TopologyTask, there is no default value. When used with a ShapeTask,
                the default value is MODEL.

            maxThickness=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize.maxThickness "Permalink to this definition")
            :   A Float specifying the maximum thickness. The default value is 0.0.

            minThickness=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize.minThickness "Permalink to this definition")
            :   A Float specifying the minimum thickness. The default value is 0.0.

            separation=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize.separation "Permalink to this definition")
            :   A Float specifying the minimum gap. The default value is 0.0.

            sizeRestriction=`abaqusConstants.MINIMUM`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize.sizeRestriction "Permalink to this definition")
            :   A SymbolicConstant specifying whether to restrict the minimum or maximum thickness or an
                envelope of both. Possible values are ENVELOPE, MAXIMUM, and MINIMUM. The default value
                is MINIMUM.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize-returns "Permalink to this headline")
        :   A TopologyMemberSize object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize-return-type "Permalink to this headline")
        :   [`TopologyMemberSize`](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMemberSize (Python method) — This method creates a TopologyMemberSize object.")

    TopologyMillingControl(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl.name "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[millingDirections](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl.millingDirections "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl.millingDirections (Python parameter) — A tuple of VertexArray objects of length 2 specifying the milling directions.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl.region "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied.")*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the millingDirections.")=`None`*, *[millingCheckRegion](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl.millingCheckRegion "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl.millingCheckRegion (Python parameter) — The SymbolicConstant MILLING_REGION or a Region object specifying the milling check region.")=`abaqusConstants.MILLING_REGION`*, *[radius](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl.radius "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl.radius (Python parameter) — A Float specifying the radius for the collision check during the removal of the elements for the milling criteria.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L1800-L1851)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl "Permalink to this definition")
    :   This method creates a TopologyMillingControl object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].TopologyMillingControl
        ```

        New in version 2022: The `TopologyMillingControl` method was added.

        Note

        Check [TopologyMillingControl on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologymillingcontrolpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            millingDirections[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl.millingDirections "Permalink to this definition")
            :   A tuple of VertexArray objects of length 2 specifying the milling directions. Each point
                can be specified through a tuple of coordinates instead of through a ConstrainedSketchVertex.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the
                **millingDirections**. If **csys** = None, the global coordinate system is used. When this
                member is queried, it returns an Int indicating the identifier of the DatumCsys. The
                default value is None.

            millingCheckRegion=`abaqusConstants.MILLING_REGION`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl.millingCheckRegion "Permalink to this definition")
            :   The SymbolicConstant MILLING\_REGION or a Region object specifying the milling check
                region. If the value is MILLING\_REGION, the value of **region** is used as both the
                milling control region and the milling check region. The default value is
                MILLING\_REGION.

            radius=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl.radius "Permalink to this definition")
            :   A Float specifying the radius for the collision check during the removal of the elements
                for the milling criteria.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl-returns "Permalink to this headline")
        :   A TopologyMillingControl object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl-return-type "Permalink to this headline")
        :   [`TopologyMillingControl`](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyMillingControl (Python method) — This method creates a TopologyMillingControl object.")

    TopologyOverhangControl(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl.name "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[pullDirection](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl.pullDirection "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl.pullDirection (Python parameter) — A VertexArray object of length 2 specifying the overhang control print direction. Instead of through a ConstrainedSketchVertex, each point can be specified through a tuple of coordinates.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl.region "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied.")*, *[csys=None](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl.csys=None (Python parameter)")*, *[draftAngle=45](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl.draftAngle=45 (Python parameter)")*, *[overhangCheckRegion=abaqusConstants.OVERHANG\_REGION](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl.overhangCheckRegion=abaqusConstants.OVERHANG_REGION (Python parameter)")*, *[pointRegion=<abaqus.Region.Region.Region object>](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl.pointRegion=<abaqus.Region.Region.Region object> (Python parameter)")*, *[radius=None](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl.radius=None (Python parameter)")*, *[technique=abaqusConstants.AUTO](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl.technique=abaqusConstants.AUTO (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L1853-L1922)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl "Permalink to this definition")
    :   This method creates a TopologyOverhangControl object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].TopologyOverhangControl
        ```

        New in version 2019: The `TopologyOverhangControl` method was added.

        Note

        Check [TopologyOverhangControl on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologyoverhangcontrolpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            pullDirection[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl.pullDirection "Permalink to this definition")
            :   A VertexArray object of length 2 specifying the overhang control print direction.
                Instead of through a ConstrainedSketchVertex, each point can be specified through a tuple of coordinates.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.

            csys : [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.13)")[[`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")], default: `None`
            :   None or a DatumCsys object specifying the local coordinate system of the
                **pullDirection**. If **csys** = None, the global coordinate system is used. When this member
                is queried, it returns an Int indicating the identifier of the DatumCsys. The default
                value is None.

            draftAngle : [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"), default: `45`
            :   A Float specifying the overhang angle. The default value is 45.0.

            overhangCheckRegion : [`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")[`OVERHANG_REGION`], default: `OVERHANG_REGION`
            :   The SymbolicConstant OVERHANG\_REGION or a Region object specifying the overhang check
                region. If the value is OVERHANG\_REGION, the value of **region** is used as both the
                overhang control region and the overhang check region. The default value is
                OVERHANG\_REGION.

            pointRegion : [`Region`](part_assembly/region.html#abaqus.Region.Surface.Region "abaqus.Region.Region.Region (Python class)"), default: `<abaqus.Region.Region.Region object at 0x7f850c6dc210>`
            :   A Region object specifying the point on a plane perpendicular to the **pullDirection**
                that is used to specify the base plane when **technique** is POINT.

            radius : [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.13)")[[`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")], default: `None`
            :   A Float specifying the radius to define the size of the cones that are used in the
                internal check for the overhang criteria.

            technique : [`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")[`POINT`, `NONE`, `AUTO`], default: `AUTO`
            :   A SymbolicConstant specifying the overhang control technique used to define the base
                plane. Possible values are AUTO, POINT, and NONE. The default value is AUTO.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyOverhangControl-returns "Permalink to this headline")
        :   A TopologyOverhangControl object.

    TopologyPlanarSymmetry(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPlanarSymmetry.name "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPlanarSymmetry.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPlanarSymmetry.region "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPlanarSymmetry.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied. When used with a TopologyTask, there is no default value.")*, *[axis](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPlanarSymmetry.axis "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPlanarSymmetry.axis (Python parameter) — A SymbolicConstant specifying the axis of symmetry.")=`abaqusConstants.AXIS_1`*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPlanarSymmetry.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPlanarSymmetry.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[ignoreFrozenArea](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPlanarSymmetry.ignoreFrozenArea "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPlanarSymmetry.ignoreFrozenArea (Python parameter) — A Boolean specifying whether to ignore frozen areas.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L1924-L1966)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPlanarSymmetry "Permalink to this definition")
    :   This method creates a TopologyPlanarSymmetry object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].TopologyPlanarSymmetry
        ```

        Note

        Check [TopologyPlanarSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologyplanarsymmetrypyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPlanarSymmetry-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPlanarSymmetry.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPlanarSymmetry.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.
                When used with a TopologyTask, there is no default value. When used with a ShapeTask,
                the default value is MODEL.

            axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPlanarSymmetry.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS\_1, AXIS\_2,
                and AXIS\_3. The default value is AXIS\_1.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPlanarSymmetry.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            ignoreFrozenArea=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPlanarSymmetry.ignoreFrozenArea "Permalink to this definition")
            :   A Boolean specifying whether to ignore frozen areas. The default value is OFF.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPlanarSymmetry-returns "Permalink to this headline")
        :   A TopologyPlanarSymmetry object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPlanarSymmetry-return-type "Permalink to this headline")
        :   [`TopologyPlanarSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPlanarSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPlanarSymmetry (Python method) — This method creates a TopologyPlanarSymmetry object.")

    TopologyPointSymmetry(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPointSymmetry.name "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPointSymmetry.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPointSymmetry.region "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPointSymmetry.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied. When used with a TopologyTask, there is no default value.")*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPointSymmetry.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPointSymmetry.csys (Python parameter) — None or a DatumCsys object specifying the position of the symmetry point defined as the origin of a local coordinate system.")=`None`*, *[ignoreFrozenArea](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPointSymmetry.ignoreFrozenArea "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPointSymmetry.ignoreFrozenArea (Python parameter) — A Boolean specifying whether to ignore frozen areas.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L1968-L2006)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPointSymmetry "Permalink to this definition")
    :   This method creates a TopologyPointSymmetry object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].TopologyPointSymmetry
        ```

        Note

        Check [TopologyPointSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologypointsymmetrypyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPointSymmetry-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPointSymmetry.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPointSymmetry.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.
                When used with a TopologyTask, there is no default value. When used with a ShapeTask,
                the default value is MODEL.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPointSymmetry.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the position of the symmetry point defined as the
                origin of a local coordinate system. If **csys** = None, the global coordinate system is
                used. When this member is queried, it returns an Int. The default value is None.

            ignoreFrozenArea=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPointSymmetry.ignoreFrozenArea "Permalink to this definition")
            :   A Boolean specifying whether to ignore frozen areas. The default value is OFF.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPointSymmetry-returns "Permalink to this headline")
        :   A TopologyPointSymmetry object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPointSymmetry-return-type "Permalink to this headline")
        :   [`TopologyPointSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPointSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyPointSymmetry (Python method) — This method creates a TopologyPointSymmetry object.")

    TopologyRibDesign(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign.name "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[ribDirection](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign.ribDirection "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign.ribDirection (Python parameter) — A VertexArray object of length 2 specifying the out-of-plane growth direction of the ribs.")*, *[ribThickness](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign.ribThickness "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign.ribThickness (Python parameter) — A Float specifying the average thickness of the ribs.")*, *[ribDistance](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign.ribDistance "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign.ribDistance (Python parameter) — A Float specifying the average distance between the rib centers.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign.region "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied. When used with a TopologyTask, there is no default value.")*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign.csys (Python parameter) — None or a DatumCsys object specifying the position of the symmetry point defined as the origin of a local coordinate system.")=`None`*, *[ribDesignCheckRegion](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign.ribDesignCheckRegion "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign.ribDesignCheckRegion (Python parameter) — The SymbolicConstant RIBDESIGN_REGION or a Region object specifying the overhang check region.")=`abaqusConstants.RIBDESIGN_REGION`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L2008-L2069)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign "Permalink to this definition")
    :   This method creates a TopologyRibDesign object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].TopologyRibDesign
        ```

        New in version 2022: The `TopologyRibDesign` method was added.

        Note

        Check [TopologyRibDesign on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologyribdesignpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            ribDirection[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign.ribDirection "Permalink to this definition")
            :   A VertexArray object of length 2 specifying the out-of-plane growth direction of the ribs. Instead of
                through a Vertex, each point can be specified through a tuple of coordinates.

            ribThickness[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign.ribThickness "Permalink to this definition")
            :   A Float specifying the average thickness of the ribs.

            ribDistance[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign.ribDistance "Permalink to this definition")
            :   A Float specifying the average distance between the rib centers. The distance must be larger than twice
                the average element edge length.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.
                When used with a TopologyTask, there is no default value. When used with a ShapeTask,
                the default value is MODEL.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the position of the symmetry point defined as the
                origin of a local coordinate system. If **csys** = None, the global coordinate system is
                used. When this member is queried, it returns an Int. The default value is None.

            ribDesignCheckRegion=`abaqusConstants.RIBDESIGN_REGION`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign.ribDesignCheckRegion "Permalink to this definition")
            :   The SymbolicConstant RIBDESIGN\_REGION or a Region object specifying the overhang check region. If the value
                is OVERHANG\_REGION, the value of region is used as both the overhang control region and the overhang check
                region. The default value is RIBDESIGN\_REGION.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign-returns "Permalink to this headline")
        :   A TopologyRibDesign object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign-return-type "Permalink to this headline")
        :   [`TopologyRibDesign`](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRibDesign (Python method) — This method creates a TopologyRibDesign object.")

    TopologyRotationalSymmetry(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry.name "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[angle](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry.angle "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry.angle (Python parameter) — A Float specifying the repeating segment size, an angle in degrees.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry.region "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied. When used with a TopologyTask, there is no default value.")*, *[axis](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry.axis "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry.axis (Python parameter) — A SymbolicConstant specifying the axis of symmetry.")=`abaqusConstants.AXIS_1`*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[ignoreFrozenArea](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry.ignoreFrozenArea "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry.ignoreFrozenArea (Python parameter) — A Boolean specifying whether to ignore frozen areas.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L2071-L2116)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry "Permalink to this definition")
    :   This method creates a TopologyRotationalSymmetry object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].TopologyRotationalSymmetry
        ```

        Note

        Check [TopologyRotationalSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologyrotationalsymmetrypyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            angle[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry.angle "Permalink to this definition")
            :   A Float specifying the repeating segment size, an angle in degrees.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.
                When used with a TopologyTask, there is no default value. When used with a ShapeTask,
                the default value is MODEL.

            axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS\_1, AXIS\_2,
                and AXIS\_3. The default value is AXIS\_1.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            ignoreFrozenArea=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry.ignoreFrozenArea "Permalink to this definition")
            :   A Boolean specifying whether to ignore frozen areas. The default value is OFF.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry-returns "Permalink to this headline")
        :   A TopologyRotationalSymmetry object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry-return-type "Permalink to this headline")
        :   [`TopologyRotationalSymmetry`](#abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry "abaqus.Optimization.OptimizationTask.OptimizationTask.TopologyRotationalSymmetry (Python method) — This method creates a TopologyRotationalSymmetry object.")

    TurnControl(*[name](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.name "abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.name (Python parameter) — A String specifying the geometric restriction repository key.")*, *[clientDirection](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.clientDirection "abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.clientDirection (Python parameter) — A VertexArray object of length 2 specifying the direction of the rotation axis as a vector positioned at the csys origin.")*, *[region](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.region "abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied. When used with a TopologyTask, there is no default value.")*, *[csys](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.csys "abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[mainPoint](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.mainPoint "abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.mainPoint (Python parameter) — None or a Region object specifying the main point used when mainPointDetermination is SPECIFY.")=`None`*, *[mainPointDetermination](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.mainPointDetermination "abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.mainPointDetermination (Python parameter) — A SymbolicConstant specifying the rule for assigning point priority.")=`abaqusConstants.MAXIMUM`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.presumeFeasibleRegionAtStart "abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.presumeFeasibleRegionAtStart (Python parameter) — A Boolean specifying whether to ignore the geometric restriction in the first design cycle.")=`1`*, *[tolerance1](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.tolerance1 "abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.tolerance1 (Python parameter) — A Float specifying the geometric tolerance in the 1-direction.")=`0`*, *[tolerance2](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.tolerance2 "abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.tolerance2 (Python parameter) — A Float specifying the geometric tolerance in the 2-direction.")=`0`*, *[tolerance3](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.tolerance3 "abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.tolerance3 (Python parameter) — A Float specifying the geometric tolerance in the 3-direction.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L2118-L2197)[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl "Permalink to this definition")
    :   This method creates a TurnControl object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].optimizationTasks[name].TurnControl
        ```

        Note

        Check [TurnControl on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-turncontrolpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.name "Permalink to this definition")
            :   A String specifying the geometric restriction repository key.

            clientDirection[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.clientDirection "Permalink to this definition")
            :   A VertexArray object of length 2 specifying the direction of the rotation axis as a
                vector positioned at the **csys** origin. Instead of through a ConstrainedSketchVertex, each point might be
                specified through a tuple of coordinates.

            region[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.
                When used with a TopologyTask, there is no default value. When used with a ShapeTask,
                the default value is MODEL.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            mainPoint=`None`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.mainPoint "Permalink to this definition")
            :   None or a Region object specifying the main point used when **mainPointDetermination** is
                SPECIFY. The default value is None.

                Changed in version 2022: The argument `masterPoint` was renamed to `mainPoint`.

            mainPointDetermination=`abaqusConstants.MAXIMUM`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.mainPointDetermination "Permalink to this definition")
            :   A SymbolicConstant specifying the rule for assigning point priority. Possible values are
                MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.

                Changed in version 2022: The argument `masterPointDetermination` was renamed to `mainPointDetermination`.

            presumeFeasibleRegionAtStart=`1`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.presumeFeasibleRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore the geometric restriction in the first design
                cycle. The default value is ON.

            tolerance1=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.tolerance1 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 1-direction. The default value is
                0.01.

            tolerance2=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.tolerance2 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 2-direction. The default value is
                0.01.

            tolerance3=`0`[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl.tolerance3 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 3-direction. The default value is
                0.01.

        Returns:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl-returns "Permalink to this headline")
        :   A TurnControl object.

        Return type:[¶](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl-return-type "Permalink to this headline")
        :   [`TurnControl`](#abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl "abaqus.Optimization.OptimizationTask.OptimizationTask.TurnControl (Python method) — This method creates a TurnControl object.")

## Other Classes[¶](#other-classes "Permalink to this heading")

*class* BeadFilter(*[name](#abaqus.Optimization.OptimizationTask.BeadFilter "abaqus.Optimization.OptimizationTask.BeadFilter.__init__.name (Python parameter)")*, *[region](#abaqus.Optimization.OptimizationTask.BeadFilter "abaqus.Optimization.OptimizationTask.BeadFilter.__init__.region (Python parameter)")*, *[radius](#abaqus.Optimization.OptimizationTask.BeadFilter "abaqus.Optimization.OptimizationTask.BeadFilter.__init__.radius (Python parameter)")=`None`*, *[filterRadiusBy](#abaqus.Optimization.OptimizationTask.BeadFilter "abaqus.Optimization.OptimizationTask.BeadFilter.__init__.filterRadiusBy (Python parameter)")=`abaqusConstants.ABSOLUTE_VALUE`*, *[filterCheckRegion](#abaqus.Optimization.OptimizationTask.BeadFilter "abaqus.Optimization.OptimizationTask.BeadFilter.__init__.filterCheckRegion (Python parameter)")=`abaqusConstants.FILTER_REGION`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L15-L115)[¶](#abaqus.Optimization.OptimizationTask.BeadFilter "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The BeadFilter object defines a growth geometric restriction. The BeadFilter object is derived from the
    GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    New in version 2023: The `BeadFilter` class was added.

    Note

    Check [BeadFilter on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadfilterpyc.htm?contextscope=all).

    Member Details:

    filterCheckRegion : --is-rst--:py:data:`~typing.Union`\[:py:data:`~typing.Literal`\[``FILTER\_REGION``], :py:class:`~abaqus.Region.Region.Region`] = `'FILTER_REGION'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L45-L48)[¶](#abaqus.Optimization.OptimizationTask.BeadFilter.filterCheckRegion "Permalink to this definition")
    :   The SymbolicConstant FILTER\_REGION or a Region object specifying the filter check region. If the value is
        FILTER\_REGION, the value of the region is used as both the filter region and the filter check region.
        The default value is FILTER\_REGION.

    filterRadiusBy : --is-rst--:py:data:`~typing.Literal`\[``ABSOLUTE\_VALUE``, ``RELATIVE``] = `'ABSOLUTE_VALUE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L40-L43)[¶](#abaqus.Optimization.OptimizationTask.BeadFilter.filterRadiusBy "Permalink to this definition")
    :   The SymbolicConstant defines whether the filter radius is in absolute or relative units. For an absolute
        radius, the value is ABSOLUTE\_VALUE. For a relative radius, the value is RELATIVE. The default value is
        ABSOLUTE\_VALUE.

    radius : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py)[¶](#abaqus.Optimization.OptimizationTask.BeadFilter.radius "Permalink to this definition")
    :   A Float specifying the filter radius. The default value is double the average edge length of the model.

    setValues(*[region](#abaqus.Optimization.OptimizationTask.BeadFilter.setValues.region "abaqus.Optimization.OptimizationTask.BeadFilter.setValues.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied.")*, *[radius](#abaqus.Optimization.OptimizationTask.BeadFilter.setValues.radius "abaqus.Optimization.OptimizationTask.BeadFilter.setValues.radius (Python parameter) — A Float specifying the filter radius.")=`None`*, *[filterRadiusBy](#abaqus.Optimization.OptimizationTask.BeadFilter.setValues.filterRadiusBy "abaqus.Optimization.OptimizationTask.BeadFilter.setValues.filterRadiusBy (Python parameter) — The SymbolicConstant defines whether the filter radius is in absolute or relative units.")=`abaqusConstants.ABSOLUTE_VALUE`*, *[filterCheckRegion](#abaqus.Optimization.OptimizationTask.BeadFilter.setValues.filterCheckRegion "abaqus.Optimization.OptimizationTask.BeadFilter.setValues.filterCheckRegion (Python parameter) — The SymbolicConstant FILTER_REGION or a Region object specifying the filter check region.")=`abaqusConstants.FILTER_REGION`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L90-L115)[¶](#abaqus.Optimization.OptimizationTask.BeadFilter.setValues "Permalink to this definition")
    :   This method modifies the BeadFilter object.

        Note

        Check [BeadFilter.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadfilterpyc.htm?contextscope=all#simaker-beadfiltersetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.BeadFilter.setValues-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Optimization.OptimizationTask.BeadFilter.setValues.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.

            radius=`None`[¶](#abaqus.Optimization.OptimizationTask.BeadFilter.setValues.radius "Permalink to this definition")
            :   A Float specifying the filter radius. The default value is double the average edge length of the model.

            filterRadiusBy=`abaqusConstants.ABSOLUTE_VALUE`[¶](#abaqus.Optimization.OptimizationTask.BeadFilter.setValues.filterRadiusBy "Permalink to this definition")
            :   The SymbolicConstant defines whether the filter radius is in absolute or relative units. For an absolute
                radius, the value is ABSOLUTE\_VALUE. For a relative radius, the value is RELATIVE. The default value is
                ABSOLUTE\_VALUE.

            filterCheckRegion=`abaqusConstants.FILTER_REGION`[¶](#abaqus.Optimization.OptimizationTask.BeadFilter.setValues.filterCheckRegion "Permalink to this definition")
            :   The SymbolicConstant FILTER\_REGION or a Region object specifying the filter check region. If the value is
                FILTER\_REGION, the value of the region is used as both the filter region and the filter check region.
                The default value is FILTER\_REGION.

*class* GeometricRestriction[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TurnControl.py#L8-L27)[¶](#abaqus.Optimization.TurnControl.GeometricRestriction "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The GeometricRestriction object is the abstract base type for other GeometricRestriction objects. The
    GeometricRestriction object has no explicit constructor. The methods and members of the GeometricRestriction
    object are common to all objects derived from GeometricRestriction.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [GeometricRestriction on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometricrestrictionpyc.htm?contextscope=all).

    Member Details:

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TurnControl.py#L21-L22)[¶](#abaqus.Optimization.TurnControl.GeometricRestriction.name "Permalink to this definition")
    :   A String specifying the geometric restriction repository key.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TurnControl.py#L8-L27)[¶](#abaqus.Optimization.TurnControl.GeometricRestriction.region "Permalink to this definition")
    :   A Region object specifying the region to which the geometric restriction is applied.
        When used with a TopologyTask, there is no default value. When used with a ShapeTask,
        the default value is MODEL.

*class* BeadFixedRegion(*[name](#abaqus.Optimization.OptimizationTask.BeadFixedRegion "abaqus.Optimization.OptimizationTask.BeadFixedRegion.__init__.name (Python parameter)")*, *[region](#abaqus.Optimization.OptimizationTask.BeadFixedRegion "abaqus.Optimization.OptimizationTask.BeadFixedRegion.__init__.region (Python parameter)")*, *[csys](#abaqus.Optimization.OptimizationTask.BeadFixedRegion "abaqus.Optimization.OptimizationTask.BeadFixedRegion.__init__.csys (Python parameter)")=`None`*, *[u1](#abaqus.Optimization.OptimizationTask.BeadFixedRegion "abaqus.Optimization.OptimizationTask.BeadFixedRegion.__init__.u1 (Python parameter)")=`0`*, *[u2](#abaqus.Optimization.OptimizationTask.BeadFixedRegion "abaqus.Optimization.OptimizationTask.BeadFixedRegion.__init__.u2 (Python parameter)")=`0`*, *[u3](#abaqus.Optimization.OptimizationTask.BeadFixedRegion "abaqus.Optimization.OptimizationTask.BeadFixedRegion.__init__.u3 (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L10-L109)[¶](#abaqus.Optimization.OptimizationTask.BeadFixedRegion "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The BeadFixedRegion object defines a fixed region geometric restriction. The BeadFixedRegion object is
    derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [BeadFixedRegion on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadfixedregionpyc.htm?contextscope=all).

    Member Details:

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L28-L31)[¶](#abaqus.Optimization.OptimizationTask.BeadFixedRegion.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
        global coordinate system is used. When this member is queried, it returns an Int. The
        default value is None.

    setValues(*[csys](#abaqus.Optimization.OptimizationTask.BeadFixedRegion.setValues.csys "abaqus.Optimization.OptimizationTask.BeadFixedRegion.setValues.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[u1](#abaqus.Optimization.OptimizationTask.BeadFixedRegion.setValues.u1 "abaqus.Optimization.OptimizationTask.BeadFixedRegion.setValues.u1 (Python parameter) — A Boolean specifying whether to fix the region in the 1-direction.")=`0`*, *[u2](#abaqus.Optimization.OptimizationTask.BeadFixedRegion.setValues.u2 "abaqus.Optimization.OptimizationTask.BeadFixedRegion.setValues.u2 (Python parameter) — A Boolean specifying whether to fix the region in the 2-direction.")=`0`*, *[u3](#abaqus.Optimization.OptimizationTask.BeadFixedRegion.setValues.u3 "abaqus.Optimization.OptimizationTask.BeadFixedRegion.setValues.u3 (Python parameter) — A Boolean specifying whether to fix the region in the 3-direction.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L89-L109)[¶](#abaqus.Optimization.OptimizationTask.BeadFixedRegion.setValues "Permalink to this definition")
    :   This method modifies the BeadFixedRegion object.

        Note

        Check [BeadFixedRegion.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadfixedregionpyc.htm?contextscope=all#simaker-beadfixedregionsetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.BeadFixedRegion.setValues-parameters "Permalink to this headline")
        :   csys=`None`[¶](#abaqus.Optimization.OptimizationTask.BeadFixedRegion.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            u1=`0`[¶](#abaqus.Optimization.OptimizationTask.BeadFixedRegion.setValues.u1 "Permalink to this definition")
            :   A Boolean specifying whether to fix the region in the 1-direction. The default value is
                OFF.

            u2=`0`[¶](#abaqus.Optimization.OptimizationTask.BeadFixedRegion.setValues.u2 "Permalink to this definition")
            :   A Boolean specifying whether to fix the region in the 2-direction. The default value is
                OFF.

            u3=`0`[¶](#abaqus.Optimization.OptimizationTask.BeadFixedRegion.setValues.u3 "Permalink to this definition")
            :   A Boolean specifying whether to fix the region in the 3-direction. The default value is
                OFF.

    u1 : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L33-L35)[¶](#abaqus.Optimization.OptimizationTask.BeadFixedRegion.u1 "Permalink to this definition")
    :   A Boolean specifying whether to fix the region in the 1-direction. The default value is
        OFF.

    u2 : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L37-L39)[¶](#abaqus.Optimization.OptimizationTask.BeadFixedRegion.u2 "Permalink to this definition")
    :   A Boolean specifying whether to fix the region in the 2-direction. The default value is
        OFF.

    u3 : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L41-L43)[¶](#abaqus.Optimization.OptimizationTask.BeadFixedRegion.u3 "Permalink to this definition")
    :   A Boolean specifying whether to fix the region in the 3-direction. The default value is
        OFF.

*class* BeadGrowth(*[name](#abaqus.Optimization.OptimizationTask.BeadGrowth "abaqus.Optimization.OptimizationTask.BeadGrowth.__init__.name (Python parameter)")*, *[region](#abaqus.Optimization.OptimizationTask.BeadGrowth "abaqus.Optimization.OptimizationTask.BeadGrowth.__init__.region (Python parameter)")*, *[beadGrowth](#abaqus.Optimization.OptimizationTask.BeadGrowth "abaqus.Optimization.OptimizationTask.BeadGrowth.__init__.beadGrowth (Python parameter)")=`0`*, *[shrink](#abaqus.Optimization.OptimizationTask.BeadGrowth "abaqus.Optimization.OptimizationTask.BeadGrowth.__init__.shrink (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L9-L77)[¶](#abaqus.Optimization.OptimizationTask.BeadGrowth "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The BeadGrowth object defines a growth geometric restriction. The BeadGrowth object is derived from the
    GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [BeadGrowth on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadgrowthpyc.htm?contextscope=all).

    Member Details:

    beadGrowth : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L27-L29)[¶](#abaqus.Optimization.OptimizationTask.BeadGrowth.beadGrowth "Permalink to this definition")
    :   A Float specifying the maximum optimization displacement in the growth direction. Either
        **beadGrowth** or **shrink** or both must be specified. The default value is 0.0.

    setValues(*[beadGrowth](#abaqus.Optimization.OptimizationTask.BeadGrowth.setValues.beadGrowth "abaqus.Optimization.OptimizationTask.BeadGrowth.setValues.beadGrowth (Python parameter) — A Float specifying the maximum optimization displacement in the growth direction.")=`0`*, *[shrink](#abaqus.Optimization.OptimizationTask.BeadGrowth.setValues.shrink "abaqus.Optimization.OptimizationTask.BeadGrowth.setValues.shrink (Python parameter) — A Float specifying the maximum optimization displacement in the shrink direction.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L64-L77)[¶](#abaqus.Optimization.OptimizationTask.BeadGrowth.setValues "Permalink to this definition")
    :   This method modifies the BeadGrowth object.

        Note

        Check [BeadGrowth.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadgrowthpyc.htm?contextscope=all#simaker-beadgrowthsetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.BeadGrowth.setValues-parameters "Permalink to this headline")
        :   beadGrowth=`0`[¶](#abaqus.Optimization.OptimizationTask.BeadGrowth.setValues.beadGrowth "Permalink to this definition")
            :   A Float specifying the maximum optimization displacement in the growth direction. Either
                **beadGrowth** or **shrink** or both must be specified. The default value is 0.0.

            shrink=`0`[¶](#abaqus.Optimization.OptimizationTask.BeadGrowth.setValues.shrink "Permalink to this definition")
            :   A Float specifying the maximum optimization displacement in the shrink direction. Either
                **beadGrowth** or **shrink** or both must be specified The default value is 0.0.

    shrink : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L31-L33)[¶](#abaqus.Optimization.OptimizationTask.BeadGrowth.shrink "Permalink to this definition")
    :   A Float specifying the maximum optimization displacement in the shrink direction. Either
        **beadGrowth** or **shrink** or both must be specified The default value is 0.0.

*class* BeadPenetrationCheck(*[name](#abaqus.Optimization.OptimizationTask.BeadPenetrationCheck "abaqus.Optimization.OptimizationTask.BeadPenetrationCheck.__init__.name (Python parameter)")*, *[beadPenetrationCheckRegion](#abaqus.Optimization.OptimizationTask.BeadPenetrationCheck "abaqus.Optimization.OptimizationTask.BeadPenetrationCheck.__init__.beadPenetrationCheckRegion (Python parameter)")*, *[region](#abaqus.Optimization.OptimizationTask.BeadPenetrationCheck "abaqus.Optimization.OptimizationTask.BeadPenetrationCheck.__init__.region (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L9-L58)[¶](#abaqus.Optimization.OptimizationTask.BeadPenetrationCheck "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The BeadPenetrationCheck object defines a penetration check geometric restriction. The
    BeadPenetrationCheck object is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [BeadPenetrationCheck on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadpenetrationcheckpyc.htm?contextscope=all).

    Member Details:

    beadPenetrationCheckRegion : --is-rst--:py:class:`~abaqus.Region.Region.Region`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py)[¶](#abaqus.Optimization.OptimizationTask.BeadPenetrationCheck.beadPenetrationCheckRegion "Permalink to this definition")
    :   A Region object specifying the penetration check region.

    setValues(*\*[args](#abaqus.Optimization.OptimizationTask.BeadPenetrationCheck.setValues "abaqus.Optimization.OptimizationTask.BeadPenetrationCheck.setValues.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Optimization.OptimizationTask.BeadPenetrationCheck.setValues "abaqus.Optimization.OptimizationTask.BeadPenetrationCheck.setValues.kwargs (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L55-L58)[¶](#abaqus.Optimization.OptimizationTask.BeadPenetrationCheck.setValues "Permalink to this definition")
    :   This method modifies the BeadPenetrationCheck object.

*class* BeadPlanarSymmetry(*[name](#abaqus.Optimization.OptimizationTask.BeadPlanarSymmetry "abaqus.Optimization.OptimizationTask.BeadPlanarSymmetry.__init__.name (Python parameter)")*, *[region](#abaqus.Optimization.OptimizationTask.BeadPlanarSymmetry "abaqus.Optimization.OptimizationTask.BeadPlanarSymmetry.__init__.region (Python parameter)")*, *[axis](#abaqus.Optimization.OptimizationTask.BeadPlanarSymmetry "abaqus.Optimization.OptimizationTask.BeadPlanarSymmetry.__init__.axis (Python parameter)")=`abaqusConstants.AXIS_1`*, *[csys](#abaqus.Optimization.OptimizationTask.BeadPlanarSymmetry "abaqus.Optimization.OptimizationTask.BeadPlanarSymmetry.__init__.csys (Python parameter)")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L13-L90)[¶](#abaqus.Optimization.OptimizationTask.BeadPlanarSymmetry "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The BeadPlanarSymmetry object defines a bead planar symmetry geometric restriction. The
    BeadPlanarSymmetry object is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [BeadPlanarSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadplanarsymmetrypyc.htm?contextscope=all).

    Member Details:

    axis : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'AXIS_1'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L31-L33)[¶](#abaqus.Optimization.OptimizationTask.BeadPlanarSymmetry.axis "Permalink to this definition")
    :   A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS\_1, AXIS\_2,
        and AXIS\_3. The default value is AXIS\_1.

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L35-L38)[¶](#abaqus.Optimization.OptimizationTask.BeadPlanarSymmetry.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
        global coordinate system is used. When this member is queried, it returns an Int. The
        default value is None.

    setValues(*[axis](#abaqus.Optimization.OptimizationTask.BeadPlanarSymmetry.setValues.axis "abaqus.Optimization.OptimizationTask.BeadPlanarSymmetry.setValues.axis (Python parameter) — A SymbolicConstant specifying the axis of symmetry.")=`abaqusConstants.AXIS_1`*, *[csys](#abaqus.Optimization.OptimizationTask.BeadPlanarSymmetry.setValues.csys "abaqus.Optimization.OptimizationTask.BeadPlanarSymmetry.setValues.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L76-L90)[¶](#abaqus.Optimization.OptimizationTask.BeadPlanarSymmetry.setValues "Permalink to this definition")
    :   This method modifies the BeadPlanarSymmetry object.

        Note

        Check [BeadPlanarSymmetry.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadplanarsymmetrypyc.htm?contextscope=all#simaker-beadplanarsymmetrysetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.BeadPlanarSymmetry.setValues-parameters "Permalink to this headline")
        :   axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Optimization.OptimizationTask.BeadPlanarSymmetry.setValues.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS\_1, AXIS\_2,
                and AXIS\_3. The default value is AXIS\_1.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.BeadPlanarSymmetry.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

*class* BeadPointSymmetry(*[name](#abaqus.Optimization.OptimizationTask.BeadPointSymmetry "abaqus.Optimization.OptimizationTask.BeadPointSymmetry.__init__.name (Python parameter)")*, *[region](#abaqus.Optimization.OptimizationTask.BeadPointSymmetry "abaqus.Optimization.OptimizationTask.BeadPointSymmetry.__init__.region (Python parameter)")*, *[csys](#abaqus.Optimization.OptimizationTask.BeadPointSymmetry "abaqus.Optimization.OptimizationTask.BeadPointSymmetry.__init__.csys (Python parameter)")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L9-L70)[¶](#abaqus.Optimization.OptimizationTask.BeadPointSymmetry "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The BeadPointSymmetry object defines a point symmetry geometric restriction. The BeadPointSymmetry object
    is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [BeadPointSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadpointsymmetrypyc.htm?contextscope=all).

    Member Details:

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L27-L30)[¶](#abaqus.Optimization.OptimizationTask.BeadPointSymmetry.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the position of the symmetry point defined as the
        origin of a local coordinate system. If **csys** = None, the global coordinate system is
        used. When this member is queried, it returns an Int. The default value is None.

    setValues(*[csys](#abaqus.Optimization.OptimizationTask.BeadPointSymmetry.setValues.csys "abaqus.Optimization.OptimizationTask.BeadPointSymmetry.setValues.csys (Python parameter) — None or a DatumCsys object specifying the position of the symmetry point defined as the origin of a local coordinate system.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L59-L70)[¶](#abaqus.Optimization.OptimizationTask.BeadPointSymmetry.setValues "Permalink to this definition")
    :   This method modifies the BeadPointSymmetry object.

        Note

        Check [BeadPointSymmetry.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadpointsymmetrypyc.htm?contextscope=all#simaker-beadpointsymmetrysetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.BeadPointSymmetry.setValues-parameters "Permalink to this headline")
        :   csys=`None`[¶](#abaqus.Optimization.OptimizationTask.BeadPointSymmetry.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the position of the symmetry point defined as the
                origin of a local coordinate system. If **csys** = None, the global coordinate system is
                used. When this member is queried, it returns an Int. The default value is None.

*class* BeadRotationalSymmetry(*[name](#abaqus.Optimization.OptimizationTask.BeadRotationalSymmetry "abaqus.Optimization.OptimizationTask.BeadRotationalSymmetry.__init__.name (Python parameter)")*, *[angle](#abaqus.Optimization.OptimizationTask.BeadRotationalSymmetry "abaqus.Optimization.OptimizationTask.BeadRotationalSymmetry.__init__.angle (Python parameter)")*, *[region](#abaqus.Optimization.OptimizationTask.BeadRotationalSymmetry "abaqus.Optimization.OptimizationTask.BeadRotationalSymmetry.__init__.region (Python parameter)")*, *[axis](#abaqus.Optimization.OptimizationTask.BeadRotationalSymmetry "abaqus.Optimization.OptimizationTask.BeadRotationalSymmetry.__init__.axis (Python parameter)")=`abaqusConstants.AXIS_1`*, *[csys](#abaqus.Optimization.OptimizationTask.BeadRotationalSymmetry "abaqus.Optimization.OptimizationTask.BeadRotationalSymmetry.__init__.csys (Python parameter)")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L13-L96)[¶](#abaqus.Optimization.OptimizationTask.BeadRotationalSymmetry "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The BeadRotationalSymmetry object defines a bead rotational symmetry geometric restriction. The
    BeadRotationalSymmetry object is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [BeadRotationalSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadrotationalsymmetrypyc.htm?contextscope=all).

    Member Details:

    angle : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py)[¶](#abaqus.Optimization.OptimizationTask.BeadRotationalSymmetry.angle "Permalink to this definition")
    :   A Float specifying the repeating segment size, an angle in degrees.

    axis : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'AXIS_1'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L34-L36)[¶](#abaqus.Optimization.OptimizationTask.BeadRotationalSymmetry.axis "Permalink to this definition")
    :   A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS\_1, AXIS\_2,
        and AXIS\_3. The default value is AXIS\_1.

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L38-L41)[¶](#abaqus.Optimization.OptimizationTask.BeadRotationalSymmetry.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
        global coordinate system is used. When this member is queried, it returns an Int. The
        default value is None.

    setValues(*[axis](#abaqus.Optimization.OptimizationTask.BeadRotationalSymmetry.setValues.axis "abaqus.Optimization.OptimizationTask.BeadRotationalSymmetry.setValues.axis (Python parameter) — A SymbolicConstant specifying the axis of symmetry.")=`abaqusConstants.AXIS_1`*, *[csys](#abaqus.Optimization.OptimizationTask.BeadRotationalSymmetry.setValues.csys "abaqus.Optimization.OptimizationTask.BeadRotationalSymmetry.setValues.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L82-L96)[¶](#abaqus.Optimization.OptimizationTask.BeadRotationalSymmetry.setValues "Permalink to this definition")
    :   This method modifies the BeadRotationalSymmetry object.

        Note

        Check [BeadRotationalSymmetry.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadrotationalsymmetrypyc.htm?contextscope=all#simaker-beadrotationalsymmetrysetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.BeadRotationalSymmetry.setValues-parameters "Permalink to this headline")
        :   axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Optimization.OptimizationTask.BeadRotationalSymmetry.setValues.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS\_1, AXIS\_2,
                and AXIS\_3. The default value is AXIS\_1.

            csys=`None`[¶](#abaqus.Optimization.OptimizationTask.BeadRotationalSymmetry.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

*class* BeadTask(*[name](#abaqus.Optimization.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.BeadTask.__init__.name (Python parameter)")*, *[abaqusSensitivities](#abaqus.Optimization.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.BeadTask.__init__.abaqusSensitivities (Python parameter)")=`True`*, *[algorithm](#abaqus.Optimization.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.BeadTask.__init__.algorithm (Python parameter)")=`abaqusConstants.GENERAL_OPTIMIZATION`*, *[areBCRegionsFrozen](#abaqus.Optimization.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.BeadTask.__init__.areBCRegionsFrozen (Python parameter)")=`0`*, *[beadIter](#abaqus.Optimization.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.BeadTask.__init__.beadIter (Python parameter)")=`1`*, *[beadMaxMembraneStress](#abaqus.Optimization.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.BeadTask.__init__.beadMaxMembraneStress (Python parameter)")=`0`*, *[beadMinStress](#abaqus.Optimization.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.BeadTask.__init__.beadMinStress (Python parameter)")=`0`*, *[beadPerturbation](#abaqus.Optimization.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.BeadTask.__init__.beadPerturbation (Python parameter)")=`0`*, *[beadWidth](#abaqus.Optimization.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.BeadTask.__init__.beadWidth (Python parameter)")=`abaqusConstants.DEFAULT`*, *[curveSmooth](#abaqus.Optimization.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.BeadTask.__init__.curveSmooth (Python parameter)")=`5`*, *[filterRadius](#abaqus.Optimization.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.BeadTask.__init__.filterRadius (Python parameter)")=`4`*, *[filterRadiusBy](#abaqus.Optimization.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.BeadTask.__init__.filterRadiusBy (Python parameter)")=`abaqusConstants.VALUE`*, *[flipNormalDir](#abaqus.Optimization.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.BeadTask.__init__.flipNormalDir (Python parameter)")=`0`*, *[frozenBoundaryConditionRegion](#abaqus.Optimization.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.BeadTask.__init__.frozenBoundaryConditionRegion (Python parameter)")=`abaqusConstants.MODEL`*, *[isSensCalcOnlyOnDesignNodes](#abaqus.Optimization.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.BeadTask.__init__.isSensCalcOnlyOnDesignNodes (Python parameter)")=`0`*, *[modeTrackingRegion](#abaqus.Optimization.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.BeadTask.__init__.modeTrackingRegion (Python parameter)")=`abaqusConstants.MODEL`*, *[nodalMoveLimit](#abaqus.Optimization.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.BeadTask.__init__.nodalMoveLimit (Python parameter)")=`0`*, *[nodeSmooth](#abaqus.Optimization.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.BeadTask.__init__.nodeSmooth (Python parameter)")=`abaqusConstants.DEFAULT`*, *[nodeUpdateStrategy](#abaqus.Optimization.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.BeadTask.__init__.nodeUpdateStrategy (Python parameter)")=`abaqusConstants.CONSERVATIVE`*, *[numTrackedModes](#abaqus.Optimization.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.BeadTask.__init__.numTrackedModes (Python parameter)")=`5`*, *[updateShapeBasisVectors](#abaqus.Optimization.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.BeadTask.__init__.updateShapeBasisVectors (Python parameter)")=`abaqusConstants.EVERY_CYCLE`*, *[groupOperator](#abaqus.Optimization.OptimizationTaskModel.BeadTask "abaqus.Optimization.OptimizationTaskModel.BeadTask.__init__.groupOperator (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L26-L361)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask "Permalink to this definition")
:   Bases: [`OptimizationTask`](#abaqus.Optimization.OptimizationTask.OptimizationTask "abaqus.Optimization.OptimizationTask.OptimizationTask (Python class) — Bases: OptimizationTaskBase")

    The BeadTask object defines a bead task. The BeadTask object is derived from the OptimizationTask object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name]
    ```

    Note

    Check [BeadTask on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadtaskpyc.htm?contextscope=all).

    Member Details:

    abaqusSensitivities : --is-rst--Boolean = `False`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L55-L57)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.abaqusSensitivities "Permalink to this definition")
    :   A Boolean specifying whether to use Abaqus to compute the design responses and their
        sensitivities. The default value is False.

        New in version 2019: The `abaqusSensitivities` attribute was added.

    algorithm : --is-rst--SymbolicConstant = `'GENERAL_OPTIMIZATION'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L59-L62)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.algorithm "Permalink to this definition")
    :   A SymbolicConstant specifying the optimization task algorithm. Possible values are
        GENERAL\_OPTIMIZATION and CONDITION\_BASED\_OPTIMIZATION. The default value is
        GENERAL\_OPTIMIZATION.

    areBCRegionsFrozen : --is-rst--Boolean = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L64-L66)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.areBCRegionsFrozen "Permalink to this definition")
    :   A Boolean specifying whether to exclude elements with boundary conditions from the
        optimization. The default value is OFF.

    beadIter : --is-rst--int = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L68-L69)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.beadIter "Permalink to this definition")
    :   An int specifying the step size of the optimization. The default value is 1.

    beadMaxMembraneStress : --is-rst--float = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L71-L72)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.beadMaxMembraneStress "Permalink to this definition")
    :   A float specifying maximum membrane/bending stress. The default value is 0.1.

    beadMinStress : --is-rst--float = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L74-L75)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.beadMinStress "Permalink to this definition")
    :   A float specifying minimum stress. The default value is 0.001.

    beadPerturbation : --is-rst--float = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L77-L78)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.beadPerturbation "Permalink to this definition")
    :   A Sets perturbation size for finite differences. The default value is 0.0001.

    beadWidth : --is-rst--SymbolicConstant = `'DEFAULT'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L80-L82)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.beadWidth "Permalink to this definition")
    :   A SymbolicConstant specifying the Optimization product default or a float specifying the
        bead width. The default value is DEFAULT.

    curveSmooth : --is-rst--float = `5`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L84-L86)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.curveSmooth "Permalink to this definition")
    :   A float specifying relative value to the middle element edge length such that normals in
        this area do not cross each other. The default value is 5.

    designResponses : --is-rst--dict[str, DesignResponse] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L37-L38)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.designResponses "Permalink to this definition")
    :   A repository of DesignResponse objects.

    filterRadius : --is-rst--float = `4`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L88-L89)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.filterRadius "Permalink to this definition")
    :   A float specifying the filter radius. The default value is 4.

    filterRadiusBy : --is-rst--SymbolicConstant = `'VALUE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L91-L93)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.filterRadiusBy "Permalink to this definition")
    :   A SymbolicConstant specifying the method used to define filter radius. Possible values
        are VALUE and REFERENCE. The default is VALUE.

    flipNormalDir : --is-rst--Boolean = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L95-L97)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.flipNormalDir "Permalink to this definition")
    :   A Boolean specifying whether the growth direction is along the normal direction of
        elements or opposite to the normal direction. The default value is OFF

    frozenBoundaryConditionRegion : --is-rst--SymbolicConstant = `'MODEL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L99-L105)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.frozenBoundaryConditionRegion "Permalink to this definition")
    :   When nodes with boundary conditions are excluded from the optimization
        (*frozenBoundaryConditionRegions* = ON). you can specify that this exclusion apply to
        nodes throughout the model or only to those nodes from a specific region. Set this
        parameter to the SymbolicConstant MODEL to apply the freeze to the entire model, or set
        this parameter to a Region object to specify an individual region over which nodes with
        boundary conditions should be frozen. The default value is MODEL.

    geometricRestrictions : --is-rst--dict[str, GeometricRestriction] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L46-L47)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.geometricRestrictions "Permalink to this definition")
    :   A repository of GeometricRestriction objects.

    groupOperator : --is-rst--Boolean = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L140-L142)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.groupOperator "Permalink to this definition")
    :   A Boolean specifying whether the group in the design response will be evaluated using
        the existing algorithm or a new algorithm based on Abaqus sensitivities. The default
        value of False means that the existing algorithm will be used.

        New in version 2022: The `groupSensitivities` attribute was added.

    isSensCalcOnlyOnDesignNodes : --is-rst--Boolean = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L107-L109)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.isSensCalcOnlyOnDesignNodes "Permalink to this definition")
    :   A Boolean specifying whether to calculate the sensitivities only on design nodes or the
        whole model. The default value is ON

    modeTrackingRegion : --is-rst--SymbolicConstant = `'MODEL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L111-L113)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.modeTrackingRegion "Permalink to this definition")
    :   The SymbolicConstant MODEL or a Region object specifying the region to use for mode
        tracking. The default value is MODEL.

    nodalMoveLimit : --is-rst--float = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L115-L117)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.nodalMoveLimit "Permalink to this definition")
    :   A Float specifying the maximum change in nodal displacement per design cycle. The
        default value is 0.1.

    nodeSmooth : --is-rst--SymbolicConstant = `'DEFAULT'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L80-L82)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.nodeSmooth "Permalink to this definition")
    :   A SymbolicConstant specifying the Optimization product default or a float specifying the
        node smooth. The default value is DEFAULT.

    nodeUpdateStrategy : --is-rst--SymbolicConstant = `'CONSERVATIVE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L123-L126)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.nodeUpdateStrategy "Permalink to this definition")
    :   A SymbolicConstant specifying the strategy for how the nodal displacements are updated
        in the method of moving asymptotes. Possible values are NORMAL, CONSERVATIVE, and
        AGGRESSIVE. The default value is CONSERVATIVE.

    numTrackedModes : --is-rst--int = `5`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L128-L129)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.numTrackedModes "Permalink to this definition")
    :   An Int specifying the number of modes included in mode tracking. The default value is 5.

    objectiveFunctions : --is-rst--dict[str, ObjectiveFunction] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L40-L41)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.objectiveFunctions "Permalink to this definition")
    :   A repository of ObjectiveFunction objects.

    optimizationConstraints : --is-rst--dict[str, OptimizationConstraint] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L43-L44)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.optimizationConstraints "Permalink to this definition")
    :   A repository of OptimizationConstraint objects.

    setValues(*[abaqusSensitivities](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.abaqusSensitivities "abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.abaqusSensitivities (Python parameter) — A Boolean specifying whether to use Abaqus to compute the design responses and their sensitivities.")=`True`*, *[algorithm](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.algorithm "abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.algorithm (Python parameter) — A SymbolicConstant specifying the optimization task algorithm.")=`abaqusConstants.GENERAL_OPTIMIZATION`*, *[areBCRegionsFrozen](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.areBCRegionsFrozen "abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.areBCRegionsFrozen (Python parameter) — A Boolean specifying whether to exclude elements with boundary conditions from the optimization.")=`0`*, *[beadIter](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.beadIter "abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.beadIter (Python parameter) — An int specifying the step size of the optimization.")=`1`*, *[beadMaxMembraneStress](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.beadMaxMembraneStress "abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.beadMaxMembraneStress (Python parameter) — A float specifying maximum membrane/bending stress.")=`0`*, *[beadMinStress](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.beadMinStress "abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.beadMinStress (Python parameter) — A float specifying minimum stress.")=`0`*, *[beadPerturbation](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.beadPerturbation "abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.beadPerturbation (Python parameter) — A Sets perturbation size for finite differences.")=`0`*, *[beadWidth](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.beadWidth "abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.beadWidth (Python parameter) — A SymbolicConstant specifying the Optimization product default or a float specifying the bead width.")=`abaqusConstants.DEFAULT`*, *[curveSmooth](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.curveSmooth "abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.curveSmooth (Python parameter) — A float specifying relative value to the middle element edge length such that normals in this area do not cross each other.")=`5`*, *[filterRadius](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.filterRadius "abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.filterRadius (Python parameter) — A float specifying the filter radius.")=`4`*, *[filterRadiusBy](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.filterRadiusBy "abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.filterRadiusBy (Python parameter) — A SymbolicConstant specifying the method used to define filter radius.")=`abaqusConstants.VALUE`*, *[flipNormalDir](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.flipNormalDir "abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.flipNormalDir (Python parameter) — A Boolean specifying whether the growth direction is along the normal direction of elements or opposite to the normal direction.")=`0`*, *[frozenBoundaryConditionRegion](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.frozenBoundaryConditionRegion "abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.frozenBoundaryConditionRegion (Python parameter) — When nodes with boundary conditions are excluded from the optimization (frozenBoundaryConditionRegions = ON).")=`abaqusConstants.MODEL`*, *[isSensCalcOnlyOnDesignNodes](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.isSensCalcOnlyOnDesignNodes "abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.isSensCalcOnlyOnDesignNodes (Python parameter) — A Boolean specifying whether to calculate the sensitivities only on design nodes or the whole model.")=`0`*, *[modeTrackingRegion](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.modeTrackingRegion "abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.modeTrackingRegion (Python parameter) — The SymbolicConstant MODEL or a Region object specifying the region to use for mode tracking.")=`abaqusConstants.MODEL`*, *[nodalMoveLimit](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.nodalMoveLimit "abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.nodalMoveLimit (Python parameter) — A Float specifying the maximum change in nodal displacement per design cycle.")=`0`*, *[nodeSmooth](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.nodeSmooth "abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.nodeSmooth (Python parameter) — A SymbolicConstant specifying the Optimization product default or a float specifying the node smooth.")=`abaqusConstants.DEFAULT`*, *[nodeUpdateStrategy](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.nodeUpdateStrategy "abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.nodeUpdateStrategy (Python parameter) — A SymbolicConstant specifying the strategy for how the nodal displacements are updated in the method of moving asymptotes.")=`abaqusConstants.CONSERVATIVE`*, *[numTrackedModes](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.numTrackedModes "abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.numTrackedModes (Python parameter) — An Int specifying the number of modes included in mode tracking.")=`5`*, *[updateShapeBasisVectors](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.updateShapeBasisVectors "abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.updateShapeBasisVectors (Python parameter) — A SymbolicConstant specifying whether to update shape basis vectors in the first design cycle or every design cycle.")=`abaqusConstants.EVERY_CYCLE`*, *[groupOperator](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.groupOperator "abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.groupOperator (Python parameter) — A Boolean specifying whether the group in the design response will be evaluated using the existing algorithm or a new algorithm based on Abaqus sensitivities.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L260-L361)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues "Permalink to this definition")
    :   This method modifies the BeadTask object.

        Note

        Check [BeadTask.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beadtaskpyc.htm?contextscope=all#simaker-beadtasksetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues-parameters "Permalink to this headline")
        :   abaqusSensitivities=`True`[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.abaqusSensitivities "Permalink to this definition")
            :   A Boolean specifying whether to use Abaqus to compute the design responses and their
                sensitivities. The default value is True.

                New in version 2019: The `abaqusSensitivities` argument was added.

            algorithm=`abaqusConstants.GENERAL_OPTIMIZATION`[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.algorithm "Permalink to this definition")
            :   A SymbolicConstant specifying the optimization task algorithm. Possible values are
                GENERAL\_OPTIMIZATION and CONDITION\_BASED\_OPTIMIZATION. The default value is
                GENERAL\_OPTIMIZATION.

            areBCRegionsFrozen=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.areBCRegionsFrozen "Permalink to this definition")
            :   A Boolean specifying whether to exclude elements with boundary conditions from the
                optimization. The default value is OFF.

            beadIter=`1`[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.beadIter "Permalink to this definition")
            :   An int specifying the step size of the optimization. The default value is 1.

            beadMaxMembraneStress=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.beadMaxMembraneStress "Permalink to this definition")
            :   A float specifying maximum membrane/bending stress. The default value is 0.1.

            beadMinStress=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.beadMinStress "Permalink to this definition")
            :   A float specifying minimum stress. The default value is 0.001.

            beadPerturbation=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.beadPerturbation "Permalink to this definition")
            :   A Sets perturbation size for finite differences. The default value is 0.0001.

            beadWidth=`abaqusConstants.DEFAULT`[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.beadWidth "Permalink to this definition")
            :   A SymbolicConstant specifying the Optimization product default or a float specifying the
                bead width. The default value is DEFAULT.

            curveSmooth=`5`[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.curveSmooth "Permalink to this definition")
            :   A float specifying relative value to the middle element edge length such that normals in
                this area do not cross each other. The default value is 5.

            filterRadius=`4`[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.filterRadius "Permalink to this definition")
            :   A float specifying the filter radius. The default value is 4.

            filterRadiusBy=`abaqusConstants.VALUE`[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.filterRadiusBy "Permalink to this definition")
            :   A SymbolicConstant specifying the method used to define filter radius. Possible values
                are VALUE and REFERENCE. The default is VALUE.

            flipNormalDir=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.flipNormalDir "Permalink to this definition")
            :   A Boolean specifying whether the growth direction is along the normal direction of
                elements or opposite to the normal direction. The default value is OFF

            frozenBoundaryConditionRegion=`abaqusConstants.MODEL`[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.frozenBoundaryConditionRegion "Permalink to this definition")
            :   When nodes with boundary conditions are excluded from the optimization
                (*frozenBoundaryConditionRegions* = ON). you can specify that this exclusion apply to
                nodes throughout the model or only to those nodes from a specific region. Set this
                parameter to the SymbolicConstant MODEL to apply the freeze to the entire model, or set
                this parameter to a Region object to specify an individual region over which nodes with
                boundary conditions should be frozen. The default value is MODEL.

            isSensCalcOnlyOnDesignNodes=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.isSensCalcOnlyOnDesignNodes "Permalink to this definition")
            :   A Boolean specifying whether to calculate the sensitivities only on design nodes or the
                whole model. The default value is ON

            modeTrackingRegion=`abaqusConstants.MODEL`[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.modeTrackingRegion "Permalink to this definition")
            :   The SymbolicConstant MODEL or a Region object specifying the region to use for mode
                tracking. The default value is MODEL.

            nodalMoveLimit=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.nodalMoveLimit "Permalink to this definition")
            :   A Float specifying the maximum change in nodal displacement per design cycle. The
                default value is 0.1.

            nodeSmooth=`abaqusConstants.DEFAULT`[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.nodeSmooth "Permalink to this definition")
            :   A SymbolicConstant specifying the Optimization product default or a float specifying the
                node smooth. The default value is DEFAULT.

            nodeUpdateStrategy=`abaqusConstants.CONSERVATIVE`[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.nodeUpdateStrategy "Permalink to this definition")
            :   A SymbolicConstant specifying the strategy for how the nodal displacements are updated
                in the method of moving asymptotes. Possible values are NORMAL, CONSERVATIVE, and
                AGGRESSIVE. The default value is CONSERVATIVE.

            numTrackedModes=`5`[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.numTrackedModes "Permalink to this definition")
            :   An Int specifying the number of modes included in mode tracking. The default value is 5.

            updateShapeBasisVectors=`abaqusConstants.EVERY_CYCLE`[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.updateShapeBasisVectors "Permalink to this definition")
            :   A SymbolicConstant specifying whether to update shape basis vectors in the first design
                cycle or every design cycle. Possible values are EVERY\_CYCLE and FIRST\_CYCLE. The
                default value is EVERY\_CYCLE.

            groupOperator=`0`[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.setValues.groupOperator "Permalink to this definition")
            :   A Boolean specifying whether the group in the design response will be evaluated using
                the existing algorithm or a new algorithm based on Abaqus sensitivities. The default
                value of False means that the existing algorithm will be used.

                New in version 2022: The `groupOperator` argument was added.

    updateShapeBasisVectors : --is-rst--SymbolicConstant = `'EVERY_CYCLE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskModel.py#L131-L134)[¶](#abaqus.Optimization.OptimizationTaskModel.BeadTask.updateShapeBasisVectors "Permalink to this definition")
    :   A SymbolicConstant specifying whether to update shape basis vectors in the first design
        cycle or every design cycle. Possible values are EVERY\_CYCLE and FIRST\_CYCLE. The
        default value is EVERY\_CYCLE.

*class* DesignResponse[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L6-L20)[¶](#abaqus.Optimization.TopologyTask.DesignResponse "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The DesignResponse object is the abstract base type for other DesignResponse objects. The
    DesponseResponse object has no explicit constructor. The methods and members of the DesignResponse object
    are common to all objects derived from DesignResponse.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].designResponses[name]
    ```

    Note

    Check [DesignResponse on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-designresponsepyc.htm?contextscope=all).

    Member Details:

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L6-L20)[¶](#abaqus.Optimization.TopologyTask.DesignResponse.name "Permalink to this definition")
    :   A String specifying the design response repository key.

*class* ObjectiveFunction(*[name](#abaqus.Optimization.TopologyTask.ObjectiveFunction "abaqus.Optimization.TopologyTask.ObjectiveFunction.__init__.name (Python parameter)")*, *[objectives](#abaqus.Optimization.TopologyTask.ObjectiveFunction "abaqus.Optimization.TopologyTask.ObjectiveFunction.__init__.objectives (Python parameter)")*, *[target](#abaqus.Optimization.TopologyTask.ObjectiveFunction "abaqus.Optimization.TopologyTask.ObjectiveFunction.__init__.target (Python parameter)")=`abaqusConstants.MINIMIZE`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L12-L83)[¶](#abaqus.Optimization.TopologyTask.ObjectiveFunction "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The ObjectiveFunction object defines the objective of the optimization.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].objectiveFunctions[name]
    ```

    Note

    Check [ObjectiveFunction on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-objectivefunctionpyc.htm?contextscope=all).

    Member Details:

    name : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py)[¶](#abaqus.Optimization.TopologyTask.ObjectiveFunction.name "Permalink to this definition")
    :   A String specifying the objective function repository key.

    objectives : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Optimization.OptimizationObjective.OptimizationObjective`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L23-L24)[¶](#abaqus.Optimization.TopologyTask.ObjectiveFunction.objectives "Permalink to this definition")
    :   Optimization objectives

    setValues(*[target](#abaqus.Optimization.TopologyTask.ObjectiveFunction.setValues.target "abaqus.Optimization.TopologyTask.ObjectiveFunction.setValues.target (Python parameter) — A SymbolicConstant specifying the target of the objective function.")=`abaqusConstants.MINIMIZE`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L69-L83)[¶](#abaqus.Optimization.TopologyTask.ObjectiveFunction.setValues "Permalink to this definition")
    :   This method modifies the ObjectiveFunction object.

        Note

        Check [ObjectiveFunction.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-objectivefunctionpyc.htm?contextscope=all#simaker-objectivefunctionsetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.TopologyTask.ObjectiveFunction.setValues-parameters "Permalink to this headline")
        :   target=`abaqusConstants.MINIMIZE`[¶](#abaqus.Optimization.TopologyTask.ObjectiveFunction.setValues.target "Permalink to this definition")
            :   A SymbolicConstant specifying the target of the objective function. Possible values are
                MINIMIZE, MAXIMIZE, and MINIMIZE\_MAXIMUM. The default value is MINIMIZE.

        Raises:[¶](#abaqus.Optimization.TopologyTask.ObjectiveFunction.setValues-raises "Permalink to this headline")
        :   **RangeError** –

    target : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MINIMIZE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L29-L31)[¶](#abaqus.Optimization.TopologyTask.ObjectiveFunction.target "Permalink to this definition")
    :   A SymbolicConstant specifying the target of the objective function. Possible values are
        MINIMIZE, MAXIMIZE, and MINIMIZE\_MAXIMUM. The default value is MINIMIZE.

*class* OptimizationConstraint(*[name](#abaqus.Optimization.TopologyTask.OptimizationConstraint "abaqus.Optimization.TopologyTask.OptimizationConstraint.__init__.name (Python parameter)")*, *[designResponse](#abaqus.Optimization.TopologyTask.OptimizationConstraint "abaqus.Optimization.TopologyTask.OptimizationConstraint.__init__.designResponse (Python parameter)")*, *[restrictionValue](#abaqus.Optimization.TopologyTask.OptimizationConstraint "abaqus.Optimization.TopologyTask.OptimizationConstraint.__init__.restrictionValue (Python parameter)")*, *[restrictionMethod](#abaqus.Optimization.TopologyTask.OptimizationConstraint "abaqus.Optimization.TopologyTask.OptimizationConstraint.__init__.restrictionMethod (Python parameter)")=`abaqusConstants.ABSOLUTE_EQUAL`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L11-L112)[¶](#abaqus.Optimization.TopologyTask.OptimizationConstraint "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The OptimizationConstraint object constrains an optimization from making changes to the topology of the
    model.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].optimizationConstraints[name]
    ```

    Note

    Check [OptimizationConstraint on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optimizationconstraintpyc.htm?contextscope=all).

    Member Details:

    designResponse : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py)[¶](#abaqus.Optimization.TopologyTask.OptimizationConstraint.designResponse "Permalink to this definition")
    :   A String specifying the name of the design response to constrain.

    name : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py)[¶](#abaqus.Optimization.TopologyTask.OptimizationConstraint.name "Permalink to this definition")
    :   A String specifying the optimization constraint repository key.

    restrictionMethod : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'ABSOLUTE_EQUAL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L32-L36)[¶](#abaqus.Optimization.TopologyTask.OptimizationConstraint.restrictionMethod "Permalink to this definition")
    :   A SymbolicConstant specifying the method used to constrain the design response. Possible
        values are ABSOLUTE\_EQUAL, ABSOLUTE\_GREATER\_THAN\_EQUAL, ABSOLUTE\_LESS\_THAN\_EQUAL,
        RELATIVE\_EQUAL, RELATIVE\_GREATER\_THAN\_EQUAL, and RELATIVE\_LESS\_THAN\_EQUAL. The default
        value is ABSOLUTE\_EQUAL.

    restrictionValue : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py)[¶](#abaqus.Optimization.TopologyTask.OptimizationConstraint.restrictionValue "Permalink to this definition")
    :   A Float specifying the value to which the design response should be constrained.

    setValues(*[restrictionMethod](#abaqus.Optimization.TopologyTask.OptimizationConstraint.setValues.restrictionMethod "abaqus.Optimization.TopologyTask.OptimizationConstraint.setValues.restrictionMethod (Python parameter) — A SymbolicConstant specifying the method used to constrain the design response.")=`abaqusConstants.ABSOLUTE_EQUAL`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L86-L112)[¶](#abaqus.Optimization.TopologyTask.OptimizationConstraint.setValues "Permalink to this definition")
    :   This method modifies the OptimizationConstraint object.

        Note

        Check [OptimizationConstraint.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optimizationconstraintpyc.htm?contextscope=all#simaker-optimizationconstraintsetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.TopologyTask.OptimizationConstraint.setValues-parameters "Permalink to this headline")
        :   restrictionMethod=`abaqusConstants.ABSOLUTE_EQUAL`[¶](#abaqus.Optimization.TopologyTask.OptimizationConstraint.setValues.restrictionMethod "Permalink to this definition")
            :   A SymbolicConstant specifying the method used to constrain the design response. Possible
                values are ABSOLUTE\_EQUAL, ABSOLUTE\_GREATER\_THAN\_EQUAL, ABSOLUTE\_LESS\_THAN\_EQUAL,
                RELATIVE\_EQUAL, RELATIVE\_GREATER\_THAN\_EQUAL, and RELATIVE\_LESS\_THAN\_EQUAL. The default
                value is ABSOLUTE\_EQUAL.

        Raises:[¶](#abaqus.Optimization.TopologyTask.OptimizationConstraint.setValues-raises "Permalink to this headline")
        :   **RangeError** –

*class* CombinedTermDesignResponse(*[name](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse "abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.__init__.name (Python parameter)")*, *[terms](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse "abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.__init__.terms (Python parameter)")*, *[filterMaxRadius](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse "abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.__init__.filterMaxRadius (Python parameter)")=`None`*, *[filterExponent](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse "abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.__init__.filterExponent (Python parameter)")=`1`*, *[filterRadiusReduction](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse "abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.__init__.filterRadiusReduction (Python parameter)")=`0`*, *[highCutOff](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse "abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.__init__.highCutOff (Python parameter)")=`None`*, *[lowCutOff](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse "abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.__init__.lowCutOff (Python parameter)")=`0`*, *[method](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse "abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.__init__.method (Python parameter)")=`abaqusConstants.ADD`*, *[weights](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse "abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.__init__.weights (Python parameter)")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/CombinedTermDesignResponse.py#L12-L316)[¶](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse "Permalink to this definition")
:   Bases: [`DesignResponse`](#abaqus.Optimization.TopologyTask.DesignResponse "abaqus.Optimization.DesignResponse.DesignResponse (Python class)")

    The CombinedTermDesignResponse object defines a combined-term design response. The
    CombinedTermDesignResponse object is derived from the DesignResponse object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].designResponses[name]
    ```

    Note

    Check [CombinedTermDesignResponse on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-combinedtermdesignresponsepyc.htm?contextscope=all).

    Member Details:

    filterExponent : --is-rst--:py:class:`float` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/CombinedTermDesignResponse.py#L34-L35)[¶](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.filterExponent "Permalink to this definition")
    :   A Float specifying the exponent used when **method** is FILTER. The default value is 1.0.

    filterMaxRadius : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/CombinedTermDesignResponse.py#L30-L32)[¶](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.filterMaxRadius "Permalink to this definition")
    :   None or a sequence of Floats specifying the maximum radius of influence used when
        **method** is FILTER. The default value is None.

    filterRadiusReduction : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/CombinedTermDesignResponse.py#L37-L39)[¶](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.filterRadiusReduction "Permalink to this definition")
    :   A Float specifying the reduction of the radius depending on surface bending, used when
        **method** is FILTER. The default value is 0.2.

    highCutOff : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/CombinedTermDesignResponse.py#L41-L44)[¶](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.highCutOff "Permalink to this definition")
    :   None or a sequence of Floats specifying the upper bound of the vector value used when
        **method** is CUT\_OFF. All values greater than the **highCutOff** are set to the
        **highCutOff** value. The default value is None.

    lowCutOff : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/CombinedTermDesignResponse.py#L46-L48)[¶](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.lowCutOff "Permalink to this definition")
    :   A Float specifying the lower bound of the vector value used when **method** is CUT\_OFF.
        All values less than the **lowCutOff** are treated as 0. The default value is 0.0.

    method : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'ADD'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/CombinedTermDesignResponse.py#L85-L86)[¶](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.method "Permalink to this definition")
    :   * ABSOLUTE\_DIFFERENCE
        * ABSOLUTE\_VALUE
        * ADD
        * COSINE
        * CUT\_OFF
        * DELTA\_OVER\_1\_ITERATION
        * DELTA\_OVER\_2\_ITERATIONS
        * DELTA\_OVER\_3\_ITERATIONS
        * DELTA\_OVER\_4\_ITERATIONS
        * DELTA\_OVER\_5\_ITERATIONS
        * DELTA\_OVER\_6\_ITERATIONS
        * DIVIDE
        * EXPONENTIAL
        * FILTER
        * INTEGER
        * LOG
        * MAXIMUM
        * MINIMUM
        * MULTIPLY
        * NATURAL\_LOG
        * NEAREST\_INTEGER
        * NORM
        * NORM\_FIRST
        * NTH\_POWER
        * NTH\_ROOT
        * SIGN
        * SINE
        * SQUARE\_ROOT
        * SUBTRACT
        * TANGENT
        * WEIGHTED\_ADD

        The default value is ADD.

    setValues(*[filterMaxRadius](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.setValues.filterMaxRadius "abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.setValues.filterMaxRadius (Python parameter) — None or a sequence of Floats specifying the maximum radius of influence used when method is FILTER.")=`None`*, *[filterExponent](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.setValues.filterExponent "abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.setValues.filterExponent (Python parameter) — A Float specifying the exponent used when method is FILTER.")=`1`*, *[filterRadiusReduction](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.setValues.filterRadiusReduction "abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.setValues.filterRadiusReduction (Python parameter) — A Float specifying the reduction of the radius depending on surface bending, used when method is FILTER.")=`0`*, *[highCutOff](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.setValues.highCutOff "abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.setValues.highCutOff (Python parameter) — None or a sequence of Floats specifying the upper bound of the vector value used when method is CUT_OFF.")=`None`*, *[lowCutOff](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.setValues.lowCutOff "abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.setValues.lowCutOff (Python parameter) — A Float specifying the lower bound of the vector value used when method is CUT_OFF. All values less than the lowCutOff are treated as 0.")=`0`*, *[method](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.setValues.method "abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.setValues.method (Python parameter) — A SymbolicConstant specifying the method used to combine selected design responses. Possible values are:")=`abaqusConstants.ADD`*, *[weights](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.setValues.weights "abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.setValues.weights (Python parameter) — A sequence of Floats specifying the weights to apply to the list of design responses used when method is WEIGHTED_ADD.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/CombinedTermDesignResponse.py#L213-L316)[¶](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.setValues "Permalink to this definition")
    :   This method modifies the CombinedTermDesignResponse object.

        Note

        Check [CombinedTermDesignResponse.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-combinedtermdesignresponsepyc.htm?contextscope=all#simaker-combinedtermdesignresponsesetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.setValues-parameters "Permalink to this headline")
        :   filterMaxRadius=`None`[¶](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.setValues.filterMaxRadius "Permalink to this definition")
            :   None or a sequence of Floats specifying the maximum radius of influence used when
                **method** is FILTER. The default value is None.

            filterExponent=`1`[¶](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.setValues.filterExponent "Permalink to this definition")
            :   A Float specifying the exponent used when **method** is FILTER. The default value is 1.0.

            filterRadiusReduction=`0`[¶](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.setValues.filterRadiusReduction "Permalink to this definition")
            :   A Float specifying the reduction of the radius depending on surface bending, used when
                **method** is FILTER. The default value is 0.2.

            highCutOff=`None`[¶](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.setValues.highCutOff "Permalink to this definition")
            :   None or a sequence of Floats specifying the upper bound of the vector value used when
                **method** is CUT\_OFF. All values greater than the **highCutOff** are set to the
                **highCutOff** value. The default value is None.

            lowCutOff=`0`[¶](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.setValues.lowCutOff "Permalink to this definition")
            :   A Float specifying the lower bound of the vector value used when **method** is CUT\_OFF.
                All values less than the **lowCutOff** are treated as 0. The default value is 0.0.

            method=`abaqusConstants.ADD`[¶](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.setValues.method "Permalink to this definition")
            :   A SymbolicConstant specifying the method used to combine selected design responses.
                Possible values are:

                * ABSOLUTE\_DIFFERENCE
                * ABSOLUTE\_VALUE
                * ADD
                * COSINE
                * CUT\_OFF
                * DELTA\_OVER\_1\_ITERATION
                * DELTA\_OVER\_2\_ITERATIONS
                * DELTA\_OVER\_3\_ITERATIONS
                * DELTA\_OVER\_4\_ITERATIONS
                * DELTA\_OVER\_5\_ITERATIONS
                * DELTA\_OVER\_6\_ITERATIONS
                * DIVIDE
                * EXPONENTIAL
                * FILTER
                * INTEGER
                * LOG
                * MAXIMUM
                * MINIMUM
                * MULTIPLY
                * NATURAL\_LOG
                * NEAREST\_INTEGER
                * NORM
                * NORM\_FIRST
                * NTH\_POWER
                * NTH\_ROOT
                * SIGN
                * SINE
                * SQUARE\_ROOT
                * SUBTRACT
                * TANGENT
                * WEIGHTED\_ADD

                The default value is ADD.

            weights=`()`[¶](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.setValues.weights "Permalink to this definition")
            :   A sequence of Floats specifying the weights to apply to the list of design responses
                used when **method** is WEIGHTED\_ADD. The default value is an empty sequence.

    terms : --is-rst--:py:class:`tuple`\[:py:class:`str`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/CombinedTermDesignResponse.py#L27-L28)[¶](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.terms "Permalink to this definition")
    :   A sequence of Strings specifying the names of the design responses to combine.

    weights : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/CombinedTermDesignResponse.py#L88-L90)[¶](#abaqus.Optimization.CombinedTermDesignResponse.CombinedTermDesignResponse.weights "Permalink to this definition")
    :   A sequence of Floats specifying the weights to apply to the list of design responses
        used when **method** is WEIGHTED\_ADD. The default value is an empty sequence.

*class* DesignDirection(*[name](#abaqus.Optimization.OptimizationTask.DesignDirection "abaqus.Optimization.OptimizationTask.DesignDirection.__init__.name (Python parameter)")*, *[region](#abaqus.Optimization.OptimizationTask.DesignDirection "abaqus.Optimization.OptimizationTask.DesignDirection.__init__.region (Python parameter)")*, *[csys](#abaqus.Optimization.OptimizationTask.DesignDirection "abaqus.Optimization.OptimizationTask.DesignDirection.__init__.csys (Python parameter)")=`None`*, *[mainPoint](#abaqus.Optimization.OptimizationTask.DesignDirection "abaqus.Optimization.OptimizationTask.DesignDirection.__init__.mainPoint (Python parameter)")=`None`*, *[mainPointDetermination](#abaqus.Optimization.OptimizationTask.DesignDirection "abaqus.Optimization.OptimizationTask.DesignDirection.__init__.mainPointDetermination (Python parameter)")=`abaqusConstants.MAXIMUM`*, *[movementRestriction](#abaqus.Optimization.OptimizationTask.DesignDirection "abaqus.Optimization.OptimizationTask.DesignDirection.__init__.movementRestriction (Python parameter)")=`abaqusConstants.VECTOR`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.OptimizationTask.DesignDirection "abaqus.Optimization.OptimizationTask.DesignDirection.__init__.presumeFeasibleRegionAtStart (Python parameter)")=`1`*, *[u1](#abaqus.Optimization.OptimizationTask.DesignDirection "abaqus.Optimization.OptimizationTask.DesignDirection.__init__.u1 (Python parameter)")=`1`*, *[u2](#abaqus.Optimization.OptimizationTask.DesignDirection "abaqus.Optimization.OptimizationTask.DesignDirection.__init__.u2 (Python parameter)")=`1`*, *[u3](#abaqus.Optimization.OptimizationTask.DesignDirection "abaqus.Optimization.OptimizationTask.DesignDirection.__init__.u3 (Python parameter)")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L19-L209)[¶](#abaqus.Optimization.OptimizationTask.DesignDirection "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The DesignDirection object defines a design direction geometric restriction. The DesignDirection object
    is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [DesignDirection on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-designdirectionpyc.htm?contextscope=all).

    Member Details:

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L39-L42)[¶](#abaqus.Optimization.OptimizationTask.DesignDirection.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
        global coordinate system is used. When this member is queried, it returns an Int. The
        default value is None.

    mainPoint : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L47-L49)[¶](#abaqus.Optimization.OptimizationTask.DesignDirection.mainPoint "Permalink to this definition")
    :   None or a Region object specifying the main point used when **mainPointDetermination** is
        SPECIFY. The default value is None.

        Changed in version 2022: The attribute `masterPoint` was renamed to `mainPoint`.

    mainPointDetermination : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MAXIMUM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L47-L49)[¶](#abaqus.Optimization.OptimizationTask.DesignDirection.mainPointDetermination "Permalink to this definition")
    :   A SymbolicConstant specifying the rule for assigning point priority. Possible values are
        MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.

        Changed in version 2022: The attribute `masterPointDetermination` was renamed to `mainPointDetermination`.

    movementRestriction : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'VECTOR'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L58-L62)[¶](#abaqus.Optimization.OptimizationTask.DesignDirection.movementRestriction "Permalink to this definition")
    :   A SymbolicConstant specifying whether movement in the region should follow only the
        direction of the **mainPoint**, only the magnitude, or both the magnitude of the
        **mainPoint** and the directions specified by **u1**, **u2** and **u3**. Possible values are
        DIRECTION, MAGNITUDE, and VECTOR. The default value is VECTOR.

    presumeFeasibleRegionAtStart : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L64-L66)[¶](#abaqus.Optimization.OptimizationTask.DesignDirection.presumeFeasibleRegionAtStart "Permalink to this definition")
    :   A Boolean specifying whether to ignore the geometric restriction in the first design
        cycle. The default value is ON.

    setValues(*[csys](#abaqus.Optimization.OptimizationTask.DesignDirection.setValues.csys "abaqus.Optimization.OptimizationTask.DesignDirection.setValues.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[mainPoint](#abaqus.Optimization.OptimizationTask.DesignDirection.setValues.mainPoint "abaqus.Optimization.OptimizationTask.DesignDirection.setValues.mainPoint (Python parameter) — None or a Region object specifying the main point used when mainPointDetermination is SPECIFY.")=`None`*, *[mainPointDetermination](#abaqus.Optimization.OptimizationTask.DesignDirection.setValues.mainPointDetermination "abaqus.Optimization.OptimizationTask.DesignDirection.setValues.mainPointDetermination (Python parameter) — A SymbolicConstant specifying the rule for assigning point priority.")=`abaqusConstants.MAXIMUM`*, *[movementRestriction](#abaqus.Optimization.OptimizationTask.DesignDirection.setValues.movementRestriction "abaqus.Optimization.OptimizationTask.DesignDirection.setValues.movementRestriction (Python parameter) — A SymbolicConstant specifying whether movement in the region should follow only the direction of the mainPoint, only the magnitude, or both the magnitude of the mainPoint and the directions specified by u1, u2 and u3.")=`abaqusConstants.VECTOR`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.OptimizationTask.DesignDirection.setValues.presumeFeasibleRegionAtStart "abaqus.Optimization.OptimizationTask.DesignDirection.setValues.presumeFeasibleRegionAtStart (Python parameter) — A Boolean specifying whether to ignore the geometric restriction in the first design cycle.")=`1`*, *[u1](#abaqus.Optimization.OptimizationTask.DesignDirection.setValues.u1 "abaqus.Optimization.OptimizationTask.DesignDirection.setValues.u1 (Python parameter) — A Boolean specifying whether movement in the region should follow the masterPoint in the 1-direction.")=`1`*, *[u2](#abaqus.Optimization.OptimizationTask.DesignDirection.setValues.u2 "abaqus.Optimization.OptimizationTask.DesignDirection.setValues.u2 (Python parameter) — A Boolean specifying whether movement in the region should follow the masterPoint in the 2-direction.")=`1`*, *[u3](#abaqus.Optimization.OptimizationTask.DesignDirection.setValues.u3 "abaqus.Optimization.OptimizationTask.DesignDirection.setValues.u3 (Python parameter) — A Boolean specifying whether movement in the region should follow the masterPoint in the 3-direction.")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L156-L209)[¶](#abaqus.Optimization.OptimizationTask.DesignDirection.setValues "Permalink to this definition")
    :   This method modifies the DesignDirection object.

        Note

        Check [DesignDirection.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-designdirectionpyc.htm?contextscope=all#simaker-designdirectionsetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.DesignDirection.setValues-parameters "Permalink to this headline")
        :   csys=`None`[¶](#abaqus.Optimization.OptimizationTask.DesignDirection.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            mainPoint=`None`[¶](#abaqus.Optimization.OptimizationTask.DesignDirection.setValues.mainPoint "Permalink to this definition")
            :   None or a Region object specifying the main point used when **mainPointDetermination** is
                SPECIFY. The default value is None.

                Changed in version 2022: The argument `masterPoint` was renamed to `mainPoint`.

            mainPointDetermination=`abaqusConstants.MAXIMUM`[¶](#abaqus.Optimization.OptimizationTask.DesignDirection.setValues.mainPointDetermination "Permalink to this definition")
            :   A SymbolicConstant specifying the rule for assigning point priority. Possible values are
                MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.

                Changed in version 2022: The argument `masterPointDetermination` was renamed to `mainPointDetermination`.

            movementRestriction=`abaqusConstants.VECTOR`[¶](#abaqus.Optimization.OptimizationTask.DesignDirection.setValues.movementRestriction "Permalink to this definition")
            :   A SymbolicConstant specifying whether movement in the region should follow only the
                direction of the **mainPoint**, only the magnitude, or both the magnitude of the
                **mainPoint** and the directions specified by **u1**, **u2** and **u3**. Possible values are
                DIRECTION, MAGNITUDE, and VECTOR. The default value is VECTOR.

            presumeFeasibleRegionAtStart=`1`[¶](#abaqus.Optimization.OptimizationTask.DesignDirection.setValues.presumeFeasibleRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore the geometric restriction in the first design
                cycle. The default value is ON.

            u1=`1`[¶](#abaqus.Optimization.OptimizationTask.DesignDirection.setValues.u1 "Permalink to this definition")
            :   A Boolean specifying whether movement in the region should follow the **masterPoint** in
                the 1-direction. This is used when **movementRestriction** is VECTOR. The default value is
                ON.

            u2=`1`[¶](#abaqus.Optimization.OptimizationTask.DesignDirection.setValues.u2 "Permalink to this definition")
            :   A Boolean specifying whether movement in the region should follow the **masterPoint** in
                the 2-direction. This is used when **movementRestriction** is VECTOR. The default value is
                ON.

            u3=`1`[¶](#abaqus.Optimization.OptimizationTask.DesignDirection.setValues.u3 "Permalink to this definition")
            :   A Boolean specifying whether movement in the region should follow the **masterPoint** in
                the 3-direction. This is used when **movementRestriction** is VECTOR. The default value is
                ON.

    u1 : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L68-L71)[¶](#abaqus.Optimization.OptimizationTask.DesignDirection.u1 "Permalink to this definition")
    :   A Boolean specifying whether movement in the region should follow the **masterPoint** in
        the 1-direction. This is used when **movementRestriction** is VECTOR. The default value is
        ON.

    u2 : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L68-L71)[¶](#abaqus.Optimization.OptimizationTask.DesignDirection.u2 "Permalink to this definition")
    :   A Boolean specifying whether movement in the region should follow the **masterPoint** in
        the 2-direction. This is used when **movementRestriction** is VECTOR. The default value is
        ON.

    u3 : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L68-L71)[¶](#abaqus.Optimization.OptimizationTask.DesignDirection.u3 "Permalink to this definition")
    :   A Boolean specifying whether movement in the region should follow the **masterPoint** in
        the 3-direction. This is used when **movementRestriction** is VECTOR. The default value is
        ON.

*class* DrillControl(*[name](#abaqus.Optimization.OptimizationTask.DrillControl "abaqus.Optimization.OptimizationTask.DrillControl.__init__.name (Python parameter)")*, *[clientDirection](#abaqus.Optimization.OptimizationTask.DrillControl "abaqus.Optimization.OptimizationTask.DrillControl.__init__.clientDirection (Python parameter)")*, *[region](#abaqus.Optimization.OptimizationTask.DrillControl "abaqus.Optimization.OptimizationTask.DrillControl.__init__.region (Python parameter)")*, *[csys](#abaqus.Optimization.OptimizationTask.DrillControl "abaqus.Optimization.OptimizationTask.DrillControl.__init__.csys (Python parameter)")=`None`*, *[drawAngle](#abaqus.Optimization.OptimizationTask.DrillControl "abaqus.Optimization.OptimizationTask.DrillControl.__init__.drawAngle (Python parameter)")=`0`*, *[mainPoint](#abaqus.Optimization.OptimizationTask.DrillControl "abaqus.Optimization.OptimizationTask.DrillControl.__init__.mainPoint (Python parameter)")=`None`*, *[mainPointDetermination](#abaqus.Optimization.OptimizationTask.DrillControl "abaqus.Optimization.OptimizationTask.DrillControl.__init__.mainPointDetermination (Python parameter)")=`abaqusConstants.MAXIMUM`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.OptimizationTask.DrillControl "abaqus.Optimization.OptimizationTask.DrillControl.__init__.presumeFeasibleRegionAtStart (Python parameter)")=`1`*, *[tolerance1](#abaqus.Optimization.OptimizationTask.DrillControl "abaqus.Optimization.OptimizationTask.DrillControl.__init__.tolerance1 (Python parameter)")=`0`*, *[tolerance2](#abaqus.Optimization.OptimizationTask.DrillControl "abaqus.Optimization.OptimizationTask.DrillControl.__init__.tolerance2 (Python parameter)")=`0`*, *[tolerance3](#abaqus.Optimization.OptimizationTask.DrillControl "abaqus.Optimization.OptimizationTask.DrillControl.__init__.tolerance3 (Python parameter)")=`0`*, *[undercutTolerance](#abaqus.Optimization.OptimizationTask.DrillControl "abaqus.Optimization.OptimizationTask.DrillControl.__init__.undercutTolerance (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L13-L204)[¶](#abaqus.Optimization.OptimizationTask.DrillControl "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The DrillControl object defines a drill control geometric restriction. The DrillControl object is derived
    from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [DrillControl on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-drillcontrolpyc.htm?contextscope=all).

    Member Details:

    clientDirection : --is-rst--:py:class:`tuple`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py)[¶](#abaqus.Optimization.OptimizationTask.DrillControl.clientDirection "Permalink to this definition")
    :   A VertexArray object of length 2 specifying the direction of the drill axis positioned
        at the **csys** origin. Instead of through a ConstrainedSketchVertex, each point may be specified through a
        tuple of coordinates.

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L38-L41)[¶](#abaqus.Optimization.OptimizationTask.DrillControl.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
        global coordinate system is used. When this member is queried, it returns an Int. The
        default value is None.

    drawAngle : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L43-L44)[¶](#abaqus.Optimization.OptimizationTask.DrillControl.drawAngle "Permalink to this definition")
    :   A Float specifying the draw angle. The default value is 0.0.

    mainPoint : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L49-L51)[¶](#abaqus.Optimization.OptimizationTask.DrillControl.mainPoint "Permalink to this definition")
    :   None or a Region object specifying the main point used when **mainPointDetermination** is
        SPECIFY. The default value is None.

        Changed in version 2022: The attribute `masterPoint` was renamed to `mainPoint`.

    mainPointDetermination : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MAXIMUM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L49-L51)[¶](#abaqus.Optimization.OptimizationTask.DrillControl.mainPointDetermination "Permalink to this definition")
    :   A SymbolicConstant specifying the rule for assigning point priority. Possible values are
        MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.

        Changed in version 2022: The attribute `masterPointDetermination` was renamed to `mainPointDetermination`.

    presumeFeasibleRegionAtStart : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L60-L62)[¶](#abaqus.Optimization.OptimizationTask.DrillControl.presumeFeasibleRegionAtStart "Permalink to this definition")
    :   A Boolean specifying whether to ignore the geometric restriction in the first design
        cycle. The default value is ON.

    setValues(*[csys](#abaqus.Optimization.OptimizationTask.DrillControl.setValues.csys "abaqus.Optimization.OptimizationTask.DrillControl.setValues.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[drawAngle](#abaqus.Optimization.OptimizationTask.DrillControl.setValues.drawAngle "abaqus.Optimization.OptimizationTask.DrillControl.setValues.drawAngle (Python parameter) — A Float specifying the draw angle.")=`0`*, *[mainPoint](#abaqus.Optimization.OptimizationTask.DrillControl.setValues.mainPoint "abaqus.Optimization.OptimizationTask.DrillControl.setValues.mainPoint (Python parameter) — None or a Region object specifying the main point used when mainPointDetermination is SPECIFY.")=`None`*, *[mainPointDetermination](#abaqus.Optimization.OptimizationTask.DrillControl.setValues.mainPointDetermination "abaqus.Optimization.OptimizationTask.DrillControl.setValues.mainPointDetermination (Python parameter) — A SymbolicConstant specifying the rule for assigning point priority.")=`abaqusConstants.MAXIMUM`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.OptimizationTask.DrillControl.setValues.presumeFeasibleRegionAtStart "abaqus.Optimization.OptimizationTask.DrillControl.setValues.presumeFeasibleRegionAtStart (Python parameter) — A Boolean specifying whether to ignore the geometric restriction in the first design cycle.")=`1`*, *[tolerance1](#abaqus.Optimization.OptimizationTask.DrillControl.setValues.tolerance1 "abaqus.Optimization.OptimizationTask.DrillControl.setValues.tolerance1 (Python parameter) — A Float specifying the geometric tolerance in the 1-direction.")=`0`*, *[tolerance2](#abaqus.Optimization.OptimizationTask.DrillControl.setValues.tolerance2 "abaqus.Optimization.OptimizationTask.DrillControl.setValues.tolerance2 (Python parameter) — A Float specifying the geometric tolerance in the 2-direction.")=`0`*, *[tolerance3](#abaqus.Optimization.OptimizationTask.DrillControl.setValues.tolerance3 "abaqus.Optimization.OptimizationTask.DrillControl.setValues.tolerance3 (Python parameter) — A Float specifying the geometric tolerance in the 3-direction.")=`0`*, *[undercutTolerance](#abaqus.Optimization.OptimizationTask.DrillControl.setValues.undercutTolerance "abaqus.Optimization.OptimizationTask.DrillControl.setValues.undercutTolerance (Python parameter) — A Float specifying the undercut tolerance.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L154-L204)[¶](#abaqus.Optimization.OptimizationTask.DrillControl.setValues "Permalink to this definition")
    :   This method modifies the DrillControl object.

        Note

        Check [DrillControl.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-drillcontrolpyc.htm?contextscope=all#simaker-drillcontrolsetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.DrillControl.setValues-parameters "Permalink to this headline")
        :   csys=`None`[¶](#abaqus.Optimization.OptimizationTask.DrillControl.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            drawAngle=`0`[¶](#abaqus.Optimization.OptimizationTask.DrillControl.setValues.drawAngle "Permalink to this definition")
            :   A Float specifying the draw angle. The default value is 0.0.

            mainPoint=`None`[¶](#abaqus.Optimization.OptimizationTask.DrillControl.setValues.mainPoint "Permalink to this definition")
            :   None or a Region object specifying the main point used when **mainPointDetermination** is
                SPECIFY. The default value is None.

                Changed in version 2022: The argument `masterPoint` was renamed to `mainPoint`.

            mainPointDetermination=`abaqusConstants.MAXIMUM`[¶](#abaqus.Optimization.OptimizationTask.DrillControl.setValues.mainPointDetermination "Permalink to this definition")
            :   A SymbolicConstant specifying the rule for assigning point priority. Possible values are
                MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.

                Changed in version 2022: The argument `masterPointDetermination` was renamed to `mainPointDetermination`.

            presumeFeasibleRegionAtStart=`1`[¶](#abaqus.Optimization.OptimizationTask.DrillControl.setValues.presumeFeasibleRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore the geometric restriction in the first design
                cycle. The default value is ON.

            tolerance1=`0`[¶](#abaqus.Optimization.OptimizationTask.DrillControl.setValues.tolerance1 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 1-direction. The default value is
                0.01.

            tolerance2=`0`[¶](#abaqus.Optimization.OptimizationTask.DrillControl.setValues.tolerance2 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 2-direction. The default value is
                0.01.

            tolerance3=`0`[¶](#abaqus.Optimization.OptimizationTask.DrillControl.setValues.tolerance3 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 3-direction. The default value is
                0.01.

            undercutTolerance=`0`[¶](#abaqus.Optimization.OptimizationTask.DrillControl.setValues.undercutTolerance "Permalink to this definition")
            :   A Float specifying the undercut tolerance. The default value is 0.0.

    tolerance1 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L64-L66)[¶](#abaqus.Optimization.OptimizationTask.DrillControl.tolerance1 "Permalink to this definition")
    :   A Float specifying the geometric tolerance in the 1-direction. The default value is
        0.01.

    tolerance2 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L68-L70)[¶](#abaqus.Optimization.OptimizationTask.DrillControl.tolerance2 "Permalink to this definition")
    :   A Float specifying the geometric tolerance in the 2-direction. The default value is
        0.01.

    tolerance3 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L72-L74)[¶](#abaqus.Optimization.OptimizationTask.DrillControl.tolerance3 "Permalink to this definition")
    :   A Float specifying the geometric tolerance in the 3-direction. The default value is
        0.01.

    undercutTolerance : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L76-L77)[¶](#abaqus.Optimization.OptimizationTask.DrillControl.undercutTolerance "Permalink to this definition")
    :   A Float specifying the undercut tolerance. The default value is 0.0.

*class* FixedRegion(*[name](#abaqus.Optimization.OptimizationTask.FixedRegion "abaqus.Optimization.OptimizationTask.FixedRegion.__init__.name (Python parameter)")*, *[region](#abaqus.Optimization.OptimizationTask.FixedRegion "abaqus.Optimization.OptimizationTask.FixedRegion.__init__.region (Python parameter)")*, *[csys](#abaqus.Optimization.OptimizationTask.FixedRegion "abaqus.Optimization.OptimizationTask.FixedRegion.__init__.csys (Python parameter)")=`None`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.OptimizationTask.FixedRegion "abaqus.Optimization.OptimizationTask.FixedRegion.__init__.presumeFeasibleRegionAtStart (Python parameter)")=`1`*, *[u1](#abaqus.Optimization.OptimizationTask.FixedRegion "abaqus.Optimization.OptimizationTask.FixedRegion.__init__.u1 (Python parameter)")=`0`*, *[u2](#abaqus.Optimization.OptimizationTask.FixedRegion "abaqus.Optimization.OptimizationTask.FixedRegion.__init__.u2 (Python parameter)")=`0`*, *[u3](#abaqus.Optimization.OptimizationTask.FixedRegion "abaqus.Optimization.OptimizationTask.FixedRegion.__init__.u3 (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L10-L131)[¶](#abaqus.Optimization.OptimizationTask.FixedRegion "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The FixedRegion object defines a fixed region geometric restriction. The FixedRegion object is derived
    from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [FixedRegion on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fixedregionpyc.htm?contextscope=all).

    Member Details:

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L30-L33)[¶](#abaqus.Optimization.OptimizationTask.FixedRegion.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
        global coordinate system is used. When this member is queried, it returns an Int. The
        default value is None.

    presumeFeasibleRegionAtStart : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L35-L37)[¶](#abaqus.Optimization.OptimizationTask.FixedRegion.presumeFeasibleRegionAtStart "Permalink to this definition")
    :   A Boolean specifying whether to ignore the geometric restriction in the first design
        cycle. The default value is ON.

    setValues(*[csys](#abaqus.Optimization.OptimizationTask.FixedRegion.setValues.csys "abaqus.Optimization.OptimizationTask.FixedRegion.setValues.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.OptimizationTask.FixedRegion.setValues.presumeFeasibleRegionAtStart "abaqus.Optimization.OptimizationTask.FixedRegion.setValues.presumeFeasibleRegionAtStart (Python parameter) — A Boolean specifying whether to ignore the geometric restriction in the first design cycle.")=`1`*, *[u1](#abaqus.Optimization.OptimizationTask.FixedRegion.setValues.u1 "abaqus.Optimization.OptimizationTask.FixedRegion.setValues.u1 (Python parameter) — A Boolean specifying whether to fix the region in the 1-direction.")=`0`*, *[u2](#abaqus.Optimization.OptimizationTask.FixedRegion.setValues.u2 "abaqus.Optimization.OptimizationTask.FixedRegion.setValues.u2 (Python parameter) — A Boolean specifying whether to fix the region in the 2-direction.")=`0`*, *[u3](#abaqus.Optimization.OptimizationTask.FixedRegion.setValues.u3 "abaqus.Optimization.OptimizationTask.FixedRegion.setValues.u3 (Python parameter) — A Boolean specifying whether to fix the region in the 3-direction.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L101-L131)[¶](#abaqus.Optimization.OptimizationTask.FixedRegion.setValues "Permalink to this definition")
    :   This method modifies the FixedRegion object.

        Note

        Check [FixedRegion.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fixedregionpyc.htm?contextscope=all#simaker-fixedregionsetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.FixedRegion.setValues-parameters "Permalink to this headline")
        :   csys=`None`[¶](#abaqus.Optimization.OptimizationTask.FixedRegion.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            presumeFeasibleRegionAtStart=`1`[¶](#abaqus.Optimization.OptimizationTask.FixedRegion.setValues.presumeFeasibleRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore the geometric restriction in the first design
                cycle. The default value is ON.

            u1=`0`[¶](#abaqus.Optimization.OptimizationTask.FixedRegion.setValues.u1 "Permalink to this definition")
            :   A Boolean specifying whether to fix the region in the 1-direction. The default value is
                OFF.

            u2=`0`[¶](#abaqus.Optimization.OptimizationTask.FixedRegion.setValues.u2 "Permalink to this definition")
            :   A Boolean specifying whether to fix the region in the 2-direction. The default value is
                OFF.

            u3=`0`[¶](#abaqus.Optimization.OptimizationTask.FixedRegion.setValues.u3 "Permalink to this definition")
            :   A Boolean specifying whether to fix the region in the 3-direction. The default value is
                OFF.

    u1 : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L39-L41)[¶](#abaqus.Optimization.OptimizationTask.FixedRegion.u1 "Permalink to this definition")
    :   A Boolean specifying whether to fix the region in the 1-direction. The default value is
        OFF.

    u2 : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L43-L45)[¶](#abaqus.Optimization.OptimizationTask.FixedRegion.u2 "Permalink to this definition")
    :   A Boolean specifying whether to fix the region in the 2-direction. The default value is
        OFF.

    u3 : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L47-L49)[¶](#abaqus.Optimization.OptimizationTask.FixedRegion.u3 "Permalink to this definition")
    :   A Boolean specifying whether to fix the region in the 3-direction. The default value is
        OFF.

*class* FrozenArea(*[name](#abaqus.Optimization.OptimizationTask.FrozenArea "abaqus.Optimization.OptimizationTask.FrozenArea.__init__.name (Python parameter)")*, *[region=<abaqus.Region.Region.Region object>](#abaqus.Optimization.OptimizationTask.FrozenArea "abaqus.Optimization.OptimizationTask.FrozenArea.__init__.region=<abaqus.Region.Region.Region object> (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L9-L65)[¶](#abaqus.Optimization.OptimizationTask.FrozenArea "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The FrozenArea object defines a frozen area geometric restriction. The FrozenArea object is derived from
    the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [FrozenArea on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-frozenareapyc.htm?contextscope=all).

    Member Details:

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region` = `<abaqus.Region.Region.Region object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L24-L27)[¶](#abaqus.Optimization.OptimizationTask.FrozenArea.region "Permalink to this definition")
    :   A Region object specifying the region to which the geometric restriction is applied.
        When used with a TopologyTask, there is no default value. When used with a ShapeTask,
        the default value is MODEL.

    setValues(*[region=<abaqus.Region.Region.Region object>](#abaqus.Optimization.OptimizationTask.FrozenArea.setValues "abaqus.Optimization.OptimizationTask.FrozenArea.setValues.region=<abaqus.Region.Region.Region object> (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L54-L65)[¶](#abaqus.Optimization.OptimizationTask.FrozenArea.setValues "Permalink to this definition")
    :   This method modifies the FrozenArea object.

        Note

        Check [FrozenArea.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-frozenareapyc.htm?contextscope=all#simaker-frozenareasetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.FrozenArea.setValues-parameters "Permalink to this headline")
        :   region : [`Region`](part_assembly/region.html#abaqus.Region.Surface.Region "abaqus.Region.Region.Region (Python class)"), default: `<abaqus.Region.Region.Region object at 0x7f850c6cbad0>`
            :   A Region object specifying the region to which the geometric restriction is applied.
                When used with a TopologyTask, there is no default value. When used with a ShapeTask,
                the default value is MODEL.

*class* Growth(*[name](#abaqus.Optimization.OptimizationTask.Growth "abaqus.Optimization.OptimizationTask.Growth.__init__.name (Python parameter)")*, *[region](#abaqus.Optimization.OptimizationTask.Growth "abaqus.Optimization.OptimizationTask.Growth.__init__.region (Python parameter)")*, *[growth](#abaqus.Optimization.OptimizationTask.Growth "abaqus.Optimization.OptimizationTask.Growth.__init__.growth (Python parameter)")=`0`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.OptimizationTask.Growth "abaqus.Optimization.OptimizationTask.Growth.__init__.presumeFeasibleRegionAtStart (Python parameter)")=`1`*, *[shrink](#abaqus.Optimization.OptimizationTask.Growth "abaqus.Optimization.OptimizationTask.Growth.__init__.shrink (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L10-L104)[¶](#abaqus.Optimization.OptimizationTask.Growth "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The Growth object defines a growth geometric restriction. The Growth object is derived from the
    GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [Growth on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-growthpyc.htm?contextscope=all).

    Member Details:

    growth : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L30-L32)[¶](#abaqus.Optimization.OptimizationTask.Growth.growth "Permalink to this definition")
    :   A Float specifying the maximum optimization displacement in the growth direction. Either
        **growth** or **shrink** or both must be specified. The default value is 0.0.

    presumeFeasibleRegionAtStart : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L34-L36)[¶](#abaqus.Optimization.OptimizationTask.Growth.presumeFeasibleRegionAtStart "Permalink to this definition")
    :   A Boolean specifying whether to ignore the geometric restriction in the first design
        cycle. The default value is ON.

    setValues(*[growth](#abaqus.Optimization.OptimizationTask.Growth.setValues.growth "abaqus.Optimization.OptimizationTask.Growth.setValues.growth (Python parameter) — A Float specifying the maximum optimization displacement in the growth direction.")=`0`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.OptimizationTask.Growth.setValues.presumeFeasibleRegionAtStart "abaqus.Optimization.OptimizationTask.Growth.setValues.presumeFeasibleRegionAtStart (Python parameter) — A Boolean specifying whether to ignore the geometric restriction in the first design cycle.")=`1`*, *[shrink](#abaqus.Optimization.OptimizationTask.Growth.setValues.shrink "abaqus.Optimization.OptimizationTask.Growth.setValues.shrink (Python parameter) — A Float specifying the maximum optimization displacement in the shrink direction.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L83-L104)[¶](#abaqus.Optimization.OptimizationTask.Growth.setValues "Permalink to this definition")
    :   This method modifies the Growth object.

        Note

        Check [Growth.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-growthpyc.htm?contextscope=all#simaker-growthsetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.OptimizationTask.Growth.setValues-parameters "Permalink to this headline")
        :   growth=`0`[¶](#abaqus.Optimization.OptimizationTask.Growth.setValues.growth "Permalink to this definition")
            :   A Float specifying the maximum optimization displacement in the growth direction. Either
                **growth** or **shrink** or both must be specified. The default value is 0.0.

            presumeFeasibleRegionAtStart=`1`[¶](#abaqus.Optimization.OptimizationTask.Growth.setValues.presumeFeasibleRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore the geometric restriction in the first design
                cycle. The default value is ON.

            shrink=`0`[¶](#abaqus.Optimization.OptimizationTask.Growth.setValues.shrink "Permalink to this definition")
            :   A Float specifying the maximum optimization displacement in the shrink direction. Either
                **growth** or **shrink** or both must be specified The default value is 0.0.

    shrink : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTask.py#L38-L40)[¶](#abaqus.Optimization.OptimizationTask.Growth.shrink "Permalink to this definition")
    :   A Float specifying the maximum optimization displacement in the shrink direction. Either
        **growth** or **shrink** or both must be specified The default value is 0.0.

*class* LocalStopCondition(*[name](#abaqus.Optimization.LocalStopCondition.LocalStopCondition "abaqus.Optimization.LocalStopCondition.LocalStopCondition.__init__.name (Python parameter)")*, *[referenceFactor](#abaqus.Optimization.LocalStopCondition.LocalStopCondition "abaqus.Optimization.LocalStopCondition.LocalStopCondition.__init__.referenceFactor (Python parameter)")*, *[comparisonOperation](#abaqus.Optimization.LocalStopCondition.LocalStopCondition "abaqus.Optimization.LocalStopCondition.LocalStopCondition.__init__.comparisonOperation (Python parameter)")=`abaqusConstants.LESS_THAN`*, *[identifier](#abaqus.Optimization.LocalStopCondition.LocalStopCondition "abaqus.Optimization.LocalStopCondition.LocalStopCondition.__init__.identifier (Python parameter)")=`abaqusConstants.MOVEMENT`*, *[identifierOperation](#abaqus.Optimization.LocalStopCondition.LocalStopCondition "abaqus.Optimization.LocalStopCondition.LocalStopCondition.__init__.identifierOperation (Python parameter)")=`abaqusConstants.MAXIMUM`*, *[referenceDesignCycle](#abaqus.Optimization.LocalStopCondition.LocalStopCondition "abaqus.Optimization.LocalStopCondition.LocalStopCondition.__init__.referenceDesignCycle (Python parameter)")=`abaqusConstants.PREVIOUS`*, *[referenceOperation](#abaqus.Optimization.LocalStopCondition.LocalStopCondition "abaqus.Optimization.LocalStopCondition.LocalStopCondition.__init__.referenceOperation (Python parameter)")=`abaqusConstants.ADD`*, *[region](#abaqus.Optimization.LocalStopCondition.LocalStopCondition "abaqus.Optimization.LocalStopCondition.LocalStopCondition.__init__.region (Python parameter)")=`abaqusConstants.MODEL`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/LocalStopCondition.py#L20-L220)[¶](#abaqus.Optimization.LocalStopCondition.LocalStopCondition "Permalink to this definition")
:   Bases: [`StopCondition`](#abaqus.Optimization.TopologyTask.StopCondition "abaqus.Optimization.StopCondition.StopCondition (Python class)")

    The LocalStopCondition object defines a local stop condition. The LocalStopCondition object is derived
    from the StopCondition object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].stopConditions[name]
    ```

    Note

    Check [LocalStopCondition on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-localstopconditionpyc.htm?contextscope=all).

    Member Details:

    comparisonOperation : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'LESS_THAN'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/LocalStopCondition.py#L38-L41)[¶](#abaqus.Optimization.LocalStopCondition.LocalStopCondition.comparisonOperation "Permalink to this definition")
    :   A SymbolicConstant specifying the operation used to compare the selected value to the
        reference value. Possible values are LESS\_THAN, LESS\_THAN\_EQUAL, EQUAL,
        GREATER\_THAN\_EQUAL, and GREATER\_THAN. The default value is LESS\_THAN.

    identifier : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MOVEMENT'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/LocalStopCondition.py#L58-L59)[¶](#abaqus.Optimization.LocalStopCondition.LocalStopCondition.identifier "Permalink to this definition")
    :   A SymbolicConstant specifying the variable identifier of the compared value. Possible
        values are:

        * ABSOLUTE\_GROWTH\_MOVEMENT
        * ABSOLUTE\_SHRINK\_MOVEMENT
        * GROWTH\_MOVEMENT
        * SHRINK\_MOVEMENT
        * MOVEMENT
        * TOTAL\_ABSOLUTE\_MOVEMENT
        * EQUIV\_STRESS
        * FREE\_TASK\_REGION\_EQUIV\_STRESS
        * RESTRICTED\_TASK\_REGION\_EQUIV\_STRESS
        * SURFACE\_POINT\_EQUIV\_STRESS
        * TASK\_REGION\_EQUIV\_STRESS

        The default value is MOVEMENT.

    identifierOperation : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MAXIMUM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/LocalStopCondition.py#L61-L63)[¶](#abaqus.Optimization.LocalStopCondition.LocalStopCondition.identifierOperation "Permalink to this definition")
    :   A SymbolicConstant specifying the operation used to evaluate values in the region.
        Possible values are MAXIMUM, MINIMUM, and SUM. The default value is MAXIMUM.

    referenceDesignCycle : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'PREVIOUS'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/LocalStopCondition.py#L65-L67)[¶](#abaqus.Optimization.LocalStopCondition.LocalStopCondition.referenceDesignCycle "Permalink to this definition")
    :   A SymbolicConstant specifying the iteration from which a value is compared to the
        reference value. Possible values are FIRST and PREVIOUS. The default value is PREVIOUS.

    referenceFactor : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/LocalStopCondition.py)[¶](#abaqus.Optimization.LocalStopCondition.LocalStopCondition.referenceFactor "Permalink to this definition")
    :   A Float specifying the factor used to modify the reference value.

    referenceOperation : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'ADD'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/LocalStopCondition.py#L69-L72)[¶](#abaqus.Optimization.LocalStopCondition.LocalStopCondition.referenceOperation "Permalink to this definition")
    :   A SymbolicConstant specifying the operation used to modify the reference value by the
        reference factor. Possible values are ADD, DIVIDE, MULTIPLY, and SUBTRACT. The default
        value is ADD.

    region : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MODEL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/LocalStopCondition.py#L74-L76)[¶](#abaqus.Optimization.LocalStopCondition.LocalStopCondition.region "Permalink to this definition")
    :   The SymbolicConstant MODEL or a Region object specifying the region to which the stop
        condition is applied. The default value is MODEL.

    setValues(*[comparisonOperation](#abaqus.Optimization.LocalStopCondition.LocalStopCondition.setValues.comparisonOperation "abaqus.Optimization.LocalStopCondition.LocalStopCondition.setValues.comparisonOperation (Python parameter) — A SymbolicConstant specifying the operation used to compare the selected value to the reference value.")=`abaqusConstants.LESS_THAN`*, *[identifier](#abaqus.Optimization.LocalStopCondition.LocalStopCondition.setValues.identifier "abaqus.Optimization.LocalStopCondition.LocalStopCondition.setValues.identifier (Python parameter) — A SymbolicConstant specifying the variable identifier of the compared value.")=`abaqusConstants.MOVEMENT`*, *[identifierOperation](#abaqus.Optimization.LocalStopCondition.LocalStopCondition.setValues.identifierOperation "abaqus.Optimization.LocalStopCondition.LocalStopCondition.setValues.identifierOperation (Python parameter) — A SymbolicConstant specifying the operation used to evaluate values in the region. Possible values are MAXIMUM, MINIMUM, and SUM.")=`abaqusConstants.MAXIMUM`*, *[referenceDesignCycle](#abaqus.Optimization.LocalStopCondition.LocalStopCondition.setValues.referenceDesignCycle "abaqus.Optimization.LocalStopCondition.LocalStopCondition.setValues.referenceDesignCycle (Python parameter) — A SymbolicConstant specifying the iteration from which a value is compared to the reference value.")=`abaqusConstants.PREVIOUS`*, *[referenceOperation](#abaqus.Optimization.LocalStopCondition.LocalStopCondition.setValues.referenceOperation "abaqus.Optimization.LocalStopCondition.LocalStopCondition.setValues.referenceOperation (Python parameter) — A SymbolicConstant specifying the operation used to modify the reference value by the reference factor.")=`abaqusConstants.ADD`*, *[region](#abaqus.Optimization.LocalStopCondition.LocalStopCondition.setValues.region "abaqus.Optimization.LocalStopCondition.LocalStopCondition.setValues.region (Python parameter) — The SymbolicConstant MODEL or a Region object specifying the region to which the stop condition is applied.")=`abaqusConstants.MODEL`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/LocalStopCondition.py#L158-L220)[¶](#abaqus.Optimization.LocalStopCondition.LocalStopCondition.setValues "Permalink to this definition")
    :   This method modifies the LocalStopCondition object.

        Note

        Check [LocalStopCondition.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-localstopconditionpyc.htm?contextscope=all#simaker-localstopconditionsetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.LocalStopCondition.LocalStopCondition.setValues-parameters "Permalink to this headline")
        :   comparisonOperation=`abaqusConstants.LESS_THAN`[¶](#abaqus.Optimization.LocalStopCondition.LocalStopCondition.setValues.comparisonOperation "Permalink to this definition")
            :   A SymbolicConstant specifying the operation used to compare the selected value to the
                reference value. Possible values are LESS\_THAN, LESS\_THAN\_EQUAL, EQUAL,
                GREATER\_THAN\_EQUAL, and GREATER\_THAN. The default value is LESS\_THAN.

            identifier=`abaqusConstants.MOVEMENT`[¶](#abaqus.Optimization.LocalStopCondition.LocalStopCondition.setValues.identifier "Permalink to this definition")
            :   A SymbolicConstant specifying the variable identifier of the compared value. Possible
                values are:
                - ABSOLUTE\_GROWTH\_MOVEMENT
                - ABSOLUTE\_SHRINK\_MOVEMENT
                - GROWTH\_MOVEMENT
                - SHRINK\_MOVEMENT
                - MOVEMENT
                - TOTAL\_ABSOLUTE\_MOVEMENT
                - EQUIV\_STRESS
                - FREE\_TASK\_REGION\_EQUIV\_STRESS
                - RESTRICTED\_TASK\_REGION\_EQUIV\_STRESS
                - SURFACE\_POINT\_EQUIV\_STRESS
                - TASK\_REGION\_EQUIV\_STRESS

                The default value is MOVEMENT.

            identifierOperation=`abaqusConstants.MAXIMUM`[¶](#abaqus.Optimization.LocalStopCondition.LocalStopCondition.setValues.identifierOperation "Permalink to this definition")
            :   A SymbolicConstant specifying the operation used to evaluate values in the region.
                Possible values are MAXIMUM, MINIMUM, and SUM. The default value is MAXIMUM.

            referenceDesignCycle=`abaqusConstants.PREVIOUS`[¶](#abaqus.Optimization.LocalStopCondition.LocalStopCondition.setValues.referenceDesignCycle "Permalink to this definition")
            :   A SymbolicConstant specifying the iteration from which a value is compared to the
                reference value. Possible values are FIRST and PREVIOUS. The default value is PREVIOUS.

            referenceOperation=`abaqusConstants.ADD`[¶](#abaqus.Optimization.LocalStopCondition.LocalStopCondition.setValues.referenceOperation "Permalink to this definition")
            :   A SymbolicConstant specifying the operation used to modify the reference value by the
                reference factor. Possible values are ADD, DIVIDE, MULTIPLY, and SUBTRACT. The default
                value is ADD.

            region=`abaqusConstants.MODEL`[¶](#abaqus.Optimization.LocalStopCondition.LocalStopCondition.setValues.region "Permalink to this definition")
            :   The SymbolicConstant MODEL or a Region object specifying the region to which the stop
                condition is applied. The default value is MODEL.

*class* StopCondition[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L8-L26)[¶](#abaqus.Optimization.TopologyTask.StopCondition "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The StopCondition object is the abstract base type for other StopCondition objects. The StopCondition
    object has no explicit constructor. The methods and members of the StopCondition object are common to all
    objects derived from StopCondition.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].stopConditions[name]
    ```

    Note

    Check [StopCondition on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stopconditionpyc.htm?contextscope=all).

    Member Details:

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L21-L22)[¶](#abaqus.Optimization.TopologyTask.StopCondition.name "Permalink to this definition")
    :   A String specifying the stop condition repository key.

    region : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MODEL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L8-L26)[¶](#abaqus.Optimization.TopologyTask.StopCondition.region "Permalink to this definition")
    :   The SymbolicConstant MODEL or a Region object specifying the region to which the stop
        condition is applied. The default value is MODEL.

*class* OptimizationObjective[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationObjectiveArray.py#L10-L36)[¶](#abaqus.Optimization.OptimizationObjectiveArray.OptimizationObjective "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    An OptimizationObjective is an object used to define objectives in an objective function.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].objectiveFunctions[name].objectives[i]
    ```

    Note

    Check [OptimizationObjective on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optimizationobjectivepyc.htm?contextscope=all).

    Member Details:

    designResponse : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationObjectiveArray.py#L10-L36)[¶](#abaqus.Optimization.OptimizationObjectiveArray.OptimizationObjective.designResponse "Permalink to this definition")
    :   A String specifying the name of the design response.

    referenceValue : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`, :py:class:`float`] = `'DEFAULT'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationObjectiveArray.py#L29-L33)[¶](#abaqus.Optimization.OptimizationObjectiveArray.OptimizationObjective.referenceValue "Permalink to this definition")
    :   The SymbolicConstant DEFAULT or a Float specifying the reference value used in
        evaluating a design response. For topology optimization, DEFAULT> indicates the
        reference value is 0. For shape optimization, DEFAULT indicates the reference value is
        the nodal average. The default value is DEFAULT.

    suppress : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationObjectiveArray.py#L21-L23)[¶](#abaqus.Optimization.OptimizationObjectiveArray.OptimizationObjective.suppress "Permalink to this definition")
    :   A Boolean specifying whether the objective is suppressed or not. The default value is
        OFF.

    weight : --is-rst--:py:class:`float` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationObjectiveArray.py#L25-L27)[¶](#abaqus.Optimization.OptimizationObjectiveArray.OptimizationObjective.weight "Permalink to this definition")
    :   A Float specifying the weight applied to the design response value. The default value is
        1.0.

*class* OptimizationTaskBase[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskBase.py#L13-L46)[¶](#abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The OptimizationTask object is the abstract base type for other OptimizationTask objects. The
    OptimizationTask object has no explicit constructor. The methods and members of the OptimizationTask object
    are common to all objects derived from OptimizationTask.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name]
    ```

    Note

    Check [OptimizationTaskBase on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-optimizationtaskpyc.htm?contextscope=all).

    Member Details:

    designResponses : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Optimization.DesignResponse.DesignResponse`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskBase.py#L33-L34)[¶](#abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase.designResponses "Permalink to this definition")
    :   A repository of DesignResponse objects.

    geometricRestrictions : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Optimization.GeometricRestriction.GeometricRestriction`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskBase.py#L42-L43)[¶](#abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase.geometricRestrictions "Permalink to this definition")
    :   A repository of GeometricRestriction objects.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskBase.py#L26-L27)[¶](#abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase.name "Permalink to this definition")
    :   A String specifying the optimization task repository key.

    objectiveFunctions : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Optimization.ObjectiveFunction.ObjectiveFunction`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskBase.py#L36-L37)[¶](#abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase.objectiveFunctions "Permalink to this definition")
    :   A repository of ObjectiveFunction objects.

    optimizationConstraints : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Optimization.OptimizationConstraint.OptimizationConstraint`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskBase.py#L39-L40)[¶](#abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase.optimizationConstraints "Permalink to this definition")
    :   A repository of OptimizationConstraint objects.

    region : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MODEL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskBase.py#L29-L31)[¶](#abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase.region "Permalink to this definition")
    :   The SymbolicConstant MODEL or a Region object specifying the region to which the
        optimization task is applied. The default value is MODEL.

    stopConditions : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Optimization.StopCondition.StopCondition`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/OptimizationTaskBase.py#L13-L46)[¶](#abaqus.Optimization.OptimizationTaskBase.OptimizationTaskBase.stopConditions "Permalink to this definition")
    :   A repository of StopCondition objects.

*class* PenetrationCheck(*[name](#abaqus.Optimization.PenetrationCheck.PenetrationCheck "abaqus.Optimization.PenetrationCheck.PenetrationCheck.__init__.name (Python parameter)")*, *[penetrationCheckRegion](#abaqus.Optimization.PenetrationCheck.PenetrationCheck "abaqus.Optimization.PenetrationCheck.PenetrationCheck.__init__.penetrationCheckRegion (Python parameter)")*, *[region](#abaqus.Optimization.PenetrationCheck.PenetrationCheck "abaqus.Optimization.PenetrationCheck.PenetrationCheck.__init__.region (Python parameter)")*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.PenetrationCheck.PenetrationCheck "abaqus.Optimization.PenetrationCheck.PenetrationCheck.__init__.presumeFeasibleRegionAtStart (Python parameter)")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/PenetrationCheck.py#L10-L83)[¶](#abaqus.Optimization.PenetrationCheck.PenetrationCheck "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The PenetrationCheck object defines a penetration check geometric restriction. The PenetrationCheck
    object is derived from the GeometricRestriction object. This page discusses:

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [PenetrationCheck on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-penetrationcheckpyc.htm?contextscope=all).

    Member Details:

    penetrationCheckRegion : --is-rst--:py:class:`~abaqus.Region.Region.Region`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/PenetrationCheck.py)[¶](#abaqus.Optimization.PenetrationCheck.PenetrationCheck.penetrationCheckRegion "Permalink to this definition")
    :   A Region object specifying the penetration check region.

    presumeFeasibleRegionAtStart : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/PenetrationCheck.py#L33-L35)[¶](#abaqus.Optimization.PenetrationCheck.PenetrationCheck.presumeFeasibleRegionAtStart "Permalink to this definition")
    :   A Boolean specifying whether to ignore the geometric restriction in the first design
        cycle. The default value is ON.

    setValues(*[presumeFeasibleRegionAtStart](#abaqus.Optimization.PenetrationCheck.PenetrationCheck.setValues.presumeFeasibleRegionAtStart "abaqus.Optimization.PenetrationCheck.PenetrationCheck.setValues.presumeFeasibleRegionAtStart (Python parameter) — A Boolean specifying whether to ignore the geometric restriction in the first design cycle.")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/PenetrationCheck.py#L73-L83)[¶](#abaqus.Optimization.PenetrationCheck.PenetrationCheck.setValues "Permalink to this definition")
    :   This method modifies the PenetrationCheck object.

        Note

        Check [PenetrationCheck.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-penetrationcheckpyc.htm?contextscope=all#simaker-penetrationchecksetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.PenetrationCheck.PenetrationCheck.setValues-parameters "Permalink to this headline")
        :   presumeFeasibleRegionAtStart=`1`[¶](#abaqus.Optimization.PenetrationCheck.PenetrationCheck.setValues.presumeFeasibleRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore the geometric restriction in the first design
                cycle. The default value is ON.

*class* ShapeDemoldControl(*[name](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl "abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.__init__.name (Python parameter)")*, *[pullDirection](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl "abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.__init__.pullDirection (Python parameter)")*, *[region](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl "abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.__init__.region (Python parameter)")*, *[collisionCheckRegion](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl "abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.__init__.collisionCheckRegion (Python parameter)")=`abaqusConstants.DEMOLD_REGION`*, *[csys](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl "abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.__init__.csys (Python parameter)")=`None`*, *[drawAngle](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl "abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.__init__.drawAngle (Python parameter)")=`0`*, *[mainPointDetermination](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl "abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.__init__.mainPointDetermination (Python parameter)")=`abaqusConstants.MAXIMUM`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl "abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.__init__.presumeFeasibleRegionAtStart (Python parameter)")=`1`*, *[tolerance1](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl "abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.__init__.tolerance1 (Python parameter)")=`0`*, *[tolerance2](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl "abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.__init__.tolerance2 (Python parameter)")=`0`*, *[tolerance3](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl "abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.__init__.tolerance3 (Python parameter)")=`0`*, *[undercutTolerance](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl "abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.__init__.undercutTolerance (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeDemoldControl.py#L19-L205)[¶](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The ShapeDemoldControl object defines a shape demold control geometric restriction. The
    ShapeDemoldControl object is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [ShapeDemoldControl on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapedemoldcontrolpyc.htm?contextscope=all).

    Member Details:

    collisionCheckRegion : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'DEMOLD_REGION'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeDemoldControl.py#L43-L46)[¶](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.collisionCheckRegion "Permalink to this definition")
    :   The SymbolicConstant DEMOLD\_REGION or a Region object specifying the collision check
        region. If the value is DEMOLD\_REGION, then the value of **region** is used as both the
        demold region and the collision check region. The default value is DEMOLD\_REGION.

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeDemoldControl.py#L48-L52)[¶](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the
        **pullDirection**. If **csys** = None, the global coordinate system is used. When this member
        is queried, it returns an Int indicating the identifier of the DatumCsys. The default
        value is None.

    drawAngle : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeDemoldControl.py#L54-L55)[¶](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.drawAngle "Permalink to this definition")
    :   A Float specifying the draw angle. The default value is 0.0.

    mainPointDetermination : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MAXIMUM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeDemoldControl.py#L60-L62)[¶](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.mainPointDetermination "Permalink to this definition")
    :   A SymbolicConstant specifying the rule for assigning point priority. Possible values are
        MAXIMUM and MINIMUM. The default value is MAXIMUM.

        Changed in version 2022: The attribute `masterPointDetermination` was renamed to `mainPointDetermination`.

    presumeFeasibleRegionAtStart : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeDemoldControl.py#L64-L66)[¶](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.presumeFeasibleRegionAtStart "Permalink to this definition")
    :   A Boolean specifying whether to ignore the geometric restriction in the first design
        cycle. The default value is ON.

    pullDirection : --is-rst--:py:class:`tuple`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeDemoldControl.py)[¶](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.pullDirection "Permalink to this definition")
    :   A VertexArray object of length 2 specifying the demold pull direction. Instead of
        through a ConstrainedSketchVertex, each point might be specified through a tuple of coordinates.

    setValues(*[collisionCheckRegion](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.collisionCheckRegion "abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.collisionCheckRegion (Python parameter) — The SymbolicConstant DEMOLD_REGION or a Region object specifying the collision check region.")=`abaqusConstants.DEMOLD_REGION`*, *[csys](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.csys "abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the pullDirection.")=`None`*, *[drawAngle](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.drawAngle "abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.drawAngle (Python parameter) — A Float specifying the draw angle.")=`0`*, *[mainPointDetermination](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.mainPointDetermination "abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.mainPointDetermination (Python parameter) — A SymbolicConstant specifying the rule for assigning point priority.")=`abaqusConstants.MAXIMUM`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.presumeFeasibleRegionAtStart "abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.presumeFeasibleRegionAtStart (Python parameter) — A Boolean specifying whether to ignore the geometric restriction in the first design cycle.")=`1`*, *[tolerance1](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.tolerance1 "abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.tolerance1 (Python parameter) — A Float specifying the geometric tolerance in the 1-direction.")=`0`*, *[tolerance2](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.tolerance2 "abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.tolerance2 (Python parameter) — A Float specifying the geometric tolerance in the 2-direction.")=`0`*, *[tolerance3](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.tolerance3 "abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.tolerance3 (Python parameter) — A Float specifying the geometric tolerance in the 3-direction.")=`0`*, *[undercutTolerance](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.undercutTolerance "abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.undercutTolerance (Python parameter) — A Float specifying the undercut tolerance.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeDemoldControl.py#L156-L205)[¶](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues "Permalink to this definition")
    :   This method modifies the ShapeDemoldControl object.

        Note

        Check [ShapeDemoldControl.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapedemoldcontrolpyc.htm?contextscope=all#simaker-shapedemoldcontrolsetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues-parameters "Permalink to this headline")
        :   collisionCheckRegion=`abaqusConstants.DEMOLD_REGION`[¶](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.collisionCheckRegion "Permalink to this definition")
            :   The SymbolicConstant DEMOLD\_REGION or a Region object specifying the collision check
                region. If the value is DEMOLD\_REGION, then the value of **region** is used as both the
                demold region and the collision check region. The default value is DEMOLD\_REGION.

            csys=`None`[¶](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the
                **pullDirection**. If **csys** = None, the global coordinate system is used. When this member
                is queried, it returns an Int indicating the identifier of the DatumCsys. The default
                value is None.

            drawAngle=`0`[¶](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.drawAngle "Permalink to this definition")
            :   A Float specifying the draw angle. The default value is 0.0.

            mainPointDetermination=`abaqusConstants.MAXIMUM`[¶](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.mainPointDetermination "Permalink to this definition")
            :   A SymbolicConstant specifying the rule for assigning point priority. Possible values are
                MAXIMUM and MINIMUM. The default value is MAXIMUM.

                Changed in version 2022: The argument `masterPointDetermination` was renamed to `mainPointDetermination`.

            presumeFeasibleRegionAtStart=`1`[¶](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.presumeFeasibleRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore the geometric restriction in the first design
                cycle. The default value is ON.

            tolerance1=`0`[¶](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.tolerance1 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 1-direction. The default value is
                0.01.

            tolerance2=`0`[¶](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.tolerance2 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 2-direction. The default value is
                0.01.

            tolerance3=`0`[¶](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.tolerance3 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 3-direction. The default value is
                0.01.

            undercutTolerance=`0`[¶](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.setValues.undercutTolerance "Permalink to this definition")
            :   A Float specifying the undercut tolerance. The default value is 0.0.

    tolerance1 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeDemoldControl.py#L68-L70)[¶](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.tolerance1 "Permalink to this definition")
    :   A Float specifying the geometric tolerance in the 1-direction. The default value is
        0.01.

    tolerance2 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeDemoldControl.py#L72-L74)[¶](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.tolerance2 "Permalink to this definition")
    :   A Float specifying the geometric tolerance in the 2-direction. The default value is
        0.01.

    tolerance3 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeDemoldControl.py#L76-L78)[¶](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.tolerance3 "Permalink to this definition")
    :   A Float specifying the geometric tolerance in the 3-direction. The default value is
        0.01.

    undercutTolerance : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeDemoldControl.py#L80-L81)[¶](#abaqus.Optimization.ShapeDemoldControl.ShapeDemoldControl.undercutTolerance "Permalink to this definition")
    :   A Float specifying the undercut tolerance. The default value is 0.0.

*class* ShapeMemberSize(*[name](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize "abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.__init__.name (Python parameter)")*, *[region](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize "abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.__init__.region (Python parameter)")*, *[maxThickness](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize "abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.__init__.maxThickness (Python parameter)")=`0`*, *[minThickness](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize "abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.__init__.minThickness (Python parameter)")=`0`*, *[sizeRestriction](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize "abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.__init__.sizeRestriction (Python parameter)")=`abaqusConstants.MINIMUM`*, *[assignNodeGroupRegion](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize "abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.__init__.assignNodeGroupRegion (Python parameter)")=`0`*, *[nodeGroupRegion](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize "abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.__init__.nodeGroupRegion (Python parameter)")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeMemberSize.py#L13-L137)[¶](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The ShapeMemberSize object defines a shape member size geometric restriction. The ShapeMemberSize object
    is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [ShapeMemberSize on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapemembersizepyc.htm?contextscope=all).

    Member Details:

    assignNodeGroupRegion : --is-rst--:py:class:`str` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeMemberSize.py#L45-L47)[¶](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.assignNodeGroupRegion "Permalink to this definition")
    :   A bool specifying whether to use the node group region. The default value is OFF.

        New in version 2022: The `assignNodeGroupRegion` attribute was added.

    maxThickness : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeMemberSize.py#L33-L34)[¶](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.maxThickness "Permalink to this definition")
    :   A Float specifying the maximum thickness. The default value is 0.0.

    minThickness : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeMemberSize.py#L36-L37)[¶](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.minThickness "Permalink to this definition")
    :   A Float specifying the minimum thickness. The default value is 0.0.

    nodeGroupRegion : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeMemberSize.py#L45-L47)[¶](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.nodeGroupRegion "Permalink to this definition")
    :   A Node Region object specifying the check node group.

        New in version 2022: The `nodeGroupRegion` attribute was added.

    setValues(*[maxThickness](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.setValues.maxThickness "abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.setValues.maxThickness (Python parameter) — A Float specifying the maximum thickness.")=`0`*, *[minThickness](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.setValues.minThickness "abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.setValues.minThickness (Python parameter) — A Float specifying the minimum thickness.")=`0`*, *[sizeRestriction](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.setValues.sizeRestriction "abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.setValues.sizeRestriction (Python parameter) — A SymbolicConstant specifying whether to restrict the minimum or maximum thickness. Possible values are MAXIMUM and MINIMUM.")=`abaqusConstants.MINIMUM`*, *[assignNodeGroupRegion](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.setValues.assignNodeGroupRegion "abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.setValues.assignNodeGroupRegion (Python parameter) — A bool specifying whether to use the node group region.")=`0`*, *[nodeGroupRegion](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.setValues.nodeGroupRegion "abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.setValues.nodeGroupRegion (Python parameter) — A Node Region object specifying the check node group.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeMemberSize.py#L106-L137)[¶](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.setValues "Permalink to this definition")
    :   This method modifies the ShapeMemberSize object.

        Note

        Check [ShapeMemberSize.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapemembersizepyc.htm?contextscope=all#simaker-shapemembersizesetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.setValues-parameters "Permalink to this headline")
        :   maxThickness=`0`[¶](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.setValues.maxThickness "Permalink to this definition")
            :   A Float specifying the maximum thickness. The default value is 0.0.

            minThickness=`0`[¶](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.setValues.minThickness "Permalink to this definition")
            :   A Float specifying the minimum thickness. The default value is 0.0.

            sizeRestriction=`abaqusConstants.MINIMUM`[¶](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.setValues.sizeRestriction "Permalink to this definition")
            :   A SymbolicConstant specifying whether to restrict the minimum or maximum thickness.
                Possible values are MAXIMUM and MINIMUM. The default value is MINIMUM.

            assignNodeGroupRegion=`0`[¶](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.setValues.assignNodeGroupRegion "Permalink to this definition")
            :   A bool specifying whether to use the node group region. The default value is OFF.

                New in version 2022: The `assignNodeGroupRegion` argument was added.

            nodeGroupRegion=`''`[¶](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.setValues.nodeGroupRegion "Permalink to this definition")
            :   A Node Region object specifying the check node group.

                New in version 2022: The `nodeGroupRegion` argument was added.

    sizeRestriction : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MINIMUM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeMemberSize.py#L39-L41)[¶](#abaqus.Optimization.ShapeMemberSize.ShapeMemberSize.sizeRestriction "Permalink to this definition")
    :   A SymbolicConstant specifying whether to restrict the minimum or maximum thickness.
        Possible values are MAXIMUM and MINIMUM. The default value is MINIMUM.

*class* ShapePlanarSymmetry(*[name](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry "abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.__init__.name (Python parameter)")*, *[clientDirection](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry "abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.__init__.clientDirection (Python parameter)")*, *[region](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry "abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.__init__.region (Python parameter)")*, *[allowNonSymmetricMesh](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry "abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.__init__.allowNonSymmetricMesh (Python parameter)")=`True`*, *[csys](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry "abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.__init__.csys (Python parameter)")=`None`*, *[mainPointDetermination](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry "abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.__init__.mainPointDetermination (Python parameter)")=`abaqusConstants.MAXIMUM`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry "abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.__init__.presumeFeasibleRegionAtStart (Python parameter)")=`1`*, *[tolerance1](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry "abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.__init__.tolerance1 (Python parameter)")=`0`*, *[tolerance2](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry "abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.__init__.tolerance2 (Python parameter)")=`0`*, *[tolerance3](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry "abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.__init__.tolerance3 (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapePlanarSymmetry.py#L19-L180)[¶](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The ShapePlanarSymmetry object defines a shape planar symmetry geometric restriction. The
    ShapePlanarSymmetry object is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [ShapePlanarSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapeplanarsymmetrypyc.htm?contextscope=all).

    Member Details:

    allowNonSymmetricMesh : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `True`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapePlanarSymmetry.py#L52-L54)[¶](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.allowNonSymmetricMesh "Permalink to this definition")
    :   A Boolean specifying whether to allow a nonsymmetric mesh for this geometric
        restriction. The default value is TRUE.

        New in version 2021: The `allowNonSymmetricMesh` attribute was added.

    clientDirection : --is-rst--:py:class:`tuple`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapePlanarSymmetry.py)[¶](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.clientDirection "Permalink to this definition")
    :   A VertexArray object of length 2 specifying the vector positioned at the **csys** origin
        that is normal to the symmetry plane. Instead of through a ConstrainedSketchVertex, each point may be
        specified through a tuple of coordinates.

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapePlanarSymmetry.py#L44-L47)[¶](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
        global coordinate system is used. When this member is queried, it returns an Int. The
        default value is None.

    mainPointDetermination : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MAXIMUM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapePlanarSymmetry.py#L56-L58)[¶](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.mainPointDetermination "Permalink to this definition")
    :   A SymbolicConstant specifying the rule for determining the main node. Possible values
        are MAXIMUM and MINIMUM. The default value is MAXIMUM.

    presumeFeasibleRegionAtStart : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapePlanarSymmetry.py#L60-L62)[¶](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.presumeFeasibleRegionAtStart "Permalink to this definition")
    :   A Boolean specifying whether to ignore the geometric restriction in the first design
        cycle. The default value is ON.

    setValues(*[allowNonSymmetricMesh](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.setValues.allowNonSymmetricMesh "abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.setValues.allowNonSymmetricMesh (Python parameter) — A Boolean specifying whether to allow a nonsymmetric mesh for this geometric restriction.")=`True`*, *[csys](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.setValues.csys "abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.setValues.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[mainPointDetermination](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.setValues.mainPointDetermination "abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.setValues.mainPointDetermination (Python parameter) — A SymbolicConstant specifying the rule for determining the main node.")=`abaqusConstants.MAXIMUM`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.setValues.presumeFeasibleRegionAtStart "abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.setValues.presumeFeasibleRegionAtStart (Python parameter) — A Boolean specifying whether to ignore the geometric restriction in the first design cycle.")=`1`*, *[tolerance1](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.setValues.tolerance1 "abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.setValues.tolerance1 (Python parameter) — A Float specifying the geometric tolerance in the 1-direction.")=`0`*, *[tolerance2](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.setValues.tolerance2 "abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.setValues.tolerance2 (Python parameter) — A Float specifying the geometric tolerance in the 2-direction.")=`0`*, *[tolerance3](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.setValues.tolerance3 "abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.setValues.tolerance3 (Python parameter) — A Float specifying the geometric tolerance in the 3-direction.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapePlanarSymmetry.py#L142-L180)[¶](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.setValues "Permalink to this definition")
    :   This method modifies the ShapePlanarSymmetry object.

        Note

        Check [ShapePlanarSymmetry.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapeplanarsymmetrypyc.htm?contextscope=all#simaker-shapeplanarsymmetrysetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.setValues-parameters "Permalink to this headline")
        :   allowNonSymmetricMesh=`True`[¶](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.setValues.allowNonSymmetricMesh "Permalink to this definition")
            :   A Boolean specifying whether to allow a nonsymmetric mesh for this geometric
                restriction. The default value is TRUE.

            csys=`None`[¶](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            mainPointDetermination=`abaqusConstants.MAXIMUM`[¶](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.setValues.mainPointDetermination "Permalink to this definition")
            :   A SymbolicConstant specifying the rule for determining the main node. Possible values
                are MAXIMUM and MINIMUM. The default value is MAXIMUM.

            presumeFeasibleRegionAtStart=`1`[¶](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.setValues.presumeFeasibleRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore the geometric restriction in the first design
                cycle. The default value is ON.

            tolerance1=`0`[¶](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.setValues.tolerance1 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 1-direction. The default value is
                0.01.

            tolerance2=`0`[¶](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.setValues.tolerance2 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 2-direction. The default value is
                0.01.

            tolerance3=`0`[¶](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.setValues.tolerance3 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 3-direction. The default value is
                0.01.

    tolerance1 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapePlanarSymmetry.py#L64-L66)[¶](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.tolerance1 "Permalink to this definition")
    :   A Float specifying the geometric tolerance in the 1-direction. The default value is
        0.01.

    tolerance2 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapePlanarSymmetry.py#L68-L70)[¶](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.tolerance2 "Permalink to this definition")
    :   A Float specifying the geometric tolerance in the 2-direction. The default value is
        0.01.

    tolerance3 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapePlanarSymmetry.py#L72-L74)[¶](#abaqus.Optimization.ShapePlanarSymmetry.ShapePlanarSymmetry.tolerance3 "Permalink to this definition")
    :   A Float specifying the geometric tolerance in the 3-direction. The default value is
        0.01.

*class* ShapePointSymmetry(*[name](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry "abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.__init__.name (Python parameter)")*, *[region](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry "abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.__init__.region (Python parameter)")*, *[csys](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry "abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.__init__.csys (Python parameter)")=`None`*, *[mainPointDetermination](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry "abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.__init__.mainPointDetermination (Python parameter)")=`abaqusConstants.MAXIMUM`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry "abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.__init__.presumeFeasibleRegionAtStart (Python parameter)")=`1`*, *[tolerance1](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry "abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.__init__.tolerance1 (Python parameter)")=`0`*, *[tolerance2](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry "abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.__init__.tolerance2 (Python parameter)")=`0`*, *[tolerance3](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry "abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.__init__.tolerance3 (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapePointSymmetry.py#L13-L155)[¶](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The ShapePointSymmetry object defines a shape point symmetry geometric restriction. The
    ShapePointSymmetry object is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [ShapePointSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapepointsymmetrypyc.htm?contextscope=all).

    Member Details:

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapePointSymmetry.py#L33-L36)[¶](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the symmetry point represented as the origin of a
        local coordinate system. If **csys** = None, the global coordinate system is used. When this
        member is queried, it returns an Int. The default value is None.

    mainPointDetermination : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MAXIMUM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapePointSymmetry.py#L41-L43)[¶](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.mainPointDetermination "Permalink to this definition")
    :   A SymbolicConstant specifying the rule for determining the main node. Possible values
        are MAXIMUM and MINIMUM. The default value is MAXIMUM.

        Changed in version 2022: The attribute `masterPointDetermination` was renamed to `mainPointDetermination`.

    presumeFeasibleRegionAtStart : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapePointSymmetry.py#L45-L47)[¶](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.presumeFeasibleRegionAtStart "Permalink to this definition")
    :   A Boolean specifying whether to ignore the geometric restriction in the first design
        cycle. The default value is ON.

    setValues(*[csys](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.setValues.csys "abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.setValues.csys (Python parameter) — None or a DatumCsys object specifying the symmetry point represented as the origin of a local coordinate system.")=`None`*, *[mainPointDetermination](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.setValues.mainPointDetermination "abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.setValues.mainPointDetermination (Python parameter) — A SymbolicConstant specifying the rule for determining the main node.")=`abaqusConstants.MAXIMUM`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.setValues.presumeFeasibleRegionAtStart "abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.setValues.presumeFeasibleRegionAtStart (Python parameter) — A Boolean specifying whether to ignore the geometric restriction in the first design cycle.")=`1`*, *[tolerance1](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.setValues.tolerance1 "abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.setValues.tolerance1 (Python parameter) — A Float specifying the geometric tolerance in the 1-direction.")=`0`*, *[tolerance2](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.setValues.tolerance2 "abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.setValues.tolerance2 (Python parameter) — A Float specifying the geometric tolerance in the 2-direction.")=`0`*, *[tolerance3](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.setValues.tolerance3 "abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.setValues.tolerance3 (Python parameter) — A Float specifying the geometric tolerance in the 3-direction.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapePointSymmetry.py#L118-L155)[¶](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.setValues "Permalink to this definition")
    :   This method modifies the ShapePointSymmetry object.

        Note

        Check [ShapePointSymmetry.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapepointsymmetrypyc.htm?contextscope=all#simaker-shapepointsymmetrysetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.setValues-parameters "Permalink to this headline")
        :   csys=`None`[¶](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the symmetry point represented as the origin of a
                local coordinate system. If **csys** = None, the global coordinate system is used. When this
                member is queried, it returns an Int. The default value is None.

            mainPointDetermination=`abaqusConstants.MAXIMUM`[¶](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.setValues.mainPointDetermination "Permalink to this definition")
            :   A SymbolicConstant specifying the rule for determining the main node. Possible values
                are MAXIMUM and MINIMUM. The default value is MAXIMUM.

                Changed in version 2022: The argument `masterPointDetermination` was renamed to `mainPointDetermination`.

            presumeFeasibleRegionAtStart=`1`[¶](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.setValues.presumeFeasibleRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore the geometric restriction in the first design
                cycle. The default value is ON.

            tolerance1=`0`[¶](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.setValues.tolerance1 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 1-direction. The default value is
                0.01.

            tolerance2=`0`[¶](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.setValues.tolerance2 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 2-direction. The default value is
                0.01.

            tolerance3=`0`[¶](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.setValues.tolerance3 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 3-direction. The default value is
                0.01.

    tolerance1 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapePointSymmetry.py#L49-L51)[¶](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.tolerance1 "Permalink to this definition")
    :   A Float specifying the geometric tolerance in the 1-direction. The default value is
        0.01.

    tolerance2 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapePointSymmetry.py#L53-L55)[¶](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.tolerance2 "Permalink to this definition")
    :   A Float specifying the geometric tolerance in the 2-direction. The default value is
        0.01.

    tolerance3 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapePointSymmetry.py#L57-L59)[¶](#abaqus.Optimization.ShapePointSymmetry.ShapePointSymmetry.tolerance3 "Permalink to this definition")
    :   A Float specifying the geometric tolerance in the 3-direction. The default value is
        0.01.

*class* ShapeRotationalSymmetry(*[name](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry "abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.__init__.name (Python parameter)")*, *[clientDirection](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry "abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.__init__.clientDirection (Python parameter)")*, *[region](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry "abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.__init__.region (Python parameter)")*, *[allowNonSymmetricMesh](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry "abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.__init__.allowNonSymmetricMesh (Python parameter)")=`True`*, *[angle](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry "abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.__init__.angle (Python parameter)")=`0`*, *[csys](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry "abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.__init__.csys (Python parameter)")=`None`*, *[mainPoint](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry "abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.__init__.mainPoint (Python parameter)")=`None`*, *[mainPointDetermination](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry "abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.__init__.mainPointDetermination (Python parameter)")=`abaqusConstants.MAXIMUM`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry "abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.__init__.presumeFeasibleRegionAtStart (Python parameter)")=`1`*, *[startPoint](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry "abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.__init__.startPoint (Python parameter)")=`None`*, *[tolerance1](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry "abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.__init__.tolerance1 (Python parameter)")=`0`*, *[tolerance2](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry "abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.__init__.tolerance2 (Python parameter)")=`0`*, *[tolerance3](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry "abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.__init__.tolerance3 (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeRotationalSymmetry.py#L19-L234)[¶](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The ShapeRotationalSymmetry object defines a shape rotational symmetry geometric restriction. The
    ShapeRotationalSymmetry object is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [ShapeRotationalSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shaperotationalsymmetrypyc.htm?contextscope=all).

    Member Details:

    allowNonSymmetricMesh : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `True`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeRotationalSymmetry.py#L56-L58)[¶](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.allowNonSymmetricMesh "Permalink to this definition")
    :   A Boolean specifying whether to allow a nonsymmetric mesh for this geometric
        restriction. The default value is TRUE.

        New in version 2021: The `allowNonSymmetricMesh` attribute was added.

    angle : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeRotationalSymmetry.py#L44-L46)[¶](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.angle "Permalink to this definition")
    :   A Float specifying the segment size of the repeating pattern in degrees. If the **angle**
        value is 0, no repeating pattern is created. The default value is 0.0.

    clientDirection : --is-rst--:py:class:`tuple`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeRotationalSymmetry.py)[¶](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.clientDirection "Permalink to this definition")
    :   A VertexArray object of length 2 specifying the vector positioned at the **csys** origin,
        used as the axis of symmetry. Instead of through a ConstrainedSketchVertex, each point might be specified
        through a tuple of coordinates.

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeRotationalSymmetry.py#L48-L51)[¶](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
        global coordinate system is used. When this member is queried, it returns an Int. The
        default value is None.

    mainPoint : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeRotationalSymmetry.py#L63-L65)[¶](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.mainPoint "Permalink to this definition")
    :   None or a Region object specifying the main point used when **mainPointDetermination** is
        SPECIFY. The default value is None.

        Changed in version 2022: The attribute `masterPoint` was renamed to `mainPoint`.

    mainPointDetermination : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MAXIMUM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeRotationalSymmetry.py#L63-L65)[¶](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.mainPointDetermination "Permalink to this definition")
    :   A SymbolicConstant specifying the rule for determining the main node. Possible values
        are MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.

        Changed in version 2022: The attribute `masterPointDetermination` was renamed to `mainPointDetermination`.

    presumeFeasibleRegionAtStart : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeRotationalSymmetry.py#L74-L76)[¶](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.presumeFeasibleRegionAtStart "Permalink to this definition")
    :   A Boolean specifying whether to ignore the geometric restriction in the first design
        cycle. The default value is ON.

    setValues(*[allowNonSymmetricMesh](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.allowNonSymmetricMesh "abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.allowNonSymmetricMesh (Python parameter) — A Boolean specifying whether to allow a nonsymmetric mesh for this geometric restriction.")=`True`*, *[angle](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.angle "abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.angle (Python parameter) — A Float specifying the segment size of the repeating pattern in degrees.")=`0`*, *[csys](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.csys "abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[mainPoint](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.mainPoint "abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.mainPoint (Python parameter) — None or a Region object specifying the main point used when mainPointDetermination is SPECIFY.")=`None`*, *[mainPointDetermination](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.mainPointDetermination "abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.mainPointDetermination (Python parameter) — A SymbolicConstant specifying the rule for determining the main node.")=`abaqusConstants.MAXIMUM`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.presumeFeasibleRegionAtStart "abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.presumeFeasibleRegionAtStart (Python parameter) — A Boolean specifying whether to ignore the geometric restriction in the first design cycle.")=`1`*, *[startPoint](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.startPoint "abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.startPoint (Python parameter) — A tuple of Floats representing the coordinates of a start point of the rotational symmetry.")=`None`*, *[tolerance1](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.tolerance1 "abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.tolerance1 (Python parameter) — A Float specifying the geometric tolerance in the 1-direction.")=`0`*, *[tolerance2](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.tolerance2 "abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.tolerance2 (Python parameter) — A Float specifying the geometric tolerance in the 2-direction.")=`0`*, *[tolerance3](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.tolerance3 "abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.tolerance3 (Python parameter) — A Float specifying the geometric tolerance in the 3-direction.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeRotationalSymmetry.py#L178-L234)[¶](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues "Permalink to this definition")
    :   This method modifies the ShapeRotationalSymmetry object.

        Note

        Check [ShapeRotationalSymmetry.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shaperotationalsymmetrypyc.htm?contextscope=all#simaker-shaperotationalsymmetrysetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues-parameters "Permalink to this headline")
        :   allowNonSymmetricMesh=`True`[¶](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.allowNonSymmetricMesh "Permalink to this definition")
            :   A Boolean specifying whether to allow a nonsymmetric mesh for this geometric
                restriction. The default value is TRUE.

            angle=`0`[¶](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.angle "Permalink to this definition")
            :   A Float specifying the segment size of the repeating pattern in degrees. If the **angle**
                value is 0, no repeating pattern is created. The default value is 0.0.

            csys=`None`[¶](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            mainPoint=`None`[¶](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.mainPoint "Permalink to this definition")
            :   None or a Region object specifying the main point used when **mainPointDetermination** is
                SPECIFY. The default value is None.

                Changed in version 2022: The argument `masterPoint` was renamed to `mainPoint`.

            mainPointDetermination=`abaqusConstants.MAXIMUM`[¶](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.mainPointDetermination "Permalink to this definition")
            :   A SymbolicConstant specifying the rule for determining the main node. Possible values
                are MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.

                Changed in version 2022: The argument `masterPointDetermination` was renamed to `mainPointDetermination`.

            presumeFeasibleRegionAtStart=`1`[¶](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.presumeFeasibleRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore the geometric restriction in the first design
                cycle. The default value is ON.

            startPoint=`None`[¶](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.startPoint "Permalink to this definition")
            :   A tuple of Floats representing the coordinates of a start point of the rotational
                symmetry.

            tolerance1=`0`[¶](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.tolerance1 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 1-direction. The default value is
                0.01.

            tolerance2=`0`[¶](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.tolerance2 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 2-direction. The default value is
                0.01.

            tolerance3=`0`[¶](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.setValues.tolerance3 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 3-direction. The default value is
                0.01.

    startPoint : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeRotationalSymmetry.py#L78-L80)[¶](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.startPoint "Permalink to this definition")
    :   A tuple of Floats representing the coordinates of a start point of the rotational
        symmetry.

    tolerance1 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeRotationalSymmetry.py#L82-L84)[¶](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.tolerance1 "Permalink to this definition")
    :   A Float specifying the geometric tolerance in the 1-direction. The default value is
        0.01.

    tolerance2 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeRotationalSymmetry.py#L86-L88)[¶](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.tolerance2 "Permalink to this definition")
    :   A Float specifying the geometric tolerance in the 2-direction. The default value is
        0.01.

    tolerance3 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeRotationalSymmetry.py#L90-L92)[¶](#abaqus.Optimization.ShapeRotationalSymmetry.ShapeRotationalSymmetry.tolerance3 "Permalink to this definition")
    :   A Float specifying the geometric tolerance in the 3-direction. The default value is
        0.01.

*class* SingleTermDesignResponse(*[name](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse "abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.__init__.name (Python parameter)")*, *[identifier](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse "abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.__init__.identifier (Python parameter)")*, *[csys](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse "abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.__init__.csys (Python parameter)")=`None`*, *[drivingRegion](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse "abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.__init__.drivingRegion (Python parameter)")=`None`*, *[operation](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse "abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.__init__.operation (Python parameter)")=`abaqusConstants.SUM`*, *[region](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse "abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.__init__.region (Python parameter)")=`abaqusConstants.MODEL`*, *[shellLayer](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse "abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.__init__.shellLayer (Python parameter)")=`abaqusConstants.MAXIMUM`*, *[stepOptions](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse "abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.__init__.stepOptions (Python parameter)")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SingleTermDesignResponse.py#L13-L147)[¶](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse "Permalink to this definition")
:   Bases: [`DesignResponse`](#abaqus.Optimization.TopologyTask.DesignResponse "abaqus.Optimization.DesignResponse.DesignResponse (Python class)")

    The SingleTermDesignResponse object defines a single-term design response. The SingleTermDesignResponse
    object is derived from the DesignResponse object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].designResponses[name]
    ```

    Changed in version 2024: The attribute stepOperation was removed.

    Note

    Check [SingleTermDesignResponse on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-singletermdesignresponsepyc.htm?contextscope=all).

    Member Details:

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SingleTermDesignResponse.py#L35-L38)[¶](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
        global coordinate system is used. When this member is queried, it returns an Int. The
        default value is None.

    drivingRegion : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SingleTermDesignResponse.py#L40-L42)[¶](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.drivingRegion "Permalink to this definition")
    :   None or a sequence of Floats specifying the driving region used when **identifier** is an
        internal nodal variable. The default value is None.

    identifier : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SingleTermDesignResponse.py)[¶](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.identifier "Permalink to this definition")
    :   A String specifying the name of the variable identifier.

    operation : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'SUM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SingleTermDesignResponse.py#L44-L46)[¶](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.operation "Permalink to this definition")
    :   A SymbolicConstant specifying the operation used on values in the region. Possible
        values are MAXIMUM, MINIMUM, and SUM. The default value is SUM.

    region : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MODEL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SingleTermDesignResponse.py#L48-L50)[¶](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.region "Permalink to this definition")
    :   The SymbolicConstant MODEL or a Region object specifying the region of the design
        response variable. The default value is MODEL.

    setValues(*[csys](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.setValues.csys "abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.setValues.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[drivingRegion](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.setValues.drivingRegion "abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.setValues.drivingRegion (Python parameter) — None or a sequence of Floats specifying the driving region used when identifier is an internal nodal variable.")=`None`*, *[operation](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.setValues.operation "abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.setValues.operation (Python parameter) — A SymbolicConstant specifying the operation used on values in the region.")=`abaqusConstants.SUM`*, *[region](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.setValues.region "abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.setValues.region (Python parameter) — The SymbolicConstant MODEL or a Region object specifying the region of the design response variable.")=`abaqusConstants.MODEL`*, *[shellLayer](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.setValues.shellLayer "abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.setValues.shellLayer (Python parameter) — A SymbolicConstant specifying the location used for shell layer values.")=`abaqusConstants.MAXIMUM`*, *[stepOptions](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.setValues.stepOptions "abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.setValues.stepOptions (Python parameter) — A StepOptionArray object.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SingleTermDesignResponse.py#L114-L147)[¶](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.setValues "Permalink to this definition")
    :   This method modifies the SingleTermDesignResponse object.

        Note

        Check [SingleTermDesignResponse.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-singletermdesignresponsepyc.htm?contextscope=all#simaker-singletermdesignresponsesetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.setValues-parameters "Permalink to this headline")
        :   csys=`None`[¶](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            drivingRegion=`None`[¶](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.setValues.drivingRegion "Permalink to this definition")
            :   None or a sequence of Floats specifying the driving region used when **identifier** is an
                internal nodal variable. The default value is None.

            operation=`abaqusConstants.SUM`[¶](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.setValues.operation "Permalink to this definition")
            :   A SymbolicConstant specifying the operation used on values in the region. Possible
                values are MAXIMUM, MINIMUM, and SUM. The default value is SUM.

            region=`abaqusConstants.MODEL`[¶](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.setValues.region "Permalink to this definition")
            :   The SymbolicConstant MODEL or a Region object specifying the region of the design
                response variable. The default value is MODEL.

            shellLayer=`abaqusConstants.MAXIMUM`[¶](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.setValues.shellLayer "Permalink to this definition")
            :   A SymbolicConstant specifying the location used for shell layer values. Possible values
                are BOTTOM, MAXIMUM, MIDDLE, MINIMUM, and TOP. The default value is MAXIMUM.

            stepOptions=`None`[¶](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.setValues.stepOptions "Permalink to this definition")
            :   A StepOptionArray object.

    shellLayer : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MAXIMUM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SingleTermDesignResponse.py#L52-L54)[¶](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.shellLayer "Permalink to this definition")
    :   A SymbolicConstant specifying the location used for shell layer values. Possible values
        are BOTTOM, MAXIMUM, MIDDLE, MINIMUM, and TOP. The default value is MAXIMUM.

    stepOptions : --is-rst--:py:data:`~typing.Optional`\[:py:class:`~typing.List`\[:py:class:`~abaqus.Optimization.StepOption.StepOption`]] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SingleTermDesignResponse.py#L56-L57)[¶](#abaqus.Optimization.SingleTermDesignResponse.SingleTermDesignResponse.stepOptions "Permalink to this definition")
    :   A StepOptionArray object.

*class* SizingClusterAreas(*[name](#abaqus.Optimization.SizingClusterAreas.SizingClusterAreas "abaqus.Optimization.SizingClusterAreas.SizingClusterAreas.__init__.name (Python parameter)")*, *[regions](#abaqus.Optimization.SizingClusterAreas.SizingClusterAreas "abaqus.Optimization.SizingClusterAreas.SizingClusterAreas.__init__.regions (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingClusterAreas.py#L8-L54)[¶](#abaqus.Optimization.SizingClusterAreas.SizingClusterAreas "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The SizingClusterAreas object defines a sizing cluster areas geometric restriction. The
    SizingClusterAreas object is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [SizingClusterAreas on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingclusterareaspyc.htm?contextscope=all).

    Member Details:

    regions : --is-rst--tuple[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingClusterAreas.py)[¶](#abaqus.Optimization.SizingClusterAreas.SizingClusterAreas.regions "Permalink to this definition")
    :   tuple of Region objects specifying the regions to which the geometric restriction is
        applied.

    setValues(*\*[args](#abaqus.Optimization.SizingClusterAreas.SizingClusterAreas.setValues "abaqus.Optimization.SizingClusterAreas.SizingClusterAreas.setValues.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Optimization.SizingClusterAreas.SizingClusterAreas.setValues "abaqus.Optimization.SizingClusterAreas.SizingClusterAreas.setValues.kwargs (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingClusterAreas.py#L51-L54)[¶](#abaqus.Optimization.SizingClusterAreas.SizingClusterAreas.setValues "Permalink to this definition")
    :   This method modifies the SizingClusterAreas object.

*class* SizingCyclicSymmetry(*[name](#abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry "abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry.__init__.name (Python parameter)")*, *[region](#abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry "abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry.__init__.region (Python parameter)")*, *[translation](#abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry "abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry.__init__.translation (Python parameter)")*, *[axis](#abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry "abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry.__init__.axis (Python parameter)")=`abaqusConstants.AXIS_1`*, *[csys](#abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry "abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry.__init__.csys (Python parameter)")=`None`*, *[ignoreFrozenArea](#abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry "abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry.__init__.ignoreFrozenArea (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingCyclicSymmetry.py#L13-L112)[¶](#abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The SizingCyclicSymmetry object defines a sizing cyclic symmetry geometric restriction. The
    SizingCyclicSymmetry object is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [SizingCyclicSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingcyclicsymmetrypyc.htm?contextscope=all).

    Member Details:

    axis : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'AXIS_1'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingCyclicSymmetry.py#L34-L37)[¶](#abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry.axis "Permalink to this definition")
    :   A SymbolicConstant specifying the translation direction defined along an axis positioned
        at the **csys** origin. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default value
        is AXIS\_1.

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingCyclicSymmetry.py#L39-L42)[¶](#abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
        global coordinate system is used. When this member is queried, it returns an Int. The
        default value is None.

    ignoreFrozenArea : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingCyclicSymmetry.py#L44-L45)[¶](#abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry.ignoreFrozenArea "Permalink to this definition")
    :   A Boolean specifying whether to ignore frozen areas. The default value is OFF.

    setValues(*[axis](#abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry.setValues.axis "abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry.setValues.axis (Python parameter) — A SymbolicConstant specifying the translation direction defined along an axis positioned at the csys origin.")=`abaqusConstants.AXIS_1`*, *[csys](#abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry.setValues.csys "abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry.setValues.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[ignoreFrozenArea](#abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry.setValues.ignoreFrozenArea "abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry.setValues.ignoreFrozenArea (Python parameter) — A Boolean specifying whether to ignore frozen areas.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingCyclicSymmetry.py#L90-L112)[¶](#abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry.setValues "Permalink to this definition")
    :   This method modifies the SizingCyclicSymmetry object.

        Note

        Check [SizingCyclicSymmetry.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingcyclicsymmetrypyc.htm?contextscope=all#simaker-sizingcyclicsymmetrysetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry.setValues-parameters "Permalink to this headline")
        :   axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry.setValues.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the translation direction defined along an axis positioned
                at the **csys** origin. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default value
                is AXIS\_1.

            csys=`None`[¶](#abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            ignoreFrozenArea=`0`[¶](#abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry.setValues.ignoreFrozenArea "Permalink to this definition")
            :   A Boolean specifying whether to ignore frozen areas. The default value is OFF.

    translation : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingCyclicSymmetry.py)[¶](#abaqus.Optimization.SizingCyclicSymmetry.SizingCyclicSymmetry.translation "Permalink to this definition")
    :   A Float specifying the translation distance.

*class* SizingFrozenArea(*[name](#abaqus.Optimization.SizingFrozenArea.SizingFrozenArea "abaqus.Optimization.SizingFrozenArea.SizingFrozenArea.__init__.name (Python parameter)")*, *[region](#abaqus.Optimization.SizingFrozenArea.SizingFrozenArea "abaqus.Optimization.SizingFrozenArea.SizingFrozenArea.__init__.region (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingFrozenArea.py#L9-L53)[¶](#abaqus.Optimization.SizingFrozenArea.SizingFrozenArea "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The SizingFrozenArea object defines a sizing frozen area geometric restriction. The SizingFrozenArea
    object is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [SizingFrozenArea on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingfrozenareapyc.htm?contextscope=all).

    Member Details:

    setValues(*\*[args](#abaqus.Optimization.SizingFrozenArea.SizingFrozenArea.setValues "abaqus.Optimization.SizingFrozenArea.SizingFrozenArea.setValues.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Optimization.SizingFrozenArea.SizingFrozenArea.setValues "abaqus.Optimization.SizingFrozenArea.SizingFrozenArea.setValues.kwargs (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingFrozenArea.py#L50-L53)[¶](#abaqus.Optimization.SizingFrozenArea.SizingFrozenArea.setValues "Permalink to this definition")
    :   This method modifies the SizingFrozenArea object.

*class* SizingMemberSize(*[name](#abaqus.Optimization.SizingMemberSize.SizingMemberSize "abaqus.Optimization.SizingMemberSize.SizingMemberSize.__init__.name (Python parameter)")*, *[region](#abaqus.Optimization.SizingMemberSize.SizingMemberSize "abaqus.Optimization.SizingMemberSize.SizingMemberSize.__init__.region (Python parameter)")*, *[minWidth](#abaqus.Optimization.SizingMemberSize.SizingMemberSize "abaqus.Optimization.SizingMemberSize.SizingMemberSize.__init__.minWidth (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingMemberSize.py#L9-L59)[¶](#abaqus.Optimization.SizingMemberSize.SizingMemberSize "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The SizingMemberSize object defines a sizing member size geometric restriction. The SizingMemberSize
    object is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [SizingMemberSize on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingmembersizepyc.htm?contextscope=all).

    Member Details:

    minWidth : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingMemberSize.py)[¶](#abaqus.Optimization.SizingMemberSize.SizingMemberSize.minWidth "Permalink to this definition")
    :   A Float specifying the min width.

    setValues(*\*[args](#abaqus.Optimization.SizingMemberSize.SizingMemberSize.setValues "abaqus.Optimization.SizingMemberSize.SizingMemberSize.setValues.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Optimization.SizingMemberSize.SizingMemberSize.setValues "abaqus.Optimization.SizingMemberSize.SizingMemberSize.setValues.kwargs (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingMemberSize.py#L56-L59)[¶](#abaqus.Optimization.SizingMemberSize.SizingMemberSize.setValues "Permalink to this definition")
    :   This method modifies the sizingMemberSize object.

*class* SizingPlanarSymmetry(*[name](#abaqus.Optimization.SizingPlanarSymmetry.SizingPlanarSymmetry "abaqus.Optimization.SizingPlanarSymmetry.SizingPlanarSymmetry.__init__.name (Python parameter)")*, *[region](#abaqus.Optimization.SizingPlanarSymmetry.SizingPlanarSymmetry "abaqus.Optimization.SizingPlanarSymmetry.SizingPlanarSymmetry.__init__.region (Python parameter)")*, *[axis](#abaqus.Optimization.SizingPlanarSymmetry.SizingPlanarSymmetry "abaqus.Optimization.SizingPlanarSymmetry.SizingPlanarSymmetry.__init__.axis (Python parameter)")=`abaqusConstants.AXIS_1`*, *[csys](#abaqus.Optimization.SizingPlanarSymmetry.SizingPlanarSymmetry "abaqus.Optimization.SizingPlanarSymmetry.SizingPlanarSymmetry.__init__.csys (Python parameter)")=`None`*, *[ignoreFrozenArea](#abaqus.Optimization.SizingPlanarSymmetry.SizingPlanarSymmetry "abaqus.Optimization.SizingPlanarSymmetry.SizingPlanarSymmetry.__init__.ignoreFrozenArea (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingPlanarSymmetry.py#L13-L85)[¶](#abaqus.Optimization.SizingPlanarSymmetry.SizingPlanarSymmetry "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The SizingPlanarSymmetry object defines a sizing planar symmetry geometric restriction. The
    SizingPlanarSymmetry object is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [SizingPlanarSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingplanarsymmetrypyc.htm?contextscope=all).

    Member Details:

    axis : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'AXIS_1'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingPlanarSymmetry.py#L31-L33)[¶](#abaqus.Optimization.SizingPlanarSymmetry.SizingPlanarSymmetry.axis "Permalink to this definition")
    :   A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS\_1, AXIS\_2,
        and AXIS\_3. The default value is AXIS\_1.

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingPlanarSymmetry.py#L35-L38)[¶](#abaqus.Optimization.SizingPlanarSymmetry.SizingPlanarSymmetry.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
        global coordinate system is used. When this member is queried, it returns an Int. The
        default value is None.

    ignoreFrozenArea : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingPlanarSymmetry.py#L40-L41)[¶](#abaqus.Optimization.SizingPlanarSymmetry.SizingPlanarSymmetry.ignoreFrozenArea "Permalink to this definition")
    :   A Boolean specifying whether to ignore frozen areas. The default value is OFF.

    setValues(*\*[args](#abaqus.Optimization.SizingPlanarSymmetry.SizingPlanarSymmetry.setValues "abaqus.Optimization.SizingPlanarSymmetry.SizingPlanarSymmetry.setValues.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Optimization.SizingPlanarSymmetry.SizingPlanarSymmetry.setValues "abaqus.Optimization.SizingPlanarSymmetry.SizingPlanarSymmetry.setValues.kwargs (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingPlanarSymmetry.py#L82-L85)[¶](#abaqus.Optimization.SizingPlanarSymmetry.SizingPlanarSymmetry.setValues "Permalink to this definition")
    :   This method modifies the sizingPlanarSymmetry object.

*class* SizingPointSymmetry(*[name](#abaqus.Optimization.SizingPointSymmetry.SizingPointSymmetry "abaqus.Optimization.SizingPointSymmetry.SizingPointSymmetry.__init__.name (Python parameter)")*, *[region](#abaqus.Optimization.SizingPointSymmetry.SizingPointSymmetry "abaqus.Optimization.SizingPointSymmetry.SizingPointSymmetry.__init__.region (Python parameter)")*, *[csys](#abaqus.Optimization.SizingPointSymmetry.SizingPointSymmetry "abaqus.Optimization.SizingPointSymmetry.SizingPointSymmetry.__init__.csys (Python parameter)")=`None`*, *[ignoreFrozenArea](#abaqus.Optimization.SizingPointSymmetry.SizingPointSymmetry "abaqus.Optimization.SizingPointSymmetry.SizingPointSymmetry.__init__.ignoreFrozenArea (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingPointSymmetry.py#L10-L84)[¶](#abaqus.Optimization.SizingPointSymmetry.SizingPointSymmetry "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The SizingPointSymmetry object defines a sizing point symmetry geometric restriction. The
    SizingPointSymmetry object is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [SizingPointSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingpointsymmetrypyc.htm?contextscope=all).

    Member Details:

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingPointSymmetry.py#L28-L31)[¶](#abaqus.Optimization.SizingPointSymmetry.SizingPointSymmetry.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the position of the symmetry point defined as the
        origin of a local coordinate system. If **csys** = None, the global coordinate system is
        used. When this member is queried, it returns an Int. The default value is None.

    ignoreFrozenArea : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingPointSymmetry.py#L33-L34)[¶](#abaqus.Optimization.SizingPointSymmetry.SizingPointSymmetry.ignoreFrozenArea "Permalink to this definition")
    :   A Boolean specifying whether to ignore frozen areas. The default value is OFF.

    setValues(*[csys](#abaqus.Optimization.SizingPointSymmetry.SizingPointSymmetry.setValues.csys "abaqus.Optimization.SizingPointSymmetry.SizingPointSymmetry.setValues.csys (Python parameter) — None or a DatumCsys object specifying the position of the symmetry point defined as the origin of a local coordinate system.")=`None`*, *[ignoreFrozenArea](#abaqus.Optimization.SizingPointSymmetry.SizingPointSymmetry.setValues.ignoreFrozenArea "abaqus.Optimization.SizingPointSymmetry.SizingPointSymmetry.setValues.ignoreFrozenArea (Python parameter) — A Boolean specifying whether to ignore frozen areas.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingPointSymmetry.py#L71-L84)[¶](#abaqus.Optimization.SizingPointSymmetry.SizingPointSymmetry.setValues "Permalink to this definition")
    :   This method modifies the SizingPointSymmetry object.

        Note

        Check [SizingPointSymmetry.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingpointsymmetrypyc.htm?contextscope=all#simaker-sizingpointsymmetrysetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.SizingPointSymmetry.SizingPointSymmetry.setValues-parameters "Permalink to this headline")
        :   csys=`None`[¶](#abaqus.Optimization.SizingPointSymmetry.SizingPointSymmetry.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the position of the symmetry point defined as the
                origin of a local coordinate system. If **csys** = None, the global coordinate system is
                used. When this member is queried, it returns an Int. The default value is None.

            ignoreFrozenArea=`0`[¶](#abaqus.Optimization.SizingPointSymmetry.SizingPointSymmetry.setValues.ignoreFrozenArea "Permalink to this definition")
            :   A Boolean specifying whether to ignore frozen areas. The default value is OFF.

*class* SizingRotationalSymmetry(*[name](#abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry "abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry.__init__.name (Python parameter)")*, *[angle](#abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry "abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry.__init__.angle (Python parameter)")*, *[region](#abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry "abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry.__init__.region (Python parameter)")*, *[axis](#abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry "abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry.__init__.axis (Python parameter)")=`abaqusConstants.AXIS_1`*, *[csys](#abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry "abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry.__init__.csys (Python parameter)")=`None`*, *[ignoreFrozenArea](#abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry "abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry.__init__.ignoreFrozenArea (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingRotationalSymmetry.py#L13-L109)[¶](#abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The SizingRotationalSymmetry object defines a sizing rotational symmetry geometric restriction. The
    SizingRotationalSymmetry object is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [SizingRotationalSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingrotationalsymmetrypyc.htm?contextscope=all).

    Member Details:

    angle : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingRotationalSymmetry.py)[¶](#abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry.angle "Permalink to this definition")
    :   A Float specifying the repeating segment size, an angle in degrees.

    axis : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'AXIS_1'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingRotationalSymmetry.py#L34-L36)[¶](#abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry.axis "Permalink to this definition")
    :   A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS\_1, AXIS\_2,
        and AXIS\_3. The default value is AXIS\_1.

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingRotationalSymmetry.py#L38-L41)[¶](#abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
        global coordinate system is used. When this member is queried, it returns an Int. The
        default value is None.

    ignoreFrozenArea : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingRotationalSymmetry.py#L43-L44)[¶](#abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry.ignoreFrozenArea "Permalink to this definition")
    :   A Boolean specifying whether to ignore frozen areas. The default value is OFF.

    setValues(*[axis](#abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry.setValues.axis "abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry.setValues.axis (Python parameter) — A SymbolicConstant specifying the axis of symmetry.")=`abaqusConstants.AXIS_1`*, *[csys](#abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry.setValues.csys "abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry.setValues.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[ignoreFrozenArea](#abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry.setValues.ignoreFrozenArea "abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry.setValues.ignoreFrozenArea (Python parameter) — A Boolean specifying whether to ignore frozen areas.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingRotationalSymmetry.py#L88-L109)[¶](#abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry.setValues "Permalink to this definition")
    :   This method modifies the SizingRotationalSymmetry object.

        Note

        Check [SizingRotationalSymmetry.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingrotationalsymmetrypyc.htm?contextscope=all#simaker-sizingrotationalsymmetrysetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry.setValues-parameters "Permalink to this headline")
        :   axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry.setValues.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS\_1, AXIS\_2,
                and AXIS\_3. The default value is AXIS\_1.

            csys=`None`[¶](#abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            ignoreFrozenArea=`0`[¶](#abaqus.Optimization.SizingRotationalSymmetry.SizingRotationalSymmetry.setValues.ignoreFrozenArea "Permalink to this definition")
            :   A Boolean specifying whether to ignore frozen areas. The default value is OFF.

*class* SlideRegionControl(*[name](#abaqus.Optimization.SlideRegionControl.SlideRegionControl "abaqus.Optimization.SlideRegionControl.SlideRegionControl.__init__.name (Python parameter)")*, *[clientDirection](#abaqus.Optimization.SlideRegionControl.SlideRegionControl "abaqus.Optimization.SlideRegionControl.SlideRegionControl.__init__.clientDirection (Python parameter)")*, *[region](#abaqus.Optimization.SlideRegionControl.SlideRegionControl "abaqus.Optimization.SlideRegionControl.SlideRegionControl.__init__.region (Python parameter)")*, *[approach](#abaqus.Optimization.SlideRegionControl.SlideRegionControl "abaqus.Optimization.SlideRegionControl.SlideRegionControl.__init__.approach (Python parameter)")=`abaqusConstants.FREE_FORM`*, *[csys](#abaqus.Optimization.SlideRegionControl.SlideRegionControl "abaqus.Optimization.SlideRegionControl.SlideRegionControl.__init__.csys (Python parameter)")=`None`*, *[freeFormRegion](#abaqus.Optimization.SlideRegionControl.SlideRegionControl "abaqus.Optimization.SlideRegionControl.SlideRegionControl.__init__.freeFormRegion (Python parameter)")=`None`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.SlideRegionControl.SlideRegionControl "abaqus.Optimization.SlideRegionControl.SlideRegionControl.__init__.presumeFeasibleRegionAtStart (Python parameter)")=`1`*, *[revolvedRegion](#abaqus.Optimization.SlideRegionControl.SlideRegionControl "abaqus.Optimization.SlideRegionControl.SlideRegionControl.__init__.revolvedRegion (Python parameter)")=`None`*, *[tolerance1](#abaqus.Optimization.SlideRegionControl.SlideRegionControl "abaqus.Optimization.SlideRegionControl.SlideRegionControl.__init__.tolerance1 (Python parameter)")=`0`*, *[tolerance2](#abaqus.Optimization.SlideRegionControl.SlideRegionControl "abaqus.Optimization.SlideRegionControl.SlideRegionControl.__init__.tolerance2 (Python parameter)")=`0`*, *[tolerance3](#abaqus.Optimization.SlideRegionControl.SlideRegionControl "abaqus.Optimization.SlideRegionControl.SlideRegionControl.__init__.tolerance3 (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SlideRegionControl.py#L13-L186)[¶](#abaqus.Optimization.SlideRegionControl.SlideRegionControl "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The SlideRegionControl object defines a slide region control geometric restriction. The
    SlideRegionControl object is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [SlideRegionControl on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-slideregioncontrolpyc.htm?contextscope=all).

    Member Details:

    approach : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FREE_FORM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SlideRegionControl.py#L38-L42)[¶](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.approach "Permalink to this definition")
    :   A SymbolicConstant specifying the restriction approach. The SymbolicConstant FREE\_FORM
        indicates a free-form slide region, and the SymbolicConstant TURN indicates that the
        restriction should conserve a turnable surface. Possible values are FREE\_FORM and TURN.
        The default value is FREE\_FORM.

    clientDirection : --is-rst--:py:class:`tuple`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SlideRegionControl.py)[¶](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.clientDirection "Permalink to this definition")
    :   A VertexArray object of length 2 specifying the axis of revolution. Instead of through a
        ConstrainedSketchVertex, each point may be specified through a tuple of coordinates. This is used when
        **approach** is TURN.

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SlideRegionControl.py#L44-L47)[¶](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
        global coordinate system is used. When this member is queried, it returns an Int. This
        is used when **approach** is TURN. The default value is None.

    freeFormRegion : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SlideRegionControl.py#L49-L51)[¶](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.freeFormRegion "Permalink to this definition")
    :   None or a Region object specifying the free-form region. This is used when **approach** is
        FREE\_FORM. The default value is None.

    presumeFeasibleRegionAtStart : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SlideRegionControl.py#L53-L55)[¶](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.presumeFeasibleRegionAtStart "Permalink to this definition")
    :   A Boolean specifying whether to ignore the geometric restriction in the first design
        cycle. The default value is ON.

    revolvedRegion : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SlideRegionControl.py#L57-L59)[¶](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.revolvedRegion "Permalink to this definition")
    :   None or a Region object specifying the region to revolve into a slide region. This is
        used when **approach** is TURN. The default value is None.

    setValues(*[approach](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues.approach "abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues.approach (Python parameter) — A SymbolicConstant specifying the restriction approach.")=`abaqusConstants.FREE_FORM`*, *[csys](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues.csys "abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[freeFormRegion](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues.freeFormRegion "abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues.freeFormRegion (Python parameter) — None or a Region object specifying the free-form region.")=`None`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues.presumeFeasibleRegionAtStart "abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues.presumeFeasibleRegionAtStart (Python parameter) — A Boolean specifying whether to ignore the geometric restriction in the first design cycle.")=`1`*, *[revolvedRegion](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues.revolvedRegion "abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues.revolvedRegion (Python parameter) — None or a Region object specifying the region to revolve into a slide region.")=`None`*, *[tolerance1](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues.tolerance1 "abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues.tolerance1 (Python parameter) — A Float specifying the geometric tolerance in the 1-direction.")=`0`*, *[tolerance2](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues.tolerance2 "abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues.tolerance2 (Python parameter) — A Float specifying the geometric tolerance in the 2-direction.")=`0`*, *[tolerance3](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues.tolerance3 "abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues.tolerance3 (Python parameter) — A Float specifying the geometric tolerance in the 3-direction.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SlideRegionControl.py#L142-L186)[¶](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues "Permalink to this definition")
    :   This method modifies the SlideRegionControl object.

        Note

        Check [SlideRegionControl.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-slideregioncontrolpyc.htm?contextscope=all#simaker-slideregioncontrolsetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues-parameters "Permalink to this headline")
        :   approach=`abaqusConstants.FREE_FORM`[¶](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues.approach "Permalink to this definition")
            :   A SymbolicConstant specifying the restriction approach. The SymbolicConstant FREE\_FORM
                indicates a free-form slide region, and the SymbolicConstant TURN indicates that the
                restriction should conserve a turnable surface. Possible values are FREE\_FORM and TURN.
                The default value is FREE\_FORM.

            csys=`None`[¶](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. This
                is used when **approach** is TURN. The default value is None.

            freeFormRegion=`None`[¶](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues.freeFormRegion "Permalink to this definition")
            :   None or a Region object specifying the free-form region. This is used when **approach** is
                FREE\_FORM. The default value is None.

            presumeFeasibleRegionAtStart=`1`[¶](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues.presumeFeasibleRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore the geometric restriction in the first design
                cycle. The default value is ON.

            revolvedRegion=`None`[¶](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues.revolvedRegion "Permalink to this definition")
            :   None or a Region object specifying the region to revolve into a slide region. This is
                used when **approach** is TURN. The default value is None.

            tolerance1=`0`[¶](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues.tolerance1 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 1-direction. This is used when
                **approach** is TURN. The default value is 0.01.

            tolerance2=`0`[¶](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues.tolerance2 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 2-direction. This is used when
                **approach** is TURN. The default value is 0.01.

            tolerance3=`0`[¶](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.setValues.tolerance3 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 3-direction. This is used when
                **approach** is TURN. The default value is 0.01.

    tolerance1 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SlideRegionControl.py#L61-L63)[¶](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.tolerance1 "Permalink to this definition")
    :   A Float specifying the geometric tolerance in the 1-direction. This is used when
        **approach** is TURN. The default value is 0.01.

    tolerance2 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SlideRegionControl.py#L65-L67)[¶](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.tolerance2 "Permalink to this definition")
    :   A Float specifying the geometric tolerance in the 2-direction. This is used when
        **approach** is TURN. The default value is 0.01.

    tolerance3 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SlideRegionControl.py#L69-L71)[¶](#abaqus.Optimization.SlideRegionControl.SlideRegionControl.tolerance3 "Permalink to this definition")
    :   A Float specifying the geometric tolerance in the 3-direction. This is used when
        **approach** is TURN. The default value is 0.01.

*class* StampControl(*[name](#abaqus.Optimization.StampControl.StampControl "abaqus.Optimization.StampControl.StampControl.__init__.name (Python parameter)")*, *[clientDirection](#abaqus.Optimization.StampControl.StampControl "abaqus.Optimization.StampControl.StampControl.__init__.clientDirection (Python parameter)")*, *[region](#abaqus.Optimization.StampControl.StampControl "abaqus.Optimization.StampControl.StampControl.__init__.region (Python parameter)")*, *[csys](#abaqus.Optimization.StampControl.StampControl "abaqus.Optimization.StampControl.StampControl.__init__.csys (Python parameter)")=`None`*, *[drawAngle](#abaqus.Optimization.StampControl.StampControl "abaqus.Optimization.StampControl.StampControl.__init__.drawAngle (Python parameter)")=`0`*, *[mainPoint](#abaqus.Optimization.StampControl.StampControl "abaqus.Optimization.StampControl.StampControl.__init__.mainPoint (Python parameter)")=`None`*, *[mainPointDetermination](#abaqus.Optimization.StampControl.StampControl "abaqus.Optimization.StampControl.StampControl.__init__.mainPointDetermination (Python parameter)")=`abaqusConstants.MAXIMUM`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.StampControl.StampControl "abaqus.Optimization.StampControl.StampControl.__init__.presumeFeasibleRegionAtStart (Python parameter)")=`1`*, *[tolerance1](#abaqus.Optimization.StampControl.StampControl "abaqus.Optimization.StampControl.StampControl.__init__.tolerance1 (Python parameter)")=`0`*, *[tolerance2](#abaqus.Optimization.StampControl.StampControl "abaqus.Optimization.StampControl.StampControl.__init__.tolerance2 (Python parameter)")=`0`*, *[tolerance3](#abaqus.Optimization.StampControl.StampControl "abaqus.Optimization.StampControl.StampControl.__init__.tolerance3 (Python parameter)")=`0`*, *[undercutTolerance](#abaqus.Optimization.StampControl.StampControl "abaqus.Optimization.StampControl.StampControl.__init__.undercutTolerance (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/StampControl.py#L13-L202)[¶](#abaqus.Optimization.StampControl.StampControl "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The StampControl object defines a stamp control geometric restriction. The StampControl object is derived
    from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [StampControl on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stampcontrolpyc.htm?contextscope=all).

    Member Details:

    clientDirection : --is-rst--:py:class:`tuple`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/StampControl.py)[¶](#abaqus.Optimization.StampControl.StampControl.clientDirection "Permalink to this definition")
    :   A VertexArray object of length 2 specifying the stamping direction. Instead of through a
        ConstrainedSketchVertex, each point may be specified through a tuple of coordinates.

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/StampControl.py#L37-L40)[¶](#abaqus.Optimization.StampControl.StampControl.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
        global coordinate system is used. When this member is queried, it returns an Int. The
        default value is None.

    drawAngle : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/StampControl.py#L42-L43)[¶](#abaqus.Optimization.StampControl.StampControl.drawAngle "Permalink to this definition")
    :   A Float specifying the draw angle. The default value is 0.0.

    mainPoint : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/StampControl.py#L48-L50)[¶](#abaqus.Optimization.StampControl.StampControl.mainPoint "Permalink to this definition")
    :   None or a Region object specifying the main point used when **mainPointDetermination** is
        SPECIFY. The default value is None.

        Changed in version 2022: The attribute `masterPoint` was renamed to `mainPoint`.

    mainPointDetermination : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MAXIMUM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/StampControl.py#L48-L50)[¶](#abaqus.Optimization.StampControl.StampControl.mainPointDetermination "Permalink to this definition")
    :   A SymbolicConstant specifying the rule for assigning point priority. Possible values are
        MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.

        Changed in version 2022: The attribute `masterPointDetermination` was renamed to `mainPointDetermination`.

    presumeFeasibleRegionAtStart : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/StampControl.py#L59-L61)[¶](#abaqus.Optimization.StampControl.StampControl.presumeFeasibleRegionAtStart "Permalink to this definition")
    :   A Boolean specifying whether to ignore the geometric restriction in the first design
        cycle. The default value is ON.

    setValues(*[csys](#abaqus.Optimization.StampControl.StampControl.setValues.csys "abaqus.Optimization.StampControl.StampControl.setValues.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[drawAngle](#abaqus.Optimization.StampControl.StampControl.setValues.drawAngle "abaqus.Optimization.StampControl.StampControl.setValues.drawAngle (Python parameter) — A Float specifying the draw angle.")=`0`*, *[mainPoint](#abaqus.Optimization.StampControl.StampControl.setValues.mainPoint "abaqus.Optimization.StampControl.StampControl.setValues.mainPoint (Python parameter) — None or a Region object specifying the main point used when mainPointDetermination is SPECIFY.")=`None`*, *[mainPointDetermination](#abaqus.Optimization.StampControl.StampControl.setValues.mainPointDetermination "abaqus.Optimization.StampControl.StampControl.setValues.mainPointDetermination (Python parameter) — A SymbolicConstant specifying the rule for assigning point priority.")=`abaqusConstants.MAXIMUM`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.StampControl.StampControl.setValues.presumeFeasibleRegionAtStart "abaqus.Optimization.StampControl.StampControl.setValues.presumeFeasibleRegionAtStart (Python parameter) — A Boolean specifying whether to ignore the geometric restriction in the first design cycle.")=`1`*, *[tolerance1](#abaqus.Optimization.StampControl.StampControl.setValues.tolerance1 "abaqus.Optimization.StampControl.StampControl.setValues.tolerance1 (Python parameter) — A Float specifying the geometric tolerance in the 1-direction.")=`0`*, *[tolerance2](#abaqus.Optimization.StampControl.StampControl.setValues.tolerance2 "abaqus.Optimization.StampControl.StampControl.setValues.tolerance2 (Python parameter) — A Float specifying the geometric tolerance in the 2-direction.")=`0`*, *[tolerance3](#abaqus.Optimization.StampControl.StampControl.setValues.tolerance3 "abaqus.Optimization.StampControl.StampControl.setValues.tolerance3 (Python parameter) — A Float specifying the geometric tolerance in the 3-direction.")=`0`*, *[undercutTolerance](#abaqus.Optimization.StampControl.StampControl.setValues.undercutTolerance "abaqus.Optimization.StampControl.StampControl.setValues.undercutTolerance (Python parameter) — A Float specifying the undercut tolerance.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/StampControl.py#L152-L202)[¶](#abaqus.Optimization.StampControl.StampControl.setValues "Permalink to this definition")
    :   This method modifies the StampControl object.

        Note

        Check [StampControl.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stampcontrolpyc.htm?contextscope=all#simaker-stampcontrolsetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.StampControl.StampControl.setValues-parameters "Permalink to this headline")
        :   csys=`None`[¶](#abaqus.Optimization.StampControl.StampControl.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            drawAngle=`0`[¶](#abaqus.Optimization.StampControl.StampControl.setValues.drawAngle "Permalink to this definition")
            :   A Float specifying the draw angle. The default value is 0.0.

            mainPoint=`None`[¶](#abaqus.Optimization.StampControl.StampControl.setValues.mainPoint "Permalink to this definition")
            :   None or a Region object specifying the main point used when **mainPointDetermination** is
                SPECIFY. The default value is None.

                Changed in version 2022: The argument `masterPoint` was renamed to `mainPoint`.

            mainPointDetermination=`abaqusConstants.MAXIMUM`[¶](#abaqus.Optimization.StampControl.StampControl.setValues.mainPointDetermination "Permalink to this definition")
            :   A SymbolicConstant specifying the rule for assigning point priority. Possible values are
                MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.

                Changed in version 2022: The argument `masterPointDetermination` was renamed to `mainPointDetermination`.

            presumeFeasibleRegionAtStart=`1`[¶](#abaqus.Optimization.StampControl.StampControl.setValues.presumeFeasibleRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore the geometric restriction in the first design
                cycle. The default value is ON.

            tolerance1=`0`[¶](#abaqus.Optimization.StampControl.StampControl.setValues.tolerance1 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 1-direction. The default value is
                0.01.

            tolerance2=`0`[¶](#abaqus.Optimization.StampControl.StampControl.setValues.tolerance2 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 2-direction. The default value is
                0.01.

            tolerance3=`0`[¶](#abaqus.Optimization.StampControl.StampControl.setValues.tolerance3 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 3-direction. The default value is
                0.01.

            undercutTolerance=`0`[¶](#abaqus.Optimization.StampControl.StampControl.setValues.undercutTolerance "Permalink to this definition")
            :   A Float specifying the undercut tolerance. The default value is 0.0.

    tolerance1 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/StampControl.py#L63-L65)[¶](#abaqus.Optimization.StampControl.StampControl.tolerance1 "Permalink to this definition")
    :   A Float specifying the geometric tolerance in the 1-direction. The default value is
        0.01.

    tolerance2 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/StampControl.py#L67-L69)[¶](#abaqus.Optimization.StampControl.StampControl.tolerance2 "Permalink to this definition")
    :   A Float specifying the geometric tolerance in the 2-direction. The default value is
        0.01.

    tolerance3 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/StampControl.py#L71-L73)[¶](#abaqus.Optimization.StampControl.StampControl.tolerance3 "Permalink to this definition")
    :   A Float specifying the geometric tolerance in the 3-direction. The default value is
        0.01.

    undercutTolerance : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/StampControl.py#L75-L76)[¶](#abaqus.Optimization.StampControl.StampControl.undercutTolerance "Permalink to this definition")
    :   A Float specifying the undercut tolerance. The default value is 0.0.

*class* TopologyCyclicSymmetry(*[name](#abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry "abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry.__init__.name (Python parameter)")*, *[region](#abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry "abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry.__init__.region (Python parameter)")*, *[translation](#abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry "abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry.__init__.translation (Python parameter)")*, *[axis](#abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry "abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry.__init__.axis (Python parameter)")=`abaqusConstants.AXIS_1`*, *[csys](#abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry "abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry.__init__.csys (Python parameter)")=`None`*, *[ignoreFrozenArea](#abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry "abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry.__init__.ignoreFrozenArea (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyCyclicSymmetry.py#L13-L116)[¶](#abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The TopologyCyclicSymmetry object defines a topology cyclic symmetry geometric restriction. The
    TopologyCyclicSymmetry object is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [TopologyCyclicSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologycyclicsymmetrypyc.htm?contextscope=all).

    Member Details:

    axis : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'AXIS_1'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyCyclicSymmetry.py#L36-L39)[¶](#abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry.axis "Permalink to this definition")
    :   A SymbolicConstant specifying the translation direction defined along an axis positioned
        at the **csys** origin. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default value
        is AXIS\_1.

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyCyclicSymmetry.py#L41-L44)[¶](#abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
        global coordinate system is used. When this member is queried, it returns an Int. The
        default value is None.

    ignoreFrozenArea : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyCyclicSymmetry.py#L46-L47)[¶](#abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry.ignoreFrozenArea "Permalink to this definition")
    :   A Boolean specifying whether to ignore frozen areas. The default value is OFF.

    setValues(*[axis](#abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry.setValues.axis "abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry.setValues.axis (Python parameter) — A SymbolicConstant specifying the translation direction defined along an axis positioned at the csys origin.")=`abaqusConstants.AXIS_1`*, *[csys](#abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry.setValues.csys "abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry.setValues.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[ignoreFrozenArea](#abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry.setValues.ignoreFrozenArea "abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry.setValues.ignoreFrozenArea (Python parameter) — A Boolean specifying whether to ignore frozen areas.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyCyclicSymmetry.py#L94-L116)[¶](#abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry.setValues "Permalink to this definition")
    :   This method modifies the TopologyCyclicSymmetry object.

        Note

        Check [TopologyCyclicSymmetry.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologycyclicsymmetrypyc.htm?contextscope=all#simaker-topologycyclicsymmetrysetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry.setValues-parameters "Permalink to this headline")
        :   axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry.setValues.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the translation direction defined along an axis positioned
                at the **csys** origin. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default value
                is AXIS\_1.

            csys=`None`[¶](#abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            ignoreFrozenArea=`0`[¶](#abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry.setValues.ignoreFrozenArea "Permalink to this definition")
            :   A Boolean specifying whether to ignore frozen areas. The default value is OFF.

    translation : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyCyclicSymmetry.py)[¶](#abaqus.Optimization.TopologyCyclicSymmetry.TopologyCyclicSymmetry.translation "Permalink to this definition")
    :   A Float specifying the translation distance.

*class* TopologyDemoldControl(*[name](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl "abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.__init__.name (Python parameter)")*, *[region](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl "abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.__init__.region (Python parameter)")*, *[csys](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl "abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.__init__.csys (Python parameter)")=`None`*, *[draftAngle](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl "abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.__init__.draftAngle (Python parameter)")=`0`*, *[collisionCheckRegion](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl "abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.__init__.collisionCheckRegion (Python parameter)")=`abaqusConstants.DEMOLD_REGION`*, *[pointRegion](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl "abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.__init__.pointRegion (Python parameter)")=`None`*, *[pullDirection](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl "abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.__init__.pullDirection (Python parameter)")=`()`*, *[technique](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl "abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.__init__.technique (Python parameter)")=`abaqusConstants.AUTO`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyDemoldControl.py#L13-L149)[¶](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The TopologyDemoldControl object defines a topology demold control geometric restriction. The
    TopologyDemoldControl object is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [TopologyDemoldControl on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologydemoldcontrolpyc.htm?contextscope=all).

    Member Details:

    collisionCheckRegion : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'DEMOLD_REGION'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyDemoldControl.py#L42-L45)[¶](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.collisionCheckRegion "Permalink to this definition")
    :   The SymbolicConstant DEMOLD\_REGION or a Region object specifying the collision check
        region. If the value is DEMOLD\_REGION, then the value of **region** is used as both the
        demold region and the collision check region. The default value is DEMOLD\_REGION.

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyDemoldControl.py#L33-L37)[¶](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the
        **pullDirection**. If **csys** = None, the global coordinate system is used. When this member
        is queried, it returns an Int indicating the identifier of the DatumCsys. The default
        value is None.

    draftAngle : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyDemoldControl.py#L39-L40)[¶](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.draftAngle "Permalink to this definition")
    :   A Float specifying the draft angle. The default value is 0.0.

    pointRegion : --is-rst--:py:data:`~typing.Optional`\[:py:class:`~abaqus.Region.Region.Region`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyDemoldControl.py#L47-L49)[¶](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.pointRegion "Permalink to this definition")
    :   A Region object specifying the point on a plane perpendicular to the pull direction,
        used to specify the central plane when **technique** is POINT.

    pullDirection : --is-rst--:py:class:`tuple` = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyDemoldControl.py#L51-L53)[¶](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.pullDirection "Permalink to this definition")
    :   A VertexArray object of length 2 specifying the demold pull direction. Instead of
        through a ConstrainedSketchVertex, each point may be specified through a tuple of coordinates.

    setValues(*[csys](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.setValues.csys "abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.setValues.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the pullDirection.")=`None`*, *[draftAngle](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.setValues.draftAngle "abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.setValues.draftAngle (Python parameter) — A Float specifying the draft angle.")=`0`*, *[collisionCheckRegion](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.setValues.collisionCheckRegion "abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.setValues.collisionCheckRegion (Python parameter) — The SymbolicConstant DEMOLD_REGION or a Region object specifying the collision check region.")=`abaqusConstants.DEMOLD_REGION`*, *[pointRegion](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.setValues.pointRegion "abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.setValues.pointRegion (Python parameter) — A Region object specifying the point on a plane perpendicular to the pull direction, used to specify the central plane when technique is POINT.")=`None`*, *[pullDirection](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.setValues.pullDirection "abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.setValues.pullDirection (Python parameter) — A VertexArray object of length 2 specifying the demold pull direction.")=`()`*, *[technique](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.setValues.technique "abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.setValues.technique (Python parameter) — A SymbolicConstant specifying the demold technique.")=`abaqusConstants.AUTO`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyDemoldControl.py#L114-L149)[¶](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.setValues "Permalink to this definition")
    :   This method modifies the TopologyDemoldControl object.

        Note

        Check [TopologyDemoldControl.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologydemoldcontrolpyc.htm?contextscope=all#simaker-topologydemoldcontrolsetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.setValues-parameters "Permalink to this headline")
        :   csys=`None`[¶](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the
                **pullDirection**. If **csys** = None, the global coordinate system is used. When this member
                is queried, it returns an Int indicating the identifier of the DatumCsys. The default
                value is None.

            draftAngle=`0`[¶](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.setValues.draftAngle "Permalink to this definition")
            :   A Float specifying the draft angle. The default value is 0.0.

            collisionCheckRegion=`abaqusConstants.DEMOLD_REGION`[¶](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.setValues.collisionCheckRegion "Permalink to this definition")
            :   The SymbolicConstant DEMOLD\_REGION or a Region object specifying the collision check
                region. If the value is DEMOLD\_REGION, then the value of **region** is used as both the
                demold region and the collision check region. The default value is DEMOLD\_REGION.

            pointRegion=`None`[¶](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.setValues.pointRegion "Permalink to this definition")
            :   A Region object specifying the point on a plane perpendicular to the pull direction,
                used to specify the central plane when **technique** is POINT.

            pullDirection=`()`[¶](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.setValues.pullDirection "Permalink to this definition")
            :   A VertexArray object of length 2 specifying the demold pull direction. Instead of
                through a ConstrainedSketchVertex, each point may be specified through a tuple of coordinates.

            technique=`abaqusConstants.AUTO`[¶](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.setValues.technique "Permalink to this definition")
            :   A SymbolicConstant specifying the demold technique. Possible values are AUTO,
                AUTO\_TIGHT, POINT, SURFACE, and STAMP. The default value is AUTO.

    technique : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'AUTO'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyDemoldControl.py#L55-L57)[¶](#abaqus.Optimization.TopologyDemoldControl.TopologyDemoldControl.technique "Permalink to this definition")
    :   A SymbolicConstant specifying the demold technique. Possible values are AUTO,
        AUTO\_TIGHT, POINT, SURFACE, and STAMP. The default value is AUTO.

*class* TopologyMemberSize(*[name](#abaqus.Optimization.TopologyMemberSize.TopologyMemberSize "abaqus.Optimization.TopologyMemberSize.TopologyMemberSize.__init__.name (Python parameter)")*, *[region](#abaqus.Optimization.TopologyMemberSize.TopologyMemberSize "abaqus.Optimization.TopologyMemberSize.TopologyMemberSize.__init__.region (Python parameter)")*, *[maxThickness](#abaqus.Optimization.TopologyMemberSize.TopologyMemberSize "abaqus.Optimization.TopologyMemberSize.TopologyMemberSize.__init__.maxThickness (Python parameter)")=`0`*, *[minThickness](#abaqus.Optimization.TopologyMemberSize.TopologyMemberSize "abaqus.Optimization.TopologyMemberSize.TopologyMemberSize.__init__.minThickness (Python parameter)")=`0`*, *[separation](#abaqus.Optimization.TopologyMemberSize.TopologyMemberSize "abaqus.Optimization.TopologyMemberSize.TopologyMemberSize.__init__.separation (Python parameter)")=`0`*, *[sizeRestriction](#abaqus.Optimization.TopologyMemberSize.TopologyMemberSize "abaqus.Optimization.TopologyMemberSize.TopologyMemberSize.__init__.sizeRestriction (Python parameter)")=`abaqusConstants.MINIMUM`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyMemberSize.py#L13-L113)[¶](#abaqus.Optimization.TopologyMemberSize.TopologyMemberSize "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The TopologyMemberSize object defines a topology member size geometric restriction. The
    TopologyMemberSize object is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [TopologyMemberSize on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologymembersizepyc.htm?contextscope=all).

    Member Details:

    maxThickness : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyMemberSize.py#L33-L34)[¶](#abaqus.Optimization.TopologyMemberSize.TopologyMemberSize.maxThickness "Permalink to this definition")
    :   A Float specifying the maximum thickness. The default value is 0.0.

    minThickness : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyMemberSize.py#L36-L37)[¶](#abaqus.Optimization.TopologyMemberSize.TopologyMemberSize.minThickness "Permalink to this definition")
    :   A Float specifying the minimum thickness. The default value is 0.0.

    separation : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyMemberSize.py#L39-L40)[¶](#abaqus.Optimization.TopologyMemberSize.TopologyMemberSize.separation "Permalink to this definition")
    :   A Float specifying the minimum gap. The default value is 0.0.

    setValues(*[maxThickness](#abaqus.Optimization.TopologyMemberSize.TopologyMemberSize.setValues.maxThickness "abaqus.Optimization.TopologyMemberSize.TopologyMemberSize.setValues.maxThickness (Python parameter) — A Float specifying the maximum thickness.")=`0`*, *[minThickness](#abaqus.Optimization.TopologyMemberSize.TopologyMemberSize.setValues.minThickness "abaqus.Optimization.TopologyMemberSize.TopologyMemberSize.setValues.minThickness (Python parameter) — A Float specifying the minimum thickness.")=`0`*, *[separation](#abaqus.Optimization.TopologyMemberSize.TopologyMemberSize.setValues.separation "abaqus.Optimization.TopologyMemberSize.TopologyMemberSize.setValues.separation (Python parameter) — A Float specifying the minimum gap.")=`0`*, *[sizeRestriction](#abaqus.Optimization.TopologyMemberSize.TopologyMemberSize.setValues.sizeRestriction "abaqus.Optimization.TopologyMemberSize.TopologyMemberSize.setValues.sizeRestriction (Python parameter) — A SymbolicConstant specifying whether to restrict the minimum or maximum thickness or an envelope of both.")=`abaqusConstants.MINIMUM`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyMemberSize.py#L90-L113)[¶](#abaqus.Optimization.TopologyMemberSize.TopologyMemberSize.setValues "Permalink to this definition")
    :   This method modifies the TopologyMemberSize object.

        Note

        Check [TopologyMemberSize.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologymembersizepyc.htm?contextscope=all#simaker-topologymembersizesetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.TopologyMemberSize.TopologyMemberSize.setValues-parameters "Permalink to this headline")
        :   maxThickness=`0`[¶](#abaqus.Optimization.TopologyMemberSize.TopologyMemberSize.setValues.maxThickness "Permalink to this definition")
            :   A Float specifying the maximum thickness. The default value is 0.0.

            minThickness=`0`[¶](#abaqus.Optimization.TopologyMemberSize.TopologyMemberSize.setValues.minThickness "Permalink to this definition")
            :   A Float specifying the minimum thickness. The default value is 0.0.

            separation=`0`[¶](#abaqus.Optimization.TopologyMemberSize.TopologyMemberSize.setValues.separation "Permalink to this definition")
            :   A Float specifying the minimum gap. The default value is 0.0.

            sizeRestriction=`abaqusConstants.MINIMUM`[¶](#abaqus.Optimization.TopologyMemberSize.TopologyMemberSize.setValues.sizeRestriction "Permalink to this definition")
            :   A SymbolicConstant specifying whether to restrict the minimum or maximum thickness or an
                envelope of both. Possible values are ENVELOPE, MAXIMUM, and MINIMUM. The default value
                is MINIMUM.

    sizeRestriction : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MINIMUM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyMemberSize.py#L42-L45)[¶](#abaqus.Optimization.TopologyMemberSize.TopologyMemberSize.sizeRestriction "Permalink to this definition")
    :   A SymbolicConstant specifying whether to restrict the minimum or maximum thickness or an
        envelope of both. Possible values are ENVELOPE, MAXIMUM, and MINIMUM. The default value
        is MINIMUM.

*class* TopologyMillingControl(*[name](#abaqus.Optimization.TopologyMillingControl.TopologyMillingControl "abaqus.Optimization.TopologyMillingControl.TopologyMillingControl.__init__.name (Python parameter)")*, *[millingDirections](#abaqus.Optimization.TopologyMillingControl.TopologyMillingControl "abaqus.Optimization.TopologyMillingControl.TopologyMillingControl.__init__.millingDirections (Python parameter)")*, *[region](#abaqus.Optimization.TopologyMillingControl.TopologyMillingControl "abaqus.Optimization.TopologyMillingControl.TopologyMillingControl.__init__.region (Python parameter)")*, *[csys](#abaqus.Optimization.TopologyMillingControl.TopologyMillingControl "abaqus.Optimization.TopologyMillingControl.TopologyMillingControl.__init__.csys (Python parameter)")=`None`*, *[millingCheckRegion](#abaqus.Optimization.TopologyMillingControl.TopologyMillingControl "abaqus.Optimization.TopologyMillingControl.TopologyMillingControl.__init__.millingCheckRegion (Python parameter)")=`abaqusConstants.MILLING_REGION`*, *[radius](#abaqus.Optimization.TopologyMillingControl.TopologyMillingControl "abaqus.Optimization.TopologyMillingControl.TopologyMillingControl.__init__.radius (Python parameter)")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyMillingControl.py#L13-L126)[¶](#abaqus.Optimization.TopologyMillingControl.TopologyMillingControl "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The TopologyMillingControl object defines a topology milling control geometric restriction. The
    TopologyMillingControl object is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    New in version 2022: The `TopologyMillingControl` class was added.

    Note

    Check [TopologyMillingControl on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologymillingcontrolpyc.htm?contextscope=all).

    Member Details:

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyMillingControl.py#L38-L42)[¶](#abaqus.Optimization.TopologyMillingControl.TopologyMillingControl.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the
        **millingDirections**. If **csys** = None, the global coordinate system is used. When this
        member is queried, it returns an Int indicating the identifier of the DatumCsys. The
        default value is None.

    millingCheckRegion : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MILLING_REGION'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyMillingControl.py#L44-L48)[¶](#abaqus.Optimization.TopologyMillingControl.TopologyMillingControl.millingCheckRegion "Permalink to this definition")
    :   The SymbolicConstant MILLING\_REGION or a Region object specifying the milling check
        region. If the value is MILLING\_REGION, the value of **region** is used as both the
        milling control region and the milling check region. The default value is
        MILLING\_REGION.

    millingDirections : --is-rst--:py:class:`tuple`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyMillingControl.py)[¶](#abaqus.Optimization.TopologyMillingControl.TopologyMillingControl.millingDirections "Permalink to this definition")
    :   A tuple of VertexArray objects of length 2 specifying the milling directions. Each point
        can be specified through a tuple of coordinates instead of through a ConstrainedSketchVertex.

    radius : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyMillingControl.py#L50-L52)[¶](#abaqus.Optimization.TopologyMillingControl.TopologyMillingControl.radius "Permalink to this definition")
    :   A Float specifying the radius for the collision check during the removal of the elements
        for the milling criteria.

    setValues(*[csys](#abaqus.Optimization.TopologyMillingControl.TopologyMillingControl.setValues.csys "abaqus.Optimization.TopologyMillingControl.TopologyMillingControl.setValues.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the millingDirections.")=`None`*, *[millingCheckRegion](#abaqus.Optimization.TopologyMillingControl.TopologyMillingControl.setValues.millingCheckRegion "abaqus.Optimization.TopologyMillingControl.TopologyMillingControl.setValues.millingCheckRegion (Python parameter) — The SymbolicConstant MILLING_REGION or a Region object specifying the milling check region.")=`abaqusConstants.MILLING_REGION`*, *[radius](#abaqus.Optimization.TopologyMillingControl.TopologyMillingControl.setValues.radius "abaqus.Optimization.TopologyMillingControl.TopologyMillingControl.setValues.radius (Python parameter) — A Float specifying the radius for the collision check during the removal of the elements for the milling criteria.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyMillingControl.py#L101-L126)[¶](#abaqus.Optimization.TopologyMillingControl.TopologyMillingControl.setValues "Permalink to this definition")
    :   This method modifies the TopologyMillingControl object.

        Note

        Check [TopologyMillingControl.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologymillingcontrolpyc.htm?contextscope=all#simaker-topologymillingcontrolsetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.TopologyMillingControl.TopologyMillingControl.setValues-parameters "Permalink to this headline")
        :   csys=`None`[¶](#abaqus.Optimization.TopologyMillingControl.TopologyMillingControl.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the
                **millingDirections**. If **csys** = None, the global coordinate system is used. When this
                member is queried, it returns an Int indicating the identifier of the DatumCsys. The
                default value is None.

            millingCheckRegion=`abaqusConstants.MILLING_REGION`[¶](#abaqus.Optimization.TopologyMillingControl.TopologyMillingControl.setValues.millingCheckRegion "Permalink to this definition")
            :   The SymbolicConstant MILLING\_REGION or a Region object specifying the milling check
                region. If the value is MILLING\_REGION, the value of **region** is used as both the
                milling control region and the milling check region. The default value is
                MILLING\_REGION.

            radius=`None`[¶](#abaqus.Optimization.TopologyMillingControl.TopologyMillingControl.setValues.radius "Permalink to this definition")
            :   A Float specifying the radius for the collision check during the removal of the elements
                for the milling criteria.

*class* TopologyOverhangControl(*[name](#abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl "abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl.__init__.name (Python parameter)")*, *[pullDirection](#abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl "abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl.__init__.pullDirection (Python parameter)")*, *[region](#abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl "abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl.__init__.region (Python parameter)")*, *[csys=None](#abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl "abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl.__init__.csys=None (Python parameter)")*, *[draftAngle=45](#abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl "abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl.__init__.draftAngle=45 (Python parameter)")*, *[overhangCheckRegion=abaqusConstants.OVERHANG\_REGION](#abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl "abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl.__init__.overhangCheckRegion=abaqusConstants.OVERHANG_REGION (Python parameter)")*, *[pointRegion=<abaqus.Region.Region.Region object>](#abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl "abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl.__init__.pointRegion=<abaqus.Region.Region.Region object> (Python parameter)")*, *[radius=None](#abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl "abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl.__init__.radius=None (Python parameter)")*, *[technique=abaqusConstants.AUTO](#abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl "abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl.__init__.technique=abaqusConstants.AUTO (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyOverhangControl.py#L13-L121)[¶](#abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The TopologyOverhangControl object defines a topology overhang control geometric restriction. The
    TopologyOverhangControl object is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    New in version 2019: The `TopologyOverhangControl` class was added.

    Note

    Check [TopologyOverhangControl on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologyoverhangcontrolpyc.htm?contextscope=all).

    Member Details:

    setValues(*[csys=None](#abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl.setValues "abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl.setValues.csys=None (Python parameter)")*, *[draftAngle=45](#abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl.setValues "abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl.setValues.draftAngle=45 (Python parameter)")*, *[overhangCheckRegion=abaqusConstants.OVERHANG\_REGION](#abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl.setValues "abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl.setValues.overhangCheckRegion=abaqusConstants.OVERHANG_REGION (Python parameter)")*, *[pointRegion=<abaqus.Region.Region.Region object>](#abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl.setValues "abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl.setValues.pointRegion=<abaqus.Region.Region.Region object> (Python parameter)")*, *[radius=None](#abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl.setValues "abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl.setValues.radius=None (Python parameter)")*, *[technique=abaqusConstants.AUTO](#abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl.setValues "abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl.setValues.technique=abaqusConstants.AUTO (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyOverhangControl.py#L85-L121)[¶](#abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl.setValues "Permalink to this definition")
    :   This method modifies the TopologyOverhangControl object.

        Note

        Check [TopologyOverhangControl.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologyoverhangcontrolpyc.htm?contextscope=all#simaker-topologyoverhangcontrolsetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.TopologyOverhangControl.TopologyOverhangControl.setValues-parameters "Permalink to this headline")
        :   csys : [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.13)")[[`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")], default: `None`
            :   None or a DatumCsys object specifying the local coordinate system of the
                *pullDirection*. If **csys** = None, the global coordinate system is used. When this member
                is queried, it returns an Int indicating the identifier of the DatumCsys. The default
                value is None.

            draftAngle : [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"), default: `45`
            :   A Float specifying the overhang angle. The default value is 45.0.

            overhangCheckRegion : [`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")[`OVERHANG_REGION`], default: `OVERHANG_REGION`
            :   The SymbolicConstant OVERHANG\_REGION or a Region object specifying the overhang check
                region. If the value is OVERHANG\_REGION, the value of **region** is used as both the
                overhang control region and the overhang check region. The default value is
                OVERHANG\_REGION.

            pointRegion : [`Region`](part_assembly/region.html#abaqus.Region.Surface.Region "abaqus.Region.Region.Region (Python class)"), default: `<abaqus.Region.Region.Region object at 0x7f850c6df210>`
            :   A Region object specifying the point on a plane perpendicular to the *pullDirection*
                that is used to specify the base plane when **technique** is POINT.

            radius : [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.13)")[[`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")], default: `None`
            :   A Float specifying the radius to define the size of the cones that are used in the
                internal check for the overhang criteria.

            technique : [`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")[`POINT`, `NONE`, `AUTO`], default: `AUTO`
            :   A SymbolicConstant specifying the overhang control technique used to define the base
                plane. Possible values are AUTO, POINT, and NONE. The default value is AUTO.

*class* TopologyPlanarSymmetry(*[name](#abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry "abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry.__init__.name (Python parameter)")*, *[region](#abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry "abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry.__init__.region (Python parameter)")*, *[axis](#abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry "abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry.__init__.axis (Python parameter)")=`abaqusConstants.AXIS_1`*, *[csys](#abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry "abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry.__init__.csys (Python parameter)")=`None`*, *[ignoreFrozenArea](#abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry "abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry.__init__.ignoreFrozenArea (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyPlanarSymmetry.py#L13-L107)[¶](#abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The TopologyPlanarSymmetry object defines a topology planar symmetry geometric restriction. The
    TopologyPlanarSymmetry object is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [TopologyPlanarSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologyplanarsymmetrypyc.htm?contextscope=all).

    Member Details:

    axis : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'AXIS_1'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyPlanarSymmetry.py#L33-L35)[¶](#abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry.axis "Permalink to this definition")
    :   A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS\_1, AXIS\_2,
        and AXIS\_3. The default value is AXIS\_1.

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyPlanarSymmetry.py#L37-L40)[¶](#abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
        global coordinate system is used. When this member is queried, it returns an Int. The
        default value is None.

    ignoreFrozenArea : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyPlanarSymmetry.py#L42-L43)[¶](#abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry.ignoreFrozenArea "Permalink to this definition")
    :   A Boolean specifying whether to ignore frozen areas. The default value is OFF.

    setValues(*[axis](#abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry.setValues.axis "abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry.setValues.axis (Python parameter) — A SymbolicConstant specifying the axis of symmetry.")=`abaqusConstants.AXIS_1`*, *[csys](#abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry.setValues.csys "abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry.setValues.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[ignoreFrozenArea](#abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry.setValues.ignoreFrozenArea "abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry.setValues.ignoreFrozenArea (Python parameter) — A Boolean specifying whether to ignore frozen areas.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyPlanarSymmetry.py#L86-L107)[¶](#abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry.setValues "Permalink to this definition")
    :   This method modifies the TopologyPlanarSymmetry object.

        Note

        Check [TopologyPlanarSymmetry.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologyplanarsymmetrypyc.htm?contextscope=all#simaker-topologyplanarsymmetrysetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry.setValues-parameters "Permalink to this headline")
        :   axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry.setValues.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS\_1, AXIS\_2,
                and AXIS\_3. The default value is AXIS\_1.

            csys=`None`[¶](#abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            ignoreFrozenArea=`0`[¶](#abaqus.Optimization.TopologyPlanarSymmetry.TopologyPlanarSymmetry.setValues.ignoreFrozenArea "Permalink to this definition")
            :   A Boolean specifying whether to ignore frozen areas. The default value is OFF.

*class* TopologyPointSymmetry(*[name](#abaqus.Optimization.TopologyPointSymmetry.TopologyPointSymmetry "abaqus.Optimization.TopologyPointSymmetry.TopologyPointSymmetry.__init__.name (Python parameter)")*, *[region](#abaqus.Optimization.TopologyPointSymmetry.TopologyPointSymmetry "abaqus.Optimization.TopologyPointSymmetry.TopologyPointSymmetry.__init__.region (Python parameter)")*, *[csys](#abaqus.Optimization.TopologyPointSymmetry.TopologyPointSymmetry "abaqus.Optimization.TopologyPointSymmetry.TopologyPointSymmetry.__init__.csys (Python parameter)")=`None`*, *[ignoreFrozenArea](#abaqus.Optimization.TopologyPointSymmetry.TopologyPointSymmetry "abaqus.Optimization.TopologyPointSymmetry.TopologyPointSymmetry.__init__.ignoreFrozenArea (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyPointSymmetry.py#L10-L88)[¶](#abaqus.Optimization.TopologyPointSymmetry.TopologyPointSymmetry "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The TopologyPointSymmetry object defines a topology point symmetry geometric restriction. The
    TopologyPointSymmetry object is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [TopologyPointSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologypointsymmetrypyc.htm?contextscope=all).

    Member Details:

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyPointSymmetry.py#L30-L33)[¶](#abaqus.Optimization.TopologyPointSymmetry.TopologyPointSymmetry.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the position of the symmetry point defined as the
        origin of a local coordinate system. If **csys** = None, the global coordinate system is
        used. When this member is queried, it returns an Int. The default value is None.

    ignoreFrozenArea : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyPointSymmetry.py#L35-L36)[¶](#abaqus.Optimization.TopologyPointSymmetry.TopologyPointSymmetry.ignoreFrozenArea "Permalink to this definition")
    :   A Boolean specifying whether to ignore frozen areas. The default value is OFF.

    setValues(*[csys](#abaqus.Optimization.TopologyPointSymmetry.TopologyPointSymmetry.setValues.csys "abaqus.Optimization.TopologyPointSymmetry.TopologyPointSymmetry.setValues.csys (Python parameter) — None or a DatumCsys object specifying the position of the symmetry point defined as the origin of a local coordinate system.")=`None`*, *[ignoreFrozenArea](#abaqus.Optimization.TopologyPointSymmetry.TopologyPointSymmetry.setValues.ignoreFrozenArea "abaqus.Optimization.TopologyPointSymmetry.TopologyPointSymmetry.setValues.ignoreFrozenArea (Python parameter) — A Boolean specifying whether to ignore frozen areas.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyPointSymmetry.py#L75-L88)[¶](#abaqus.Optimization.TopologyPointSymmetry.TopologyPointSymmetry.setValues "Permalink to this definition")
    :   This method modifies the TopologyPointSymmetry object.

        Note

        Check [TopologyPointSymmetry.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologypointsymmetrypyc.htm?contextscope=all#simaker-topologypointsymmetrysetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.TopologyPointSymmetry.TopologyPointSymmetry.setValues-parameters "Permalink to this headline")
        :   csys=`None`[¶](#abaqus.Optimization.TopologyPointSymmetry.TopologyPointSymmetry.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the position of the symmetry point defined as the
                origin of a local coordinate system. If **csys** = None, the global coordinate system is
                used. When this member is queried, it returns an Int. The default value is None.

            ignoreFrozenArea=`0`[¶](#abaqus.Optimization.TopologyPointSymmetry.TopologyPointSymmetry.setValues.ignoreFrozenArea "Permalink to this definition")
            :   A Boolean specifying whether to ignore frozen areas. The default value is OFF.

*class* TopologyRibDesign(*[name](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign "abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.__init__.name (Python parameter)")*, *[ribDirection](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign "abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.__init__.ribDirection (Python parameter)")*, *[ribThickness](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign "abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.__init__.ribThickness (Python parameter)")*, *[ribDistance](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign "abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.__init__.ribDistance (Python parameter)")*, *[region](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign "abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.__init__.region (Python parameter)")*, *[csys](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign "abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.__init__.csys (Python parameter)")=`None`*, *[ribDesignCheckRegion](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign "abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.__init__.ribDesignCheckRegion (Python parameter)")=`abaqusConstants.RIBDESIGN_REGION`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyRibDesign.py#L17-L147)[¶](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The TopologyRibDesign object defines a topology rib design geometric restriction. The TopologyRibDesign
    object is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    New in version 2023: The `TopologyRibDesign` class was added.

    Note

    Check [TopologyRibDesign on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologyribdesignpyc.htm?contextscope=all).

    Member Details:

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`~abaqus.Datum.DatumCsys.DatumCsys`] = `<abaqus.Datum.DatumCsys.DatumCsys object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyRibDesign.py#L52-L55)[¶](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the position of the symmetry point defined as the
        origin of a local coordinate system. If **csys** = None, the global coordinate system is
        used. When this member is queried, it returns an Int. The default value is None.

    ribDesignCheckRegion : --is-rst--:py:data:`~typing.Union`\[:py:data:`~typing.Literal`\[``RIBDESIGN\_REGION``], :py:class:`~abaqus.Region.Region.Region`] = `'RIBDESIGN_REGION'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyRibDesign.py#L57-L60)[¶](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.ribDesignCheckRegion "Permalink to this definition")
    :   The SymbolicConstant RIBDESIGN\_REGION or a Region object specifying the overhang check region. If the value
        is OVERHANG\_REGION, the value of region is used as both the overhang control region and the overhang check
        region. The default value is RIBDESIGN\_REGION.

    ribDirection : --is-rst--:py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyRibDesign.py)[¶](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.ribDirection "Permalink to this definition")
    :   A VertexArray object of length 2 specifying the out-of-plane growth direction of the ribs. Instead of
        through a Vertex, each point can be specified through a tuple of coordinates.

    ribDistance : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyRibDesign.py)[¶](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.ribDistance "Permalink to this definition")
    :   A Float specifying the average distance between the rib centers. The distance must be larger than twice
        the average element edge length.

    ribThickness : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyRibDesign.py)[¶](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.ribThickness "Permalink to this definition")
    :   A Float specifying the average thickness of the ribs.

    setValues(*[ribDirection](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.setValues.ribDirection "abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.setValues.ribDirection (Python parameter) — A VertexArray object of length 2 specifying the out-of-plane growth direction of the ribs.")*, *[ribThickness](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.setValues.ribThickness "abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.setValues.ribThickness (Python parameter) — A Float specifying the average thickness of the ribs.")*, *[ribDistance](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.setValues.ribDistance "abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.setValues.ribDistance (Python parameter) — A Float specifying the average distance between the rib centers.")*, *[region](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.setValues.region "abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.setValues.region (Python parameter) — A Region object specifying the region to which the geometric restriction is applied. When used with a TopologyTask, there is no default value.")*, *[csys](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.setValues.csys "abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.setValues.csys (Python parameter) — None or a DatumCsys object specifying the position of the symmetry point defined as the origin of a local coordinate system.")=`None`*, *[ribDesignCheckRegion](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.setValues.ribDesignCheckRegion "abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.setValues.ribDesignCheckRegion (Python parameter) — The SymbolicConstant RIBDESIGN_REGION or a Region object specifying the overhang check region.")=`abaqusConstants.RIBDESIGN_REGION`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyRibDesign.py#L112-L147)[¶](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.setValues "Permalink to this definition")
    :   This method modifies the TopologyRibDesign object.

        Note

        Check [TopologyRibDesign.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologyribdesignpyc.htm?contextscope=all#simaker-topologyribdesignsetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.setValues-parameters "Permalink to this headline")
        :   ribDirection[¶](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.setValues.ribDirection "Permalink to this definition")
            :   A VertexArray object of length 2 specifying the out-of-plane growth direction of the ribs. Instead of
                through a Vertex, each point can be specified through a tuple of coordinates.

            ribThickness[¶](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.setValues.ribThickness "Permalink to this definition")
            :   A Float specifying the average thickness of the ribs.

            ribDistance[¶](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.setValues.ribDistance "Permalink to this definition")
            :   A Float specifying the average distance between the rib centers. The distance must be larger than twice
                the average element edge length.

            region[¶](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.setValues.region "Permalink to this definition")
            :   A Region object specifying the region to which the geometric restriction is applied.
                When used with a TopologyTask, there is no default value. When used with a ShapeTask,
                the default value is MODEL.

            csys=`None`[¶](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the position of the symmetry point defined as the
                origin of a local coordinate system. If **csys** = None, the global coordinate system is
                used. When this member is queried, it returns an Int. The default value is None.

            ribDesignCheckRegion=`abaqusConstants.RIBDESIGN_REGION`[¶](#abaqus.Optimization.TopologyRibDesign.TopologyRibDesign.setValues.ribDesignCheckRegion "Permalink to this definition")
            :   The SymbolicConstant RIBDESIGN\_REGION or a Region object specifying the overhang check region. If the value
                is OVERHANG\_REGION, the value of region is used as both the overhang control region and the overhang check
                region. The default value is RIBDESIGN\_REGION.

*class* TopologyRotationalSymmetry(*[name](#abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry "abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry.__init__.name (Python parameter)")*, *[angle](#abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry "abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry.__init__.angle (Python parameter)")*, *[region](#abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry "abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry.__init__.region (Python parameter)")*, *[axis](#abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry "abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry.__init__.axis (Python parameter)")=`abaqusConstants.AXIS_1`*, *[csys](#abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry "abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry.__init__.csys (Python parameter)")=`None`*, *[ignoreFrozenArea](#abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry "abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry.__init__.ignoreFrozenArea (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyRotationalSymmetry.py#L13-L113)[¶](#abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The TopologyRotationalSymmetry object defines a topology rotational symmetry geometric restriction. The
    TopologyRotationalSymmetry object is derived from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [TopologyRotationalSymmetry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologyrotationalsymmetrypyc.htm?contextscope=all).

    Member Details:

    angle : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyRotationalSymmetry.py)[¶](#abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry.angle "Permalink to this definition")
    :   A Float specifying the repeating segment size, an angle in degrees.

    axis : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'AXIS_1'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyRotationalSymmetry.py#L36-L38)[¶](#abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry.axis "Permalink to this definition")
    :   A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS\_1, AXIS\_2,
        and AXIS\_3. The default value is AXIS\_1.

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyRotationalSymmetry.py#L40-L43)[¶](#abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
        global coordinate system is used. When this member is queried, it returns an Int. The
        default value is None.

    ignoreFrozenArea : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyRotationalSymmetry.py#L45-L46)[¶](#abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry.ignoreFrozenArea "Permalink to this definition")
    :   A Boolean specifying whether to ignore frozen areas. The default value is OFF.

    setValues(*[axis](#abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry.setValues.axis "abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry.setValues.axis (Python parameter) — A SymbolicConstant specifying the axis of symmetry.")=`abaqusConstants.AXIS_1`*, *[csys](#abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry.setValues.csys "abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry.setValues.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[ignoreFrozenArea](#abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry.setValues.ignoreFrozenArea "abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry.setValues.ignoreFrozenArea (Python parameter) — A Boolean specifying whether to ignore frozen areas.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyRotationalSymmetry.py#L92-L113)[¶](#abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry.setValues "Permalink to this definition")
    :   This method modifies the TopologyRotationalSymmetry object.

        Note

        Check [TopologyRotationalSymmetry.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologyrotationalsymmetrypyc.htm?contextscope=all#simaker-topologyrotationalsymmetrysetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry.setValues-parameters "Permalink to this headline")
        :   axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry.setValues.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the axis of symmetry. Possible values are AXIS\_1, AXIS\_2,
                and AXIS\_3. The default value is AXIS\_1.

            csys=`None`[¶](#abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            ignoreFrozenArea=`0`[¶](#abaqus.Optimization.TopologyRotationalSymmetry.TopologyRotationalSymmetry.setValues.ignoreFrozenArea "Permalink to this definition")
            :   A Boolean specifying whether to ignore frozen areas. The default value is OFF.

*class* TurnControl(*[name](#abaqus.Optimization.TurnControl.TurnControl "abaqus.Optimization.TurnControl.TurnControl.__init__.name (Python parameter)")*, *[clientDirection](#abaqus.Optimization.TurnControl.TurnControl "abaqus.Optimization.TurnControl.TurnControl.__init__.clientDirection (Python parameter)")*, *[region](#abaqus.Optimization.TurnControl.TurnControl "abaqus.Optimization.TurnControl.TurnControl.__init__.region (Python parameter)")*, *[csys](#abaqus.Optimization.TurnControl.TurnControl "abaqus.Optimization.TurnControl.TurnControl.__init__.csys (Python parameter)")=`None`*, *[mainPoint](#abaqus.Optimization.TurnControl.TurnControl "abaqus.Optimization.TurnControl.TurnControl.__init__.mainPoint (Python parameter)")=`None`*, *[mainPointDetermination](#abaqus.Optimization.TurnControl.TurnControl "abaqus.Optimization.TurnControl.TurnControl.__init__.mainPointDetermination (Python parameter)")=`abaqusConstants.MAXIMUM`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.TurnControl.TurnControl "abaqus.Optimization.TurnControl.TurnControl.__init__.presumeFeasibleRegionAtStart (Python parameter)")=`1`*, *[tolerance1](#abaqus.Optimization.TurnControl.TurnControl "abaqus.Optimization.TurnControl.TurnControl.__init__.tolerance1 (Python parameter)")=`0`*, *[tolerance2](#abaqus.Optimization.TurnControl.TurnControl "abaqus.Optimization.TurnControl.TurnControl.__init__.tolerance2 (Python parameter)")=`0`*, *[tolerance3](#abaqus.Optimization.TurnControl.TurnControl "abaqus.Optimization.TurnControl.TurnControl.__init__.tolerance3 (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TurnControl.py#L13-L180)[¶](#abaqus.Optimization.TurnControl.TurnControl "Permalink to this definition")
:   Bases: [`GeometricRestriction`](#abaqus.Optimization.TurnControl.GeometricRestriction "abaqus.Optimization.GeometricRestriction.GeometricRestriction (Python class)")

    The TurnControl object defines a turn control geometric restriction. The TurnControl object is derived
    from the GeometricRestriction object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].geometricRestrictions[name]
    ```

    Note

    Check [TurnControl on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-turncontrolpyc.htm?contextscope=all).

    Member Details:

    clientDirection : --is-rst--:py:class:`tuple`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TurnControl.py)[¶](#abaqus.Optimization.TurnControl.TurnControl.clientDirection "Permalink to this definition")
    :   A VertexArray object of length 2 specifying the direction of the rotation axis as a
        vector positioned at the **csys** origin. Instead of through a ConstrainedSketchVertex, each point might be
        specified through a tuple of coordinates.

    csys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TurnControl.py#L38-L41)[¶](#abaqus.Optimization.TurnControl.TurnControl.csys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
        global coordinate system is used. When this member is queried, it returns an Int. The
        default value is None.

    mainPoint : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TurnControl.py#L46-L48)[¶](#abaqus.Optimization.TurnControl.TurnControl.mainPoint "Permalink to this definition")
    :   None or a Region object specifying the main point used when **mainPointDetermination** is
        SPECIFY. The default value is None.

        Changed in version 2022: The attribute `masterPoint` was renamed to `mainPoint`.

    mainPointDetermination : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MAXIMUM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TurnControl.py#L46-L48)[¶](#abaqus.Optimization.TurnControl.TurnControl.mainPointDetermination "Permalink to this definition")
    :   A SymbolicConstant specifying the rule for assigning point priority. Possible values are
        MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.

        Changed in version 2022: The attribute `masterPointDetermination` was renamed to `mainPointDetermination`.

    presumeFeasibleRegionAtStart : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TurnControl.py#L57-L59)[¶](#abaqus.Optimization.TurnControl.TurnControl.presumeFeasibleRegionAtStart "Permalink to this definition")
    :   A Boolean specifying whether to ignore the geometric restriction in the first design
        cycle. The default value is ON.

    setValues(*[csys](#abaqus.Optimization.TurnControl.TurnControl.setValues.csys "abaqus.Optimization.TurnControl.TurnControl.setValues.csys (Python parameter) — None or a DatumCsys object specifying the local coordinate system.")=`None`*, *[mainPoint](#abaqus.Optimization.TurnControl.TurnControl.setValues.mainPoint "abaqus.Optimization.TurnControl.TurnControl.setValues.mainPoint (Python parameter) — None or a Region object specifying the main point used when mainPointDetermination is SPECIFY.")=`None`*, *[mainPointDetermination](#abaqus.Optimization.TurnControl.TurnControl.setValues.mainPointDetermination "abaqus.Optimization.TurnControl.TurnControl.setValues.mainPointDetermination (Python parameter) — A SymbolicConstant specifying the rule for assigning point priority.")=`abaqusConstants.MAXIMUM`*, *[presumeFeasibleRegionAtStart](#abaqus.Optimization.TurnControl.TurnControl.setValues.presumeFeasibleRegionAtStart "abaqus.Optimization.TurnControl.TurnControl.setValues.presumeFeasibleRegionAtStart (Python parameter) — A Boolean specifying whether to ignore the geometric restriction in the first design cycle.")=`1`*, *[tolerance1](#abaqus.Optimization.TurnControl.TurnControl.setValues.tolerance1 "abaqus.Optimization.TurnControl.TurnControl.setValues.tolerance1 (Python parameter) — A Float specifying the geometric tolerance in the 1-direction.")=`0`*, *[tolerance2](#abaqus.Optimization.TurnControl.TurnControl.setValues.tolerance2 "abaqus.Optimization.TurnControl.TurnControl.setValues.tolerance2 (Python parameter) — A Float specifying the geometric tolerance in the 2-direction.")=`0`*, *[tolerance3](#abaqus.Optimization.TurnControl.TurnControl.setValues.tolerance3 "abaqus.Optimization.TurnControl.TurnControl.setValues.tolerance3 (Python parameter) — A Float specifying the geometric tolerance in the 3-direction.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TurnControl.py#L139-L180)[¶](#abaqus.Optimization.TurnControl.TurnControl.setValues "Permalink to this definition")
    :   This method modifies the TurnControl object.

        Note

        Check [TurnControl.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-turncontrolpyc.htm?contextscope=all#simaker-turncontrolsetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.TurnControl.TurnControl.setValues-parameters "Permalink to this headline")
        :   csys=`None`[¶](#abaqus.Optimization.TurnControl.TurnControl.setValues.csys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system. If **csys** = None, the
                global coordinate system is used. When this member is queried, it returns an Int. The
                default value is None.

            mainPoint=`None`[¶](#abaqus.Optimization.TurnControl.TurnControl.setValues.mainPoint "Permalink to this definition")
            :   None or a Region object specifying the main point used when **mainPointDetermination** is
                SPECIFY. The default value is None.

            mainPointDetermination=`abaqusConstants.MAXIMUM`[¶](#abaqus.Optimization.TurnControl.TurnControl.setValues.mainPointDetermination "Permalink to this definition")
            :   A SymbolicConstant specifying the rule for assigning point priority. Possible values are
                MAXIMUM, MINIMUM, and SPECIFY. The default value is MAXIMUM.

                Changed in version 2022: The argument `masterPointDetermination` was renamed to `mainPointDetermination`.

            presumeFeasibleRegionAtStart=`1`[¶](#abaqus.Optimization.TurnControl.TurnControl.setValues.presumeFeasibleRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore the geometric restriction in the first design
                cycle. The default value is ON.

            tolerance1=`0`[¶](#abaqus.Optimization.TurnControl.TurnControl.setValues.tolerance1 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 1-direction. The default value is
                0.01.

            tolerance2=`0`[¶](#abaqus.Optimization.TurnControl.TurnControl.setValues.tolerance2 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 2-direction. The default value is
                0.01.

            tolerance3=`0`[¶](#abaqus.Optimization.TurnControl.TurnControl.setValues.tolerance3 "Permalink to this definition")
            :   A Float specifying the geometric tolerance in the 3-direction. The default value is
                0.01.

    tolerance1 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TurnControl.py#L61-L63)[¶](#abaqus.Optimization.TurnControl.TurnControl.tolerance1 "Permalink to this definition")
    :   A Float specifying the geometric tolerance in the 1-direction. The default value is
        0.01.

    tolerance2 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TurnControl.py#L65-L67)[¶](#abaqus.Optimization.TurnControl.TurnControl.tolerance2 "Permalink to this definition")
    :   A Float specifying the geometric tolerance in the 2-direction. The default value is
        0.01.

    tolerance3 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TurnControl.py#L69-L71)[¶](#abaqus.Optimization.TurnControl.TurnControl.tolerance3 "Permalink to this definition")
    :   A Float specifying the geometric tolerance in the 3-direction. The default value is
        0.01.

*class* ShapeTask(*[name](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.name (Python parameter)")*, *[abaqusSensitivities](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.abaqusSensitivities (Python parameter)")=`True`*, *[absoluteStepSizeControl](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.absoluteStepSizeControl (Python parameter)")=`abaqusConstants.MINIMUM`*, *[activateDurability](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.activateDurability (Python parameter)")=`1`*, *[additionalDurabilityFiles](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.additionalDurabilityFiles (Python parameter)")=`''`*, *[constrainedLaplacianConvergenceLevel](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.constrainedLaplacianConvergenceLevel (Python parameter)")=`abaqusConstants.NORMAL`*, *[curvatureSmoothingEdgeLength](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.curvatureSmoothingEdgeLength (Python parameter)")=`5`*, *[durabilityInputfile](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.durabilityInputfile (Python parameter)")=`''`*, *[durabilitySolver](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.durabilitySolver (Python parameter)")=`abaqusConstants.FE_SAFE`*, *[equalityConstraintTolerance](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.equalityConstraintTolerance (Python parameter)")=`None`*, *[featureRecognitionAngle](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.featureRecognitionAngle (Python parameter)")=`30`*, *[filterExponent](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.filterExponent (Python parameter)")=`1`*, *[filterMaxRadius](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.filterMaxRadius (Python parameter)")=`None`*, *[filterRadiusReduction](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.filterRadiusReduction (Python parameter)")=`None`*, *[firstCycleDeletedVolumeTechnique](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.firstCycleDeletedVolumeTechnique (Python parameter)")=`0`*, *[freezeBoundaryConditionRegions](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.freezeBoundaryConditionRegions (Python parameter)")=`0`*, *[frozenBoundaryConditionRegion](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.frozenBoundaryConditionRegion (Python parameter)")=`abaqusConstants.MODEL`*, *[geometricRestrictionEvaluationFrequency](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.geometricRestrictionEvaluationFrequency (Python parameter)")=`abaqusConstants.LOW`*, *[growthScaleFactor](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.growthScaleFactor (Python parameter)")=`1`*, *[haltUponViolation](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.haltUponViolation (Python parameter)")=`0`*, *[layerReferenceRegion](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.layerReferenceRegion (Python parameter)")=`None`*, *[meshSmoothingRegionMethod](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.meshSmoothingRegionMethod (Python parameter)")=`abaqusConstants.TASK_REGION_LAYERS`*, *[meshSmoothingStrategy](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.meshSmoothingStrategy (Python parameter)")=`abaqusConstants.CONSTRAINED_LAPLACIAN`*, *[midsideInterpolation](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.midsideInterpolation (Python parameter)")=`abaqusConstants.POSITIONS`*, *[numFreeNodeLayers](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.numFreeNodeLayers (Python parameter)")=`0`*, *[numSmoothedElementLayers](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.numSmoothedElementLayers (Python parameter)")=`None`*, *[presumeFeasibleBCRegionAtStart](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.presumeFeasibleBCRegionAtStart (Python parameter)")=`1`*, *[quadMaxAngle](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.quadMaxAngle (Python parameter)")=`160`*, *[quadMinAngle](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.quadMinAngle (Python parameter)")=`20`*, *[quadSkew](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.quadSkew (Python parameter)")=`30`*, *[quadTaper](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.quadTaper (Python parameter)")=`0`*, *[region](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.region (Python parameter)")=`abaqusConstants.MODEL`*, *[reportPoorQualityElements](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.reportPoorQualityElements (Python parameter)")=`0`*, *[reportQualityViolation](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.reportQualityViolation (Python parameter)")=`0`*, *[shrinkScaleFactor](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.shrinkScaleFactor (Python parameter)")=`1`*, *[smoothingRegion](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.smoothingRegion (Python parameter)")=`None`*, *[targetMeshQuality](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.targetMeshQuality (Python parameter)")=`abaqusConstants.LOW`*, *[tetAspectRatio](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.tetAspectRatio (Python parameter)")=`100`*, *[tetMaxAspect](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.tetMaxAspect (Python parameter)")=`8`*, *[tetMinAspect](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.tetMinAspect (Python parameter)")=`0`*, *[tetSkew](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.tetSkew (Python parameter)")=`100`*, *[triMaxAngle](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.triMaxAngle (Python parameter)")=`140`*, *[triMinAngle](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.triMinAngle (Python parameter)")=`20`*, *[updateShapeBasisVectors](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.updateShapeBasisVectors (Python parameter)")=`abaqusConstants.EVERY_CYCLE`*, *[groupOperator](#abaqus.Optimization.ShapeTask.ShapeTask "abaqus.Optimization.ShapeTask.ShapeTask.__init__.groupOperator (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L34-L687)[¶](#abaqus.Optimization.ShapeTask.ShapeTask "Permalink to this definition")
:   Bases: [`OptimizationTask`](#abaqus.Optimization.OptimizationTask.OptimizationTask "abaqus.Optimization.OptimizationTask.OptimizationTask (Python class) — Bases: OptimizationTaskBase")

    The ShapeTask object defines a shape task. The ShapeTask object is derived from the OptimizationTask
    object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name]
    ```

    Note

    Check [ShapeTask on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapetaskpyc.htm?contextscope=all).

    Member Details:

    abaqusSensitivities : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `False`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L67-L69)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.abaqusSensitivities "Permalink to this definition")
    :   A Boolean specifying whether to use Abaqus to compute the design responses and their
        sensitivities. The default value is False.

        New in version 2019: The `abaqusSensitivities` attribute was added.

    absoluteStepSizeControl : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MINIMUM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L71-L74)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.absoluteStepSizeControl "Permalink to this definition")
    :   A SymbolicConstant specifying whether to control the permitted absolute step size by the
        average optimization displacement or minimum optimization displacement. Possible values
        are MINIMUM and AVERAGE. The default value is MINIMUM.

    activateDurability : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L76-L78)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.activateDurability "Permalink to this definition")
    :   A boolean specifying whether or not the durability approach of optimization is turned
        on. The default value is ON.

    additionalDurabilityFiles : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L80-L82)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.additionalDurabilityFiles "Permalink to this definition")
    :   A String specifying the path of additional files pertaining to durability optimization.
        Only valid if the **activateDurability** argument is ON.

    constrainedLaplacianConvergenceLevel : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'NORMAL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L84-L86)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.constrainedLaplacianConvergenceLevel "Permalink to this definition")
    :   A SymbolicConstant specifying the constrained Laplacian convergence level. Possible
        values are NORMAL, CONSERVATIVE, and AGGRESSIVE. The default value is NORMAL.

    curvatureSmoothingEdgeLength : --is-rst--:py:class:`float` = `5`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L88-L89)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.curvatureSmoothingEdgeLength "Permalink to this definition")
    :   A Float specifying the edge length for the movement vector. The default value is 5.0.

    designResponses : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Optimization.DesignResponse.DesignResponse`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L46-L47)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.designResponses "Permalink to this definition")
    :   A repository of DesignResponse objects.

    durabilityInputfile : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L91-L93)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.durabilityInputfile "Permalink to this definition")
    :   A string specifying the path of the input file. Only valid if the **activateDurability**
        argument is ON and is a required argument in that case.

    durabilitySolver : --is-rst--:py:class:`str` = `'FE_SAFE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L95-L98)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.durabilitySolver "Permalink to this definition")
    :   A String specifying the type of solver for durability optimization. Possible values are:
        FE\_SAFE, FEMFAT, FALANCS, MSC\_FATIGUE, FE\_FATIGUE, DESIGN\_LIFE, CUSTOM, FEMSITE. The
        default value is FE\_SAFE. Only valid if the **activateDurability** argument is ON.

    equalityConstraintTolerance : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L100-L101)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.equalityConstraintTolerance "Permalink to this definition")
    :   A Float specifying the equality constraint tolerance. The default value is 10⁻³.

    featureRecognitionAngle : --is-rst--:py:class:`float` = `30`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L103-L105)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.featureRecognitionAngle "Permalink to this definition")
    :   A Float specifying the mesh smoothing feature recognition angle for edges and corners.
        The default value is 30.0.

    filterExponent : --is-rst--:py:class:`float` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L107-L109)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.filterExponent "Permalink to this definition")
    :   A Float specifying the weight depending on the radius, used when **filterMaxRadius** is
        specified. The default value is 1.0.

    filterMaxRadius : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L111-L113)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.filterMaxRadius "Permalink to this definition")
    :   None or a Float specifying the maximum influence radius for equivalent stress. The
        default value is None.

    filterRadiusReduction : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L115-L117)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.filterRadiusReduction "Permalink to this definition")
    :   None or a Float specifying the reduction of the radius depending on surface bending,
        used when **filterMaxRadius** is specified. The default value is None.

    firstCycleDeletedVolumeTechnique : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`, :py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L119-L122)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.firstCycleDeletedVolumeTechnique "Permalink to this definition")
    :   A SymbolicConstant specifying the method of specifying volume that can be removed
        immediately in the first design cycle. Possible values are OFF, PERCENTAGE, and
        ABSOLUTE. The default value is OFF.

    freezeBoundaryConditionRegions : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L124-L126)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.freezeBoundaryConditionRegions "Permalink to this definition")
    :   A Boolean specifying whether to exclude nodes with boundary conditions from the
        optimization. The default value is OFF.

    frozenBoundaryConditionRegion : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MODEL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L128-L131)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.frozenBoundaryConditionRegion "Permalink to this definition")
    :   The SymbolicConstant MODEL or a Region object specifying the region in which to freeze
        boundary condition regions, or the SymbolicConstant MODEL, used with
        **freezeBoundaryConditionRegions**. The default value is MODEL.

    geometricRestrictionEvaluationFrequency : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'LOW'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L133-L135)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.geometricRestrictionEvaluationFrequency "Permalink to this definition")
    :   A SymbolicConstant specifying the frequency of evaluating geometric restrictions during
        mesh smoothing. Possible values are LOW, MEDIUM, and HIGH. The default value is LOW.

    geometricRestrictions : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Optimization.GeometricRestriction.GeometricRestriction`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L55-L56)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.geometricRestrictions "Permalink to this definition")
    :   A repository of GeometricRestriction objects.

    groupOperator : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L255-L257)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.groupOperator "Permalink to this definition")
    :   A Boolean specifying whether the group in the design response will be evaluated using
        the existing algorithm or a new algorithm based on Abaqus sensitivities. The default
        value of False means that the existing algorithm will be used.

        New in version 2022: The `groupSensitivities` attribute was added.

    growthScaleFactor : --is-rst--:py:class:`float` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L137-L139)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.growthScaleFactor "Permalink to this definition")
    :   A Float specifying the scale factor to apply to optimization displacements for nodes
        with growth. The default value is 1.0.

    haltUponViolation : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L141-L143)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.haltUponViolation "Permalink to this definition")
    :   A Boolean specifying whether to halt the optimization if quality criteria are not
        satisified. The default value is OFF.

    layerReferenceRegion : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L145-L148)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.layerReferenceRegion "Permalink to this definition")
    :   None or a Region object specifying the region specifying the first node layer for mesh
        smoothing, used when **meshSmoothingRegionMethod** is TASK\_REGION\_LAYERS. The default
        value is None.

    meshSmoothingRegionMethod : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'TASK_REGION_LAYERS'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L150-L155)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.meshSmoothingRegionMethod "Permalink to this definition")
    :   A SymbolicConstant specifying the method used to determine the mesh smoothing region.
        The REGION value uses the **smoothingRegion**. The NUMBER\_OF\_LAYERS value uses the
        **layerReferenceRegion**. The TASK\_REGION\_LAYERS value will smooth six layers using the
        task region. Possible values are TASK\_REGION\_LAYERS, REGION, and NUMBER\_OF\_LAYERS. The
        default value is TASK\_REGION\_LAYERS.

    meshSmoothingStrategy : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'CONSTRAINED_LAPLACIAN'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L157-L159)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.meshSmoothingStrategy "Permalink to this definition")
    :   A SymbolicConstant specifying the method smoothing strategy. Possible values are
        CONSTRAINED\_LAPLACIAN and LOCAL\_GRADIENT. The default value is CONSTRAINED\_LAPLACIAN.

    midsideInterpolation : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'POSITIONS'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L161-L166)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.midsideInterpolation "Permalink to this definition")
    :   A SymbolicConstant specifying the approach used when treating midside node positions
        during optimization. POSITIONS indicates midside node positions are interpolated
        linearly by position. OPTIMIZATION\_DISPLACEMENT indicates they are interpolated by
        optimization displacement of corner nodes. Possible values are POSITIONS and
        OPTIMIZATION\_DISPLACEMENT. The default value is POSITIONS.

    numFreeNodeLayers : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` | :py:class:`int` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L168-L171)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.numFreeNodeLayers "Permalink to this definition")
    :   The SymbolicConstant FIX\_NONE or an Int specifying the number of node layers adjoining
        the task region to remain free during mesh smoothing. A value of 0 indicates that no
        layers are free and all layers are fixed. The default value is 0.

    numSmoothedElementLayers : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L173-L175)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.numSmoothedElementLayers "Permalink to this definition")
    :   None or an Int specifying the number of layers for mesh smoothing when
        **meshSmoothingRegionMethod** is NUMBER\_OF\_LAYERS. The default value is None.

    objectiveFunctions : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Optimization.ObjectiveFunction.ObjectiveFunction`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L49-L50)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.objectiveFunctions "Permalink to this definition")
    :   A repository of ObjectiveFunction objects.

    optimizationConstraints : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Optimization.OptimizationConstraint.OptimizationConstraint`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L52-L53)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.optimizationConstraints "Permalink to this definition")
    :   A repository of OptimizationConstraint objects.

    presumeFeasibleBCRegionAtStart : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L177-L180)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.presumeFeasibleBCRegionAtStart "Permalink to this definition")
    :   A Boolean specifying whether to ignore automatically frozen boundary condition regions
        in the first design cycle. This is used with **freezeBoundaryConditionRegions**. The
        default value is ON.

    quadMaxAngle : --is-rst--:py:class:`float` = `160`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L182-L184)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.quadMaxAngle "Permalink to this definition")
    :   A Float specifying the maximum angle for quad elements during mesh smoothing. The
        default value is 160.0.

    quadMinAngle : --is-rst--:py:class:`float` = `20`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L186-L188)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.quadMinAngle "Permalink to this definition")
    :   A Float specifying the minimum angle for quad elements during mesh smoothing. The
        default value is 20.0.

    quadSkew : --is-rst--:py:class:`float` = `30`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L190-L192)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.quadSkew "Permalink to this definition")
    :   A Float specifying the skew angle for quad elements during mesh smoothing, used with
        **reportQualityViolation**. The default value is 30.0.

    quadTaper : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L194-L196)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.quadTaper "Permalink to this definition")
    :   A Float specifying the taper for quad elements during mesh smoothing, used with
        **reportQualityViolation**. The default value is 0.5.

    region : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MODEL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L198-L200)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.region "Permalink to this definition")
    :   The SymbolicConstant MODEL or a Region object specifying the region to which the
        optimization task is applied. The default value is MODEL.

    reportPoorQualityElements : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L202-L204)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.reportPoorQualityElements "Permalink to this definition")
    :   A Boolean specifying whether to report poor quality elements during mesh smoothing. The
        default value is OFF.

    reportQualityViolation : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L206-L208)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.reportQualityViolation "Permalink to this definition")
    :   A Boolean specifying whether to report a quality criteria violation during mesh
        smoothing. The default value is OFF.

    setValues(*[abaqusSensitivities](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.abaqusSensitivities "abaqus.Optimization.ShapeTask.ShapeTask.setValues.abaqusSensitivities (Python parameter) — A Boolean specifying whether to use Abaqus to compute the design responses and their sensitivities.")=`True`*, *[absoluteStepSizeControl](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.absoluteStepSizeControl "abaqus.Optimization.ShapeTask.ShapeTask.setValues.absoluteStepSizeControl (Python parameter) — A SymbolicConstant specifying whether to control the permitted absolute step size by the average optimization displacement or minimum optimization displacement.")=`abaqusConstants.MINIMUM`*, *[activateDurability](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.activateDurability "abaqus.Optimization.ShapeTask.ShapeTask.setValues.activateDurability (Python parameter) — A boolean specifying whether or not the durability approach of optimization is turned on.")=`1`*, *[additionalDurabilityFiles](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.additionalDurabilityFiles "abaqus.Optimization.ShapeTask.ShapeTask.setValues.additionalDurabilityFiles (Python parameter) — A String specifying the path of additional files pertaining to durability optimization. Only valid if the activateDurability argument is ON.")=`''`*, *[algorithm](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.algorithm "abaqus.Optimization.ShapeTask.ShapeTask.setValues.algorithm (Python parameter) — A SymbolicConstant specifying the optimization task algorithm.")=`abaqusConstants.CONDITION_BASED_OPTIMIZATION`*, *[constrainedLaplacianConvergenceLevel](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.constrainedLaplacianConvergenceLevel "abaqus.Optimization.ShapeTask.ShapeTask.setValues.constrainedLaplacianConvergenceLevel (Python parameter) — A SymbolicConstant specifying the constrained Laplacian convergence level.")=`abaqusConstants.NORMAL`*, *[curvatureSmoothingEdgeLength](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.curvatureSmoothingEdgeLength "abaqus.Optimization.ShapeTask.ShapeTask.setValues.curvatureSmoothingEdgeLength (Python parameter) — A Float specifying the edge length for the movement vector.")=`5`*, *[durabilityInputfile](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.durabilityInputfile "abaqus.Optimization.ShapeTask.ShapeTask.setValues.durabilityInputfile (Python parameter) — A string specifying the path of the input file.")=`''`*, *[durabilitySolver](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.durabilitySolver "abaqus.Optimization.ShapeTask.ShapeTask.setValues.durabilitySolver (Python parameter) — A String specifying the type of solver for durability optimization.")=`abaqusConstants.FE_SAFE`*, *[equalityConstraintTolerance](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.equalityConstraintTolerance "abaqus.Optimization.ShapeTask.ShapeTask.setValues.equalityConstraintTolerance (Python parameter) — A Float specifying the equality constraint tolerance.")=`None`*, *[featureRecognitionAngle](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.featureRecognitionAngle "abaqus.Optimization.ShapeTask.ShapeTask.setValues.featureRecognitionAngle (Python parameter) — A Float specifying the mesh smoothing feature recognition angle for edges and corners. The default value is 30.0.")=`30`*, *[filterExponent](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.filterExponent "abaqus.Optimization.ShapeTask.ShapeTask.setValues.filterExponent (Python parameter) — A Float specifying the weight depending on the radius, used when filterMaxRadius is specified.")=`1`*, *[filterMaxRadius](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.filterMaxRadius "abaqus.Optimization.ShapeTask.ShapeTask.setValues.filterMaxRadius (Python parameter) — None or a Float specifying the maximum influence radius for equivalent stress.")=`None`*, *[filterRadiusReduction](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.filterRadiusReduction "abaqus.Optimization.ShapeTask.ShapeTask.setValues.filterRadiusReduction (Python parameter) — None or a Float specifying the reduction of the radius depending on surface bending, used when filterMaxRadius is specified.")=`None`*, *[firstCycleDeletedVolumeTechnique](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.firstCycleDeletedVolumeTechnique "abaqus.Optimization.ShapeTask.ShapeTask.setValues.firstCycleDeletedVolumeTechnique (Python parameter) — A SymbolicConstant specifying the method of specifying volume that can be removed immediately in the first design cycle.")=`0`*, *[freezeBoundaryConditionRegions](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.freezeBoundaryConditionRegions "abaqus.Optimization.ShapeTask.ShapeTask.setValues.freezeBoundaryConditionRegions (Python parameter) — A Boolean specifying whether to exclude nodes with boundary conditions from the optimization.")=`0`*, *[frozenBoundaryConditionRegion](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.frozenBoundaryConditionRegion "abaqus.Optimization.ShapeTask.ShapeTask.setValues.frozenBoundaryConditionRegion (Python parameter) — The SymbolicConstant MODEL or a Region object specifying the region in which to freeze boundary condition regions, or the SymbolicConstant MODEL, used with freezeBoundaryConditionRegions.")=`abaqusConstants.MODEL`*, *[geometricRestrictionEvaluationFrequency](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.geometricRestrictionEvaluationFrequency "abaqus.Optimization.ShapeTask.ShapeTask.setValues.geometricRestrictionEvaluationFrequency (Python parameter) — A SymbolicConstant specifying the frequency of evaluating geometric restrictions during mesh smoothing.")=`abaqusConstants.LOW`*, *[growthScaleFactor](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.growthScaleFactor "abaqus.Optimization.ShapeTask.ShapeTask.setValues.growthScaleFactor (Python parameter) — A Float specifying the scale factor to apply to optimization displacements for nodes with growth.")=`1`*, *[haltUponViolation](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.haltUponViolation "abaqus.Optimization.ShapeTask.ShapeTask.setValues.haltUponViolation (Python parameter) — A Boolean specifying whether to halt the optimization if quality criteria are not satisified.")=`0`*, *[layerReferenceRegion](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.layerReferenceRegion "abaqus.Optimization.ShapeTask.ShapeTask.setValues.layerReferenceRegion (Python parameter) — None or a Region object specifying the region specifying the first node layer for mesh smoothing, used when meshSmoothingRegionMethod is TASK_REGION_LAYERS.")=`None`*, *[meshSmoothingRegionMethod](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.meshSmoothingRegionMethod "abaqus.Optimization.ShapeTask.ShapeTask.setValues.meshSmoothingRegionMethod (Python parameter) — A SymbolicConstant specifying the method used to determine the mesh smoothing region. The REGION value uses the smoothingRegion.")=`abaqusConstants.TASK_REGION_LAYERS`*, *[meshSmoothingStrategy](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.meshSmoothingStrategy "abaqus.Optimization.ShapeTask.ShapeTask.setValues.meshSmoothingStrategy (Python parameter) — A SymbolicConstant specifying the method smoothing strategy.")=`abaqusConstants.CONSTRAINED_LAPLACIAN`*, *[midsideInterpolation](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.midsideInterpolation "abaqus.Optimization.ShapeTask.ShapeTask.setValues.midsideInterpolation (Python parameter) — A SymbolicConstant specifying the approach used when treating midside node positions during optimization.")=`abaqusConstants.POSITIONS`*, *[numFreeNodeLayers](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.numFreeNodeLayers "abaqus.Optimization.ShapeTask.ShapeTask.setValues.numFreeNodeLayers (Python parameter) — The SymbolicConstant FIX_NONE or an Int specifying the number of node layers adjoining the task region to remain free during mesh smoothing.")=`0`*, *[numSmoothedElementLayers](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.numSmoothedElementLayers "abaqus.Optimization.ShapeTask.ShapeTask.setValues.numSmoothedElementLayers (Python parameter) — None or an Int specifying the number of layers for mesh smoothing when meshSmoothingRegionMethod is NUMBER_OF_LAYERS.")=`None`*, *[presumeFeasibleBCRegionAtStart](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.presumeFeasibleBCRegionAtStart "abaqus.Optimization.ShapeTask.ShapeTask.setValues.presumeFeasibleBCRegionAtStart (Python parameter) — A Boolean specifying whether to ignore automatically frozen boundary condition regions in the first design cycle.")=`1`*, *[quadMaxAngle](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.quadMaxAngle "abaqus.Optimization.ShapeTask.ShapeTask.setValues.quadMaxAngle (Python parameter) — A Float specifying the maximum angle for quad elements during mesh smoothing.")=`160`*, *[quadMinAngle](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.quadMinAngle "abaqus.Optimization.ShapeTask.ShapeTask.setValues.quadMinAngle (Python parameter) — A Float specifying the minimum angle for quad elements during mesh smoothing.")=`20`*, *[quadSkew](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.quadSkew "abaqus.Optimization.ShapeTask.ShapeTask.setValues.quadSkew (Python parameter) — A Float specifying the skew angle for quad elements during mesh smoothing, used with reportQualityViolation.")=`30`*, *[quadTaper](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.quadTaper "abaqus.Optimization.ShapeTask.ShapeTask.setValues.quadTaper (Python parameter) — A Float specifying the taper for quad elements during mesh smoothing, used with reportQualityViolation.")=`0`*, *[region](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.region "abaqus.Optimization.ShapeTask.ShapeTask.setValues.region (Python parameter) — The SymbolicConstant MODEL or a Region object specifying the region to which the optimization task is applied.")=`abaqusConstants.MODEL`*, *[reportPoorQualityElements](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.reportPoorQualityElements "abaqus.Optimization.ShapeTask.ShapeTask.setValues.reportPoorQualityElements (Python parameter) — A Boolean specifying whether to report poor quality elements during mesh smoothing.")=`0`*, *[reportQualityViolation](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.reportQualityViolation "abaqus.Optimization.ShapeTask.ShapeTask.setValues.reportQualityViolation (Python parameter) — A Boolean specifying whether to report a quality criteria violation during mesh smoothing.")=`0`*, *[shrinkScaleFactor](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.shrinkScaleFactor "abaqus.Optimization.ShapeTask.ShapeTask.setValues.shrinkScaleFactor (Python parameter) — A Float specifying the scale factor to apply to optimization displacements for nodes with shrinkage.")=`1`*, *[smoothingRegion](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.smoothingRegion "abaqus.Optimization.ShapeTask.ShapeTask.setValues.smoothingRegion (Python parameter) — None or a Region object specifying the mesh smoothing region, used when meshSmoothingRegionMethod is REGION.")=`None`*, *[targetMeshQuality](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.targetMeshQuality "abaqus.Optimization.ShapeTask.ShapeTask.setValues.targetMeshQuality (Python parameter) — A SymbolicConstant specifying the target mesh quality for mesh smoothing.")=`abaqusConstants.LOW`*, *[tetAspectRatio](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.tetAspectRatio "abaqus.Optimization.ShapeTask.ShapeTask.setValues.tetAspectRatio (Python parameter) — A Float specifying the tet element aspect ratio during mesh smoothing.")=`100`*, *[tetMaxAspect](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.tetMaxAspect "abaqus.Optimization.ShapeTask.ShapeTask.setValues.tetMaxAspect (Python parameter) — A Float specifying the maximum tet element aspect ratio during mesh smoothing.")=`8`*, *[tetMinAspect](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.tetMinAspect "abaqus.Optimization.ShapeTask.ShapeTask.setValues.tetMinAspect (Python parameter) — A Float specifying the minimum tet element aspect ratio during mesh smoothing.")=`0`*, *[tetSkew](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.tetSkew "abaqus.Optimization.ShapeTask.ShapeTask.setValues.tetSkew (Python parameter) — A Float specifying the tet element skew value during mesh smoothing.")=`100`*, *[triMaxAngle](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.triMaxAngle "abaqus.Optimization.ShapeTask.ShapeTask.setValues.triMaxAngle (Python parameter) — A Float specifying the tri element maximum angle during mesh smoothing.")=`140`*, *[triMinAngle](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.triMinAngle "abaqus.Optimization.ShapeTask.ShapeTask.setValues.triMinAngle (Python parameter) — A Float specifying the tri element maximum angle during mesh smoothing.")=`20`*, *[updateShapeBasisVectors](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.updateShapeBasisVectors "abaqus.Optimization.ShapeTask.ShapeTask.setValues.updateShapeBasisVectors (Python parameter) — A SymbolicConstant specifying whether to update shape basis vectors in the first design cycle or every design cycle.")=`abaqusConstants.EVERY_CYCLE`*, *[groupOperator](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.groupOperator "abaqus.Optimization.ShapeTask.ShapeTask.setValues.groupOperator (Python parameter) — A Boolean specifying whether the group in the design response will be evaluated using the existing algorithm or a new algorithm based on Abaqus sensitivities.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L478-L687)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues "Permalink to this definition")
    :   This method modifies the ShapeTask object.

        Note

        Check [ShapeTask.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shapetaskpyc.htm?contextscope=all#simaker-shapetasksetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues-parameters "Permalink to this headline")
        :   abaqusSensitivities=`True`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.abaqusSensitivities "Permalink to this definition")
            :   A Boolean specifying whether to use Abaqus to compute the design responses and their
                sensitivities. The default value is True.

                New in version 2019: The `abaqusSensitivities` argument was added.

            absoluteStepSizeControl=`abaqusConstants.MINIMUM`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.absoluteStepSizeControl "Permalink to this definition")
            :   A SymbolicConstant specifying whether to control the permitted absolute step size by the
                average optimization displacement or minimum optimization displacement. Possible values
                are MINIMUM and AVERAGE. The default value is MINIMUM.

            activateDurability=`1`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.activateDurability "Permalink to this definition")
            :   A boolean specifying whether or not the durability approach of optimization is turned
                on. The default value is ON.

            additionalDurabilityFiles=`''`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.additionalDurabilityFiles "Permalink to this definition")
            :   A String specifying the path of additional files pertaining to durability optimization.
                Only valid if the **activateDurability** argument is ON.

            algorithm=`abaqusConstants.CONDITION_BASED_OPTIMIZATION`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.algorithm "Permalink to this definition")
            :   A SymbolicConstant specifying the optimization task algorithm. Possible values are
                GENERAL\_OPTIMIZATION and CONDITION\_BASED\_OPTIMIZATION. The default value is
                CONDITION\_BASED\_OPTIMIZATION.

            constrainedLaplacianConvergenceLevel=`abaqusConstants.NORMAL`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.constrainedLaplacianConvergenceLevel "Permalink to this definition")
            :   A SymbolicConstant specifying the constrained Laplacian convergence level. Possible
                values are NORMAL, CONSERVATIVE, and AGGRESSIVE. The default value is NORMAL.

            curvatureSmoothingEdgeLength=`5`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.curvatureSmoothingEdgeLength "Permalink to this definition")
            :   A Float specifying the edge length for the movement vector. The default value is 5.0.

            durabilityInputfile=`''`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.durabilityInputfile "Permalink to this definition")
            :   A string specifying the path of the input file. Only valid if the **activateDurability**
                argument is ON and is a required argument in that case.

            durabilitySolver=`abaqusConstants.FE_SAFE`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.durabilitySolver "Permalink to this definition")
            :   A String specifying the type of solver for durability optimization. Possible values are:
                FE\_SAFE, FEMFAT, FALANCS, MSC\_FATIGUE, FE\_FATIGUE, DESIGN\_LIFE, CUSTOM, FEMSITE. The
                default value is FE\_SAFE. Only valid if the **activateDurability** argument is ON.

            equalityConstraintTolerance=`None`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.equalityConstraintTolerance "Permalink to this definition")
            :   A Float specifying the equality constraint tolerance. The default value is 10⁻³.

            featureRecognitionAngle=`30`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.featureRecognitionAngle "Permalink to this definition")
            :   A Float specifying the mesh smoothing feature recognition angle for edges and corners.
                The default value is 30.0.

            filterExponent=`1`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.filterExponent "Permalink to this definition")
            :   A Float specifying the weight depending on the radius, used when **filterMaxRadius** is
                specified. The default value is 1.0.

            filterMaxRadius=`None`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.filterMaxRadius "Permalink to this definition")
            :   None or a Float specifying the maximum influence radius for equivalent stress. The
                default value is None.

            filterRadiusReduction=`None`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.filterRadiusReduction "Permalink to this definition")
            :   None or a Float specifying the reduction of the radius depending on surface bending,
                used when **filterMaxRadius** is specified. The default value is None.

            firstCycleDeletedVolumeTechnique=`0`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.firstCycleDeletedVolumeTechnique "Permalink to this definition")
            :   A SymbolicConstant specifying the method of specifying volume that can be removed
                immediately in the first design cycle. Possible values are OFF, PERCENTAGE, and
                ABSOLUTE. The default value is OFF.

            freezeBoundaryConditionRegions=`0`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.freezeBoundaryConditionRegions "Permalink to this definition")
            :   A Boolean specifying whether to exclude nodes with boundary conditions from the
                optimization. The default value is OFF.

            frozenBoundaryConditionRegion=`abaqusConstants.MODEL`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.frozenBoundaryConditionRegion "Permalink to this definition")
            :   The SymbolicConstant MODEL or a Region object specifying the region in which to freeze
                boundary condition regions, or the SymbolicConstant MODEL, used with
                **freezeBoundaryConditionRegions**. The default value is MODEL.

            geometricRestrictionEvaluationFrequency=`abaqusConstants.LOW`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.geometricRestrictionEvaluationFrequency "Permalink to this definition")
            :   A SymbolicConstant specifying the frequency of evaluating geometric restrictions during
                mesh smoothing. Possible values are LOW, MEDIUM, and HIGH. The default value is LOW.

            growthScaleFactor=`1`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.growthScaleFactor "Permalink to this definition")
            :   A Float specifying the scale factor to apply to optimization displacements for nodes
                with growth. The default value is 1.0.

            haltUponViolation=`0`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.haltUponViolation "Permalink to this definition")
            :   A Boolean specifying whether to halt the optimization if quality criteria are not
                satisified. The default value is OFF.

            layerReferenceRegion=`None`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.layerReferenceRegion "Permalink to this definition")
            :   None or a Region object specifying the region specifying the first node layer for mesh
                smoothing, used when **meshSmoothingRegionMethod** is TASK\_REGION\_LAYERS. The default
                value is None.

            meshSmoothingRegionMethod=`abaqusConstants.TASK_REGION_LAYERS`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.meshSmoothingRegionMethod "Permalink to this definition")
            :   A SymbolicConstant specifying the method used to determine the mesh smoothing region.
                The REGION value uses the **smoothingRegion**. The NUMBER\_OF\_LAYERS value uses the
                **layerReferenceRegion**. The TASK\_REGION\_LAYERS value will smooth six layers using the
                task region. Possible values are TASK\_REGION\_LAYERS, REGION, and NUMBER\_OF\_LAYERS. The
                default value is TASK\_REGION\_LAYERS.

            meshSmoothingStrategy=`abaqusConstants.CONSTRAINED_LAPLACIAN`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.meshSmoothingStrategy "Permalink to this definition")
            :   A SymbolicConstant specifying the method smoothing strategy. Possible values are
                CONSTRAINED\_LAPLACIAN and LOCAL\_GRADIENT. The default value is CONSTRAINED\_LAPLACIAN.

            midsideInterpolation=`abaqusConstants.POSITIONS`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.midsideInterpolation "Permalink to this definition")
            :   A SymbolicConstant specifying the approach used when treating midside node positions
                during optimization. POSITIONS indicates midside node positions are interpolated
                linearly by position. OPTIMIZATION\_DISPLACEMENT indicates they are interpolated by
                optimization displacement of corner nodes. Possible values are POSITIONS and
                OPTIMIZATION\_DISPLACEMENT. The default value is POSITIONS.

            numFreeNodeLayers=`0`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.numFreeNodeLayers "Permalink to this definition")
            :   The SymbolicConstant FIX\_NONE or an Int specifying the number of node layers adjoining
                the task region to remain free during mesh smoothing. A value of 0 indicates that no
                layers are free and all layers are fixed. The default value is 0.

            numSmoothedElementLayers=`None`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.numSmoothedElementLayers "Permalink to this definition")
            :   None or an Int specifying the number of layers for mesh smoothing when
                **meshSmoothingRegionMethod** is NUMBER\_OF\_LAYERS. The default value is None.

            presumeFeasibleBCRegionAtStart=`1`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.presumeFeasibleBCRegionAtStart "Permalink to this definition")
            :   A Boolean specifying whether to ignore automatically frozen boundary condition regions
                in the first design cycle. This is used with **freezeBoundaryConditionRegions**. The
                default value is ON.

            quadMaxAngle=`160`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.quadMaxAngle "Permalink to this definition")
            :   A Float specifying the maximum angle for quad elements during mesh smoothing. The
                default value is 160.0.

            quadMinAngle=`20`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.quadMinAngle "Permalink to this definition")
            :   A Float specifying the minimum angle for quad elements during mesh smoothing. The
                default value is 20.0.

            quadSkew=`30`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.quadSkew "Permalink to this definition")
            :   A Float specifying the skew angle for quad elements during mesh smoothing, used with
                **reportQualityViolation**. The default value is 30.0.

            quadTaper=`0`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.quadTaper "Permalink to this definition")
            :   A Float specifying the taper for quad elements during mesh smoothing, used with
                **reportQualityViolation**. The default value is 0.5.

            region=`abaqusConstants.MODEL`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.region "Permalink to this definition")
            :   The SymbolicConstant MODEL or a Region object specifying the region to which the
                optimization task is applied. The default value is MODEL.

            reportPoorQualityElements=`0`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.reportPoorQualityElements "Permalink to this definition")
            :   A Boolean specifying whether to report poor quality elements during mesh smoothing. The
                default value is OFF.

            reportQualityViolation=`0`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.reportQualityViolation "Permalink to this definition")
            :   A Boolean specifying whether to report a quality criteria violation during mesh
                smoothing. The default value is OFF.

            shrinkScaleFactor=`1`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.shrinkScaleFactor "Permalink to this definition")
            :   A Float specifying the scale factor to apply to optimization displacements for nodes
                with shrinkage. The default value is 1.0.

            smoothingRegion=`None`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.smoothingRegion "Permalink to this definition")
            :   None or a Region object specifying the mesh smoothing region, used when
                **meshSmoothingRegionMethod** is REGION. The default value is None.

            targetMeshQuality=`abaqusConstants.LOW`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.targetMeshQuality "Permalink to this definition")
            :   A SymbolicConstant specifying the target mesh quality for mesh smoothing. Possible
                values are NONE, LOW, MEDIUM, and HIGH. The default value is LOW.

            tetAspectRatio=`100`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.tetAspectRatio "Permalink to this definition")
            :   A Float specifying the tet element aspect ratio during mesh smoothing. The default value
                is 100.0.

            tetMaxAspect=`8`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.tetMaxAspect "Permalink to this definition")
            :   A Float specifying the maximum tet element aspect ratio during mesh smoothing. The
                default value is 8.0.

            tetMinAspect=`0`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.tetMinAspect "Permalink to this definition")
            :   A Float specifying the minimum tet element aspect ratio during mesh smoothing. The
                default value is 0.222.

            tetSkew=`100`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.tetSkew "Permalink to this definition")
            :   A Float specifying the tet element skew value during mesh smoothing. The default value
                is 100.0.

            triMaxAngle=`140`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.triMaxAngle "Permalink to this definition")
            :   A Float specifying the tri element maximum angle during mesh smoothing. The default
                value is 140.0.

            triMinAngle=`20`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.triMinAngle "Permalink to this definition")
            :   A Float specifying the tri element maximum angle during mesh smoothing. The default
                value is 20.0.

            updateShapeBasisVectors=`abaqusConstants.EVERY_CYCLE`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.updateShapeBasisVectors "Permalink to this definition")
            :   A SymbolicConstant specifying whether to update shape basis vectors in the first design
                cycle or every design cycle. Possible values are EVERY\_CYCLE and FIRST\_CYCLE. The
                default value is EVERY\_CYCLE.

            groupOperator=`0`[¶](#abaqus.Optimization.ShapeTask.ShapeTask.setValues.groupOperator "Permalink to this definition")
            :   A Boolean specifying whether the group in the design response will be evaluated using
                the existing algorithm or a new algorithm based on Abaqus sensitivities. The default
                value of False means that the existing algorithm will be used.

                New in version 2022: The `groupOperator` argument was added.

    shrinkScaleFactor : --is-rst--:py:class:`float` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L137-L139)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.shrinkScaleFactor "Permalink to this definition")
    :   A Float specifying the scale factor to apply to optimization displacements for nodes
        with shrinkage. The default value is 1.0.

    smoothingRegion : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L214-L216)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.smoothingRegion "Permalink to this definition")
    :   None or a Region object specifying the mesh smoothing region, used when
        **meshSmoothingRegionMethod** is REGION. The default value is None.

    stopConditions : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Optimization.StopCondition.StopCondition`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L58-L59)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.stopConditions "Permalink to this definition")
    :   A repository of StopCondition objects.

    targetMeshQuality : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'LOW'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L218-L220)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.targetMeshQuality "Permalink to this definition")
    :   A SymbolicConstant specifying the target mesh quality for mesh smoothing. Possible
        values are NONE, LOW, MEDIUM, and HIGH. The default value is LOW.

    tetAspectRatio : --is-rst--:py:class:`float` = `100`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L222-L224)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.tetAspectRatio "Permalink to this definition")
    :   A Float specifying the tet element aspect ratio during mesh smoothing. The default value
        is 100.0.

    tetMaxAspect : --is-rst--:py:class:`float` = `8`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L226-L228)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.tetMaxAspect "Permalink to this definition")
    :   A Float specifying the maximum tet element aspect ratio during mesh smoothing. The
        default value is 8.0.

    tetMinAspect : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L230-L232)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.tetMinAspect "Permalink to this definition")
    :   A Float specifying the minimum tet element aspect ratio during mesh smoothing. The
        default value is 0.222.

    tetSkew : --is-rst--:py:class:`float` = `100`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L234-L236)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.tetSkew "Permalink to this definition")
    :   A Float specifying the tet element skew value during mesh smoothing. The default value
        is 100.0.

    triMaxAngle : --is-rst--:py:class:`float` = `140`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L238-L240)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.triMaxAngle "Permalink to this definition")
    :   A Float specifying the tri element maximum angle during mesh smoothing. The default
        value is 140.0.

    triMinAngle : --is-rst--:py:class:`float` = `20`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L238-L240)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.triMinAngle "Permalink to this definition")
    :   A Float specifying the tri element maximum angle during mesh smoothing. The default
        value is 20.0.

    updateShapeBasisVectors : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'EVERY_CYCLE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/ShapeTask.py#L246-L249)[¶](#abaqus.Optimization.ShapeTask.ShapeTask.updateShapeBasisVectors "Permalink to this definition")
    :   A SymbolicConstant specifying whether to update shape basis vectors in the first design
        cycle or every design cycle. Possible values are EVERY\_CYCLE and FIRST\_CYCLE. The
        default value is EVERY\_CYCLE.

*class* SizingTask(*[name](#abaqus.Optimization.SizingTask.SizingTask "abaqus.Optimization.SizingTask.SizingTask.__init__.name (Python parameter)")*, *[abaqusSensitivities](#abaqus.Optimization.SizingTask.SizingTask "abaqus.Optimization.SizingTask.SizingTask.__init__.abaqusSensitivities (Python parameter)")=`True`*, *[elementThicknessDeltaStopCriteria](#abaqus.Optimization.SizingTask.SizingTask "abaqus.Optimization.SizingTask.SizingTask.__init__.elementThicknessDeltaStopCriteria (Python parameter)")=`0`*, *[freezeBoundaryConditionRegions](#abaqus.Optimization.SizingTask.SizingTask "abaqus.Optimization.SizingTask.SizingTask.__init__.freezeBoundaryConditionRegions (Python parameter)")=`0`*, *[freezeLoadRegions](#abaqus.Optimization.SizingTask.SizingTask "abaqus.Optimization.SizingTask.SizingTask.__init__.freezeLoadRegions (Python parameter)")=`1`*, *[modeTrackingRegion](#abaqus.Optimization.SizingTask.SizingTask "abaqus.Optimization.SizingTask.SizingTask.__init__.modeTrackingRegion (Python parameter)")=`abaqusConstants.MODEL`*, *[numFulfilledStopCriteria](#abaqus.Optimization.SizingTask.SizingTask "abaqus.Optimization.SizingTask.SizingTask.__init__.numFulfilledStopCriteria (Python parameter)")=`2`*, *[numTrackedModes](#abaqus.Optimization.SizingTask.SizingTask "abaqus.Optimization.SizingTask.SizingTask.__init__.numTrackedModes (Python parameter)")=`5`*, *[objectiveFunctionDeltaStopCriteria](#abaqus.Optimization.SizingTask.SizingTask "abaqus.Optimization.SizingTask.SizingTask.__init__.objectiveFunctionDeltaStopCriteria (Python parameter)")=`0`*, *[stopCriteriaDesignCycle](#abaqus.Optimization.SizingTask.SizingTask "abaqus.Optimization.SizingTask.SizingTask.__init__.stopCriteriaDesignCycle (Python parameter)")=`4`*, *[thicknessMoveLimit](#abaqus.Optimization.SizingTask.SizingTask "abaqus.Optimization.SizingTask.SizingTask.__init__.thicknessMoveLimit (Python parameter)")=`0`*, *[thicknessUpdateStrategy](#abaqus.Optimization.SizingTask.SizingTask "abaqus.Optimization.SizingTask.SizingTask.__init__.thicknessUpdateStrategy (Python parameter)")=`abaqusConstants.NORMAL`*, *[groupOperator](#abaqus.Optimization.SizingTask.SizingTask "abaqus.Optimization.SizingTask.SizingTask.__init__.groupOperator (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingTask.py#L24-L249)[¶](#abaqus.Optimization.SizingTask.SizingTask "Permalink to this definition")
:   Bases: [`OptimizationTask`](#abaqus.Optimization.OptimizationTask.OptimizationTask "abaqus.Optimization.OptimizationTask.OptimizationTask (Python class) — Bases: OptimizationTaskBase")

    The SizingTask object defines a Sizing task. The SizingTask object is derived from the OptimizationTask
    object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name]
    ```

    Note

    Check [SizingTask on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingtaskpyc.htm?contextscope=all).

    Member Details:

    abaqusSensitivities : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `False`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingTask.py#L57-L59)[¶](#abaqus.Optimization.SizingTask.SizingTask.abaqusSensitivities "Permalink to this definition")
    :   A Boolean specifying whether to use Abaqus to compute the design responses and their
        sensitivities. The default value is False.

        New in version 2019: The `abaqusSensitivities` attribute was added.

    designResponses : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Optimization.DesignResponse.DesignResponse`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingTask.py#L36-L37)[¶](#abaqus.Optimization.SizingTask.SizingTask.designResponses "Permalink to this definition")
    :   A repository of DesignResponse objects.

    elementThicknessDeltaStopCriteria : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingTask.py#L61-L63)[¶](#abaqus.Optimization.SizingTask.SizingTask.elementThicknessDeltaStopCriteria "Permalink to this definition")
    :   A Float specifying the stop criteria based on the change in element thickness. The
        default value is 0.5 x 10⁻².

    freezeBoundaryConditionRegions : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingTask.py#L65-L67)[¶](#abaqus.Optimization.SizingTask.SizingTask.freezeBoundaryConditionRegions "Permalink to this definition")
    :   A Boolean specifying whether to exclude elements with boundary conditions from the
        optimization. The default value is OFF.

    freezeLoadRegions : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingTask.py#L69-L71)[¶](#abaqus.Optimization.SizingTask.SizingTask.freezeLoadRegions "Permalink to this definition")
    :   A Boolean specifying whether to exclude elements with loads and elements with loaded
        nodes from the optimization. The default value is ON.

    geometricRestrictions : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Optimization.GeometricRestriction.GeometricRestriction`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingTask.py#L45-L46)[¶](#abaqus.Optimization.SizingTask.SizingTask.geometricRestrictions "Permalink to this definition")
    :   A repository of GeometricRestriction objects.

    groupOperator : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingTask.py#L104-L106)[¶](#abaqus.Optimization.SizingTask.SizingTask.groupOperator "Permalink to this definition")
    :   A Boolean specifying whether the group in the design response will be evaluated using
        the existing algorithm or a new algorithm based on Abaqus sensitivities. The default
        value of False means that the existing algorithm will be used.

        New in version 2022: The `groupSensitivities` attribute was added.

    modeTrackingRegion : --is-rst--:py:class:`str` = `'MODEL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingTask.py#L73-L75)[¶](#abaqus.Optimization.SizingTask.SizingTask.modeTrackingRegion "Permalink to this definition")
    :   The SymbolicConstatnt MODEL or a Region object specifying the region to use for mode
        tracking. The default value is MODEL.

    numFulfilledStopCriteria : --is-rst--:py:class:`int` = `2`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingTask.py#L77-L78)[¶](#abaqus.Optimization.SizingTask.SizingTask.numFulfilledStopCriteria "Permalink to this definition")
    :   An Int specifying the number of stop criteria. The default value is 2.

    numTrackedModes : --is-rst--:py:class:`int` = `5`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingTask.py#L80-L81)[¶](#abaqus.Optimization.SizingTask.SizingTask.numTrackedModes "Permalink to this definition")
    :   An Int specifying the number of modes included in mode tracking. The default value is 5.

    objectiveFunctionDeltaStopCriteria : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingTask.py#L83-L85)[¶](#abaqus.Optimization.SizingTask.SizingTask.objectiveFunctionDeltaStopCriteria "Permalink to this definition")
    :   A Float specifying the stop criteria based on the change in objective function. The
        default value is 0.001.

    objectiveFunctions : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Optimization.ObjectiveFunction.ObjectiveFunction`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingTask.py#L39-L40)[¶](#abaqus.Optimization.SizingTask.SizingTask.objectiveFunctions "Permalink to this definition")
    :   A repository of ObjectiveFunction objects.

    optimizationConstraints : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Optimization.OptimizationConstraint.OptimizationConstraint`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingTask.py#L42-L43)[¶](#abaqus.Optimization.SizingTask.SizingTask.optimizationConstraints "Permalink to this definition")
    :   A repository of OptimizationConstraint objects.

    setValues(*[abaqusSensitivities](#abaqus.Optimization.SizingTask.SizingTask.setValues.abaqusSensitivities "abaqus.Optimization.SizingTask.SizingTask.setValues.abaqusSensitivities (Python parameter) — A Boolean specifying whether to use Abaqus to compute the design responses and their sensitivities.")=`True`*, *[elementThicknessDeltaStopCriteria](#abaqus.Optimization.SizingTask.SizingTask.setValues.elementThicknessDeltaStopCriteria "abaqus.Optimization.SizingTask.SizingTask.setValues.elementThicknessDeltaStopCriteria (Python parameter) — A Float specifying the stop criteria based on the change in element thickness.")=`0`*, *[freezeBoundaryConditionRegions](#abaqus.Optimization.SizingTask.SizingTask.setValues.freezeBoundaryConditionRegions "abaqus.Optimization.SizingTask.SizingTask.setValues.freezeBoundaryConditionRegions (Python parameter) — A Boolean specifying whether to exclude elements with boundary conditions from the optimization.")=`0`*, *[freezeLoadRegions](#abaqus.Optimization.SizingTask.SizingTask.setValues.freezeLoadRegions "abaqus.Optimization.SizingTask.SizingTask.setValues.freezeLoadRegions (Python parameter) — A Boolean specifying whether to exclude elements with loads and elements with loaded nodes from the optimization.")=`1`*, *[modeTrackingRegion](#abaqus.Optimization.SizingTask.SizingTask.setValues.modeTrackingRegion "abaqus.Optimization.SizingTask.SizingTask.setValues.modeTrackingRegion (Python parameter) — The SymbolicConstatnt MODEL or a Region object specifying the region to use for mode tracking.")=`abaqusConstants.MODEL`*, *[numFulfilledStopCriteria](#abaqus.Optimization.SizingTask.SizingTask.setValues.numFulfilledStopCriteria "abaqus.Optimization.SizingTask.SizingTask.setValues.numFulfilledStopCriteria (Python parameter) — An Int specifying the number of stop criteria.")=`2`*, *[numTrackedModes](#abaqus.Optimization.SizingTask.SizingTask.setValues.numTrackedModes "abaqus.Optimization.SizingTask.SizingTask.setValues.numTrackedModes (Python parameter) — An Int specifying the number of modes included in mode tracking.")=`5`*, *[objectiveFunctionDeltaStopCriteria](#abaqus.Optimization.SizingTask.SizingTask.setValues.objectiveFunctionDeltaStopCriteria "abaqus.Optimization.SizingTask.SizingTask.setValues.objectiveFunctionDeltaStopCriteria (Python parameter) — A Float specifying the stop criteria based on the change in objective function.")=`0`*, *[stopCriteriaDesignCycle](#abaqus.Optimization.SizingTask.SizingTask.setValues.stopCriteriaDesignCycle "abaqus.Optimization.SizingTask.SizingTask.setValues.stopCriteriaDesignCycle (Python parameter) — An Int specifying the first design cycle used to evaluate convergence criteria.")=`4`*, *[thicknessMoveLimit](#abaqus.Optimization.SizingTask.SizingTask.setValues.thicknessMoveLimit "abaqus.Optimization.SizingTask.SizingTask.setValues.thicknessMoveLimit (Python parameter) — A Float specifying the maximum change in thickness per design cycle.")=`0`*, *[thicknessUpdateStrategy](#abaqus.Optimization.SizingTask.SizingTask.setValues.thicknessUpdateStrategy "abaqus.Optimization.SizingTask.SizingTask.setValues.thicknessUpdateStrategy (Python parameter) — A SymbolicConstant specifying the strategy for how the thickness is updated in the method of moving asymptotes.")=`abaqusConstants.NORMAL`*, *[groupOperator](#abaqus.Optimization.SizingTask.SizingTask.setValues.groupOperator "abaqus.Optimization.SizingTask.SizingTask.setValues.groupOperator (Python parameter) — A Boolean specifying whether the group in the design response will be evaluated using the existing algorithm or a new algorithm based on Abaqus sensitivities.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingTask.py#L186-L249)[¶](#abaqus.Optimization.SizingTask.SizingTask.setValues "Permalink to this definition")
    :   This method modifies the SizingTask object.

        Note

        Check [SizingTask.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sizingtaskpyc.htm?contextscope=all#simaker-sizingtasksetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.SizingTask.SizingTask.setValues-parameters "Permalink to this headline")
        :   abaqusSensitivities=`True`[¶](#abaqus.Optimization.SizingTask.SizingTask.setValues.abaqusSensitivities "Permalink to this definition")
            :   A Boolean specifying whether to use Abaqus to compute the design responses and their
                sensitivities. The default value is True.

                New in version 2019: The `abaqusSensitivities` argument was added.

            elementThicknessDeltaStopCriteria=`0`[¶](#abaqus.Optimization.SizingTask.SizingTask.setValues.elementThicknessDeltaStopCriteria "Permalink to this definition")
            :   A Float specifying the stop criteria based on the change in element thickness. The
                default value is 0.5 x 10⁻².

            freezeBoundaryConditionRegions=`0`[¶](#abaqus.Optimization.SizingTask.SizingTask.setValues.freezeBoundaryConditionRegions "Permalink to this definition")
            :   A Boolean specifying whether to exclude elements with boundary conditions from the
                optimization. The default value is OFF.

            freezeLoadRegions=`1`[¶](#abaqus.Optimization.SizingTask.SizingTask.setValues.freezeLoadRegions "Permalink to this definition")
            :   A Boolean specifying whether to exclude elements with loads and elements with loaded
                nodes from the optimization. The default value is ON.

            modeTrackingRegion=`abaqusConstants.MODEL`[¶](#abaqus.Optimization.SizingTask.SizingTask.setValues.modeTrackingRegion "Permalink to this definition")
            :   The SymbolicConstatnt MODEL or a Region object specifying the region to use for mode
                tracking. The default value is MODEL.

            numFulfilledStopCriteria=`2`[¶](#abaqus.Optimization.SizingTask.SizingTask.setValues.numFulfilledStopCriteria "Permalink to this definition")
            :   An Int specifying the number of stop criteria. The default value is 2.

            numTrackedModes=`5`[¶](#abaqus.Optimization.SizingTask.SizingTask.setValues.numTrackedModes "Permalink to this definition")
            :   An Int specifying the number of modes included in mode tracking. The default value is 5.

            objectiveFunctionDeltaStopCriteria=`0`[¶](#abaqus.Optimization.SizingTask.SizingTask.setValues.objectiveFunctionDeltaStopCriteria "Permalink to this definition")
            :   A Float specifying the stop criteria based on the change in objective function. The
                default value is 0.001.

            stopCriteriaDesignCycle=`4`[¶](#abaqus.Optimization.SizingTask.SizingTask.setValues.stopCriteriaDesignCycle "Permalink to this definition")
            :   An Int specifying the first design cycle used to evaluate convergence criteria. The
                default value is 4.

            thicknessMoveLimit=`0`[¶](#abaqus.Optimization.SizingTask.SizingTask.setValues.thicknessMoveLimit "Permalink to this definition")
            :   A Float specifying the maximum change in thickness per design cycle. The default value
                is 0.25.

            thicknessUpdateStrategy=`abaqusConstants.NORMAL`[¶](#abaqus.Optimization.SizingTask.SizingTask.setValues.thicknessUpdateStrategy "Permalink to this definition")
            :   A SymbolicConstant specifying the strategy for how the thickness is updated in the
                method of moving asymptotes. Possible values are NORMAL, CONSERVATIVE, and AGGRESSIVE.
                The default value is NORMAL.

            groupOperator=`0`[¶](#abaqus.Optimization.SizingTask.SizingTask.setValues.groupOperator "Permalink to this definition")
            :   A Boolean specifying whether the group in the design response will be evaluated using
                the existing algorithm or a new algorithm based on Abaqus sensitivities. The default
                value of False means that the existing algorithm will be used.

                New in version 2022: The `groupOperator` argument was added.

    stopConditions : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Optimization.StopCondition.StopCondition`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingTask.py#L48-L49)[¶](#abaqus.Optimization.SizingTask.SizingTask.stopConditions "Permalink to this definition")
    :   A repository of StopCondition objects.

    stopCriteriaDesignCycle : --is-rst--:py:class:`int` = `4`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingTask.py#L87-L89)[¶](#abaqus.Optimization.SizingTask.SizingTask.stopCriteriaDesignCycle "Permalink to this definition")
    :   An Int specifying the first design cycle used to evaluate convergence criteria. The
        default value is 4.

    thicknessMoveLimit : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingTask.py#L91-L93)[¶](#abaqus.Optimization.SizingTask.SizingTask.thicknessMoveLimit "Permalink to this definition")
    :   A Float specifying the maximum change in thickness per design cycle. The default value
        is 0.25.

    thicknessUpdateStrategy : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'NORMAL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/SizingTask.py#L95-L98)[¶](#abaqus.Optimization.SizingTask.SizingTask.thicknessUpdateStrategy "Permalink to this definition")
    :   A SymbolicConstant specifying the strategy for how the thickness is updated in the
        method of moving asymptotes. Possible values are NORMAL, CONSERVATIVE, and AGGRESSIVE.
        The default value is NORMAL.

*class* TopologyTask(*[name](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.name (Python parameter)")*, *[abaqusSensitivities](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.abaqusSensitivities (Python parameter)")=`False`*, *[algorithm](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.algorithm (Python parameter)")=`abaqusConstants.GENERAL_OPTIMIZATION`*, *[densityMoveLimit](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.densityMoveLimit (Python parameter)")=`0`*, *[densityUpdateStrategy](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.densityUpdateStrategy (Python parameter)")=`abaqusConstants.NORMAL`*, *[elementDensityDeltaStopCriteria](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.elementDensityDeltaStopCriteria (Python parameter)")=`0`*, *[filterRadius](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.filterRadius (Python parameter)")=`None`*, *[firstCycleDeletedVolume](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.firstCycleDeletedVolume (Python parameter)")=`5`*, *[firstCycleDeletedVolumeTechnique](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.firstCycleDeletedVolumeTechnique (Python parameter)")=`0`*, *[freezeBoundaryConditionRegions](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.freezeBoundaryConditionRegions (Python parameter)")=`0`*, *[freezeLoadRegions](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.freezeLoadRegions (Python parameter)")=`1`*, *[frequencySpectrumWeight](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.frequencySpectrumWeight (Python parameter)")=`6`*, *[initialDensity](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.initialDensity (Python parameter)")=`abaqusConstants.DEFAULT`*, *[materialInterpolationPenalty](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.materialInterpolationPenalty (Python parameter)")=`3`*, *[materialInterpolationTechnique](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.materialInterpolationTechnique (Python parameter)")=`abaqusConstants.DEFAULT`*, *[maxDensity](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.maxDensity (Python parameter)")=`1`*, *[minDensity](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.minDensity (Python parameter)")=`None`*, *[modeTrackingRegion](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.modeTrackingRegion (Python parameter)")=`abaqusConstants.MODEL`*, *[numDesignCycles](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.numDesignCycles (Python parameter)")=`15`*, *[numFulfilledStopCriteria](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.numFulfilledStopCriteria (Python parameter)")=`2`*, *[numTrackedModes](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.numTrackedModes (Python parameter)")=`5`*, *[objectiveFunctionDeltaStopCriteria](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.objectiveFunctionDeltaStopCriteria (Python parameter)")=`None`*, *[region](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.region (Python parameter)")=`abaqusConstants.MODEL`*, *[softDeletionMethod](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.softDeletionMethod (Python parameter)")=`abaqusConstants.STANDARD`*, *[softDeletionRadius](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.softDeletionRadius (Python parameter)")=`0`*, *[softDeletionRegion](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.softDeletionRegion (Python parameter)")=`None`*, *[softDeletionThreshold](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.softDeletionThreshold (Python parameter)")=`None`*, *[stepSize](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.stepSize (Python parameter)")=`abaqusConstants.MEDIUM`*, *[stiffnessMassDamping](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.stiffnessMassDamping (Python parameter)")=`abaqusConstants.AVERAGE_EDGE_LENGTH`*, *[stopCriteriaDesignCycle](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.stopCriteriaDesignCycle (Python parameter)")=`4`*, *[structuralMassDamping](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.structuralMassDamping (Python parameter)")=`None`*, *[viscousMassDamping](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.viscousMassDamping (Python parameter)")=`None`*, *[viscousStiffnessDamping](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.viscousStiffnessDamping (Python parameter)")=`None`*, *[groupOperator](#abaqus.Optimization.TopologyTask.TopologyTask "abaqus.Optimization.TopologyTask.TopologyTask.__init__.groupOperator (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L31-L555)[¶](#abaqus.Optimization.TopologyTask.TopologyTask "Permalink to this definition")
:   Bases: [`OptimizationTask`](#abaqus.Optimization.OptimizationTask.OptimizationTask "abaqus.Optimization.OptimizationTask.OptimizationTask (Python class) — Bases: OptimizationTaskBase")

    The TopologyTask object defines a topology task. The TopologyTask object is derived from the
    OptimizationTask object.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name]
    ```

    Note

    Check [TopologyTask on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologytaskpyc.htm?contextscope=all).

    Member Details:

    abaqusSensitivities : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `False`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L64-L66)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.abaqusSensitivities "Permalink to this definition")
    :   A Boolean specifying whether to use Abaqus to compute the design responses and their
        sensitivities. The default value is False.

        New in version 2019: The `abaqusSensitivities` attribute was added.

    algorithm : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'GENERAL_OPTIMIZATION'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L68-L71)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.algorithm "Permalink to this definition")
    :   A SymbolicConstant specifying the optimization task algorithm. Possible values are
        GENERAL\_OPTIMIZATION and CONDITION\_BASED\_OPTIMIZATION. The default value is
        GENERAL\_OPTIMIZATION.

    densityMoveLimit : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L73-L75)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.densityMoveLimit "Permalink to this definition")
    :   A Float specifying the maximum density change per design cycle. The default value is
        0.25.

    densityUpdateStrategy : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'NORMAL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L77-L80)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.densityUpdateStrategy "Permalink to this definition")
    :   A SymbolicConstant specifying the strategy for how the densities are updated in the
        method of moving asymptotes. Possible values are NORMAL, CONSERVATIVE, and AGGRESSIVE.
        The default value is NORMAL.

    designResponses : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Optimization.DesignResponse.DesignResponse`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L43-L44)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.designResponses "Permalink to this definition")
    :   A repository of DesignResponse objects.

    elementDensityDeltaStopCriteria : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L82-L84)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.elementDensityDeltaStopCriteria "Permalink to this definition")
    :   A Float specifying the stop criteria based upon the change in element densities. The
        default value is 0.5x10⁻².

    filterRadius : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L86-L88)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.filterRadius "Permalink to this definition")
    :   None or a Float specifying the mesh filter radius for mesh independence and minimum
        size. The default value is None.

    firstCycleDeletedVolume : --is-rst--:py:class:`float` = `5`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L90-L92)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.firstCycleDeletedVolume "Permalink to this definition")
    :   A Float specifying the volume that can be removed immediately in the first design cycle.
        The default value is 5.0.

    firstCycleDeletedVolumeTechnique : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`, :py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L94-L97)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.firstCycleDeletedVolumeTechnique "Permalink to this definition")
    :   A SymbolicConstant specifying the method of quantifying volume that can be removed
        immediately in the first design cycle. Possible values are OFF, PERCENTAGE, and
        ABSOLUTE. The default value is OFF.

    freezeBoundaryConditionRegions : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L99-L101)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.freezeBoundaryConditionRegions "Permalink to this definition")
    :   A Boolean specifying whether to exclude elements with boundary conditions from the
        optimization. The default value is OFF.

    freezeLoadRegions : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L103-L105)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.freezeLoadRegions "Permalink to this definition")
    :   A Boolean specifying whether to exclude elements with loads and elements with loaded
        nodes from the optimization. The default value is ON.

    frequencySpectrumWeight : --is-rst--:py:class:`float` = `6`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L107-L109)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.frequencySpectrumWeight "Permalink to this definition")
    :   A Float specifying the weighting factor for frequency spectrum peaks. The default value
        is 6.0.

    geometricRestrictions : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Optimization.GeometricRestriction.GeometricRestriction`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L52-L53)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.geometricRestrictions "Permalink to this definition")
    :   A repository of GeometricRestriction objects.

    groupOperator : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L206-L208)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.groupOperator "Permalink to this definition")
    :   A Boolean specifying whether the group in the design response will be evaluated using
        the existing algorithm or a new algorithm based on Abaqus sensitivities. The default
        value of False means that the existing algorithm will be used.

        New in version 2022: The `groupSensitivities` attribute was added.

    initialDensity : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'DEFAULT'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L111-L113)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.initialDensity "Permalink to this definition")
    :   A SymbolicConstant specifying the Optimization product default or a float specifying the
        initial density. The default value is DEFAULT.

    materialInterpolationPenalty : --is-rst--:py:class:`float` = `3`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L115-L117)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.materialInterpolationPenalty "Permalink to this definition")
    :   A Float specifying the penalty factor for the material interpolation technique. The
        default value is 3.0.

    materialInterpolationTechnique : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'DEFAULT'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L119-L123)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.materialInterpolationTechnique "Permalink to this definition")
    :   optimization product
        default, solid isotropic material with penalization, or rational approximation of
        material properties. Possible values are DEFAULT, SIMP, and RAMP. The default value is
        DEFAULT.

        Type:[¶](#abaqus.Optimization.TopologyTask.TopologyTask.materialInterpolationTechnique-type "Permalink to this headline")
        :   A SymbolicConstant specifying the material interpolation technique

    maxDensity : --is-rst--:py:class:`float` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L125-L126)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.maxDensity "Permalink to this definition")
    :   A Float specifying the maximum density in the density update. The default value is 1.0.

    minDensity : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L128-L129)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.minDensity "Permalink to this definition")
    :   A Float specifying the minimum density in the density update. The default value is 10⁻³.

    modeTrackingRegion : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MODEL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L131-L133)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.modeTrackingRegion "Permalink to this definition")
    :   The SymbolicConstant MODEL or a Region object specifying the region to use for mode
        tracking. The default value is MODEL.

    numDesignCycles : --is-rst--:py:class:`int` = `15`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L135-L137)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.numDesignCycles "Permalink to this definition")
    :   An Int specifying the number of design cycles permitted when **stepSize** is DYNAMIC. The
        default value is 15.

    numFulfilledStopCriteria : --is-rst--:py:class:`int` = `2`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L139-L140)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.numFulfilledStopCriteria "Permalink to this definition")
    :   An Int specifying the number of stop criteria. The default value is 2.

    numTrackedModes : --is-rst--:py:class:`int` = `5`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L142-L143)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.numTrackedModes "Permalink to this definition")
    :   An Int specifying the number of modes included in mode tracking. The default value is 5.

    objectiveFunctionDeltaStopCriteria : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L145-L147)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.objectiveFunctionDeltaStopCriteria "Permalink to this definition")
    :   A Float specifying the stop criteria based on the change in objective function. The
        default value is 10⁻³.

    objectiveFunctions : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Optimization.ObjectiveFunction.ObjectiveFunction`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L46-L47)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.objectiveFunctions "Permalink to this definition")
    :   A repository of ObjectiveFunction objects.

    optimizationConstraints : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Optimization.OptimizationConstraint.OptimizationConstraint`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L49-L50)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.optimizationConstraints "Permalink to this definition")
    :   A repository of OptimizationConstraint objects.

    region : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MODEL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L149-L151)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.region "Permalink to this definition")
    :   The SymbolicConstant MODEL or a Region object specifying the region to which the
        optimization task is applied. The default value is MODEL.

    setValues(*[abaqusSensitivities](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.abaqusSensitivities "abaqus.Optimization.TopologyTask.TopologyTask.setValues.abaqusSensitivities (Python parameter) — A Boolean specifying whether to use Abaqus to compute the design responses and their sensitivities.")=`True`*, *[algorithm](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.algorithm "abaqus.Optimization.TopologyTask.TopologyTask.setValues.algorithm (Python parameter) — A SymbolicConstant specifying the optimization task algorithm.")=`abaqusConstants.GENERAL_OPTIMIZATION`*, *[densityMoveLimit](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.densityMoveLimit "abaqus.Optimization.TopologyTask.TopologyTask.setValues.densityMoveLimit (Python parameter) — A Float specifying the maximum density change per design cycle.")=`0`*, *[densityUpdateStrategy](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.densityUpdateStrategy "abaqus.Optimization.TopologyTask.TopologyTask.setValues.densityUpdateStrategy (Python parameter) — A SymbolicConstant specifying the strategy for how the densities are updated in the method of moving asymptotes.")=`abaqusConstants.NORMAL`*, *[elementDensityDeltaStopCriteria](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.elementDensityDeltaStopCriteria "abaqus.Optimization.TopologyTask.TopologyTask.setValues.elementDensityDeltaStopCriteria (Python parameter) — A Float specifying the stop criteria based upon the change in element densities.")=`0`*, *[filterRadius](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.filterRadius "abaqus.Optimization.TopologyTask.TopologyTask.setValues.filterRadius (Python parameter) — None or a Float specifying the mesh filter radius for mesh independence and minimum size.")=`None`*, *[firstCycleDeletedVolume](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.firstCycleDeletedVolume "abaqus.Optimization.TopologyTask.TopologyTask.setValues.firstCycleDeletedVolume (Python parameter) — A Float specifying the volume that can be removed immediately in the first design cycle. The default value is 5.0.")=`5`*, *[firstCycleDeletedVolumeTechnique](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.firstCycleDeletedVolumeTechnique "abaqus.Optimization.TopologyTask.TopologyTask.setValues.firstCycleDeletedVolumeTechnique (Python parameter) — A SymbolicConstant specifying the method of quantifying volume that can be removed immediately in the first design cycle.")=`0`*, *[freezeBoundaryConditionRegions](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.freezeBoundaryConditionRegions "abaqus.Optimization.TopologyTask.TopologyTask.setValues.freezeBoundaryConditionRegions (Python parameter) — A Boolean specifying whether to exclude elements with boundary conditions from the optimization.")=`0`*, *[freezeLoadRegions](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.freezeLoadRegions "abaqus.Optimization.TopologyTask.TopologyTask.setValues.freezeLoadRegions (Python parameter) — A Boolean specifying whether to exclude elements with loads and elements with loaded nodes from the optimization.")=`1`*, *[frequencySpectrumWeight](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.frequencySpectrumWeight "abaqus.Optimization.TopologyTask.TopologyTask.setValues.frequencySpectrumWeight (Python parameter) — A Float specifying the weighting factor for frequency spectrum peaks.")=`6`*, *[initialDensity](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.initialDensity "abaqus.Optimization.TopologyTask.TopologyTask.setValues.initialDensity (Python parameter) — A SymbolicConstant specifying the Optimization product default or a float specifying the initial density.")=`abaqusConstants.DEFAULT`*, *[materialInterpolationPenalty](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.materialInterpolationPenalty "abaqus.Optimization.TopologyTask.TopologyTask.setValues.materialInterpolationPenalty (Python parameter) — A Float specifying the penalty factor for the material interpolation technique.")=`3`*, *[materialInterpolationTechnique](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.materialInterpolationTechnique "abaqus.Optimization.TopologyTask.TopologyTask.setValues.materialInterpolationTechnique (Python parameter) — A SymbolicConstant specifying the material interpolation technique: optimization product default, solid isotropic material with penalization, or rational approximation of material properties.")=`abaqusConstants.DEFAULT`*, *[maxDensity](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.maxDensity "abaqus.Optimization.TopologyTask.TopologyTask.setValues.maxDensity (Python parameter) — A Float specifying the maximum density in the density update.")=`1`*, *[minDensity](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.minDensity "abaqus.Optimization.TopologyTask.TopologyTask.setValues.minDensity (Python parameter) — A Float specifying the minimum density in the density update.")=`None`*, *[modeTrackingRegion](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.modeTrackingRegion "abaqus.Optimization.TopologyTask.TopologyTask.setValues.modeTrackingRegion (Python parameter) — The SymbolicConstant MODEL or a Region object specifying the region to use for mode tracking.")=`abaqusConstants.MODEL`*, *[numDesignCycles](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.numDesignCycles "abaqus.Optimization.TopologyTask.TopologyTask.setValues.numDesignCycles (Python parameter) — An Int specifying the number of design cycles permitted when stepSize is DYNAMIC.")=`15`*, *[numFulfilledStopCriteria](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.numFulfilledStopCriteria "abaqus.Optimization.TopologyTask.TopologyTask.setValues.numFulfilledStopCriteria (Python parameter) — An Int specifying the number of stop criteria.")=`2`*, *[numTrackedModes](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.numTrackedModes "abaqus.Optimization.TopologyTask.TopologyTask.setValues.numTrackedModes (Python parameter) — An Int specifying the number of modes included in mode tracking.")=`5`*, *[objectiveFunctionDeltaStopCriteria](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.objectiveFunctionDeltaStopCriteria "abaqus.Optimization.TopologyTask.TopologyTask.setValues.objectiveFunctionDeltaStopCriteria (Python parameter) — A Float specifying the stop criteria based on the change in objective function.")=`None`*, *[region](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.region "abaqus.Optimization.TopologyTask.TopologyTask.setValues.region (Python parameter) — The SymbolicConstant MODEL or a Region object specifying the region to which the optimization task is applied.")=`abaqusConstants.MODEL`*, *[softDeletionMethod](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.softDeletionMethod "abaqus.Optimization.TopologyTask.TopologyTask.setValues.softDeletionMethod (Python parameter) — A SymbolicConstant specifying the method used when softDeletionRegion is specified. The STANDARD method avoids creating disconnected regions.")=`abaqusConstants.STANDARD`*, *[softDeletionRadius](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.softDeletionRadius "abaqus.Optimization.TopologyTask.TopologyTask.setValues.softDeletionRadius (Python parameter) — A Float specifying the radius to use when considering neighboring soft elements to delete.")=`0`*, *[softDeletionRegion](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.softDeletionRegion "abaqus.Optimization.TopologyTask.TopologyTask.setValues.softDeletionRegion (Python parameter) — None or a Region object specifying the region in which the soft elements should be deleted during optimization.")=`None`*, *[softDeletionThreshold](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.softDeletionThreshold "abaqus.Optimization.TopologyTask.TopologyTask.setValues.softDeletionThreshold (Python parameter) — A Float specifying the relative material density value used to identify soft elements. Those with values below the threshold are considered for removal.")=`None`*, *[stepSize](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.stepSize "abaqus.Optimization.TopologyTask.TopologyTask.setValues.stepSize (Python parameter) — A SymbolicConstant specifying the size of the increment for volume modification. Possible values are DYNAMIC, VERY_SMALL, SMALL, MODERATE, MEDIUM, and LARGE.")=`abaqusConstants.MEDIUM`*, *[stiffnessMassDamping](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.stiffnessMassDamping "abaqus.Optimization.TopologyTask.TopologyTask.setValues.stiffnessMassDamping (Python parameter) — The SymbolicConstant AVERAGE_EDGE_LENGTH or a Float specifying the stiffness mass damping for the task region.")=`abaqusConstants.AVERAGE_EDGE_LENGTH`*, *[stopCriteriaDesignCycle](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.stopCriteriaDesignCycle "abaqus.Optimization.TopologyTask.TopologyTask.setValues.stopCriteriaDesignCycle (Python parameter) — An Int specifying the first design cycle used to evaluate convergence criteria.")=`4`*, *[structuralMassDamping](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.structuralMassDamping "abaqus.Optimization.TopologyTask.TopologyTask.setValues.structuralMassDamping (Python parameter) — None or a Float specifying the structural mass damping for the task region.")=`None`*, *[viscousMassDamping](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.viscousMassDamping "abaqus.Optimization.TopologyTask.TopologyTask.setValues.viscousMassDamping (Python parameter) — None or a Float specifying the viscous mass damping for the task region.")=`None`*, *[viscousStiffnessDamping](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.viscousStiffnessDamping "abaqus.Optimization.TopologyTask.TopologyTask.setValues.viscousStiffnessDamping (Python parameter) — None or a Float specifying the viscous stiffness damping for the task region.")=`None`*, *[groupOperator](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.groupOperator "abaqus.Optimization.TopologyTask.TopologyTask.setValues.groupOperator (Python parameter) — A Boolean specifying whether the group in the design response will be evaluated using the existing algorithm or a new algorithm based on Abaqus sensitivities.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L390-L555)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues "Permalink to this definition")
    :   This method modifies the TopologyTask object.

        Note

        Check [TopologyTask.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-topologytaskpyc.htm?contextscope=all#simaker-topologytasksetvaluespyc).

        Parameters:[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues-parameters "Permalink to this headline")
        :   abaqusSensitivities=`True`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.abaqusSensitivities "Permalink to this definition")
            :   A Boolean specifying whether to use Abaqus to compute the design responses and their
                sensitivities. The default value is True.

                New in version 2019: The `abaqusSensitivities` argument was added.

            algorithm=`abaqusConstants.GENERAL_OPTIMIZATION`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.algorithm "Permalink to this definition")
            :   A SymbolicConstant specifying the optimization task algorithm. Possible values are
                GENERAL\_OPTIMIZATION and CONDITION\_BASED\_OPTIMIZATION. The default value is
                GENERAL\_OPTIMIZATION.

            densityMoveLimit=`0`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.densityMoveLimit "Permalink to this definition")
            :   A Float specifying the maximum density change per design cycle. The default value is
                0.25.

            densityUpdateStrategy=`abaqusConstants.NORMAL`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.densityUpdateStrategy "Permalink to this definition")
            :   A SymbolicConstant specifying the strategy for how the densities are updated in the
                method of moving asymptotes. Possible values are NORMAL, CONSERVATIVE, and AGGRESSIVE.
                The default value is NORMAL.

            elementDensityDeltaStopCriteria=`0`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.elementDensityDeltaStopCriteria "Permalink to this definition")
            :   A Float specifying the stop criteria based upon the change in element densities. The
                default value is 0.5x10⁻².

            filterRadius=`None`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.filterRadius "Permalink to this definition")
            :   None or a Float specifying the mesh filter radius for mesh independence and minimum
                size. The default value is None.

            firstCycleDeletedVolume=`5`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.firstCycleDeletedVolume "Permalink to this definition")
            :   A Float specifying the volume that can be removed immediately in the first design cycle.
                The default value is 5.0.

            firstCycleDeletedVolumeTechnique=`0`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.firstCycleDeletedVolumeTechnique "Permalink to this definition")
            :   A SymbolicConstant specifying the method of quantifying volume that can be removed
                immediately in the first design cycle. Possible values are OFF, PERCENTAGE, and
                ABSOLUTE. The default value is OFF.

            freezeBoundaryConditionRegions=`0`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.freezeBoundaryConditionRegions "Permalink to this definition")
            :   A Boolean specifying whether to exclude elements with boundary conditions from the
                optimization. The default value is OFF.

            freezeLoadRegions=`1`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.freezeLoadRegions "Permalink to this definition")
            :   A Boolean specifying whether to exclude elements with loads and elements with loaded
                nodes from the optimization. The default value is ON.

            frequencySpectrumWeight=`6`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.frequencySpectrumWeight "Permalink to this definition")
            :   A Float specifying the weighting factor for frequency spectrum peaks. The default value
                is 6.0.

            initialDensity=`abaqusConstants.DEFAULT`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.initialDensity "Permalink to this definition")
            :   A SymbolicConstant specifying the Optimization product default or a float specifying the
                initial density. The default value is DEFAULT.

            materialInterpolationPenalty=`3`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.materialInterpolationPenalty "Permalink to this definition")
            :   A Float specifying the penalty factor for the material interpolation technique. The
                default value is 3.0.

            materialInterpolationTechnique=`abaqusConstants.DEFAULT`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.materialInterpolationTechnique "Permalink to this definition")
            :   A SymbolicConstant specifying the material interpolation technique: optimization product
                default, solid isotropic material with penalization, or rational approximation of
                material properties. Possible values are DEFAULT, SIMP, and RAMP. The default value is
                DEFAULT.

            maxDensity=`1`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.maxDensity "Permalink to this definition")
            :   A Float specifying the maximum density in the density update. The default value is 1.0.

            minDensity=`None`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.minDensity "Permalink to this definition")
            :   A Float specifying the minimum density in the density update. The default value is 10⁻³.

            modeTrackingRegion=`abaqusConstants.MODEL`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.modeTrackingRegion "Permalink to this definition")
            :   The SymbolicConstant MODEL or a Region object specifying the region to use for mode
                tracking. The default value is MODEL.

            numDesignCycles=`15`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.numDesignCycles "Permalink to this definition")
            :   An Int specifying the number of design cycles permitted when **stepSize** is DYNAMIC. The
                default value is 15.

            numFulfilledStopCriteria=`2`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.numFulfilledStopCriteria "Permalink to this definition")
            :   An Int specifying the number of stop criteria. The default value is 2.

            numTrackedModes=`5`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.numTrackedModes "Permalink to this definition")
            :   An Int specifying the number of modes included in mode tracking. The default value is 5.

            objectiveFunctionDeltaStopCriteria=`None`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.objectiveFunctionDeltaStopCriteria "Permalink to this definition")
            :   A Float specifying the stop criteria based on the change in objective function. The
                default value is 10⁻³.

            region=`abaqusConstants.MODEL`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.region "Permalink to this definition")
            :   The SymbolicConstant MODEL or a Region object specifying the region to which the
                optimization task is applied. The default value is MODEL.

            softDeletionMethod=`abaqusConstants.STANDARD`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.softDeletionMethod "Permalink to this definition")
            :   A SymbolicConstant specifying the method used when **softDeletionRegion** is specified.
                The STANDARD method avoids creating disconnected regions. The AGGRESSIVE method only
                considers the **softDeletionThreshold**. The MAX\_SHEAR\_STRAIN, MAX\_ELASTOPLASTIC\_STRAIN
                and VOLUME\_COMPRESSION methods do not need the **softDeletionRadius**. Possible values are
                STANDARD, AGGRESSIVE, MAX\_SHEAR\_STRAIN, MIN\_PRINCIPAL\_STRAIN, MAX\_ELASTOPLASTIC\_STRAIN
                and VOLUME\_COMPRESSION. The default value is STANDARD.

            softDeletionRadius=`0`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.softDeletionRadius "Permalink to this definition")
            :   A Float specifying the radius to use when considering neighboring soft elements to
                delete. The default value is 0.0.

            softDeletionRegion=`None`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.softDeletionRegion "Permalink to this definition")
            :   None or a Region object specifying the region in which the soft elements should be
                deleted during optimization. The default value is None.

            softDeletionThreshold=`None`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.softDeletionThreshold "Permalink to this definition")
            :   A Float specifying the relative material density value used to identify soft elements.
                Those with values below the threshold are considered for removal. For STANDARD and
                AGGRESSIVE methods positive values are accepted and the default value is 0.05. For
                MAX\_SHEAR\_STRAIN and MAX\_ELASTOPLASTIC\_STRAIN methods positive values are accepted
                whereas for MIN\_PRINCIPAL\_STRAIN and VOLUME\_COMPRESSION methods negative values are
                accepted.

            stepSize=`abaqusConstants.MEDIUM`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.stepSize "Permalink to this definition")
            :   A SymbolicConstant specifying the size of the increment for volume modification.
                Possible values are DYNAMIC, VERY\_SMALL, SMALL, MODERATE, MEDIUM, and LARGE. The default
                value is MEDIUM.

            stiffnessMassDamping=`abaqusConstants.AVERAGE_EDGE_LENGTH`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.stiffnessMassDamping "Permalink to this definition")
            :   The SymbolicConstant AVERAGE\_EDGE\_LENGTH or a Float specifying the stiffness mass
                damping for the task region. The default value is AVERAGE\_EDGE\_LENGTH.

            stopCriteriaDesignCycle=`4`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.stopCriteriaDesignCycle "Permalink to this definition")
            :   An Int specifying the first design cycle used to evaluate convergence criteria. The
                default value is 4.

            structuralMassDamping=`None`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.structuralMassDamping "Permalink to this definition")
            :   None or a Float specifying the structural mass damping for the task region. The default
                value is None.

            viscousMassDamping=`None`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.viscousMassDamping "Permalink to this definition")
            :   None or a Float specifying the viscous mass damping for the task region. The default
                value is None.

            viscousStiffnessDamping=`None`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.viscousStiffnessDamping "Permalink to this definition")
            :   None or a Float specifying the viscous stiffness damping for the task region. The
                default value is None.

            groupOperator=`0`[¶](#abaqus.Optimization.TopologyTask.TopologyTask.setValues.groupOperator "Permalink to this definition")
            :   A Boolean specifying whether the group in the design response will be evaluated using
                the existing algorithm or a new algorithm based on Abaqus sensitivities. The default
                value of False means that the existing algorithm will be used.

                New in version 2022: The `groupOperator` argument was added.

    softDeletionMethod : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'STANDARD'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L153-L159)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.softDeletionMethod "Permalink to this definition")
    :   A SymbolicConstant specifying the method used when **softDeletionRegion** is specified.
        The STANDARD method avoids creating disconnected regions. The AGGRESSIVE method only
        considers the **softDeletionThreshold**. The MAX\_SHEAR\_STRAIN, MAX\_ELASTOPLASTIC\_STRAIN
        and VOLUME\_COMPRESSION methods do not need the **softDeletionRadius**. Possible values are
        STANDARD, AGGRESSIVE, MAX\_SHEAR\_STRAIN, MIN\_PRINCIPAL\_STRAIN, MAX\_ELASTOPLASTIC\_STRAIN
        and VOLUME\_COMPRESSION. The default value is STANDARD.

    softDeletionRadius : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L161-L163)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.softDeletionRadius "Permalink to this definition")
    :   A Float specifying the radius to use when considering neighboring soft elements to
        delete. The default value is 0.0.

    softDeletionRegion : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L165-L167)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.softDeletionRegion "Permalink to this definition")
    :   None or a Region object specifying the region in which the soft elements should be
        deleted during optimization. The default value is None.

    softDeletionThreshold : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L169-L175)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.softDeletionThreshold "Permalink to this definition")
    :   A Float specifying the relative material density value used to identify soft elements.
        Those with values below the threshold are considered for removal. For STANDARD and
        AGGRESSIVE methods positive values are accepted and the default value is 0.05. For
        MAX\_SHEAR\_STRAIN and MAX\_ELASTOPLASTIC\_STRAIN methods positive values are accepted
        whereas for MIN\_PRINCIPAL\_STRAIN and VOLUME\_COMPRESSION methods negative values are
        accepted.

    stepSize : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'MEDIUM'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L177-L180)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.stepSize "Permalink to this definition")
    :   A SymbolicConstant specifying the size of the increment for volume modification.
        Possible values are DYNAMIC, VERY\_SMALL, SMALL, MODERATE, MEDIUM, and LARGE. The default
        value is MEDIUM.

    stiffnessMassDamping : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`, :py:class:`float`] = `'AVERAGE_EDGE_LENGTH'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L182-L184)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.stiffnessMassDamping "Permalink to this definition")
    :   The SymbolicConstant AVERAGE\_EDGE\_LENGTH or a Float specifying the stiffness mass
        damping for the task region. The default value is AVERAGE\_EDGE\_LENGTH.

    stopConditions : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Optimization.StopCondition.StopCondition`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L55-L56)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.stopConditions "Permalink to this definition")
    :   A repository of StopCondition objects.

    stopCriteriaDesignCycle : --is-rst--:py:class:`int` = `4`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L186-L188)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.stopCriteriaDesignCycle "Permalink to this definition")
    :   An Int specifying the first design cycle used to evaluate convergence criteria. The
        default value is 4.

    structuralMassDamping : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L190-L192)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.structuralMassDamping "Permalink to this definition")
    :   None or a Float specifying the structural mass damping for the task region. The default
        value is None.

    viscousMassDamping : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L194-L196)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.viscousMassDamping "Permalink to this definition")
    :   None or a Float specifying the viscous mass damping for the task region. The default
        value is None.

    viscousStiffnessDamping : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/TopologyTask.py#L198-L200)[¶](#abaqus.Optimization.TopologyTask.TopologyTask.viscousStiffnessDamping "Permalink to this definition")
    :   None or a Float specifying the viscous stiffness damping for the task region. The
        default value is None.

*class* StepOption[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/StepOptionArray.py#L8-L40)[¶](#abaqus.Optimization.StepOptionArray.StepOption "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    A StepOption is an object used to define step options in a design response.

    Note

    This object can be accessed by:

    ```python
    import optimization
    mdb.models[name].optimizationTasks[name].designResponses[name].stepOptions[i]
    ```

    Note

    Check [StepOption on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stepoptionpyc.htm?contextscope=all).

    Member Details:

    loadCase : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'ALL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/StepOptionArray.py#L29-L32)[¶](#abaqus.Optimization.StepOptionArray.StepOption.loadCase "Permalink to this definition")
    :   The SymbolicConstant ALL or a String specifying the name of the load case. **loadCase** is
        ignored when the specified **step** does not contain a load case. The default value is
        ALL.

    lowerMode : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'ALL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/StepOptionArray.py#L19-L22)[¶](#abaqus.Optimization.StepOptionArray.StepOption.lowerMode "Permalink to this definition")
    :   The SymbolicConstant ALL or an Int specifying the lower mode in the range of modes to
        consider in the step. **lowerMode** is ignored for steps without modes. The default value
        is ALL.

    model : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/StepOptionArray.py#L8-L40)[¶](#abaqus.Optimization.StepOptionArray.StepOption.model "Permalink to this definition")
    :   A string specifying the name of the model from which the steps are supposed to be used
        in the design response. Specify only if the steps are not from the current model.

    step : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'ALL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/StepOptionArray.py#L34-L36)[¶](#abaqus.Optimization.StepOptionArray.StepOption.step "Permalink to this definition")
    :   The SymbolicConstant ALL or a String specifying the name of the step. The default value
        is ALL.

    upperMode : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'ALL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Optimization/StepOptionArray.py#L24-L27)[¶](#abaqus.Optimization.StepOptionArray.StepOption.upperMode "Permalink to this definition")
    :   The SymbolicConstant ALL or an Int specifying the upper mode in the range of modes to
        consider in the step. **upperMode** is ignored for steps without modes. The default value
        is ALL.

[Back to top](#)