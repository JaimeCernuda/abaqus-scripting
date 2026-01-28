# Abaqus MDB Module API Reference

> Source: [https://hailin.wang/abqpy/en/2025/reference/mdb/index.html](https://hailin.wang/abqpy/en/2025/reference/mdb/index.html)
> Downloaded for offline use by Claude Code skills.

---

# Abaqus Model Database[¶](#abaqus-model-database "Permalink to this heading")

Mdb commands are used to create and upgrade an Abaqus model database that stores models and analysis controls.

Objects in Mdb

* [Model](model/index.html)
* [Job](job.html)
* [Annotation](annotation.html)
* [Edit Mesh](edit_mesh.html)

## Classes[¶](#classes "Permalink to this heading")

### Mdb[¶](#mdb "Permalink to this heading")

*class* Mdb(*[pathName](#abaqus.Mdb.Mdb.Mdb "abaqus.Mdb.Mdb.Mdb.__init__.pathName (Python parameter)")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/Mdb.py#L27-L277)[¶](#abaqus.Mdb.Mdb.Mdb "Permalink to this definition")
:   Bases: [`AcisMdb`](model/part_assembly/part.html#abaqus.Part.AcisMdb.AcisMdb "abaqus.Part.AcisMdb.AcisMdb (Python class) — Bases: MdbBase"), [`JobMdb`](job.html#abaqus.Job.JobMdb.JobMdb "abaqus.Job.JobMdb.JobMdb (Python class) — Bases: MdbBase")

    The Mdb object is the high-level Abaqus model database. A model database stores models and analysis
    controls.

    Note

    This object can be accessed by:

    ```python
    mdb
    ```

    Note

    Check [Mdb on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mdbpyc.htm?contextscope=all).

    Public Data Attributes:

    Inherited from [`MdbBase`](#abaqus.Mdb.MdbBase.MdbBase "abaqus.Mdb.MdbBase.MdbBase (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | [`version`](#abaqus.Mdb.MdbBase.MdbBase.version "abaqus.Mdb.MdbBase.MdbBase.version (Python attribute) — An Int specifying the release number of the Mdb object in memory.") | An Int specifying the release number of the Mdb object in memory. |
    | [`lastChangedCount`](#abaqus.Mdb.MdbBase.MdbBase.lastChangedCount "abaqus.Mdb.MdbBase.MdbBase.lastChangedCount (Python attribute) — A Float specifying the value of a counter associated with the Mdb object. The counter indicates when the Mdb object was last changed.") | A Float specifying the value of a counter associated with the Mdb object. |
    | [`jobs`](#abaqus.Mdb.MdbBase.MdbBase.jobs "abaqus.Mdb.MdbBase.MdbBase.jobs (Python attribute) — A repository of Job objects.") | A repository of Job objects. |
    | [`adaptivityProcesses`](#abaqus.Mdb.MdbBase.MdbBase.adaptivityProcesses "abaqus.Mdb.MdbBase.MdbBase.adaptivityProcesses (Python attribute) — A repository of AdaptivityProcess objects.") | A repository of AdaptivityProcess objects. |
    | [`coexecutions`](#abaqus.Mdb.MdbBase.MdbBase.coexecutions "abaqus.Mdb.MdbBase.MdbBase.coexecutions (Python attribute) — A repository of Coexecution objects.") | A repository of Coexecution objects. |
    | [`optimizationProcesses`](#abaqus.Mdb.MdbBase.MdbBase.optimizationProcesses "abaqus.Mdb.MdbBase.MdbBase.optimizationProcesses (Python attribute) — A repository of OptimizationProcess objects.") | A repository of OptimizationProcess objects. |
    | [`meshEditOptions`](#abaqus.Mdb.MdbBase.MdbBase.meshEditOptions "abaqus.Mdb.MdbBase.MdbBase.meshEditOptions (Python attribute) — A MeshEditOptions object specifying the undo/redo behavior when editing meshes on parts or part instances.") | A MeshEditOptions object specifying the undo/redo behavior when editing meshes on parts or part instances. |
    | [`models`](#abaqus.Mdb.MdbBase.MdbBase.models "abaqus.Mdb.MdbBase.MdbBase.models (Python attribute) — A repository of Model objects.") | A repository of Model objects. |
    | [`customData`](#abaqus.Mdb.MdbBase.MdbBase.customData "abaqus.Mdb.MdbBase.MdbBase.customData (Python attribute) — A RepositorySupport object.") | A RepositorySupport object. |
    | [`annotations`](#abaqus.Mdb.MdbBase.MdbBase.annotations "abaqus.Mdb.MdbBase.MdbBase.annotations (Python attribute) — A repository of Annotation objects.") | A repository of Annotation objects. |

    Public Methods:

    |  |  |
    | --- | --- |
    | [`Model`](#abaqus.Mdb.Mdb.Mdb.Model "abaqus.Mdb.Mdb.Mdb.Model (Python method) — This method creates a Model object.")(name, \*args, \*\*kwargs) | This method creates a Model object. |
    | [`ModelFromInputFile`](#abaqus.Mdb.Mdb.Mdb.ModelFromInputFile "abaqus.Mdb.Mdb.Mdb.ModelFromInputFile (Python method) — This method creates a Model object by reading the keywords in an input file and creating the corresponding Abaqus/CAE objects.")(name, inputFileName) | This method creates a Model object by reading the keywords in an input file and creating the corresponding Abaqus/CAE objects. |
    | [`ModelFromOdbFile`](#abaqus.Mdb.Mdb.Mdb.ModelFromOdbFile "abaqus.Mdb.Mdb.Mdb.ModelFromOdbFile (Python method) — This method creates a Model object by reading an output database and creating any corresponding Abaqus/CAE objects.")(name, odbFileName) | This method creates a Model object by reading an output database and creating any corresponding Abaqus/CAE objects. |
    | [`ModelFromNastranFile`](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile "abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile (Python method) — This method creates a Model object by reading the keywords in a Nastran bulk data file or Nastran input file and creating any corresponding Abaqus/CAE objects. The default values is discussed in following and can be defined alternatively in the Abaqus environment file as the one used for the translator from Nastran to Abaqus. For more information, see Translating Nastran data to Abaqus files.")(modelName, inputFileName) | This method creates a Model object by reading the keywords in a Nastran bulk data file or Nastran input file and creating any corresponding Abaqus/CAE objects. |

    Inherited from [`AcisMdb`](model/part_assembly/part.html#abaqus.Part.AcisMdb.AcisMdb "abaqus.Part.AcisMdb.AcisMdb (Python class) — Bases: MdbBase")

    |  |  |
    | --- | --- |
    | [`openAcis`](model/part_assembly/part.html#abaqus.Part.AcisMdb.AcisMdb.openAcis "abaqus.Part.AcisMdb.AcisMdb.openAcis (Python method) — This method creates an AcisFile object from a file containing ACIS-format geometry. This object is subsequently used by the PartFromGeometryFile method.")(fileName[, scaleFromFile]) | This method creates an AcisFile object from a file containing ACIS-format geometry. |
    | [`openCatia`](model/part_assembly/part.html#abaqus.Part.AcisMdb.AcisMdb.openCatia "abaqus.Part.AcisMdb.AcisMdb.openCatia (Python method) — This method creates an AcisFile object from a file containing V5-format geometry. This object is subsequently used by the PartFromGeometryFile method.")(fileName[, topology, ...]) | This method creates an AcisFile object from a file containing V5-format geometry. |
    | [`openEnf`](model/part_assembly/part.html#abaqus.Part.AcisMdb.AcisMdb.openEnf "abaqus.Part.AcisMdb.AcisMdb.openEnf (Python method) — This method creates an AcisFile object from a file containing Elysium Neutral File-format geometry that was created by CATIA V5, I-DEAS, or Pro/ENGINEER. This object is subsequently used by the PartFromGeometryFile method.")(fileName, fileType[, topology, ...]) | This method creates an AcisFile object from a file containing Elysium Neutral File-format geometry that was created by CATIA V5, I-DEAS, or Pro/ENGINEER. |
    | [`openIges`](model/part_assembly/part.html#abaqus.Part.AcisMdb.AcisMdb.openIges "abaqus.Part.AcisMdb.AcisMdb.openIges (Python method) — This method creates an AcisFile object from a file containing IGES-format geometry. This object is subsequently used by the PartFromGeometryFile method.")(fileName[, trimCurve, ...]) | This method creates an AcisFile object from a file containing IGES-format geometry. |
    | [`openParasolid`](model/part_assembly/part.html#abaqus.Part.AcisMdb.AcisMdb.openParasolid "abaqus.Part.AcisMdb.AcisMdb.openParasolid (Python method) — This method creates an AcisFile object from a file containing Parasolid-format geometry. This object is subsequently used by the PartFromGeometryFile method.")(fileName[, topology]) | This method creates an AcisFile object from a file containing Parasolid-format geometry. |
    | [`openStep`](model/part_assembly/part.html#abaqus.Part.AcisMdb.AcisMdb.openStep "abaqus.Part.AcisMdb.AcisMdb.openStep (Python method) — This method creates an AcisFile object from a file containing STEP-format geometry. This object is subsequently used by the PartFromGeometryFile method.")(fileName[, scale]) | This method creates an AcisFile object from a file containing STEP-format geometry. |
    | [`openVda`](model/part_assembly/part.html#abaqus.Part.AcisMdb.AcisMdb.openVda "abaqus.Part.AcisMdb.AcisMdb.openVda (Python method) — This method creates an AcisFile object from a file containing VDA-FS-format geometry. This object is subsequently used by the PartFromGeometryFile method.")(fileName) | This method creates an AcisFile object from a file containing VDA-FS-format geometry. |
    | [`openSolidworks`](model/part_assembly/part.html#abaqus.Part.AcisMdb.AcisMdb.openSolidworks "abaqus.Part.AcisMdb.AcisMdb.openSolidworks (Python method) — This method creates an AcisFile object from a file containing Solidworks format geometry. This object is subsequently used by the PartFromGeometryFile method.")(fileName[, topology]) | This method creates an AcisFile object from a file containing Solidworks format geometry. |

    Inherited from [`JobMdb`](job.html#abaqus.Job.JobMdb.JobMdb "abaqus.Job.JobMdb.JobMdb (Python class) — Bases: MdbBase")

    |  |  |
    | --- | --- |
    | [`Job`](job.html#abaqus.Job.JobMdb.JobMdb.Job "abaqus.Job.JobMdb.JobMdb.Job (Python method) — This method creates an analysis job using a model on a model database (MDB) for the model definition.")(name, model[, description, type, queue, ...]) | This method creates an analysis job using a model on a model database (MDB) for the model definition. |
    | [`JobFromInputFile`](job.html#abaqus.Job.JobMdb.JobMdb.JobFromInputFile "abaqus.Job.JobMdb.JobMdb.JobFromInputFile (Python method) — This method creates an analysis job using an input file for the model definition.")(name, inputFileName[, ...]) | This method creates an analysis job using an input file for the model definition. |
    | [`OptimizationProcess`](job.html#abaqus.Job.JobMdb.JobMdb.OptimizationProcess "abaqus.Job.JobMdb.JobMdb.OptimizationProcess (Python method) — This method creates an OptimizationProcess object.")(name, model, task, ...) | This method creates an OptimizationProcess object. |

    Inherited from [`MdbBase`](#abaqus.Mdb.MdbBase.MdbBase "abaqus.Mdb.MdbBase.MdbBase (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | `__init__`([pathName]) | This constructor creates an empty Mdb object. |
    | [`importDxf`](#abaqus.Mdb.MdbBase.MdbBase.importDxf "abaqus.Mdb.MdbBase.MdbBase.importDxf (Python method) — This method creates a ConstrainedSketch object from a file containing dxf-format (AutoCAD) geometry. Only a limited number of entities are supported. This format should be used only if no other formats are available.")(fileName) | This method creates a ConstrainedSketch object from a file containing dxf-format (AutoCAD) geometry. |
    | [`openMdb`](#abaqus.Mdb.MdbBase.MdbBase.openMdb "abaqus.Mdb.MdbBase.MdbBase.openMdb (Python method) — This method opens an existing model database file.")(pathName) | This method opens an existing model database file. |
    | [`close`](#abaqus.Mdb.MdbBase.MdbBase.close "abaqus.Mdb.MdbBase.MdbBase.close (Python method) — This method closes an open Mdb object but does not save the Mdb object to disk.")() | This method closes an open Mdb object but does not save the Mdb object to disk. |
    | [`save`](#abaqus.Mdb.MdbBase.MdbBase.save "abaqus.Mdb.MdbBase.MdbBase.save (Python method) — This method saves an Mdb object to disk at the location specified by pathName (pathName is a member of the Mdb object).")() | This method saves an Mdb object to disk at the location specified by **pathName** (*pathName* is a member of the Mdb object). |
    | [`saveAs`](#abaqus.Mdb.MdbBase.MdbBase.saveAs "abaqus.Mdb.MdbBase.MdbBase.saveAs (Python method) — This method saves an Mdb object to disk at the specified location.")(pathName) | This method saves an Mdb object to disk at the specified location. |
    | [`openAuxMdb`](#abaqus.Mdb.MdbBase.MdbBase.openAuxMdb "abaqus.Mdb.MdbBase.MdbBase.openAuxMdb (Python method) — This method opens an auxiliary Mdb object on the disk at the specified location. This enables models from the auxiliary Mdb object to be copied into the current Mdb.")(pathName) | This method opens an auxiliary Mdb object on the disk at the specified location. |
    | [`closeAuxMdb`](#abaqus.Mdb.MdbBase.MdbBase.closeAuxMdb "abaqus.Mdb.MdbBase.MdbBase.closeAuxMdb (Python method) — This method closes the auxiliary Mdb which had been opened earlier using the openAuxMdb command.")() | This method closes the auxiliary Mdb which had been opened earlier using the openAuxMdb command. |
    | [`getAuxMdbModelNames`](#abaqus.Mdb.MdbBase.MdbBase.getAuxMdbModelNames "abaqus.Mdb.MdbBase.MdbBase.getAuxMdbModelNames (Python method) — This method returns a list of model names present in the auxiliary Mdb which had been opened earlier using the openAuxMdb command.")() | This method returns a list of model names present in the auxiliary Mdb which had been opened earlier using the openAuxMdb command. |
    | [`copyAuxMdbModel`](#abaqus.Mdb.MdbBase.MdbBase.copyAuxMdbModel "abaqus.Mdb.MdbBase.MdbBase.copyAuxMdbModel (Python method) — This method copies a specified model from the auxiliary Mdb which had been opened earlier using the openAuxMdb command.")(fromName[, toName]) | This method copies a specified model from the auxiliary Mdb which had been opened earlier using the openAuxMdb command. |

    ---

    Member Details:

    Model(*[name](#abaqus.Mdb.Mdb.Mdb.Model.name "abaqus.Mdb.Mdb.Mdb.Model.name (Python parameter) — A String specifying the repository key.")*, *\*[args](#abaqus.Mdb.Mdb.Mdb.Model.args "abaqus.Mdb.Mdb.Mdb.Model.args (Python parameter) — Positional and keyword arguments to be passed to the Model object.")*, *\*\*[kwargs](#abaqus.Mdb.Mdb.Mdb.Model.kwargs "abaqus.Mdb.Mdb.Mdb.Model.kwargs (Python parameter) — Positional and keyword arguments to be passed to the Model object.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/Mdb.py#L114-L136)[¶](#abaqus.Mdb.Mdb.Mdb.Model "Permalink to this definition")
    :   This method creates a Model object.

        Note

        This function can be accessed by:

        ```python
        mdb.Model
        ```

        Note

        Check [Model on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Mdb.Mdb.Mdb.Model-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Mdb.Mdb.Mdb.Model.name "Permalink to this definition")
            :   A String specifying the repository key.

            \*args[¶](#abaqus.Mdb.Mdb.Mdb.Model.args "Permalink to this definition")
            :   Positional and keyword arguments to be passed to the Model object.

            \*\*kwargs[¶](#abaqus.Mdb.Mdb.Mdb.Model.kwargs "Permalink to this definition")
            :   Positional and keyword arguments to be passed to the Model object.

    ModelFromInputFile(*[name](#abaqus.Mdb.Mdb.Mdb.ModelFromInputFile.name "abaqus.Mdb.Mdb.Mdb.ModelFromInputFile.name (Python parameter) — A String specifying the repository key.")*, *[inputFileName](#abaqus.Mdb.Mdb.Mdb.ModelFromInputFile.inputFileName "abaqus.Mdb.Mdb.Mdb.ModelFromInputFile.inputFileName (Python parameter) — A String specifying the name of the input file (including the .inp extension) to be parsed into the new model.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/Mdb.py#L138-L163)[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromInputFile "Permalink to this definition")
    :   This method creates a Model object by reading the keywords in an input file and creating the
        corresponding Abaqus/CAE objects.

        Note

        This function can be accessed by:

        ```python
        mdb.ModelFromInputFile
        ```

        Note

        Check [ModelFromInputFile on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelfrominputfilepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromInputFile-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromInputFile.name "Permalink to this definition")
            :   A String specifying the repository key.

            inputFileName[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromInputFile.inputFileName "Permalink to this definition")
            :   A String specifying the name of the input file (including the .inp extension) to be
                parsed into the new model. This String can also be the full path to the input file if it
                is located in another directory.

        Returns:[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromInputFile-returns "Permalink to this headline")
        :   A Model object.

        Return type:[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromInputFile-return-type "Permalink to this headline")
        :   [`Model`](#abaqus.Mdb.Mdb.Mdb.Model "abaqus.Mdb.Mdb.Mdb.Model (Python method) — This method creates a Model object.")

    ModelFromNastranFile(*[modelName](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.modelName "abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.modelName (Python parameter) — A String specifying the repository key.")*, *[inputFileName](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.inputFileName "abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.inputFileName (Python parameter) — A String specifying the name of the Nastran input file (including the .bdf, .dat, .nas, .nastran, .blk, .bulk extension) to be read into the new model.")*, *[sectionConsolidation](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.sectionConsolidation "abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.sectionConsolidation (Python parameter) — A SymbolicConstant specifying the method used to create shell section.")=`abaqusConstants.PRESERVE_SECTION`*, *[preIntegratedShell](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.preIntegratedShell "abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.preIntegratedShell (Python parameter) — A Boolean specifying whether the pre-integrated shell section is created in default for shell element.")=`0`*, *[weightMassScaling](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.weightMassScaling "abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.weightMassScaling (Python parameter) — A Boolean specifying whether the value on the Nastran data line PARAM, WTMASS is used as a multiplier for all density, mass, and rotary inertia values created in the Abaqus input file.")=`1`*, *[loadCases](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.loadCases "abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.loadCases (Python parameter) — A Boolean specifying whether each SUBCASE for linear static analyses is translated to a LOAD CASE option, and all such LOAD CASE options are grouped in a single STEP option. The default value is ON.")=`1`*, *[coupleBeamOffsets](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.coupleBeamOffsets "abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.coupleBeamOffsets (Python parameter) — A Boolean specifying whether to translate the beam element connectivity to newly created nodes at the offset location and rigidly coupling the new and original nodes.")=`1`*, *[cbar](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.cbar "abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.cbar (Python parameter) — A String specifying the 2-node beam that is created from CBAR and CBEAM elements. Possible values are B31 and B33.")=`abaqusConstants.B31`*, *[cquad4](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.cquad4 "abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.cquad4 (Python parameter) — A String specifying the 4-node shell that is created from CQUAD4 elements.")=`abaqusConstants.S4`*, *[chexa](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.chexa "abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.chexa (Python parameter) — A String specifying the 8-node brick that is created from CHEXA elements.")=`abaqusConstants.C3D8I`*, *[ctetra](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.ctetra "abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.ctetra (Python parameter) — A String specifying the 10-node tetrahedron that is created from CTETRA elements. Possible values are C3D10 and C3D10M.")=`abaqusConstants.C3D10`*, *[keepTranslatedFiles](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.keepTranslatedFiles "abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.keepTranslatedFiles (Python parameter) — A Boolean specifying whether to keep the generated Abaqus input file after the model is created from the Nastran input file.")=`1`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/Mdb.py#L192-L277)[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile "Permalink to this definition")
    :   This method creates a Model object by reading the keywords in a Nastran bulk data file or Nastran
        input file and creating any corresponding Abaqus/CAE objects. The default values is discussed in
        following and can be defined alternatively in the Abaqus environment file as the one used for the
        translator from Nastran to Abaqus. For more information, see Translating Nastran data to Abaqus files.

        Note

        This function can be accessed by:

        ```python
        mdb.ModelFromNastranFile
        ```

        Note

        Check [ModelFromNastranFile on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelfromnastranfilepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile-parameters "Permalink to this headline")
        :   modelName[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.modelName "Permalink to this definition")
            :   A String specifying the repository key.

            inputFileName[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.inputFileName "Permalink to this definition")
            :   A String specifying the name of the Nastran input file (including the .bdf, .dat, .nas,
                .nastran, .blk, .bulk extension) to be read into the new model. This String can also be
                the full path to the Nastran input file if it is located in another directory.

            sectionConsolidation=`abaqusConstants.PRESERVE_SECTION`[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.sectionConsolidation "Permalink to this definition")
            :   A SymbolicConstant specifying the method used to create shell section. Possible values
                are PRESERVE\_SECTION, GROUP\_BY\_MATERIAL, and NONE. If PRESERVE\_SECTION is used, an
                Abaqus section is created corresponding to each shell property ID. If GROUP\_BY\_MATERIAL
                is used, a single Abaqus section is created for all homogeneous elements referencing the
                same material. In both cases, material orientations and offsets are created using
                discrete fields. If NONE is used, a separate shell section is created for each
                combination of orientation, material offset, and/or thickness. The default is
                PRESERVE\_SECTION.

            preIntegratedShell=`0`[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.preIntegratedShell "Permalink to this definition")
            :   A Boolean specifying whether the pre-integrated shell section is created in default for
                shell element. The default value is OFF.

            weightMassScaling=`1`[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.weightMassScaling "Permalink to this definition")
            :   A Boolean specifying whether the value on the Nastran data line PARAM, WTMASS is used as
                a multiplier for all density, mass, and rotary inertia values created in the Abaqus
                input file. The default value is ON.

            loadCases=`1`[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.loadCases "Permalink to this definition")
            :   A Boolean specifying whether each SUBCASE for linear static analyses is translated to a
                LOAD CASE option, and all such LOAD CASE options are grouped in a single STEP option.
                The default value is ON.

            coupleBeamOffsets=`1`[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.coupleBeamOffsets "Permalink to this definition")
            :   A Boolean specifying whether to translate the beam element connectivity to newly created
                nodes at the offset location and rigidly coupling the new and original nodes. If not,
                beam element offsets are translated to the CENTROID and SHEAR CENTER options, which are
                suboptions of the BEAM GENERAL SECTION option. The default value is ON. When the beam
                element references a PBARL or PBEAML property or if the beam offset has a significant
                component in the direction of the beam axis, the setting for this argument is always ON.

            cbar=`abaqusConstants.B31`[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.cbar "Permalink to this definition")
            :   A String specifying the 2-node beam that is created from CBAR and CBEAM elements.
                Possible values are B31 and B33. The default is B31.

            cquad4=`abaqusConstants.S4`[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.cquad4 "Permalink to this definition")
            :   A String specifying the 4-node shell that is created from CQUAD4 elements. Possible
                values are S4 and S4R. The default is S4. If a reduced-integration element is chosen,
                the enhanced hourglass formulation is applied automatically.

            chexa=`abaqusConstants.C3D8I`[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.chexa "Permalink to this definition")
            :   A String specifying the 8-node brick that is created from CHEXA elements. Possible
                values are C3D8I, C3D8 and C3D8R. The default is C3D8I. If a reduced-integration element
                is chosen, the enhanced hourglass formulation is applied automatically.

            ctetra=`abaqusConstants.C3D10`[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.ctetra "Permalink to this definition")
            :   A String specifying the 10-node tetrahedron that is created from CTETRA elements.
                Possible values are C3D10 and C3D10M. The default is C3D10.

            keepTranslatedFiles=`1`[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile.keepTranslatedFiles "Permalink to this definition")
            :   A Boolean specifying whether to keep the generated Abaqus input file after the model is
                created from the Nastran input file. The default value is ON.

        Returns:[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile-returns "Permalink to this headline")
        :   A Model object.

        Return type:[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromNastranFile-return-type "Permalink to this headline")
        :   [`Model`](#abaqus.Mdb.Mdb.Mdb.Model "abaqus.Mdb.Mdb.Mdb.Model (Python method) — This method creates a Model object.")

    ModelFromOdbFile(*[name](#abaqus.Mdb.Mdb.Mdb.ModelFromOdbFile.name "abaqus.Mdb.Mdb.Mdb.ModelFromOdbFile.name (Python parameter) — A String specifying the repository key.")*, *[odbFileName](#abaqus.Mdb.Mdb.Mdb.ModelFromOdbFile.odbFileName "abaqus.Mdb.Mdb.Mdb.ModelFromOdbFile.odbFileName (Python parameter) — A String specifying the name of the output database file (including the .odb extension) to be read into the new model.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/Mdb.py#L165-L190)[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromOdbFile "Permalink to this definition")
    :   This method creates a Model object by reading an output database and creating any corresponding
        Abaqus/CAE objects.

        Note

        This function can be accessed by:

        ```python
        mdb.ModelFromOdbFile
        ```

        Note

        Check [ModelFromOdbFile on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-modelfromodbfilepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromOdbFile-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromOdbFile.name "Permalink to this definition")
            :   A String specifying the repository key.

            odbFileName[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromOdbFile.odbFileName "Permalink to this definition")
            :   A String specifying the name of the output database file (including the .odb extension)
                to be read into the new model. This String can also be the full path to the output
                database file if it is located in another directory.

        Returns:[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromOdbFile-returns "Permalink to this headline")
        :   A Model object.

        Return type:[¶](#abaqus.Mdb.Mdb.Mdb.ModelFromOdbFile-return-type "Permalink to this headline")
        :   [`Model`](#abaqus.Mdb.Mdb.Mdb.Model "abaqus.Mdb.Mdb.Mdb.Model (Python method) — This method creates a Model object.")

### Other Classes[¶](#other-classes "Permalink to this heading")

*class* MdbBase(*[pathName](#abaqus.Mdb.MdbBase.MdbBase "abaqus.Mdb.MdbBase.MdbBase.__init__.pathName (Python parameter)")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/MdbBase.py#L22-L278)[¶](#abaqus.Mdb.MdbBase.MdbBase "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The Mdb object is the high-level Abaqus model database. A model database stores models and analysis
    controls.

    Note

    This object can be accessed by:

    ```python
    mdb
    ```

    Note

    Check [MdbBase on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mdbpyc.htm?contextscope=all).

    Member Details:

    adaptivityProcesses : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Adaptivity.AdaptivityProcess.AdaptivityProcess`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/MdbBase.py#L43-L44)[¶](#abaqus.Mdb.MdbBase.MdbBase.adaptivityProcesses "Permalink to this definition")
    :   A repository of AdaptivityProcess objects.

    annotations : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Annotation.Annotation.Annotation`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/MdbBase.py#L62-L63)[¶](#abaqus.Mdb.MdbBase.MdbBase.annotations "Permalink to this definition")
    :   A repository of Annotation objects.

    close()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/MdbBase.py#L151-L157)[¶](#abaqus.Mdb.MdbBase.MdbBase.close "Permalink to this definition")
    :   This method closes an open Mdb object but does not save the Mdb object to disk.

        After closing the Mdb object, this method creates a new unnamed empty Mdb object.

    closeAuxMdb()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/MdbBase.py#L225-L235)[¶](#abaqus.Mdb.MdbBase.MdbBase.closeAuxMdb "Permalink to this definition")
    :   This method closes the auxiliary Mdb which had been opened earlier using the openAuxMdb command.

        Raises:[¶](#abaqus.Mdb.MdbBase.MdbBase.closeAuxMdb-raises "Permalink to this headline")
        :   **MdbError** – The auxiliary Mdb was not opened;
            If the auxiliary Mdb was not opened earlier

    coexecutions : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Job.Coexecution.Coexecution`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/MdbBase.py#L46-L47)[¶](#abaqus.Mdb.MdbBase.MdbBase.coexecutions "Permalink to this definition")
    :   A repository of Coexecution objects.

    copyAuxMdbModel(*[fromName](#abaqus.Mdb.MdbBase.MdbBase.copyAuxMdbModel.fromName "abaqus.Mdb.MdbBase.MdbBase.copyAuxMdbModel.fromName (Python parameter) — A String specifying the model name in the auxiliary Mdb which is to be copied.")*, *[toName](#abaqus.Mdb.MdbBase.MdbBase.copyAuxMdbModel.toName "abaqus.Mdb.MdbBase.MdbBase.copyAuxMdbModel.toName (Python parameter) — A String specifying the name to be given to the model after it is copied into the Mdb. If this argument is not specified toName is assumed to be the same as fromName.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/MdbBase.py#L255-L278)[¶](#abaqus.Mdb.MdbBase.MdbBase.copyAuxMdbModel "Permalink to this definition")
    :   This method copies a specified model from the auxiliary Mdb which had been opened earlier using the
        openAuxMdb command.

        Note

        Check [MdbBase.copyAuxMdbModel on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mdbpyc.htm?contextscope=all#simaker-mdbcopyauxmdbmodelpyc).

        Parameters:[¶](#abaqus.Mdb.MdbBase.MdbBase.copyAuxMdbModel-parameters "Permalink to this headline")
        :   fromName[¶](#abaqus.Mdb.MdbBase.MdbBase.copyAuxMdbModel.fromName "Permalink to this definition")
            :   A String specifying the model name in the auxiliary Mdb which is to be copied.

            toName=`''`[¶](#abaqus.Mdb.MdbBase.MdbBase.copyAuxMdbModel.toName "Permalink to this definition")
            :   A String specifying the name to be given to the model after it is copied into the Mdb.
                If this argument is not specified **toName** is assumed to be the same as **fromName**. If a
                model with name **toName** already exists in Mdb, it is overwritten.

        Raises:[¶](#abaqus.Mdb.MdbBase.MdbBase.copyAuxMdbModel-raises "Permalink to this headline")
        :   * **MdbError** – The auxiliary Mdb was not opened;
              If the auxiliary Mdb was not opened earlier
            * [**KeyError**](https://docs.python.org/3/library/exceptions.html#KeyError "(in Python v3.13)") – fromName does not exist;
              If the model fromName does not exist in the auxiliary Mdb

    customData : --is-rst--:py:class:`~abaqus.CustomKernel.RepositorySupport.RepositorySupport` = `<abaqus.CustomKernel.RepositorySupport.RepositorySupport object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/MdbBase.py#L59-L60)[¶](#abaqus.Mdb.MdbBase.MdbBase.customData "Permalink to this definition")
    :   A RepositorySupport object.

    getAuxMdbModelNames()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/MdbBase.py#L237-L253)[¶](#abaqus.Mdb.MdbBase.MdbBase.getAuxMdbModelNames "Permalink to this definition")
    :   This method returns a list of model names present in the auxiliary Mdb which had been opened earlier
        using the openAuxMdb command.

        Returns:[¶](#abaqus.Mdb.MdbBase.MdbBase.getAuxMdbModelNames-returns "Permalink to this headline")
        :   A list of model names present in the auxiliaryMdb

        Return type:[¶](#abaqus.Mdb.MdbBase.MdbBase.getAuxMdbModelNames-return-type "Permalink to this headline")
        :   `list[str]`

        Raises:[¶](#abaqus.Mdb.MdbBase.MdbBase.getAuxMdbModelNames-raises "Permalink to this headline")
        :   **MdbError** – The auxiliary Mdb was not opened;
            If the auxiliary Mdb was not opened earlier

    importDxf(*[fileName](#abaqus.Mdb.MdbBase.MdbBase.importDxf.fileName "abaqus.Mdb.MdbBase.MdbBase.importDxf.fileName (Python parameter) — A String specifying the path to the dxf file to open.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/MdbBase.py#L90-L111)[¶](#abaqus.Mdb.MdbBase.MdbBase.importDxf "Permalink to this definition")
    :   This method creates a ConstrainedSketch object from a file containing dxf-format (AutoCAD) geometry.
        Only a limited number of entities are supported. This format should be used only if no other formats are
        available.

        Note

        This function can be accessed by:

        ```python
        Mdb
        ```

        Note

        Check [MdbBase.importDxf on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mdbpyc.htm?contextscope=all#simaker-mdbimportdxfpyc).

        Parameters:[¶](#abaqus.Mdb.MdbBase.MdbBase.importDxf-parameters "Permalink to this headline")
        :   fileName[¶](#abaqus.Mdb.MdbBase.MdbBase.importDxf.fileName "Permalink to this definition")
            :   A String specifying the path to the dxf file to open.

        Returns:[¶](#abaqus.Mdb.MdbBase.MdbBase.importDxf-returns "Permalink to this headline")
        :   A Mdb object

        Return type:[¶](#abaqus.Mdb.MdbBase.MdbBase.importDxf-return-type "Permalink to this headline")
        :   `Mdb`

    jobs : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:data:`~typing.Union`\[:py:class:`~abaqus.Job.Job.Job`, :py:class:`~abaqus.Job.ModelJob.ModelJob`, :py:class:`~abaqus.Job.JobFromInputFile.JobFromInputFile`]] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/MdbBase.py#L40-L41)[¶](#abaqus.Mdb.MdbBase.MdbBase.jobs "Permalink to this definition")
    :   A repository of Job objects.

    lastChangedCount : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/MdbBase.py#L36-L38)[¶](#abaqus.Mdb.MdbBase.MdbBase.lastChangedCount "Permalink to this definition")
    :   A Float specifying the value of a counter associated with the Mdb object. The counter
        indicates when the Mdb object was last changed.

    meshEditOptions : --is-rst--:py:class:`~abaqus.EditMesh.MeshEditOptions.MeshEditOptions` = `<abaqus.EditMesh.MeshEditOptions.MeshEditOptions object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/MdbBase.py#L52-L54)[¶](#abaqus.Mdb.MdbBase.MdbBase.meshEditOptions "Permalink to this definition")
    :   A MeshEditOptions object specifying the undo/redo behavior when editing meshes on parts
        or part instances.

    models : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Model.Model.Model`] = `{'Model-1': <abaqus.Model.Model.Model object>}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/MdbBase.py#L56-L57)[¶](#abaqus.Mdb.MdbBase.MdbBase.models "Permalink to this definition")
    :   A repository of Model objects.

    openAuxMdb(*[pathName](#abaqus.Mdb.MdbBase.MdbBase.openAuxMdb.pathName "abaqus.Mdb.MdbBase.MdbBase.openAuxMdb.pathName (Python parameter) — A String specifying the path to the auxiliary Mdb which is to be opened.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/MdbBase.py#L199-L223)[¶](#abaqus.Mdb.MdbBase.MdbBase.openAuxMdb "Permalink to this definition")
    :   This method opens an auxiliary Mdb object on the disk at the specified location. This enables models
        from the auxiliary Mdb object to be copied into the current Mdb.

        Note

        Check [MdbBase.openAuxMdb on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mdbpyc.htm?contextscope=all#simaker-mdbopenauxmdbpyc).

        Parameters:[¶](#abaqus.Mdb.MdbBase.MdbBase.openAuxMdb-parameters "Permalink to this headline")
        :   pathName[¶](#abaqus.Mdb.MdbBase.MdbBase.openAuxMdb.pathName "Permalink to this definition")
            :   A String specifying the path to the auxiliary Mdb which is to be opened. If you do not
                provide a file extension, .cae is appended automatically to the path.

        Raises:[¶](#abaqus.Mdb.MdbBase.MdbBase.openAuxMdb-raises "Permalink to this headline")
        :   * **MdbError** – invalid model database;
              If the file is an invalid model database
            * **MdbError** – incompatible release number;
              If the file contains a model database from an Abaqus release other than the Abaqus
              release you are currently running
            * **MdbError** – cannot open file;
              If the command fails to open the model database file for reasons not mentioned above

    openMdb(*[pathName](#abaqus.Mdb.MdbBase.MdbBase.openMdb.pathName "abaqus.Mdb.MdbBase.MdbBase.openMdb.pathName (Python parameter) — A String specifying the path to the model database file to open.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/MdbBase.py#L113-L149)[¶](#abaqus.Mdb.MdbBase.MdbBase.openMdb "Permalink to this definition")
    :   This method opens an existing model database file.

        Note

        This function can be accessed by:

        ```python
        Mdb
        ```

        Note

        Check [MdbBase.openMdb on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mdbpyc.htm?contextscope=all#simaker-mdbopenmdbpyc).

        Parameters:[¶](#abaqus.Mdb.MdbBase.MdbBase.openMdb-parameters "Permalink to this headline")
        :   pathName[¶](#abaqus.Mdb.MdbBase.MdbBase.openMdb.pathName "Permalink to this definition")
            :   A String specifying the path to the model database file to open. If you do not provide a
                file extension, Abaqus/CAE attempts to open the file with .cae appended to the path.

        Returns:[¶](#abaqus.Mdb.MdbBase.MdbBase.openMdb-returns "Permalink to this headline")
        :   A Mdb object

        Return type:[¶](#abaqus.Mdb.MdbBase.MdbBase.openMdb-return-type "Permalink to this headline")
        :   `Mdb`

        Raises:[¶](#abaqus.Mdb.MdbBase.MdbBase.openMdb-raises "Permalink to this headline")
        :   * **MdbError** – invalid model database;
              If the file is an invalid model database
            * **MdbError** – incompatible release number, expected *<Abaqus release>*, got *<earlier or later Abaqus release>*;
              If the file contains a model database from an Abaqus release other than the Abaqus
              release you are currently running
            * **MdbError** – cannot open file; may be in use by another CAE session;
              If the model database file is already opened in write mode
            * **MdbError** – cannot open file;
              If the command fails to open the model database file for reasons not mentioned above

    optimizationProcesses : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Job.OptimizationProcess.OptimizationProcess`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/MdbBase.py#L49-L50)[¶](#abaqus.Mdb.MdbBase.MdbBase.optimizationProcesses "Permalink to this definition")
    :   A repository of OptimizationProcess objects.

    save()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/MdbBase.py#L159-L176)[¶](#abaqus.Mdb.MdbBase.MdbBase.save "Permalink to this definition")
    :   This method saves an Mdb object to disk at the location specified by **pathName**
        (*pathName* is a member of the Mdb object).

        Raises:[¶](#abaqus.Mdb.MdbBase.MdbBase.save-raises "Permalink to this headline")
        :   * **MdbError** – cannot save file;
              If the command fails to save the Mdb object to disk for reasons not mentioned above
            * **MdbError** – cannot save file: pathname member is empty;
              If **pathName** is empty
            * **MdbError** – “abaqus.cae” is an invalid CAE filename;
              If **pathName** is abaqus.cae

    saveAs(*[pathName](#abaqus.Mdb.MdbBase.MdbBase.saveAs.pathName "abaqus.Mdb.MdbBase.MdbBase.saveAs.pathName (Python parameter) — A String specifying the path to be used when the model database is saved to a file.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/MdbBase.py#L178-L197)[¶](#abaqus.Mdb.MdbBase.MdbBase.saveAs "Permalink to this definition")
    :   This method saves an Mdb object to disk at the specified location.

        Note

        Check [MdbBase.saveAs on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mdbpyc.htm?contextscope=all#simaker-mdbsaveaspyc).

        Parameters:[¶](#abaqus.Mdb.MdbBase.MdbBase.saveAs-parameters "Permalink to this headline")
        :   pathName[¶](#abaqus.Mdb.MdbBase.MdbBase.saveAs.pathName "Permalink to this definition")
            :   A String specifying the path to be used when the model database is saved to a file. If
                you do not provide a file extension, .cae is appended automatically to the path.

        Raises:[¶](#abaqus.Mdb.MdbBase.MdbBase.saveAs-raises "Permalink to this headline")
        :   * **MdbError** – “abaqus.cae” is an invalid CAE filename;
              If **pathName** is abaqus.cae
            * **MdbError** – cannot save file;
              If the command fails to save the Mdb object to disk for reasons not mentioned above

    version : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/MdbBase.py#L33-L34)[¶](#abaqus.Mdb.MdbBase.MdbBase.version "Permalink to this definition")
    :   An Int specifying the release number of the Mdb object in memory.

CombineOptResults(*[optResultLocation](#abaqus.Mdb.MdbCommands.CombineOptResults.optResultLocation "abaqus.Mdb.MdbCommands.CombineOptResults.optResultLocation (Python parameter) — A String specifying the path to the folder in which optimization results are present.")*, *[optIter](#abaqus.Mdb.MdbCommands.CombineOptResults.optIter "abaqus.Mdb.MdbCommands.CombineOptResults.optIter (Python parameter) — A Symbolic Constant to specify the optimization cycles from which the results should be merged.")=`abaqusConstants.INITIAL_AND_LAST`*, *[nValues](#abaqus.Mdb.MdbCommands.CombineOptResults.nValues "abaqus.Mdb.MdbCommands.CombineOptResults.nValues (Python parameter) — An Int or a tuple of Ints specifying the optimization cycles from which the results should be merged.")=`abaqusConstants.ALL`*, *[models](#abaqus.Mdb.MdbCommands.CombineOptResults.models "abaqus.Mdb.MdbCommands.CombineOptResults.models (Python parameter) — A tuple of strings specifying the list of models for which the merging of results is performed.")=`abaqusConstants.ALL`*, *[steps](#abaqus.Mdb.MdbCommands.CombineOptResults.steps "abaqus.Mdb.MdbCommands.CombineOptResults.steps (Python parameter) — A tuple of strings specifying the list of steps from the selected models to be included in the odb merge.")=`abaqusConstants.ALL`*, *[analysisFieldVariables](#abaqus.Mdb.MdbCommands.CombineOptResults.analysisFieldVariables "abaqus.Mdb.MdbCommands.CombineOptResults.analysisFieldVariables (Python parameter) — A tuple of strings specifying the list of analysisFieldVariables to be included in the odb merge.")=`abaqusConstants.ALL`*, *[includeResultsFrom](#abaqus.Mdb.MdbCommands.CombineOptResults.includeResultsFrom "abaqus.Mdb.MdbCommands.CombineOptResults.includeResultsFrom (Python parameter) — A Symbolic Constant to specify the target odb to which the results will be merged.")=`abaqusConstants.FIRST`*, *[originalModel](#abaqus.Mdb.MdbCommands.CombineOptResults.originalModel "abaqus.Mdb.MdbCommands.CombineOptResults.originalModel (Python parameter) — A String to specify the path of target odb if includeResultsFrom is set to ORIGINAL_MODEL.")=`Ellipsis`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/MdbCommands.py#L51-L93)[¶](#abaqus.Mdb.MdbCommands.CombineOptResults "Permalink to this definition")
:   This method combines the results from existing ODB files for each optimization cycle and writes a merged
    ODB file.

    Parameters:[¶](#abaqus.Mdb.MdbCommands.CombineOptResults-parameters "Permalink to this headline")
    :   optResultLocation[¶](#abaqus.Mdb.MdbCommands.CombineOptResults.optResultLocation "Permalink to this definition")
        :   A String specifying the path to the folder in which optimization results are present.

        optIter=`abaqusConstants.INITIAL_AND_LAST`[¶](#abaqus.Mdb.MdbCommands.CombineOptResults.optIter "Permalink to this definition")
        :   A Symbolic Constant to specify the optimization cycles from which the results
            should be merged. The possible values are INITIAL\_AND\_LAST, NONE, ALL, LAST,
            EVERY\_NCYCLES, SPECIFY. The default value is INITIAL\_AND\_LAST.

        nValues=`abaqusConstants.ALL`[¶](#abaqus.Mdb.MdbCommands.CombineOptResults.nValues "Permalink to this definition")
        :   An Int or a tuple of Ints specifying the optimization cycles from which the
            results should be merged. This argument is used only when EVERY\_NCYCLES or
            SPECIFY is selected for optIter. The default value is ALL.

        models=`abaqusConstants.ALL`[¶](#abaqus.Mdb.MdbCommands.CombineOptResults.models "Permalink to this definition")
        :   A tuple of strings specifying the list of models for which the merging of
            results is performed. The default value is ALL.

        steps=`abaqusConstants.ALL`[¶](#abaqus.Mdb.MdbCommands.CombineOptResults.steps "Permalink to this definition")
        :   A tuple of strings specifying the list of steps from the selected models to
            be included in the odb merge. The default value is ALL.

        analysisFieldVariables=`abaqusConstants.ALL`[¶](#abaqus.Mdb.MdbCommands.CombineOptResults.analysisFieldVariables "Permalink to this definition")
        :   A tuple of strings specifying the list of analysisFieldVariables to be
            included in the odb merge. The default value is ALL.

        includeResultsFrom=`abaqusConstants.FIRST`[¶](#abaqus.Mdb.MdbCommands.CombineOptResults.includeResultsFrom "Permalink to this definition")
        :   A Symbolic Constant to specify the target odb to which the results will be
            merged. The possible values are ORIGINAL\_MODEL, FIRST or LAST. The default
            value is FIRST.

        originalModel=`Ellipsis`[¶](#abaqus.Mdb.MdbCommands.CombineOptResults.originalModel "Permalink to this definition")
        :   A String to specify the path of target odb if includeResultsFrom is set to
            ORIGINAL\_MODEL.

openMdb(*[pathName](#abaqus.Mdb.MdbCommands.openMdb.pathName "abaqus.Mdb.MdbCommands.openMdb.pathName (Python parameter) — A String specifying the path to the model database file to open.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/MdbCommands.py#L96-L132)[¶](#abaqus.Mdb.MdbCommands.openMdb "Permalink to this definition")
:   This method opens an existing model database file.

    Note

    This function can be accessed by:

    ```python
    Mdb
    ```

    Note

    Check [MdbCommands.openMdb on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-functionmdbcommandspyc.htm?contextscope=all#simaker-functionmdbcommandsopenmdbpyc).

    Parameters:[¶](#abaqus.Mdb.MdbCommands.openMdb-parameters "Permalink to this headline")
    :   pathName[¶](#abaqus.Mdb.MdbCommands.openMdb.pathName "Permalink to this definition")
        :   A String specifying the path to the model database file to open. If you do not provide a
            file extension, Abaqus/CAE attempts to open the file with .cae appended to the path.

    Returns:[¶](#abaqus.Mdb.MdbCommands.openMdb-returns "Permalink to this headline")
    :   A Mdb object

    Return type:[¶](#abaqus.Mdb.MdbCommands.openMdb-return-type "Permalink to this headline")
    :   `Mdb`

    Raises:[¶](#abaqus.Mdb.MdbCommands.openMdb-raises "Permalink to this headline")
    :   * **MdbError** – invalid model database;
          If the file is an invalid model database
        * **MdbError** – incompatible release number, expected *<Abaqus release>*, got *<earlier or later Abaqus release>*;
          If the file contains a model database from an Abaqus release other than the Abaqus
          release you are currently running
        * **MdbError** – cannot open file; may be in use by another CAE session;
          If the model database file is already opened in write mode
        * **MdbError** – cannot open file;
          If the command fails to open the model database file for reasons not mentioned above

upgradeMdb(*[existingMdbPath](#abaqus.Mdb.MdbCommands.upgradeMdb.existingMdbPath "abaqus.Mdb.MdbCommands.upgradeMdb.existingMdbPath (Python parameter) — A String specifying the path to the file containing the model database to be upgraded.")*, *[upgradedMdbPath](#abaqus.Mdb.MdbCommands.upgradeMdb.upgradedMdbPath "abaqus.Mdb.MdbCommands.upgradeMdb.upgradedMdbPath (Python parameter) — A String specifying the path to the file that will contain the upgraded model database.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mdb/MdbCommands.py#L27-L48)[¶](#abaqus.Mdb.MdbCommands.upgradeMdb "Permalink to this definition")
:   This method upgrades an existing Mdb object to the current release and writes the upgraded version of the
    Mdb object to a file. In addition, Abaqus/CAE writes.

    information about the status of the upgrade to the log file ( upgradedMdbPath.log
    ).

    Parameters:[¶](#abaqus.Mdb.MdbCommands.upgradeMdb-parameters "Permalink to this headline")
    :   existingMdbPath[¶](#abaqus.Mdb.MdbCommands.upgradeMdb.existingMdbPath "Permalink to this definition")
        :   A String specifying the path to the file containing the model database to be
            upgraded.

        upgradedMdbPath[¶](#abaqus.Mdb.MdbCommands.upgradeMdb.upgradedMdbPath "Permalink to this definition")
        :   A String specifying the path to the file that will contain the upgraded model
            database.

    Raises:[¶](#abaqus.Mdb.MdbCommands.upgradeMdb-raises "Permalink to this headline")
    :   **MdbError** – Cannot convert file

[Back to top](#)