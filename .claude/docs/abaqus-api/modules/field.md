# Abaqus FIELD Module API Reference

> Source: [https://hailin.wang/abqpy/en/2025/reference/mdb/model/field.html](https://hailin.wang/abqpy/en/2025/reference/mdb/model/field.html)
> Downloaded for offline use by Claude Code skills.

---

# Field[¶](#field "Permalink to this heading")

A Field object stores the non-propagating data of a field as well as a number of instances of the corresponding FieldState object. The FieldState object stores the propagating data of the field in a single step. A specific type of Field object and a specific type of FieldState object are designed for each type of predefined field. Instances of the FieldState object are created and deleted internally by its corresponding Field object.

## Create fields[¶](#create-fields "Permalink to this heading")

*class* FieldModel(*[name](#abaqus.Field.FieldModel.FieldModel "abaqus.Field.FieldModel.FieldModel.__init__.name (Python parameter)")*, *[description](#abaqus.Field.FieldModel.FieldModel "abaqus.Field.FieldModel.FieldModel.__init__.description (Python parameter)")=`''`*, *[stefanBoltzmann](#abaqus.Field.FieldModel.FieldModel "abaqus.Field.FieldModel.FieldModel.__init__.stefanBoltzmann (Python parameter)")=`None`*, *[absoluteZero](#abaqus.Field.FieldModel.FieldModel "abaqus.Field.FieldModel.FieldModel.__init__.absoluteZero (Python parameter)")=`None`*, *[waveFormulation](#abaqus.Field.FieldModel.FieldModel "abaqus.Field.FieldModel.FieldModel.__init__.waveFormulation (Python parameter)")=`abaqusConstants.NOT_SET`*, *[modelType](#abaqus.Field.FieldModel.FieldModel "abaqus.Field.FieldModel.FieldModel.__init__.modelType (Python parameter)")=`abaqusConstants.STANDARD_EXPLICIT`*, *[universalGas](#abaqus.Field.FieldModel.FieldModel "abaqus.Field.FieldModel.FieldModel.__init__.universalGas (Python parameter)")=`None`*, *[copyConstraints](#abaqus.Field.FieldModel.FieldModel "abaqus.Field.FieldModel.FieldModel.__init__.copyConstraints (Python parameter)")=`1`*, *[copyConnectors](#abaqus.Field.FieldModel.FieldModel "abaqus.Field.FieldModel.FieldModel.__init__.copyConnectors (Python parameter)")=`1`*, *[copyInteractions](#abaqus.Field.FieldModel.FieldModel "abaqus.Field.FieldModel.FieldModel.__init__.copyInteractions (Python parameter)")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/FieldModel.py#L26-L260)[¶](#abaqus.Field.FieldModel.FieldModel "Permalink to this definition")
:   Bases: [`ModelBase`](index.html#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase (Python class) — Bases: object")

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
    | [`DiscreteField`](#abaqus.Field.FieldModel.FieldModel.DiscreteField "abaqus.Field.FieldModel.FieldModel.DiscreteField (Python method) — This method creates a DiscreteField object.")(name, defaultValues, fieldType) | This method creates a DiscreteField object. |
    | [`ExpressionField`](#abaqus.Field.FieldModel.FieldModel.ExpressionField "abaqus.Field.FieldModel.FieldModel.ExpressionField (Python method) — This method creates an ExpressionField object.")(name, expression[, ...]) | This method creates an ExpressionField object. |
    | [`MappedField`](#abaqus.Field.FieldModel.FieldModel.MappedField "abaqus.Field.FieldModel.FieldModel.MappedField (Python method) — This method creates an MappedField object.")(name[, regionType, ...]) | This method creates an MappedField object. |

    Inherited from [`ModelBase`](index.html#abaqus.Model.ModelBase.ModelBase "abaqus.Model.ModelBase.ModelBase (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | `__init__`(name[, description, ...]) | This method creates a Model object. |
    | [`setValues`](index.html#abaqus.Model.ModelBase.ModelBase.setValues "abaqus.Model.ModelBase.ModelBase.setValues (Python method) — This method modifies the Model object.")([description, noPartsInputFile, ...]) | This method modifies the Model object. |

    ---

    Member Details:

    DiscreteField(*[name](#abaqus.Field.FieldModel.FieldModel.DiscreteField.name "abaqus.Field.FieldModel.FieldModel.DiscreteField.name (Python parameter) — A String specifying the repository key.")*, *[defaultValues](#abaqus.Field.FieldModel.FieldModel.DiscreteField.defaultValues "abaqus.Field.FieldModel.FieldModel.DiscreteField.defaultValues (Python parameter) — A sequence of Floats specifying a sequence of floats specifying the default values.")*, *[fieldType](#abaqus.Field.FieldModel.FieldModel.DiscreteField.fieldType "abaqus.Field.FieldModel.FieldModel.DiscreteField.fieldType (Python parameter) — A SymbolicConstant or an Int specifying the type of data represented by this discrete field.")*, *[location](#abaqus.Field.FieldModel.FieldModel.DiscreteField.location "abaqus.Field.FieldModel.FieldModel.DiscreteField.location (Python parameter) — A SymbolicConstant or an Int specifying the location of the domain data.")=`abaqusConstants.NODES`*, *[dataWidth](#abaqus.Field.FieldModel.FieldModel.DiscreteField.dataWidth "abaqus.Field.FieldModel.FieldModel.DiscreteField.dataWidth (Python parameter) — An Int specifying the width of the supplied data.")=`1`*, *[data](#abaqus.Field.FieldModel.FieldModel.DiscreteField.data "abaqus.Field.FieldModel.FieldModel.DiscreteField.data (Python parameter) — A DataTableArray object.")=`None`*, *[description](#abaqus.Field.FieldModel.FieldModel.DiscreteField.description "abaqus.Field.FieldModel.FieldModel.DiscreteField.description (Python parameter) — A String specifying the description of the field.")=`''`*, *[orientationType](#abaqus.Field.FieldModel.FieldModel.DiscreteField.orientationType "abaqus.Field.FieldModel.FieldModel.DiscreteField.orientationType (Python parameter) — A SymbolicConstant specifying the type of the system being described by a discrete field used for an orientation.")=`abaqusConstants.CARTESIAN`*, *[partLevelOrientation](#abaqus.Field.FieldModel.FieldModel.DiscreteField.partLevelOrientation "abaqus.Field.FieldModel.FieldModel.DiscreteField.partLevelOrientation (Python parameter) — A Boolean specifying whether or not the orientations are described in terms of part level coordinates.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/FieldModel.py#L28-L94)[¶](#abaqus.Field.FieldModel.FieldModel.DiscreteField "Permalink to this definition")
    :   This method creates a DiscreteField object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].DiscreteField
        ```

        Note

        Check [DiscreteField on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefieldpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Field.FieldModel.FieldModel.DiscreteField-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Field.FieldModel.FieldModel.DiscreteField.name "Permalink to this definition")
            :   A String specifying the repository key.

            defaultValues[¶](#abaqus.Field.FieldModel.FieldModel.DiscreteField.defaultValues "Permalink to this definition")
            :   A sequence of Floats specifying a sequence of floats specifying the default values.

            fieldType[¶](#abaqus.Field.FieldModel.FieldModel.DiscreteField.fieldType "Permalink to this definition")
            :   A SymbolicConstant or an Int specifying the type of data represented by this discrete
                field. Possible values are SCALAR, ORIENTATION, and PRESCRIBEDCONDITION\_DOF.

            location=`abaqusConstants.NODES`[¶](#abaqus.Field.FieldModel.FieldModel.DiscreteField.location "Permalink to this definition")
            :   A SymbolicConstant or an Int specifying the location of the domain data. Possible values
                are NODES and ELEMENTS. The default value is NODES.

            dataWidth=`1`[¶](#abaqus.Field.FieldModel.FieldModel.DiscreteField.dataWidth "Permalink to this definition")
            :   An Int specifying the width of the supplied data. The default value is 1.

            data=`None`[¶](#abaqus.Field.FieldModel.FieldModel.DiscreteField.data "Permalink to this definition")
            :   A DataTableArray object.

            description=`''`[¶](#abaqus.Field.FieldModel.FieldModel.DiscreteField.description "Permalink to this definition")
            :   A String specifying the description of the field. The default value is an empty string.

            orientationType=`abaqusConstants.CARTESIAN`[¶](#abaqus.Field.FieldModel.FieldModel.DiscreteField.orientationType "Permalink to this definition")
            :   A SymbolicConstant specifying the type of the system being described by a discrete field
                used for an orientation. Possible values are CARTESIAN, CYLINDRICAL, and SPHERICAL. The
                default value is CARTESIAN.

            partLevelOrientation=`0`[¶](#abaqus.Field.FieldModel.FieldModel.DiscreteField.partLevelOrientation "Permalink to this definition")
            :   A Boolean specifying whether or not the orientations are described in terms of part
                level coordinates. The default value is OFF.

        Returns:[¶](#abaqus.Field.FieldModel.FieldModel.DiscreteField-returns "Permalink to this headline")
        :   A DiscreteField object.

        Return type:[¶](#abaqus.Field.FieldModel.FieldModel.DiscreteField-return-type "Permalink to this headline")
        :   [`DiscreteField`](#abaqus.Field.FieldModel.DiscreteField "abaqus.Field.FieldModel.DiscreteField (Python class) — Bases: Field")

        Raises:[¶](#abaqus.Field.FieldModel.FieldModel.DiscreteField-raises "Permalink to this headline")
        :   [**AbaqusException**](../../kernel/utility.html#abaqus.UtilityAndView.AbaqusException.AbaqusException "abaqus.UtilityAndView.AbaqusException.AbaqusException (Python class) — Bases: Exception") –

    ExpressionField(*[name](#abaqus.Field.FieldModel.FieldModel.ExpressionField.name "abaqus.Field.FieldModel.FieldModel.ExpressionField.name (Python parameter) — A String specifying the repository key.")*, *[expression](#abaqus.Field.FieldModel.FieldModel.ExpressionField.expression "abaqus.Field.FieldModel.FieldModel.ExpressionField.expression (Python parameter) — A String specifying the Python expression to evaluate in space.")*, *[localCsys](#abaqus.Field.FieldModel.FieldModel.ExpressionField.localCsys "abaqus.Field.FieldModel.FieldModel.ExpressionField.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the field.")=`None`*, *[description](#abaqus.Field.FieldModel.FieldModel.ExpressionField.description "abaqus.Field.FieldModel.FieldModel.ExpressionField.description (Python parameter) — A String specifying the description of the field.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/FieldModel.py#L96-L131)[¶](#abaqus.Field.FieldModel.FieldModel.ExpressionField "Permalink to this definition")
    :   This method creates an ExpressionField object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].ExpressionField
        ```

        Note

        Check [ExpressionField on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-expressionfieldpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Field.FieldModel.FieldModel.ExpressionField-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Field.FieldModel.FieldModel.ExpressionField.name "Permalink to this definition")
            :   A String specifying the repository key.

            expression[¶](#abaqus.Field.FieldModel.FieldModel.ExpressionField.expression "Permalink to this definition")
            :   A String specifying the Python expression to evaluate in space. Variables are X, Y, and
                Z; R, Th, and Z; or R, Th, and P based on the selected coordinate system.

            localCsys=`None`[¶](#abaqus.Field.FieldModel.FieldModel.ExpressionField.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the field. If
                **localCsys** = None, the field is defined in the global coordinate system. The default
                value is None.

            description=`''`[¶](#abaqus.Field.FieldModel.FieldModel.ExpressionField.description "Permalink to this definition")
            :   A String specifying the description of the field. The default value is an empty string.

        Returns:[¶](#abaqus.Field.FieldModel.FieldModel.ExpressionField-returns "Permalink to this headline")
        :   An ExpressionField object.

        Return type:[¶](#abaqus.Field.FieldModel.FieldModel.ExpressionField-return-type "Permalink to this headline")
        :   [`ExpressionField`](#abaqus.Field.FieldModel.ExpressionField "abaqus.Field.FieldModel.ExpressionField (Python class) — Bases: AnalyticalField")

        Raises:[¶](#abaqus.Field.FieldModel.FieldModel.ExpressionField-raises "Permalink to this headline")
        :   **TextException** –

    MappedField(*[name](#abaqus.Field.FieldModel.FieldModel.MappedField.name "abaqus.Field.FieldModel.FieldModel.MappedField.name (Python parameter) — A String specifying the repository key.")*, *[regionType](#abaqus.Field.FieldModel.FieldModel.MappedField.regionType "abaqus.Field.FieldModel.FieldModel.MappedField.regionType (Python parameter) — A SymbolicConstant specifying the data source region type.")=`abaqusConstants.POINT`*, *[partLevelData](#abaqus.Field.FieldModel.FieldModel.MappedField.partLevelData "abaqus.Field.FieldModel.FieldModel.MappedField.partLevelData (Python parameter) — A Boolean specifying whether or not the point cloud source data are described in terms of part level coordinates.")=`0`*, *[pointDataFormat](#abaqus.Field.FieldModel.FieldModel.MappedField.pointDataFormat "abaqus.Field.FieldModel.FieldModel.MappedField.pointDataFormat (Python parameter) — A SymbolicConstant specifying point cloud source data format.")=`abaqusConstants.XYZ`*, *[gridPointPlane](#abaqus.Field.FieldModel.FieldModel.MappedField.gridPointPlane "abaqus.Field.FieldModel.FieldModel.MappedField.gridPointPlane (Python parameter) — A SymbolicConstant specifying the plane on which the point cloud source data of grid format are described.")=`abaqusConstants.XYPLANE`*, *[defaultUnMappedValue](#abaqus.Field.FieldModel.FieldModel.MappedField.defaultUnMappedValue "abaqus.Field.FieldModel.FieldModel.MappedField.defaultUnMappedValue (Python parameter) — A Float specifying the parameter (field) value reported when a value cannot be calculated from the data source.")=`0`*, *[mappingAlgorithm](#abaqus.Field.FieldModel.FieldModel.MappedField.mappingAlgorithm "abaqus.Field.FieldModel.FieldModel.MappedField.mappingAlgorithm (Python parameter) — A SymbolicConstant specifying the mapping algorithm for target surface, or on mesh target model when the parameter value are located at nodes, for example nodal temperatures.")=`abaqusConstants.SURFACE`*, *[searchTolType](#abaqus.Field.FieldModel.FieldModel.MappedField.searchTolType "abaqus.Field.FieldModel.FieldModel.MappedField.searchTolType (Python parameter) — A SymbolicConstant specifying searching tolerance type in terms of absolute value or a fraction of the average of all element characteristic length in target model region. Possible values are ABSOLUTE and RELATIVE.")=`abaqusConstants.RELATIVE`*, *[boundarySearchTol](#abaqus.Field.FieldModel.FieldModel.MappedField.boundarySearchTol "abaqus.Field.FieldModel.FieldModel.MappedField.boundarySearchTol (Python parameter) — A Float specifying the search distance tolerance value on the exterior boundary of target model region.")=`0`*, *[neighborhoodSearchTol](#abaqus.Field.FieldModel.FieldModel.MappedField.neighborhoodSearchTol "abaqus.Field.FieldModel.FieldModel.MappedField.neighborhoodSearchTol (Python parameter) — A Float specifying the search distance tolerance value used for distance weighting algorithm.")=`1000000`*, *[negativeNormalSearchTol](#abaqus.Field.FieldModel.FieldModel.MappedField.negativeNormalSearchTol "abaqus.Field.FieldModel.FieldModel.MappedField.negativeNormalSearchTol (Python parameter) — A Float specifying the search distance tolerance value in the negative normal of target surface region.")=`0`*, *[positiveNormalSearchTol](#abaqus.Field.FieldModel.FieldModel.MappedField.positiveNormalSearchTol "abaqus.Field.FieldModel.FieldModel.MappedField.positiveNormalSearchTol (Python parameter) — A Float specifying the search distance tolerance value in the positive normal of target surface region.")=`0`*, *[scaleCoordinates](#abaqus.Field.FieldModel.FieldModel.MappedField.scaleCoordinates "abaqus.Field.FieldModel.FieldModel.MappedField.scaleCoordinates (Python parameter) — A Boolean specifying whether or not to scale the user-supplied coordinate values from the point cloud or indicated ODB.")=`0`*, *[gridPointData](#abaqus.Field.FieldModel.FieldModel.MappedField.gridPointData "abaqus.Field.FieldModel.FieldModel.MappedField.gridPointData (Python parameter) — A sequence of sequences of Floats specifying the point cloud source data of grid format. The default value is an empty sequence.")=`()`*, *[xyzPointData](#abaqus.Field.FieldModel.FieldModel.MappedField.xyzPointData "abaqus.Field.FieldModel.FieldModel.MappedField.xyzPointData (Python parameter) — A sequence of sequences of Floats specifying the point cloud source data of XYZ format. Each data item is defining the XYZ coordinates of a point and its field value.")=`()`*, *[coordinateScalingFactors](#abaqus.Field.FieldModel.FieldModel.MappedField.coordinateScalingFactors "abaqus.Field.FieldModel.FieldModel.MappedField.coordinateScalingFactors (Python parameter) — A sequence of Floats specifying the scaling factors for the global 1, 2 and 3 directions.")=`()`*, *[localCsys](#abaqus.Field.FieldModel.FieldModel.MappedField.localCsys "abaqus.Field.FieldModel.FieldModel.MappedField.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the field.")=`None`*, *[description](#abaqus.Field.FieldModel.FieldModel.MappedField.description "abaqus.Field.FieldModel.FieldModel.MappedField.description (Python parameter) — A String specifying the description of the field.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/FieldModel.py#L133-L260)[¶](#abaqus.Field.FieldModel.FieldModel.MappedField "Permalink to this definition")
    :   This method creates an MappedField object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].MappedField
        ```

        Note

        Check [MappedField on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mappedfieldpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Field.FieldModel.FieldModel.MappedField-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Field.FieldModel.FieldModel.MappedField.name "Permalink to this definition")
            :   A String specifying the repository key.

            regionType=`abaqusConstants.POINT`[¶](#abaqus.Field.FieldModel.FieldModel.MappedField.regionType "Permalink to this definition")
            :   A SymbolicConstant specifying the data source region type. It can be either an ODB mesh
                or a cloud of points. Possible values are MESH and POINT. The default value is POINT.

            partLevelData=`0`[¶](#abaqus.Field.FieldModel.FieldModel.MappedField.partLevelData "Permalink to this definition")
            :   A Boolean specifying whether or not the point cloud source data are described in terms
                of part level coordinates. If part level coordinates is employed, the local coordinate
                system defined in **localCsys** will be ignored. The default value is OFF.

            pointDataFormat=`abaqusConstants.XYZ`[¶](#abaqus.Field.FieldModel.FieldModel.MappedField.pointDataFormat "Permalink to this definition")
            :   A SymbolicConstant specifying point cloud source data format. Possible values are GRID
                and XYZ. The default value is XYZ.

            gridPointPlane=`abaqusConstants.XYPLANE`[¶](#abaqus.Field.FieldModel.FieldModel.MappedField.gridPointPlane "Permalink to this definition")
            :   A SymbolicConstant specifying the plane on which the point cloud source data of grid
                format are described. Possible values are XYPLANE, YZPLANE, and XZPLANE. The default
                value is XYPLANE.

            defaultUnMappedValue=`0`[¶](#abaqus.Field.FieldModel.FieldModel.MappedField.defaultUnMappedValue "Permalink to this definition")
            :   A Float specifying the parameter (field) value reported when a value cannot be
                calculated from the data source. The default value is 0.0.

            mappingAlgorithm=`abaqusConstants.SURFACE`[¶](#abaqus.Field.FieldModel.FieldModel.MappedField.mappingAlgorithm "Permalink to this definition")
            :   A SymbolicConstant specifying the mapping algorithm for target surface, or on mesh
                target model when the parameter value are located at nodes, for example nodal
                temperatures. Possible values are SURFACE and VOLUMETRIC. The default value is SURFACE.

            searchTolType=`abaqusConstants.RELATIVE`[¶](#abaqus.Field.FieldModel.FieldModel.MappedField.searchTolType "Permalink to this definition")
            :   A SymbolicConstant specifying searching tolerance type in terms of absolute value or a
                fraction of the average of all element characteristic length in target model region.
                Possible values are ABSOLUTE and RELATIVE. The default value is RELATIVE.

            boundarySearchTol=`0`[¶](#abaqus.Field.FieldModel.FieldModel.MappedField.boundarySearchTol "Permalink to this definition")
            :   A Float specifying the search distance tolerance value on the exterior boundary of
                target model region. Source points within this distance will be included in computing
                the parameter value of target region. This tolerance applies to both surface and
                volumetric mapping. The default value is 0.01.

            neighborhoodSearchTol=`1000000`[¶](#abaqus.Field.FieldModel.FieldModel.MappedField.neighborhoodSearchTol "Permalink to this definition")
            :   A Float specifying the search distance tolerance value used for distance weighting
                algorithm. Source points within this distance will be included in computing the
                parameter value of target region. This tolerance only applies to surface mapping. The
                default value is 1000000.0.

            negativeNormalSearchTol=`0`[¶](#abaqus.Field.FieldModel.FieldModel.MappedField.negativeNormalSearchTol "Permalink to this definition")
            :   A Float specifying the search distance tolerance value in the negative normal of target
                surface region. Source points within this distance will be included in computing the
                parameter value of target region. This tolerance only applies to surface mapping. The
                default value is 0.15.

            positiveNormalSearchTol=`0`[¶](#abaqus.Field.FieldModel.FieldModel.MappedField.positiveNormalSearchTol "Permalink to this definition")
            :   A Float specifying the search distance tolerance value in the positive normal of target
                surface region. Source points within this distance will be included in computing the
                parameter value of target region. This tolerance only applies to surface mapping. The
                default value is 0.05.

            scaleCoordinates=`0`[¶](#abaqus.Field.FieldModel.FieldModel.MappedField.scaleCoordinates "Permalink to this definition")
            :   A Boolean specifying whether or not to scale the user-supplied coordinate values from
                the point cloud or indicated ODB. The default value is OFF.

            gridPointData=`()`[¶](#abaqus.Field.FieldModel.FieldModel.MappedField.gridPointData "Permalink to this definition")
            :   A sequence of sequences of Floats specifying the point cloud source data of grid format.
                The default value is an empty sequence.

            xyzPointData=`()`[¶](#abaqus.Field.FieldModel.FieldModel.MappedField.xyzPointData "Permalink to this definition")
            :   A sequence of sequences of Floats specifying the point cloud source data of XYZ format.
                Each data item is defining the XYZ coordinates of a point and its field value. The
                default value is an empty sequence.

            coordinateScalingFactors=`()`[¶](#abaqus.Field.FieldModel.FieldModel.MappedField.coordinateScalingFactors "Permalink to this definition")
            :   A sequence of Floats specifying the scaling factors for the global 1, 2 and 3
                directions. The default value is (1.0, 1.0, 1.0).

            localCsys=`None`[¶](#abaqus.Field.FieldModel.FieldModel.MappedField.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the field. If
                **localCsys** = None, the field is defined in the global coordinate system. The default
                value is None.

            description=`''`[¶](#abaqus.Field.FieldModel.FieldModel.MappedField.description "Permalink to this definition")
            :   A String specifying the description of the field. The default value is an empty string.

        Returns:[¶](#abaqus.Field.FieldModel.FieldModel.MappedField-returns "Permalink to this headline")
        :   A MappedField object.

        Return type:[¶](#abaqus.Field.FieldModel.FieldModel.MappedField-return-type "Permalink to this headline")
        :   [`MappedField`](#abaqus.Field.FieldModel.FieldModel.MappedField "abaqus.Field.FieldModel.FieldModel.MappedField (Python method) — This method creates an MappedField object.")

        Raises:[¶](#abaqus.Field.FieldModel.FieldModel.MappedField-raises "Permalink to this headline")
        :   [**AbaqusException**](../../kernel/utility.html#abaqus.UtilityAndView.AbaqusException.AbaqusException "abaqus.UtilityAndView.AbaqusException.AbaqusException (Python class) — Bases: Exception") –

## Other Classes[¶](#other-classes "Permalink to this heading")

*class* AnalyticalField[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L24-L281)[¶](#abaqus.Field.MappedField.AnalyticalField "Permalink to this definition")
:   Bases: [`Field`](#abaqus.Field.Field.Field "abaqus.Field.Field.Field (Python class) — Bases: object")

    The AnalyticalField object is the abstract base type for other AnalyticalField objects. The
    AnalyticalField object has no explicit constructor. The methods and members of the AnalyticalField object
    are common to all objects derived from the AnalyticalField. The AnalyticalField object is derived from the
    Field object.

    Note

    This object can be accessed by:

    ```python
    import fields
    mdb.models[name].analyticalFields[name]
    ```

    Note

    Check [AnalyticalField on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticalfieldpyc.htm?contextscope=all).

    Member Details:

    OdbMeshRegionData(*[odbFileName](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.odbFileName "abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.odbFileName (Python parameter) — A String specifying the name of the output database file (including the .odb extension) to be read into as the source data.")*, *[variableLabel](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.variableLabel "abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.variableLabel (Python parameter) — A String specifying the field output variable.")*, *[stepIndex](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.stepIndex "abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.stepIndex (Python parameter) — An Int specifying the step index.")=`0`*, *[frameIndex](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.frameIndex "abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.frameIndex (Python parameter) — An Int specifying the frame in the specified step.")=`0`*, *[outputPosition](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.outputPosition "abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.outputPosition (Python parameter) — A SymbolicConstant specifying the position where the data is written in the output database.")=`abaqusConstants.UNDEFINED_POSITION`*, *[dataType](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.dataType "abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.dataType (Python parameter) — A SymbolicConstant specifying the data type of the field output variable which should be aligned with the variable.")=`abaqusConstants.SCALAR`*, *[storageType](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.storageType "abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.storageType (Python parameter) — A SymbolicConstant specifying the storage type of the field output variable which should be aligned with the variable.")=`abaqusConstants.FLOAT`*, *[quantityToPlot](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.quantityToPlot "abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.quantityToPlot (Python parameter) — A SymbolicConstant specifying the quantity to plot.")=`abaqusConstants.FIELD_OUTPUT`*, *[averageElementOutput](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.averageElementOutput "abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.averageElementOutput (Python parameter) — A Boolean specifying whether to average the element output.")=`0`*, *[useRegionBoundaries](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.useRegionBoundaries "abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.useRegionBoundaries (Python parameter) — A Boolean specifying whether to use region boundaries when averaging.")=`0`*, *[regionBoundaries](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.regionBoundaries "abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.regionBoundaries (Python parameter) — A SymbolicConstant specifying the type of averaging region boundaries.")=`abaqusConstants.NONE`*, *[includeFeatureBoundaries](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.includeFeatureBoundaries "abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.includeFeatureBoundaries (Python parameter) — A Boolean specifying whether to include additional averaging boundaries for shells and membranes based on feature edges.")=`1`*, *[featureAngle](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.featureAngle "abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.featureAngle (Python parameter) — A Float specifying the feature angle to be used when includeFeatureBoundaries = ON. The default value is 20.0.")=`20`*, *[averageOnlyDisplayed](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.averageOnlyDisplayed "abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.averageOnlyDisplayed (Python parameter) — A Boolean specifying whether to average only values on displayed elements.")=`0`*, *[averagingThreshold](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.averagingThreshold "abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.averagingThreshold (Python parameter) — A Float specifying the nodal averaging threshold percentage.")=`75`*, *[computeOrder](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.computeOrder "abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.computeOrder (Python parameter) — A SymbolicConstant specifying the order or the computations to be performed on the interested field output variable.")=`abaqusConstants.EXTRAPOLATE_COMPUTE_AVERAGE`*, *[numericForm](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.numericForm "abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.numericForm (Python parameter) — A SymbolicConstant specifying the numeric form in which to display results that contain complex numbers.")=`abaqusConstants.REAL`*, *[complexAngle](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.complexAngle "abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.complexAngle (Python parameter) — A Float specifying the angle (in degrees) at which to display results that contain complex numbers when numericForm = COMPLEX_MAG_AT_ANGLE = COMPLEX_MAG_AT_ANGLE.")=`0`*, *[sectionPoint](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.sectionPoint "abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.sectionPoint (Python parameter) — A Dictionary with String keys and String values.")=`''`*, *[refinementType](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.refinementType "abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.refinementType (Python parameter) — A SymbolicConstant specifying the type of the FieldOutput object.")=`None`*, *[refinementLabel](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.refinementLabel "abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.refinementLabel (Python parameter) — A String specifying the Label of FieldOutput object.")=`''`*, *[displayOutputPosition](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.displayOutputPosition "abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.displayOutputPosition (Python parameter) — A SymbolicConstant specifying the position from which to obtain the data.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L52-L281)[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData "Permalink to this definition")
    :   This method creates an OdbMeshRegionData object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].analyticalFields[name].OdbMeshRegionData
        ```

        Note

        Check [OdbMeshRegionData on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshregiondatapyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData-parameters "Permalink to this headline")
        :   odbFileName[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.odbFileName "Permalink to this definition")
            :   A String specifying the name of the output database file (including the .odb extension)
                to be read into as the source data. This String can also be the full path to the output
                database file if it is located in another directory.

            variableLabel[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.variableLabel "Permalink to this definition")
            :   A String specifying the field output variable.

            stepIndex=`0`[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.stepIndex "Permalink to this definition")
            :   An Int specifying the step index. Possible values are 0 ≤ **stepIndex** ≤ (**numSteps** −
                1). The default value is 0.

            frameIndex=`0`[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.frameIndex "Permalink to this definition")
            :   An Int specifying the frame in the specified step. Valid values are 0 ≤ **frameIndex** ≤
                (**numFramesInStep** − 1). The default value is 0.

            outputPosition=`abaqusConstants.UNDEFINED_POSITION`[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.outputPosition "Permalink to this definition")
            :   A SymbolicConstant specifying the position where the data is written in the output
                database. Data can be obtained only from the position at which it was written to the
                output database during the analysis. This position should be aligned with the field
                output variable. Possible values are:

                * UNDEFINED\_POSITION
                * NODAL
                * INTEGRATION\_POINT
                * ELEMENT\_FACE
                * ELEMENT\_NODAL
                * ELEMENT\_CENTROID
                * WHOLE\_ELEMENT
                * WHOLE\_REGION
                * WHOLE\_PART\_INSTANCE
                * WHOLE\_MODEL
                * GENERAL\_PARTICLE

                The default value is UNDEFINED\_POSITION.

            dataType=`abaqusConstants.SCALAR`[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.dataType "Permalink to this definition")
            :   A SymbolicConstant specifying the data type of the field output variable which should be
                aligned with the variable. Currently only SCALAR is supported. Possible values are:

                * ENUMERATION
                * BOOLEAN
                * INTEGER
                * SCALAR
                * VECTOR
                * QUATERNION\_2D
                * QUATERNION\_3D
                * TENSOR
                * TENSOR\_3D\_FULL
                * TENSOR\_3D\_PLANAR
                * TENSOR\_3D\_SURFACE
                * TENSOR\_2D\_PLANAR
                * TENSOR\_2D\_SURFACE

                The default value is SCALAR.

            storageType=`abaqusConstants.FLOAT`[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.storageType "Permalink to this definition")
            :   A SymbolicConstant specifying the storage type of the field output variable which
                should be aligned with the variable. Possible values are FLOAT, DOUBLE, INTEGER, and
                BOOLEAN. The default value is FLOAT.

            quantityToPlot=`abaqusConstants.FIELD_OUTPUT`[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.quantityToPlot "Permalink to this definition")
            :   A SymbolicConstant specifying the quantity to plot. Currently only FIELD\_OUTPUT is
                supported. Possible values are FIELD\_OUTPUT and DISCONTINUITIES. The default value is
                FIELD\_OUTPUT.

            averageElementOutput=`0`[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.averageElementOutput "Permalink to this definition")
            :   A Boolean specifying whether to average the element output. The default value is OFF.

            useRegionBoundaries=`0`[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.useRegionBoundaries "Permalink to this definition")
            :   A Boolean specifying whether to use region boundaries when averaging. The default
                value is OFF.

            regionBoundaries=`abaqusConstants.NONE`[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.regionBoundaries "Permalink to this definition")
            :   A SymbolicConstant specifying the type of averaging region boundaries. Currently only
                NONE and ODB\_REGIONS are supported. Possible values are NONE, ODB\_REGIONS, ELEMENT\_SET,
                and DISPLAY\_GROUPS. The default value is NONE.

            includeFeatureBoundaries=`1`[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.includeFeatureBoundaries "Permalink to this definition")
            :   A Boolean specifying whether to include additional averaging boundaries for shells and
                membranes based on feature edges. The default value is ON.

            featureAngle=`20`[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.featureAngle "Permalink to this definition")
            :   A Float specifying the feature angle to be used when **includeFeatureBoundaries** = ON.
                The default value is 20.0.

            averageOnlyDisplayed=`0`[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.averageOnlyDisplayed "Permalink to this definition")
            :   A Boolean specifying whether to average only values on displayed elements. The default
                value is OFF.

            averagingThreshold=`75`[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.averagingThreshold "Permalink to this definition")
            :   A Float specifying the nodal averaging threshold percentage. 0 ≤ **averagingThreshold**
                ≤ 100. The default value is 75.0.

            computeOrder=`abaqusConstants.EXTRAPOLATE_COMPUTE_AVERAGE`[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.computeOrder "Permalink to this definition")
            :   A SymbolicConstant specifying the order or the computations to be performed on the
                interested field output variable. Possible values are EXTRAPOLATE\_AVERAGE\_COMPUTE,
                EXTRAPOLATE\_COMPUTE\_AVERAGE, EXTRAPOLATE\_COMPUTE, EXTRAPOLATE\_COMPUTE\_DISCONTINUITIES,
                and RAW\_DATA. The default value is EXTRAPOLATE\_COMPUTE\_AVERAGE.

            numericForm=`abaqusConstants.REAL`[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.numericForm "Permalink to this definition")
            :   A SymbolicConstant specifying the numeric form in which to display results that
                contain complex numbers. Possible values are COMPLEX\_MAGNITUDE, COMPLEX\_PHASE, REAL,
                IMAGINARY, and COMPLEX\_MAG\_AT\_ANGLE. The default value is REAL.

            complexAngle=`0`[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.complexAngle "Permalink to this definition")
            :   A Float specifying the angle (in degrees) at which to display results that contain
                complex numbers when **numericForm = COMPLEX\_MAG\_AT\_ANGLE = COMPLEX\_MAG\_AT\_ANGLE**. The
                default value is 0.0.

            sectionPoint=`''`[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.sectionPoint "Permalink to this definition")
            :   A Dictionary with String keys and String values. Each key specifies a region in the
                model; the corresponding value specifies a section point within that region. For
                example:

                ```python
                sectionPoint = {
                    'shell < MAT > < 7 section points >': 'SPOS, (fraction = 1.0)',
                    'shell < MAT > < 5 section points >': 'SPOS, (fraction = 1.0)',
                }
                ```

            refinementType=`None`[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.refinementType "Permalink to this definition")
            :   A SymbolicConstant specifying the type of the FieldOutput object. Possible values for
                the SymbolicConstant are NO\_REFINEMENT, INVARIANT and COMPONENT. Default argument is
                NO\_REFINEMENT. **refinementType** is mandetory if **variableLabel** has an INVARIANT or a
                COMPONENT.

            refinementLabel=`''`[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.refinementLabel "Permalink to this definition")
            :   A String specifying the Label of FieldOutput object. This is required only if the
                **refinementType** is INVARIANT or COMPONENT.

            displayOutputPosition=`None`[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData.displayOutputPosition "Permalink to this definition")
            :   A SymbolicConstant specifying the position from which to obtain the data. Possible
                values are NODAL, INTEGRATION\_POINT, ELEMENT\_FACE, ELEMENT\_NODAL, ELEMENT\_CENTROID,
                WHOLE\_ELEMENT, WHOLE\_REGION, WHOLE\_PART\_INSTANCE, WHOLE\_MODEL, and GENERAL\_PARTICLE.

        Returns:[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData-returns "Permalink to this headline")
        :   An OdbMeshRegionData object.

        Return type:[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData-return-type "Permalink to this headline")
        :   [`OdbMeshRegionData`](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData "abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData (Python method) — This method creates an OdbMeshRegionData object.")

        Raises:[¶](#abaqus.Field.MappedField.AnalyticalField.OdbMeshRegionData-raises "Permalink to this headline")
        :   **TextException** –

    description : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L46-L47)[¶](#abaqus.Field.MappedField.AnalyticalField.description "Permalink to this definition")
    :   A String specifying the description of the field. The default value is an empty string.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`~abaqus.Datum.DatumCsys.DatumCsys`] = `<abaqus.Datum.DatumCsys.DatumCsys object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L41-L44)[¶](#abaqus.Field.MappedField.AnalyticalField.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the field. If
        **localCsys** = None, the field is defined in the global coordinate system. The default
        value is None.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L38-L39)[¶](#abaqus.Field.MappedField.AnalyticalField.name "Permalink to this definition")
    :   A String specifying the repository key.

    odbMeshRegionData : --is-rst--:py:class:`~abaqus.Field.OdbMeshRegionData.OdbMeshRegionData` = `<abaqus.Field.OdbMeshRegionData.OdbMeshRegionData object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L49-L50)[¶](#abaqus.Field.MappedField.AnalyticalField.odbMeshRegionData "Permalink to this definition")
    :   An OdbMeshRegionData object.

*class* Field[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/Field.py#L6-L21)[¶](#abaqus.Field.Field.Field "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The Field object is the abstract base type for other Field objects. The Field object has no explicit
    constructor. The methods and members of the Field object are common to all objects derived from the Field.

    Note

    This object can be accessed by:

    ```python
    import fields
    ```

    Note

    Check [Field on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldpyc.htm?contextscope=all).

    Member Details:

    description : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/Field.py#L6-L21)[¶](#abaqus.Field.Field.Field.description "Permalink to this definition")
    :   A String specifying the description of the field. The default value is an empty string.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/Field.py#L17-L18)[¶](#abaqus.Field.Field.Field.name "Permalink to this definition")
    :   A String specifying the repository key.

*class* OdbMeshRegionData(*[odbFileName](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData "abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.__init__.odbFileName (Python parameter)")*, *[variableLabel](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData "abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.__init__.variableLabel (Python parameter)")*, *[stepIndex](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData "abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.__init__.stepIndex (Python parameter)")=`0`*, *[frameIndex](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData "abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.__init__.frameIndex (Python parameter)")=`0`*, *[outputPosition](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData "abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.__init__.outputPosition (Python parameter)")=`abaqusConstants.UNDEFINED_POSITION`*, *[dataType](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData "abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.__init__.dataType (Python parameter)")=`abaqusConstants.SCALAR`*, *[storageType](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData "abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.__init__.storageType (Python parameter)")=`abaqusConstants.FLOAT`*, *[quantityToPlot](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData "abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.__init__.quantityToPlot (Python parameter)")=`abaqusConstants.FIELD_OUTPUT`*, *[averageElementOutput](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData "abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.__init__.averageElementOutput (Python parameter)")=`0`*, *[useRegionBoundaries](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData "abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.__init__.useRegionBoundaries (Python parameter)")=`0`*, *[regionBoundaries](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData "abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.__init__.regionBoundaries (Python parameter)")=`abaqusConstants.NONE`*, *[includeFeatureBoundaries](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData "abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.__init__.includeFeatureBoundaries (Python parameter)")=`1`*, *[featureAngle](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData "abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.__init__.featureAngle (Python parameter)")=`20`*, *[averageOnlyDisplayed](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData "abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.__init__.averageOnlyDisplayed (Python parameter)")=`0`*, *[averagingThreshold](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData "abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.__init__.averagingThreshold (Python parameter)")=`75`*, *[computeOrder](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData "abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.__init__.computeOrder (Python parameter)")=`abaqusConstants.EXTRAPOLATE_COMPUTE_AVERAGE`*, *[numericForm](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData "abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.__init__.numericForm (Python parameter)")=`abaqusConstants.REAL`*, *[complexAngle](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData "abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.__init__.complexAngle (Python parameter)")=`0`*, *[sectionPoint](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData "abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.__init__.sectionPoint (Python parameter)")=`''`*, *[refinementType](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData "abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.__init__.refinementType (Python parameter)")=`None`*, *[refinementLabel](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData "abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.__init__.refinementLabel (Python parameter)")=`''`*, *[displayOutputPosition](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData "abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.__init__.displayOutputPosition (Python parameter)")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/OdbMeshRegionData.py#L23-L377)[¶](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The OdbMeshRegionData object defines the external source data of MappedField from an ODB file.

    Note

    This object can be accessed by:

    ```python
    import field
    mdb.models[name].analyticalFields[name].odbMeshRegionData
    ```

    Changed in version 2017: The `transformationType` attribute was moved.

    Note

    Check [OdbMeshRegionData on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshregiondatapyc.htm?contextscope=all).

    Member Details:

    averageElementOutput : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/OdbMeshRegionData.py#L95-L96)[¶](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.averageElementOutput "Permalink to this definition")
    :   A Boolean specifying whether to average the element output. The default value is OFF.

    averageOnlyDisplayed : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/OdbMeshRegionData.py#L115-L117)[¶](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.averageOnlyDisplayed "Permalink to this definition")
    :   A Boolean specifying whether to average only values on displayed elements. The default
        value is OFF.

    averagingThreshold : --is-rst--:py:class:`float` = `75`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/OdbMeshRegionData.py#L119-L121)[¶](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.averagingThreshold "Permalink to this definition")
    :   A Float specifying the nodal averaging threshold percentage. 0 ≤ **averagingThreshold**
        ≤100. The default value is 75.0.

    complexAngle : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/OdbMeshRegionData.py#L134-L137)[¶](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.complexAngle "Permalink to this definition")
    :   A Float specifying the angle (in degrees) at which to display results that contain
        complex numbers when *numericForm=COMPLEX\_MAG\_AT\_ANGLE* = COMPLEX\_MAG\_AT\_ANGLE. The
        default value is 0.0.

    computeOrder : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'EXTRAPOLATE_COMPUTE_AVERAGE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/OdbMeshRegionData.py#L123-L127)[¶](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.computeOrder "Permalink to this definition")
    :   A SymbolicConstant specifying the order or the computations to be performed on the
        interested field output variable. Possible values are EXTRAPOLATE\_AVERAGE\_COMPUTE,
        EXTRAPOLATE\_COMPUTE\_AVERAGE, EXTRAPOLATE\_COMPUTE, EXTRAPOLATE\_COMPUTE\_DISCONTINUITIES,
        and RAW\_DATA. The default value is EXTRAPOLATE\_COMPUTE\_AVERAGE.

    dataType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'SCALAR'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/OdbMeshRegionData.py#L82-L83)[¶](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.dataType "Permalink to this definition")
    :   A SymbolicConstant specifying the data type of the field output variable which should be
        aligned with the variable. Currently only SCALAR is supported. Possible values are:

        * ENUMERATION
        * BOOLEAN
        * INTEGER
        * SCALAR
        * VECTOR
        * QUATERNION\_2D
        * QUATERNION\_3D
        * TENSOR
        * TENSOR\_3D\_FULL
        * TENSOR\_3D\_PLANAR
        * TENSOR\_3D\_SURFACE
        * TENSOR\_2D\_PLANAR
        * TENSOR\_2D\_SURFACE

        The default value is SCALAR.

    displayOutputPosition : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNDEFINED_POSITION'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/OdbMeshRegionData.py#L62-L63)[¶](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.displayOutputPosition "Permalink to this definition")
    :   A SymbolicConstant specifying the position where the output is displayed in the
        viewport. Possible values are:

        * UNDEFINED\_POSITION
        * NODAL
        * INTEGRATION\_POINT
        * ELEMENT\_FACE
        * ELEMENT\_NODAL
        * ELEMENT\_CENTROID
        * WHOLE\_ELEMENT
        * WHOLE\_REGION
        * WHOLE\_PART\_INSTANCE
        * WHOLE\_MODEL
        * GENERAL\_PARTICLE

        The default value is UNDEFINED\_POSITION.

    featureAngle : --is-rst--:py:class:`float` = `20`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/OdbMeshRegionData.py#L111-L113)[¶](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.featureAngle "Permalink to this definition")
    :   A Float specifying the feature angle to be used when **includeFeatureBoundaries** = ON. The
        default value is 20.0.

    frameIndex : --is-rst--:py:class:`int` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/OdbMeshRegionData.py#L41-L43)[¶](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.frameIndex "Permalink to this definition")
    :   An Int specifying the frame in the specified step. Valid values are 0 ≤ **frameIndex** ≤
        (*numFramesInStep* − 1). The default value is 0.

    includeFeatureBoundaries : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/OdbMeshRegionData.py#L107-L109)[¶](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.includeFeatureBoundaries "Permalink to this definition")
    :   A Boolean specifying whether to include additional averaging boundaries for shells and
        membranes based on feature edges. The default value is ON.

    numericForm : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'REAL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/OdbMeshRegionData.py#L129-L132)[¶](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.numericForm "Permalink to this definition")
    :   A SymbolicConstant specifying the numeric form in which to display results that contain
        complex numbers. Possible values are COMPLEX\_MAGNITUDE, COMPLEX\_PHASE, REAL, IMAGINARY,
        and COMPLEX\_MAG\_AT\_ANGLE. The default value is REAL.

    odbFileName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/OdbMeshRegionData.py#L139-L142)[¶](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.odbFileName "Permalink to this definition")
    :   A String specifying the name of the output database file (including the .odb extension)
        to be read into as the source data. This String can also be the full path to the output
        database file if it is located in another directory.

    outputPosition : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'UNDEFINED_POSITION'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/OdbMeshRegionData.py#L62-L63)[¶](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.outputPosition "Permalink to this definition")
    :   A SymbolicConstant specifying the position from which to obtain data. Data can be
        obtained only from the position at which they were written to the output database during
        the analysis. This position should be aligned with the field output variable. Possible
        values are:

        * UNDEFINED\_POSITION
        * NODAL
        * INTEGRATION\_POINT
        * ELEMENT\_FACE
        * ELEMENT\_NODAL
        * ELEMENT\_CENTROID
        * WHOLE\_ELEMENT
        * WHOLE\_REGION
        * WHOLE\_PART\_INSTANCE
        * WHOLE\_MODEL
        * GENERAL\_PARTICLE

        The default value is UNDEFINED\_POSITION.

    quantityToPlot : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FIELD_OUTPUT'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/OdbMeshRegionData.py#L90-L93)[¶](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.quantityToPlot "Permalink to this definition")
    :   A SymbolicConstant specifying the quantity to plot. Currently only FIELD\_OUTPUT is
        supported. Possible values are FIELD\_OUTPUT and DISCONTINUITIES. The default value is
        FIELD\_OUTPUT.

    regionBoundaries : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'NONE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/OdbMeshRegionData.py#L102-L105)[¶](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.regionBoundaries "Permalink to this definition")
    :   A SymbolicConstant specifying the type of averaging region boundaries. Currently only
        NONE and ODB\_REGIONS are supported. Possible values are NONE, ODB\_REGIONS, ELEMENT\_SET,
        and DISPLAY\_GROUPS. The default value is NONE.

    setValues(*\*[args](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.setValues "abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.setValues.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.setValues "abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.setValues.kwargs (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/OdbMeshRegionData.py#L374-L377)[¶](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.setValues "Permalink to this definition")
    :   This method modifies the OdbMeshRegionData object.

    stepIndex : --is-rst--:py:class:`int` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/OdbMeshRegionData.py#L37-L39)[¶](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.stepIndex "Permalink to this definition")
    :   An Int specifying the step index. Possible values are 0 ≤ **stepIndex** ≤ (*numSteps* −
        1). The default value is 0.

    storageType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FLOAT'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/OdbMeshRegionData.py#L85-L88)[¶](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.storageType "Permalink to this definition")
    :   A SymbolicConstant specifying the storage type of the field output variable which should
        be aligned with the variable. Possible values are FLOAT, DOUBLE, INTEGER, and BOOLEAN.
        The default value is FLOAT.

    useRegionBoundaries : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/OdbMeshRegionData.py#L98-L100)[¶](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.useRegionBoundaries "Permalink to this definition")
    :   A Boolean specifying whether to use region boundaries when averaging. The default value
        is OFF.

    variableLabel : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/OdbMeshRegionData.py#L144-L145)[¶](#abaqus.Field.OdbMeshRegionData.OdbMeshRegionData.variableLabel "Permalink to this definition")
    :   A String specifying the field output variable.

*class* DataTable[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/DataTableArray.py#L6-L31)[¶](#abaqus.Field.DataTableArray.DataTable "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    A DataTable is an object used to define the domain and data for a DiscreteField.

    Note

    This object can be accessed by:

    ```python
    import field
    mdb.models[name].discreteFields[name].data[i]
    ```

    Note

    Check [DataTable on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datatablepyc.htm?contextscope=all).

    Member Details:

    dataWidth : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/DataTableArray.py#L17-L19)[¶](#abaqus.Field.DataTableArray.DataTable.dataWidth "Permalink to this definition")
    :   An Int specifying the width of the data. Valid widths are 1, 6, 21, corresponding to
        scalar data, orientations and 4D tensors.

    domain : --is-rst--:py:class:`tuple`\[:py:class:`int`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/DataTableArray.py#L27-L28)[¶](#abaqus.Field.DataTableArray.DataTable.domain "Permalink to this definition")
    :   A tuple of Ints specifying the domain node, element or integration point identifiers.

    instanceName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/DataTableArray.py#L24-L25)[¶](#abaqus.Field.DataTableArray.DataTable.instanceName "Permalink to this definition")
    :   A String specifying the instance name.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/DataTableArray.py#L21-L22)[¶](#abaqus.Field.DataTableArray.DataTable.name "Permalink to this definition")
    :   A String specifying the index.

    table : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/DataTableArray.py#L6-L31)[¶](#abaqus.Field.DataTableArray.DataTable.table "Permalink to this definition")
    :   A tuple of Floats specifying the data within the domain.

*class* DiscreteField(*[name](#abaqus.Field.FieldModel.DiscreteField "abaqus.Field.FieldModel.DiscreteField.__init__.name (Python parameter)")*, *[defaultValues](#abaqus.Field.FieldModel.DiscreteField "abaqus.Field.FieldModel.DiscreteField.__init__.defaultValues (Python parameter)")*, *[fieldType](#abaqus.Field.FieldModel.DiscreteField "abaqus.Field.FieldModel.DiscreteField.__init__.fieldType (Python parameter)")*, *[location](#abaqus.Field.FieldModel.DiscreteField "abaqus.Field.FieldModel.DiscreteField.__init__.location (Python parameter)")=`abaqusConstants.NODES`*, *[dataWidth](#abaqus.Field.FieldModel.DiscreteField "abaqus.Field.FieldModel.DiscreteField.__init__.dataWidth (Python parameter)")=`1`*, *[data](#abaqus.Field.FieldModel.DiscreteField "abaqus.Field.FieldModel.DiscreteField.__init__.data (Python parameter)")=`None`*, *[description](#abaqus.Field.FieldModel.DiscreteField "abaqus.Field.FieldModel.DiscreteField.__init__.description (Python parameter)")=`''`*, *[orientationType](#abaqus.Field.FieldModel.DiscreteField "abaqus.Field.FieldModel.DiscreteField.__init__.orientationType (Python parameter)")=`abaqusConstants.CARTESIAN`*, *[partLevelOrientation](#abaqus.Field.FieldModel.DiscreteField "abaqus.Field.FieldModel.DiscreteField.__init__.partLevelOrientation (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/FieldModel.py#L23-L245)[¶](#abaqus.Field.FieldModel.DiscreteField "Permalink to this definition")
:   Bases: [`Field`](#abaqus.Field.Field.Field "abaqus.Field.Field.Field (Python class) — Bases: object")

    The DiscreteField object defines a varying field whose values correspond to distinct points within a
    domain. The DiscreteField object is derived from the Field object.

    Note

    This object can be accessed by:

    ```python
    import fields
    mdb.models[name].discreteFields[name]
    ```

    Note

    Check [DiscreteField on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefieldpyc.htm?contextscope=all).

    Member Details:

    DiscreteFieldByVolumeFraction(*[name](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction.name "abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction.name (Python parameter) — A String specifying the repository key.")*, *[eulerianInstance](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction.eulerianInstance "abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction.eulerianInstance (Python parameter) — A PartInstance object specifying the elements for which volume fraction values will be computed.")*, *[referenceInstance](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction.referenceInstance "abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction.referenceInstance (Python parameter) — A PartInstance object specifying the region that either contains material or is empty of material.")*, *[accuracy](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction.accuracy "abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction.accuracy (Python parameter) — A Symbolic Constant specifying the level of accuracy that will be used in computing volume fractions.")=`abaqusConstants.MEDIUM`*, *[materialLocation](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction.materialLocation "abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction.materialLocation (Python parameter) — A Symbolic Constant indicating whether the material is inside or outside the referenceInstance.")=`abaqusConstants.INSIDE`*, *[description](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction.description "abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction.description (Python parameter) — A String specifying the description of the field.")=`''`*, *[scaleFactor](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction.scaleFactor "abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction.scaleFactor (Python parameter) — A float specifying the fraction of the volume that is occupied by the referenceInstance.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/FieldModel.py#L124-L174)[¶](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction "Permalink to this definition")
    :   This method creates a DiscreteField object that represents the volume fraction of each element of an
        Eulerian Instance that is occupied by a reference instance.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].DiscreteField
        ```

        Note

        Check [DiscreteFieldByVolumeFraction on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefieldbyvolumefractionpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction.name "Permalink to this definition")
            :   A String specifying the repository key.

            eulerianInstance[¶](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction.eulerianInstance "Permalink to this definition")
            :   A PartInstance object specifying the elements for which volume fraction values will be
                computed.

            referenceInstance[¶](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction.referenceInstance "Permalink to this definition")
            :   A PartInstance object specifying the region that either contains material or is empty of
                material.

            accuracy=`abaqusConstants.MEDIUM`[¶](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction.accuracy "Permalink to this definition")
            :   A Symbolic Constant specifying the level of accuracy that will be used in computing
                volume fractions. Possible values are LOW, MEDIUM, or HIGH. The default value is MEDIUM.

            materialLocation=`abaqusConstants.INSIDE`[¶](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction.materialLocation "Permalink to this definition")
            :   A Symbolic Constant indicating whether the material is inside or outside the
                **referenceInstance**. Possible values are INSIDE or OUTSIDE. The default value is INSIDE.

            description=`''`[¶](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction.description "Permalink to this definition")
            :   A String specifying the description of the field. The default value is an empty string.

            scaleFactor=`''`[¶](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction.scaleFactor "Permalink to this definition")
            :   A float specifying the fraction of the volume that is occupied by the
                *referenceInstance.* Valid values are between 0 and 1.

        Returns:[¶](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction-returns "Permalink to this headline")
        :   A DiscreteField object.

        Return type:[¶](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction-return-type "Permalink to this headline")
        :   [`DiscreteField`](#abaqus.Field.FieldModel.DiscreteField "abaqus.Field.FieldModel.DiscreteField (Python class) — Bases: Field")

        Raises:[¶](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldByVolumeFraction-raises "Permalink to this headline")
        :   [**AbaqusException**](../../kernel/utility.html#abaqus.UtilityAndView.AbaqusException.AbaqusException "abaqus.UtilityAndView.AbaqusException.AbaqusException (Python class) — Bases: Exception") –

    DiscreteFieldFromAnalytic(*[name](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldFromAnalytic.name "abaqus.Field.FieldModel.DiscreteField.DiscreteFieldFromAnalytic.name (Python parameter) — A String specifying the repository key.")*, *[location](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldFromAnalytic.location "abaqus.Field.FieldModel.DiscreteField.DiscreteFieldFromAnalytic.location (Python parameter) — A SymbolicConstant or an Int specifying the location of the domain data.")*, *[analyticFieldName](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldFromAnalytic.analyticFieldName "abaqus.Field.FieldModel.DiscreteField.DiscreteFieldFromAnalytic.analyticFieldName (Python parameter) — A String specifying the name of the AnalyticalField containing the source data.")*, *[region](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldFromAnalytic.region "abaqus.Field.FieldModel.DiscreteField.DiscreteFieldFromAnalytic.region (Python parameter) — A Region object for the field.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/FieldModel.py#L176-L212)[¶](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldFromAnalytic "Permalink to this definition")
    :   This method creates a DiscreteField object from a AnalyticalField object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].DiscreteField
        ```

        Note

        Check [DiscreteFieldFromAnalytic on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefieldfromanalyticpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldFromAnalytic-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldFromAnalytic.name "Permalink to this definition")
            :   A String specifying the repository key.

            location[¶](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldFromAnalytic.location "Permalink to this definition")
            :   A SymbolicConstant or an Int specifying the location of the domain data. Possible values
                are NODES and ELEMENTS. The default value is NODES.

            analyticFieldName[¶](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldFromAnalytic.analyticFieldName "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField containing the source data.

            region[¶](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldFromAnalytic.region "Permalink to this definition")
            :   A Region object for the field.

        Returns:[¶](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldFromAnalytic-returns "Permalink to this headline")
        :   A DiscreteField object.

        Return type:[¶](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldFromAnalytic-return-type "Permalink to this headline")
        :   [`DiscreteField`](#abaqus.Field.FieldModel.DiscreteField "abaqus.Field.FieldModel.DiscreteField (Python class) — Bases: Field")

        Raises:[¶](#abaqus.Field.FieldModel.DiscreteField.DiscreteFieldFromAnalytic-raises "Permalink to this headline")
        :   [**AbaqusException**](../../kernel/utility.html#abaqus.UtilityAndView.AbaqusException.AbaqusException "abaqus.UtilityAndView.AbaqusException.AbaqusException (Python class) — Bases: Exception") –

    data : --is-rst--:py:data:`~typing.Optional`\[:py:class:`~typing.List`\[:py:class:`~abaqus.Field.DataTable.DataTable`]] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/FieldModel.py#L52-L53)[¶](#abaqus.Field.FieldModel.DiscreteField.data "Permalink to this definition")
    :   A DataTableArray object.

    dataWidth : --is-rst--:py:class:`int` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/FieldModel.py#L49-L50)[¶](#abaqus.Field.FieldModel.DiscreteField.dataWidth "Permalink to this definition")
    :   An Int specifying the width of the supplied data. The default value is 1.

    defaultValues : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/FieldModel.py#L38-L39)[¶](#abaqus.Field.FieldModel.DiscreteField.defaultValues "Permalink to this definition")
    :   A sequence of Floats specifying a sequence of floats specifying the default values.

    description : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/FieldModel.py#L55-L56)[¶](#abaqus.Field.FieldModel.DiscreteField.description "Permalink to this definition")
    :   A String specifying the description of the field. The default value is an empty string.

    fieldType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/FieldModel.py)[¶](#abaqus.Field.FieldModel.DiscreteField.fieldType "Permalink to this definition")
    :   A SymbolicConstant or an Int specifying the type of data represented by this discrete
        field. Possible values are SCALAR, ORIENTATION, and PRESCRIBEDCONDITION\_DOF.

    location : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'NODES'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/FieldModel.py#L45-L47)[¶](#abaqus.Field.FieldModel.DiscreteField.location "Permalink to this definition")
    :   A SymbolicConstant or an Int specifying the location of the domain data. Possible values
        are NODES and ELEMENTS. The default value is NODES.

    orientationType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'CARTESIAN'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/FieldModel.py#L58-L61)[¶](#abaqus.Field.FieldModel.DiscreteField.orientationType "Permalink to this definition")
    :   A SymbolicConstant specifying the type of the system being described by a discrete field
        used for an orientation. Possible values are CARTESIAN, CYLINDRICAL, and SPHERICAL. The
        default value is CARTESIAN.

    partLevelOrientation : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/FieldModel.py#L63-L65)[¶](#abaqus.Field.FieldModel.DiscreteField.partLevelOrientation "Permalink to this definition")
    :   A Boolean specifying whether or not the orientations are described in terms of part
        level coordinates. The default value is OFF.

    setValues(*[location](#abaqus.Field.FieldModel.DiscreteField.setValues.location "abaqus.Field.FieldModel.DiscreteField.setValues.location (Python parameter) — A SymbolicConstant or an Int specifying the location of the domain data.")=`abaqusConstants.NODES`*, *[dataWidth](#abaqus.Field.FieldModel.DiscreteField.setValues.dataWidth "abaqus.Field.FieldModel.DiscreteField.setValues.dataWidth (Python parameter) — An Int specifying the width of the supplied data.")=`1`*, *[data](#abaqus.Field.FieldModel.DiscreteField.setValues.data "abaqus.Field.FieldModel.DiscreteField.setValues.data (Python parameter) — A DataTableArray object.")=`None`*, *[description](#abaqus.Field.FieldModel.DiscreteField.setValues.description "abaqus.Field.FieldModel.DiscreteField.setValues.description (Python parameter) — A String specifying the description of the field.")=`''`*, *[orientationType](#abaqus.Field.FieldModel.DiscreteField.setValues.orientationType "abaqus.Field.FieldModel.DiscreteField.setValues.orientationType (Python parameter) — A SymbolicConstant specifying the type of the system being described by a discrete field used for an orientation.")=`abaqusConstants.CARTESIAN`*, *[partLevelOrientation](#abaqus.Field.FieldModel.DiscreteField.setValues.partLevelOrientation "abaqus.Field.FieldModel.DiscreteField.setValues.partLevelOrientation (Python parameter) — A Boolean specifying whether or not the orientations are described in terms of part level coordinates.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/FieldModel.py#L214-L245)[¶](#abaqus.Field.FieldModel.DiscreteField.setValues "Permalink to this definition")
    :   This method modifies the DiscreteField object.

        Note

        Check [DiscreteField.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-discretefieldpyc.htm?contextscope=all#simaker-discretefieldsetvaluespyc).

        Parameters:[¶](#abaqus.Field.FieldModel.DiscreteField.setValues-parameters "Permalink to this headline")
        :   location=`abaqusConstants.NODES`[¶](#abaqus.Field.FieldModel.DiscreteField.setValues.location "Permalink to this definition")
            :   A SymbolicConstant or an Int specifying the location of the domain data. Possible values
                are NODES and ELEMENTS. The default value is NODES.

            dataWidth=`1`[¶](#abaqus.Field.FieldModel.DiscreteField.setValues.dataWidth "Permalink to this definition")
            :   An Int specifying the width of the supplied data. The default value is 1.

            data=`None`[¶](#abaqus.Field.FieldModel.DiscreteField.setValues.data "Permalink to this definition")
            :   A DataTableArray object.

            description=`''`[¶](#abaqus.Field.FieldModel.DiscreteField.setValues.description "Permalink to this definition")
            :   A String specifying the description of the field. The default value is an empty string.

            orientationType=`abaqusConstants.CARTESIAN`[¶](#abaqus.Field.FieldModel.DiscreteField.setValues.orientationType "Permalink to this definition")
            :   A SymbolicConstant specifying the type of the system being described by a discrete field
                used for an orientation. Possible values are CARTESIAN, CYLINDRICAL, and SPHERICAL. The
                default value is CARTESIAN.

            partLevelOrientation=`0`[¶](#abaqus.Field.FieldModel.DiscreteField.setValues.partLevelOrientation "Permalink to this definition")
            :   A Boolean specifying whether or not the orientations are described in terms of part
                level coordinates. The default value is OFF.

*class* ExpressionField(*[name](#abaqus.Field.FieldModel.ExpressionField "abaqus.Field.FieldModel.ExpressionField.__init__.name (Python parameter)")*, *[expression](#abaqus.Field.FieldModel.ExpressionField "abaqus.Field.FieldModel.ExpressionField.__init__.expression (Python parameter)")*, *[localCsys](#abaqus.Field.FieldModel.ExpressionField "abaqus.Field.FieldModel.ExpressionField.__init__.localCsys (Python parameter)")=`None`*, *[description](#abaqus.Field.FieldModel.ExpressionField "abaqus.Field.FieldModel.ExpressionField.__init__.description (Python parameter)")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/FieldModel.py#L9-L83)[¶](#abaqus.Field.FieldModel.ExpressionField "Permalink to this definition")
:   Bases: [`AnalyticalField`](#abaqus.Field.MappedField.AnalyticalField "abaqus.Field.AnalyticalField.AnalyticalField (Python class)")

    The ExpressionField object defines a spatially varying field whose value is calculated from a user-
    supplied mathematical expression. The ExpressionField object is derived from the AnalyticalField object.

    Note

    This object can be accessed by:

    ```python
    import fields
    mdb.models[name].analyticalFields[name]
    ```

    Note

    Check [ExpressionField on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-expressionfieldpyc.htm?contextscope=all).

    Member Details:

    description : --is-rst--str = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/FieldModel.py#L33-L34)[¶](#abaqus.Field.FieldModel.ExpressionField.description "Permalink to this definition")
    :   A String specifying the description of the field. The default value is an empty string.

    expression : --is-rst--str[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/FieldModel.py)[¶](#abaqus.Field.FieldModel.ExpressionField.expression "Permalink to this definition")
    :   A String specifying the Python expression to evaluate in space. Variables are X, Y, and
        Z; R, Th, and Z; or R, Th, and P based on the selected coordinate system.

    localCsys : --is-rst--DatumCsys | None = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/FieldModel.py#L28-L31)[¶](#abaqus.Field.FieldModel.ExpressionField.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the field. If
        **localCsys** = None, the field is defined in the global coordinate system. The default
        value is None.

    setValues(*[localCsys](#abaqus.Field.FieldModel.ExpressionField.setValues.localCsys "abaqus.Field.FieldModel.ExpressionField.setValues.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the field.")=`None`*, *[description](#abaqus.Field.FieldModel.ExpressionField.setValues.description "abaqus.Field.FieldModel.ExpressionField.setValues.description (Python parameter) — A String specifying the description of the field.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/FieldModel.py#L70-L83)[¶](#abaqus.Field.FieldModel.ExpressionField.setValues "Permalink to this definition")
    :   This method modifies the ExpressionField object.

        Note

        Check [ExpressionField.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-expressionfieldpyc.htm?contextscope=all#simaker-expressionfieldsetvaluespyc).

        Parameters:[¶](#abaqus.Field.FieldModel.ExpressionField.setValues-parameters "Permalink to this headline")
        :   localCsys=`None`[¶](#abaqus.Field.FieldModel.ExpressionField.setValues.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the field. If
                **localCsys** = None, the field is defined in the global coordinate system. The default
                value is None.

            description=`''`[¶](#abaqus.Field.FieldModel.ExpressionField.setValues.description "Permalink to this definition")
            :   A String specifying the description of the field. The default value is an empty string.

*class* MappedField(*[name](#abaqus.Field.MappedField.MappedField "abaqus.Field.MappedField.MappedField.__init__.name (Python parameter)")*, *[regionType](#abaqus.Field.MappedField.MappedField "abaqus.Field.MappedField.MappedField.__init__.regionType (Python parameter)")=`abaqusConstants.POINT`*, *[partLevelData](#abaqus.Field.MappedField.MappedField "abaqus.Field.MappedField.MappedField.__init__.partLevelData (Python parameter)")=`0`*, *[pointDataFormat](#abaqus.Field.MappedField.MappedField "abaqus.Field.MappedField.MappedField.__init__.pointDataFormat (Python parameter)")=`abaqusConstants.XYZ`*, *[gridPointPlane](#abaqus.Field.MappedField.MappedField "abaqus.Field.MappedField.MappedField.__init__.gridPointPlane (Python parameter)")=`abaqusConstants.XYPLANE`*, *[defaultUnMappedValue](#abaqus.Field.MappedField.MappedField "abaqus.Field.MappedField.MappedField.__init__.defaultUnMappedValue (Python parameter)")=`0`*, *[mappingAlgorithm](#abaqus.Field.MappedField.MappedField "abaqus.Field.MappedField.MappedField.__init__.mappingAlgorithm (Python parameter)")=`abaqusConstants.SURFACE`*, *[searchTolType](#abaqus.Field.MappedField.MappedField "abaqus.Field.MappedField.MappedField.__init__.searchTolType (Python parameter)")=`abaqusConstants.RELATIVE`*, *[boundarySearchTol](#abaqus.Field.MappedField.MappedField "abaqus.Field.MappedField.MappedField.__init__.boundarySearchTol (Python parameter)")=`0`*, *[neighborhoodSearchTol](#abaqus.Field.MappedField.MappedField "abaqus.Field.MappedField.MappedField.__init__.neighborhoodSearchTol (Python parameter)")=`1000000`*, *[negativeNormalSearchTol](#abaqus.Field.MappedField.MappedField "abaqus.Field.MappedField.MappedField.__init__.negativeNormalSearchTol (Python parameter)")=`0`*, *[positiveNormalSearchTol](#abaqus.Field.MappedField.MappedField "abaqus.Field.MappedField.MappedField.__init__.positiveNormalSearchTol (Python parameter)")=`0`*, *[scaleCoordinates](#abaqus.Field.MappedField.MappedField "abaqus.Field.MappedField.MappedField.__init__.scaleCoordinates (Python parameter)")=`0`*, *[gridPointData](#abaqus.Field.MappedField.MappedField "abaqus.Field.MappedField.MappedField.__init__.gridPointData (Python parameter)")=`()`*, *[xyzPointData](#abaqus.Field.MappedField.MappedField "abaqus.Field.MappedField.MappedField.__init__.xyzPointData (Python parameter)")=`()`*, *[coordinateScalingFactors](#abaqus.Field.MappedField.MappedField "abaqus.Field.MappedField.MappedField.__init__.coordinateScalingFactors (Python parameter)")=`()`*, *[localCsys](#abaqus.Field.MappedField.MappedField "abaqus.Field.MappedField.MappedField.__init__.localCsys (Python parameter)")=`None`*, *[description](#abaqus.Field.MappedField.MappedField "abaqus.Field.MappedField.MappedField.__init__.description (Python parameter)")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L23-L321)[¶](#abaqus.Field.MappedField.MappedField "Permalink to this definition")
:   Bases: [`AnalyticalField`](#abaqus.Field.MappedField.AnalyticalField "abaqus.Field.AnalyticalField.AnalyticalField (Python class)")

    The MappedField object defines a spatially varying field whose value is calculated from an external
    source data. The MappedField object is derived from the AnalyticalField object.

    Note

    This object can be accessed by:

    ```python
    import fields
    mdb.models[name].analyticalFields[name]
    ```

    Note

    Check [MappedField on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mappedfieldpyc.htm?contextscope=all).

    Member Details:

    boundarySearchTol : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L70-L74)[¶](#abaqus.Field.MappedField.MappedField.boundarySearchTol "Permalink to this definition")
    :   A Float specifying the search distance tolerance value on the exterior boundary of
        target model region. Source points within this distance will be included in computing
        the parameter value of target region. This tolerance applies to both surface and
        volumetric mapping. The default value is 0.01.

    coordinateScalingFactors : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:class:`float`, :py:class:`float`] = `(1.0, 1.0, 1.0)`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L110-L112)[¶](#abaqus.Field.MappedField.MappedField.coordinateScalingFactors "Permalink to this definition")
    :   A tuple of Floats specifying the scaling factors for the global 1, 2 and 3 directions.
        The default value is (1.0, 1.0, 1.0).

    defaultUnMappedValue : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L56-L58)[¶](#abaqus.Field.MappedField.MappedField.defaultUnMappedValue "Permalink to this definition")
    :   A Float specifying default parameter (field) value of target model region while its
        value cannot be calculated from the data source. The default value is 0.0.

    description : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L119-L120)[¶](#abaqus.Field.MappedField.MappedField.description "Permalink to this definition")
    :   A String specifying the description of the field. The default value is an empty string.

    gridPointData : --is-rst--:py:class:`tuple`\[:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`], :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L98-L100)[¶](#abaqus.Field.MappedField.MappedField.gridPointData "Permalink to this definition")
    :   A tuple of tuples of Floats specifying the point cloud source data of grid format. The
        default value is an empty sequence.

    gridPointPlane : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'XYPLANE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L51-L54)[¶](#abaqus.Field.MappedField.MappedField.gridPointPlane "Permalink to this definition")
    :   A SymbolicConstant specifying the plane on which the point cloud source data of grid
        format are described. Possible values are XYPLANE, YZPLANE, and XZPLANE. The default
        value is XYPLANE.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`~abaqus.Datum.DatumCsys.DatumCsys`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L114-L117)[¶](#abaqus.Field.MappedField.MappedField.localCsys "Permalink to this definition")
    :   None or a DatumCsys object specifying the local coordinate system of the field. If
        **localCsys** = None, the field is defined in the global coordinate system. The default
        value is None.

    mappingAlgorithm : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'SURFACE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L60-L63)[¶](#abaqus.Field.MappedField.MappedField.mappingAlgorithm "Permalink to this definition")
    :   A SymbolicConstant specifying the mapping algorithm for target surface, or on mesh
        target model when the parameter value are located at nodes, for example nodal
        temperatures. Possible values are SURFACE and VOLUMETRIC. The default value is SURFACE.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L35-L36)[¶](#abaqus.Field.MappedField.MappedField.name "Permalink to this definition")
    :   A String specifying the repository key.

    negativeNormalSearchTol : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L82-L86)[¶](#abaqus.Field.MappedField.MappedField.negativeNormalSearchTol "Permalink to this definition")
    :   A Float specifying the search distance tolerance value in the negative normal of target
        surface region. Source points within this distance will be included in computing the
        parameter value of target region. This tolerance only applies to surface mapping. The
        default value is 0.15.

    neighborhoodSearchTol : --is-rst--:py:class:`float` = `1000000`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L76-L80)[¶](#abaqus.Field.MappedField.MappedField.neighborhoodSearchTol "Permalink to this definition")
    :   A Float specifying the search distance tolerance value used for distance weighting
        algorithm. Source points within this distance will be included in computing the
        parameter value of target region. This tolerance only applies to surface mapping. The
        default value is 1000000.0.

    odbMeshRegionData : --is-rst--:py:class:`~abaqus.Field.OdbMeshRegionData.OdbMeshRegionData` = `<abaqus.Field.OdbMeshRegionData.OdbMeshRegionData object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L107-L108)[¶](#abaqus.Field.MappedField.MappedField.odbMeshRegionData "Permalink to this definition")
    :   An OdbMeshRegionData object specifying the external source data from ODB mesh region.

    partLevelData : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L42-L45)[¶](#abaqus.Field.MappedField.MappedField.partLevelData "Permalink to this definition")
    :   A Boolean specifying whether or not the point cloud source data are described in terms
        of part level coordinates. If part level coordinates is employed, the local coordinate
        system defined in **localCsys** will be ignored. The default value is OFF.

    pointDataFormat : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'XYZ'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L47-L49)[¶](#abaqus.Field.MappedField.MappedField.pointDataFormat "Permalink to this definition")
    :   A SymbolicConstant specifying point cloud source data format. Possible values are GRID
        and XYZ. The default value is XYZ.

    positiveNormalSearchTol : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L88-L92)[¶](#abaqus.Field.MappedField.MappedField.positiveNormalSearchTol "Permalink to this definition")
    :   A Float specifying the search distance tolerance value in the positive normal of target
        surface region. Source points within this distance will be included in computing the
        parameter value of target region. This tolerance only applies to surface mapping. The
        default value is 0.05.

    regionType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'POINT'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L38-L40)[¶](#abaqus.Field.MappedField.MappedField.regionType "Permalink to this definition")
    :   A SymbolicConstant specifying the data source region type. It can be either an ODB mesh
        or a cloud of points. Possible values are MESH and POINT. The default value is POINT.

    scaleCoordinates : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L94-L96)[¶](#abaqus.Field.MappedField.MappedField.scaleCoordinates "Permalink to this definition")
    :   A Boolean specifying whether or not to scale the user-supplied coordinate values from
        the point cloud or indicated ODB. The default value is OFF.

    searchTolType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'RELATIVE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L65-L68)[¶](#abaqus.Field.MappedField.MappedField.searchTolType "Permalink to this definition")
    :   A SymbolicConstant specifying searching tolerance type in terms of absolute value or a
        fraction of the average of all element characteristic length in target model region.
        Possible values are ABSOLUTE and RELATIVE. The default value is RELATIVE.

    setValues(*[regionType](#abaqus.Field.MappedField.MappedField.setValues.regionType "abaqus.Field.MappedField.MappedField.setValues.regionType (Python parameter) — A SymbolicConstant specifying the data source region type.")=`abaqusConstants.POINT`*, *[partLevelData](#abaqus.Field.MappedField.MappedField.setValues.partLevelData "abaqus.Field.MappedField.MappedField.setValues.partLevelData (Python parameter) — A Boolean specifying whether or not the point cloud source data are described in terms of part level coordinates.")=`0`*, *[pointDataFormat](#abaqus.Field.MappedField.MappedField.setValues.pointDataFormat "abaqus.Field.MappedField.MappedField.setValues.pointDataFormat (Python parameter) — A SymbolicConstant specifying point cloud source data format.")=`abaqusConstants.XYZ`*, *[gridPointPlane](#abaqus.Field.MappedField.MappedField.setValues.gridPointPlane "abaqus.Field.MappedField.MappedField.setValues.gridPointPlane (Python parameter) — A SymbolicConstant specifying the plane on which the point cloud source data of grid format are described.")=`abaqusConstants.XYPLANE`*, *[defaultUnMappedValue](#abaqus.Field.MappedField.MappedField.setValues.defaultUnMappedValue "abaqus.Field.MappedField.MappedField.setValues.defaultUnMappedValue (Python parameter) — A Float specifying the parameter (field) value reported when a value cannot be calculated from the data source.")=`0`*, *[mappingAlgorithm](#abaqus.Field.MappedField.MappedField.setValues.mappingAlgorithm "abaqus.Field.MappedField.MappedField.setValues.mappingAlgorithm (Python parameter) — A SymbolicConstant specifying the mapping algorithm for target surface, or on mesh target model when the parameter value are located at nodes, for example nodal temperatures.")=`abaqusConstants.SURFACE`*, *[searchTolType](#abaqus.Field.MappedField.MappedField.setValues.searchTolType "abaqus.Field.MappedField.MappedField.setValues.searchTolType (Python parameter) — A SymbolicConstant specifying searching tolerance type in terms of absolute value or a fraction of the average of all element characteristic length in target model region. Possible values are ABSOLUTE and RELATIVE.")=`abaqusConstants.RELATIVE`*, *[boundarySearchTol](#abaqus.Field.MappedField.MappedField.setValues.boundarySearchTol "abaqus.Field.MappedField.MappedField.setValues.boundarySearchTol (Python parameter) — A Float specifying the search distance tolerance value on the exterior boundary of target model region.")=`0`*, *[neighborhoodSearchTol](#abaqus.Field.MappedField.MappedField.setValues.neighborhoodSearchTol "abaqus.Field.MappedField.MappedField.setValues.neighborhoodSearchTol (Python parameter) — A Float specifying the search distance tolerance value used for distance weighting algorithm.")=`1000000`*, *[negativeNormalSearchTol](#abaqus.Field.MappedField.MappedField.setValues.negativeNormalSearchTol "abaqus.Field.MappedField.MappedField.setValues.negativeNormalSearchTol (Python parameter) — A Float specifying the search distance tolerance value in the negative normal of target surface region.")=`0`*, *[positiveNormalSearchTol](#abaqus.Field.MappedField.MappedField.setValues.positiveNormalSearchTol "abaqus.Field.MappedField.MappedField.setValues.positiveNormalSearchTol (Python parameter) — A Float specifying the search distance tolerance value in the positive normal of target surface region.")=`0`*, *[scaleCoordinates](#abaqus.Field.MappedField.MappedField.setValues.scaleCoordinates "abaqus.Field.MappedField.MappedField.setValues.scaleCoordinates (Python parameter) — A Boolean specifying whether or not to scale the user-supplied coordinate values from the point cloud or indicated ODB.")=`0`*, *[gridPointData](#abaqus.Field.MappedField.MappedField.setValues.gridPointData "abaqus.Field.MappedField.MappedField.setValues.gridPointData (Python parameter) — A sequence of sequences of Floats specifying the point cloud source data of grid format. The default value is an empty sequence.")=`()`*, *[xyzPointData](#abaqus.Field.MappedField.MappedField.setValues.xyzPointData "abaqus.Field.MappedField.MappedField.setValues.xyzPointData (Python parameter) — A sequence of sequences of Floats specifying the point cloud source data of XYZ format. Each data item is defining the XYZ coordinates of a point and its field value.")=`()`*, *[coordinateScalingFactors](#abaqus.Field.MappedField.MappedField.setValues.coordinateScalingFactors "abaqus.Field.MappedField.MappedField.setValues.coordinateScalingFactors (Python parameter) — A sequence of Floats specifying the scaling factors for the global 1, 2 and 3 directions.")=`()`*, *[localCsys](#abaqus.Field.MappedField.MappedField.setValues.localCsys "abaqus.Field.MappedField.MappedField.setValues.localCsys (Python parameter) — None or a DatumCsys object specifying the local coordinate system of the field.")=`None`*, *[description](#abaqus.Field.MappedField.MappedField.setValues.description "abaqus.Field.MappedField.MappedField.setValues.description (Python parameter) — A String specifying the description of the field.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L231-L321)[¶](#abaqus.Field.MappedField.MappedField.setValues "Permalink to this definition")
    :   This method modifies the MappedField object.

        Note

        Check [MappedField.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mappedfieldpyc.htm?contextscope=all#simaker-mappedfieldsetvaluespyc).

        Parameters:[¶](#abaqus.Field.MappedField.MappedField.setValues-parameters "Permalink to this headline")
        :   regionType=`abaqusConstants.POINT`[¶](#abaqus.Field.MappedField.MappedField.setValues.regionType "Permalink to this definition")
            :   A SymbolicConstant specifying the data source region type. It can be either an ODB mesh
                or a cloud of points. Possible values are MESH and POINT. The default value is POINT.

            partLevelData=`0`[¶](#abaqus.Field.MappedField.MappedField.setValues.partLevelData "Permalink to this definition")
            :   A Boolean specifying whether or not the point cloud source data are described in terms
                of part level coordinates. If part level coordinates is employed, the local coordinate
                system defined in **localCsys** will be ignored. The default value is OFF.

            pointDataFormat=`abaqusConstants.XYZ`[¶](#abaqus.Field.MappedField.MappedField.setValues.pointDataFormat "Permalink to this definition")
            :   A SymbolicConstant specifying point cloud source data format. Possible values are GRID
                and XYZ. The default value is XYZ.

            gridPointPlane=`abaqusConstants.XYPLANE`[¶](#abaqus.Field.MappedField.MappedField.setValues.gridPointPlane "Permalink to this definition")
            :   A SymbolicConstant specifying the plane on which the point cloud source data of grid
                format are described. Possible values are XYPLANE, YZPLANE, and XZPLANE. The default
                value is XYPLANE.

            defaultUnMappedValue=`0`[¶](#abaqus.Field.MappedField.MappedField.setValues.defaultUnMappedValue "Permalink to this definition")
            :   A Float specifying the parameter (field) value reported when a value cannot be
                calculated from the data source. The default value is 0.0.

            mappingAlgorithm=`abaqusConstants.SURFACE`[¶](#abaqus.Field.MappedField.MappedField.setValues.mappingAlgorithm "Permalink to this definition")
            :   A SymbolicConstant specifying the mapping algorithm for target surface, or on mesh
                target model when the parameter value are located at nodes, for example nodal
                temperatures. Possible values are SURFACE and VOLUMETRIC. The default value is SURFACE.

            searchTolType=`abaqusConstants.RELATIVE`[¶](#abaqus.Field.MappedField.MappedField.setValues.searchTolType "Permalink to this definition")
            :   A SymbolicConstant specifying searching tolerance type in terms of absolute value or a
                fraction of the average of all element characteristic length in target model region.
                Possible values are ABSOLUTE and RELATIVE. The default value is RELATIVE.

            boundarySearchTol=`0`[¶](#abaqus.Field.MappedField.MappedField.setValues.boundarySearchTol "Permalink to this definition")
            :   A Float specifying the search distance tolerance value on the exterior boundary of
                target model region. Source points within this distance will be included in computing
                the parameter value of target region. This tolerance applies to both surface and
                volumetric mapping. The default value is 0.01.

            neighborhoodSearchTol=`1000000`[¶](#abaqus.Field.MappedField.MappedField.setValues.neighborhoodSearchTol "Permalink to this definition")
            :   A Float specifying the search distance tolerance value used for distance weighting
                algorithm. Source points within this distance will be included in computing the
                parameter value of target region. This tolerance only applies to surface mapping. The
                default value is 1000000.0.

            negativeNormalSearchTol=`0`[¶](#abaqus.Field.MappedField.MappedField.setValues.negativeNormalSearchTol "Permalink to this definition")
            :   A Float specifying the search distance tolerance value in the negative normal of target
                surface region. Source points within this distance will be included in computing the
                parameter value of target region. This tolerance only applies to surface mapping. The
                default value is 0.15.

            positiveNormalSearchTol=`0`[¶](#abaqus.Field.MappedField.MappedField.setValues.positiveNormalSearchTol "Permalink to this definition")
            :   A Float specifying the search distance tolerance value in the positive normal of target
                surface region. Source points within this distance will be included in computing the
                parameter value of target region. This tolerance only applies to surface mapping. The
                default value is 0.05.

            scaleCoordinates=`0`[¶](#abaqus.Field.MappedField.MappedField.setValues.scaleCoordinates "Permalink to this definition")
            :   A Boolean specifying whether or not to scale the user-supplied coordinate values from
                the point cloud or indicated ODB. The default value is OFF.

            gridPointData=`()`[¶](#abaqus.Field.MappedField.MappedField.setValues.gridPointData "Permalink to this definition")
            :   A sequence of sequences of Floats specifying the point cloud source data of grid format.
                The default value is an empty sequence.

            xyzPointData=`()`[¶](#abaqus.Field.MappedField.MappedField.setValues.xyzPointData "Permalink to this definition")
            :   A sequence of sequences of Floats specifying the point cloud source data of XYZ format.
                Each data item is defining the XYZ coordinates of a point and its field value. The
                default value is an empty sequence.

            coordinateScalingFactors=`()`[¶](#abaqus.Field.MappedField.MappedField.setValues.coordinateScalingFactors "Permalink to this definition")
            :   A sequence of Floats specifying the scaling factors for the global 1, 2 and 3
                directions. The default value is (1.0, 1.0, 1.0).

            localCsys=`None`[¶](#abaqus.Field.MappedField.MappedField.setValues.localCsys "Permalink to this definition")
            :   None or a DatumCsys object specifying the local coordinate system of the field. If
                **localCsys** = None, the field is defined in the global coordinate system. The default
                value is None.

            description=`''`[¶](#abaqus.Field.MappedField.MappedField.setValues.description "Permalink to this definition")
            :   A String specifying the description of the field. The default value is an empty string.

    xyzPointData : --is-rst--:py:class:`tuple`\[:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`], :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/MappedField.py#L102-L105)[¶](#abaqus.Field.MappedField.MappedField.xyzPointData "Permalink to this definition")
    :   A tuple of tuples of Floats specifying the point cloud source data of XYZ format. Each
        data item is defining the XYZ coordinates of a point and its field value. The default
        value is an empty sequence.

*class* FieldOdb(*[name](#abaqus.Field.FieldOdb.FieldOdb "abaqus.Field.FieldOdb.FieldOdb.__init__.name (Python parameter)")*, *[analysisTitle](#abaqus.Field.FieldOdb.FieldOdb "abaqus.Field.FieldOdb.FieldOdb.__init__.analysisTitle (Python parameter)")=`''`*, *[description](#abaqus.Field.FieldOdb.FieldOdb "abaqus.Field.FieldOdb.FieldOdb.__init__.description (Python parameter)")=`''`*, *[path](#abaqus.Field.FieldOdb.FieldOdb "abaqus.Field.FieldOdb.FieldOdb.__init__.path (Python parameter)")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Field/FieldOdb.py#L6-L6)[¶](#abaqus.Field.FieldOdb.FieldOdb "Permalink to this definition")
:   Bases: [`OdbBase`](../../odb.html#abaqus.Odb.OdbBase.OdbBase "abaqus.Odb.OdbBase.OdbBase (Python class) — Bases: object")

    Member Details:

[Back to top](#)