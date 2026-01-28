# Abaqus SKETCHER Module API Reference

> Source: [https://hailin.wang/abqpy/en/2025/reference/mdb/model/sketcher.html](https://hailin.wang/abqpy/en/2025/reference/mdb/model/sketcher.html)
> Downloaded for offline use by Claude Code skills.

---

# Sketcher[¶](#sketcher "Permalink to this heading")

Sketcher commands are used to define the entities, such as the geometry, constraints, and dimensions, to create a sketch and to store the values and attributes associated with a particular sketch.

## Create constrained sketches[¶](#create-constrained-sketches "Permalink to this heading")

*class* SketchModel(*[name](#abaqus.Sketcher.SketchModel.SketchModel "abaqus.Sketcher.SketchModel.SketchModel.__init__.name (Python parameter)")*, *[description](#abaqus.Sketcher.SketchModel.SketchModel "abaqus.Sketcher.SketchModel.SketchModel.__init__.description (Python parameter)")=`''`*, *[stefanBoltzmann](#abaqus.Sketcher.SketchModel.SketchModel "abaqus.Sketcher.SketchModel.SketchModel.__init__.stefanBoltzmann (Python parameter)")=`None`*, *[absoluteZero](#abaqus.Sketcher.SketchModel.SketchModel "abaqus.Sketcher.SketchModel.SketchModel.__init__.absoluteZero (Python parameter)")=`None`*, *[waveFormulation](#abaqus.Sketcher.SketchModel.SketchModel "abaqus.Sketcher.SketchModel.SketchModel.__init__.waveFormulation (Python parameter)")=`abaqusConstants.NOT_SET`*, *[modelType](#abaqus.Sketcher.SketchModel.SketchModel "abaqus.Sketcher.SketchModel.SketchModel.__init__.modelType (Python parameter)")=`abaqusConstants.STANDARD_EXPLICIT`*, *[universalGas](#abaqus.Sketcher.SketchModel.SketchModel "abaqus.Sketcher.SketchModel.SketchModel.__init__.universalGas (Python parameter)")=`None`*, *[copyConstraints](#abaqus.Sketcher.SketchModel.SketchModel "abaqus.Sketcher.SketchModel.SketchModel.__init__.copyConstraints (Python parameter)")=`1`*, *[copyConnectors](#abaqus.Sketcher.SketchModel.SketchModel "abaqus.Sketcher.SketchModel.SketchModel.__init__.copyConnectors (Python parameter)")=`1`*, *[copyInteractions](#abaqus.Sketcher.SketchModel.SketchModel "abaqus.Sketcher.SketchModel.SketchModel.__init__.copyInteractions (Python parameter)")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L14-L63)[¶](#abaqus.Sketcher.SketchModel.SketchModel "Permalink to this definition")
:   Bases: [`ModelBase`](index.html#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase (Python class) — Bases: object")

    Abaqus creates a Model object named Model-1 when a session is started.

    Note

    This object can be accessed by:

    ```python
    mdb.models[name]
    ```

    Note

    Check [SketchModel on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?contextscope=all).

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
    | [`ConstrainedSketch`](#abaqus.Sketcher.SketchModel.SketchModel.ConstrainedSketch "abaqus.Sketcher.SketchModel.SketchModel.ConstrainedSketch (Python method) — This method creates a ConstrainedSketch object. If the sketch cannot be created, the method returns None.")(name, sheetSize[, ...]) | This method creates a ConstrainedSketch object. |

    Inherited from [`ModelBase`](index.html#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | `__init__`(name[, description, ...]) | This method creates a Model object. |
    | [`setValues`](index.html#abaqus.Model.ModelBase.ModelBase.setValues "abaqus.Model.ModelBase.ModelBase.setValues (Python method) — This method modifies the Model object.")([description, noPartsInputFile, ...]) | This method modifies the Model object. |

    ---

    Member Details:

    ConstrainedSketch(*[name](#abaqus.Sketcher.SketchModel.SketchModel.ConstrainedSketch.name "abaqus.Sketcher.SketchModel.SketchModel.ConstrainedSketch.name (Python parameter) — A String specifying the repository key.")*, *[sheetSize](#abaqus.Sketcher.SketchModel.SketchModel.ConstrainedSketch.sheetSize "abaqus.Sketcher.SketchModel.SketchModel.ConstrainedSketch.sheetSize (Python parameter) — A Float specifying the sheet size.")*, *[gridSpacing](#abaqus.Sketcher.SketchModel.SketchModel.ConstrainedSketch.gridSpacing "abaqus.Sketcher.SketchModel.SketchModel.ConstrainedSketch.gridSpacing (Python parameter) — A Float specifying the spacing between gridlines.")=`None`*, *[transform](#abaqus.Sketcher.SketchModel.SketchModel.ConstrainedSketch.transform "abaqus.Sketcher.SketchModel.SketchModel.ConstrainedSketch.transform (Python parameter) — A sequence of sequences of Floats specifying the three-dimensional orientation of the sketch.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L24-L63)[¶](#abaqus.Sketcher.SketchModel.SketchModel.ConstrainedSketch "Permalink to this definition")
    :   This method creates a ConstrainedSketch object. If the sketch cannot be created, the method returns
        None.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ConstrainedSketch
        ```

        Note

        Check [ConstrainedSketch on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.SketchModel.ConstrainedSketch-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Sketcher.SketchModel.SketchModel.ConstrainedSketch.name "Permalink to this definition")
            :   A String specifying the repository key.

            sheetSize[¶](#abaqus.Sketcher.SketchModel.SketchModel.ConstrainedSketch.sheetSize "Permalink to this definition")
            :   A Float specifying the sheet size.

            gridSpacing=`None`[¶](#abaqus.Sketcher.SketchModel.SketchModel.ConstrainedSketch.gridSpacing "Permalink to this definition")
            :   A Float specifying the spacing between gridlines. Possible values are Floats > 0. The
                default value is approximately 2 percent of **sheetSize**.

            transform=`()`[¶](#abaqus.Sketcher.SketchModel.SketchModel.ConstrainedSketch.transform "Permalink to this definition")
            :   A sequence of sequences of Floats specifying the three-dimensional orientation of the
                sketch. The sequence is a 3 x 4 transformation matrix specifying the axis of rotation
                and the translation vector. Possible values are any Floats.The default value for the
                axis of rotation is the identity matrix`(1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0,
                1.0)`The default value for the translation vector is`(0.0, 0.0, 0.0)`The default values
                position the sketch on the **X - Y** plane centered at the origin.

        Returns:[¶](#abaqus.Sketcher.SketchModel.SketchModel.ConstrainedSketch-returns "Permalink to this headline")
        :   **sketch** – A ConstrainedSketch object.

        Return type:[¶](#abaqus.Sketcher.SketchModel.SketchModel.ConstrainedSketch-return-type "Permalink to this headline")
        :   [`ConstrainedSketch`](#abaqus.Sketcher.SketchModel.ConstrainedSketch "abaqus.Sketcher.SketchModel.ConstrainedSketch (Python class) — Bases: ConstrainedSketchConstraintModel, ConstrainedSketchDimensionModel, ConstrainedSketchGeometryModel, ConstrainedSketchParameterModel, ConstrainedSketchVertexModel")

## Other Classes[¶](#other-classes "Permalink to this heading")

*class* ConstrainedSketch(*[name](#abaqus.Sketcher.SketchModel.ConstrainedSketch "abaqus.Sketcher.SketchModel.ConstrainedSketch.__init__.name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[sheetSize](#abaqus.Sketcher.SketchModel.ConstrainedSketch "abaqus.Sketcher.SketchModel.ConstrainedSketch.__init__.sheetSize (Python parameter)"): [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*, *[gridSpacing](#abaqus.Sketcher.SketchModel.ConstrainedSketch "abaqus.Sketcher.SketchModel.ConstrainedSketch.__init__.gridSpacing (Python parameter)"): [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[transform](#abaqus.Sketcher.SketchModel.ConstrainedSketch "abaqus.Sketcher.SketchModel.ConstrainedSketch.__init__.transform (Python parameter)"): [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)") = `()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L33-L705)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch "Permalink to this definition")

*class* ConstrainedSketch(*[name](#abaqus.Sketcher.SketchModel.ConstrainedSketch "abaqus.Sketcher.SketchModel.ConstrainedSketch.__init__.name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[objectToCopy](#abaqus.Sketcher.SketchModel.ConstrainedSketch "abaqus.Sketcher.SketchModel.ConstrainedSketch.__init__.objectToCopy (Python parameter)"): [ConstrainedSketch](#abaqus.Sketcher.SketchModel.ConstrainedSketch "abaqus.Sketcher.ConstrainedSketch.ConstrainedSketch (Python class)")*)
:   Bases: [`ConstrainedSketchConstraintModel`](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel (Python class) — Bases: ConstrainedSketchBase"), [`ConstrainedSketchDimensionModel`](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel (Python class) — Bases: ConstrainedSketchBase"), [`ConstrainedSketchGeometryModel`](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel (Python class) — Bases: ConstrainedSketchBase"), [`ConstrainedSketchParameterModel`](#abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameterModel.ConstrainedSketchParameterModel "abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameterModel.ConstrainedSketchParameterModel (Python class) — Bases: ConstrainedSketchBase"), [`ConstrainedSketchVertexModel`](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchVertexModel "abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchVertexModel (Python class) — Bases: ConstrainedSketchBase")

    Member Details:

    ConstrainedSketchFromGeometryFile(*[name](#abaqus.Sketcher.SketchModel.ConstrainedSketch.ConstrainedSketchFromGeometryFile.name "abaqus.Sketcher.SketchModel.ConstrainedSketch.ConstrainedSketchFromGeometryFile.name (Python parameter) — A String specifying the repository key.")*, *[geometryFile](#abaqus.Sketcher.SketchModel.ConstrainedSketch.ConstrainedSketchFromGeometryFile.geometryFile "abaqus.Sketcher.SketchModel.ConstrainedSketch.ConstrainedSketchFromGeometryFile.geometryFile (Python parameter) — An AcisFile object specifying a file containing geometry.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L113-L134)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.ConstrainedSketchFromGeometryFile "Permalink to this definition")
    :   This method creates a ConstrainedSketch object and places it in the sketches repository.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ConstrainedSketchFromGeometryFile
        ```

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.ConstrainedSketchFromGeometryFile-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.ConstrainedSketchFromGeometryFile.name "Permalink to this definition")
            :   A String specifying the repository key.

            geometryFile[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.ConstrainedSketchFromGeometryFile.geometryFile "Permalink to this definition")
            :   An AcisFile object specifying a file containing geometry. The geometry in the file is
                converted to two-dimensional sketch geometry in the **X - Y** plane.

        Returns:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.ConstrainedSketchFromGeometryFile-returns "Permalink to this headline")
        :   **sketch** – A ConstrainedSketch object

        Return type:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.ConstrainedSketchFromGeometryFile-return-type "Permalink to this headline")
        :   [`ConstrainedSketch`](#abaqus.Sketcher.SketchModel.ConstrainedSketch "abaqus.Sketcher.SketchModel.ConstrainedSketch (Python class) — Bases: ConstrainedSketchConstraintModel, ConstrainedSketchDimensionModel, ConstrainedSketchGeometryModel, ConstrainedSketchParameterModel, ConstrainedSketchVertexModel")

    assignCenterOfTwist(*[point](#abaqus.Sketcher.SketchModel.ConstrainedSketch.assignCenterOfTwist.point "abaqus.Sketcher.SketchModel.ConstrainedSketch.assignCenterOfTwist.point (Python parameter) — A ConstrainedSketchVertex object specifying an isolated point that indicates the center of twist for extruded features that use a twist angle.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L159-L170)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.assignCenterOfTwist "Permalink to this definition")
    :   This method indicates the isolated point that will be used as the center of twist when an extruded
        feature is created with twist.

        Note

        Check [ConstrainedSketch.assignCenterOfTwist on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchassigncenteroftwistpyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.assignCenterOfTwist-parameters "Permalink to this headline")
        :   point[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.assignCenterOfTwist.point "Permalink to this definition")
            :   A ConstrainedSketchVertex object specifying an isolated point that indicates the center
                of twist for extruded features that use a twist angle.

    assignCenterline(*[line](#abaqus.Sketcher.SketchModel.ConstrainedSketch.assignCenterline.line "abaqus.Sketcher.SketchModel.ConstrainedSketch.assignCenterline.line (Python parameter) — A ConstrainedSketchGeometry object specifying a construction line that indicates the centerline of revolved features.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L147-L157)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.assignCenterline "Permalink to this definition")
    :   This method indicates the construction line that will be used as a centerline for revolved features.

        Note

        Check [ConstrainedSketch.assignCenterline on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchassigncenterlinepyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.assignCenterline-parameters "Permalink to this headline")
        :   line[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.assignCenterline.line "Permalink to this definition")
            :   A ConstrainedSketchGeometry object specifying a construction line that indicates the
                centerline of revolved features.

    autoDimension(*[objectList](#abaqus.Sketcher.SketchModel.ConstrainedSketch.autoDimension.objectList "abaqus.Sketcher.SketchModel.ConstrainedSketch.autoDimension.objectList (Python parameter) — A sequence specifying the ConstrainedSketchGeometry objects to dimension.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L172-L182)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.autoDimension "Permalink to this definition")
    :   This method applies dimensions to the selected ConstrainedSketchGeometry objects in an effort to make
        the ConstrainedSketch well defined.

        Note

        Check [ConstrainedSketch.autoDimension on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchautodimensionpyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.autoDimension-parameters "Permalink to this headline")
        :   objectList[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.autoDimension.objectList "Permalink to this definition")
            :   A sequence specifying the ConstrainedSketchGeometry objects to dimension.

    autoTrimCurve(*[curve1](#abaqus.Sketcher.SketchModel.ConstrainedSketch.autoTrimCurve.curve1 "abaqus.Sketcher.SketchModel.ConstrainedSketch.autoTrimCurve.curve1 (Python parameter) — The ConstrainedSketchGeometry object to be trimmed.")*, *[point1](#abaqus.Sketcher.SketchModel.ConstrainedSketch.autoTrimCurve.point1 "abaqus.Sketcher.SketchModel.ConstrainedSketch.autoTrimCurve.point1 (Python parameter) — A pair of Floats specifying the location on ConstrainedSketchGeometry where the trimming should be applied.")*, *[parameter1](#abaqus.Sketcher.SketchModel.ConstrainedSketch.autoTrimCurve.parameter1 "abaqus.Sketcher.SketchModel.ConstrainedSketch.autoTrimCurve.parameter1 (Python parameter) — A Float specifying the parameter location on the ConstrainedSketchGeometry where the trimming should be applied.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L184-L201)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.autoTrimCurve "Permalink to this definition")
    :   This method automatically trims a selected ConstrainedSketchGeometry object at the specified
        location. If the object does not intersect other ConstrainedSketchGeometry objects, the entire selected
        object will be deleted.

        Note

        Check [ConstrainedSketch.autoTrimCurve on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchautotrimcurvepyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.autoTrimCurve-parameters "Permalink to this headline")
        :   curve1[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.autoTrimCurve.curve1 "Permalink to this definition")
            :   The ConstrainedSketchGeometry object to be trimmed.

            point1[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.autoTrimCurve.point1 "Permalink to this definition")
            :   A pair of Floats specifying the location on ConstrainedSketchGeometry where the trimming
                should be applied. **point1** and **parameter1** are mutually exclusive.

            parameter1[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.autoTrimCurve.parameter1 "Permalink to this definition")
            :   A Float specifying the parameter location on the ConstrainedSketchGeometry where the
                trimming should be applied. **point1** and **parameter1** are mutually exclusive.

    breakCurve(*[curve1](#abaqus.Sketcher.SketchModel.ConstrainedSketch.breakCurve.curve1 "abaqus.Sketcher.SketchModel.ConstrainedSketch.breakCurve.curve1 (Python parameter) — A ConstrainedSketchGeometry object specifying the object to be broken.")*, *[point1](#abaqus.Sketcher.SketchModel.ConstrainedSketch.breakCurve.point1 "abaqus.Sketcher.SketchModel.ConstrainedSketch.breakCurve.point1 (Python parameter) — A pair of Floats specifying the location on curve1 near where the break should be applied.")*, *[curve2](#abaqus.Sketcher.SketchModel.ConstrainedSketch.breakCurve.curve2 "abaqus.Sketcher.SketchModel.ConstrainedSketch.breakCurve.curve2 (Python parameter) — A ConstrainedSketchGeometry object specifying where curve1 should be broken.")*, *[point2](#abaqus.Sketcher.SketchModel.ConstrainedSketch.breakCurve.point2 "abaqus.Sketcher.SketchModel.ConstrainedSketch.breakCurve.point2 (Python parameter) — A pair of Floats specifying the location on curve2 near where curve1 should be broken.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L203-L229)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.breakCurve "Permalink to this definition")
    :   This method breaks a specified ConstrainedSketchGeometry object (*curve1*) using another specified
        ConstrainedSketchGeometry object (*curve2*). If the selected ConstrainedSketchGeometry objects
        intersect, then only **curve1** will be broken; **curve2** is not affected by the operation. The
        location for the break is determined by the specified point values.

        Note

        Check [ConstrainedSketch.breakCurve on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchbreakcurvepyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.breakCurve-parameters "Permalink to this headline")
        :   curve1[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.breakCurve.curve1 "Permalink to this definition")
            :   A ConstrainedSketchGeometry object specifying the object to be broken.

            point1[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.breakCurve.point1 "Permalink to this definition")
            :   A pair of Floats specifying the location on **curve1** near where the break should be
                applied.

            curve2[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.breakCurve.curve2 "Permalink to this definition")
            :   A ConstrainedSketchGeometry object specifying where **curve1** should be broken.

            point2[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.breakCurve.point2 "Permalink to this definition")
            :   A pair of Floats specifying the location on **curve2** near where **curve1** should be
                broken.

    copyMirror(*[mirrorLine](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyMirror.mirrorLine "abaqus.Sketcher.SketchModel.ConstrainedSketch.copyMirror.mirrorLine (Python parameter) — A ConstrainedSketchGeometry object specifying the line about which Abaqus will mirror the sketch.")*, *[objectList](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyMirror.objectList "abaqus.Sketcher.SketchModel.ConstrainedSketch.copyMirror.objectList (Python parameter) — A sequence of ConstrainedSketchGeometry objects specifying the sketch to be copied and mirrored.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L231-L249)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyMirror "Permalink to this definition")
    :   This method creates copies of the given ConstrainedSketchGeometry objects, mirrors them about a
        selected line, and inserts them into the appropriate repositories of the ConstrainedSketch object.

        Note

        Check [ConstrainedSketch.copyMirror on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchcopymirrorpyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyMirror-parameters "Permalink to this headline")
        :   mirrorLine[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyMirror.mirrorLine "Permalink to this definition")
            :   A ConstrainedSketchGeometry object specifying the line about which Abaqus will mirror
                the sketch.

            objectList[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyMirror.objectList "Permalink to this definition")
            :   A sequence of ConstrainedSketchGeometry objects specifying the sketch to be copied and
                mirrored.

    copyMove(*[vector](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyMove.vector "abaqus.Sketcher.SketchModel.ConstrainedSketch.copyMove.vector (Python parameter) — A sequence of two Floats specifying the translation vector.")*, *[objectList](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyMove.objectList "abaqus.Sketcher.SketchModel.ConstrainedSketch.copyMove.objectList (Python parameter) — A sequence of ConstrainedSketchGeometry objects to be copied and moved.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L251-L263)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyMove "Permalink to this definition")
    :   This method creates copies of the given ConstrainedSketchGeometry objects, moves them from their
        original position, and inserts them into the appropriate repositories of the ConstrainedSketch object.

        Note

        Check [ConstrainedSketch.copyMove on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchcopymovepyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyMove-parameters "Permalink to this headline")
        :   vector[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyMove.vector "Permalink to this definition")
            :   A sequence of two Floats specifying the translation vector.

            objectList[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyMove.objectList "Permalink to this definition")
            :   A sequence of ConstrainedSketchGeometry objects to be copied and moved.

    copyRotate(*[centerPoint](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyRotate.centerPoint "abaqus.Sketcher.SketchModel.ConstrainedSketch.copyRotate.centerPoint (Python parameter) — A pair of Floats specifying the center of rotation.")*, *[angle](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyRotate.angle "abaqus.Sketcher.SketchModel.ConstrainedSketch.copyRotate.angle (Python parameter) — A Float specifying the angle of rotation in degrees.")*, *[objectList](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyRotate.objectList "abaqus.Sketcher.SketchModel.ConstrainedSketch.copyRotate.objectList (Python parameter) — A sequence of ConstrainedSketchGeometry objects to be copied and moved.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L265-L284)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyRotate "Permalink to this definition")
    :   This method creates copies of the given ConstrainedSketchGeometry objects, rotates them, and inserts
        them into the appropriate repositories of the ConstrainedSketch object.

        Note

        Check [ConstrainedSketch.copyRotate on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchcopyrotatepyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyRotate-parameters "Permalink to this headline")
        :   centerPoint[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyRotate.centerPoint "Permalink to this definition")
            :   A pair of Floats specifying the center of rotation.

            angle[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyRotate.angle "Permalink to this definition")
            :   A Float specifying the angle of rotation in degrees.

            objectList[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyRotate.objectList "Permalink to this definition")
            :   A sequence of ConstrainedSketchGeometry objects to be copied and moved.

    copyScale(*[scaleValue](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyScale.scaleValue "abaqus.Sketcher.SketchModel.ConstrainedSketch.copyScale.scaleValue (Python parameter) — A Float specifying the value for scaling.")*, *[scaleCenter](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyScale.scaleCenter "abaqus.Sketcher.SketchModel.ConstrainedSketch.copyScale.scaleCenter (Python parameter) — A pair of Floats specifying the center of scaling.")*, *[objectList](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyScale.objectList "abaqus.Sketcher.SketchModel.ConstrainedSketch.copyScale.objectList (Python parameter) — A sequence of ConstrainedSketchGeometry objects to be copied and scaled.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L286-L306)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyScale "Permalink to this definition")
    :   This method creates copies of the given ConstrainedSketchGeometry objects, scales them by the
        specified value about a selected point, and inserts them into the appropriate repositories of the
        ConstrainedSketch object.

        Note

        Check [ConstrainedSketch.copyScale on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchcopyscalepyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyScale-parameters "Permalink to this headline")
        :   scaleValue[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyScale.scaleValue "Permalink to this definition")
            :   A Float specifying the value for scaling.

            scaleCenter[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyScale.scaleCenter "Permalink to this definition")
            :   A pair of Floats specifying the center of scaling.

            objectList[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.copyScale.objectList "Permalink to this definition")
            :   A sequence of ConstrainedSketchGeometry objects to be copied and scaled.

    delete(*[objectList](#abaqus.Sketcher.SketchModel.ConstrainedSketch.delete.objectList "abaqus.Sketcher.SketchModel.ConstrainedSketch.delete.objectList (Python parameter) — A sequence of ConstrainedSketchGeometry, ConstrainedSketchDimension, or ConstrainedSketchConstraint objects to be deleted.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L308-L319)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.delete "Permalink to this definition")
    :   This method deletes the given ConstrainedSketchGeometry, ConstrainedSketchDimension, or
        ConstrainedSketchConstraint objects.

        Note

        Check [ConstrainedSketch.delete on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchdeletepyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.delete-parameters "Permalink to this headline")
        :   objectList[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.delete.objectList "Permalink to this definition")
            :   A sequence of ConstrainedSketchGeometry, ConstrainedSketchDimension, or
                ConstrainedSketchConstraint objects to be deleted.

    deleteParameter(*[name](#abaqus.Sketcher.SketchModel.ConstrainedSketch.deleteParameter.name "abaqus.Sketcher.SketchModel.ConstrainedSketch.deleteParameter.name (Python parameter) — A String specifying the name of the parameter to delete.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L321-L330)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.deleteParameter "Permalink to this definition")
    :   The command deletes a specified parameter.

        Note

        Check [ConstrainedSketch.deleteParameter on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchdeleteparameterpyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.deleteParameter-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.deleteParameter.name "Permalink to this definition")
            :   A String specifying the name of the parameter to delete.

    dragEntity(*[entity](#abaqus.Sketcher.SketchModel.ConstrainedSketch.dragEntity.entity "abaqus.Sketcher.SketchModel.ConstrainedSketch.dragEntity.entity (Python parameter) — A ConstrainedSketchGeometry or ConstrainedSketchVertex object specifying the object to drag.")*, *[points](#abaqus.Sketcher.SketchModel.ConstrainedSketch.dragEntity.points "abaqus.Sketcher.SketchModel.ConstrainedSketch.dragEntity.points (Python parameter) — A sequence of sequences of three Floats specifying a sequence of points along which to drag the entity.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L332-L347)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.dragEntity "Permalink to this definition")
    :   This method drags a specified ConstrainedSketchGeometry or ConstrainedSketchVertex object to a
        specific location.

        Note

        Check [ConstrainedSketch.dragEntity on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchdragentitypyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.dragEntity-parameters "Permalink to this headline")
        :   entity[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.dragEntity.entity "Permalink to this definition")
            :   A ConstrainedSketchGeometry or ConstrainedSketchVertex object specifying the object to
                drag.

            points[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.dragEntity.points "Permalink to this definition")
            :   A sequence of sequences of three Floats specifying a sequence of points along which to
                drag the entity. The order of points in the sequence defines a path that determines the
                solution.

    linearPattern(*[number1](#abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern.number1 "abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern.number1 (Python parameter) — An Integer specifying the total number of copies, including the original objects, that appear along the first direction in the pattern.")*, *[spacing1](#abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern.spacing1 "abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern.spacing1 (Python parameter) — A Float specifying the spacing between copies along the first direction in the pattern. Possible values are 0.0 ≤ spacing1 .")*, *[angle1](#abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern.angle1 "abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern.angle1 (Python parameter) — A Float specifying the angle in degrees of the first direction in the pattern.")*, *[vertexList](#abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern.vertexList "abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern.vertexList (Python parameter) — A sequence of ConstrainedSketchVertex objects to copy.")=`()`*, *[geomList](#abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern.geomList "abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern.geomList (Python parameter) — A sequence of ConstrainedSketchGeometry objects to copy.")=`()`*, *[number2](#abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern.number2 "abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern.number2 (Python parameter) — An integer specifying the total number of copies, including the original objects, that appear along the second direction in the pattern.")=`1`*, *[spacing2](#abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern.spacing2 "abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern.spacing2 (Python parameter) — A Float specifying the spacing between copies along the first direction in the pattern. Possible values are 0.0 ≤ spacing2.")=`None`*, *[angle2](#abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern.angle2 "abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern.angle2 (Python parameter) — A Float specifying the angle in degrees of the first direction in the pattern.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L349-L403)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern "Permalink to this definition")
    :   This method copies ConstrainedSketchGeometry objects in a linear pattern along one or two directions.
        This method also copies any associated dimension or constraint objects that exist between the given
        objects.

        Note

        Check [ConstrainedSketch.linearPattern on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchlinearpatternpyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern-parameters "Permalink to this headline")
        :   number1[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern.number1 "Permalink to this definition")
            :   An Integer specifying the total number of copies, including the original objects, that
                appear along the first direction in the pattern. Possible values are 1 ≤ **number1** ≤
                1000.

            spacing1[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern.spacing1 "Permalink to this definition")
            :   A Float specifying the spacing between copies along the first direction in the pattern.
                Possible values are 0.0 ≤ **spacing1** .

            angle1[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern.angle1 "Permalink to this definition")
            :   A Float specifying the angle in degrees of the first direction in the pattern. Possible
                values are -360.0 ≤ **angle1** ≤ 360.0.

            vertexList=`()`[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern.vertexList "Permalink to this definition")
            :   A sequence of ConstrainedSketchVertex objects to copy.

            geomList=`()`[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern.geomList "Permalink to this definition")
            :   A sequence of ConstrainedSketchGeometry objects to copy.

            number2=`1`[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern.number2 "Permalink to this definition")
            :   An integer specifying the total number of copies, including the original objects, that
                appear along the second direction in the pattern. Possible values are 1 ≤ **number2** ≤
                1000. The default value is 1. The value of either **number1** or **number2** must be greater
                than one.

            spacing2=`None`[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern.spacing2 "Permalink to this definition")
            :   A Float specifying the spacing between copies along the first direction in the pattern.
                Possible values are 0.0 ≤ **spacing2**. The default value is **spacing1**.

            angle2=`None`[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern.angle2 "Permalink to this definition")
            :   A Float specifying the angle in degrees of the first direction in the pattern. Possible
                values are -360.0 ≤ **angle2** ≤ 360.0. The default value is 90° beyond the value of
                **angle1**.

        Return type:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern-return-type "Permalink to this headline")
        :   `None.`

        Raises:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.linearPattern-raises "Permalink to this headline")
        :   [**AbaqusException**](../../kernel/utility.html#abaqus.UtilityAndView.AbaqusException.AbaqusException "abaqus.UtilityAndView.AbaqusException.AbaqusException (Python class) — Bases: Exception") – Number must be greater than 1 for at least one direction

    mergeVertices(*[value](#abaqus.Sketcher.SketchModel.ConstrainedSketch.mergeVertices.value "abaqus.Sketcher.SketchModel.ConstrainedSketch.mergeVertices.value (Python parameter) — A Float specifying the search radius.")*, *[vertexList](#abaqus.Sketcher.SketchModel.ConstrainedSketch.mergeVertices.vertexList "abaqus.Sketcher.SketchModel.ConstrainedSketch.mergeVertices.vertexList (Python parameter) — A sequence of ConstrainedSketchVertex objects to be merged.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L405-L419)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.mergeVertices "Permalink to this definition")
    :   This method merges the ConstrainedSketchVertex objects that lie within the specified distance of each
        other. If only one ConstrainedSketchVertex object is selected, it will merge all ConstrainedSketchVertex
        objects that lie within the specified distance of that vertex. If more than one vertex is selected, the
        search will be restricted to only the selected ConstrainedSketchVertex objects.

        Note

        Check [ConstrainedSketch.mergeVertices on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchmergeverticespyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.mergeVertices-parameters "Permalink to this headline")
        :   value[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.mergeVertices.value "Permalink to this definition")
            :   A Float specifying the search radius.

            vertexList[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.mergeVertices.vertexList "Permalink to this definition")
            :   A sequence of ConstrainedSketchVertex objects to be merged.

    move(*[vector](#abaqus.Sketcher.SketchModel.ConstrainedSketch.move.vector "abaqus.Sketcher.SketchModel.ConstrainedSketch.move.vector (Python parameter) — A sequence of two Floats specifying the translation vector.")*, *[objectList](#abaqus.Sketcher.SketchModel.ConstrainedSketch.move.objectList "abaqus.Sketcher.SketchModel.ConstrainedSketch.move.objectList (Python parameter) — A sequence of ConstrainedSketchGeometry objects specifying the objects to be translated.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L421-L432)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.move "Permalink to this definition")
    :   This method translates the given ConstrainedSketchGeometry objects by the given vector.

        Note

        Check [ConstrainedSketch.move on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchmovepyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.move-parameters "Permalink to this headline")
        :   vector[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.move.vector "Permalink to this definition")
            :   A sequence of two Floats specifying the translation vector.

            objectList[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.move.objectList "Permalink to this definition")
            :   A sequence of ConstrainedSketchGeometry objects specifying the objects to be translated.

    offset(*[distance](#abaqus.Sketcher.SketchModel.ConstrainedSketch.offset.distance "abaqus.Sketcher.SketchModel.ConstrainedSketch.offset.distance (Python parameter) — A Float specifying the distance to be offset.")*, *[objectList](#abaqus.Sketcher.SketchModel.ConstrainedSketch.offset.objectList "abaqus.Sketcher.SketchModel.ConstrainedSketch.offset.objectList (Python parameter) — A sequence of ConstrainedSketchGeometry objects to be copied and offset.")*, *[side](#abaqus.Sketcher.SketchModel.ConstrainedSketch.offset.side "abaqus.Sketcher.SketchModel.ConstrainedSketch.offset.side (Python parameter) — A SymbolicConstant specifying which side the offset should occur.")*, *[filletCorners](#abaqus.Sketcher.SketchModel.ConstrainedSketch.offset.filletCorners "abaqus.Sketcher.SketchModel.ConstrainedSketch.offset.filletCorners (Python parameter) — A Boolean specifying whether the corners need to be rounded instead of being extended.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L434-L459)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.offset "Permalink to this definition")
    :   This method creates copies of the selected ConstrainedSketchGeometry objects, offsets them by the
        specified distance in the specified direction, and inserts them into the ConstrainedSketch object’s
        appropriate repositories. If connected objects are selected, trim or extend is carried out to complete
        the offset.

        Note

        Check [ConstrainedSketch.offset on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchoffsetpyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.offset-parameters "Permalink to this headline")
        :   distance[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.offset.distance "Permalink to this definition")
            :   A Float specifying the distance to be offset.

            objectList[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.offset.objectList "Permalink to this definition")
            :   A sequence of ConstrainedSketchGeometry objects to be copied and offset.

            side[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.offset.side "Permalink to this definition")
            :   A SymbolicConstant specifying which side the offset should occur. Possible values are
                LEFT and RIGHT.

            filletCorners=`0`[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.offset.filletCorners "Permalink to this definition")
            :   A Boolean specifying whether the corners need to be rounded instead of being extended.

    print()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L136-L145)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.print "Permalink to this definition")
    :   This method prints the following statistics about a sketch:

        * The sketch Id (a positive integer).
        * The number of geometry curves (the number of ConstrainedSketchGeometry objects).
        * The number of dimensions (the number of ConstrainedSketchDimension objects).
        * The number of vertices (the number of ConstrainedSketchVertex objects).

    radialPattern(*[number](#abaqus.Sketcher.SketchModel.ConstrainedSketch.radialPattern.number "abaqus.Sketcher.SketchModel.ConstrainedSketch.radialPattern.number (Python parameter) — An Int specifying the total number of copies, including the original objects, that appear in the radial pattern.")*, *[totalAngle](#abaqus.Sketcher.SketchModel.ConstrainedSketch.radialPattern.totalAngle "abaqus.Sketcher.SketchModel.ConstrainedSketch.radialPattern.totalAngle (Python parameter) — A Float specifying the total angle in degrees between the first and last instance in the pattern.")*, *[centerPoint](#abaqus.Sketcher.SketchModel.ConstrainedSketch.radialPattern.centerPoint "abaqus.Sketcher.SketchModel.ConstrainedSketch.radialPattern.centerPoint (Python parameter) — A pair of Floats specifying the center of the radial pattern.")*, *[vertexList](#abaqus.Sketcher.SketchModel.ConstrainedSketch.radialPattern.vertexList "abaqus.Sketcher.SketchModel.ConstrainedSketch.radialPattern.vertexList (Python parameter) — A sequence of ConstrainedSketchVertex objects to copy.")=`()`*, *[geomList](#abaqus.Sketcher.SketchModel.ConstrainedSketch.radialPattern.geomList "abaqus.Sketcher.SketchModel.ConstrainedSketch.radialPattern.geomList (Python parameter) — A sequence of ConstrainedSketchGeometry objects to copy.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L461-L491)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.radialPattern "Permalink to this definition")
    :   This method copies ConstrainedSketchGeometry objects in a radial pattern about a specified center
        point.

        Note

        Check [ConstrainedSketch.radialPattern on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchradialpatternpyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.radialPattern-parameters "Permalink to this headline")
        :   number[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.radialPattern.number "Permalink to this definition")
            :   An Int specifying the total number of copies, including the original objects, that
                appear in the radial pattern. Possible values are 2 ≤ **number2** ≤ 1000.

            totalAngle[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.radialPattern.totalAngle "Permalink to this definition")
            :   A Float specifying the total angle in degrees between the first and last instance in the
                pattern. A positive angle corresponds to a counter-clockwise direction. The values 360°
                and -360° represent a special case where the pattern makes a full circle. In this case,
                because the copy would overlay the original, the copy is not placed at the last
                position. Possible values are -360.0 ≤ **totalAngle** ≤ 360.0.

            centerPoint[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.radialPattern.centerPoint "Permalink to this definition")
            :   A pair of Floats specifying the center of the radial pattern.

            vertexList=`()`[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.radialPattern.vertexList "Permalink to this definition")
            :   A sequence of ConstrainedSketchVertex objects to copy.

            geomList=`()`[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.radialPattern.geomList "Permalink to this definition")
            :   A sequence of ConstrainedSketchGeometry objects to copy.

    rectangle(*[point1](#abaqus.Sketcher.SketchModel.ConstrainedSketch.rectangle.point1 "abaqus.Sketcher.SketchModel.ConstrainedSketch.rectangle.point1 (Python parameter) — A pair of Floats specifying the first corner of the rectangle.")*, *[point2](#abaqus.Sketcher.SketchModel.ConstrainedSketch.rectangle.point2 "abaqus.Sketcher.SketchModel.ConstrainedSketch.rectangle.point2 (Python parameter) — A pair of Floats specifying the second corner of the rectangle.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L498-L515)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.rectangle "Permalink to this definition")
    :   This method creates four lines that form a rectangle with diagonal corners defined by the given
        points and inserts them into the geometry repository of the ConstrainedSketch object.

        Note

        Check [ConstrainedSketch.rectangle on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchrectanglepyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.rectangle-parameters "Permalink to this headline")
        :   point1[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.rectangle.point1 "Permalink to this definition")
            :   A pair of Floats specifying the first corner of the rectangle.

            point2[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.rectangle.point2 "Permalink to this definition")
            :   A pair of Floats specifying the second corner of the rectangle.

        Returns:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.rectangle-returns "Permalink to this headline")
        :   **success** – An Int specifying the success or failure of the method. A value of 0 indicates failure

        Return type:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.rectangle-return-type "Permalink to this headline")
        :   [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")

    removeGapsAndOverlaps(*[tolerance](#abaqus.Sketcher.SketchModel.ConstrainedSketch.removeGapsAndOverlaps.tolerance "abaqus.Sketcher.SketchModel.ConstrainedSketch.removeGapsAndOverlaps.tolerance (Python parameter) — A float value which specifies the largest size of the gap or overlap between entities that is to be removed.")*, *[geomList](#abaqus.Sketcher.SketchModel.ConstrainedSketch.removeGapsAndOverlaps.geomList "abaqus.Sketcher.SketchModel.ConstrainedSketch.removeGapsAndOverlaps.geomList (Python parameter) — A sequence of ConstrainedSketchGeometry objects where the gaps and overlaps are to be removed.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L517-L533)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.removeGapsAndOverlaps "Permalink to this definition")
    :   This method removes gaps and overlaps between sketch geometries specified by the user. This method is
        particularly useful when cleaning up imported sketches.

        Note

        Check [ConstrainedSketch.removeGapsAndOverlaps on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchremovegapsandoverlapspyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.removeGapsAndOverlaps-parameters "Permalink to this headline")
        :   tolerance[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.removeGapsAndOverlaps.tolerance "Permalink to this definition")
            :   A float value which specifies the largest size of the gap or overlap between entities
                that is to be removed. Typically this value is small and is used to close gaps and
                overlaps which may not exist in the originating program but exist in the sketch because
                of mismatched tolerances between the two programs.

            geomList[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.removeGapsAndOverlaps.geomList "Permalink to this definition")
            :   A sequence of ConstrainedSketchGeometry objects where the gaps and overlaps are to be
                removed.

    repairShortEdges(*[geomList](#abaqus.Sketcher.SketchModel.ConstrainedSketch.repairShortEdges.geomList "abaqus.Sketcher.SketchModel.ConstrainedSketch.repairShortEdges.geomList (Python parameter) — A sequence of ConstrainedSketchGeometry objects where the short edges are to be removed.")*, *[tolerance](#abaqus.Sketcher.SketchModel.ConstrainedSketch.repairShortEdges.tolerance "abaqus.Sketcher.SketchModel.ConstrainedSketch.repairShortEdges.tolerance (Python parameter) — A float value that is used to select and delete only those edges specified in geomList whose lengths are smaller than the given value.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L535-L552)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.repairShortEdges "Permalink to this definition")
    :   This method deletes the short edges specified, optionally selecting only those short edges whose
        lengths are smaller than the specified tolerance and healing the resultant gap in the sketch. This
        method is particularly useful in conjunction with removeGapsAndOverlap when cleaning up imported
        sketches.

        Note

        Check [ConstrainedSketch.repairShortEdges on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchrepairshortedgespyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.repairShortEdges-parameters "Permalink to this headline")
        :   geomList[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.repairShortEdges.geomList "Permalink to this definition")
            :   A sequence of ConstrainedSketchGeometry objects where the short edges are to be removed.

            tolerance=`''`[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.repairShortEdges.tolerance "Permalink to this definition")
            :   A float value that is used to select and delete only those edges specified in **geomList**
                whose lengths are smaller than the given value. The default value is -1.0. This value
                implies that all edges specified in **geomList** will be removed and the sketch healed to
                remove gaps left by their removal.

    resetView()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L493-L496)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.resetView "Permalink to this definition")
    :   This method resets the view to be perpendicular to the sketching plane.

    retrieveSketch(*[sketch](#abaqus.Sketcher.SketchModel.ConstrainedSketch.retrieveSketch.sketch "abaqus.Sketcher.SketchModel.ConstrainedSketch.retrieveSketch.sketch (Python parameter) — A ConstrainedSketch object specifying the object from which to copy.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L554-L566)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.retrieveSketch "Permalink to this definition")
    :   This method copies all ConstrainedSketchGeometry, ConstrainedSketchDimension,
        ConstrainedSketchConstraint, and ConstrainedSketchParameter objects from the specified ConstrainedSketch
        object. The new objects are added to the existing objects (if any). The objects in the specified
        ConstrainedSketch object are not modified by the retrieve operation.

        Note

        Check [ConstrainedSketch.retrieveSketch on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchretrievesketchpyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.retrieveSketch-parameters "Permalink to this headline")
        :   sketch[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.retrieveSketch.sketch "Permalink to this definition")
            :   A ConstrainedSketch object specifying the object from which to copy.

    rotate(*[centerPoint](#abaqus.Sketcher.SketchModel.ConstrainedSketch.rotate.centerPoint "abaqus.Sketcher.SketchModel.ConstrainedSketch.rotate.centerPoint (Python parameter) — A pair of Floats specifying the center of rotation.")*, *[angle](#abaqus.Sketcher.SketchModel.ConstrainedSketch.rotate.angle "abaqus.Sketcher.SketchModel.ConstrainedSketch.rotate.angle (Python parameter) — A Float specifying the angle of rotation in degrees.")*, *[objectList](#abaqus.Sketcher.SketchModel.ConstrainedSketch.rotate.objectList "abaqus.Sketcher.SketchModel.ConstrainedSketch.rotate.objectList (Python parameter) — A sequence of ConstrainedSketchGeometry specifying the objects to be rotated.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L568-L582)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.rotate "Permalink to this definition")
    :   This method rotates the given ConstrainedSketchGeometry objects by the given angle and about the
        given point.

        Note

        Check [ConstrainedSketch.rotate on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchrotatepyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.rotate-parameters "Permalink to this headline")
        :   centerPoint[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.rotate.centerPoint "Permalink to this definition")
            :   A pair of Floats specifying the center of rotation.

            angle[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.rotate.angle "Permalink to this definition")
            :   A Float specifying the angle of rotation in degrees.

            objectList[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.rotate.objectList "Permalink to this definition")
            :   A sequence of ConstrainedSketchGeometry specifying the objects to be rotated.

    scale(*[scaleValue](#abaqus.Sketcher.SketchModel.ConstrainedSketch.scale.scaleValue "abaqus.Sketcher.SketchModel.ConstrainedSketch.scale.scaleValue (Python parameter) — A Float specifying the value of scale.")*, *[scaleCenter](#abaqus.Sketcher.SketchModel.ConstrainedSketch.scale.scaleCenter "abaqus.Sketcher.SketchModel.ConstrainedSketch.scale.scaleCenter (Python parameter) — A pair of Floats specifying the center of scale.")*, *[objectList](#abaqus.Sketcher.SketchModel.ConstrainedSketch.scale.objectList "abaqus.Sketcher.SketchModel.ConstrainedSketch.scale.objectList (Python parameter) — A sequence of ConstrainedSketchGeometry objects specifying the objects to be scaled.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L584-L603)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.scale "Permalink to this definition")
    :   This method scales the given ConstrainedSketchGeometry objects by the given scale factor and about
        the given point.

        Note

        Check [ConstrainedSketch.scale on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchscalepyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.scale-parameters "Permalink to this headline")
        :   scaleValue[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.scale.scaleValue "Permalink to this definition")
            :   A Float specifying the value of scale.

            scaleCenter[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.scale.scaleCenter "Permalink to this definition")
            :   A pair of Floats specifying the center of scale.

            objectList[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.scale.objectList "Permalink to this definition")
            :   A sequence of ConstrainedSketchGeometry objects specifying the objects to be scaled.

    setPrimaryObject(*[option](#abaqus.Sketcher.SketchModel.ConstrainedSketch.setPrimaryObject.option "abaqus.Sketcher.SketchModel.ConstrainedSketch.setPrimaryObject.option (Python parameter) — A SymbolicConstant specifying how the sketch is displayed.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L605-L624)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.setPrimaryObject "Permalink to this definition")
    :   This method makes the ConstrainedSketch object the primary object in the current viewport. The sketch
        remains the primary object in the current viewport until an unsetPrimaryobject command is issued.

        Note

        Check [ConstrainedSketch.setPrimaryObject on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchsetprimaryobjectpyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.setPrimaryObject-parameters "Permalink to this headline")
        :   option[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.setPrimaryObject.option "Permalink to this definition")
            :   A SymbolicConstant specifying how the sketch is displayed. Possible values are:

                * `STANDALONE`: Indicates a new stand-alone sketch. The current viewport is
                  :   cleared and is replaced by the stand-alone sketch. The view direction
                      is set to -Z.
                * `SUPERIMPOSE`: Indicates that the sketch is superimposed on the current
                  :   viewport. The view direction is changed to be perpendicular to the
                      sketch plane. The change is effected smoothly as an animated sequence
                      of many small viewing steps.

    trimExtendCurve(*[curve1](#abaqus.Sketcher.SketchModel.ConstrainedSketch.trimExtendCurve.curve1 "abaqus.Sketcher.SketchModel.ConstrainedSketch.trimExtendCurve.curve1 (Python parameter) — The ConstrainedSketchGeometry object specifying the object to be trimmed or extended.")*, *[point1](#abaqus.Sketcher.SketchModel.ConstrainedSketch.trimExtendCurve.point1 "abaqus.Sketcher.SketchModel.ConstrainedSketch.trimExtendCurve.point1 (Python parameter) — A pair of Floats specifying the location on curve1 where trim or extend should be applied.")*, *[curve2](#abaqus.Sketcher.SketchModel.ConstrainedSketch.trimExtendCurve.curve2 "abaqus.Sketcher.SketchModel.ConstrainedSketch.trimExtendCurve.curve2 (Python parameter) — The ConstrainedSketchGeometry object specifying the object to which curve1 is trimmed or extended.")*, *[point2](#abaqus.Sketcher.SketchModel.ConstrainedSketch.trimExtendCurve.point2 "abaqus.Sketcher.SketchModel.ConstrainedSketch.trimExtendCurve.point2 (Python parameter) — A pair of Floats specifying the location on curve2 near where curve1 should be trimmed or extended.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L626-L652)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.trimExtendCurve "Permalink to this definition")
    :   This method trims or extends a specified ConstrainedSketchGeometry object (*curve1*) using another
        specified ConstrainedSketchGeometry object (*curve2*). **curve2** is not affected by the operation. The
        location for the trim or extend is determined by the specified point values.

        Note

        Check [ConstrainedSketch.trimExtendCurve on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchtrimextendcurvepyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.trimExtendCurve-parameters "Permalink to this headline")
        :   curve1[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.trimExtendCurve.curve1 "Permalink to this definition")
            :   The ConstrainedSketchGeometry object specifying the object to be trimmed or extended.

            point1[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.trimExtendCurve.point1 "Permalink to this definition")
            :   A pair of Floats specifying the location on **curve1** where trim or extend should be
                applied.

            curve2[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.trimExtendCurve.curve2 "Permalink to this definition")
            :   The ConstrainedSketchGeometry object specifying the object to which **curve1** is trimmed
                or extended. **curve2** is not trimmed or extended.

            point2[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.trimExtendCurve.point2 "Permalink to this definition")
            :   A pair of Floats specifying the location on **curve2** near where **curve1** should be
                trimmed or extended.

    undo()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L654-L657)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.undo "Permalink to this definition")
    :   This method undoes the effects of the last ConstrainedSketch object method.

    unsetPrimaryObject()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L659-L668)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.unsetPrimaryObject "Permalink to this definition")
    :   This method removes the ConstrainedSketch object from the current viewport, reversing the effects of
        the setPrimaryobject command.

        If the **option** argument was set to SUPERIMPOSE, the viewport will be returned to the view
        orientation that was in place when the setPrimaryobject command was issued. If the **option**
        argument was set to STANDALONE, the viewport will be left empty.

    writeAcisFile(*[fileName](#abaqus.Sketcher.SketchModel.ConstrainedSketch.writeAcisFile.fileName "abaqus.Sketcher.SketchModel.ConstrainedSketch.writeAcisFile.fileName (Python parameter) — A String specifying the name of the file to which to write.")*, *[version](#abaqus.Sketcher.SketchModel.ConstrainedSketch.writeAcisFile.version "abaqus.Sketcher.SketchModel.ConstrainedSketch.writeAcisFile.version (Python parameter) — A Float specifying the ACIS version.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L670-L687)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.writeAcisFile "Permalink to this definition")
    :   This method exports the geometry of the sketch to a named file in ACIS format.

        Note

        Check [ConstrainedSketch.writeAcisFile on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchwriteacisfilepyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.writeAcisFile-parameters "Permalink to this headline")
        :   fileName[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.writeAcisFile.fileName "Permalink to this definition")
            :   A String specifying the name of the file to which to write. The file name’s extension is
                used to determine whether a part or assembly is written. Use the file extension .asat
                for the assembly format.

                Changed in version 2018: Add description for thr file name’s extension.

            version=`None`[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.writeAcisFile.version "Permalink to this definition")
            :   A Float specifying the ACIS version. For example, the Float 12.0 corresponds to ACIS
                Version 12.0. The default value is the current version of ACIS.

    writeIgesFile(*[filename](#abaqus.Sketcher.SketchModel.ConstrainedSketch.writeIgesFile.filename "abaqus.Sketcher.SketchModel.ConstrainedSketch.writeIgesFile.filename (Python parameter) — A String specifying the file name.")*, *[flavor](#abaqus.Sketcher.SketchModel.ConstrainedSketch.writeIgesFile.flavor "abaqus.Sketcher.SketchModel.ConstrainedSketch.writeIgesFile.flavor (Python parameter) — A SymbolicConstant specifying a particular flavor of IGES to export.")=`Ellipsis`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/SketchModel.py#L689-L705)[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.writeIgesFile "Permalink to this definition")
    :   This method exports the geometry of the sketch to a named file in IGES format.

        Note

        Check [ConstrainedSketch.writeIgesFile on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all#simaker-constrainedsketchwriteigesfilepyc).

        Parameters:[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.writeIgesFile-parameters "Permalink to this headline")
        :   filename[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.writeIgesFile.filename "Permalink to this definition")
            :   A String specifying the file name.

            flavor=`Ellipsis`[¶](#abaqus.Sketcher.SketchModel.ConstrainedSketch.writeIgesFile.flavor "Permalink to this definition")
            :   A SymbolicConstant specifying a particular flavor of IGES to export. Possible values
                are STANDARD, AUTOCAD, SOLIDWORKS, JAMA, and MSBO.

*class* ConstrainedSketchConstraintModel[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchConstraint/ConstrainedSketchConstraintModel.py#L13-L309)[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel "Permalink to this definition")
:   Bases: [`ConstrainedSketchBase`](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchBase "abaqus.Sketcher.ConstrainedSketchBase.ConstrainedSketchBase (Python class)")

    A ConstrainedSketch object contains the entities that are used to create a sketch. The objects include
    ConstrainedSketchGeometry objects contained in the ConstrainedSketchGeometry Repository, such as Line, Arc,
    and Spline. ConstrainedSketchVertex, ConstrainedSketchDimension, ConstrainedSketchConstraint, and
    ConstrainedSketchParameter objects are contained in their respective repositories.

    Note

    This object can be accessed by:

    ```python
    import sketch
    mdb.models[name].sketches[name]
    ```

    Note

    Check [ConstrainedSketchConstraintModel on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?contextscope=all).

    Member Details:

    CoincidentConstraint(*[entity1](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.CoincidentConstraint.entity1 "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.CoincidentConstraint.entity1 (Python parameter) — A ConstrainedSketchGeometry object or a ConstrainedSketchVertex object specifying the first object.")*, *[entity2](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.CoincidentConstraint.entity2 "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.CoincidentConstraint.entity2 (Python parameter) — A ConstrainedSketchGeometry object or a ConstrainedSketchVertex object specifying the second object.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchConstraint/ConstrainedSketchConstraintModel.py#L27-L52)[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.CoincidentConstraint "Permalink to this definition")
    :   This method creates a coincident constraint. This constraint applies to two vertices, to a vertex and
        a ConstrainedSketchGeometry object, or to two ConstrainedSketchGeometry objects of the same type and
        constrains them to be coincident.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].CoincidentConstraint
        ```

        Note

        Check [CoincidentConstraint on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-coincidentconstraintpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.CoincidentConstraint-parameters "Permalink to this headline")
        :   entity1[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.CoincidentConstraint.entity1 "Permalink to this definition")
            :   A ConstrainedSketchGeometry object or a ConstrainedSketchVertex object specifying the first object.

            entity2[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.CoincidentConstraint.entity2 "Permalink to this definition")
            :   A ConstrainedSketchGeometry object or a ConstrainedSketchVertex object specifying the second object.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.CoincidentConstraint-returns "Permalink to this headline")
        :   **constraint** – A ConstrainedSketchConstraint object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.CoincidentConstraint-return-type "Permalink to this headline")
        :   `ConstrainedSketchConstraint`

    ConcentricConstraint(*[entity1](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.ConcentricConstraint.entity1 "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.ConcentricConstraint.entity1 (Python parameter) — A ConstrainedSketchGeometry object specifying the first arc, circle, ellipse, or sketch vertex.")*, *[entity2](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.ConcentricConstraint.entity2 "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.ConcentricConstraint.entity2 (Python parameter) — A ConstrainedSketchGeometry object specifying the second arc, circle, ellipse, or sketch vertex.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchConstraint/ConstrainedSketchConstraintModel.py#L54-L81)[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.ConcentricConstraint "Permalink to this definition")
    :   This method creates a concentric constraint. This constraint applies to any combination of circles,
        arcs, ellipses, and points and constrains them to be concentric. A concentric constraint implies that
        the center of ConstrainedSketchGeometry objects coincide.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].ConcentricConstraint
        ```

        Note

        Check [ConcentricConstraint on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-concentricconstraintpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.ConcentricConstraint-parameters "Permalink to this headline")
        :   entity1[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.ConcentricConstraint.entity1 "Permalink to this definition")
            :   A ConstrainedSketchGeometry object specifying the first arc, circle, ellipse, or sketch
                vertex.

            entity2[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.ConcentricConstraint.entity2 "Permalink to this definition")
            :   A ConstrainedSketchGeometry object specifying the second arc, circle, ellipse, or sketch
                vertex.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.ConcentricConstraint-returns "Permalink to this headline")
        :   **constraint** – A ConstrainedSketchConstraint object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.ConcentricConstraint-return-type "Permalink to this headline")
        :   `ConstrainedSketchConstraint`

    EqualDistanceConstraint(*[entity1](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualDistanceConstraint.entity1 "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualDistanceConstraint.entity1 (Python parameter) — AConstrainedSketchGeometry object specifying the first line or ConstrainedSketchVertex object.")*, *[entity2](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualDistanceConstraint.entity2 "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualDistanceConstraint.entity2 (Python parameter) — A ConstrainedSketchGeometry object specifying the second line or ConstrainedSketchVertex object.")*, *[midpoint](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualDistanceConstraint.midpoint "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualDistanceConstraint.midpoint (Python parameter) — A ConstrainedSketchVertex object specifying the vertex that will be positioned an equal distance from entity1 and entity2.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchConstraint/ConstrainedSketchConstraintModel.py#L253-L283)[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualDistanceConstraint "Permalink to this definition")
    :   This method creates an equal distance constraint. This constraint can be applied between a midpoint
        ConstrainedSketchVertex object and any other two ConstrainedSketchVertex objects or between a midpoint
        ConstrainedSketchVertex object and two ConstrainedSketchGeometry objects that are lines. The equal
        distance constraint forces the midpoint vertex to remain at an equal distance from the two other
        vertices or lines.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].EqualDistanceConstraint
        ```

        Note

        Check [EqualDistanceConstraint on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-equaldistanceconstraintpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualDistanceConstraint-parameters "Permalink to this headline")
        :   entity1[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualDistanceConstraint.entity1 "Permalink to this definition")
            :   AConstrainedSketchGeometry object specifying the first line or ConstrainedSketchVertex object.

            entity2[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualDistanceConstraint.entity2 "Permalink to this definition")
            :   A ConstrainedSketchGeometry object specifying the second line or ConstrainedSketchVertex object.

            midpoint[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualDistanceConstraint.midpoint "Permalink to this definition")
            :   A ConstrainedSketchVertex object specifying the vertex that will be positioned an equal distance from
                **entity1** and **entity2**.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualDistanceConstraint-returns "Permalink to this headline")
        :   **constraint** – A ConstrainedSketchConstraint object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualDistanceConstraint-return-type "Permalink to this headline")
        :   `ConstrainedSketchConstraint`

    EqualLengthConstraint(*[entity1](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualLengthConstraint.entity1 "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualLengthConstraint.entity1 (Python parameter) — A ConstrainedSketchGeometry object specifying the first line.")*, *[entity2](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualLengthConstraint.entity2 "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualLengthConstraint.entity2 (Python parameter) — A ConstrainedSketchGeometry object specifying the second line.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchConstraint/ConstrainedSketchConstraintModel.py#L83-L107)[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualLengthConstraint "Permalink to this definition")
    :   This method creates an equal length constraint. This constraint applies to lines and constrains them
        such that their lengths are equal.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].EqualLengthConstraint
        ```

        Note

        Check [EqualLengthConstraint on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-equallengthconstraintpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualLengthConstraint-parameters "Permalink to this headline")
        :   entity1[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualLengthConstraint.entity1 "Permalink to this definition")
            :   A ConstrainedSketchGeometry object specifying the first line.

            entity2[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualLengthConstraint.entity2 "Permalink to this definition")
            :   A ConstrainedSketchGeometry object specifying the second line.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualLengthConstraint-returns "Permalink to this headline")
        :   **constraint** – A ConstrainedSketchConstraint object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualLengthConstraint-return-type "Permalink to this headline")
        :   `ConstrainedSketchConstraint`

    EqualRadiusConstraint(*[entity1](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualRadiusConstraint.entity1 "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualRadiusConstraint.entity1 (Python parameter) — A ConstrainedSketchGeometry object specifying the first arc or circle.")*, *[entity2](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualRadiusConstraint.entity2 "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualRadiusConstraint.entity2 (Python parameter) — A ConstrainedSketchGeometry specifying the second arc or circle.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchConstraint/ConstrainedSketchConstraintModel.py#L109-L131)[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualRadiusConstraint "Permalink to this definition")
    :   This method creates an equal radius constraint. This constraint applies to circles and arcs and
        constrains them such that their radii are equal.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].EqualRadiusConstraint
        ```

        Note

        Check [EqualRadiusConstraint on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-equalradiusconstraintpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualRadiusConstraint-parameters "Permalink to this headline")
        :   entity1[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualRadiusConstraint.entity1 "Permalink to this definition")
            :   A ConstrainedSketchGeometry object specifying the first arc or circle.

            entity2[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualRadiusConstraint.entity2 "Permalink to this definition")
            :   A ConstrainedSketchGeometry specifying the second arc or circle.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualRadiusConstraint-returns "Permalink to this headline")
        :   **constraint** – A ConstrainedSketchConstraint object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.EqualRadiusConstraint-return-type "Permalink to this headline")
        :   `ConstrainedSketchConstraint`

    FixedConstraint(*[entity](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.FixedConstraint.entity "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.FixedConstraint.entity (Python parameter) — A ConstrainedSketchGeometry object or a ConstrainedSketchVertex object specifying the item to fix in space.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchConstraint/ConstrainedSketchConstraintModel.py#L133-L155)[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.FixedConstraint "Permalink to this definition")
    :   This method creates a fixed constraint. This constraint applies to a ConstrainedSketchGeometry object
        or a ConstrainedSketchVertex object and constrains them to be fixed in space. Both the location and the
        shape of the sketch geometry is fixed.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].FixedConstraint
        ```

        Note

        Check [FixedConstraint on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fixedconstraintpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.FixedConstraint-parameters "Permalink to this headline")
        :   entity[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.FixedConstraint.entity "Permalink to this definition")
            :   A ConstrainedSketchGeometry object or a ConstrainedSketchVertex object specifying the item to fix in
                space.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.FixedConstraint-returns "Permalink to this headline")
        :   **constraint** – A ConstrainedSketchConstraint object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.FixedConstraint-return-type "Permalink to this headline")
        :   `ConstrainedSketchConstraint`

    HorizontalConstraint(*[entity](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.HorizontalConstraint.entity "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.HorizontalConstraint.entity (Python parameter) — A ConstrainedSketchGeometry object specifying the line to constrain.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchConstraint/ConstrainedSketchConstraintModel.py#L157-L177)[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.HorizontalConstraint "Permalink to this definition")
    :   This method creates a horizontal constraint. This constraint applies to a line and constrains it to
        be horizontal.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].HorizontalConstraint
        ```

        Note

        Check [HorizontalConstraint on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-horizontalconstraintpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.HorizontalConstraint-parameters "Permalink to this headline")
        :   entity[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.HorizontalConstraint.entity "Permalink to this definition")
            :   A ConstrainedSketchGeometry object specifying the line to constrain.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.HorizontalConstraint-returns "Permalink to this headline")
        :   **constraint** – A ConstrainedSketchConstraint object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.HorizontalConstraint-return-type "Permalink to this headline")
        :   `ConstrainedSketchConstraint`

    ParallelConstraint(*[entity1](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.ParallelConstraint.entity1 "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.ParallelConstraint.entity1 (Python parameter) — A ConstrainedSketchGeometry object specifying the first line.")*, *[entity2](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.ParallelConstraint.entity2 "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.ParallelConstraint.entity2 (Python parameter) — A ConstrainedSketchGeometry object specifying the second line.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchConstraint/ConstrainedSketchConstraintModel.py#L201-L225)[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.ParallelConstraint "Permalink to this definition")
    :   This method creates a parallel constraint. This constraint applies to lines and constrains them to be
        parallel.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].ParallelConstraint
        ```

        Note

        Check [ParallelConstraint on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-parallelconstraintpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.ParallelConstraint-parameters "Permalink to this headline")
        :   entity1[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.ParallelConstraint.entity1 "Permalink to this definition")
            :   A ConstrainedSketchGeometry object specifying the first line.

            entity2[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.ParallelConstraint.entity2 "Permalink to this definition")
            :   A ConstrainedSketchGeometry object specifying the second line.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.ParallelConstraint-returns "Permalink to this headline")
        :   **constraint** – A ConstrainedSketchConstraint object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.ParallelConstraint-return-type "Permalink to this headline")
        :   `ConstrainedSketchConstraint`

    PerpendicularConstraint(*[entity1](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.PerpendicularConstraint.entity1 "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.PerpendicularConstraint.entity1 (Python parameter) — A ConstrainedSketchGeometry object specifying the first object.")*, *[entity2](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.PerpendicularConstraint.entity2 "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.PerpendicularConstraint.entity2 (Python parameter) — A ConstrainedSketchGeometry object specifying the second object.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchConstraint/ConstrainedSketchConstraintModel.py#L227-L251)[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.PerpendicularConstraint "Permalink to this definition")
    :   This method creates a perpendicular constraint. This constraint applies to different types of
        ConstrainedSketchGeometry objects and constrains them to be perpendicular to each other.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].PerpendicularConstraint
        ```

        Note

        Check [PerpendicularConstraint on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-perpendicularconstraintpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.PerpendicularConstraint-parameters "Permalink to this headline")
        :   entity1[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.PerpendicularConstraint.entity1 "Permalink to this definition")
            :   A ConstrainedSketchGeometry object specifying the first object.

            entity2[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.PerpendicularConstraint.entity2 "Permalink to this definition")
            :   A ConstrainedSketchGeometry object specifying the second object.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.PerpendicularConstraint-returns "Permalink to this headline")
        :   **constraint** – A ConstrainedSketchConstraint object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.PerpendicularConstraint-return-type "Permalink to this headline")
        :   `ConstrainedSketchConstraint`

    TangentConstraint(*[entity1](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.TangentConstraint.entity1 "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.TangentConstraint.entity1 (Python parameter) — A ConstrainedSketchGeometry object specifying the first object.")*, *[entity2](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.TangentConstraint.entity2 "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.TangentConstraint.entity2 (Python parameter) — A ConstrainedSketchGeometry object specifying the second object.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchConstraint/ConstrainedSketchConstraintModel.py#L285-L309)[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.TangentConstraint "Permalink to this definition")
    :   This method creates a tangent constraint. This constraint applies to different types of
        ConstrainedSketchGeometry objects and constrains them to remain tangential.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].TangentConstraint
        ```

        Note

        Check [TangentConstraint on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-tangentconstraintpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.TangentConstraint-parameters "Permalink to this headline")
        :   entity1[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.TangentConstraint.entity1 "Permalink to this definition")
            :   A ConstrainedSketchGeometry object specifying the first object.

            entity2[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.TangentConstraint.entity2 "Permalink to this definition")
            :   A ConstrainedSketchGeometry object specifying the second object.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.TangentConstraint-returns "Permalink to this headline")
        :   **constraint** – A ConstrainedSketchConstraint object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.TangentConstraint-return-type "Permalink to this headline")
        :   `ConstrainedSketchConstraint`

    VerticalConstraint(*[entity](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.VerticalConstraint.entity "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.VerticalConstraint.entity (Python parameter) — A ConstrainedSketchGeometry object specifying the line to constrain.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchConstraint/ConstrainedSketchConstraintModel.py#L179-L199)[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.VerticalConstraint "Permalink to this definition")
    :   This method creates a vertical constraint. This constraint applies to a line and constrains it to be
        vertical.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].VerticalConstraint
        ```

        Note

        Check [VerticalConstraint on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-verticalconstraintpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.VerticalConstraint-parameters "Permalink to this headline")
        :   entity[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.VerticalConstraint.entity "Permalink to this definition")
            :   A ConstrainedSketchGeometry object specifying the line to constrain.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.VerticalConstraint-returns "Permalink to this headline")
        :   **constraint** – A ConstrainedSketchConstraint object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraintModel.ConstrainedSketchConstraintModel.VerticalConstraint-return-type "Permalink to this headline")
        :   `ConstrainedSketchConstraint`

*class* ConstrainedSketchDimensionModel[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchDimension/ConstrainedSketchDimensionModel.py#L16-L262)[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel "Permalink to this definition")
:   Bases: [`ConstrainedSketchBase`](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchBase "abaqus.Sketcher.ConstrainedSketchBase.ConstrainedSketchBase (Python class)")

    A ConstrainedSketch object contains the entities that are used to create a sketch. The objects include
    ConstrainedSketchGeometry objects contained in the ConstrainedSketchGeometry Repository, such as Line, Arc,
    and Spline. ConstrainedSketchVertex, ConstrainedSketchDimension, ConstrainedSketchConstraint, and
    ConstrainedSketchParameter objects are contained in their respective repositories.

    Note

    This object can be accessed by:

    ```python
    import sketch
    mdb.models[name].sketches[name]
    ```

    Note

    Check [ConstrainedSketchDimensionModel on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?contextscope=all).

    Member Details:

    AngularDimension(*[line1](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.AngularDimension.line1 "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.AngularDimension.line1 (Python parameter) — A ConstrainedSketchGeometry object specifying the first line.")*, *[line2](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.AngularDimension.line2 "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.AngularDimension.line2 (Python parameter) — A ConstrainedSketchGeometry object specifying the second line.")*, *[textPoint](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.AngularDimension.textPoint "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.AngularDimension.textPoint (Python parameter) — A pair of Floats specifying the location of the dimension text.")*, *[value](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.AngularDimension.value "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.AngularDimension.value (Python parameter) — A Float specifying the angle between the two lines.")=`None`*, *[reference](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.AngularDimension.reference "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.AngularDimension.reference (Python parameter) — A Boolean specifying whether the created dimension enforces the above value or if it simply measures the angle between two lines.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchDimension/ConstrainedSketchDimensionModel.py#L30-L66)[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.AngularDimension "Permalink to this definition")
    :   This method constructs a ConstrainedSketchDimension object between two ConstrainedSketchGeometry
        objects, with the given angle between them.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].AngularDimension
        ```

        Note

        Check [AngularDimension on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-angulardimensionpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.AngularDimension-parameters "Permalink to this headline")
        :   line1[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.AngularDimension.line1 "Permalink to this definition")
            :   A ConstrainedSketchGeometry object specifying the first line.

            line2[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.AngularDimension.line2 "Permalink to this definition")
            :   A ConstrainedSketchGeometry object specifying the second line.

            textPoint[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.AngularDimension.textPoint "Permalink to this definition")
            :   A pair of Floats specifying the location of the dimension text.

            value=`None`[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.AngularDimension.value "Permalink to this definition")
            :   A Float specifying the angle between the two lines.

            reference=`0`[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.AngularDimension.reference "Permalink to this definition")
            :   A Boolean specifying whether the created dimension enforces the above value or if it
                simply measures the angle between two lines.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.AngularDimension-returns "Permalink to this headline")
        :   A ConstrainedSketchDimension object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.AngularDimension-return-type "Permalink to this headline")
        :   `dimension`

    DistanceDimension(*[entity1](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.DistanceDimension.entity1 "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.DistanceDimension.entity1 (Python parameter) — A ConstrainedSketchVertex object or ConstrainedSketchGeometry object.")*, *[entity2](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.DistanceDimension.entity2 "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.DistanceDimension.entity2 (Python parameter) — A ConstrainedSketchVertex object or ConstrainedSketchGeometry object.")*, *[textPoint](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.DistanceDimension.textPoint "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.DistanceDimension.textPoint (Python parameter) — A pair of Floats specifying the location of the dimension text.")*, *[value](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.DistanceDimension.value "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.DistanceDimension.value (Python parameter) — A Float specifying the angle between the two lines.")=`None`*, *[reference](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.DistanceDimension.reference "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.DistanceDimension.reference (Python parameter) — A Boolean specifying whether the created dimension enforces the above value or if it simply measures the angle between two lines.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchDimension/ConstrainedSketchDimensionModel.py#L225-L262)[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.DistanceDimension "Permalink to this definition")
    :   This method constructs a ConstrainedSketchDimension object between two ConstrainedSketchGeometry, or
        aConstrainedSketchVertex and ConstrainedSketchGeometry object. A distance dimension specifies the
        shortest distance between two entities.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].DistanceDimension
        ```

        Note

        Check [DistanceDimension on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-distancedimensionpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.DistanceDimension-parameters "Permalink to this headline")
        :   entity1[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.DistanceDimension.entity1 "Permalink to this definition")
            :   A ConstrainedSketchVertex object or ConstrainedSketchGeometry object.

            entity2[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.DistanceDimension.entity2 "Permalink to this definition")
            :   A ConstrainedSketchVertex object or ConstrainedSketchGeometry object.

            textPoint[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.DistanceDimension.textPoint "Permalink to this definition")
            :   A pair of Floats specifying the location of the dimension text.

            value=`None`[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.DistanceDimension.value "Permalink to this definition")
            :   A Float specifying the angle between the two lines.

            reference=`0`[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.DistanceDimension.reference "Permalink to this definition")
            :   A Boolean specifying whether the created dimension enforces the above value or if it
                simply measures the angle between two lines.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.DistanceDimension-returns "Permalink to this headline")
        :   A ConstrainedSketchDimension object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.DistanceDimension-return-type "Permalink to this headline")
        :   `dimension`

    HorizontalDimension(*[vertex1](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.HorizontalDimension.vertex1 "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.HorizontalDimension.vertex1 (Python parameter) — A ConstrainedSketchVertex object specifying the first endpoint.")*, *[vertex2](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.HorizontalDimension.vertex2 "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.HorizontalDimension.vertex2 (Python parameter) — A ConstrainedSketchVertex object specifying the second endpoint.")*, *[textPoint](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.HorizontalDimension.textPoint "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.HorizontalDimension.textPoint (Python parameter) — A pair of Floats specifying the location of the dimension text.")*, *[value](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.HorizontalDimension.value "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.HorizontalDimension.value (Python parameter) — A Float distance between the two vertices.")=`None`*, *[reference](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.HorizontalDimension.reference "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.HorizontalDimension.reference (Python parameter) — A Boolean specifying whether the created dimension enforces the above value or if it simply measures the distance between the two vertices.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchDimension/ConstrainedSketchDimensionModel.py#L68-L104)[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.HorizontalDimension "Permalink to this definition")
    :   This method constructs a ConstrainedSketchDimension object between two vertices. A horizontal
        dimension indicates the horizontal distance along the **X** axis between two vertices.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].HorizontalDimension
        ```

        Note

        Check [HorizontalDimension on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-horizontaldimensionpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.HorizontalDimension-parameters "Permalink to this headline")
        :   vertex1[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.HorizontalDimension.vertex1 "Permalink to this definition")
            :   A ConstrainedSketchVertex object specifying the first endpoint.

            vertex2[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.HorizontalDimension.vertex2 "Permalink to this definition")
            :   A ConstrainedSketchVertex object specifying the second endpoint.

            textPoint[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.HorizontalDimension.textPoint "Permalink to this definition")
            :   A pair of Floats specifying the location of the dimension text.

            value=`None`[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.HorizontalDimension.value "Permalink to this definition")
            :   A Float distance between the two vertices.

            reference=`0`[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.HorizontalDimension.reference "Permalink to this definition")
            :   A Boolean specifying whether the created dimension enforces the above value or if it
                simply measures the distance between the two vertices.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.HorizontalDimension-returns "Permalink to this headline")
        :   A ConstrainedSketchDimension object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.HorizontalDimension-return-type "Permalink to this headline")
        :   `dimension`

    ObliqueDimension(*[vertex1](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.ObliqueDimension.vertex1 "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.ObliqueDimension.vertex1 (Python parameter) — A ConstrainedSketchVertex object specifying the first endpoint.")*, *[vertex2](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.ObliqueDimension.vertex2 "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.ObliqueDimension.vertex2 (Python parameter) — A ConstrainedSketchVertex object specifying the second endpoint.")*, *[textPoint](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.ObliqueDimension.textPoint "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.ObliqueDimension.textPoint (Python parameter) — A pair of Floats specifying the location of the dimension text.")*, *[value](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.ObliqueDimension.value "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.ObliqueDimension.value (Python parameter) — A Float specifying the distance between the two ConstrainedSketchVertex objects.")=`None`*, *[reference](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.ObliqueDimension.reference "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.ObliqueDimension.reference (Python parameter) — A Boolean specifying whether the created dimension enforces the above value or if it simply measures the distance between the two vertices.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchDimension/ConstrainedSketchDimensionModel.py#L106-L142)[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.ObliqueDimension "Permalink to this definition")
    :   This method constructs a ConstrainedSketchDimension object between two vertices. An oblique dimension
        indicates the distance between two vertices.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].ObliqueDimension
        ```

        Note

        Check [ObliqueDimension on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-obliquedimensionpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.ObliqueDimension-parameters "Permalink to this headline")
        :   vertex1[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.ObliqueDimension.vertex1 "Permalink to this definition")
            :   A ConstrainedSketchVertex object specifying the first endpoint.

            vertex2[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.ObliqueDimension.vertex2 "Permalink to this definition")
            :   A ConstrainedSketchVertex object specifying the second endpoint.

            textPoint[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.ObliqueDimension.textPoint "Permalink to this definition")
            :   A pair of Floats specifying the location of the dimension text.

            value=`None`[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.ObliqueDimension.value "Permalink to this definition")
            :   A Float specifying the distance between the two ConstrainedSketchVertex objects.

            reference=`0`[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.ObliqueDimension.reference "Permalink to this definition")
            :   A Boolean specifying whether the created dimension enforces the above value or if it
                simply measures the distance between the two vertices.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.ObliqueDimension-returns "Permalink to this headline")
        :   A ConstrainedSketchDimension object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.ObliqueDimension-return-type "Permalink to this headline")
        :   `dimension`

    RadialDimension(*[curve](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.RadialDimension.curve "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.RadialDimension.curve (Python parameter) — A ConstrainedSketchGeometry object specifying the circular or elliptical arc.")*, *[textPoint](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.RadialDimension.textPoint "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.RadialDimension.textPoint (Python parameter) — A pair of Floats specifying the location of the dimension text.")*, *[value](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.RadialDimension.value "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.RadialDimension.value (Python parameter) — A Float specifying the radius of the arc, circle or ellipse.")=`None`*, *[reference](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.RadialDimension.reference "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.RadialDimension.reference (Python parameter) — A Boolean specifying whether the created dimension enforces the above value or if it simply measures the angle between two lines.")=`0`*, *[majorRadius](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.RadialDimension.majorRadius "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.RadialDimension.majorRadius (Python parameter) — A Float specifying the major Radius if curve is an ellipse.")=`None`*, *[minorRadius](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.RadialDimension.minorRadius "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.RadialDimension.minorRadius (Python parameter) — A Float specifying the minor Radius if curve is an ellipse.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchDimension/ConstrainedSketchDimensionModel.py#L144-L185)[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.RadialDimension "Permalink to this definition")
    :   This method constructs a ConstrainedSketchDimension object on a circular or elliptical arc. A radial
        dimension indicates the radius of an arc or circle or the major or minor radius of an ellipse.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].RadialDimension
        ```

        Note

        Check [RadialDimension on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-radialdimensionpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.RadialDimension-parameters "Permalink to this headline")
        :   curve[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.RadialDimension.curve "Permalink to this definition")
            :   A ConstrainedSketchGeometry object specifying the circular or elliptical arc.

            textPoint[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.RadialDimension.textPoint "Permalink to this definition")
            :   A pair of Floats specifying the location of the dimension text.

            value=`None`[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.RadialDimension.value "Permalink to this definition")
            :   A Float specifying the radius of the arc, circle or ellipse.

            reference=`0`[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.RadialDimension.reference "Permalink to this definition")
            :   A Boolean specifying whether the created dimension enforces the above value or if it
                simply measures the angle between two lines.

            majorRadius=`None`[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.RadialDimension.majorRadius "Permalink to this definition")
            :   A Float specifying the major Radius if **curve** is an ellipse. This is mutually exclusive
                with **value** and **minorRadius**.

            minorRadius=`None`[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.RadialDimension.minorRadius "Permalink to this definition")
            :   A Float specifying the minor Radius if **curve** is an ellipse. This is mutually exclusive
                with **value** and **majorRadius**.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.RadialDimension-returns "Permalink to this headline")
        :   A ConstrainedSketchDimension object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.RadialDimension-return-type "Permalink to this headline")
        :   `dimension`

    VerticalDimension(*[vertex1](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.VerticalDimension.vertex1 "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.VerticalDimension.vertex1 (Python parameter) — A ConstrainedSketchVertex object specifying the first endpoint.")*, *[vertex2](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.VerticalDimension.vertex2 "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.VerticalDimension.vertex2 (Python parameter) — A ConstrainedSketchVertex object specifying the second endpoint.")*, *[textPoint](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.VerticalDimension.textPoint "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.VerticalDimension.textPoint (Python parameter) — A pair of Floats specifying the location of the dimension text.")*, *[value](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.VerticalDimension.value "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.VerticalDimension.value (Python parameter) — A Float specifying the angle between the two lines.")=`None`*, *[reference](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.VerticalDimension.reference "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.VerticalDimension.reference (Python parameter) — A Boolean specifying whether the created dimension enforces the above value or if it simply measures the angle between two lines.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchDimension/ConstrainedSketchDimensionModel.py#L187-L223)[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.VerticalDimension "Permalink to this definition")
    :   This method constructs a ConstrainedSketchDimension between two vertices. A vertical dimension
        controls the vertical distance along the **Y** axis between two vertices.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].VerticalDimension
        ```

        Note

        Check [VerticalDimension on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-verticaldimensionpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.VerticalDimension-parameters "Permalink to this headline")
        :   vertex1[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.VerticalDimension.vertex1 "Permalink to this definition")
            :   A ConstrainedSketchVertex object specifying the first endpoint.

            vertex2[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.VerticalDimension.vertex2 "Permalink to this definition")
            :   A ConstrainedSketchVertex object specifying the second endpoint.

            textPoint[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.VerticalDimension.textPoint "Permalink to this definition")
            :   A pair of Floats specifying the location of the dimension text.

            value=`None`[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.VerticalDimension.value "Permalink to this definition")
            :   A Float specifying the angle between the two lines.

            reference=`0`[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.VerticalDimension.reference "Permalink to this definition")
            :   A Boolean specifying whether the created dimension enforces the above value or if it
                simply measures the angle between two lines.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.VerticalDimension-returns "Permalink to this headline")
        :   A ConstrainedSketchDimension object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimensionModel.ConstrainedSketchDimensionModel.VerticalDimension-return-type "Permalink to this headline")
        :   `dimension`

*class* ConstrainedSketchGeometry[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/getPointAtDistance.py#L8-L34)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.ConstrainedSketchGeometry "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The ConstrainedSketchGeometry object stores the geometry of a sketch, such as lines, circles, arcs, and
    construction lines.

    Note

    This object can be accessed by:

    ```python
    import sketch
    mdb.models[name].sketches[name].geometry[i]
    mdb.models[name].sketches[name].geometry[i][i]
    ```

    Note

    Check [ConstrainedSketchGeometry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometrypyc.htm?contextscope=all).

    Member Details:

    curveType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/getPointAtDistance.py)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.ConstrainedSketchGeometry.curveType "Permalink to this definition")
    :   A SymbolicConstant specifying the geometry of the sketch entity. Possible values are
        ARC, CIRCLE, ELLIPSE, LINE, and SPLINE.

    id : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/getPointAtDistance.py#L21-L22)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.ConstrainedSketchGeometry.id "Permalink to this definition")
    :   An Int specifying the index of the sketch entity in the ConstrainedSketchGeometryArray.

    pointOn : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/getPointAtDistance.py#L8-L34)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.ConstrainedSketchGeometry.pointOn "Permalink to this definition")
    :   A tuple of Floats specifying the **X** and\*Y\*-coordinates of a point located on the
        geometry.

    type : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/getPointAtDistance.py)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.ConstrainedSketchGeometry.type "Permalink to this definition")
    :   A SymbolicConstant specifying the type of sketch entity. Possible values are REGULAR,
        REFERENCE, and CONSTRUCTION.

*class* ConstrainedSketchGeometryModel[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/ConstrainedSketchGeometryModel.py#L15-L388)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel "Permalink to this definition")
:   Bases: [`ConstrainedSketchBase`](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchBase "abaqus.Sketcher.ConstrainedSketchBase.ConstrainedSketchBase (Python class)")

    A ConstrainedSketch object contains the entities that are used to create a sketch. The objects include
    ConstrainedSketchGeometry objects contained in the ConstrainedSketchGeometry Repository, such as Line, Arc,
    and Spline. ConstrainedSketchVertex, ConstrainedSketchDimension, ConstrainedSketchConstraint, and
    ConstrainedSketchParameter objects are contained in their respective repositories.

    Note

    This object can be accessed by:

    ```python
    import sketch
    mdb.models[name].sketches[name]
    ```

    Note

    Check [ConstrainedSketchGeometryModel on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?contextscope=all).

    Member Details:

    Arc3Points(*[point1](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Arc3Points.point1 "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Arc3Points.point1 (Python parameter) — A pair of Floats specifying the first endpoint of the arc.")*, *[point2](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Arc3Points.point2 "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Arc3Points.point2 (Python parameter) — A pair of Floats specifying the second endpoint of the arc.")*, *[point3](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Arc3Points.point3 "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Arc3Points.point3 (Python parameter) — A pair of Floats specifying the third point on the arc.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/ConstrainedSketchGeometryModel.py#L29-L54)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Arc3Points "Permalink to this definition")
    :   This method constructs an arc using a two endpoints and an intermediate third point on the arc.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].Arc3Points
        ```

        Note

        Check [Arc3Points on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-arc3pointspyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Arc3Points-parameters "Permalink to this headline")
        :   point1[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Arc3Points.point1 "Permalink to this definition")
            :   A pair of Floats specifying the first endpoint of the arc.

            point2[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Arc3Points.point2 "Permalink to this definition")
            :   A pair of Floats specifying the second endpoint of the arc.

            point3[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Arc3Points.point3 "Permalink to this definition")
            :   A pair of Floats specifying the third point on the arc.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Arc3Points-returns "Permalink to this headline")
        :   **geometry** – A ConstrainedSketchGeometry object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Arc3Points-return-type "Permalink to this headline")
        :   `ConstrainedSketchGeometry`

    ArcByCenterEnds(*[center](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByCenterEnds.center "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByCenterEnds.center (Python parameter) — A pair of Floats specifying the center point of the arc.")*, *[point1](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByCenterEnds.point1 "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByCenterEnds.point1 (Python parameter) — A pair of Floats specifying the first endpoint of the arc.")*, *[point2](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByCenterEnds.point2 "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByCenterEnds.point2 (Python parameter) — A pair of Floats specifying the second endpoint of the arc.")*, *[direction](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByCenterEnds.direction "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByCenterEnds.direction (Python parameter) — A SymbolicConstant specifying the direction of the arc.")=`abaqusConstants.COUNTERCLOCKWISE`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/ConstrainedSketchGeometryModel.py#L56-L95)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByCenterEnds "Permalink to this definition")
    :   This method constructs an arc using a center point and two vertices. The Arc object is added to the
        geometry repository of the ConstrainedSketch object. The arc is created in a clockwise fashion from
        **point1** to **point2**.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].ArcByCenterEnds
        ```

        Note

        Check [ArcByCenterEnds on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-arcbycenterendspyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByCenterEnds-parameters "Permalink to this headline")
        :   center[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByCenterEnds.center "Permalink to this definition")
            :   A pair of Floats specifying the center point of the arc.

            point1[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByCenterEnds.point1 "Permalink to this definition")
            :   A pair of Floats specifying the first endpoint of the arc.

            point2[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByCenterEnds.point2 "Permalink to this definition")
            :   A pair of Floats specifying the second endpoint of the arc.

            direction=`abaqusConstants.COUNTERCLOCKWISE`[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByCenterEnds.direction "Permalink to this definition")
            :   A SymbolicConstant specifying the direction of the arc. Possible values are CLOCKWISE
                and COUNTERCLOCKWISE.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByCenterEnds-returns "Permalink to this headline")
        :   **geometry** – A ConstrainedSketchGeometry object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByCenterEnds-return-type "Permalink to this headline")
        :   `ConstrainedSketchGeometry`

        Raises:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByCenterEnds-raises "Permalink to this headline")
        :   [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.13)") – If incompatible data are given, the second endpoint is ignored

    ArcByStartEndTangent(*[point1](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByStartEndTangent.point1 "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByStartEndTangent.point1 (Python parameter) — A pair of Floats specifying the first endpoint of the arc.")*, *[point2](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByStartEndTangent.point2 "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByStartEndTangent.point2 (Python parameter) — A pair of Floats specifying the second endpoint of the arc.")*, *[vector](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByStartEndTangent.vector "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByStartEndTangent.vector (Python parameter) — A sequence of two Floats specifying the start direction for constructing the arc.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/ConstrainedSketchGeometryModel.py#L97-L123)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByStartEndTangent "Permalink to this definition")
    :   This method constructs an arc using two vertices. The Arc object is added to the geometry repository
        of the ConstrainedSketch object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].ArcByStartEndTangent
        ```

        Note

        Check [ArcByStartEndTangent on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-arcbystartendtangentpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByStartEndTangent-parameters "Permalink to this headline")
        :   point1[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByStartEndTangent.point1 "Permalink to this definition")
            :   A pair of Floats specifying the first endpoint of the arc.

            point2[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByStartEndTangent.point2 "Permalink to this definition")
            :   A pair of Floats specifying the second endpoint of the arc.

            vector[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByStartEndTangent.vector "Permalink to this definition")
            :   A sequence of two Floats specifying the start direction for constructing the arc.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByStartEndTangent-returns "Permalink to this headline")
        :   **geometry** – A ConstrainedSketchGeometry object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ArcByStartEndTangent-return-type "Permalink to this headline")
        :   `ConstrainedSketchGeometry`

    CircleByCenterPerimeter(*[center](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.CircleByCenterPerimeter.center "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.CircleByCenterPerimeter.center (Python parameter) — A pair of Floats specifying the center point of the circle.")*, *[point1](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.CircleByCenterPerimeter.point1 "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.CircleByCenterPerimeter.point1 (Python parameter) — A pair of Floats specifying a point on the perimeter of the circle.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/ConstrainedSketchGeometryModel.py#L125-L147)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.CircleByCenterPerimeter "Permalink to this definition")
    :   This method constructs a circle using a center point and a point on the perimeter. The circle is
        added to the geometry repository of the ConstrainedSketch object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].CircleByCenterPerimeter
        ```

        Note

        Check [CircleByCenterPerimeter on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-circlebycenterperimeterpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.CircleByCenterPerimeter-parameters "Permalink to this headline")
        :   center[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.CircleByCenterPerimeter.center "Permalink to this definition")
            :   A pair of Floats specifying the center point of the circle.

            point1[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.CircleByCenterPerimeter.point1 "Permalink to this definition")
            :   A pair of Floats specifying a point on the perimeter of the circle.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.CircleByCenterPerimeter-returns "Permalink to this headline")
        :   **geometry** – A ConstrainedSketchGeometry object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.CircleByCenterPerimeter-return-type "Permalink to this headline")
        :   `ConstrainedSketchGeometry`

    ConstructionCircleByCenterPerimeter(*[center](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ConstructionCircleByCenterPerimeter.center "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ConstructionCircleByCenterPerimeter.center (Python parameter) — A pair of Floats specifying the center point of the construction circle.")*, *[point1](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ConstructionCircleByCenterPerimeter.point1 "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ConstructionCircleByCenterPerimeter.point1 (Python parameter) — A pair of Floats specifying a point on the perimeter of the construction circle.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/ConstrainedSketchGeometryModel.py#L149-L173)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ConstructionCircleByCenterPerimeter "Permalink to this definition")
    :   This method constructs a construction circle using a center point and a point on the perimeter. The
        circle is added to the geometry repository of the ConstrainedSketch object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].ConstructionCircleByCenterPerimeter
        ```

        Note

        Check [ConstructionCircleByCenterPerimeter on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constructioncirclebycenterperimeterpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ConstructionCircleByCenterPerimeter-parameters "Permalink to this headline")
        :   center[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ConstructionCircleByCenterPerimeter.center "Permalink to this definition")
            :   A pair of Floats specifying the center point of the construction circle.

            point1[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ConstructionCircleByCenterPerimeter.point1 "Permalink to this definition")
            :   A pair of Floats specifying a point on the perimeter of the construction circle.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ConstructionCircleByCenterPerimeter-returns "Permalink to this headline")
        :   **geometry** – A ConstrainedSketchGeometry object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ConstructionCircleByCenterPerimeter-return-type "Permalink to this headline")
        :   `ConstrainedSketchGeometry`

    ConstructionLine(*[point1](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ConstructionLine.point1 "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ConstructionLine.point1 (Python parameter) — A pair of Floats specifying the first endpoint.")*, *[point2](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ConstructionLine.point2 "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ConstructionLine.point2 (Python parameter) — A pair of Floats specifying the second endpoint.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/ConstrainedSketchGeometryModel.py#L273-L294)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ConstructionLine "Permalink to this definition")
    :   This method creates an oblique construction line that runs between two given points.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].ConstructionLine
        ```

        Note

        Check [ConstructionLine on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constructionlinepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ConstructionLine-parameters "Permalink to this headline")
        :   point1[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ConstructionLine.point1 "Permalink to this definition")
            :   A pair of Floats specifying the first endpoint.

            point2[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ConstructionLine.point2 "Permalink to this definition")
            :   A pair of Floats specifying the second endpoint.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ConstructionLine-returns "Permalink to this headline")
        :   **geometry** – A ConstrainedSketchGeometry object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.ConstructionLine-return-type "Permalink to this headline")
        :   `ConstrainedSketchGeometry`

    EllipseByCenterPerimeter(*[center](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.EllipseByCenterPerimeter.center "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.EllipseByCenterPerimeter.center (Python parameter) — A pair of Floats specifying the center point of the ellipse.")*, *[axisPoint1](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.EllipseByCenterPerimeter.axisPoint1 "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.EllipseByCenterPerimeter.axisPoint1 (Python parameter) — A pair of Floats specifying the major or minor axis point of the ellipse.")*, *[axisPoint2](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.EllipseByCenterPerimeter.axisPoint2 "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.EllipseByCenterPerimeter.axisPoint2 (Python parameter) — A pair of Floats specifying the minor or major axis point of the ellipse.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/ConstrainedSketchGeometryModel.py#L175-L201)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.EllipseByCenterPerimeter "Permalink to this definition")
    :   This method constructs an ellipse using a center point, a major axis point, and a minor axis point.
        The ellipse is added to the geometry repository of the ConstrainedSketch object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].EllipseByCenterPerimeter
        ```

        Note

        Check [EllipseByCenterPerimeter on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-ellipsebycenterperimeterpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.EllipseByCenterPerimeter-parameters "Permalink to this headline")
        :   center[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.EllipseByCenterPerimeter.center "Permalink to this definition")
            :   A pair of Floats specifying the center point of the ellipse.

            axisPoint1[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.EllipseByCenterPerimeter.axisPoint1 "Permalink to this definition")
            :   A pair of Floats specifying the major or minor axis point of the ellipse.

            axisPoint2[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.EllipseByCenterPerimeter.axisPoint2 "Permalink to this definition")
            :   A pair of Floats specifying the minor or major axis point of the ellipse.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.EllipseByCenterPerimeter-returns "Permalink to this headline")
        :   **geometry** – A ConstrainedSketchGeometry object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.EllipseByCenterPerimeter-return-type "Permalink to this headline")
        :   `ConstrainedSketchGeometry`

    FilletByRadius(*[radius](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.FilletByRadius.radius "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.FilletByRadius.radius (Python parameter) — A Float specifying the radius of the fillet arc.")*, *[curve1](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.FilletByRadius.curve1 "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.FilletByRadius.curve1 (Python parameter) — A ConstrainedSketchGeometry object specifying the first curve.")*, *[nearPoint1](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.FilletByRadius.nearPoint1 "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.FilletByRadius.nearPoint1 (Python parameter) — A pair of Floats specifying a point on the sketch near where the user wishes the fillet to intersect with curve1.")*, *[curve2](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.FilletByRadius.curve2 "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.FilletByRadius.curve2 (Python parameter) — A ConstrainedSketchGeometry object specifying the second curve.")*, *[nearPoint2](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.FilletByRadius.nearPoint2 "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.FilletByRadius.nearPoint2 (Python parameter) — A pair of Floats specifying a point on the sketch near where the user wishes the fillet to intersect with curve2.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/ConstrainedSketchGeometryModel.py#L203-L248)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.FilletByRadius "Permalink to this definition")
    :   This method constructs a fillet arc of a given radius between two curves. The fillet is added to the
        geometry repository of the ConstrainedSketch object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].FilletByRadius
        ```

        Note

        Check [FilletByRadius on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-filletbyradiuspyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.FilletByRadius-parameters "Permalink to this headline")
        :   radius[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.FilletByRadius.radius "Permalink to this definition")
            :   A Float specifying the radius of the fillet arc. Possible values are Floats > 0.

            curve1[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.FilletByRadius.curve1 "Permalink to this definition")
            :   A ConstrainedSketchGeometry object specifying the first curve.

            nearPoint1[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.FilletByRadius.nearPoint1 "Permalink to this definition")
            :   A pair of Floats specifying a point on the sketch near where the user wishes the fillet
                to intersect with **curve1**. This point does not need to be on\*curve1\*; it is used as a
                hint to draw the fillet.

            curve2[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.FilletByRadius.curve2 "Permalink to this definition")
            :   A ConstrainedSketchGeometry object specifying the second curve.

            nearPoint2[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.FilletByRadius.nearPoint2 "Permalink to this definition")
            :   A pair of Floats specifying a point on the sketch near where the user wishes the fillet
                to intersect with **curve2**. This point does not need to be on **curve2**; it is used as a
                hint to draw the fillet.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.FilletByRadius-returns "Permalink to this headline")
        :   **geometry** – A ConstrainedSketchGeometry object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.FilletByRadius-return-type "Permalink to this headline")
        :   `ConstrainedSketchGeometry`

        Raises:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.FilletByRadius-raises "Permalink to this headline")
        :   **Range Error** – cannot construct the Fillet specified,
            If the radius given cannot be used to create a fillet between the two curves given.

    Line(*[point1](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Line.point1 "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Line.point1 (Python parameter) — A pair of Floats specifying the first endpoint.")*, *[point2](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Line.point2 "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Line.point2 (Python parameter) — A pair of Floats specifying the second endpoint.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/ConstrainedSketchGeometryModel.py#L250-L271)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Line "Permalink to this definition")
    :   This method creates a line between two given points.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].Line
        ```

        Note

        Check [Line on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-linepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Line-parameters "Permalink to this headline")
        :   point1[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Line.point1 "Permalink to this definition")
            :   A pair of Floats specifying the first endpoint.

            point2[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Line.point2 "Permalink to this definition")
            :   A pair of Floats specifying the second endpoint.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Line-returns "Permalink to this headline")
        :   **geometry** – A ConstrainedSketchGeometry object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Line-return-type "Permalink to this headline")
        :   `ConstrainedSketchGeometry`

    Spline(*[points](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Spline.points "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Spline.points (Python parameter) — A sequence of pairs of Floats specifying the points through which the spline passes.")*, *[constrainPoints](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Spline.constrainPoints "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Spline.constrainPoints (Python parameter) — A Boolean that determines whether the points given are to constrained to always remain on the Spline.")=`True`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/ConstrainedSketchGeometryModel.py#L296-L319)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Spline "Permalink to this definition")
    :   This method creates a spline curve running through a sequence of points.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].Spline
        ```

        Note

        Check [Spline on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-splinepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Spline-parameters "Permalink to this headline")
        :   points[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Spline.points "Permalink to this definition")
            :   A sequence of pairs of Floats specifying the points through which the spline passes.

            constrainPoints=`True`[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Spline.constrainPoints "Permalink to this definition")
            :   A Boolean that determines whether the points given are to constrained to always remain
                on the Spline. The default is True. For a large sequence of **points**, significant
                performance gains may be achieved by setting the value to False.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Spline-returns "Permalink to this headline")
        :   **geometry** – A ConstrainedSketchGeometry object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Spline-return-type "Permalink to this headline")
        :   `ConstrainedSketchGeometry`

    Spot(*[point](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Spot.point "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Spot.point (Python parameter) — A pair of Floats specifying the coordinates of the spot construction point.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/ConstrainedSketchGeometryModel.py#L321-L341)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Spot "Permalink to this definition")
    :   This method creates a spot construction point located at the specified coordinates. The spot is added
        to the vertex repository of the ConstrainedSketch object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].Spot
        ```

        Note

        Check [Spot on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-spotpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Spot-parameters "Permalink to this headline")
        :   point[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Spot.point "Permalink to this definition")
            :   A pair of Floats specifying the coordinates of the spot construction point.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Spot-returns "Permalink to this headline")
        :   **geometry** – A ConstrainedSketchGeometry object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.Spot-return-type "Permalink to this headline")
        :   `ConstrainedSketchGeometry`

    getPointAtDistance(*[point](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.getPointAtDistance.point "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.getPointAtDistance.point (Python parameter) — A pair of Floats specifying the point from which the distance is to be measured.")*, *[distance](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.getPointAtDistance.distance "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.getPointAtDistance.distance (Python parameter) — A float specifying the arc length distance along the ConstrainedSketchGeometry from the point at which the required point is situated.")*, *[percentage](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.getPointAtDistance.percentage "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.getPointAtDistance.percentage (Python parameter) — A Boolean that specifies if the distance is an absolute distance or is a fraction relative to the length of the ConstrainedSketchGeometry object.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/ConstrainedSketchGeometryModel.py#L366-L388)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.getPointAtDistance "Permalink to this definition")
    :   This method returns a point offset along the given ConstrainedSketchGeometry from the given end by a
        specified arc length distance or a percentage of the total length of the ConstrainedSketchGeometry
        object.

        Note

        Check [ConstrainedSketchGeometryModel.getPointAtDistance on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?contextscope=all#simaker-modelgetpointatdistancepyc).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.getPointAtDistance-parameters "Permalink to this headline")
        :   point[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.getPointAtDistance.point "Permalink to this definition")
            :   A pair of Floats specifying the point from which the distance is to be measured.

            distance[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.getPointAtDistance.distance "Permalink to this definition")
            :   A float specifying the arc length distance along the ConstrainedSketchGeometry from the
                **point** at which the required point is situated.

            percentage=`0`[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.getPointAtDistance.percentage "Permalink to this definition")
            :   A Boolean that specifies if the **distance** is an absolute distance or is a fraction
                relative to the length of the ConstrainedSketchGeometry object.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.getPointAtDistance-returns "Permalink to this headline")
        :   **points** – A pair of floats representing the point along the edge

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.getPointAtDistance-return-type "Permalink to this headline")
        :   `Sequence[float]`

    getSize()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/ConstrainedSketchGeometryModel.py#L355-L364)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.getSize "Permalink to this definition")
    :   This method returns the length of the given ConstrainedSketchGeometry object.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.getSize-returns "Permalink to this headline")
        :   **length** – The length of the given ConstrainedSketchGeometry

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.getSize-return-type "Permalink to this headline")
        :   [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")

    getVertices()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/ConstrainedSketchGeometryModel.py#L343-L353)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.getVertices "Permalink to this definition")
    :   This method returns an list of ConstrainedSketchVertex objects which are a part of the given
        ConstrainedSketchGeometry object.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.getVertices-returns "Permalink to this headline")
        :   **vertices** – A list of ConstrainedSketchVertex objects

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryModel.ConstrainedSketchGeometryModel.getVertices-return-type "Permalink to this headline")
        :   `list[ConstrainedSketchVertex]`

*class* ConstrainedSketchParameterModel[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchParameter/ConstrainedSketchParameterModel.py#L9-L59)[¶](#abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameterModel.ConstrainedSketchParameterModel "Permalink to this definition")
:   Bases: [`ConstrainedSketchBase`](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchBase "abaqus.Sketcher.ConstrainedSketchBase.ConstrainedSketchBase (Python class)")

    A ConstrainedSketch object contains the entities that are used to create a sketch. The objects include
    ConstrainedSketchGeometry objects contained in the ConstrainedSketchGeometry Repository, such as Line, Arc,
    and Spline. ConstrainedSketchVertex, ConstrainedSketchDimension, ConstrainedSketchConstraint, and
    ConstrainedSketchParameter objects are contained in their respective repositories.

    Note

    This object can be accessed by:

    ```python
    import sketch
    mdb.models[name].sketches[name]
    ```

    Note

    Check [ConstrainedSketchParameterModel on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?contextscope=all).

    Member Details:

    ConstrainedSketchParameter(*[name](#abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameterModel.ConstrainedSketchParameterModel.ConstrainedSketchParameter.name "abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameterModel.ConstrainedSketchParameterModel.ConstrainedSketchParameter.name (Python parameter) — A String specifying the name of the ConstrainedSketchParameter object.")*, *[path](#abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameterModel.ConstrainedSketchParameterModel.ConstrainedSketchParameter.path "abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameterModel.ConstrainedSketchParameterModel.ConstrainedSketchParameter.path (Python parameter) — A String specifying the ConstrainedSketchDimension object with which this parameter is associated.")=`''`*, *[expression](#abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameterModel.ConstrainedSketchParameterModel.ConstrainedSketchParameter.expression "abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameterModel.ConstrainedSketchParameterModel.ConstrainedSketchParameter.expression (Python parameter) — A String specifying the expression or value associated with the ConstrainedSketchParameter.")=`''`*, *[previousParameter](#abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameterModel.ConstrainedSketchParameterModel.ConstrainedSketchParameter.previousParameter "abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameterModel.ConstrainedSketchParameterModel.ConstrainedSketchParameter.previousParameter (Python parameter) — A String specifying the name of the previous ConstrainedSketchParameter, if it exists. The previousParameter argument implies an order among the parameters.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchParameter/ConstrainedSketchParameterModel.py#L23-L59)[¶](#abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameterModel.ConstrainedSketchParameterModel.ConstrainedSketchParameter "Permalink to this definition")
    :   This method creates a parameter and optionally associates a dimension with this parameter.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].ConstrainedSketchParameter
        ```

        Note

        Check [ConstrainedSketchParameter on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchparameterpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameterModel.ConstrainedSketchParameterModel.ConstrainedSketchParameter-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameterModel.ConstrainedSketchParameterModel.ConstrainedSketchParameter.name "Permalink to this definition")
            :   A String specifying the name of the ConstrainedSketchParameter object. No two parameters
                in the same ConstrainedSketch can have the same name.

            path=`''`[¶](#abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameterModel.ConstrainedSketchParameterModel.ConstrainedSketchParameter.path "Permalink to this definition")
            :   A String specifying the ConstrainedSketchDimension object with which this parameter is
                associated.

            expression=`''`[¶](#abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameterModel.ConstrainedSketchParameterModel.ConstrainedSketchParameter.expression "Permalink to this definition")
            :   A String specifying the expression or value associated with the
                ConstrainedSketchParameter.

            previousParameter=`''`[¶](#abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameterModel.ConstrainedSketchParameterModel.ConstrainedSketchParameter.previousParameter "Permalink to this definition")
            :   A String specifying the name of the previous ConstrainedSketchParameter, if it exists.
                The **previousParameter** argument implies an order among the parameters. No two
                parameters can reference the same parameter as the previous parameter.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameterModel.ConstrainedSketchParameterModel.ConstrainedSketchParameter-returns "Permalink to this headline")
        :   **parameter** – A ConstrainedSketchParameter object

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameterModel.ConstrainedSketchParameterModel.ConstrainedSketchParameter-return-type "Permalink to this headline")
        :   [`ConstrainedSketchParameter`](#abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameterModel.ConstrainedSketchParameterModel.ConstrainedSketchParameter "abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameterModel.ConstrainedSketchParameterModel.ConstrainedSketchParameter (Python method) — This method creates a parameter and optionally associates a dimension with this parameter.")

*class* ConstrainedSketchVertex[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchVertex/Spot.py#L8-L42)[¶](#abaqus.Sketcher.ConstrainedSketchVertex.Spot.ConstrainedSketchVertex "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The ConstrainedSketchVertex object stores the vertex position.

    Note

    This object can be accessed by:

    ```python
    import sketch
    mdb.models[name].sketches[name].vertices[i]
    mdb.models[name].sketches[name].vertices[i][i]
    ```

    Note

    Check [ConstrainedSketchVertex on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexpyc.htm?contextscope=all).

    Member Details:

    Spot(*[point](#abaqus.Sketcher.ConstrainedSketchVertex.Spot.ConstrainedSketchVertex.Spot.point "abaqus.Sketcher.ConstrainedSketchVertex.Spot.ConstrainedSketchVertex.Spot.point (Python parameter) — A pair of Floats specifying the coordinates of the construction point.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchVertex/Spot.py#L23-L42)[¶](#abaqus.Sketcher.ConstrainedSketchVertex.Spot.ConstrainedSketchVertex.Spot "Permalink to this definition")
    :   This method creates a spot (construction point) located at the specified coordinates.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].Spot
        ```

        Note

        Check [Spot on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-spotpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchVertex.Spot.ConstrainedSketchVertex.Spot-parameters "Permalink to this headline")
        :   point[¶](#abaqus.Sketcher.ConstrainedSketchVertex.Spot.ConstrainedSketchVertex.Spot.point "Permalink to this definition")
            :   A pair of Floats specifying the coordinates of the construction point.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchVertex.Spot.ConstrainedSketchVertex.Spot-returns "Permalink to this headline")
        :   A ConstrainedSketchVertex object (None if the spot cannot be created).

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchVertex.Spot.ConstrainedSketchVertex.Spot-return-type "Permalink to this headline")
        :   [`ConstrainedSketchVertex`](#abaqus.Sketcher.ConstrainedSketchVertex.Spot.ConstrainedSketchVertex "abaqus.Sketcher.ConstrainedSketchVertex.Spot.ConstrainedSketchVertex (Python class) — Bases: object")

    coords : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchVertex/Spot.py#L20-L21)[¶](#abaqus.Sketcher.ConstrainedSketchVertex.Spot.ConstrainedSketchVertex.coords "Permalink to this definition")
    :   A tuple of Floats specifying the\*X\*-, **Y**, and **Z** coordinates of the sketch vertex.

*class* ConstrainedSketchVertexModel[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchVertex/ConstrainedSketchVertexModel.py#L11-L44)[¶](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchVertexModel "Permalink to this definition")
:   Bases: [`ConstrainedSketchBase`](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchBase "abaqus.Sketcher.ConstrainedSketchBase.ConstrainedSketchBase (Python class)")

    A ConstrainedSketch object contains the entities that are used to create a sketch. The objects include
    ConstrainedSketchGeometry objects contained in the ConstrainedSketchGeometry Repository, such as Line, Arc,
    and Spline. ConstrainedSketchVertex, ConstrainedSketchDimension, ConstrainedSketchConstraint, and
    ConstrainedSketchParameter objects are contained in their respective repositories.

    Note

    This object can be accessed by:

    ```python
    import sketch
    mdb.models[name].sketches[name]
    ```

    Note

    Check [ConstrainedSketchVertexModel on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?contextscope=all).

    Member Details:

    Spot(*[point](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchVertexModel.Spot.point "abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchVertexModel.Spot.point (Python parameter) — A pair of Floats specifying the coordinates of the construction point.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchVertex/ConstrainedSketchVertexModel.py#L25-L44)[¶](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchVertexModel.Spot "Permalink to this definition")
    :   This method creates a spot (construction point) located at the specified coordinates.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].Spot
        ```

        Note

        Check [Spot on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-spotpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchVertexModel.Spot-parameters "Permalink to this headline")
        :   point[¶](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchVertexModel.Spot.point "Permalink to this definition")
            :   A pair of Floats specifying the coordinates of the construction point.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchVertexModel.Spot-returns "Permalink to this headline")
        :   **vertex** – A ConstrainedSketchVertex object (None if the spot cannot be created)

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchVertexModel.Spot-return-type "Permalink to this headline")
        :   `ConstrainedSketchVertex`

*class* ConstrainedSketchBase[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchVertex/ConstrainedSketchVertexModel.py#L26-L61)[¶](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchBase "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    A ConstrainedSketch object contains the entities that are used to create a sketch. The objects include
    ConstrainedSketchGeometry objects contained in the ConstrainedSketchGeometry Repository, such as Line, Arc,
    and Spline. ConstrainedSketchVertex, ConstrainedSketchDimension, ConstrainedSketchConstraint, and
    ConstrainedSketchParameter objects are contained in their respective repositories.

    Note

    This object can be accessed by:

    ```python
    import sketch
    mdb.models[name].sketches[name]
    ```

    Note

    Check [ConstrainedSketchBase on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchpyc.htm?contextscope=all).

    Member Details:

    constraints : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraint.ConstrainedSketchConstraint`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchVertex/ConstrainedSketchVertexModel.py#L40-L41)[¶](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchBase.constraints "Permalink to this definition")
    :   A repository of ConstrainedSketchConstraint objects.

    dimensions : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimension.ConstrainedSketchDimension`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchVertex/ConstrainedSketchVertexModel.py#L43-L44)[¶](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchBase.dimensions "Permalink to this definition")
    :   A repository of ConstrainedSketchDimension objects.

    geometry : --is-rst--:py:class:`~abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryArray.ConstrainedSketchGeometryArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchVertex/ConstrainedSketchVertexModel.py#L46-L48)[¶](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchBase.geometry "Permalink to this definition")
    :   A ConstrainedSketchGeometryArray object specifying the sketch geometry, such as lines,
        arcs, circles, and splines.

    imageOptions : --is-rst--:py:class:`~abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions` = `<abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchVertex/ConstrainedSketchVertexModel.py#L26-L61)[¶](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchBase.imageOptions "Permalink to this definition")
    :   A ConstrainedSketchImageOptions object.

    parameters : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameter.ConstrainedSketchParameter`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchVertex/ConstrainedSketchVertexModel.py#L50-L52)[¶](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchBase.parameters "Permalink to this definition")
    :   A repository of ConstrainedSketchParameter objects specifying sketch parameters, which
        may be associated with dimensions.

    sketchOptions : --is-rst--:py:class:`~abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions` = `<abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchVertex/ConstrainedSketchVertexModel.py#L54-L55)[¶](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchBase.sketchOptions "Permalink to this definition")
    :   A ConstrainedSketchOptions object specifying the sketch option settings.

    vertices : --is-rst--:py:class:`~abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexArray.ConstrainedSketchVertexArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchVertex/ConstrainedSketchVertexModel.py#L57-L58)[¶](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexModel.ConstrainedSketchBase.vertices "Permalink to this definition")
    :   A ConstrainedSketchVertexArray object.

*class* ConstrainedSketchConstraint[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchConstraint/VerticalConstraint.py#L6-L17)[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.VerticalConstraint.ConstrainedSketchConstraint "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The ConstrainedSketchConstraint object stores the constraints associated with a sketch.

    Note

    This object can be accessed by:

    ```python
    import sketch
    mdb.models[name].sketches[name].constraints[i]
    ```

    Note

    Check [ConstrainedSketchConstraint on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchconstraintpyc.htm?contextscope=all).

    Member Details:

*class* ConstrainedSketchDimension[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchDimension/VerticalDimension.py#L6-L17)[¶](#abaqus.Sketcher.ConstrainedSketchDimension.VerticalDimension.ConstrainedSketchDimension "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The ConstrainedSketchDimension object stores the dimensions associated with a sketch.

    Note

    This object can be accessed by:

    ```python
    import sketch
    mdb.models[name].sketches[name].dimensions[i]
    ```

    Note

    Check [ConstrainedSketchDimension on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchdimensionpyc.htm?contextscope=all).

    Member Details:

*class* ConstrainedSketchGeometryArray(*[iterable](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryArray.ConstrainedSketchGeometryArray "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryArray.ConstrainedSketchGeometryArray.__init__.iterable (Python parameter)")=`()`*, */*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/ConstrainedSketchGeometryArray.py#L11-L39)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryArray.ConstrainedSketchGeometryArray "Permalink to this definition")
:   Bases: [`List`](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")[[`ConstrainedSketchGeometry`](#abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.ConstrainedSketchGeometry "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry (Python class)")]

    The ConstrainedSketchGeometryArray is a sequence of ConstrainedSketchGeometry objects.

    Note

    This object can be accessed by:

    ```python
    import sketch
    mdb.models[name].sketches[name].geometry[i]
    ```

    Note

    Check [ConstrainedSketchGeometryArray on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometryarraypyc.htm?contextscope=all).

    Member Details:

    findAt(*[coordinates](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryArray.ConstrainedSketchGeometryArray.findAt.coordinates "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryArray.ConstrainedSketchGeometryArray.findAt.coordinates (Python parameter) — A sequence of Floats specifying the X and Y coordinates of the object to find.")*, *[printWarning](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryArray.ConstrainedSketchGeometryArray.findAt.printWarning "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryArray.ConstrainedSketchGeometryArray.findAt.printWarning (Python parameter) — A Boolean specifying whether a message is to be printed to the CLI if no entity is found at the specified location.")=`True`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/ConstrainedSketchGeometryArray.py#L22-L39)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryArray.ConstrainedSketchGeometryArray.findAt "Permalink to this definition")
    :   This method returns the ConstrainedSketchGeometry object located at the given coordinates.

        Note

        Check [ConstrainedSketchGeometryArray.findAt on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchgeometryarraypyc.htm?contextscope=all#simaker-constrainedsketchgeometryarrayfindatpyc).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryArray.ConstrainedSketchGeometryArray.findAt-parameters "Permalink to this headline")
        :   coordinates[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryArray.ConstrainedSketchGeometryArray.findAt.coordinates "Permalink to this definition")
            :   A sequence of Floats specifying the **X** and **Y** coordinates of the object to find.

            printWarning=`True`[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryArray.ConstrainedSketchGeometryArray.findAt.printWarning "Permalink to this definition")
            :   A Boolean specifying whether a message is to be printed to the CLI if no entity is found
                at the specified location. The default value is True.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryArray.ConstrainedSketchGeometryArray.findAt-returns "Permalink to this headline")
        :   A ConstrainedSketchGeometry object.

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometryArray.ConstrainedSketchGeometryArray.findAt-return-type "Permalink to this headline")
        :   `ConstrainedSketchGeometry`

*class* ConstrainedSketchImageOptions[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchOptions/ConstrainedSketchImageOptions.py#L10-L62)[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The ConstrainedSketchImageOptions object is used to store values and attributes associated with the
    background image for a particular sketch. The ConstrainedSketchImageOptions object has no constructor.

    Note

    This object can be accessed by:

    ```python
    import sketch
    mdb.models[name].sketches[name].imageOptions
    ```

    Note

    Check [ConstrainedSketchImageOptions on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchimageoptionspyc.htm?contextscope=all).

    Member Details:

    setValues(*[imageName](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions.setValues.imageName "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions.setValues.imageName (Python parameter) — A String specifying the name of the image.")=`''`*, *[showImage](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions.setValues.showImage "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions.setValues.showImage (Python parameter) — A Boolean specifying whether an image should be displayed in the sketcher background. The default value is OFF.")=`0`*, *[origin](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions.setValues.origin "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions.setValues.origin (Python parameter) — A pair of Floats specifying the X and Y offsets in millimeters from the lower-left corner of the viewport.")=`()`*, *[xScale](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions.setValues.xScale "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions.setValues.xScale (Python parameter) — A Float specifying the scale applied to the image width.")=`1`*, *[yScale](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions.setValues.yScale "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions.setValues.yScale (Python parameter) — A Float specifying the scale applied to the image height.")=`1`*, *[translucency](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions.setValues.translucency "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions.setValues.translucency (Python parameter) — A Float specifying the translucency factor to use when displaying the image.")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchOptions/ConstrainedSketchImageOptions.py#L22-L62)[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions.setValues "Permalink to this definition")
    :   This method modifies the ConstrainedSketchOptions object.

        Note

        Check [ConstrainedSketchImageOptions.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchimageoptionspyc.htm?contextscope=all#simaker-constrainedsketchimageoptionssetvaluespyc).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions.setValues-parameters "Permalink to this headline")
        :   imageName=`''`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions.setValues.imageName "Permalink to this definition")
            :   A String specifying the name of the image. A list of valid image names is in the
                **images** repository in the **session** object.

            showImage=`0`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions.setValues.showImage "Permalink to this definition")
            :   A Boolean specifying whether an image should be displayed in the sketcher background.
                The default value is OFF.

            origin=`()`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions.setValues.origin "Permalink to this definition")
            :   A pair of Floats specifying the **X** and **Y** offsets in millimeters from the lower-left
                corner of the viewport. The default value is (0, 0).

            xScale=`1`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions.setValues.xScale "Permalink to this definition")
            :   A Float specifying the scale applied to the image width. The default value is 1.0.When
                **xScale** is negative, the image is mirrored about its y-axis but its position is not
                affected.

            yScale=`1`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions.setValues.yScale "Permalink to this definition")
            :   A Float specifying the scale applied to the image height. The default value is 1.0.When
                **yScale** is negative, the image is mirrored about its x-axis but its position is not
                affected.

            translucency=`1`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions.setValues.translucency "Permalink to this definition")
            :   A Float specifying the translucency factor to use when displaying the image. Possible
                values are 0.0 ≤ **translucency** ≤ 1.0 with 0.0 being invisible and 1.0 being opaque.
                The default value is 1.0.

        Raises:[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchImageOptions.ConstrainedSketchImageOptions.setValues-raises "Permalink to this headline")
        :   **RangeError** –

*class* ConstrainedSketchOptions[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchOptions/ConstrainedSketchOptions.py#L17-L130)[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The ConstrainedSketchOptions object is used to store values and attributes associated with a particular
    sketch. The ConstrainedSketchOptions object has no constructor.

    Note

    This object can be accessed by:

    ```python
    import sketch
    mdb.models[name].sketches[name].sketchOptions
    ```

    Note

    Check [ConstrainedSketchOptions on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchoptionspyc.htm?contextscope=all).

    Member Details:

    setValues(*[sheetSize](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.sheetSize "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.sheetSize (Python parameter) — A Float specifying the sheet size.")=`None`*, *[gridSpacing](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.gridSpacing "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.gridSpacing (Python parameter) — A Float specifying the spacing between gridlines.")=`None`*, *[grid](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.grid "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.grid (Python parameter) — A Boolean specifying whether the grid is shown.")=`1`*, *[gridFrequency](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.gridFrequency "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.gridFrequency (Python parameter) — An Int specifying how often gridlines are shown.")=`1`*, *[dimensionTextHeight](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.dimensionTextHeight "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.dimensionTextHeight (Python parameter) — A Float specifying the height of the dimension text in points.")=`12`*, *[decimalPlaces](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.decimalPlaces "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.decimalPlaces (Python parameter) — An Int specifying how many decimal places are shown in dimensions.")=`None`*, *[constructionGeometry](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.constructionGeometry "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.constructionGeometry (Python parameter) — A Boolean specifying whether construction geometry is shown.")=`1`*, *[gridSnap](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.gridSnap "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.gridSnap (Python parameter) — A Boolean specifying whether the cursor snaps to the grid.")=`1`*, *[preselection](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.preselection "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.preselection (Python parameter) — A Boolean specifying whether geometry will be preselected.")=`1`*, *[sheetAuto](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.sheetAuto "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.sheetAuto (Python parameter) — A Boolean specifying if the sheet size and the grid spacing are automatically computed. The default value is ON.")=`1`*, *[gridOrigin](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.gridOrigin "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.gridOrigin (Python parameter) — A sequence of Floats specifying the X - Y coordinates for the origin of the grid.")=`()`*, *[gridAngle](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.gridAngle "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.gridAngle (Python parameter) — A Float specifying the angle of the grid relative to the computer screen.")=`0`*, *[viewStyle](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.viewStyle "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.viewStyle (Python parameter) — A SymbolicConstant specifying the type of sketch displayed in the viewport.")=`abaqusConstants.REGULAR`*, *[addImpliedConstraints](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.addImpliedConstraints "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.addImpliedConstraints (Python parameter) — A Boolean specifying if implied constraints are added during sketching.")=`1`*, *[maxCoplanarEntities](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.maxCoplanarEntities "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.maxCoplanarEntities (Python parameter) — An Int specifying the maximum number of coplanar entities which should be automatically projected from the background, when a sketch based feature is created or edited.")=`300`*, *[autoConstrainAngularTolerance](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.autoConstrainAngularTolerance "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.autoConstrainAngularTolerance (Python parameter) — A Float specifying the angular tolerance in degrees which is used to determine parallel and tangential conditions during the auto-constrain operation.")=`0`*, *[autoConstrainLinearTolerance](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.autoConstrainLinearTolerance "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.autoConstrainLinearTolerance (Python parameter) — A Float specifying the linear tolerance which is used to determine when two points or geometries are coincident during the auto-constrain operation.")=`None`*, *[autoConstrainOptions](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.autoConstrainOptions "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.autoConstrainOptions (Python parameter) — A sequence of SymbolicConstants specifying which type of constraints may be added by the auto-constraint tool.")=`None`*, *[dragMethod](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.dragMethod "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.dragMethod (Python parameter) — A SymbolicConstant specifying the constraint solving mode used by the sketcher during drag operation.")=`abaqusConstants.MINIMUM_MOVE`*, *[editMethod](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.editMethod "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.editMethod (Python parameter) — A SymbolicConstant specifying the constraint solving mode used by the sketcher during regular sketch editing and adding new constraints and dimensions.")=`abaqusConstants.STANDARD`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchOptions/ConstrainedSketchOptions.py#L29-L130)[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues "Permalink to this definition")
    :   This method modifies the ConstrainedSketchOptions object.

        Note

        Check [ConstrainedSketchOptions.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchoptionspyc.htm?contextscope=all#simaker-constrainedsketchoptionssetvaluespyc).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues-parameters "Permalink to this headline")
        :   sheetSize=`None`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.sheetSize "Permalink to this definition")
            :   A Float specifying the sheet size. Possible values are Floats > 0. The default value is
                the **sheetSize** specified with the Sketch method.

            gridSpacing=`None`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.gridSpacing "Permalink to this definition")
            :   A Float specifying the spacing between gridlines. Possible values are Floats > 0. The
                default value is approximately 2.5% of **sheetSize**.

            grid=`1`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.grid "Permalink to this definition")
            :   A Boolean specifying whether the grid is shown. The default value is ON.

            gridFrequency=`1`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.gridFrequency "Permalink to this definition")
            :   An Int specifying how often gridlines are shown. Possible values are **gridFrequency** >
                0. The default value is 1.

            dimensionTextHeight=`12`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.dimensionTextHeight "Permalink to this definition")
            :   A Float specifying the height of the dimension text in points. Possible values are
                Floats > 0. The default value is 12.0.

            decimalPlaces=`None`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.decimalPlaces "Permalink to this definition")
            :   An Int specifying how many decimal places are shown in dimensions. Possible values are 0
                ≤ **decimalPlaces** ≤ 6. The initial value depends on the value of **sheetSize**.

            constructionGeometry=`1`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.constructionGeometry "Permalink to this definition")
            :   A Boolean specifying whether construction geometry is shown. The default value is ON.

            gridSnap=`1`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.gridSnap "Permalink to this definition")
            :   A Boolean specifying whether the cursor snaps to the grid. The default value is ON.

            preselection=`1`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.preselection "Permalink to this definition")
            :   A Boolean specifying whether geometry will be preselected. The default value is ON.

            sheetAuto=`1`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.sheetAuto "Permalink to this definition")
            :   A Boolean specifying if the sheet size and the grid spacing are automatically computed.
                The default value is ON.

            gridOrigin=`()`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.gridOrigin "Permalink to this definition")
            :   A sequence of Floats specifying the **X - Y** coordinates for the origin of the grid. The
                default value is (0, 0).

            gridAngle=`0`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.gridAngle "Permalink to this definition")
            :   A Float specifying the angle of the grid relative to the computer screen. The default
                value is 0.0.

            viewStyle=`abaqusConstants.REGULAR`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.viewStyle "Permalink to this definition")
            :   A SymbolicConstant specifying the type of sketch displayed in the viewport. Possible
                values are REGULAR and AXISYM. The default value is REGULAR.

            addImpliedConstraints=`1`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.addImpliedConstraints "Permalink to this definition")
            :   A Boolean specifying if implied constraints are added during sketching. The default
                value is ON.

            maxCoplanarEntities=`300`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.maxCoplanarEntities "Permalink to this definition")
            :   An Int specifying the maximum number of coplanar entities which should be automatically
                projected from the background, when a sketch based feature is created or edited. When
                this value is exceeded no entities are automatically projected and a warning issued.
                Possible values are **maxCoplanarEntities** > 0. The default value is 300.

            autoConstrainAngularTolerance=`0`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.autoConstrainAngularTolerance "Permalink to this definition")
            :   A Float specifying the angular tolerance in degrees which is used to determine parallel
                and tangential conditions during the auto-constrain operation. For example any two lines
                which have an angle smaller than the given **autoConstrainAngularTolerance** will be
                assumed to be parallel, and a parallel constrain may be added during the auto-constrain
                operation. The default value is 0.01.

            autoConstrainLinearTolerance=`None`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.autoConstrainLinearTolerance "Permalink to this definition")
            :   A Float specifying the linear tolerance which is used to determine when two points or
                geometries are coincident during the auto-constrain operation. The default value is
                10⁻⁶.

            autoConstrainOptions=`None`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.autoConstrainOptions "Permalink to this definition")
            :   A sequence of SymbolicConstants specifying which type of constraints may be added by the
                auto-constraint tool. Possible values are PARALLEL, PERPENDICULAR, IDENTICAL, TANGENT,
                CONCENTRIC, and EQUALRADIUS. The default value is (PARALLEL,, PERPENDICULAR,,
                IDENTICAL,, TANGENT,, CONCENTRIC,, EQUALRADIUS).

            dragMethod=`abaqusConstants.MINIMUM_MOVE`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.dragMethod "Permalink to this definition")
            :   A SymbolicConstant specifying the constraint solving mode used by the sketcher during
                drag operation. Possible values are MINIMUM\_MOVE, STANDARD, WEIGHTED, and RELAXATION.
                The default value is MINIMUM\_MOVE.

            editMethod=`abaqusConstants.STANDARD`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues.editMethod "Permalink to this definition")
            :   A SymbolicConstant specifying the constraint solving mode used by the sketcher during
                regular sketch editing and adding new constraints and dimensions. Possible values are
                MINIMUM\_MOVE, STANDARD, WEIGHTED, and RELAXATION. The default value is STANDARD.

        Raises:[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketchOptions.ConstrainedSketchOptions.setValues-raises "Permalink to this headline")
        :   **RangeError** –

*class* ConstrainedSketchParameter[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchParameter/Parameter.py#L6-L68)[¶](#abaqus.Sketcher.ConstrainedSketchParameter.Parameter.ConstrainedSketchParameter "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The ConstrainedSketchParameter object stores the definition of a parameter in the sketch.

    Note

    This object can be accessed by:

    ```python
    import sketch
    mdb.models[name].sketches[name].parameters[i]
    ```

    Note

    Check [ConstrainedSketchParameter on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchparameterpyc.htm?contextscope=all).

    Member Details:

    Parameter(*[name](#abaqus.Sketcher.ConstrainedSketchParameter.Parameter.ConstrainedSketchParameter.Parameter.name "abaqus.Sketcher.ConstrainedSketchParameter.Parameter.ConstrainedSketchParameter.Parameter.name (Python parameter) — A String specifying the name of the ConstrainedSketchParameter object.")*, *[path](#abaqus.Sketcher.ConstrainedSketchParameter.Parameter.ConstrainedSketchParameter.Parameter.path "abaqus.Sketcher.ConstrainedSketchParameter.Parameter.ConstrainedSketchParameter.Parameter.path (Python parameter) — A String specifying the ConstrainedSketchDimension object with which this parameter is associated.")=`''`*, *[expression](#abaqus.Sketcher.ConstrainedSketchParameter.Parameter.ConstrainedSketchParameter.Parameter.expression "abaqus.Sketcher.ConstrainedSketchParameter.Parameter.ConstrainedSketchParameter.Parameter.expression (Python parameter) — A String specifying the expression or value associated with the ConstrainedSketchParameter.")=`''`*, *[previousParameter](#abaqus.Sketcher.ConstrainedSketchParameter.Parameter.ConstrainedSketchParameter.Parameter.previousParameter "abaqus.Sketcher.ConstrainedSketchParameter.Parameter.ConstrainedSketchParameter.Parameter.previousParameter (Python parameter) — A String specifying the name of the previous ConstrainedSketchParameter, if it exists. The previousParameter argument implies an order among the parameters.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchParameter/Parameter.py#L32-L68)[¶](#abaqus.Sketcher.ConstrainedSketchParameter.Parameter.ConstrainedSketchParameter.Parameter "Permalink to this definition")
    :   This method creates a parameter and optionally associates a dimension with this parameter.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].sketches[name].ConstrainedSketchParameter
        ```

        Note

        Check [Parameter on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-parameterpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchParameter.Parameter.ConstrainedSketchParameter.Parameter-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Sketcher.ConstrainedSketchParameter.Parameter.ConstrainedSketchParameter.Parameter.name "Permalink to this definition")
            :   A String specifying the name of the ConstrainedSketchParameter object. No two parameters
                in the same ConstrainedSketch can have the same name.

            path=`''`[¶](#abaqus.Sketcher.ConstrainedSketchParameter.Parameter.ConstrainedSketchParameter.Parameter.path "Permalink to this definition")
            :   A String specifying the ConstrainedSketchDimension object with which this parameter is
                associated.

            expression=`''`[¶](#abaqus.Sketcher.ConstrainedSketchParameter.Parameter.ConstrainedSketchParameter.Parameter.expression "Permalink to this definition")
            :   A String specifying the expression or value associated with the
                ConstrainedSketchParameter.

            previousParameter=`''`[¶](#abaqus.Sketcher.ConstrainedSketchParameter.Parameter.ConstrainedSketchParameter.Parameter.previousParameter "Permalink to this definition")
            :   A String specifying the name of the previous ConstrainedSketchParameter, if it exists.
                The **previousParameter** argument implies an order among the parameters. No two
                parameters can reference the same parameter as the previous parameter.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchParameter.Parameter.ConstrainedSketchParameter.Parameter-returns "Permalink to this headline")
        :   A ConstrainedSketchParameter object.

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchParameter.Parameter.ConstrainedSketchParameter.Parameter-return-type "Permalink to this headline")
        :   [`ConstrainedSketchParameter`](#abaqus.Sketcher.ConstrainedSketchParameter.Parameter.ConstrainedSketchParameter "abaqus.Sketcher.ConstrainedSketchParameter.Parameter.ConstrainedSketchParameter (Python class) — Bases: object")

    expression : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchParameter/Parameter.py#L24-L26)[¶](#abaqus.Sketcher.ConstrainedSketchParameter.Parameter.ConstrainedSketchParameter.expression "Permalink to this definition")
    :   A String specifying an expression or value associated with this
        ConstrainedSketchParameter.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchParameter/Parameter.py#L17-L18)[¶](#abaqus.Sketcher.ConstrainedSketchParameter.Parameter.ConstrainedSketchParameter.name "Permalink to this definition")
    :   A String specifying the name of the ConstrainedSketchParameter object.

    path : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchParameter/Parameter.py#L20-L22)[¶](#abaqus.Sketcher.ConstrainedSketchParameter.Parameter.ConstrainedSketchParameter.path "Permalink to this definition")
    :   A String specifying the path to the ConstrainedSketchDimension that depends on this
        ConstrainedSketchParameter.

    previousParameter : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchParameter/Parameter.py#L28-L30)[¶](#abaqus.Sketcher.ConstrainedSketchParameter.Parameter.ConstrainedSketchParameter.previousParameter "Permalink to this definition")
    :   A String specifying the name of the ConstrainedSketchParameter that appears before this
        one in the ordered list.

*class* ConstrainedSketchVertexArray(*[iterable](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexArray.ConstrainedSketchVertexArray "abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexArray.ConstrainedSketchVertexArray.__init__.iterable (Python parameter)")=`()`*, */*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchVertex/ConstrainedSketchVertexArray.py#L11-L39)[¶](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexArray.ConstrainedSketchVertexArray "Permalink to this definition")
:   Bases: [`List`](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")[[`ConstrainedSketchVertex`](#abaqus.Sketcher.ConstrainedSketchVertex.Spot.ConstrainedSketchVertex "abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertex.ConstrainedSketchVertex (Python class)")]

    The ConstrainedSketchVertexArray is a sequence of ConstrainedSketchVertex objects.

    Note

    This object can be accessed by:

    ```python
    import sketch
    mdb.models[name].sketches[name].vertices[i]
    ```

    Note

    Check [ConstrainedSketchVertexArray on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexarraypyc.htm?contextscope=all).

    Member Details:

    findAt(*[coordinates](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexArray.ConstrainedSketchVertexArray.findAt.coordinates "abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexArray.ConstrainedSketchVertexArray.findAt.coordinates (Python parameter) — A sequence of Floats specifying the X and Y coordinates of the object to find.")*, *[printWarning](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexArray.ConstrainedSketchVertexArray.findAt.printWarning "abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexArray.ConstrainedSketchVertexArray.findAt.printWarning (Python parameter) — A Boolean specifying whether a message is to be printed to the CLI if no entity is found at the specified location.")=`True`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchVertex/ConstrainedSketchVertexArray.py#L22-L39)[¶](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexArray.ConstrainedSketchVertexArray.findAt "Permalink to this definition")
    :   This method returns the ConstrainedSketchVertex located at the given coordinates.

        Note

        Check [ConstrainedSketchVertexArray.findAt on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketchvertexarraypyc.htm?contextscope=all#simaker-constrainedsketchvertexarrayfindatpyc).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexArray.ConstrainedSketchVertexArray.findAt-parameters "Permalink to this headline")
        :   coordinates[¶](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexArray.ConstrainedSketchVertexArray.findAt.coordinates "Permalink to this definition")
            :   A sequence of Floats specifying the **X** and **Y** coordinates of the object to find.

            printWarning=`True`[¶](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexArray.ConstrainedSketchVertexArray.findAt.printWarning "Permalink to this definition")
            :   A Boolean specifying whether a message is to be printed to the CLI if no entity is found
                at the specified location. The default value is True.

        Returns:[¶](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexArray.ConstrainedSketchVertexArray.findAt-returns "Permalink to this headline")
        :   A ConstrainedSketchVertex object.

        Return type:[¶](#abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertexArray.ConstrainedSketchVertexArray.findAt-return-type "Permalink to this headline")
        :   `ConstrainedSketchVertex`

*class* CoincidentConstraint(*[entity1](#abaqus.Sketcher.ConstrainedSketchConstraint.CoincidentConstraint.CoincidentConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.CoincidentConstraint.CoincidentConstraint.__init__.entity1 (Python parameter)")*, *[entity2](#abaqus.Sketcher.ConstrainedSketchConstraint.CoincidentConstraint.CoincidentConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.CoincidentConstraint.CoincidentConstraint.__init__.entity2 (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchConstraint/CoincidentConstraint.py#L11-L36)[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.CoincidentConstraint.CoincidentConstraint "Permalink to this definition")
:   Bases: [`ConstrainedSketchConstraint`](#abaqus.Sketcher.ConstrainedSketchConstraint.VerticalConstraint.ConstrainedSketchConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraint.ConstrainedSketchConstraint (Python class)")

    Member Details:

*class* ConcentricConstraint(*[entity1](#abaqus.Sketcher.ConstrainedSketchConstraint.ConcentricConstraint.ConcentricConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.ConcentricConstraint.ConcentricConstraint.__init__.entity1 (Python parameter)")*, *[entity2](#abaqus.Sketcher.ConstrainedSketchConstraint.ConcentricConstraint.ConcentricConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.ConcentricConstraint.ConcentricConstraint.__init__.entity2 (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchConstraint/ConcentricConstraint.py#L11-L38)[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ConcentricConstraint.ConcentricConstraint "Permalink to this definition")
:   Bases: [`ConstrainedSketchConstraint`](#abaqus.Sketcher.ConstrainedSketchConstraint.VerticalConstraint.ConstrainedSketchConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraint.ConstrainedSketchConstraint (Python class)")

    Member Details:

*class* EqualDistanceConstraint(*[entity1](#abaqus.Sketcher.ConstrainedSketchConstraint.EqualDistanceConstraint.EqualDistanceConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.EqualDistanceConstraint.EqualDistanceConstraint.__init__.entity1 (Python parameter)")*, *[entity2](#abaqus.Sketcher.ConstrainedSketchConstraint.EqualDistanceConstraint.EqualDistanceConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.EqualDistanceConstraint.EqualDistanceConstraint.__init__.entity2 (Python parameter)")*, *[midpoint](#abaqus.Sketcher.ConstrainedSketchConstraint.EqualDistanceConstraint.EqualDistanceConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.EqualDistanceConstraint.EqualDistanceConstraint.__init__.midpoint (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchConstraint/EqualDistanceConstraint.py#L12-L42)[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.EqualDistanceConstraint.EqualDistanceConstraint "Permalink to this definition")
:   Bases: [`ConstrainedSketchConstraint`](#abaqus.Sketcher.ConstrainedSketchConstraint.VerticalConstraint.ConstrainedSketchConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraint.ConstrainedSketchConstraint (Python class)")

    Member Details:

*class* EqualLengthConstraint(*[entity1](#abaqus.Sketcher.ConstrainedSketchConstraint.EqualLengthConstraint.EqualLengthConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.EqualLengthConstraint.EqualLengthConstraint.__init__.entity1 (Python parameter)")*, *[entity2](#abaqus.Sketcher.ConstrainedSketchConstraint.EqualLengthConstraint.EqualLengthConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.EqualLengthConstraint.EqualLengthConstraint.__init__.entity2 (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchConstraint/EqualLengthConstraint.py#L11-L35)[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.EqualLengthConstraint.EqualLengthConstraint "Permalink to this definition")
:   Bases: [`ConstrainedSketchConstraint`](#abaqus.Sketcher.ConstrainedSketchConstraint.VerticalConstraint.ConstrainedSketchConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraint.ConstrainedSketchConstraint (Python class)")

    Member Details:

*class* EqualRadiusConstraint(*[entity1](#abaqus.Sketcher.ConstrainedSketchConstraint.EqualRadiusConstraint.EqualRadiusConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.EqualRadiusConstraint.EqualRadiusConstraint.__init__.entity1 (Python parameter)")*, *[entity2](#abaqus.Sketcher.ConstrainedSketchConstraint.EqualRadiusConstraint.EqualRadiusConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.EqualRadiusConstraint.EqualRadiusConstraint.__init__.entity2 (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchConstraint/EqualRadiusConstraint.py#L11-L35)[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.EqualRadiusConstraint.EqualRadiusConstraint "Permalink to this definition")
:   Bases: [`ConstrainedSketchConstraint`](#abaqus.Sketcher.ConstrainedSketchConstraint.VerticalConstraint.ConstrainedSketchConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraint.ConstrainedSketchConstraint (Python class)")

    Member Details:

*class* FixedConstraint(*[entity](#abaqus.Sketcher.ConstrainedSketchConstraint.FixedConstraint.FixedConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.FixedConstraint.FixedConstraint.__init__.entity (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchConstraint/FixedConstraint.py#L11-L35)[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.FixedConstraint.FixedConstraint "Permalink to this definition")
:   Bases: [`ConstrainedSketchConstraint`](#abaqus.Sketcher.ConstrainedSketchConstraint.VerticalConstraint.ConstrainedSketchConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraint.ConstrainedSketchConstraint (Python class)")

    Member Details:

*class* HorizontalConstraint(*[entity](#abaqus.Sketcher.ConstrainedSketchConstraint.HorizontalConstraint.HorizontalConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.HorizontalConstraint.HorizontalConstraint.__init__.entity (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchConstraint/HorizontalConstraint.py#L11-L33)[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.HorizontalConstraint.HorizontalConstraint "Permalink to this definition")
:   Bases: [`ConstrainedSketchConstraint`](#abaqus.Sketcher.ConstrainedSketchConstraint.VerticalConstraint.ConstrainedSketchConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraint.ConstrainedSketchConstraint (Python class)")

    Member Details:

*class* ParallelConstraint(*[entity1](#abaqus.Sketcher.ConstrainedSketchConstraint.ParallelConstraint.ParallelConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.ParallelConstraint.ParallelConstraint.__init__.entity1 (Python parameter)")*, *[entity2](#abaqus.Sketcher.ConstrainedSketchConstraint.ParallelConstraint.ParallelConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.ParallelConstraint.ParallelConstraint.__init__.entity2 (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchConstraint/ParallelConstraint.py#L11-L35)[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.ParallelConstraint.ParallelConstraint "Permalink to this definition")
:   Bases: [`ConstrainedSketchConstraint`](#abaqus.Sketcher.ConstrainedSketchConstraint.VerticalConstraint.ConstrainedSketchConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraint.ConstrainedSketchConstraint (Python class)")

    Member Details:

*class* PerpendicularConstraint(*[entity1](#abaqus.Sketcher.ConstrainedSketchConstraint.PerpendicularConstraint.PerpendicularConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.PerpendicularConstraint.PerpendicularConstraint.__init__.entity1 (Python parameter)")*, *[entity2](#abaqus.Sketcher.ConstrainedSketchConstraint.PerpendicularConstraint.PerpendicularConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.PerpendicularConstraint.PerpendicularConstraint.__init__.entity2 (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchConstraint/PerpendicularConstraint.py#L11-L35)[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.PerpendicularConstraint.PerpendicularConstraint "Permalink to this definition")
:   Bases: [`ConstrainedSketchConstraint`](#abaqus.Sketcher.ConstrainedSketchConstraint.VerticalConstraint.ConstrainedSketchConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraint.ConstrainedSketchConstraint (Python class)")

    Member Details:

*class* TangentConstraint(*[entity1](#abaqus.Sketcher.ConstrainedSketchConstraint.TangentConstraint.TangentConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.TangentConstraint.TangentConstraint.__init__.entity1 (Python parameter)")*, *[entity2](#abaqus.Sketcher.ConstrainedSketchConstraint.TangentConstraint.TangentConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.TangentConstraint.TangentConstraint.__init__.entity2 (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchConstraint/TangentConstraint.py#L11-L35)[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.TangentConstraint.TangentConstraint "Permalink to this definition")
:   Bases: [`ConstrainedSketchConstraint`](#abaqus.Sketcher.ConstrainedSketchConstraint.VerticalConstraint.ConstrainedSketchConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraint.ConstrainedSketchConstraint (Python class)")

    Member Details:

*class* VerticalConstraint(*[entity](#abaqus.Sketcher.ConstrainedSketchConstraint.VerticalConstraint.VerticalConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.VerticalConstraint.VerticalConstraint.__init__.entity (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchConstraint/VerticalConstraint.py#L11-L33)[¶](#abaqus.Sketcher.ConstrainedSketchConstraint.VerticalConstraint.VerticalConstraint "Permalink to this definition")
:   Bases: [`ConstrainedSketchConstraint`](#abaqus.Sketcher.ConstrainedSketchConstraint.VerticalConstraint.ConstrainedSketchConstraint "abaqus.Sketcher.ConstrainedSketchConstraint.ConstrainedSketchConstraint.ConstrainedSketchConstraint (Python class)")

    Member Details:

*class* AngularDimension(*[line1](#abaqus.Sketcher.ConstrainedSketchDimension.AngularDimension.AngularDimension "abaqus.Sketcher.ConstrainedSketchDimension.AngularDimension.AngularDimension.__init__.line1 (Python parameter)")*, *[line2](#abaqus.Sketcher.ConstrainedSketchDimension.AngularDimension.AngularDimension "abaqus.Sketcher.ConstrainedSketchDimension.AngularDimension.AngularDimension.__init__.line2 (Python parameter)")*, *[textPoint](#abaqus.Sketcher.ConstrainedSketchDimension.AngularDimension.AngularDimension "abaqus.Sketcher.ConstrainedSketchDimension.AngularDimension.AngularDimension.__init__.textPoint (Python parameter)")*, *[value](#abaqus.Sketcher.ConstrainedSketchDimension.AngularDimension.AngularDimension "abaqus.Sketcher.ConstrainedSketchDimension.AngularDimension.AngularDimension.__init__.value (Python parameter)")=`None`*, *[reference](#abaqus.Sketcher.ConstrainedSketchDimension.AngularDimension.AngularDimension "abaqus.Sketcher.ConstrainedSketchDimension.AngularDimension.AngularDimension.__init__.reference (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchDimension/AngularDimension.py#L14-L52)[¶](#abaqus.Sketcher.ConstrainedSketchDimension.AngularDimension.AngularDimension "Permalink to this definition")
:   Bases: [`ConstrainedSketchDimension`](#abaqus.Sketcher.ConstrainedSketchDimension.VerticalDimension.ConstrainedSketchDimension "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimension.ConstrainedSketchDimension (Python class)")

    Member Details:

*class* DistanceDimension(*[entity1](#abaqus.Sketcher.ConstrainedSketchDimension.DistanceDimension.DistanceDimension "abaqus.Sketcher.ConstrainedSketchDimension.DistanceDimension.DistanceDimension.__init__.entity1 (Python parameter)")*, *[entity2](#abaqus.Sketcher.ConstrainedSketchDimension.DistanceDimension.DistanceDimension "abaqus.Sketcher.ConstrainedSketchDimension.DistanceDimension.DistanceDimension.__init__.entity2 (Python parameter)")*, *[textPoint](#abaqus.Sketcher.ConstrainedSketchDimension.DistanceDimension.DistanceDimension "abaqus.Sketcher.ConstrainedSketchDimension.DistanceDimension.DistanceDimension.__init__.textPoint (Python parameter)")*, *[value](#abaqus.Sketcher.ConstrainedSketchDimension.DistanceDimension.DistanceDimension "abaqus.Sketcher.ConstrainedSketchDimension.DistanceDimension.DistanceDimension.__init__.value (Python parameter)")=`None`*, *[reference](#abaqus.Sketcher.ConstrainedSketchDimension.DistanceDimension.DistanceDimension "abaqus.Sketcher.ConstrainedSketchDimension.DistanceDimension.DistanceDimension.__init__.reference (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchDimension/DistanceDimension.py#L12-L54)[¶](#abaqus.Sketcher.ConstrainedSketchDimension.DistanceDimension.DistanceDimension "Permalink to this definition")
:   Bases: [`ConstrainedSketchDimension`](#abaqus.Sketcher.ConstrainedSketchDimension.VerticalDimension.ConstrainedSketchDimension "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimension.ConstrainedSketchDimension (Python class)")

    Member Details:

*class* HorizontalDimension(*[vertex1](#abaqus.Sketcher.ConstrainedSketchDimension.HorizontalDimension.HorizontalDimension "abaqus.Sketcher.ConstrainedSketchDimension.HorizontalDimension.HorizontalDimension.__init__.vertex1 (Python parameter)")*, *[vertex2](#abaqus.Sketcher.ConstrainedSketchDimension.HorizontalDimension.HorizontalDimension "abaqus.Sketcher.ConstrainedSketchDimension.HorizontalDimension.HorizontalDimension.__init__.vertex2 (Python parameter)")*, *[textPoint](#abaqus.Sketcher.ConstrainedSketchDimension.HorizontalDimension.HorizontalDimension "abaqus.Sketcher.ConstrainedSketchDimension.HorizontalDimension.HorizontalDimension.__init__.textPoint (Python parameter)")*, *[value](#abaqus.Sketcher.ConstrainedSketchDimension.HorizontalDimension.HorizontalDimension "abaqus.Sketcher.ConstrainedSketchDimension.HorizontalDimension.HorizontalDimension.__init__.value (Python parameter)")=`None`*, *[reference](#abaqus.Sketcher.ConstrainedSketchDimension.HorizontalDimension.HorizontalDimension "abaqus.Sketcher.ConstrainedSketchDimension.HorizontalDimension.HorizontalDimension.__init__.reference (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchDimension/HorizontalDimension.py#L12-L50)[¶](#abaqus.Sketcher.ConstrainedSketchDimension.HorizontalDimension.HorizontalDimension "Permalink to this definition")
:   Bases: [`ConstrainedSketchDimension`](#abaqus.Sketcher.ConstrainedSketchDimension.VerticalDimension.ConstrainedSketchDimension "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimension.ConstrainedSketchDimension (Python class)")

    Member Details:

*class* ObliqueDimension(*[vertex1](#abaqus.Sketcher.ConstrainedSketchDimension.ObliqueDimension.ObliqueDimension "abaqus.Sketcher.ConstrainedSketchDimension.ObliqueDimension.ObliqueDimension.__init__.vertex1 (Python parameter)")*, *[vertex2](#abaqus.Sketcher.ConstrainedSketchDimension.ObliqueDimension.ObliqueDimension "abaqus.Sketcher.ConstrainedSketchDimension.ObliqueDimension.ObliqueDimension.__init__.vertex2 (Python parameter)")*, *[textPoint](#abaqus.Sketcher.ConstrainedSketchDimension.ObliqueDimension.ObliqueDimension "abaqus.Sketcher.ConstrainedSketchDimension.ObliqueDimension.ObliqueDimension.__init__.textPoint (Python parameter)")*, *[value](#abaqus.Sketcher.ConstrainedSketchDimension.ObliqueDimension.ObliqueDimension "abaqus.Sketcher.ConstrainedSketchDimension.ObliqueDimension.ObliqueDimension.__init__.value (Python parameter)")=`None`*, *[reference](#abaqus.Sketcher.ConstrainedSketchDimension.ObliqueDimension.ObliqueDimension "abaqus.Sketcher.ConstrainedSketchDimension.ObliqueDimension.ObliqueDimension.__init__.reference (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchDimension/ObliqueDimension.py#L12-L50)[¶](#abaqus.Sketcher.ConstrainedSketchDimension.ObliqueDimension.ObliqueDimension "Permalink to this definition")
:   Bases: [`ConstrainedSketchDimension`](#abaqus.Sketcher.ConstrainedSketchDimension.VerticalDimension.ConstrainedSketchDimension "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimension.ConstrainedSketchDimension (Python class)")

    Member Details:

*class* RadialDimension(*[curve](#abaqus.Sketcher.ConstrainedSketchDimension.RadialDimension.RadialDimension "abaqus.Sketcher.ConstrainedSketchDimension.RadialDimension.RadialDimension.__init__.curve (Python parameter)")*, *[textPoint](#abaqus.Sketcher.ConstrainedSketchDimension.RadialDimension.RadialDimension "abaqus.Sketcher.ConstrainedSketchDimension.RadialDimension.RadialDimension.__init__.textPoint (Python parameter)")*, *[value](#abaqus.Sketcher.ConstrainedSketchDimension.RadialDimension.RadialDimension "abaqus.Sketcher.ConstrainedSketchDimension.RadialDimension.RadialDimension.__init__.value (Python parameter)")=`None`*, *[reference](#abaqus.Sketcher.ConstrainedSketchDimension.RadialDimension.RadialDimension "abaqus.Sketcher.ConstrainedSketchDimension.RadialDimension.RadialDimension.__init__.reference (Python parameter)")=`0`*, *[majorRadius](#abaqus.Sketcher.ConstrainedSketchDimension.RadialDimension.RadialDimension "abaqus.Sketcher.ConstrainedSketchDimension.RadialDimension.RadialDimension.__init__.majorRadius (Python parameter)")=`None`*, *[minorRadius](#abaqus.Sketcher.ConstrainedSketchDimension.RadialDimension.RadialDimension "abaqus.Sketcher.ConstrainedSketchDimension.RadialDimension.RadialDimension.__init__.minorRadius (Python parameter)")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchDimension/RadialDimension.py#L14-L57)[¶](#abaqus.Sketcher.ConstrainedSketchDimension.RadialDimension.RadialDimension "Permalink to this definition")
:   Bases: [`ConstrainedSketchDimension`](#abaqus.Sketcher.ConstrainedSketchDimension.VerticalDimension.ConstrainedSketchDimension "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimension.ConstrainedSketchDimension (Python class)")

    Member Details:

*class* VerticalDimension(*[vertex1](#abaqus.Sketcher.ConstrainedSketchDimension.VerticalDimension.VerticalDimension "abaqus.Sketcher.ConstrainedSketchDimension.VerticalDimension.VerticalDimension.__init__.vertex1 (Python parameter)")*, *[vertex2](#abaqus.Sketcher.ConstrainedSketchDimension.VerticalDimension.VerticalDimension "abaqus.Sketcher.ConstrainedSketchDimension.VerticalDimension.VerticalDimension.__init__.vertex2 (Python parameter)")*, *[textPoint](#abaqus.Sketcher.ConstrainedSketchDimension.VerticalDimension.VerticalDimension "abaqus.Sketcher.ConstrainedSketchDimension.VerticalDimension.VerticalDimension.__init__.textPoint (Python parameter)")*, *[value](#abaqus.Sketcher.ConstrainedSketchDimension.VerticalDimension.VerticalDimension "abaqus.Sketcher.ConstrainedSketchDimension.VerticalDimension.VerticalDimension.__init__.value (Python parameter)")=`None`*, *[reference](#abaqus.Sketcher.ConstrainedSketchDimension.VerticalDimension.VerticalDimension "abaqus.Sketcher.ConstrainedSketchDimension.VerticalDimension.VerticalDimension.__init__.reference (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchDimension/VerticalDimension.py#L12-L50)[¶](#abaqus.Sketcher.ConstrainedSketchDimension.VerticalDimension.VerticalDimension "Permalink to this definition")
:   Bases: [`ConstrainedSketchDimension`](#abaqus.Sketcher.ConstrainedSketchDimension.VerticalDimension.ConstrainedSketchDimension "abaqus.Sketcher.ConstrainedSketchDimension.ConstrainedSketchDimension.ConstrainedSketchDimension (Python class)")

    Member Details:

*class* Arc3Points(*[point1](#abaqus.Sketcher.ConstrainedSketchGeometry.Arc3Points.Arc3Points "abaqus.Sketcher.ConstrainedSketchGeometry.Arc3Points.Arc3Points.__init__.point1 (Python parameter)")*, *[point2](#abaqus.Sketcher.ConstrainedSketchGeometry.Arc3Points.Arc3Points "abaqus.Sketcher.ConstrainedSketchGeometry.Arc3Points.Arc3Points.__init__.point2 (Python parameter)")*, *[point3](#abaqus.Sketcher.ConstrainedSketchGeometry.Arc3Points.Arc3Points "abaqus.Sketcher.ConstrainedSketchGeometry.Arc3Points.Arc3Points.__init__.point3 (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/Arc3Points.py#L10-L35)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.Arc3Points.Arc3Points "Permalink to this definition")
:   Bases: [`ConstrainedSketchGeometry`](#abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.ConstrainedSketchGeometry "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry (Python class)")

    Member Details:

*class* ArcByCenterEnds(*[center](#abaqus.Sketcher.ConstrainedSketchGeometry.ArcByCenterEnds.ArcByCenterEnds "abaqus.Sketcher.ConstrainedSketchGeometry.ArcByCenterEnds.ArcByCenterEnds.__init__.center (Python parameter)")*, *[point1](#abaqus.Sketcher.ConstrainedSketchGeometry.ArcByCenterEnds.ArcByCenterEnds "abaqus.Sketcher.ConstrainedSketchGeometry.ArcByCenterEnds.ArcByCenterEnds.__init__.point1 (Python parameter)")*, *[point2](#abaqus.Sketcher.ConstrainedSketchGeometry.ArcByCenterEnds.ArcByCenterEnds "abaqus.Sketcher.ConstrainedSketchGeometry.ArcByCenterEnds.ArcByCenterEnds.__init__.point2 (Python parameter)")*, *[direction](#abaqus.Sketcher.ConstrainedSketchGeometry.ArcByCenterEnds.ArcByCenterEnds "abaqus.Sketcher.ConstrainedSketchGeometry.ArcByCenterEnds.ArcByCenterEnds.__init__.direction (Python parameter)")=`abaqusConstants.COUNTERCLOCKWISE`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/ArcByCenterEnds.py#L13-L57)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ArcByCenterEnds.ArcByCenterEnds "Permalink to this definition")
:   Bases: [`ConstrainedSketchGeometry`](#abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.ConstrainedSketchGeometry "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry (Python class)")

    Member Details:

*class* ArcByStartEndTangent(*[point1](#abaqus.Sketcher.ConstrainedSketchGeometry.ArcByStartEndTangent.ArcByStartEndTangent "abaqus.Sketcher.ConstrainedSketchGeometry.ArcByStartEndTangent.ArcByStartEndTangent.__init__.point1 (Python parameter)")*, *[point2](#abaqus.Sketcher.ConstrainedSketchGeometry.ArcByStartEndTangent.ArcByStartEndTangent "abaqus.Sketcher.ConstrainedSketchGeometry.ArcByStartEndTangent.ArcByStartEndTangent.__init__.point2 (Python parameter)")*, *[vector](#abaqus.Sketcher.ConstrainedSketchGeometry.ArcByStartEndTangent.ArcByStartEndTangent "abaqus.Sketcher.ConstrainedSketchGeometry.ArcByStartEndTangent.ArcByStartEndTangent.__init__.vector (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/ArcByStartEndTangent.py#L10-L36)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ArcByStartEndTangent.ArcByStartEndTangent "Permalink to this definition")
:   Bases: [`ConstrainedSketchGeometry`](#abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.ConstrainedSketchGeometry "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry (Python class)")

    Member Details:

*class* CircleByCenterPerimeter(*[center](#abaqus.Sketcher.ConstrainedSketchGeometry.CircleByCenterPerimeter.CircleByCenterPerimeter "abaqus.Sketcher.ConstrainedSketchGeometry.CircleByCenterPerimeter.CircleByCenterPerimeter.__init__.center (Python parameter)")*, *[point1](#abaqus.Sketcher.ConstrainedSketchGeometry.CircleByCenterPerimeter.CircleByCenterPerimeter "abaqus.Sketcher.ConstrainedSketchGeometry.CircleByCenterPerimeter.CircleByCenterPerimeter.__init__.point1 (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/CircleByCenterPerimeter.py#L10-L34)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.CircleByCenterPerimeter.CircleByCenterPerimeter "Permalink to this definition")
:   Bases: [`ConstrainedSketchGeometry`](#abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.ConstrainedSketchGeometry "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry (Python class)")

    Member Details:

*class* ConstructionCircleByCenterPerimeter(*[center](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstructionCircleByCenterPerimeter.ConstructionCircleByCenterPerimeter "abaqus.Sketcher.ConstrainedSketchGeometry.ConstructionCircleByCenterPerimeter.ConstructionCircleByCenterPerimeter.__init__.center (Python parameter)")*, *[point1](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstructionCircleByCenterPerimeter.ConstructionCircleByCenterPerimeter "abaqus.Sketcher.ConstrainedSketchGeometry.ConstructionCircleByCenterPerimeter.ConstructionCircleByCenterPerimeter.__init__.point1 (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/ConstructionCircleByCenterPerimeter.py#L10-L34)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstructionCircleByCenterPerimeter.ConstructionCircleByCenterPerimeter "Permalink to this definition")
:   Bases: [`ConstrainedSketchGeometry`](#abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.ConstrainedSketchGeometry "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry (Python class)")

    Member Details:

*class* ConstructionLine(*[point1](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstructionLine.ConstructionLine "abaqus.Sketcher.ConstrainedSketchGeometry.ConstructionLine.ConstructionLine.__init__.point1 (Python parameter)")*, *[point2](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstructionLine.ConstructionLine "abaqus.Sketcher.ConstrainedSketchGeometry.ConstructionLine.ConstructionLine.__init__.point2 (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/ConstructionLine.py#L10-L33)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.ConstructionLine.ConstructionLine "Permalink to this definition")
:   Bases: [`ConstrainedSketchGeometry`](#abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.ConstrainedSketchGeometry "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry (Python class)")

    Member Details:

*class* EllipseByCenterPerimeter(*[center](#abaqus.Sketcher.ConstrainedSketchGeometry.EllipseByCenterPerimeter.EllipseByCenterPerimeter "abaqus.Sketcher.ConstrainedSketchGeometry.EllipseByCenterPerimeter.EllipseByCenterPerimeter.__init__.center (Python parameter)")*, *[axisPoint1](#abaqus.Sketcher.ConstrainedSketchGeometry.EllipseByCenterPerimeter.EllipseByCenterPerimeter "abaqus.Sketcher.ConstrainedSketchGeometry.EllipseByCenterPerimeter.EllipseByCenterPerimeter.__init__.axisPoint1 (Python parameter)")*, *[axisPoint2](#abaqus.Sketcher.ConstrainedSketchGeometry.EllipseByCenterPerimeter.EllipseByCenterPerimeter "abaqus.Sketcher.ConstrainedSketchGeometry.EllipseByCenterPerimeter.EllipseByCenterPerimeter.__init__.axisPoint2 (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/EllipseByCenterPerimeter.py#L10-L36)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.EllipseByCenterPerimeter.EllipseByCenterPerimeter "Permalink to this definition")
:   Bases: [`ConstrainedSketchGeometry`](#abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.ConstrainedSketchGeometry "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry (Python class)")

    Member Details:

*class* FilletByRadius(*[radius](#abaqus.Sketcher.ConstrainedSketchGeometry.FilletByRadius.FilletByRadius "abaqus.Sketcher.ConstrainedSketchGeometry.FilletByRadius.FilletByRadius.__init__.radius (Python parameter)")*, *[curve1](#abaqus.Sketcher.ConstrainedSketchGeometry.FilletByRadius.FilletByRadius "abaqus.Sketcher.ConstrainedSketchGeometry.FilletByRadius.FilletByRadius.__init__.curve1 (Python parameter)")*, *[nearPoint1](#abaqus.Sketcher.ConstrainedSketchGeometry.FilletByRadius.FilletByRadius "abaqus.Sketcher.ConstrainedSketchGeometry.FilletByRadius.FilletByRadius.__init__.nearPoint1 (Python parameter)")*, *[curve2](#abaqus.Sketcher.ConstrainedSketchGeometry.FilletByRadius.FilletByRadius "abaqus.Sketcher.ConstrainedSketchGeometry.FilletByRadius.FilletByRadius.__init__.curve2 (Python parameter)")*, *[nearPoint2](#abaqus.Sketcher.ConstrainedSketchGeometry.FilletByRadius.FilletByRadius "abaqus.Sketcher.ConstrainedSketchGeometry.FilletByRadius.FilletByRadius.__init__.nearPoint2 (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/FilletByRadius.py#L10-L57)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.FilletByRadius.FilletByRadius "Permalink to this definition")
:   Bases: [`ConstrainedSketchGeometry`](#abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.ConstrainedSketchGeometry "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry (Python class)")

    Member Details:

*class* Line(*[point1](#abaqus.Sketcher.ConstrainedSketchGeometry.Line.Line "abaqus.Sketcher.ConstrainedSketchGeometry.Line.Line.__init__.point1 (Python parameter)")*, *[point2](#abaqus.Sketcher.ConstrainedSketchGeometry.Line.Line "abaqus.Sketcher.ConstrainedSketchGeometry.Line.Line.__init__.point2 (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/Line.py#L10-L33)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.Line.Line "Permalink to this definition")
:   Bases: [`ConstrainedSketchGeometry`](#abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.ConstrainedSketchGeometry "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry (Python class)")

    Member Details:

*class* Spline(*[points](#abaqus.Sketcher.ConstrainedSketchGeometry.Spline.Spline "abaqus.Sketcher.ConstrainedSketchGeometry.Spline.Spline.__init__.points (Python parameter)")*, *[constrainPoints](#abaqus.Sketcher.ConstrainedSketchGeometry.Spline.Spline "abaqus.Sketcher.ConstrainedSketchGeometry.Spline.Spline.__init__.constrainPoints (Python parameter)")=`True`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/Spline.py#L9-L34)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.Spline.Spline "Permalink to this definition")
:   Bases: [`ConstrainedSketchGeometry`](#abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.ConstrainedSketchGeometry "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry (Python class)")

    Member Details:

*class* Spot(*[point](#abaqus.Sketcher.ConstrainedSketchVertex.Spot.Spot "abaqus.Sketcher.ConstrainedSketchVertex.Spot.Spot.__init__.point (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchVertex/Spot.py#L10-L31)[¶](#abaqus.Sketcher.ConstrainedSketchVertex.Spot.Spot "Permalink to this definition")
:   Bases: [`ConstrainedSketchVertex`](#abaqus.Sketcher.ConstrainedSketchVertex.Spot.ConstrainedSketchVertex "abaqus.Sketcher.ConstrainedSketchVertex.ConstrainedSketchVertex.ConstrainedSketchVertex (Python class)")

    Member Details:

*class* getPointAtDistance(*[point](#abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.getPointAtDistance "abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.getPointAtDistance.__init__.point (Python parameter)")*, *[distance](#abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.getPointAtDistance "abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.getPointAtDistance.__init__.distance (Python parameter)")*, *[percentage](#abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.getPointAtDistance "abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.getPointAtDistance.__init__.percentage (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchGeometry/getPointAtDistance.py#L11-L35)[¶](#abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.getPointAtDistance "Permalink to this definition")
:   Bases: [`ConstrainedSketchGeometry`](#abaqus.Sketcher.ConstrainedSketchGeometry.getPointAtDistance.ConstrainedSketchGeometry "abaqus.Sketcher.ConstrainedSketchGeometry.ConstrainedSketchGeometry.ConstrainedSketchGeometry (Python class)")

    Member Details:

*class* ConstrainedSketcherOptions[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchOptions/ConstrainedSketcherOptions.py#L11-L85)[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The ConstrainedSketcherOptions object is used to store values and attributes which will be applied to all
    sketches used in the current session. The ConstrainedSketcherOptions object has no constructor.

    Note

    This object can be accessed by:

    ```python
    import sketch
    session.sketcherOptions
    ```

    Note

    Check [ConstrainedSketcherOptions on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketcheroptionspyc.htm?contextscope=all).

    Member Details:

    setValues(*[constructionGeometry](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.constructionGeometry "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.constructionGeometry (Python parameter) — A Boolean specifying whether construction geometry is shown.")=`1`*, *[gridSnap](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.gridSnap "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.gridSnap (Python parameter) — A Boolean specifying whether the cursor snaps to the grid.")=`1`*, *[preselection](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.preselection "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.preselection (Python parameter) — A Boolean specifying whether geometry will be preselected.")=`1`*, *[addImpliedConstraints](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.addImpliedConstraints "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.addImpliedConstraints (Python parameter) — A Boolean specifying if implied constraints are added during sketching.")=`1`*, *[maxCoplanarEntities](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.maxCoplanarEntities "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.maxCoplanarEntities (Python parameter) — An Int specifying the maximum number of coplanar entities which should be automatically projected from the background, when a sketch based feature is created or edited.")=`300`*, *[autoConstrainAngularTolerance](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.autoConstrainAngularTolerance "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.autoConstrainAngularTolerance (Python parameter) — A Float specifying the angular tolerance in degrees which is used to determine parallel and tangential conditions during the auto-constrain operation.")=`0`*, *[autoConstrainLinearTolerance](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.autoConstrainLinearTolerance "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.autoConstrainLinearTolerance (Python parameter) — A Float specifying the linear tolerance which is used to determine when two points or geometries are coincident during the auto-constrain operation.")=`None`*, *[autoConstrainOptions](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.autoConstrainOptions "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.autoConstrainOptions (Python parameter) — A sequence of SymbolicConstants specifying which type of constraints may be added by the auto-constraint tool.")=`None`*, *[dragMethod](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.dragMethod "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.dragMethod (Python parameter) — A SymbolicConstant specifying the constraint solving mode used by the sketcher during drag operation.")=`abaqusConstants.MINIMUM_MOVE`*, *[editMethod](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.editMethod "abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.editMethod (Python parameter) — A SymbolicConstant specifying the constraint solving mode used by the sketcher during regular sketch editing and adding new constraints and dimensions.")=`abaqusConstants.STANDARD`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchOptions/ConstrainedSketcherOptions.py#L23-L85)[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues "Permalink to this definition")
    :   This method modifies the ConstrainedSketchOptions object.

        Note

        Check [ConstrainedSketcherOptions.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-constrainedsketcheroptionspyc.htm?contextscope=all#simaker-constrainedsketcheroptionssetvaluespyc).

        Parameters:[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues-parameters "Permalink to this headline")
        :   constructionGeometry=`1`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.constructionGeometry "Permalink to this definition")
            :   A Boolean specifying whether construction geometry is shown. The default value is ON.

            gridSnap=`1`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.gridSnap "Permalink to this definition")
            :   A Boolean specifying whether the cursor snaps to the grid. The default value is ON.

            preselection=`1`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.preselection "Permalink to this definition")
            :   A Boolean specifying whether geometry will be preselected. The default value is ON.

            addImpliedConstraints=`1`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.addImpliedConstraints "Permalink to this definition")
            :   A Boolean specifying if implied constraints are added during sketching. The default
                value is ON.

            maxCoplanarEntities=`300`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.maxCoplanarEntities "Permalink to this definition")
            :   An Int specifying the maximum number of coplanar entities which should be automatically
                projected from the background, when a sketch based feature is created or edited. When
                this value is exceeded no entities are automatically projected and a warning issued.
                Possible values are **maxCoplanarEntities** > 0. The default value is 300.

            autoConstrainAngularTolerance=`0`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.autoConstrainAngularTolerance "Permalink to this definition")
            :   A Float specifying the angular tolerance in degrees which is used to determine parallel
                and tangential conditions during the auto-constrain operation. For example any two lines
                which have an angle smaller than the given **autoConstrainAngularTolerance** will be
                assumed to be parallel, and a parallel constrain may be added during the auto-constrain
                operation. The default value is 0.01.

            autoConstrainLinearTolerance=`None`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.autoConstrainLinearTolerance "Permalink to this definition")
            :   A Float specifying the linear tolerance which is used to determine when two points or
                geometries are coincident during the auto-constrain operation. The default value is
                10⁻⁶.

            autoConstrainOptions=`None`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.autoConstrainOptions "Permalink to this definition")
            :   A sequence of SymbolicConstants specifying which type of constraints may be added by the
                auto-constraint tool. Possible values are PARALLEL, PERPENDICULAR, IDENTICAL, TANGENT,
                CONCENTRIC, and EQUALRADIUS. The default value is (PARALLEL,, PERPENDICULAR,,
                IDENTICAL,, TANGENT,, CONCENTRIC,, EQUALRADIUS).

            dragMethod=`abaqusConstants.MINIMUM_MOVE`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.dragMethod "Permalink to this definition")
            :   A SymbolicConstant specifying the constraint solving mode used by the sketcher during
                drag operation. Possible values are MINIMUM\_MOVE, STANDARD, WEIGHTED, and RELAXATION.
                The default value is MINIMUM\_MOVE.

            editMethod=`abaqusConstants.STANDARD`[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues.editMethod "Permalink to this definition")
            :   A SymbolicConstant specifying the constraint solving mode used by the sketcher during
                regular sketch editing and adding new constraints and dimensions. Possible values are
                MINIMUM\_MOVE, STANDARD, WEIGHTED, and RELAXATION. The default value is STANDARD.

        Raises:[¶](#abaqus.Sketcher.ConstrainedSketchOptions.ConstrainedSketcherOptions.ConstrainedSketcherOptions.setValues-raises "Permalink to this headline")
        :   **RangeError** –

*class* Parameter(*[name](#abaqus.Sketcher.ConstrainedSketchParameter.Parameter.Parameter "abaqus.Sketcher.ConstrainedSketchParameter.Parameter.Parameter.__init__.name (Python parameter)")*, *[path](#abaqus.Sketcher.ConstrainedSketchParameter.Parameter.Parameter "abaqus.Sketcher.ConstrainedSketchParameter.Parameter.Parameter.__init__.path (Python parameter)")=`''`*, *[expression](#abaqus.Sketcher.ConstrainedSketchParameter.Parameter.Parameter "abaqus.Sketcher.ConstrainedSketchParameter.Parameter.Parameter.__init__.expression (Python parameter)")=`''`*, *[previous](#abaqus.Sketcher.ConstrainedSketchParameter.Parameter.Parameter "abaqus.Sketcher.ConstrainedSketchParameter.Parameter.Parameter.__init__.previous (Python parameter)")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Sketcher/ConstrainedSketchParameter/Parameter.py#L8-L40)[¶](#abaqus.Sketcher.ConstrainedSketchParameter.Parameter.Parameter "Permalink to this definition")
:   Bases: [`ConstrainedSketchParameter`](#abaqus.Sketcher.ConstrainedSketchParameter.Parameter.ConstrainedSketchParameter "abaqus.Sketcher.ConstrainedSketchParameter.ConstrainedSketchParameter.ConstrainedSketchParameter (Python class)")

    Member Details:

[Back to top](#)