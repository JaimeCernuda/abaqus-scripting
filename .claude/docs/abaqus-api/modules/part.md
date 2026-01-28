# Abaqus PART Module API Reference

> Source: [https://hailin.wang/abqpy/en/2025/reference/mdb/model/part_assembly/part.html](https://hailin.wang/abqpy/en/2025/reference/mdb/model/part_assembly/part.html)
> Downloaded for offline use by Claude Code skills.

---

# Part[¶](#part "Permalink to this heading")

Features in Abaqus/CAE include Parts, Datums, Partitions, and Assembly operations. Part commands create Feature objects on only the Part object. The commands that create Feature objects on only the rootAssembly object are described in Assembly commands. The commands that create Feature objects on both the Part and the rootAssembly objects are described in Feature commands.

## Create parts[¶](#create-parts "Permalink to this heading")

*class* PartModel(*[name](#abaqus.Part.PartModel.PartModel "abaqus.Part.PartModel.PartModel.__init__.name (Python parameter)")*, *[description](#abaqus.Part.PartModel.PartModel "abaqus.Part.PartModel.PartModel.__init__.description (Python parameter)")=`''`*, *[stefanBoltzmann](#abaqus.Part.PartModel.PartModel "abaqus.Part.PartModel.PartModel.__init__.stefanBoltzmann (Python parameter)")=`None`*, *[absoluteZero](#abaqus.Part.PartModel.PartModel "abaqus.Part.PartModel.PartModel.__init__.absoluteZero (Python parameter)")=`None`*, *[waveFormulation](#abaqus.Part.PartModel.PartModel "abaqus.Part.PartModel.PartModel.__init__.waveFormulation (Python parameter)")=`abaqusConstants.NOT_SET`*, *[modelType](#abaqus.Part.PartModel.PartModel "abaqus.Part.PartModel.PartModel.__init__.modelType (Python parameter)")=`abaqusConstants.STANDARD_EXPLICIT`*, *[universalGas](#abaqus.Part.PartModel.PartModel "abaqus.Part.PartModel.PartModel.__init__.universalGas (Python parameter)")=`None`*, *[copyConstraints](#abaqus.Part.PartModel.PartModel "abaqus.Part.PartModel.PartModel.__init__.copyConstraints (Python parameter)")=`1`*, *[copyConnectors](#abaqus.Part.PartModel.PartModel "abaqus.Part.PartModel.PartModel.__init__.copyConnectors (Python parameter)")=`1`*, *[copyInteractions](#abaqus.Part.PartModel.PartModel "abaqus.Part.PartModel.PartModel.__init__.copyInteractions (Python parameter)")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartModel.py#L13-L59)[¶](#abaqus.Part.PartModel.PartModel "Permalink to this definition")
:   Bases: [`ModelBase`](../index.html#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase (Python class) — Bases: object")

    Abaqus creates a Model object named Model-1 when a session is started.

    Note

    This object can be accessed by:

    ```python
    mdb.models[name]
    ```

    Note

    Check [PartModel on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?contextscope=all).

    Public Data Attributes:

    Inherited from [`ModelBase`](../index.html#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | [`name`](../index.html#abaqus.Model.ModelBase.ModelBase.name "abaqus.Model.ModelBase.ModelBase.name (Python attribute) — A String specifying the repository key.") | A String specifying the repository key. |
    | [`stefanBoltzmann`](../index.html#abaqus.Model.ModelBase.ModelBase.stefanBoltzmann "abaqus.Model.ModelBase.ModelBase.stefanBoltzmann (Python attribute) — None or a Float specifying the Stefan-Boltzmann constant. The default value is None.") | None or a Float specifying the Stefan-Boltzmann constant. |
    | [`absoluteZero`](../index.html#abaqus.Model.ModelBase.ModelBase.absoluteZero "abaqus.Model.ModelBase.ModelBase.absoluteZero (Python attribute) — None or a Float specifying the absolute zero constant. The default value is None.") | None or a Float specifying the absolute zero constant. |
    | [`waveFormulation`](../index.html#abaqus.Model.ModelBase.ModelBase.waveFormulation "abaqus.Model.ModelBase.ModelBase.waveFormulation (Python attribute) — A SymbolicConstant specifying the type of incident wave formulation to be used in acoustic problems. Possible values are NOT_SET, SCATTERED, and TOTAL. The default value is NOT_SET.") | A SymbolicConstant specifying the type of incident wave formulation to be used in acoustic problems. |
    | [`universalGas`](../index.html#abaqus.Model.ModelBase.ModelBase.universalGas "abaqus.Model.ModelBase.ModelBase.universalGas (Python attribute) — None or a Float specifying the universal gas constant. The default value is None.") | None or a Float specifying the universal gas constant. |
    | [`noPartsInputFile`](../index.html#abaqus.Model.ModelBase.ModelBase.noPartsInputFile "abaqus.Model.ModelBase.ModelBase.noPartsInputFile (Python attribute) — A Boolean specifying whether an input file should be written without parts and assemblies. The default value is OFF.") | A Boolean specifying whether an input file should be written without parts and assemblies. |
    | [`endRestartStep`](../index.html#abaqus.Model.ModelBase.ModelBase.endRestartStep "abaqus.Model.ModelBase.ModelBase.endRestartStep (Python attribute) — A Boolean specifying that the step specified by restartStep should be terminated at the increment specified by restartIncrement.") | A Boolean specifying that the step specified by **restartStep** should be terminated at the increment specified by **restartIncrement**. |
    | [`shellToSolid`](../index.html#abaqus.Model.ModelBase.ModelBase.shellToSolid "abaqus.Model.ModelBase.ModelBase.shellToSolid (Python attribute) — A Boolean specifying that a shell global model drives a solid submodel.") | A Boolean specifying that a shell global model drives a solid submodel. |
    | [`lastChangedCount`](../index.html#abaqus.Model.ModelBase.ModelBase.lastChangedCount "abaqus.Model.ModelBase.ModelBase.lastChangedCount (Python attribute) — A Float specifying the time stamp that indicates when the model was last changed.") | A Float specifying the time stamp that indicates when the model was last changed. |
    | [`description`](../index.html#abaqus.Model.ModelBase.ModelBase.description "abaqus.Model.ModelBase.ModelBase.description (Python attribute) — A String specifying the purpose and contents of the Model object. The default value is an empty string.") | A String specifying the purpose and contents of the Model object. |
    | [`restartJob`](../index.html#abaqus.Model.ModelBase.ModelBase.restartJob "abaqus.Model.ModelBase.ModelBase.restartJob (Python attribute) — A String specifying the name of the job that generated the restart data.") | A String specifying the name of the job that generated the restart data. |
    | [`restartStep`](../index.html#abaqus.Model.ModelBase.ModelBase.restartStep "abaqus.Model.ModelBase.ModelBase.restartStep (Python attribute) — A String specifying the name of the step where the restart analysis will start.") | A String specifying the name of the step where the restart analysis will start. |
    | [`globalJob`](../index.html#abaqus.Model.ModelBase.ModelBase.globalJob "abaqus.Model.ModelBase.ModelBase.globalJob (Python attribute) — A String specifying the name of the job that generated the results for the global model.") | A String specifying the name of the job that generated the results for the global model. |
    | [`copyConstraints`](../index.html#abaqus.Model.ModelBase.ModelBase.copyConstraints "abaqus.Model.ModelBase.ModelBase.copyConstraints (Python attribute) — A boolean specifying the status of constraints created in a model, in the model which instances this model.") | A boolean specifying the status of constraints created in a model, in the model which instances this model. |
    | [`copyConnectors`](../index.html#abaqus.Model.ModelBase.ModelBase.copyConnectors "abaqus.Model.ModelBase.ModelBase.copyConnectors (Python attribute) — A boolean specifying the status of connectors created in a model, in the model which instances this model.") | A boolean specifying the status of connectors created in a model, in the model which instances this model. |
    | [`copyInteractions`](../index.html#abaqus.Model.ModelBase.ModelBase.copyInteractions "abaqus.Model.ModelBase.ModelBase.copyInteractions (Python attribute) — A boolean specifying the status of interactions created in a model, in the model which instances this model.") | A boolean specifying the status of interactions created in a model, in the model which instances this model. |
    | [`keywordBlock`](../index.html#abaqus.Model.ModelBase.ModelBase.keywordBlock "abaqus.Model.ModelBase.ModelBase.keywordBlock (Python attribute) — A KeywordBlock object.") | A KeywordBlock object. |
    | [`amplitudes`](../index.html#abaqus.Model.ModelBase.ModelBase.amplitudes "abaqus.Model.ModelBase.ModelBase.amplitudes (Python attribute) — A repository of Amplitude objects.") | A repository of Amplitude objects. |
    | [`profiles`](../index.html#abaqus.Model.ModelBase.ModelBase.profiles "abaqus.Model.ModelBase.ModelBase.profiles (Python attribute) — A repository of Profile objects.") | A repository of Profile objects. |
    | [`boundaryConditions`](../index.html#abaqus.Model.ModelBase.ModelBase.boundaryConditions "abaqus.Model.ModelBase.ModelBase.boundaryConditions (Python attribute) — A repository of BoundaryCondition objects.") | A repository of BoundaryCondition objects. |
    | [`constraints`](../index.html#abaqus.Model.ModelBase.ModelBase.constraints "abaqus.Model.ModelBase.ModelBase.constraints (Python attribute) — A repository of ConstrainedSketchConstraint objects.") | A repository of ConstrainedSketchConstraint objects. |
    | [`analyticalFields`](../index.html#abaqus.Model.ModelBase.ModelBase.analyticalFields "abaqus.Model.ModelBase.ModelBase.analyticalFields (Python attribute) — A repository of AnalyticalField objects.") | A repository of AnalyticalField objects. |
    | [`discreteFields`](../index.html#abaqus.Model.ModelBase.ModelBase.discreteFields "abaqus.Model.ModelBase.ModelBase.discreteFields (Python attribute) — A repository of DiscreteField objects.") | A repository of DiscreteField objects. |
    | [`predefinedFields`](../index.html#abaqus.Model.ModelBase.ModelBase.predefinedFields "abaqus.Model.ModelBase.ModelBase.predefinedFields (Python attribute) — A repository of PredefinedField objects.") | A repository of PredefinedField objects. |
    | [`interactions`](../index.html#abaqus.Model.ModelBase.ModelBase.interactions "abaqus.Model.ModelBase.ModelBase.interactions (Python attribute) — A repository of Interaction objects.") | A repository of Interaction objects. |
    | [`interactionProperties`](../index.html#abaqus.Model.ModelBase.ModelBase.interactionProperties "abaqus.Model.ModelBase.ModelBase.interactionProperties (Python attribute) — A repository of InteractionProperty objects.") | A repository of InteractionProperty objects. |
    | [`contactControls`](../index.html#abaqus.Model.ModelBase.ModelBase.contactControls "abaqus.Model.ModelBase.ModelBase.contactControls (Python attribute) — A repository of ContactControl objects.") | A repository of ContactControl objects. |
    | [`contactInitializations`](../index.html#abaqus.Model.ModelBase.ModelBase.contactInitializations "abaqus.Model.ModelBase.ModelBase.contactInitializations (Python attribute) — A repository of ContactInitialization objects.") | A repository of ContactInitialization objects. |
    | [`contactStabilizations`](../index.html#abaqus.Model.ModelBase.ModelBase.contactStabilizations "abaqus.Model.ModelBase.ModelBase.contactStabilizations (Python attribute) — A repository of ContactStabilization objects.") | A repository of ContactStabilization objects. |
    | [`linkedInstances`](../index.html#abaqus.Model.ModelBase.ModelBase.linkedInstances "abaqus.Model.ModelBase.ModelBase.linkedInstances (Python attribute) — A tuple of tuples of Strings specifying the linked child PartInstance name in the current model to the corresponding parent PartInstance name in a different model.") | A tuple of tuples of Strings specifying the linked child PartInstance name in the current model to the corresponding parent PartInstance name in a different model. |
    | [`linkedParts`](../index.html#abaqus.Model.ModelBase.ModelBase.linkedParts "abaqus.Model.ModelBase.ModelBase.linkedParts (Python attribute) — A tuple of tuples of Strings specifying the linked child Part name in the current model to the corresponding parent Part name in a different model.") | A tuple of tuples of Strings specifying the linked child Part name in the current model to the corresponding parent Part name in a different model. |
    | [`loads`](../index.html#abaqus.Model.ModelBase.ModelBase.loads "abaqus.Model.ModelBase.ModelBase.loads (Python attribute) — A repository of Load objects.") | A repository of Load objects. |
    | [`materials`](../index.html#abaqus.Model.ModelBase.ModelBase.materials "abaqus.Model.ModelBase.ModelBase.materials (Python attribute) — A repository of Material objects.") | A repository of Material objects. |
    | [`calibrations`](../index.html#abaqus.Model.ModelBase.ModelBase.calibrations "abaqus.Model.ModelBase.ModelBase.calibrations (Python attribute) — A repository of Calibration objects.") | A repository of Calibration objects. |
    | [`sections`](../index.html#abaqus.Model.ModelBase.ModelBase.sections "abaqus.Model.ModelBase.ModelBase.sections (Python attribute) — A repository of Section objects.") | A repository of Section objects. |
    | [`remeshingRules`](../index.html#abaqus.Model.ModelBase.ModelBase.remeshingRules "abaqus.Model.ModelBase.ModelBase.remeshingRules (Python attribute) — A repository of RemeshingRule objects.") | A repository of RemeshingRule objects. |
    | [`sketches`](../index.html#abaqus.Model.ModelBase.ModelBase.sketches "abaqus.Model.ModelBase.ModelBase.sketches (Python attribute) — A repository of ConstrainedSketch objects.") | A repository of ConstrainedSketch objects. |
    | [`parts`](../index.html#abaqus.Model.ModelBase.ModelBase.parts "abaqus.Model.ModelBase.ModelBase.parts (Python attribute) — A repository of Part objects.") | A repository of Part objects. |
    | [`steps`](../index.html#abaqus.Model.ModelBase.ModelBase.steps "abaqus.Model.ModelBase.ModelBase.steps (Python attribute) — A repository of Step objects.") | A repository of Step objects. |
    | [`featureOptions`](../index.html#abaqus.Model.ModelBase.ModelBase.featureOptions "abaqus.Model.ModelBase.ModelBase.featureOptions (Python attribute) — A FeatureOptions object.") | A FeatureOptions object. |
    | [`adaptiveMeshConstraints`](../index.html#abaqus.Model.ModelBase.ModelBase.adaptiveMeshConstraints "abaqus.Model.ModelBase.ModelBase.adaptiveMeshConstraints (Python attribute) — A repository of AdaptiveMeshConstraint objects.") | A repository of AdaptiveMeshConstraint objects. |
    | [`adaptiveMeshControls`](../index.html#abaqus.Model.ModelBase.ModelBase.adaptiveMeshControls "abaqus.Model.ModelBase.ModelBase.adaptiveMeshControls (Python attribute) — A repository of AdaptiveMeshControl objects.") | A repository of AdaptiveMeshControl objects. |
    | [`timePoints`](../index.html#abaqus.Model.ModelBase.ModelBase.timePoints "abaqus.Model.ModelBase.ModelBase.timePoints (Python attribute) — A repository of TimePoint objects.") | A repository of TimePoint objects. |
    | [`filters`](../index.html#abaqus.Model.ModelBase.ModelBase.filters "abaqus.Model.ModelBase.ModelBase.filters (Python attribute) — A repository of Filter objects.") | A repository of Filter objects. |
    | [`integratedOutputSections`](../index.html#abaqus.Model.ModelBase.ModelBase.integratedOutputSections "abaqus.Model.ModelBase.ModelBase.integratedOutputSections (Python attribute) — A repository of IntegratedOutputSection objects.") | A repository of IntegratedOutputSection objects. |
    | [`fieldOutputRequests`](../index.html#abaqus.Model.ModelBase.ModelBase.fieldOutputRequests "abaqus.Model.ModelBase.ModelBase.fieldOutputRequests (Python attribute) — A repository of FieldOutputRequest objects.") | A repository of FieldOutputRequest objects. |
    | [`historyOutputRequests`](../index.html#abaqus.Model.ModelBase.ModelBase.historyOutputRequests "abaqus.Model.ModelBase.ModelBase.historyOutputRequests (Python attribute) — A repository of HistoryOutputRequest objects.") | A repository of HistoryOutputRequest objects. |
    | [`optimizationTasks`](../index.html#abaqus.Model.ModelBase.ModelBase.optimizationTasks "abaqus.Model.ModelBase.ModelBase.optimizationTasks (Python attribute) — A repository of OptimizationTask objects.") | A repository of OptimizationTask objects. |
    | [`tableCollections`](../index.html#abaqus.Model.ModelBase.ModelBase.tableCollections "abaqus.Model.ModelBase.ModelBase.tableCollections (Python attribute) — A repository of TableCollection objects.") | A repository of TableCollection objects. |
    | [`eventSeriesTypes`](../index.html#abaqus.Model.ModelBase.ModelBase.eventSeriesTypes "abaqus.Model.ModelBase.ModelBase.eventSeriesTypes (Python attribute) — A repository of EventSeriesType objects.") | A repository of EventSeriesType objects. |
    | [`eventSeriesDatas`](../index.html#abaqus.Model.ModelBase.ModelBase.eventSeriesDatas "abaqus.Model.ModelBase.ModelBase.eventSeriesDatas (Python attribute) — A repository of EventSeriesData objects.") | A repository of EventSeriesData objects. |
    | [`restartIncrement`](../index.html#abaqus.Model.ModelBase.ModelBase.restartIncrement "abaqus.Model.ModelBase.ModelBase.restartIncrement (Python attribute) — An Int specifying the increment, interval, iteration or cycle where the restart analysis will start. To select the end of the step use the SymbolicConstant STEP_END.") | An Int specifying the increment, interval, iteration or cycle where the restart analysis will start. |
    | [`rootAssembly`](../index.html#abaqus.Model.ModelBase.ModelBase.rootAssembly "abaqus.Model.ModelBase.ModelBase.rootAssembly (Python attribute) — An Assembly object.") | An Assembly object. |

    Public Methods:

    |  |  |
    | --- | --- |
    | [`Part`](#abaqus.Part.PartModel.PartModel.Part "abaqus.Part.PartModel.PartModel.Part (Python method) — This method creates a Part object and places it in the parts repository.")(name, dimensionality, type[, twist]) | This method creates a Part object and places it in the parts repository. |

    Inherited from [`ModelBase`](../index.html#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | `__init__`(name[, description, ...]) | This method creates a Model object. |
    | [`setValues`](../index.html#abaqus.Model.ModelBase.ModelBase.setValues "abaqus.Model.ModelBase.ModelBase.setValues (Python method) — This method modifies the Model object.")([description, noPartsInputFile, ...]) | This method modifies the Model object. |

    ---

    Member Details:

    Part(*[name](#abaqus.Part.PartModel.PartModel.Part.name "abaqus.Part.PartModel.PartModel.Part.name (Python parameter) — A String specifying the repository key.")*, *[dimensionality](#abaqus.Part.PartModel.PartModel.Part.dimensionality "abaqus.Part.PartModel.PartModel.Part.dimensionality (Python parameter) — A SymbolicConstant specifying the dimensionality of the part.")*, *[type](#abaqus.Part.PartModel.PartModel.Part.type "abaqus.Part.PartModel.PartModel.Part.type (Python parameter) — A SymbolicConstant specifying the type of the part.")*, *[twist](#abaqus.Part.PartModel.PartModel.Part.twist "abaqus.Part.PartModel.PartModel.Part.twist (Python parameter) — A Boolean specifying whether to include a twist DEGREE OF FREEDOM in the part (only available when dimensionality = AXISYMMETRIC and type = DEFORMABLE_BODY).")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartModel.py#L23-L59)[¶](#abaqus.Part.PartModel.PartModel.Part "Permalink to this definition")
    :   This method creates a Part object and places it in the parts repository.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].Part
        ```

        Note

        Check [Part on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartModel.PartModel.Part-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Part.PartModel.PartModel.Part.name "Permalink to this definition")
            :   A String specifying the repository key.

            dimensionality[¶](#abaqus.Part.PartModel.PartModel.Part.dimensionality "Permalink to this definition")
            :   A SymbolicConstant specifying the dimensionality of the part. Possible values are
                THREE\_D, TWO\_D\_PLANAR, and AXISYMMETRIC.

            type[¶](#abaqus.Part.PartModel.PartModel.Part.type "Permalink to this definition")
            :   A SymbolicConstant specifying the type of the part. Possible values are DEFORMABLE\_BODY,
                EULERIAN, DISCRETE\_RIGID\_SURFACE, and ANALYTIC\_RIGID\_SURFACE.

            twist=`0`[¶](#abaqus.Part.PartModel.PartModel.Part.twist "Permalink to this definition")
            :   A Boolean specifying whether to include a twist DEGREE OF FREEDOM in the part (only
                available when **dimensionality** = AXISYMMETRIC and **type** = DEFORMABLE\_BODY). The default
                value is OFF.

        Returns:[¶](#abaqus.Part.PartModel.PartModel.Part-returns "Permalink to this headline")
        :   A Part object.

        Return type:[¶](#abaqus.Part.PartModel.PartModel.Part-return-type "Permalink to this headline")
        :   [`Part`](#abaqus.Part.PartModel.Part "abaqus.Part.PartModel.Part (Python class) — Bases: BasicGeometryPart, MeshEditPart, MeshPart, PropertyPart, RegionPart, Displayable")

*class* PartBase(*[name](#abaqus.Part.PartBase.PartBase "abaqus.Part.PartBase.PartBase.__init__.name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[dimensionality](#abaqus.Part.PartBase.PartBase "abaqus.Part.PartBase.PartBase.__init__.dimensionality (Python parameter)"): [SymbolicConstant](../../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.SymbolicConstant "abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant (Python class)")*, *[type](#abaqus.Part.PartBase.PartBase "abaqus.Part.PartBase.PartBase.__init__.type (Python parameter)"): [SymbolicConstant](../../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.SymbolicConstant "abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant (Python class)")*, *[twist](#abaqus.Part.PartBase.PartBase "abaqus.Part.PartBase.PartBase.__init__.twist (Python parameter)"): [AbaqusBoolean](../../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.AbaqusBoolean "abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean (Python class)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `OFF`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L60-L1850)[¶](#abaqus.Part.PartBase.PartBase "Permalink to this definition")

*class* PartBase(*[name](#abaqus.Part.PartBase.PartBase "abaqus.Part.PartBase.PartBase.__init__.name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[objectToCopy](#abaqus.Part.PartBase.PartBase "abaqus.Part.PartBase.PartBase.__init__.objectToCopy (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[scale](#abaqus.Part.PartBase.PartBase "abaqus.Part.PartBase.PartBase.__init__.scale (Python parameter)"): [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") = `1`*, *[mirrorPlane](#abaqus.Part.PartBase.PartBase "abaqus.Part.PartBase.PartBase.__init__.mirrorPlane (Python parameter)"): [SymbolicConstant](../../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.SymbolicConstant "abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant (Python class)") = `NONE`*, *[compressFeatureList](#abaqus.Part.PartBase.PartBase "abaqus.Part.PartBase.PartBase.__init__.compressFeatureList (Python parameter)"): [AbaqusBoolean](../../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.AbaqusBoolean "abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean (Python class)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `OFF`*, *[separate](#abaqus.Part.PartBase.PartBase "abaqus.Part.PartBase.PartBase.__init__.separate (Python parameter)"): [AbaqusBoolean](../../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.AbaqusBoolean "abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean (Python class)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `OFF`*)
:   Bases: [`PartFeature`](#abaqus.Part.PartFeature.PartFeature "abaqus.Part.PartFeature.PartFeature (Python class) — Bases: Feature")

    The Part object defines the physical attributes of a structure. Parts are instanced into the assembly and
    positioned before an analysis.

    Note

    This object can be accessed by:

    ```python
    import part
    mdb.models[name].parts[name]
    ```

    Public Data Attributes:

    |  |  |
    | --- | --- |
    | [`geometryValidity`](#abaqus.Part.PartBase.PartBase.geometryValidity "abaqus.Part.PartBase.PartBase.geometryValidity (Python attribute) — A Boolean specifying the validity of the geometry of the part. The value is computed, but it can be set to ON to perform feature and mesh operations on an invalid part. There is no guarantee that such operations will work if the part was originally invalid.") | A Boolean specifying the validity of the geometry of the part. |
    | [`isOutOfDate`](#abaqus.Part.PartBase.PartBase.isOutOfDate "abaqus.Part.PartBase.PartBase.isOutOfDate (Python attribute) — An Int specifying that feature parameters have been modified but that the part has not been regenerated. Possible values are 0 and 1.") | An Int specifying that feature parameters have been modified but that the part has not been regenerated. |
    | [`timeStamp`](#abaqus.Part.PartBase.PartBase.timeStamp "abaqus.Part.PartBase.PartBase.timeStamp (Python attribute) — A Float specifying when the part was last modified.") | A Float specifying when the part was last modified. |
    | [`vertices`](#abaqus.Part.PartBase.PartBase.vertices "abaqus.Part.PartBase.PartBase.vertices (Python attribute) — A VertexArray object specifying all the vertices in the part.") | A VertexArray object specifying all the vertices in the part. |
    | [`ignoredVertices`](#abaqus.Part.PartBase.PartBase.ignoredVertices "abaqus.Part.PartBase.PartBase.ignoredVertices (Python attribute) — An IgnoredVertexArray object specifying all the ignored vertices in the part.") | An IgnoredVertexArray object specifying all the ignored vertices in the part. |
    | [`edges`](#abaqus.Part.PartBase.PartBase.edges "abaqus.Part.PartBase.PartBase.edges (Python attribute) — An EdgeArray object specifying all the edges in the part.") | An EdgeArray object specifying all the edges in the part. |
    | [`ignoredEdges`](#abaqus.Part.PartBase.PartBase.ignoredEdges "abaqus.Part.PartBase.PartBase.ignoredEdges (Python attribute) — An IgnoredEdgeArray object specifying all the ignored edges in the part.") | An IgnoredEdgeArray object specifying all the ignored edges in the part. |
    | [`faces`](#abaqus.Part.PartBase.PartBase.faces "abaqus.Part.PartBase.PartBase.faces (Python attribute) — A FaceArray object specifying all the faces in the part.") | A FaceArray object specifying all the faces in the part. |
    | [`cells`](#abaqus.Part.PartBase.PartBase.cells "abaqus.Part.PartBase.PartBase.cells (Python attribute) — A CellArray object specifying all the cells in the part.") | A CellArray object specifying all the cells in the part. |
    | [`features`](#abaqus.Part.PartBase.PartBase.features "abaqus.Part.PartBase.PartBase.features (Python attribute) — A repository of Feature objects specifying all the features in the part.") | A repository of Feature objects specifying all the features in the part. |
    | [`featuresById`](#abaqus.Part.PartBase.PartBase.featuresById "abaqus.Part.PartBase.PartBase.featuresById (Python attribute) — A repository of Feature objects specifying all Feature objects in the part. The Feature objects in the featuresById repository are the same as the Feature objects in the features' repository. However, the key to the objects in the featuresById repository is an integer specifying the ID, whereas the key to the objects in the features repository is a string specifying the name.") | A repository of Feature objects specifying all Feature objects in the part. |
    | [`datums`](#abaqus.Part.PartBase.PartBase.datums "abaqus.Part.PartBase.PartBase.datums (Python attribute) — A repository of Datum objects specifying all the datums in the part.") | A repository of Datum objects specifying all the datums in the part. |
    | [`elements`](#abaqus.Part.PartBase.PartBase.elements "abaqus.Part.PartBase.PartBase.elements (Python attribute) — A MeshElementArray object specifying all the elements in the part.") | A MeshElementArray object specifying all the elements in the part. |
    | [`elemFaces`](#abaqus.Part.PartBase.PartBase.elemFaces "abaqus.Part.PartBase.PartBase.elemFaces (Python attribute) — A repository of MeshFace objects specifying all the element faces in the part. For a given element and a given face index within that element, the corresponding MeshFace object can be retrieved from the repository by using the key calculated as (i*8 + j), where i and j are zero-based element and face indices, respectively.") | A repository of MeshFace objects specifying all the element faces in the part. |
    | [`elementFaces`](#abaqus.Part.PartBase.PartBase.elementFaces "abaqus.Part.PartBase.PartBase.elementFaces (Python attribute) — A MeshFaceArray object specifying all the unique element faces in the part.") | A MeshFaceArray object specifying all the unique element faces in the part. |
    | [`nodes`](#abaqus.Part.PartBase.PartBase.nodes "abaqus.Part.PartBase.PartBase.nodes (Python attribute) — A MeshNodeArray object specifying all the nodes in the part.") | A MeshNodeArray object specifying all the nodes in the part. |
    | [`retainedNodes`](#abaqus.Part.PartBase.PartBase.retainedNodes "abaqus.Part.PartBase.PartBase.retainedNodes (Python attribute) — A MeshNodeArray object specifying all the retained nodes in the substructure part.") | A MeshNodeArray object specifying all the retained nodes in the substructure part. |
    | [`sets`](#abaqus.Part.PartBase.PartBase.sets "abaqus.Part.PartBase.PartBase.sets (Python attribute) — A repository of Set objects specifying for more information, see Set.") | A repository of Set objects specifying for more information, see Set. |
    | [`allSets`](#abaqus.Part.PartBase.PartBase.allSets "abaqus.Part.PartBase.PartBase.allSets (Python attribute) — A repository of Set objects specifying the contents of the allSets repository is the same as the contents of the sets repository.") | A repository of Set objects specifying the contents of the **allSets** repository is the same as the contents of the **sets** repository. |
    | [`allInternalSets`](#abaqus.Part.PartBase.PartBase.allInternalSets "abaqus.Part.PartBase.PartBase.allInternalSets (Python attribute) — A repository of Set objects specifying picked regions.") | A repository of Set objects specifying picked regions. |
    | [`surfaces`](#abaqus.Part.PartBase.PartBase.surfaces "abaqus.Part.PartBase.PartBase.surfaces (Python attribute) — A repository of Surface objects specifying for more information, see Surface.") | A repository of Surface objects specifying for more information, see Surface. |
    | [`allSurfaces`](#abaqus.Part.PartBase.PartBase.allSurfaces "abaqus.Part.PartBase.PartBase.allSurfaces (Python attribute) — A repository of Surface objects specifying the contents of the allSurfaces repository is the same as the contents of the surfaces repository.") | A repository of Surface objects specifying the contents of the **allSurfaces** repository is the same as the contents of the **surfaces** repository. |
    | [`allInternalSurfaces`](#abaqus.Part.PartBase.PartBase.allInternalSurfaces "abaqus.Part.PartBase.PartBase.allInternalSurfaces (Python attribute) — A repository of Surface objects specifying picked regions.") | A repository of Surface objects specifying picked regions. |
    | [`skins`](#abaqus.Part.PartBase.PartBase.skins "abaqus.Part.PartBase.PartBase.skins (Python attribute) — A repository of Skin objects specifying the skins created on the part.") | A repository of Skin objects specifying the skins created on the part. |
    | [`stringers`](#abaqus.Part.PartBase.PartBase.stringers "abaqus.Part.PartBase.PartBase.stringers (Python attribute) — A repository of Stringer objects specifying the stringers created on the part.") | A repository of Stringer objects specifying the stringers created on the part. |
    | [`referencePoints`](#abaqus.Part.PartBase.PartBase.referencePoints "abaqus.Part.PartBase.PartBase.referencePoints (Python attribute) — A repository of ReferencePoint objects.") | A repository of ReferencePoint objects. |
    | [`engineeringFeatures`](#abaqus.Part.PartBase.PartBase.engineeringFeatures "abaqus.Part.PartBase.PartBase.engineeringFeatures (Python attribute) — An EngineeringFeature object.") | An EngineeringFeature object. |
    | [`sectionAssignments`](#abaqus.Part.PartBase.PartBase.sectionAssignments "abaqus.Part.PartBase.PartBase.sectionAssignments (Python attribute) — A SectionAssignmentArray object.") | A SectionAssignmentArray object. |
    | [`materialOrientations`](#abaqus.Part.PartBase.PartBase.materialOrientations "abaqus.Part.PartBase.PartBase.materialOrientations (Python attribute) — A MaterialOrientationArray object.") | A MaterialOrientationArray object. |
    | [`compositeLayups`](#abaqus.Part.PartBase.PartBase.compositeLayups "abaqus.Part.PartBase.PartBase.compositeLayups (Python attribute) — A repository of CompositeLayup objects.") | A repository of CompositeLayup objects. |
    | [`elemEdges`](#abaqus.Part.PartBase.PartBase.elemEdges "abaqus.Part.PartBase.PartBase.elemEdges (Python attribute) — A repository of MeshEdge objects specifying all the element edges in the part. For a given element and a given edge index on a given face within that element, the corresponding MeshEdge object can be retrieved from the repository by using the key calculated as (i*32 + j*4 + k), where i, j, and k are zero-based element, face, and edge indices, respectively.") | A repository of MeshEdge objects specifying all the element edges in the part. |
    | [`elementEdges`](#abaqus.Part.PartBase.PartBase.elementEdges "abaqus.Part.PartBase.PartBase.elementEdges (Python attribute) — A MeshEdgeArray object specifying all the unique element edges in the part.") | A MeshEdgeArray object specifying all the unique element edges in the part. |
    | `name` | A String specifying the repository key. |
    | `id` | An Int specifying the ID of the feature. |

    Inherited from [`Feature`](feature.html#abaqus.Feature.Feature.Feature "abaqus.Feature.Feature.Feature (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | [`name`](feature.html#abaqus.Feature.Feature.Feature.name "abaqus.Feature.Feature.Feature.name (Python attribute) — A String specifying the repository key.") | A String specifying the repository key. |
    | [`id`](feature.html#abaqus.Feature.Feature.Feature.id "abaqus.Feature.Feature.Feature.id (Python attribute) — An Int specifying the ID of the feature.") | An Int specifying the ID of the feature. |

    Public Methods:

    |  |  |
    | --- | --- |
    | `__init__`() |  |
    | [`PartFromBooleanCut`](#abaqus.Part.PartBase.PartBase.PartFromBooleanCut "abaqus.Part.PartBase.PartBase.PartFromBooleanCut (Python method) — This method creates a Part in the parts repository after subtracting or cutting the geometries of a group of part instances from that of a base part instance.")(name, instanceToBeCut, ...) | This method creates a Part in the parts repository after subtracting or cutting the geometries of a group of part instances from that of a base part instance. |
    | [`PartFromBooleanMerge`](#abaqus.Part.PartBase.PartBase.PartFromBooleanMerge "abaqus.Part.PartBase.PartBase.PartFromBooleanMerge (Python method) — This method creates a Part in the parts repository after merging two or more part instances. The part instances can be either Abaqus native parts or orphan mesh parts, but they cannot be a combination of both.")(name, instances[, ...]) | This method creates a Part in the parts repository after merging two or more part instances. |
    | [`PartFromExtrude2DMesh`](#abaqus.Part.PartBase.PartBase.PartFromExtrude2DMesh "abaqus.Part.PartBase.PartBase.PartFromExtrude2DMesh (Python method) — This method creates a Part object by extruding an existing two-dimensional orphan mesh Part object in the positive Z direction and places it in the parts repository.")(name, part, depth, ...) | This method creates a Part object by extruding an existing two-dimensional orphan mesh Part object in the positive **Z** direction and places it in the parts repository. |
    | [`PartFromGeometryFile`](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile "abaqus.Part.PartBase.PartBase.PartFromGeometryFile (Python method) — This method creates a Part object and places it in the parts repository.")(name, geometryFile, ...) | This method creates a Part object and places it in the parts repository. |
    | [`PartFromInstanceMesh`](#abaqus.Part.PartBase.PartBase.PartFromInstanceMesh "abaqus.Part.PartBase.PartBase.PartFromInstanceMesh (Python method) — This method creates a Part object containing the mesh found in the supplied PartInstance objects and places the new Part object in the parts repository.")(name[, partInstances, ...]) | This method creates a Part object containing the mesh found in the supplied PartInstance objects and places the new Part object in the parts repository. |
    | [`PartFromMesh`](#abaqus.Part.PartBase.PartBase.PartFromMesh "abaqus.Part.PartBase.PartBase.PartFromMesh (Python method) — This method creates a Part object containing the mesh found in the part and places the new Part object in the parts repository.")(name[, copySets]) | This method creates a Part object containing the mesh found in the part and places the new Part object in the parts repository. |
    | [`PartFromMeshMirror`](#abaqus.Part.PartBase.PartBase.PartFromMeshMirror "abaqus.Part.PartBase.PartBase.PartFromMeshMirror (Python method) — This method creates a Part object by mirroring an existing orphan mesh Part object about a specified plane and places it in the parts repository. The result is a union of the original and the mirrored copy. Contrast the PartFromMeshMirror method with the mirrorPlane argument of the Part copy constructor. The mirrorPlane argument creates only the second half of the part but does not unite the two halves.")(name, part, point1, point2) | This method creates a Part object by mirroring an existing orphan mesh Part object about a specified plane and places it in the parts repository. |
    | [`PartFromNodesAndElements`](#abaqus.Part.PartBase.PartBase.PartFromNodesAndElements "abaqus.Part.PartBase.PartBase.PartFromNodesAndElements (Python method) — This method creates a Part object from nodes and elements and places it in the parts repository.")(name, ...[, twist]) | This method creates a Part object from nodes and elements and places it in the parts repository. |
    | [`PartFromOdb`](#abaqus.Part.PartBase.PartBase.PartFromOdb "abaqus.Part.PartBase.PartBase.PartFromOdb (Python method) — This method creates an orphan mesh Part object by reading an output database. The new part is placed in the parts repository.")(name, odb[, fileName, instance, ...]) | This method creates an orphan mesh Part object by reading an output database. |
    | [`PartFromSection3DMeshByPlane`](#abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane "abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane (Python method) — This method creates a Part object by cutting an existing three-dimensional orphan mesh Part object by a plane and places it in the parts repository. This method is valid only for orphan mesh parts composed of 8-node brick elements.")(name, part, ...) | This method creates a Part object by cutting an existing three-dimensional orphan mesh Part object by a plane and places it in the parts repository. |
    | [`PartFromSubstructure`](#abaqus.Part.PartBase.PartBase.PartFromSubstructure "abaqus.Part.PartBase.PartBase.PartFromSubstructure (Python method) — This method creates a substructure Part object by reading a substructure sim file and places it in the parts repository.")(name, substructureFile, ...) | This method creates a substructure Part object by reading a substructure sim file and places it in the parts repository. |
    | [`Part2DGeomFrom2DMesh`](#abaqus.Part.PartBase.PartBase.Part2DGeomFrom2DMesh "abaqus.Part.PartBase.PartBase.Part2DGeomFrom2DMesh (Python method) — This method creates a geometric Part object from the outline of an existing two-dimensional orphan mesh Part object and places it in the parts repository. If the Part2DGeomFrom2DMesh method cannot create a valid two-dimensional shell section from the two-dimensional mesh, the method fails and creates an empty geometry part with a failed base shell feature.")(name, part, featureAngle) | This method creates a geometric Part object from the outline of an existing two-dimensional orphan mesh Part object and places it in the parts repository. |
    | [`setValues`](#abaqus.Part.PartBase.PartBase.setValues "abaqus.Part.PartBase.PartBase.setValues (Python method) — This method modifies the Part object.")(\*args, \*\*kwargs) | This method modifies the Part object. |
    | [`addGeomToSketch`](#abaqus.Part.PartBase.PartBase.addGeomToSketch "abaqus.Part.PartBase.PartBase.addGeomToSketch (Python method) — This method converts a part into a sketch by projecting all of the edges of the part onto the X-Y plane of the sketch. You can use addGeomToSketch with a part of any modeling space.")(sketch) | This method converts a part into a sketch by projecting all of the edges of the part onto the X-Y plane of the sketch. |
    | [`assignThickness`](#abaqus.Part.PartBase.PartBase.assignThickness "abaqus.Part.PartBase.PartBase.assignThickness (Python method) — This method assigns thickness data to shell faces. The thickness can be used while assigning shell and membrane sections to faces.")(faces[, thickness, ...]) | This method assigns thickness data to shell faces. |
    | [`backup`](#abaqus.Part.PartBase.PartBase.backup "abaqus.Part.PartBase.PartBase.backup (Python method) — This method makes a backup copy of the features in the part.")() | This method makes a backup copy of the features in the part. |
    | [`checkGeometry`](#abaqus.Part.PartBase.PartBase.checkGeometry "abaqus.Part.PartBase.PartBase.checkGeometry (Python method) — This method checks the validity of the geometry of the part and prints a count of all topological entities on the part (faces, edges, vertices, etc.).")([detailed, reportFacetErrors, ...]) | This method checks the validity of the geometry of the part and prints a count of all topological entities on the part (faces, edges, vertices, etc.). |
    | [`clearGeometryCache`](#abaqus.Part.PartBase.PartBase.clearGeometryCache "abaqus.Part.PartBase.PartBase.clearGeometryCache (Python method) — This method clears the geometry cache.")() | This method clears the geometry cache. |
    | [`deleteAllFeatures`](#abaqus.Part.PartBase.PartBase.deleteAllFeatures "abaqus.Part.PartBase.PartBase.deleteAllFeatures (Python method) — This method deletes all the features in the part.")() | This method deletes all the features in the part. |
    | [`deleteFeatures`](#abaqus.Part.PartBase.PartBase.deleteFeatures "abaqus.Part.PartBase.PartBase.deleteFeatures (Python method) — This method deletes the given features.")(featureNames) | This method deletes the given features. |
    | [`getAngle`](#abaqus.Part.PartBase.PartBase.getAngle "abaqus.Part.PartBase.PartBase.getAngle (Python method) — This method returns the angle between the specified entities.")(plane1, plane2, line1, line2[, ...]) | This method returns the angle between the specified entities. |
    | [`getArea`](#abaqus.Part.PartBase.PartBase.getArea "abaqus.Part.PartBase.PartBase.getArea (Python method) — This method returns the total surface area of a given face or group of faces.")(faces[, relativeAccuracy]) | This method returns the total surface area of a given face or group of faces. |
    | [`getAssociatedCADPaths`](#abaqus.Part.PartBase.PartBase.getAssociatedCADPaths "abaqus.Part.PartBase.PartBase.getAssociatedCADPaths (Python method) — This method returns the paths to the associated CAD part and root file. These are only available if the part was imported from one of the supported CAD softwares using the Associative Import capability. The root file can be the assembly file or the part file, depending on what which one was imported.")() | This method returns the paths to the associated CAD part and root file. |
    | [`getCADParameters`](#abaqus.Part.PartBase.PartBase.getCADParameters "abaqus.Part.PartBase.PartBase.getCADParameters (Python method) — This method returns the names and values of the CAD parameters associated with the part. These are only available if the part was imported from one of the supported CAD softwares using the Associative Import capability, and if the parameter names defined in that CAD software are prefixed with the string ABQ.")() | This method returns the names and values of the CAD parameters associated with the part. |
    | [`getCentroid`](#abaqus.Part.PartBase.PartBase.getCentroid "abaqus.Part.PartBase.PartBase.getCentroid (Python method) — Location of the centroid of a given face/cell or group of faces/cells.")(faces, cells[, relativeAccuracy]) | Location of the centroid of a given face/cell or group of faces/cells. |
    | [`getCoordinates`](#abaqus.Part.PartBase.PartBase.getCoordinates "abaqus.Part.PartBase.PartBase.getCoordinates (Python method) — This method returns the coordinates of specified point.")(entity, csys) | This method returns the coordinates of specified point. |
    | [`getCurvature`](#abaqus.Part.PartBase.PartBase.getCurvature "abaqus.Part.PartBase.PartBase.getCurvature (Python method) — This method returns the maximum curvature of a given edge or group of edges. For an arc, the curvature is constant over the entire edge, and equal to the inverse of the radius. For a straight line, the curvature is constant and equal to 0. For a spline edge, the curvature varies over a range, and this methods computes the maximum.")(edges[, samplePoints]) | This method returns the maximum curvature of a given edge or group of edges. |
    | [`getDistance`](#abaqus.Part.PartBase.PartBase.getDistance "abaqus.Part.PartBase.PartBase.getDistance (Python method) — Depending on the arguments provided, this method returns one of the following:")(entity1, entity2) | Depending on the arguments provided, this method returns one of the following: |
    | [`getLength`](#abaqus.Part.PartBase.PartBase.getLength "abaqus.Part.PartBase.PartBase.getLength (Python method) — This method returns the length of a given edge or group of edges.")(edges) | This method returns the length of a given edge or group of edges. |
    | [`getPerimeter`](#abaqus.Part.PartBase.PartBase.getPerimeter "abaqus.Part.PartBase.PartBase.getPerimeter (Python method) — This method returns the total perimeter of a given face or group of faces. All faces need to be on the same part. If the specified faces have shared edges, these edges are excluded from the computation, thus providing the length of the outer perimeter of the specified faces.")(faces) | This method returns the total perimeter of a given face or group of faces. |
    | [`getVolume`](#abaqus.Part.PartBase.PartBase.getVolume "abaqus.Part.PartBase.PartBase.getVolume (Python method) — This method returns the volume area of a given cell or group of cells.")(cells[, relativeAccuracy]) | This method returns the volume area of a given cell or group of cells. |
    | [`getMassProperties`](#abaqus.Part.PartBase.PartBase.getMassProperties "abaqus.Part.PartBase.PartBase.getMassProperties (Python method) — This method returns the mass properties of a part or region. Only beams, trusses, shells, solids, point, nonstructural mass, and rotary inertia elements are supported.")([regions, ...]) | This method returns the mass properties of a part or region. |
    | [`getFeatureFaces`](#abaqus.Part.PartBase.PartBase.getFeatureFaces "abaqus.Part.PartBase.PartBase.getFeatureFaces (Python method) — This method returns a sequence of Face objects that are created by the given feature.")(name) | This method returns a sequence of Face objects that are created by the given feature. |
    | [`getFeatureEdges`](#abaqus.Part.PartBase.PartBase.getFeatureEdges "abaqus.Part.PartBase.PartBase.getFeatureEdges (Python method) — This method returns a sequence of Edge objects that are created by the given feature.")(name) | This method returns a sequence of Edge objects that are created by the given feature. |
    | [`getFeatureCells`](#abaqus.Part.PartBase.PartBase.getFeatureCells "abaqus.Part.PartBase.PartBase.getFeatureCells (Python method) — This method returns a sequence of Cell objects that are created by the given feature.")(name) | This method returns a sequence of Cell objects that are created by the given feature. |
    | [`getFeatureVertices`](#abaqus.Part.PartBase.PartBase.getFeatureVertices "abaqus.Part.PartBase.PartBase.getFeatureVertices (Python method) — This method returns a sequence of ConstrainedSketchVertex objects that are created by the given feature.")(name) | This method returns a sequence of ConstrainedSketchVertex objects that are created by the given feature. |
    | [`isAlignedWithSketch`](#abaqus.Part.PartBase.PartBase.isAlignedWithSketch "abaqus.Part.PartBase.PartBase.isAlignedWithSketch (Python method) — This method checks if the normal of an analytical rigid surface part is aligned with that of its sketch.")() | This method checks if the normal of an analytical rigid surface part is aligned with that of its sketch. |
    | [`printAssignedSections`](#abaqus.Part.PartBase.PartBase.printAssignedSections "abaqus.Part.PartBase.PartBase.printAssignedSections (Python method) — This method prints information on each section that has been assigned to a region of the part.")() | This method prints information on each section that has been assigned to a region of the part. |
    | [`projectEdgesOntoSketch`](#abaqus.Part.PartBase.PartBase.projectEdgesOntoSketch "abaqus.Part.PartBase.PartBase.projectEdgesOntoSketch (Python method) — This method projects the selected edges of a part onto the specified ConstrainedSketch object. The edges appear as sketch geometry after projection. If the plane of projection is not parallel to the specified edge, the resultant sketch geometry may be of a different type. For example, a circular edge can be projected as an ellipse or a line depending on the angle of the plane of projection. By default, the projected edge will be constrained to the background geometry. You can remove this constraint by setting constrainToBackground to False.")(sketch, edges[, ...]) | This method projects the selected edges of a part onto the specified ConstrainedSketch object. |
    | [`projectReferencesOntoSketch`](#abaqus.Part.PartBase.PartBase.projectReferencesOntoSketch "abaqus.Part.PartBase.PartBase.projectReferencesOntoSketch (Python method) — This method projects the vertices of specified edges, and datum points from the part onto the specified ConstrainedSketch object. The vertices and datum points appear on the sketch as reference geometry.")(sketch[, ...]) | This method projects the vertices of specified edges, and datum points from the part onto the specified ConstrainedSketch object. |
    | [`queryAttributes`](#abaqus.Part.PartBase.PartBase.queryAttributes "abaqus.Part.PartBase.PartBase.queryAttributes (Python method) — This method prints the following information about a part:")([printResults]) | This method prints the following information about a part: |
    | [`queryCachedStates`](#abaqus.Part.PartBase.PartBase.queryCachedStates "abaqus.Part.PartBase.PartBase.queryCachedStates (Python method) — This method displays the position of geometric states relative to the sequence of features in the part cache.")() | This method displays the position of geometric states relative to the sequence of features in the part cache. |
    | [`queryGeometry`](#abaqus.Part.PartBase.PartBase.queryGeometry "abaqus.Part.PartBase.PartBase.queryGeometry (Python method) — This method prints the following information about a part:")([relativeAccuracy, printResults]) | This method prints the following information about a part: |
    | [`queryRegionsMissingSections`](#abaqus.Part.PartBase.PartBase.queryRegionsMissingSections "abaqus.Part.PartBase.PartBase.queryRegionsMissingSections (Python method) — This method returns all regions in the part that do not have a section assignment but require one for analysis.")() | This method returns all regions in the part that do not have a section assignment but require one for analysis. |
    | [`queryDisjointPlyRegions`](#abaqus.Part.PartBase.PartBase.queryDisjointPlyRegions "abaqus.Part.PartBase.PartBase.queryDisjointPlyRegions (Python method) — This method provides a list of all composite plys in the current part which have disjoint regions.")() | This method provides a list of all composite plys in the current part which have disjoint regions. |
    | [`regenerate`](#abaqus.Part.PartBase.PartBase.regenerate "abaqus.Part.PartBase.PartBase.regenerate (Python method) — This method regenerates a part.")() | This method regenerates a part. |
    | [`regenerationWarnings`](#abaqus.Part.PartBase.PartBase.regenerationWarnings "abaqus.Part.PartBase.PartBase.regenerationWarnings (Python method) — This method prints any regeneration warnings associated with the features.")() | This method prints any regeneration warnings associated with the features. |
    | [`removeInvalidGeometry`](#abaqus.Part.PartBase.PartBase.removeInvalidGeometry "abaqus.Part.PartBase.PartBase.removeInvalidGeometry (Python method) — Removes all invalid entities from the part, leaving a valid part.")() | Removes all invalid entities from the part, leaving a valid part. |
    | [`restore`](#abaqus.Part.PartBase.PartBase.restore "abaqus.Part.PartBase.PartBase.restore (Python method) — This method restores the parameters of all features in the assembly to the value they had before a failed regeneration.")() | This method restores the parameters of all features in the assembly to the value they had before a failed regeneration. |
    | [`resumeAllFeatures`](#abaqus.Part.PartBase.PartBase.resumeAllFeatures "abaqus.Part.PartBase.PartBase.resumeAllFeatures (Python method) — This method resumes all the suppressed features in the part.")() | This method resumes all the suppressed features in the part. |
    | [`resumeFeatures`](#abaqus.Part.PartBase.PartBase.resumeFeatures "abaqus.Part.PartBase.PartBase.resumeFeatures (Python method) — This method resumes the specified suppressed features in the part.")(featureNames) | This method resumes the specified suppressed features in the part. |
    | [`resumeLastSetFeatures`](#abaqus.Part.PartBase.PartBase.resumeLastSetFeatures "abaqus.Part.PartBase.PartBase.resumeLastSetFeatures (Python method) — This method resumes the last set of features to be suppressed in the part.")() | This method resumes the last set of features to be suppressed in the part. |
    | [`saveGeometryCache`](#abaqus.Part.PartBase.PartBase.saveGeometryCache "abaqus.Part.PartBase.PartBase.saveGeometryCache (Python method) — This method caches the current geometry.")() | This method caches the current geometry. |
    | [`setAssociatedCADPaths`](#abaqus.Part.PartBase.PartBase.setAssociatedCADPaths "abaqus.Part.PartBase.PartBase.setAssociatedCADPaths (Python method) — This method sets the paths to the associated CAD part and root file. This method is only available if the part was imported from one of the supported CAD softwares using the Associative Import capability. The root file can be the assembly file or the part file, depending on the one that was imported. This method can be used to specify the new paths when the CAD data is moved to a different directory.")([partFile, rootFile]) | This method sets the paths to the associated CAD part and root file. |
    | [`suppressFeatures`](#abaqus.Part.PartBase.PartBase.suppressFeatures "abaqus.Part.PartBase.PartBase.suppressFeatures (Python method) — This method suppresses the given features.")(featureNames) | This method suppresses the given features. |
    | [`writeAcisFile`](#abaqus.Part.PartBase.PartBase.writeAcisFile "abaqus.Part.PartBase.PartBase.writeAcisFile (Python method) — This method exports the geometry of the part to a named file in ACIS format.")(fileName[, version]) | This method exports the geometry of the part to a named file in ACIS format. |
    | [`writeCADParameters`](#abaqus.Part.PartBase.PartBase.writeCADParameters "abaqus.Part.PartBase.PartBase.writeCADParameters (Python method) — This method writes the parameters that were imported from the CAD system to a parameter file.")(paramFile[, ...]) | This method writes the parameters that were imported from the CAD system to a parameter file. |
    | [`writeIgesFile`](#abaqus.Part.PartBase.PartBase.writeIgesFile "abaqus.Part.PartBase.PartBase.writeIgesFile (Python method) — This method exports the geometry of the part to a named file in IGES format.")(fileName, flavor) | This method exports the geometry of the part to a named file in IGES format. |
    | [`writeStepFile`](#abaqus.Part.PartBase.PartBase.writeStepFile "abaqus.Part.PartBase.PartBase.writeStepFile (Python method) — This method exports the geometry of the part to a named file in STEP format.")(fileName) | This method exports the geometry of the part to a named file in STEP format. |
    | [`writeVdaFile`](#abaqus.Part.PartBase.PartBase.writeVdaFile "abaqus.Part.PartBase.PartBase.writeVdaFile (Python method) — This method exports the geometry of the part to a named file in VDA-FS format.")(fileName) | This method exports the geometry of the part to a named file in VDA-FS format. |
    | [`copyMeshPattern`](#abaqus.Part.PartBase.PartBase.copyMeshPattern "abaqus.Part.PartBase.PartBase.copyMeshPattern (Python method) — This method copies a mesh pattern from a source region consisting of a set of shell elements or element faces onto a target face, mapping nodes and elements in a one-one correspondence between source and target.")(elements, faces, elemFaces, ...) | This method copies a mesh pattern from a source region consisting of a set of shell elements or element faces onto a target face, mapping nodes and elements in a one-one correspondence between source and target. |
    | [`smoothNodes`](#abaqus.Part.PartBase.PartBase.smoothNodes "abaqus.Part.PartBase.PartBase.smoothNodes (Python method) — This method smooths the given nodes of a native mesh, moving them locally to a more optimal location that improves the quality of the mesh.")(nodes) | This method smooths the given nodes of a native mesh, moving them locally to a more optimal location that improves the quality of the mesh. |
    | [`Lock`](#abaqus.Part.PartBase.PartBase.Lock "abaqus.Part.PartBase.PartBase.Lock (Python method) — This method locks the part.")() | This method locks the part. |
    | [`Unlock`](#abaqus.Part.PartBase.PartBase.Unlock "abaqus.Part.PartBase.PartBase.Unlock (Python method) — This method unlocks the part.")() | This method unlocks the part. |
    | [`LockForUpgrade`](#abaqus.Part.PartBase.PartBase.LockForUpgrade "abaqus.Part.PartBase.PartBase.LockForUpgrade (Python method) — This method locks the part for upgrade.")() | This method locks the part for upgrade. |

    Inherited from [`PartFeature`](#abaqus.Part.PartFeature.PartFeature "abaqus.Part.PartFeature.PartFeature (Python class) — Bases: Feature")

    |  |  |
    | --- | --- |
    | [`AutoRepair`](#abaqus.Part.PartFeature.PartFeature.AutoRepair "abaqus.Part.PartFeature.PartFeature.AutoRepair (Python method) — This method carries out a sequence of geometry repair operations if it contains invalid entities. It is expected to improve the geometry, but it does not guarantee that the number of invalid entities will decrease. In some cases, it can also increase the number of invalid entities. Since a number of geometry repair operations and validity checks are performed, it could be a slow operation depending on the complexity of the geometry.")() | This method carries out a sequence of geometry repair operations if it contains invalid entities. |
    | [`AddCells`](#abaqus.Part.PartFeature.PartFeature.AddCells "abaqus.Part.PartFeature.PartFeature.AddCells (Python method) — This method tries to convert a shell entity to a solid entity. The conversion is not always successful.")(faceList[, flipped]) | This method tries to convert a shell entity to a solid entity. |
    | [`AnalyticRigidSurf2DPlanar`](#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurf2DPlanar "abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurf2DPlanar (Python method) — This method creates a first Feature object for an analytical rigid surface by creating a planar wire from the given ConstrainedSketch object.")(sketch) | This method creates a first Feature object for an analytical rigid surface by creating a planar wire from the given ConstrainedSketch object. |
    | [`AnalyticRigidSurfExtrude`](#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfExtrude "abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfExtrude (Python method) — This method creates a first Feature object for an analytical rigid surface by extruding the given ConstrainedSketch object by the given depth, creating a surface.")(sketch[, depth]) | This method creates a first Feature object for an analytical rigid surface by extruding the given ConstrainedSketch object by the given depth, creating a surface. |
    | [`AnalyticRigidSurfRevolve`](#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfRevolve "abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfRevolve (Python method) — This method creates a first Feature object for an analytical rigid surface by revolving the given ConstrainedSketch object by 360° about the Y axis.")(sketch) | This method creates a first Feature object for an analytical rigid surface by revolving the given ConstrainedSketch object by 360° about the **Y** axis. |
    | [`AssignMidsurfaceRegion`](#abaqus.Part.PartFeature.PartFeature.AssignMidsurfaceRegion "abaqus.Part.PartFeature.PartFeature.AssignMidsurfaceRegion (Python method) — This method assign a mid-surface property to sequence of Cell objects. If a reference representation of the part does not exist, it creates one. It also copies the cells to the reference representation and deletes the cells from the active representation of the part.")(cellList) | This method assign a mid-surface property to sequence of Cell objects. |
    | [`BaseSolidExtrude`](#abaqus.Part.PartFeature.PartFeature.BaseSolidExtrude "abaqus.Part.PartFeature.PartFeature.BaseSolidExtrude (Python method) — This method creates a first Feature object by extruding the given ConstrainedSketch object by the given depth, creating a solid. The ConstrainedSketch object must define a closed profile.")(sketch, depth[, ...]) | This method creates a first Feature object by extruding the given ConstrainedSketch object by the given depth, creating a solid. |
    | [`BaseSolidRevolve`](#abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve "abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve (Python method) — This method creates a first Feature object by revolving the given ConstrainedSketch object by the given angle, creating a solid. The ConstrainedSketch object must define a closed profile and an axis of revolution. The axis is defined by a single construction line.")(sketch, angle[, pitch, ...]) | This method creates a first Feature object by revolving the given ConstrainedSketch object by the given angle, creating a solid. |
    | [`BaseSolidSweep`](#abaqus.Part.PartFeature.PartFeature.BaseSolidSweep "abaqus.Part.PartFeature.PartFeature.BaseSolidSweep (Python method) — This method creates a first Feature object by sweeping the given profile ConstrainedSketch object along the path defined by the path ConstrainedSketch object, creating a solid. The profile ConstrainedSketch object must define a closed profile. The origin of the profile sketch is positioned at the start of the sweep path and swept perpendicular to the path. No checks are made for self- intersection.")(sketch, path) | This method creates a first Feature object by sweeping the given profile ConstrainedSketch object along the path defined by the path ConstrainedSketch object, creating a solid. |
    | [`BaseShell`](#abaqus.Part.PartFeature.PartFeature.BaseShell "abaqus.Part.PartFeature.PartFeature.BaseShell (Python method) — This method creates a first Feature object by creating a planar shell from the given ConstrainedSketch object. The ConstrainedSketch object must define a closed profile.")(sketch) | This method creates a first Feature object by creating a planar shell from the given ConstrainedSketch object. |
    | [`BaseShellExtrude`](#abaqus.Part.PartFeature.PartFeature.BaseShellExtrude "abaqus.Part.PartFeature.PartFeature.BaseShellExtrude (Python method) — This method creates a first Feature object by extruding the given ConstrainedSketch object by the given depth, creating a shell. The ConstrainedSketch object can define either an open or closed profile.")(sketch, depth[, ...]) | This method creates a first Feature object by extruding the given ConstrainedSketch object by the given depth, creating a shell. |
    | [`BaseShellRevolve`](#abaqus.Part.PartFeature.PartFeature.BaseShellRevolve "abaqus.Part.PartFeature.PartFeature.BaseShellRevolve (Python method) — This method creates a first Feature object by revolving the given ConstrainedSketch object by the given angle, creating a shell. The ConstrainedSketch object can define either an open or closed profile and an axis of revolution. The axis is defined by a single construction line.")(sketch, angle[, pitch, ...]) | This method creates a first Feature object by revolving the given ConstrainedSketch object by the given angle, creating a shell. |
    | [`BaseShellSweep`](#abaqus.Part.PartFeature.PartFeature.BaseShellSweep "abaqus.Part.PartFeature.PartFeature.BaseShellSweep (Python method) — This method creates a first Feature object by sweeping the given section ConstrainedSketch object along the path defined by the path ConstrainedSketch object, creating a shell. The ConstrainedSketch object can define either an open or closed profile. The origin of the profile sketch is positioned at the start of the sweep path and swept perpendicular to the path. No checks are made for self- intersection.")(sketch, path) | This method creates a first Feature object by sweeping the given section ConstrainedSketch object along the path defined by the path ConstrainedSketch object, creating a shell. |
    | [`BaseWire`](#abaqus.Part.PartFeature.PartFeature.BaseWire "abaqus.Part.PartFeature.PartFeature.BaseWire (Python method) — This method creates a first Feature object by creating a planar wire from the given ConstrainedSketch object.")(sketch) | This method creates a first Feature object by creating a planar wire from the given ConstrainedSketch object. |
    | [`BlendFaces`](#abaqus.Part.PartFeature.PartFeature.BlendFaces "abaqus.Part.PartFeature.PartFeature.BlendFaces (Python method) — This method creates a Feature object by creating new faces that blends two sets of faces.")(side1, side2[, method, path]) | This method creates a Feature object by creating new faces that blends two sets of faces. |
    | [`Chamfer`](#abaqus.Part.PartFeature.PartFeature.Chamfer "abaqus.Part.PartFeature.PartFeature.Chamfer (Python method) — This method creates an additional Feature object by chamfering the given list of edges with a given length.")(length, edgeList) | This method creates an additional Feature object by chamfering the given list of edges with a given length. |
    | [`Mirror`](#abaqus.Part.PartFeature.PartFeature.Mirror "abaqus.Part.PartFeature.PartFeature.Mirror (Python method) — This method mirrors existing part geometry across a plane to create new geometry.")(mirrorPlane, keepOriginal[, ...]) | This method mirrors existing part geometry across a plane to create new geometry. |
    | [`ConvertToAnalytical`](#abaqus.Part.PartFeature.PartFeature.ConvertToAnalytical "abaqus.Part.PartFeature.PartFeature.ConvertToAnalytical (Python method) — This method attempts to change entities into a simpler form that will speed up processing and make entities available during feature operations.")() | This method attempts to change entities into a simpler form that will speed up processing and make entities available during feature operations. |
    | [`ConvertToPrecise`](#abaqus.Part.PartFeature.PartFeature.ConvertToPrecise "abaqus.Part.PartFeature.PartFeature.ConvertToPrecise (Python method) — This method attempts to change imprecise entities so that the geometry becomes precise.")([method]) | This method attempts to change imprecise entities so that the geometry becomes precise. |
    | [`CoverEdges`](#abaqus.Part.PartFeature.PartFeature.CoverEdges "abaqus.Part.PartFeature.PartFeature.CoverEdges (Python method) — This method generates a face using the given edges as the face's boundaries. The CoverEdges method generates a face by creating the geometry consisting of the underlying surface, associated edges, and vertices.")(edgeList[, tryAnalytical]) | This method generates a face using the given edges as the face's boundaries. |
    | [`Cut`](#abaqus.Part.PartFeature.PartFeature.Cut "abaqus.Part.PartFeature.PartFeature.Cut (Python method) — This method creates an additional Feature object by cutting a hole using the given ConstrainedSketch object.")(sketchPlane, sketchPlaneSide, ...[, ...]) | This method creates an additional Feature object by cutting a hole using the given ConstrainedSketch object. |
    | [`CutExtrude`](#abaqus.Part.PartFeature.PartFeature.CutExtrude "abaqus.Part.PartFeature.PartFeature.CutExtrude (Python method) — This method creates an additional Feature object by extruding the given ConstrainedSketch object by the given depth and cutting away material in the solid and shell regions of the part. The ConstrainedSketch object must define a closed profile. The CutExtrude method creates a blind cut (using depth), an up-to-face cut (using upToFace), or a through-all cut (if depth and upToFace are not specified).")(sketchPlane, sketchPlaneSide, ...) | This method creates an additional Feature object by extruding the given ConstrainedSketch object by the given depth and cutting away material in the solid and shell regions of the part. |
    | [`CutLoft`](#abaqus.Part.PartFeature.PartFeature.CutLoft "abaqus.Part.PartFeature.PartFeature.CutLoft (Python method) — This method creates an additional Feature object by lofting between the given sections and cutting away material from the part. You define the sections using a sequence of edges from the part or an EdgeArray.")(loftsections[, startCondition, ...]) | This method creates an additional Feature object by lofting between the given sections and cutting away material from the part. |
    | [`CutRevolve`](#abaqus.Part.PartFeature.PartFeature.CutRevolve "abaqus.Part.PartFeature.PartFeature.CutRevolve (Python method) — This method creates an additional Feature object by revolving the given ConstrainedSketch object by the given angle and cutting away material from the part. The ConstrainedSketch object must define a closed profile and an axis of revolution.")(sketchPlane, sketchPlaneSide, ...) | This method creates an additional Feature object by revolving the given ConstrainedSketch object by the given angle and cutting away material from the part. |
    | [`CutSweep`](#abaqus.Part.PartFeature.PartFeature.CutSweep "abaqus.Part.PartFeature.PartFeature.CutSweep (Python method) — This method creates an additional Feature object by sweeping the given ConstrainedSketch object along a path which may be a ConstrainedSketch or a sequence of Edge objects and cutting away material from the part. If the profile section is a ConstrainedSketch object, it must define a closed profile. The section sketch can be created at the normal plane at the start of the sweep path or it may be created on a Datum plane or a planar Face. No checks are made for self-intersection.")(path, profile[, pathPlane, ...]) | This method creates an additional Feature object by sweeping the given ConstrainedSketch object along a path which may be a ConstrainedSketch or a sequence of Edge objects and cutting away material from the part. |
    | [`ExtendFaces`](#abaqus.Part.PartFeature.PartFeature.ExtendFaces "abaqus.Part.PartFeature.PartFeature.ExtendFaces (Python method) — This method extends faces along its free edges by offsetting the external edges along the surfaces. One of distance, upToReferenceRep, or upToFaces must be used to specify how far the faces need to be extended.")([faces, extendAlong, distance, ...]) | This method extends faces along its free edges by offsetting the external edges along the surfaces. |
    | [`FaceFromElementFaces`](#abaqus.Part.PartFeature.PartFeature.FaceFromElementFaces "abaqus.Part.PartFeature.PartFeature.FaceFromElementFaces (Python method) — This method creates a geometry face from a collection of orphan element faces.")(elementFaces[, stitch, ...]) | This method creates a geometry face from a collection of orphan element faces. |
    | [`HoleBlindFromEdges`](#abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges "abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges (Python method) — This method creates an additional Feature object by creating a circular blind hole of the given diameter and depth and cutting away material in the solid and shell regions of the part. The center of the hole is offset from two non-parallel straight edges by the given distances.")(plane, planeSide, ...) | This method creates an additional Feature object by creating a circular blind hole of the given diameter and depth and cutting away material in the solid and shell regions of the part. |
    | [`HoleFromEdges`](#abaqus.Part.PartFeature.PartFeature.HoleFromEdges "abaqus.Part.PartFeature.PartFeature.HoleFromEdges (Python method) — This method creates an additional Feature object by creating a circular hole of the given diameter in a 2D planar part and cutting away material in the shell and wire regions of the part. The center of the hole is offset from two non-parallel straight edges by the given distances.")(diameter, edge1, distance1, ...) | This method creates an additional Feature object by creating a circular hole of the given diameter in a 2D planar part and cutting away material in the shell and wire regions of the part. |
    | [`HoleThruAllFromEdges`](#abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges "abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges (Python method) — This method creates an additional Feature object by creating a circular through hole of the given diameter and cutting away material in the solid and shell regions of the part. The center of the hole is offset from two non-parallel straight edges by the given distances.")(plane, planeSide, ...) | This method creates an additional Feature object by creating a circular through hole of the given diameter and cutting away material in the solid and shell regions of the part. |
    | [`MergeEdges`](#abaqus.Part.PartFeature.PartFeature.MergeEdges "abaqus.Part.PartFeature.PartFeature.MergeEdges (Python method) — This method merges edges either by extending the user selection or using only the selected edges.")([edgeList, extendSelection]) | This method merges edges either by extending the user selection or using only the selected edges. |
    | [`OffsetFaces`](#abaqus.Part.PartFeature.PartFeature.OffsetFaces "abaqus.Part.PartFeature.PartFeature.OffsetFaces (Python method) — This method creates new faces by offsetting existing faces.")(faceList[, distance, ...]) | This method creates new faces by offsetting existing faces. |
    | [`RemoveCells`](#abaqus.Part.PartFeature.PartFeature.RemoveCells "abaqus.Part.PartFeature.PartFeature.RemoveCells (Python method) — This method converts a solid entity to a shell entity.")(cellList) | This method converts a solid entity to a shell entity. |
    | [`RemoveFaces`](#abaqus.Part.PartFeature.PartFeature.RemoveFaces "abaqus.Part.PartFeature.PartFeature.RemoveFaces (Python method) — This method removes faces from a solid entity or from a shell entity.")(faceList[, deleteCells]) | This method removes faces from a solid entity or from a shell entity. |
    | [`RemoveFacesAndStitch`](#abaqus.Part.PartFeature.PartFeature.RemoveFacesAndStitch "abaqus.Part.PartFeature.PartFeature.RemoveFacesAndStitch (Python method) — This method removes faces from a solid entity and attempts to close the resulting gap by extending the neighboring faces of the solid.")(faceList) | This method removes faces from a solid entity and attempts to close the resulting gap by extending the neighboring faces of the solid. |
    | [`RemoveRedundantEntities`](#abaqus.Part.PartFeature.PartFeature.RemoveRedundantEntities "abaqus.Part.PartFeature.PartFeature.RemoveRedundantEntities (Python method) — This method removes redundant edges and vertices from a solid or a shell entity. One of the two arguments is required.")([vertexList, ...]) | This method removes redundant edges and vertices from a solid or a shell entity. |
    | [`RepairFaceNormals`](#abaqus.Part.PartFeature.PartFeature.RepairFaceNormals "abaqus.Part.PartFeature.PartFeature.RepairFaceNormals (Python method) — This method works on the entire part or a sequence of shell faces. When the entire part is selected, it aligns all the shell face normals, and inverts all of the solid faces' normals if the solid was originally inside out. When a few shell faces are selected, it inverts the normals of the selected faces.")([faceList]) | This method works on the entire part or a sequence of shell faces. |
    | [`RepairInvalidEdges`](#abaqus.Part.PartFeature.PartFeature.RepairInvalidEdges "abaqus.Part.PartFeature.PartFeature.RepairInvalidEdges (Python method) — This method repairs invalid edges. It will always attempt to improve edges even if none of selected edges are initially invalid and may leave behind invalid edges that could not be repaired.")(edgeList) | This method repairs invalid edges. |
    | [`RepairSliver`](#abaqus.Part.PartFeature.PartFeature.RepairSliver "abaqus.Part.PartFeature.PartFeature.RepairSliver (Python method) — This method repairs the selected sliver from the selected face. The sliver area is specified using two points. A face partition is carried out at the specified points and the smaller of the two faces is removed.")(face, point1, point2[, ...]) | This method repairs the selected sliver from the selected face. |
    | [`RepairSmallEdges`](#abaqus.Part.PartFeature.PartFeature.RepairSmallEdges "abaqus.Part.PartFeature.PartFeature.RepairSmallEdges (Python method) — This method repairs small edges. This method will attempt to replace selected small edges with vertices and extend the adjacent faces and edges. This method might leave behind some small edges that cannot be removed.")(edgeList[, toleranceChecks]) | This method repairs small edges. |
    | [`RepairSmallFaces`](#abaqus.Part.PartFeature.PartFeature.RepairSmallFaces "abaqus.Part.PartFeature.PartFeature.RepairSmallFaces (Python method) — This method repairs small faces. It will attempt to replace the selected small faces with edges or vertices and extend the adjacent faces. This method might leave behind some small faces that cannot be removed.")(faceList[, toleranceChecks]) | This method repairs small faces. |
    | [`ReplaceFaces`](#abaqus.Part.PartFeature.PartFeature.ReplaceFaces "abaqus.Part.PartFeature.PartFeature.ReplaceFaces (Python method) — This method replaces the selected faces with a single face. If one single face is selected, that alone is replaced with a new face.")(faceList[, stitch]) | This method replaces the selected faces with a single face. |
    | [`Round`](#abaqus.Part.PartFeature.PartFeature.Round "abaqus.Part.PartFeature.PartFeature.Round (Python method) — This method creates an additional Feature object by rounding (filleting) the given list of entities with the given radius.")(radius[, edgeList, vertexList]) | This method creates an additional Feature object by rounding (filleting) the given list of entities with the given radius. |
    | [`Shell`](#abaqus.Part.PartFeature.PartFeature.Shell "abaqus.Part.PartFeature.PartFeature.Shell (Python method) — This method creates an additional Feature object by creating a planar shell from the given ConstrainedSketch object. The ConstrainedSketch object must define a closed profile.")(sketchPlane, sketchPlaneSide, ...[, ...]) | This method creates an additional Feature object by creating a planar shell from the given ConstrainedSketch object. |
    | [`ShellExtrude`](#abaqus.Part.PartFeature.PartFeature.ShellExtrude "abaqus.Part.PartFeature.PartFeature.ShellExtrude (Python method) — This method creates an additional Feature object by extruding the given ConstrainedSketch object by the given depth, creating a shell protrusion. The ConstrainedSketch object can define either an open or closed profile.")(sketchPlane, sketchPlaneSide, ...) | This method creates an additional Feature object by extruding the given ConstrainedSketch object by the given depth, creating a shell protrusion. |
    | [`ShellLoft`](#abaqus.Part.PartFeature.PartFeature.ShellLoft "abaqus.Part.PartFeature.PartFeature.ShellLoft (Python method) — This method creates an additional Feature object by lofting between the given sections and adding shell faces to the part. You define the sections using a sequence of edges from the part or an EdgeArray.")(loftsections[, startCondition, ...]) | This method creates an additional Feature object by lofting between the given sections and adding shell faces to the part. |
    | [`ShellRevolve`](#abaqus.Part.PartFeature.PartFeature.ShellRevolve "abaqus.Part.PartFeature.PartFeature.ShellRevolve (Python method) — This method creates an additional Feature object by revolving the given ConstrainedSketch object by the given angle, creating a shell protrusion. The ConstrainedSketch object can define either an open or closed profile and an axis of revolution. The axis is defined by a single construction line. For a description of the plane positioning arguments, see SolidExtrude.")(sketchPlane, sketchPlaneSide, ...) | This method creates an additional Feature object by revolving the given ConstrainedSketch object by the given angle, creating a shell protrusion. |
    | [`ShellSweep`](#abaqus.Part.PartFeature.PartFeature.ShellSweep "abaqus.Part.PartFeature.PartFeature.ShellSweep (Python method) — This method creates an additional Feature object by sweeping the given ConstrainedSketch object or a sequence of Edge objects along a path which may be a ConstrainedSketch or a sequence of Edge objects, creating a shell swept protrusion. The section can be an open or a closed profile. The section sketch can be created at the normal plane at the start of the sweep path or it may be created on a Datum plane or a planar Face. No checks are made for self-intersection.")(path, profile[, pathPlane, ...]) | This method creates an additional Feature object by sweeping the given ConstrainedSketch object or a sequence of Edge objects along a path which may be a ConstrainedSketch or a sequence of Edge objects, creating a shell swept protrusion. |
    | [`SolidExtrude`](#abaqus.Part.PartFeature.PartFeature.SolidExtrude "abaqus.Part.PartFeature.PartFeature.SolidExtrude (Python method) — This method creates an additional Feature object by extruding the given ConstrainedSketch object by the given depth, creating a solid protrusion. The ConstrainedSketch object must define a closed profile.")(sketchPlane, sketchPlaneSide, ...) | This method creates an additional Feature object by extruding the given ConstrainedSketch object by the given depth, creating a solid protrusion. |
    | [`SolidLoft`](#abaqus.Part.PartFeature.PartFeature.SolidLoft "abaqus.Part.PartFeature.PartFeature.SolidLoft (Python method) — This method creates an additional Feature object by lofting between the given sections and adding material to the part. You define the sections using a sequence of edges from the part or an EdgeArray.")(loftsections[, startCondition, ...]) | This method creates an additional Feature object by lofting between the given sections and adding material to the part. |
    | [`SolidRevolve`](#abaqus.Part.PartFeature.PartFeature.SolidRevolve "abaqus.Part.PartFeature.PartFeature.SolidRevolve (Python method) — This method creates an additional Feature object by revolving the given ConstrainedSketch object by the given angle, creating a solid protrusion. The ConstrainedSketch object must define a closed profile and an axis of revolution. The axis is defined by a single construction line.")(sketchPlane, sketchPlaneSide, ...) | This method creates an additional Feature object by revolving the given ConstrainedSketch object by the given angle, creating a solid protrusion. |
    | [`SolidSweep`](#abaqus.Part.PartFeature.PartFeature.SolidSweep "abaqus.Part.PartFeature.PartFeature.SolidSweep (Python method) — This method creates an additional Feature object by sweeping the given ConstrainedSketch object or a Face object along a path which may be a ConstrainedSketch or a sequence of Edge objects, creating a solid swept protrusion. If the profile section is a ConstrainedSketch object, it must define a closed profile. The section sketch can be created at the normal plane at the start of the sweep path or it may be created on a Datum plane or a planar Face. No checks are made for self-intersection.")(path, profile[, pathPlane, ...]) | This method creates an additional Feature object by sweeping the given ConstrainedSketch object or a Face object along a path which may be a ConstrainedSketch or a sequence of Edge objects, creating a solid swept protrusion. |
    | [`Stitch`](#abaqus.Part.PartFeature.PartFeature.Stitch "abaqus.Part.PartFeature.PartFeature.Stitch (Python method) — This method attempts to create a valid part by binding together free and imprecise edges of all the faces of a part. If edgeList is not given, a global stitch will be performed. If stitchTolerance is not specified, a value of 1.0 will be used.")([edgeList, stitchTolerance]) | This method attempts to create a valid part by binding together free and imprecise edges of all the faces of a part. |
    | [`Wire`](#abaqus.Part.PartFeature.PartFeature.Wire "abaqus.Part.PartFeature.PartFeature.Wire (Python method) — This method creates an additional Feature object by creating a planar wire from the given ConstrainedSketch object. The ConstrainedSketch object must define a closed profile.")(sketchPlane, sketchPlaneSide, ...[, ...]) | This method creates an additional Feature object by creating a planar wire from the given ConstrainedSketch object. |
    | [`WireSpline`](#abaqus.Part.PartFeature.PartFeature.WireSpline "abaqus.Part.PartFeature.PartFeature.WireSpline (Python method) — This method creates an additional Feature object by creating a spline wire that passes through a sequence of given points. Each point can be a datum point, a vertex, an interesting point, or a tuple.")(points[, mergeType, ...]) | This method creates an additional Feature object by creating a spline wire that passes through a sequence of given points. |
    | [`WirePolyLine`](#abaqus.Part.PartFeature.PartFeature.WirePolyLine "abaqus.Part.PartFeature.PartFeature.WirePolyLine (Python method) — This method creates an additional Feature object by creating a polyline wire that passes through a sequence of given points. Each point can be a datum point, a vertex, an interesting point, or a tuple.")(points[, mergeType, meshable]) | This method creates an additional Feature object by creating a polyline wire that passes through a sequence of given points. |
    | [`WireFromEdge`](#abaqus.Part.PartFeature.PartFeature.WireFromEdge "abaqus.Part.PartFeature.PartFeature.WireFromEdge (Python method) — This method creates an additional Feature object by creating a Wire by selecting one or more Edge objects of a Solid or Shell part.")(edgeList) | This method creates an additional Feature object by creating a Wire by selecting one or more Edge objects of a Solid or Shell part. |

    Inherited from [`Feature`](feature.html#abaqus.Feature.Feature.Feature "abaqus.Feature.Feature.Feature (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | [`AttachmentPoints`](feature.html#abaqus.Feature.Feature.Feature.AttachmentPoints "abaqus.Feature.Feature.Feature.AttachmentPoints (Python method) — This method creates an attachment points Feature. Attachment points may be created using datum points, vertices, reference points, attachment points, interesting points, orphan mesh nodes or coordinates. Optionally, the attachment points can be projected on geometric faces or element faces.")(name, points[, ...]) | This method creates an attachment points Feature. |
    | [`AttachmentPointsAlongDirection`](feature.html#abaqus.Feature.Feature.Feature.AttachmentPointsAlongDirection "abaqus.Feature.Feature.Feature.AttachmentPointsAlongDirection (Python method) — This method creates a Feature object by creating attachment points along a direction or between two points. A Datum point, a ConstrainedSketchVertex, a Reference point, an Attachment point, an Interesting point, or an orphan mesh Node can be specified as the start or end point. The direction can be specified using a straight edge or a datum axis.")(name, ...[, ...]) | This method creates a Feature object by creating attachment points along a direction or between two points. |
    | [`AttachmentPointsOffsetFromEdges`](feature.html#abaqus.Feature.Feature.Feature.AttachmentPointsOffsetFromEdges "abaqus.Feature.Feature.Feature.AttachmentPointsOffsetFromEdges (Python method) — This method creates a Feature object by creating attachment points along or offset from one or more connected edges.")(name, edges) | This method creates a Feature object by creating attachment points along or offset from one or more connected edges. |
    | [`DatumAxisByCylFace`](feature.html#abaqus.Feature.Feature.Feature.DatumAxisByCylFace "abaqus.Feature.Feature.Feature.DatumAxisByCylFace (Python method) — This method creates a Feature object and a DatumAxis object along the axis of a cylinder or cone.")(face) | This method creates a Feature object and a DatumAxis object along the axis of a cylinder or cone. |
    | [`DatumAxisByNormalToPlane`](feature.html#abaqus.Feature.Feature.Feature.DatumAxisByNormalToPlane "abaqus.Feature.Feature.Feature.DatumAxisByNormalToPlane (Python method) — This method creates a Feature object and a DatumAxis object normal to the specified plane and passing through the specified point.")(plane, point) | This method creates a Feature object and a DatumAxis object normal to the specified plane and passing through the specified point. |
    | [`DatumAxisByParToEdge`](feature.html#abaqus.Feature.Feature.Feature.DatumAxisByParToEdge "abaqus.Feature.Feature.Feature.DatumAxisByParToEdge (Python method) — This method creates a Feature object and a DatumAxis object parallel to the specified edge and passing through the specified point.")(edge, point) | This method creates a Feature object and a DatumAxis object parallel to the specified edge and passing through the specified point. |
    | [`DatumAxisByPrincipalAxis`](feature.html#abaqus.Feature.Feature.Feature.DatumAxisByPrincipalAxis "abaqus.Feature.Feature.Feature.DatumAxisByPrincipalAxis (Python method) — This method creates a Feature object and a DatumAxis object along one of the three principal axes.")(principalAxis) | This method creates a Feature object and a DatumAxis object along one of the three principal axes. |
    | [`DatumAxisByRotation`](feature.html#abaqus.Feature.Feature.Feature.DatumAxisByRotation "abaqus.Feature.Feature.Feature.DatumAxisByRotation (Python method)")() |  |
    | [`DatumAxisByThreePoint`](feature.html#abaqus.Feature.Feature.Feature.DatumAxisByThreePoint "abaqus.Feature.Feature.Feature.DatumAxisByThreePoint (Python method) — This method creates a Feature object and a DatumAxis object normal to the circle described by three points and through its center.")(point1, point2, point3) | This method creates a Feature object and a DatumAxis object normal to the circle described by three points and through its center. |
    | [`DatumAxisByThruEdge`](feature.html#abaqus.Feature.Feature.Feature.DatumAxisByThruEdge "abaqus.Feature.Feature.Feature.DatumAxisByThruEdge (Python method) — This method creates a Feature object and a DatumAxis object along the specified edge.")(edge) | This method creates a Feature object and a DatumAxis object along the specified edge. |
    | [`DatumAxisByTwoPlane`](feature.html#abaqus.Feature.Feature.Feature.DatumAxisByTwoPlane "abaqus.Feature.Feature.Feature.DatumAxisByTwoPlane (Python method) — This method creates a Feature object and a DatumAxis object at the intersection of two planes.")(plane1, plane2) | This method creates a Feature object and a DatumAxis object at the intersection of two planes. |
    | [`DatumAxisByTwoPoint`](feature.html#abaqus.Feature.Feature.Feature.DatumAxisByTwoPoint "abaqus.Feature.Feature.Feature.DatumAxisByTwoPoint (Python method) — This method creates a Feature object and a DatumAxis object along the line joining two points.")(point1, point2) | This method creates a Feature object and a DatumAxis object along the line joining two points. |
    | [`DatumCsysByDefault`](feature.html#abaqus.Feature.Feature.Feature.DatumCsysByDefault "abaqus.Feature.Feature.Feature.DatumCsysByDefault (Python method) — This method creates a Feature object and a DatumCsys object from the specified default coordinate system at the origin.")(coordSysType[, name]) | This method creates a Feature object and a DatumCsys object from the specified default coordinate system at the origin. |
    | [`DatumCsysByOffset`](feature.html#abaqus.Feature.Feature.Feature.DatumCsysByOffset "abaqus.Feature.Feature.Feature.DatumCsysByOffset (Python method) — This method creates a Feature object and a DatumCsys object by offsetting the origin of an existing datum coordinate system to a specified point.")(coordSysType, ...[, name]) | This method creates a Feature object and a DatumCsys object by offsetting the origin of an existing datum coordinate system to a specified point. |
    | [`DatumCsysByThreePoints`](feature.html#abaqus.Feature.Feature.Feature.DatumCsysByThreePoints "abaqus.Feature.Feature.Feature.DatumCsysByThreePoints (Python method) — This method creates a Feature object and a DatumCsys object from three points.")(coordSysType, origin, ...) | This method creates a Feature object and a DatumCsys object from three points. |
    | [`DatumCsysByTwoLines`](feature.html#abaqus.Feature.Feature.Feature.DatumCsysByTwoLines "abaqus.Feature.Feature.Feature.DatumCsysByTwoLines (Python method) — This method creates a Feature object and a DatumCsys object from two orthogonal lines. The origin of the new datum coordinate system is placed at the intersection of the two lines.")(coordSysType, line1, line2) | This method creates a Feature object and a DatumCsys object from two orthogonal lines. |
    | [`DatumPlaneByPrincipalPlane`](feature.html#abaqus.Feature.Feature.Feature.DatumPlaneByPrincipalPlane "abaqus.Feature.Feature.Feature.DatumPlaneByPrincipalPlane (Python method) — This method creates a Feature object and a DatumPlane object through the origin along one of the three principal planes.")(principalPlane, ...) | This method creates a Feature object and a DatumPlane object through the origin along one of the three principal planes. |
    | [`DatumPlaneByOffset`](feature.html#abaqus.Feature.Feature.Feature.DatumPlaneByOffset "abaqus.Feature.Feature.Feature.DatumPlaneByOffset (Python method)")() |  |
    | [`DatumPlaneByRotation`](feature.html#abaqus.Feature.Feature.Feature.DatumPlaneByRotation "abaqus.Feature.Feature.Feature.DatumPlaneByRotation (Python method) — This method creates a Feature object and a DatumPlane object by rotating a plane about the specified axis through the specified angle.")(plane, axis, angle) | This method creates a Feature object and a DatumPlane object by rotating a plane about the specified axis through the specified angle. |
    | [`DatumPlaneByThreePoints`](feature.html#abaqus.Feature.Feature.Feature.DatumPlaneByThreePoints "abaqus.Feature.Feature.Feature.DatumPlaneByThreePoints (Python method) — This method creates a Feature object and a DatumPlane object defined by passing through three points.")(point1, point2, point3) | This method creates a Feature object and a DatumPlane object defined by passing through three points. |
    | [`DatumPlaneByLinePoint`](feature.html#abaqus.Feature.Feature.Feature.DatumPlaneByLinePoint "abaqus.Feature.Feature.Feature.DatumPlaneByLinePoint (Python method) — This method creates a Feature object and a DatumPlane object that pass through the specified line and through the specified point that does not lie on the line.")(line, point) | This method creates a Feature object and a DatumPlane object that pass through the specified line and through the specified point that does not lie on the line. |
    | [`DatumPlaneByPointNormal`](feature.html#abaqus.Feature.Feature.Feature.DatumPlaneByPointNormal "abaqus.Feature.Feature.Feature.DatumPlaneByPointNormal (Python method) — This method creates a Feature object and a DatumPlane object normal to the specified line and running through the specified point.")(point, normal) | This method creates a Feature object and a DatumPlane object normal to the specified line and running through the specified point. |
    | [`DatumPlaneByTwoPoint`](feature.html#abaqus.Feature.Feature.Feature.DatumPlaneByTwoPoint "abaqus.Feature.Feature.Feature.DatumPlaneByTwoPoint (Python method) — This method creates a Feature object and a DatumPlane object midway between two points and normal to the line connecting the points.")(point1, point2) | This method creates a Feature object and a DatumPlane object midway between two points and normal to the line connecting the points. |
    | [`DatumPointByCoordinate`](feature.html#abaqus.Feature.Feature.Feature.DatumPointByCoordinate "abaqus.Feature.Feature.Feature.DatumPointByCoordinate (Python method) — This method creates a Feature object and a DatumPoint object at the point defined by the specified coordinates.")(coords) | This method creates a Feature object and a DatumPoint object at the point defined by the specified coordinates. |
    | [`DatumPointByOffset`](feature.html#abaqus.Feature.Feature.Feature.DatumPointByOffset "abaqus.Feature.Feature.Feature.DatumPointByOffset (Python method) — This method creates a Feature object and a DatumPoint object offset from an existing point by a vector.")(point, vector) | This method creates a Feature object and a DatumPoint object offset from an existing point by a vector. |
    | [`DatumPointByMidPoint`](feature.html#abaqus.Feature.Feature.Feature.DatumPointByMidPoint "abaqus.Feature.Feature.Feature.DatumPointByMidPoint (Python method) — This method creates a Feature object and a DatumPoint object midway between two points.")(point1, point2) | This method creates a Feature object and a DatumPoint object midway between two points. |
    | [`DatumPointByOnFace`](feature.html#abaqus.Feature.Feature.Feature.DatumPointByOnFace "abaqus.Feature.Feature.Feature.DatumPointByOnFace (Python method) — This method creates a Feature object and a DatumPoint object on the specified face, offset from two edges.")(face, edge1, offset1, ...) | This method creates a Feature object and a DatumPoint object on the specified face, offset from two edges. |
    | [`DatumPointByEdgeParam`](feature.html#abaqus.Feature.Feature.Feature.DatumPointByEdgeParam "abaqus.Feature.Feature.Feature.DatumPointByEdgeParam (Python method) — This method creates a Feature object and a DatumPoint object along an edge at a selected distance from one end of the edge.")(edge, parameter) | This method creates a Feature object and a DatumPoint object along an edge at a selected distance from one end of the edge. |
    | [`DatumPointByProjOnEdge`](feature.html#abaqus.Feature.Feature.Feature.DatumPointByProjOnEdge "abaqus.Feature.Feature.Feature.DatumPointByProjOnEdge (Python method) — This method creates a Feature object and a DatumPoint object along an edge by projecting an existing point along the normal to the edge.")(point, edge) | This method creates a Feature object and a DatumPoint object along an edge by projecting an existing point along the normal to the edge. |
    | [`DatumPointByProjOnFace`](feature.html#abaqus.Feature.Feature.Feature.DatumPointByProjOnFace "abaqus.Feature.Feature.Feature.DatumPointByProjOnFace (Python method) — This method creates a Feature object and a DatumPoint object on a specified face by projecting an existing point onto the face.")(point, face) | This method creates a Feature object and a DatumPoint object on a specified face by projecting an existing point onto the face. |
    | [`MakeSketchTransform`](feature.html#abaqus.Feature.Feature.Feature.MakeSketchTransform "abaqus.Feature.Feature.Feature.MakeSketchTransform (Python method) — This method creates a Transform object. A Transform object is a 4x3 matrix of Floats that represents the transformation from sketch coordinates to part coordinates.")(sketchPlane[, origin, ...]) | This method creates a Transform object. |
    | [`PartitionCellByDatumPlane`](feature.html#abaqus.Feature.Feature.Feature.PartitionCellByDatumPlane "abaqus.Feature.Feature.Feature.PartitionCellByDatumPlane (Python method) — This method partitions one or more cells using the given datum plane.")(cells, datumPlane) | This method partitions one or more cells using the given datum plane. |
    | [`PartitionCellByExtendFace`](feature.html#abaqus.Feature.Feature.Feature.PartitionCellByExtendFace "abaqus.Feature.Feature.Feature.PartitionCellByExtendFace (Python method) — This method partitions one or more cells by extending the underlying geometry of a given face to partition the target cells.")(cells, extendFace) | This method partitions one or more cells by extending the underlying geometry of a given face to partition the target cells. |
    | [`PartitionCellByExtrudeEdge`](feature.html#abaqus.Feature.Feature.Feature.PartitionCellByExtrudeEdge "abaqus.Feature.Feature.Feature.PartitionCellByExtrudeEdge (Python method) — This method partitions one or more cells by extruding selected edges in the given direction.")(cells, edges, ...) | This method partitions one or more cells by extruding selected edges in the given direction. |
    | [`PartitionCellByPatchNCorners`](feature.html#abaqus.Feature.Feature.Feature.PartitionCellByPatchNCorners "abaqus.Feature.Feature.Feature.PartitionCellByPatchNCorners (Python method) — This method partitions a cell using an N-sided cutting patch defined by the given corner points.")(cell, cornerPoints) | This method partitions a cell using an N-sided cutting patch defined by the given corner points. |
    | [`PartitionCellByPatchNEdges`](feature.html#abaqus.Feature.Feature.Feature.PartitionCellByPatchNEdges "abaqus.Feature.Feature.Feature.PartitionCellByPatchNEdges (Python method) — This method partitions a cell using an N-sided cutting patch defined by the given edges.")(cell, edges) | This method partitions a cell using an N-sided cutting patch defined by the given edges. |
    | [`PartitionCellByPlaneNormalToEdge`](feature.html#abaqus.Feature.Feature.Feature.PartitionCellByPlaneNormalToEdge "abaqus.Feature.Feature.Feature.PartitionCellByPlaneNormalToEdge (Python method) — This method partitions one or more cells using a plane normal to an edge at the given edge point.")(cells, ...) | This method partitions one or more cells using a plane normal to an edge at the given edge point. |
    | [`PartitionCellByPlanePointNormal`](feature.html#abaqus.Feature.Feature.Feature.PartitionCellByPlanePointNormal "abaqus.Feature.Feature.Feature.PartitionCellByPlanePointNormal (Python method) — This method partitions one or more cells using a plane defined by a point and a normal direction.")(cells, ...) | This method partitions one or more cells using a plane defined by a point and a normal direction. |
    | [`PartitionCellByPlaneThreePoints`](feature.html#abaqus.Feature.Feature.Feature.PartitionCellByPlaneThreePoints "abaqus.Feature.Feature.Feature.PartitionCellByPlaneThreePoints (Python method) — This method partitions one or more cells using a plane defined by three points.")(cells, ...) | This method partitions one or more cells using a plane defined by three points. |
    | [`PartitionCellBySweepEdge`](feature.html#abaqus.Feature.Feature.Feature.PartitionCellBySweepEdge "abaqus.Feature.Feature.Feature.PartitionCellBySweepEdge (Python method) — This method partitions one or more cells by sweeping selected edges along the given sweep path.")(cells, edges, sweepPath) | This method partitions one or more cells by sweeping selected edges along the given sweep path. |
    | [`PartitionEdgeByDatumPlane`](feature.html#abaqus.Feature.Feature.Feature.PartitionEdgeByDatumPlane "abaqus.Feature.Feature.Feature.PartitionEdgeByDatumPlane (Python method) — This method partitions an edge where it intersects with a datum plane.")(edges, datumPlane) | This method partitions an edge where it intersects with a datum plane. |
    | [`PartitionEdgeByParam`](feature.html#abaqus.Feature.Feature.Feature.PartitionEdgeByParam "abaqus.Feature.Feature.Feature.PartitionEdgeByParam (Python method) — This method partitions one or more edges at the given normalized edge parameter.")(edges, parameter) | This method partitions one or more edges at the given normalized edge parameter. |
    | [`PartitionEdgeByPoint`](feature.html#abaqus.Feature.Feature.Feature.PartitionEdgeByPoint "abaqus.Feature.Feature.Feature.PartitionEdgeByPoint (Python method) — This method partitions an edge at the given point.")(edge, point) | This method partitions an edge at the given point. |
    | [`PartitionFaceByAuto`](feature.html#abaqus.Feature.Feature.Feature.PartitionFaceByAuto "abaqus.Feature.Feature.Feature.PartitionFaceByAuto (Python method) — This method automatically partitions a target face into simple regions that can be meshed using a structured meshing technique.")(face) | This method automatically partitions a target face into simple regions that can be meshed using a structured meshing technique. |
    | [`PartitionFaceByCurvedPathEdgeParams`](feature.html#abaqus.Feature.Feature.Feature.PartitionFaceByCurvedPathEdgeParams "abaqus.Feature.Feature.Feature.PartitionFaceByCurvedPathEdgeParams (Python method) — This method partitions a face normal to two edges, using a curved path between the two given edge points defined by the normalized edge parameters.")(face, ...) | This method partitions a face normal to two edges, using a curved path between the two given edge points defined by the normalized edge parameters. |
    | [`PartitionFaceByCurvedPathEdgePoints`](feature.html#abaqus.Feature.Feature.Feature.PartitionFaceByCurvedPathEdgePoints "abaqus.Feature.Feature.Feature.PartitionFaceByCurvedPathEdgePoints (Python method) — This method partitions a face normal to two edges, using a curved path between the two given edge points.")(face, ...) | This method partitions a face normal to two edges, using a curved path between the two given edge points. |
    | [`PartitionFaceByDatumPlane`](feature.html#abaqus.Feature.Feature.Feature.PartitionFaceByDatumPlane "abaqus.Feature.Feature.Feature.PartitionFaceByDatumPlane (Python method) — This method partitions one or more faces using the given datum plane.")(faces, datumPlane) | This method partitions one or more faces using the given datum plane. |
    | [`PartitionFaceByExtendFace`](feature.html#abaqus.Feature.Feature.Feature.PartitionFaceByExtendFace "abaqus.Feature.Feature.Feature.PartitionFaceByExtendFace (Python method) — This method partitions one or more faces by extending the underlying geometry of another given face to partition the target faces.")(faces, extendFace) | This method partitions one or more faces by extending the underlying geometry of another given face to partition the target faces. |
    | [`PartitionFaceByIntersectFace`](feature.html#abaqus.Feature.Feature.Feature.PartitionFaceByIntersectFace "abaqus.Feature.Feature.Feature.PartitionFaceByIntersectFace (Python method) — This method partitions one or more faces using the given cutting faces to partition the target faces.")(faces, cuttingFaces) | This method partitions one or more faces using the given cutting faces to partition the target faces. |
    | [`PartitionFaceByProjectingEdges`](feature.html#abaqus.Feature.Feature.Feature.PartitionFaceByProjectingEdges "abaqus.Feature.Feature.Feature.PartitionFaceByProjectingEdges (Python method) — This method partitions one or more faces by projecting the given edges on the target faces.")(faces, edges) | This method partitions one or more faces by projecting the given edges on the target faces. |
    | [`PartitionFaceByShortestPath`](feature.html#abaqus.Feature.Feature.Feature.PartitionFaceByShortestPath "abaqus.Feature.Feature.Feature.PartitionFaceByShortestPath (Python method) — This method partitions one or more faces using a minimum distance path between the two given points.")(faces, point1, ...) | This method partitions one or more faces using a minimum distance path between the two given points. |
    | [`PartitionFaceBySketch`](feature.html#abaqus.Feature.Feature.Feature.PartitionFaceBySketch "abaqus.Feature.Feature.Feature.PartitionFaceBySketch (Python method) — This method partitions one or more planar faces by sketching on them.")(faces, sketch[, ...]) | This method partitions one or more planar faces by sketching on them. |
    | [`PartitionFaceBySketchDistance`](feature.html#abaqus.Feature.Feature.Feature.PartitionFaceBySketchDistance "abaqus.Feature.Feature.Feature.PartitionFaceBySketchDistance (Python method) — This method partitions one or more faces by sketching on a sketch plane and then projecting the sketch toward the target faces through the given distance.")(faces, ...[, ...]) | This method partitions one or more faces by sketching on a sketch plane and then projecting the sketch toward the target faces through the given distance. |
    | [`PartitionFaceBySketchRefPoint`](feature.html#abaqus.Feature.Feature.Feature.PartitionFaceBySketchRefPoint "abaqus.Feature.Feature.Feature.PartitionFaceBySketchRefPoint (Python method) — This method partitions one or more faces by sketching on a sketch plane and then projecting the sketch toward the target faces through a distance governed by the reference point.")(faces, ...[, ...]) | This method partitions one or more faces by sketching on a sketch plane and then projecting the sketch toward the target faces through a distance governed by the reference point. |
    | [`PartitionFaceBySketchThruAll`](feature.html#abaqus.Feature.Feature.Feature.PartitionFaceBySketchThruAll "abaqus.Feature.Feature.Feature.PartitionFaceBySketchThruAll (Python method) — This method partitions one or more faces by sketching on a sketch plane and then projecting toward the target faces through an infinite distance.")(faces, ...[, ...]) | This method partitions one or more faces by sketching on a sketch plane and then projecting toward the target faces through an infinite distance. |
    | [`ReferencePoint`](feature.html#abaqus.Feature.Feature.Feature.ReferencePoint "abaqus.Feature.Feature.Feature.ReferencePoint (Python method) — This method creates a Feature object and a ReferencePoint object at the specified location.")(point[, instanceName]) | This method creates a Feature object and a ReferencePoint object at the specified location. |
    | [`RemoveWireEdges`](feature.html#abaqus.Feature.Feature.Feature.RemoveWireEdges "abaqus.Feature.Feature.Feature.RemoveWireEdges (Python method) — This method removes wire edges.")(wireEdgeList) | This method removes wire edges. |
    | [`WirePolyLine`](feature.html#abaqus.Feature.Feature.Feature.WirePolyLine "abaqus.Feature.Feature.Feature.WirePolyLine (Python method) — This method creates an additional Feature object by creating a series of wires joining points in pairs. When such a feature is created at the Part level, then each point can be either a datum point, a vertex, a reference point, an interesting point, an orphan mesh node, or the coordinates of a point. When such a feature is created at the Assembly level, then each point can only be a vertex, a reference point, or an orphan mesh node.")(points[, mergeType, meshable]) | This method creates an additional Feature object by creating a series of wires joining points in pairs. |
    | [`isSuppressed`](feature.html#abaqus.Feature.Feature.Feature.isSuppressed "abaqus.Feature.Feature.Feature.isSuppressed (Python method) — This method queries the suppressed state of the feature.")() | This method queries the suppressed state of the feature. |
    | [`restore`](feature.html#abaqus.Feature.Feature.Feature.restore "abaqus.Feature.Feature.Feature.restore (Python method) — This method restores the parameters of a feature to the value they had when the backup method was invoked on the part or assembly.")() | This method restores the parameters of a feature to the value they had when the backup method was invoked on the part or assembly. |
    | [`resume`](feature.html#abaqus.Feature.Feature.Feature.resume "abaqus.Feature.Feature.Feature.resume (Python method) — This method resumes suppressed features.")() | This method resumes suppressed features. |
    | [`setValues`](feature.html#abaqus.Feature.Feature.Feature.setValues "abaqus.Feature.Feature.Feature.setValues (Python method) — This method modifies the Feature object.")([parameter, parameter1, ...]) | This method modifies the Feature object. |
    | [`suppress`](feature.html#abaqus.Feature.Feature.Feature.suppress "abaqus.Feature.Feature.Feature.suppress (Python method) — This method suppresses features.")() | This method suppresses features. |

    ---

    Member Details:

    Lock()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1827-L1833)[¶](#abaqus.Part.PartBase.PartBase.Lock "Permalink to this definition")
    :   This method locks the part.

        Locking the part prevents any further changes to the part that can trigger regeneration of the part.

    LockForUpgrade()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1843-L1850)[¶](#abaqus.Part.PartBase.PartBase.LockForUpgrade "Permalink to this definition")
    :   This method locks the part for upgrade.

        Locking the part prevents any further changes to the part that can trigger regeneration of the part.
        When the part is unlocked, all the parts are upgraded and regenrated.

    Part2DGeomFrom2DMesh(*[name](#abaqus.Part.PartBase.PartBase.Part2DGeomFrom2DMesh.name "abaqus.Part.PartBase.PartBase.Part2DGeomFrom2DMesh.name (Python parameter) — A String specifying the repository key.")*, *[part](#abaqus.Part.PartBase.PartBase.Part2DGeomFrom2DMesh.part "abaqus.Part.PartBase.PartBase.Part2DGeomFrom2DMesh.part (Python parameter) — A Part object specifying an existing two-dimensional orphan mesh Part object.")*, *[featureAngle](#abaqus.Part.PartBase.PartBase.Part2DGeomFrom2DMesh.featureAngle "abaqus.Part.PartBase.PartBase.Part2DGeomFrom2DMesh.featureAngle (Python parameter) — A Float specifying the angle (in degrees) between line segments that triggers a break in the geometry.")*, *[splineCurvatureLimit](#abaqus.Part.PartBase.PartBase.Part2DGeomFrom2DMesh.splineCurvatureLimit "abaqus.Part.PartBase.PartBase.Part2DGeomFrom2DMesh.splineCurvatureLimit (Python parameter) — A Float specifying the traversal angle in degrees of the spline that triggers a break in the geometry.")=`90`*, *[twist](#abaqus.Part.PartBase.PartBase.Part2DGeomFrom2DMesh.twist "abaqus.Part.PartBase.PartBase.Part2DGeomFrom2DMesh.twist (Python parameter) — A Boolean specifying whether to include a twist DEGREE OF FREEDOM in the part (only available when dimensionality = AXISYMMETRIC and type = DEFORMABLE_BODY).")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L825-L875)[¶](#abaqus.Part.PartBase.PartBase.Part2DGeomFrom2DMesh "Permalink to this definition")
    :   This method creates a geometric Part object from the outline of an existing two-dimensional orphan
        mesh Part object and places it in the parts repository. If the Part2DGeomFrom2DMesh method cannot create
        a valid two-dimensional shell section from the two-dimensional mesh, the method fails and creates an
        empty geometry part with a failed base shell feature.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].Part2DGeomFrom2DMesh
        ```

        Note

        Check [Part2DGeomFrom2DMesh on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-part2dgeomfrom2dmeshpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.Part2DGeomFrom2DMesh-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Part.PartBase.PartBase.Part2DGeomFrom2DMesh.name "Permalink to this definition")
            :   A String specifying the repository key.

            part[¶](#abaqus.Part.PartBase.PartBase.Part2DGeomFrom2DMesh.part "Permalink to this definition")
            :   A Part object specifying an existing two-dimensional orphan mesh Part object.

            featureAngle[¶](#abaqus.Part.PartBase.PartBase.Part2DGeomFrom2DMesh.featureAngle "Permalink to this definition")
            :   A Float specifying the angle (in degrees) between line segments that triggers a break in
                the geometry.

            splineCurvatureLimit=`90`[¶](#abaqus.Part.PartBase.PartBase.Part2DGeomFrom2DMesh.splineCurvatureLimit "Permalink to this definition")
            :   A Float specifying the traversal angle in degrees of the spline that triggers a break in
                the geometry. The default value is 90.

            twist=`0`[¶](#abaqus.Part.PartBase.PartBase.Part2DGeomFrom2DMesh.twist "Permalink to this definition")
            :   A Boolean specifying whether to include a twist DEGREE OF FREEDOM in the part (only
                available when **dimensionality** = AXISYMMETRIC and **type** = DEFORMABLE\_BODY). The default
                value is OFF.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.Part2DGeomFrom2DMesh-returns "Permalink to this headline")
        :   **part** – A Part object

            * If the specified part is not an orphan mesh part:
              Specified part must be an orphan mesh.
            * If the Part2DGeomFrom2DMesh method cannot create a valid two-dimensional shell section from the two-dimensional mesh:
              Planar shell feature failed
            * If the specified part is not two-dimensional:
              Cannot create a geometry from a 3D part.
            * If the specified part is a rigid body:
              Cannot create a geometry from a rigid body.

        Return type:[¶](#abaqus.Part.PartBase.PartBase.Part2DGeomFrom2DMesh-return-type "Permalink to this headline")
        :   `Part`

    PartFromBooleanCut(*[name](#abaqus.Part.PartBase.PartBase.PartFromBooleanCut.name "abaqus.Part.PartBase.PartBase.PartFromBooleanCut.name (Python parameter) — A String specifying the repository key.")*, *[instanceToBeCut](#abaqus.Part.PartBase.PartBase.PartFromBooleanCut.instanceToBeCut "abaqus.Part.PartBase.PartBase.PartFromBooleanCut.instanceToBeCut (Python parameter) — A PartInstance specifying the base instance from which to cut other instances.")*, *[cuttingInstances](#abaqus.Part.PartBase.PartBase.PartFromBooleanCut.cuttingInstances "abaqus.Part.PartBase.PartBase.PartFromBooleanCut.cuttingInstances (Python parameter) — A sequence of PartInstance objects specifying the instances with which to cut the base instance.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L273-L297)[¶](#abaqus.Part.PartBase.PartBase.PartFromBooleanCut "Permalink to this definition")
    :   This method creates a Part in the parts repository after subtracting or cutting the geometries of a
        group of part instances from that of a base part instance.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].PartFromBooleanCut
        ```

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.PartFromBooleanCut-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Part.PartBase.PartBase.PartFromBooleanCut.name "Permalink to this definition")
            :   A String specifying the repository key.

            instanceToBeCut[¶](#abaqus.Part.PartBase.PartBase.PartFromBooleanCut.instanceToBeCut "Permalink to this definition")
            :   A PartInstance specifying the base instance from which to cut other instances.

            cuttingInstances[¶](#abaqus.Part.PartBase.PartBase.PartFromBooleanCut.cuttingInstances "Permalink to this definition")
            :   A sequence of PartInstance objects specifying the instances with which to cut the base
                instance.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.PartFromBooleanCut-returns "Permalink to this headline")
        :   **part** – A Part object

        Return type:[¶](#abaqus.Part.PartBase.PartBase.PartFromBooleanCut-return-type "Permalink to this headline")
        :   `Part`

    PartFromBooleanMerge(*[name](#abaqus.Part.PartBase.PartBase.PartFromBooleanMerge.name "abaqus.Part.PartBase.PartBase.PartFromBooleanMerge.name (Python parameter) — A String specifying the repository key.")*, *[instances](#abaqus.Part.PartBase.PartBase.PartFromBooleanMerge.instances "abaqus.Part.PartBase.PartBase.PartFromBooleanMerge.instances (Python parameter) — A sequence of PartInstance objects specifying the part instances to merge.")*, *[keepIntersections](#abaqus.Part.PartBase.PartBase.PartFromBooleanMerge.keepIntersections "abaqus.Part.PartBase.PartBase.PartFromBooleanMerge.keepIntersections (Python parameter) — A Boolean specifying whether the boundary intersections of Abaqus native part instances should be retained after the merge operation.")=`False`*, *[mergeNodes](#abaqus.Part.PartBase.PartBase.PartFromBooleanMerge.mergeNodes "abaqus.Part.PartBase.PartBase.PartFromBooleanMerge.mergeNodes (Python parameter) — A SymbolicConstant specifying whether the nodes of orphan mesh part instances should be retained after the merge operation.")=`abaqusConstants.BOUNDARY_ONLY`*, *[nodeMergingTolerance](#abaqus.Part.PartBase.PartBase.PartFromBooleanMerge.nodeMergingTolerance "abaqus.Part.PartBase.PartBase.PartFromBooleanMerge.nodeMergingTolerance (Python parameter) — A Float specifying the maximum distance between nodes of orphan mesh part instances that will be merged and replaced with a single new node.")=`None`*, *[removeDuplicateElements](#abaqus.Part.PartBase.PartBase.PartFromBooleanMerge.removeDuplicateElements "abaqus.Part.PartBase.PartBase.PartFromBooleanMerge.removeDuplicateElements (Python parameter) — A Boolean specifying whether elements with the same connectivity after the merge will merged into a single element.")=`1`*, *[domain](#abaqus.Part.PartBase.PartBase.PartFromBooleanMerge.domain "abaqus.Part.PartBase.PartBase.PartFromBooleanMerge.domain (Python parameter) — A SymbolicConstant specifying whether the part instances being merged are geometric instances or mesh instances.")=`abaqusConstants.GEOMETRY`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L299-L349)[¶](#abaqus.Part.PartBase.PartBase.PartFromBooleanMerge "Permalink to this definition")
    :   This method creates a Part in the parts repository after merging two or more part instances. The part
        instances can be either Abaqus native parts or orphan mesh parts, but they cannot be a combination of
        both.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].PartFromBooleanMerge
        ```

        Note

        Check [PartFromBooleanMerge on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partfrombooleanmergepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.PartFromBooleanMerge-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Part.PartBase.PartBase.PartFromBooleanMerge.name "Permalink to this definition")
            :   A String specifying the repository key.

            instances[¶](#abaqus.Part.PartBase.PartBase.PartFromBooleanMerge.instances "Permalink to this definition")
            :   A sequence of PartInstance objects specifying the part instances to merge.

            keepIntersections=`False`[¶](#abaqus.Part.PartBase.PartBase.PartFromBooleanMerge.keepIntersections "Permalink to this definition")
            :   A Boolean specifying whether the boundary intersections of Abaqus native part instances
                should be retained after the merge operation. The default value is False.

            mergeNodes=`abaqusConstants.BOUNDARY_ONLY`[¶](#abaqus.Part.PartBase.PartBase.PartFromBooleanMerge.mergeNodes "Permalink to this definition")
            :   A SymbolicConstant specifying whether the nodes of orphan mesh part instances should be
                retained after the merge operation. Possible values are BOUNDARY\_ONLY, ALL, or NONE. The
                default value is BOUNDARY\_ONLY.

            nodeMergingTolerance=`None`[¶](#abaqus.Part.PartBase.PartBase.PartFromBooleanMerge.nodeMergingTolerance "Permalink to this definition")
            :   A Float specifying the maximum distance between nodes of orphan mesh part instances that
                will be merged and replaced with a single new node. The location of the new node is the
                average position of the deleted nodes. The default value is 10⁻⁶.

            removeDuplicateElements=`1`[¶](#abaqus.Part.PartBase.PartBase.PartFromBooleanMerge.removeDuplicateElements "Permalink to this definition")
            :   A Boolean specifying whether elements with the same connectivity after the merge will
                merged into a single element. The default value is ON.

            domain=`abaqusConstants.GEOMETRY`[¶](#abaqus.Part.PartBase.PartBase.PartFromBooleanMerge.domain "Permalink to this definition")
            :   A SymbolicConstant specifying whether the part instances being merged are geometric
                instances or mesh instances. Possible values are GEOMETRY, MESH or BOTH. The default
                value is GEOMETRY.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.PartFromBooleanMerge-returns "Permalink to this headline")
        :   **part** – A Part object

        Return type:[¶](#abaqus.Part.PartBase.PartBase.PartFromBooleanMerge-return-type "Permalink to this headline")
        :   `Part`

    PartFromExtrude2DMesh(*[name](#abaqus.Part.PartBase.PartBase.PartFromExtrude2DMesh.name "abaqus.Part.PartBase.PartBase.PartFromExtrude2DMesh.name (Python parameter) — A String specifying the repository key.")*, *[part](#abaqus.Part.PartBase.PartBase.PartFromExtrude2DMesh.part "abaqus.Part.PartBase.PartBase.PartFromExtrude2DMesh.part (Python parameter) — A Part object specifying an existing two-dimensional orphan mesh Part object.")*, *[depth](#abaqus.Part.PartBase.PartBase.PartFromExtrude2DMesh.depth "abaqus.Part.PartBase.PartBase.PartFromExtrude2DMesh.depth (Python parameter) — A Float specifying the total extrusion distance.")*, *[elementSize](#abaqus.Part.PartBase.PartBase.PartFromExtrude2DMesh.elementSize "abaqus.Part.PartBase.PartBase.PartFromExtrude2DMesh.elementSize (Python parameter) — A Float specifying an approximate element length in the extruded direction.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L351-L384)[¶](#abaqus.Part.PartBase.PartBase.PartFromExtrude2DMesh "Permalink to this definition")
    :   This method creates a Part object by extruding an existing two-dimensional orphan mesh Part object in
        the positive **Z** direction and places it in the parts repository.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].PartFromExtrude2DMesh
        ```

        Note

        Check [PartFromExtrude2DMesh on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partfromextrude2dmeshpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.PartFromExtrude2DMesh-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Part.PartBase.PartBase.PartFromExtrude2DMesh.name "Permalink to this definition")
            :   A String specifying the repository key.

            part[¶](#abaqus.Part.PartBase.PartBase.PartFromExtrude2DMesh.part "Permalink to this definition")
            :   A Part object specifying an existing two-dimensional orphan mesh Part object.

            depth[¶](#abaqus.Part.PartBase.PartBase.PartFromExtrude2DMesh.depth "Permalink to this definition")
            :   A Float specifying the total extrusion distance.

            elementSize[¶](#abaqus.Part.PartBase.PartBase.PartFromExtrude2DMesh.elementSize "Permalink to this definition")
            :   A Float specifying an approximate element length in the extruded direction.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.PartFromExtrude2DMesh-returns "Permalink to this headline")
        :   **part** – A Part object

            * If the specified part is not an orphan mesh part:
              Cannot extrude a geometric part.
            * If the specified part is not two-dimensional:
              Cannot extrude a 3D part.
            * If the specified part is a rigid body:
              Cannot change dimension of a rigid body.

        Return type:[¶](#abaqus.Part.PartBase.PartBase.PartFromExtrude2DMesh-return-type "Permalink to this headline")
        :   `Part`

    PartFromGeometryFile(*[name](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.name "abaqus.Part.PartBase.PartBase.PartFromGeometryFile.name (Python parameter) — A String specifying the repository key.")*, *[geometryFile](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.geometryFile "abaqus.Part.PartBase.PartBase.PartFromGeometryFile.geometryFile (Python parameter) — An AcisFile object specifying a file containing geometry.")*, *[dimensionality](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.dimensionality "abaqus.Part.PartBase.PartBase.PartFromGeometryFile.dimensionality (Python parameter) — A SymbolicConstant specifying the dimensionality of the part.")*, *[type](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.type "abaqus.Part.PartBase.PartBase.PartFromGeometryFile.type (Python parameter) — A SymbolicConstant specifying the type of the part.")*, *[bodyNum](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.bodyNum "abaqus.Part.PartBase.PartBase.PartFromGeometryFile.bodyNum (Python parameter) — An Int specifying the desired body to be selected from an ACIS object containing a list of N ACIS bodies.")=`1`*, *[combine](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.combine "abaqus.Part.PartBase.PartBase.PartFromGeometryFile.combine (Python parameter) — A Boolean specifying weather to create a single part by combining all the bodies in the ACIS object.")=`False`*, *[booleanSolids](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.booleanSolids "abaqus.Part.PartBase.PartBase.PartFromGeometryFile.booleanSolids (Python parameter) — A Boolean specifying whether the solids should be boolean while combining all the bodies.The default value is FALSE.")=`False`*, *[retainBoundary](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.retainBoundary "abaqus.Part.PartBase.PartBase.PartFromGeometryFile.retainBoundary (Python parameter) — A Boolean specifying whether the intersecting boundaries should be retained while boolean the solids.The default value is FALSE.")=`False`*, *[usePartNameFromFile](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.usePartNameFromFile "abaqus.Part.PartBase.PartBase.PartFromGeometryFile.usePartNameFromFile (Python parameter) — A Boolean specifying whether the part names specified in a STEP file should be used as the names in the Abaqus model database.")=`0`*, *[stitchTolerance](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.stitchTolerance "abaqus.Part.PartBase.PartBase.PartFromGeometryFile.stitchTolerance (Python parameter) — A Float indicating the maximum gap to be stitched.")=`1`*, *[twist](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.twist "abaqus.Part.PartBase.PartBase.PartFromGeometryFile.twist (Python parameter) — A Boolean specifying whether to include a twist DEGREE OF FREEDOM in the part (only available when dimensionality = AXISYMMETRIC and type = DEFORMABLE_BODY).")=`0`*, *[scale](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.scale "abaqus.Part.PartBase.PartBase.PartFromGeometryFile.scale (Python parameter) — A Float specifying the scaling factor to apply to the imported geometric entities.")=`1`*, *[convertToAnalytical](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.convertToAnalytical "abaqus.Part.PartBase.PartBase.PartFromGeometryFile.convertToAnalytical (Python parameter) — An Int specifying whether to convert to analytical entities.")=`0`*, *[convertToPrecise](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.convertToPrecise "abaqus.Part.PartBase.PartBase.PartFromGeometryFile.convertToPrecise (Python parameter) — An Int specifying whether to convert to precise geometry.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L386-L479)[¶](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile "Permalink to this definition")
    :   This method creates a Part object and places it in the parts repository.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].PartFromGeometryFile
        ```

        Note

        Check [PartFromGeometryFile on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partfromgeometryfilepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.name "Permalink to this definition")
            :   A String specifying the repository key.

            geometryFile[¶](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.geometryFile "Permalink to this definition")
            :   An AcisFile object specifying a file containing geometry.

            dimensionality[¶](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.dimensionality "Permalink to this definition")
            :   A SymbolicConstant specifying the dimensionality of the part. Possible values are
                THREE\_D, TWO\_D\_PLANAR, and AXISYMMETRIC.

            type[¶](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.type "Permalink to this definition")
            :   A SymbolicConstant specifying the type of the part. Possible values are DEFORMABLE\_BODY,
                EULERIAN, DISCRETE\_RIGID\_SURFACE, and ANALYTIC\_RIGID\_SURFACE.

            bodyNum=`1`[¶](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.bodyNum "Permalink to this definition")
            :   An Int specifying the desired body to be selected from an ACIS object containing a list
                of **N** ACIS bodies. Possible values are 1 ≤ **bodyNum** ≤ **N**. The default value is 1.

            combine=`False`[¶](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.combine "Permalink to this definition")
            :   A Boolean specifying weather to create a single part by combining all the bodies in the
                ACIS object. This argument is ignored if **bodyNum** is specified. The default value is
                False.

            booleanSolids=`False`[¶](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.booleanSolids "Permalink to this definition")
            :   A Boolean specifying whether the solids should be boolean while combining all the
                bodies.The default value is FALSE.

            retainBoundary=`False`[¶](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.retainBoundary "Permalink to this definition")
            :   A Boolean specifying whether the intersecting boundaries should be retained while
                boolean the solids.The default value is FALSE.

            usePartNameFromFile=`0`[¶](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.usePartNameFromFile "Permalink to this definition")
            :   A Boolean specifying whether the part names specified in a STEP file should be used as
                the names in the Abaqus model database. If this option is TRUE, the part names in the
                STEP file will be used; if FALSE, each imported part will be named using the text of the
                **name** argument followed by a number. This functionality is available only for import
                from STEP files; for import from all other types of files this option should be FALSE.

            stitchTolerance=`1`[¶](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.stitchTolerance "Permalink to this definition")
            :   A Float indicating the maximum gap to be stitched. The value should be smaller than the
                minimum feature size and bigger than the maximum gap expected to be stitched in the
                model. Otherwise this command may remove small (sliver) edges that are smaller than the
                tolerance. The default value is 1.0

            twist=`0`[¶](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.twist "Permalink to this definition")
            :   A Boolean specifying whether to include a twist DEGREE OF FREEDOM in the part (only
                available when **dimensionality** = AXISYMMETRIC and **type** = DEFORMABLE\_BODY). The default
                value is OFF.

            scale=`1`[¶](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.scale "Permalink to this definition")
            :   A Float specifying the scaling factor to apply to the imported geometric entities. The
                default value is 1.0.

            convertToAnalytical=`0`[¶](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.convertToAnalytical "Permalink to this definition")
            :   An Int specifying whether to convert to analytical entities. Possible values are 0 or 1.
                The default value is 0. If **convertToAnalytical** = 1, all the numerical entities, such as
                splines, are converted to analytical entities, such as arcs and lines, during the repair
                phase of the command.

            convertToPrecise=`0`[¶](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile.convertToPrecise "Permalink to this definition")
            :   An Int specifying whether to convert to precise geometry. Possible value are 0 or 1. The
                default value is 0. If **convertToPrecise** = 1, the application will attempt to re-evaluate
                the tolerant entities to be more precise.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile-returns "Permalink to this headline")
        :   **part** – A Part object

        Return type:[¶](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile-return-type "Permalink to this headline")
        :   `Part`

        Raises:[¶](#abaqus.Part.PartBase.PartBase.PartFromGeometryFile-raises "Permalink to this headline")
        :   * **PartError** – If the ACIS file is corrupt
            * **PartError** – the file is corrupt, If the dimensionality does not correspond to what is found in the ACIS file
            * **PartError** – type does not match the contents of the file, dimensionality does not match the contents of the file,
              If the type does not correspond to what is found in the ACIS file

    PartFromInstanceMesh(*[name](#abaqus.Part.PartBase.PartBase.PartFromInstanceMesh.name "abaqus.Part.PartBase.PartBase.PartFromInstanceMesh.name (Python parameter) — A String specifying the repository key.")*, *[partInstances](#abaqus.Part.PartBase.PartBase.PartFromInstanceMesh.partInstances "abaqus.Part.PartBase.PartBase.PartFromInstanceMesh.partInstances (Python parameter) — A sequence of PartInstance objects to be used in the creation of the new mesh part.")=`()`*, *[copyPartSets](#abaqus.Part.PartBase.PartBase.PartFromInstanceMesh.copyPartSets "abaqus.Part.PartBase.PartBase.PartFromInstanceMesh.copyPartSets (Python parameter) — A Boolean specifying whether to copy sets, surfaces, and attributes from the base part or parts of the specified part instances to the new part.")=`False`*, *[copyAssemblySets](#abaqus.Part.PartBase.PartBase.PartFromInstanceMesh.copyAssemblySets "abaqus.Part.PartBase.PartBase.PartFromInstanceMesh.copyAssemblySets (Python parameter) — A Boolean specifying whether to copy assembly-level sets that reference entities of the specified part instances to the new part.")=`False`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L481-L525)[¶](#abaqus.Part.PartBase.PartBase.PartFromInstanceMesh "Permalink to this definition")
    :   This method creates a Part object containing the mesh found in the supplied PartInstance objects and
        places the new Part object in the parts repository.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].PartFromInstanceMesh
        ```

        Note

        Check [PartFromInstanceMesh on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partfrominstancemeshpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.PartFromInstanceMesh-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Part.PartBase.PartBase.PartFromInstanceMesh.name "Permalink to this definition")
            :   A String specifying the repository key.

            partInstances=`()`[¶](#abaqus.Part.PartBase.PartBase.PartFromInstanceMesh.partInstances "Permalink to this definition")
            :   A sequence of PartInstance objects to be used in the creation of the new mesh part. If
                the **partInstances** argument is omitted, the new Part object contains the mesh of all
                the part instances in the assembly.

            copyPartSets=`False`[¶](#abaqus.Part.PartBase.PartBase.PartFromInstanceMesh.copyPartSets "Permalink to this definition")
            :   A Boolean specifying whether to copy sets, surfaces, and attributes from the base part
                or parts of the specified part instances to the new part. The default is False.

            copyAssemblySets=`False`[¶](#abaqus.Part.PartBase.PartBase.PartFromInstanceMesh.copyAssemblySets "Permalink to this definition")
            :   A Boolean specifying whether to copy assembly-level sets that reference entities of the
                specified part instances to the new part. The default is False.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.PartFromInstanceMesh-returns "Permalink to this headline")
        :   **part** – A Part object

            * If the analysis type (deformable or rigid) is not consistent among the supplied part
              instances:
              The selected part instances do not have a consistent analysis type.
            * If the assembly does not contain a mesh:
              The current assembly does not contain a mesh for a mesh part.
            * If the specified part instances do not contain a mesh:
              The selected part instances do not have a mesh for a mesh part.

        Return type:[¶](#abaqus.Part.PartBase.PartBase.PartFromInstanceMesh-return-type "Permalink to this headline")
        :   `Part`

    PartFromMesh(*[name](#abaqus.Part.PartBase.PartBase.PartFromMesh.name "abaqus.Part.PartBase.PartBase.PartFromMesh.name (Python parameter) — A String specifying the repository key.")*, *[copySets](#abaqus.Part.PartBase.PartBase.PartFromMesh.copySets "abaqus.Part.PartBase.PartBase.PartFromMesh.copySets (Python parameter) — A Boolean specifying whether to copy sets, surfaces, and attributes to the new part.")=`False`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L527-L553)[¶](#abaqus.Part.PartBase.PartBase.PartFromMesh "Permalink to this definition")
    :   This method creates a Part object containing the mesh found in the part and places the new Part
        object in the parts repository.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].PartFromMesh
        ```

        Note

        Check [PartFromMesh on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partfrommeshpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.PartFromMesh-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Part.PartBase.PartBase.PartFromMesh.name "Permalink to this definition")
            :   A String specifying the repository key.

            copySets=`False`[¶](#abaqus.Part.PartBase.PartBase.PartFromMesh.copySets "Permalink to this definition")
            :   A Boolean specifying whether to copy sets, surfaces, and attributes to the new part. The
                default is False.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.PartFromMesh-returns "Permalink to this headline")
        :   **part** – A Part object

            * If the part does not contain a mesh:
              The current part does not contain a mesh for a mesh part.

        Return type:[¶](#abaqus.Part.PartBase.PartBase.PartFromMesh-return-type "Permalink to this headline")
        :   `Part`

    PartFromMeshMirror(*[name](#abaqus.Part.PartBase.PartBase.PartFromMeshMirror.name "abaqus.Part.PartBase.PartBase.PartFromMeshMirror.name (Python parameter) — A String specifying the repository key.")*, *[part](#abaqus.Part.PartBase.PartBase.PartFromMeshMirror.part "abaqus.Part.PartBase.PartBase.PartFromMeshMirror.part (Python parameter) — A Part object specifying an existing orphan mesh part.")*, *[point1](#abaqus.Part.PartBase.PartBase.PartFromMeshMirror.point1 "abaqus.Part.PartBase.PartBase.PartFromMeshMirror.point1 (Python parameter) — A sequence of three Floats specifying a point on the mirror plane.")*, *[point2](#abaqus.Part.PartBase.PartBase.PartFromMeshMirror.point2 "abaqus.Part.PartBase.PartBase.PartFromMeshMirror.point2 (Python parameter) — A sequence of three Floats specifying a point in the direction of the normal to the mirror plane.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L555-L596)[¶](#abaqus.Part.PartBase.PartBase.PartFromMeshMirror "Permalink to this definition")
    :   This method creates a Part object by mirroring an existing orphan mesh Part object about
        a specified plane and places it in the parts repository. The result is a union of the
        original and the mirrored copy. Contrast the PartFromMeshMirror method with the
        **mirrorPlane** argument of the Part copy constructor. The **mirrorPlane** argument creates
        only the second half of the part but does not unite the two halves.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].PartFromMeshMirror
        ```

        Note

        Check [PartFromMeshMirror on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partfrommeshmirrorpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.PartFromMeshMirror-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Part.PartBase.PartBase.PartFromMeshMirror.name "Permalink to this definition")
            :   A String specifying the repository key.

            part[¶](#abaqus.Part.PartBase.PartBase.PartFromMeshMirror.part "Permalink to this definition")
            :   A Part object specifying an existing orphan mesh part.

            point1[¶](#abaqus.Part.PartBase.PartBase.PartFromMeshMirror.point1 "Permalink to this definition")
            :   A sequence of three Floats specifying a point on the mirror plane. This point is the
                local origin in the local system of the plane.

            point2[¶](#abaqus.Part.PartBase.PartBase.PartFromMeshMirror.point2 "Permalink to this definition")
            :   A sequence of three Floats specifying a point in the direction of the normal to the
                mirror plane. This point must not be coincident with **point1**.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.PartFromMeshMirror-returns "Permalink to this headline")
        :   **part** – A Part object

            * If the specified part is not an orphan mesh part:
              Cannot mirror a geometric part.
            * If the specified part is a rigid body:
              Cannot mirror a rigid body.
            * If **point1** and **point2** are coincident:
              Mirror plane director has zero length.
            * If the specified part is two-dimensional and the plane is not parallel to the
              **Z** axis:
              Mirror plane must be parallel to Z axis for 2D parts

        Return type:[¶](#abaqus.Part.PartBase.PartBase.PartFromMeshMirror-return-type "Permalink to this headline")
        :   `Part`

    PartFromNodesAndElements(*[name](#abaqus.Part.PartBase.PartBase.PartFromNodesAndElements.name "abaqus.Part.PartBase.PartBase.PartFromNodesAndElements.name (Python parameter) — A String specifying the repository key.")*, *[dimensionality](#abaqus.Part.PartBase.PartBase.PartFromNodesAndElements.dimensionality "abaqus.Part.PartBase.PartBase.PartFromNodesAndElements.dimensionality (Python parameter) — A SymbolicConstant specifying the dimensionality of the part.")*, *[type](#abaqus.Part.PartBase.PartBase.PartFromNodesAndElements.type "abaqus.Part.PartBase.PartBase.PartFromNodesAndElements.type (Python parameter) — A SymbolicConstant specifying the type of the part.")*, *[nodes](#abaqus.Part.PartBase.PartBase.PartFromNodesAndElements.nodes "abaqus.Part.PartBase.PartBase.PartFromNodesAndElements.nodes (Python parameter) — A sequence of (nodeLabels, nodeCoords) specifying the nodes of the mesh. nodeLabels is a sequence of Ints specifying the node labels, and nodeCoords is a sequence of sequences of three Floats specifying the nodal coordinates.")*, *[elements](#abaqus.Part.PartBase.PartBase.PartFromNodesAndElements.elements "abaqus.Part.PartBase.PartBase.PartFromNodesAndElements.elements (Python parameter) — A sequence of sequences of(meshType, elementLabels, elementConns) specifying the elements of the mesh.")*, *[twist](#abaqus.Part.PartBase.PartBase.PartFromNodesAndElements.twist "abaqus.Part.PartBase.PartBase.PartFromNodesAndElements.twist (Python parameter) — A boolean specifying whether the part is defined with twist.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L598-L644)[¶](#abaqus.Part.PartBase.PartBase.PartFromNodesAndElements "Permalink to this definition")
    :   This method creates a Part object from nodes and elements and places it in the parts repository.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].PartFromNodesAndElements
        ```

        Note

        Check [PartFromNodesAndElements on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partfromnodesandelementspyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.PartFromNodesAndElements-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Part.PartBase.PartBase.PartFromNodesAndElements.name "Permalink to this definition")
            :   A String specifying the repository key.

            dimensionality[¶](#abaqus.Part.PartBase.PartBase.PartFromNodesAndElements.dimensionality "Permalink to this definition")
            :   A SymbolicConstant specifying the dimensionality of the part. Possible values are
                THREE\_D, TWO\_D\_PLANAR, and AXISYMMETRIC.

            type[¶](#abaqus.Part.PartBase.PartBase.PartFromNodesAndElements.type "Permalink to this definition")
            :   A SymbolicConstant specifying the type of the part. Possible values are DEFORMABLE\_BODY,
                EULERIAN, DISCRETE\_RIGID\_SURFACE, and ANALYTIC\_RIGID\_SURFACE.

            nodes[¶](#abaqus.Part.PartBase.PartBase.PartFromNodesAndElements.nodes "Permalink to this definition")
            :   A sequence of (*nodeLabels*, **nodeCoords**) specifying the nodes of the mesh.
                **nodeLabels** is a sequence of Ints specifying the node labels, and **nodeCoords** is a
                sequence of sequences of three Floats specifying the nodal coordinates.

            elements[¶](#abaqus.Part.PartBase.PartBase.PartFromNodesAndElements.elements "Permalink to this definition")
            :   A sequence of sequences of(*meshType*, **elementLabels**, **elementConns**) specifying the
                elements of the mesh. **meshType** is a String specifying the element type.
                **elementlabels** is a sequence of Ints specifying the element labels. **elementConns** is a
                sequence of sequences of node labels specifying the element connectivity.

            twist=`0`[¶](#abaqus.Part.PartBase.PartBase.PartFromNodesAndElements.twist "Permalink to this definition")
            :   A boolean specifying whether the part is defined with twist. This option has meaning
                only when **dimensionality** = AXISYMMETRIC. Possible values are ON and OFF. The default
                value is OFF.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.PartFromNodesAndElements-returns "Permalink to this headline")
        :   **part** – A Part object

        Return type:[¶](#abaqus.Part.PartBase.PartBase.PartFromNodesAndElements-return-type "Permalink to this headline")
        :   `Part`

    PartFromOdb(*[name](#abaqus.Part.PartBase.PartBase.PartFromOdb.name "abaqus.Part.PartBase.PartBase.PartFromOdb.name (Python parameter) — A String specifying the repository key.")*, *[odb](#abaqus.Part.PartBase.PartBase.PartFromOdb.odb "abaqus.Part.PartBase.PartBase.PartFromOdb.odb (Python parameter) — An output database object.")*, *[fileName](#abaqus.Part.PartBase.PartBase.PartFromOdb.fileName "abaqus.Part.PartBase.PartBase.PartFromOdb.fileName (Python parameter) — A String specifying the name of the output database file from which to create the part. The default value is an empty string.")=`''`*, *[instance](#abaqus.Part.PartBase.PartBase.PartFromOdb.instance "abaqus.Part.PartBase.PartBase.PartFromOdb.instance (Python parameter) — A String specifying the part instance in the output database from which to create the part.")=`''`*, *[elementSet](#abaqus.Part.PartBase.PartBase.PartFromOdb.elementSet "abaqus.Part.PartBase.PartBase.PartFromOdb.elementSet (Python parameter) — A String specifying an element set defined on the output database.")=`''`*, *[shape](#abaqus.Part.PartBase.PartBase.PartFromOdb.shape "abaqus.Part.PartBase.PartBase.PartFromOdb.shape (Python parameter) — A SymbolicConstant specifying the configuration state.")=`abaqusConstants.UNDEFORMED`*, *[step](#abaqus.Part.PartBase.PartBase.PartFromOdb.step "abaqus.Part.PartBase.PartBase.PartFromOdb.step (Python parameter) — An Int specifying the step number for reading deformed coordinates.")=`None`*, *[frame](#abaqus.Part.PartBase.PartBase.PartFromOdb.frame "abaqus.Part.PartBase.PartBase.PartFromOdb.frame (Python parameter) — An Int specifying the frame number for reading deformed coordinates. 0≤frame≤N−10≤frame≤N-1 where NN is the number of available frames.")=`None`*, *[twist](#abaqus.Part.PartBase.PartBase.PartFromOdb.twist "abaqus.Part.PartBase.PartBase.PartFromOdb.twist (Python parameter) — A Boolean specifying whether to include a twist DEGREE OF FREEDOM in the part (only available when dimensionality = AXISYMMETRIC and type = DEFORMABLE_BODY).")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L646-L728)[¶](#abaqus.Part.PartBase.PartBase.PartFromOdb "Permalink to this definition")
    :   This method creates an orphan mesh Part object by reading an output database. The new part is placed
        in the parts repository.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].PartFromOdb
        ```

        Note

        Check [PartFromOdb on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partfromodbpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.PartFromOdb-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Part.PartBase.PartBase.PartFromOdb.name "Permalink to this definition")
            :   A String specifying the repository key.

            odb[¶](#abaqus.Part.PartBase.PartBase.PartFromOdb.odb "Permalink to this definition")
            :   An output database object.

            fileName=`''`[¶](#abaqus.Part.PartBase.PartBase.PartFromOdb.fileName "Permalink to this definition")
            :   A String specifying the name of the output database file from which to create the part.
                The default value is an empty string.

            instance=`''`[¶](#abaqus.Part.PartBase.PartBase.PartFromOdb.instance "Permalink to this definition")
            :   A String specifying the part instance in the output database from which to create the
                part. If no instance name is specified, Abaqus creates an orphan mesh part from the
                first part instance in the output database.

            elementSet=`''`[¶](#abaqus.Part.PartBase.PartBase.PartFromOdb.elementSet "Permalink to this definition")
            :   A String specifying an element set defined on the output database. Only elements from
                this set will be imported. The default is to import all element sets.

            shape=`abaqusConstants.UNDEFORMED`[¶](#abaqus.Part.PartBase.PartBase.PartFromOdb.shape "Permalink to this definition")
            :   A SymbolicConstant specifying the configuration state. Possible values are UNDEFORMED
                and DEFORMED. The default value is UNDEFORMED.

            step=`None`[¶](#abaqus.Part.PartBase.PartBase.PartFromOdb.step "Permalink to this definition")
            :   An Int specifying the step number for reading deformed coordinates. 0≤step≤N−10≤step≤N-1
                where NN is the number of available steps. The default value is the last available step.
                You should specify the **step** argument only when **shape** = DEFORMED.

            frame=`None`[¶](#abaqus.Part.PartBase.PartBase.PartFromOdb.frame "Permalink to this definition")
            :   An Int specifying the frame number for reading deformed coordinates.
                0≤frame≤N−10≤frame≤N-1 where NN is the number of available frames. The default value is
                the last available frame. You should specify the **frame** argument only when
                **shape** = DEFORMED.

            twist=`0`[¶](#abaqus.Part.PartBase.PartBase.PartFromOdb.twist "Permalink to this definition")
            :   A Boolean specifying whether to include a twist DEGREE OF FREEDOM in the part (only
                available when **dimensionality** = AXISYMMETRIC and **type** = DEFORMABLE\_BODY). The default
                value is OFF.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.PartFromOdb-returns "Permalink to this headline")
        :   **part** – A Part object

        Return type:[¶](#abaqus.Part.PartBase.PartBase.PartFromOdb-return-type "Permalink to this headline")
        :   `Part`

        Raises:[¶](#abaqus.Part.PartBase.PartBase.PartFromOdb-raises "Permalink to this headline")
        :   * **PartError** – If the output database contains elements of more than one dimensionality or type:
              File contains both axisymmetric and nonaxisymmetric elements.File contains both 2D and
              3D elements.File contains both rigid and deformable elements.
              If more than one part is found on the output database:
            * **Error** – File does not contain any valid frames.
              importing of more than one part is not currently supported, - If the output database does not contain any valid results for the specified step:
            * **Error** – Specified frame does not contain nodal displacements.
              If the specified step and frame do not contain any displacements:
            * **Error** – Specified element set is not defined in the ODB.
              If the specified element set is not found on the output database:
            * **OdiError** – Invalid step index: i. Available step indices: 0 - j.
              If the step number is invalid:
            * **OdiError** – Invalid frame index: i. Available frame indices: 0 - j.
              If the frame number is invalid:

    PartFromSection3DMeshByPlane(*[name](#abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane.name "abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane.name (Python parameter) — A String specifying the repository key.")*, *[part](#abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane.part "abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane.part (Python parameter) — A Part object specifying an existing three-dimensional orphan mesh part.")*, *[point1](#abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane.point1 "abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane.point1 (Python parameter) — A Sequence of three Floats specifying a point on the cutting plane.")*, *[point2](#abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane.point2 "abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane.point2 (Python parameter) — A Sequence of three Floats specifying a point in the direction of the normal to the cutting plane.")*, *[point3](#abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane.point3 "abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane.point3 (Python parameter) — A sequence of three Floats specifying the direction of the local 1-axis in the local system of the plane.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L730-L783)[¶](#abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane "Permalink to this definition")
    :   This method creates a Part object by cutting an existing three-dimensional orphan mesh Part object by
        a plane and places it in the parts repository. This method is valid only for orphan mesh parts composed
        of 8-node brick elements.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].PartFromSection3DMeshByPlane
        ```

        Note

        Check [PartFromSection3DMeshByPlane on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partfromsection3dmeshbyplanepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane.name "Permalink to this definition")
            :   A String specifying the repository key.

            part[¶](#abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane.part "Permalink to this definition")
            :   A Part object specifying an existing three-dimensional orphan mesh part.

            point1[¶](#abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane.point1 "Permalink to this definition")
            :   A Sequence of three Floats specifying a point on the cutting plane. This point is the
                local origin in the local system of the plane.

            point2[¶](#abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane.point2 "Permalink to this definition")
            :   A Sequence of three Floats specifying a point in the direction of the normal to the
                cutting plane. This point must not be coincident with **point1**.

            point3[¶](#abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane.point3 "Permalink to this definition")
            :   A sequence of three Floats specifying the direction of the local 1-axis in the local
                system of the plane. This point must not project onto **point1**.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane-returns "Permalink to this headline")
        :   **part** – A Part object

        Return type:[¶](#abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane-return-type "Permalink to this headline")
        :   `Part`

        Raises:[¶](#abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane-raises "Permalink to this headline")
        :   * [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.13)") – If the specified part is not an orphan mesh part,
              Cannot reduce dimension of a geometric part.
            * [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.13)") – If the specified part is not three-dimensional,
              Cannot reduce dimension of a 2D part.
            * [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.13)") – If the specified part is a rigid body,
              Cannot change dimension of a rigid body.
            * [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.13)") – If **point1** and **point2** are coincident,
              Cutting plane director has zero length.
            * [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.13)") – If **point3** projects onto **point1**,
              Local axis point projects to origin.
            * [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.13)") – If no elements are cut by the specified plane,
              Cannot reduce part dimension.

    PartFromSubstructure(*[name](#abaqus.Part.PartBase.PartBase.PartFromSubstructure.name "abaqus.Part.PartBase.PartBase.PartFromSubstructure.name (Python parameter) — A String specifying the repository key.")*, *[substructureFile](#abaqus.Part.PartBase.PartBase.PartFromSubstructure.substructureFile "abaqus.Part.PartBase.PartBase.PartFromSubstructure.substructureFile (Python parameter) — A substructure sim file.")*, *[odbFile](#abaqus.Part.PartBase.PartBase.PartFromSubstructure.odbFile "abaqus.Part.PartBase.PartBase.PartFromSubstructure.odbFile (Python parameter) — The output database file corresponding to the substructure sim file.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L785-L823)[¶](#abaqus.Part.PartBase.PartBase.PartFromSubstructure "Permalink to this definition")
    :   This method creates a substructure Part object by reading a substructure sim file and places it in
        the parts repository.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].PartFromSubstructure
        ```

        Note

        Check [PartFromSubstructure on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partfromsubstructurepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.PartFromSubstructure-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Part.PartBase.PartBase.PartFromSubstructure.name "Permalink to this definition")
            :   A String specifying the repository key.

            substructureFile[¶](#abaqus.Part.PartBase.PartBase.PartFromSubstructure.substructureFile "Permalink to this definition")
            :   A substructure sim file.

            odbFile[¶](#abaqus.Part.PartBase.PartBase.PartFromSubstructure.odbFile "Permalink to this definition")
            :   The output database file corresponding to the substructure sim file.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.PartFromSubstructure-returns "Permalink to this headline")
        :   **part** – A Part object

        Return type:[¶](#abaqus.Part.PartBase.PartBase.PartFromSubstructure-return-type "Permalink to this headline")
        :   `Part`

        Raises:[¶](#abaqus.Part.PartBase.PartBase.PartFromSubstructure-raises "Permalink to this headline")
        :   * [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.13)") – If the specified part is not a substructure,
              File specified does not contain a substructure.
            * [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.13)") – If the specified part already exists,
              A part with the same name already exists.
            * [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.13)") – If the substructure cannot be imported,
              The output database is missing nodes and elements.Nested substructures are not
              supported.The substructure sim file was generated using a version that is different from
              the current version.

    Unlock()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1835-L1841)[¶](#abaqus.Part.PartBase.PartBase.Unlock "Permalink to this definition")
    :   This method unlocks the part.

        Unlocking the part allows it to be regenerated after any modifications to the part.

    addGeomToSketch(*[sketch](#abaqus.Part.PartBase.PartBase.addGeomToSketch.sketch "abaqus.Part.PartBase.PartBase.addGeomToSketch.sketch (Python parameter) — A ConstrainedSketch object.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L887-L897)[¶](#abaqus.Part.PartBase.PartBase.addGeomToSketch "Permalink to this definition")
    :   This method converts a part into a sketch by projecting all of the edges of the part onto the X-Y
        plane of the sketch. You can use addGeomToSketch with a part of any modeling space.

        Note

        Check [PartBase.addGeomToSketch on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partaddgeomtosketchpyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.addGeomToSketch-parameters "Permalink to this headline")
        :   sketch[¶](#abaqus.Part.PartBase.PartBase.addGeomToSketch.sketch "Permalink to this definition")
            :   A ConstrainedSketch object.

    allInternalSets : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Region.Set.Set`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L139-L140)[¶](#abaqus.Part.PartBase.PartBase.allInternalSets "Permalink to this definition")
    :   A repository of Set objects specifying picked regions.

    allInternalSurfaces : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Region.Surface.Surface`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L149-L150)[¶](#abaqus.Part.PartBase.PartBase.allInternalSurfaces "Permalink to this definition")
    :   A repository of Surface objects specifying picked regions.

    allSets : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Region.Set.Set`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L135-L137)[¶](#abaqus.Part.PartBase.PartBase.allSets "Permalink to this definition")
    :   A repository of Set objects specifying the contents of the **allSets** repository is the
        same as the contents of the **sets** repository.

    allSurfaces : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Region.Surface.Surface`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L145-L147)[¶](#abaqus.Part.PartBase.PartBase.allSurfaces "Permalink to this definition")
    :   A repository of Surface objects specifying the contents of the **allSurfaces** repository
        is the same as the contents of the **surfaces** repository.

    assignThickness(*[faces](#abaqus.Part.PartBase.PartBase.assignThickness.faces "abaqus.Part.PartBase.PartBase.assignThickness.faces (Python parameter) — A sequence of Face objects specifying the regions where thickness will be applied.")*, *[thickness](#abaqus.Part.PartBase.PartBase.assignThickness.thickness "abaqus.Part.PartBase.PartBase.assignThickness.thickness (Python parameter) — A Float specifying the thickness along the given faces .")=`None`*, *[topFaces](#abaqus.Part.PartBase.PartBase.assignThickness.topFaces "abaqus.Part.PartBase.PartBase.assignThickness.topFaces (Python parameter) — A sequence of Face objects whose distance to faces argument is used to calculate the thickness along the faces.")=`()`*, *[bottomFaces](#abaqus.Part.PartBase.PartBase.assignThickness.bottomFaces "abaqus.Part.PartBase.PartBase.assignThickness.bottomFaces (Python parameter) — A sequence of Face objects whose distance to faces is used to calculate the thickness along the faces.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L899-L932)[¶](#abaqus.Part.PartBase.PartBase.assignThickness "Permalink to this definition")
    :   This method assigns thickness data to shell faces. The thickness can be used while assigning shell
        and membrane sections to faces.

        Note

        Check [PartBase.assignThickness on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partassignthicknesspyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.assignThickness-parameters "Permalink to this headline")
        :   faces[¶](#abaqus.Part.PartBase.PartBase.assignThickness.faces "Permalink to this definition")
            :   A sequence of Face objects specifying the regions where thickness will be applied.

            thickness=`None`[¶](#abaqus.Part.PartBase.PartBase.assignThickness.thickness "Permalink to this definition")
            :   A Float specifying the thickness along the given **faces** . Either **thickness**,
                **topFaces**, or **bottomFaces** must be specified.

            topFaces=`()`[¶](#abaqus.Part.PartBase.PartBase.assignThickness.topFaces "Permalink to this definition")
            :   A sequence of Face objects whose distance to **faces** argument is used to calculate the
                thickness along the **faces**. The combination of **topFaces** and **bottomFaces** determines
                the thickness and the offset of the elements. If **bottomFaces** is not specified then the
                thickness is twice the distance to the **topFaces**. This argument will be ignored if
                **thickness** is specified. Either **thickness**, **topFaces**, or **bottomFaces** must be
                specified.

            bottomFaces=`()`[¶](#abaqus.Part.PartBase.PartBase.assignThickness.bottomFaces "Permalink to this definition")
            :   A sequence of Face objects whose distance to **faces** is used to calculate the thickness
                along the **faces**. The combination of **topFaces** and **bottomFaces** determines the
                thickness and the offset of the elements. If **topFaces** is not specified then the
                thickness is twice the distance to the **bottomFaces**. This argument will be ignored if
                **thickness** is specified. Either **thickness**, **topFaces**, or **bottomFaces** must be
                specified.

    backup()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L934-L940)[¶](#abaqus.Part.PartBase.PartBase.backup "Permalink to this definition")
    :   This method makes a backup copy of the features in the part.

        Use the restore method to retrieve the part’s features from the backup.

    cells : --is-rst--:py:class:`~abaqus.BasicGeometry.CellArray.CellArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L98-L99)[¶](#abaqus.Part.PartBase.PartBase.cells "Permalink to this definition")
    :   A CellArray object specifying all the cells in the part.

    checkGeometry(*[detailed](#abaqus.Part.PartBase.PartBase.checkGeometry.detailed "abaqus.Part.PartBase.PartBase.checkGeometry.detailed (Python parameter) — A Boolean specifying whether detailed output will be printed to the replay file.")=`0`*, *[reportFacetErrors](#abaqus.Part.PartBase.PartBase.checkGeometry.reportFacetErrors "abaqus.Part.PartBase.PartBase.checkGeometry.reportFacetErrors (Python parameter) — A Boolean specifying whether faces are checked for proper facetting.")=`0`*, *[level](#abaqus.Part.PartBase.PartBase.checkGeometry.level "abaqus.Part.PartBase.PartBase.checkGeometry.level (Python parameter) — An Int specifying which level of checking is performed.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L942-L966)[¶](#abaqus.Part.PartBase.PartBase.checkGeometry "Permalink to this definition")
    :   This method checks the validity of the geometry of the part and prints a count of all topological
        entities on the part (faces, edges, vertices, etc.).

        Note

        Check [PartBase.checkGeometry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partcheckgeometrypyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.checkGeometry-parameters "Permalink to this headline")
        :   detailed=`0`[¶](#abaqus.Part.PartBase.PartBase.checkGeometry.detailed "Permalink to this definition")
            :   A Boolean specifying whether detailed output will be printed to the replay file. The
                default value is OFF.

            reportFacetErrors=`0`[¶](#abaqus.Part.PartBase.PartBase.checkGeometry.reportFacetErrors "Permalink to this definition")
            :   A Boolean specifying whether faces are checked for proper facetting. The default value
                is OFF.

            level=`None`[¶](#abaqus.Part.PartBase.PartBase.checkGeometry.level "Permalink to this definition")
            :   An Int specifying which level of checking is performed. Values can range from 20 to 70,
                with higher values reporting less and less important errors. The default value is 20,
                which reports all critical errors. When the default value is used, the stored validity
                status is updated to agree with the result of this check.

    clearGeometryCache()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L968-L974)[¶](#abaqus.Part.PartBase.PartBase.clearGeometryCache "Permalink to this definition")
    :   This method clears the geometry cache.

        Clearing the geometry cache reduces the amount of memory being used to cache part features.

    compositeLayups : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Property.CompositeLayup.CompositeLayup`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L170-L171)[¶](#abaqus.Part.PartBase.PartBase.compositeLayups "Permalink to this definition")
    :   A repository of CompositeLayup objects.

    copyMeshPattern(*[elements](#abaqus.Part.PartBase.PartBase.copyMeshPattern.elements "abaqus.Part.PartBase.PartBase.copyMeshPattern.elements (Python parameter) — A sequence of MeshElement objects or a Set object containing elements and specifying the source region.")*, *[faces](#abaqus.Part.PartBase.PartBase.copyMeshPattern.faces "abaqus.Part.PartBase.PartBase.copyMeshPattern.faces (Python parameter) — A sequence of Face objects that have associated with shell elements or element faces and specifying the source region.")*, *[elemFaces](#abaqus.Part.PartBase.PartBase.copyMeshPattern.elemFaces "abaqus.Part.PartBase.PartBase.copyMeshPattern.elemFaces (Python parameter) — A sequence of MeshFace objects specifying the source region.")*, *[targetFace](#abaqus.Part.PartBase.PartBase.copyMeshPattern.targetFace "abaqus.Part.PartBase.PartBase.copyMeshPattern.targetFace (Python parameter) — A MeshFace object specifying the target region.")*, *[nodes](#abaqus.Part.PartBase.PartBase.copyMeshPattern.nodes "abaqus.Part.PartBase.PartBase.copyMeshPattern.nodes (Python parameter) — A sequence of MeshNode objects or a Set object containing nodes on the boundary of source region which are to be positioned to the boundary of target face.")*, *[coordinates](#abaqus.Part.PartBase.PartBase.copyMeshPattern.coordinates "abaqus.Part.PartBase.PartBase.copyMeshPattern.coordinates (Python parameter) — A sequence of three-dimensional coordinate tuples specifying the coordinates for each of the given nodes.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1777-L1813)[¶](#abaqus.Part.PartBase.PartBase.copyMeshPattern "Permalink to this definition")
    :   This method copies a mesh pattern from a source region consisting of a set of shell elements or
        element faces onto a target face, mapping nodes and elements in a one-one correspondence between source
        and target.

        Note

        Check [PartBase.copyMeshPattern on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partcopymeshpatternpyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.copyMeshPattern-parameters "Permalink to this headline")
        :   elements[¶](#abaqus.Part.PartBase.PartBase.copyMeshPattern.elements "Permalink to this definition")
            :   A sequence of MeshElement objects or a Set object containing elements and specifying the
                source region.

            faces[¶](#abaqus.Part.PartBase.PartBase.copyMeshPattern.faces "Permalink to this definition")
            :   A sequence of Face objects that have associated with shell elements or element faces and
                specifying the source region.

            elemFaces[¶](#abaqus.Part.PartBase.PartBase.copyMeshPattern.elemFaces "Permalink to this definition")
            :   A sequence of MeshFace objects specifying the source region.

            targetFace[¶](#abaqus.Part.PartBase.PartBase.copyMeshPattern.targetFace "Permalink to this definition")
            :   A MeshFace object specifying the target region.

            nodes[¶](#abaqus.Part.PartBase.PartBase.copyMeshPattern.nodes "Permalink to this definition")
            :   A sequence of MeshNode objects or a Set object containing nodes on the boundary of
                source region which are to be positioned to the boundary of target face.

            coordinates[¶](#abaqus.Part.PartBase.PartBase.copyMeshPattern.coordinates "Permalink to this definition")
            :   A sequence of three-dimensional coordinate tuples specifying the coordinates for each of
                the given nodes. When specified, the number of coordinate tuples must match the number
                of given nodes, and be ordered to correspond to the given nodes in *ascending order*
                according to index. These coordinates are positions of the nodes of a mesh that will be
                the target face corresponding to nodes provided.

    datums : --is-rst--:py:class:`dict`\[:py:class:`int`, :py:class:`~abaqus.Datum.Datum.Datum`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L111-L112)[¶](#abaqus.Part.PartBase.PartBase.datums "Permalink to this definition")
    :   A repository of Datum objects specifying all the datums in the part.

    deleteAllFeatures()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L976-L979)[¶](#abaqus.Part.PartBase.PartBase.deleteAllFeatures "Permalink to this definition")
    :   This method deletes all the features in the part.

    deleteFeatures(*[featureNames](#abaqus.Part.PartBase.PartBase.deleteFeatures.featureNames "abaqus.Part.PartBase.PartBase.deleteFeatures.featureNames (Python parameter) — A sequence of Strings specifying the feature names that will be deleted from the part.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L981-L990)[¶](#abaqus.Part.PartBase.PartBase.deleteFeatures "Permalink to this definition")
    :   This method deletes the given features.

        Note

        Check [PartBase.deleteFeatures on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partdeletefeaturespyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.deleteFeatures-parameters "Permalink to this headline")
        :   featureNames[¶](#abaqus.Part.PartBase.PartBase.deleteFeatures.featureNames "Permalink to this definition")
            :   A sequence of Strings specifying the feature names that will be deleted from the part.

    edges : --is-rst--:py:class:`~abaqus.BasicGeometry.EdgeArray.EdgeArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L89-L90)[¶](#abaqus.Part.PartBase.PartBase.edges "Permalink to this definition")
    :   An EdgeArray object specifying all the edges in the part.

    elemEdges : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Mesh.MeshEdge.MeshEdge`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L173-L178)[¶](#abaqus.Part.PartBase.PartBase.elemEdges "Permalink to this definition")
    :   A repository of MeshEdge objects specifying all the element edges in the part. For a
        given element and a given edge index on a given face within that element, the
        corresponding MeshEdge object can be retrieved from the repository by using the key
        calculated as (i\*32 + j\*4 + k), where i, j, and k are zero-based element, face, and edge
        indices, respectively.

    elemFaces : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Mesh.MeshFace.MeshFace`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L117-L121)[¶](#abaqus.Part.PartBase.PartBase.elemFaces "Permalink to this definition")
    :   A repository of MeshFace objects specifying all the element faces in the part. For a
        given element and a given face index within that element, the corresponding MeshFace
        object can be retrieved from the repository by using the key calculated as (i\*8 + j),
        where i and j are zero-based element and face indices, respectively.

    elementEdges : --is-rst--:py:class:`~abaqus.Mesh.MeshEdgeArray.MeshEdgeArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L180-L181)[¶](#abaqus.Part.PartBase.PartBase.elementEdges "Permalink to this definition")
    :   A MeshEdgeArray object specifying all the unique element edges in the part.

    elementFaces : --is-rst--:py:class:`~abaqus.Mesh.MeshFaceArray.MeshFaceArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L123-L124)[¶](#abaqus.Part.PartBase.PartBase.elementFaces "Permalink to this definition")
    :   A MeshFaceArray object specifying all the unique element faces in the part.

    elements : --is-rst--:py:class:`~abaqus.Mesh.MeshElementArray.MeshElementArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L114-L115)[¶](#abaqus.Part.PartBase.PartBase.elements "Permalink to this definition")
    :   A MeshElementArray object specifying all the elements in the part.

    engineeringFeatures : --is-rst--:py:class:`~abaqus.EngineeringFeature.EngineeringFeature.EngineeringFeature` = `<abaqus.EngineeringFeature.EngineeringFeature.EngineeringFeature object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L161-L162)[¶](#abaqus.Part.PartBase.PartBase.engineeringFeatures "Permalink to this definition")
    :   An EngineeringFeature object.

    faces : --is-rst--:py:class:`~abaqus.BasicGeometry.FaceArray.FaceArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L95-L96)[¶](#abaqus.Part.PartBase.PartBase.faces "Permalink to this definition")
    :   A FaceArray object specifying all the faces in the part.

    features : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Part.PartFeature.PartFeature`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L101-L102)[¶](#abaqus.Part.PartBase.PartBase.features "Permalink to this definition")
    :   A repository of Feature objects specifying all the features in the part.

    featuresById : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Part.PartFeature.PartFeature`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L104-L109)[¶](#abaqus.Part.PartBase.PartBase.featuresById "Permalink to this definition")
    :   A repository of Feature objects specifying all Feature objects in the part. The Feature
        objects in the featuresById repository are the same as the Feature objects in the
        features’ repository. However, the key to the objects in the featuresById repository is
        an integer specifying the **ID**, whereas the key to the objects in the features
        repository is a string specifying the **name**.

    geometryValidity : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L71-L74)[¶](#abaqus.Part.PartBase.PartBase.geometryValidity "Permalink to this definition")
    :   A Boolean specifying the validity of the geometry of the part. The value is computed,
        but it can be set to ON to perform feature and mesh operations on an invalid part. There
        is no guarantee that such operations will work if the part was originally invalid.

    getAngle(*[plane1](#abaqus.Part.PartBase.PartBase.getAngle.plane1 "abaqus.Part.PartBase.PartBase.getAngle.plane1 (Python parameter) — A Face, MeshFace, or a Datum object specifying the first plane.")*, *[plane2](#abaqus.Part.PartBase.PartBase.getAngle.plane2 "abaqus.Part.PartBase.PartBase.getAngle.plane2 (Python parameter) — A Face, MeshFace, or a Datum object specifying the second plane.")*, *[line1](#abaqus.Part.PartBase.PartBase.getAngle.line1 "abaqus.Part.PartBase.PartBase.getAngle.line1 (Python parameter) — An Edge, MeshEdge, or a Datum object specifying the first curve.")*, *[line2](#abaqus.Part.PartBase.PartBase.getAngle.line2 "abaqus.Part.PartBase.PartBase.getAngle.line2 (Python parameter) — An Edge, MeshEdge, or a Datum object specifying the second curve.")*, *[commonVertex](#abaqus.Part.PartBase.PartBase.getAngle.commonVertex "abaqus.Part.PartBase.PartBase.getAngle.commonVertex (Python parameter) — If the two selected Edge objects have more than one vertex in common, this ConstrainedSketchVertex object specifies the vertex at which to evaluate the angle.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L992-L1024)[¶](#abaqus.Part.PartBase.PartBase.getAngle "Permalink to this definition")
    :   This method returns the angle between the specified entities.

        Note

        Check [PartBase.getAngle on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partgetanglepyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.getAngle-parameters "Permalink to this headline")
        :   plane1[¶](#abaqus.Part.PartBase.PartBase.getAngle.plane1 "Permalink to this definition")
            :   A Face, MeshFace, or a Datum object specifying the first plane. The Datum object must
                represent a datum plane. The **plane1** and **line1** arguments are mutually exclusive. One
                of them must be specified.

            plane2[¶](#abaqus.Part.PartBase.PartBase.getAngle.plane2 "Permalink to this definition")
            :   A Face, MeshFace, or a Datum object specifying the second plane. The Datum object must
                represent a datum plane. The **plane2** and **line2** arguments are mutually exclusive. One
                of them must be specified.

            line1[¶](#abaqus.Part.PartBase.PartBase.getAngle.line1 "Permalink to this definition")
            :   An Edge, MeshEdge, or a Datum object specifying the first curve. The Datum object must
                represent a datum axis. The **plane1** and **line1** arguments are mutually exclusive. One
                of them must be specified.

            line2[¶](#abaqus.Part.PartBase.PartBase.getAngle.line2 "Permalink to this definition")
            :   An Edge, MeshEdge, or a Datum object specifying the second curve. The Datum object must
                represent a datum axis. The **plane2** and **line2** arguments are mutually exclusive. One
                of them must be specified.

            commonVertex=`''`[¶](#abaqus.Part.PartBase.PartBase.getAngle.commonVertex "Permalink to this definition")
            :   If the two selected Edge objects have more than one vertex in common, this ConstrainedSketchVertex object
                specifies the vertex at which to evaluate the angle.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.getAngle-returns "Permalink to this headline")
        :   **angle** – A Float specifying the angle between the specified entities. If you provide a plane as
            an argument, Abaqus/CAE computes the angle using the normal to the plane.

        Return type:[¶](#abaqus.Part.PartBase.PartBase.getAngle-return-type "Permalink to this headline")
        :   [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")

    getArea(*[faces](#abaqus.Part.PartBase.PartBase.getArea.faces "abaqus.Part.PartBase.PartBase.getArea.faces (Python parameter) — A sequence of Face objects whose area the method will calculate.")*, *[relativeAccuracy](#abaqus.Part.PartBase.PartBase.getArea.relativeAccuracy "abaqus.Part.PartBase.PartBase.getArea.relativeAccuracy (Python parameter) — A Float specifying that the area computation should stop when the specified relative accuracy has been achieved.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1026-L1043)[¶](#abaqus.Part.PartBase.PartBase.getArea "Permalink to this definition")
    :   This method returns the total surface area of a given face or group of faces.

        Note

        Check [PartBase.getArea on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partgetareapyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.getArea-parameters "Permalink to this headline")
        :   faces[¶](#abaqus.Part.PartBase.PartBase.getArea.faces "Permalink to this definition")
            :   A sequence of Face objects whose area the method will calculate.

            relativeAccuracy=`0`[¶](#abaqus.Part.PartBase.PartBase.getArea.relativeAccuracy "Permalink to this definition")
            :   A Float specifying that the area computation should stop when the specified relative
                accuracy has been achieved. The default value is 0.000001 (0.0001%).

        Returns:[¶](#abaqus.Part.PartBase.PartBase.getArea-returns "Permalink to this headline")
        :   **area** – A Float specifying the sum of the calculated areas of the given faces.

        Return type:[¶](#abaqus.Part.PartBase.PartBase.getArea-return-type "Permalink to this headline")
        :   [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")

    getAssociatedCADPaths()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1045-L1056)[¶](#abaqus.Part.PartBase.PartBase.getAssociatedCADPaths "Permalink to this definition")
    :   This method returns the paths to the associated CAD part and root file. These are only available if
        the part was imported from one of the supported CAD softwares using the Associative Import capability.
        The root file can be the assembly file or the part file, depending on what which one was imported.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.getAssociatedCADPaths-returns "Permalink to this headline")
        :   **paths** – A sequence containing the path to the associated CAD part and assembly file

        Return type:[¶](#abaqus.Part.PartBase.PartBase.getAssociatedCADPaths-return-type "Permalink to this headline")
        :   [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")

    getCADParameters()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1058-L1071)[¶](#abaqus.Part.PartBase.PartBase.getCADParameters "Permalink to this definition")
    :   This method returns the names and values of the CAD parameters associated with the part. These are
        only available if the part was imported from one of the supported CAD softwares using the Associative
        Import capability, and if the parameter names defined in that CAD software are prefixed with the string
        ABQ.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.getCADParameters-returns "Permalink to this headline")
        :   **paras** – A dictionary object representing a map of the name of the parameter and its associated
            value.

        Return type:[¶](#abaqus.Part.PartBase.PartBase.getCADParameters-return-type "Permalink to this headline")
        :   [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")

    getCentroid(*[faces](#abaqus.Part.PartBase.PartBase.getCentroid.faces "abaqus.Part.PartBase.PartBase.getCentroid.faces (Python parameter) — A sequence of Face objects whose centroid the method will calculate.")*, *[cells](#abaqus.Part.PartBase.PartBase.getCentroid.cells "abaqus.Part.PartBase.PartBase.getCentroid.cells (Python parameter) — A sequence of Face objects whose centroid the method will calculate.")*, *[relativeAccuracy](#abaqus.Part.PartBase.PartBase.getCentroid.relativeAccuracy "abaqus.Part.PartBase.PartBase.getCentroid.relativeAccuracy (Python parameter) — A Float specifying that the centroid computation should stop when the specified relative accuracy has been achieved.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1073-L1098)[¶](#abaqus.Part.PartBase.PartBase.getCentroid "Permalink to this definition")
    :   Location of the centroid of a given face/cell or group of faces/cells.

        Note

        Check [PartBase.getCentroid on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partgetcentroidpyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.getCentroid-parameters "Permalink to this headline")
        :   faces[¶](#abaqus.Part.PartBase.PartBase.getCentroid.faces "Permalink to this definition")
            :   A sequence of Face objects whose centroid the method will calculate. The arguments
                **faces** and **cells** are mutually exclusive.

            cells[¶](#abaqus.Part.PartBase.PartBase.getCentroid.cells "Permalink to this definition")
            :   A sequence of Face objects whose centroid the method will calculate. The arguments
                **faces** and **cells** are mutually exclusive.

            relativeAccuracy=`0`[¶](#abaqus.Part.PartBase.PartBase.getCentroid.relativeAccuracy "Permalink to this definition")
            :   A Float specifying that the centroid computation should stop when the specified relative
                accuracy has been achieved. The default value is 0.000001 (0.0001%).

        Returns:[¶](#abaqus.Part.PartBase.PartBase.getCentroid-returns "Permalink to this headline")
        :   **centroid** – A sequence of Floats specifying the **X**, **Y**, and **Z** coordinates of the centroid.
            Depending on the arguments provided, this method returns the following:

            * The location of the centroid of a given face or group of faces.
            * The location of the centroid of a given cell or group of cells.

        Return type:[¶](#abaqus.Part.PartBase.PartBase.getCentroid-return-type "Permalink to this headline")
        :   `Sequence[float]`

    getCoordinates(*[entity](#abaqus.Part.PartBase.PartBase.getCoordinates.entity "abaqus.Part.PartBase.PartBase.getCoordinates.entity (Python parameter) — A ConstrainedSketchVertex, Datum point, MeshNode, or ReferencePoint specifying the entity to query.")*, *[csys](#abaqus.Part.PartBase.PartBase.getCoordinates.csys "abaqus.Part.PartBase.PartBase.getCoordinates.csys (Python parameter) — A DatumCsys object specifying the desired coordinate system of the returned coordinates.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1100-L1119)[¶](#abaqus.Part.PartBase.PartBase.getCoordinates "Permalink to this definition")
    :   This method returns the coordinates of specified point.

        Note

        Check [PartBase.getCoordinates on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partgetcoordinatespyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.getCoordinates-parameters "Permalink to this headline")
        :   entity[¶](#abaqus.Part.PartBase.PartBase.getCoordinates.entity "Permalink to this definition")
            :   A ConstrainedSketchVertex, Datum point, MeshNode, or ReferencePoint specifying the entity to query.

            csys[¶](#abaqus.Part.PartBase.PartBase.getCoordinates.csys "Permalink to this definition")
            :   A DatumCsys object specifying the desired coordinate system of the returned
                coordinates. By default, coordinates are given in the global coordinate system.

                New in version 2022: The `csys` argument was added.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.getCoordinates-returns "Permalink to this headline")
        :   A tuple of 3 Floats representing the coordinates of the specified point.

    getCurvature(*[edges](#abaqus.Part.PartBase.PartBase.getCurvature.edges "abaqus.Part.PartBase.PartBase.getCurvature.edges (Python parameter) — A sequence of Edge objects whose curvature the method will calculate.")*, *[samplePoints](#abaqus.Part.PartBase.PartBase.getCurvature.samplePoints "abaqus.Part.PartBase.PartBase.getCurvature.samplePoints (Python parameter) — An Int specifying the number of points along each edge at which the curvature will be computed.")=`100`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1121-L1142)[¶](#abaqus.Part.PartBase.PartBase.getCurvature "Permalink to this definition")
    :   This method returns the maximum curvature of a given edge or group of edges. For an arc, the
        curvature is constant over the entire edge, and equal to the inverse of the radius. For a straight line,
        the curvature is constant and equal to 0. For a spline edge, the curvature varies over a range, and this
        methods computes the maximum.

        Note

        Check [PartBase.getCurvature on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partgetcurvaturepyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.getCurvature-parameters "Permalink to this headline")
        :   edges[¶](#abaqus.Part.PartBase.PartBase.getCurvature.edges "Permalink to this definition")
            :   A sequence of Edge objects whose curvature the method will calculate.

            samplePoints=`100`[¶](#abaqus.Part.PartBase.PartBase.getCurvature.samplePoints "Permalink to this definition")
            :   An Int specifying the number of points along each edge at which the curvature will be
                computed. The higher the number of sample points, the better the accuracy of the
                computation. The default value is 100.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.getCurvature-returns "Permalink to this headline")
        :   **curvature** – A Float specifying the maximum curvature.

        Return type:[¶](#abaqus.Part.PartBase.PartBase.getCurvature-return-type "Permalink to this headline")
        :   [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")

    getDistance(*[entity1](#abaqus.Part.PartBase.PartBase.getDistance.entity1 "abaqus.Part.PartBase.PartBase.getDistance.entity1 (Python parameter) — A ConstrainedSketchVertex, Datum point, MeshNode, or Edge specifying the first entity from which to measure.")*, *[entity2](#abaqus.Part.PartBase.PartBase.getDistance.entity2 "abaqus.Part.PartBase.PartBase.getDistance.entity2 (Python parameter) — A ConstrainedSketchVertex, Datum point, MeshNode, or Edge specifying the second entity to which to measure.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1144-L1166)[¶](#abaqus.Part.PartBase.PartBase.getDistance "Permalink to this definition")
    :   Depending on the arguments provided, this method returns one of the following:

        * The distance between two points.
        * The minimum distance between a point and an edge.
        * The minimum distance between two edges.

        Note

        Check [PartBase.getDistance on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partgetdistancepyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.getDistance-parameters "Permalink to this headline")
        :   entity1[¶](#abaqus.Part.PartBase.PartBase.getDistance.entity1 "Permalink to this definition")
            :   A ConstrainedSketchVertex, Datum point, MeshNode, or Edge specifying the first entity from which to
                measure.

            entity2[¶](#abaqus.Part.PartBase.PartBase.getDistance.entity2 "Permalink to this definition")
            :   A ConstrainedSketchVertex, Datum point, MeshNode, or Edge specifying the second entity to which to
                measure.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.getDistance-returns "Permalink to this headline")
        :   **distance** – A Float specifying the distance between **entity1** and **entity2**.

        Return type:[¶](#abaqus.Part.PartBase.PartBase.getDistance-return-type "Permalink to this headline")
        :   [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")

    getFeatureCells(*[name](#abaqus.Part.PartBase.PartBase.getFeatureCells.name "abaqus.Part.PartBase.PartBase.getFeatureCells.name (Python parameter) — A string specifying the feature name.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1385-L1405)[¶](#abaqus.Part.PartBase.PartBase.getFeatureCells "Permalink to this definition")
    :   This method returns a sequence of Cell objects that are created by the given feature.

        Note

        Check [PartBase.getFeatureCells on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partgetfeaturecellspyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.getFeatureCells-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Part.PartBase.PartBase.getFeatureCells.name "Permalink to this definition")
            :   A string specifying the feature name.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.getFeatureCells-returns "Permalink to this headline")
        :   **cells** – Sequence of Cell objects.

        Return type:[¶](#abaqus.Part.PartBase.PartBase.getFeatureCells-return-type "Permalink to this headline")
        :   `Sequence[Cell]`

        Raises:[¶](#abaqus.Part.PartBase.PartBase.getFeatureCells-raises "Permalink to this headline")
        :   **Error** – Incorrect feature name,
            An exception occurs if a feature with the given name does not exist.

    getFeatureEdges(*[name](#abaqus.Part.PartBase.PartBase.getFeatureEdges.name "abaqus.Part.PartBase.PartBase.getFeatureEdges.name (Python parameter) — A string specifying the feature name.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1364-L1383)[¶](#abaqus.Part.PartBase.PartBase.getFeatureEdges "Permalink to this definition")
    :   This method returns a sequence of Edge objects that are created by the given feature.

        Note

        Check [PartBase.getFeatureEdges on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partgetfeatureedgespyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.getFeatureEdges-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Part.PartBase.PartBase.getFeatureEdges.name "Permalink to this definition")
            :   A string specifying the feature name.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.getFeatureEdges-returns "Permalink to this headline")
        :   **edges** – Sequence of Edge objects.

        Return type:[¶](#abaqus.Part.PartBase.PartBase.getFeatureEdges-return-type "Permalink to this headline")
        :   `Sequence[Edge]`

        Raises:[¶](#abaqus.Part.PartBase.PartBase.getFeatureEdges-raises "Permalink to this headline")
        :   **Error** – Incorrect feature name, An exception occurs if a feature with the given name does not exist.

    getFeatureFaces(*[name](#abaqus.Part.PartBase.PartBase.getFeatureFaces.name "abaqus.Part.PartBase.PartBase.getFeatureFaces.name (Python parameter) — A string specifying the feature name.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1342-L1362)[¶](#abaqus.Part.PartBase.PartBase.getFeatureFaces "Permalink to this definition")
    :   This method returns a sequence of Face objects that are created by the given feature.

        Note

        Check [PartBase.getFeatureFaces on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partgetfeaturefacespyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.getFeatureFaces-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Part.PartBase.PartBase.getFeatureFaces.name "Permalink to this definition")
            :   A string specifying the feature name.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.getFeatureFaces-returns "Permalink to this headline")
        :   **faces** – Sequence of Face objects.

        Return type:[¶](#abaqus.Part.PartBase.PartBase.getFeatureFaces-return-type "Permalink to this headline")
        :   `Sequence[Face]`

        Raises:[¶](#abaqus.Part.PartBase.PartBase.getFeatureFaces-raises "Permalink to this headline")
        :   **Error** – Incorrect feature name,
            An exception occurs if a feature with the given name does not exist.

    getFeatureVertices(*[name](#abaqus.Part.PartBase.PartBase.getFeatureVertices.name "abaqus.Part.PartBase.PartBase.getFeatureVertices.name (Python parameter) — A string specifying the feature name.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1407-L1427)[¶](#abaqus.Part.PartBase.PartBase.getFeatureVertices "Permalink to this definition")
    :   This method returns a sequence of ConstrainedSketchVertex objects that are created by the given
        feature.

        Note

        Check [PartBase.getFeatureVertices on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partgetfeatureverticespyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.getFeatureVertices-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Part.PartBase.PartBase.getFeatureVertices.name "Permalink to this definition")
            :   A string specifying the feature name.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.getFeatureVertices-returns "Permalink to this headline")
        :   **vertices** – Sequence of ConstrainedSketchVertex objects.

        Return type:[¶](#abaqus.Part.PartBase.PartBase.getFeatureVertices-return-type "Permalink to this headline")
        :   `Sequence[ConstrainedSketchVertex]`

        Raises:[¶](#abaqus.Part.PartBase.PartBase.getFeatureVertices-raises "Permalink to this headline")
        :   **Error** – Incorrect feature name, An exception occurs if a feature with the given name does not exist.

    getLength(*[edges](#abaqus.Part.PartBase.PartBase.getLength.edges "abaqus.Part.PartBase.PartBase.getLength.edges (Python parameter) — A sequence of Edge objects whose total length the method will calculate.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1168-L1182)[¶](#abaqus.Part.PartBase.PartBase.getLength "Permalink to this definition")
    :   This method returns the length of a given edge or group of edges.

        Note

        Check [PartBase.getLength on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partgetlengthpyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.getLength-parameters "Permalink to this headline")
        :   edges[¶](#abaqus.Part.PartBase.PartBase.getLength.edges "Permalink to this definition")
            :   A sequence of Edge objects whose total length the method will calculate.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.getLength-returns "Permalink to this headline")
        :   **length** – A Float specifying the total length

        Return type:[¶](#abaqus.Part.PartBase.PartBase.getLength-return-type "Permalink to this headline")
        :   [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")

    getMassProperties(*[regions](#abaqus.Part.PartBase.PartBase.getMassProperties.regions "abaqus.Part.PartBase.PartBase.getMassProperties.regions (Python parameter) — A MeshElementArray, CellArray, FaceArray, or EdgeArray specifying the regions whose mass properties are to be queried.")=`''`*, *[relativeAccuracy](#abaqus.Part.PartBase.PartBase.getMassProperties.relativeAccuracy "abaqus.Part.PartBase.PartBase.getMassProperties.relativeAccuracy (Python parameter) — A SymbolicConstant specifying the relative accuracy for geometry computation.")=`abaqusConstants.LOW`*, *[useMesh](#abaqus.Part.PartBase.PartBase.getMassProperties.useMesh "abaqus.Part.PartBase.PartBase.getMassProperties.useMesh (Python parameter) — A Boolean specifying whether the mesh should be used in the computation if the geometry is meshed.")=`False`*, *[specifyDensity](#abaqus.Part.PartBase.PartBase.getMassProperties.specifyDensity "abaqus.Part.PartBase.PartBase.getMassProperties.specifyDensity (Python parameter) — A Boolean specifying whether a user-specified density should be used in regions with density errors such as undefined material density.")=`False`*, *[density](#abaqus.Part.PartBase.PartBase.getMassProperties.density "abaqus.Part.PartBase.PartBase.getMassProperties.density (Python parameter) — A double value specifying the user-specified density value to be used in regions with density errors.")=`''`*, *[specifyThickness](#abaqus.Part.PartBase.PartBase.getMassProperties.specifyThickness "abaqus.Part.PartBase.PartBase.getMassProperties.specifyThickness (Python parameter) — A Boolean specifying whether a user-specified thickness should be used in regions with thickness errors such as undefined thickness.")=`False`*, *[thickness](#abaqus.Part.PartBase.PartBase.getMassProperties.thickness "abaqus.Part.PartBase.PartBase.getMassProperties.thickness (Python parameter) — A double value specifying the user-specified thickness value to be used in regions with thickness errors.")=`''`*, *[miAboutCenterOfMass](#abaqus.Part.PartBase.PartBase.getMassProperties.miAboutCenterOfMass "abaqus.Part.PartBase.PartBase.getMassProperties.miAboutCenterOfMass (Python parameter) — A Boolean specifying if the moments of inertia should be evaluated about the center of mass.")=`True`*, *[miAboutPoint](#abaqus.Part.PartBase.PartBase.getMassProperties.miAboutPoint "abaqus.Part.PartBase.PartBase.getMassProperties.miAboutPoint (Python parameter) — A tuple of three floats specifying the coordinates of the point about which to evaluate the moment of inertia.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1221-L1340)[¶](#abaqus.Part.PartBase.PartBase.getMassProperties "Permalink to this definition")
    :   This method returns the mass properties of a part or region. Only beams, trusses, shells, solids,
        point, nonstructural mass, and rotary inertia elements are supported.

        Note

        Check [PartBase.getMassProperties on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partgetmasspropertiespyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.getMassProperties-parameters "Permalink to this headline")
        :   regions=`''`[¶](#abaqus.Part.PartBase.PartBase.getMassProperties.regions "Permalink to this definition")
            :   A MeshElementArray, CellArray, FaceArray, or EdgeArray specifying the regions whose mass
                properties are to be queried. The whole part is queried by default.

            relativeAccuracy=`abaqusConstants.LOW`[¶](#abaqus.Part.PartBase.PartBase.getMassProperties.relativeAccuracy "Permalink to this definition")
            :   A SymbolicConstant specifying the relative accuracy for geometry computation. Possible
                values are LOW, MEDIUM and HIGH. The default value is LOW.

            useMesh=`False`[¶](#abaqus.Part.PartBase.PartBase.getMassProperties.useMesh "Permalink to this definition")
            :   A Boolean specifying whether the mesh should be used in the computation if the geometry
                is meshed. The default value is False.

            specifyDensity=`False`[¶](#abaqus.Part.PartBase.PartBase.getMassProperties.specifyDensity "Permalink to this definition")
            :   A Boolean specifying whether a user-specified density should be used in regions with
                density errors such as undefined material density. The default value is False.

            density=`''`[¶](#abaqus.Part.PartBase.PartBase.getMassProperties.density "Permalink to this definition")
            :   A double value specifying the user-specified density value to be used in regions with
                density errors. The user-specified density should be greater than 0.

            specifyThickness=`False`[¶](#abaqus.Part.PartBase.PartBase.getMassProperties.specifyThickness "Permalink to this definition")
            :   A Boolean specifying whether a user-specified thickness should be used in regions with
                thickness errors such as undefined thickness. The default value is False.

            thickness=`''`[¶](#abaqus.Part.PartBase.PartBase.getMassProperties.thickness "Permalink to this definition")
            :   A double value specifying the user-specified thickness value to be used in regions with
                thickness errors. The user-specified thickness should be greater than 0.

            miAboutCenterOfMass=`True`[¶](#abaqus.Part.PartBase.PartBase.getMassProperties.miAboutCenterOfMass "Permalink to this definition")
            :   A Boolean specifying if the moments of inertia should be evaluated about the center of
                mass. The default value is True.

            miAboutPoint=`()`[¶](#abaqus.Part.PartBase.PartBase.getMassProperties.miAboutPoint "Permalink to this definition")
            :   A tuple of three floats specifying the coordinates of the point about which to evaluate
                the moment of inertia. By default if the moments of inertia are not being evaluated
                about the center of mass, they will be evaluated about the origin.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.getMassProperties-returns "Permalink to this headline")
        :   **properties** – A Dictionary object with the following items:

            * **area**: None or a Float specifying the sum of the area of the specified faces. The area
              is computed only for one side for shells.
            * **areaCentroid**: None or a tuple of three Floats representing the coordinates of the area
              centroid.
            * **volume**: None or a Float specifying the volume of the specified regions.
            * **volumeCentroid**: None or a tuple of three Floats representing the coordinates of the
              volume centroid.
            * **massFromMassPerUnitSurfaceArea**: None or a Float specifying the mass due to mass per
              unit surface area.
            * **mass**: None or a Float specifying the mass of the specified regions. It is the total
              mass and includes mass from quantities such as mass per unit surface area.
            * **centerOfMass**: None or a tuple of three Floats representing the coordinates of the
              center of mass.
            * **momentOfInertia**: None or a tuple of six Floats representing the moments of inertia
              about the center of mass or about the point specified.
            * **warnings**: A tuple of SymbolicConstants representing the problems encountered while
              computing the mass properties. Possible SymbolicConstants are:
            * UNSUPPORTED\_ENTITIES: Some unsupported entities exist in the specified region. The mass
              properties are computed only for beams, trusses, shells, solids, point and
              non-structural mass elements and rotary inertia elements. The mass properties are not
              computed for axisymmetric elements, springs, connectors, gaskets or any other elements.
            * MISSING\_THICKNESS: For some regions, the section definitions are missing thickness
              values.
            * ZERO\_THICKNESS: For some regions, the section definitions have a zero thickness value.
            * VARIABLE\_THICKNESS: The nodal thickness or field thickness specified for some regions
              has been ignored.
            * NON\_APPLICABLE\_THICKNESS: For some regions, the thickness value is not applicable to the
              corresponding sections specified on the regions.
            * MISSING\_DENSITY: For some regions, the section definitions are missing material density
              values.
            * MISSING\_MATERIAL\_DEFINITION: For some regions, the material definition is missing.
            * ZERO\_DENSITY: For some regions, the section definitions have a zero material density
              value.
            * UNSUPPORTED\_DENSITY: For some regions, either a negative material density or a
              temperature dependent density has been specified, or the material value is missing for
              one or more plies in the composite section.
            * SHELL\_OFFSETS: For shells, this method does not account for any offsets specified.
            * MISSING\_SECTION\_DEFINITION: For some regions, the section definition is missing.
            * UNSUPPORTED\_SECTION\_DEFINITION: The section definition provided for some regions is not
              supported.
            * REINFORCEMENTS: This method does not account for any reinforcements specified on the
              model.
            * SMEARED\_PROPERTIES: For regions with composite section assignments, the density is
              smeared across the thickness. The volume centroid and center of mass computations for a
              composite shell use a lumped mass approach where the volume and mass is assumed to be
              lumped in the plane of the shell. As a result of these approximations the volume
              centroid, center of mass and moments of inertia may be slightly inaccurate for regions
              with composite section assignments.
            * UNSUPPORTED\_NON\_STRUCTURAL\_MASS\_ENTITIES: This method does not account for any
              non-structural mass on wires.
            * INCORRECT\_MOMENT\_OF\_INERTIA: For geometry regions with non-structural mass per volume,
              the non-structural mass is assumed to be a point mass at the centroid of the regions.
              Thus, the moments of inertia may be inaccurate as the distribution of the non-structural
              mass is not accounted for. Use the mesh for accurately computing the moments of inertia.
            * MISSING\_BEAM\_ORIENTATIONS: For some regions with beam section assignments, the beam
              section orientations are missing.
            * UNSUPPORTED\_BEAM\_PROFILES: This method supports the Box, Pipe, Circular, Rectangular,
              Hexagonal, Trapezoidal, I, L, T, Arbitrary, and Tapered beam profiles. Any other beam
              profile is not supported.
            * TAPERED\_BEAM\_MI: Moment of inertia calculations for tapered beams are not accurate.
            * SUBSTRUCTURE\_INCORRECT\_PROPERTIES: The user assigned density and thickness is not
              considered for substructures.
            * UNSUPPORTED\_NON\_STRUCTURAL\_MASS\_PROPORTIONAL: Non-structural mass with Mass Proportional
              distribution is not supported. Results are computed using Volume Proportional
              distribution.

        Return type:[¶](#abaqus.Part.PartBase.PartBase.getMassProperties-return-type "Permalink to this headline")
        :   [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")

    getPerimeter(*[faces](#abaqus.Part.PartBase.PartBase.getPerimeter.faces "abaqus.Part.PartBase.PartBase.getPerimeter.faces (Python parameter) — A sequence of Face objects whose perimeter the method will calculate.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1184-L1200)[¶](#abaqus.Part.PartBase.PartBase.getPerimeter "Permalink to this definition")
    :   This method returns the total perimeter of a given face or group of faces. All faces need to be on
        the same part. If the specified faces have shared edges, these edges are excluded from the computation,
        thus providing the length of the outer perimeter of the specified faces.

        Note

        Check [PartBase.getPerimeter on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partgetperimeterpyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.getPerimeter-parameters "Permalink to this headline")
        :   faces[¶](#abaqus.Part.PartBase.PartBase.getPerimeter.faces "Permalink to this definition")
            :   A sequence of Face objects whose perimeter the method will calculate.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.getPerimeter-returns "Permalink to this headline")
        :   **perimeter** – A Float specifying the perimeter

        Return type:[¶](#abaqus.Part.PartBase.PartBase.getPerimeter-return-type "Permalink to this headline")
        :   [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")

    getVolume(*[cells](#abaqus.Part.PartBase.PartBase.getVolume.cells "abaqus.Part.PartBase.PartBase.getVolume.cells (Python parameter) — A sequence of Cell objects whose volume the method will calculate.")*, *[relativeAccuracy](#abaqus.Part.PartBase.PartBase.getVolume.relativeAccuracy "abaqus.Part.PartBase.PartBase.getVolume.relativeAccuracy (Python parameter) — A Float specifying the relative accuracy of the computation.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1202-L1219)[¶](#abaqus.Part.PartBase.PartBase.getVolume "Permalink to this definition")
    :   This method returns the volume area of a given cell or group of cells.

        Note

        Check [PartBase.getVolume on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partgetvolumepyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.getVolume-parameters "Permalink to this headline")
        :   cells[¶](#abaqus.Part.PartBase.PartBase.getVolume.cells "Permalink to this definition")
            :   A sequence of Cell objects whose volume the method will calculate.

            relativeAccuracy=`0`[¶](#abaqus.Part.PartBase.PartBase.getVolume.relativeAccuracy "Permalink to this definition")
            :   A Float specifying the relative accuracy of the computation. The default value is
                0.000001 (0.0001%).

        Returns:[¶](#abaqus.Part.PartBase.PartBase.getVolume-returns "Permalink to this headline")
        :   **volume** – A Float specifying the sum of the areas of the given faces

        Return type:[¶](#abaqus.Part.PartBase.PartBase.getVolume-return-type "Permalink to this headline")
        :   [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")

    ignoredEdges : --is-rst--:py:class:`~abaqus.BasicGeometry.IgnoredEdgeArray.IgnoredEdgeArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L92-L93)[¶](#abaqus.Part.PartBase.PartBase.ignoredEdges "Permalink to this definition")
    :   An IgnoredEdgeArray object specifying all the ignored edges in the part.

    ignoredVertices : --is-rst--:py:class:`~abaqus.BasicGeometry.IgnoredVertexArray.IgnoredVertexArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L86-L87)[¶](#abaqus.Part.PartBase.PartBase.ignoredVertices "Permalink to this definition")
    :   An IgnoredVertexArray object specifying all the ignored vertices in the part.

    isAlignedWithSketch()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1429-L1445)[¶](#abaqus.Part.PartBase.PartBase.isAlignedWithSketch "Permalink to this definition")
    :   This method checks if the normal of an analytical rigid surface part is aligned with that of its
        sketch.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.isAlignedWithSketch-returns "Permalink to this headline")
        :   A Boolean value of True if the part is aligned with the sketch and False if it is not
            aligned.

        Return type:[¶](#abaqus.Part.PartBase.PartBase.isAlignedWithSketch-return-type "Permalink to this headline")
        :   `Boolean`

        Raises:[¶](#abaqus.Part.PartBase.PartBase.isAlignedWithSketch-raises "Permalink to this headline")
        :   [**AbaqusException**](../../../kernel/utility.html#abaqus.UtilityAndView.AbaqusException.AbaqusException "abaqus.UtilityAndView.AbaqusException.AbaqusException (Python class) — Bases: Exception") – Can only be used with analytical rigid parts, If the part is not an analytical rigid part.

    isOutOfDate : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L76-L78)[¶](#abaqus.Part.PartBase.PartBase.isOutOfDate "Permalink to this definition")
    :   An Int specifying that feature parameters have been modified but that the part has not
        been regenerated. Possible values are 0 and 1.

    materialOrientations : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Property.MaterialOrientation.MaterialOrientation`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L167-L168)[¶](#abaqus.Part.PartBase.PartBase.materialOrientations "Permalink to this definition")
    :   A MaterialOrientationArray object.

    nodes : --is-rst--:py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L126-L127)[¶](#abaqus.Part.PartBase.PartBase.nodes "Permalink to this definition")
    :   A MeshNodeArray object specifying all the nodes in the part.

    printAssignedSections()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1447-L1450)[¶](#abaqus.Part.PartBase.PartBase.printAssignedSections "Permalink to this definition")
    :   This method prints information on each section that has been assigned to a region of the part.

    projectEdgesOntoSketch(*[sketch](#abaqus.Part.PartBase.PartBase.projectEdgesOntoSketch.sketch "abaqus.Part.PartBase.PartBase.projectEdgesOntoSketch.sketch (Python parameter) — The ConstrainedSketch object on which the edges are projected.")*, *[edges](#abaqus.Part.PartBase.PartBase.projectEdgesOntoSketch.edges "abaqus.Part.PartBase.PartBase.projectEdgesOntoSketch.edges (Python parameter) — A sequence of candidate edges to be projected onto the sketch.")*, *[constrainToBackground](#abaqus.Part.PartBase.PartBase.projectEdgesOntoSketch.constrainToBackground "abaqus.Part.PartBase.PartBase.projectEdgesOntoSketch.constrainToBackground (Python parameter) — A Boolean that determines whether the projected edges need to constrained to the background geometry.")=`True`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1452-L1472)[¶](#abaqus.Part.PartBase.PartBase.projectEdgesOntoSketch "Permalink to this definition")
    :   This method projects the selected edges of a part onto the specified ConstrainedSketch
        object. The edges appear as sketch geometry after projection. If the plane of projection
        is not parallel to the specified edge, the resultant sketch geometry may be of a
        different type. For example, a circular edge can be projected as an ellipse or a line
        depending on the angle of the plane of projection. By default, the projected edge will
        be constrained to the background geometry. You can remove this constraint by setting
        **constrainToBackground** to False.

        Note

        Check [PartBase.projectEdgesOntoSketch on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partprojectedgesontosketchpyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.projectEdgesOntoSketch-parameters "Permalink to this headline")
        :   sketch[¶](#abaqus.Part.PartBase.PartBase.projectEdgesOntoSketch.sketch "Permalink to this definition")
            :   The ConstrainedSketch object on which the edges are projected.

            edges[¶](#abaqus.Part.PartBase.PartBase.projectEdgesOntoSketch.edges "Permalink to this definition")
            :   A sequence of candidate edges to be projected onto the sketch.

            constrainToBackground=`True`[¶](#abaqus.Part.PartBase.PartBase.projectEdgesOntoSketch.constrainToBackground "Permalink to this definition")
            :   A Boolean that determines whether the projected edges need to constrained to the
                background geometry. The default is True.

    projectReferencesOntoSketch(*[sketch](#abaqus.Part.PartBase.PartBase.projectReferencesOntoSketch.sketch "abaqus.Part.PartBase.PartBase.projectReferencesOntoSketch.sketch (Python parameter) — The ConstrainedSketch object on which the edges, vertices, and datum points are projected.")*, *[filter](#abaqus.Part.PartBase.PartBase.projectReferencesOntoSketch.filter "abaqus.Part.PartBase.PartBase.projectReferencesOntoSketch.filter (Python parameter) — A SymbolicConstant specifying how to limit the amount of projection.")=`abaqusConstants.ALL_EDGES`*, *[upToFeature](#abaqus.Part.PartBase.PartBase.projectReferencesOntoSketch.upToFeature "abaqus.Part.PartBase.PartBase.projectReferencesOntoSketch.upToFeature (Python parameter) — A Feature object specifying a marker in the feature-based history of the part. Abaqus/CAE projects onto the sketch only the part entities that were created before the feature specified by this marker.")=`None`*, *[edges](#abaqus.Part.PartBase.PartBase.projectReferencesOntoSketch.edges "abaqus.Part.PartBase.PartBase.projectReferencesOntoSketch.edges (Python parameter) — A sequence of candidate edges whose vertices need to be projected onto the sketch.")=`()`*, *[vertices](#abaqus.Part.PartBase.PartBase.projectReferencesOntoSketch.vertices "abaqus.Part.PartBase.PartBase.projectReferencesOntoSketch.vertices (Python parameter) — A sequence of candidate vertices to be projected onto the sketch.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1474-L1508)[¶](#abaqus.Part.PartBase.PartBase.projectReferencesOntoSketch "Permalink to this definition")
    :   This method projects the vertices of specified edges, and datum points from the part onto the
        specified ConstrainedSketch object. The vertices and datum points appear on the sketch as reference
        geometry.

        Note

        Check [PartBase.projectReferencesOntoSketch on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partprojectreferencesontosketchpyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.projectReferencesOntoSketch-parameters "Permalink to this headline")
        :   sketch[¶](#abaqus.Part.PartBase.PartBase.projectReferencesOntoSketch.sketch "Permalink to this definition")
            :   The ConstrainedSketch object on which the edges, vertices, and datum points are
                projected.

            filter=`abaqusConstants.ALL_EDGES`[¶](#abaqus.Part.PartBase.PartBase.projectReferencesOntoSketch.filter "Permalink to this definition")
            :   A SymbolicConstant specifying how to limit the amount of projection. Possible values are
                ALL\_EDGES and COPLANAR\_EDGES. If **filter** = COPLANAR\_EDGES, edges that are coplanar to the
                sketching plane are the only candidates for projection. The default value is ALL\_EDGES.

            upToFeature=`None`[¶](#abaqus.Part.PartBase.PartBase.projectReferencesOntoSketch.upToFeature "Permalink to this definition")
            :   A Feature object specifying a marker in the feature-based history of the part.
                Abaqus/CAE projects onto the sketch only the part entities that were created before the
                feature specified by this marker. By default, part entities in features created before
                the sketch you are editing are candidates for projection.

            edges=`()`[¶](#abaqus.Part.PartBase.PartBase.projectReferencesOntoSketch.edges "Permalink to this definition")
            :   A sequence of candidate edges whose vertices need to be projected onto the sketch. By
                default, all edges specified by the **filter** argument are candidates for projection.

            vertices=`()`[¶](#abaqus.Part.PartBase.PartBase.projectReferencesOntoSketch.vertices "Permalink to this definition")
            :   A sequence of candidate vertices to be projected onto the sketch. By default, all
                vertices are candidates for projection.

    queryAttributes(*[printResults](#abaqus.Part.PartBase.PartBase.queryAttributes.printResults "abaqus.Part.PartBase.PartBase.queryAttributes.printResults (Python parameter) — A Boolean which specifies whether the above information is to be printed.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1510-L1532)[¶](#abaqus.Part.PartBase.PartBase.queryAttributes "Permalink to this definition")
    :   This method prints the following information about a part:

        > * the name, modeling space, and analysis type; and
        > * whether twist is included (only available when the modeling space is axisymmetric and
        >   the analysis type is deformable); and
        > * the number of vertices, edges, faces and cells if applicable.

        Note

        Check [PartBase.queryAttributes on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partqueryattributespyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.queryAttributes-parameters "Permalink to this headline")
        :   printResults=`0`[¶](#abaqus.Part.PartBase.PartBase.queryAttributes.printResults "Permalink to this definition")
            :   A Boolean which specifies whether the above information is to be printed. The default
                value is True

        Returns:[¶](#abaqus.Part.PartBase.PartBase.queryAttributes-returns "Permalink to this headline")
        :   **attributes** – A Dictionary object with string keys and integer values which returns the above
            information with the keys being numVertices, numEdges, numFaces, numCells,
            numWiredEdges, numShellFaces and numSolidFaces.

        Return type:[¶](#abaqus.Part.PartBase.PartBase.queryAttributes-return-type "Permalink to this headline")
        :   [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")

    queryCachedStates()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1534-L1541)[¶](#abaqus.Part.PartBase.PartBase.queryCachedStates "Permalink to this definition")
    :   This method displays the position of geometric states relative to the sequence of features in the
        part cache.

        The output is displayed in the message area.

    queryDisjointPlyRegions()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1584-L1587)[¶](#abaqus.Part.PartBase.PartBase.queryDisjointPlyRegions "Permalink to this definition")
    :   This method provides a list of all composite plys in the current part which have disjoint regions.

    queryGeometry(*[relativeAccuracy](#abaqus.Part.PartBase.PartBase.queryGeometry.relativeAccuracy "abaqus.Part.PartBase.PartBase.queryGeometry.relativeAccuracy (Python parameter) — A Float specifying that the property computations should stop when the specified relative accuracy has been achieved.")=`0`*, *[printResults](#abaqus.Part.PartBase.PartBase.queryGeometry.printResults "abaqus.Part.PartBase.PartBase.queryGeometry.printResults (Python parameter) — A Boolean which specifies whether the above information is to be printed.")=`True`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1543-L1570)[¶](#abaqus.Part.PartBase.PartBase.queryGeometry "Permalink to this definition")
    :   This method prints the following information about a part:

        * the name, modeling space, and analysis type;
        * whether twist is included (only available when the modeling space is axisymmetric and
          the analysis type is deformable);
        * a 3D point representing the minimum of the part’s bounding box;
        * a 3D point representing the maximum of the part’s bounding box;
        * a 3D point representing the part’s centroid (only on 3D solid parts); and
        * the volume (only on 3D solid parts).

        Note

        Check [PartBase.queryGeometry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partquerygeometrypyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.queryGeometry-parameters "Permalink to this headline")
        :   relativeAccuracy=`0`[¶](#abaqus.Part.PartBase.PartBase.queryGeometry.relativeAccuracy "Permalink to this definition")
            :   A Float specifying that the property computations should stop when the specified
                relative accuracy has been achieved. The default value is 0.000001 (0.0001%).

            printResults=`True`[¶](#abaqus.Part.PartBase.PartBase.queryGeometry.printResults "Permalink to this definition")
            :   A Boolean which specifies whether the above information is to be printed. The default
                value is True.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.queryGeometry-returns "Permalink to this headline")
        :   **geometry** – A Dictionary object with string keys, which returns the above information with the keys
            being name, space, type, volume, centroid, category and boundingBox.

        Return type:[¶](#abaqus.Part.PartBase.PartBase.queryGeometry-return-type "Permalink to this headline")
        :   [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")

    queryRegionsMissingSections()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1572-L1582)[¶](#abaqus.Part.PartBase.PartBase.queryRegionsMissingSections "Permalink to this definition")
    :   This method returns all regions in the part that do not have a section assignment but require one for
        analysis.

        Returns:[¶](#abaqus.Part.PartBase.PartBase.queryRegionsMissingSections-returns "Permalink to this headline")
        :   **region** – A Region object, or None

        Return type:[¶](#abaqus.Part.PartBase.PartBase.queryRegionsMissingSections-return-type "Permalink to this headline")
        :   `Region`

    referencePoints : --is-rst--:py:class:`~abaqus.BasicGeometry.ReferencePoints.ReferencePoints` = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L158-L159)[¶](#abaqus.Part.PartBase.PartBase.referencePoints "Permalink to this definition")
    :   A repository of ReferencePoint objects.

    regenerate()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1589-L1596)[¶](#abaqus.Part.PartBase.PartBase.regenerate "Permalink to this definition")
    :   This method regenerates a part.

        When you modify features, it may be convenient to postpone regeneration until you make all your
        changes, since regeneration can be time consuming.

    regenerationWarnings()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1598-L1601)[¶](#abaqus.Part.PartBase.PartBase.regenerationWarnings "Permalink to this definition")
    :   This method prints any regeneration warnings associated with the features.

    removeInvalidGeometry()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1603-L1612)[¶](#abaqus.Part.PartBase.PartBase.removeInvalidGeometry "Permalink to this definition")
    :   Removes all invalid entities from the part, leaving a valid part.

        This is not recorded as a feature in the feature list, therefore it should be used on parts that
        have a single feature (such as an imported part). Note:This may remove valid entities that are
        connected to invalid ones. You can identify invalid entities using the query toolset before using
        this command.

    restore()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1614-L1621)[¶](#abaqus.Part.PartBase.PartBase.restore "Permalink to this definition")
    :   This method restores the parameters of all features in the assembly to the value they had before a
        failed regeneration.

        Use the restore method after a failed regeneration, followed by a regenerate command.

    resumeAllFeatures()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1623-L1626)[¶](#abaqus.Part.PartBase.PartBase.resumeAllFeatures "Permalink to this definition")
    :   This method resumes all the suppressed features in the part.

    resumeFeatures(*[featureNames](#abaqus.Part.PartBase.PartBase.resumeFeatures.featureNames "abaqus.Part.PartBase.PartBase.resumeFeatures.featureNames (Python parameter) — A tuple of names of features which are to be resumed.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1628-L1637)[¶](#abaqus.Part.PartBase.PartBase.resumeFeatures "Permalink to this definition")
    :   This method resumes the specified suppressed features in the part.

        Note

        Check [PartBase.resumeFeatures on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partresumefeaturespyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.resumeFeatures-parameters "Permalink to this headline")
        :   featureNames[¶](#abaqus.Part.PartBase.PartBase.resumeFeatures.featureNames "Permalink to this definition")
            :   A tuple of names of features which are to be resumed.

    resumeLastSetFeatures()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1639-L1642)[¶](#abaqus.Part.PartBase.PartBase.resumeLastSetFeatures "Permalink to this definition")
    :   This method resumes the last set of features to be suppressed in the part.

    retainedNodes : --is-rst--:py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L129-L130)[¶](#abaqus.Part.PartBase.PartBase.retainedNodes "Permalink to this definition")
    :   A MeshNodeArray object specifying all the retained nodes in the substructure part.

    saveGeometryCache()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1644-L1650)[¶](#abaqus.Part.PartBase.PartBase.saveGeometryCache "Permalink to this definition")
    :   This method caches the current geometry.

        Caching the current geometry improves regeneration performance.

    sectionAssignments : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Property.SectionAssignment.SectionAssignment`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L164-L165)[¶](#abaqus.Part.PartBase.PartBase.sectionAssignments "Permalink to this definition")
    :   A SectionAssignmentArray object.

    setAssociatedCADPaths(*[partFile](#abaqus.Part.PartBase.PartBase.setAssociatedCADPaths.partFile "abaqus.Part.PartBase.PartBase.setAssociatedCADPaths.partFile (Python parameter) — A String specifying the name of the associated CAD part file.")=`''`*, *[rootFile](#abaqus.Part.PartBase.PartBase.setAssociatedCADPaths.rootFile "abaqus.Part.PartBase.PartBase.setAssociatedCADPaths.rootFile (Python parameter) — A String specifying the name of the root associated CAD file.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1652-L1667)[¶](#abaqus.Part.PartBase.PartBase.setAssociatedCADPaths "Permalink to this definition")
    :   This method sets the paths to the associated CAD part and root file. This method is only available if
        the part was imported from one of the supported CAD softwares using the Associative Import capability.
        The root file can be the assembly file or the part file, depending on the one that was imported. This
        method can be used to specify the new paths when the CAD data is moved to a different directory.

        Note

        Check [PartBase.setAssociatedCADPaths on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partsetassociatedcadpathspyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.setAssociatedCADPaths-parameters "Permalink to this headline")
        :   partFile=`''`[¶](#abaqus.Part.PartBase.PartBase.setAssociatedCADPaths.partFile "Permalink to this definition")
            :   A String specifying the name of the associated CAD part file.

            rootFile=`''`[¶](#abaqus.Part.PartBase.PartBase.setAssociatedCADPaths.rootFile "Permalink to this definition")
            :   A String specifying the name of the root associated CAD file. This can be the same as
                the part file or can be the assembly file, depending on the one that was imported.

    setValues(*\*[args](#abaqus.Part.PartBase.PartBase.setValues "abaqus.Part.PartBase.PartBase.setValues.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Part.PartBase.PartBase.setValues "abaqus.Part.PartBase.PartBase.setValues.kwargs (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L877-L885)[¶](#abaqus.Part.PartBase.PartBase.setValues "Permalink to this definition")
    :   This method modifies the Part object.

        Raises:[¶](#abaqus.Part.PartBase.PartBase.setValues-raises "Permalink to this headline")
        :   **RangeError** –

    sets : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Region.Set.Set`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L132-L133)[¶](#abaqus.Part.PartBase.PartBase.sets "Permalink to this definition")
    :   A repository of Set objects specifying for more information, see Set.

    skins : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Region.Skin.Skin`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L152-L153)[¶](#abaqus.Part.PartBase.PartBase.skins "Permalink to this definition")
    :   A repository of Skin objects specifying the skins created on the part.

    smoothNodes(*[nodes](#abaqus.Part.PartBase.PartBase.smoothNodes.nodes "abaqus.Part.PartBase.PartBase.smoothNodes.nodes (Python parameter) — A sequence of MeshNode objects or a Set object containing nodes.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1815-L1825)[¶](#abaqus.Part.PartBase.PartBase.smoothNodes "Permalink to this definition")
    :   This method smooths the given nodes of a native mesh, moving them locally to a more optimal location
        that improves the quality of the mesh.

        Note

        Check [PartBase.smoothNodes on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partsmoothnodespyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.smoothNodes-parameters "Permalink to this headline")
        :   nodes[¶](#abaqus.Part.PartBase.PartBase.smoothNodes.nodes "Permalink to this definition")
            :   A sequence of MeshNode objects or a Set object containing nodes.

    stringers : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Region.Stringer.Stringer`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L155-L156)[¶](#abaqus.Part.PartBase.PartBase.stringers "Permalink to this definition")
    :   A repository of Stringer objects specifying the stringers created on the part.

    suppressFeatures(*[featureNames](#abaqus.Part.PartBase.PartBase.suppressFeatures.featureNames "abaqus.Part.PartBase.PartBase.suppressFeatures.featureNames (Python parameter) — A tuple of names of features which are to be suppressed in the part.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1669-L1678)[¶](#abaqus.Part.PartBase.PartBase.suppressFeatures "Permalink to this definition")
    :   This method suppresses the given features.

        Note

        Check [PartBase.suppressFeatures on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partsuppressfeaturespyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.suppressFeatures-parameters "Permalink to this headline")
        :   featureNames[¶](#abaqus.Part.PartBase.PartBase.suppressFeatures.featureNames "Permalink to this definition")
            :   A tuple of names of features which are to be suppressed in the part.

    surfaces : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Region.Surface.Surface`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L142-L143)[¶](#abaqus.Part.PartBase.PartBase.surfaces "Permalink to this definition")
    :   A repository of Surface objects specifying for more information, see Surface.

    timeStamp : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L80-L81)[¶](#abaqus.Part.PartBase.PartBase.timeStamp "Permalink to this definition")
    :   A Float specifying when the part was last modified.

    vertices : --is-rst--:py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L83-L84)[¶](#abaqus.Part.PartBase.PartBase.vertices "Permalink to this definition")
    :   A VertexArray object specifying all the vertices in the part.

    writeAcisFile(*[fileName](#abaqus.Part.PartBase.PartBase.writeAcisFile.fileName "abaqus.Part.PartBase.PartBase.writeAcisFile.fileName (Python parameter) — A String specifying the name of the file to which to write.")*, *[version](#abaqus.Part.PartBase.PartBase.writeAcisFile.version "abaqus.Part.PartBase.PartBase.writeAcisFile.version (Python parameter) — A Float specifying the ACIS version.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1680-L1703)[¶](#abaqus.Part.PartBase.PartBase.writeAcisFile "Permalink to this definition")
    :   This method exports the geometry of the part to a named file in ACIS format.

        Note

        Check [PartBase.writeAcisFile on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partwriteacisfilepyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.writeAcisFile-parameters "Permalink to this headline")
        :   fileName[¶](#abaqus.Part.PartBase.PartBase.writeAcisFile.fileName "Permalink to this definition")
            :   A String specifying the name of the file to which to write. The file name’s extension is
                used to determine whether a part or assembly is written. Use the file extension .asat
                for the assembly format.

                Changed in version 2018: Add description for thr file name’s extension.

            version=`None`[¶](#abaqus.Part.PartBase.PartBase.writeAcisFile.version "Permalink to this definition")
            :   A Float specifying the ACIS version. For example, the Float 12.0 corresponds to ACIS
                Version 12.0. The default value is the current version of ACIS.

        Raises:[¶](#abaqus.Part.PartBase.PartBase.writeAcisFile-raises "Permalink to this headline")
        :   [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.13)") – Cannot export orphan mesh parts to ACIS,
            If the part is an orphan mesh part.

    writeCADParameters(*[paramFile](#abaqus.Part.PartBase.PartBase.writeCADParameters.paramFile "abaqus.Part.PartBase.PartBase.writeCADParameters.paramFile (Python parameter) — A String specifying the parameter file name.")*, *[modifiedParams](#abaqus.Part.PartBase.PartBase.writeCADParameters.modifiedParams "abaqus.Part.PartBase.PartBase.writeCADParameters.modifiedParams (Python parameter) — A tuple of tuples each containing the part name, the parameter name, and the modified parameter value.")=`()`*, *[updatePaths](#abaqus.Part.PartBase.PartBase.writeCADParameters.updatePaths "abaqus.Part.PartBase.PartBase.writeCADParameters.updatePaths (Python parameter) — A Bool specifying whether to update the path of the CAD model file specified in the parameterFile to the current directory, if the CAD model is present in the current directory.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1705-L1721)[¶](#abaqus.Part.PartBase.PartBase.writeCADParameters "Permalink to this definition")
    :   This method writes the parameters that were imported from the CAD system to a parameter file.

        Note

        Check [PartBase.writeCADParameters on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partwritecadparameterspyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.writeCADParameters-parameters "Permalink to this headline")
        :   paramFile[¶](#abaqus.Part.PartBase.PartBase.writeCADParameters.paramFile "Permalink to this definition")
            :   A String specifying the parameter file name.

            modifiedParams=`()`[¶](#abaqus.Part.PartBase.PartBase.writeCADParameters.modifiedParams "Permalink to this definition")
            :   A tuple of tuples each containing the part name, the parameter name, and the modified
                parameter value. Default is an empty tuple.

            updatePaths=`''`[¶](#abaqus.Part.PartBase.PartBase.writeCADParameters.updatePaths "Permalink to this definition")
            :   A Bool specifying whether to update the path of the CAD model file specified in the
                **parameterFile** to the current directory, if the CAD model is present in the current
                directory.

    writeIgesFile(*[fileName](#abaqus.Part.PartBase.PartBase.writeIgesFile.fileName "abaqus.Part.PartBase.PartBase.writeIgesFile.fileName (Python parameter) — A String specifying the name of the file to which to write.")*, *[flavor](#abaqus.Part.PartBase.PartBase.writeIgesFile.flavor "abaqus.Part.PartBase.PartBase.writeIgesFile.flavor (Python parameter) — A SymbolicConstant specifying a particular flavor of IGES.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1723-L1743)[¶](#abaqus.Part.PartBase.PartBase.writeIgesFile "Permalink to this definition")
    :   This method exports the geometry of the part to a named file in IGES format.

        Note

        Check [PartBase.writeIgesFile on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partwriteigesfilepyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.writeIgesFile-parameters "Permalink to this headline")
        :   fileName[¶](#abaqus.Part.PartBase.PartBase.writeIgesFile.fileName "Permalink to this definition")
            :   A String specifying the name of the file to which to write.

            flavor[¶](#abaqus.Part.PartBase.PartBase.writeIgesFile.flavor "Permalink to this definition")
            :   A SymbolicConstant specifying a particular flavor of IGES. Possible values are STANDARD,
                AUTOCAD, SOLIDWORKS, JAMA, and MSBO.

        Raises:[¶](#abaqus.Part.PartBase.PartBase.writeIgesFile-raises "Permalink to this headline")
        :   [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.13)") – Cannot export orphan mesh parts to IGES,
            If the part is an orphan mesh part.

    writeStepFile(*[fileName](#abaqus.Part.PartBase.PartBase.writeStepFile.fileName "abaqus.Part.PartBase.PartBase.writeStepFile.fileName (Python parameter) — A String specifying the name of the file to which to write.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1745-L1759)[¶](#abaqus.Part.PartBase.PartBase.writeStepFile "Permalink to this definition")
    :   This method exports the geometry of the part to a named file in STEP format.

        Note

        Check [PartBase.writeStepFile on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partwritestepfilepyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.writeStepFile-parameters "Permalink to this headline")
        :   fileName[¶](#abaqus.Part.PartBase.PartBase.writeStepFile.fileName "Permalink to this definition")
            :   A String specifying the name of the file to which to write.

        Raises:[¶](#abaqus.Part.PartBase.PartBase.writeStepFile-raises "Permalink to this headline")
        :   **Parterror** – Cannot export orphan mesh parts to STEP, If the part contains no geometry.

    writeVdaFile(*[fileName](#abaqus.Part.PartBase.PartBase.writeVdaFile.fileName "abaqus.Part.PartBase.PartBase.writeVdaFile.fileName (Python parameter) — A String specifying the name of the file to which to write.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L1761-L1775)[¶](#abaqus.Part.PartBase.PartBase.writeVdaFile "Permalink to this definition")
    :   This method exports the geometry of the part to a named file in VDA-FS format.

        Note

        Check [PartBase.writeVdaFile on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partwritevdafilepyc).

        Parameters:[¶](#abaqus.Part.PartBase.PartBase.writeVdaFile-parameters "Permalink to this headline")
        :   fileName[¶](#abaqus.Part.PartBase.PartBase.writeVdaFile.fileName "Permalink to this definition")
            :   A String specifying the name of the file to which to write.

        Raises:[¶](#abaqus.Part.PartBase.PartBase.writeVdaFile-raises "Permalink to this headline")
        :   [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.13)") – Cannot export orphan mesh parts to VDA-FS If the part is an orphan mesh part.

## Other Classes[¶](#other-classes "Permalink to this heading")

*class* AcisFile[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L20-L350)[¶](#abaqus.Part.PartBase.AcisFile "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The AcisFile object is a file object used to open ACIS-, STEP-, and IGES-format files.

    Note

    This object can be accessed by:

    ```python
    import part
    ```

    Note

    Check [AcisFile on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acisfilepyc.htm?contextscope=all).

    Member Details:

    numberOfParts : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L30-L31)[¶](#abaqus.Part.PartBase.AcisFile.numberOfParts "Permalink to this definition")
    :   An Int specifying the number of parts in the object.

    openAcis(*[fileName](#abaqus.Part.PartBase.AcisFile.openAcis.fileName "abaqus.Part.PartBase.AcisFile.openAcis.fileName (Python parameter) — A String specifying the path to the ACIS file to open.")*, *[scaleFromFile](#abaqus.Part.PartBase.AcisFile.openAcis.scaleFromFile "abaqus.Part.PartBase.AcisFile.openAcis.scaleFromFile (Python parameter) — A Boolean specifying whether to scale, rotate, and translate the part using the transform read from the ACIS file.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L33-L63)[¶](#abaqus.Part.PartBase.AcisFile.openAcis "Permalink to this definition")
    :   This method creates an AcisFile object from a file containing ACIS-format geometry. This object is
        subsequently used by the PartFromGeometryFile method.

        Note

        This function can be accessed by:

        ```python
        mdb.openAcis
        ```

        Note

        Check [AcisFile.openAcis on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acisfilepyc.htm?contextscope=all#simaker-acisfileopenacispyc).

        Parameters:[¶](#abaqus.Part.PartBase.AcisFile.openAcis-parameters "Permalink to this headline")
        :   fileName[¶](#abaqus.Part.PartBase.AcisFile.openAcis.fileName "Permalink to this definition")
            :   A String specifying the path to the ACIS file to open.

            scaleFromFile=`0`[¶](#abaqus.Part.PartBase.AcisFile.openAcis.scaleFromFile "Permalink to this definition")
            :   A Boolean specifying whether to scale, rotate, and translate the part using the
                transform read from the ACIS file. The default value is OFF.

        Returns:[¶](#abaqus.Part.PartBase.AcisFile.openAcis-returns "Permalink to this headline")
        :   An AcisFile object.

        Return type:[¶](#abaqus.Part.PartBase.AcisFile.openAcis-return-type "Permalink to this headline")
        :   [`AcisFile`](#abaqus.Part.PartBase.AcisFile "abaqus.Part.PartBase.AcisFile (Python class) — Bases: object")

        Raises:[¶](#abaqus.Part.PartBase.AcisFile.openAcis-raises "Permalink to this headline")
        :   * **Texterror** – ACIS File version exceeds Kernel, File is from a newer version of ACIS than the CAE kernel.
            * **Texterror** – Failed to read ACIS file, The data in the ACIS file are corrupted.

    openCatia(*[fileName](#abaqus.Part.PartBase.AcisFile.openCatia.fileName "abaqus.Part.PartBase.AcisFile.openCatia.fileName (Python parameter) — A String specifying the path to the CATIA file to open.")*, *[topology](#abaqus.Part.PartBase.AcisFile.openCatia.topology "abaqus.Part.PartBase.AcisFile.openCatia.topology (Python parameter) — A SymbolicConstant specifying the topology of the data to be read from the file and of the part to be created.")=`None`*, *[convertUnits](#abaqus.Part.PartBase.AcisFile.openCatia.convertUnits "abaqus.Part.PartBase.AcisFile.openCatia.convertUnits (Python parameter) — A SymbolicConstant specifying whether the original units should be retained.")=`0`*, *[combineBodies](#abaqus.Part.PartBase.AcisFile.openCatia.combineBodies "abaqus.Part.PartBase.AcisFile.openCatia.combineBodies (Python parameter) — A Boolean specifying whether to combine the bodies in the CATPart file.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L65-L104)[¶](#abaqus.Part.PartBase.AcisFile.openCatia "Permalink to this definition")
    :   This method creates an AcisFile object from a file containing V5-format geometry. This object is
        subsequently used by the PartFromGeometryFile method.

        Note

        This function can be accessed by:

        ```python
        mdb.openAcis
        ```

        Note

        Check [AcisFile.openCatia on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acisfilepyc.htm?contextscope=all#simaker-acisfileopencatiapyc).

        Parameters:[¶](#abaqus.Part.PartBase.AcisFile.openCatia-parameters "Permalink to this headline")
        :   fileName[¶](#abaqus.Part.PartBase.AcisFile.openCatia.fileName "Permalink to this definition")
            :   A String specifying the path to the CATIA file to open.

            topology=`None`[¶](#abaqus.Part.PartBase.AcisFile.openCatia.topology "Permalink to this definition")
            :   A SymbolicConstant specifying the topology of the data to be read from the file and of
                the part to be created. Possible values are SOLID , SHELL, and WIRE. If
                **topology** = SOLID, Abaqus/CAE attempts to attach cells to create a solid. If
                **topology** = SHELL, Abaqus/CAE builds the body as a shell entity and not as a solid
                entity. The default value is SOLID .

            convertUnits=`0`[¶](#abaqus.Part.PartBase.AcisFile.openCatia.convertUnits "Permalink to this definition")
            :   A SymbolicConstant specifying whether the original units should be retained. Possible
                values are ON and OFF. The default value is OFF.

            combineBodies=`0`[¶](#abaqus.Part.PartBase.AcisFile.openCatia.combineBodies "Permalink to this definition")
            :   A Boolean specifying whether to combine the bodies in the CATPart file. If the bodies to
                be combined touch or overlap, invalid entities would result. For CATProduct files, this
                option will be ignored.

        Returns:[¶](#abaqus.Part.PartBase.AcisFile.openCatia-returns "Permalink to this headline")
        :   An AcisFile object.

        Return type:[¶](#abaqus.Part.PartBase.AcisFile.openCatia-return-type "Permalink to this headline")
        :   [`AcisFile`](#abaqus.Part.PartBase.AcisFile "abaqus.Part.PartBase.AcisFile (Python class) — Bases: object")

    openEnf(*[fileName](#abaqus.Part.PartBase.AcisFile.openEnf.fileName "abaqus.Part.PartBase.AcisFile.openEnf.fileName (Python parameter) — A String specifying the path to the Elysium Neutral File that was created by I-DEAS, Pro/ENGINEER, or CATIA V5.")*, *[fileType](#abaqus.Part.PartBase.AcisFile.openEnf.fileType "abaqus.Part.PartBase.AcisFile.openEnf.fileType (Python parameter) — A String specifying the type of CAD system that created the file.")*, *[topology](#abaqus.Part.PartBase.AcisFile.openEnf.topology "abaqus.Part.PartBase.AcisFile.openEnf.topology (Python parameter) — A SymbolicConstant specifying the topology of the data to be read from the file and of the part to be created.")=`abaqusConstants.SOLID`*, *[convertUnits](#abaqus.Part.PartBase.AcisFile.openEnf.convertUnits "abaqus.Part.PartBase.AcisFile.openEnf.convertUnits (Python parameter) — A Boolean specifying if the dimensions of the part should be converted to millimeters. The default value is OFF.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L106-L147)[¶](#abaqus.Part.PartBase.AcisFile.openEnf "Permalink to this definition")
    :   This method creates an AcisFile object from a file containing Elysium Neutral File-format geometry
        that was created by CATIA V5, I-DEAS, or Pro/ENGINEER. This object is subsequently used by the
        PartFromGeometryFile method.

        Note

        This function can be accessed by:

        ```python
        mdb.openAcis
        ```

        Note

        Check [AcisFile.openEnf on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acisfilepyc.htm?contextscope=all#simaker-acisfileopenenfpyc).

        Parameters:[¶](#abaqus.Part.PartBase.AcisFile.openEnf-parameters "Permalink to this headline")
        :   fileName[¶](#abaqus.Part.PartBase.AcisFile.openEnf.fileName "Permalink to this definition")
            :   A String specifying the path to the Elysium Neutral File that was created by I-DEAS,
                Pro/ENGINEER, or CATIA V5.

            fileType[¶](#abaqus.Part.PartBase.AcisFile.openEnf.fileType "Permalink to this definition")
            :   A String specifying the type of CAD system that created the file. Possible values are
                “ideas”, “proe”, or “catiav5” or a combination similar to “proe/ideas/catiav5” if the
                type is unknown.

            topology=`abaqusConstants.SOLID`[¶](#abaqus.Part.PartBase.AcisFile.openEnf.topology "Permalink to this definition")
            :   A SymbolicConstant specifying the topology of the data to be read from the file and of
                the part to be created. Possible values are SOLID , SHELL, and WIRE. If
                **topology** = SOLID, Abaqus/CAE attempts to attach cells to create a solid. If
                **topology** = SHELL, Abaqus/CAE builds the body as a shell entity and not as a solid
                entity. The default value is SOLID.

            convertUnits=`0`[¶](#abaqus.Part.PartBase.AcisFile.openEnf.convertUnits "Permalink to this definition")
            :   A Boolean specifying if the dimensions of the part should be converted to millimeters.
                The default value is OFF.

        Returns:[¶](#abaqus.Part.PartBase.AcisFile.openEnf-returns "Permalink to this headline")
        :   An AcisFile object.

        Return type:[¶](#abaqus.Part.PartBase.AcisFile.openEnf-return-type "Permalink to this headline")
        :   [`AcisFile`](#abaqus.Part.PartBase.AcisFile "abaqus.Part.PartBase.AcisFile (Python class) — Bases: object")

    openIges(*[fileName](#abaqus.Part.PartBase.AcisFile.openIges.fileName "abaqus.Part.PartBase.AcisFile.openIges.fileName (Python parameter) — A String specifying the path to the IGES file to open.")*, *[trimCurve](#abaqus.Part.PartBase.AcisFile.openIges.trimCurve "abaqus.Part.PartBase.AcisFile.openIges.trimCurve (Python parameter) — A SymbolicConstant specifying the method used to define the trim curves that bound parametric surfaces.")=`abaqusConstants.DEFAULT`*, *[scaleFromFile](#abaqus.Part.PartBase.AcisFile.openIges.scaleFromFile "abaqus.Part.PartBase.AcisFile.openIges.scaleFromFile (Python parameter) — A SymbolicConstant specifying whether the imported geometry needs to be scaled using the units information available in the IGES file.")=`0`*, *[msbo](#abaqus.Part.PartBase.AcisFile.openIges.msbo "abaqus.Part.PartBase.AcisFile.openIges.msbo (Python parameter) — A Boolean specifying if the IGES file contains MSBO (Manifold Solid B-Rep Object) entities.")=`False`*, *[includedLayers](#abaqus.Part.PartBase.AcisFile.openIges.includedLayers "abaqus.Part.PartBase.AcisFile.openIges.includedLayers (Python parameter) — A sequence of Ints specifying the levels or layers of entities that will be translated from the IGES file to build the part.")=`()`*, *[topology](#abaqus.Part.PartBase.AcisFile.openIges.topology "abaqus.Part.PartBase.AcisFile.openIges.topology (Python parameter) — A SymbolicConstant specifying the topology of the data to be read from the file and of the part to be created.")=`abaqusConstants.SOLID`*, *[uniteWires](#abaqus.Part.PartBase.AcisFile.openIges.uniteWires "abaqus.Part.PartBase.AcisFile.openIges.uniteWires (Python parameter) — A SymbolicConstant specifying whether the imported wires need to be united or not. Possible values are ON and OFF.")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L149-L211)[¶](#abaqus.Part.PartBase.AcisFile.openIges "Permalink to this definition")
    :   This method creates an AcisFile object from a file containing IGES-format geometry. This object is
        subsequently used by the PartFromGeometryFile method.

        Note

        This function can be accessed by:

        ```python
        mdb.openAcis
        ```

        Note

        Check [AcisFile.openIges on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acisfilepyc.htm?contextscope=all#simaker-acisfileopenigespyc).

        Parameters:[¶](#abaqus.Part.PartBase.AcisFile.openIges-parameters "Permalink to this headline")
        :   fileName[¶](#abaqus.Part.PartBase.AcisFile.openIges.fileName "Permalink to this definition")
            :   A String specifying the path to the IGES file to open.

            trimCurve=`abaqusConstants.DEFAULT`[¶](#abaqus.Part.PartBase.AcisFile.openIges.trimCurve "Permalink to this definition")
            :   A SymbolicConstant specifying the method used to define the trim curves that bound
                parametric surfaces. Possible values are:DEFAULT, use either of the following as
                specified by the contents of the IGES file.PARAMETRIC\_DATA, use the parameter space of
                the surface being trimmed.THREED\_DATA, use real space—the coordinate system of the part
                along with an indication that the trim curve lies on the parametric surface.The default
                value is DEFAULT.

            scaleFromFile=`0`[¶](#abaqus.Part.PartBase.AcisFile.openIges.scaleFromFile "Permalink to this definition")
            :   A SymbolicConstant specifying whether the imported geometry needs to be scaled using the
                units information available in the IGES file. Possible values are ON and OFF. The
                default value is OFF. When the argument is set to ON, the geometry is scaled to
                millimeters with respect to the unit system specified in the IGES file.

            msbo=`False`[¶](#abaqus.Part.PartBase.AcisFile.openIges.msbo "Permalink to this definition")
            :   A Boolean specifying if the IGES file contains MSBO (Manifold Solid B-Rep Object)
                entities. The default value is False.

            includedLayers=`()`[¶](#abaqus.Part.PartBase.AcisFile.openIges.includedLayers "Permalink to this definition")
            :   A sequence of Ints specifying the levels or layers of entities that will be translated
                from the IGES file to build the part. The default is to include all the layers.

            topology=`abaqusConstants.SOLID`[¶](#abaqus.Part.PartBase.AcisFile.openIges.topology "Permalink to this definition")
            :   A SymbolicConstant specifying the topology of the data to be read from the file and of
                the part to be created. Possible values are SOLID , SHELL, and WIRE. If
                **topology** = SOLID, Abaqus/CAE attempts to attach cells to create a solid. If
                **topology** = SHELL, Abaqus/CAE builds the body as a shell entity and not as a solid
                entity. The default value is SOLID.

            uniteWires=`1`[¶](#abaqus.Part.PartBase.AcisFile.openIges.uniteWires "Permalink to this definition")
            :   A SymbolicConstant specifying whether the imported wires need to be united or not.
                Possible values are ON and OFF. The default value is ON. When importing a sketch, this
                value is set to OFF.

        Returns:[¶](#abaqus.Part.PartBase.AcisFile.openIges-returns "Permalink to this headline")
        :   An AcisFile object.

        Return type:[¶](#abaqus.Part.PartBase.AcisFile.openIges-return-type "Permalink to this headline")
        :   [`AcisFile`](#abaqus.Part.PartBase.AcisFile "abaqus.Part.PartBase.AcisFile (Python class) — Bases: object")

        Raises:[¶](#abaqus.Part.PartBase.AcisFile.openIges-raises "Permalink to this headline")
        :   **Texterror** – Failed to read IGES file, The data in the IGES file are corrupted.

    openParasolid(*[fileName](#abaqus.Part.PartBase.AcisFile.openParasolid.fileName "abaqus.Part.PartBase.AcisFile.openParasolid.fileName (Python parameter) — A String specifying the path to the Parasolid file to open.")*, *[topology](#abaqus.Part.PartBase.AcisFile.openParasolid.topology "abaqus.Part.PartBase.AcisFile.openParasolid.topology (Python parameter) — A SymbolicConstant specifying the topology of the data to be read from the file and of the part to be created.")=`abaqusConstants.SOLID`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L213-L239)[¶](#abaqus.Part.PartBase.AcisFile.openParasolid "Permalink to this definition")
    :   This method creates an AcisFile object from a file containing Parasolid-format geometry. This object
        is subsequently used by the PartFromGeometryFile method.

        Note

        This function can be accessed by:

        ```python
        mdb.openAcis
        ```

        Note

        Check [AcisFile.openParasolid on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acisfilepyc.htm?contextscope=all#simaker-acisfileopenparasolidpyc).

        Parameters:[¶](#abaqus.Part.PartBase.AcisFile.openParasolid-parameters "Permalink to this headline")
        :   fileName[¶](#abaqus.Part.PartBase.AcisFile.openParasolid.fileName "Permalink to this definition")
            :   A String specifying the path to the Parasolid file to open.

            topology=`abaqusConstants.SOLID`[¶](#abaqus.Part.PartBase.AcisFile.openParasolid.topology "Permalink to this definition")
            :   A SymbolicConstant specifying the topology of the data to be read from the file and of
                the part to be created. Possible values are SOLID , SHELL, and WIRE. If
                **topology** = SOLID, Abaqus/CAE attempts to attach cells to create a solid. If
                **topology** = SHELL, Abaqus/CAE builds the body as a shell entity and not as a solid
                entity. The default value is SOLID.

        Returns:[¶](#abaqus.Part.PartBase.AcisFile.openParasolid-returns "Permalink to this headline")
        :   An AcisFile object.

        Return type:[¶](#abaqus.Part.PartBase.AcisFile.openParasolid-return-type "Permalink to this headline")
        :   [`AcisFile`](#abaqus.Part.PartBase.AcisFile "abaqus.Part.PartBase.AcisFile (Python class) — Bases: object")

    openSolidworks(*[fileName](#abaqus.Part.PartBase.AcisFile.openSolidworks.fileName "abaqus.Part.PartBase.AcisFile.openSolidworks.fileName (Python parameter) — A String specifying the path to the Solidworks file to open.")*, *[topology](#abaqus.Part.PartBase.AcisFile.openSolidworks.topology "abaqus.Part.PartBase.AcisFile.openSolidworks.topology (Python parameter) — A SymbolicConstant specifying the topology of the data to be read from the file and of the part to be created.")=`abaqusConstants.SOLID`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L298-L331)[¶](#abaqus.Part.PartBase.AcisFile.openSolidworks "Permalink to this definition")
    :   This method creates an AcisFile object from a file containing Solidworks format geometry. This object
        is subsequently used by the PartFromGeometryFile method.

        Note

        This function can be accessed by:

        ```python
        mdb.openAcis
        ```

        New in version 2020: The `openSolidworks` method was added.

        Note

        Check [AcisFile.openSolidworks on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acisfilepyc.htm?contextscope=all#simaker-acisfileopensolidworkspyc).

        Parameters:[¶](#abaqus.Part.PartBase.AcisFile.openSolidworks-parameters "Permalink to this headline")
        :   fileName[¶](#abaqus.Part.PartBase.AcisFile.openSolidworks.fileName "Permalink to this definition")
            :   A String specifying the path to the Solidworks file to open.

            topology=`abaqusConstants.SOLID`[¶](#abaqus.Part.PartBase.AcisFile.openSolidworks.topology "Permalink to this definition")
            :   A SymbolicConstant specifying the topology of the data to be read from the file and of
                the part to be created. Possible values are SOLID, SHELL, and WIRE. If **topology** = SOLID,
                Abaqus/CAE attempts to attach cells to create a solid entity. If **topology** = SHELL,
                Abaqus/CAE builds the body as a shell entity, not as a solid entity. The default value
                is SOLID.

        Returns:[¶](#abaqus.Part.PartBase.AcisFile.openSolidworks-returns "Permalink to this headline")
        :   An AcisFile object.

        Raises:[¶](#abaqus.Part.PartBase.AcisFile.openSolidworks-raises "Permalink to this headline")
        :   **Texterror** – Failed to read Solidworks file, The data in the Solidworks file are corrupted.

    openStep(*[fileName](#abaqus.Part.PartBase.AcisFile.openStep.fileName "abaqus.Part.PartBase.AcisFile.openStep.fileName (Python parameter) — A String specifying the path to the STEP file to open.")*, *[scale](#abaqus.Part.PartBase.AcisFile.openStep.scale "abaqus.Part.PartBase.AcisFile.openStep.scale (Python parameter) — A Float specifying the scaling factor to apply to the imported geometric entities.")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L241-L269)[¶](#abaqus.Part.PartBase.AcisFile.openStep "Permalink to this definition")
    :   This method creates an AcisFile object from a file containing STEP-format geometry. This object is
        subsequently used by the PartFromGeometryFile method.

        Note

        This function can be accessed by:

        ```python
        mdb.openAcis
        ```

        Note

        Check [AcisFile.openStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acisfilepyc.htm?contextscope=all#simaker-acisfileopensteppyc).

        Parameters:[¶](#abaqus.Part.PartBase.AcisFile.openStep-parameters "Permalink to this headline")
        :   fileName[¶](#abaqus.Part.PartBase.AcisFile.openStep.fileName "Permalink to this definition")
            :   A String specifying the path to the STEP file to open.

            scale=`1`[¶](#abaqus.Part.PartBase.AcisFile.openStep.scale "Permalink to this definition")
            :   A Float specifying the scaling factor to apply to the imported geometric entities. The
                default value is 1.0.

        Returns:[¶](#abaqus.Part.PartBase.AcisFile.openStep-returns "Permalink to this headline")
        :   An AcisFile object.

        Return type:[¶](#abaqus.Part.PartBase.AcisFile.openStep-return-type "Permalink to this headline")
        :   [`AcisFile`](#abaqus.Part.PartBase.AcisFile "abaqus.Part.PartBase.AcisFile (Python class) — Bases: object")

        Raises:[¶](#abaqus.Part.PartBase.AcisFile.openStep-raises "Permalink to this headline")
        :   **Texterror** – Failed to read STEP file, The data in the STEP file are corrupted.

    openVda(*[fileName](#abaqus.Part.PartBase.AcisFile.openVda.fileName "abaqus.Part.PartBase.AcisFile.openVda.fileName (Python parameter) — A String specifying the path to the VDA-FS file to open.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L271-L296)[¶](#abaqus.Part.PartBase.AcisFile.openVda "Permalink to this definition")
    :   This method creates an AcisFile object from a file containing VDA-FS-format geometry. This object is
        subsequently used by the PartFromGeometryFile method.

        Note

        This function can be accessed by:

        ```python
        mdb.openAcis
        ```

        Note

        Check [AcisFile.openVda on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acisfilepyc.htm?contextscope=all#simaker-acisfileopenvdapyc).

        Parameters:[¶](#abaqus.Part.PartBase.AcisFile.openVda-parameters "Permalink to this headline")
        :   fileName[¶](#abaqus.Part.PartBase.AcisFile.openVda.fileName "Permalink to this definition")
            :   A String specifying the path to the VDA-FS file to open.

        Returns:[¶](#abaqus.Part.PartBase.AcisFile.openVda-returns "Permalink to this headline")
        :   An AcisFile object.

        Return type:[¶](#abaqus.Part.PartBase.AcisFile.openVda-return-type "Permalink to this headline")
        :   [`AcisFile`](#abaqus.Part.PartBase.AcisFile "abaqus.Part.PartBase.AcisFile (Python class) — Bases: object")

        Raises:[¶](#abaqus.Part.PartBase.AcisFile.openVda-raises "Permalink to this headline")
        :   **Texterror** – Failed to read VDA file, The data in the VDA-FS file are corrupted.

    writeAcisFile(*[fileName](#abaqus.Part.PartBase.AcisFile.writeAcisFile.fileName "abaqus.Part.PartBase.AcisFile.writeAcisFile.fileName (Python parameter) — A String specifying the name of the file to which to write.")*, *[version](#abaqus.Part.PartBase.AcisFile.writeAcisFile.version "abaqus.Part.PartBase.AcisFile.writeAcisFile.version (Python parameter) — A Float specifying the ACIS version.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartBase.py#L333-L350)[¶](#abaqus.Part.PartBase.AcisFile.writeAcisFile "Permalink to this definition")
    :   This method exports the assembly to a named file in ACIS format.

        Note

        Check [AcisFile.writeAcisFile on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-acisfilepyc.htm?contextscope=all#simaker-acisfilewriteacisfilepyc).

        Parameters:[¶](#abaqus.Part.PartBase.AcisFile.writeAcisFile-parameters "Permalink to this headline")
        :   fileName[¶](#abaqus.Part.PartBase.AcisFile.writeAcisFile.fileName "Permalink to this definition")
            :   A String specifying the name of the file to which to write. The file name’s extension is
                used to determine whether a part or assembly is written. Use the file extension .asat
                for the assembly format.

                Changed in version 2018: Add description for thr file name’s extension.

            version=`None`[¶](#abaqus.Part.PartBase.AcisFile.writeAcisFile.version "Permalink to this definition")
            :   A Float specifying the ACIS version. For example, the Float 12.0 corresponds to ACIS
                Version 12.0. The default value is the current version of ACIS.

*class* AcisMdb(*[pathName](#abaqus.Part.AcisMdb.AcisMdb "abaqus.Part.AcisMdb.AcisMdb.__init__.pathName (Python parameter)")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/AcisMdb.py#L19-L333)[¶](#abaqus.Part.AcisMdb.AcisMdb "Permalink to this definition")
:   Bases: [`MdbBase`](../../index.html#abaqus.Mdb.MdbBase.MdbBase "abaqus.Mdb.MdbBase.MdbBase (Python class) — Bases: object")

    The Mdb object is the high-level Abaqus model database. A model database stores models and analysis
    controls.

    Note

    This object can be accessed by:

    ```python
    mdb
    ```

    Note

    Check [AcisMdb on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mdbpyc.htm?contextscope=all).

    Member Details:

    *static* openAcis(*[fileName](#abaqus.Part.AcisMdb.AcisMdb.openAcis.fileName "abaqus.Part.AcisMdb.AcisMdb.openAcis.fileName (Python parameter) — A String specifying the path to the ACIS file to open.")*, *[scaleFromFile](#abaqus.Part.AcisMdb.AcisMdb.openAcis.scaleFromFile "abaqus.Part.AcisMdb.AcisMdb.openAcis.scaleFromFile (Python parameter) — A Boolean specifying whether to scale, rotate, and translate the part using the transform read from the ACIS file.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/AcisMdb.py#L30-L61)[¶](#abaqus.Part.AcisMdb.AcisMdb.openAcis "Permalink to this definition")
    :   This method creates an AcisFile object from a file containing ACIS-format geometry. This object is
        subsequently used by the PartFromGeometryFile method.

        Note

        This function can be accessed by:

        ```python
        mdb.openAcis
        ```

        Note

        Check [AcisMdb.openAcis on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mdbpyc.htm?contextscope=all#simaker-mdbopenacispyc).

        Parameters:[¶](#abaqus.Part.AcisMdb.AcisMdb.openAcis-parameters "Permalink to this headline")
        :   fileName[¶](#abaqus.Part.AcisMdb.AcisMdb.openAcis.fileName "Permalink to this definition")
            :   A String specifying the path to the ACIS file to open.

            scaleFromFile=`0`[¶](#abaqus.Part.AcisMdb.AcisMdb.openAcis.scaleFromFile "Permalink to this definition")
            :   A Boolean specifying whether to scale, rotate, and translate the part using the
                transform read from the ACIS file. The default value is OFF.

        Returns:[¶](#abaqus.Part.AcisMdb.AcisMdb.openAcis-returns "Permalink to this headline")
        :   An AcisFile object.

        Return type:[¶](#abaqus.Part.AcisMdb.AcisMdb.openAcis-return-type "Permalink to this headline")
        :   `AcisFile`

        Raises:[¶](#abaqus.Part.AcisMdb.AcisMdb.openAcis-raises "Permalink to this headline")
        :   * **Texterror** – ACIS File version exceeds Kernel, File is from a newer version of ACIS than the CAE kernel.
            * **Texterror** – Failed to read ACIS file, The data in the ACIS file are corrupted.

    *static* openCatia(*[fileName](#abaqus.Part.AcisMdb.AcisMdb.openCatia.fileName "abaqus.Part.AcisMdb.AcisMdb.openCatia.fileName (Python parameter) — A String specifying the path to the CATIA file to open.")*, *[topology](#abaqus.Part.AcisMdb.AcisMdb.openCatia.topology "abaqus.Part.AcisMdb.AcisMdb.openCatia.topology (Python parameter) — A SymbolicConstant specifying the topology of the data to be read from the file and of the part to be created.")=`None`*, *[convertUnits](#abaqus.Part.AcisMdb.AcisMdb.openCatia.convertUnits "abaqus.Part.AcisMdb.AcisMdb.openCatia.convertUnits (Python parameter) — A SymbolicConstant specifying whether the original units should be retained.")=`0`*, *[combineBodies](#abaqus.Part.AcisMdb.AcisMdb.openCatia.combineBodies "abaqus.Part.AcisMdb.AcisMdb.openCatia.combineBodies (Python parameter) — A Boolean specifying whether to combine the bodies in the CATPart file.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/AcisMdb.py#L63-L102)[¶](#abaqus.Part.AcisMdb.AcisMdb.openCatia "Permalink to this definition")
    :   This method creates an AcisFile object from a file containing V5-format geometry. This object is
        subsequently used by the PartFromGeometryFile method.

        Note

        This function can be accessed by:

        ```python
        mdb.openCatia
        ```

        Note

        Check [AcisMdb.openCatia on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mdbpyc.htm?contextscope=all#simaker-mdbopencatiapyc).

        Parameters:[¶](#abaqus.Part.AcisMdb.AcisMdb.openCatia-parameters "Permalink to this headline")
        :   fileName[¶](#abaqus.Part.AcisMdb.AcisMdb.openCatia.fileName "Permalink to this definition")
            :   A String specifying the path to the CATIA file to open.

            topology=`None`[¶](#abaqus.Part.AcisMdb.AcisMdb.openCatia.topology "Permalink to this definition")
            :   A SymbolicConstant specifying the topology of the data to be read from the file and of
                the part to be created. Possible values are SOLID , SHELL, and WIRE. If
                **topology** = SOLID, Abaqus/CAE attempts to attach cells to create a solid. If
                **topology** = SHELL, Abaqus/CAE builds the body as a shell entity and not as a solid
                entity. The default value is SOLID .

            convertUnits=`0`[¶](#abaqus.Part.AcisMdb.AcisMdb.openCatia.convertUnits "Permalink to this definition")
            :   A SymbolicConstant specifying whether the original units should be retained. Possible
                values are ON and OFF. The default value is OFF.

            combineBodies=`0`[¶](#abaqus.Part.AcisMdb.AcisMdb.openCatia.combineBodies "Permalink to this definition")
            :   A Boolean specifying whether to combine the bodies in the CATPart file. If the bodies to
                be combined touch or overlap, invalid entities would result. For CATProduct files, this
                option will be ignored.

        Returns:[¶](#abaqus.Part.AcisMdb.AcisMdb.openCatia-returns "Permalink to this headline")
        :   An AcisFile object.

        Return type:[¶](#abaqus.Part.AcisMdb.AcisMdb.openCatia-return-type "Permalink to this headline")
        :   `AcisFile`

    *static* openEnf(*[fileName](#abaqus.Part.AcisMdb.AcisMdb.openEnf.fileName "abaqus.Part.AcisMdb.AcisMdb.openEnf.fileName (Python parameter) — A String specifying the path to the Elysium Neutral File that was created by I-DEAS, Pro/ENGINEER, or CATIA V5.")*, *[fileType](#abaqus.Part.AcisMdb.AcisMdb.openEnf.fileType "abaqus.Part.AcisMdb.AcisMdb.openEnf.fileType (Python parameter) — A String specifying the type of CAD system that created the file.")*, *[topology](#abaqus.Part.AcisMdb.AcisMdb.openEnf.topology "abaqus.Part.AcisMdb.AcisMdb.openEnf.topology (Python parameter) — A SymbolicConstant specifying the topology of the data to be read from the file and of the part to be created.")=`abaqusConstants.SOLID`*, *[convertUnits](#abaqus.Part.AcisMdb.AcisMdb.openEnf.convertUnits "abaqus.Part.AcisMdb.AcisMdb.openEnf.convertUnits (Python parameter) — A Boolean specifying if the dimensions of the part should be converted to millimeters. The default value is OFF.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/AcisMdb.py#L104-L145)[¶](#abaqus.Part.AcisMdb.AcisMdb.openEnf "Permalink to this definition")
    :   This method creates an AcisFile object from a file containing Elysium Neutral File-format geometry
        that was created by CATIA V5, I-DEAS, or Pro/ENGINEER. This object is subsequently used by the
        PartFromGeometryFile method.

        Note

        This function can be accessed by:

        ```python
        mdb.openEnf
        ```

        Note

        Check [AcisMdb.openEnf on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mdbpyc.htm?contextscope=all#simaker-mdbopenenfpyc).

        Parameters:[¶](#abaqus.Part.AcisMdb.AcisMdb.openEnf-parameters "Permalink to this headline")
        :   fileName[¶](#abaqus.Part.AcisMdb.AcisMdb.openEnf.fileName "Permalink to this definition")
            :   A String specifying the path to the Elysium Neutral File that was created by I-DEAS,
                Pro/ENGINEER, or CATIA V5.

            fileType[¶](#abaqus.Part.AcisMdb.AcisMdb.openEnf.fileType "Permalink to this definition")
            :   A String specifying the type of CAD system that created the file. Possible values are
                “ideas”, “proe”, or “catiav5” or a combination similar to “proe/ideas/catiav5” if the
                type is unknown.

            topology=`abaqusConstants.SOLID`[¶](#abaqus.Part.AcisMdb.AcisMdb.openEnf.topology "Permalink to this definition")
            :   A SymbolicConstant specifying the topology of the data to be read from the file and of
                the part to be created. Possible values are SOLID , SHELL, and WIRE. If
                **topology** = SOLID, Abaqus/CAE attempts to attach cells to create a solid. If
                **topology** = SHELL, Abaqus/CAE builds the body as a shell entity and not as a solid
                entity. The default value is SOLID.

            convertUnits=`0`[¶](#abaqus.Part.AcisMdb.AcisMdb.openEnf.convertUnits "Permalink to this definition")
            :   A Boolean specifying if the dimensions of the part should be converted to millimeters.
                The default value is OFF.

        Returns:[¶](#abaqus.Part.AcisMdb.AcisMdb.openEnf-returns "Permalink to this headline")
        :   An AcisFile object.

        Return type:[¶](#abaqus.Part.AcisMdb.AcisMdb.openEnf-return-type "Permalink to this headline")
        :   `AcisFile`

    *static* openIges(*[fileName](#abaqus.Part.AcisMdb.AcisMdb.openIges.fileName "abaqus.Part.AcisMdb.AcisMdb.openIges.fileName (Python parameter) — A String specifying the path to the IGES file to open.")*, *[trimCurve](#abaqus.Part.AcisMdb.AcisMdb.openIges.trimCurve "abaqus.Part.AcisMdb.AcisMdb.openIges.trimCurve (Python parameter) — A SymbolicConstant specifying the method used to define the trim curves that bound parametric surfaces.")=`abaqusConstants.DEFAULT`*, *[scaleFromFile](#abaqus.Part.AcisMdb.AcisMdb.openIges.scaleFromFile "abaqus.Part.AcisMdb.AcisMdb.openIges.scaleFromFile (Python parameter) — A SymbolicConstant specifying whether the imported geometry needs to be scaled using the units information available in the IGES file.")=`0`*, *[msbo](#abaqus.Part.AcisMdb.AcisMdb.openIges.msbo "abaqus.Part.AcisMdb.AcisMdb.openIges.msbo (Python parameter) — A Boolean specifying if the IGES file contains MSBO (Manifold Solid B-Rep Object) entities.")=`False`*, *[includedLayers](#abaqus.Part.AcisMdb.AcisMdb.openIges.includedLayers "abaqus.Part.AcisMdb.AcisMdb.openIges.includedLayers (Python parameter) — A sequence of Ints specifying the levels or layers of entities that will be translated from the IGES file to build the part.")=`()`*, *[topology](#abaqus.Part.AcisMdb.AcisMdb.openIges.topology "abaqus.Part.AcisMdb.AcisMdb.openIges.topology (Python parameter) — A SymbolicConstant specifying the topology of the data to be read from the file and of the part to be created.")=`abaqusConstants.SOLID`*, *[uniteWires](#abaqus.Part.AcisMdb.AcisMdb.openIges.uniteWires "abaqus.Part.AcisMdb.AcisMdb.openIges.uniteWires (Python parameter) — A SymbolicConstant specifying whether the imported wires need to be united or not. Possible values are ON and OFF.")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/AcisMdb.py#L147-L209)[¶](#abaqus.Part.AcisMdb.AcisMdb.openIges "Permalink to this definition")
    :   This method creates an AcisFile object from a file containing IGES-format geometry. This object is
        subsequently used by the PartFromGeometryFile method.

        Note

        This function can be accessed by:

        ```python
        mdb.openIges
        ```

        Note

        Check [AcisMdb.openIges on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mdbpyc.htm?contextscope=all#simaker-mdbopenigespyc).

        Parameters:[¶](#abaqus.Part.AcisMdb.AcisMdb.openIges-parameters "Permalink to this headline")
        :   fileName[¶](#abaqus.Part.AcisMdb.AcisMdb.openIges.fileName "Permalink to this definition")
            :   A String specifying the path to the IGES file to open.

            trimCurve=`abaqusConstants.DEFAULT`[¶](#abaqus.Part.AcisMdb.AcisMdb.openIges.trimCurve "Permalink to this definition")
            :   A SymbolicConstant specifying the method used to define the trim curves that bound
                parametric surfaces. Possible values are:DEFAULT, use either of the following as
                specified by the contents of the IGES file.PARAMETRIC\_DATA, use the parameter space of
                the surface being trimmed.THREED\_DATA, use real space—the coordinate system of the part
                along with an indication that the trim curve lies on the parametric surface.The default
                value is DEFAULT.

            scaleFromFile=`0`[¶](#abaqus.Part.AcisMdb.AcisMdb.openIges.scaleFromFile "Permalink to this definition")
            :   A SymbolicConstant specifying whether the imported geometry needs to be scaled using the
                units information available in the IGES file. Possible values are ON and OFF. The
                default value is OFF. When the argument is set to ON, the geometry is scaled to
                millimeters with respect to the unit system specified in the IGES file.

            msbo=`False`[¶](#abaqus.Part.AcisMdb.AcisMdb.openIges.msbo "Permalink to this definition")
            :   A Boolean specifying if the IGES file contains MSBO (Manifold Solid B-Rep Object)
                entities. The default value is False.

            includedLayers=`()`[¶](#abaqus.Part.AcisMdb.AcisMdb.openIges.includedLayers "Permalink to this definition")
            :   A sequence of Ints specifying the levels or layers of entities that will be translated
                from the IGES file to build the part. The default is to include all the layers.

            topology=`abaqusConstants.SOLID`[¶](#abaqus.Part.AcisMdb.AcisMdb.openIges.topology "Permalink to this definition")
            :   A SymbolicConstant specifying the topology of the data to be read from the file and of
                the part to be created. Possible values are SOLID , SHELL, and WIRE. If
                **topology** = SOLID, Abaqus/CAE attempts to attach cells to create a solid. If
                **topology** = SHELL, Abaqus/CAE builds the body as a shell entity and not as a solid
                entity. The default value is SOLID.

            uniteWires=`1`[¶](#abaqus.Part.AcisMdb.AcisMdb.openIges.uniteWires "Permalink to this definition")
            :   A SymbolicConstant specifying whether the imported wires need to be united or not.
                Possible values are ON and OFF. The default value is ON. When importing a sketch, this
                value is set to OFF.

        Returns:[¶](#abaqus.Part.AcisMdb.AcisMdb.openIges-returns "Permalink to this headline")
        :   An AcisFile object.

        Return type:[¶](#abaqus.Part.AcisMdb.AcisMdb.openIges-return-type "Permalink to this headline")
        :   `AcisFile`

        Raises:[¶](#abaqus.Part.AcisMdb.AcisMdb.openIges-raises "Permalink to this headline")
        :   **Texterror** – Failed to read IGES file, The data in the IGES file are corrupted.

    *static* openParasolid(*[fileName](#abaqus.Part.AcisMdb.AcisMdb.openParasolid.fileName "abaqus.Part.AcisMdb.AcisMdb.openParasolid.fileName (Python parameter) — A String specifying the path to the Parasolid file to open.")*, *[topology](#abaqus.Part.AcisMdb.AcisMdb.openParasolid.topology "abaqus.Part.AcisMdb.AcisMdb.openParasolid.topology (Python parameter) — A SymbolicConstant specifying the topology of the data to be read from the file and of the part to be created.")=`abaqusConstants.SOLID`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/AcisMdb.py#L211-L238)[¶](#abaqus.Part.AcisMdb.AcisMdb.openParasolid "Permalink to this definition")
    :   This method creates an AcisFile object from a file containing Parasolid-format geometry. This object
        is subsequently used by the PartFromGeometryFile method.

        Note

        This function can be accessed by:

        ```python
        mdb.openParasolid
        ```

        Note

        Check [AcisMdb.openParasolid on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mdbpyc.htm?contextscope=all#simaker-mdbopenparasolidpyc).

        Parameters:[¶](#abaqus.Part.AcisMdb.AcisMdb.openParasolid-parameters "Permalink to this headline")
        :   fileName[¶](#abaqus.Part.AcisMdb.AcisMdb.openParasolid.fileName "Permalink to this definition")
            :   A String specifying the path to the Parasolid file to open.

            topology=`abaqusConstants.SOLID`[¶](#abaqus.Part.AcisMdb.AcisMdb.openParasolid.topology "Permalink to this definition")
            :   A SymbolicConstant specifying the topology of the data to be read from the file and of
                the part to be created. Possible values are SOLID , SHELL, and WIRE. If
                **topology** = SOLID, Abaqus/CAE attempts to attach cells to create a solid. If
                **topology** = SHELL, Abaqus/CAE builds the body as a shell entity and not as a solid
                entity. The default value is SOLID.

        Returns:[¶](#abaqus.Part.AcisMdb.AcisMdb.openParasolid-returns "Permalink to this headline")
        :   An AcisFile object.

        Return type:[¶](#abaqus.Part.AcisMdb.AcisMdb.openParasolid-return-type "Permalink to this headline")
        :   `AcisFile`

    *static* openSolidworks(*[fileName](#abaqus.Part.AcisMdb.AcisMdb.openSolidworks.fileName "abaqus.Part.AcisMdb.AcisMdb.openSolidworks.fileName (Python parameter) — A String specifying the path to the Solidworks file to open.")*, *[topology](#abaqus.Part.AcisMdb.AcisMdb.openSolidworks.topology "abaqus.Part.AcisMdb.AcisMdb.openSolidworks.topology (Python parameter) — A SymbolicConstant specifying the topology of the data to be read from the file and of the part to be created.")=`abaqusConstants.SOLID`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/AcisMdb.py#L299-L333)[¶](#abaqus.Part.AcisMdb.AcisMdb.openSolidworks "Permalink to this definition")
    :   This method creates an AcisFile object from a file containing Solidworks format geometry. This object
        is subsequently used by the PartFromGeometryFile method.

        Note

        This function can be accessed by:

        ```python
        openSolidworks
        ```

        New in version 2020: The `openSolidworks` method was added.

        Note

        Check [AcisMdb.openSolidworks on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mdbpyc.htm?contextscope=all#simaker-mdbopensolidworkspyc).

        Parameters:[¶](#abaqus.Part.AcisMdb.AcisMdb.openSolidworks-parameters "Permalink to this headline")
        :   fileName[¶](#abaqus.Part.AcisMdb.AcisMdb.openSolidworks.fileName "Permalink to this definition")
            :   A String specifying the path to the Solidworks file to open.

            topology=`abaqusConstants.SOLID`[¶](#abaqus.Part.AcisMdb.AcisMdb.openSolidworks.topology "Permalink to this definition")
            :   A SymbolicConstant specifying the topology of the data to be read from the file and of
                the part to be created. Possible values are SOLID, SHELL, and WIRE. If **topology** = SOLID,
                Abaqus/CAE attempts to attach cells to create a solid entity. If **topology** = SHELL,
                Abaqus/CAE builds the body as a shell entity, not as a solid entity. The default value
                is SOLID.

        Returns:[¶](#abaqus.Part.AcisMdb.AcisMdb.openSolidworks-returns "Permalink to this headline")
        :   An AcisFile object.

        Raises:[¶](#abaqus.Part.AcisMdb.AcisMdb.openSolidworks-raises "Permalink to this headline")
        :   **Texterror** – Failed to read Solidworks file, The data in the Solidworks file are corrupted.

    *static* openStep(*[fileName](#abaqus.Part.AcisMdb.AcisMdb.openStep.fileName "abaqus.Part.AcisMdb.AcisMdb.openStep.fileName (Python parameter) — A String specifying the path to the STEP file to open.")*, *[scale](#abaqus.Part.AcisMdb.AcisMdb.openStep.scale "abaqus.Part.AcisMdb.AcisMdb.openStep.scale (Python parameter) — A Float specifying the scaling factor to apply to the imported geometric entities.")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/AcisMdb.py#L240-L269)[¶](#abaqus.Part.AcisMdb.AcisMdb.openStep "Permalink to this definition")
    :   This method creates an AcisFile object from a file containing STEP-format geometry. This object is
        subsequently used by the PartFromGeometryFile method.

        Note

        This function can be accessed by:

        ```python
        mdb.openStep
        ```

        Note

        Check [AcisMdb.openStep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mdbpyc.htm?contextscope=all#simaker-mdbopensteppyc).

        Parameters:[¶](#abaqus.Part.AcisMdb.AcisMdb.openStep-parameters "Permalink to this headline")
        :   fileName[¶](#abaqus.Part.AcisMdb.AcisMdb.openStep.fileName "Permalink to this definition")
            :   A String specifying the path to the STEP file to open.

            scale=`1`[¶](#abaqus.Part.AcisMdb.AcisMdb.openStep.scale "Permalink to this definition")
            :   A Float specifying the scaling factor to apply to the imported geometric entities. The
                default value is 1.0.

        Returns:[¶](#abaqus.Part.AcisMdb.AcisMdb.openStep-returns "Permalink to this headline")
        :   An AcisFile object.

        Return type:[¶](#abaqus.Part.AcisMdb.AcisMdb.openStep-return-type "Permalink to this headline")
        :   `AcisFile`

        Raises:[¶](#abaqus.Part.AcisMdb.AcisMdb.openStep-raises "Permalink to this headline")
        :   **Texterror** – Failed to read STEP file, The data in the STEP file are corrupted.

    *static* openVda(*[fileName](#abaqus.Part.AcisMdb.AcisMdb.openVda.fileName "abaqus.Part.AcisMdb.AcisMdb.openVda.fileName (Python parameter) — A String specifying the path to the VDA-FS file to open.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/AcisMdb.py#L271-L297)[¶](#abaqus.Part.AcisMdb.AcisMdb.openVda "Permalink to this definition")
    :   This method creates an AcisFile object from a file containing VDA-FS-format geometry. This object is
        subsequently used by the PartFromGeometryFile method.

        Note

        This function can be accessed by:

        ```python
        mdb.openVda
        ```

        Note

        Check [AcisMdb.openVda on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mdbpyc.htm?contextscope=all#simaker-mdbopenvdapyc).

        Parameters:[¶](#abaqus.Part.AcisMdb.AcisMdb.openVda-parameters "Permalink to this headline")
        :   fileName[¶](#abaqus.Part.AcisMdb.AcisMdb.openVda.fileName "Permalink to this definition")
            :   A String specifying the path to the VDA-FS file to open.

        Returns:[¶](#abaqus.Part.AcisMdb.AcisMdb.openVda-returns "Permalink to this headline")
        :   An AcisFile object.

        Return type:[¶](#abaqus.Part.AcisMdb.AcisMdb.openVda-return-type "Permalink to this headline")
        :   `AcisFile`

        Raises:[¶](#abaqus.Part.AcisMdb.AcisMdb.openVda-raises "Permalink to this headline")
        :   **Texterror** – Failed to read VDA file, The data in the VDA-FS file are corrupted.

*class* Part(*[name](#abaqus.Part.PartModel.Part "abaqus.Part.PartModel.Part.__init__.name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[dimensionality](#abaqus.Part.PartModel.Part "abaqus.Part.PartModel.Part.__init__.dimensionality (Python parameter)"): [SymbolicConstant](../../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.SymbolicConstant "abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant (Python class)")*, *[type](#abaqus.Part.PartModel.Part "abaqus.Part.PartModel.Part.__init__.type (Python parameter)"): [SymbolicConstant](../../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.SymbolicConstant "abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant (Python class)")*, *[twist](#abaqus.Part.PartModel.Part "abaqus.Part.PartModel.Part.__init__.twist (Python parameter)"): [AbaqusBoolean](../../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.AbaqusBoolean "abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean (Python class)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `OFF`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartModel.py#L14-L30)[¶](#abaqus.Part.PartModel.Part "Permalink to this definition")

*class* Part(*[name](#abaqus.Part.PartModel.Part "abaqus.Part.PartModel.Part.__init__.name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[objectToCopy](#abaqus.Part.PartModel.Part "abaqus.Part.PartModel.Part.__init__.objectToCopy (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[scale](#abaqus.Part.PartModel.Part "abaqus.Part.PartModel.Part.__init__.scale (Python parameter)"): [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") = `1`*, *[mirrorPlane](#abaqus.Part.PartModel.Part "abaqus.Part.PartModel.Part.__init__.mirrorPlane (Python parameter)"): [SymbolicConstant](../../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.SymbolicConstant "abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant (Python class)") = `NONE`*, *[compressFeatureList](#abaqus.Part.PartModel.Part "abaqus.Part.PartModel.Part.__init__.compressFeatureList (Python parameter)"): [AbaqusBoolean](../../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.AbaqusBoolean "abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean (Python class)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `OFF`*, *[separate](#abaqus.Part.PartModel.Part "abaqus.Part.PartModel.Part.__init__.separate (Python parameter)"): [AbaqusBoolean](../../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.AbaqusBoolean "abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean (Python class)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `OFF`*)
:   Bases: [`BasicGeometryPart`](geometry.html#abaqus.BasicGeometry.BasicGeometryPart.BasicGeometryPart "abaqus.BasicGeometry.BasicGeometryPart.BasicGeometryPart (Python class) — Bases: PartBase"), [`MeshEditPart`](../../edit_mesh.html#abaqus.EditMesh.MeshEditPart.MeshEditPart "abaqus.EditMesh.MeshEditPart.MeshEditPart (Python class) — Bases: PartBase"), [`MeshPart`](../mesh.html#abaqus.Mesh.MeshPart.MeshPart "abaqus.Mesh.MeshPart.MeshPart (Python class) — Bases: PartBase"), [`PropertyPart`](../property.html#abaqus.Property.PropertyPart.PropertyPart "abaqus.Property.PropertyPart.PropertyPart (Python class) — Bases: PartBase"), [`RegionPart`](region.html#abaqus.Region.RegionPart.RegionPart "abaqus.Region.RegionPart.RegionPart (Python class) — Bases: RegionPartBase"), [`Displayable`](../../../session/canvas.html#abaqus.Canvas.ViewportBase.Displayable "abaqus.Canvas.Displayable.Displayable (Python class)")

    The Part object defines the physical attributes of a structure. Parts are instanced into the assembly and
    positioned before an analysis.

    Note

    This object can be accessed by:

    ```python
    import part
    mdb.models[name].parts[name]
    ```

    Note

    Check [Part on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all).

    Member Details:

    insertElements(*[faces](#abaqus.Part.PartModel.Part.insertElements "abaqus.Part.PartModel.Part.insertElements.faces (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartModel.py#L28-L30)[¶](#abaqus.Part.PartModel.Part.insertElements "Permalink to this definition")
    :   Insert elements on the Part.

*class* PartFeature[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L32-L2564)[¶](#abaqus.Part.PartFeature.PartFeature "Permalink to this definition")
:   Bases: [`Feature`](feature.html#abaqus.Feature.Feature.Feature "abaqus.Feature.Feature.Feature (Python class) — Bases: object")

    The following commands operate on Feature objects. For more information about the Feature object, see
    Feature object.

    Note

    This object can be accessed by:

    ```python
    import part
    ```

    Note

    Check [PartFeature on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partfeaturepyc.htm?contextscope=all).

    Member Details:

    AddCells(*[faceList](#abaqus.Part.PartFeature.PartFeature.AddCells.faceList "abaqus.Part.PartFeature.PartFeature.AddCells.faceList (Python parameter) — A sequence of Face objects specifying the faces bounding the cell to add.")*, *[flipped](#abaqus.Part.PartFeature.PartFeature.AddCells.flipped "abaqus.Part.PartFeature.PartFeature.AddCells.flipped (Python parameter) — A Boolean specifying the direction of feature creation.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L65-L92)[¶](#abaqus.Part.PartFeature.PartFeature.AddCells "Permalink to this definition")
    :   This method tries to convert a shell entity to a solid entity. The conversion is not always
        successful.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [AddCells on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-addcellspyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.AddCells-parameters "Permalink to this headline")
        :   faceList[¶](#abaqus.Part.PartFeature.PartFeature.AddCells.faceList "Permalink to this definition")
            :   A sequence of Face objects specifying the faces bounding the cell to add.

            flipped=`0`[¶](#abaqus.Part.PartFeature.PartFeature.AddCells.flipped "Permalink to this definition")
            :   A Boolean specifying the direction of feature creation. The possible values are True and
                False. The default is True indicating that the direction is opposite to the face normal.
                When multiple faces are selected, Abaqus attempts to create cells on both sides of the
                selected faces and ignores the **flipped** argument.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.AddCells-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.AddCells-return-type "Permalink to this headline")
        :   `Feature`

    AnalyticRigidSurf2DPlanar(*[sketch](#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurf2DPlanar.sketch "abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurf2DPlanar.sketch (Python parameter) — A ConstrainedSketch object specifying the planar wire.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L94-L116)[¶](#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurf2DPlanar "Permalink to this definition")
    :   This method creates a first Feature object for an analytical rigid surface by creating a planar wire
        from the given ConstrainedSketch object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [AnalyticRigidSurf2DPlanar on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticrigidsurf2dplanarpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurf2DPlanar-parameters "Permalink to this headline")
        :   sketch[¶](#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurf2DPlanar.sketch "Permalink to this definition")
            :   A ConstrainedSketch object specifying the planar wire.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurf2DPlanar-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurf2DPlanar-return-type "Permalink to this headline")
        :   `Feature`

    AnalyticRigidSurfExtrude(*[sketch](#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfExtrude.sketch "abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfExtrude.sketch (Python parameter) — A ConstrainedSketch object specifying the planar wire.")*, *[depth](#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfExtrude.depth "abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfExtrude.depth (Python parameter) — A Float specifying the extrusion depth.")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L118-L142)[¶](#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfExtrude "Permalink to this definition")
    :   This method creates a first Feature object for an analytical rigid surface by extruding the given
        ConstrainedSketch object by the given depth, creating a surface.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [AnalyticRigidSurfExtrude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticrigidsurfextrudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfExtrude-parameters "Permalink to this headline")
        :   sketch[¶](#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfExtrude.sketch "Permalink to this definition")
            :   A ConstrainedSketch object specifying the planar wire.

            depth=`1`[¶](#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfExtrude.depth "Permalink to this definition")
            :   A Float specifying the extrusion depth. The default value is 1.0.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfExtrude-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfExtrude-return-type "Permalink to this headline")
        :   `Feature`

    AnalyticRigidSurfRevolve(*[sketch](#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfRevolve.sketch "abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfRevolve.sketch (Python parameter) — A ConstrainedSketch object specifying the surface to be revolved.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L144-L166)[¶](#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfRevolve "Permalink to this definition")
    :   This method creates a first Feature object for an analytical rigid surface by revolving the given
        ConstrainedSketch object by 360° about the **Y** axis.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [AnalyticRigidSurfRevolve on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticrigidsurfrevolvepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfRevolve-parameters "Permalink to this headline")
        :   sketch[¶](#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfRevolve.sketch "Permalink to this definition")
            :   A ConstrainedSketch object specifying the surface to be revolved.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfRevolve-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfRevolve-return-type "Permalink to this headline")
        :   `Feature`

    AssignMidsurfaceRegion(*[cellList](#abaqus.Part.PartFeature.PartFeature.AssignMidsurfaceRegion.cellList "abaqus.Part.PartFeature.PartFeature.AssignMidsurfaceRegion.cellList (Python parameter) — A sequence of Cell objects specifying the regions that will be used for mid-surface construction.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L168-L192)[¶](#abaqus.Part.PartFeature.PartFeature.AssignMidsurfaceRegion "Permalink to this definition")
    :   This method assign a mid-surface property to sequence of Cell objects. If a reference representation
        of the part does not exist, it creates one. It also copies the **cells** to the reference representation
        and deletes the **cells** from the active representation of the part.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [AssignMidsurfaceRegion on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assignmidsurfaceregionpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.AssignMidsurfaceRegion-parameters "Permalink to this headline")
        :   cellList[¶](#abaqus.Part.PartFeature.PartFeature.AssignMidsurfaceRegion.cellList "Permalink to this definition")
            :   A sequence of Cell objects specifying the regions that will be used for mid-surface
                construction. These regions will be copied to the reference representation of the part.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.AssignMidsurfaceRegion-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.AssignMidsurfaceRegion-return-type "Permalink to this headline")
        :   `Feature`

    AutoRepair()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L43-L63)[¶](#abaqus.Part.PartFeature.PartFeature.AutoRepair "Permalink to this definition")
    :   This method carries out a sequence of geometry repair operations if it contains invalid entities. It
        is expected to improve the geometry, but it does not guarantee that the number of invalid entities will
        decrease. In some cases, it can also increase the number of invalid entities. Since a number of geometry
        repair operations and validity checks are performed, it could be a slow operation depending on the
        complexity of the geometry.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.AutoRepair-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.AutoRepair-return-type "Permalink to this headline")
        :   `Feature`

    BaseShell(*[sketch](#abaqus.Part.PartFeature.PartFeature.BaseShell.sketch "abaqus.Part.PartFeature.PartFeature.BaseShell.sketch (Python parameter) — A ConstrainedSketch object specifying the planar shell.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L328-L350)[¶](#abaqus.Part.PartFeature.PartFeature.BaseShell "Permalink to this definition")
    :   This method creates a first Feature object by creating a planar shell from the given
        ConstrainedSketch object. The ConstrainedSketch object must define a closed profile.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [BaseShell on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-baseshellpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.BaseShell-parameters "Permalink to this headline")
        :   sketch[¶](#abaqus.Part.PartFeature.PartFeature.BaseShell.sketch "Permalink to this definition")
            :   A ConstrainedSketch object specifying the planar shell.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.BaseShell-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.BaseShell-return-type "Permalink to this headline")
        :   `Feature`

    BaseShellExtrude(*[sketch](#abaqus.Part.PartFeature.PartFeature.BaseShellExtrude.sketch "abaqus.Part.PartFeature.PartFeature.BaseShellExtrude.sketch (Python parameter) — A ConstrainedSketch object specifying the shape to be extruded.")*, *[depth](#abaqus.Part.PartFeature.PartFeature.BaseShellExtrude.depth "abaqus.Part.PartFeature.PartFeature.BaseShellExtrude.depth (Python parameter) — A Float specifying the extrusion depth.")*, *[draftAngle](#abaqus.Part.PartFeature.PartFeature.BaseShellExtrude.draftAngle "abaqus.Part.PartFeature.PartFeature.BaseShellExtrude.draftAngle (Python parameter) — A Float specifying the draft angle in degrees.")=`None`*, *[pitch](#abaqus.Part.PartFeature.PartFeature.BaseShellExtrude.pitch "abaqus.Part.PartFeature.PartFeature.BaseShellExtrude.pitch (Python parameter) — A Float specifying the pitch.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L352-L399)[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellExtrude "Permalink to this definition")
    :   This method creates a first Feature object by extruding the given ConstrainedSketch object by the
        given depth, creating a shell. The ConstrainedSketch object can define either an open or closed profile.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [BaseShellExtrude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-baseshellextrudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellExtrude-parameters "Permalink to this headline")
        :   sketch[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellExtrude.sketch "Permalink to this definition")
            :   A ConstrainedSketch object specifying the shape to be extruded.

            depth[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellExtrude.depth "Permalink to this definition")
            :   A Float specifying the extrusion depth. Possible values are Floats > 0.

            draftAngle=`None`[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellExtrude.draftAngle "Permalink to this definition")
            :   A Float specifying the draft angle in degrees. Possible values are -90.0 ≤ **draftAngle**
                ≤ 90.0. By convention, for a positive draft angle an outer loop will draft outward and
                an inner loop will draft inward. The opposite is true for a negative draft angle. The
                default value, 0, implies a normal extrude. The arguments **draftAngle** and **pitch** are
                mutually exclusive.

            pitch=`None`[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellExtrude.pitch "Permalink to this definition")
            :   A Float specifying the pitch. The pitch is the distance traveled along the axial
                direction by the sketch when the sketch has completed one full revolution about the
                twist axis. Pitch can be specified as positive or negative to achieve right-handed or
                left-handed twist about the twist axis, respectively. The default value, 0, implies a
                normal extrude. Possible values are -10⁵ ≤ **pitch** ≤ 10⁵. The arguments **draftAngle**
                and **pitch** are mutually exclusive.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellExtrude-returns "Permalink to this headline")
        :   A Feature object.

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellExtrude-return-type "Permalink to this headline")
        :   `Feature`

        Raises:[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellExtrude-raises "Permalink to this headline")
        :   **RangeError** –

    BaseShellRevolve(*[sketch](#abaqus.Part.PartFeature.PartFeature.BaseShellRevolve.sketch "abaqus.Part.PartFeature.PartFeature.BaseShellRevolve.sketch (Python parameter) — A ConstrainedSketch object specifying the shape to be revolved.")*, *[angle](#abaqus.Part.PartFeature.PartFeature.BaseShellRevolve.angle "abaqus.Part.PartFeature.PartFeature.BaseShellRevolve.angle (Python parameter) — A Float specifying the revolve angle in degrees.")*, *[pitch](#abaqus.Part.PartFeature.PartFeature.BaseShellRevolve.pitch "abaqus.Part.PartFeature.PartFeature.BaseShellRevolve.pitch (Python parameter) — A Float specifying the pitch.")=`None`*, *[flipRevolveDirection](#abaqus.Part.PartFeature.PartFeature.BaseShellRevolve.flipRevolveDirection "abaqus.Part.PartFeature.PartFeature.BaseShellRevolve.flipRevolveDirection (Python parameter) — A Boolean specifying whether to override the direction of feature creation.")=`0`*, *[flipPitchDirection](#abaqus.Part.PartFeature.PartFeature.BaseShellRevolve.flipPitchDirection "abaqus.Part.PartFeature.PartFeature.BaseShellRevolve.flipPitchDirection (Python parameter) — A Boolean specifying whether to override the direction of translation.")=`0`*, *[moveSketchNormalToPath](#abaqus.Part.PartFeature.PartFeature.BaseShellRevolve.moveSketchNormalToPath "abaqus.Part.PartFeature.PartFeature.BaseShellRevolve.moveSketchNormalToPath (Python parameter) — A Boolean specifying whether to rotate the sketch so that it is normal to the path of revolution when using the pitch option.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L401-L455)[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellRevolve "Permalink to this definition")
    :   This method creates a first Feature object by revolving the given ConstrainedSketch object by the
        given angle, creating a shell. The ConstrainedSketch object can define either an open or closed profile
        and an axis of revolution. The axis is defined by a single construction line.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [BaseShellRevolve on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-baseshellrevolvepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellRevolve-parameters "Permalink to this headline")
        :   sketch[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellRevolve.sketch "Permalink to this definition")
            :   A ConstrainedSketch object specifying the shape to be revolved.

            angle[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellRevolve.angle "Permalink to this definition")
            :   A Float specifying the revolve angle in degrees. Possible values are 0 ≤ **angle** ≤
                360. Note: If **pitch** > 0, there is no upper limit for **angle**.

            pitch=`None`[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellRevolve.pitch "Permalink to this definition")
            :   A Float specifying the pitch. The pitch is the distance traveled along the axial
                direction, measured between corresponding points on the sketch when it has completed one
                full revolution about the axis of revolution. Possible values are 0 ≤ **pitch** ≤ 10⁵.
                The default value, 0, implies a normal revolve.

            flipRevolveDirection=`0`[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellRevolve.flipRevolveDirection "Permalink to this definition")
            :   A Boolean specifying whether to override the direction of feature creation. If
                **flipRevolveDirection** = OFF, the default direction of revolution is used. If
                **flipRevolveDirection** = ON, the revolve direction is reversed. The default value is OFF.

            flipPitchDirection=`0`[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellRevolve.flipPitchDirection "Permalink to this definition")
            :   A Boolean specifying whether to override the direction of translation. If
                **flipPitchDirection** = OFF, the direction of translation is given by the direction of the
                revolve axis. If **flipPitchDirection** = ON, the translation direction is reversed. The
                default value is OFF.

            moveSketchNormalToPath=`0`[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellRevolve.moveSketchNormalToPath "Permalink to this definition")
            :   A Boolean specifying whether to rotate the sketch so that it is normal to the path of
                revolution when using the **pitch** option. If **moveSketchNormalToPath** = OFF, the sketch
                plane remains parallel to the revolve axis. If **moveSketchNormalToPath** = ON, the sketch
                is moved to match the angle created by the **pitch** before being revolved. The default
                value is OFF.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellRevolve-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellRevolve-return-type "Permalink to this headline")
        :   `Feature`

    BaseShellSweep(*[sketch](#abaqus.Part.PartFeature.PartFeature.BaseShellSweep.sketch "abaqus.Part.PartFeature.PartFeature.BaseShellSweep.sketch (Python parameter) — A ConstrainedSketch object specifying the section to be swept.")*, *[path](#abaqus.Part.PartFeature.PartFeature.BaseShellSweep.path "abaqus.Part.PartFeature.PartFeature.BaseShellSweep.path (Python parameter) — A ConstrainedSketch object specifying the path of the sweep.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L457-L484)[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellSweep "Permalink to this definition")
    :   This method creates a first Feature object by sweeping the given section ConstrainedSketch object
        along the path defined by the path ConstrainedSketch object, creating a shell. The ConstrainedSketch
        object can define either an open or closed profile. The origin of the profile sketch is positioned at
        the start of the sweep path and swept perpendicular to the path. No checks are made for self-
        intersection.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [BaseShellSweep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-baseshellsweeppyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellSweep-parameters "Permalink to this headline")
        :   sketch[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellSweep.sketch "Permalink to this definition")
            :   A ConstrainedSketch object specifying the section to be swept.

            path[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellSweep.path "Permalink to this definition")
            :   A ConstrainedSketch object specifying the path of the sweep.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellSweep-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.BaseShellSweep-return-type "Permalink to this headline")
        :   `Feature`

    BaseSolidExtrude(*[sketch](#abaqus.Part.PartFeature.PartFeature.BaseSolidExtrude.sketch "abaqus.Part.PartFeature.PartFeature.BaseSolidExtrude.sketch (Python parameter) — A ConstrainedSketch object specifying the plane shape to be extruded.")*, *[depth](#abaqus.Part.PartFeature.PartFeature.BaseSolidExtrude.depth "abaqus.Part.PartFeature.PartFeature.BaseSolidExtrude.depth (Python parameter) — A Float specifying the extrusion depth.")*, *[draftAngle](#abaqus.Part.PartFeature.PartFeature.BaseSolidExtrude.draftAngle "abaqus.Part.PartFeature.PartFeature.BaseSolidExtrude.draftAngle (Python parameter) — A Float specifying the draft angle in degrees.")=`None`*, *[pitch](#abaqus.Part.PartFeature.PartFeature.BaseSolidExtrude.pitch "abaqus.Part.PartFeature.PartFeature.BaseSolidExtrude.pitch (Python parameter) — A Float specifying the pitch.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L194-L237)[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidExtrude "Permalink to this definition")
    :   This method creates a first Feature object by extruding the given ConstrainedSketch object by the
        given depth, creating a solid. The ConstrainedSketch object must define a closed profile.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [BaseSolidExtrude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-basesolidextrudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidExtrude-parameters "Permalink to this headline")
        :   sketch[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidExtrude.sketch "Permalink to this definition")
            :   A ConstrainedSketch object specifying the plane shape to be extruded.

            depth[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidExtrude.depth "Permalink to this definition")
            :   A Float specifying the extrusion depth. Possible values are 10^-5 <= **depth** <= 10^5.

            draftAngle=`None`[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidExtrude.draftAngle "Permalink to this definition")
            :   A Float specifying the draft angle in degrees. Possible values are -90.0 ≤ **draftAngle**
                ≤ 90.0. By convention, for a positive draft angle an outer loop will draft outward and
                an inner loop will draft inward. The opposite is true for a negative draft angle. The
                default value, 0, implies a normal extrude. The arguments **draftAngle** and **pitch** are
                mutually exclusive.

            pitch=`None`[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidExtrude.pitch "Permalink to this definition")
            :   A Float specifying the pitch. The pitch is the distance traveled along the axial
                direction by the sketch when the sketch has completed one full revolution about the
                twist axis. Pitch can be specified as positive or negative to achieve right-handed or
                left-handed twist about the twist axis, respectively. The default value, 0, implies a
                normal extrude. Possible values are -10⁵ ≤ **pitch** ≤ 10⁵. The arguments **draftAngle**
                and **pitch** are mutually exclusive.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidExtrude-returns "Permalink to this headline")
        :   A Feature object.

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidExtrude-return-type "Permalink to this headline")
        :   `Feature`

    BaseSolidRevolve(*[sketch](#abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve.sketch "abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve.sketch (Python parameter) — A ConstrainedSketch object specifying the shape to be revolved.")*, *[angle](#abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve.angle "abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve.angle (Python parameter) — A Float specifying the revolve angle in degrees.")*, *[pitch](#abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve.pitch "abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve.pitch (Python parameter) — A Float specifying the pitch.")=`None`*, *[flipRevolveDirection](#abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve.flipRevolveDirection "abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve.flipRevolveDirection (Python parameter) — A Boolean specifying whether to override the direction of feature creation.")=`0`*, *[flipPitchDirection](#abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve.flipPitchDirection "abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve.flipPitchDirection (Python parameter) — A Boolean specifying whether to override the direction of translation.")=`0`*, *[moveSketchNormalToPath](#abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve.moveSketchNormalToPath "abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve.moveSketchNormalToPath (Python parameter) — A Boolean specifying whether to rotate the sketch so that it is normal to the path of revolution when using the pitch option.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L239-L297)[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve "Permalink to this definition")
    :   This method creates a first Feature object by revolving the given ConstrainedSketch object by the
        given angle, creating a solid. The ConstrainedSketch object must define a closed profile and an axis of
        revolution. The axis is defined by a single construction line.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [BaseSolidRevolve on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-basesolidrevolvepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve-parameters "Permalink to this headline")
        :   sketch[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve.sketch "Permalink to this definition")
            :   A ConstrainedSketch object specifying the shape to be revolved.

            angle[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve.angle "Permalink to this definition")
            :   A Float specifying the revolve angle in degrees. Possible values are 10⁻⁴ ≤ **angle** ≤
                360. Note: If **pitch** > 0, there is no upper limit for **angle**.

            pitch=`None`[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve.pitch "Permalink to this definition")
            :   A Float specifying the pitch. The pitch is the distance traveled along the axial
                direction, measured between corresponding points on the sketch when it has completed one
                full revolution about the axis of revolution. Possible values are 0 ≤ **pitch** ≤ 10⁵.
                The default value, 0, implies a normal revolve.

            flipRevolveDirection=`0`[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve.flipRevolveDirection "Permalink to this definition")
            :   A Boolean specifying whether to override the direction of feature creation. If
                **flipRevolveDirection** = OFF, the default direction of revolution is used. If
                **flipRevolveDirection** = ON, the revolve direction is reversed. The default value is OFF.

            flipPitchDirection=`0`[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve.flipPitchDirection "Permalink to this definition")
            :   A Boolean specifying whether to override the direction of translation. If
                **flipPitchDirection** = OFF, the direction of translation is given by the direction of the
                revolve axis. If **flipPitchDirection** = ON, the translation direction is reversed. The
                default value is OFF.

            moveSketchNormalToPath=`0`[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve.moveSketchNormalToPath "Permalink to this definition")
            :   A Boolean specifying whether to rotate the sketch so that it is normal to the path of
                revolution when using the **pitch** option. If **moveSketchNormalToPath** = OFF, the sketch
                plane remains parallel to the revolve axis. If **moveSketchNormalToPath** = ON, the sketch
                is moved to match the angle created by the **pitch** before being revolved. The default
                value is OFF.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve-returns "Permalink to this headline")
        :   A Feature object.

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve-return-type "Permalink to this headline")
        :   `Feature`

        Raises:[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve-raises "Permalink to this headline")
        :   **RangeError** –

    BaseSolidSweep(*[sketch](#abaqus.Part.PartFeature.PartFeature.BaseSolidSweep.sketch "abaqus.Part.PartFeature.PartFeature.BaseSolidSweep.sketch (Python parameter) — A ConstrainedSketch object specifying the profile to be swept.")*, *[path](#abaqus.Part.PartFeature.PartFeature.BaseSolidSweep.path "abaqus.Part.PartFeature.PartFeature.BaseSolidSweep.path (Python parameter) — A ConstrainedSketch object specifying the path of the sweep.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L299-L326)[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidSweep "Permalink to this definition")
    :   This method creates a first Feature object by sweeping the given profile ConstrainedSketch object
        along the path defined by the path ConstrainedSketch object, creating a solid. The profile
        ConstrainedSketch object must define a closed profile. The origin of the profile sketch is positioned at
        the start of the sweep path and swept perpendicular to the path. No checks are made for self-
        intersection.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [BaseSolidSweep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-basesolidsweeppyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidSweep-parameters "Permalink to this headline")
        :   sketch[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidSweep.sketch "Permalink to this definition")
            :   A ConstrainedSketch object specifying the profile to be swept.

            path[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidSweep.path "Permalink to this definition")
            :   A ConstrainedSketch object specifying the path of the sweep.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidSweep-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.BaseSolidSweep-return-type "Permalink to this headline")
        :   `Feature`

    BaseWire(*[sketch](#abaqus.Part.PartFeature.PartFeature.BaseWire.sketch "abaqus.Part.PartFeature.PartFeature.BaseWire.sketch (Python parameter) — A ConstrainedSketch object specifying the planar wire.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L486-L508)[¶](#abaqus.Part.PartFeature.PartFeature.BaseWire "Permalink to this definition")
    :   This method creates a first Feature object by creating a planar wire from the given ConstrainedSketch
        object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [BaseWire on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-basewirepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.BaseWire-parameters "Permalink to this headline")
        :   sketch[¶](#abaqus.Part.PartFeature.PartFeature.BaseWire.sketch "Permalink to this definition")
            :   A ConstrainedSketch object specifying the planar wire.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.BaseWire-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.BaseWire-return-type "Permalink to this headline")
        :   `Feature`

    BlendFaces(*[side1](#abaqus.Part.PartFeature.PartFeature.BlendFaces.side1 "abaqus.Part.PartFeature.PartFeature.BlendFaces.side1 (Python parameter) — A sequence of Edge objects specifying one side of the blend.")*, *[side2](#abaqus.Part.PartFeature.PartFeature.BlendFaces.side2 "abaqus.Part.PartFeature.PartFeature.BlendFaces.side2 (Python parameter) — A sequence of Edge or Face objects specifying the second side of the blend.")*, *[method](#abaqus.Part.PartFeature.PartFeature.BlendFaces.method "abaqus.Part.PartFeature.PartFeature.BlendFaces.method (Python parameter) — A SymbolicConstant indicating a method for creating blends.")=`None`*, *[path](#abaqus.Part.PartFeature.PartFeature.BlendFaces.path "abaqus.Part.PartFeature.PartFeature.BlendFaces.path (Python parameter) — An Edge object that connects side1 to side2 and specifies the path for creating the blend.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L510-L551)[¶](#abaqus.Part.PartFeature.PartFeature.BlendFaces "Permalink to this definition")
    :   This method creates a Feature object by creating new faces that blends two sets of faces.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [BlendFaces on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-blendfacespyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.BlendFaces-parameters "Permalink to this headline")
        :   side1[¶](#abaqus.Part.PartFeature.PartFeature.BlendFaces.side1 "Permalink to this definition")
            :   A sequence of Edge objects specifying one side of the blend. The edges must form a
                continuous chain without branches.

            side2[¶](#abaqus.Part.PartFeature.PartFeature.BlendFaces.side2 "Permalink to this definition")
            :   A sequence of Edge or Face objects specifying the second side of the blend. If **side2**
                contains Edge objects then they must form a continuous chain without branches.

            method=`None`[¶](#abaqus.Part.PartFeature.PartFeature.BlendFaces.method "Permalink to this definition")
            :   A SymbolicConstant indicating a method for creating blends. This argument is a required
                argument if **side2** contains Edge object and it is ignored if **side2** contains
                Faceobjects. It can have one of the following values:TANGENT: The blend is tangent to
                the sides.SHORTEST\_PATH: The blend connects the two sides based on linear interpolation
                between the two sides.SPECIFY\_PATH: The blend connects the two sides along a specified
                path.

            path=`None`[¶](#abaqus.Part.PartFeature.PartFeature.BlendFaces.path "Permalink to this definition")
            :   An Edge object that connects **side1** to **side2** and specifies the path for creating the
                blend. This argument is required if **method** = SPECIFY\_PATH; otherwise, it is ignored.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.BlendFaces-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.BlendFaces-return-type "Permalink to this headline")
        :   `Feature`

    Chamfer(*[length](#abaqus.Part.PartFeature.PartFeature.Chamfer.length "abaqus.Part.PartFeature.PartFeature.Chamfer.length (Python parameter) — A Float specifying the length of the chamfer.")*, *[edgeList](#abaqus.Part.PartFeature.PartFeature.Chamfer.edgeList "abaqus.Part.PartFeature.PartFeature.Chamfer.edgeList (Python parameter) — A sequence of Edge objects specifying the edges to chamfer.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L553-L577)[¶](#abaqus.Part.PartFeature.PartFeature.Chamfer "Permalink to this definition")
    :   This method creates an additional Feature object by chamfering the given list of edges with a given
        length.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [Chamfer on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-chamferpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.Chamfer-parameters "Permalink to this headline")
        :   length[¶](#abaqus.Part.PartFeature.PartFeature.Chamfer.length "Permalink to this definition")
            :   A Float specifying the length of the chamfer.

            edgeList[¶](#abaqus.Part.PartFeature.PartFeature.Chamfer.edgeList "Permalink to this definition")
            :   A sequence of Edge objects specifying the edges to chamfer.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.Chamfer-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.Chamfer-return-type "Permalink to this headline")
        :   `Feature`

    ConvertToAnalytical()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L612-L629)[¶](#abaqus.Part.PartFeature.PartFeature.ConvertToAnalytical "Permalink to this definition")
    :   This method attempts to change entities into a simpler form that will speed up processing and make
        entities available during feature operations.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.ConvertToAnalytical-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.ConvertToAnalytical-return-type "Permalink to this headline")
        :   `Feature`

    ConvertToPrecise(*[method](#abaqus.Part.PartFeature.PartFeature.ConvertToPrecise.method "abaqus.Part.PartFeature.PartFeature.ConvertToPrecise.method (Python parameter) — A SymbolicConstant specifying the method to be used to convert the part to precise. Possible values are RECOMPUTE_GEOMETRY and TIGHTEN_GAPS.")=`abaqusConstants.RECOMPUTE_GEOMETRY`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L631-L654)[¶](#abaqus.Part.PartFeature.PartFeature.ConvertToPrecise "Permalink to this definition")
    :   This method attempts to change imprecise entities so that the geometry becomes precise.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [ConvertToPrecise on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-converttoprecisepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.ConvertToPrecise-parameters "Permalink to this headline")
        :   method=`abaqusConstants.RECOMPUTE_GEOMETRY`[¶](#abaqus.Part.PartFeature.PartFeature.ConvertToPrecise.method "Permalink to this definition")
            :   A SymbolicConstant specifying the method to be used to convert the part to precise.
                Possible values are RECOMPUTE\_GEOMETRY and TIGHTEN\_GAPS. The default value is
                RECOMPUTE\_GEOMETRY.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.ConvertToPrecise-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.ConvertToPrecise-return-type "Permalink to this headline")
        :   `Feature`

    CoverEdges(*[edgeList](#abaqus.Part.PartFeature.PartFeature.CoverEdges.edgeList "abaqus.Part.PartFeature.PartFeature.CoverEdges.edgeList (Python parameter) — A sequence of Edge objects specifying the edges that bound the new face.")*, *[tryAnalytical](#abaqus.Part.PartFeature.PartFeature.CoverEdges.tryAnalytical "abaqus.Part.PartFeature.PartFeature.CoverEdges.tryAnalytical (Python parameter) — A Boolean specifying whether the newly created face should be analytical or not.")=`False`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L656-L691)[¶](#abaqus.Part.PartFeature.PartFeature.CoverEdges "Permalink to this definition")
    :   This method generates a face using the given edges as the face’s boundaries. The CoverEdges method
        generates a face by creating the geometry consisting of the underlying surface, associated edges, and
        vertices.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [CoverEdges on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-coveredgespyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.CoverEdges-parameters "Permalink to this headline")
        :   edgeList[¶](#abaqus.Part.PartFeature.PartFeature.CoverEdges.edgeList "Permalink to this definition")
            :   A sequence of Edge objects specifying the edges that bound the new face.

            tryAnalytical=`False`[¶](#abaqus.Part.PartFeature.PartFeature.CoverEdges.tryAnalytical "Permalink to this definition")
            :   A Boolean specifying whether the newly created face should be analytical or not. The
                default is False.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.CoverEdges-returns "Permalink to this headline")
        :   A Feature object.

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.CoverEdges-return-type "Permalink to this headline")
        :   `Feature`

        Raises:[¶](#abaqus.Part.PartFeature.PartFeature.CoverEdges-raises "Permalink to this headline")
        :   * **Parterror** – Cannot find a closed loop, If the given boundary is not a closed loop.
            * **Parterror** – Cannot find a closed loop, If the given boundary contains a zero length component.
            * **Parterror** – Cannot construct face geometry, If the underlying surface is too difficult to fit.

    Cut(*[sketchPlane](#abaqus.Part.PartFeature.PartFeature.Cut.sketchPlane "abaqus.Part.PartFeature.PartFeature.Cut.sketchPlane (Python parameter) — A Datum plane object or a planar Face object.")*, *[sketchPlaneSide](#abaqus.Part.PartFeature.PartFeature.Cut.sketchPlaneSide "abaqus.Part.PartFeature.PartFeature.Cut.sketchPlaneSide (Python parameter) — A SymbolicConstant specifying the direction of feature creation.")*, *[sketchUpEdge](#abaqus.Part.PartFeature.PartFeature.Cut.sketchUpEdge "abaqus.Part.PartFeature.PartFeature.Cut.sketchUpEdge (Python parameter) — An Edge object or a Datum axis object specifying the vertical (Y) direction of the sketch.")*, *[sketch](#abaqus.Part.PartFeature.PartFeature.Cut.sketch "abaqus.Part.PartFeature.PartFeature.Cut.sketch (Python parameter) — A ConstrainedSketch object specifying the planar cut.")*, *[sketchOrientation](#abaqus.Part.PartFeature.PartFeature.Cut.sketchOrientation "abaqus.Part.PartFeature.PartFeature.Cut.sketchOrientation (Python parameter) — A SymbolicConstant specifying the orientation of sketchUpEdge on the sketch.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L693-L733)[¶](#abaqus.Part.PartFeature.PartFeature.Cut "Permalink to this definition")
    :   This method creates an additional Feature object by cutting a hole using the given ConstrainedSketch
        object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [Cut on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cutpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.Cut-parameters "Permalink to this headline")
        :   sketchPlane[¶](#abaqus.Part.PartFeature.PartFeature.Cut.sketchPlane "Permalink to this definition")
            :   A Datum plane object or a planar Face object.

            sketchPlaneSide[¶](#abaqus.Part.PartFeature.PartFeature.Cut.sketchPlaneSide "Permalink to this definition")
            :   A SymbolicConstant specifying the direction of feature creation. Possible values are
                SIDE1 and SIDE2.

            sketchUpEdge[¶](#abaqus.Part.PartFeature.PartFeature.Cut.sketchUpEdge "Permalink to this definition")
            :   An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the
                sketch.

            sketch[¶](#abaqus.Part.PartFeature.PartFeature.Cut.sketch "Permalink to this definition")
            :   A ConstrainedSketch object specifying the planar cut.

            sketchOrientation=`None`[¶](#abaqus.Part.PartFeature.PartFeature.Cut.sketchOrientation "Permalink to this definition")
            :   A SymbolicConstant specifying the orientation of **sketchUpEdge** on the sketch. Possible
                values are RIGHT, LEFT, TOP, and BOTTOM.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.Cut-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.Cut-return-type "Permalink to this headline")
        :   `Feature`

    CutExtrude(*[sketchPlane](#abaqus.Part.PartFeature.PartFeature.CutExtrude.sketchPlane "abaqus.Part.PartFeature.PartFeature.CutExtrude.sketchPlane (Python parameter) — A Datum plane object or a planar Face object.")*, *[sketchPlaneSide](#abaqus.Part.PartFeature.PartFeature.CutExtrude.sketchPlaneSide "abaqus.Part.PartFeature.PartFeature.CutExtrude.sketchPlaneSide (Python parameter) — A SymbolicConstant specifying the direction of feature creation.")*, *[sketchUpEdge](#abaqus.Part.PartFeature.PartFeature.CutExtrude.sketchUpEdge "abaqus.Part.PartFeature.PartFeature.CutExtrude.sketchUpEdge (Python parameter) — An Edge object or a Datum axis object specifying the vertical (Y) direction of the sketch.")*, *[sketchOrientation](#abaqus.Part.PartFeature.PartFeature.CutExtrude.sketchOrientation "abaqus.Part.PartFeature.PartFeature.CutExtrude.sketchOrientation (Python parameter) — A SymbolicConstant specifying the orientation of sketchUpEdge on the sketch.")*, *[sketch](#abaqus.Part.PartFeature.PartFeature.CutExtrude.sketch "abaqus.Part.PartFeature.PartFeature.CutExtrude.sketch (Python parameter) — A ConstrainedSketch object specifying the planar sketch to be extruded.")*, *[depth](#abaqus.Part.PartFeature.PartFeature.CutExtrude.depth "abaqus.Part.PartFeature.PartFeature.CutExtrude.depth (Python parameter) — A Float specifying the extrusion depth.")=`None`*, *[upToFace](#abaqus.Part.PartFeature.PartFeature.CutExtrude.upToFace "abaqus.Part.PartFeature.PartFeature.CutExtrude.upToFace (Python parameter) — A Face specifying the face up to which to cut.")=`''`*, *[draftAngle](#abaqus.Part.PartFeature.PartFeature.CutExtrude.draftAngle "abaqus.Part.PartFeature.PartFeature.CutExtrude.draftAngle (Python parameter) — A Float specifying the draft angle in degrees.")=`None`*, *[pitch](#abaqus.Part.PartFeature.PartFeature.CutExtrude.pitch "abaqus.Part.PartFeature.PartFeature.CutExtrude.pitch (Python parameter) — A Float specifying the pitch.")=`None`*, *[flipExtrudeDirection](#abaqus.Part.PartFeature.PartFeature.CutExtrude.flipExtrudeDirection "abaqus.Part.PartFeature.PartFeature.CutExtrude.flipExtrudeDirection (Python parameter) — A Boolean specifying whether to override the direction of feature creation.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L735-L808)[¶](#abaqus.Part.PartFeature.PartFeature.CutExtrude "Permalink to this definition")
    :   This method creates an additional Feature object by extruding the given
        ConstrainedSketch object by the given depth and cutting away material in the solid and
        shell regions of the part. The ConstrainedSketch object must define a closed profile.
        The CutExtrude method creates a blind cut (using **depth**), an up-to-face cut (using
        **upToFace**), or a through-all cut (if **depth** and **upToFace** are not specified).

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [CutExtrude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cutextrudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.CutExtrude-parameters "Permalink to this headline")
        :   sketchPlane[¶](#abaqus.Part.PartFeature.PartFeature.CutExtrude.sketchPlane "Permalink to this definition")
            :   A Datum plane object or a planar Face object.

            sketchPlaneSide[¶](#abaqus.Part.PartFeature.PartFeature.CutExtrude.sketchPlaneSide "Permalink to this definition")
            :   A SymbolicConstant specifying the direction of feature creation. Possible values are
                SIDE1 and SIDE2.

            sketchUpEdge[¶](#abaqus.Part.PartFeature.PartFeature.CutExtrude.sketchUpEdge "Permalink to this definition")
            :   An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the
                sketch.

            sketchOrientation[¶](#abaqus.Part.PartFeature.PartFeature.CutExtrude.sketchOrientation "Permalink to this definition")
            :   A SymbolicConstant specifying the orientation of **sketchUpEdge** on the sketch. Possible
                values are RIGHT, LEFT, TOP, and BOTTOM.

            sketch[¶](#abaqus.Part.PartFeature.PartFeature.CutExtrude.sketch "Permalink to this definition")
            :   A ConstrainedSketch object specifying the planar sketch to be extruded.

            depth=`None`[¶](#abaqus.Part.PartFeature.PartFeature.CutExtrude.depth "Permalink to this definition")
            :   A Float specifying the extrusion depth. If **depth** is specified, the cut will be a blind
                cut. The default is to not specify a depth.

            upToFace=`''`[¶](#abaqus.Part.PartFeature.PartFeature.CutExtrude.upToFace "Permalink to this definition")
            :   A Face specifying the face up to which to cut. If **upToFace** is specified, the cut will
                be an up-to-face cut. The default is to not specify a face. Note: If neither **depth** nor
                **upToFace** is specified, the cut will be a through-all cut.

            draftAngle=`None`[¶](#abaqus.Part.PartFeature.PartFeature.CutExtrude.draftAngle "Permalink to this definition")
            :   A Float specifying the draft angle in degrees. Possible values are -90.0 ≤ **draftAngle**
                ≤ 90.0. By convention, for a positive draft angle an outer loop will draft outward and
                an inner loop will draft inward. The opposite is true for a negative draft angle. The
                default value, 0, implies a normal extrude. The arguments **draftAngle** and **pitch** are
                mutually exclusive.

            pitch=`None`[¶](#abaqus.Part.PartFeature.PartFeature.CutExtrude.pitch "Permalink to this definition")
            :   A Float specifying the pitch. The pitch is the distance traveled along the axial
                direction by the sketch when the sketch has completed one full revolution about the
                twist axis. Pitch can be specified as positive or negative to achieve right-handed or
                left-handed twist about the twist axis, respectively. The default value, 0, implies a
                normal extrude. Possible values are -10⁵ ≤ **pitch** ≤ 10⁵. The arguments **draftAngle**
                and **pitch** are mutually exclusive.

            flipExtrudeDirection=`0`[¶](#abaqus.Part.PartFeature.PartFeature.CutExtrude.flipExtrudeDirection "Permalink to this definition")
            :   A Boolean specifying whether to override the direction of feature creation. If the value
                is OFF, it means use the direction defined by the **sketchPlaneSide**; if the value is ON,
                it means use the opposite direction to the one defined by **sketchPlaneSide**. The default
                value is OFF.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.CutExtrude-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.CutExtrude-return-type "Permalink to this headline")
        :   `Feature`

    CutLoft(*[loftsections](#abaqus.Part.PartFeature.PartFeature.CutLoft.loftsections "abaqus.Part.PartFeature.PartFeature.CutLoft.loftsections (Python parameter) — A sequence of sequences of edges specifying the cross-sections to be lofted.")*, *[startCondition](#abaqus.Part.PartFeature.PartFeature.CutLoft.startCondition "abaqus.Part.PartFeature.PartFeature.CutLoft.startCondition (Python parameter) — A SymbolicConstant specifying the tangent direction at the start section of the loft feature.")=`None`*, *[endCondition](#abaqus.Part.PartFeature.PartFeature.CutLoft.endCondition "abaqus.Part.PartFeature.PartFeature.CutLoft.endCondition (Python parameter) — A SymbolicConstant specifying the tangent direction at the end section of the loft feature.")=`None`*, *[startTangent](#abaqus.Part.PartFeature.PartFeature.CutLoft.startTangent "abaqus.Part.PartFeature.PartFeature.CutLoft.startTangent (Python parameter) — A Float specifying the angle in degrees of the tangent with respect to the plane in which the start section lies.")=`None`*, *[startMagnitude](#abaqus.Part.PartFeature.PartFeature.CutLoft.startMagnitude "abaqus.Part.PartFeature.PartFeature.CutLoft.startMagnitude (Python parameter) — A Float specifying the magnitude of the startTangent.")=`None`*, *[endTangent](#abaqus.Part.PartFeature.PartFeature.CutLoft.endTangent "abaqus.Part.PartFeature.PartFeature.CutLoft.endTangent (Python parameter) — A Float specifying the angle in degrees of the tangent with respect to the plane in which the end section lies.")=`None`*, *[endMagnitude](#abaqus.Part.PartFeature.PartFeature.CutLoft.endMagnitude "abaqus.Part.PartFeature.PartFeature.CutLoft.endMagnitude (Python parameter) — A Float specifying the magnitude of the endTangent.")=`None`*, *[globalSmoothing](#abaqus.Part.PartFeature.PartFeature.CutLoft.globalSmoothing "abaqus.Part.PartFeature.PartFeature.CutLoft.globalSmoothing (Python parameter) — A Boolean specifying whether each path defined in the paths argument is applied locally or globally.If the path is applied locally, its effect is felt only on faces created from the edges on the loftSections through which the paths pass through.If the path is applied globally, an averaging algorithm is applied over all the paths defined and is distributed over all the faces created.The default value is ON (globally).")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L810-L882)[¶](#abaqus.Part.PartFeature.PartFeature.CutLoft "Permalink to this definition")
    :   This method creates an additional Feature object by lofting between the given sections and cutting
        away material from the part. You define the sections using a sequence of edges from the part or an
        EdgeArray.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [CutLoft on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cutloftpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.CutLoft-parameters "Permalink to this headline")
        :   loftsections[¶](#abaqus.Part.PartFeature.PartFeature.CutLoft.loftsections "Permalink to this definition")
            :   A sequence of sequences of edges specifying the cross-sections to be lofted. Each outer
                sequence specifies a section through which the method will pass the loft feature. Each
                outer sequence can be defined as a sequence of edges or as an EdgeArray. The edges
                specifying a section must form a simple closed profile and must not contain multiple
                loops.

            startCondition=`None`[¶](#abaqus.Part.PartFeature.PartFeature.CutLoft.startCondition "Permalink to this definition")
            :   A SymbolicConstant specifying the tangent direction at the start section of the loft
                feature. Possible values are NONE, NORMAL, RADIAL, and SPECIFIED. You can specify this
                argument only if the start and end sections are planar. You cannot use this argument in
                conjunction with the **path** argument. You must use the **startCondition** argument in
                conjunction with the **endCondition** argument.

            endCondition=`None`[¶](#abaqus.Part.PartFeature.PartFeature.CutLoft.endCondition "Permalink to this definition")
            :   A SymbolicConstant specifying the tangent direction at the end section of the loft
                feature. Possible values are NONE, NORMAL, RADIAL, and SPECIFIED. You can specify this
                argument only if the start and end sections are planar. You cannot use this argument in
                conjunction with the **path** argument. You must use the **endCondition** argument in
                conjunction with the **startCondition** argument.

            startTangent=`None`[¶](#abaqus.Part.PartFeature.PartFeature.CutLoft.startTangent "Permalink to this definition")
            :   A Float specifying the angle in degrees of the tangent with respect to the plane in
                which the start section lies. You must specify the **startTangent** argument if
                **startCondition** = SPECIFIED. Possible values are 0.0 ≤ **startTangent** ≤ 180.0.

            startMagnitude=`None`[¶](#abaqus.Part.PartFeature.PartFeature.CutLoft.startMagnitude "Permalink to this definition")
            :   A Float specifying the magnitude of the **startTangent**. You must specify the
                **startMagnitude** argument if **startCondition** = SPECIFIED. Possible values are 0.0 <
                **startMagnitude** < 100.0.

            endTangent=`None`[¶](#abaqus.Part.PartFeature.PartFeature.CutLoft.endTangent "Permalink to this definition")
            :   A Float specifying the angle in degrees of the tangent with respect to the plane in
                which the end section lies. You must specify the **endTangent** argument if
                **startCondition** = SPECIFIED. Possible values are 0.0 ≤ **endTangent** ≤ 180.0.

            endMagnitude=`None`[¶](#abaqus.Part.PartFeature.PartFeature.CutLoft.endMagnitude "Permalink to this definition")
            :   A Float specifying the magnitude of the **endTangent**. This argument is to be used when
                the **endCondition** argument has the value SPECIFIED. Possible values are 0.0 <
                **endMagnitude** < 100.0.

            globalSmoothing=`0`[¶](#abaqus.Part.PartFeature.PartFeature.CutLoft.globalSmoothing "Permalink to this definition")
            :   A Boolean specifying whether each path defined in the **paths** argument is applied
                locally or globally.If the path is applied locally, its effect is felt only on faces
                created from the edges on the **loftSections** through which the **paths** pass through.If
                the path is applied globally, an averaging algorithm is applied over all the paths
                defined and is distributed over all the faces created.The default value is ON
                (globally).

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.CutLoft-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.CutLoft-return-type "Permalink to this headline")
        :   `Feature`

    CutRevolve(*[sketchPlane](#abaqus.Part.PartFeature.PartFeature.CutRevolve.sketchPlane "abaqus.Part.PartFeature.PartFeature.CutRevolve.sketchPlane (Python parameter) — A Datum plane object or a planar Face object.")*, *[sketchPlaneSide](#abaqus.Part.PartFeature.PartFeature.CutRevolve.sketchPlaneSide "abaqus.Part.PartFeature.PartFeature.CutRevolve.sketchPlaneSide (Python parameter) — A SymbolicConstant specifying the direction of feature creation.")*, *[sketchUpEdge](#abaqus.Part.PartFeature.PartFeature.CutRevolve.sketchUpEdge "abaqus.Part.PartFeature.PartFeature.CutRevolve.sketchUpEdge (Python parameter) — An Edge object or a Datum axis object specifying the vertical (Y) direction of the sketch.")*, *[sketchOrientation](#abaqus.Part.PartFeature.PartFeature.CutRevolve.sketchOrientation "abaqus.Part.PartFeature.PartFeature.CutRevolve.sketchOrientation (Python parameter) — A SymbolicConstant specifying the orientation of sketchUpEdge on the sketch.")*, *[sketch](#abaqus.Part.PartFeature.PartFeature.CutRevolve.sketch "abaqus.Part.PartFeature.PartFeature.CutRevolve.sketch (Python parameter) — A ConstrainedSketch object specifying the planar sketch to be revolved.")*, *[angle](#abaqus.Part.PartFeature.PartFeature.CutRevolve.angle "abaqus.Part.PartFeature.PartFeature.CutRevolve.angle (Python parameter) — A Float specifying the angle in degrees to be revolved.")*, *[pitch](#abaqus.Part.PartFeature.PartFeature.CutRevolve.pitch "abaqus.Part.PartFeature.PartFeature.CutRevolve.pitch (Python parameter) — A Float specifying the pitch.")=`None`*, *[flipRevolveDirection](#abaqus.Part.PartFeature.PartFeature.CutRevolve.flipRevolveDirection "abaqus.Part.PartFeature.PartFeature.CutRevolve.flipRevolveDirection (Python parameter) — A Boolean specifying whether to override the direction of feature creation.")=`0`*, *[flipPitchDirection](#abaqus.Part.PartFeature.PartFeature.CutRevolve.flipPitchDirection "abaqus.Part.PartFeature.PartFeature.CutRevolve.flipPitchDirection (Python parameter) — A Boolean specifying whether to override the direction of translation.")=`0`*, *[moveSketchNormalToPath](#abaqus.Part.PartFeature.PartFeature.CutRevolve.moveSketchNormalToPath "abaqus.Part.PartFeature.PartFeature.CutRevolve.moveSketchNormalToPath (Python parameter) — A Boolean specifying whether to rotate the sketch so that it is normal to the path of revolution when using the pitch option.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L884-L952)[¶](#abaqus.Part.PartFeature.PartFeature.CutRevolve "Permalink to this definition")
    :   This method creates an additional Feature object by revolving the given ConstrainedSketch object by
        the given angle and cutting away material from the part. The ConstrainedSketch object must define a
        closed profile and an axis of revolution.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [CutRevolve on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cutrevolvepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.CutRevolve-parameters "Permalink to this headline")
        :   sketchPlane[¶](#abaqus.Part.PartFeature.PartFeature.CutRevolve.sketchPlane "Permalink to this definition")
            :   A Datum plane object or a planar Face object.

            sketchPlaneSide[¶](#abaqus.Part.PartFeature.PartFeature.CutRevolve.sketchPlaneSide "Permalink to this definition")
            :   A SymbolicConstant specifying the direction of feature creation. Possible values are
                SIDE1 and SIDE2.

            sketchUpEdge[¶](#abaqus.Part.PartFeature.PartFeature.CutRevolve.sketchUpEdge "Permalink to this definition")
            :   An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the
                sketch.

            sketchOrientation[¶](#abaqus.Part.PartFeature.PartFeature.CutRevolve.sketchOrientation "Permalink to this definition")
            :   A SymbolicConstant specifying the orientation of **sketchUpEdge** on the sketch. Possible
                values are RIGHT, LEFT, TOP, and BOTTOM.

            sketch[¶](#abaqus.Part.PartFeature.PartFeature.CutRevolve.sketch "Permalink to this definition")
            :   A ConstrainedSketch object specifying the planar sketch to be revolved.

            angle[¶](#abaqus.Part.PartFeature.PartFeature.CutRevolve.angle "Permalink to this definition")
            :   A Float specifying the angle in degrees to be revolved.

            pitch=`None`[¶](#abaqus.Part.PartFeature.PartFeature.CutRevolve.pitch "Permalink to this definition")
            :   A Float specifying the pitch. The pitch is the distance traveled along the axial
                direction, measured between corresponding points on the sketch when it has completed one
                full revolution about the axis of revolution. Possible values are 0 ≤ **pitch** ≤ 10⁵.
                The default value, 0, implies a normal revolve.

            flipRevolveDirection=`0`[¶](#abaqus.Part.PartFeature.PartFeature.CutRevolve.flipRevolveDirection "Permalink to this definition")
            :   A Boolean specifying whether to override the direction of feature creation. If
                **flipRevolveDirection** = OFF, the default direction of revolution is used. If
                **flipRevolveDirection** = ON, the revolve direction is reversed. The default value is OFF.

            flipPitchDirection=`0`[¶](#abaqus.Part.PartFeature.PartFeature.CutRevolve.flipPitchDirection "Permalink to this definition")
            :   A Boolean specifying whether to override the direction of translation. If
                **flipPitchDirection** = OFF, the direction of translation is given by the direction of the
                revolve axis. If **flipPitchDirection** = ON, the translation direction is reversed. The
                default value is OFF.

            moveSketchNormalToPath=`0`[¶](#abaqus.Part.PartFeature.PartFeature.CutRevolve.moveSketchNormalToPath "Permalink to this definition")
            :   A Boolean specifying whether to rotate the sketch so that it is normal to the path of
                revolution when using the **pitch** option. If **moveSketchNormalToPath** = OFF, the sketch
                plane remains parallel to the revolve axis. If **moveSketchNormalToPath** = ON, the sketch
                is moved to match the angle created by the **pitch** before being revolved. The default
                value is OFF.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.CutRevolve-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.CutRevolve-return-type "Permalink to this headline")
        :   `Feature`

    CutSweep(*[path](#abaqus.Part.PartFeature.PartFeature.CutSweep.path "abaqus.Part.PartFeature.PartFeature.CutSweep.path (Python parameter) — Path may either be a ConstrainedSketch object or a sequence of Edge objects specifying the path of the sweep.")*, *[profile](#abaqus.Part.PartFeature.PartFeature.CutSweep.profile "abaqus.Part.PartFeature.PartFeature.CutSweep.profile (Python parameter) — Profile may either be a ConstrainedSketch object or a Face object specifying the section to be swept.")*, *[pathPlane](#abaqus.Part.PartFeature.PartFeature.CutSweep.pathPlane "abaqus.Part.PartFeature.PartFeature.CutSweep.pathPlane (Python parameter) — A Datum plane object or a planar Face object.")=`''`*, *[pathUpEdge](#abaqus.Part.PartFeature.PartFeature.CutSweep.pathUpEdge "abaqus.Part.PartFeature.PartFeature.CutSweep.pathUpEdge (Python parameter) — An Edge object or a Datum axis object specifying the vertical (Y) direction of the path sketch.")=`None`*, *[pathOrientation](#abaqus.Part.PartFeature.PartFeature.CutSweep.pathOrientation "abaqus.Part.PartFeature.PartFeature.CutSweep.pathOrientation (Python parameter) — A SymbolicConstant specifying the orientation of pathUpEdge on the sketch.")=`abaqusConstants.RIGHT`*, *[sketchPlane](#abaqus.Part.PartFeature.PartFeature.CutSweep.sketchPlane "abaqus.Part.PartFeature.PartFeature.CutSweep.sketchPlane (Python parameter) — A Datum plane object or a planar Face object specifying the plane on which to sketch the profile.")=`''`*, *[sketchUpEdge](#abaqus.Part.PartFeature.PartFeature.CutSweep.sketchUpEdge "abaqus.Part.PartFeature.PartFeature.CutSweep.sketchUpEdge (Python parameter) — An Edge object or a Datum axis object specifying the vertical (Y) direction of the profile sketch.")=`None`*, *[sketchOrientation](#abaqus.Part.PartFeature.PartFeature.CutSweep.sketchOrientation "abaqus.Part.PartFeature.PartFeature.CutSweep.sketchOrientation (Python parameter) — A SymbolicConstant specifying the orientation of sketchUpEdge on the sketch.")=`abaqusConstants.RIGHT`*, *[draftAngle](#abaqus.Part.PartFeature.PartFeature.CutSweep.draftAngle "abaqus.Part.PartFeature.PartFeature.CutSweep.draftAngle (Python parameter) — A Float specifying the draft angle in degrees.")=`None`*, *[pitch](#abaqus.Part.PartFeature.PartFeature.CutSweep.pitch "abaqus.Part.PartFeature.PartFeature.CutSweep.pitch (Python parameter) — A Float specifying the pitch.")=`None`*, *[profileNormal](#abaqus.Part.PartFeature.PartFeature.CutSweep.profileNormal "abaqus.Part.PartFeature.PartFeature.CutSweep.profileNormal (Python parameter) — A Boolean specifying whether to keep the profile normal same as original or varying through out the sweep path.")=`0`*, *[flipSweepDirection](#abaqus.Part.PartFeature.PartFeature.CutSweep.flipSweepDirection "abaqus.Part.PartFeature.PartFeature.CutSweep.flipSweepDirection (Python parameter) — A Boolean specifying whether to flip the direction in which sweep operation will be performed.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L954-L1042)[¶](#abaqus.Part.PartFeature.PartFeature.CutSweep "Permalink to this definition")
    :   This method creates an additional Feature object by sweeping the given ConstrainedSketch object along
        a path which may be a ConstrainedSketch or a sequence of Edge objects and cutting away material from the
        part. If the profile section is a ConstrainedSketch object, it must define a closed profile. The section
        sketch can be created at the normal plane at the start of the sweep path or it may be created on a Datum
        plane or a planar Face. No checks are made for self-intersection.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [CutSweep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-cutsweeppyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.CutSweep-parameters "Permalink to this headline")
        :   path[¶](#abaqus.Part.PartFeature.PartFeature.CutSweep.path "Permalink to this definition")
            :   Path may either be a ConstrainedSketch object or a sequence of Edge objects specifying
                the path of the sweep.

            profile[¶](#abaqus.Part.PartFeature.PartFeature.CutSweep.profile "Permalink to this definition")
            :   Profile may either be a ConstrainedSketch object or a Face object specifying the section
                to be swept.

            pathPlane=`''`[¶](#abaqus.Part.PartFeature.PartFeature.CutSweep.pathPlane "Permalink to this definition")
            :   A Datum plane object or a planar Face object. Only required when path is a
                ConstrainedSketch object.

            pathUpEdge=`None`[¶](#abaqus.Part.PartFeature.PartFeature.CutSweep.pathUpEdge "Permalink to this definition")
            :   An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the
                path sketch. Only required when path is a ConstrainedSketch object.

            pathOrientation=`abaqusConstants.RIGHT`[¶](#abaqus.Part.PartFeature.PartFeature.CutSweep.pathOrientation "Permalink to this definition")
            :   A SymbolicConstant specifying the orientation of **pathUpEdge** on the sketch. Possible
                values are RIGHT, LEFT, TOP, and BOTTOM. Default value is RIGHT. Only required when path
                is a ConstrainedSketch object.

            sketchPlane=`''`[¶](#abaqus.Part.PartFeature.PartFeature.CutSweep.sketchPlane "Permalink to this definition")
            :   A Datum plane object or a planar Face object specifying the plane on which to sketch the
                profile. Not required when profile is a Face object. When profile is chosen as a
                ConstrainedSketch object, user may or may not give this as input. If user does not give
                this as input, the normal plane at the start of the path will be the sketchPlane.

            sketchUpEdge=`None`[¶](#abaqus.Part.PartFeature.PartFeature.CutSweep.sketchUpEdge "Permalink to this definition")
            :   An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the
                profile sketch. Only required when profile is a ConstrainedSketch object.

            sketchOrientation=`abaqusConstants.RIGHT`[¶](#abaqus.Part.PartFeature.PartFeature.CutSweep.sketchOrientation "Permalink to this definition")
            :   A SymbolicConstant specifying the orientation of **sketchUpEdge** on the sketch. Possible
                values are RIGHT, LEFT, TOP, and BOTTOM. Default value is RIGHT. Only required when
                profile is a ConstrainedSketch object.

            draftAngle=`None`[¶](#abaqus.Part.PartFeature.PartFeature.CutSweep.draftAngle "Permalink to this definition")
            :   A Float specifying the draft angle in degrees. Possible values are -90.0 ≤ **draftAngle**
                ≤ 90.0. By convention, for a positive draft angle an outer loop will draft outward and
                an inner loop will draft inward. The opposite is true for a negative draft angle. The
                default value, 0, implies a normal extrude. The arguments **draftAngle** and **pitch** are
                mutually exclusive.

            pitch=`None`[¶](#abaqus.Part.PartFeature.PartFeature.CutSweep.pitch "Permalink to this definition")
            :   A Float specifying the pitch. The pitch is the distance traveled along the axial
                direction by the sketch when the sketch has completed one full revolution about the
                twist axis. Pitch can be specified as positive or negative to achieve right-handed or
                left-handed twist about the twist axis, respectively. The default value, 0, implies a
                normal extrude. Possible values are -10⁵ ≤ **pitch** ≤ 10⁵. The arguments **draftAngle**
                and **pitch** are mutually exclusive.

            profileNormal=`0`[¶](#abaqus.Part.PartFeature.PartFeature.CutSweep.profileNormal "Permalink to this definition")
            :   A Boolean specifying whether to keep the profile normal same as original or varying
                through out the sweep path. When **profileNormal** = OFF, the profile normal will vary
                through out the sweep path. When **profileNormal** = ON, the profile normal will be same as
                original through out the sweep path. The default value is OFF.

            flipSweepDirection=`0`[¶](#abaqus.Part.PartFeature.PartFeature.CutSweep.flipSweepDirection "Permalink to this definition")
            :   A Boolean specifying whether to flip the direction in which sweep operation will be
                performed. When **flipSweepDirection** = OFF, sweep operation will be performed in the
                direction of path direction. When **flipSweepDirection** = ON, sweep operation will be
                performed in the direction opposite to the path direction. The default value is OFF.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.CutSweep-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.CutSweep-return-type "Permalink to this headline")
        :   `Feature`

    ExtendFaces(*[faces](#abaqus.Part.PartFeature.PartFeature.ExtendFaces.faces "abaqus.Part.PartFeature.PartFeature.ExtendFaces.faces (Python parameter) — A sequence of Face objects specifying the faces to be extended.")=`()`*, *[extendAlong](#abaqus.Part.PartFeature.PartFeature.ExtendFaces.extendAlong "abaqus.Part.PartFeature.PartFeature.ExtendFaces.extendAlong (Python parameter) — A sequence of Edge objects specifying the edges where to extend the faces.")=`()`*, *[distance](#abaqus.Part.PartFeature.PartFeature.ExtendFaces.distance "abaqus.Part.PartFeature.PartFeature.ExtendFaces.distance (Python parameter) — A Float indicating the distance to extend the faces along the edges.")=`None`*, *[upToFaces](#abaqus.Part.PartFeature.PartFeature.ExtendFaces.upToFaces "abaqus.Part.PartFeature.PartFeature.ExtendFaces.upToFaces (Python parameter) — A sequence of Face objects specifying the faces that the selected faces should be extended up to.")=`()`*, *[trimToExtendedTargetSurfaces](#abaqus.Part.PartFeature.PartFeature.ExtendFaces.trimToExtendedTargetSurfaces "abaqus.Part.PartFeature.PartFeature.ExtendFaces.trimToExtendedTargetSurfaces (Python parameter) — A Boolean indicating that the surfaces of up to target faces should be extended before extending and trimming the selected faces.")=`True`*, *[upToReferenceRep](#abaqus.Part.PartFeature.PartFeature.ExtendFaces.upToReferenceRep "abaqus.Part.PartFeature.PartFeature.ExtendFaces.upToReferenceRep (Python parameter) — A Boolean indicating that the selected faces should be extended along the selected edges and be trimmed along their intersection with the reference representation.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L1044-L1093)[¶](#abaqus.Part.PartFeature.PartFeature.ExtendFaces "Permalink to this definition")
    :   This method extends faces along its free edges by offsetting the external edges along the surfaces.
        One of **distance**, **upToReferenceRep**, or **upToFaces** must be used to specify how far the faces
        need to be extended.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [ExtendFaces on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-extendfacespyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.ExtendFaces-parameters "Permalink to this headline")
        :   faces=`()`[¶](#abaqus.Part.PartFeature.PartFeature.ExtendFaces.faces "Permalink to this definition")
            :   A sequence of Face objects specifying the faces to be extended. The faces cannot belong
                to the reference representation. The **faces** and **extendAlong** arguments are mutually
                exclusive. One of them must be specified.

            extendAlong=`()`[¶](#abaqus.Part.PartFeature.PartFeature.ExtendFaces.extendAlong "Permalink to this definition")
            :   A sequence of Edge objects specifying the edges where to extend the faces. Only free
                edges are considered. The interior edges will be ignored. The **faces** and **extendAlong**
                arguments are mutually exclusive. One of them must be specified.

            distance=`None`[¶](#abaqus.Part.PartFeature.PartFeature.ExtendFaces.distance "Permalink to this definition")
            :   A Float indicating the distance to extend the faces along the edges. Either **distance**,
                **upToReferenceRep**, or **upToFaces** must be specified.

            upToFaces=`()`[¶](#abaqus.Part.PartFeature.PartFeature.ExtendFaces.upToFaces "Permalink to this definition")
            :   A sequence of Face objects specifying the faces that the selected faces should be
                extended up to.

            trimToExtendedTargetSurfaces=`True`[¶](#abaqus.Part.PartFeature.PartFeature.ExtendFaces.trimToExtendedTargetSurfaces "Permalink to this definition")
            :   A Boolean indicating that the surfaces of up to target faces should be extended before
                extending and trimming the selected faces. The default value is True.

            upToReferenceRep=`0`[¶](#abaqus.Part.PartFeature.PartFeature.ExtendFaces.upToReferenceRep "Permalink to this definition")
            :   A Boolean indicating that the selected faces should be extended along the selected edges
                and be trimmed along their intersection with the reference representation.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.ExtendFaces-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.ExtendFaces-return-type "Permalink to this headline")
        :   `Feature`

    FaceFromElementFaces(*[elementFaces](#abaqus.Part.PartFeature.PartFeature.FaceFromElementFaces.elementFaces "abaqus.Part.PartFeature.PartFeature.FaceFromElementFaces.elementFaces (Python parameter) — A Region object specifying the collection of orphan element faces.")*, *[stitch](#abaqus.Part.PartFeature.PartFeature.FaceFromElementFaces.stitch "abaqus.Part.PartFeature.PartFeature.FaceFromElementFaces.stitch (Python parameter) — A Boolean specifying whether the created geometry face should be stitched with existing geometry faces.")=`0`*, *[stitchTolerance](#abaqus.Part.PartFeature.PartFeature.FaceFromElementFaces.stitchTolerance "abaqus.Part.PartFeature.PartFeature.FaceFromElementFaces.stitchTolerance (Python parameter) — A Float indicating the maximum gap to be stitched.")=`None`*, *[analyticFitTolerance](#abaqus.Part.PartFeature.PartFeature.FaceFromElementFaces.analyticFitTolerance "abaqus.Part.PartFeature.PartFeature.FaceFromElementFaces.analyticFitTolerance (Python parameter) — A Float indicating the analytical surface fitting tolerance.")=`None`*, *[associateFace](#abaqus.Part.PartFeature.PartFeature.FaceFromElementFaces.associateFace "abaqus.Part.PartFeature.PartFeature.FaceFromElementFaces.associateFace (Python parameter) — A Boolean specifying whether the created geometry face should be associated with the mesh.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L1095-L1138)[¶](#abaqus.Part.PartFeature.PartFeature.FaceFromElementFaces "Permalink to this definition")
    :   This method creates a geometry face from a collection of orphan element faces.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [FaceFromElementFaces on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facefromelementfacespyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.FaceFromElementFaces-parameters "Permalink to this headline")
        :   elementFaces[¶](#abaqus.Part.PartFeature.PartFeature.FaceFromElementFaces.elementFaces "Permalink to this definition")
            :   A Region object specifying the collection of orphan element faces.

            stitch=`0`[¶](#abaqus.Part.PartFeature.PartFeature.FaceFromElementFaces.stitch "Permalink to this definition")
            :   A Boolean specifying whether the created geometry face should be stitched with existing
                geometry faces. Default value is TRUE.

            stitchTolerance=`None`[¶](#abaqus.Part.PartFeature.PartFeature.FaceFromElementFaces.stitchTolerance "Permalink to this definition")
            :   A Float indicating the maximum gap to be stitched. The value should be smaller than the
                minimum feature size and bigger than the maximum gap expected to be stitched in the
                model. Otherwise this command may remove small (sliver) edges that are smaller than the
                tolerance. If stitch tolerance is not provided then default value of 0.001 will be used
                for stitching.

            analyticFitTolerance=`None`[¶](#abaqus.Part.PartFeature.PartFeature.FaceFromElementFaces.analyticFitTolerance "Permalink to this definition")
            :   A Float indicating the analytical surface fitting tolerance. If analytical tolerance is
                not provided then default value of 0.015 will be used for analytical surface fitting.

            associateFace=`0`[¶](#abaqus.Part.PartFeature.PartFeature.FaceFromElementFaces.associateFace "Permalink to this definition")
            :   A Boolean specifying whether the created geometry face should be associated with the
                mesh. Default value is TRUE.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.FaceFromElementFaces-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.FaceFromElementFaces-return-type "Permalink to this headline")
        :   `Feature`

    HoleBlindFromEdges(*[plane](#abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges.plane "abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges.plane (Python parameter) — A Datum plane object or a planar Face object.")*, *[planeSide](#abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges.planeSide "abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges.planeSide (Python parameter) — A SymbolicConstant specifying the direction of feature creation.")*, *[diameter](#abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges.diameter "abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges.diameter (Python parameter) — A Float specifying the diameter of the hole.")*, *[edge1](#abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges.edge1 "abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges.edge1 (Python parameter) — An Edge object specifying the edge from which distance1 is measured.")*, *[distance1](#abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges.distance1 "abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges.distance1 (Python parameter) — A Float specifying the offset from edge1.")*, *[edge2](#abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges.edge2 "abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges.edge2 (Python parameter) — An Edge object specifying the edge from which distance2 is measured.")*, *[distance2](#abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges.distance2 "abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges.distance2 (Python parameter) — A Float specifying the offset from edge2.")*, *[depth](#abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges.depth "abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges.depth (Python parameter) — A Float specifying the depth of the hole.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L1140-L1188)[¶](#abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges "Permalink to this definition")
    :   This method creates an additional Feature object by creating a circular blind hole of the given
        diameter and depth and cutting away material in the solid and shell regions of the part. The center of
        the hole is offset from two non-parallel straight edges by the given distances.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [HoleBlindFromEdges on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-holeblindfromedgespyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges-parameters "Permalink to this headline")
        :   plane[¶](#abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges.plane "Permalink to this definition")
            :   A Datum plane object or a planar Face object.

            planeSide[¶](#abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges.planeSide "Permalink to this definition")
            :   A SymbolicConstant specifying the direction of feature creation. Possible values are
                SIDE1 and SIDE2.

            diameter[¶](#abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges.diameter "Permalink to this definition")
            :   A Float specifying the diameter of the hole.

            edge1[¶](#abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges.edge1 "Permalink to this definition")
            :   An Edge object specifying the edge from which **distance1** is measured.

            distance1[¶](#abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges.distance1 "Permalink to this definition")
            :   A Float specifying the offset from **edge1**.

            edge2[¶](#abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges.edge2 "Permalink to this definition")
            :   An Edge object specifying the edge from which **distance2** is measured.

            distance2[¶](#abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges.distance2 "Permalink to this definition")
            :   A Float specifying the offset from **edge2**.

            depth[¶](#abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges.depth "Permalink to this definition")
            :   A Float specifying the depth of the hole.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges-return-type "Permalink to this headline")
        :   `Feature`

    HoleFromEdges(*[diameter](#abaqus.Part.PartFeature.PartFeature.HoleFromEdges.diameter "abaqus.Part.PartFeature.PartFeature.HoleFromEdges.diameter (Python parameter) — A Float specifying the diameter of the hole.")*, *[edge1](#abaqus.Part.PartFeature.PartFeature.HoleFromEdges.edge1 "abaqus.Part.PartFeature.PartFeature.HoleFromEdges.edge1 (Python parameter) — An Edge object specifying the edge from which distance1 is measured.")*, *[distance1](#abaqus.Part.PartFeature.PartFeature.HoleFromEdges.distance1 "abaqus.Part.PartFeature.PartFeature.HoleFromEdges.distance1 (Python parameter) — A Float specifying the offset from edge1.")*, *[edge2](#abaqus.Part.PartFeature.PartFeature.HoleFromEdges.edge2 "abaqus.Part.PartFeature.PartFeature.HoleFromEdges.edge2 (Python parameter) — An Edge object specifying the edge from which distance2 is measured.")*, *[distance2](#abaqus.Part.PartFeature.PartFeature.HoleFromEdges.distance2 "abaqus.Part.PartFeature.PartFeature.HoleFromEdges.distance2 (Python parameter) — A Float specifying the offset from edge2.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L1190-L1228)[¶](#abaqus.Part.PartFeature.PartFeature.HoleFromEdges "Permalink to this definition")
    :   This method creates an additional Feature object by creating a circular hole of the given diameter in
        a 2D planar part and cutting away material in the shell and wire regions of the part. The center of the
        hole is offset from two non-parallel straight edges by the given distances.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [HoleFromEdges on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-holefromedgespyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.HoleFromEdges-parameters "Permalink to this headline")
        :   diameter[¶](#abaqus.Part.PartFeature.PartFeature.HoleFromEdges.diameter "Permalink to this definition")
            :   A Float specifying the diameter of the hole.

            edge1[¶](#abaqus.Part.PartFeature.PartFeature.HoleFromEdges.edge1 "Permalink to this definition")
            :   An Edge object specifying the edge from which **distance1** is measured.

            distance1[¶](#abaqus.Part.PartFeature.PartFeature.HoleFromEdges.distance1 "Permalink to this definition")
            :   A Float specifying the offset from **edge1**.

            edge2[¶](#abaqus.Part.PartFeature.PartFeature.HoleFromEdges.edge2 "Permalink to this definition")
            :   An Edge object specifying the edge from which **distance2** is measured.

            distance2[¶](#abaqus.Part.PartFeature.PartFeature.HoleFromEdges.distance2 "Permalink to this definition")
            :   A Float specifying the offset from **edge2**.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.HoleFromEdges-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.HoleFromEdges-return-type "Permalink to this headline")
        :   `Feature`

    HoleThruAllFromEdges(*[plane](#abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges.plane "abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges.plane (Python parameter) — A Datum plane object or a planar Face object.")*, *[planeSide](#abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges.planeSide "abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges.planeSide (Python parameter) — A SymbolicConstant specifying the direction of feature creation.")*, *[diameter](#abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges.diameter "abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges.diameter (Python parameter) — A Float specifying the diameter of the hole.")*, *[edge1](#abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges.edge1 "abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges.edge1 (Python parameter) — An Edge object specifying the edge from which distance1 is measured.")*, *[distance1](#abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges.distance1 "abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges.distance1 (Python parameter) — A Float specifying the offset from edge1.")*, *[edge2](#abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges.edge2 "abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges.edge2 (Python parameter) — An Edge object specifying the edge from which distance2 is measured.")*, *[distance2](#abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges.distance2 "abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges.distance2 (Python parameter) — A Float specifying the offset from edge2.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L1230-L1275)[¶](#abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges "Permalink to this definition")
    :   This method creates an additional Feature object by creating a circular through hole of the given
        diameter and cutting away material in the solid and shell regions of the part. The center of the hole is
        offset from two non-parallel straight edges by the given distances.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [HoleThruAllFromEdges on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-holethruallfromedgespyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges-parameters "Permalink to this headline")
        :   plane[¶](#abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges.plane "Permalink to this definition")
            :   A Datum plane object or a planar Face object.

            planeSide[¶](#abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges.planeSide "Permalink to this definition")
            :   A SymbolicConstant specifying the direction of feature creation. Possible values are
                SIDE1 and SIDE2.

            diameter[¶](#abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges.diameter "Permalink to this definition")
            :   A Float specifying the diameter of the hole.

            edge1[¶](#abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges.edge1 "Permalink to this definition")
            :   An Edge object specifying the edge from which **distance1** is measured.

            distance1[¶](#abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges.distance1 "Permalink to this definition")
            :   A Float specifying the offset from **edge1**.

            edge2[¶](#abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges.edge2 "Permalink to this definition")
            :   An Edge object specifying the edge from which **distance2** is measured.

            distance2[¶](#abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges.distance2 "Permalink to this definition")
            :   A Float specifying the offset from **edge2**.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges-return-type "Permalink to this headline")
        :   `Feature`

    MergeEdges(*[edgeList](#abaqus.Part.PartFeature.PartFeature.MergeEdges.edgeList "abaqus.Part.PartFeature.PartFeature.MergeEdges.edgeList (Python parameter) — A sequence of Edge objects specifying the edges to be merged.")=`()`*, *[extendSelection](#abaqus.Part.PartFeature.PartFeature.MergeEdges.extendSelection "abaqus.Part.PartFeature.PartFeature.MergeEdges.extendSelection (Python parameter) — A Boolean specifying whether the user selection needs to be extended to include edges till branching occurs.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L1277-L1302)[¶](#abaqus.Part.PartFeature.PartFeature.MergeEdges "Permalink to this definition")
    :   This method merges edges either by extending the user selection or using only the selected edges.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [MergeEdges on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mergeedgespyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.MergeEdges-parameters "Permalink to this headline")
        :   edgeList=`()`[¶](#abaqus.Part.PartFeature.PartFeature.MergeEdges.edgeList "Permalink to this definition")
            :   A sequence of Edge objects specifying the edges to be merged.

            extendSelection=`0`[¶](#abaqus.Part.PartFeature.PartFeature.MergeEdges.extendSelection "Permalink to this definition")
            :   A Boolean specifying whether the user selection needs to be extended to include edges
                till branching occurs. Branching is said to occur when the vertex of an edge is shared
                by more than two edges.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.MergeEdges-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.MergeEdges-return-type "Permalink to this headline")
        :   `Feature`

    Mirror(*[mirrorPlane](#abaqus.Part.PartFeature.PartFeature.Mirror.mirrorPlane "abaqus.Part.PartFeature.PartFeature.Mirror.mirrorPlane (Python parameter) — A Datum plane object or a planar Face object.")*, *[keepOriginal](#abaqus.Part.PartFeature.PartFeature.Mirror.keepOriginal "abaqus.Part.PartFeature.PartFeature.Mirror.keepOriginal (Python parameter) — A boolean specifying whether or not the original part geometry should be retained.")*, *[keepInternalBoundaries](#abaqus.Part.PartFeature.PartFeature.Mirror.keepInternalBoundaries "abaqus.Part.PartFeature.PartFeature.Mirror.keepInternalBoundaries (Python parameter) — A Boolean specifying whether internal boundaries will be retained.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L579-L610)[¶](#abaqus.Part.PartFeature.PartFeature.Mirror "Permalink to this definition")
    :   This method mirrors existing part geometry across a plane to create new geometry.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [Mirror on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mirrorpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.Mirror-parameters "Permalink to this headline")
        :   mirrorPlane[¶](#abaqus.Part.PartFeature.PartFeature.Mirror.mirrorPlane "Permalink to this definition")
            :   A Datum plane object or a planar Face object.

            keepOriginal[¶](#abaqus.Part.PartFeature.PartFeature.Mirror.keepOriginal "Permalink to this definition")
            :   A boolean specifying whether or not the original part geometry should be retained.

            keepInternalBoundaries=`0`[¶](#abaqus.Part.PartFeature.PartFeature.Mirror.keepInternalBoundaries "Permalink to this definition")
            :   A Boolean specifying whether internal boundaries will be retained. The default value is
                OFF.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.Mirror-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.Mirror-return-type "Permalink to this headline")
        :   `Feature`

    OffsetFaces(*[faceList](#abaqus.Part.PartFeature.PartFeature.OffsetFaces.faceList "abaqus.Part.PartFeature.PartFeature.OffsetFaces.faceList (Python parameter) — A sequence of Face objects specifying the faces that will be offset.")*, *[distance](#abaqus.Part.PartFeature.PartFeature.OffsetFaces.distance "abaqus.Part.PartFeature.PartFeature.OffsetFaces.distance (Python parameter) — A Float indicating the distance to offset the faces.")=`None`*, *[targetFaces](#abaqus.Part.PartFeature.PartFeature.OffsetFaces.targetFaces "abaqus.Part.PartFeature.PartFeature.OffsetFaces.targetFaces (Python parameter) — A sequence of Face objects whose distance to the faces argument together with the targetFacesMethod determines the distance to offset the faces.")=`()`*, *[targetFacesMethod](#abaqus.Part.PartFeature.PartFeature.OffsetFaces.targetFacesMethod "abaqus.Part.PartFeature.PartFeature.OffsetFaces.targetFacesMethod (Python parameter) — A SymbolicConstant indicating how to calculate the distance to offset.")=`None`*, *[fractionDistance](#abaqus.Part.PartFeature.PartFeature.OffsetFaces.fractionDistance "abaqus.Part.PartFeature.PartFeature.OffsetFaces.fractionDistance (Python parameter) — A Float indicating the fraction of the distance to the closest or the farthest point on the target faces.")=`None`*, *[trimToReferenceRep](#abaqus.Part.PartFeature.PartFeature.OffsetFaces.trimToReferenceRep "abaqus.Part.PartFeature.PartFeature.OffsetFaces.trimToReferenceRep (Python parameter) — A Boolean indicating whether to extend the offset faces and trim them along their intersection with the reference representation.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L1304-L1357)[¶](#abaqus.Part.PartFeature.PartFeature.OffsetFaces "Permalink to this definition")
    :   This method creates new faces by offsetting existing faces.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [OffsetFaces on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-offsetfacespyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.OffsetFaces-parameters "Permalink to this headline")
        :   faceList[¶](#abaqus.Part.PartFeature.PartFeature.OffsetFaces.faceList "Permalink to this definition")
            :   A sequence of Face objects specifying the faces that will be offset. The faces may
                belong to the part or to the reference representation associated with the part.

            distance=`None`[¶](#abaqus.Part.PartFeature.PartFeature.OffsetFaces.distance "Permalink to this definition")
            :   A Float indicating the distance to offset the faces. Either **distance** or **targetFaces**
                must be specified.

            targetFaces=`()`[¶](#abaqus.Part.PartFeature.PartFeature.OffsetFaces.targetFaces "Permalink to this definition")
            :   A sequence of Face objects whose distance to the faces argument together with the
                **targetFacesMethod** determines the distance to offset the faces. Either **distance** or
                **targetFaces** must be specified.

            targetFacesMethod=`None`[¶](#abaqus.Part.PartFeature.PartFeature.OffsetFaces.targetFacesMethod "Permalink to this definition")
            :   A SymbolicConstant indicating how to calculate the distance to offset. It can have one
                of the following values:HALF\_OF\_AVERAGE: Offset the faces by a distance equals to half
                the average distance to target faces.CLOSEST\_POINT\_FRACTION: Offset the faces by a
                distance equals to the fraction of the distance to the approximate closest point on the
                selected target faces.FARTHEST\_POINT\_FRACTION: Offset the faces by a distance equals to
                the fraction of the distance to the approximate farthest point on the selected target
                faces.

            fractionDistance=`None`[¶](#abaqus.Part.PartFeature.PartFeature.OffsetFaces.fractionDistance "Permalink to this definition")
            :   A Float indicating the fraction of the distance to the closest or the farthest point on
                the target faces. Its default value is 0.5.

            trimToReferenceRep=`0`[¶](#abaqus.Part.PartFeature.PartFeature.OffsetFaces.trimToReferenceRep "Permalink to this definition")
            :   A Boolean indicating whether to extend the offset faces and trim them along their
                intersection with the reference representation.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.OffsetFaces-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.OffsetFaces-return-type "Permalink to this headline")
        :   `Feature`

    RemoveCells(*[cellList](#abaqus.Part.PartFeature.PartFeature.RemoveCells.cellList "abaqus.Part.PartFeature.PartFeature.RemoveCells.cellList (Python parameter) — A sequence of Cell objects specifying the cells to remove.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L1359-L1383)[¶](#abaqus.Part.PartFeature.PartFeature.RemoveCells "Permalink to this definition")
    :   This method converts a solid entity to a shell entity.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [RemoveCells on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-removecellspyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.RemoveCells-parameters "Permalink to this headline")
        :   cellList[¶](#abaqus.Part.PartFeature.PartFeature.RemoveCells.cellList "Permalink to this definition")
            :   A sequence of Cell objects specifying the cells to remove.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.RemoveCells-returns "Permalink to this headline")
        :   A Boolean value.

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.RemoveCells-return-type "Permalink to this headline")
        :   `Boolean`

        Raises:[¶](#abaqus.Part.PartFeature.PartFeature.RemoveCells-raises "Permalink to this headline")
        :   **Parterror** – If the intended volume to be turned into a shell entity is not three-dimensional.

    RemoveFaces(*[faceList](#abaqus.Part.PartFeature.PartFeature.RemoveFaces.faceList "abaqus.Part.PartFeature.PartFeature.RemoveFaces.faceList (Python parameter) — A sequence of Face objects specifying the faces to remove.")*, *[deleteCells](#abaqus.Part.PartFeature.PartFeature.RemoveFaces.deleteCells "abaqus.Part.PartFeature.PartFeature.RemoveFaces.deleteCells (Python parameter) — A Boolean specifying whether all cells are to be deleted when the faces are removed.")=`False`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L1385-L1409)[¶](#abaqus.Part.PartFeature.PartFeature.RemoveFaces "Permalink to this definition")
    :   This method removes faces from a solid entity or from a shell entity.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [RemoveFaces on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-removefacespyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.RemoveFaces-parameters "Permalink to this headline")
        :   faceList[¶](#abaqus.Part.PartFeature.PartFeature.RemoveFaces.faceList "Permalink to this definition")
            :   A sequence of Face objects specifying the faces to remove.

            deleteCells=`False`[¶](#abaqus.Part.PartFeature.PartFeature.RemoveFaces.deleteCells "Permalink to this definition")
            :   A Boolean specifying whether all cells are to be deleted when the faces are removed. The
                default value is False.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.RemoveFaces-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.RemoveFaces-return-type "Permalink to this headline")
        :   `Feature`

    RemoveFacesAndStitch(*[faceList](#abaqus.Part.PartFeature.PartFeature.RemoveFacesAndStitch.faceList "abaqus.Part.PartFeature.PartFeature.RemoveFacesAndStitch.faceList (Python parameter) — A sequence of Face objects specifying the faces to remove.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L1411-L1433)[¶](#abaqus.Part.PartFeature.PartFeature.RemoveFacesAndStitch "Permalink to this definition")
    :   This method removes faces from a solid entity and attempts to close the resulting gap by extending
        the neighboring faces of the solid.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [RemoveFacesAndStitch on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-removefacesandstitchpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.RemoveFacesAndStitch-parameters "Permalink to this headline")
        :   faceList[¶](#abaqus.Part.PartFeature.PartFeature.RemoveFacesAndStitch.faceList "Permalink to this definition")
            :   A sequence of Face objects specifying the faces to remove.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.RemoveFacesAndStitch-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.RemoveFacesAndStitch-return-type "Permalink to this headline")
        :   `Feature`

    RemoveRedundantEntities(*[vertexList](#abaqus.Part.PartFeature.PartFeature.RemoveRedundantEntities.vertexList "abaqus.Part.PartFeature.PartFeature.RemoveRedundantEntities.vertexList (Python parameter) — A sequence of ConstrainedSketchVertex objects specifying the vertices to be removed.")=`()`*, *[edgeList](#abaqus.Part.PartFeature.PartFeature.RemoveRedundantEntities.edgeList "abaqus.Part.PartFeature.PartFeature.RemoveRedundantEntities.edgeList (Python parameter) — A sequence of Edge objects specifying the edges to be removed.")=`()`*, *[removeEdgeVertices](#abaqus.Part.PartFeature.PartFeature.RemoveRedundantEntities.removeEdgeVertices "abaqus.Part.PartFeature.PartFeature.RemoveRedundantEntities.removeEdgeVertices (Python parameter) — A Boolean specifying whether the vertices of the redundant edges need to be removed.")=`True`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L1435-L1472)[¶](#abaqus.Part.PartFeature.PartFeature.RemoveRedundantEntities "Permalink to this definition")
    :   This method removes redundant edges and vertices from a solid or a shell entity. One of the two
        arguments is required.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [RemoveRedundantEntities on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-removeredundantentitiespyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.RemoveRedundantEntities-parameters "Permalink to this headline")
        :   vertexList=`()`[¶](#abaqus.Part.PartFeature.PartFeature.RemoveRedundantEntities.vertexList "Permalink to this definition")
            :   A sequence of ConstrainedSketchVertex objects specifying the vertices to be removed.

            edgeList=`()`[¶](#abaqus.Part.PartFeature.PartFeature.RemoveRedundantEntities.edgeList "Permalink to this definition")
            :   A sequence of Edge objects specifying the edges to be removed.

            removeEdgeVertices=`True`[¶](#abaqus.Part.PartFeature.PartFeature.RemoveRedundantEntities.removeEdgeVertices "Permalink to this definition")
            :   A Boolean specifying whether the vertices of the redundant edges need to be removed. The
                default is True.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.RemoveRedundantEntities-returns "Permalink to this headline")
        :   A Feature object.

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.RemoveRedundantEntities-return-type "Permalink to this headline")
        :   `Feature`

        Raises:[¶](#abaqus.Part.PartFeature.PartFeature.RemoveRedundantEntities-raises "Permalink to this headline")
        :   **Parterror** – None of the selected entities are redundant, If the selected entity is not a redundant entity.

    RepairFaceNormals(*[faceList](#abaqus.Part.PartFeature.PartFeature.RepairFaceNormals.faceList "abaqus.Part.PartFeature.PartFeature.RepairFaceNormals.faceList (Python parameter) — A sequence of Face objects.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L1474-L1498)[¶](#abaqus.Part.PartFeature.PartFeature.RepairFaceNormals "Permalink to this definition")
    :   This method works on the entire part or a sequence of shell faces. When the entire part is selected,
        it aligns all the shell face normals, and inverts all of the solid faces’ normals if the solid was
        originally inside out. When a few shell faces are selected, it inverts the normals of the selected
        faces.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [RepairFaceNormals on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-repairfacenormalspyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.RepairFaceNormals-parameters "Permalink to this headline")
        :   faceList=`()`[¶](#abaqus.Part.PartFeature.PartFeature.RepairFaceNormals.faceList "Permalink to this definition")
            :   A sequence of Face objects.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.RepairFaceNormals-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.RepairFaceNormals-return-type "Permalink to this headline")
        :   `Feature`

    RepairInvalidEdges(*[edgeList](#abaqus.Part.PartFeature.PartFeature.RepairInvalidEdges.edgeList "abaqus.Part.PartFeature.PartFeature.RepairInvalidEdges.edgeList (Python parameter) — A sequence of Edge objects.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L1500-L1522)[¶](#abaqus.Part.PartFeature.PartFeature.RepairInvalidEdges "Permalink to this definition")
    :   This method repairs invalid edges. It will always attempt to improve edges even if none of selected
        edges are initially invalid and may leave behind invalid edges that could not be repaired.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [RepairInvalidEdges on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-repairinvalidedgespyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.RepairInvalidEdges-parameters "Permalink to this headline")
        :   edgeList[¶](#abaqus.Part.PartFeature.PartFeature.RepairInvalidEdges.edgeList "Permalink to this definition")
            :   A sequence of Edge objects.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.RepairInvalidEdges-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.RepairInvalidEdges-return-type "Permalink to this headline")
        :   `Feature`

    RepairSliver(*[face](#abaqus.Part.PartFeature.PartFeature.RepairSliver.face "abaqus.Part.PartFeature.PartFeature.RepairSliver.face (Python parameter) — A Face object specifying the face on which the sliver is located.")*, *[point1](#abaqus.Part.PartFeature.PartFeature.RepairSliver.point1 "abaqus.Part.PartFeature.PartFeature.RepairSliver.point1 (Python parameter) — A point specifying the location for partition creation.")*, *[point2](#abaqus.Part.PartFeature.PartFeature.RepairSliver.point2 "abaqus.Part.PartFeature.PartFeature.RepairSliver.point2 (Python parameter) — A point specifying the location for partition creation.")*, *[toleranceChecks](#abaqus.Part.PartFeature.PartFeature.RepairSliver.toleranceChecks "abaqus.Part.PartFeature.PartFeature.RepairSliver.toleranceChecks (Python parameter) — A Boolean specifying whether to use internal tolerance checks to restrict the size of the sliver face being removed.")=`True`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L1524-L1556)[¶](#abaqus.Part.PartFeature.PartFeature.RepairSliver "Permalink to this definition")
    :   This method repairs the selected sliver from the selected face. The sliver area is specified using
        two points. A face partition is carried out at the specified points and the smaller of the two faces is
        removed.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [RepairSliver on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-repairsliverpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.RepairSliver-parameters "Permalink to this headline")
        :   face[¶](#abaqus.Part.PartFeature.PartFeature.RepairSliver.face "Permalink to this definition")
            :   A Face object specifying the face on which the sliver is located.

            point1[¶](#abaqus.Part.PartFeature.PartFeature.RepairSliver.point1 "Permalink to this definition")
            :   A point specifying the location for partition creation. It can be a ConstrainedSketchVertex object, an
                Interesting Point or three coordinates specifying the point on an edge of the **face**.

            point2[¶](#abaqus.Part.PartFeature.PartFeature.RepairSliver.point2 "Permalink to this definition")
            :   A point specifying the location for partition creation. It can be a ConstrainedSketchVertex object, an
                Interesting Point or three coordinates specifying the point on an edge of the **face**.

            toleranceChecks=`True`[¶](#abaqus.Part.PartFeature.PartFeature.RepairSliver.toleranceChecks "Permalink to this definition")
            :   A Boolean specifying whether to use internal tolerance checks to restrict the size of
                the sliver face being removed. The default is True.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.RepairSliver-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.RepairSliver-return-type "Permalink to this headline")
        :   `Feature`

    RepairSmallEdges(*[edgeList](#abaqus.Part.PartFeature.PartFeature.RepairSmallEdges.edgeList "abaqus.Part.PartFeature.PartFeature.RepairSmallEdges.edgeList (Python parameter) — A sequence of Edge objects.")*, *[toleranceChecks](#abaqus.Part.PartFeature.PartFeature.RepairSmallEdges.toleranceChecks "abaqus.Part.PartFeature.PartFeature.RepairSmallEdges.toleranceChecks (Python parameter) — A Boolean specifying whether to use internal tolerance checks to restrict the size of the edges being removed.")=`True`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L1558-L1584)[¶](#abaqus.Part.PartFeature.PartFeature.RepairSmallEdges "Permalink to this definition")
    :   This method repairs small edges. This method will attempt to replace selected small edges with
        vertices and extend the adjacent faces and edges. This method might leave behind some small edges that
        cannot be removed.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [RepairSmallEdges on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-repairsmalledgespyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.RepairSmallEdges-parameters "Permalink to this headline")
        :   edgeList[¶](#abaqus.Part.PartFeature.PartFeature.RepairSmallEdges.edgeList "Permalink to this definition")
            :   A sequence of Edge objects.

            toleranceChecks=`True`[¶](#abaqus.Part.PartFeature.PartFeature.RepairSmallEdges.toleranceChecks "Permalink to this definition")
            :   A Boolean specifying whether to use internal tolerance checks to restrict the size of
                the edges being removed. The default is True.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.RepairSmallEdges-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.RepairSmallEdges-return-type "Permalink to this headline")
        :   `Feature`

    RepairSmallFaces(*[faceList](#abaqus.Part.PartFeature.PartFeature.RepairSmallFaces.faceList "abaqus.Part.PartFeature.PartFeature.RepairSmallFaces.faceList (Python parameter) — A sequence of Face objects.")*, *[toleranceChecks](#abaqus.Part.PartFeature.PartFeature.RepairSmallFaces.toleranceChecks "abaqus.Part.PartFeature.PartFeature.RepairSmallFaces.toleranceChecks (Python parameter) — A Boolean specifying whether to use internal tolerance checks to restrict the size of the faces being removed.")=`True`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L1586-L1612)[¶](#abaqus.Part.PartFeature.PartFeature.RepairSmallFaces "Permalink to this definition")
    :   This method repairs small faces. It will attempt to replace the selected small faces with edges or
        vertices and extend the adjacent faces. This method might leave behind some small faces that cannot be
        removed.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [RepairSmallFaces on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-repairsmallfacespyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.RepairSmallFaces-parameters "Permalink to this headline")
        :   faceList[¶](#abaqus.Part.PartFeature.PartFeature.RepairSmallFaces.faceList "Permalink to this definition")
            :   A sequence of Face objects.

            toleranceChecks=`True`[¶](#abaqus.Part.PartFeature.PartFeature.RepairSmallFaces.toleranceChecks "Permalink to this definition")
            :   A Boolean specifying whether to use internal tolerance checks to restrict the size of
                the faces being removed. The default is True.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.RepairSmallFaces-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.RepairSmallFaces-return-type "Permalink to this headline")
        :   `Feature`

    ReplaceFaces(*[faceList](#abaqus.Part.PartFeature.PartFeature.ReplaceFaces.faceList "abaqus.Part.PartFeature.PartFeature.ReplaceFaces.faceList (Python parameter) — A sequence of Face objects to be replaced.")*, *[stitch](#abaqus.Part.PartFeature.PartFeature.ReplaceFaces.stitch "abaqus.Part.PartFeature.PartFeature.ReplaceFaces.stitch (Python parameter) — A Boolean specifying whether the newly created face needs to be stitched to the existing geometry.")=`True`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L1614-L1639)[¶](#abaqus.Part.PartFeature.PartFeature.ReplaceFaces "Permalink to this definition")
    :   This method replaces the selected faces with a single face. If one single face is selected, that
        alone is replaced with a new face.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [ReplaceFaces on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-replacefacespyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.ReplaceFaces-parameters "Permalink to this headline")
        :   faceList[¶](#abaqus.Part.PartFeature.PartFeature.ReplaceFaces.faceList "Permalink to this definition")
            :   A sequence of Face objects to be replaced.

            stitch=`True`[¶](#abaqus.Part.PartFeature.PartFeature.ReplaceFaces.stitch "Permalink to this definition")
            :   A Boolean specifying whether the newly created face needs to be stitched to the existing
                geometry. The default is True.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.ReplaceFaces-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.ReplaceFaces-return-type "Permalink to this headline")
        :   `Feature`

    Round(*[radius](#abaqus.Part.PartFeature.PartFeature.Round.radius "abaqus.Part.PartFeature.PartFeature.Round.radius (Python parameter) — A Float specifying the radius of the fillets.")*, *[edgeList](#abaqus.Part.PartFeature.PartFeature.Round.edgeList "abaqus.Part.PartFeature.PartFeature.Round.edgeList (Python parameter) — A sequence of Edge objects.")=`None`*, *[vertexList](#abaqus.Part.PartFeature.PartFeature.Round.vertexList "abaqus.Part.PartFeature.PartFeature.Round.vertexList (Python parameter) — A sequence of ConstrainedSketchVertex objects.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L1641-L1676)[¶](#abaqus.Part.PartFeature.PartFeature.Round "Permalink to this definition")
    :   This method creates an additional Feature object by rounding (filleting) the given list of entities
        with the given radius.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [Round on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-roundpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.Round-parameters "Permalink to this headline")
        :   radius[¶](#abaqus.Part.PartFeature.PartFeature.Round.radius "Permalink to this definition")
            :   A Float specifying the radius of the fillets.

            edgeList=`None`[¶](#abaqus.Part.PartFeature.PartFeature.Round.edgeList "Permalink to this definition")
            :   A sequence of Edge objects. Solid and Shell edges of a part can be rounded. The
                operation will fail for non-manifold edges. The **edgeList** and **vertexList** arguments
                are mutually exclusive. One of them must be specified.

            vertexList=`None`[¶](#abaqus.Part.PartFeature.PartFeature.Round.vertexList "Permalink to this definition")
            :   A sequence of ConstrainedSketchVertex objects. Vertices that are connected to two wire edges can be
                rounded. The operation will fail for a vertex connected to a face. The **edgeList** and
                **vertexList** arguments are mutually exclusive. One of them must be specified.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.Round-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.Round-return-type "Permalink to this headline")
        :   `Feature`

    Shell(*[sketchPlane](#abaqus.Part.PartFeature.PartFeature.Shell.sketchPlane "abaqus.Part.PartFeature.PartFeature.Shell.sketchPlane (Python parameter) — A Datum plane object or a planar Face object.")*, *[sketchPlaneSide](#abaqus.Part.PartFeature.PartFeature.Shell.sketchPlaneSide "abaqus.Part.PartFeature.PartFeature.Shell.sketchPlaneSide (Python parameter) — A SymbolicConstant specifying the direction of feature creation.")*, *[sketchUpEdge](#abaqus.Part.PartFeature.PartFeature.Shell.sketchUpEdge "abaqus.Part.PartFeature.PartFeature.Shell.sketchUpEdge (Python parameter) — An Edge object or a Datum axis object specifying the vertical (Y) direction of the sketch.")*, *[sketch](#abaqus.Part.PartFeature.PartFeature.Shell.sketch "abaqus.Part.PartFeature.PartFeature.Shell.sketch (Python parameter) — A ConstrainedSketch object specifying the planar shell.")*, *[sketchOrientation](#abaqus.Part.PartFeature.PartFeature.Shell.sketchOrientation "abaqus.Part.PartFeature.PartFeature.Shell.sketchOrientation (Python parameter) — A SymbolicConstant specifying the orientation of sketchUpEdge on the sketch.")=`abaqusConstants.RIGHT`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L1678-L1718)[¶](#abaqus.Part.PartFeature.PartFeature.Shell "Permalink to this definition")
    :   This method creates an additional Feature object by creating a planar shell from the given
        ConstrainedSketch object. The ConstrainedSketch object must define a closed profile.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [Shell on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shellpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.Shell-parameters "Permalink to this headline")
        :   sketchPlane[¶](#abaqus.Part.PartFeature.PartFeature.Shell.sketchPlane "Permalink to this definition")
            :   A Datum plane object or a planar Face object.

            sketchPlaneSide[¶](#abaqus.Part.PartFeature.PartFeature.Shell.sketchPlaneSide "Permalink to this definition")
            :   A SymbolicConstant specifying the direction of feature creation. Possible values are
                SIDE1 and SIDE2.

            sketchUpEdge[¶](#abaqus.Part.PartFeature.PartFeature.Shell.sketchUpEdge "Permalink to this definition")
            :   An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the
                sketch.

            sketch[¶](#abaqus.Part.PartFeature.PartFeature.Shell.sketch "Permalink to this definition")
            :   A ConstrainedSketch object specifying the planar shell.

            sketchOrientation=`abaqusConstants.RIGHT`[¶](#abaqus.Part.PartFeature.PartFeature.Shell.sketchOrientation "Permalink to this definition")
            :   A SymbolicConstant specifying the orientation of **sketchUpEdge** on the sketch. Possible
                values are RIGHT, LEFT, TOP, and BOTTOM. The default value is RIGHT.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.Shell-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.Shell-return-type "Permalink to this headline")
        :   `Feature`

    ShellExtrude(*[sketchPlane](#abaqus.Part.PartFeature.PartFeature.ShellExtrude.sketchPlane "abaqus.Part.PartFeature.PartFeature.ShellExtrude.sketchPlane (Python parameter) — A Datum plane object or a planar Face object.")*, *[sketchPlaneSide](#abaqus.Part.PartFeature.PartFeature.ShellExtrude.sketchPlaneSide "abaqus.Part.PartFeature.PartFeature.ShellExtrude.sketchPlaneSide (Python parameter) — A SymbolicConstant specifying the direction of feature creation.")*, *[sketchUpEdge](#abaqus.Part.PartFeature.PartFeature.ShellExtrude.sketchUpEdge "abaqus.Part.PartFeature.PartFeature.ShellExtrude.sketchUpEdge (Python parameter) — An Edge object or a Datum axis object specifying the vertical (Y) direction of the sketch.")*, *[sketch](#abaqus.Part.PartFeature.PartFeature.ShellExtrude.sketch "abaqus.Part.PartFeature.PartFeature.ShellExtrude.sketch (Python parameter) — A ConstrainedSketch object specifying the planar sketch to be extruded.")*, *[depth](#abaqus.Part.PartFeature.PartFeature.ShellExtrude.depth "abaqus.Part.PartFeature.PartFeature.ShellExtrude.depth (Python parameter) — A Float specifying the extrusion depth.")=`None`*, *[upToFace](#abaqus.Part.PartFeature.PartFeature.ShellExtrude.upToFace "abaqus.Part.PartFeature.PartFeature.ShellExtrude.upToFace (Python parameter) — A Face specifying the face up to which to extrude.")=`''`*, *[sketchOrientation](#abaqus.Part.PartFeature.PartFeature.ShellExtrude.sketchOrientation "abaqus.Part.PartFeature.PartFeature.ShellExtrude.sketchOrientation (Python parameter) — A SymbolicConstant specifying the orientation of sketchUpEdge on the sketch.")=`abaqusConstants.RIGHT`*, *[draftAngle](#abaqus.Part.PartFeature.PartFeature.ShellExtrude.draftAngle "abaqus.Part.PartFeature.PartFeature.ShellExtrude.draftAngle (Python parameter) — A Float specifying the draft angle in degrees.")=`None`*, *[pitch](#abaqus.Part.PartFeature.PartFeature.ShellExtrude.pitch "abaqus.Part.PartFeature.PartFeature.ShellExtrude.pitch (Python parameter) — A Float specifying the pitch.")=`None`*, *[flipExtrudeDirection](#abaqus.Part.PartFeature.PartFeature.ShellExtrude.flipExtrudeDirection "abaqus.Part.PartFeature.PartFeature.ShellExtrude.flipExtrudeDirection (Python parameter) — A Boolean specifying whether to override the direction of feature creation.")=`0`*, *[keepInternalBoundaries](#abaqus.Part.PartFeature.PartFeature.ShellExtrude.keepInternalBoundaries "abaqus.Part.PartFeature.PartFeature.ShellExtrude.keepInternalBoundaries (Python parameter) — A Boolean specifying whether internal boundaries will be retained.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L1720-L1795)[¶](#abaqus.Part.PartFeature.PartFeature.ShellExtrude "Permalink to this definition")
    :   This method creates an additional Feature object by extruding the given ConstrainedSketch object by
        the given depth, creating a shell protrusion. The ConstrainedSketch object can define either an open or
        closed profile.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [ShellExtrude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shellextrudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.ShellExtrude-parameters "Permalink to this headline")
        :   sketchPlane[¶](#abaqus.Part.PartFeature.PartFeature.ShellExtrude.sketchPlane "Permalink to this definition")
            :   A Datum plane object or a planar Face object.

            sketchPlaneSide[¶](#abaqus.Part.PartFeature.PartFeature.ShellExtrude.sketchPlaneSide "Permalink to this definition")
            :   A SymbolicConstant specifying the direction of feature creation. Possible values are
                SIDE1 and SIDE2.

            sketchUpEdge[¶](#abaqus.Part.PartFeature.PartFeature.ShellExtrude.sketchUpEdge "Permalink to this definition")
            :   An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the
                sketch.

            sketch[¶](#abaqus.Part.PartFeature.PartFeature.ShellExtrude.sketch "Permalink to this definition")
            :   A ConstrainedSketch object specifying the planar sketch to be extruded.

            depth=`None`[¶](#abaqus.Part.PartFeature.PartFeature.ShellExtrude.depth "Permalink to this definition")
            :   A Float specifying the extrusion depth. The default is to not specify a depth. Either
                **depth** or **upToFace** must be used to define the extrusion depth.

            upToFace=`''`[¶](#abaqus.Part.PartFeature.PartFeature.ShellExtrude.upToFace "Permalink to this definition")
            :   A Face specifying the face up to which to extrude. If **upToFace** is specified, the
                extrusion will be an up-to-face extrusion. The default is to not specify a face. Either
                **depth** or **upToFace** must be used to define the extrusion depth.

            sketchOrientation=`abaqusConstants.RIGHT`[¶](#abaqus.Part.PartFeature.PartFeature.ShellExtrude.sketchOrientation "Permalink to this definition")
            :   A SymbolicConstant specifying the orientation of **sketchUpEdge** on the sketch. Possible
                values are RIGHT, LEFT, TOP, and BOTTOM. The default value is RIGHT.

            draftAngle=`None`[¶](#abaqus.Part.PartFeature.PartFeature.ShellExtrude.draftAngle "Permalink to this definition")
            :   A Float specifying the draft angle in degrees. Possible values are -90.0 ≤ **draftAngle**
                ≤ 90.0. By convention, for a positive draft angle an outer loop will draft outward and
                an inner loop will draft inward. The opposite is true for a negative draft angle. The
                default value, 0, implies a normal extrude. The arguments **draftAngle** and **pitch** are
                mutually exclusive.

            pitch=`None`[¶](#abaqus.Part.PartFeature.PartFeature.ShellExtrude.pitch "Permalink to this definition")
            :   A Float specifying the pitch. The pitch is the distance traveled along the axial
                direction by the sketch when the sketch has completed one full revolution about the
                twist axis. Pitch can be specified as positive or negative to achieve right-handed or
                left-handed twist about the twist axis, respectively. The default value, 0, implies a
                normal extrude. Possible values are -10⁵ ≤ **pitch** ≤ 10⁵. The arguments **draftAngle**
                and **pitch** are mutually exclusive.

            flipExtrudeDirection=`0`[¶](#abaqus.Part.PartFeature.PartFeature.ShellExtrude.flipExtrudeDirection "Permalink to this definition")
            :   A Boolean specifying whether to override the direction of feature creation. If the value
                is OFF, it means use the direction defined by the **sketchPlaneSide**; if the value is ON,
                it means use the opposite direction to the one defined by **sketchPlaneSide**. The default
                value is OFF.

            keepInternalBoundaries=`0`[¶](#abaqus.Part.PartFeature.PartFeature.ShellExtrude.keepInternalBoundaries "Permalink to this definition")
            :   A Boolean specifying whether internal boundaries will be retained. The default value is
                OFF.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.ShellExtrude-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.ShellExtrude-return-type "Permalink to this headline")
        :   `Feature`

    ShellLoft(*[loftsections](#abaqus.Part.PartFeature.PartFeature.ShellLoft.loftsections "abaqus.Part.PartFeature.PartFeature.ShellLoft.loftsections (Python parameter) — A sequence of sequences of edges specifying the cross-sections to be lofted.")*, *[startCondition](#abaqus.Part.PartFeature.PartFeature.ShellLoft.startCondition "abaqus.Part.PartFeature.PartFeature.ShellLoft.startCondition (Python parameter) — A SymbolicConstant specifying the tangent direction at the start section of the loft feature.")=`None`*, *[endCondition](#abaqus.Part.PartFeature.PartFeature.ShellLoft.endCondition "abaqus.Part.PartFeature.PartFeature.ShellLoft.endCondition (Python parameter) — A SymbolicConstant specifying the tangent direction at the end section of the loft feature.")=`None`*, *[startTangent](#abaqus.Part.PartFeature.PartFeature.ShellLoft.startTangent "abaqus.Part.PartFeature.PartFeature.ShellLoft.startTangent (Python parameter) — A Float specifying the angle in degrees of the tangent with respect to the plane in which the start section lies.")=`None`*, *[startMagnitude](#abaqus.Part.PartFeature.PartFeature.ShellLoft.startMagnitude "abaqus.Part.PartFeature.PartFeature.ShellLoft.startMagnitude (Python parameter) — A Float specifying the magnitude of the startTangent.")=`None`*, *[endTangent](#abaqus.Part.PartFeature.PartFeature.ShellLoft.endTangent "abaqus.Part.PartFeature.PartFeature.ShellLoft.endTangent (Python parameter) — A Float specifying the angle in degrees of the tangent with respect to the plane in which the end section lies.")=`None`*, *[endMagnitude](#abaqus.Part.PartFeature.PartFeature.ShellLoft.endMagnitude "abaqus.Part.PartFeature.PartFeature.ShellLoft.endMagnitude (Python parameter) — A Float specifying the magnitude of the endTangent.")=`None`*, *[paths](#abaqus.Part.PartFeature.PartFeature.ShellLoft.paths "abaqus.Part.PartFeature.PartFeature.ShellLoft.paths (Python parameter) — A sequence of sequences of edges that pass through each section in the loft feature. Each sequence specifies a path followed by the face or an edge created by a loft feature.")=`()`*, *[globalSmoothing](#abaqus.Part.PartFeature.PartFeature.ShellLoft.globalSmoothing "abaqus.Part.PartFeature.PartFeature.ShellLoft.globalSmoothing (Python parameter) — A Boolean specifying whether each path defined in the paths argument is applied locally or globally.If the path is applied locally, its effect is felt only on faces created from the edges on the loftsections through which the paths pass through.If the path is applied globally, an averaging algorithm is applied over all the paths defined and is distributed over all the faces created.The default value is ON (globally).")=`0`*, *[keepInternalBoundaries](#abaqus.Part.PartFeature.PartFeature.ShellLoft.keepInternalBoundaries "abaqus.Part.PartFeature.PartFeature.ShellLoft.keepInternalBoundaries (Python parameter) — A Boolean specifying whether internal boundaries will be retained.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L1797-L1883)[¶](#abaqus.Part.PartFeature.PartFeature.ShellLoft "Permalink to this definition")
    :   This method creates an additional Feature object by lofting between the given sections and adding
        shell faces to the part. You define the sections using a sequence of edges from the part or an
        EdgeArray.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [ShellLoft on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shellloftpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.ShellLoft-parameters "Permalink to this headline")
        :   loftsections[¶](#abaqus.Part.PartFeature.PartFeature.ShellLoft.loftsections "Permalink to this definition")
            :   A sequence of sequences of edges specifying the cross-sections to be lofted. Each outer
                sequence specifies a section through which the method will pass the loft feature. Each
                outer sequence can be defined as a sequence of edges or as an EdgeArray. The edges
                specifying a section must form a simple closed profile and must not contain multiple
                loops.

            startCondition=`None`[¶](#abaqus.Part.PartFeature.PartFeature.ShellLoft.startCondition "Permalink to this definition")
            :   A SymbolicConstant specifying the tangent direction at the start section of the loft
                feature. Possible values are NONE, NORMAL, RADIAL and SPECIFIED. You can specify this
                argument only if the start and end sections are planar. You cannot use this argument in
                conjunction with the **path** argument. You must use the **startCondition** argument in
                conjunction with the **endCondition** argument.

            endCondition=`None`[¶](#abaqus.Part.PartFeature.PartFeature.ShellLoft.endCondition "Permalink to this definition")
            :   A SymbolicConstant specifying the tangent direction at the end section of the loft
                feature. Possible values are NONE, NORMAL, RADIAL and SPECIFIED. You can specify this
                argument only if the start and end sections are planar. You cannot use this argument in
                conjunction with the **path** argument. You must use the **endCondition** argument in
                conjunction with the **startCondition** argument.

            startTangent=`None`[¶](#abaqus.Part.PartFeature.PartFeature.ShellLoft.startTangent "Permalink to this definition")
            :   A Float specifying the angle in degrees of the tangent with respect to the plane in
                which the start section lies. You must specify the **startTangent** argument if
                **startCondition** = SPECIFIED. Possible values are 0.0 ≤ **startTangent** ≤ 180.0.

            startMagnitude=`None`[¶](#abaqus.Part.PartFeature.PartFeature.ShellLoft.startMagnitude "Permalink to this definition")
            :   A Float specifying the magnitude of the **startTangent**. You must specify the
                **startMagnitude** argument if **startCondition** = SPECIFIED. Possible values are 0.0 <
                **startMagnitude** < 100.0.

            endTangent=`None`[¶](#abaqus.Part.PartFeature.PartFeature.ShellLoft.endTangent "Permalink to this definition")
            :   A Float specifying the angle in degrees of the tangent with respect to the plane in
                which the end section lies. You must specify the **endTangent** argument if
                **startCondition** = SPECIFIED. Possible values are 0.0 ≤ **endTangent** ≤ 180.0.

            endMagnitude=`None`[¶](#abaqus.Part.PartFeature.PartFeature.ShellLoft.endMagnitude "Permalink to this definition")
            :   A Float specifying the magnitude of the **endTangent**. This argument is to be used when
                the **endCondition** argument has the value SPECIFIED. Possible values are 0.0 <
                **endMagnitude** < 100.0.

            paths=`()`[¶](#abaqus.Part.PartFeature.PartFeature.ShellLoft.paths "Permalink to this definition")
            :   A sequence of sequences of edges that pass through each section in the loft feature.
                Each sequence specifies a path followed by the face or an edge created by a loft
                feature. Each path must start at the first section, end at the last section, and pass
                through each section. In addition, the order of the sequences must be the same as the
                order of the sections in the **loftsections** argument. Each path must not self-intersect
                and must be tangent continuous. In addition, the paths must not intersect each other.
                You cannot use the **paths** argument in conjunction with the **startCondition** and
                **endCondition** arguments.

            globalSmoothing=`0`[¶](#abaqus.Part.PartFeature.PartFeature.ShellLoft.globalSmoothing "Permalink to this definition")
            :   A Boolean specifying whether each path defined in the **paths** argument is applied
                locally or globally.If the path is applied locally, its effect is felt only on faces
                created from the edges on the **loftsections** through which the **paths** pass through.If
                the path is applied globally, an averaging algorithm is applied over all the paths
                defined and is distributed over all the faces created.The default value is ON
                (globally).

            keepInternalBoundaries=`0`[¶](#abaqus.Part.PartFeature.PartFeature.ShellLoft.keepInternalBoundaries "Permalink to this definition")
            :   A Boolean specifying whether internal boundaries will be retained. The default value is
                OFF.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.ShellLoft-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.ShellLoft-return-type "Permalink to this headline")
        :   `Feature`

    ShellRevolve(*[sketchPlane](#abaqus.Part.PartFeature.PartFeature.ShellRevolve.sketchPlane "abaqus.Part.PartFeature.PartFeature.ShellRevolve.sketchPlane (Python parameter) — A Datum plane object or a planar Face object.")*, *[sketchPlaneSide](#abaqus.Part.PartFeature.PartFeature.ShellRevolve.sketchPlaneSide "abaqus.Part.PartFeature.PartFeature.ShellRevolve.sketchPlaneSide (Python parameter) — A SymbolicConstant specifying the direction of feature creation.")*, *[sketchUpEdge](#abaqus.Part.PartFeature.PartFeature.ShellRevolve.sketchUpEdge "abaqus.Part.PartFeature.PartFeature.ShellRevolve.sketchUpEdge (Python parameter) — An Edge object or a Datum axis object specifying the vertical (Y) direction of the sketch.")*, *[sketch](#abaqus.Part.PartFeature.PartFeature.ShellRevolve.sketch "abaqus.Part.PartFeature.PartFeature.ShellRevolve.sketch (Python parameter) — A ConstrainedSketch object specifying the planar sketch to be revolved.")*, *[angle](#abaqus.Part.PartFeature.PartFeature.ShellRevolve.angle "abaqus.Part.PartFeature.PartFeature.ShellRevolve.angle (Python parameter) — A Float specifying the angle in degrees to be revolved.")*, *[sketchOrientation](#abaqus.Part.PartFeature.PartFeature.ShellRevolve.sketchOrientation "abaqus.Part.PartFeature.PartFeature.ShellRevolve.sketchOrientation (Python parameter) — A SymbolicConstant specifying the orientation of sketchUpEdge on the sketch.")=`abaqusConstants.RIGHT`*, *[pitch](#abaqus.Part.PartFeature.PartFeature.ShellRevolve.pitch "abaqus.Part.PartFeature.PartFeature.ShellRevolve.pitch (Python parameter) — A Float specifying the pitch.")=`None`*, *[flipRevolveDirection](#abaqus.Part.PartFeature.PartFeature.ShellRevolve.flipRevolveDirection "abaqus.Part.PartFeature.PartFeature.ShellRevolve.flipRevolveDirection (Python parameter) — A Boolean specifying whether to override the direction of feature creation.")=`0`*, *[flipPitchDirection](#abaqus.Part.PartFeature.PartFeature.ShellRevolve.flipPitchDirection "abaqus.Part.PartFeature.PartFeature.ShellRevolve.flipPitchDirection (Python parameter) — A Boolean specifying whether to override the direction of translation.")=`0`*, *[moveSketchNormalToPath](#abaqus.Part.PartFeature.PartFeature.ShellRevolve.moveSketchNormalToPath "abaqus.Part.PartFeature.PartFeature.ShellRevolve.moveSketchNormalToPath (Python parameter) — A Boolean specifying whether to rotate the sketch so that it is normal to the path of revolution when using the pitch option.")=`0`*, *[keepInternalBoundaries](#abaqus.Part.PartFeature.PartFeature.ShellRevolve.keepInternalBoundaries "abaqus.Part.PartFeature.PartFeature.ShellRevolve.keepInternalBoundaries (Python parameter) — A Boolean specifying whether internal boundaries will be retained.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L1885-L1958)[¶](#abaqus.Part.PartFeature.PartFeature.ShellRevolve "Permalink to this definition")
    :   This method creates an additional Feature object by revolving the given ConstrainedSketch object by
        the given angle, creating a shell protrusion. The ConstrainedSketch object can define either an open or
        closed profile and an axis of revolution. The axis is defined by a single construction line. For a
        description of the plane positioning arguments, see SolidExtrude.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [ShellRevolve on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shellrevolvepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.ShellRevolve-parameters "Permalink to this headline")
        :   sketchPlane[¶](#abaqus.Part.PartFeature.PartFeature.ShellRevolve.sketchPlane "Permalink to this definition")
            :   A Datum plane object or a planar Face object.

            sketchPlaneSide[¶](#abaqus.Part.PartFeature.PartFeature.ShellRevolve.sketchPlaneSide "Permalink to this definition")
            :   A SymbolicConstant specifying the direction of feature creation. Possible values are
                SIDE1 and SIDE2.

            sketchUpEdge[¶](#abaqus.Part.PartFeature.PartFeature.ShellRevolve.sketchUpEdge "Permalink to this definition")
            :   An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the
                sketch.

            sketch[¶](#abaqus.Part.PartFeature.PartFeature.ShellRevolve.sketch "Permalink to this definition")
            :   A ConstrainedSketch object specifying the planar sketch to be revolved.

            angle[¶](#abaqus.Part.PartFeature.PartFeature.ShellRevolve.angle "Permalink to this definition")
            :   A Float specifying the angle in degrees to be revolved.

            sketchOrientation=`abaqusConstants.RIGHT`[¶](#abaqus.Part.PartFeature.PartFeature.ShellRevolve.sketchOrientation "Permalink to this definition")
            :   A SymbolicConstant specifying the orientation of **sketchUpEdge** on the sketch. Possible
                values are RIGHT, LEFT, TOP, and BOTTOM. The default value is RIGHT.

            pitch=`None`[¶](#abaqus.Part.PartFeature.PartFeature.ShellRevolve.pitch "Permalink to this definition")
            :   A Float specifying the pitch. The pitch is the distance traveled along the axial
                direction, measured between corresponding points on the sketch when it has completed one
                full revolution about the axis of revolution. Possible values are 0 ≤ **pitch** ≤ 10⁵.
                The default value, 0, implies a normal revolve.

            flipRevolveDirection=`0`[¶](#abaqus.Part.PartFeature.PartFeature.ShellRevolve.flipRevolveDirection "Permalink to this definition")
            :   A Boolean specifying whether to override the direction of feature creation. If
                **flipRevolveDirection** = OFF, the default direction of revolution is used. If
                **flipRevolveDirection** = ON, the revolve direction is reversed. The default value is OFF.

            flipPitchDirection=`0`[¶](#abaqus.Part.PartFeature.PartFeature.ShellRevolve.flipPitchDirection "Permalink to this definition")
            :   A Boolean specifying whether to override the direction of translation. If
                **flipPitchDirection** = OFF, the direction of translation is given by the direction of the
                revolve axis. If **flipPitchDirection** = ON, the translation direction is reversed. The
                default value is OFF.

            moveSketchNormalToPath=`0`[¶](#abaqus.Part.PartFeature.PartFeature.ShellRevolve.moveSketchNormalToPath "Permalink to this definition")
            :   A Boolean specifying whether to rotate the sketch so that it is normal to the path of
                revolution when using the **pitch** option. If **moveSketchNormalToPath** = OFF, the sketch
                plane remains parallel to the revolve axis. If **moveSketchNormalToPath** = ON, the sketch
                is moved to match the angle created by the **pitch** before being revolved. The default
                value is OFF.

            keepInternalBoundaries=`0`[¶](#abaqus.Part.PartFeature.PartFeature.ShellRevolve.keepInternalBoundaries "Permalink to this definition")
            :   A Boolean specifying whether internal boundaries will be retained. The default value is
                OFF.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.ShellRevolve-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.ShellRevolve-return-type "Permalink to this headline")
        :   `Feature`

    ShellSweep(*[path](#abaqus.Part.PartFeature.PartFeature.ShellSweep.path "abaqus.Part.PartFeature.PartFeature.ShellSweep.path (Python parameter) — Path may either be a ConstrainedSketch object or a sequence of Edge objects specifying the path of the sweep.")*, *[profile](#abaqus.Part.PartFeature.PartFeature.ShellSweep.profile "abaqus.Part.PartFeature.PartFeature.ShellSweep.profile (Python parameter) — Profile may either be a ConstrainedSketch object or a sequence of Edge objects specifying the section to be swept.")*, *[pathPlane](#abaqus.Part.PartFeature.PartFeature.ShellSweep.pathPlane "abaqus.Part.PartFeature.PartFeature.ShellSweep.pathPlane (Python parameter) — A Datum plane object or a planar Face object.")=`''`*, *[pathUpEdge](#abaqus.Part.PartFeature.PartFeature.ShellSweep.pathUpEdge "abaqus.Part.PartFeature.PartFeature.ShellSweep.pathUpEdge (Python parameter) — An Edge object or a Datum axis object specifying the vertical (Y) direction of the path sketch.")=`None`*, *[pathOrientation](#abaqus.Part.PartFeature.PartFeature.ShellSweep.pathOrientation "abaqus.Part.PartFeature.PartFeature.ShellSweep.pathOrientation (Python parameter) — A SymbolicConstant specifying the orientation of pathUpEdge on the sketch.")=`abaqusConstants.RIGHT`*, *[sketchPlane](#abaqus.Part.PartFeature.PartFeature.ShellSweep.sketchPlane "abaqus.Part.PartFeature.PartFeature.ShellSweep.sketchPlane (Python parameter) — A Datum plane object or a planar Face object specifying the plane on which to sketch the profile.")=`''`*, *[sketchUpEdge](#abaqus.Part.PartFeature.PartFeature.ShellSweep.sketchUpEdge "abaqus.Part.PartFeature.PartFeature.ShellSweep.sketchUpEdge (Python parameter) — An Edge object or a Datum axis object specifying the vertical (Y) direction of the profile sketch.")=`None`*, *[sketchOrientation](#abaqus.Part.PartFeature.PartFeature.ShellSweep.sketchOrientation "abaqus.Part.PartFeature.PartFeature.ShellSweep.sketchOrientation (Python parameter) — A SymbolicConstant specifying the orientation of sketchUpEdge on the sketch.")=`abaqusConstants.RIGHT`*, *[draftAngle](#abaqus.Part.PartFeature.PartFeature.ShellSweep.draftAngle "abaqus.Part.PartFeature.PartFeature.ShellSweep.draftAngle (Python parameter) — A Float specifying the draft angle in degrees.")=`None`*, *[pitch](#abaqus.Part.PartFeature.PartFeature.ShellSweep.pitch "abaqus.Part.PartFeature.PartFeature.ShellSweep.pitch (Python parameter) — A Float specifying the pitch.")=`None`*, *[profileNormal](#abaqus.Part.PartFeature.PartFeature.ShellSweep.profileNormal "abaqus.Part.PartFeature.PartFeature.ShellSweep.profileNormal (Python parameter) — A Boolean specifying whether to keep the profile normal same as original or varying through out the sweep path.")=`0`*, *[flipSweepDirection](#abaqus.Part.PartFeature.PartFeature.ShellSweep.flipSweepDirection "abaqus.Part.PartFeature.PartFeature.ShellSweep.flipSweepDirection (Python parameter) — A Boolean specifying whether to flip the direction in which sweep operation will be performed.")=`0`*, *[keepInternalBoundaries](#abaqus.Part.PartFeature.PartFeature.ShellSweep.keepInternalBoundaries "abaqus.Part.PartFeature.PartFeature.ShellSweep.keepInternalBoundaries (Python parameter) — A Boolean specifying whether internal boundaries will be retained.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L1960-L2052)[¶](#abaqus.Part.PartFeature.PartFeature.ShellSweep "Permalink to this definition")
    :   This method creates an additional Feature object by sweeping the given ConstrainedSketch object or a
        sequence of Edge objects along a path which may be a ConstrainedSketch or a sequence of Edge objects,
        creating a shell swept protrusion. The section can be an open or a closed profile. The section sketch
        can be created at the normal plane at the start of the sweep path or it may be created on a Datum plane
        or a planar Face. No checks are made for self-intersection.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [ShellSweep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-shellsweeppyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.ShellSweep-parameters "Permalink to this headline")
        :   path[¶](#abaqus.Part.PartFeature.PartFeature.ShellSweep.path "Permalink to this definition")
            :   Path may either be a ConstrainedSketch object or a sequence of Edge objects specifying
                the path of the sweep.

            profile[¶](#abaqus.Part.PartFeature.PartFeature.ShellSweep.profile "Permalink to this definition")
            :   Profile may either be a ConstrainedSketch object or a sequence of Edge objects
                specifying the section to be swept.

            pathPlane=`''`[¶](#abaqus.Part.PartFeature.PartFeature.ShellSweep.pathPlane "Permalink to this definition")
            :   A Datum plane object or a planar Face object. Only required when path is a
                ConstrainedSketch object.

            pathUpEdge=`None`[¶](#abaqus.Part.PartFeature.PartFeature.ShellSweep.pathUpEdge "Permalink to this definition")
            :   An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the
                path sketch. Only required when path is a ConstrainedSketch object.

            pathOrientation=`abaqusConstants.RIGHT`[¶](#abaqus.Part.PartFeature.PartFeature.ShellSweep.pathOrientation "Permalink to this definition")
            :   A SymbolicConstant specifying the orientation of **pathUpEdge** on the sketch. Possible
                values are RIGHT, LEFT, TOP, and BOTTOM. Default value is RIGHT. Only required when path
                is a ConstrainedSketch object.

            sketchPlane=`''`[¶](#abaqus.Part.PartFeature.PartFeature.ShellSweep.sketchPlane "Permalink to this definition")
            :   A Datum plane object or a planar Face object specifying the plane on which to sketch the
                profile. Not required when profile is a Face object. When profile is chosen as
                ConstrainedSketch object, user may or may not give this as input. If user does not give
                this as input, the normal plane at the start of the path will be the sketchPlane.

            sketchUpEdge=`None`[¶](#abaqus.Part.PartFeature.PartFeature.ShellSweep.sketchUpEdge "Permalink to this definition")
            :   An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the
                profile sketch. Only required when profile is a ConstrainedSketch object.

            sketchOrientation=`abaqusConstants.RIGHT`[¶](#abaqus.Part.PartFeature.PartFeature.ShellSweep.sketchOrientation "Permalink to this definition")
            :   A SymbolicConstant specifying the orientation of **sketchUpEdge** on the sketch. Possible
                values are RIGHT, LEFT, TOP, and BOTTOM. Default value is RIGHT. Only required when
                profile is a ConstrainedSketch object.

            draftAngle=`None`[¶](#abaqus.Part.PartFeature.PartFeature.ShellSweep.draftAngle "Permalink to this definition")
            :   A Float specifying the draft angle in degrees. Possible values are -90.0 ≤ **draftAngle**
                ≤ 90.0. By convention, for a positive draft angle an outer loop will draft outward and
                an inner loop will draft inward. The opposite is true for a negative draft angle. The
                default value, 0, implies a normal extrude. The arguments **draftAngle** and **pitch** are
                mutually exclusive.

            pitch=`None`[¶](#abaqus.Part.PartFeature.PartFeature.ShellSweep.pitch "Permalink to this definition")
            :   A Float specifying the pitch. The pitch is the distance traveled along the axial
                direction by the sketch when the sketch has completed one full revolution about the
                twist axis. Pitch can be specified as positive or negative to achieve right-handed or
                left-handed twist about the twist axis, respectively. The default value, 0, implies a
                normal extrude. Possible values are -10⁵ ≤ **pitch** ≤ 10⁵. The arguments **draftAngle**
                and **pitch** are mutually exclusive.

            profileNormal=`0`[¶](#abaqus.Part.PartFeature.PartFeature.ShellSweep.profileNormal "Permalink to this definition")
            :   A Boolean specifying whether to keep the profile normal same as original or varying
                through out the sweep path. When **profileNormal** = OFF, the profile normal will vary
                through out the sweep path. When **profileNormal** = ON, the profile normal will be same as
                original through out the sweep path. The default value is OFF.

            flipSweepDirection=`0`[¶](#abaqus.Part.PartFeature.PartFeature.ShellSweep.flipSweepDirection "Permalink to this definition")
            :   A Boolean specifying whether to flip the direction in which sweep operation will be
                performed. When **flipSweepDirection** = OFF, sweep operation will be performed in the
                direction of path direction. When **flipSweepDirection** = ON, sweep operation will be
                performed in the direction opposite to the path direction. The default value is OFF.

            keepInternalBoundaries=`0`[¶](#abaqus.Part.PartFeature.PartFeature.ShellSweep.keepInternalBoundaries "Permalink to this definition")
            :   A Boolean specifying whether internal boundaries will be retained. The default value is
                OFF.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.ShellSweep-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.ShellSweep-return-type "Permalink to this headline")
        :   `Feature`

    SolidExtrude(*[sketchPlane](#abaqus.Part.PartFeature.PartFeature.SolidExtrude.sketchPlane "abaqus.Part.PartFeature.PartFeature.SolidExtrude.sketchPlane (Python parameter) — A Datum plane object or a planar Face object.")*, *[sketchPlaneSide](#abaqus.Part.PartFeature.PartFeature.SolidExtrude.sketchPlaneSide "abaqus.Part.PartFeature.PartFeature.SolidExtrude.sketchPlaneSide (Python parameter) — A SymbolicConstant specifying the direction of feature creation.")*, *[sketchUpEdge](#abaqus.Part.PartFeature.PartFeature.SolidExtrude.sketchUpEdge "abaqus.Part.PartFeature.PartFeature.SolidExtrude.sketchUpEdge (Python parameter) — An Edge object or a Datum axis object specifying the vertical (Y) direction of the sketch.")*, *[sketch](#abaqus.Part.PartFeature.PartFeature.SolidExtrude.sketch "abaqus.Part.PartFeature.PartFeature.SolidExtrude.sketch (Python parameter) — A ConstrainedSketch object specifying the planar sketch to be extruded.")*, *[depth](#abaqus.Part.PartFeature.PartFeature.SolidExtrude.depth "abaqus.Part.PartFeature.PartFeature.SolidExtrude.depth (Python parameter) — A Float specifying the extrusion depth.")=`None`*, *[upToFace](#abaqus.Part.PartFeature.PartFeature.SolidExtrude.upToFace "abaqus.Part.PartFeature.PartFeature.SolidExtrude.upToFace (Python parameter) — A Face specifying the face up to which to extrude.")=`None`*, *[sketchOrientation](#abaqus.Part.PartFeature.PartFeature.SolidExtrude.sketchOrientation "abaqus.Part.PartFeature.PartFeature.SolidExtrude.sketchOrientation (Python parameter) — A SymbolicConstant specifying the orientation of sketchUpEdge on the sketch.")=`abaqusConstants.RIGHT`*, *[draftAngle](#abaqus.Part.PartFeature.PartFeature.SolidExtrude.draftAngle "abaqus.Part.PartFeature.PartFeature.SolidExtrude.draftAngle (Python parameter) — A Float specifying the draft angle in degrees.")=`None`*, *[pitch](#abaqus.Part.PartFeature.PartFeature.SolidExtrude.pitch "abaqus.Part.PartFeature.PartFeature.SolidExtrude.pitch (Python parameter) — A Float specifying the pitch.")=`None`*, *[flipExtrudeDirection](#abaqus.Part.PartFeature.PartFeature.SolidExtrude.flipExtrudeDirection "abaqus.Part.PartFeature.PartFeature.SolidExtrude.flipExtrudeDirection (Python parameter) — A Boolean specifying whether to override the direction of feature creation.")=`0`*, *[keepInternalBoundaries](#abaqus.Part.PartFeature.PartFeature.SolidExtrude.keepInternalBoundaries "abaqus.Part.PartFeature.PartFeature.SolidExtrude.keepInternalBoundaries (Python parameter) — A Boolean specifying whether internal boundaries will be retained.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L2054-L2128)[¶](#abaqus.Part.PartFeature.PartFeature.SolidExtrude "Permalink to this definition")
    :   This method creates an additional Feature object by extruding the given ConstrainedSketch object by
        the given depth, creating a solid protrusion. The ConstrainedSketch object must define a closed profile.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [SolidExtrude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-solidextrudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.SolidExtrude-parameters "Permalink to this headline")
        :   sketchPlane[¶](#abaqus.Part.PartFeature.PartFeature.SolidExtrude.sketchPlane "Permalink to this definition")
            :   A Datum plane object or a planar Face object.

            sketchPlaneSide[¶](#abaqus.Part.PartFeature.PartFeature.SolidExtrude.sketchPlaneSide "Permalink to this definition")
            :   A SymbolicConstant specifying the direction of feature creation. Possible values are
                SIDE1 and SIDE2.

            sketchUpEdge[¶](#abaqus.Part.PartFeature.PartFeature.SolidExtrude.sketchUpEdge "Permalink to this definition")
            :   An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the
                sketch.

            sketch[¶](#abaqus.Part.PartFeature.PartFeature.SolidExtrude.sketch "Permalink to this definition")
            :   A ConstrainedSketch object specifying the planar sketch to be extruded.

            depth=`None`[¶](#abaqus.Part.PartFeature.PartFeature.SolidExtrude.depth "Permalink to this definition")
            :   A Float specifying the extrusion depth. The default is to not specify a depth. Either
                **depth** or **upToFace** must be used to define the extrusion depth.

            upToFace=`None`[¶](#abaqus.Part.PartFeature.PartFeature.SolidExtrude.upToFace "Permalink to this definition")
            :   A Face specifying the face up to which to extrude. If **upToFace** is specified, the
                extrusion will be an up-to-face extrusion. The default is to not specify a face. Either
                **depth** or **upToFace** must be used to define the extrusion depth.

            sketchOrientation=`abaqusConstants.RIGHT`[¶](#abaqus.Part.PartFeature.PartFeature.SolidExtrude.sketchOrientation "Permalink to this definition")
            :   A SymbolicConstant specifying the orientation of **sketchUpEdge** on the sketch. Possible
                values are RIGHT, LEFT, TOP, and BOTTOM. The default value is RIGHT.

            draftAngle=`None`[¶](#abaqus.Part.PartFeature.PartFeature.SolidExtrude.draftAngle "Permalink to this definition")
            :   A Float specifying the draft angle in degrees. Possible values are -90.0 ≤ **draftAngle**
                ≤ 90.0. By convention, for a positive draft angle an outer loop will draft outward and
                an inner loop will draft inward. The opposite is true for a negative draft angle. The
                default value, 0, implies a normal extrude. The arguments **draftAngle** and **pitch** are
                mutually exclusive.

            pitch=`None`[¶](#abaqus.Part.PartFeature.PartFeature.SolidExtrude.pitch "Permalink to this definition")
            :   A Float specifying the pitch. The pitch is the distance traveled along the axial
                direction by the sketch when the sketch has completed one full revolution about the
                twist axis. Pitch can be specified as positive or negative to achieve right-handed or
                left-handed twist about the twist axis, respectively. The default value, 0, implies a
                normal extrude. Possible values are -10⁵ ≤ **pitch** ≤ 10⁵. The arguments **draftAngle**
                and **pitch** are mutually exclusive.

            flipExtrudeDirection=`0`[¶](#abaqus.Part.PartFeature.PartFeature.SolidExtrude.flipExtrudeDirection "Permalink to this definition")
            :   A Boolean specifying whether to override the direction of feature creation. If the value
                is OFF, it means use the direction defined by the **sketchPlaneSide**; if the value is ON,
                it means use the opposite direction to the one defined by **sketchPlaneSide**. The default
                value is OFF.

            keepInternalBoundaries=`0`[¶](#abaqus.Part.PartFeature.PartFeature.SolidExtrude.keepInternalBoundaries "Permalink to this definition")
            :   A Boolean specifying whether internal boundaries will be retained. The default value is
                OFF.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.SolidExtrude-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.SolidExtrude-return-type "Permalink to this headline")
        :   `Feature`

    SolidLoft(*[loftsections](#abaqus.Part.PartFeature.PartFeature.SolidLoft.loftsections "abaqus.Part.PartFeature.PartFeature.SolidLoft.loftsections (Python parameter) — A sequence of sequences of edges specifying the cross-sections to be lofted.")*, *[startCondition](#abaqus.Part.PartFeature.PartFeature.SolidLoft.startCondition "abaqus.Part.PartFeature.PartFeature.SolidLoft.startCondition (Python parameter) — A SymbolicConstant specifying the tangent direction at the start section of the loft feature.")=`None`*, *[endCondition](#abaqus.Part.PartFeature.PartFeature.SolidLoft.endCondition "abaqus.Part.PartFeature.PartFeature.SolidLoft.endCondition (Python parameter) — A SymbolicConstant specifying the tangent direction at the end section of the loft feature.")=`None`*, *[startTangent](#abaqus.Part.PartFeature.PartFeature.SolidLoft.startTangent "abaqus.Part.PartFeature.PartFeature.SolidLoft.startTangent (Python parameter) — A Float specifying the angle in degrees of the tangent with respect to the plane in which the start section lies.")=`None`*, *[startMagnitude](#abaqus.Part.PartFeature.PartFeature.SolidLoft.startMagnitude "abaqus.Part.PartFeature.PartFeature.SolidLoft.startMagnitude (Python parameter) — A Float specifying the magnitude of the startTangent.")=`None`*, *[endTangent](#abaqus.Part.PartFeature.PartFeature.SolidLoft.endTangent "abaqus.Part.PartFeature.PartFeature.SolidLoft.endTangent (Python parameter) — A Float specifying the angle in degrees of the tangent with respect to the plane in which the end section lies.")=`None`*, *[endMagnitude](#abaqus.Part.PartFeature.PartFeature.SolidLoft.endMagnitude "abaqus.Part.PartFeature.PartFeature.SolidLoft.endMagnitude (Python parameter) — A Float specifying the magnitude of the endTangent.")=`None`*, *[paths](#abaqus.Part.PartFeature.PartFeature.SolidLoft.paths "abaqus.Part.PartFeature.PartFeature.SolidLoft.paths (Python parameter) — A sequence of sequences of edges that pass through each section in the loft feature. Each sequence specifies a path followed by the face or an edge created by a loft feature.")=`()`*, *[globalSmoothing](#abaqus.Part.PartFeature.PartFeature.SolidLoft.globalSmoothing "abaqus.Part.PartFeature.PartFeature.SolidLoft.globalSmoothing (Python parameter) — A Boolean specifying whether each path defined in the paths argument is applied locally or globally.If the path is applied locally, its effect is felt only on faces created from the edges on the loftsections through which the paths pass through.If the path is applied globally, an averaging algorithm is applied over all the paths defined and is distributed over all the faces created.The default value is ON (globally).")=`0`*, *[keepInternalBoundaries](#abaqus.Part.PartFeature.PartFeature.SolidLoft.keepInternalBoundaries "abaqus.Part.PartFeature.PartFeature.SolidLoft.keepInternalBoundaries (Python parameter) — A Boolean specifying whether internal boundaries will be retained.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L2130-L2214)[¶](#abaqus.Part.PartFeature.PartFeature.SolidLoft "Permalink to this definition")
    :   This method creates an additional Feature object by lofting between the given sections and adding
        material to the part. You define the sections using a sequence of edges from the part or an EdgeArray.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [SolidLoft on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-solidloftpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.SolidLoft-parameters "Permalink to this headline")
        :   loftsections[¶](#abaqus.Part.PartFeature.PartFeature.SolidLoft.loftsections "Permalink to this definition")
            :   A sequence of sequences of edges specifying the cross-sections to be lofted. Each outer
                sequence specifies a section through which Abaqus will pass the loft feature. Each outer
                sequence can be defined as a sequence of edges or as an EdgeArray. The edges specifying
                a section must form a simple closed profile and must not contain multiple loops.

            startCondition=`None`[¶](#abaqus.Part.PartFeature.PartFeature.SolidLoft.startCondition "Permalink to this definition")
            :   A SymbolicConstant specifying the tangent direction at the start section of the loft
                feature. Possible values are NONE, NORMAL, RADIAL and SPECIFIED. You can specify this
                argument only if the start and end sections are planar. You cannot use this argument in
                conjunction with the **path** argument. You must use the **startCondition** argument in
                conjunction with the **endCondition** argument.

            endCondition=`None`[¶](#abaqus.Part.PartFeature.PartFeature.SolidLoft.endCondition "Permalink to this definition")
            :   A SymbolicConstant specifying the tangent direction at the end section of the loft
                feature. Possible values are NONE, NORMAL, RADIAL and SPECIFIED. You can specify this
                argument only if the start and end sections are planar. You cannot use this argument in
                conjunction with the **path** argument. You must use the **endCondition** argument in
                conjunction with the **startCondition** argument.

            startTangent=`None`[¶](#abaqus.Part.PartFeature.PartFeature.SolidLoft.startTangent "Permalink to this definition")
            :   A Float specifying the angle in degrees of the tangent with respect to the plane in
                which the start section lies. You must specify the **startTangent** argument if
                **startCondition** = SPECIFIED. Possible values are 0.0 ≤ **startTangent** ≤ 180.0.

            startMagnitude=`None`[¶](#abaqus.Part.PartFeature.PartFeature.SolidLoft.startMagnitude "Permalink to this definition")
            :   A Float specifying the magnitude of the **startTangent**. You must specify the
                **startMagnitude** argument if **startCondition** = SPECIFIED. Possible values are 0.0 <
                **startMagnitude** < 100.0.

            endTangent=`None`[¶](#abaqus.Part.PartFeature.PartFeature.SolidLoft.endTangent "Permalink to this definition")
            :   A Float specifying the angle in degrees of the tangent with respect to the plane in
                which the end section lies. You must specify the **endTangent** argument if
                **startCondition** = SPECIFIED. Possible values are 0.0 ≤ **endTangent** ≤ 180.0.

            endMagnitude=`None`[¶](#abaqus.Part.PartFeature.PartFeature.SolidLoft.endMagnitude "Permalink to this definition")
            :   A Float specifying the magnitude of the **endTangent**. This argument is to be used when
                the **endCondition** argument has the value SPECIFIED. Possible values are 0.0 <
                **endMagnitude** < 100.0.

            paths=`()`[¶](#abaqus.Part.PartFeature.PartFeature.SolidLoft.paths "Permalink to this definition")
            :   A sequence of sequences of edges that pass through each section in the loft feature.
                Each sequence specifies a path followed by the face or an edge created by a loft
                feature. Each path must start at the first section, end at the last section, and pass
                through each section. In addition, the order of the sequences must be the same as the
                order of the sections in the **loftsections** argument. Each path must not self-intersect
                and must be tangent continuous. In addition, the paths must not intersect each other.
                You cannot use the **paths** argument in conjunction with the **startCondition** and
                **endCondition** arguments.

            globalSmoothing=`0`[¶](#abaqus.Part.PartFeature.PartFeature.SolidLoft.globalSmoothing "Permalink to this definition")
            :   A Boolean specifying whether each path defined in the **paths** argument is applied
                locally or globally.If the path is applied locally, its effect is felt only on faces
                created from the edges on the **loftsections** through which the **paths** pass through.If
                the path is applied globally, an averaging algorithm is applied over all the paths
                defined and is distributed over all the faces created.The default value is ON
                (globally).

            keepInternalBoundaries=`0`[¶](#abaqus.Part.PartFeature.PartFeature.SolidLoft.keepInternalBoundaries "Permalink to this definition")
            :   A Boolean specifying whether internal boundaries will be retained. The default value is
                OFF.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.SolidLoft-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.SolidLoft-return-type "Permalink to this headline")
        :   `Feature`

    SolidRevolve(*[sketchPlane](#abaqus.Part.PartFeature.PartFeature.SolidRevolve.sketchPlane "abaqus.Part.PartFeature.PartFeature.SolidRevolve.sketchPlane (Python parameter) — A Datum plane object or a planar Face object.")*, *[sketchPlaneSide](#abaqus.Part.PartFeature.PartFeature.SolidRevolve.sketchPlaneSide "abaqus.Part.PartFeature.PartFeature.SolidRevolve.sketchPlaneSide (Python parameter) — A SymbolicConstant specifying the direction of feature creation.")*, *[sketchUpEdge](#abaqus.Part.PartFeature.PartFeature.SolidRevolve.sketchUpEdge "abaqus.Part.PartFeature.PartFeature.SolidRevolve.sketchUpEdge (Python parameter) — An Edge object or a Datum axis object specifying the vertical (Y) direction of the sketch.")*, *[sketch](#abaqus.Part.PartFeature.PartFeature.SolidRevolve.sketch "abaqus.Part.PartFeature.PartFeature.SolidRevolve.sketch (Python parameter) — A ConstrainedSketch object specifying the planar sketch to be revolved.")*, *[angle](#abaqus.Part.PartFeature.PartFeature.SolidRevolve.angle "abaqus.Part.PartFeature.PartFeature.SolidRevolve.angle (Python parameter) — A Float specifying the angle in degrees to be revolved.")*, *[sketchOrientation](#abaqus.Part.PartFeature.PartFeature.SolidRevolve.sketchOrientation "abaqus.Part.PartFeature.PartFeature.SolidRevolve.sketchOrientation (Python parameter) — A SymbolicConstant specifying the orientation of sketchUpEdge on the sketch.")=`abaqusConstants.RIGHT`*, *[pitch](#abaqus.Part.PartFeature.PartFeature.SolidRevolve.pitch "abaqus.Part.PartFeature.PartFeature.SolidRevolve.pitch (Python parameter) — A Float specifying the pitch.")=`None`*, *[flipRevolveDirection](#abaqus.Part.PartFeature.PartFeature.SolidRevolve.flipRevolveDirection "abaqus.Part.PartFeature.PartFeature.SolidRevolve.flipRevolveDirection (Python parameter) — A Boolean specifying whether to override the direction of feature creation.")=`0`*, *[flipPitchDirection](#abaqus.Part.PartFeature.PartFeature.SolidRevolve.flipPitchDirection "abaqus.Part.PartFeature.PartFeature.SolidRevolve.flipPitchDirection (Python parameter) — A Boolean specifying whether to override the direction of translation.")=`0`*, *[moveSketchNormalToPath](#abaqus.Part.PartFeature.PartFeature.SolidRevolve.moveSketchNormalToPath "abaqus.Part.PartFeature.PartFeature.SolidRevolve.moveSketchNormalToPath (Python parameter) — A Boolean specifying whether to rotate the sketch so that it is normal to the path of revolution when using the pitch option.")=`0`*, *[keepInternalBoundaries](#abaqus.Part.PartFeature.PartFeature.SolidRevolve.keepInternalBoundaries "abaqus.Part.PartFeature.PartFeature.SolidRevolve.keepInternalBoundaries (Python parameter) — A Boolean specifying whether internal boundaries will be retained.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L2216-L2288)[¶](#abaqus.Part.PartFeature.PartFeature.SolidRevolve "Permalink to this definition")
    :   This method creates an additional Feature object by revolving the given ConstrainedSketch object by
        the given angle, creating a solid protrusion. The ConstrainedSketch object must define a closed profile
        and an axis of revolution. The axis is defined by a single construction line.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [SolidRevolve on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-solidrevolvepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.SolidRevolve-parameters "Permalink to this headline")
        :   sketchPlane[¶](#abaqus.Part.PartFeature.PartFeature.SolidRevolve.sketchPlane "Permalink to this definition")
            :   A Datum plane object or a planar Face object.

            sketchPlaneSide[¶](#abaqus.Part.PartFeature.PartFeature.SolidRevolve.sketchPlaneSide "Permalink to this definition")
            :   A SymbolicConstant specifying the direction of feature creation. Possible values are
                SIDE1 and SIDE2.

            sketchUpEdge[¶](#abaqus.Part.PartFeature.PartFeature.SolidRevolve.sketchUpEdge "Permalink to this definition")
            :   An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the
                sketch.

            sketch[¶](#abaqus.Part.PartFeature.PartFeature.SolidRevolve.sketch "Permalink to this definition")
            :   A ConstrainedSketch object specifying the planar sketch to be revolved.

            angle[¶](#abaqus.Part.PartFeature.PartFeature.SolidRevolve.angle "Permalink to this definition")
            :   A Float specifying the angle in degrees to be revolved.

            sketchOrientation=`abaqusConstants.RIGHT`[¶](#abaqus.Part.PartFeature.PartFeature.SolidRevolve.sketchOrientation "Permalink to this definition")
            :   A SymbolicConstant specifying the orientation of **sketchUpEdge** on the sketch. Possible
                values are RIGHT, LEFT, TOP, and BOTTOM. The default value is RIGHT.

            pitch=`None`[¶](#abaqus.Part.PartFeature.PartFeature.SolidRevolve.pitch "Permalink to this definition")
            :   A Float specifying the pitch. The pitch is the distance traveled along the axial
                direction, measured between corresponding points on the sketch when it has completed one
                full revolution about the axis of revolution. Possible values are 0 ≤ **pitch** ≤ 10⁵.
                The default value, 0, implies a normal revolve.

            flipRevolveDirection=`0`[¶](#abaqus.Part.PartFeature.PartFeature.SolidRevolve.flipRevolveDirection "Permalink to this definition")
            :   A Boolean specifying whether to override the direction of feature creation. If
                **flipRevolveDirection** = OFF, the default direction of revolution is used. If
                **flipRevolveDirection** = ON, the revolve direction is reversed. The default value is OFF.

            flipPitchDirection=`0`[¶](#abaqus.Part.PartFeature.PartFeature.SolidRevolve.flipPitchDirection "Permalink to this definition")
            :   A Boolean specifying whether to override the direction of translation. If
                **flipPitchDirection** = OFF, the direction of translation is given by the direction of the
                revolve axis. If **flipPitchDirection** = ON, the translation direction is reversed. The
                default value is OFF.

            moveSketchNormalToPath=`0`[¶](#abaqus.Part.PartFeature.PartFeature.SolidRevolve.moveSketchNormalToPath "Permalink to this definition")
            :   A Boolean specifying whether to rotate the sketch so that it is normal to the path of
                revolution when using the **pitch** option. If **moveSketchNormalToPath** = OFF, the sketch
                plane remains parallel to the revolve axis. If **moveSketchNormalToPath** = ON, the sketch
                is moved to match the angle created by the **pitch** before being revolved. The default
                value is OFF.

            keepInternalBoundaries=`0`[¶](#abaqus.Part.PartFeature.PartFeature.SolidRevolve.keepInternalBoundaries "Permalink to this definition")
            :   A Boolean specifying whether internal boundaries will be retained. The default value is
                OFF.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.SolidRevolve-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.SolidRevolve-return-type "Permalink to this headline")
        :   `Feature`

    SolidSweep(*[path](#abaqus.Part.PartFeature.PartFeature.SolidSweep.path "abaqus.Part.PartFeature.PartFeature.SolidSweep.path (Python parameter) — Path may either be a ConstrainedSketch object or a sequence of Edge objects specifying the path of the sweep.")*, *[profile](#abaqus.Part.PartFeature.PartFeature.SolidSweep.profile "abaqus.Part.PartFeature.PartFeature.SolidSweep.profile (Python parameter) — Profile may either be a ConstrainedSketch object or a Face object specifying the section to be swept.")*, *[pathPlane](#abaqus.Part.PartFeature.PartFeature.SolidSweep.pathPlane "abaqus.Part.PartFeature.PartFeature.SolidSweep.pathPlane (Python parameter) — A Datum plane object or a planar Face object.")=`''`*, *[pathUpEdge](#abaqus.Part.PartFeature.PartFeature.SolidSweep.pathUpEdge "abaqus.Part.PartFeature.PartFeature.SolidSweep.pathUpEdge (Python parameter) — An Edge object or a Datum axis object specifying the vertical (Y) direction of the path sketch.")=`None`*, *[pathOrientation](#abaqus.Part.PartFeature.PartFeature.SolidSweep.pathOrientation "abaqus.Part.PartFeature.PartFeature.SolidSweep.pathOrientation (Python parameter) — A SymbolicConstant specifying the orientation of pathUpEdge on the sketch.")=`abaqusConstants.RIGHT`*, *[sketchPlane](#abaqus.Part.PartFeature.PartFeature.SolidSweep.sketchPlane "abaqus.Part.PartFeature.PartFeature.SolidSweep.sketchPlane (Python parameter) — A Datum plane object or a planar Face object specifying the plane on which to sketch the profile.")=`''`*, *[sketchUpEdge](#abaqus.Part.PartFeature.PartFeature.SolidSweep.sketchUpEdge "abaqus.Part.PartFeature.PartFeature.SolidSweep.sketchUpEdge (Python parameter) — An Edge object or a Datum axis object specifying the vertical (Y) direction of the profile sketch.")=`None`*, *[sketchOrientation](#abaqus.Part.PartFeature.PartFeature.SolidSweep.sketchOrientation "abaqus.Part.PartFeature.PartFeature.SolidSweep.sketchOrientation (Python parameter) — A SymbolicConstant specifying the orientation of sketchUpEdge on the sketch.")=`abaqusConstants.RIGHT`*, *[draftAngle](#abaqus.Part.PartFeature.PartFeature.SolidSweep.draftAngle "abaqus.Part.PartFeature.PartFeature.SolidSweep.draftAngle (Python parameter) — A Float specifying the draft angle in degrees.")=`None`*, *[pitch](#abaqus.Part.PartFeature.PartFeature.SolidSweep.pitch "abaqus.Part.PartFeature.PartFeature.SolidSweep.pitch (Python parameter) — A Float specifying the pitch.")=`None`*, *[profileNormal](#abaqus.Part.PartFeature.PartFeature.SolidSweep.profileNormal "abaqus.Part.PartFeature.PartFeature.SolidSweep.profileNormal (Python parameter) — A Boolean specifying whether to keep the profile normal same as original or varying through out the sweep path.")=`0`*, *[flipSweepDirection](#abaqus.Part.PartFeature.PartFeature.SolidSweep.flipSweepDirection "abaqus.Part.PartFeature.PartFeature.SolidSweep.flipSweepDirection (Python parameter) — A Boolean specifying whether to flip the direction in which sweep operation will be performed.")=`0`*, *[keepInternalBoundaries](#abaqus.Part.PartFeature.PartFeature.SolidSweep.keepInternalBoundaries "abaqus.Part.PartFeature.PartFeature.SolidSweep.keepInternalBoundaries (Python parameter) — A Boolean specifying whether internal boundaries will be retained.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L2290-L2382)[¶](#abaqus.Part.PartFeature.PartFeature.SolidSweep "Permalink to this definition")
    :   This method creates an additional Feature object by sweeping the given ConstrainedSketch object or a
        Face object along a path which may be a ConstrainedSketch or a sequence of Edge objects, creating a
        solid swept protrusion. If the profile section is a ConstrainedSketch object, it must define a closed
        profile. The section sketch can be created at the normal plane at the start of the sweep path or it may
        be created on a Datum plane or a planar Face. No checks are made for self-intersection.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [SolidSweep on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-solidsweeppyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.SolidSweep-parameters "Permalink to this headline")
        :   path[¶](#abaqus.Part.PartFeature.PartFeature.SolidSweep.path "Permalink to this definition")
            :   Path may either be a ConstrainedSketch object or a sequence of Edge objects specifying
                the path of the sweep.

            profile[¶](#abaqus.Part.PartFeature.PartFeature.SolidSweep.profile "Permalink to this definition")
            :   Profile may either be a ConstrainedSketch object or a Face object specifying the section
                to be swept.

            pathPlane=`''`[¶](#abaqus.Part.PartFeature.PartFeature.SolidSweep.pathPlane "Permalink to this definition")
            :   A Datum plane object or a planar Face object. Only required when path is a
                ConstrainedSketch object.

            pathUpEdge=`None`[¶](#abaqus.Part.PartFeature.PartFeature.SolidSweep.pathUpEdge "Permalink to this definition")
            :   An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the
                path sketch. Only required when path is a ConstrainedSketch object.

            pathOrientation=`abaqusConstants.RIGHT`[¶](#abaqus.Part.PartFeature.PartFeature.SolidSweep.pathOrientation "Permalink to this definition")
            :   A SymbolicConstant specifying the orientation of **pathUpEdge** on the sketch. Possible
                values are RIGHT, LEFT, TOP, and BOTTOM. Default value is RIGHT. Only required when path
                is a ConstrainedSketch object.

            sketchPlane=`''`[¶](#abaqus.Part.PartFeature.PartFeature.SolidSweep.sketchPlane "Permalink to this definition")
            :   A Datum plane object or a planar Face object specifying the plane on which to sketch the
                profile. Not required when profile is a Face object. When profile is chosen as
                ConstrainedSketch object, user may or may not give this as input. If user does not give
                this as input, the normal plane at the start of the path will be the sketchPlane.

            sketchUpEdge=`None`[¶](#abaqus.Part.PartFeature.PartFeature.SolidSweep.sketchUpEdge "Permalink to this definition")
            :   An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the
                profile sketch. Only required when profile is a ConstrainedSketch object.

            sketchOrientation=`abaqusConstants.RIGHT`[¶](#abaqus.Part.PartFeature.PartFeature.SolidSweep.sketchOrientation "Permalink to this definition")
            :   A SymbolicConstant specifying the orientation of **sketchUpEdge** on the sketch. Possible
                values are RIGHT, LEFT, TOP, and BOTTOM. Default value is RIGHT. Only required when
                profile is a ConstrainedSketch object.

            draftAngle=`None`[¶](#abaqus.Part.PartFeature.PartFeature.SolidSweep.draftAngle "Permalink to this definition")
            :   A Float specifying the draft angle in degrees. Possible values are -90.0 ≤ **draftAngle**
                ≤ 90.0. By convention, for a positive draft angle an outer loop will draft outward and
                an inner loop will draft inward. The opposite is true for a negative draft angle. The
                default value, 0, implies a normal extrude. The arguments **draftAngle** and **pitch** are
                mutually exclusive.

            pitch=`None`[¶](#abaqus.Part.PartFeature.PartFeature.SolidSweep.pitch "Permalink to this definition")
            :   A Float specifying the pitch. The pitch is the distance traveled along the axial
                direction by the sketch when the sketch has completed one full revolution about the
                twist axis. Pitch can be specified as positive or negative to achieve right-handed or
                left-handed twist about the twist axis, respectively. The default value, 0, implies a
                normal extrude. Possible values are -10⁵ ≤ **pitch** ≤ 10⁵. The arguments **draftAngle**
                and **pitch** are mutually exclusive.

            profileNormal=`0`[¶](#abaqus.Part.PartFeature.PartFeature.SolidSweep.profileNormal "Permalink to this definition")
            :   A Boolean specifying whether to keep the profile normal same as original or varying
                through out the sweep path. When **profileNormal** = OFF, the profile normal will vary
                through out the sweep path. When **profileNormal** = ON, the profile normal will be same as
                original through out the sweep path. The default value is OFF.

            flipSweepDirection=`0`[¶](#abaqus.Part.PartFeature.PartFeature.SolidSweep.flipSweepDirection "Permalink to this definition")
            :   A Boolean specifying whether to flip the direction in which sweep operation will be
                performed. When **flipSweepDirection** = OFF, sweep operation will be performed in the
                direction of path direction. When **flipSweepDirection** = ON, sweep operation will be
                performed in the direction opposite to the path direction. The default value is OFF.

            keepInternalBoundaries=`0`[¶](#abaqus.Part.PartFeature.PartFeature.SolidSweep.keepInternalBoundaries "Permalink to this definition")
            :   A Boolean specifying whether internal boundaries will be retained. The default value is
                OFF.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.SolidSweep-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.SolidSweep-return-type "Permalink to this headline")
        :   `Feature`

    Stitch(*[edgeList](#abaqus.Part.PartFeature.PartFeature.Stitch.edgeList "abaqus.Part.PartFeature.PartFeature.Stitch.edgeList (Python parameter) — A sequence of Edge objects specifying the edges that need to be stitched.")=`()`*, *[stitchTolerance](#abaqus.Part.PartFeature.PartFeature.Stitch.stitchTolerance "abaqus.Part.PartFeature.PartFeature.Stitch.stitchTolerance (Python parameter) — A Float indicating the maximum gap to be stitched.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L2384-L2412)[¶](#abaqus.Part.PartFeature.PartFeature.Stitch "Permalink to this definition")
    :   This method attempts to create a valid part by binding together free and imprecise edges of all the
        faces of a part. If **edgeList** is not given, a global stitch will be performed. If **stitchTolerance**
        is not specified, a value of 1.0 will be used.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [Stitch on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-stitchpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.Stitch-parameters "Permalink to this headline")
        :   edgeList=`()`[¶](#abaqus.Part.PartFeature.PartFeature.Stitch.edgeList "Permalink to this definition")
            :   A sequence of Edge objects specifying the edges that need to be stitched.

            stitchTolerance=`None`[¶](#abaqus.Part.PartFeature.PartFeature.Stitch.stitchTolerance "Permalink to this definition")
            :   A Float indicating the maximum gap to be stitched. The value should be smaller than the
                minimum feature size and bigger than the maximum gap expected to be stitched in the
                model. Otherwise this command may remove small (sliver) edges that are smaller than the
                tolerance.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.Stitch-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.Stitch-return-type "Permalink to this headline")
        :   `Feature`

    Wire(*[sketchPlane](#abaqus.Part.PartFeature.PartFeature.Wire.sketchPlane "abaqus.Part.PartFeature.PartFeature.Wire.sketchPlane (Python parameter) — A Datum plane object or a planar Face object specifying the plane on which to sketch.")*, *[sketchPlaneSide](#abaqus.Part.PartFeature.PartFeature.Wire.sketchPlaneSide "abaqus.Part.PartFeature.PartFeature.Wire.sketchPlaneSide (Python parameter) — A SymbolicConstant specifying the direction of feature creation.")*, *[sketchUpEdge](#abaqus.Part.PartFeature.PartFeature.Wire.sketchUpEdge "abaqus.Part.PartFeature.PartFeature.Wire.sketchUpEdge (Python parameter) — An Edge object or a Datum axis object specifying the vertical (Y) direction of the sketch.")*, *[sketch](#abaqus.Part.PartFeature.PartFeature.Wire.sketch "abaqus.Part.PartFeature.PartFeature.Wire.sketch (Python parameter) — A ConstrainedSketch object specifying the planar sketch to be revolved.")*, *[sketchOrientation](#abaqus.Part.PartFeature.PartFeature.Wire.sketchOrientation "abaqus.Part.PartFeature.PartFeature.Wire.sketchOrientation (Python parameter) — A SymbolicConstant specifying the orientation of sketchUpEdge on the sketch.")=`abaqusConstants.RIGHT`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L2414-L2454)[¶](#abaqus.Part.PartFeature.PartFeature.Wire "Permalink to this definition")
    :   This method creates an additional Feature object by creating a planar wire from the given
        ConstrainedSketch object. The ConstrainedSketch object must define a closed profile.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [Wire on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-wirepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.Wire-parameters "Permalink to this headline")
        :   sketchPlane[¶](#abaqus.Part.PartFeature.PartFeature.Wire.sketchPlane "Permalink to this definition")
            :   A Datum plane object or a planar Face object specifying the plane on which to sketch.

            sketchPlaneSide[¶](#abaqus.Part.PartFeature.PartFeature.Wire.sketchPlaneSide "Permalink to this definition")
            :   A SymbolicConstant specifying the direction of feature creation. Possible values are
                SIDE1 and SIDE2.

            sketchUpEdge[¶](#abaqus.Part.PartFeature.PartFeature.Wire.sketchUpEdge "Permalink to this definition")
            :   An Edge object or a Datum axis object specifying the vertical (*Y*) direction of the
                sketch.

            sketch[¶](#abaqus.Part.PartFeature.PartFeature.Wire.sketch "Permalink to this definition")
            :   A ConstrainedSketch object specifying the planar sketch to be revolved.

            sketchOrientation=`abaqusConstants.RIGHT`[¶](#abaqus.Part.PartFeature.PartFeature.Wire.sketchOrientation "Permalink to this definition")
            :   A SymbolicConstant specifying the orientation of **sketchUpEdge** on the sketch. Possible
                values are RIGHT, LEFT, TOP, and BOTTOM. The default value is RIGHT.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.Wire-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.Wire-return-type "Permalink to this headline")
        :   `Feature`

    WireFromEdge(*[edgeList](#abaqus.Part.PartFeature.PartFeature.WireFromEdge.edgeList "abaqus.Part.PartFeature.PartFeature.WireFromEdge.edgeList (Python parameter) — A list of Edge objects specifying the edges from which the wire is to be created.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L2542-L2564)[¶](#abaqus.Part.PartFeature.PartFeature.WireFromEdge "Permalink to this definition")
    :   This method creates an additional Feature object by creating a Wire by selecting one or more Edge
        objects of a Solid or Shell part.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [WireFromEdge on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-wirefromedgepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.WireFromEdge-parameters "Permalink to this headline")
        :   edgeList[¶](#abaqus.Part.PartFeature.PartFeature.WireFromEdge.edgeList "Permalink to this definition")
            :   A list of Edge objects specifying the edges from which the wire is to be created.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.WireFromEdge-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.WireFromEdge-return-type "Permalink to this headline")
        :   `Feature`

    WirePolyLine(*[points](#abaqus.Part.PartFeature.PartFeature.WirePolyLine.points "abaqus.Part.PartFeature.PartFeature.WirePolyLine.points (Python parameter) — A sequence of ConstrainedSketchVertex, Datum point, or InterestingPoint objects specifying the points through which the polyline wire will pass.")*, *[mergeType](#abaqus.Part.PartFeature.PartFeature.WirePolyLine.mergeType "abaqus.Part.PartFeature.PartFeature.WirePolyLine.mergeType (Python parameter) — A SymbolicConstant specifying the merge behavior of the wire with existing geometry.")=`abaqusConstants.IMPRINT`*, *[meshable](#abaqus.Part.PartFeature.PartFeature.WirePolyLine.meshable "abaqus.Part.PartFeature.PartFeature.WirePolyLine.meshable (Python parameter) — A Boolean specifying whether the wire should be available for selection in meshing operations.")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L2500-L2540)[¶](#abaqus.Part.PartFeature.PartFeature.WirePolyLine "Permalink to this definition")
    :   This method creates an additional Feature object by creating a polyline wire that passes through a
        sequence of given points. Each point can be a datum point, a vertex, an interesting point, or a tuple.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [WirePolyLine on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-wirepolylinepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.WirePolyLine-parameters "Permalink to this headline")
        :   points[¶](#abaqus.Part.PartFeature.PartFeature.WirePolyLine.points "Permalink to this definition")
            :   A sequence of ConstrainedSketchVertex, Datum point, or InterestingPoint objects specifying the points
                through which the polyline wire will pass. **points** can also be a sequence of tuples of
                Floats. You must specify at least two values in the sequence.

            mergeType=`abaqusConstants.IMPRINT`[¶](#abaqus.Part.PartFeature.PartFeature.WirePolyLine.mergeType "Permalink to this definition")
            :   A SymbolicConstant specifying the merge behavior of the wire with existing geometry. If
                **mergeType** is MERGE, Abaqus merges the wire into solid regions of the part if the wire
                passes through them. If **mergeType** is IMPRINT, Abaqus imprints the wire on existing
                geometry as edges. If **mergeType** is SEPARATE, Abaqus neither merges nor imprints the
                spline wire with existing geometry. It creates the wire separately. The default value is
                IMPRINT.

            meshable=`1`[¶](#abaqus.Part.PartFeature.PartFeature.WirePolyLine.meshable "Permalink to this definition")
            :   A Boolean specifying whether the wire should be available for selection in meshing
                operations. If **meshable** = OFF, the wire can be used for connector section assignment.
                The default value is ON.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.WirePolyLine-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.WirePolyLine-return-type "Permalink to this headline")
        :   `Feature`

    WireSpline(*[points](#abaqus.Part.PartFeature.PartFeature.WireSpline.points "abaqus.Part.PartFeature.PartFeature.WireSpline.points (Python parameter) — A sequence of ConstrainedSketchVertex, Datum point, or InterestingPoint objects specifying the points through which the spline wire will pass.")*, *[mergeType](#abaqus.Part.PartFeature.PartFeature.WireSpline.mergeType "abaqus.Part.PartFeature.PartFeature.WireSpline.mergeType (Python parameter) — A SymbolicConstant specifying the merge behavior of the wire with existing geometry.")=`abaqusConstants.IMPRINT`*, *[smoothClosedSpline](#abaqus.Part.PartFeature.PartFeature.WireSpline.smoothClosedSpline "abaqus.Part.PartFeature.PartFeature.WireSpline.smoothClosedSpline (Python parameter) — A Boolean specifying the behavior of Abaqus when the points defining a spline wire form a closed loop (the start and end points are the same).")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Part/PartFeature.py#L2456-L2498)[¶](#abaqus.Part.PartFeature.PartFeature.WireSpline "Permalink to this definition")
    :   This method creates an additional Feature object by creating a spline wire that passes through a
        sequence of given points. Each point can be a datum point, a vertex, an interesting point, or a tuple.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].AutoRepair
        ```

        Note

        Check [WireSpline on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-wiresplinepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Part.PartFeature.PartFeature.WireSpline-parameters "Permalink to this headline")
        :   points[¶](#abaqus.Part.PartFeature.PartFeature.WireSpline.points "Permalink to this definition")
            :   A sequence of ConstrainedSketchVertex, Datum point, or InterestingPoint objects specifying the points
                through which the spline wire will pass. **points** can also be a sequence of tuples of
                Floats. You must specify at least two values in the sequence.

            mergeType=`abaqusConstants.IMPRINT`[¶](#abaqus.Part.PartFeature.PartFeature.WireSpline.mergeType "Permalink to this definition")
            :   A SymbolicConstant specifying the merge behavior of the wire with existing geometry. If
                **mergeType** is MERGE, Abaqus merges the wire into solid regions of the part if the wire
                passes through them. If **mergeType** is IMPRINT, Abaqus imprints the spline wire on
                existing geometry as edges. If **mergeType** is SEPARATE, Abaqus neither merges nor
                imprints the spline wire with existing geometry. It creates the wire separately. The
                default value is IMPRINT.

            smoothClosedSpline=`0`[¶](#abaqus.Part.PartFeature.PartFeature.WireSpline.smoothClosedSpline "Permalink to this definition")
            :   A Boolean specifying the behavior of Abaqus when the points defining a spline wire form
                a closed loop (the start and end points are the same). If **smoothClosedSpline** = ON,
                Abaqus creates a smooth spline wire where the tangencies at the end point meet smoothly.
                If **smoothClosedSpline** = OFF, Abaqus does not automatically create a smooth end
                condition. The default value in OFF.

        Returns:[¶](#abaqus.Part.PartFeature.PartFeature.WireSpline-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Part.PartFeature.PartFeature.WireSpline-return-type "Permalink to this headline")
        :   `Feature`

[Back to top](#)