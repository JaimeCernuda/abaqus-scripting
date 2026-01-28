# Abaqus ASSEMBLY Module API Reference

> Source: [https://hailin.wang/abqpy/en/2025/reference/mdb/model/part_assembly/assembly.html](https://hailin.wang/abqpy/en/2025/reference/mdb/model/part_assembly/assembly.html)
> Downloaded for offline use by Claude Code skills.

---

# Assembly[¶](#assembly "Permalink to this heading")

Features in Abaqus/CAE include Parts, Datums, Partitions, and Assembly operations. Assembly commands create Feature objects on only the rootAssembly object. The commands that create Feature objects on only the Part object are described in Part commands. The commands that create Feature objects on both the Part and the rootAssembly objects are described in Feature commands.

## Create instances[¶](#create-instances "Permalink to this heading")

*class* AssemblyModel(*[name](#abaqus.Assembly.AssemblyModel.AssemblyModel "abaqus.Assembly.AssemblyModel.AssemblyModel.__init__.name (Python parameter)")*, *[description](#abaqus.Assembly.AssemblyModel.AssemblyModel "abaqus.Assembly.AssemblyModel.AssemblyModel.__init__.description (Python parameter)")=`''`*, *[stefanBoltzmann](#abaqus.Assembly.AssemblyModel.AssemblyModel "abaqus.Assembly.AssemblyModel.AssemblyModel.__init__.stefanBoltzmann (Python parameter)")=`None`*, *[absoluteZero](#abaqus.Assembly.AssemblyModel.AssemblyModel "abaqus.Assembly.AssemblyModel.AssemblyModel.__init__.absoluteZero (Python parameter)")=`None`*, *[waveFormulation](#abaqus.Assembly.AssemblyModel.AssemblyModel "abaqus.Assembly.AssemblyModel.AssemblyModel.__init__.waveFormulation (Python parameter)")=`abaqusConstants.NOT_SET`*, *[modelType](#abaqus.Assembly.AssemblyModel.AssemblyModel "abaqus.Assembly.AssemblyModel.AssemblyModel.__init__.modelType (Python parameter)")=`abaqusConstants.STANDARD_EXPLICIT`*, *[universalGas](#abaqus.Assembly.AssemblyModel.AssemblyModel "abaqus.Assembly.AssemblyModel.AssemblyModel.__init__.universalGas (Python parameter)")=`None`*, *[copyConstraints](#abaqus.Assembly.AssemblyModel.AssemblyModel "abaqus.Assembly.AssemblyModel.AssemblyModel.__init__.copyConstraints (Python parameter)")=`1`*, *[copyConnectors](#abaqus.Assembly.AssemblyModel.AssemblyModel "abaqus.Assembly.AssemblyModel.AssemblyModel.__init__.copyConnectors (Python parameter)")=`1`*, *[copyInteractions](#abaqus.Assembly.AssemblyModel.AssemblyModel "abaqus.Assembly.AssemblyModel.AssemblyModel.__init__.copyInteractions (Python parameter)")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyModel.py#L10-L85)[¶](#abaqus.Assembly.AssemblyModel.AssemblyModel "Permalink to this definition")
:   Bases: [`ModelBase`](../index.html#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase (Python class) — Bases: object")

    Abaqus creates a Model object named Model-1 when a session is started.

    Note

    This object can be accessed by:

    ```python
    mdb.models[name]
    ```

    Note

    Check [AssemblyModel on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelasmpyc.htm?contextscope=all).

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
    | [`Instance`](#abaqus.Assembly.AssemblyModel.AssemblyModel.Instance "abaqus.Assembly.AssemblyModel.AssemblyModel.Instance (Python method) — This method copies a PartInstance object from the specified model and creates a new PartInstance object.")(name, objectToCopy) | This method copies a PartInstance object from the specified model and creates a new PartInstance object. |
    | [`convertAllSketches`](#abaqus.Assembly.AssemblyModel.AssemblyModel.convertAllSketches "abaqus.Assembly.AssemblyModel.AssemblyModel.convertAllSketches (Python method) — This method converts all sketches from Abaqus 6.5 or earlier to the equivalent ConstrainedSketch objects.")([regenerate, ...]) | This method converts all sketches from Abaqus 6.5 or earlier to the equivalent ConstrainedSketch objects. |
    | [`linkInstances`](#abaqus.Assembly.AssemblyModel.AssemblyModel.linkInstances "abaqus.Assembly.AssemblyModel.AssemblyModel.linkInstances (Python method) — This method links the selected PartInstance objects to the corresponding PartInstance objects from the specified models. If all instances of a Part are selected for linking, the Part will be linked as well. If not, a new linked child Part object will be created and added to the repository.")(instancesMap) | This method links the selected PartInstance objects to the corresponding PartInstance objects from the specified models. |

    Inherited from [`ModelBase`](../index.html#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | `__init__`(name[, description, ...]) | This method creates a Model object. |
    | [`setValues`](../index.html#abaqus.Model.ModelBase.ModelBase.setValues "abaqus.Model.ModelBase.ModelBase.setValues (Python method) — This method modifies the Model object.")([description, noPartsInputFile, ...]) | This method modifies the Model object. |

    ---

    Member Details:

    Instance(*[name](#abaqus.Assembly.AssemblyModel.AssemblyModel.Instance.name "abaqus.Assembly.AssemblyModel.AssemblyModel.Instance.name (Python parameter) — A String specifying the repository key.")*, *[objectToCopy](#abaqus.Assembly.AssemblyModel.AssemblyModel.Instance.objectToCopy "abaqus.Assembly.AssemblyModel.AssemblyModel.Instance.objectToCopy (Python parameter) — A PartInstance object to be copied.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyModel.py#L20-L42)[¶](#abaqus.Assembly.AssemblyModel.AssemblyModel.Instance "Permalink to this definition")
    :   This method copies a PartInstance object from the specified model and creates a new PartInstance
        object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].Instance
        ```

        Note

        Check [Instance on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-instanceasmpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Assembly.AssemblyModel.AssemblyModel.Instance-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Assembly.AssemblyModel.AssemblyModel.Instance.name "Permalink to this definition")
            :   A String specifying the repository key.

            objectToCopy[¶](#abaqus.Assembly.AssemblyModel.AssemblyModel.Instance.objectToCopy "Permalink to this definition")
            :   A PartInstance object to be copied.

        Returns:[¶](#abaqus.Assembly.AssemblyModel.AssemblyModel.Instance-returns "Permalink to this headline")
        :   A Model object.

        Return type:[¶](#abaqus.Assembly.AssemblyModel.AssemblyModel.Instance-return-type "Permalink to this headline")
        :   `Model`

    convertAllSketches(*[regenerate](#abaqus.Assembly.AssemblyModel.AssemblyModel.convertAllSketches.regenerate "abaqus.Assembly.AssemblyModel.AssemblyModel.convertAllSketches.regenerate (Python parameter) — A Boolean specifying if all the features in assembly as well as in all the parts in the model should be regenerated after the conversion.")=`True`*, *[convertReversedSketches](#abaqus.Assembly.AssemblyModel.AssemblyModel.convertAllSketches.convertReversedSketches "abaqus.Assembly.AssemblyModel.AssemblyModel.convertAllSketches.convertReversedSketches (Python parameter) — A Boolean specifying whether sketches in analytic rigid parts should be converted even if they cause the orientation of surfaces defined on them to be flipped.")=`True`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyModel.py#L44-L65)[¶](#abaqus.Assembly.AssemblyModel.AssemblyModel.convertAllSketches "Permalink to this definition")
    :   This method converts all sketches from Abaqus 6.5 or earlier to the equivalent ConstrainedSketch
        objects.

        Note

        Check [AssemblyModel.convertAllSketches on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelasmpyc.htm?contextscope=all#simaker-modelconvertallsketchespyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyModel.AssemblyModel.convertAllSketches-parameters "Permalink to this headline")
        :   regenerate=`True`[¶](#abaqus.Assembly.AssemblyModel.AssemblyModel.convertAllSketches.regenerate "Permalink to this definition")
            :   A Boolean specifying if all the features in assembly as well as in all the parts in the
                model should be regenerated after the conversion. The default value is True.

            convertReversedSketches=`True`[¶](#abaqus.Assembly.AssemblyModel.AssemblyModel.convertAllSketches.convertReversedSketches "Permalink to this definition")
            :   A Boolean specifying whether sketches in analytic rigid parts should be converted even
                if they cause the orientation of surfaces defined on them to be flipped. The default
                value is True.

        Returns:[¶](#abaqus.Assembly.AssemblyModel.AssemblyModel.convertAllSketches-returns "Permalink to this headline")
        :   A list of strings describing any warnings or errors encountered during the conversion
            process.

        Return type:[¶](#abaqus.Assembly.AssemblyModel.AssemblyModel.convertAllSketches-return-type "Permalink to this headline")
        :   `list[str]`

    linkInstances(*[instancesMap](#abaqus.Assembly.AssemblyModel.AssemblyModel.linkInstances.instancesMap "abaqus.Assembly.AssemblyModel.AssemblyModel.linkInstances.instancesMap (Python parameter) — A tuple of tuples containing the instance name to be linked and the corresponding PartInstance object to which it will be linked.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyModel.py#L67-L85)[¶](#abaqus.Assembly.AssemblyModel.AssemblyModel.linkInstances "Permalink to this definition")
    :   This method links the selected PartInstance objects to the corresponding PartInstance objects from
        the specified models. If all instances of a Part are selected for linking, the Part will be linked as
        well. If not, a new linked child Part object will be created and added to the repository.

        Note

        Check [AssemblyModel.linkInstances on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelasmpyc.htm?contextscope=all#simaker-modellinkinstancespyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyModel.AssemblyModel.linkInstances-parameters "Permalink to this headline")
        :   instancesMap[¶](#abaqus.Assembly.AssemblyModel.AssemblyModel.linkInstances.instancesMap "Permalink to this definition")
            :   A tuple of tuples containing the instance name to be linked and the corresponding
                PartInstance object to which it will be linked.

        Returns:[¶](#abaqus.Assembly.AssemblyModel.AssemblyModel.linkInstances-returns "Permalink to this headline")
        :   A list of strings describing any warnings or errors encountered during the conversion
            process.

        Return type:[¶](#abaqus.Assembly.AssemblyModel.AssemblyModel.linkInstances-return-type "Permalink to this headline")
        :   `list[str]`

## Other Classes[¶](#other-classes "Permalink to this heading")

*class* Assembly[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/Assembly.py#L19-L86)[¶](#abaqus.Assembly.Assembly.Assembly "Permalink to this definition")
:   Bases: [`MeshEditAssembly`](../../edit_mesh.html#abaqus.EditMesh.MeshEditAssembly.MeshEditAssembly "abaqus.EditMesh.MeshEditAssembly.MeshEditAssembly (Python class) — Bases: AssemblyBase"), [`MeshAssembly`](../mesh.html#abaqus.Mesh.MeshAssembly.MeshAssembly "abaqus.Mesh.MeshAssembly.MeshAssembly (Python class) — Bases: AssemblyBase"), [`PropertyAssembly`](../property.html#abaqus.Property.PropertyAssembly.PropertyAssembly "abaqus.Property.PropertyAssembly.PropertyAssembly (Python class) — Bases: AssemblyBase"), [`RegionAssembly`](region.html#abaqus.Region.RegionAssembly.RegionAssembly "abaqus.Region.RegionAssembly.RegionAssembly (Python class) — Bases: RegionAssemblyBase"), [`Displayable`](../../../session/canvas.html#abaqus.Canvas.ViewportBase.Displayable "abaqus.Canvas.Displayable.Displayable (Python class)")

    An Assembly object is a container for instances of parts. The Assembly object has no constructor command.
    Abaqus creates the **rootAssembly** member when a Model object is created.

    Note

    This object can be accessed by:

    ```python
    import assembly
    mdb.models[name].rootAssembly
    ```

    Note

    Check [Assembly on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all).

    Member Details:

    ConnectorOrientation(*[region](#abaqus.Assembly.Assembly.Assembly.ConnectorOrientation.region "abaqus.Assembly.Assembly.Assembly.ConnectorOrientation.region (Python parameter) — A Set object specifying the region to which the orientation is assigned.")*, *[localCsys1](#abaqus.Assembly.Assembly.Assembly.ConnectorOrientation.localCsys1 "abaqus.Assembly.Assembly.Assembly.ConnectorOrientation.localCsys1 (Python parameter) — A DatumCsys object specifying the local coordinate system of the first connector point. This value may be None, indicating the global coordinate system.")=`None`*, *[axis1](#abaqus.Assembly.Assembly.Assembly.ConnectorOrientation.axis1 "abaqus.Assembly.Assembly.Assembly.ConnectorOrientation.axis1 (Python parameter) — A SymbolicConstant specifying the axis of a datum coordinate system about which an additional rotation is applied.")=`abaqusConstants.AXIS_1`*, *[angle1](#abaqus.Assembly.Assembly.Assembly.ConnectorOrientation.angle1 "abaqus.Assembly.Assembly.Assembly.ConnectorOrientation.angle1 (Python parameter) — A Float specifying the angle of the additional rotation.")=`0`*, *[orient2sameAs1](#abaqus.Assembly.Assembly.Assembly.ConnectorOrientation.orient2sameAs1 "abaqus.Assembly.Assembly.Assembly.ConnectorOrientation.orient2sameAs1 (Python parameter) — A Boolean specifying whether or not the second connector point is to use the same local coordinate system, axis, and angle as the first point.")=`1`*, *[localCsys2](#abaqus.Assembly.Assembly.Assembly.ConnectorOrientation.localCsys2 "abaqus.Assembly.Assembly.Assembly.ConnectorOrientation.localCsys2 (Python parameter) — A DatumCsys object specifying the local coordinate system of the second connector point. This value may be None, indicating the global coordinate system.")=`None`*, *[axis2](#abaqus.Assembly.Assembly.Assembly.ConnectorOrientation.axis2 "abaqus.Assembly.Assembly.Assembly.ConnectorOrientation.axis2 (Python parameter) — A SymbolicConstant specifying the axis of a datum coordinate system about which an additional rotation is applied.")=`abaqusConstants.AXIS_1`*, *[angle2](#abaqus.Assembly.Assembly.Assembly.ConnectorOrientation.angle2 "abaqus.Assembly.Assembly.Assembly.ConnectorOrientation.angle2 (Python parameter) — A Float specifying the angle of the additional rotation.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/Assembly.py#L31-L86)[¶](#abaqus.Assembly.Assembly.Assembly.ConnectorOrientation "Permalink to this definition")
    :   This method creates a ConnectorOrientation object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].rootAssembly.ConnectorOrientation
        session.odbs[name].rootAssembly.ConnectorOrientation
        ```

        Note

        Check [ConnectorOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectororientationpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Assembly.Assembly.Assembly.ConnectorOrientation-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Assembly.Assembly.Assembly.ConnectorOrientation.region "Permalink to this definition")
            :   A Set object specifying the region to which the orientation is assigned.

            localCsys1=`None`[¶](#abaqus.Assembly.Assembly.Assembly.ConnectorOrientation.localCsys1 "Permalink to this definition")
            :   A DatumCsys object specifying the local coordinate system of the first connector point.
                This value may be None, indicating the global coordinate system.

            axis1=`abaqusConstants.AXIS_1`[¶](#abaqus.Assembly.Assembly.Assembly.ConnectorOrientation.axis1 "Permalink to this definition")
            :   A SymbolicConstant specifying the axis of a datum coordinate system about which an
                additional rotation is applied. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The
                default value is AXIS\_1.

            angle1=`0`[¶](#abaqus.Assembly.Assembly.Assembly.ConnectorOrientation.angle1 "Permalink to this definition")
            :   A Float specifying the angle of the additional rotation. The default value is 0.0.

            orient2sameAs1=`1`[¶](#abaqus.Assembly.Assembly.Assembly.ConnectorOrientation.orient2sameAs1 "Permalink to this definition")
            :   A Boolean specifying whether or not the second connector point is to use the same local
                coordinate system, axis, and angle as the first point. The default value is ON.

            localCsys2=`None`[¶](#abaqus.Assembly.Assembly.Assembly.ConnectorOrientation.localCsys2 "Permalink to this definition")
            :   A DatumCsys object specifying the local coordinate system of the second connector point.
                This value may be None, indicating the global coordinate system.

            axis2=`abaqusConstants.AXIS_1`[¶](#abaqus.Assembly.Assembly.Assembly.ConnectorOrientation.axis2 "Permalink to this definition")
            :   A SymbolicConstant specifying the axis of a datum coordinate system about which an
                additional rotation is applied. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The
                default value is AXIS\_1.

            angle2=`0`[¶](#abaqus.Assembly.Assembly.Assembly.ConnectorOrientation.angle2 "Permalink to this definition")
            :   A Float specifying the angle of the additional rotation. The default value is 0.0.

        Returns:[¶](#abaqus.Assembly.Assembly.Assembly.ConnectorOrientation-returns "Permalink to this headline")
        :   A ConnectorOrientation object.

        Return type:[¶](#abaqus.Assembly.Assembly.Assembly.ConnectorOrientation-return-type "Permalink to this headline")
        :   [`ConnectorOrientation`](#abaqus.Assembly.Assembly.Assembly.ConnectorOrientation "abaqus.Assembly.Assembly.Assembly.ConnectorOrientation (Python method) — This method creates a ConnectorOrientation object.")

*class* ConnectorOrientation(*[region](#abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation "abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation.__init__.region (Python parameter)")*, *[localCsys1](#abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation "abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation.__init__.localCsys1 (Python parameter)")=`None`*, *[axis1](#abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation "abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation.__init__.axis1 (Python parameter)")=`abaqusConstants.AXIS_1`*, *[angle1](#abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation "abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation.__init__.angle1 (Python parameter)")=`0`*, *[orient2sameAs1](#abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation "abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation.__init__.orient2sameAs1 (Python parameter)")=`1`*, *[localCsys2](#abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation "abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation.__init__.localCsys2 (Python parameter)")=`None`*, *[axis2](#abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation "abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation.__init__.axis2 (Python parameter)")=`abaqusConstants.AXIS_1`*, *[angle2](#abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation "abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation.__init__.angle2 (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/ConnectorOrientationArray.py#L13-L113)[¶](#abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The ConnectorOrientation object is used to assign a connector orientation to a connector.

    Note

    This object can be accessed by:

    ```python
    import assembly
    mdb.models[name].rootAssembly.connectorOrientations[i]
    import odbAccess
    session.odbs[name].rootAssembly.connectorOrientations[i]
    ```

    Note

    Check [ConnectorOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectororientationpyc.htm?contextscope=all).

    Member Details:

    angle1 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/ConnectorOrientationArray.py#L38-L39)[¶](#abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation.angle1 "Permalink to this definition")
    :   A Float specifying the angle of the additional rotation. The default value is 0.0.

    angle2 : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/ConnectorOrientationArray.py#L38-L39)[¶](#abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation.angle2 "Permalink to this definition")
    :   A Float specifying the angle of the additional rotation. The default value is 0.0.

    axis1 : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'AXIS_1'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/ConnectorOrientationArray.py#L33-L36)[¶](#abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation.axis1 "Permalink to this definition")
    :   A SymbolicConstant specifying the axis of a datum coordinate system about which an
        additional rotation is applied. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The
        default value is AXIS\_1.

    axis2 : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'AXIS_1'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/ConnectorOrientationArray.py#L33-L36)[¶](#abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation.axis2 "Permalink to this definition")
    :   A SymbolicConstant specifying the axis of a datum coordinate system about which an
        additional rotation is applied. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The
        default value is AXIS\_1.

    localCsys1 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`~abaqus.Datum.DatumCsys.DatumCsys`] = `<abaqus.Datum.DatumCsys.DatumCsys object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/ConnectorOrientationArray.py#L29-L31)[¶](#abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation.localCsys1 "Permalink to this definition")
    :   A DatumCsys object specifying the local coordinate system of the first connector point.
        This value may be None, indicating the global coordinate system.

    localCsys2 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`~abaqus.Datum.DatumCsys.DatumCsys`] = `<abaqus.Datum.DatumCsys.DatumCsys object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/ConnectorOrientationArray.py#L45-L47)[¶](#abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation.localCsys2 "Permalink to this definition")
    :   A DatumCsys object specifying the local coordinate system of the second connector point.
        This value may be None, indicating the global coordinate system.

    orient2sameAs1 : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/ConnectorOrientationArray.py#L41-L43)[¶](#abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation.orient2sameAs1 "Permalink to this definition")
    :   A Boolean specifying whether or not the second connector point is to use the same local
        coordinate system, axis, and angle as the first point. The default value is ON.

    region : --is-rst--:py:class:`~abaqus.Region.Set.Set`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/ConnectorOrientationArray.py)[¶](#abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation.region "Permalink to this definition")
    :   A Set object specifying the region to which the orientation is assigned.

    setValues(*\*[args](#abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation.setValues "abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation.setValues.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation.setValues "abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation.setValues.kwargs (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/ConnectorOrientationArray.py#L110-L113)[¶](#abaqus.Assembly.ConnectorOrientationArray.ConnectorOrientation.setValues "Permalink to this definition")
    :   This method modifies the ConnectorOrientation object.

*class* AssemblyBase[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L49-L1170)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase "Permalink to this definition")
:   Bases: [`AssemblyFeature`](#abaqus.Assembly.AssemblyFeature.AssemblyFeature "abaqus.Assembly.AssemblyFeature.AssemblyFeature (Python class) — Bases: Feature")

    An Assembly object is a container for instances of parts. The Assembly object has no constructor command.
    Abaqus creates the **rootAssembly** member when a Model object is created.

    Note

    This object can be accessed by:

    ```python
    import assembly
    mdb.models[name].rootAssembly
    ```

    Note

    Check [AssemblyBase on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all).

    Member Details:

    Instance(*[name](#abaqus.Assembly.AssemblyBase.AssemblyBase.Instance.name "abaqus.Assembly.AssemblyBase.AssemblyBase.Instance.name (Python parameter) — A String specifying the repository key."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[part](#abaqus.Assembly.AssemblyBase.AssemblyBase.Instance "abaqus.Assembly.AssemblyBase.AssemblyBase.Instance.part (Python parameter)"): [Part](part.html#abaqus.Part.PartModel.Part "abaqus.Part.Part.Part (Python class)")*, *[autoOffset](#abaqus.Assembly.AssemblyBase.AssemblyBase.Instance "abaqus.Assembly.AssemblyBase.AssemblyBase.Instance.autoOffset (Python parameter)"): [AbaqusBoolean](../../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.AbaqusBoolean "abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean (Python class)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `OFF`*, *[dependent](#abaqus.Assembly.AssemblyBase.AssemblyBase.Instance "abaqus.Assembly.AssemblyBase.AssemblyBase.Instance.dependent (Python parameter)"): [AbaqusBoolean](../../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.AbaqusBoolean "abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean (Python class)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `OFF`*) → [PartInstance](#abaqus.Assembly.PartInstanceArray.PartInstance "abaqus.Assembly.PartInstance.PartInstance (Python class)")[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L217-L245)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.Instance "Permalink to this definition")

    Instance(*[name](#abaqus.Assembly.AssemblyBase.AssemblyBase.Instance.name "abaqus.Assembly.AssemblyBase.AssemblyBase.Instance.name (Python parameter) — A String specifying the repository key."): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[model](#abaqus.Assembly.AssemblyBase.AssemblyBase.Instance "abaqus.Assembly.AssemblyBase.AssemblyBase.Instance.model (Python parameter)"): [AssemblyModel](#abaqus.Assembly.AssemblyModel.AssemblyModel "abaqus.Assembly.AssemblyModel.AssemblyModel (Python class) — Bases: ModelBase")*, *[autoOffset](#abaqus.Assembly.AssemblyBase.AssemblyBase.Instance "abaqus.Assembly.AssemblyBase.AssemblyBase.Instance.autoOffset (Python parameter)"): [AbaqusBoolean](../../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.AbaqusBoolean "abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean (Python class)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `OFF`*) → [ModelInstance](#abaqus.Assembly.ModelInstance.ModelInstance "abaqus.Assembly.ModelInstance.ModelInstance (Python class) — Bases: object")

    Instance(*[name](#abaqus.Assembly.AssemblyBase.AssemblyBase.Instance.name "abaqus.Assembly.AssemblyBase.AssemblyBase.Instance.name (Python parameter) — A String specifying the repository key.")*, *\*[args](#abaqus.Assembly.AssemblyBase.AssemblyBase.Instance "abaqus.Assembly.AssemblyBase.AssemblyBase.Instance.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Assembly.AssemblyBase.AssemblyBase.Instance.kwargs "abaqus.Assembly.AssemblyBase.AssemblyBase.Instance.kwargs (Python parameter) — Key-value arguments")*)
    :   This method creates a PartInstance object and puts it into the instances repository.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].rootAssembly.Instance
        ```

        Note

        Check [Instance on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-instancepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.Instance-parameters "Permalink to this headline")
        :   name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.Instance.name "Permalink to this definition")

            name
            :   A String specifying the repository key. The name must be a valid Abaqus object name.

            \*\*kwargs
            :   Key-value arguments

        Returns:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.Instance-returns "Permalink to this headline")
        :   A PartInstance object.

        Return type:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.Instance-return-type "Permalink to this headline")
        :   `PartInstance`

    InstanceFromBooleanCut(*[name](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanCut.name "abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanCut.name (Python parameter) — A String specifying the repository key.")*, *[instanceToBeCut](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanCut.instanceToBeCut "abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanCut.instanceToBeCut (Python parameter) — A PartInstance specifying the base instance from which to cut other instances.")*, *[cuttingInstances](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanCut.cuttingInstances "abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanCut.cuttingInstances (Python parameter) — A sequence of PartInstance objects specifying the instances with which to cut the base instance.")*, *[originalInstances](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanCut.originalInstances "abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanCut.originalInstances (Python parameter) — A SymbolicConstant specifying whether the original instances should be suppressed or deleted after the merge operation.")=`abaqusConstants.SUPPRESS`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L247-L282)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanCut "Permalink to this definition")
    :   This method creates a PartInstance in the instances repository after subtracting or cutting the
        geometries of a group of part instances from that of a base part instance.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].rootAssembly.InstanceFromBooleanCut
        ```

        Note

        Check [InstanceFromBooleanCut on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-instancefrombooleancutpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanCut-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanCut.name "Permalink to this definition")
            :   A String specifying the repository key. The name must be a valid Abaqus object name.

            instanceToBeCut[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanCut.instanceToBeCut "Permalink to this definition")
            :   A PartInstance specifying the base instance from which to cut other instances.

            cuttingInstances[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanCut.cuttingInstances "Permalink to this definition")
            :   A sequence of PartInstance objects specifying the instances with which to cut the base
                instance.

            originalInstances=`abaqusConstants.SUPPRESS`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanCut.originalInstances "Permalink to this definition")
            :   A SymbolicConstant specifying whether the original instances should be suppressed or
                deleted after the merge operation. Possible values are SUPPRESS or DELETE. The default
                value is SUPPRESS.

        Returns:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanCut-returns "Permalink to this headline")
        :   A PartInstance object.

        Return type:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanCut-return-type "Permalink to this headline")
        :   `PartInstance`

    InstanceFromBooleanMerge(*[name](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge.name "abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge.name (Python parameter) — A String specifying the repository key.")*, *[instances](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge.instances "abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge.instances (Python parameter) — A sequence of PartInstance objects specifying the part instances to merge.")*, *[keepIntersections](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge.keepIntersections "abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge.keepIntersections (Python parameter) — A Boolean specifying whether the boundary intersections of Abaqus native part instances should be retained after the merge operation.")=`False`*, *[originalInstances](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge.originalInstances "abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge.originalInstances (Python parameter) — A SymbolicConstant specifying whether the original instances should be suppressed or deleted after the merge operation.")=`abaqusConstants.SUPPRESS`*, *[domain](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge.domain "abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge.domain (Python parameter) — A SymbolicConstant specifying whether geometry or mesh of the specified part instances is to be merged.")=`abaqusConstants.GEOMETRY`*, *[mergeNodes](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge.mergeNodes "abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge.mergeNodes (Python parameter) — A SymbolicConstant specifying which nodes of the specified part instances should be considered for merging.")=`abaqusConstants.BOUNDARY_ONLY`*, *[nodeMergingTolerance](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge.nodeMergingTolerance "abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge.nodeMergingTolerance (Python parameter) — A Float specifying the maximum distance between nodes of the specified part instances that will be merged and replaced with a single node in the new part.")=`None`*, *[removeDuplicateElements](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge.removeDuplicateElements "abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge.removeDuplicateElements (Python parameter) — A Boolean specifying whether elements with the same connectivity in the new part will be merged into a single element.")=`True`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L284-L340)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge "Permalink to this definition")
    :   This method creates a PartInstance in the instances repository after merging two or more part
        instances.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].rootAssembly.InstanceFromBooleanMerge
        ```

        Note

        Check [InstanceFromBooleanMerge on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-instancefrombooleanmergepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge.name "Permalink to this definition")
            :   A String specifying the repository key. The name must be a valid Abaqus object name.

            instances[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge.instances "Permalink to this definition")
            :   A sequence of PartInstance objects specifying the part instances to merge.

            keepIntersections=`False`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge.keepIntersections "Permalink to this definition")
            :   A Boolean specifying whether the boundary intersections of Abaqus native part instances
                should be retained after the merge operation. The default value is False.

            originalInstances=`abaqusConstants.SUPPRESS`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge.originalInstances "Permalink to this definition")
            :   A SymbolicConstant specifying whether the original instances should be suppressed or
                deleted after the merge operation. Possible values are SUPPRESS or DELETE. The default
                value is SUPPRESS.

            domain=`abaqusConstants.GEOMETRY`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge.domain "Permalink to this definition")
            :   A SymbolicConstant specifying whether geometry or mesh of the specified part instances
                is to be merged. Possible values are GEOMETRY, MESH or BOTH. The default value is
                GEOMETRY.

            mergeNodes=`abaqusConstants.BOUNDARY_ONLY`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge.mergeNodes "Permalink to this definition")
            :   A SymbolicConstant specifying which nodes of the specified part instances should be
                considered for merging. This argument is only applicable if **domain** is MESH. Possible
                values are BOUNDARY\_ONLY, ALL, or NONE. The default value is BOUNDARY\_ONLY.

            nodeMergingTolerance=`None`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge.nodeMergingTolerance "Permalink to this definition")
            :   A Float specifying the maximum distance between nodes of the specified part instances
                that will be merged and replaced with a single node in the new part. The location of the
                new node is the average position of the deleted nodes. This argument is only applicable
                if **domain** is MESH. The default value is 10⁻⁶.

            removeDuplicateElements=`True`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge.removeDuplicateElements "Permalink to this definition")
            :   A Boolean specifying whether elements with the same connectivity in the new part will be
                merged into a single element. This argument is only applicable if **domain** is MESH. The
                default value is True.

        Returns:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge-returns "Permalink to this headline")
        :   A PartInstance object.

        Return type:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.InstanceFromBooleanMerge-return-type "Permalink to this headline")
        :   `PartInstance`

    LinearInstancePattern(*[instanceList](#abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern.instanceList "abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern.instanceList (Python parameter) — A sequence of Strings specifying the names of instances to pattern.")*, *[number1](#abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern.number1 "abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern.number1 (Python parameter) — An Int specifying the total number of instances, including the original instances, that appear along the first direction in the pattern.")*, *[spacing1](#abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern.spacing1 "abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern.spacing1 (Python parameter) — A Float specifying the spacing between instances along the first direction in the pattern.")*, *[number2](#abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern.number2 "abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern.number2 (Python parameter) — An Int specifying the total number of instances, including the original instances, that appear along the second direction in the pattern.")*, *[spacing2](#abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern.spacing2 "abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern.spacing2 (Python parameter) — A Float specifying the spacing between instances along the second direction in the pattern.")*, *[direction1](#abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern.direction1 "abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern.direction1 (Python parameter) — A sequence of three Floats specifying a vector along the first direction.")=`()`*, *[direction2](#abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern.direction2 "abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern.direction2 (Python parameter) — A sequence of three Floats specifying a vector along the second direction.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L342-L389)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern "Permalink to this definition")
    :   This method creates multiple PartInstance objects in a linear pattern and puts them into the
        instances repository.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].rootAssembly.LinearInstancePattern
        ```

        Note

        Check [LinearInstancePattern on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-linearinstancepatternpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern-parameters "Permalink to this headline")
        :   instanceList[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern.instanceList "Permalink to this definition")
            :   A sequence of Strings specifying the names of instances to pattern.

            number1[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern.number1 "Permalink to this definition")
            :   An Int specifying the total number of instances, including the original instances, that
                appear along the first direction in the pattern.

            spacing1[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern.spacing1 "Permalink to this definition")
            :   A Float specifying the spacing between instances along the first direction in the
                pattern.

            number2[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern.number2 "Permalink to this definition")
            :   An Int specifying the total number of instances, including the original instances, that
                appear along the second direction in the pattern.

            spacing2[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern.spacing2 "Permalink to this definition")
            :   A Float specifying the spacing between instances along the second direction in the
                pattern.

            direction1=`()`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern.direction1 "Permalink to this definition")
            :   A sequence of three Floats specifying a vector along the first direction. The default
                value is (1.0, 0.0, 0.0).

            direction2=`()`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern.direction2 "Permalink to this definition")
            :   A sequence of three Floats specifying a vector along the second direction. The default
                value is (0.0, 1.0, 0.0).

        Returns:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern-returns "Permalink to this headline")
        :   A sequence of PartInstance objects.

        Return type:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.LinearInstancePattern-return-type "Permalink to this headline")
        :   `Sequence[PartInstance]`

    RadialInstancePattern(*[instanceList](#abaqus.Assembly.AssemblyBase.AssemblyBase.RadialInstancePattern.instanceList "abaqus.Assembly.AssemblyBase.AssemblyBase.RadialInstancePattern.instanceList (Python parameter) — A sequence of Strings specifying the names of instances to pattern.")*, *[number](#abaqus.Assembly.AssemblyBase.AssemblyBase.RadialInstancePattern.number "abaqus.Assembly.AssemblyBase.AssemblyBase.RadialInstancePattern.number (Python parameter) — An Int specifying the total number of instances, including the original instances, that appear in the radial pattern.")*, *[totalAngle](#abaqus.Assembly.AssemblyBase.AssemblyBase.RadialInstancePattern.totalAngle "abaqus.Assembly.AssemblyBase.AssemblyBase.RadialInstancePattern.totalAngle (Python parameter) — A Float specifying the total angle in degrees between the first and last instance in the pattern.")*, *[point](#abaqus.Assembly.AssemblyBase.AssemblyBase.RadialInstancePattern.point "abaqus.Assembly.AssemblyBase.AssemblyBase.RadialInstancePattern.point (Python parameter) — A sequence of three Floats specifying the center of the radial pattern.")=`()`*, *[axis](#abaqus.Assembly.AssemblyBase.AssemblyBase.RadialInstancePattern.axis "abaqus.Assembly.AssemblyBase.AssemblyBase.RadialInstancePattern.axis (Python parameter) — A sequence of three Floats specifying the central axis of the radial pattern.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L391-L433)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.RadialInstancePattern "Permalink to this definition")
    :   This method creates multiple PartInstance objects in a radial pattern and puts them into the
        instances repository.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].rootAssembly.RadialInstancePattern
        ```

        Note

        Check [RadialInstancePattern on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-radialinstancepatternpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.RadialInstancePattern-parameters "Permalink to this headline")
        :   instanceList[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.RadialInstancePattern.instanceList "Permalink to this definition")
            :   A sequence of Strings specifying the names of instances to pattern.

            number[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.RadialInstancePattern.number "Permalink to this definition")
            :   An Int specifying the total number of instances, including the original instances, that
                appear in the radial pattern.

            totalAngle[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.RadialInstancePattern.totalAngle "Permalink to this definition")
            :   A Float specifying the total angle in degrees between the first and last instance in the
                pattern. A positive angle corresponds to a counter-clockwise direction. The values 360°
                and -360° represent a special case where the pattern makes a full circle. In this case,
                because the copy would overlay the original, the copy is not placed at the last
                position. Possible values are -360.0 ≤ **totalAngle** ≤ 360.0.

            point=`()`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.RadialInstancePattern.point "Permalink to this definition")
            :   A sequence of three Floats specifying the center of the radial pattern. The default
                value is (0.0, 0.0, 0.0).

            axis=`()`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.RadialInstancePattern.axis "Permalink to this definition")
            :   A sequence of three Floats specifying the central axis of the radial pattern. The
                default value is (0.0, 0.0, 1.0).

        Returns:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.RadialInstancePattern-returns "Permalink to this headline")
        :   A sequence of PartInstance objects.

        Return type:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.RadialInstancePattern-return-type "Permalink to this headline")
        :   `Sequence[PartInstance]`

    allInstances : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:data:`~typing.Union`\[:py:class:`~abaqus.Assembly.PartInstance.PartInstance`, :py:class:`~abaqus.Assembly.ModelInstance.ModelInstance`]] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L142-L144)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.allInstances "Permalink to this definition")
    :   A PartInstance object specifying the PartInstances and A ModelInstance object specifying
        the ModelInstances.

    allInternalSets : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Region.Set.Set`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L127-L128)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.allInternalSets "Permalink to this definition")
    :   A repository of Set objects specifying picked regions.

    allInternalSurfaces : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Region.Surface.Surface`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L117-L118)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.allInternalSurfaces "Permalink to this definition")
    :   A repository of Surface objects specifying picked regions.

    allSets : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Region.Set.Set`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L123-L125)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.allSets "Permalink to this definition")
    :   A repository of Set objects specifying for more information, see [Region
        commands](<https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all>).

    allSurfaces : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Region.Surface.Surface`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L109-L111)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.allSurfaces "Permalink to this definition")
    :   A repository of Surface objects specifying for more information, see [Region
        commands](<https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all>).

    backup()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L435-L441)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.backup "Permalink to this definition")
    :   This method makes a backup copy of the features in the assembly.

        The backup() method is used in conjunction with the restore() method.

    clearGeometryCache()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L443-L449)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.clearGeometryCache "Permalink to this definition")
    :   This method deletes the geometry cache.

        Deleting the geometry cache reduces the amount of memory being used.

    connectorOrientations : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Assembly.ConnectorOrientation.ConnectorOrientation`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L152-L153)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.connectorOrientations "Permalink to this definition")
    :   A ConnectorOrientationArray object.

    copyMeshPattern(*[elements](#abaqus.Assembly.AssemblyBase.AssemblyBase.copyMeshPattern.elements "abaqus.Assembly.AssemblyBase.AssemblyBase.copyMeshPattern.elements (Python parameter) — A sequence of MeshElement objects or a Set object containing elements and specifying the source region.")=`()`*, *[faces](#abaqus.Assembly.AssemblyBase.AssemblyBase.copyMeshPattern.faces "abaqus.Assembly.AssemblyBase.AssemblyBase.copyMeshPattern.faces (Python parameter) — A sequence of Face objects that have associated with shell elements or element faces and specifying the source region.")=`()`*, *[elemFaces](#abaqus.Assembly.AssemblyBase.AssemblyBase.copyMeshPattern.elemFaces "abaqus.Assembly.AssemblyBase.AssemblyBase.copyMeshPattern.elemFaces (Python parameter) — A sequence of MeshFace objects specifying the source region.")=`()`*, *[targetFace](#abaqus.Assembly.AssemblyBase.AssemblyBase.copyMeshPattern.targetFace "abaqus.Assembly.AssemblyBase.AssemblyBase.copyMeshPattern.targetFace (Python parameter) — A MeshFace object specifying the target region.")=`None`*, *[nodes](#abaqus.Assembly.AssemblyBase.AssemblyBase.copyMeshPattern.nodes "abaqus.Assembly.AssemblyBase.AssemblyBase.copyMeshPattern.nodes (Python parameter) — A sequence of MeshNode objects or a Set object containing nodes on the boundary of source region which are to be positioned to the boundary of target face.")=`()`*, *[coordinates](#abaqus.Assembly.AssemblyBase.AssemblyBase.copyMeshPattern.coordinates "abaqus.Assembly.AssemblyBase.AssemblyBase.copyMeshPattern.coordinates (Python parameter) — A sequence of three-dimensional coordinate tuples specifying the coordinates for each of the given nodes.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L1118-L1155)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.copyMeshPattern "Permalink to this definition")
    :   This method copies a mesh pattern from a source region consisting of a set of shell elements or
        element faces onto a target face, mapping nodes and elements in a one-one correspondence between source
        and target.

        Note

        Check [AssemblyBase.copyMeshPattern on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblycopymeshpatternpyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.copyMeshPattern-parameters "Permalink to this headline")
        :   elements=`()`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.copyMeshPattern.elements "Permalink to this definition")
            :   A sequence of MeshElement objects or a Set object containing elements and specifying the
                source region.

            faces=`()`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.copyMeshPattern.faces "Permalink to this definition")
            :   A sequence of Face objects that have associated with shell elements or element faces and
                specifying the source region.

            elemFaces=`()`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.copyMeshPattern.elemFaces "Permalink to this definition")
            :   A sequence of MeshFace objects specifying the source region.

            targetFace=`None`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.copyMeshPattern.targetFace "Permalink to this definition")
            :   A MeshFace object specifying the target region. The target face can be of a different
                part instance.

            nodes=`()`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.copyMeshPattern.nodes "Permalink to this definition")
            :   A sequence of MeshNode objects or a Set object containing nodes on the boundary of
                source region which are to be positioned to the boundary of target face.

            coordinates=`()`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.copyMeshPattern.coordinates "Permalink to this definition")
            :   A sequence of three-dimensional coordinate tuples specifying the coordinates for each of
                the given nodes. When specified, the number of coordinate tuples must match the number
                of given nodes, and be ordered to correspond to the given nodes in *ascending order*
                according to index. These coordinates are positions of the nodes of a mesh that will be
                the target face corresponding to nodes provided.

    datums : --is-rst--:py:class:`dict`\[:py:class:`int`, :py:class:`~abaqus.Datum.Datum.Datum`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L96-L97)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.datums "Permalink to this definition")
    :   A repository of Datum objects specifying all Datum objects in the assembly.

    deleteAllFeatures()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L451-L454)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.deleteAllFeatures "Permalink to this definition")
    :   This method deletes all the features in the assembly.

    deleteFeatures(*[featureNames](#abaqus.Assembly.AssemblyBase.AssemblyBase.deleteFeatures.featureNames "abaqus.Assembly.AssemblyBase.AssemblyBase.deleteFeatures.featureNames (Python parameter) — A sequence of Strings specifying the feature names that will be deleted from the assembly.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L456-L466)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.deleteFeatures "Permalink to this definition")
    :   This method deletes specified features from the assembly.

        Note

        Check [AssemblyBase.deleteFeatures on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblydeletefeaturespyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.deleteFeatures-parameters "Permalink to this headline")
        :   featureNames[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.deleteFeatures.featureNames "Permalink to this definition")
            :   A sequence of Strings specifying the feature names that will be deleted from the
                assembly.

    edges : --is-rst--:py:class:`~abaqus.BasicGeometry.EdgeArray.EdgeArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L81-L83)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.edges "Permalink to this definition")
    :   An EdgeArray object specifying all the edges existing at the assembly level. This member
        does not provide access to the edges at the instance level.

    elements : --is-rst--:py:class:`~abaqus.Mesh.MeshElementArray.MeshElementArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L85-L87)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.elements "Permalink to this definition")
    :   A MeshElementArray object specifying all the elements existing at the assembly level.
        This member does not provide access to the elements at the instance level.

    engineeringFeatures : --is-rst--:py:class:`~abaqus.EngineeringFeature.EngineeringFeature.EngineeringFeature` = `<abaqus.EngineeringFeature.EngineeringFeature.EngineeringFeature object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L146-L147)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.engineeringFeatures "Permalink to this definition")
    :   An EngineeringFeature object.

    excludeFromSimulation(*[instances](#abaqus.Assembly.AssemblyBase.AssemblyBase.excludeFromSimulation.instances "abaqus.Assembly.AssemblyBase.AssemblyBase.excludeFromSimulation.instances (Python parameter) — A sequence of PartInstance objects to be excluded from the analysis.")*, *[exclude](#abaqus.Assembly.AssemblyBase.AssemblyBase.excludeFromSimulation.exclude "abaqus.Assembly.AssemblyBase.AssemblyBase.excludeFromSimulation.exclude (Python parameter) — A Bool specifying whether to exclude the selected instances from the analysis or include them.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L468-L480)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.excludeFromSimulation "Permalink to this definition")
    :   This method excludes the specified part instances from the analysis.

        Note

        Check [AssemblyBase.excludeFromSimulation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblyexcludefromsimulationpyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.excludeFromSimulation-parameters "Permalink to this headline")
        :   instances[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.excludeFromSimulation.instances "Permalink to this definition")
            :   A sequence of PartInstance objects to be excluded from the analysis.

            exclude[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.excludeFromSimulation.exclude "Permalink to this definition")
            :   A Bool specifying whether to exclude the selected instances from the analysis or include
                them.

    featurelistInfo()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L482-L485)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.featurelistInfo "Permalink to this definition")
    :   This method prints the name and status of all the features in the feature lists.

    features : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Assembly.AssemblyFeature.AssemblyFeature`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L99-L100)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.features "Permalink to this definition")
    :   A repository of Feature objects specifying all Feature objects in the assembly.

    featuresById : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Assembly.AssemblyFeature.AssemblyFeature`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L102-L107)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.featuresById "Permalink to this definition")
    :   A repository of Feature objects specifying all Feature objects in the assembly.The
        Feature objects in the featuresById repository are the same as the Feature objects in
        the features repository. However, the key to the objects in the featuresById repository
        is an integer specifying the **ID**, whereas the key to the objects in the features
        repository is a string specifying the **name**.

    getAngle(*[plane1](#abaqus.Assembly.AssemblyBase.AssemblyBase.getAngle.plane1 "abaqus.Assembly.AssemblyBase.AssemblyBase.getAngle.plane1 (Python parameter) — A Face, MeshFace, or a Datum object specifying the first plane.")*, *[plane2](#abaqus.Assembly.AssemblyBase.AssemblyBase.getAngle.plane2 "abaqus.Assembly.AssemblyBase.AssemblyBase.getAngle.plane2 (Python parameter) — A Face, MeshFace, or a Datum object specifying the second plane.")*, *[line1](#abaqus.Assembly.AssemblyBase.AssemblyBase.getAngle.line1 "abaqus.Assembly.AssemblyBase.AssemblyBase.getAngle.line1 (Python parameter) — An Edge, MeshEdge, or a Datum object specifying the first curve.")*, *[line2](#abaqus.Assembly.AssemblyBase.AssemblyBase.getAngle.line2 "abaqus.Assembly.AssemblyBase.AssemblyBase.getAngle.line2 (Python parameter) — An Edge, MeshEdge, or a Datum object specifying the second curve.")*, *[commonVertex](#abaqus.Assembly.AssemblyBase.AssemblyBase.getAngle.commonVertex "abaqus.Assembly.AssemblyBase.AssemblyBase.getAngle.commonVertex (Python parameter) — If the two selected Edge objects have more than one vertex in common, this ConstrainedSketchVertex object specifies the vertex at which to evaluate the angle.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L604-L636)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getAngle "Permalink to this definition")
    :   This method returns the angle between the specified entities.

        Note

        Check [AssemblyBase.getAngle on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblygetanglepyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getAngle-parameters "Permalink to this headline")
        :   plane1[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getAngle.plane1 "Permalink to this definition")
            :   A Face, MeshFace, or a Datum object specifying the first plane. The Datum object must
                represent a datum plane. The **plane1** and **line1** arguments are mutually exclusive. One
                of them must be specified.

            plane2[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getAngle.plane2 "Permalink to this definition")
            :   A Face, MeshFace, or a Datum object specifying the second plane. The Datum object must
                represent a datum plane. The **plane2** and **line2** arguments are mutually exclusive. One
                of them must be specified.

            line1[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getAngle.line1 "Permalink to this definition")
            :   An Edge, MeshEdge, or a Datum object specifying the first curve. The Datum object must
                represent a datum axis. The **plane1** and **line1** arguments are mutually exclusive. One
                of them must be specified.

            line2[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getAngle.line2 "Permalink to this definition")
            :   An Edge, MeshEdge, or a Datum object specifying the second curve. The Datum object must
                represent a datum axis. The **plane2** and **line2** arguments are mutually exclusive. One
                of them must be specified.

            commonVertex=`''`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getAngle.commonVertex "Permalink to this definition")
            :   If the two selected Edge objects have more than one vertex in common, this ConstrainedSketchVertex object
                specifies the vertex at which to evaluate the angle.

        Returns:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getAngle-returns "Permalink to this headline")
        :   A Float specifying the angle between the specified entities. If you provide a plane as
            an argument, Abaqus/CAE computes the angle using the normal to the plane.

        Return type:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getAngle-return-type "Permalink to this headline")
        :   [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")

    getCoordinates(*[entity](#abaqus.Assembly.AssemblyBase.AssemblyBase.getCoordinates.entity "abaqus.Assembly.AssemblyBase.AssemblyBase.getCoordinates.entity (Python parameter) — A ConstrainedSketchVertex, Datum point, MeshNode, or ReferencePoint specifying the entity to query.")*, *[csys=<abaqus.Datum.DatumCsys.DatumCsys object>](#abaqus.Assembly.AssemblyBase.AssemblyBase.getCoordinates "abaqus.Assembly.AssemblyBase.AssemblyBase.getCoordinates.csys=<abaqus.Datum.DatumCsys.DatumCsys object> (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L638-L659)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getCoordinates "Permalink to this definition")
    :   This method returns the coordinates of a specified point.

        Note

        Check [AssemblyBase.getCoordinates on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblygetcoordinatespyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getCoordinates-parameters "Permalink to this headline")
        :   entity[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getCoordinates.entity "Permalink to this definition")
            :   A ConstrainedSketchVertex, Datum point, MeshNode, or ReferencePoint specifying the entity to query.

            csys : [`DatumCsys`](datum.html#abaqus.Datum.DatumCsys.DatumCsys "abaqus.Datum.DatumCsys.DatumCsys (Python class) — Bases: Datum"), default: `<abaqus.Datum.DatumCsys.DatumCsys object at 0x7f850c2d4ed0>`
            :   A DatumCsys object specifying the desired coordinate system of the returned coordinates. By default,
                coordinates are given in the global coordinate system.

                New in version 2023: The `csys` argument was added.

        Returns:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getCoordinates-returns "Permalink to this headline")
        :   A tuple of three Floats representing the coordinates of the specified point.

        Return type:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getCoordinates-return-type "Permalink to this headline")
        :   `tuple[float`, `float]`

    getDistance(*[entity1](#abaqus.Assembly.AssemblyBase.AssemblyBase.getDistance.entity1 "abaqus.Assembly.AssemblyBase.AssemblyBase.getDistance.entity1 (Python parameter) — A ConstrainedSketchVertex, Datum point, MeshNode, or Edge specifying the first entity from which to measure.")*, *[entity2](#abaqus.Assembly.AssemblyBase.AssemblyBase.getDistance.entity2 "abaqus.Assembly.AssemblyBase.AssemblyBase.getDistance.entity2 (Python parameter) — A ConstrainedSketchVertex, Datum point, MeshNode, or Edge specifying the second entity to which to measure.")*, *[printResults=0](#abaqus.Assembly.AssemblyBase.AssemblyBase.getDistance "abaqus.Assembly.AssemblyBase.AssemblyBase.getDistance.printResults=0 (Python parameter)")*, *[csys=<abaqus.Datum.DatumCsys.DatumCsys object>](#abaqus.Assembly.AssemblyBase.AssemblyBase.getDistance "abaqus.Assembly.AssemblyBase.AssemblyBase.getDistance.csys=<abaqus.Datum.DatumCsys.DatumCsys object> (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L661-L689)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getDistance "Permalink to this definition")
    :   Depending on the arguments provided, this method returns one of the following:

        * The distance between two points.
        * The minimum distance between a point and an edge.
        * The minimum distance between two edges.

        Changed in version 2023: The `csys` argument was removed.

        Note

        Check [AssemblyBase.getDistance on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblygetdistancepyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getDistance-parameters "Permalink to this headline")
        :   entity1[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getDistance.entity1 "Permalink to this definition")
            :   A ConstrainedSketchVertex, Datum point, MeshNode, or Edge specifying the first entity from which to
                measure.

            entity2[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getDistance.entity2 "Permalink to this definition")
            :   A ConstrainedSketchVertex, Datum point, MeshNode, or Edge specifying the second entity to which to
                measure.

            printResults : [`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.13)")[[`AbaqusBoolean`](../../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.AbaqusBoolean "abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean (Python class)"), [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")], default: `0`
            :   A Boolean that determines whether a verbose output is to be printed. The default is True

        Returns:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getDistance-returns "Permalink to this headline")
        :   A Float specifying the calculated distance.

        Return type:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getDistance-return-type "Permalink to this headline")
        :   [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")

    getFacesAndVerticesOfAttachmentLines(*[edges](#abaqus.Assembly.AssemblyBase.AssemblyBase.getFacesAndVerticesOfAttachmentLines.edges "abaqus.Assembly.AssemblyBase.AssemblyBase.getFacesAndVerticesOfAttachmentLines.edges (Python parameter) — An EdgeArray object which is a sequence of Edge objects.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L691-L716)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getFacesAndVerticesOfAttachmentLines "Permalink to this definition")
    :   Given an array of edge objects, this method returns a tuple of dictionary objects. Each object
        consists of five members including the attachment line and associated face and vertex objects.

        Note

        Check [AssemblyBase.getFacesAndVerticesOfAttachmentLines on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblygetfacesandverticesofattachmentlinespyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getFacesAndVerticesOfAttachmentLines-parameters "Permalink to this headline")
        :   edges[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getFacesAndVerticesOfAttachmentLines.edges "Permalink to this definition")
            :   An EdgeArray object which is a sequence of Edge objects.

        Returns:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getFacesAndVerticesOfAttachmentLines-returns "Permalink to this headline")
        :   A tuple of dictionary objects. Each dictionary contains five items with the following keys:

            * **edge**: An Edge object specifying the attachment line.
            * **startFace**: A Face object specifying the face associated with one end of the
              attachment line.
            * **endFace**: A Face object specifying the face associated with the other end of
              the attachment line.
            * **startVertex**: A ConstrainedSketchVertex
              object specifying the vertex associated with one end of the attachment line. This end is also associated with the startFace.
            * **endVertex**: A ConstrainedSketchVertex
              object specifying the vertex associated with the other end of the attachment line. This end is also associated with the endFace.

        Return type:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getFacesAndVerticesOfAttachmentLines-return-type "Permalink to this headline")
        :   `Sequence[dict]`

    getMassProperties(*[regions](#abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.regions "abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.regions (Python parameter) — A MeshElementArray, CellArray, FaceArray, EdgeArray, or list of PartInstance objects specifying the regions whose mass properties are to be queried.")=`''`*, *[relativeAccuracy](#abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.relativeAccuracy "abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.relativeAccuracy (Python parameter) — A SymbolicConstant specifying the relative accuracy for geometry computation.")=`abaqusConstants.LOW`*, *[useMesh](#abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.useMesh "abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.useMesh (Python parameter) — A Boolean specifying whether the mesh should be used in the computation if the geometry is meshed.")=`False`*, *[specifyDensity](#abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.specifyDensity "abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.specifyDensity (Python parameter) — A Boolean specifying whether a user-specified density should be used in regions with density errors such as undefined material density.")=`False`*, *[density](#abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.density "abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.density (Python parameter) — A double value specifying the user-specified density value to be used in regions with density errors.")=`''`*, *[specifyThickness](#abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.specifyThickness "abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.specifyThickness (Python parameter) — A Boolean specifying whether a user-specified thickness should be used in regions with thickness errors such as undefined thickness.")=`False`*, *[thickness](#abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.thickness "abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.thickness (Python parameter) — A double value specifying the user-specified thickness value to be used in regions with thickness errors.")=`''`*, *[miAboutCenterOfMass](#abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.miAboutCenterOfMass "abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.miAboutCenterOfMass (Python parameter) — A Boolean specifying if the moments of inertia should be evaluated about the center of mass.")=`True`*, *[miAboutPoint](#abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.miAboutPoint "abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.miAboutPoint (Python parameter) — A tuple of three floats specifying the coordinates of the point about which to evaluate the moment of inertia.")=`Ellipsis`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L487-L602)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties "Permalink to this definition")
    :   This method returns the mass properties of the assembly, or instances or regions. Only beams,
        trusses, shells, solids, point, nonstructural mass, and rotary inertia elements are supported.

        Note

        Check [AssemblyBase.getMassProperties on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblygetmasspropertiespyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties-parameters "Permalink to this headline")
        :   regions=`''`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.regions "Permalink to this definition")
            :   A MeshElementArray, CellArray, FaceArray, EdgeArray, or list of PartInstance objects
                specifying the regions whose mass properties are to be queried. The whole assembly is
                queried by default.

            relativeAccuracy=`abaqusConstants.LOW`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.relativeAccuracy "Permalink to this definition")
            :   A SymbolicConstant specifying the relative accuracy for geometry computation. Possible
                values are LOW, MEDIUM, and HIGH. The default value is LOW.

            useMesh=`False`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.useMesh "Permalink to this definition")
            :   A Boolean specifying whether the mesh should be used in the computation if the geometry
                is meshed. The default value is False.

            specifyDensity=`False`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.specifyDensity "Permalink to this definition")
            :   A Boolean specifying whether a user-specified density should be used in regions with
                density errors such as undefined material density. The default value is False.

            density=`''`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.density "Permalink to this definition")
            :   A double value specifying the user-specified density value to be used in regions with
                density errors. The user-specified density should be greater than 0.

            specifyThickness=`False`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.specifyThickness "Permalink to this definition")
            :   A Boolean specifying whether a user-specified thickness should be used in regions with
                thickness errors such as undefined thickness. The default value is False.

            thickness=`''`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.thickness "Permalink to this definition")
            :   A double value specifying the user-specified thickness value to be used in regions with
                thickness errors. The user-specified thickness should be greater than 0.

            miAboutCenterOfMass=`True`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.miAboutCenterOfMass "Permalink to this definition")
            :   A Boolean specifying if the moments of inertia should be evaluated about the center of
                mass. The default value is True.

            miAboutPoint=`Ellipsis`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties.miAboutPoint "Permalink to this definition")
            :   A tuple of three floats specifying the coordinates of the point about which to evaluate
                the moment of inertia. By default if the moments of inertia are not being evaluated
                about the center of mass, they will be evaluated about the origin.

        Returns:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties-returns "Permalink to this headline")
        :   **properties** – A Dictionary object with the following items:
            **area**: None or a Float specifying the sum of the area of the specified faces. The area
            is computed only for one side for shells.
            **areaCentroid**: None or a tuple of three Floats representing the coordinates of the area
            centroid.
            **volume**: None or a Float specifying the volume of the specified regions.
            **volumeCentroid**: None or a tuple of three Floats representing the coordinates of the
            volume centroid.
            **massFromMassPerUnitSurfaceArea**: None or a Float specifying the mass due to mass per
            unit surface area.
            **mass**: None or a Float specifying the mass of the specified regions. It is the total
            mass and includes mass from quantities such as mass per unit surface area.
            **centerOfMass**: None or a tuple of three Floats representing the coordinates of the
            center of mass.
            **momentOfInertia**: None or a tuple of six Floats representing the moments of inertia
            about the center of mass or about the point specified.
            **warnings**: A tuple of SymbolicConstants representing the problems encountered while
            computing the mass properties. Possible SymbolicConstants are:
            UNSUPPORTED\_ENTITIES: Some unsupported entities exist in the specified regions. The mass
            properties are computed only for beams, trusses, shells, solids, point and
            non-structural mass elements, and rotary inertia elements. The mass properties are not
            computed for axisymmetric elements, springs, connectors, gaskets, or any other elements.
            MISSING\_THICKNESS: For some regions, the section definitions are missing thickness
            values.
            ZERO\_THICKNESS: For some regions, the section definitions have a zero thickness value.
            VARIABLE\_THICKNESS: The nodal thickness or field thickness specified for some regions
            has been ignored.
            NON\_APPLICABLE\_THICKNESS: For some regions, the thickness value is not applicable to the
            corresponding sections specified on the regions.
            MISSING\_DENSITY: For some regions, the section definitions are missing material density
            values.
            MISSING\_MATERIAL\_DEFINITION: For some regions, the material definition is missing.
            ZERO\_DENSITY: For some regions, the section definitions have a zero material density
            value.
            UNSUPPORTED\_DENSITY: For some regions, either a negative material density or a
            temperature dependent density has been specified, or the material value is missing for
            one or more plies in the composite section.
            SHELL\_OFFSETS: For shells, this method does not account for any offsets specified.
            MISSING\_SECTION\_DEFINITION: For some regions, the section definition is missing.
            UNSUPPORTED\_SECTION\_DEFINITION: The section definition provided for some regions is not
            supported.
            REINFORCEMENTS: This method does not account for any reinforcements specified on the
            model.
            SMEARED\_PROPERTIES: For regions with composite section assignments, the density is
            smeared across the thickness. The volume centroid and center of mass computations for a
            composite shell use a lumped mass approach where the volume and mass is assumed to be
            lumped in the plane of the shell. As a result of these approximations the volume
            centroid, center of mass and moments of inertia may be slightly inaccurate for regions
            with composite section assignments.
            UNSUPPORTED\_NON\_STRUCTURAL\_MASS\_ENTITIES: This method does not account for any
            non-structural mass on wires.
            INCORRECT\_MOMENT\_OF\_INERTIA: For geometry regions with non-structural mass per volume,
            the non-structural mass is assumed to be a point mass at the centroid of the regions.
            Thus, the moments of inertia may be inaccurate as the distribution of the non-structural
            mass is not accounted for. Use the mesh for accurately computing the moments of inertia.
            MISSING\_BEAM\_ORIENTATIONS: For some regions with beam section assignments, the beam
            section orientations are missing.
            UNSUPPORTED\_BEAM\_PROFILES: This method supports the Box, Pipe, Circular, Rectangular,
            Hexagonal, Trapezoidal, I, L, T, Arbitrary, and Tapered beam profiles. Any other beam
            profile is not supported.
            TAPERED\_BEAM\_MI: Moment of inertia calculations for tapered beams are not accurate.
            SUBSTRUCTURE\_INCORRECT\_PROPERTIES: The user assigned density and thickness is not
            considered for substructures.

        Return type:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getMassProperties-return-type "Permalink to this headline")
        :   [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.13)")

    getSurfaceSections(*[surface](#abaqus.Assembly.AssemblyBase.AssemblyBase.getSurfaceSections.surface "abaqus.Assembly.AssemblyBase.AssemblyBase.getSurfaceSections.surface (Python parameter) — A string specifying the Surface name.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L718-L734)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getSurfaceSections "Permalink to this definition")
    :   This method returns a list of the sections assigned to the regions encompassed by the specified
        surface.

        Note

        Check [AssemblyBase.getSurfaceSections on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblygetsurfacesectionspyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getSurfaceSections-parameters "Permalink to this headline")
        :   surface[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getSurfaceSections.surface "Permalink to this definition")
            :   A string specifying the Surface name.

        Returns:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getSurfaceSections-returns "Permalink to this headline")
        :   A tuple of strings representing the section names. If no section names are found, the
            tuple will contain one empty string.

        Return type:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.getSurfaceSections-return-type "Permalink to this headline")
        :   `Sequence[str]`

    importCatiaV5File(*[filename](#abaqus.Assembly.AssemblyBase.AssemblyBase.importCatiaV5File.filename "abaqus.Assembly.AssemblyBase.AssemblyBase.importCatiaV5File.filename (Python parameter) — A String specifying the path to the CATIA V5 Elysium Neutral file from which to import the assembly.")*, *[ids](#abaqus.Assembly.AssemblyBase.AssemblyBase.importCatiaV5File.ids "abaqus.Assembly.AssemblyBase.AssemblyBase.importCatiaV5File.ids (Python parameter) — A sequence of Ints.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L768-L783)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.importCatiaV5File "Permalink to this definition")
    :   This method imports an assembly from a CATIA V5 Elysium Neutral file into the root assembly.

        Note

        Check [AssemblyBase.importCatiaV5File on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblyimportcatiav5filepyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.importCatiaV5File-parameters "Permalink to this headline")
        :   filename[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.importCatiaV5File.filename "Permalink to this definition")
            :   A String specifying the path to the CATIA V5 Elysium Neutral file from which to import
                the assembly.

            ids=`()`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.importCatiaV5File.ids "Permalink to this definition")
            :   A sequence of Ints. Each Int in the sequence is a unique identifier of the occurrence in
                the assembly tree or component identifier associated with the part in the EAF file. If
                **ids** is an empty sequence, all occurrences or parts will be imported. The default value
                is an empty sequence.

    importEafFile(*[filename](#abaqus.Assembly.AssemblyBase.AssemblyBase.importEafFile.filename "abaqus.Assembly.AssemblyBase.AssemblyBase.importEafFile.filename (Python parameter) — A String specifying the path to the EAF file from which to import the assembly.")*, *[ids](#abaqus.Assembly.AssemblyBase.AssemblyBase.importEafFile.ids "abaqus.Assembly.AssemblyBase.AssemblyBase.importEafFile.ids (Python parameter) — A sequence of Ints.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L736-L750)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.importEafFile "Permalink to this definition")
    :   This method imports an assembly from an EAF file into the root assembly.

        Note

        Check [AssemblyBase.importEafFile on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblyimporteaffilepyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.importEafFile-parameters "Permalink to this headline")
        :   filename[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.importEafFile.filename "Permalink to this definition")
            :   A String specifying the path to the EAF file from which to import the assembly.

            ids=`()`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.importEafFile.ids "Permalink to this definition")
            :   A sequence of Ints. Each Int in the sequence is a unique identifier of the occurrence in
                the assembly tree or component identifier associated with the part in the EAF file. If
                **ids** is an empty sequence, all occurrences or parts will be imported. The default value
                is an empty sequence.

    importEnfFile(*[filename](#abaqus.Assembly.AssemblyBase.AssemblyBase.importEnfFile.filename "abaqus.Assembly.AssemblyBase.AssemblyBase.importEnfFile.filename (Python parameter) — A String specifying the path to the Elysium Neutral file from which to import the assembly.")*, *[ids](#abaqus.Assembly.AssemblyBase.AssemblyBase.importEnfFile.ids "abaqus.Assembly.AssemblyBase.AssemblyBase.importEnfFile.ids (Python parameter) — A sequence of Ints.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L785-L801)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.importEnfFile "Permalink to this definition")
    :   This method imports an assembly from an Elysium Neutral file created by Pro/ENGINEER, I-DEAS, or
        CATIA V5 into the root assembly.

        Note

        Check [AssemblyBase.importEnfFile on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblyimportenffilepyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.importEnfFile-parameters "Permalink to this headline")
        :   filename[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.importEnfFile.filename "Permalink to this definition")
            :   A String specifying the path to the Elysium Neutral file from which to import the
                assembly.

            ids=`()`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.importEnfFile.ids "Permalink to this definition")
            :   A sequence of Ints. Each Int in the sequence is a unique identifier of the occurrence in
                the assembly tree or component identifier associated with the part in the EAF file. If
                **ids** is an empty sequence, all occurrences or parts will be imported. The default value
                is an empty sequence.

    importIdeasFile(*[filename](#abaqus.Assembly.AssemblyBase.AssemblyBase.importIdeasFile.filename "abaqus.Assembly.AssemblyBase.AssemblyBase.importIdeasFile.filename (Python parameter) — A String specifying the path to the I-DEAS Elysium Neutral file from which to import the assembly.")*, *[ids](#abaqus.Assembly.AssemblyBase.AssemblyBase.importIdeasFile.ids "abaqus.Assembly.AssemblyBase.AssemblyBase.importIdeasFile.ids (Python parameter) — A sequence of Ints.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L803-L818)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.importIdeasFile "Permalink to this definition")
    :   This method imports an assembly from an I-DEAS Elysium Neutral file into the root assembly.

        Note

        Check [AssemblyBase.importIdeasFile on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblyimportideasfilepyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.importIdeasFile-parameters "Permalink to this headline")
        :   filename[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.importIdeasFile.filename "Permalink to this definition")
            :   A String specifying the path to the I-DEAS Elysium Neutral file from which to import the
                assembly.

            ids=`()`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.importIdeasFile.ids "Permalink to this definition")
            :   A sequence of Ints. Each Int in the sequence is a unique identifier of the occurrence in
                the assembly tree or component identifier associated with the part in the EAF file. If
                **ids** is an empty sequence, all occurrences or parts will be imported. The default value
                is an empty sequence.

    importParasolidFile(*[filename](#abaqus.Assembly.AssemblyBase.AssemblyBase.importParasolidFile.filename "abaqus.Assembly.AssemblyBase.AssemblyBase.importParasolidFile.filename (Python parameter) — A String specifying the path to a Parasolid file from which to import the assembly.")*, *[ids](#abaqus.Assembly.AssemblyBase.AssemblyBase.importParasolidFile.ids "abaqus.Assembly.AssemblyBase.AssemblyBase.importParasolidFile.ids (Python parameter) — A sequence of Ints.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L752-L766)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.importParasolidFile "Permalink to this definition")
    :   This method imports an assembly from the Parasolid file into the root assembly.

        Note

        Check [AssemblyBase.importParasolidFile on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblyimportparasolidfilepyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.importParasolidFile-parameters "Permalink to this headline")
        :   filename[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.importParasolidFile.filename "Permalink to this definition")
            :   A String specifying the path to a Parasolid file from which to import the assembly.

            ids=`()`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.importParasolidFile.ids "Permalink to this definition")
            :   A sequence of Ints. Each Int in the sequence is a unique identifier of the occurrence in
                the assembly tree or component identifier associated with the part in the EAF file. If
                **ids** is an empty sequence, all occurrences or parts will be imported. The default value
                is an empty sequence.

    importProEFile(*[filename](#abaqus.Assembly.AssemblyBase.AssemblyBase.importProEFile.filename "abaqus.Assembly.AssemblyBase.AssemblyBase.importProEFile.filename (Python parameter) — A String specifying the path to the Pro/ENGINEER Elysium Neutral file from which to import the assembly.")*, *[ids](#abaqus.Assembly.AssemblyBase.AssemblyBase.importProEFile.ids "abaqus.Assembly.AssemblyBase.AssemblyBase.importProEFile.ids (Python parameter) — A sequence of Ints.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L820-L835)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.importProEFile "Permalink to this definition")
    :   This method imports an assembly from a Pro/ENGINEER Elysium Neutral file into the root assembly.

        Note

        Check [AssemblyBase.importProEFile on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblyimportproefilepyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.importProEFile-parameters "Permalink to this headline")
        :   filename[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.importProEFile.filename "Permalink to this definition")
            :   A String specifying the path to the Pro/ENGINEER Elysium Neutral file from which to
                import the assembly.

            ids=`()`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.importProEFile.ids "Permalink to this definition")
            :   A sequence of Ints. Each Int in the sequence is a unique identifier of the occurrence in
                the assembly tree or component identifier associated with the part in the EAF file. If
                **ids** is an empty sequence, all occurrences or parts will be imported. The default value
                is an empty sequence.

    instances : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Assembly.PartInstance.PartInstance`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L93-L94)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.instances "Permalink to this definition")
    :   A repository of PartInstance objects.

    isLocked : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L68-L69)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.isLocked "Permalink to this definition")
    :   An Int specifying whether the assembly is locked or not. Possible values are 0 and 1.

    isOutOfDate : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L61-L63)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.isOutOfDate "Permalink to this definition")
    :   An Int specifying that feature parameters have been modified but that the assembly has
        not been regenerated. Possible values are 0 and 1.

    lock()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L1079-L1086)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.lock "Permalink to this definition")
    :   This method locks the assembly.

        Locking the assembly prevents any further changes to the assembly that can trigger regeneration of
        the assembly.

    makeDependent(*[instances](#abaqus.Assembly.AssemblyBase.AssemblyBase.makeDependent.instances "abaqus.Assembly.AssemblyBase.AssemblyBase.makeDependent.instances (Python parameter) — A sequence of PartInstance objects to convert to dependent part instances.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L837-L846)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.makeDependent "Permalink to this definition")
    :   This method converts the specified part instances from independent to dependent part instances.

        Note

        Check [AssemblyBase.makeDependent on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblymakedependentpyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.makeDependent-parameters "Permalink to this headline")
        :   instances[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.makeDependent.instances "Permalink to this definition")
            :   A sequence of PartInstance objects to convert to dependent part instances.

    makeIndependent(*[instances](#abaqus.Assembly.AssemblyBase.AssemblyBase.makeIndependent.instances "abaqus.Assembly.AssemblyBase.AssemblyBase.makeIndependent.instances (Python parameter) — A sequence of PartInstance objects to convert to independent part instances.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L848-L857)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.makeIndependent "Permalink to this definition")
    :   This method converts the specified part instances from dependent to independent part instances.

        Note

        Check [AssemblyBase.makeIndependent on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblymakeindependentpyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.makeIndependent-parameters "Permalink to this headline")
        :   instances[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.makeIndependent.instances "Permalink to this definition")
            :   A sequence of PartInstance objects to convert to independent part instances.

    modelInstances : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Assembly.ModelInstance.ModelInstance`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L139-L140)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.modelInstances "Permalink to this definition")
    :   A repository of ModelInstance objects.

    modelName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L149-L150)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.modelName "Permalink to this definition")
    :   A String specifying the name of the model to which the assembly belongs.

    nodes : --is-rst--:py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L89-L91)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.nodes "Permalink to this definition")
    :   A MeshNodeArray object specifying all the nodes existing at the assembly level. This
        member does not provide access to the nodes at the instance level.

    printAssignedSections()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L859-L862)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.printAssignedSections "Permalink to this definition")
    :   This method prints a summary of assigned connector sections.

    printConnectorOrientations()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L864-L867)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.printConnectorOrientations "Permalink to this definition")
    :   This method prints a summary of connector orientations.

    projectReferencesOntoSketch(*[sketch](#abaqus.Assembly.AssemblyBase.AssemblyBase.projectReferencesOntoSketch.sketch "abaqus.Assembly.AssemblyBase.AssemblyBase.projectReferencesOntoSketch.sketch (Python parameter) — The ConstrainedSketch object on which the edges, vertices, and datum points are projected.")*, *[filter](#abaqus.Assembly.AssemblyBase.AssemblyBase.projectReferencesOntoSketch.filter "abaqus.Assembly.AssemblyBase.AssemblyBase.projectReferencesOntoSketch.filter (Python parameter) — A SymbolicConstant specifying how to limit the amount of projection.")=`abaqusConstants.ALL_EDGES`*, *[upToFeature](#abaqus.Assembly.AssemblyBase.AssemblyBase.projectReferencesOntoSketch.upToFeature "abaqus.Assembly.AssemblyBase.AssemblyBase.projectReferencesOntoSketch.upToFeature (Python parameter) — A Feature object specifying a marker in the feature-based history of the part. Abaqus/CAE projects onto the sketch only the part entities that were created before the feature specified by this marker.")=`None`*, *[edges](#abaqus.Assembly.AssemblyBase.AssemblyBase.projectReferencesOntoSketch.edges "abaqus.Assembly.AssemblyBase.AssemblyBase.projectReferencesOntoSketch.edges (Python parameter) — A sequence of candidate edges to be projected onto the sketch.")=`()`*, *[vertices](#abaqus.Assembly.AssemblyBase.AssemblyBase.projectReferencesOntoSketch.vertices "abaqus.Assembly.AssemblyBase.AssemblyBase.projectReferencesOntoSketch.vertices (Python parameter) — A sequence of candidate vertices to be projected onto the sketch.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L869-L903)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.projectReferencesOntoSketch "Permalink to this definition")
    :   This method projects the specified edges, vertices, and datum points from the assembly onto the
        specified ConstrainedSketch object. The edges, vertices, and datum points appear on the sketch as
        reference geometry.

        Note

        Check [AssemblyBase.projectReferencesOntoSketch on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblyprojectreferencesontosketchpyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.projectReferencesOntoSketch-parameters "Permalink to this headline")
        :   sketch[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.projectReferencesOntoSketch.sketch "Permalink to this definition")
            :   The ConstrainedSketch object on which the edges, vertices, and datum points are
                projected.

            filter=`abaqusConstants.ALL_EDGES`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.projectReferencesOntoSketch.filter "Permalink to this definition")
            :   A SymbolicConstant specifying how to limit the amount of projection. Possible values are
                ALL\_EDGES and COPLANAR\_EDGES. If **filter** = COPLANAR\_EDGES, edges that are coplanar to the
                sketching plane are the only candidates for projection. The default value is ALL\_EDGES.

            upToFeature=`None`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.projectReferencesOntoSketch.upToFeature "Permalink to this definition")
            :   A Feature object specifying a marker in the feature-based history of the part.
                Abaqus/CAE projects onto the sketch only the part entities that were created before the
                feature specified by this marker. By default, all part entities are candidates for
                projection.

            edges=`()`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.projectReferencesOntoSketch.edges "Permalink to this definition")
            :   A sequence of candidate edges to be projected onto the sketch. By default, all edges are
                candidates for projection.

            vertices=`()`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.projectReferencesOntoSketch.vertices "Permalink to this definition")
            :   A sequence of candidate vertices to be projected onto the sketch. By default, all
                vertices are candidates for projection.

    queryCachedStates()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L905-L912)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.queryCachedStates "Permalink to this definition")
    :   This method displays the position of geometric states relative to the sequence of features in the
        assembly cache.

        The output is displayed in the message area.

    referencePoints : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.BasicGeometry.ReferencePoint.ReferencePoint`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L136-L137)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.referencePoints "Permalink to this definition")
    :   A repository of ReferencePoint objects.

    regenerate()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L914-L924)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.regenerate "Permalink to this definition")
    :   This method regenerates the assembly and brings it up to date with the latest values of the assembly
        parameters.

        When you modify features of an assembly, it may be convenient to postpone regeneration until you
        make all your changes, since regeneration can be time consuming. In contrast, when you modify
        features of a part that is included in the assembly, you should use this command to regenerate the
        assembly. When you regenerate the assembly, it will reflect the changes that you made to the part.

    regenerateConstraintsTogether : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L71-L75)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.regenerateConstraintsTogether "Permalink to this definition")
    :   A Boolean specifying whether the positioning constraints in the assembly should be
        regenerated together before regenerating other assembly features. The default value is
        ON.If the assembly has position constraint features and you modify the value of
        **regenerateConstraintsTogether**, Abaqus/CAE will regenerate the assembly features.

    regenerationWarnings()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L926-L929)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.regenerationWarnings "Permalink to this definition")
    :   This method prints any regeneration warnings associated with the features.

    restore()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L931-L938)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.restore "Permalink to this definition")
    :   This method restores the parameters of all features in the assembly to the value they had before a
        failed regeneration.

        Use the restore method after a failed regeneration, followed by a regenerate command.

    resumeAllFeatures()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L940-L943)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.resumeAllFeatures "Permalink to this definition")
    :   This method resumes all the suppressed features in the part or assembly.

    resumeFeatures(*[featureNames](#abaqus.Assembly.AssemblyBase.AssemblyBase.resumeFeatures.featureNames "abaqus.Assembly.AssemblyBase.AssemblyBase.resumeFeatures.featureNames (Python parameter) — A sequence of Strings specifying the names of features to resume.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L945-L954)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.resumeFeatures "Permalink to this definition")
    :   This method resumes the specified suppressed features in the assembly.

        Note

        Check [AssemblyBase.resumeFeatures on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblyresumefeaturespyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.resumeFeatures-parameters "Permalink to this headline")
        :   featureNames[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.resumeFeatures.featureNames "Permalink to this definition")
            :   A sequence of Strings specifying the names of features to resume.

    resumeLastSetFeatures()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L956-L959)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.resumeLastSetFeatures "Permalink to this definition")
    :   This method resumes the last set of features to be suppressed in the assembly.

    rotate(*[instanceList](#abaqus.Assembly.AssemblyBase.AssemblyBase.rotate.instanceList "abaqus.Assembly.AssemblyBase.AssemblyBase.rotate.instanceList (Python parameter) — A sequence of Strings specifying the names of instances to rotate.")*, *[axisPoint](#abaqus.Assembly.AssemblyBase.AssemblyBase.rotate.axisPoint "abaqus.Assembly.AssemblyBase.AssemblyBase.rotate.axisPoint (Python parameter) — A sequence of three Floats specifying the coordinates of a point on the axis.")*, *[axisDirection](#abaqus.Assembly.AssemblyBase.AssemblyBase.rotate.axisDirection "abaqus.Assembly.AssemblyBase.AssemblyBase.rotate.axisDirection (Python parameter) — A sequence of three Floats specifying the direction of the axis.")*, *[angle](#abaqus.Assembly.AssemblyBase.AssemblyBase.rotate.angle "abaqus.Assembly.AssemblyBase.AssemblyBase.rotate.angle (Python parameter) — A Float specifying the rotation angle in degrees.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L961-L983)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.rotate "Permalink to this definition")
    :   This method rotates given instances by the specified amount.

        Note

        Check [AssemblyBase.rotate on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblyrotatepyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.rotate-parameters "Permalink to this headline")
        :   instanceList[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.rotate.instanceList "Permalink to this definition")
            :   A sequence of Strings specifying the names of instances to rotate.

            axisPoint[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.rotate.axisPoint "Permalink to this definition")
            :   A sequence of three Floats specifying the coordinates of a point on the axis.

            axisDirection[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.rotate.axisDirection "Permalink to this definition")
            :   A sequence of three Floats specifying the direction of the axis.

            angle[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.rotate.angle "Permalink to this definition")
            :   A Float specifying the rotation angle in degrees. Use the right-hand rule to determine
                the direction.

    saveGeometryCache()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L998-L1001)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.saveGeometryCache "Permalink to this definition")
    :   This method caches the current geometry, which improves regeneration performance.

    sectionAssignments : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Property.SectionAssignment.SectionAssignment`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L155-L156)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.sectionAssignments "Permalink to this definition")
    :   A SectionAssignmentArray object.

    setMeshNumberingControl(*[instances](#abaqus.Assembly.AssemblyBase.AssemblyBase.setMeshNumberingControl.instances "abaqus.Assembly.AssemblyBase.AssemblyBase.setMeshNumberingControl.instances (Python parameter) — A sequence of PartInstance objects to change the start node and/or element labels.")*, *[startNodeLabel](#abaqus.Assembly.AssemblyBase.AssemblyBase.setMeshNumberingControl.startNodeLabel "abaqus.Assembly.AssemblyBase.AssemblyBase.setMeshNumberingControl.startNodeLabel (Python parameter) — A positive Integer specifying the new start node label.")=`None`*, *[startElemLabel](#abaqus.Assembly.AssemblyBase.AssemblyBase.setMeshNumberingControl.startElemLabel "abaqus.Assembly.AssemblyBase.AssemblyBase.setMeshNumberingControl.startElemLabel (Python parameter) — A positive Integer specifying the new start element label.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L1096-L1116)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.setMeshNumberingControl "Permalink to this definition")
    :   This method changes the start node and/or element labels on the specified independent part instances
        before or after Abaqus/CAE generates the meshes. For the meshed instances, Abaqus/CAE changes the node
        and/or element labels while preserving the original order and incrementation.

        Note

        Check [AssemblyBase.setMeshNumberingControl on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblysetmeshnumberingcontrolpyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.setMeshNumberingControl-parameters "Permalink to this headline")
        :   instances[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.setMeshNumberingControl.instances "Permalink to this definition")
            :   A sequence of PartInstance objects to change the start node and/or element labels.

            startNodeLabel=`None`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.setMeshNumberingControl.startNodeLabel "Permalink to this definition")
            :   A positive Integer specifying the new start node label.

            startElemLabel=`None`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.setMeshNumberingControl.startElemLabel "Permalink to this definition")
            :   A positive Integer specifying the new start element label.

    setValues(*[regenerateConstraintsTogether](#abaqus.Assembly.AssemblyBase.AssemblyBase.setValues.regenerateConstraintsTogether "abaqus.Assembly.AssemblyBase.AssemblyBase.setValues.regenerateConstraintsTogether (Python parameter) — A Boolean specifying whether the positioning constraints in the assembly should be regenerated together before regenerating other assembly features.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L1003-L1020)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.setValues "Permalink to this definition")
    :   This method modifies the behavior associated with the specified assembly.

        Note

        Check [AssemblyBase.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblysetvaluespyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.setValues-parameters "Permalink to this headline")
        :   regenerateConstraintsTogether[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.setValues.regenerateConstraintsTogether "Permalink to this definition")
            :   A Boolean specifying whether the positioning constraints in the assembly should be
                regenerated together before regenerating other assembly features. The default value is
                ON.If the assembly has position constraint features and you modify the value of
                **regenerateConstraintsTogether**, Abaqus/CAE will regenerate the assembly features.

        Raises:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.setValues-raises "Permalink to this headline")
        :   **FeatureError** – Regeneration failed, If one or more features in the assembly fails to regenerate

    sets : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Region.Set.Set`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L120-L121)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.sets "Permalink to this definition")
    :   A repository of Set objects.

    skins : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Region.Skin.Skin`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L130-L131)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.skins "Permalink to this definition")
    :   A repository of Skin objects specifying the skins created on the assembly.

    smoothNodes(*[nodes](#abaqus.Assembly.AssemblyBase.AssemblyBase.smoothNodes.nodes "abaqus.Assembly.AssemblyBase.AssemblyBase.smoothNodes.nodes (Python parameter) — A sequence of MeshNode objects or a Set object containing nodes.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L1157-L1170)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.smoothNodes "Permalink to this definition")
    :   This method smooths the given nodes of a native mesh, moving them locally to a more optimal location
        that improves the quality of the mesh.

        Note

        Check [AssemblyBase.smoothNodes on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblysmoothnodespyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.smoothNodes-parameters "Permalink to this headline")
        :   nodes=`()`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.smoothNodes.nodes "Permalink to this definition")
            :   A sequence of MeshNode objects or a Set object containing nodes.

                Changed in version 2020: The `coordinates` arguments was removed, the `nodes` now replaces it.

    stringers : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Region.Stringer.Stringer`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L133-L134)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.stringers "Permalink to this definition")
    :   A repository of Stringer objects specifying the stringers created on the assembly.

    suppressFeatures(*[featureNames](#abaqus.Assembly.AssemblyBase.AssemblyBase.suppressFeatures.featureNames "abaqus.Assembly.AssemblyBase.AssemblyBase.suppressFeatures.featureNames (Python parameter) — A sequence of Strings specifying the names of features to suppress in the assembly.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L1022-L1031)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.suppressFeatures "Permalink to this definition")
    :   This method suppresses specified features.

        Note

        Check [AssemblyBase.suppressFeatures on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblysuppressfeaturespyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.suppressFeatures-parameters "Permalink to this headline")
        :   featureNames[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.suppressFeatures.featureNames "Permalink to this definition")
            :   A sequence of Strings specifying the names of features to suppress in the assembly.

    surfaces : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Region.Surface.Surface`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L109-L111)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.surfaces "Permalink to this definition")
    :   A repository of Surface objects specifying for more information, see [Region
        commands](<https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all>).

    timeStamp : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L65-L66)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.timeStamp "Permalink to this definition")
    :   A Float specifying which gives an indication when the assembly was last modified.

    translate(*[instanceList](#abaqus.Assembly.AssemblyBase.AssemblyBase.translate.instanceList "abaqus.Assembly.AssemblyBase.AssemblyBase.translate.instanceList (Python parameter) — A sequence of Strings specifying the names of instances to translate.")*, *[vector](#abaqus.Assembly.AssemblyBase.AssemblyBase.translate.vector "abaqus.Assembly.AssemblyBase.AssemblyBase.translate.vector (Python parameter) — A sequence of three Floats specifying a translation vector.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L985-L996)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.translate "Permalink to this definition")
    :   This method translates given instances by the specified amount.

        Note

        Check [AssemblyBase.translate on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblytranslatepyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.translate-parameters "Permalink to this headline")
        :   instanceList[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.translate.instanceList "Permalink to this definition")
            :   A sequence of Strings specifying the names of instances to translate.

            vector[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.translate.vector "Permalink to this definition")
            :   A sequence of three Floats specifying a translation vector.

    unlinkInstances(*[instances](#abaqus.Assembly.AssemblyBase.AssemblyBase.unlinkInstances.instances "abaqus.Assembly.AssemblyBase.AssemblyBase.unlinkInstances.instances (Python parameter) — A sequence of PartInstance objects to be converted to regular part instances.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L1033-L1043)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.unlinkInstances "Permalink to this definition")
    :   This method converts the specified PartInstance objects from linked child instances to regular
        instances. The parts associated with the selected instances will be converted to regular parts as well.

        Note

        Check [AssemblyBase.unlinkInstances on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblyunlinkinstancespyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.unlinkInstances-parameters "Permalink to this headline")
        :   instances[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.unlinkInstances.instances "Permalink to this definition")
            :   A sequence of PartInstance objects to be converted to regular part instances.

    unlock()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L1088-L1094)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.unlock "Permalink to this definition")
    :   This method unlocks the assembly.

        Unlocking the assembly allows it to be regenerated after any modifications to the assembly.

    vertices : --is-rst--:py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L77-L79)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.vertices "Permalink to this definition")
    :   A VertexArray object specifying all the vertices existing at the assembly level. This
        member does not provide access to the vertices at the instance level.

    writeAcisFile(*[fileName](#abaqus.Assembly.AssemblyBase.AssemblyBase.writeAcisFile.fileName "abaqus.Assembly.AssemblyBase.AssemblyBase.writeAcisFile.fileName (Python parameter) — A String specifying the name of the file to which to write.")*, *[version](#abaqus.Assembly.AssemblyBase.AssemblyBase.writeAcisFile.version "abaqus.Assembly.AssemblyBase.AssemblyBase.writeAcisFile.version (Python parameter) — A Float specifying the ACIS version.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L1045-L1059)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.writeAcisFile "Permalink to this definition")
    :   This method exports the assembly to a named file in ACIS part (SAT) or assembly (ASAT) format.

        Note

        Check [AssemblyBase.writeAcisFile on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblywriteacisfilepyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.writeAcisFile-parameters "Permalink to this headline")
        :   fileName[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.writeAcisFile.fileName "Permalink to this definition")
            :   A String specifying the name of the file to which to write. The file name’s extension is
                used to determine whether a part or assembly is written. Use the file extension .asat
                for the assembly format.

            version=`None`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.writeAcisFile.version "Permalink to this definition")
            :   A Float specifying the ACIS version. For example, the Float 12.0 corresponds to ACIS
                Version 12.0. The default value is the current version of ACIS.

    writeCADParameters(*[paramFile](#abaqus.Assembly.AssemblyBase.AssemblyBase.writeCADParameters.paramFile "abaqus.Assembly.AssemblyBase.AssemblyBase.writeCADParameters.paramFile (Python parameter) — A String specifying the parameter file name.")*, *[modifiedParams](#abaqus.Assembly.AssemblyBase.AssemblyBase.writeCADParameters.modifiedParams "abaqus.Assembly.AssemblyBase.AssemblyBase.writeCADParameters.modifiedParams (Python parameter) — A tuple of tuples each containing the part name, the parameter name and the modified parameter value.")=`()`*, *[updatePaths](#abaqus.Assembly.AssemblyBase.AssemblyBase.writeCADParameters.updatePaths "abaqus.Assembly.AssemblyBase.AssemblyBase.writeCADParameters.updatePaths (Python parameter) — A Bool specifying whether to update the path of the CAD model file specified in the parameterFile to the current directory, if the CAD model is present in the current directory.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyBase.py#L1061-L1077)[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.writeCADParameters "Permalink to this definition")
    :   This method writes the parameters that were imported from the CAD system to a parameter file.

        Note

        Check [AssemblyBase.writeCADParameters on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblywritecadparameterspyc).

        Parameters:[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.writeCADParameters-parameters "Permalink to this headline")
        :   paramFile[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.writeCADParameters.paramFile "Permalink to this definition")
            :   A String specifying the parameter file name.

            modifiedParams=`()`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.writeCADParameters.modifiedParams "Permalink to this definition")
            :   A tuple of tuples each containing the part name, the parameter name and the modified
                parameter value. Default is an empty tuple.

            updatePaths=`''`[¶](#abaqus.Assembly.AssemblyBase.AssemblyBase.writeCADParameters.updatePaths "Permalink to this definition")
            :   A Bool specifying whether to update the path of the CAD model file specified in the
                **parameterFile** to the current directory, if the CAD model is present in the current
                directory.

*class* AssemblyFeature[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyFeature.py#L19-L338)[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature "Permalink to this definition")
:   Bases: [`Feature`](feature.html#abaqus.Feature.Feature.Feature "abaqus.Feature.Feature.Feature (Python class) — Bases: object")

    The following commands operate on Feature objects. For more information about the Feature object, see
    Feature object.

    Note

    This object can be accessed by:

    ```python
    import assembly
    ```

    Note

    Check [AssemblyFeature on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblyfeaturepyc.htm?contextscope=all).

    Member Details:

    *static* AttachmentLines(*[name](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.name "abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.name (Python parameter) — A String specifying a unique Feature name.")*, *[points](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.points "abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.points (Python parameter) — A tuple of points.")*, *[sourceFaces](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.sourceFaces "abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.sourceFaces (Python parameter) — A sequence of Face objects specifying the geometry faces onto which the points are to be projected.")*, *[sourceElementFaces](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.sourceElementFaces "abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.sourceElementFaces (Python parameter) — A sequence of MeshFace objects specifying the orphan mesh element faces onto which the points are to be projected.")*, *[targetFaces](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.targetFaces "abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.targetFaces (Python parameter) — A sequence of Face objects specifying the geometry faces on which the attachment lines will terminate.")*, *[targetElementFaces](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.targetElementFaces "abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.targetElementFaces (Python parameter) — A sequence of MeshFace objects specifying the orphan mesh element faces on which the attachment lines will terminate.")*, *[projectionMethod](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.projectionMethod "abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.projectionMethod (Python parameter) — A SymbolicConstant specifying the method to be used to project onto source faces. Possible values are PROJECT_BY_PROXIMITY and PROJECT_BY_DIRECTION.")=`abaqusConstants.PROJECT_BY_PROXIMITY`*, *[projectionDirStartPt](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.projectionDirStartPt "abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.projectionDirStartPt (Python parameter) — A point specifying the start point of the projection direction to project onto source faces.")=`None`*, *[projectionDirEndPt](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.projectionDirEndPt "abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.projectionDirEndPt (Python parameter) — A point specifying the end point of the projection direction to project onto source faces.")=`None`*, *[sourceToTargetProjMethod](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.sourceToTargetProjMethod "abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.sourceToTargetProjMethod (Python parameter) — A SymbolicConstant specifying the method to be used to project onto target faces. Possible values are PROJECT_BY_NUMBER and PROJECT_BY_DISTANCE.")=`abaqusConstants.PROJECT_BY_NUMBER`*, *[numProjections](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.numProjections "abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.numProjections (Python parameter) — An integer specifying the maximum number of layers each point should be projected onto when the source to target projection method is PROJECT_BY_NUMBER.")=`''`*, *[projectionDistance](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.projectionDistance "abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.projectionDistance (Python parameter) — A float specifying the maximum distance of the projection vector when the source to target projection method is PROJECT_BY_DISTANCE.")=`''`*, *[flipSourceToTargetDirection](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.flipSourceToTargetDirection "abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.flipSourceToTargetDirection (Python parameter) — A Boolean specifying whether the computed projection direction from the source to the target faces should be flipped.")=`0`*, *[setName](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.setName "abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.setName (Python parameter) — A String specifying a unique set name.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyFeature.py#L30-L114)[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines "Permalink to this definition")
    :   This method creates a Feature object by creating attachment lines between the given set of source and
        target faces. The given points are first projected onto the source faces using the specified projection
        method. The points are then projected normal to the source faces onto the target faces. The user can
        specify the number of projections or the length of projection vector for projection onto the target
        faces. The lines are then created between the source face and the closest target face. Subsequent lines
        are created between the target faces.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].rootAssembly.AttachmentLines
        ```

        Note

        Check [AttachmentLines on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-attachmentlinespyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.name "Permalink to this definition")
            :   A String specifying a unique Feature name.

            points[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.points "Permalink to this definition")
            :   A tuple of points. Each point can be a ConstrainedSketchVertex, Datum point, Reference point, an
                Attachment point, orphan mesh Node, or an Interesting point object.

            sourceFaces[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.sourceFaces "Permalink to this definition")
            :   A sequence of Face objects specifying the geometry faces onto which the points are to be
                projected.

            sourceElementFaces[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.sourceElementFaces "Permalink to this definition")
            :   A sequence of MeshFace objects specifying the orphan mesh element faces onto which the
                points are to be projected.

            targetFaces[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.targetFaces "Permalink to this definition")
            :   A sequence of Face objects specifying the geometry faces on which the attachment lines
                will terminate.

            targetElementFaces[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.targetElementFaces "Permalink to this definition")
            :   A sequence of MeshFace objects specifying the orphan mesh element faces on which the
                attachment lines will terminate.

            projectionMethod=`abaqusConstants.PROJECT_BY_PROXIMITY`[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.projectionMethod "Permalink to this definition")
            :   A SymbolicConstant specifying the method to be used to project onto source faces.
                Possible values are PROJECT\_BY\_PROXIMITY and PROJECT\_BY\_DIRECTION. The default value is
                PROJECT\_BY\_PROXIMITY.

            projectionDirStartPt=`None`[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.projectionDirStartPt "Permalink to this definition")
            :   A point specifying the start point of the projection direction to project onto source
                faces. The point can be a ConstrainedSketchVertex, Datum point, Reference point, Attachment point, orphan
                mesh Node, Interesting Point object, or a tuple of Floats representing the coordinates
                of a point.

            projectionDirEndPt=`None`[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.projectionDirEndPt "Permalink to this definition")
            :   A point specifying the end point of the projection direction to project onto source
                faces. The point can be a ConstrainedSketchVertex, Datum point, Reference point, Attachment point, orphan
                mesh Node, Interesting point object, or a tuple of Floats representing the coordinates
                of a point.

            sourceToTargetProjMethod=`abaqusConstants.PROJECT_BY_NUMBER`[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.sourceToTargetProjMethod "Permalink to this definition")
            :   A SymbolicConstant specifying the method to be used to project onto target faces.
                Possible values are PROJECT\_BY\_NUMBER and PROJECT\_BY\_DISTANCE. The default value is
                PROJECT\_BY\_NUMBER.

            numProjections=`''`[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.numProjections "Permalink to this definition")
            :   An integer specifying the maximum number of layers each point should be projected onto
                when the source to target projection method is PROJECT\_BY\_NUMBER.

            projectionDistance=`''`[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.projectionDistance "Permalink to this definition")
            :   A float specifying the maximum distance of the projection vector when the source to
                target projection method is PROJECT\_BY\_DISTANCE.

            flipSourceToTargetDirection=`0`[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.flipSourceToTargetDirection "Permalink to this definition")
            :   A Boolean specifying whether the computed projection direction from the source to the
                target faces should be flipped.

            setName=`''`[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines.setName "Permalink to this definition")
            :   A String specifying a unique set name.

        Returns:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines-returns "Permalink to this headline")
        :   A Feature object.

        Return type:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.AttachmentLines-return-type "Permalink to this headline")
        :   [`AssemblyFeature`](#abaqus.Assembly.AssemblyFeature.AssemblyFeature "abaqus.Assembly.AssemblyFeature.AssemblyFeature (Python class) — Bases: Feature")

    *static* Coaxial(*[movableAxis](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.Coaxial.movableAxis "abaqus.Assembly.AssemblyFeature.AssemblyFeature.Coaxial.movableAxis (Python parameter) — A cylindrical or conical Face on the part instance to be moved.")*, *[fixedAxis](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.Coaxial.fixedAxis "abaqus.Assembly.AssemblyFeature.AssemblyFeature.Coaxial.fixedAxis (Python parameter) — A cylindrical or conical Face on the part instance that remains fixed.")*, *[flip](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.Coaxial.flip "abaqus.Assembly.AssemblyFeature.AssemblyFeature.Coaxial.flip (Python parameter) — A Boolean specifying whether the axes are forward aligned (OFF) or reverse aligned (ON).")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyFeature.py#L116-L145)[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.Coaxial "Permalink to this definition")
    :   This method moves an instance so that its selected face is coaxial with the selected face of a fixed
        instance.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].rootAssembly.AttachmentLines
        ```

        Note

        Check [Coaxial on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-coaxialpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.Coaxial-parameters "Permalink to this headline")
        :   movableAxis[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.Coaxial.movableAxis "Permalink to this definition")
            :   A cylindrical or conical Face on the part instance to be moved.

            fixedAxis[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.Coaxial.fixedAxis "Permalink to this definition")
            :   A cylindrical or conical Face on the part instance that remains fixed.

            flip[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.Coaxial.flip "Permalink to this definition")
            :   A Boolean specifying whether the axes are forward aligned (OFF) or reverse aligned (ON).

        Returns:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.Coaxial-returns "Permalink to this headline")
        :   A Feature object.

        Return type:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.Coaxial-return-type "Permalink to this headline")
        :   [`AssemblyFeature`](#abaqus.Assembly.AssemblyFeature.AssemblyFeature "abaqus.Assembly.AssemblyFeature.AssemblyFeature (Python class) — Bases: Feature")

        Raises:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.Coaxial-raises "Permalink to this headline")
        :   [**AbaqusException**](../../../kernel/utility.html#abaqus.UtilityAndView.AbaqusException.AbaqusException "abaqus.UtilityAndView.AbaqusException.AbaqusException (Python class) — Bases: Exception") –

    *static* CoincidentPoint(*[movablePoint](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.CoincidentPoint.movablePoint "abaqus.Assembly.AssemblyFeature.AssemblyFeature.CoincidentPoint.movablePoint (Python parameter) — A ConstrainedSketchVertex, a Datum point, or a ReferencePoint or a mesh node from an orphan mesh on the part instance to be moved.")*, *[fixedPoint](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.CoincidentPoint.fixedPoint "abaqus.Assembly.AssemblyFeature.AssemblyFeature.CoincidentPoint.fixedPoint (Python parameter) — A ConstrainedSketchVertex, a Datum point, or a ReferencePoint or a mesh node from an orphan mesh on the part instance to remain fixed.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyFeature.py#L147-L172)[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.CoincidentPoint "Permalink to this definition")
    :   This method moves an instance so that a specified point is coincident with a specified point of a
        fixed instance.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].rootAssembly.AttachmentLines
        ```

        Note

        Check [CoincidentPoint on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-coincidentpointpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.CoincidentPoint-parameters "Permalink to this headline")
        :   movablePoint[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.CoincidentPoint.movablePoint "Permalink to this definition")
            :   A ConstrainedSketchVertex, a Datum point, or a ReferencePoint or a mesh node from an orphan mesh on the
                part instance to be moved.

            fixedPoint[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.CoincidentPoint.fixedPoint "Permalink to this definition")
            :   A ConstrainedSketchVertex, a Datum point, or a ReferencePoint or a mesh node from an orphan mesh on the
                part instance to remain fixed.

        Returns:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.CoincidentPoint-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.CoincidentPoint-return-type "Permalink to this headline")
        :   [`AssemblyFeature`](#abaqus.Assembly.AssemblyFeature.AssemblyFeature "abaqus.Assembly.AssemblyFeature.AssemblyFeature (Python class) — Bases: Feature")

    *static* EdgeToEdge(*[movableAxis](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.EdgeToEdge.movableAxis "abaqus.Assembly.AssemblyFeature.AssemblyFeature.EdgeToEdge.movableAxis (Python parameter) — A straight Edge, a Datum axis, or an element edge from an orphan mesh on the part instance to be moved.")*, *[fixedAxis](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.EdgeToEdge.fixedAxis "abaqus.Assembly.AssemblyFeature.AssemblyFeature.EdgeToEdge.fixedAxis (Python parameter) — A straight Edge, a Datum axis, or an element edge from an orphan mesh on the part instance to remain fixed.")*, *[flip](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.EdgeToEdge.flip "abaqus.Assembly.AssemblyFeature.AssemblyFeature.EdgeToEdge.flip (Python parameter) — A Boolean specifying whether the edges are forward aligned (OFF) or reverse aligned (ON).")*, *[clearance](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.EdgeToEdge.clearance "abaqus.Assembly.AssemblyFeature.AssemblyFeature.EdgeToEdge.clearance (Python parameter) — A Float specifying the distance between the two edges (for two-dimensional and axisymmetric instances only).")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyFeature.py#L174-L208)[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.EdgeToEdge "Permalink to this definition")
    :   This method moves an instance so that its edge is parallel to an edge of a fixed instance.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].rootAssembly.AttachmentLines
        ```

        Note

        Check [EdgeToEdge on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-edgetoedgepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.EdgeToEdge-parameters "Permalink to this headline")
        :   movableAxis[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.EdgeToEdge.movableAxis "Permalink to this definition")
            :   A straight Edge, a Datum axis, or an element edge from an orphan mesh on the part
                instance to be moved.

            fixedAxis[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.EdgeToEdge.fixedAxis "Permalink to this definition")
            :   A straight Edge, a Datum axis, or an element edge from an orphan mesh on the part
                instance to remain fixed.

            flip[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.EdgeToEdge.flip "Permalink to this definition")
            :   A Boolean specifying whether the edges are forward aligned (OFF) or reverse aligned
                (ON).

            clearance[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.EdgeToEdge.clearance "Permalink to this definition")
            :   A Float specifying the distance between the two edges (for two-dimensional and
                axisymmetric instances only).

        Returns:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.EdgeToEdge-returns "Permalink to this headline")
        :   A Feature Object.

        Return type:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.EdgeToEdge-return-type "Permalink to this headline")
        :   [`AssemblyFeature`](#abaqus.Assembly.AssemblyFeature.AssemblyFeature "abaqus.Assembly.AssemblyFeature.AssemblyFeature (Python class) — Bases: Feature")

        Raises:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.EdgeToEdge-raises "Permalink to this headline")
        :   [**AbaqusException**](../../../kernel/utility.html#abaqus.UtilityAndView.AbaqusException.AbaqusException "abaqus.UtilityAndView.AbaqusException.AbaqusException (Python class) — Bases: Exception") –

    *static* FaceToFace(*[movablePlane](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.FaceToFace.movablePlane "abaqus.Assembly.AssemblyFeature.AssemblyFeature.FaceToFace.movablePlane (Python parameter) — A planar face, a Datum plane, or a face from an orphan mesh on the part instance to be moved.")*, *[fixedPlane](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.FaceToFace.fixedPlane "abaqus.Assembly.AssemblyFeature.AssemblyFeature.FaceToFace.fixedPlane (Python parameter) — A planar face, a Datum plane, or a face from an orphan mesh on the part instance to remain fixed.")*, *[flip](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.FaceToFace.flip "abaqus.Assembly.AssemblyFeature.AssemblyFeature.FaceToFace.flip (Python parameter) — A Boolean specifying whether the normals to the faces are forward aligned (OFF) or reverse aligned (ON).")*, *[clearance](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.FaceToFace.clearance "abaqus.Assembly.AssemblyFeature.AssemblyFeature.FaceToFace.clearance (Python parameter) — A Float specifying the distance between the two faces.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyFeature.py#L210-L243)[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.FaceToFace "Permalink to this definition")
    :   This method moves an instance so that its face is coincident with a face of a fixed instance.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].rootAssembly.AttachmentLines
        ```

        Note

        Check [FaceToFace on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-facetofacepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.FaceToFace-parameters "Permalink to this headline")
        :   movablePlane[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.FaceToFace.movablePlane "Permalink to this definition")
            :   A planar face, a Datum plane, or a face from an orphan mesh on the part instance to be
                moved.

            fixedPlane[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.FaceToFace.fixedPlane "Permalink to this definition")
            :   A planar face, a Datum plane, or a face from an orphan mesh on the part instance to
                remain fixed.

            flip[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.FaceToFace.flip "Permalink to this definition")
            :   A Boolean specifying whether the normals to the faces are forward aligned (OFF) or
                reverse aligned (ON).

            clearance[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.FaceToFace.clearance "Permalink to this definition")
            :   A Float specifying the distance between the two faces.

        Returns:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.FaceToFace-returns "Permalink to this headline")
        :   A Feature Object.

        Return type:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.FaceToFace-return-type "Permalink to this headline")
        :   [`AssemblyFeature`](#abaqus.Assembly.AssemblyFeature.AssemblyFeature "abaqus.Assembly.AssemblyFeature.AssemblyFeature (Python class) — Bases: Feature")

        Raises:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.FaceToFace-raises "Permalink to this headline")
        :   [**AbaqusException**](../../../kernel/utility.html#abaqus.UtilityAndView.AbaqusException.AbaqusException "abaqus.UtilityAndView.AbaqusException.AbaqusException (Python class) — Bases: Exception") –

    *static* ParallelCsys(*[movableCsys](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelCsys.movableCsys "abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelCsys.movableCsys (Python parameter) — A Datum coordinate system on the part instance to be moved.")*, *[fixedCsys](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelCsys.fixedCsys "abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelCsys.fixedCsys (Python parameter) — A Datum coordinate system on the part instance to remain fixed.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyFeature.py#L245-L272)[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelCsys "Permalink to this definition")
    :   This method moves an instance so that its Datum coordinate system is parallel to a Datum coordinate
        system of a fixed instance.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].rootAssembly.AttachmentLines
        ```

        Note

        Check [ParallelCsys on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-parallelcsyspyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelCsys-parameters "Permalink to this headline")
        :   movableCsys[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelCsys.movableCsys "Permalink to this definition")
            :   A Datum coordinate system on the part instance to be moved.

            fixedCsys[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelCsys.fixedCsys "Permalink to this definition")
            :   A Datum coordinate system on the part instance to remain fixed.

        Returns:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelCsys-returns "Permalink to this headline")
        :   A Feature object.

        Return type:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelCsys-return-type "Permalink to this headline")
        :   [`AssemblyFeature`](#abaqus.Assembly.AssemblyFeature.AssemblyFeature "abaqus.Assembly.AssemblyFeature.AssemblyFeature (Python class) — Bases: Feature")

        Raises:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelCsys-raises "Permalink to this headline")
        :   [**AbaqusException**](../../../kernel/utility.html#abaqus.UtilityAndView.AbaqusException.AbaqusException "abaqus.UtilityAndView.AbaqusException.AbaqusException (Python class) — Bases: Exception") –

    *static* ParallelEdge(*[movableAxis](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelEdge.movableAxis "abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelEdge.movableAxis (Python parameter) — A straight Edge, a Datum axis, or an element edge from an orphan mesh on the part instance to be moved.")*, *[fixedAxis](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelEdge.fixedAxis "abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelEdge.fixedAxis (Python parameter) — A straight Edge, a Datum axis, or an element edge from an orphan mesh on the part instance to remain fixed.")*, *[flip](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelEdge.flip "abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelEdge.flip (Python parameter) — A Boolean specifying whether the edges are forward aligned (OFF) or reverse aligned (ON).")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyFeature.py#L274-L305)[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelEdge "Permalink to this definition")
    :   This method moves an instance so that its edge is parallel to an edge of a fixed instance.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].rootAssembly.AttachmentLines
        ```

        Note

        Check [ParallelEdge on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-paralleledgepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelEdge-parameters "Permalink to this headline")
        :   movableAxis[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelEdge.movableAxis "Permalink to this definition")
            :   A straight Edge, a Datum axis, or an element edge from an orphan mesh on the part
                instance to be moved.

            fixedAxis[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelEdge.fixedAxis "Permalink to this definition")
            :   A straight Edge, a Datum axis, or an element edge from an orphan mesh on the part
                instance to remain fixed.

            flip[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelEdge.flip "Permalink to this definition")
            :   A Boolean specifying whether the edges are forward aligned (OFF) or reverse aligned
                (ON).

        Returns:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelEdge-returns "Permalink to this headline")
        :   A Feature object.

        Return type:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelEdge-return-type "Permalink to this headline")
        :   [`AssemblyFeature`](#abaqus.Assembly.AssemblyFeature.AssemblyFeature "abaqus.Assembly.AssemblyFeature.AssemblyFeature (Python class) — Bases: Feature")

        Raises:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelEdge-raises "Permalink to this headline")
        :   [**AbaqusException**](../../../kernel/utility.html#abaqus.UtilityAndView.AbaqusException.AbaqusException "abaqus.UtilityAndView.AbaqusException.AbaqusException (Python class) — Bases: Exception") –

    *static* ParallelFace(*[movablePlane](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelFace.movablePlane "abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelFace.movablePlane (Python parameter) — A planar face, a Datum plane, or a face from an orphan mesh on the part instance to be moved.")*, *[fixedPlane](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelFace.fixedPlane "abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelFace.fixedPlane (Python parameter) — A planar face, a Datum plane, or a face from an orphan mesh on the part instance to remain fixed.")*, *[flip](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelFace.flip "abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelFace.flip (Python parameter) — A Boolean specifying whether the normals to the faces are forward aligned (OFF) or reverse aligned (ON).")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/AssemblyFeature.py#L307-L338)[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelFace "Permalink to this definition")
    :   This method moves an instance so that its face is parallel to a face of a fixed instance.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].rootAssembly.AttachmentLines
        ```

        Note

        Check [ParallelFace on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-parallelfacepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelFace-parameters "Permalink to this headline")
        :   movablePlane[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelFace.movablePlane "Permalink to this definition")
            :   A planar face, a Datum plane, or a face from an orphan mesh on the part instance to be
                moved.

            fixedPlane[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelFace.fixedPlane "Permalink to this definition")
            :   A planar face, a Datum plane, or a face from an orphan mesh on the part instance to
                remain fixed.

            flip[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelFace.flip "Permalink to this definition")
            :   A Boolean specifying whether the normals to the faces are forward aligned (OFF) or
                reverse aligned (ON).

        Returns:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelFace-returns "Permalink to this headline")
        :   A Feature object.

        Return type:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelFace-return-type "Permalink to this headline")
        :   [`AssemblyFeature`](#abaqus.Assembly.AssemblyFeature.AssemblyFeature "abaqus.Assembly.AssemblyFeature.AssemblyFeature (Python class) — Bases: Feature")

        Raises:[¶](#abaqus.Assembly.AssemblyFeature.AssemblyFeature.ParallelFace-raises "Permalink to this headline")
        :   [**AbaqusException**](../../../kernel/utility.html#abaqus.UtilityAndView.AbaqusException.AbaqusException "abaqus.UtilityAndView.AbaqusException.AbaqusException (Python class) — Bases: Exception") –

*class* ModelInstance(*[name](#abaqus.Assembly.ModelInstance.ModelInstance "abaqus.Assembly.ModelInstance.ModelInstance.__init__.name (Python parameter)")*, *[model](#abaqus.Assembly.ModelInstance.ModelInstance "abaqus.Assembly.ModelInstance.ModelInstance.__init__.model (Python parameter)")*, *[autoOffset](#abaqus.Assembly.ModelInstance.ModelInstance "abaqus.Assembly.ModelInstance.ModelInstance.__init__.autoOffset (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/ModelInstance.py#L21-L129)[¶](#abaqus.Assembly.ModelInstance.ModelInstance "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    A ModelInstance object is an instance of a Model.

    Note

    This object can be accessed by:

    ```python
    import assembly
    mdb.models[name].rootAssembly.modelInstances[i]
    ```

    Note

    Check [ModelInstance on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelinstancepyc.htm?contextscope=all).

    Member Details:

    ConvertConstraints()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/ModelInstance.py#L87-L93)[¶](#abaqus.Assembly.ModelInstance.ModelInstance.ConvertConstraints "Permalink to this definition")
    :   This method converts the position constraints of an instance to absolute positions.

        The method deletes the constraint features on the instance but preserves the position in space.

    datums : --is-rst--:py:class:`dict`\[:py:class:`int`, :py:class:`~abaqus.Datum.Datum.Datum`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/ModelInstance.py#L54-L55)[¶](#abaqus.Assembly.ModelInstance.ModelInstance.datums "Permalink to this definition")
    :   A repository of Datum objects.

    edges : --is-rst--:py:class:`~abaqus.BasicGeometry.EdgeArray.EdgeArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/ModelInstance.py#L45-L46)[¶](#abaqus.Assembly.ModelInstance.ModelInstance.edges "Permalink to this definition")
    :   An EdgeArray object.

    elements : --is-rst--:py:class:`~abaqus.Mesh.MeshElementArray.MeshElementArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/ModelInstance.py#L48-L49)[¶](#abaqus.Assembly.ModelInstance.ModelInstance.elements "Permalink to this definition")
    :   A MeshElementArray object.

    getPosition()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/ModelInstance.py#L95-L98)[¶](#abaqus.Assembly.ModelInstance.ModelInstance.getPosition "Permalink to this definition")
    :   This method prints the sum of the translations and rotations applied to the ModelInstance object.

    nodes : --is-rst--:py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/ModelInstance.py#L51-L52)[¶](#abaqus.Assembly.ModelInstance.ModelInstance.nodes "Permalink to this definition")
    :   A MeshNodeArray object.

    referencePoints : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.BasicGeometry.ReferencePoint.ReferencePoint`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/ModelInstance.py#L57-L58)[¶](#abaqus.Assembly.ModelInstance.ModelInstance.referencePoints "Permalink to this definition")
    :   A repository of ReferencePoint objects.

    replace(*[instanceOf](#abaqus.Assembly.ModelInstance.ModelInstance.replace.instanceOf "abaqus.Assembly.ModelInstance.ModelInstance.replace.instanceOf (Python parameter) — A Model object to be instanced.")*, *[applyConstraints](#abaqus.Assembly.ModelInstance.ModelInstance.replace.applyConstraints "abaqus.Assembly.ModelInstance.ModelInstance.replace.applyConstraints (Python parameter) — A Boolean specifying whether to apply existing constraints on the new instance or to position the new instance in the same place as the original instance.")=`True`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/ModelInstance.py#L100-L118)[¶](#abaqus.Assembly.ModelInstance.ModelInstance.replace "Permalink to this definition")
    :   This method replaces one instance with an instance of another model.

        New in version 2019: The `replace` method was added.

        Note

        Check [ModelInstance.replace on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelinstancepyc.htm?contextscope=all#simaker-modelinstancereplacepyc).

        Parameters:[¶](#abaqus.Assembly.ModelInstance.ModelInstance.replace-parameters "Permalink to this headline")
        :   instanceOf[¶](#abaqus.Assembly.ModelInstance.ModelInstance.replace.instanceOf "Permalink to this definition")
            :   A Model object to be instanced. If the model does not exist, no ModelInstance object is
                created.

            applyConstraints=`True`[¶](#abaqus.Assembly.ModelInstance.ModelInstance.replace.applyConstraints "Permalink to this definition")
            :   A Boolean specifying whether to apply existing constraints on the new instance or to
                position the new instance in the same place as the original instance. The default value
                is True. A value of False indicates that constraints applies to the instance are deleted
                will be deleted from the feature list.

    sets : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Region.Set.Set`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/ModelInstance.py#L32-L35)[¶](#abaqus.Assembly.ModelInstance.ModelInstance.sets "Permalink to this definition")
    :   A repository of Set objects specifying the sets created on the assembly. For more
        information, see [Region
        commands](<https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all>).

    surfaces : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Region.Surface.Surface`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/ModelInstance.py#L37-L40)[¶](#abaqus.Assembly.ModelInstance.ModelInstance.surfaces "Permalink to this definition")
    :   A repository of Surface objects specifying the surfaces created on the assembly. For
        more information, see [Region
        commands](<https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-m-RegPyc-sb.htm?ContextScope=all>).

    translate(*[vector](#abaqus.Assembly.ModelInstance.ModelInstance.translate.vector "abaqus.Assembly.ModelInstance.ModelInstance.translate.vector (Python parameter) — A sequence of three Floats specifying a translation vector.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/ModelInstance.py#L120-L129)[¶](#abaqus.Assembly.ModelInstance.ModelInstance.translate "Permalink to this definition")
    :   This method translates an instance by the specified amount.

        Note

        Check [ModelInstance.translate on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelinstancepyc.htm?contextscope=all#simaker-modelinstancetranslatepyc).

        Parameters:[¶](#abaqus.Assembly.ModelInstance.ModelInstance.translate-parameters "Permalink to this headline")
        :   vector[¶](#abaqus.Assembly.ModelInstance.ModelInstance.translate.vector "Permalink to this definition")
            :   A sequence of three Floats specifying a translation vector.

    vertices : --is-rst--:py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/ModelInstance.py#L42-L43)[¶](#abaqus.Assembly.ModelInstance.ModelInstance.vertices "Permalink to this definition")
    :   A VertexArray object.

*class* PartInstance(*[name](#abaqus.Assembly.PartInstanceArray.PartInstance "abaqus.Assembly.PartInstanceArray.PartInstance.__init__.name (Python parameter)")*, *[part](#abaqus.Assembly.PartInstanceArray.PartInstance "abaqus.Assembly.PartInstanceArray.PartInstance.__init__.part (Python parameter)")*, *[autoOffset](#abaqus.Assembly.PartInstanceArray.PartInstance "abaqus.Assembly.PartInstanceArray.PartInstance.__init__.autoOffset (Python parameter)")=`0`*, *[dependent](#abaqus.Assembly.PartInstanceArray.PartInstance "abaqus.Assembly.PartInstanceArray.PartInstance.__init__.dependent (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L29-L358)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    A PartInstance object is an instance of a Part object.

    Note

    This object can be accessed by:

    ```python
    import assembly
    mdb.models[name].rootAssembly.allInstances[name]
    mdb.models[name].rootAssembly.instances[name]
    ```

    Note

    Check [PartInstance on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?contextscope=all).

    Member Details:

    Contact(*[movableList](#abaqus.Assembly.PartInstanceArray.PartInstance.Contact.movableList "abaqus.Assembly.PartInstanceArray.PartInstance.Contact.movableList (Python parameter) — A sequence of Face or Edge objects on the part instance to be moved.")*, *[fixedList](#abaqus.Assembly.PartInstanceArray.PartInstance.Contact.fixedList "abaqus.Assembly.PartInstanceArray.PartInstance.Contact.fixedList (Python parameter) — A sequence of Face or Edge objects on the part instance to remain fixed.")*, *[direction](#abaqus.Assembly.PartInstanceArray.PartInstance.Contact.direction "abaqus.Assembly.PartInstanceArray.PartInstance.Contact.direction (Python parameter) — A sequence of three Floats specifying the direction of contact.")*, *[clearance](#abaqus.Assembly.PartInstanceArray.PartInstance.Contact.clearance "abaqus.Assembly.PartInstanceArray.PartInstance.Contact.clearance (Python parameter) — A Float specifying the distance between the two faces along the direction of contact.")*, *[isFaceEdges](#abaqus.Assembly.PartInstanceArray.PartInstance.Contact.isFaceEdges "abaqus.Assembly.PartInstanceArray.PartInstance.Contact.isFaceEdges (Python parameter) — A Boolean specifying how Abaqus calculates the contact.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L209-L242)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.Contact "Permalink to this definition")
    :   This method translates an instance along the specified direction until it is in contact with a fixed
        instance.

        Note

        Check [Contact on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-contactpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.Contact-parameters "Permalink to this headline")
        :   movableList[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.Contact.movableList "Permalink to this definition")
            :   A sequence of Face or Edge objects on the part instance to be moved.

            fixedList[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.Contact.fixedList "Permalink to this definition")
            :   A sequence of Face or Edge objects on the part instance to remain fixed.

            direction[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.Contact.direction "Permalink to this definition")
            :   A sequence of three Floats specifying the direction of contact.

            clearance[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.Contact.clearance "Permalink to this definition")
            :   A Float specifying the distance between the two faces along the direction of contact.

            isFaceEdges=`0`[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.Contact.isFaceEdges "Permalink to this definition")
            :   A Boolean specifying how Abaqus calculates the contact. If **isFaceEdges** is OFF, contact
                is computed from the movable face to the fixed face. If **isFaceEdges** is ON, contact is
                computed using only the edges of the movable face and not its interior. The default
                value is OFF.

        Returns:[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.Contact-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.Contact-return-type "Permalink to this headline")
        :   `Feature`

    ConvertConstraints()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L244-L250)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.ConvertConstraints "Permalink to this definition")
    :   This method converts the position constraints of an instance to absolute positions.

        The method deletes the constraint features on the instance but preserves the position in space.

    analysisType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.analysisType "Permalink to this definition")
    :   A SymbolicConstant specifying the part type. Possible values are DEFORMABLE\_BODY,
        EULERIAN, DISCRETE\_RIGID\_SURFACE, and ANALYTIC\_RIGID\_SURFACE.

    cells : --is-rst--:py:class:`~abaqus.BasicGeometry.CellArray.CellArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L101-L102)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.cells "Permalink to this definition")
    :   A CellArray object.

    checkGeometry(*[detailed](#abaqus.Assembly.PartInstanceArray.PartInstance.checkGeometry.detailed "abaqus.Assembly.PartInstanceArray.PartInstance.checkGeometry.detailed (Python parameter) — A Boolean specifying whether detailed output will be printed to the replay file.")=`0`*, *[level](#abaqus.Assembly.PartInstanceArray.PartInstance.checkGeometry.level "abaqus.Assembly.PartInstanceArray.PartInstance.checkGeometry.level (Python parameter) — An Int specifying which level of checking is performed.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L183-L207)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.checkGeometry "Permalink to this definition")
    :   This method checks the validity of the geometry of the part instance and prints a count of all
        topological entities on the part instance (faces, edges, vertices, etc.).

        Note

        Check [PartInstance.checkGeometry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?contextscope=all#simaker-partinstancecheckgeometrypyc).

        Parameters:[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.checkGeometry-parameters "Permalink to this headline")
        :   detailed=`0`[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.checkGeometry.detailed "Permalink to this definition")
            :   A Boolean specifying whether detailed output will be printed to the replay file. The
                default value is OFF.

            level=`None`[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.checkGeometry.level "Permalink to this definition")
            :   An Int specifying which level of checking is performed. Values can range from 20 to 70,
                with higher values reporting less and less important errors. The default value is 20,
                which reports all critical errors. When the default value is used, the stored validity
                status is updated to agree with the result of this check.

        Raises:[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.checkGeometry-raises "Permalink to this headline")
        :   [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.13)") – An exception is thrown if this is a dependent part instance and **level** was either not
            specified or was set to 20, because the validity status cannot be updated for a
            dependent part instance. In this case, this command should be called on the Part
            instead. The geometry of dependent part instances cannot be changed.

    datums : --is-rst--:py:class:`dict`\[:py:class:`int`, :py:class:`~abaqus.Datum.Datum.Datum`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L104-L105)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.datums "Permalink to this definition")
    :   A repository of Datum objects.

    dependent : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L44-L46)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.dependent "Permalink to this definition")
    :   A Boolean specifying whether the part instance is dependent or independent. If
        **dependent** = OFF, the part instance is independent. The default value is OFF.

    edges : --is-rst--:py:class:`~abaqus.BasicGeometry.EdgeArray.EdgeArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L92-L93)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.edges "Permalink to this definition")
    :   An EdgeArray object.

    elemEdges : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Mesh.MeshEdge.MeshEdge`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L122-L127)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.elemEdges "Permalink to this definition")
    :   A repository of MeshEdge objects specifying all the element edges in the part instance.
        For a given element and a given edge index on a given face within that element, the
        corresponding MeshEdge object can be retrieved from the repository by using the key
        calculated as (i\*32 + j\*4 + k), where i, j, and k are zero-based element, face, and edge
        indices, respectively.

    elemFaces : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Mesh.MeshFace.MeshFace`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L117-L117)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.elemFaces "Permalink to this definition")

    elementEdges : --is-rst--:py:class:`~abaqus.Mesh.MeshEdgeArray.MeshEdgeArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L129-L130)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.elementEdges "Permalink to this definition")
    :   A MeshEdgeArray object.

    elementFaces : --is-rst--:py:class:`~abaqus.Mesh.MeshFaceArray.MeshFaceArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L119-L120)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.elementFaces "Permalink to this definition")
    :   A MeshFaceArray object.

    elements : --is-rst--:py:class:`~abaqus.Mesh.MeshElementArray.MeshElementArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L107-L108)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.elements "Permalink to this definition")
    :   A MeshElementArray object.

    excludedFromSimulation : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L48-L51)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.excludedFromSimulation "Permalink to this definition")
    :   A Boolean specifying whether the part instance is excluded from the simulation. If
        **excludedFromSimulation** = ON, the part instance is excluded from the simulation. The
        default value is OFF.

    faces : --is-rst--:py:class:`~abaqus.BasicGeometry.FaceArray.FaceArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L98-L99)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.faces "Permalink to this definition")
    :   A FaceArray object.

    geometryValidity : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L53-L57)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.geometryValidity "Permalink to this definition")
    :   A Boolean specifying the validity of the geometry of the instance. The value is
        computed, but it can be set to ON to perform feature and mesh operations on an invalid
        instance. There is no guarantee that such operations will work if the instance was
        originally invalid.

    getPosition()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L252-L255)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.getPosition "Permalink to this definition")
    :   This method prints the sum of the translations and rotations applied to the PartInstance object.

    getRotation()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L257-L268)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.getRotation "Permalink to this definition")
    :   This method returns a tuple including the point of rotation, axis of rotation, and rotation angle (in
        degrees).

        Returns:[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.getRotation-returns "Permalink to this headline")
        :   A tuple including the point of rotation, axis of rotation, and rotation angle (in
            degrees).

        Return type:[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.getRotation-return-type "Permalink to this headline")
        :   [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")

    getTranslation()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L270-L280)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.getTranslation "Permalink to this definition")
    :   This method returns a tuple of three Floats representing translation in the **X**, **Y**, and **Z**
        directions.

        Returns:[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.getTranslation-returns "Permalink to this headline")
        :   A tuple of three Floats representing the translation.

        Return type:[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.getTranslation-return-type "Permalink to this headline")
        :   `tuple[float`, [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"), `float]`

    ignoredEdges : --is-rst--:py:class:`~abaqus.BasicGeometry.IgnoredEdgeArray.IgnoredEdgeArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L95-L96)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.ignoredEdges "Permalink to this definition")
    :   An IgnoredEdgeArray object.

    ignoredVertices : --is-rst--:py:class:`~abaqus.BasicGeometry.IgnoredVertexArray.IgnoredVertexArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L89-L90)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.ignoredVertices "Permalink to this definition")
    :   An IgnoredVertexArray object.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L41-L42)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.name "Permalink to this definition")
    :   A String specifying the repository key. The name must be a valid Abaqus object name.

    nodes : --is-rst--:py:class:`~abaqus.Mesh.MeshNodeArray.MeshNodeArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L110-L111)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.nodes "Permalink to this definition")
    :   A MeshNodeArray object.

    part : --is-rst--:py:data:`~typing.Optional`\[:py:class:`~abaqus.Part.Part.Part`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L67-L68)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.part "Permalink to this definition")
    :   A Part object specifying the instanced part.

    partName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L135-L136)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.partName "Permalink to this definition")
    :   A String specifying the name of the part from which the instance was created.

    referenceNode : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L63-L65)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.referenceNode "Permalink to this definition")
    :   An Int specifying the reference node number. This member is valid only if
        **analysisType** = DISCRETE\_RIGID\_SURFACE or ANALYTIC\_RIGID\_SURFACE.

    referencePoints : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.BasicGeometry.ReferencePoint.ReferencePoint`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L132-L133)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.referencePoints "Permalink to this definition")
    :   A repository of ReferencePoint objects.

    replace(*[instanceOf](#abaqus.Assembly.PartInstanceArray.PartInstance.replace.instanceOf "abaqus.Assembly.PartInstanceArray.PartInstance.replace.instanceOf (Python parameter) — A Part object specifying which Part will be instanced in place of the original Part.")*, *[applyConstraints](#abaqus.Assembly.PartInstanceArray.PartInstance.replace.applyConstraints "abaqus.Assembly.PartInstanceArray.PartInstance.replace.applyConstraints (Python parameter) — A Boolean specifying whether to apply existing constraints on the new instance or to position the new instance in the same place as the original instance.")=`True`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L282-L296)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.replace "Permalink to this definition")
    :   This method replaces one instance with an instance of another part.

        Note

        Check [PartInstance.replace on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?contextscope=all#simaker-partinstancereplacepyc).

        Parameters:[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.replace-parameters "Permalink to this headline")
        :   instanceOf[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.replace.instanceOf "Permalink to this definition")
            :   A Part object specifying which Part will be instanced in place of the original Part.

            applyConstraints=`True`[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.replace.applyConstraints "Permalink to this definition")
            :   A Boolean specifying whether to apply existing constraints on the new instance or to
                position the new instance in the same place as the original instance. The default value
                is True. A value of False indicates that constraints applies to the instance are deleted
                will be deleted from the feature list.

    rotateAboutAxis(*[axisPoint](#abaqus.Assembly.PartInstanceArray.PartInstance.rotateAboutAxis.axisPoint "abaqus.Assembly.PartInstanceArray.PartInstance.rotateAboutAxis.axisPoint (Python parameter) — A sequence of three Floats specifying the X, Y, and Z coordinates of a point on the axis.")*, *[axisDirection](#abaqus.Assembly.PartInstanceArray.PartInstance.rotateAboutAxis.axisDirection "abaqus.Assembly.PartInstanceArray.PartInstance.rotateAboutAxis.axisDirection (Python parameter) — A sequence of three Floats specifying the direction vector of the axis.")*, *[angle](#abaqus.Assembly.PartInstanceArray.PartInstance.rotateAboutAxis.angle "abaqus.Assembly.PartInstanceArray.PartInstance.rotateAboutAxis.angle (Python parameter) — A Float specifying the rotation angle in degrees.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L298-L313)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.rotateAboutAxis "Permalink to this definition")
    :   This method translates an instance by the specified amount.

        Note

        Check [PartInstance.rotateAboutAxis on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?contextscope=all#simaker-partinstancerotateaboutaxispyc).

        Parameters:[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.rotateAboutAxis-parameters "Permalink to this headline")
        :   axisPoint[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.rotateAboutAxis.axisPoint "Permalink to this definition")
            :   A sequence of three Floats specifying the **X**, **Y**, and **Z** coordinates of a point on
                the axis.

            axisDirection[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.rotateAboutAxis.axisDirection "Permalink to this definition")
            :   A sequence of three Floats specifying the direction vector of the axis.

            angle[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.rotateAboutAxis.angle "Permalink to this definition")
            :   A Float specifying the rotation angle in degrees. Use the right-hand rule to determine
                the direction.

    sets : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Region.Set.Set`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L70-L72)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.sets "Permalink to this definition")
    :   A repository of Set objects specifying the sets created on the part. For more
        information, see Region commands.

    skins : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Region.Skin.Skin`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L78-L80)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.skins "Permalink to this definition")
    :   A repository of Skin objects specifying the skins created on the part. For more
        information, see Region commands.

    stringers : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Region.Stringer.Stringer`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L82-L84)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.stringers "Permalink to this definition")
    :   A repository of Stringer objects specifying the stringers created on the part. For more
        information, see Region commands.

    surfaces : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Region.Surface.Surface`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L74-L76)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.surfaces "Permalink to this definition")
    :   A repository of Surface objects specifying the surfaces created on the part. For more
        information, see Region commands.

    translate(*[vector](#abaqus.Assembly.PartInstanceArray.PartInstance.translate.vector "abaqus.Assembly.PartInstanceArray.PartInstance.translate.vector (Python parameter) — A sequence of three Floats specifying a translation vector.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L315-L324)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.translate "Permalink to this definition")
    :   This method translates an instance by the specified amount.

        Note

        Check [PartInstance.translate on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?contextscope=all#simaker-partinstancetranslatepyc).

        Parameters:[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.translate-parameters "Permalink to this headline")
        :   vector[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.translate.vector "Permalink to this definition")
            :   A sequence of three Floats specifying a translation vector.

    translateTo(*[movableList](#abaqus.Assembly.PartInstanceArray.PartInstance.translateTo.movableList "abaqus.Assembly.PartInstanceArray.PartInstance.translateTo.movableList (Python parameter) — A sequence of Face or Edge objects on the part instance to be moved.")*, *[fixedList](#abaqus.Assembly.PartInstanceArray.PartInstance.translateTo.fixedList "abaqus.Assembly.PartInstanceArray.PartInstance.translateTo.fixedList (Python parameter) — A sequence of Face or Edge objects on the part instances to remain fixed.")*, *[direction](#abaqus.Assembly.PartInstanceArray.PartInstance.translateTo.direction "abaqus.Assembly.PartInstanceArray.PartInstance.translateTo.direction (Python parameter) — A sequence of three Floats specifying the direction of contact.")*, *[clearance](#abaqus.Assembly.PartInstanceArray.PartInstance.translateTo.clearance "abaqus.Assembly.PartInstanceArray.PartInstance.translateTo.clearance (Python parameter) — A Float specifying the distance between the two faces along the direction of contact.")*, *[vector](#abaqus.Assembly.PartInstanceArray.PartInstance.translateTo.vector "abaqus.Assembly.PartInstanceArray.PartInstance.translateTo.vector (Python parameter) — A sequence of three Floats specifying a translation vector.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L326-L358)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.translateTo "Permalink to this definition")
    :   This method translates an instance along the specified direction until it is in contact with a fixed
        instance.

        Note

        Check [PartInstance.translateTo on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partinstancepyc.htm?contextscope=all#simaker-partinstancetranslatetopyc).

        Parameters:[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.translateTo-parameters "Permalink to this headline")
        :   movableList[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.translateTo.movableList "Permalink to this definition")
            :   A sequence of Face or Edge objects on the part instance to be moved.

            fixedList[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.translateTo.fixedList "Permalink to this definition")
            :   A sequence of Face or Edge objects on the part instances to remain fixed.

            direction[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.translateTo.direction "Permalink to this definition")
            :   A sequence of three Floats specifying the direction of contact.

            clearance[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.translateTo.clearance "Permalink to this definition")
            :   A Float specifying the distance between the two faces along the direction of contact.

            vector=`()`[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.translateTo.vector "Permalink to this definition")
            :   A sequence of three Floats specifying a translation vector. If this argument is
                specified, the movable instance will be translated by the specified amount without
                solving for the actual contact.

        Returns:[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.translateTo-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.translateTo-return-type "Permalink to this headline")
        :   `Feature`

    vertices : --is-rst--:py:class:`~abaqus.BasicGeometry.VertexArray.VertexArray` = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Assembly/PartInstanceArray.py#L86-L87)[¶](#abaqus.Assembly.PartInstanceArray.PartInstance.vertices "Permalink to this definition")
    :   A VertexArray object.

[Back to top](#)