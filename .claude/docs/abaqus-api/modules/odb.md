# Abaqus ODB Module API Reference

> Source: [https://hailin.wang/abqpy/en/2025/reference/odb.html](https://hailin.wang/abqpy/en/2025/reference/odb.html)
> Downloaded for offline use by Claude Code skills.

---

# Abaqus Output Database[¶](#abaqus-output-database "Permalink to this heading")

The Python ODB API commands are used to read and write data from an output database (.odb) file. The path to the Odb object can be via the session.odbs repository or via a variable. In this chapter the Access and Path statements refer to a variable called odb that represents an existing Odb object.

## Classes[¶](#classes "Permalink to this heading")

### Odb[¶](#odb "Permalink to this heading")

*class* Odb(*[name](#abaqus.Odb.Odb.Odb "abaqus.Odb.Odb.Odb.__init__.name (Python parameter)")*, *[analysisTitle](#abaqus.Odb.Odb.Odb "abaqus.Odb.Odb.Odb.__init__.analysisTitle (Python parameter)")=`''`*, *[description](#abaqus.Odb.Odb.Odb "abaqus.Odb.Odb.Odb.__init__.description (Python parameter)")=`''`*, *[path](#abaqus.Odb.Odb.Odb "abaqus.Odb.Odb.Odb.__init__.path (Python parameter)")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/Odb.py#L18-L196)[¶](#abaqus.Odb.Odb.Odb "Permalink to this definition")
:   Bases: [`AmplitudeOdb`](mdb/model/amplitude.html#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb (Python class) — Bases: OdbBase"), [`FilterOdb`](mdb/model/filter.html#abaqus.Filter.FilterOdb.FilterOdb "abaqus.Filter.FilterOdb.FilterOdb (Python class) — Bases: OdbBase"), [`MaterialOdb`](mdb/model/material.html#abaqus.Material.MaterialOdb.MaterialOdb "abaqus.Material.MaterialOdb.MaterialOdb (Python class) — Bases: OdbBase"), [`BeamSectionProfileOdb`](mdb/model/profile.html#abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb "abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb (Python class) — Bases: OdbBase"), [`Displayable`](session/canvas.html#abaqus.Canvas.ViewportBase.Displayable "abaqus.Canvas.Displayable.Displayable (Python class)")

    The Odb object is the in-memory representation of an output database (ODB) file.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name]
    ```

    Note

    Check [Odb on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbpyc.htm?contextscope=all).

    Public Data Attributes:

    Inherited from [`OdbBase`](#abaqus.Odb.OdbBase.OdbBase "abaqus.Odb.OdbBase.OdbBase (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | [`isReadOnly`](#abaqus.Odb.OdbBase.OdbBase.isReadOnly "abaqus.Odb.OdbBase.OdbBase.isReadOnly (Python attribute) — A Boolean specifying whether the output database was opened with read-only access.") | A Boolean specifying whether the output database was opened with read-only access. |
    | [`amplitudes`](#abaqus.Odb.OdbBase.OdbBase.amplitudes "abaqus.Odb.OdbBase.OdbBase.amplitudes (Python attribute) — A repository of Amplitude objects.") | A repository of Amplitude objects. |
    | [`filters`](#abaqus.Odb.OdbBase.OdbBase.filters "abaqus.Odb.OdbBase.OdbBase.filters (Python attribute) — A repository of Filter objects.") | A repository of Filter objects. |
    | [`rootAssembly`](#abaqus.Odb.OdbBase.OdbBase.rootAssembly "abaqus.Odb.OdbBase.OdbBase.rootAssembly (Python attribute) — An OdbAssembly object.") | An OdbAssembly object. |
    | [`jobData`](#abaqus.Odb.OdbBase.OdbBase.jobData "abaqus.Odb.OdbBase.OdbBase.jobData (Python attribute) — A JobData object.") | A JobData object. |
    | [`parts`](#abaqus.Odb.OdbBase.OdbBase.parts "abaqus.Odb.OdbBase.OdbBase.parts (Python attribute) — A repository of OdbPart objects.") | A repository of OdbPart objects. |
    | [`materials`](#abaqus.Odb.OdbBase.OdbBase.materials "abaqus.Odb.OdbBase.OdbBase.materials (Python attribute) — A repository of Material objects.") | A repository of Material objects. |
    | [`steps`](#abaqus.Odb.OdbBase.OdbBase.steps "abaqus.Odb.OdbBase.OdbBase.steps (Python attribute) — A repository of OdbStep objects.") | A repository of OdbStep objects. |
    | [`sections`](#abaqus.Odb.OdbBase.OdbBase.sections "abaqus.Odb.OdbBase.OdbBase.sections (Python attribute) — A repository of Section objects.") | A repository of Section objects. |
    | [`sectionCategories`](#abaqus.Odb.OdbBase.OdbBase.sectionCategories "abaqus.Odb.OdbBase.OdbBase.sectionCategories (Python attribute) — A repository of SectionCategory objects.") | A repository of SectionCategory objects. |
    | [`sectorDefinition`](#abaqus.Odb.OdbBase.OdbBase.sectorDefinition "abaqus.Odb.OdbBase.OdbBase.sectorDefinition (Python attribute) — A SectorDefinition object.") | A SectorDefinition object. |
    | [`userData`](#abaqus.Odb.OdbBase.OdbBase.userData "abaqus.Odb.OdbBase.OdbBase.userData (Python attribute) — A UserData object.") | A UserData object. |
    | [`customData`](#abaqus.Odb.OdbBase.OdbBase.customData "abaqus.Odb.OdbBase.OdbBase.customData (Python attribute) — A RepositorySupport object.") | A RepositorySupport object. |
    | [`profiles`](#abaqus.Odb.OdbBase.OdbBase.profiles "abaqus.Odb.OdbBase.OdbBase.profiles (Python attribute) — A repository of Profile objects.") | A repository of Profile objects. |

    Public Methods:

    |  |  |
    | --- | --- |
    | [`Part`](#abaqus.Odb.Odb.Odb.Part "abaqus.Odb.Odb.Odb.Part (Python method) — This method creates an OdbPart object. Nodes and elements are added to this object at a later stage.")(name, embeddedSpace, type) | This method creates an OdbPart object. |
    | [`Step`](#abaqus.Odb.Odb.Odb.Step "abaqus.Odb.Odb.Odb.Step (Python method) — This method creates an OdbStep object.")(name, description, domain[, ...]) | This method creates an OdbStep object. |
    | [`SectionCategory`](#abaqus.Odb.Odb.Odb.SectionCategory "abaqus.Odb.Odb.Odb.SectionCategory (Python method) — This method creates a SectionCategory object.")(name, description) | This method creates a SectionCategory object. |

    Inherited from [`AmplitudeOdb`](mdb/model/amplitude.html#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb (Python class) — Bases: OdbBase")

    |  |  |
    | --- | --- |
    | [`ActuatorAmplitude`](mdb/model/amplitude.html#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ActuatorAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ActuatorAmplitude (Python method) — This method creates a ActuatorAmplitude object.")(name[, timeSpan]) | This method creates a ActuatorAmplitude object. |
    | [`DecayAmplitude`](mdb/model/amplitude.html#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.DecayAmplitude (Python method) — This method creates a DecayAmplitude object.")(name, initial, maximum, ...) | This method creates a DecayAmplitude object. |
    | [`EquallySpacedAmplitude`](mdb/model/amplitude.html#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.EquallySpacedAmplitude (Python method) — This method creates an EquallySpacedAmplitude object.")(name, fixedInterval, data) | This method creates an EquallySpacedAmplitude object. |
    | [`ModulatedAmplitude`](mdb/model/amplitude.html#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.ModulatedAmplitude (Python method) — This method creates a ModulatedAmplitude object.")(name, initial, magnitude, ...) | This method creates a ModulatedAmplitude object. |
    | [`PeriodicAmplitude`](mdb/model/amplitude.html#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PeriodicAmplitude (Python method) — This method creates a PeriodicAmplitude object.")(name, frequency, start, ...) | This method creates a PeriodicAmplitude object. |
    | [`PsdDefinition`](mdb/model/amplitude.html#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.PsdDefinition (Python method) — This method creates a PsdDefinition object.")(name, data[, unitType, ...]) | This method creates a PsdDefinition object. |
    | [`SmoothStepAmplitude`](mdb/model/amplitude.html#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SmoothStepAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SmoothStepAmplitude (Python method) — This method creates a SmoothStepAmplitude object.")(name, data[, timeSpan]) | This method creates a SmoothStepAmplitude object. |
    | [`SolutionDependentAmplitude`](mdb/model/amplitude.html#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SolutionDependentAmplitude (Python method) — This method creates a SolutionDependentAmplitude object.")(name[, initial, ...]) | This method creates a SolutionDependentAmplitude object. |
    | [`SpectrumAmplitude`](mdb/model/amplitude.html#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.SpectrumAmplitude (Python method) — This method creates a SpectrumAmplitude object.")(name, method, data[, ...]) | This method creates a SpectrumAmplitude object. |
    | [`TabularAmplitude`](mdb/model/amplitude.html#abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.TabularAmplitude "abaqus.Amplitude.AmplitudeOdb.AmplitudeOdb.TabularAmplitude (Python method) — This method creates a TabularAmplitude object.")(name, data[, smooth, timeSpan]) | This method creates a TabularAmplitude object. |

    Inherited from [`FilterOdb`](mdb/model/filter.html#abaqus.Filter.FilterOdb.FilterOdb "abaqus.Filter.FilterOdb.FilterOdb (Python class) — Bases: OdbBase")

    |  |  |
    | --- | --- |
    | [`ButterworthFilter`](mdb/model/filter.html#abaqus.Filter.FilterOdb.FilterOdb.ButterworthFilter "abaqus.Filter.FilterOdb.FilterOdb.ButterworthFilter (Python method) — This method creates a ButterworthFilter object.")(name, cutoffFrequency[, ...]) | This method creates a ButterworthFilter object. |
    | [`Chebyshev1Filter`](mdb/model/filter.html#abaqus.Filter.FilterOdb.FilterOdb.Chebyshev1Filter "abaqus.Filter.FilterOdb.FilterOdb.Chebyshev1Filter (Python method) — This method creates a Chebyshev1Filter object.")(name, cutoffFrequency[, ...]) | This method creates a Chebyshev1Filter object. |
    | [`Chebyshev2Filter`](mdb/model/filter.html#abaqus.Filter.FilterOdb.FilterOdb.Chebyshev2Filter "abaqus.Filter.FilterOdb.FilterOdb.Chebyshev2Filter (Python method) — This method creates a Chebyshev2Filter object.")(name, cutoffFrequency[, ...]) | This method creates a Chebyshev2Filter object. |
    | [`OperatorFilter`](mdb/model/filter.html#abaqus.Filter.FilterOdb.FilterOdb.OperatorFilter "abaqus.Filter.FilterOdb.FilterOdb.OperatorFilter (Python method) — This method creates an OperatorFilter object.")(name, cutoffFrequency[, ...]) | This method creates an OperatorFilter object. |

    Inherited from [`MaterialOdb`](mdb/model/material.html#abaqus.Material.MaterialOdb.MaterialOdb "abaqus.Material.MaterialOdb.MaterialOdb (Python class) — Bases: OdbBase")

    |  |  |
    | --- | --- |
    | [`Material`](mdb/model/material.html#abaqus.Material.MaterialOdb.MaterialOdb.Material "abaqus.Material.MaterialOdb.MaterialOdb.Material (Python method) — This method creates a Material object.")(name[, description, materialIdentifier]) | This method creates a Material object. |

    Inherited from [`BeamSectionProfileOdb`](mdb/model/profile.html#abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb "abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb (Python class) — Bases: OdbBase")

    |  |  |
    | --- | --- |
    | [`ArbitraryProfile`](mdb/model/profile.html#abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.ArbitraryProfile "abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.ArbitraryProfile (Python method) — This method creates a ArbitraryProfile object.")(name, table) | This method creates a ArbitraryProfile object. |
    | [`BoxProfile`](mdb/model/profile.html#abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.BoxProfile "abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.BoxProfile (Python method) — This method creates a BoxProfile object.")(name, a, b, uniformThickness, t1) | This method creates a BoxProfile object. |
    | [`ChannelProfile`](mdb/model/profile.html#abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.ChannelProfile "abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.ChannelProfile (Python method) — This method creates a ChannelProfile object.")(name, l, h, b1, b2, t1, t2, t3, o) | This method creates a ChannelProfile object. |
    | [`CircularProfile`](mdb/model/profile.html#abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.CircularProfile "abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.CircularProfile (Python method) — This method creates a CircularProfile object.")(name, r) | This method creates a CircularProfile object. |
    | [`GeneralizedProfile`](mdb/model/profile.html#abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.GeneralizedProfile "abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.GeneralizedProfile (Python method) — This method creates a GeneralizedProfile object.")(name, area, i11, i12, ...) | This method creates a GeneralizedProfile object. |
    | [`HatProfile`](mdb/model/profile.html#abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.HatProfile "abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.HatProfile (Python method) — This method creates a HatProfile object.")(name, l, h, b, b1, b2, t1, t2, t3) | This method creates a HatProfile object. |
    | [`HexagonalProfile`](mdb/model/profile.html#abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.HexagonalProfile "abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.HexagonalProfile (Python method) — This method creates a HexagonalProfile object.")(name, r, t) | This method creates a HexagonalProfile object. |
    | [`IProfile`](mdb/model/profile.html#abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.IProfile "abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.IProfile (Python method) — This method creates an IProfile object.")(name, l, h, b1, b2, t1, t2, t3) | This method creates an IProfile object. |
    | [`LProfile`](mdb/model/profile.html#abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.LProfile "abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.LProfile (Python method) — This method creates a LProfile object.")(name, a, b, t1, t2) | This method creates a LProfile object. |
    | [`PipeProfile`](mdb/model/profile.html#abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.PipeProfile "abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.PipeProfile (Python method) — This method creates a PipeProfile object.")(name, r, t) | This method creates a PipeProfile object. |
    | [`RectangularProfile`](mdb/model/profile.html#abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.RectangularProfile "abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.RectangularProfile (Python method) — This method creates a RectangularProfile object.")(name, a, b) | This method creates a RectangularProfile object. |
    | [`TProfile`](mdb/model/profile.html#abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.TProfile "abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.TProfile (Python method) — This method creates a TProfile object.")(name, b, h, l, tf, tw) | This method creates a TProfile object. |
    | [`TrapezoidalProfile`](mdb/model/profile.html#abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.TrapezoidalProfile "abaqus.BeamSectionProfile.BeamSectionProfileOdb.BeamSectionProfileOdb.TrapezoidalProfile (Python method) — This method creates a TrapezoidalProfile object.")(name, a, b, c, d) | This method creates a TrapezoidalProfile object. |

    Inherited from [`OdbBase`](#abaqus.Odb.OdbBase.OdbBase "abaqus.Odb.OdbBase.OdbBase (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | `__init__`(name[, analysisTitle, description, ...]) | This method creates a new Odb object. |
    | [`close`](#abaqus.Odb.OdbBase.OdbBase.close "abaqus.Odb.OdbBase.OdbBase.close (Python method) — This method closes an output database.")() | This method closes an output database. |
    | [`getFrame`](#abaqus.Odb.OdbBase.OdbBase.getFrame "abaqus.Odb.OdbBase.OdbBase.getFrame (Python method) — This method returns the frame at the specified time, frequency, or mode. It will not interpolate values between frames. The method is not applicable to an Odb object containing steps with different domains or to an Odb object containing a step with load case specific data.")(frameValue[, match]) | This method returns the frame at the specified time, frequency, or mode. |
    | [`save`](#abaqus.Odb.OdbBase.OdbBase.save "abaqus.Odb.OdbBase.OdbBase.save (Python method) — This method saves output to an output database (.odb ) file.")() | This method saves output to an output database (.odb ) file. |
    | [`update`](#abaqus.Odb.OdbBase.OdbBase.update "abaqus.Odb.OdbBase.OdbBase.update (Python method) — This method is used to update an Odb object in memory while an Abaqus analysis writes data to the associated output database. update checks if additional steps have been written to the output database since it was opened or last updated. If additional steps have been written to the output database, update adds them to the Odb object.")() | This method is used to update an Odb object in memory while an Abaqus analysis writes data to the associated output database. |

    ---

    Member Details:

    Part(*[name](#abaqus.Odb.Odb.Odb.Part.name "abaqus.Odb.Odb.Odb.Part.name (Python parameter) — A String specifying the part name.")*, *[embeddedSpace](#abaqus.Odb.Odb.Odb.Part.embeddedSpace "abaqus.Odb.Odb.Odb.Part.embeddedSpace (Python parameter) — A SymbolicConstant specifying the dimensionality of the Part object.")*, *[type](#abaqus.Odb.Odb.Odb.Part.type "abaqus.Odb.Odb.Odb.Part.type (Python parameter) — A SymbolicConstant specifying the type of the Part object.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/Odb.py#L29-L60)[¶](#abaqus.Odb.Odb.Odb.Part "Permalink to this definition")
    :   This method creates an OdbPart object. Nodes and elements are added to this object at a later stage.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].Part
        ```

        Note

        Check [Part on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.Odb.Odb.Part-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.Odb.Odb.Part.name "Permalink to this definition")
            :   A String specifying the part name.

            embeddedSpace[¶](#abaqus.Odb.Odb.Odb.Part.embeddedSpace "Permalink to this definition")
            :   A SymbolicConstant specifying the dimensionality of the Part object. Possible values are
                THREE\_D, TWO\_D\_PLANAR, and AXISYMMETRIC.

            type[¶](#abaqus.Odb.Odb.Odb.Part.type "Permalink to this definition")
            :   A SymbolicConstant specifying the type of the Part object. Possible values are
                DEFORMABLE\_BODY and ANALYTIC\_RIGID\_SURFACE.

        Returns:[¶](#abaqus.Odb.Odb.Odb.Part-returns "Permalink to this headline")
        :   An OdbPart object.

        Return type:[¶](#abaqus.Odb.Odb.Odb.Part-return-type "Permalink to this headline")
        :   `OdbPart`

    SectionCategory(*[name](#abaqus.Odb.Odb.Odb.SectionCategory.name "abaqus.Odb.Odb.Odb.SectionCategory.name (Python parameter) — A String specifying the name of the category.")*, *[description](#abaqus.Odb.Odb.Odb.SectionCategory.description "abaqus.Odb.Odb.Odb.SectionCategory.description (Python parameter) — A String specifying the description of the category.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/Odb.py#L174-L196)[¶](#abaqus.Odb.Odb.Odb.SectionCategory "Permalink to this definition")
    :   This method creates a SectionCategory object.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].SectionCategory
        ```

        Note

        Check [SectionCategory on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectioncategorypyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.Odb.Odb.SectionCategory-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.Odb.Odb.SectionCategory.name "Permalink to this definition")
            :   A String specifying the name of the category.

            description[¶](#abaqus.Odb.Odb.Odb.SectionCategory.description "Permalink to this definition")
            :   A String specifying the description of the category.

        Returns:[¶](#abaqus.Odb.Odb.Odb.SectionCategory-returns "Permalink to this headline")
        :   A SectionCategory object.

        Return type:[¶](#abaqus.Odb.Odb.Odb.SectionCategory-return-type "Permalink to this headline")
        :   [`SectionCategory`](#abaqus.Odb.Odb.Odb.SectionCategory "abaqus.Odb.Odb.Odb.SectionCategory (Python method) — This method creates a SectionCategory object.")

    Step(*[name](#abaqus.Odb.Odb.Odb.Step.name "abaqus.Odb.Odb.Odb.Step.name (Python parameter) — A String specifying the repository key.")*, *[description](#abaqus.Odb.Odb.Odb.Step.description "abaqus.Odb.Odb.Odb.Step.description (Python parameter) — A String specifying the step description.")*, *[domain](#abaqus.Odb.Odb.Odb.Step.domain "abaqus.Odb.Odb.Odb.Step.domain (Python parameter) — A SymbolicConstant specifying the domain of the step.")*, *[timePeriod](#abaqus.Odb.Odb.Odb.Step.timePeriod "abaqus.Odb.Odb.Odb.Step.timePeriod (Python parameter) — A Float specifying the time period of the step.")=`0`*, *[previousStepName](#abaqus.Odb.Odb.Odb.Step.previousStepName "abaqus.Odb.Odb.Odb.Step.previousStepName (Python parameter) — A String specifying the preceding step.")=`''`*, *[procedure](#abaqus.Odb.Odb.Odb.Step.procedure "abaqus.Odb.Odb.Odb.Step.procedure (Python parameter) — A String specifying the step procedure.")=`''`*, *[totalTime](#abaqus.Odb.Odb.Odb.Step.totalTime "abaqus.Odb.Odb.Odb.Step.totalTime (Python parameter) — A Float specifying the analysis time spend in all the steps previous to this step.")=`-1.0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/Odb.py#L62-L172)[¶](#abaqus.Odb.Odb.Odb.Step "Permalink to this definition")
    :   This method creates an OdbStep object.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].Step
        ```

        Note

        Check [Step on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-steppyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.Odb.Odb.Step-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.Odb.Odb.Step.name "Permalink to this definition")
            :   A String specifying the repository key.

            description[¶](#abaqus.Odb.Odb.Odb.Step.description "Permalink to this definition")
            :   A String specifying the step description.

            domain[¶](#abaqus.Odb.Odb.Odb.Step.domain "Permalink to this definition")
            :   A SymbolicConstant specifying the domain of the step. Possible values are TIME,
                FREQUENCY, ARC\_LENGTH, and MODAL.The type of OdbFrame object that can be created for
                this step is based on the value of the **domain** argument.

            timePeriod=`0`[¶](#abaqus.Odb.Odb.Odb.Step.timePeriod "Permalink to this definition")
            :   A Float specifying the time period of the step. **timePeriod** is required if
                **domain** = TIME; otherwise, this argument is not applicable. The default value is 0.0.

            previousStepName=`''`[¶](#abaqus.Odb.Odb.Odb.Step.previousStepName "Permalink to this definition")
            :   A String specifying the preceding step. If **previousStepName** is the empty string, the
                last step in the repository is used. If **previousStepName** is not the last step, this
                will result in a change to the **previousStepName** member of the step that was in that
                position. A special value ‘Initial’ refers to the internal initial model step and may be
                used exclusively for inserting a new step at the first position before any other
                existing steps. The default value is an empty string.

            procedure=`''`[¶](#abaqus.Odb.Odb.Odb.Step.procedure "Permalink to this definition")
            :   A String specifying the step procedure. The default value is an empty string. The
                following is the list of valid procedures:

                * \*ANNEAL
                * \*BUCKLE
                * \*COMPLEX FREQUENCY
                * \*COUPLED TEMPERATURE-DISPLACEMENT
                * \*COUPLED TEMPERATURE-DISPLACEMENT, CETOL
                * \*COUPLED TEMPERATURE-DISPLACEMENT, STEADY STATE
                * \*COUPLED THERMAL-ELECTRICAL, STEADY STATE
                * \*COUPLED THERMAL-ELECTRICAL
                * \*COUPLED THERMAL-ELECTRICAL, DELTMX
                * \*DYNAMIC
                * \*DYNAMIC, DIRECT
                * \*DYNAMIC, EXPLICIT
                * \*DYNAMIC, SUBSPACE
                * \*DYNAMIC TEMPERATURE-DISPLACEMENT, EXPLICT
                * \*ELECTROMAGNETIC, HIGH FREQUENCY, TIME HARMONIC
                * \*ELECTROMAGNETIC, LOW FREQUENCY, TIME DOMAIN
                * \*ELECTROMAGNETIC, LOW FREQUENCY, TIME DOMAIN, DIRECT
                * \*ELECTROMAGNETIC, LOW FREQUENCY, TIME HARMONIC
                * \*FREQUENCY
                * \*GEOSTATIC
                * \*HEAT TRANSFER
                * \*HEAT TRANSFER, DELTAMX=\_\_
                * \*HEAT TRANSFER, STEADY STATE
                * \*MAGNETOSTATIC
                * \*MAGNETOSTATIC, DIRECT
                * \*MASS DIFFUSION
                * \*MASS DIFFUSION, DCMAX=
                * \*MASS DIFFUSION, STEADY STATE
                * \*MODAL DYNAMIC
                * \*RANDOM RESPONSE
                * \*RESPONSE SPECTRUM
                * \*SOILS
                * \*SOILS, CETOL/UTOL
                * \*SOILS, CONSOLIDATION
                * \*SOILS, CONSOLIDATION, CETOL/UTOL
                * \*STATIC
                * \*STATIC, DIRECT
                * \*STATIC, RIKS
                * \*STEADY STATE DYNAMICS
                * \*STEADY STATE TRANSPORT
                * \*STEADY STATE TRANSPORT, DIRECT
                * \*STEP PERTURBATION, \*STATIC
                * \*SUBSTRUCTURE GENERATE
                * \*USA ADDDED MASS GENERATION
                * \*VISCO

            totalTime=`-1.0`[¶](#abaqus.Odb.Odb.Odb.Step.totalTime "Permalink to this definition")
            :   A Float specifying the analysis time spend in all the steps previous to this step. The
                default value is −1.0.

        Returns:[¶](#abaqus.Odb.Odb.Odb.Step-returns "Permalink to this headline")
        :   An OdbStep object.

        Return type:[¶](#abaqus.Odb.Odb.Odb.Step-return-type "Permalink to this headline")
        :   `OdbStep`

        Raises:[¶](#abaqus.Odb.Odb.Odb.Step-raises "Permalink to this headline")
        :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.13)") – previousStepName is invalid, If **previousStepName** is invalid.

### Other Classes[¶](#other-classes "Permalink to this heading")

*class* AnalyticSurface[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbRigidBody.py#L9-L40)[¶](#abaqus.Odb.OdbRigidBody.AnalyticSurface "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The AnalyticSurface object is a geometric surface that can be described with straight and/or curved line
    segments.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].parts[name].analyticSurface
    session.odbs[name].rootAssembly.instances[name].analyticSurface
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.analyticSurface
    ```

    Note

    Check [AnalyticSurface on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticsurfacepyc.htm?contextscope=all).

    Member Details:

    filletRadius : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbRigidBody.py#L30-L32)[¶](#abaqus.Odb.OdbRigidBody.AnalyticSurface.filletRadius "Permalink to this definition")
    :   A Float specifying radius of curvature to smooth discontinuities between adjoining
        segments. The default value is 0.0.

    localCoordData : --is-rst--:py:class:`tuple`\[:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`], :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbRigidBody.py#L9-L40)[¶](#abaqus.Odb.OdbRigidBody.AnalyticSurface.localCoordData "Permalink to this definition")
    :   A tuple of tuples of Floats specifying the global coordinates of points representing the
        local coordinate system, if used.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbRigidBody.py#L23-L24)[¶](#abaqus.Odb.OdbRigidBody.AnalyticSurface.name "Permalink to this definition")
    :   A String specifying the name of the analytic surface.

    segments : --is-rst--:py:class:`~abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment` = `<abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbRigidBody.py#L34-L36)[¶](#abaqus.Odb.OdbRigidBody.AnalyticSurface.segments "Permalink to this definition")
    :   An OdbSequenceAnalyticSurfaceSegment object specifying the profile associated with the
        surface.

    type : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbRigidBody.py)[¶](#abaqus.Odb.OdbRigidBody.AnalyticSurface.type "Permalink to this definition")
    :   A SymbolicConstant specifying the type of AnalyticSurface object. Possible values are
        SEGMENTS, CYLINDER, and REVOLUTION.

*class* OdbSequenceAnalyticSurfaceSegment[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbSequenceAnalyticSurfaceSegment.py#L6-L82)[¶](#abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    A sequence of AnalyticSurfaceSegment describing an analytic surface profile.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].parts[name].analyticSurface.segments
    session.odbs[name].rootAssembly.instances[name].analyticSurface.segments
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.analyticSurface.segments
    ```

    Note

    Check [OdbSequenceAnalyticSurfaceSegment on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsequenceanalyticsurfacesegmentpyc.htm?contextscope=all).

    Member Details:

    Circle(*[center](#abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Circle.center "abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Circle.center (Python parameter) — A sequence of Floats specifying the coordinates of center of the circular segment.")*, *[endPoint](#abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Circle.endPoint "abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Circle.endPoint (Python parameter) — A sequence of Floats specifying the coordinates of end point of the circular segment.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbSequenceAnalyticSurfaceSegment.py#L57-L68)[¶](#abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Circle "Permalink to this definition")
    :   This method adds a AnalyticSurfaceSegment describing a circular segment of the surface profile.

        Note

        Check [Circle on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-circlepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Circle-parameters "Permalink to this headline")
        :   center[¶](#abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Circle.center "Permalink to this definition")
            :   A sequence of Floats specifying the coordinates of center of the circular segment.

            endPoint[¶](#abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Circle.endPoint "Permalink to this definition")
            :   A sequence of Floats specifying the coordinates of end point of the circular segment.

    Line(*[endPoint](#abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Line.endPoint "abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Line.endPoint (Python parameter) — A sequence of Floats specifying the coordinates of end point.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbSequenceAnalyticSurfaceSegment.py#L46-L55)[¶](#abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Line "Permalink to this definition")
    :   This method adds a AnalyticSurfaceSegment describing the line segment of the surface profile.

        Note

        Check [Line on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-linepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Line-parameters "Permalink to this headline")
        :   endPoint[¶](#abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Line.endPoint "Permalink to this definition")
            :   A sequence of Floats specifying the coordinates of end point.

    Parabola(*[middlePoint](#abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Parabola.middlePoint "abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Parabola.middlePoint (Python parameter) — A sequence of Floats specifying the coordinates of middle point of the parabolic segment.")*, *[endPoint](#abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Parabola.endPoint "abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Parabola.endPoint (Python parameter) — A sequence of Floats specifying the coordinates of end point of the parabolic segment.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbSequenceAnalyticSurfaceSegment.py#L70-L82)[¶](#abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Parabola "Permalink to this definition")
    :   This method adds a AnalyticSurfaceSegment describing a parabolic segment of the surface profile.

        Note

        Check [Parabola on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-parabolapyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Parabola-parameters "Permalink to this headline")
        :   middlePoint[¶](#abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Parabola.middlePoint "Permalink to this definition")
            :   A sequence of Floats specifying the coordinates of middle point of the parabolic
                segment.

            endPoint[¶](#abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Parabola.endPoint "Permalink to this definition")
            :   A sequence of Floats specifying the coordinates of end point of the parabolic segment.

    Start(*[origin](#abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Start.origin "abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Start.origin (Python parameter) — A sequence of Floats specifying the coordinates of start point.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbSequenceAnalyticSurfaceSegment.py#L35-L44)[¶](#abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Start "Permalink to this definition")
    :   This method adds a AnalyticSurfaceSegment describing the first segment of the surface profile.

        Note

        Check [Start on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-startpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Start-parameters "Permalink to this headline")
        :   origin[¶](#abaqus.Odb.OdbSequenceAnalyticSurfaceSegment.OdbSequenceAnalyticSurfaceSegment.Start.origin "Permalink to this definition")
            :   A sequence of Floats specifying the coordinates of start point.

*class* AnalyticSurfaceSegment(*[type](#abaqus.Odb.OdbPartBase.AnalyticSurfaceSegment "abaqus.Odb.OdbPartBase.AnalyticSurfaceSegment.__init__.type (Python parameter)")*, *[data](#abaqus.Odb.OdbPartBase.AnalyticSurfaceSegment "abaqus.Odb.OdbPartBase.AnalyticSurfaceSegment.__init__.data (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py#L11-L63)[¶](#abaqus.Odb.OdbPartBase.AnalyticSurfaceSegment "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    An individual segment of the analytic surface.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].parts[name].analyticSurface.segments[i]
    session.odbs[name].rootAssembly.instances[name].analyticSurface.segments[i]
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.analyticSurface.segments[i]
    ```

    Note

    Check [AnalyticSurfaceSegment on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticsurfacesegmentpyc.htm?contextscope=all).

    Member Details:

    data : --is-rst--:py:class:`tuple`\[:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`], :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py#L28-L34)[¶](#abaqus.Odb.OdbPartBase.AnalyticSurfaceSegment.data "Permalink to this definition")
    :   A sequence of sequences of Floats specifying the coordinates of point/s representing the
        segment of the AnalyticSurface object. If **type** = CIRCLE, the first row contains
        coordinates of the end point and the second row contains coordinates of the center
        point. If **type** = PARABOLA, the first row contains coordinates of the middle point and
        the second row contains coordinates of the end point. If **type** = START or **type** = LINE, a
        single row contains coordinates of the start/end point.

    type : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py)[¶](#abaqus.Odb.OdbPartBase.AnalyticSurfaceSegment.type "Permalink to this definition")
    :   A SymbolicConstant specifying the type of AnalyticSurfaceSegment. Possible values are
        START, LINE, CIRCLE, and PARABOLA.

*class* BeamOrientation[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/BeamOrientationArray.py#L9-L32)[¶](#abaqus.Odb.BeamOrientationArray.BeamOrientation "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The BeamOrientation object represents the direction of the first beam section axis n1n1. Specifying the
    beam orientation using an additional node in the element connectivity list is not supported.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].parts[name].beamOrientations[i]
    session.odbs[name].rootAssembly.instances[name].beamOrientations[i]
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.beamOrientations[i]
    ```

    Note

    Check [BeamOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-beamorientationpyc.htm?contextscope=all).

    Member Details:

    method : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/BeamOrientationArray.py)[¶](#abaqus.Odb.BeamOrientationArray.BeamOrientation.method "Permalink to this definition")
    :   A SymbolicConstant specifying the orientation assignment method. Possible values are
        N1\_COSINES, CSYS, and VECT.

    region : --is-rst--:py:class:`~abaqus.Odb.OdbSet.OdbSet` = `<abaqus.Odb.OdbSet.OdbSet object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/BeamOrientationArray.py#L27-L28)[¶](#abaqus.Odb.BeamOrientationArray.BeamOrientation.region "Permalink to this definition")
    :   An OdbSet object specifying a region for which the beam orientation is defined.

    vector : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/BeamOrientationArray.py#L9-L32)[¶](#abaqus.Odb.BeamOrientationArray.BeamOrientation.vector "Permalink to this definition")
    :   A tuple of Floats specifying direction cosines of the n1-direction of the beam
        cross-section.

*class* OdbSet(*[name](#abaqus.Odb.RebarOrientation.OdbSet "abaqus.Odb.RebarOrientation.OdbSet.__init__.name (Python parameter)")*, *[nodes](#abaqus.Odb.RebarOrientation.OdbSet "abaqus.Odb.RebarOrientation.OdbSet.__init__.nodes (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L14-L276)[¶](#abaqus.Odb.RebarOrientation.OdbSet "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The set objects are used to identify regions of a model.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].parts[name].elementSets[name]
    session.odbs[name].parts[name].nodeSets[name]
    session.odbs[name].parts[name].surfaces[name]
    session.odbs[name].rootAssembly.elementSets[name]
    session.odbs[name].rootAssembly.instances[name].elementSets[name]
    session.odbs[name].rootAssembly.instances[name].nodeSets[name]
    session.odbs[name].rootAssembly.instances[name].surfaces[name]
    session.odbs[name].rootAssembly.nodeSets[name]
    session.odbs[name].rootAssembly.surfaces[name]
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.elementSets[name]
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.nodeSets[name]
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.surfaces[name]
    ```

    Note

    Check [OdbSet on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsetpyc.htm?contextscope=all).

    Member Details:

    ElementSet(*[name](#abaqus.Odb.RebarOrientation.OdbSet.ElementSet.name "abaqus.Odb.RebarOrientation.OdbSet.ElementSet.name (Python parameter) — A String specifying the name of the set and the repository key.")*, *[elements](#abaqus.Odb.RebarOrientation.OdbSet.ElementSet.elements "abaqus.Odb.RebarOrientation.OdbSet.ElementSet.elements (Python parameter) — A sequence of OdbMeshElement objects.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L121-L147)[¶](#abaqus.Odb.RebarOrientation.OdbSet.ElementSet "Permalink to this definition")
    :   This method creates an element set from an array of OdbMeshElement objects (for part instance-level
        sets) or from a sequence of arrays of OdbMeshElement objects (for assembly-level sets).

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].parts[name].NodeSet
        session.odbs[name].rootAssembly.instances[name].NodeSet
        session.odbs[name].rootAssembly.NodeSet
        ```

        Note

        Check [ElementSet on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-elementsetpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.RebarOrientation.OdbSet.ElementSet-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.RebarOrientation.OdbSet.ElementSet.name "Permalink to this definition")
            :   A String specifying the name of the set and the repository key.

            elements[¶](#abaqus.Odb.RebarOrientation.OdbSet.ElementSet.elements "Permalink to this definition")
            :   A sequence of OdbMeshElement objects. For example, for a
                part:elements=instance1.elements[1:5]`For an
                assembly:`elements=(instance1.elements[1:5], instance2.elements[1:5])

        Returns:[¶](#abaqus.Odb.RebarOrientation.OdbSet.ElementSet-returns "Permalink to this headline")
        :   An OdbSet object.

        Return type:[¶](#abaqus.Odb.RebarOrientation.OdbSet.ElementSet-return-type "Permalink to this headline")
        :   [`OdbSet`](#abaqus.Odb.RebarOrientation.OdbSet "abaqus.Odb.RebarOrientation.OdbSet (Python class) — Bases: object")

    ElementSetFromElementLabels(*[name](#abaqus.Odb.RebarOrientation.OdbSet.ElementSetFromElementLabels.name "abaqus.Odb.RebarOrientation.OdbSet.ElementSetFromElementLabels.name (Python parameter) — A String specifying the name of the set and the repository key.")*, *[elementLabels](#abaqus.Odb.RebarOrientation.OdbSet.ElementSetFromElementLabels.elementLabels "abaqus.Odb.RebarOrientation.OdbSet.ElementSetFromElementLabels.elementLabels (Python parameter) — A sequence of element labels.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L149-L174)[¶](#abaqus.Odb.RebarOrientation.OdbSet.ElementSetFromElementLabels "Permalink to this definition")
    :   This method creates an element set from a sequence of element labels.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].parts[name].NodeSet
        session.odbs[name].rootAssembly.instances[name].NodeSet
        session.odbs[name].rootAssembly.NodeSet
        ```

        Note

        Check [ElementSetFromElementLabels on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-elementsetfromelementlabelspyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.RebarOrientation.OdbSet.ElementSetFromElementLabels-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.RebarOrientation.OdbSet.ElementSetFromElementLabels.name "Permalink to this definition")
            :   A String specifying the name of the set and the repository key.

            elementLabels[¶](#abaqus.Odb.RebarOrientation.OdbSet.ElementSetFromElementLabels.elementLabels "Permalink to this definition")
            :   A sequence of element labels. An element label is a sequence of Int element identifiers.
                For example, for a part:elementLabels=(2,3,5,7)`For an
                assembly:`elementLabels=((‘Instance-1’, (2,3,5,7)), (‘Instance-2’, (1,2,3)))

        Returns:[¶](#abaqus.Odb.RebarOrientation.OdbSet.ElementSetFromElementLabels-returns "Permalink to this headline")
        :   An OdbSet object.

        Return type:[¶](#abaqus.Odb.RebarOrientation.OdbSet.ElementSetFromElementLabels-return-type "Permalink to this headline")
        :   [`OdbSet`](#abaqus.Odb.RebarOrientation.OdbSet "abaqus.Odb.RebarOrientation.OdbSet (Python class) — Bases: object")

    MeshSurface(*[name](#abaqus.Odb.RebarOrientation.OdbSet.MeshSurface.name "abaqus.Odb.RebarOrientation.OdbSet.MeshSurface.name (Python parameter) — A String specifying the name of the set and the repository key.")*, *[meshSurfaces](#abaqus.Odb.RebarOrientation.OdbSet.MeshSurface.meshSurfaces "abaqus.Odb.RebarOrientation.OdbSet.MeshSurface.meshSurfaces (Python parameter) — A sequence of sequences.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L176-L217)[¶](#abaqus.Odb.RebarOrientation.OdbSet.MeshSurface "Permalink to this definition")
    :   This method creates a surface from the element and side identifiers for the assembly.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].parts[name].NodeSet
        session.odbs[name].rootAssembly.instances[name].NodeSet
        session.odbs[name].rootAssembly.NodeSet
        ```

        Note

        Check [MeshSurface on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshsurfacepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.RebarOrientation.OdbSet.MeshSurface-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.RebarOrientation.OdbSet.MeshSurface.name "Permalink to this definition")
            :   A String specifying the name of the set and the repository key.

            meshSurfaces[¶](#abaqus.Odb.RebarOrientation.OdbSet.MeshSurface.meshSurfaces "Permalink to this definition")
            :   A sequence of sequences. Each sequence consists of an element sequence and a side
                identifier. The possible side identifiers depend on the type of element, as described in
                the following table:

                Sequence of elements | Side identifiers |

                ——————————– | —————————————- |

                Solid elements | FACE1, FACE2, FACE3, FACE4, FACE5, FACE6 |

                Three-dimensional shell elements | SIDE1, SIDE2 |

                Two-dimensional elements | FACE1, FACE2, FACE3, FACE4 |

                Wire elements | END, END2 |

                For example:

                ```python
                side1Elements=instance1.elements[217:218]
                side2Elements=instance2.elements[100:105]
                assembly.MeshSurface(
                    name='Surf-1',
                    meshSurfaces=((side1Elems,SIDE1), (side2Elems,SIDE2))
                )
                ```

        Returns:[¶](#abaqus.Odb.RebarOrientation.OdbSet.MeshSurface-returns "Permalink to this headline")
        :   An OdbSet object.

        Return type:[¶](#abaqus.Odb.RebarOrientation.OdbSet.MeshSurface-return-type "Permalink to this headline")
        :   [`OdbSet`](#abaqus.Odb.RebarOrientation.OdbSet "abaqus.Odb.RebarOrientation.OdbSet (Python class) — Bases: object")

    MeshSurfaceFromElsets(*[name](#abaqus.Odb.RebarOrientation.OdbSet.MeshSurfaceFromElsets.name "abaqus.Odb.RebarOrientation.OdbSet.MeshSurfaceFromElsets.name (Python parameter) — A String specifying the name of the set and the repository key.")*, *[elementSetSeq](#abaqus.Odb.RebarOrientation.OdbSet.MeshSurfaceFromElsets.elementSetSeq "abaqus.Odb.RebarOrientation.OdbSet.MeshSurfaceFromElsets.elementSetSeq (Python parameter) — A sequence of element sets.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L219-L247)[¶](#abaqus.Odb.RebarOrientation.OdbSet.MeshSurfaceFromElsets "Permalink to this definition")
    :   This method creates a mesh surface from a sequence of element sets.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].parts[name].NodeSet
        session.odbs[name].rootAssembly.instances[name].NodeSet
        session.odbs[name].rootAssembly.NodeSet
        ```

        Note

        Check [MeshSurfaceFromElsets on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshsurfacefromelsetspyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.RebarOrientation.OdbSet.MeshSurfaceFromElsets-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.RebarOrientation.OdbSet.MeshSurfaceFromElsets.name "Permalink to this definition")
            :   A String specifying the name of the set and the repository key.

            elementSetSeq[¶](#abaqus.Odb.RebarOrientation.OdbSet.MeshSurfaceFromElsets.elementSetSeq "Permalink to this definition")
            :   A sequence of element sets. For example:

                ```python
                elementSetSeq=((elset1,SIDE1),(elset2,SIDE2))``
                ```

                where `elset1=session.odbs[name].rootAssembly.elementSets['Clutch']`
                and `SIDE1` and `SIDE2` indicate the side of the element set.

        Returns:[¶](#abaqus.Odb.RebarOrientation.OdbSet.MeshSurfaceFromElsets-returns "Permalink to this headline")
        :   An OdbSet object.

        Return type:[¶](#abaqus.Odb.RebarOrientation.OdbSet.MeshSurfaceFromElsets-return-type "Permalink to this headline")
        :   [`OdbSet`](#abaqus.Odb.RebarOrientation.OdbSet "abaqus.Odb.RebarOrientation.OdbSet (Python class) — Bases: object")

    MeshSurfaceFromLabels(*[name](#abaqus.Odb.RebarOrientation.OdbSet.MeshSurfaceFromLabels.name "abaqus.Odb.RebarOrientation.OdbSet.MeshSurfaceFromLabels.name (Python parameter) — A String specifying the name of the set and the repository key.")*, *[surfaceLabels](#abaqus.Odb.RebarOrientation.OdbSet.MeshSurfaceFromLabels.surfaceLabels "abaqus.Odb.RebarOrientation.OdbSet.MeshSurfaceFromLabels.surfaceLabels (Python parameter) — A sequence of surface labels.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L249-L276)[¶](#abaqus.Odb.RebarOrientation.OdbSet.MeshSurfaceFromLabels "Permalink to this definition")
    :   This method creates a mesh surface from a sequence of surface labels.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].parts[name].NodeSet
        session.odbs[name].rootAssembly.instances[name].NodeSet
        session.odbs[name].rootAssembly.NodeSet
        ```

        Note

        Check [MeshSurfaceFromLabels on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshsurfacefromlabelspyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.RebarOrientation.OdbSet.MeshSurfaceFromLabels-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.RebarOrientation.OdbSet.MeshSurfaceFromLabels.name "Permalink to this definition")
            :   A String specifying the name of the set and the repository key.

            surfaceLabels[¶](#abaqus.Odb.RebarOrientation.OdbSet.MeshSurfaceFromLabels.surfaceLabels "Permalink to this definition")
            :   A sequence of surface labels. For example:

                ```python
                surfaceLabels=(('Instance-1', ((10, FACE1), (11, FACE2))),  ('Instance-2', ((10, FACE3), (12, FACE4))))
                ```

                where `10` is an element number and `FACE1` indicates the side of the element.

        Returns:[¶](#abaqus.Odb.RebarOrientation.OdbSet.MeshSurfaceFromLabels-returns "Permalink to this headline")
        :   An OdbSet object.

        Return type:[¶](#abaqus.Odb.RebarOrientation.OdbSet.MeshSurfaceFromLabels-return-type "Permalink to this headline")
        :   [`OdbSet`](#abaqus.Odb.RebarOrientation.OdbSet "abaqus.Odb.RebarOrientation.OdbSet (Python class) — Bases: object")

    NodeSetFromNodeLabels(*[name](#abaqus.Odb.RebarOrientation.OdbSet.NodeSetFromNodeLabels.name "abaqus.Odb.RebarOrientation.OdbSet.NodeSetFromNodeLabels.name (Python parameter) — A String specifying the name of the set and the repository key.")*, *[nodeLabels](#abaqus.Odb.RebarOrientation.OdbSet.NodeSetFromNodeLabels.nodeLabels "abaqus.Odb.RebarOrientation.OdbSet.NodeSetFromNodeLabels.nodeLabels (Python parameter) — A sequence of node labels.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L94-L119)[¶](#abaqus.Odb.RebarOrientation.OdbSet.NodeSetFromNodeLabels "Permalink to this definition")
    :   This method creates a node set from a sequence of node labels.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].parts[name].NodeSet
        session.odbs[name].rootAssembly.instances[name].NodeSet
        session.odbs[name].rootAssembly.NodeSet
        ```

        Note

        Check [NodeSetFromNodeLabels on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-nodesetfromnodelabelspyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.RebarOrientation.OdbSet.NodeSetFromNodeLabels-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.RebarOrientation.OdbSet.NodeSetFromNodeLabels.name "Permalink to this definition")
            :   A String specifying the name of the set and the repository key.

            nodeLabels[¶](#abaqus.Odb.RebarOrientation.OdbSet.NodeSetFromNodeLabels.nodeLabels "Permalink to this definition")
            :   A sequence of node labels. A node label is a sequence of Int node identifiers. For
                example, for a part:nodeLabels=(2,3,5,7)`For an assembly:`nodeLabels=((‘Instance-1’,
                (2,3,5,7)), (‘Instance-2’, (1,2,3)))

        Returns:[¶](#abaqus.Odb.RebarOrientation.OdbSet.NodeSetFromNodeLabels-returns "Permalink to this headline")
        :   An OdbSet object.

        Return type:[¶](#abaqus.Odb.RebarOrientation.OdbSet.NodeSetFromNodeLabels-return-type "Permalink to this headline")
        :   [`OdbSet`](#abaqus.Odb.RebarOrientation.OdbSet "abaqus.Odb.RebarOrientation.OdbSet (Python class) — Bases: object")

    elements : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Odb.OdbMeshElement.OdbMeshElement`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L47-L49)[¶](#abaqus.Odb.RebarOrientation.OdbSet.elements "Permalink to this definition")
    :   An OdbMeshElementArray object specifying the elements of an OdbSet. If a set spans more
        than one part instance, this member is a sequence of sequences for each part instance.

    faces : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py)[¶](#abaqus.Odb.RebarOrientation.OdbSet.faces "Permalink to this definition")
    :   A tuple of SymbolicConstants specifying the element face. If a set spans more than one
        part instance, this member is a sequence of sequences for each part instance.

    instanceNames : --is-rst--:py:class:`tuple`\[:py:class:`str`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L39-L41)[¶](#abaqus.Odb.RebarOrientation.OdbSet.instanceNames "Permalink to this definition")
    :   A tuple of Strings specifying the namespaces for the nodes, elements, and faces; None if
        the set is on a Part or an OdbInstance object.

    instances : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L57-L59)[¶](#abaqus.Odb.RebarOrientation.OdbSet.instances "Permalink to this definition")
    :   A repository of an OdbInstance object.

        New in version 2020: The `instances` attribute was added.

    isInternal : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L57-L59)[¶](#abaqus.Odb.RebarOrientation.OdbSet.isInternal "Permalink to this definition")
    :   A Boolean specifying whether the set is internal.

        New in version 2020: The `isInternal` attribute was added.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L36-L37)[¶](#abaqus.Odb.RebarOrientation.OdbSet.name "Permalink to this definition")
    :   A String specifying the name of the set and the repository key.

    nodes : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Odb.OdbMeshNode.OdbMeshNode`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L43-L45)[¶](#abaqus.Odb.RebarOrientation.OdbSet.nodes "Permalink to this definition")
    :   An OdbMeshNodeArray object specifying the nodes of an OdbSet. If a set spans more than
        one part instance, this member is a sequence of sequences for each part instance.

*class* FieldBulkData[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldOutput.py#L11-L89)[¶](#abaqus.Odb.FieldOutput.FieldBulkData "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The FieldBulkData object represents the entire field data for a class of elements or nodes. All elements
    in a class correspond to the same element type and material.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].bulkDataBlocks[i]
    ```

    Note

    Check [FieldBulkData on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldbulkdatapyc.htm?contextscope=all).

    Member Details:

    componentLabels : --is-rst--:py:class:`tuple`\[:py:class:`str`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldOutput.py#L55-L56)[¶](#abaqus.Odb.FieldOutput.FieldBulkData.componentLabels "Permalink to this definition")
    :   A sequence of Strings specifying the component labels.

    conjugateData : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldOutput.py#L62-L66)[¶](#abaqus.Odb.FieldOutput.FieldBulkData.conjugateData "Permalink to this definition")
    :   A tuple of Floats specifying data in the form described by **type**. If **type** = TENSOR or
        VECTOR, **conjugateData** is a sequence containing the imaginary part of the components
        for each element or node in the block. If the underlying data are in double precision,
        an exception will be thrown.

    data : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldOutput.py#L62-L65)[¶](#abaqus.Odb.FieldOutput.FieldBulkData.data "Permalink to this definition")
    :   A tuple of Floats specifying data in the form described by **type**. If **type** = TENSOR or
        VECTOR, **data** is a sequence containing the components for each element or node in the
        block. If the underlying data are in double precision, an exception will be thrown.

    elementLabels : --is-rst--:py:class:`tuple`\[:py:class:`int`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldOutput.py#L46-L49)[¶](#abaqus.Odb.FieldOutput.FieldBulkData.elementLabels "Permalink to this definition")
    :   A sequence of Ints specifying the element labels of the elements in the block.
        **elementLabels** is valid only if **position** = INTEGRATION\_POINT, CENTROID, ELEMENT\_NODAL,
        or ELEMENT\_FACE.

    instance : --is-rst--:py:class:`~abaqus.Odb.OdbInstance.OdbInstance` = `<abaqus.Odb.OdbInstance.OdbInstance object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldOutput.py#L40-L41)[¶](#abaqus.Odb.FieldOutput.FieldBulkData.instance "Permalink to this definition")
    :   An OdbInstance object specifying the part to which the labels belong.

    integrationPoints : --is-rst--:py:class:`tuple`\[:py:class:`int`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldOutput.py#L58-L60)[¶](#abaqus.Odb.FieldOutput.FieldBulkData.integrationPoints "Permalink to this definition")
    :   A sequence of Ints specifying the integration points in the elements in the block.
        **integrationPoints** is available only if **position** = INTEGRATION\_POINT.

    localCoordSystem : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldOutput.py#L11-L89)[¶](#abaqus.Odb.FieldOutput.FieldBulkData.localCoordSystem "Permalink to this definition")
    :   A pointer to an array of Floats specifying the quaternion representing the local
        coordinate system (the rotation from global to local) at each output location. The
        quaternion is returned in the form q=(q,q0), which is the reverse of that shown in
        [Rotation
        variables](<https://help.3ds.com/2022/english/DSSIMULIA_Established/SIMACAETHERefMap/simathe-c-rotationvars.htm?ContextScope=all>).
        **localCoordSystem** is available for TENSOR data written in a local coordinate system. It
        is also available for VECTOR data for connector element outputs. For connector element
        outputs the quaternion form is q=(q0,q)q=(q0,q), which represents the rotation from
        local to global. If the underlying data are in double precision, an exception will be
        thrown.

    mises : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldOutput.py#L73-L77)[¶](#abaqus.Odb.FieldOutput.FieldBulkData.mises "Permalink to this definition")
    :   A sequence of Floats specifying the calculated von Mises stress at each output location
        in the block of element data, or NULL. The value is valid only when the
        **validInvariants** member includes MISES; otherwise, the value is indeterminate.
        Conjugate data will be ignored in invariant calculation.

    nodeLabels : --is-rst--:py:class:`tuple`\[:py:class:`int`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldOutput.py#L51-L53)[¶](#abaqus.Odb.FieldOutput.FieldBulkData.nodeLabels "Permalink to this definition")
    :   A sequence of Ints specifying the node labels of the nodes in the block. **nodelabels** is
        valid only if **position** = ELEMENT\_NODAL or NODAL.

    position : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldOutput.py)[¶](#abaqus.Odb.FieldOutput.FieldBulkData.position "Permalink to this definition")
    :   A SymbolicConstant specifying the position of the output in the element. Possible values
        are:

        * NODAL, specifying the values calculated at the nodes.
        * INTEGRATION\_POINT, specifying the values calculated at the integration points.
        * ELEMENT\_NODAL, specifying the values obtained by extrapolating results calculated at
          the integration points.
        * ELEMENT\_FACE.
        * CENTROID, specifying the value at the centroid obtained by extrapolating results
          calculated at the integration points.

    sectionPoint : --is-rst--:py:data:`~typing.Optional`\[:py:class:`~abaqus.Odb.SectionPoint.SectionPoint`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldOutput.py#L43-L44)[¶](#abaqus.Odb.FieldOutput.FieldBulkData.sectionPoint "Permalink to this definition")
    :   A SectionPoint object specifying the section point number of the current block of data.

    type : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldOutput.py)[¶](#abaqus.Odb.FieldOutput.FieldBulkData.type "Permalink to this definition")
    :   A SymbolicConstant specifying the output type. Possible values are SCALAR, VECTOR,
        TENSOR\_3D\_FULL, TENSOR\_3D\_PLANAR, TENSOR\_3D\_SURFACE, TENSOR\_2D\_PLANAR, and
        TENSOR\_2D\_SURFACE.

*class* OdbInstance(*[name](#abaqus.Odb.OdbInstance.OdbInstance "abaqus.Odb.OdbInstance.OdbInstance.__init__.name (Python parameter)")*, *[object](#abaqus.Odb.OdbInstance.OdbInstance "abaqus.Odb.OdbInstance.OdbInstance.__init__.object (Python parameter)")*, *[localCoordSystem](#abaqus.Odb.OdbInstance.OdbInstance "abaqus.Odb.OdbInstance.OdbInstance.__init__.localCoordSystem (Python parameter)")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstance.py#L12-L40)[¶](#abaqus.Odb.OdbInstance.OdbInstance "Permalink to this definition")
:   Bases: [`OdbInstanceBase`](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase "abaqus.Odb.OdbInstanceBase.OdbInstanceBase (Python class) — Bases: object")

    Member Details:

    NodeSet(*[name](#abaqus.Odb.OdbInstance.OdbInstance.NodeSet.name "abaqus.Odb.OdbInstance.OdbInstance.NodeSet.name (Python parameter) — A String specifying the name of the set and the repository key.")*, *[nodes](#abaqus.Odb.OdbInstance.OdbInstance.NodeSet.nodes "abaqus.Odb.OdbInstance.OdbInstance.NodeSet.nodes (Python parameter) — A sequence of OdbMeshNode objects.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstance.py#L14-L40)[¶](#abaqus.Odb.OdbInstance.OdbInstance.NodeSet "Permalink to this definition")
    :   This method creates a node set from an array of OdbMeshNode objects (for part instance-level sets) or
        from a sequence of arrays of OdbMeshNode objects (for assembly-level sets).

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].parts[name].NodeSet
        session.odbs[name].rootAssembly.instances[name].NodeSet
        session.odbs[name].rootAssembly.NodeSet
        ```

        Note

        Check [NodeSet on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-nodesetpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbInstance.OdbInstance.NodeSet-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.OdbInstance.OdbInstance.NodeSet.name "Permalink to this definition")
            :   A String specifying the name of the set and the repository key.

            nodes[¶](#abaqus.Odb.OdbInstance.OdbInstance.NodeSet.nodes "Permalink to this definition")
            :   A sequence of OdbMeshNode objects. For example, for a part:nodes=part1.nodes[1:5]`For
                an assembly:`nodes=(instance1.nodes[6:7], instance2.nodes[1:5])

        Returns:[¶](#abaqus.Odb.OdbInstance.OdbInstance.NodeSet-returns "Permalink to this headline")
        :   An OdbSet object.

        Return type:[¶](#abaqus.Odb.OdbInstance.OdbInstance.NodeSet-return-type "Permalink to this headline")
        :   `OdbSet`

*class* OdbPart(*[name](#abaqus.Odb.OdbPart.OdbPart "abaqus.Odb.OdbPart.OdbPart.__init__.name (Python parameter)")*, *[embeddedSpace](#abaqus.Odb.OdbPart.OdbPart "abaqus.Odb.OdbPart.OdbPart.__init__.embeddedSpace (Python parameter)")*, *[type](#abaqus.Odb.OdbPart.OdbPart "abaqus.Odb.OdbPart.OdbPart.__init__.type (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPart.py#L13-L84)[¶](#abaqus.Odb.OdbPart.OdbPart "Permalink to this definition")
:   Bases: [`OdbPartBase`](#abaqus.Odb.OdbPartBase.OdbPartBase "abaqus.Odb.OdbPartBase.OdbPartBase (Python class) — Bases: object")

    Member Details:

    NodeSet(*[name](#abaqus.Odb.OdbPart.OdbPart.NodeSet.name "abaqus.Odb.OdbPart.OdbPart.NodeSet.name (Python parameter) — A String specifying the name of the set and the repository key.")*, *[nodes](#abaqus.Odb.OdbPart.OdbPart.NodeSet.nodes "abaqus.Odb.OdbPart.OdbPart.NodeSet.nodes (Python parameter) — A sequence of OdbMeshNode objects.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPart.py#L58-L84)[¶](#abaqus.Odb.OdbPart.OdbPart.NodeSet "Permalink to this definition")
    :   This method creates a node set from an array of OdbMeshNode objects (for part instance-level sets) or
        from a sequence of arrays of OdbMeshNode objects (for assembly-level sets).

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].parts[name].NodeSet
        session.odbs[name].rootAssembly.instances[name].NodeSet
        session.odbs[name].rootAssembly.NodeSet
        ```

        Note

        Check [NodeSet on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-nodesetpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbPart.OdbPart.NodeSet-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.OdbPart.OdbPart.NodeSet.name "Permalink to this definition")
            :   A String specifying the name of the set and the repository key.

            nodes[¶](#abaqus.Odb.OdbPart.OdbPart.NodeSet.nodes "Permalink to this definition")
            :   A sequence of OdbMeshNode objects. For example, for a part:nodes=part1.nodes[1:5]`For
                an assembly:`nodes=(instance1.nodes[6:7], instance2.nodes[1:5])

        Returns:[¶](#abaqus.Odb.OdbPart.OdbPart.NodeSet-returns "Permalink to this headline")
        :   An OdbSet object.

        Return type:[¶](#abaqus.Odb.OdbPart.OdbPart.NodeSet-return-type "Permalink to this headline")
        :   `OdbSet`

    RigidBody(*[referenceNode](#abaqus.Odb.OdbPart.OdbPart.RigidBody.referenceNode "abaqus.Odb.OdbPart.OdbPart.RigidBody.referenceNode (Python parameter) — An OdbSet specifying the reference node assigned to the rigid body.")*, *[position](#abaqus.Odb.OdbPart.OdbPart.RigidBody.position "abaqus.Odb.OdbPart.OdbPart.RigidBody.position (Python parameter) — A symbolic constant specify if the location of the reference node is to be defined by the user.")=`abaqusConstants.INPUT`*, *[isothermal](#abaqus.Odb.OdbPart.OdbPart.RigidBody.isothermal "abaqus.Odb.OdbPart.OdbPart.RigidBody.isothermal (Python parameter) — A Boolean specifying an isothermal rigid body.")=`0`*, *[elset](#abaqus.Odb.OdbPart.OdbPart.RigidBody.elset "abaqus.Odb.OdbPart.OdbPart.RigidBody.elset (Python parameter) — An OdbSet specifying an element set assigned to the rigid body.")=`''`*, *[pinNodes](#abaqus.Odb.OdbPart.OdbPart.RigidBody.pinNodes "abaqus.Odb.OdbPart.OdbPart.RigidBody.pinNodes (Python parameter) — An OdbSet specifying pin-type nodes assigned to the rigid body.")=`''`*, *[tieNodes](#abaqus.Odb.OdbPart.OdbPart.RigidBody.tieNodes "abaqus.Odb.OdbPart.OdbPart.RigidBody.tieNodes (Python parameter) — An OdbSet specifying tie-type nodes assigned to the rigid body.")=`''`*, *[analyticSurface](#abaqus.Odb.OdbPart.OdbPart.RigidBody.analyticSurface "abaqus.Odb.OdbPart.OdbPart.RigidBody.analyticSurface (Python parameter) — An AnalyticSurface specifying the Analytic Rigid Surface assigned to the rigid body.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPart.py#L15-L56)[¶](#abaqus.Odb.OdbPart.OdbPart.RigidBody "Permalink to this definition")
    :   This method defines an OdbRigidBody on the part object.

        Note

        Check [RigidBody on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rigidbodypyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbPart.OdbPart.RigidBody-parameters "Permalink to this headline")
        :   referenceNode[¶](#abaqus.Odb.OdbPart.OdbPart.RigidBody.referenceNode "Permalink to this definition")
            :   An OdbSet specifying the reference node assigned to the rigid body.

            position=`abaqusConstants.INPUT`[¶](#abaqus.Odb.OdbPart.OdbPart.RigidBody.position "Permalink to this definition")
            :   A symbolic constant specify if the location of the reference node is to be defined by
                the user. Possible values are INPUT and CENTER\_OF\_MASS. The default value is INPUT.

            isothermal=`0`[¶](#abaqus.Odb.OdbPart.OdbPart.RigidBody.isothermal "Permalink to this definition")
            :   A Boolean specifying an isothermal rigid body. The default value is OFF. This parameter
                is used only for a fully-coupled thermal stress analysis.

            elset=`''`[¶](#abaqus.Odb.OdbPart.OdbPart.RigidBody.elset "Permalink to this definition")
            :   An OdbSet specifying an element set assigned to the rigid body.

            pinNodes=`''`[¶](#abaqus.Odb.OdbPart.OdbPart.RigidBody.pinNodes "Permalink to this definition")
            :   An OdbSet specifying pin-type nodes assigned to the rigid body.

            tieNodes=`''`[¶](#abaqus.Odb.OdbPart.OdbPart.RigidBody.tieNodes "Permalink to this definition")
            :   An OdbSet specifying tie-type nodes assigned to the rigid body.

            analyticSurface=`''`[¶](#abaqus.Odb.OdbPart.OdbPart.RigidBody.analyticSurface "Permalink to this definition")
            :   An AnalyticSurface specifying the Analytic Rigid Surface assigned to the rigid body.

        Return type:[¶](#abaqus.Odb.OdbPart.OdbPart.RigidBody-return-type "Permalink to this headline")
        :   `None.`

        Raises:[¶](#abaqus.Odb.OdbPart.OdbPart.RigidBody-raises "Permalink to this headline")
        :   **OdbError** – Rigid body definition requires a node set, If **referenceNode** is not a node set.

*class* SectionPoint(*[number](#abaqus.Odb.SectionPointArray.SectionPoint "abaqus.Odb.SectionPointArray.SectionPoint.__init__.number (Python parameter)")*, *[description](#abaqus.Odb.SectionPointArray.SectionPoint "abaqus.Odb.SectionPointArray.SectionPoint.__init__.description (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/SectionPointArray.py#L6-L64)[¶](#abaqus.Odb.SectionPointArray.SectionPoint "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The SectionPoint object describes the location of a section point within a section category.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].parts[name].elements[i].sectionCategory.sectionPoints[i]
    session.odbs[name].parts[name].elementSets[name].elements[i].sectionCategory.sectionPoints[i]
    session.odbs[name].parts[name].nodeSets[name].elements[i].sectionCategory.sectionPoints[i]
    session.odbs[name].parts[name].surfaces[name].elements[i].sectionCategory.sectionPoints[i]
    session.odbs[name].rootAssembly.elements[i].sectionCategory.sectionPoints[i]
    session.odbs[name].rootAssembly.elementSets[name].elements[i].sectionCategory.sectionPoints[i]
    session.odbs[name].rootAssembly.instances[name].elements[i].sectionCategory.sectionPoints[i]
    session.odbs[name].rootAssembly.instances[name].elementSets[name].elements[i].sectionCategory.sectionPoints[i]
    session.odbs[name].rootAssembly.instances[name].nodeSets[name].elements[i].sectionCategory.sectionPoints[i]
    session.odbs[name].rootAssembly.instances[name].surfaces[name].elements[i].sectionCategory.sectionPoints[i]
    session.odbs[name].rootAssembly.nodeSets[name].elements[i].sectionCategory.sectionPoints[i]
    session.odbs[name].rootAssembly.surfaces[name].elements[i].sectionCategory.sectionPoints[i]
    session.odbs[name].sectionCategories[name].sectionPoints[i]
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].locations[i].sectionPoints[i]
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.elements[i].sectionCategory.sectionPoints[i]
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.elementSets[name].elements[i].sectionCategory.sectionPoints[i]
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.nodeSets[name].elements[i].sectionCategory.sectionPoints[i]
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.surfaces[name].elements[i].sectionCategory.sectionPoints[i]
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].sectionPoint
    ```

    Note

    Check [SectionPoint on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpointpyc.htm?contextscope=all).

    Member Details:

    description : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/SectionPointArray.py)[¶](#abaqus.Odb.SectionPointArray.SectionPoint.description "Permalink to this definition")
    :   A String specifying the description of the section point.

    number : --is-rst--:py:class:`int`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/SectionPointArray.py)[¶](#abaqus.Odb.SectionPointArray.SectionPoint.number "Permalink to this definition")
    :   An Int specifying the number of the section point. See Beam elements and Shell elements
        for the numbering convention.

*class* FieldLocation[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldOutput.py#L9-L32)[¶](#abaqus.Odb.FieldOutput.FieldLocation "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The FieldLocation object specifies locations for which data are available in the field. For example, a
    displacement field will have a FieldLocation object with a **position** member value of NODAL. The
    FieldLocation object has no constructor; it is created automatically as an element of the **location**
    member of a FieldOutput object by the addData method of a FieldOutput object.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].locations[i]
    ```

    Note

    Check [FieldLocation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldlocationpyc.htm?contextscope=all).

    Member Details:

    position : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldOutput.py)[¶](#abaqus.Odb.FieldOutput.FieldLocation.position "Permalink to this definition")
    :   A SymbolicConstant specifying the position of the output in the element. Possible values
        are:NODAL, specifying the values calculated at the nodes.INTEGRATION\_POINT, specifying
        the values calculated at the integration points.ELEMENT\_NODAL, specifying the values
        obtained by extrapolating results calculated at the integration
        points.ELEMENT\_FACE.CENTROID, specifying the value at the centroid obtained by
        extrapolating results calculated at the integration points.

    sectionPoints : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Odb.SectionPoint.SectionPoint`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldOutput.py#L9-L32)[¶](#abaqus.Odb.FieldOutput.FieldLocation.sectionPoints "Permalink to this definition")
    :   A SectionPointArray object.

*class* FieldOutput(*[name](#abaqus.Odb.OdbStepBase.FieldOutput "abaqus.Odb.OdbStepBase.FieldOutput.__init__.name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[description](#abaqus.Odb.OdbStepBase.FieldOutput "abaqus.Odb.OdbStepBase.FieldOutput.__init__.description (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[type](#abaqus.Odb.OdbStepBase.FieldOutput "abaqus.Odb.OdbStepBase.FieldOutput.__init__.type (Python parameter)"): [SymbolicConstant](kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.SymbolicConstant "abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant (Python class)")*, *[componentLabels](#abaqus.Odb.OdbStepBase.FieldOutput "abaqus.Odb.OdbStepBase.FieldOutput.__init__.componentLabels (Python parameter)"): [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)") = `()`*, *[validInvariants](#abaqus.Odb.OdbStepBase.FieldOutput "abaqus.Odb.OdbStepBase.FieldOutput.__init__.validInvariants (Python parameter)"): [SymbolicConstant](kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.SymbolicConstant "abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant (Python class)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[isEngineeringTensor](#abaqus.Odb.OdbStepBase.FieldOutput "abaqus.Odb.OdbStepBase.FieldOutput.__init__.isEngineeringTensor (Python parameter)"): [AbaqusBoolean](kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.AbaqusBoolean "abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean (Python class)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `OFF`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L22-L783)[¶](#abaqus.Odb.OdbStepBase.FieldOutput "Permalink to this definition")

*class* FieldOutput(*[field](#abaqus.Odb.OdbStepBase.FieldOutput "abaqus.Odb.OdbStepBase.FieldOutput.__init__.field (Python parameter)"): [FieldOutput](#abaqus.Odb.OdbStepBase.FieldOutput "abaqus.Odb.FieldOutput.FieldOutput (Python class)")*, *[name](#abaqus.Odb.OdbStepBase.FieldOutput "abaqus.Odb.OdbStepBase.FieldOutput.__init__.name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = `''`*, *[description](#abaqus.Odb.OdbStepBase.FieldOutput "abaqus.Odb.OdbStepBase.FieldOutput.__init__.description (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = `''`*)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    A FieldOutput object contains field data for a specific output variable.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].steps[name].frames[i].fieldOutputs[name]
    ```

    Note

    Check [FieldOutput on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldoutputpyc.htm?contextscope=all).

    Member Details:

    addData(*[position](#abaqus.Odb.OdbStepBase.FieldOutput.addData "abaqus.Odb.OdbStepBase.FieldOutput.addData.position (Python parameter)"): [SymbolicConstant](kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.SymbolicConstant "abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant (Python class)")*, *[instance](#abaqus.Odb.OdbStepBase.FieldOutput.addData "abaqus.Odb.OdbStepBase.FieldOutput.addData.instance (Python parameter)"): [OdbInstance](#abaqus.Odb.OdbInstance.OdbInstance "abaqus.Odb.OdbInstance.OdbInstance (Python class) — Bases: OdbInstanceBase")*, *[labels](#abaqus.Odb.OdbStepBase.FieldOutput.addData "abaqus.Odb.OdbStepBase.FieldOutput.addData.labels (Python parameter)"): [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L318-L319)[¶](#abaqus.Odb.OdbStepBase.FieldOutput.addData "Permalink to this definition")

    addData(*[field](#abaqus.Odb.OdbStepBase.FieldOutput.addData "abaqus.Odb.OdbStepBase.FieldOutput.addData.field (Python parameter)"): [FieldOutput](#abaqus.Odb.OdbStepBase.FieldOutput "abaqus.Odb.FieldOutput.FieldOutput (Python class)")*)

    addData(*[position](#abaqus.Odb.OdbStepBase.FieldOutput.addData "abaqus.Odb.OdbStepBase.FieldOutput.addData.position (Python parameter)"): [SymbolicConstant](kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.SymbolicConstant "abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant (Python class)")*, *[set](#abaqus.Odb.OdbStepBase.FieldOutput.addData "abaqus.Odb.OdbStepBase.FieldOutput.addData.set (Python parameter)"): [OdbSet](#abaqus.Odb.RebarOrientation.OdbSet "abaqus.Odb.OdbSet.OdbSet (Python class)")*, *[data](#abaqus.Odb.OdbStepBase.FieldOutput.addData "abaqus.Odb.OdbStepBase.FieldOutput.addData.data (Python parameter)"): [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")*)

    addData(*\*[args](#abaqus.Odb.OdbStepBase.FieldOutput.addData "abaqus.Odb.OdbStepBase.FieldOutput.addData.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Odb.OdbStepBase.FieldOutput.addData "abaqus.Odb.OdbStepBase.FieldOutput.addData.kwargs (Python parameter)")*)

    bulkDataBlocks : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Odb.FieldBulkData.FieldBulkData`][[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py)[¶](#abaqus.Odb.OdbStepBase.FieldOutput.bulkDataBlocks "Permalink to this definition")
    :   A sequence of FieldBulkData objects.

    componentLabels : --is-rst--:py:class:`tuple`\[:py:class:`str`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L63-L68)[¶](#abaqus.Odb.OdbStepBase.FieldOutput.componentLabels "Permalink to this definition")
    :   A sequence of Strings specifying the labels for each component of the value. The length
        of the sequence must match the type. If **type** = TENSOR, the default value is **name** with
        the suffixes (‘11’, ‘22’, ‘33’, ‘12’, ‘13’, ‘23’). If **type** = VECTOR, the default value
        is **name** with the suffixes (‘1’, ‘2’, ‘3’). If **type** = SCALAR, the default value is an
        empty sequence.

    description : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py)[¶](#abaqus.Odb.OdbStepBase.FieldOutput.description "Permalink to this definition")
    :   ) should not be used as a part of the
        field output description.

        Type:[¶](#abaqus.Odb.OdbStepBase.FieldOutput.description-type "Permalink to this headline")
        :   A String specifying the output variable. Colon (

    dim : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L33-L35)[¶](#abaqus.Odb.OdbStepBase.FieldOutput.dim "Permalink to this definition")
    :   An Int specifying the dimension of vector or the first dimension (number of rows) of
        matrix.

    dim2 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L37-L38)[¶](#abaqus.Odb.OdbStepBase.FieldOutput.dim2 "Permalink to this definition")
    :   An Int specifying the second dimension (number of columns) of matrix.

    getConnectorFieldXformedToNodeA(*[deformationField](#abaqus.Odb.OdbStepBase.FieldOutput.getConnectorFieldXformedToNodeA.deformationField "abaqus.Odb.OdbStepBase.FieldOutput.getConnectorFieldXformedToNodeA.deformationField (Python parameter) — A FieldOutput object specifying the nodal displacement vectors required by moving coordinate systems to determine instantaneous configurations.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L679-L702)[¶](#abaqus.Odb.OdbStepBase.FieldOutput.getConnectorFieldXformedToNodeA "Permalink to this definition")
    :   This method generates a new vector field containing the transformed component values of the parent
        connector field to the node A coordinate system. The new field will hold values for the same connector
        elements as the parent field. Some connection types such as Axial, Link, Slip Ring, and Radial Thrust
        require that the deformationField be specified.

        Parameters:[¶](#abaqus.Odb.OdbStepBase.FieldOutput.getConnectorFieldXformedToNodeA-parameters "Permalink to this headline")
        :   deformationField=`None`[¶](#abaqus.Odb.OdbStepBase.FieldOutput.getConnectorFieldXformedToNodeA.deformationField "Permalink to this definition")
            :   A FieldOutput object specifying the nodal displacement vectors required by moving
                coordinate systems to determine instantaneous configurations.

        Returns:[¶](#abaqus.Odb.OdbStepBase.FieldOutput.getConnectorFieldXformedToNodeA-returns "Permalink to this headline")
        :   A FieldOutput object.

        Return type:[¶](#abaqus.Odb.OdbStepBase.FieldOutput.getConnectorFieldXformedToNodeA-return-type "Permalink to this headline")
        :   [`FieldOutput`](#abaqus.Odb.OdbStepBase.FieldOutput "abaqus.Odb.OdbStepBase.FieldOutput (Python class) — Bases: object")

        Raises:[¶](#abaqus.Odb.OdbStepBase.FieldOutput.getConnectorFieldXformedToNodeA-raises "Permalink to this headline")
        :   **odbException** – The getConnectorFieldXformedToNodeA method throws an exception if the field requires a
            deformationField and the argument is not supplied.

    getScalarField(*[invariant](#abaqus.Odb.OdbStepBase.FieldOutput.getScalarField "abaqus.Odb.OdbStepBase.FieldOutput.getScalarField.invariant (Python parameter)"): [SymbolicConstant](kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.SymbolicConstant "abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant (Python class)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L362-L363)[¶](#abaqus.Odb.OdbStepBase.FieldOutput.getScalarField "Permalink to this definition")

    getScalarField(*[componentLabel](#abaqus.Odb.OdbStepBase.FieldOutput.getScalarField "abaqus.Odb.OdbStepBase.FieldOutput.getScalarField.componentLabel (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)

    getScalarField(*\*[args](#abaqus.Odb.OdbStepBase.FieldOutput.getScalarField "abaqus.Odb.OdbStepBase.FieldOutput.getScalarField.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Odb.OdbStepBase.FieldOutput.getScalarField "abaqus.Odb.OdbStepBase.FieldOutput.getScalarField.kwargs (Python parameter)")*)

    getSubset(*[position](#abaqus.Odb.OdbStepBase.FieldOutput.getSubset "abaqus.Odb.OdbStepBase.FieldOutput.getSubset.position (Python parameter)"): [SymbolicConstant](kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.SymbolicConstant "abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant (Python class)")*, *[readOnly](#abaqus.Odb.OdbStepBase.FieldOutput.getSubset "abaqus.Odb.OdbStepBase.FieldOutput.getSubset.readOnly (Python parameter)"): [AbaqusBoolean](kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.AbaqusBoolean "abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean (Python class)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `OFF`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L539-L541)[¶](#abaqus.Odb.OdbStepBase.FieldOutput.getSubset "Permalink to this definition")

    getSubset(*[region](#abaqus.Odb.OdbStepBase.FieldOutput.getSubset "abaqus.Odb.OdbStepBase.FieldOutput.getSubset.region (Python parameter)"): [OdbSet](#abaqus.Odb.RebarOrientation.OdbSet "abaqus.Odb.OdbSet.OdbSet (Python class)")*)

    getSubset(*[localCoordSystem](#abaqus.Odb.OdbStepBase.FieldOutput.getSubset "abaqus.Odb.OdbStepBase.FieldOutput.getSubset.localCoordSystem (Python parameter)"): [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.13)")[[Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.13)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")]]*)

    getSubset(*[sectionPoint](#abaqus.Odb.OdbStepBase.FieldOutput.getSubset "abaqus.Odb.OdbStepBase.FieldOutput.getSubset.sectionPoint (Python parameter)"): [SectionPoint](#abaqus.Odb.SectionPointArray.SectionPoint "abaqus.Odb.SectionPoint.SectionPoint (Python class)")*)

    getSubset(*[location](#abaqus.Odb.OdbStepBase.FieldOutput.getSubset "abaqus.Odb.OdbStepBase.FieldOutput.getSubset.location (Python parameter)"): [FieldLocation](#abaqus.Odb.FieldOutput.FieldLocation "abaqus.Odb.FieldLocation.FieldLocation (Python class)")*)

    getSubset(*[region](#abaqus.Odb.OdbStepBase.FieldOutput.getSubset "abaqus.Odb.OdbStepBase.FieldOutput.getSubset.region (Python parameter)"): [OdbMeshElement](#abaqus.Odb.OdbSet.OdbMeshElement "abaqus.Odb.OdbMeshElement.OdbMeshElement (Python class)")*)

    getSubset(*[region](#abaqus.Odb.OdbStepBase.FieldOutput.getSubset "abaqus.Odb.OdbStepBase.FieldOutput.getSubset.region (Python parameter)"): [OdbMeshNode](#abaqus.Odb.OdbSet.OdbMeshNode "abaqus.Odb.OdbMeshNode.OdbMeshNode (Python class)")*)

    getSubset(*[region](#abaqus.Odb.OdbStepBase.FieldOutput.getSubset "abaqus.Odb.OdbStepBase.FieldOutput.getSubset.region (Python parameter)"): [FieldOutput](#abaqus.Odb.OdbStepBase.FieldOutput "abaqus.Odb.FieldOutput.FieldOutput (Python class)")*)

    getSubset(*[elementType](#abaqus.Odb.OdbStepBase.FieldOutput.getSubset "abaqus.Odb.OdbStepBase.FieldOutput.getSubset.elementType (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)

    getSubset(*\*[args](#abaqus.Odb.OdbStepBase.FieldOutput.getSubset "abaqus.Odb.OdbStepBase.FieldOutput.getSubset.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Odb.OdbStepBase.FieldOutput.getSubset "abaqus.Odb.OdbStepBase.FieldOutput.getSubset.kwargs (Python parameter)")*)

    getTransformedField(*[datumCsys](#abaqus.Odb.OdbStepBase.FieldOutput.getTransformedField "abaqus.Odb.OdbStepBase.FieldOutput.getTransformedField.datumCsys (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[projected22Axis](#abaqus.Odb.OdbStepBase.FieldOutput.getTransformedField "abaqus.Odb.OdbStepBase.FieldOutput.getTransformedField.projected22Axis (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[projectionTol](#abaqus.Odb.OdbStepBase.FieldOutput.getTransformedField "abaqus.Odb.OdbStepBase.FieldOutput.getTransformedField.projectionTol (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = `''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L676-L677)[¶](#abaqus.Odb.OdbStepBase.FieldOutput.getTransformedField "Permalink to this definition")

    getTransformedField(*[datumCsys](#abaqus.Odb.OdbStepBase.FieldOutput.getTransformedField "abaqus.Odb.OdbStepBase.FieldOutput.getTransformedField.datumCsys (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[deformationField](#abaqus.Odb.OdbStepBase.FieldOutput.getTransformedField "abaqus.Odb.OdbStepBase.FieldOutput.getTransformedField.deformationField (Python parameter)"): [FieldOutput](#abaqus.Odb.OdbStepBase.FieldOutput "abaqus.Odb.FieldOutput.FieldOutput (Python class)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[projected22Axis](#abaqus.Odb.OdbStepBase.FieldOutput.getTransformedField "abaqus.Odb.OdbStepBase.FieldOutput.getTransformedField.projected22Axis (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)

    getTransformedField(*[datumCsys](#abaqus.Odb.OdbStepBase.FieldOutput.getTransformedField "abaqus.Odb.OdbStepBase.FieldOutput.getTransformedField.datumCsys (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[deformationField](#abaqus.Odb.OdbStepBase.FieldOutput.getTransformedField "abaqus.Odb.OdbStepBase.FieldOutput.getTransformedField.deformationField (Python parameter)"): [FieldOutput](#abaqus.Odb.OdbStepBase.FieldOutput "abaqus.Odb.FieldOutput.FieldOutput (Python class)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[rotationField](#abaqus.Odb.OdbStepBase.FieldOutput.getTransformedField "abaqus.Odb.OdbStepBase.FieldOutput.getTransformedField.rotationField (Python parameter)"): [FieldOutput](#abaqus.Odb.OdbStepBase.FieldOutput "abaqus.Odb.FieldOutput.FieldOutput (Python class)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)

    getTransformedField(*\*[args](#abaqus.Odb.OdbStepBase.FieldOutput.getTransformedField "abaqus.Odb.OdbStepBase.FieldOutput.getTransformedField.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Odb.OdbStepBase.FieldOutput.getTransformedField "abaqus.Odb.OdbStepBase.FieldOutput.getTransformedField.kwargs (Python parameter)")*)

    isComplex : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L40-L41)[¶](#abaqus.Odb.OdbStepBase.FieldOutput.isComplex "Permalink to this definition")
    :   A Boolean specifying whether the data are complex.

    isEngineeringTensor : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L77-L81)[¶](#abaqus.Odb.OdbStepBase.FieldOutput.isEngineeringTensor "Permalink to this definition")
    :   A Boolean specifying whether the field is an engineering tensor or not. Setting
        isEngineeringTensor to true makes a tensor field behave as a strain like quantity where
        the off-diagonal components of tensor are halved for invariants computation. This
        parameter applies only to tensor field outputs. The default value is OFF.

    locations : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Odb.FieldLocation.FieldLocation`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L43-L44)[¶](#abaqus.Odb.OdbStepBase.FieldOutput.locations "Permalink to this definition")
    :   A FieldLocationArray object.

    name : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py)[¶](#abaqus.Odb.OdbStepBase.FieldOutput.name "Permalink to this definition")
    :   A String specifying the output variable name.

    setComponentLabels(*[componentLabels](#abaqus.Odb.OdbStepBase.FieldOutput.setComponentLabels.componentLabels "abaqus.Odb.OdbStepBase.FieldOutput.setComponentLabels.componentLabels (Python parameter) — A sequence of Strings specifying the labels for each component of the value.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L704-L717)[¶](#abaqus.Odb.OdbStepBase.FieldOutput.setComponentLabels "Permalink to this definition")
    :   This method sets the component labels for the FieldOutput object.

        Note

        Check [FieldOutput.setComponentLabels on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldoutputpyc.htm?contextscope=all#simaker-fieldoutputsetcomponentlabelspyc).

        Parameters:[¶](#abaqus.Odb.OdbStepBase.FieldOutput.setComponentLabels-parameters "Permalink to this headline")
        :   componentLabels[¶](#abaqus.Odb.OdbStepBase.FieldOutput.setComponentLabels.componentLabels "Permalink to this definition")
            :   A sequence of Strings specifying the labels for each component of the value. The length
                of the sequence must match the type. If **type** = TENSOR, the default value is **name** with
                the suffixes (‘11’, ‘22’, ‘33’, ‘12’, ‘13’, ‘23’). If **type** = VECTOR, the default value
                is **name** with the suffixes (‘1’, ‘2’, ‘3’). If **type** = SCALAR, the default value is an
                empty sequence.

    setDataType(*[type](#abaqus.Odb.OdbStepBase.FieldOutput.setDataType.type "abaqus.Odb.OdbStepBase.FieldOutput.setDataType.type (Python parameter) — A SymbolicConstant specifying the output type.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L719-L741)[¶](#abaqus.Odb.OdbStepBase.FieldOutput.setDataType "Permalink to this definition")
    :   This method sets the data type of a FieldOutput object.

        Note

        Check [FieldOutput.setDataType on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldoutputpyc.htm?contextscope=all#simaker-fieldoutputsetdatatypepyc).

        Parameters:[¶](#abaqus.Odb.OdbStepBase.FieldOutput.setDataType-parameters "Permalink to this headline")
        :   type[¶](#abaqus.Odb.OdbStepBase.FieldOutput.setDataType.type "Permalink to this definition")
            :   A SymbolicConstant specifying the output type. Possible values are SCALAR, VECTOR,
                TENSOR\_3D\_FULL, TENSOR\_3D\_PLANAR, TENSOR\_3D\_SURFACE, TENSOR\_2D\_PLANAR, and
                TENSOR\_2D\_SURFACE.

    setValidInvariants(*[validInvariants](#abaqus.Odb.OdbStepBase.FieldOutput.setValidInvariants.validInvariants "abaqus.Odb.OdbStepBase.FieldOutput.setValidInvariants.validInvariants (Python parameter) — A sequence of SymbolicConstants specifying which invariants should be calculated for this field.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L743-L783)[¶](#abaqus.Odb.OdbStepBase.FieldOutput.setValidInvariants "Permalink to this definition")
    :   This method sets the invariants valid for the FieldOutput object.

        Note

        Check [FieldOutput.setValidInvariants on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldoutputpyc.htm?contextscope=all#simaker-fieldoutputsetvalidinvariantspyc).

        Parameters:[¶](#abaqus.Odb.OdbStepBase.FieldOutput.setValidInvariants-parameters "Permalink to this headline")
        :   validInvariants[¶](#abaqus.Odb.OdbStepBase.FieldOutput.setValidInvariants.validInvariants "Permalink to this definition")
            :   A sequence of SymbolicConstants specifying which invariants should be calculated for
                this field. An empty sequence indicates that no invariants are valid for this field.
                Possible values are:

                * MAGNITUDE
                * MISES
                * TRESCA
                * PRESS
                * INV3
                * MAX\_PRINCIPAL
                * MID\_PRINCIPAL
                * MIN\_PRINCIPAL
                * MAX\_INPLANE\_PRINCIPAL
                * MIN\_INPLANE\_PRINCIPAL
                * OUTOFPLANE\_PRINCIPAL

                The default value is an empty sequence.

    type : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py)[¶](#abaqus.Odb.OdbStepBase.FieldOutput.type "Permalink to this definition")
    :   A SymbolicConstant specifying the output type. Possible values are SCALAR, VECTOR,
        TENSOR\_3D\_FULL, TENSOR\_3D\_PLANAR, TENSOR\_3D\_SURFACE, TENSOR\_2D\_PLANAR, and
        TENSOR\_2D\_SURFACE.

    validInvariants : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py)[¶](#abaqus.Odb.OdbStepBase.FieldOutput.validInvariants "Permalink to this definition")
    :   A sequence of SymbolicConstants specifying which invariants should be calculated for
        this field. An empty sequence indicates that no invariants are valid for this field.
        Possible values
        are:MAGNITUDEMISESTRESCAPRESSINV3MAX\_PRINCIPALMID\_PRINCIPALMIN\_PRINCIPALMAX\_INPLANE\_PRINCIPALMIN\_INPLANE\_PRINCIPALOUTOFPLANE\_PRINCIPALThe
        default value is an empty sequence.

    values : --is-rst--:py:data:`~typing.Optional`\[:py:class:`~typing.List`\[:py:class:`~abaqus.Odb.FieldValue.FieldValue`]] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L46-L49)[¶](#abaqus.Odb.OdbStepBase.FieldOutput.values "Permalink to this definition")
    :   A FieldValueArray object specifying the order of the objects in the array is determined
        by the Abaqus Scripting Interface; see the **data** argument to the addData method for a
        description of the order.

*class* OdbMeshElement[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbSet.py#L12-L105)[¶](#abaqus.Odb.OdbSet.OdbMeshElement "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    OdbMeshElement objects are created with the part.addElements or rootAssembly.addElements methods.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].parts[name].elements[i]
    session.odbs[name].parts[name].elementSets[name].elements[i]
    session.odbs[name].parts[name].nodeSets[name].elements[i]
    session.odbs[name].parts[name].surfaces[name].elements[i]
    session.odbs[name].rootAssembly.elements[i]
    session.odbs[name].rootAssembly.elementSets[name].elements[i]
    session.odbs[name].rootAssembly.instances[name].elements[i]
    session.odbs[name].rootAssembly.instances[name].elementSets[name].elements[i]
    session.odbs[name].rootAssembly.instances[name].nodeSets[name].elements[i]
    session.odbs[name].rootAssembly.instances[name].surfaces[name].elements[i]
    session.odbs[name].rootAssembly.nodeSets[name].elements[i]
    session.odbs[name].rootAssembly.surfaces[name].elements[i]
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.elements[i]
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.elementSets[name].elements[i]
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.nodeSets[name].elements[i]
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.surfaces[name].elements[i]
    ```

    Note

    Check [OdbMeshElement on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshelementpyc.htm?contextscope=all).

    Member Details:

    connectivity : --is-rst--:py:class:`tuple`\[:py:class:`int`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbSet.py#L47-L52)[¶](#abaqus.Odb.OdbSet.OdbMeshElement.connectivity "Permalink to this definition")
    :   A tuple of Ints specifying the element connectivity. For connector elements connected to
        ground, the other node is repeated in the connectivity data. The position of the ground
        node cannot be ascertained. This is a limitation. It is important to note the difference
        with MeshElement object of MDB where the connectivity is node indices instead of node
        labels.

    getNormal(*[faceIndex](#abaqus.Odb.OdbSet.OdbMeshElement.getNormal.faceIndex "abaqus.Odb.OdbSet.OdbMeshElement.getNormal.faceIndex (Python parameter) — The value of faceIndex is 0 for a shell element and can range from 0 to 5 for a solid element.")*, *[stepName](#abaqus.Odb.OdbSet.OdbMeshElement.getNormal.stepName "abaqus.Odb.OdbSet.OdbMeshElement.getNormal.stepName (Python parameter) — Name of the step.")=`''`*, *[frameValue](#abaqus.Odb.OdbSet.OdbMeshElement.getNormal.frameValue "abaqus.Odb.OdbSet.OdbMeshElement.getNormal.frameValue (Python parameter) — A Double specifying the value at which the frame is required.")=`''`*, *[match](#abaqus.Odb.OdbSet.OdbMeshElement.getNormal.match "abaqus.Odb.OdbSet.OdbMeshElement.getNormal.match (Python parameter) — A SymbolicConstant specifying which frame to return if there is no frame at the exact frame value.")=`abaqusConstants.CLOSEST`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbSet.py#L60-L105)[¶](#abaqus.Odb.OdbSet.OdbMeshElement.getNormal "Permalink to this definition")
    :   This method returns the normal direction for the element face.

        New in version 2017: The getNormal method was added.

        Note

        Check [OdbMeshElement.getNormal on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshelementpyc.htm?contextscope=all#simaker-odbmeshelementgetnormalpyc).

        Parameters:[¶](#abaqus.Odb.OdbSet.OdbMeshElement.getNormal-parameters "Permalink to this headline")
        :   faceIndex[¶](#abaqus.Odb.OdbSet.OdbMeshElement.getNormal.faceIndex "Permalink to this definition")
            :   The value of **faceIndex** is 0 for a shell element and can range from 0 to 5 for a solid
                element.

            stepName=`''`[¶](#abaqus.Odb.OdbSet.OdbMeshElement.getNormal.stepName "Permalink to this definition")
            :   Name of the step.

            frameValue=`''`[¶](#abaqus.Odb.OdbSet.OdbMeshElement.getNormal.frameValue "Permalink to this definition")
            :   A Double specifying the value at which the frame is required. **frameValue** can be the
                total fime or frequency.

            match=`abaqusConstants.CLOSEST`[¶](#abaqus.Odb.OdbSet.OdbMeshElement.getNormal.match "Permalink to this definition")
            :   A SymbolicConstant specifying which frame to return if there is no frame at the exact
                frame value. Possible values are CLOSEST, BEFORE, AFTER, and EXACT. The default value is
                CLOSEST.When **match** = CLOSEST, Abaqus returns the closest frame. If the frame value
                requested is exactly halfway between two frames, Abaqus returns the frame after the
                value.When **match** = EXACT, Abaqus raises an exception if the exact frame value does not
                exist.

        Returns:[¶](#abaqus.Odb.OdbSet.OdbMeshElement.getNormal-returns "Permalink to this headline")
        :   A tuple of 3 floats representing the unit normal vector. If the element face is
            collapsed such that a normal cannot be computed, a zero-length vector is returned.

        Raises:[¶](#abaqus.Odb.OdbSet.OdbMeshElement.getNormal-raises "Permalink to this headline")
        :   * **OdbError** – Frame not found, If the exact frame is not found.
            * **OdbError** – Step is not present in the ODB, If the step name is not found.
            * **OdbError** – If **frameValue** is not provided and **stepName** is empty.

    instanceName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbSet.py#L57-L58)[¶](#abaqus.Odb.OdbSet.OdbMeshElement.instanceName "Permalink to this definition")
    :   A String specifying the instance name.

    instanceNames : --is-rst--:py:class:`tuple`\[:py:class:`str`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbSet.py#L54-L55)[¶](#abaqus.Odb.OdbSet.OdbMeshElement.instanceNames "Permalink to this definition")
    :   A tuple of Strings specifying the instance names for nodes in the element connectivity.

    label : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbSet.py#L38-L39)[¶](#abaqus.Odb.OdbSet.OdbMeshElement.label "Permalink to this definition")
    :   An Int specifying the element label.

    sectionCategory : --is-rst--:py:data:`~typing.Optional`\[:py:class:`~abaqus.Odb.SectionCategory.SectionCategory`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbSet.py#L44-L45)[¶](#abaqus.Odb.OdbSet.OdbMeshElement.sectionCategory "Permalink to this definition")
    :   A SectionCategory object specifying the element section properties.

    type : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbSet.py#L41-L42)[¶](#abaqus.Odb.OdbSet.OdbMeshElement.type "Permalink to this definition")
    :   A String specifying the element type.

*class* OdbMeshNode[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbSet.py#L6-L33)[¶](#abaqus.Odb.OdbSet.OdbMeshNode "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    OdbMeshNode objects are created with the part.addNodes method.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].parts[name].nodes[i]
    session.odbs[name].parts[name].nodeSets[name].nodes[i]
    session.odbs[name].parts[name].surfaces[name].nodes[i]
    session.odbs[name].rootAssembly.instances[name].nodes[i]
    session.odbs[name].rootAssembly.instances[name].nodeSets[name].nodes[i]
    session.odbs[name].rootAssembly.instances[name].surfaces[name].nodes[i]
    session.odbs[name].rootAssembly.nodes[i]
    session.odbs[name].rootAssembly.nodeSets[name].nodes[i]
    session.odbs[name].rootAssembly.surfaces[name].nodes[i]
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.nodes[i]
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.nodeSets[name].nodes[i]
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.surfaces[name].nodes[i]
    ```

    Note

    Check [OdbMeshNode on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbmeshnodepyc.htm?contextscope=all).

    Member Details:

    coordinates : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbSet.py#L6-L33)[¶](#abaqus.Odb.OdbSet.OdbMeshNode.coordinates "Permalink to this definition")
    :   A tuple of Floats specifying the nodal coordinates in the global Cartesian coordinate
        system.

    label : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbSet.py#L28-L29)[¶](#abaqus.Odb.OdbSet.OdbMeshNode.label "Permalink to this definition")
    :   An Int specifying the node label.

*class* FieldValue[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py#L11-L162)[¶](#abaqus.Odb.FieldValueArray.FieldValue "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The FieldValue object represents the field data at a point. The FieldValue object has no constructor; it
    is created by the Odb object when data are added to the FieldOutput object using the addData method. For
    faster, bulk-data access, see Using bulk data access to an output database.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i]
    ```

    Note

    Check [FieldValue on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-fieldvaluepyc.htm?contextscope=all).

    Member Details:

    conjugateData : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py#L144-L147)[¶](#abaqus.Odb.FieldValueArray.FieldValue.conjugateData "Permalink to this definition")
    :   A tuple of Floats specifying data in the form described by **type**. If **type** = TENSOR or
        VECTOR, **conjugateData** is a sequence containing the components. If the underlying data
        are in double precision, an exception will be thrown.

    conjugateDataDouble : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py#L11-L162)[¶](#abaqus.Odb.FieldValueArray.FieldValue.conjugateDataDouble "Permalink to this definition")
    :   A tuple of Floats specifying data in the form described by **type**. If **type** = TENSOR or
        VECTOR, **conjugateData** is a sequence containing the components. If the underlying data
        are in single precision, an exception will be thrown.

    data : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py#L144-L147)[¶](#abaqus.Odb.FieldValueArray.FieldValue.data "Permalink to this definition")
    :   A tuple of Floats specifying data in the form described by **type**. If **type** = TENSOR or
        VECTOR, **data** is a sequence containing the components. If the underlying data are in
        double precision an exception will be thrown.

    dataDouble : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py#L144-L147)[¶](#abaqus.Odb.FieldValueArray.FieldValue.dataDouble "Permalink to this definition")
    :   A tuple of Floats specifying data in the form described by **type**. If **type** = TENSOR or
        VECTOR, **data** is a sequence containing the components. If the underlying data are in
        single precision, an exception will be thrown.

    elementLabel : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py#L44-L47)[¶](#abaqus.Odb.FieldValueArray.FieldValue.elementLabel "Permalink to this definition")
    :   An Int specifying the element label of the element containing the location.
        **elementLabel** is available only if **position** = INTEGRATION\_POINT, CENTROID,
        ELEMENT\_NODAL, or ELEMENT\_FACE.

    face : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py)[¶](#abaqus.Odb.FieldValueArray.FieldValue.face "Permalink to this definition")
    :   A SymbolicConstant specifying the face of the element. **face** is available only if
        **position** = ELEMENT\_FACE.

    instance : --is-rst--:py:class:`~abaqus.Odb.OdbInstance.OdbInstance` = `<abaqus.Odb.OdbInstance.OdbInstance object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py#L120-L121)[¶](#abaqus.Odb.FieldValueArray.FieldValue.instance "Permalink to this definition")
    :   An OdbInstance object specifying the part to which the labels belong.

    integrationPoint : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py#L53-L55)[¶](#abaqus.Odb.FieldValueArray.FieldValue.integrationPoint "Permalink to this definition")
    :   An Int specifying the integration point in the element. **integrationPoint** is available
        only if **position** = INTEGRATION\_POINT.

    inv3 : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py#L85-L88)[¶](#abaqus.Odb.FieldValueArray.FieldValue.inv3 "Permalink to this definition")
    :   A Float specifying the calculated third stress invariant. The value is valid only when
        the **validInvariants** member includes INV3; otherwise, the value is indeterminate.
        Conjugate data will be ignored in invariant calculation.

    localCoordSystem : --is-rst--:py:class:`tuple`\[:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`], :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py#L126-L133)[¶](#abaqus.Odb.FieldValueArray.FieldValue.localCoordSystem "Permalink to this definition")
    :   A tuple of tuples of Floats specifying the 3 x 3 matrix of Floats specifying the
        direction cosines of the local coordinate system (the rotation from global to local).
        Each sequence represents a row in the direction cosine matrix. **localCoordSystem** is
        available for TENSOR data written in a local coordinate system. It is also available for
        VECTOR data for connector element outputs. For connector element outputs the rotation is
        from local to global. If the underlying data are in double precision, an exception will
        be thrown.

    localCoordSystemDouble : --is-rst--:py:class:`tuple`\[:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`], :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py#L135-L142)[¶](#abaqus.Odb.FieldValueArray.FieldValue.localCoordSystemDouble "Permalink to this definition")
    :   A tuple of tuples of Floats specifying the 3 x 3 matrix of Doubles specifying the
        direction cosines of the local coordinate system (the rotation from global to local).
        Each sequence represents a row in the direction cosine matrix. **localCoordSystemDouble**
        is available for TENSOR data written in a local coordinate system. It is also available
        for VECTOR data for connector element outputs. For connector element outputs the
        rotation is from local to global. If the underlying data are in single precision, an
        exception will be thrown.

    magnitude : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py#L66-L68)[¶](#abaqus.Odb.FieldValueArray.FieldValue.magnitude "Permalink to this definition")
    :   A Float specifying the length or magnitude of the vector. **magnitude** is valid only when
        **type** = VECTOR.

    maxInPlanePrincipal : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py#L105-L108)[¶](#abaqus.Odb.FieldValueArray.FieldValue.maxInPlanePrincipal "Permalink to this definition")
    :   A Float specifying the maximum principal in-plane stress. The value is valid only when
        the **validInvariants** member includes MAX\_INPLANE\_PRINCIPAL; otherwise, the value is
        indeterminate. Conjugate data will be ignored in invariant calculation.

    maxPrincipal : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py#L90-L93)[¶](#abaqus.Odb.FieldValueArray.FieldValue.maxPrincipal "Permalink to this definition")
    :   A Float specifying the calculated maximum principal stress. The value is valid only when
        the **validInvariants** member includes MAX\_PRINCIPAL; otherwise, the value is
        indeterminate. Conjugate data will be ignored in invariant calculation.

    midPrincipal : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py#L95-L98)[¶](#abaqus.Odb.FieldValueArray.FieldValue.midPrincipal "Permalink to this definition")
    :   A Float specifying the calculated intermediate principal stress. The value is valid only
        when the **validInvariants** member includes MID\_PRINCIPAL; otherwise, the value is
        indeterminate. Conjugate data will be ignored in invariant calculation.

    minInPlanePrincipal : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py#L110-L113)[¶](#abaqus.Odb.FieldValueArray.FieldValue.minInPlanePrincipal "Permalink to this definition")
    :   A Float specifying the calculated minimum principal in-plane stress. The value is valid
        only when the **validInvariants** member includes MIN\_INPLANE\_PRINCIPAL; otherwise, the
        value is indeterminate. Conjugate data will be ignored in invariant calculation.

    minPrincipal : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py#L100-L103)[¶](#abaqus.Odb.FieldValueArray.FieldValue.minPrincipal "Permalink to this definition")
    :   A Float specifying the minimum principal stress. The value is valid only when the
        **validInvariants** member includes MIN\_PRINCIPAL; otherwise, the value is indeterminate.
        Conjugate data will be ignored in invariant calculation.

    mises : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py#L70-L73)[¶](#abaqus.Odb.FieldValueArray.FieldValue.mises "Permalink to this definition")
    :   A Float specifying the calculated von Mises stress. The value is valid only when the
        **validInvariants** member includes MISES; otherwise, the value is indeterminate.
        Conjugate data will be ignored in invariant calculation.

    nodeLabel : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py#L49-L51)[¶](#abaqus.Odb.FieldValueArray.FieldValue.nodeLabel "Permalink to this definition")
    :   An Int specifying the node label of the node containing the location. **nodelabel** is
        available only if **position** = ELEMENT\_NODAL or NODAL.

    outOfPlanePrincipal : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py#L115-L118)[¶](#abaqus.Odb.FieldValueArray.FieldValue.outOfPlanePrincipal "Permalink to this definition")
    :   A Float specifying the calculated principal out-of-plane stress. The value is valid only
        when the **validInvariants** member includes OUTOFPLANE\_PRINCIPAL; otherwise, the value is
        indeterminate. Conjugate data will be ignored in invariant calculation.

    position : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py)[¶](#abaqus.Odb.FieldValueArray.FieldValue.position "Permalink to this definition")
    :   A SymbolicConstant specifying the position of the output in the element. Possible values
        are:

        * NODAL, specifying the values calculated at the nodes.
        * INTEGRATION\_POINT, specifying the values calculated at the integration points.
        * ELEMENT\_NODAL, specifying the values obtained by extrapolating results calculated at
          the integration points.
        * ELEMENT\_FACE, specifying the results obtained for surface variables such as cavity
          radiation that are defined for the surface facets of an element.
        * CENTROID, specifying the value at the centroid obtained by extrapolating results
          calculated at the integration points.

    precision : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py)[¶](#abaqus.Odb.FieldValueArray.FieldValue.precision "Permalink to this definition")
    :   A SymbolicConstant specifying the precision of the output in the element. Possible
        values are:

        * SINGLE\_PRECISION, specifying that the output values are in single precision.
        * DOUBLE\_PRECISION, specifying that the output values are in double precision.

    press : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py#L80-L83)[¶](#abaqus.Odb.FieldValueArray.FieldValue.press "Permalink to this definition")
    :   A Float specifying the calculated pressure stress. The value is valid only when the
        **validInvariants** member includes PRESS; otherwise, the value is indeterminate.
        Conjugate data will be ignored in invariant calculation.

    sectionPoint : --is-rst--:py:data:`~typing.Optional`\[:py:class:`~abaqus.Odb.SectionPoint.SectionPoint`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py#L123-L124)[¶](#abaqus.Odb.FieldValueArray.FieldValue.sectionPoint "Permalink to this definition")
    :   A SectionPoint object.

    tresca : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py#L75-L78)[¶](#abaqus.Odb.FieldValueArray.FieldValue.tresca "Permalink to this definition")
    :   A Float specifying the calculated Tresca stress. The value is valid only when the
        **validInvariants** member includes TRESCA; otherwise, the value is indeterminate.
        Conjugate data will be ignored in invariant calculation.

    type : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/FieldValueArray.py)[¶](#abaqus.Odb.FieldValueArray.FieldValue.type "Permalink to this definition")
    :   A SymbolicConstant specifying the output type. Possible values are SCALAR, VECTOR,
        TENSOR\_3D\_FULL, TENSOR\_3D\_PLANAR, TENSOR\_3D\_SURFACE, TENSOR\_2D\_PLANAR, and
        TENSOR\_2D\_SURFACE.

*class* HistoryOutput(*[name](#abaqus.Odb.HistoryRegion.HistoryOutput "abaqus.Odb.HistoryRegion.HistoryOutput.__init__.name (Python parameter)")*, *[description](#abaqus.Odb.HistoryRegion.HistoryOutput "abaqus.Odb.HistoryRegion.HistoryOutput.__init__.description (Python parameter)")*, *[type](#abaqus.Odb.HistoryRegion.HistoryOutput "abaqus.Odb.HistoryRegion.HistoryOutput.__init__.type (Python parameter)")*, *[validInvariants](#abaqus.Odb.HistoryRegion.HistoryOutput "abaqus.Odb.HistoryRegion.HistoryOutput.__init__.validInvariants (Python parameter)")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/HistoryRegion.py#L13-L136)[¶](#abaqus.Odb.HistoryRegion.HistoryOutput "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The HistoryOutput object contains the history output at a point for the specified variable.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].steps[name].historyRegions[name].historyOutputs[name]
    ```

    Note

    Check [HistoryOutput on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyoutputpyc.htm?contextscope=all).

    Member Details:

    addData(*[frame](#abaqus.Odb.HistoryRegion.HistoryOutput.addData "abaqus.Odb.HistoryRegion.HistoryOutput.addData.frame (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[value](#abaqus.Odb.HistoryRegion.HistoryOutput.addData "abaqus.Odb.HistoryRegion.HistoryOutput.addData.value (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/HistoryRegion.py#L136-L136)[¶](#abaqus.Odb.HistoryRegion.HistoryOutput.addData "Permalink to this definition")

    addData(*[frame](#abaqus.Odb.HistoryRegion.HistoryOutput.addData "abaqus.Odb.HistoryRegion.HistoryOutput.addData.frame (Python parameter)"): [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")*, *[value](#abaqus.Odb.HistoryRegion.HistoryOutput.addData "abaqus.Odb.HistoryRegion.HistoryOutput.addData.value (Python parameter)"): [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")*)

    addData(*[data](#abaqus.Odb.HistoryRegion.HistoryOutput.addData "abaqus.Odb.HistoryRegion.HistoryOutput.addData.data (Python parameter)"): [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")*)

    addData(*\*[args](#abaqus.Odb.HistoryRegion.HistoryOutput.addData "abaqus.Odb.HistoryRegion.HistoryOutput.addData.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Odb.HistoryRegion.HistoryOutput.addData "abaqus.Odb.HistoryRegion.HistoryOutput.addData.kwargs (Python parameter)")*)

    conjugateData : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/HistoryRegion.py#L29-L32)[¶](#abaqus.Odb.HistoryRegion.HistoryOutput.conjugateData "Permalink to this definition")
    :   A tuple of pairs of Floats specifying the imaginary portion of a specified complex
        variable at each frame value (time, frequency, or mode). The pairs have the form
        (*frameValue*, **value**).

    data : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/HistoryRegion.py#L24-L27)[¶](#abaqus.Odb.HistoryRegion.HistoryOutput.data "Permalink to this definition")
    :   A tuple of pairs of Floats specifying the pairs (*frameValue*, **value**) where
        **frameValue** is either time, frequency, or mode and **value** is the value of the
        specified variable at **frameValue**. (This value depends on the type of the variable.)

    description : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/HistoryRegion.py)[¶](#abaqus.Odb.HistoryRegion.HistoryOutput.description "Permalink to this definition")
    :   A String specifying the output variable.

    name : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/HistoryRegion.py)[¶](#abaqus.Odb.HistoryRegion.HistoryOutput.name "Permalink to this definition")
    :   A String specifying the output variable name.

    type : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/HistoryRegion.py)[¶](#abaqus.Odb.HistoryRegion.HistoryOutput.type "Permalink to this definition")
    :   A SymbolicConstant specifying the output type. Only SCALAR is currently supported.

    validInvariants : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/HistoryRegion.py)[¶](#abaqus.Odb.HistoryRegion.HistoryOutput.validInvariants "Permalink to this definition")
    :   A sequence of SymbolicConstants specifying which invariants should be calculated for
        this field. Possible values are MAGNITUDE, MISES, TRESCA, PRESS, INV3, MAX\_PRINCIPAL,
        MID\_PRINCIPAL, and MIN\_PRINCIPAL. The default value is an empty sequence.

*class* HistoryPoint(*[node](#abaqus.Odb.OdbStepBase.HistoryPoint "abaqus.Odb.OdbStepBase.HistoryPoint.__init__.node (Python parameter)"): [OdbMeshNode](#abaqus.Odb.OdbSet.OdbMeshNode "abaqus.Odb.OdbMeshNode.OdbMeshNode (Python class)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L22-L239)[¶](#abaqus.Odb.OdbStepBase.HistoryPoint "Permalink to this definition")

*class* HistoryPoint(*[element](#abaqus.Odb.OdbStepBase.HistoryPoint "abaqus.Odb.OdbStepBase.HistoryPoint.__init__.element (Python parameter)"): [OdbMeshElement](#abaqus.Odb.OdbSet.OdbMeshElement "abaqus.Odb.OdbMeshElement.OdbMeshElement (Python class)")*, *[ipNumber](#abaqus.Odb.OdbStepBase.HistoryPoint "abaqus.Odb.OdbStepBase.HistoryPoint.__init__.ipNumber (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)") = `0`*, *[sectionPoint](#abaqus.Odb.OdbStepBase.HistoryPoint "abaqus.Odb.OdbStepBase.HistoryPoint.__init__.sectionPoint (Python parameter)"): [SectionPoint](#abaqus.Odb.SectionPointArray.SectionPoint "abaqus.Odb.SectionPoint.SectionPoint (Python class)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*, *[face](#abaqus.Odb.OdbStepBase.HistoryPoint "abaqus.Odb.OdbStepBase.HistoryPoint.__init__.face (Python parameter)"): [SymbolicConstant](kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.SymbolicConstant "abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant (Python class)") = `FACE_UNKNOWN`*, *[node](#abaqus.Odb.OdbStepBase.HistoryPoint "abaqus.Odb.OdbStepBase.HistoryPoint.__init__.node (Python parameter)"): [OdbMeshNode](#abaqus.Odb.OdbSet.OdbMeshNode "abaqus.Odb.OdbMeshNode.OdbMeshNode (Python class)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)

*class* HistoryPoint(*[region](#abaqus.Odb.OdbStepBase.HistoryPoint "abaqus.Odb.OdbStepBase.HistoryPoint.__init__.region (Python parameter)"): [OdbSet](#abaqus.Odb.RebarOrientation.OdbSet "abaqus.Odb.OdbSet.OdbSet (Python class)")*)

*class* HistoryPoint(*[assembly](#abaqus.Odb.OdbStepBase.HistoryPoint "abaqus.Odb.OdbStepBase.HistoryPoint.__init__.assembly (Python parameter)"): [OdbAssembly](#abaqus.Odb.OdbBase.OdbAssembly "abaqus.Odb.OdbAssembly.OdbAssembly (Python class)")*)

*class* HistoryPoint(*[instance](#abaqus.Odb.OdbStepBase.HistoryPoint "abaqus.Odb.OdbStepBase.HistoryPoint.__init__.instance (Python parameter)"): [OdbInstance](#abaqus.Odb.OdbInstance.OdbInstance "abaqus.Odb.OdbInstance.OdbInstance (Python class) — Bases: OdbInstanceBase")*)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The HistoryPoint object specifies the point at which history data will be collected. The HistoryPoint
    object is a temporary object used as an argument to the HistoryRegion method.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].steps[name].historyRegions[name].point
    ```

    Note

    Check [HistoryPoint on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historypointpyc.htm?contextscope=all).

    Member Details:

    assembly : --is-rst--:py:class:`~abaqus.Odb.OdbAssembly.OdbAssembly` = `<abaqus.Odb.OdbAssembly.OdbAssembly object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L86-L87)[¶](#abaqus.Odb.OdbStepBase.HistoryPoint.assembly "Permalink to this definition")
    :   An OdbAssembly object specifying the assembly for which the data are to be collected.

    element : --is-rst--:py:class:`~abaqus.Odb.OdbMeshElement.OdbMeshElement` = `<abaqus.Odb.OdbMeshElement.OdbMeshElement object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L77-L78)[¶](#abaqus.Odb.OdbStepBase.HistoryPoint.element "Permalink to this definition")
    :   An OdbMeshElement object specifying the element for which the data are to be collected.

    face : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FACE_UNKNOWN'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L56-L57)[¶](#abaqus.Odb.OdbStepBase.HistoryPoint.face "Permalink to this definition")
    :   A SymbolicConstant specifying the element face. This argument is used to define a
        history output position of ELEMENT\_FACE or ELEMENT\_FACE\_INTEGRATION\_POINT. Possible
        values are:

        * FACE\_UNKOWN, specifying this value indicates that no value has been specified.
        * FACE1, specifying this value indicates that element face 1 has been specified.
        * FACE2, specifying this value indicates that element face 2 has been specified.
        * FACE3, specifying this value indicates that element face 3 has been specified.
        * FACE4, specifying this value indicates that element face 4 has been specified.
        * FACE5, specifying this value indicates that element face 5 has been specified.
        * FACE6, specifying this value indicates that element face 6 has been specified.
        * SIDE1, specifying this value indicates that element side 1 has been specified.
        * SIDE2, specifying this value indicates element side 2 has been specified.
        * END1, specifying this value indicates that element end 1 has been specified.
        * END2, specifying this value indicates that element end 2 has been specified.
        * END3, specifying this value indicates that element end 3 has been specified.

        The default value is FACE\_UNKNOWN.

    instance : --is-rst--:py:class:`~abaqus.Odb.OdbInstance.OdbInstance` = `<abaqus.Odb.OdbInstance.OdbInstance object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L89-L90)[¶](#abaqus.Odb.OdbStepBase.HistoryPoint.instance "Permalink to this definition")
    :   An OdbInstance object specifying the instance for which the data are to be collected.

    ipNumber : --is-rst--:py:class:`int` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L34-L37)[¶](#abaqus.Odb.OdbStepBase.HistoryPoint.ipNumber "Permalink to this definition")
    :   An Int specifying the integration point. This argument is used to define a history
        output position of INTEGRATION\_POINT or ELEMENT\_FACE\_INTEGRATION\_POINT. The default
        value is 0.

    node : --is-rst--:py:class:`~abaqus.Odb.OdbMeshNode.OdbMeshNode`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py)[¶](#abaqus.Odb.OdbStepBase.HistoryPoint.node "Permalink to this definition")
    :   An OdbMeshNode object specifying the node for which the data are to be collected.

    position : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py)[¶](#abaqus.Odb.OdbStepBase.HistoryPoint.position "Permalink to this definition")
    :   A SymbolicConstant specifying the result position of the history point. Possible values
        are:

        * NODAL, specifying the values calculated at the nodes.
        * ELEMENT\_NODAL, specifying the values obtained by extrapolating results calculated at
          the integration points.
        * INTEGRATION\_POINT, specifying the values calculated at the integration points.
        * ELEMENT\_FACE, specifying the results obtained for surface variables such as cavity
          radiation that are defined for the surface facets of an element.
        * ELEMENT\_FACE\_INTEGRATION\_POINT, specifying the results obtained for surface variables
          such as cavity radiation that are defined for the surface facets of an element when the
          surface facets have integration points.
        * WHOLE\_ELEMENT, specifying the results obtained for whole element variables.
        * WHOLE\_REGION, specifying the results for an entire region of the model.
        * WHOLE\_PART\_INSTANCE, specifying the results for an entire part instance of the model.
        * WHOLE\_MODEL, specifying the results for the entire model.

    region : --is-rst--:py:class:`~abaqus.Odb.OdbSet.OdbSet` = `<abaqus.Odb.OdbSet.OdbSet object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L83-L84)[¶](#abaqus.Odb.OdbStepBase.HistoryPoint.region "Permalink to this definition")
    :   An OdbSet object specifying the region for which the data are to be collected.

    sectionPoint : --is-rst--:py:class:`~abaqus.Odb.SectionPoint.SectionPoint`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py)[¶](#abaqus.Odb.OdbStepBase.HistoryPoint.sectionPoint "Permalink to this definition")
    :   A SectionPoint object.

*class* OdbAssembly[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L21-L327)[¶](#abaqus.Odb.OdbBase.OdbAssembly "Permalink to this definition")
:   Bases: [`OdbAssemblyBase`](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase (Python class) — Bases: object")

    Member Details:

    DatumCsys(*[name](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsys.name "abaqus.Odb.OdbBase.OdbAssembly.DatumCsys.name (Python parameter) — A String specifying the repository key.")*, *[datumCsys](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsys.datumCsys "abaqus.Odb.OdbBase.OdbAssembly.DatumCsys.datumCsys (Python parameter) — An OdbDatumCsys object specifying the object to be copied.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L180-L202)[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsys "Permalink to this definition")
    :   This method copies oneOdbDatumCsys object to a new OdbDatumCsys object.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].rootAssembly.DatumCsys
        ```

        Note

        Check [DatumCsys on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsys-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsys.name "Permalink to this definition")
            :   A String specifying the repository key.

            datumCsys[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsys.datumCsys "Permalink to this definition")
            :   An OdbDatumCsys object specifying the object to be copied.

        Returns:[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsys-returns "Permalink to this headline")
        :   An OdbDatumCsys object.

        Return type:[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsys-return-type "Permalink to this headline")
        :   `OdbDatumCsys`

    DatumCsysBy6dofNode(*[name](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysBy6dofNode.name "abaqus.Odb.OdbBase.OdbAssembly.DatumCsysBy6dofNode.name (Python parameter) — A String specifying the repository key.")*, *[coordSysType](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysBy6dofNode.coordSysType "abaqus.Odb.OdbBase.OdbAssembly.DatumCsysBy6dofNode.coordSysType (Python parameter) — A SymbolicConstant specifying the type of coordinate system.")*, *[origin](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysBy6dofNode.origin "abaqus.Odb.OdbBase.OdbAssembly.DatumCsysBy6dofNode.origin (Python parameter) — An OdbMeshNode object specifying the origin of the datum coordinate system.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L147-L178)[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysBy6dofNode "Permalink to this definition")
    :   A datum coordinate system created with this method results in a system that follows the position of a
        node. The node location defines the origin of the datum coordinate system. The rotational displacement
        (UR1, UR2, UR3) of the node defines the orientation of the coordinate system axes. Results, such as
        those for displacement, are resolved into the orientation of the datum coordinate system without regard
        to the position of its origin. The last argument is given in the form of an OdbMeshNode object.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].rootAssembly.DatumCsysBy6dofNode
        ```

        Note

        Check [DatumCsysBy6dofNode on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsysby6dofnodepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysBy6dofNode-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysBy6dofNode.name "Permalink to this definition")
            :   A String specifying the repository key.

            coordSysType[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysBy6dofNode.coordSysType "Permalink to this definition")
            :   A SymbolicConstant specifying the type of coordinate system. Possible values are
                CARTESIAN, CYLINDRICAL, and SPHERICAL.

            origin[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysBy6dofNode.origin "Permalink to this definition")
            :   An OdbMeshNode object specifying the origin of the datum coordinate system.

        Returns:[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysBy6dofNode-returns "Permalink to this headline")
        :   An OdbDatumCsys object.

        Return type:[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysBy6dofNode-return-type "Permalink to this headline")
        :   `OdbDatumCsys`

    DatumCsysByThreeCircNodes(*[name](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeCircNodes.name "abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeCircNodes.name (Python parameter) — A String specifying the repository key.")*, *[coordSysType](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeCircNodes.coordSysType "abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeCircNodes.coordSysType (Python parameter) — A SymbolicConstant specifying the type of coordinate system.")*, *[node1Arc](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeCircNodes.node1Arc "abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeCircNodes.node1Arc (Python parameter) — An OdbMeshNode object that lies on the circular arc.")*, *[node2Arc](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeCircNodes.node2Arc "abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeCircNodes.node2Arc (Python parameter) — An OdbMeshNode object that lies on the circular arc.")*, *[node3Arc](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeCircNodes.node3Arc "abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeCircNodes.node3Arc (Python parameter) — An OdbMeshNode object that lies on the circular arc.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L105-L145)[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeCircNodes "Permalink to this definition")
    :   This method is convenient to use where there are no nodes along the axis of a hollow cylinder or at
        the center of a hollow sphere. The three nodes that you provide as arguments determine a circle in
        space. The center of the circle is the origin of the datum coordinate system. The normal to the circle
        is parallel to the zz-axis of a cylindrical coordinate system or to the ϕϕ-axis of a spherical
        coordinate system. The line from the origin to the first node defines the rr-axis.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].rootAssembly.DatumCsysByThreeCircNodes
        ```

        Note

        Check [DatumCsysByThreeCircNodes on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsysbythreecircnodespyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeCircNodes-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeCircNodes.name "Permalink to this definition")
            :   A String specifying the repository key.

            coordSysType[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeCircNodes.coordSysType "Permalink to this definition")
            :   A SymbolicConstant specifying the type of coordinate system. Possible values are
                CARTESIAN, CYLINDRICAL, and SPHERICAL.

            node1Arc[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeCircNodes.node1Arc "Permalink to this definition")
            :   An OdbMeshNode object that lies on the circular arc.

            node2Arc[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeCircNodes.node2Arc "Permalink to this definition")
            :   An OdbMeshNode object that lies on the circular arc.

            node3Arc[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeCircNodes.node3Arc "Permalink to this definition")
            :   An OdbMeshNode object that lies on the circular arc.

        Returns:[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeCircNodes-returns "Permalink to this headline")
        :   An OdbDatumCsys object.

        Return type:[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeCircNodes-return-type "Permalink to this headline")
        :   `OdbDatumCsys`

    DatumCsysByThreeNodes(*[name](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeNodes.name "abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeNodes.name (Python parameter) — A String specifying the repository key.")*, *[coordSysType](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeNodes.coordSysType "abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeNodes.coordSysType (Python parameter) — A SymbolicConstant specifying the type of coordinate system.")*, *[origin](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeNodes.origin "abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeNodes.origin (Python parameter) — An OdbMeshNode object specifying a node at the origin of the datum coordinate system.")*, *[point1](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeNodes.point1 "abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeNodes.point1 (Python parameter) — An OdbMeshNode object specifying a node on the local 1- or rr-axis.")*, *[point2](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeNodes.point2 "abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeNodes.point2 (Python parameter) — An OdbMeshNode object specifying a node in the 1-2 or rr-θθ plane.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L63-L103)[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeNodes "Permalink to this definition")
    :   This method creates an OdbDatumCsys object using the coordinates of three OdbMeshNode objects. A
        datum coordinate system created with this method results in a system that follows the position of the
        three nodes. Results, such as those for displacement, are resolved into the orientation of the datum
        coordinate system without regard to the position of its origin. The last three arguments are given in
        the form of an OdbMeshNode object.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].rootAssembly.DatumCsysByThreeNodes
        ```

        Note

        Check [DatumCsysByThreeNodes on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsysbythreenodespyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeNodes-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeNodes.name "Permalink to this definition")
            :   A String specifying the repository key.

            coordSysType[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeNodes.coordSysType "Permalink to this definition")
            :   A SymbolicConstant specifying the type of coordinate system. Possible values are
                CARTESIAN, CYLINDRICAL, and SPHERICAL.

            origin[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeNodes.origin "Permalink to this definition")
            :   An OdbMeshNode object specifying a node at the origin of the datum coordinate system.

            point1[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeNodes.point1 "Permalink to this definition")
            :   An OdbMeshNode object specifying a node on the local 1- or rr-axis.

            point2[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeNodes.point2 "Permalink to this definition")
            :   An OdbMeshNode object specifying a node in the 1-2 or rr-θθ plane.

        Returns:[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeNodes-returns "Permalink to this headline")
        :   An OdbDatumCsys object.

        Return type:[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreeNodes-return-type "Permalink to this headline")
        :   `OdbDatumCsys`

    DatumCsysByThreePoints(*[name](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreePoints.name "abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreePoints.name (Python parameter) — A String specifying the repository key.")*, *[coordSysType](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreePoints.coordSysType "abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreePoints.coordSysType (Python parameter) — A SymbolicConstant specifying the type of coordinate system.")*, *[origin](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreePoints.origin "abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreePoints.origin (Python parameter) — A sequence of Floats specifying the coordinates of the origin of the datum coordinate system.")*, *[point1](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreePoints.point1 "abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreePoints.point1 (Python parameter) — A sequence of Floats specifying the coordinates of a point on the local 1- or rr-axis.")*, *[point2](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreePoints.point2 "abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreePoints.point2 (Python parameter) — A sequence of Floats specifying the coordinates of a point in the 1-2 or rr-θθ plane.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L23-L61)[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreePoints "Permalink to this definition")
    :   This method creates an OdbDatumCsys object using three points. A datum coordinate system created with
        this method results in a fixed system.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].rootAssembly.DatumCsysByThreePoints
        ```

        Note

        Check [DatumCsysByThreePoints on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsysbythreepointspyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreePoints-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreePoints.name "Permalink to this definition")
            :   A String specifying the repository key.

            coordSysType[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreePoints.coordSysType "Permalink to this definition")
            :   A SymbolicConstant specifying the type of coordinate system. Possible values are
                CARTESIAN, CYLINDRICAL, and SPHERICAL.

            origin[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreePoints.origin "Permalink to this definition")
            :   A sequence of Floats specifying the coordinates of the origin of the datum coordinate
                system.

            point1[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreePoints.point1 "Permalink to this definition")
            :   A sequence of Floats specifying the coordinates of a point on the local 1- or rr-axis.

            point2[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreePoints.point2 "Permalink to this definition")
            :   A sequence of Floats specifying the coordinates of a point in the 1-2 or rr-θθ plane.

        Returns:[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreePoints-returns "Permalink to this headline")
        :   An OdbDatumCsys object.

        Return type:[¶](#abaqus.Odb.OdbBase.OdbAssembly.DatumCsysByThreePoints-return-type "Permalink to this headline")
        :   `OdbDatumCsys`

    Instance(*[name](#abaqus.Odb.OdbBase.OdbAssembly.Instance.name "abaqus.Odb.OdbBase.OdbAssembly.Instance.name (Python parameter) — A String specifying the instance name.")*, *[object](#abaqus.Odb.OdbBase.OdbAssembly.Instance.object "abaqus.Odb.OdbBase.OdbAssembly.Instance.object (Python parameter) — An OdbPart object.")*, *[localCoordSystem](#abaqus.Odb.OdbBase.OdbAssembly.Instance.localCoordSystem "abaqus.Odb.OdbBase.OdbAssembly.Instance.localCoordSystem (Python parameter) — A sequence of sequences of three Floats specifying the rotation and translation of the part instance in the global Cartesian coordinate system.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L204-L238)[¶](#abaqus.Odb.OdbBase.OdbAssembly.Instance "Permalink to this definition")
    :   This method creates an OdbInstance object from an OdbPart object.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].rootAssembly.Instance
        ```

        Note

        Check [Instance on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-instancepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbBase.OdbAssembly.Instance-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.OdbBase.OdbAssembly.Instance.name "Permalink to this definition")
            :   A String specifying the instance name.

            object[¶](#abaqus.Odb.OdbBase.OdbAssembly.Instance.object "Permalink to this definition")
            :   An OdbPart object.

            localCoordSystem=`()`[¶](#abaqus.Odb.OdbBase.OdbAssembly.Instance.localCoordSystem "Permalink to this definition")
            :   A sequence of sequences of three Floats specifying the rotation and translation of the
                part instance in the global Cartesian coordinate system. The first three sequences
                specify the new local coordinate system with its center at the origin.The first sequence
                specifies a point on the 1-axis.The second sequence specifies a point on the 2-axis.The
                third sequence specifies a point on the 3-axis.The fourth sequence specifies the
                translation of the local coordinate system from the origin to its intended location.For
                example, the following sequence moves a part 10 units in the **X** direction with no
                rotation:localCoordSystem = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (10, 0, 0))`The following
                sequence moves a part 5 units in the \*\*X\*\* direction with rotation:
                `localCoordSystem = ((0, 1, 0), (1, 0, 0), (0, 0, 1), (5, 0, 0))`transforms a part
                containing the two points`Pt1= (1,0,0) Pt2= (2,0,0) to Pt1 = (0, 6, 0) Pt2 = (0, 7, 0)

        Returns:[¶](#abaqus.Odb.OdbBase.OdbAssembly.Instance-returns "Permalink to this headline")
        :   An OdbInstance object.

        Return type:[¶](#abaqus.Odb.OdbBase.OdbAssembly.Instance-return-type "Permalink to this headline")
        :   `OdbInstance`

    NodeSet(*[name](#abaqus.Odb.OdbBase.OdbAssembly.NodeSet.name "abaqus.Odb.OdbBase.OdbAssembly.NodeSet.name (Python parameter) — A String specifying the name of the set and the repository key.")*, *[nodes](#abaqus.Odb.OdbBase.OdbAssembly.NodeSet.nodes "abaqus.Odb.OdbBase.OdbAssembly.NodeSet.nodes (Python parameter) — A sequence of OdbMeshNode objects.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L301-L327)[¶](#abaqus.Odb.OdbBase.OdbAssembly.NodeSet "Permalink to this definition")
    :   This method creates a node set from an array of OdbMeshNode objects (for part instance-level sets) or
        from a sequence of arrays of OdbMeshNode objects (for assembly-level sets).

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].parts[name].NodeSet
        session.odbs[name].rootAssembly.instances[name].NodeSet
        session.odbs[name].rootAssembly.NodeSet
        ```

        Note

        Check [NodeSet on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-nodesetpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbBase.OdbAssembly.NodeSet-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.OdbBase.OdbAssembly.NodeSet.name "Permalink to this definition")
            :   A String specifying the name of the set and the repository key.

            nodes[¶](#abaqus.Odb.OdbBase.OdbAssembly.NodeSet.nodes "Permalink to this definition")
            :   A sequence of OdbMeshNode objects. For example, for a part:nodes=part1.nodes[1:5]`For
                an assembly:`nodes=(instance1.nodes[6:7], instance2.nodes[1:5])

        Returns:[¶](#abaqus.Odb.OdbBase.OdbAssembly.NodeSet-returns "Permalink to this headline")
        :   An OdbSet object.

        Return type:[¶](#abaqus.Odb.OdbBase.OdbAssembly.NodeSet-return-type "Permalink to this headline")
        :   `OdbSet`

    RigidBody(*[referenceNode](#abaqus.Odb.OdbBase.OdbAssembly.RigidBody.referenceNode "abaqus.Odb.OdbBase.OdbAssembly.RigidBody.referenceNode (Python parameter) — An OdbSet object specifying the reference node set associated with the rigid body.")*, *[position=abaqusConstants.INPUT](#abaqus.Odb.OdbBase.OdbAssembly.RigidBody "abaqus.Odb.OdbBase.OdbAssembly.RigidBody.position=abaqusConstants.INPUT (Python parameter)")*, *[isothermal=1](#abaqus.Odb.OdbBase.OdbAssembly.RigidBody "abaqus.Odb.OdbBase.OdbAssembly.RigidBody.isothermal=1 (Python parameter)")*, *[elements=<abaqus.Odb.OdbSet.OdbSet object>](#abaqus.Odb.OdbBase.OdbAssembly.RigidBody "abaqus.Odb.OdbBase.OdbAssembly.RigidBody.elements=<abaqus.Odb.OdbSet.OdbSet object> (Python parameter)")*, *[tieNodes=<abaqus.Odb.OdbSet.OdbSet object>](#abaqus.Odb.OdbBase.OdbAssembly.RigidBody "abaqus.Odb.OdbBase.OdbAssembly.RigidBody.tieNodes=<abaqus.Odb.OdbSet.OdbSet object> (Python parameter)")*, *[pinNodes=<abaqus.Odb.OdbSet.OdbSet object>](#abaqus.Odb.OdbBase.OdbAssembly.RigidBody "abaqus.Odb.OdbBase.OdbAssembly.RigidBody.pinNodes=<abaqus.Odb.OdbSet.OdbSet object> (Python parameter)")*, *[analyticSurface=None](#abaqus.Odb.OdbBase.OdbAssembly.RigidBody "abaqus.Odb.OdbBase.OdbAssembly.RigidBody.analyticSurface=None (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L240-L299)[¶](#abaqus.Odb.OdbBase.OdbAssembly.RigidBody "Permalink to this definition")
    :   This method creates a OdbRigidBody object.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].rootAssembly.instances[name].RigidBody
        session.odbs[name].rootAssembly.RigidBody
        ```

        Note

        Check [RigidBody on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rigidbodypyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbBase.OdbAssembly.RigidBody-parameters "Permalink to this headline")
        :   referenceNode[¶](#abaqus.Odb.OdbBase.OdbAssembly.RigidBody.referenceNode "Permalink to this definition")
            :   An OdbSet object specifying the reference node set associated with the rigid body.

            position : [`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")[`INPUT`, `CENTER_OF_MASS`], default: `INPUT`
            :   A SymbolicConstant specifying the specific location of the OdbRigidBody reference node
                relative to the rest of the rigid body. Possible values are INPUT and CENTER\_OF\_MASS.
                The default value is INPUT.

            isothermal : [`Union`](https://docs.python.org/3/library/typing.html#typing.Union "(in Python v3.13)")[[`AbaqusBoolean`](kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.AbaqusBoolean "abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean (Python class)"), [`bool`](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)")], default: `1`
            :   A Boolean specifying specify whether the OdbRigidBody can have temperature gradients or
                be isothermal. This is used only for fully coupled thermal-stress analysis The default
                value is ON.

            elements : [`OdbSet`](#abaqus.Odb.RebarOrientation.OdbSet "abaqus.Odb.OdbSet.OdbSet (Python class)"), default: `<abaqus.Odb.OdbSet.OdbSet object at 0x7f850cd94f10>`
            :   An OdbSet object specifying the element set whose motion is governed by the motion of
                rigid body reference node.

            tieNodes : [`OdbSet`](#abaqus.Odb.RebarOrientation.OdbSet "abaqus.Odb.OdbSet.OdbSet (Python class)"), default: `<abaqus.Odb.OdbSet.OdbSet object at 0x7f850c705450>`
            :   An OdbSet object specifying the node set which have both translational and rotational
                degrees of freedom associated with the rigid body.

            pinNodes : [`OdbSet`](#abaqus.Odb.RebarOrientation.OdbSet "abaqus.Odb.OdbSet.OdbSet (Python class)"), default: `<abaqus.Odb.OdbSet.OdbSet object at 0x7f850c7054d0>`
            :   An OdbSet object specifying the node set which have only translational degrees of
                freedom associated with the rigid body.

            analyticSurface : [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional "(in Python v3.13)")[[`AnalyticSurface`](#abaqus.Odb.OdbRigidBody.AnalyticSurface "abaqus.Odb.AnalyticSurface.AnalyticSurface (Python class)")], default: `None`
            :   An AnalyticSurface object specifying the analytic surface whose motion is governed by
                the motion of rigid body reference node.

        Returns:[¶](#abaqus.Odb.OdbBase.OdbAssembly.RigidBody-returns "Permalink to this headline")
        :   An OdbRigidBody object.

        Return type:[¶](#abaqus.Odb.OdbBase.OdbAssembly.RigidBody-return-type "Permalink to this headline")
        :   `OdbRigidBody`

*class* HistoryRegion(*[name](#abaqus.Odb.OdbStepBase.HistoryRegion "abaqus.Odb.OdbStepBase.HistoryRegion.__init__.name (Python parameter)")*, *[description](#abaqus.Odb.OdbStepBase.HistoryRegion "abaqus.Odb.OdbStepBase.HistoryRegion.__init__.description (Python parameter)")*, *[point](#abaqus.Odb.OdbStepBase.HistoryRegion "abaqus.Odb.OdbStepBase.HistoryRegion.__init__.point (Python parameter)")*, *[loadCase](#abaqus.Odb.OdbStepBase.HistoryRegion "abaqus.Odb.OdbStepBase.HistoryRegion.__init__.loadCase (Python parameter)")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L16-L176)[¶](#abaqus.Odb.OdbStepBase.HistoryRegion "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The HistoryRegion object contains history data for a single location in the model.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].steps[name].historyRegions[name]
    ```

    Note

    Check [HistoryRegion on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyregionpyc.htm?contextscope=all).

    Member Details:

    HistoryOutput(*[name](#abaqus.Odb.OdbStepBase.HistoryRegion.HistoryOutput.name "abaqus.Odb.OdbStepBase.HistoryRegion.HistoryOutput.name (Python parameter) — A String specifying the output variable name.")*, *[description](#abaqus.Odb.OdbStepBase.HistoryRegion.HistoryOutput.description "abaqus.Odb.OdbStepBase.HistoryRegion.HistoryOutput.description (Python parameter) — A String specifying the output variable.")*, *[type](#abaqus.Odb.OdbStepBase.HistoryRegion.HistoryOutput.type "abaqus.Odb.OdbStepBase.HistoryRegion.HistoryOutput.type (Python parameter) — A SymbolicConstant specifying the output type.")*, *[validInvariants](#abaqus.Odb.OdbStepBase.HistoryRegion.HistoryOutput.validInvariants "abaqus.Odb.OdbStepBase.HistoryRegion.HistoryOutput.validInvariants (Python parameter) — A sequence of SymbolicConstants specifying which invariants should be calculated for this field.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L140-L176)[¶](#abaqus.Odb.OdbStepBase.HistoryRegion.HistoryOutput "Permalink to this definition")
    :   This method creates a HistoryOutput object.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].steps[name].HistoryRegion
        ```

        Parameters:[¶](#abaqus.Odb.OdbStepBase.HistoryRegion.HistoryOutput-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.OdbStepBase.HistoryRegion.HistoryOutput.name "Permalink to this definition")
            :   A String specifying the output variable name.

            description[¶](#abaqus.Odb.OdbStepBase.HistoryRegion.HistoryOutput.description "Permalink to this definition")
            :   A String specifying the output variable.

            type[¶](#abaqus.Odb.OdbStepBase.HistoryRegion.HistoryOutput.type "Permalink to this definition")
            :   A SymbolicConstant specifying the output type. Only SCALAR is currently supported.

            validInvariants=`None`[¶](#abaqus.Odb.OdbStepBase.HistoryRegion.HistoryOutput.validInvariants "Permalink to this definition")
            :   A sequence of SymbolicConstants specifying which invariants should be calculated for
                this field. Possible values are MAGNITUDE, MISES, TRESCA, PRESS, INV3, MAX\_PRINCIPAL,
                MID\_PRINCIPAL, and MIN\_PRINCIPAL. The default value is an empty sequence.

        Returns:[¶](#abaqus.Odb.OdbStepBase.HistoryRegion.HistoryOutput-returns "Permalink to this headline")
        :   A HistoryOutput object.

        Return type:[¶](#abaqus.Odb.OdbStepBase.HistoryRegion.HistoryOutput-return-type "Permalink to this headline")
        :   [`HistoryOutput`](#abaqus.Odb.OdbStepBase.HistoryRegion.HistoryOutput "abaqus.Odb.OdbStepBase.HistoryRegion.HistoryOutput (Python method) — This method creates a HistoryOutput object.")

    description : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py)[¶](#abaqus.Odb.OdbStepBase.HistoryRegion.description "Permalink to this definition")
    :   A String specifying the description of the HistoryRegion object.

    getSubset(*[variableName](#abaqus.Odb.OdbStepBase.HistoryRegion.getSubset "abaqus.Odb.OdbStepBase.HistoryRegion.getSubset.variableName (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L136-L138)[¶](#abaqus.Odb.OdbStepBase.HistoryRegion.getSubset "Permalink to this definition")

    getSubset(*[start](#abaqus.Odb.OdbStepBase.HistoryRegion.getSubset "abaqus.Odb.OdbStepBase.HistoryRegion.getSubset.start (Python parameter)"): [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*)

    getSubset(*[start](#abaqus.Odb.OdbStepBase.HistoryRegion.getSubset "abaqus.Odb.OdbStepBase.HistoryRegion.getSubset.start (Python parameter)"): [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*, *[end](#abaqus.Odb.OdbStepBase.HistoryRegion.getSubset "abaqus.Odb.OdbStepBase.HistoryRegion.getSubset.end (Python parameter)"): [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*)

    getSubset(*\*[args](#abaqus.Odb.OdbStepBase.HistoryRegion.getSubset "abaqus.Odb.OdbStepBase.HistoryRegion.getSubset.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Odb.OdbStepBase.HistoryRegion.getSubset "abaqus.Odb.OdbStepBase.HistoryRegion.getSubset.kwargs (Python parameter)")*)

    historyOutputs : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Odb.HistoryOutput.HistoryOutput`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L31-L32)[¶](#abaqus.Odb.OdbStepBase.HistoryRegion.historyOutputs "Permalink to this definition")
    :   A repository of HistoryOutput objects.

    loadCase : --is-rst--:py:data:`~typing.Optional`\[:py:class:`str`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L43-L45)[¶](#abaqus.Odb.OdbStepBase.HistoryRegion.loadCase "Permalink to this definition")
    :   None or an OdbLoadCase object specifying the load case associated with the HistoryRegion
        object. The default value is None.

    name : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py)[¶](#abaqus.Odb.OdbStepBase.HistoryRegion.name "Permalink to this definition")
    :   A String specifying the name of the HistoryRegion object.

    point : --is-rst--:py:class:`~abaqus.Odb.HistoryPoint.HistoryPoint`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py)[¶](#abaqus.Odb.OdbStepBase.HistoryRegion.point "Permalink to this definition")
    :   A HistoryPoint object specifying the point to which the history data refer.

    position : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py)[¶](#abaqus.Odb.OdbStepBase.HistoryRegion.position "Permalink to this definition")
    :   A SymbolicConstant specifying the position of the history output. Possible values are
        NODAL, INTEGRATION\_POINT, WHOLE\_ELEMENT, WHOLE\_REGION, and WHOLE\_MODEL.

*class* JobData[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L8-L44)[¶](#abaqus.Odb.OdbBase.JobData "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The JobData object describes the context in which the analysis was run.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].jobData
    ```

    Note

    Check [JobData on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-jobdatapyc.htm?contextscope=all).

    Member Details:

    analysisCode : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py)[¶](#abaqus.Odb.OdbBase.JobData.analysisCode "Permalink to this definition")
    :   A SymbolicConstant specifying the analysis code. Possible values are ABAQUS\_STANDARD,
        ABAQUS\_EXPLICIT, and UNKNOWN\_ANALYSIS\_CODE.

    creationTime : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L33-L34)[¶](#abaqus.Odb.OdbBase.JobData.creationTime "Permalink to this definition")
    :   A String specifying the date and time at which the analysis was run.

    machineName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L39-L40)[¶](#abaqus.Odb.OdbBase.JobData.machineName "Permalink to this definition")
    :   A String specifying the name of the machine on which the analysis was run.

    modificationTime : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L36-L37)[¶](#abaqus.Odb.OdbBase.JobData.modificationTime "Permalink to this definition")
    :   A String specifying the date and time at which the database was last modified.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L19-L20)[¶](#abaqus.Odb.OdbBase.JobData.name "Permalink to this definition")
    :   A String specifying the name of the job.

    precision : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py)[¶](#abaqus.Odb.OdbBase.JobData.precision "Permalink to this definition")
    :   A SymbolicConstant specifying the precision. Only SINGLE\_PRECISION is currently
        supported. Possible values are DOUBLE\_PRECISION and SINGLE\_PRECISION.

    productAddOns : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L8-L44)[¶](#abaqus.Odb.OdbBase.JobData.productAddOns "Permalink to this definition")
    :   A String specifying an odb\_Sequence of productAddOns. Possible
        values are AQUA, DESIGN, BIORID, CEL, SOLITER, and CAVPARALLEL.

    version : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L30-L31)[¶](#abaqus.Odb.OdbBase.JobData.version "Permalink to this definition")
    :   A String specifying the release of the analysis code.

*class* OdbStep(*[name](#abaqus.Odb.OdbStep.OdbStep "abaqus.Odb.OdbStep.OdbStep.__init__.name (Python parameter)")*, *[description](#abaqus.Odb.OdbStep.OdbStep "abaqus.Odb.OdbStep.OdbStep.__init__.description (Python parameter)")*, *[domain](#abaqus.Odb.OdbStep.OdbStep "abaqus.Odb.OdbStep.OdbStep.__init__.domain (Python parameter)")*, *[timePeriod](#abaqus.Odb.OdbStep.OdbStep "abaqus.Odb.OdbStep.OdbStep.__init__.timePeriod (Python parameter)")=`0`*, *[previousStepName](#abaqus.Odb.OdbStep.OdbStep "abaqus.Odb.OdbStep.OdbStep.__init__.previousStepName (Python parameter)")=`''`*, *[procedure](#abaqus.Odb.OdbStep.OdbStep "abaqus.Odb.OdbStep.OdbStep.__init__.procedure (Python parameter)")=`''`*, *[totalTime](#abaqus.Odb.OdbStep.OdbStep "abaqus.Odb.OdbStep.OdbStep.__init__.totalTime (Python parameter)")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStep.py#L14-L163)[¶](#abaqus.Odb.OdbStep.OdbStep "Permalink to this definition")
:   Bases: [`OdbStepBase`](#abaqus.Odb.OdbStepBase.OdbStepBase "abaqus.Odb.OdbStepBase.OdbStepBase (Python class) — Bases: object")

    Member Details:

    Frame(*[incrementNumber](#abaqus.Odb.OdbStep.OdbStep.Frame "abaqus.Odb.OdbStep.OdbStep.Frame.incrementNumber (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[frameValue](#abaqus.Odb.OdbStep.OdbStep.Frame "abaqus.Odb.OdbStep.OdbStep.Frame.frameValue (Python parameter)"): [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*, *[description](#abaqus.Odb.OdbStep.OdbStep.Frame "abaqus.Odb.OdbStep.OdbStep.Frame.description (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = `''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStep.py#L138-L142)[¶](#abaqus.Odb.OdbStep.OdbStep.Frame "Permalink to this definition")

    Frame(*[mode](#abaqus.Odb.OdbStep.OdbStep.Frame "abaqus.Odb.OdbStep.OdbStep.Frame.mode (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[frequency](#abaqus.Odb.OdbStep.OdbStep.Frame "abaqus.Odb.OdbStep.OdbStep.Frame.frequency (Python parameter)"): [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*, *[description](#abaqus.Odb.OdbStep.OdbStep.Frame "abaqus.Odb.OdbStep.OdbStep.Frame.description (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = `''`*)

    Frame(*[loadCase](#abaqus.Odb.OdbStep.OdbStep.Frame "abaqus.Odb.OdbStep.OdbStep.Frame.loadCase (Python parameter)"): [OdbLoadCase](#abaqus.Odb.OdbStepBase.OdbLoadCase "abaqus.Odb.OdbLoadCase.OdbLoadCase (Python class)")*, *[description](#abaqus.Odb.OdbStep.OdbStep.Frame "abaqus.Odb.OdbStep.OdbStep.Frame.description (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = `''`*, *[frequency](#abaqus.Odb.OdbStep.OdbStep.Frame "abaqus.Odb.OdbStep.OdbStep.Frame.frequency (Python parameter)"): [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") = `0`*)

    Frame(*\*[args](#abaqus.Odb.OdbStep.OdbStep.Frame "abaqus.Odb.OdbStep.OdbStep.Frame.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Odb.OdbStep.OdbStep.Frame "abaqus.Odb.OdbStep.OdbStep.Frame.kwargs (Python parameter)")*)

    HistoryRegion(*[name](#abaqus.Odb.OdbStep.OdbStep.HistoryRegion.name "abaqus.Odb.OdbStep.OdbStep.HistoryRegion.name (Python parameter) — A String specifying the name of the HistoryRegion object.")*, *[description](#abaqus.Odb.OdbStep.OdbStep.HistoryRegion.description "abaqus.Odb.OdbStep.OdbStep.HistoryRegion.description (Python parameter) — A String specifying the description of the HistoryRegion object.")*, *[point](#abaqus.Odb.OdbStep.OdbStep.HistoryRegion.point "abaqus.Odb.OdbStep.OdbStep.HistoryRegion.point (Python parameter) — A HistoryPoint object specifying the point to which the history data refer.")*, *[loadCase](#abaqus.Odb.OdbStep.OdbStep.HistoryRegion.loadCase "abaqus.Odb.OdbStep.OdbStep.HistoryRegion.loadCase (Python parameter) — None or an OdbLoadCase object specifying the load case associated with the HistoryRegion object.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStep.py#L16-L49)[¶](#abaqus.Odb.OdbStep.OdbStep.HistoryRegion "Permalink to this definition")
    :   This method creates a HistoryRegion object.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].steps[name].HistoryRegion
        ```

        Note

        Check [HistoryRegion on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-historyregionpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbStep.OdbStep.HistoryRegion-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.OdbStep.OdbStep.HistoryRegion.name "Permalink to this definition")
            :   A String specifying the name of the HistoryRegion object.

            description[¶](#abaqus.Odb.OdbStep.OdbStep.HistoryRegion.description "Permalink to this definition")
            :   A String specifying the description of the HistoryRegion object.

            point[¶](#abaqus.Odb.OdbStep.OdbStep.HistoryRegion.point "Permalink to this definition")
            :   A HistoryPoint object specifying the point to which the history data refer.

            loadCase=`None`[¶](#abaqus.Odb.OdbStep.OdbStep.HistoryRegion.loadCase "Permalink to this definition")
            :   None or an OdbLoadCase object specifying the load case associated with the HistoryRegion
                object. The default value is None.

        Returns:[¶](#abaqus.Odb.OdbStep.OdbStep.HistoryRegion-returns "Permalink to this headline")
        :   A HistoryRegion object.

        Return type:[¶](#abaqus.Odb.OdbStep.OdbStep.HistoryRegion-return-type "Permalink to this headline")
        :   [`HistoryRegion`](#abaqus.Odb.OdbStep.OdbStep.HistoryRegion "abaqus.Odb.OdbStep.OdbStep.HistoryRegion (Python method) — This method creates a HistoryRegion object.")

    LoadCase(*[name](#abaqus.Odb.OdbStep.OdbStep.LoadCase.name "abaqus.Odb.OdbStep.OdbStep.LoadCase.name (Python parameter) — A String specifying the name of the OdbLoadCase object.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStep.py#L144-L163)[¶](#abaqus.Odb.OdbStep.OdbStep.LoadCase "Permalink to this definition")
    :   This method creates an OdbLoadCase object.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].steps[name].LoadCase
        ```

        Parameters:[¶](#abaqus.Odb.OdbStep.OdbStep.LoadCase-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.OdbStep.OdbStep.LoadCase.name "Permalink to this definition")
            :   A String specifying the name of the OdbLoadCase object.

        Returns:[¶](#abaqus.Odb.OdbStep.OdbStep.LoadCase-returns "Permalink to this headline")
        :   An OdbLoadCase object.

        Return type:[¶](#abaqus.Odb.OdbStep.OdbStep.LoadCase-return-type "Permalink to this headline")
        :   `OdbLoadCase`

*class* SectionCategory(*[name](#abaqus.Odb.SectionCategory.SectionCategory "abaqus.Odb.SectionCategory.SectionCategory.__init__.name (Python parameter)")*, *[description](#abaqus.Odb.SectionCategory.SectionCategory "abaqus.Odb.SectionCategory.SectionCategory.__init__.description (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/SectionCategory.py#L9-L95)[¶](#abaqus.Odb.SectionCategory.SectionCategory "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The SectionCategory object is used to group regions of the model with like sections. Section definitions
    that contain the same number of section points or integration points are grouped together. To access data
    for a particular section definition, use the individual Section objects in the output database. For more
    information, see Beam Section profile commands and Section commands.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].parts[name].elements[i].sectionCategory
    session.odbs[name].parts[name].elementSets[name].elements[i].sectionCategory
    session.odbs[name].parts[name].nodeSets[name].elements[i].sectionCategory
    session.odbs[name].parts[name].surfaces[name].elements[i].sectionCategory
    session.odbs[name].rootAssembly.elements[i].sectionCategory
    session.odbs[name].rootAssembly.elementSets[name].elements[i].sectionCategory
    session.odbs[name].rootAssembly.instances[name].elements[i].sectionCategory
    session.odbs[name].rootAssembly.instances[name].elementSets[name].elements[i].sectionCategory
    session.odbs[name].rootAssembly.instances[name].nodeSets[name].elements[i].sectionCategory
    session.odbs[name].rootAssembly.instances[name].surfaces[name].elements[i].sectionCategory
    session.odbs[name].rootAssembly.nodeSets[name].elements[i].sectionCategory
    session.odbs[name].rootAssembly.surfaces[name].elements[i].sectionCategory
    session.odbs[name].sectionCategories[name]
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.elements[i].sectionCategory
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.elementSets[name].elements[i].sectionCategory
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.nodeSets[name].elements[i].sectionCategory
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.surfaces[name].elements[i].sectionCategory
    ```

    Note

    Check [SectionCategory on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectioncategorypyc.htm?contextscope=all).

    Member Details:

    SectionPoint(*[number](#abaqus.Odb.SectionCategory.SectionCategory.SectionPoint.number "abaqus.Odb.SectionCategory.SectionCategory.SectionPoint.number (Python parameter) — An Int specifying the number of the section point.")*, *[description](#abaqus.Odb.SectionCategory.SectionCategory.SectionPoint.description "abaqus.Odb.SectionCategory.SectionCategory.SectionPoint.description (Python parameter) — A String specifying the description of the section point.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/SectionCategory.py#L71-L95)[¶](#abaqus.Odb.SectionCategory.SectionCategory.SectionPoint "Permalink to this definition")
    :   This method creates a SectionPoint object.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].SectionCategory
        ```

        Note

        Check [SectionPoint on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionpointpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.SectionCategory.SectionCategory.SectionPoint-parameters "Permalink to this headline")
        :   number[¶](#abaqus.Odb.SectionCategory.SectionCategory.SectionPoint.number "Permalink to this definition")
            :   An Int specifying the number of the section point. See Beam elements and Shell elements
                for the numbering convention.

            description[¶](#abaqus.Odb.SectionCategory.SectionCategory.SectionPoint.description "Permalink to this definition")
            :   A String specifying the description of the section point.

        Returns:[¶](#abaqus.Odb.SectionCategory.SectionCategory.SectionPoint-returns "Permalink to this headline")
        :   A SectionPoint object.

        Return type:[¶](#abaqus.Odb.SectionCategory.SectionCategory.SectionPoint-return-type "Permalink to this headline")
        :   [`SectionPoint`](#abaqus.Odb.SectionCategory.SectionCategory.SectionPoint "abaqus.Odb.SectionCategory.SectionCategory.SectionPoint (Python method) — This method creates a SectionPoint object.")

    description : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/SectionCategory.py)[¶](#abaqus.Odb.SectionCategory.SectionCategory.description "Permalink to this definition")
    :   A String specifying the description of the category.

    name : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/SectionCategory.py)[¶](#abaqus.Odb.SectionCategory.SectionCategory.name "Permalink to this definition")
    :   A String specifying the name of the category.

    sectionPoints : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Odb.SectionPoint.SectionPoint`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/SectionCategory.py#L39-L40)[¶](#abaqus.Odb.SectionCategory.SectionCategory.sectionPoints "Permalink to this definition")
    :   A SectionPointArray object.

*class* OdbAssemblyBase[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbAssemblyBase.py#L22-L237)[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The OdbAssembly object has no constructor; it is created automatically when an Odb object is created.
    Abaqus creates the **rootAssembly** member when an Odb object is created.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].rootAssembly
    ```

    Note

    Check [OdbAssemblyBase on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all).

    Member Details:

    ConnectorOrientation(*[region](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation.region "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation.region (Python parameter) — An OdbSet specifying a region.")*, *[localCsys1](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation.localCsys1 "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation.localCsys1 (Python parameter) — An OdbDatumCsys object specifying the first connector node local coordinate system or None, indicating the global coordinate system.")=`None`*, *[axis1](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation.axis1 "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation.axis1 (Python parameter) — A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate system about which an additional rotation of the first connector node is applied. Possible values are AXIS_1, AXIS_2, and AXIS_3.")=`abaqusConstants.AXIS_1`*, *[angle1](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation.angle1 "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation.angle1 (Python parameter) — A Float specifying the angle of the additional rotation about the first connector node axis.")=`0`*, *[orient2sameAs1](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation.orient2sameAs1 "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation.orient2sameAs1 (Python parameter) — A Boolean specifying whether the same orientation settings should be used for the second node of the connector.")=`0`*, *[localCsys2](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation.localCsys2 "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation.localCsys2 (Python parameter) — An OdbDatumCsys object specifying the second connector node local coordinate system or None, indicating the global coordinate system.")=`None`*, *[axis2](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation.axis2 "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation.axis2 (Python parameter) — A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate system about which an additional rotation of the second connector node is applied. Possible values are AXIS_1, AXIS_2, and AXIS_3.")=`abaqusConstants.AXIS_1`*, *[angle2](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation.angle2 "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation.angle2 (Python parameter) — A Float specifying the angle of the additional rotation about the second connector node axis.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbAssemblyBase.py#L67-L114)[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation "Permalink to this definition")
    :   This method assigns a connector orientation to a connector region.

        Note

        Check [ConnectorOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-connectororientationpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation.region "Permalink to this definition")
            :   An OdbSet specifying a region.

            localCsys1=`None`[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation.localCsys1 "Permalink to this definition")
            :   An OdbDatumCsys object specifying the first connector node local coordinate system or
                None, indicating the global coordinate system.

            axis1=`abaqusConstants.AXIS_1`[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation.axis1 "Permalink to this definition")
            :   A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate
                system about which an additional rotation of the first connector node is applied.
                Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default value is AXIS\_1.

            angle1=`0`[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation.angle1 "Permalink to this definition")
            :   A Float specifying the angle of the additional rotation about the first connector node
                axis. The default value is 0.0.

            orient2sameAs1=`0`[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation.orient2sameAs1 "Permalink to this definition")
            :   A Boolean specifying whether the same orientation settings should be used for the second
                node of the connector. The default value is OFF.

            localCsys2=`None`[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation.localCsys2 "Permalink to this definition")
            :   An OdbDatumCsys object specifying the second connector node local coordinate system or
                None, indicating the global coordinate system.

            axis2=`abaqusConstants.AXIS_1`[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation.axis2 "Permalink to this definition")
            :   A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate
                system about which an additional rotation of the second connector node is applied.
                Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default value is AXIS\_1.

            angle2=`0`[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation.angle2 "Permalink to this definition")
            :   A Float specifying the angle of the additional rotation about the second connector node
                axis. The default value is 0.0.

        Raises:[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.ConnectorOrientation-raises "Permalink to this headline")
        :   **OdbError** – Connector orientation assignment requires element set, If **region** is not an element set.

    RigidBody(*[referenceNode](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.RigidBody.referenceNode "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.RigidBody.referenceNode (Python parameter) — An OdbSet specifying the reference node assigned to the rigid body.")*, *[position](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.RigidBody.position "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.RigidBody.position (Python parameter) — A symbolic constant specify if the location of the reference node is to be defined by the user.")=`abaqusConstants.INPUT`*, *[isothermal](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.RigidBody.isothermal "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.RigidBody.isothermal (Python parameter) — A Boolean specifying an isothermal rigid body.")=`0`*, *[elset](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.RigidBody.elset "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.RigidBody.elset (Python parameter) — An OdbSet specifying an element set assigned to the rigid body.")=`''`*, *[pinNodes](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.RigidBody.pinNodes "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.RigidBody.pinNodes (Python parameter) — An OdbSet specifying pin-type nodes assigned to the rigid body.")=`''`*, *[tieNodes](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.RigidBody.tieNodes "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.RigidBody.tieNodes (Python parameter) — An OdbSet specifying tie-type nodes assigned to the rigid body.")=`''`*, *[analyticSurface](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.RigidBody.analyticSurface "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.RigidBody.analyticSurface (Python parameter) — An AnalyticSurface specifying the Analytic Rigid Surface assigned to the rigid body.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbAssemblyBase.py#L200-L237)[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.RigidBody "Permalink to this definition")
    :   This method defines an OdbRigidBody on the assembly.

        Note

        Check [RigidBody on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rigidbodypyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.RigidBody-parameters "Permalink to this headline")
        :   referenceNode[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.RigidBody.referenceNode "Permalink to this definition")
            :   An OdbSet specifying the reference node assigned to the rigid body.

            position=`abaqusConstants.INPUT`[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.RigidBody.position "Permalink to this definition")
            :   A symbolic constant specify if the location of the reference node is to be defined by
                the user. Possible values are INPUT and CENTER\_OF\_MASS. The default value is INPUT.

            isothermal=`0`[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.RigidBody.isothermal "Permalink to this definition")
            :   A Boolean specifying an isothermal rigid body. The default value is OFF. This parameter
                is used only for a fully coupled thermal stress analysis.

            elset=`''`[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.RigidBody.elset "Permalink to this definition")
            :   An OdbSet specifying an element set assigned to the rigid body.

            pinNodes=`''`[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.RigidBody.pinNodes "Permalink to this definition")
            :   An OdbSet specifying pin-type nodes assigned to the rigid body.

            tieNodes=`''`[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.RigidBody.tieNodes "Permalink to this definition")
            :   An OdbSet specifying tie-type nodes assigned to the rigid body.

            analyticSurface=`''`[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.RigidBody.analyticSurface "Permalink to this definition")
            :   An AnalyticSurface specifying the Analytic Rigid Surface assigned to the rigid body.

        Raises:[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.RigidBody-raises "Permalink to this headline")
        :   **OdbError** – Rigid body definition requires a node set, If **referenceNode** is not a node set

    SectionAssignment(*[region](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.SectionAssignment.region "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.SectionAssignment.region (Python parameter) — An OdbSet specifying a region.")*, *[section](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.SectionAssignment.section "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.SectionAssignment.section (Python parameter) — A Section object.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbAssemblyBase.py#L116-L133)[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.SectionAssignment "Permalink to this definition")
    :   This method is used to assign a section on an assembly or part. Section assignment on the assembly is
        limited to the connector elements only.

        Note

        Check [SectionAssignment on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionassignmentpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.SectionAssignment-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.SectionAssignment.region "Permalink to this definition")
            :   An OdbSet specifying a region.

            section[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.SectionAssignment.section "Permalink to this definition")
            :   A Section object.

        Raises:[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.SectionAssignment-raises "Permalink to this headline")
        :   **OdbError** – Section assignment requires element set, If **region** is not an element set.

    addElements(*[labels](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addElements.labels "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addElements.labels (Python parameter) — A sequence of Ints specifying the element labels.")*, *[connectivity](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addElements.connectivity "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addElements.connectivity (Python parameter) — A sequence of sequences of Ints specifying the nodal connectivity.")*, *[instanceNames](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addElements.instanceNames "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addElements.instanceNames (Python parameter) — A sequence of Strings specifying the instanceNames of each node in the nodal connectivity array.")*, *[type](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addElements.type "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addElements.type (Python parameter) — A String specifying the element type.")*, *[elementSetName](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addElements.elementSetName "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addElements.elementSetName (Python parameter) — A String specifying a name for this element set.")=`''`*, *[sectionCategory](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addElements.sectionCategory "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addElements.sectionCategory (Python parameter) — A SectionCategory object for this element set.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbAssemblyBase.py#L135-L175)[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addElements "Permalink to this definition")
    :   This method is used to define elements using nodes defined at the OdbAssembly and/or OdbInstance
        level. For connector elements connected to ground, specify the lone node in the connectivity. The
        position of the ground node cannot be specified. This is a limitation. Warning:Adding elements not in
        ascending order of their labels may cause Abaqus/Viewer to plot contours incorrectly.

        Note

        Check [OdbAssemblyBase.addElements on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblyaddelementspyc).

        Parameters:[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addElements-parameters "Permalink to this headline")
        :   labels[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addElements.labels "Permalink to this definition")
            :   A sequence of Ints specifying the element labels.

            connectivity[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addElements.connectivity "Permalink to this definition")
            :   A sequence of sequences of Ints specifying the nodal connectivity.

            instanceNames[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addElements.instanceNames "Permalink to this definition")
            :   A sequence of Strings specifying the instanceNames of each node in the nodal
                connectivity array. If the node is defined at the assembly level, the instance name
                should be an empty string

            type[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addElements.type "Permalink to this definition")
            :   A String specifying the element type.

            elementSetName=`''`[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addElements.elementSetName "Permalink to this definition")
            :   A String specifying a name for this element set. The default value is the empty string.

            sectionCategory=`None`[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addElements.sectionCategory "Permalink to this definition")
            :   A SectionCategory object for this element set.

        Raises:[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addElements-raises "Permalink to this headline")
        :   * **OdbError** – Addition of this element type is not permitted at the assembly level, Only certain element types are permitted at the assembly level. e.g., connector
              elements.
            * **OdbError** – Connectivity array must be provided for all element, If length of label array does not match connectivity data length.

    addNodes(*[labels](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addNodes.labels "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addNodes.labels (Python parameter) — A sequence of Ints specifying the node labels.")*, *[coordinates](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addNodes.coordinates "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addNodes.coordinates (Python parameter) — A sequence of sequences of Floats specifying the nodal coordinates.")*, *[nodeSetName](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addNodes.nodeSetName "abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addNodes.nodeSetName (Python parameter) — A String specifying a name for this node set.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbAssemblyBase.py#L177-L198)[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addNodes "Permalink to this definition")
    :   This method adds nodes to the OdbAssembly object using node labels and coordinates. Warning:Adding
        nodes not in ascending order of their labels may cause Abaqus/Viewer to plot contours incorrectly.

        Note

        Check [OdbAssemblyBase.addNodes on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all#simaker-assemblyaddnodespyc).

        Parameters:[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addNodes-parameters "Permalink to this headline")
        :   labels[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addNodes.labels "Permalink to this definition")
            :   A sequence of Ints specifying the node labels.

            coordinates[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addNodes.coordinates "Permalink to this definition")
            :   A sequence of sequences of Floats specifying the nodal coordinates.

            nodeSetName=`None`[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addNodes.nodeSetName "Permalink to this definition")
            :   A String specifying a name for this node set. The default value is None.

        Raises:[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.addNodes-raises "Permalink to this headline")
        :   * **OdbError** – Number of node labels and coordinates does not match, If length of labels does not match length of coordinates.
            * **OdbError** – Node location specification does not correspond to part dimensions, If width of coordinate array does not match assembly dimension.

    connectorOrientations : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Assembly.ConnectorOrientation.ConnectorOrientation`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbAssemblyBase.py#L64-L65)[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.connectorOrientations "Permalink to this definition")
    :   A ConnectorOrientationArray object.

    datumCsyses : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Odb.OdbDatumCsys.OdbDatumCsys`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbAssemblyBase.py#L52-L53)[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.datumCsyses "Permalink to this definition")
    :   A repository of OdbDatumCsys objects.

    elementSets : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Odb.OdbSet.OdbSet`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbAssemblyBase.py#L40-L41)[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.elementSets "Permalink to this definition")
    :   A repository of OdbSet objects specifying element sets.

    elements : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Odb.OdbMeshElement.OdbMeshElement`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbAssemblyBase.py#L49-L50)[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.elements "Permalink to this definition")
    :   An OdbMeshElementArray object.

    instances : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Odb.OdbInstance.OdbInstance`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbAssemblyBase.py#L34-L35)[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.instances "Permalink to this definition")
    :   A repository of OdbInstance objects.

    nodeSets : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Odb.OdbSet.OdbSet`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbAssemblyBase.py#L37-L38)[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.nodeSets "Permalink to this definition")
    :   A repository of OdbSet objects specifying node sets.

    nodes : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Odb.OdbMeshNode.OdbMeshNode`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbAssemblyBase.py#L46-L47)[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.nodes "Permalink to this definition")
    :   An OdbMeshNodeArray object.

    pretensionSections : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Odb.OdbPretensionSection.OdbPretensionSection`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbAssemblyBase.py#L61-L62)[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.pretensionSections "Permalink to this definition")
    :   An OdbPretensionSectionArray object.

    rigidBodies : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Odb.OdbRigidBody.OdbRigidBody`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbAssemblyBase.py#L58-L59)[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.rigidBodies "Permalink to this definition")
    :   An OdbRigidBodyArray object.

    sectionAssignments : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Property.SectionAssignment.SectionAssignment`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbAssemblyBase.py#L55-L56)[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.sectionAssignments "Permalink to this definition")
    :   A SectionAssignmentArray object.

    surfaces : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Odb.OdbSet.OdbSet`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbAssemblyBase.py#L43-L44)[¶](#abaqus.Odb.OdbAssemblyBase.OdbAssemblyBase.surfaces "Permalink to this definition")
    :   A repository of OdbSet objects specifying surfaces.

*class* OdbDatumCsys[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L12-L260)[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The OdbDatumCsys object contains a coordinate system that can be stored in an output database. You can
    create the datum coordinate system in the Visualization module during an Abaqus/CAE session and save the
    datum coordinate system to the output database before you exit Abaqus/CAE. Alternatively, the analysis code
    can write the datum coordinate system to the output database.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].rootAssembly.datumCsyses[name]
    ```

    Note

    Check [OdbDatumCsys on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdatumcsyspyc.htm?contextscope=all).

    Member Details:

    DatumCsys(*[name](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsys.name "abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsys.name (Python parameter) — A String specifying the repository key.")*, *[datumCsys](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsys.datumCsys "abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsys.datumCsys (Python parameter) — An OdbDatumCsys object specifying the object to be copied.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L199-L220)[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsys "Permalink to this definition")
    :   This method copies oneOdbDatumCsys object to a new OdbDatumCsys object.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].rootAssembly.DatumCsysByThreePoints
        ```

        Note

        Check [DatumCsys on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsyspyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsys-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsys.name "Permalink to this definition")
            :   A String specifying the repository key.

            datumCsys[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsys.datumCsys "Permalink to this definition")
            :   An OdbDatumCsys object specifying the object to be copied.

        Returns:[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsys-returns "Permalink to this headline")
        :   An OdbDatumCsys object.

        Return type:[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsys-return-type "Permalink to this headline")
        :   [`OdbDatumCsys`](#abaqus.Odb.RebarOrientation.OdbDatumCsys "abaqus.Odb.RebarOrientation.OdbDatumCsys (Python class) — Bases: object")

    DatumCsysBy6dofNode(*[name](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysBy6dofNode.name "abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysBy6dofNode.name (Python parameter) — A String specifying the repository key.")*, *[coordSysType](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysBy6dofNode.coordSysType "abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysBy6dofNode.coordSysType (Python parameter) — A SymbolicConstant specifying the type of coordinate system.")*, *[origin](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysBy6dofNode.origin "abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysBy6dofNode.origin (Python parameter) — An OdbMeshNode object specifying the origin of the datum coordinate system.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L167-L197)[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysBy6dofNode "Permalink to this definition")
    :   A datum coordinate system created with this method results in a system that follows the position of a
        node. The node location defines the origin of the datum coordinate system. The rotational displacement
        (UR1, UR2, UR3) of the node defines the orientation of the coordinate system axes. Results, such as
        those for displacement, are resolved into the orientation of the datum coordinate system without regard
        to the position of its origin. The last argument is given in the form of an OdbMeshNode object.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].rootAssembly.DatumCsysByThreePoints
        ```

        Note

        Check [DatumCsysBy6dofNode on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsysby6dofnodepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysBy6dofNode-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysBy6dofNode.name "Permalink to this definition")
            :   A String specifying the repository key.

            coordSysType[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysBy6dofNode.coordSysType "Permalink to this definition")
            :   A SymbolicConstant specifying the type of coordinate system. Possible values are
                CARTESIAN, CYLINDRICAL, and SPHERICAL.

            origin[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysBy6dofNode.origin "Permalink to this definition")
            :   An OdbMeshNode object specifying the origin of the datum coordinate system.

        Returns:[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysBy6dofNode-returns "Permalink to this headline")
        :   An OdbDatumCsys object.

        Return type:[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysBy6dofNode-return-type "Permalink to this headline")
        :   [`OdbDatumCsys`](#abaqus.Odb.RebarOrientation.OdbDatumCsys "abaqus.Odb.RebarOrientation.OdbDatumCsys (Python class) — Bases: object")

    DatumCsysByThreeCircNodes(*[name](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeCircNodes.name "abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeCircNodes.name (Python parameter) — A String specifying the repository key.")*, *[coordSysType](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeCircNodes.coordSysType "abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeCircNodes.coordSysType (Python parameter) — A SymbolicConstant specifying the type of coordinate system.")*, *[node1Arc](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeCircNodes.node1Arc "abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeCircNodes.node1Arc (Python parameter) — An OdbMeshNode object that lies on the circular arc.")*, *[node2Arc](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeCircNodes.node2Arc "abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeCircNodes.node2Arc (Python parameter) — An OdbMeshNode object that lies on the circular arc.")*, *[node3Arc](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeCircNodes.node3Arc "abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeCircNodes.node3Arc (Python parameter) — An OdbMeshNode object that lies on the circular arc.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L126-L165)[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeCircNodes "Permalink to this definition")
    :   This method is convenient to use where there are no nodes along the axis of a hollow cylinder or at
        the center of a hollow sphere. The three nodes that you provide as arguments determine a circle in
        space. The center of the circle is the origin of the datum coordinate system. The normal to the circle
        is parallel to the zz-axis of a cylindrical coordinate system or to the ϕϕ-axis of a spherical
        coordinate system. The line from the origin to the first node defines the rr-axis.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].rootAssembly.DatumCsysByThreePoints
        ```

        Note

        Check [DatumCsysByThreeCircNodes on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsysbythreecircnodespyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeCircNodes-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeCircNodes.name "Permalink to this definition")
            :   A String specifying the repository key.

            coordSysType[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeCircNodes.coordSysType "Permalink to this definition")
            :   A SymbolicConstant specifying the type of coordinate system. Possible values are
                CARTESIAN, CYLINDRICAL, and SPHERICAL.

            node1Arc[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeCircNodes.node1Arc "Permalink to this definition")
            :   An OdbMeshNode object that lies on the circular arc.

            node2Arc[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeCircNodes.node2Arc "Permalink to this definition")
            :   An OdbMeshNode object that lies on the circular arc.

            node3Arc[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeCircNodes.node3Arc "Permalink to this definition")
            :   An OdbMeshNode object that lies on the circular arc.

        Returns:[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeCircNodes-returns "Permalink to this headline")
        :   An OdbDatumCsys object.

        Return type:[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeCircNodes-return-type "Permalink to this headline")
        :   [`OdbDatumCsys`](#abaqus.Odb.RebarOrientation.OdbDatumCsys "abaqus.Odb.RebarOrientation.OdbDatumCsys (Python class) — Bases: object")

    DatumCsysByThreeNodes(*[name](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeNodes.name "abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeNodes.name (Python parameter) — A String specifying the repository key.")*, *[coordSysType](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeNodes.coordSysType "abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeNodes.coordSysType (Python parameter) — A SymbolicConstant specifying the type of coordinate system.")*, *[origin](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeNodes.origin "abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeNodes.origin (Python parameter) — An OdbMeshNode object specifying a node at the origin of the datum coordinate system.")*, *[point1](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeNodes.point1 "abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeNodes.point1 (Python parameter) — An OdbMeshNode object specifying a node on the local 1- or rr-axis.")*, *[point2](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeNodes.point2 "abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeNodes.point2 (Python parameter) — An OdbMeshNode object specifying a node in the 1-2 or rr-θθ plane.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L85-L124)[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeNodes "Permalink to this definition")
    :   This method creates an OdbDatumCsys object using the coordinates of three OdbMeshNode objects. A
        datum coordinate system created with this method results in a system that follows the position of the
        three nodes. Results, such as those for displacement, are resolved into the orientation of the datum
        coordinate system without regard to the position of its origin. The last three arguments are given in
        the form of an OdbMeshNode object.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].rootAssembly.DatumCsysByThreePoints
        ```

        Note

        Check [DatumCsysByThreeNodes on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsysbythreenodespyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeNodes-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeNodes.name "Permalink to this definition")
            :   A String specifying the repository key.

            coordSysType[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeNodes.coordSysType "Permalink to this definition")
            :   A SymbolicConstant specifying the type of coordinate system. Possible values are
                CARTESIAN, CYLINDRICAL, and SPHERICAL.

            origin[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeNodes.origin "Permalink to this definition")
            :   An OdbMeshNode object specifying a node at the origin of the datum coordinate system.

            point1[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeNodes.point1 "Permalink to this definition")
            :   An OdbMeshNode object specifying a node on the local 1- or rr-axis.

            point2[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeNodes.point2 "Permalink to this definition")
            :   An OdbMeshNode object specifying a node in the 1-2 or rr-θθ plane.

        Returns:[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeNodes-returns "Permalink to this headline")
        :   An OdbDatumCsys object.

        Return type:[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreeNodes-return-type "Permalink to this headline")
        :   [`OdbDatumCsys`](#abaqus.Odb.RebarOrientation.OdbDatumCsys "abaqus.Odb.RebarOrientation.OdbDatumCsys (Python class) — Bases: object")

    DatumCsysByThreePoints(*[name](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreePoints.name "abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreePoints.name (Python parameter) — A String specifying the repository key.")*, *[coordSysType](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreePoints.coordSysType "abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreePoints.coordSysType (Python parameter) — A SymbolicConstant specifying the type of coordinate system.")*, *[origin](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreePoints.origin "abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreePoints.origin (Python parameter) — A sequence of Floats specifying the coordinates of the origin of the datum coordinate system.")*, *[point1](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreePoints.point1 "abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreePoints.point1 (Python parameter) — A sequence of Floats specifying the coordinates of a point on the local 1- or rr-axis.")*, *[point2](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreePoints.point2 "abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreePoints.point2 (Python parameter) — A sequence of Floats specifying the coordinates of a point in the 1-2 or rr-θθ plane.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L46-L83)[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreePoints "Permalink to this definition")
    :   This method creates an OdbDatumCsys object using three points. A datum coordinate system created with
        this method results in a fixed system.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].rootAssembly.DatumCsysByThreePoints
        ```

        Note

        Check [DatumCsysByThreePoints on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-datumcsysbythreepointspyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreePoints-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreePoints.name "Permalink to this definition")
            :   A String specifying the repository key.

            coordSysType[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreePoints.coordSysType "Permalink to this definition")
            :   A SymbolicConstant specifying the type of coordinate system. Possible values are
                CARTESIAN, CYLINDRICAL, and SPHERICAL.

            origin[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreePoints.origin "Permalink to this definition")
            :   A sequence of Floats specifying the coordinates of the origin of the datum coordinate
                system.

            point1[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreePoints.point1 "Permalink to this definition")
            :   A sequence of Floats specifying the coordinates of a point on the local 1- or rr-axis.

            point2[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreePoints.point2 "Permalink to this definition")
            :   A sequence of Floats specifying the coordinates of a point in the 1-2 or rr-θθ plane.

        Returns:[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreePoints-returns "Permalink to this headline")
        :   An OdbDatumCsys object.

        Return type:[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.DatumCsysByThreePoints-return-type "Permalink to this headline")
        :   [`OdbDatumCsys`](#abaqus.Odb.RebarOrientation.OdbDatumCsys "abaqus.Odb.RebarOrientation.OdbDatumCsys (Python class) — Bases: object")

    coordSysType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py)[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.coordSysType "Permalink to this definition")
    :   A SymbolicConstant specifying the type of coordinate system. Possible values are
        CARTESIAN, CYLINDRICAL, and SPHERICAL.

    globalToLocal(*[coordinates](#abaqus.Odb.RebarOrientation.OdbDatumCsys.globalToLocal.coordinates "abaqus.Odb.RebarOrientation.OdbDatumCsys.globalToLocal.coordinates (Python parameter) — A tuple of three Floats representing the coordinates in the global coordinate system.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L222-L240)[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.globalToLocal "Permalink to this definition")
    :   This method transforms specified coordinates in the global coordinate system into this local
        coordinate system.

        New in version 2022: The `globalToLocal` method was added.

        Note

        Check [OdbDatumCsys.globalToLocal on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdatumcsyspyc.htm?contextscope=all#simaker-odbdatumcsysglobaltolocalpyc).

        Parameters:[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.globalToLocal-parameters "Permalink to this headline")
        :   coordinates[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.globalToLocal.coordinates "Permalink to this definition")
            :   A tuple of three Floats representing the coordinates in the global coordinate system.

        Returns:[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.globalToLocal-returns "Permalink to this headline")
        :   A tuple of three Floats representing the coordinates in this local coordinate system.

        Return type:[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.globalToLocal-return-type "Permalink to this headline")
        :   `tuple[float`, [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"), `float]`

    localToGlobal(*[coordinates](#abaqus.Odb.RebarOrientation.OdbDatumCsys.localToGlobal.coordinates "abaqus.Odb.RebarOrientation.OdbDatumCsys.localToGlobal.coordinates (Python parameter) — A tuple of three Floats representing the coordinates in the local coordinate system.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L242-L260)[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.localToGlobal "Permalink to this definition")
    :   This method transforms specified coordinates in this local coordinate system into the global
        coordinate system.

        New in version 2022: The `localToGlobal` method was added.

        Note

        Check [OdbDatumCsys.localToGlobal on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbdatumcsyspyc.htm?contextscope=all#simaker-odbdatumcsyslocaltoglobalpyc).

        Parameters:[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.localToGlobal-parameters "Permalink to this headline")
        :   coordinates[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.localToGlobal.coordinates "Permalink to this definition")
            :   A tuple of three Floats representing the coordinates in the local coordinate system.

        Returns:[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.localToGlobal-returns "Permalink to this headline")
        :   A tuple of three Floats representing the coordinates in this global coordinate system.

        Return type:[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.localToGlobal-return-type "Permalink to this headline")
        :   `tuple[float`, [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"), `float]`

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L26-L27)[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.name "Permalink to this definition")
    :   A String specifying the repository key.

    origin : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L33-L35)[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.origin "Permalink to this definition")
    :   A tuple of Floats specifying the coordinates of the origin of the datum coordinate
        system.

    xAxis : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L37-L38)[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.xAxis "Permalink to this definition")
    :   A tuple of Floats specifying a point on the **X** axis.

    yAxis : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L40-L41)[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.yAxis "Permalink to this definition")
    :   A tuple of Floats specifying a point on the **Y** axis.

    zAxis : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientation.py#L43-L44)[¶](#abaqus.Odb.RebarOrientation.OdbDatumCsys.zAxis "Permalink to this definition")
    :   A tuple of Floats specifying a point on the **Z** axis.

*class* OdbRigidBody(*[referenceNode](#abaqus.Odb.OdbRigidBodyArray.OdbRigidBody "abaqus.Odb.OdbRigidBodyArray.OdbRigidBody.__init__.referenceNode (Python parameter)")*, *[position=abaqusConstants.INPUT](#abaqus.Odb.OdbRigidBodyArray.OdbRigidBody "abaqus.Odb.OdbRigidBodyArray.OdbRigidBody.__init__.position=abaqusConstants.INPUT (Python parameter)")*, *[isothermal=1](#abaqus.Odb.OdbRigidBodyArray.OdbRigidBody "abaqus.Odb.OdbRigidBodyArray.OdbRigidBody.__init__.isothermal=1 (Python parameter)")*, *[elements=<abaqus.Odb.OdbSet.OdbSet object>](#abaqus.Odb.OdbRigidBodyArray.OdbRigidBody "abaqus.Odb.OdbRigidBodyArray.OdbRigidBody.__init__.elements=<abaqus.Odb.OdbSet.OdbSet object> (Python parameter)")*, *[tieNodes=<abaqus.Odb.OdbSet.OdbSet object>](#abaqus.Odb.OdbRigidBodyArray.OdbRigidBody "abaqus.Odb.OdbRigidBodyArray.OdbRigidBody.__init__.tieNodes=<abaqus.Odb.OdbSet.OdbSet object> (Python parameter)")*, *[pinNodes=<abaqus.Odb.OdbSet.OdbSet object>](#abaqus.Odb.OdbRigidBodyArray.OdbRigidBody "abaqus.Odb.OdbRigidBodyArray.OdbRigidBody.__init__.pinNodes=<abaqus.Odb.OdbSet.OdbSet object> (Python parameter)")*, *[analyticSurface=None](#abaqus.Odb.OdbRigidBodyArray.OdbRigidBody "abaqus.Odb.OdbRigidBodyArray.OdbRigidBody.__init__.analyticSurface=None (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbRigidBodyArray.py#L13-L106)[¶](#abaqus.Odb.OdbRigidBodyArray.OdbRigidBody "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The Rigid body object is used to bind a set of elements and/or a set of nodes and/or an analytical
    surface with a reference node.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].parts[name].rigidBodies[i]
    session.odbs[name].rootAssembly.instances[name].rigidBodies[i]
    session.odbs[name].rootAssembly.rigidBodies[i]
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.rigidBodies[i]
    ```

    Note

    Check [OdbRigidBody on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbrigidbodypyc.htm?contextscope=all).

    Member Details:

    analyticSurface : --is-rst--:py:data:`~typing.Optional`\[:py:class:`~abaqus.Odb.AnalyticSurface.AnalyticSurface`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbRigidBodyArray.py#L53-L55)[¶](#abaqus.Odb.OdbRigidBodyArray.OdbRigidBody.analyticSurface "Permalink to this definition")
    :   An AnalyticSurface object specifying the analytic surface whose motion is governed by
        the motion of rigid body reference node.

    elements : --is-rst--:py:class:`~abaqus.Odb.OdbSet.OdbSet` = `<abaqus.Odb.OdbSet.OdbSet object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbRigidBodyArray.py#L41-L43)[¶](#abaqus.Odb.OdbRigidBodyArray.OdbRigidBody.elements "Permalink to this definition")
    :   An OdbSet object specifying the element set whose motion is governed by the motion of
        rigid body reference node.

    isothermal : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbRigidBodyArray.py#L36-L39)[¶](#abaqus.Odb.OdbRigidBodyArray.OdbRigidBody.isothermal "Permalink to this definition")
    :   A Boolean specifying specify whether the OdbRigidBody can have temperature gradients or
        be isothermal. This is used only for fully coupled thermal-stress analysis The default
        value is ON.

    pinNodes : --is-rst--:py:class:`~abaqus.Odb.OdbSet.OdbSet` = `<abaqus.Odb.OdbSet.OdbSet object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbRigidBodyArray.py#L49-L51)[¶](#abaqus.Odb.OdbRigidBodyArray.OdbRigidBody.pinNodes "Permalink to this definition")
    :   An OdbSet object specifying the node set which have only translational degrees of
        freedom associated with the rigid body.

    position : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'INPUT'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbRigidBodyArray.py#L31-L34)[¶](#abaqus.Odb.OdbRigidBodyArray.OdbRigidBody.position "Permalink to this definition")
    :   A SymbolicConstant specifying the specific location of the OdbRigidBody reference node
        relative to the rest of the rigid body. Possible values are INPUT and CENTER\_OF\_MASS.
        The default value is INPUT.

    referenceNode : --is-rst--:py:class:`~abaqus.Odb.OdbSet.OdbSet`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbRigidBodyArray.py)[¶](#abaqus.Odb.OdbRigidBodyArray.OdbRigidBody.referenceNode "Permalink to this definition")
    :   An OdbSet object specifying the reference node set associated with the rigid body.

    tieNodes : --is-rst--:py:class:`~abaqus.Odb.OdbSet.OdbSet` = `<abaqus.Odb.OdbSet.OdbSet object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbRigidBodyArray.py#L45-L47)[¶](#abaqus.Odb.OdbRigidBodyArray.OdbRigidBody.tieNodes "Permalink to this definition")
    :   An OdbSet object specifying the node set which have both translational and rotational
        degrees of freedom associated with the rigid body.

*class* OdbBase(*[name](#abaqus.Odb.OdbBase.OdbBase "abaqus.Odb.OdbBase.OdbBase.__init__.name (Python parameter)")*, *[analysisTitle](#abaqus.Odb.OdbBase.OdbBase "abaqus.Odb.OdbBase.OdbBase.__init__.analysisTitle (Python parameter)")=`''`*, *[description](#abaqus.Odb.OdbBase.OdbBase "abaqus.Odb.OdbBase.OdbBase.__init__.description (Python parameter)")=`''`*, *[path](#abaqus.Odb.OdbBase.OdbBase "abaqus.Odb.OdbBase.OdbBase.__init__.path (Python parameter)")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L24-L167)[¶](#abaqus.Odb.OdbBase.OdbBase "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The Odb object is the in-memory representation of an output database (ODB) file.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name]
    ```

    Note

    Check [OdbBase on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbpyc.htm?contextscope=all).

    Member Details:

    amplitudes : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Amplitude.Amplitude.Amplitude`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L38-L39)[¶](#abaqus.Odb.OdbBase.OdbBase.amplitudes "Permalink to this definition")
    :   A repository of Amplitude objects.

    close()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L107-L110)[¶](#abaqus.Odb.OdbBase.OdbBase.close "Permalink to this definition")
    :   This method closes an output database.

    customData : --is-rst--:py:class:`~abaqus.CustomKernel.RepositorySupport.RepositorySupport` = `<abaqus.CustomKernel.RepositorySupport.RepositorySupport object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L71-L72)[¶](#abaqus.Odb.OdbBase.OdbBase.customData "Permalink to this definition")
    :   A RepositorySupport object.

    filters : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Filter.Filter.Filter`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L41-L42)[¶](#abaqus.Odb.OdbBase.OdbBase.filters "Permalink to this definition")
    :   A repository of Filter objects.

    getFrame(*[frameValue](#abaqus.Odb.OdbBase.OdbBase.getFrame.frameValue "abaqus.Odb.OdbBase.OdbBase.getFrame.frameValue (Python parameter) — A Double specifying the value at which the frame is required.")*, *[match](#abaqus.Odb.OdbBase.OdbBase.getFrame.match "abaqus.Odb.OdbBase.OdbBase.getFrame.match (Python parameter) — A SymbolicConstant specifying which frame to return if there is no frame at the exact frame value.")=`abaqusConstants.CLOSEST`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L112-L141)[¶](#abaqus.Odb.OdbBase.OdbBase.getFrame "Permalink to this definition")
    :   This method returns the frame at the specified time, frequency, or mode. It will not interpolate
        values between frames. The method is not applicable to an Odb object containing steps with different
        domains or to an Odb object containing a step with load case specific data.

        Note

        Check [OdbBase.getFrame on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbpyc.htm?contextscope=all#simaker-odbgetframepyc).

        Parameters:[¶](#abaqus.Odb.OdbBase.OdbBase.getFrame-parameters "Permalink to this headline")
        :   frameValue[¶](#abaqus.Odb.OdbBase.OdbBase.getFrame.frameValue "Permalink to this definition")
            :   A Double specifying the value at which the frame is required. **frameValue** can be the
                total time or frequency.

            match=`abaqusConstants.CLOSEST`[¶](#abaqus.Odb.OdbBase.OdbBase.getFrame.match "Permalink to this definition")
            :   A SymbolicConstant specifying which frame to return if there is no frame at the exact
                frame value. Possible values are CLOSEST, BEFORE, AFTER, and EXACT. The default value is
                CLOSEST.When **match** = CLOSEST, Abaqus returns the closest frame. If the frame value
                requested is exactly halfway between two frames, Abaqus returns the frame after the
                value.When **match** = EXACT, Abaqus raises an exception if the exact frame value does not
                exist.

        Returns:[¶](#abaqus.Odb.OdbBase.OdbBase.getFrame-returns "Permalink to this headline")
        :   An OdbFrame object.

        Return type:[¶](#abaqus.Odb.OdbBase.OdbBase.getFrame-return-type "Permalink to this headline")
        :   `OdbFrame`

        Raises:[¶](#abaqus.Odb.OdbBase.OdbBase.getFrame-raises "Permalink to this headline")
        :   **OdbError** – Frame not found, If the exact frame is not found.

    isReadOnly : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L35-L36)[¶](#abaqus.Odb.OdbBase.OdbBase.isReadOnly "Permalink to this definition")
    :   A Boolean specifying whether the output database was opened with read-only access.

    jobData : --is-rst--:py:class:`~abaqus.Odb.JobData.JobData` = `<abaqus.Odb.JobData.JobData object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L47-L48)[¶](#abaqus.Odb.OdbBase.OdbBase.jobData "Permalink to this definition")
    :   A JobData object.

    materials : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Material.Material.Material`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L53-L54)[¶](#abaqus.Odb.OdbBase.OdbBase.materials "Permalink to this definition")
    :   A repository of Material objects.

    parts : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Odb.OdbPart.OdbPart`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L50-L51)[¶](#abaqus.Odb.OdbBase.OdbBase.parts "Permalink to this definition")
    :   A repository of OdbPart objects.

    profiles : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.BeamSectionProfile.Profile.Profile`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L74-L75)[¶](#abaqus.Odb.OdbBase.OdbBase.profiles "Permalink to this definition")
    :   A repository of Profile objects.

    rootAssembly : --is-rst--:py:class:`~abaqus.Odb.OdbAssembly.OdbAssembly` = `<abaqus.Odb.OdbAssembly.OdbAssembly object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L44-L45)[¶](#abaqus.Odb.OdbBase.OdbBase.rootAssembly "Permalink to this definition")
    :   An OdbAssembly object.

    save()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L143-L153)[¶](#abaqus.Odb.OdbBase.OdbBase.save "Permalink to this definition")
    :   This method saves output to an output database (.odb ) file.

        Raises:[¶](#abaqus.Odb.OdbBase.OdbBase.save-raises "Permalink to this headline")
        :   **OdbError** – Database save failed. The database was opened as read-only. Modification of data is
            not permitted.

    sectionCategories : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Odb.SectionCategory.SectionCategory`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L62-L63)[¶](#abaqus.Odb.OdbBase.OdbBase.sectionCategories "Permalink to this definition")
    :   A repository of SectionCategory objects.

    sections : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Section.Section.Section`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L59-L60)[¶](#abaqus.Odb.OdbBase.OdbBase.sections "Permalink to this definition")
    :   A repository of Section objects.

    sectorDefinition : --is-rst--:py:class:`~abaqus.Odb.SectorDefinition.SectorDefinition` = `<abaqus.Odb.SectorDefinition.SectorDefinition object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L65-L66)[¶](#abaqus.Odb.OdbBase.OdbBase.sectorDefinition "Permalink to this definition")
    :   A SectorDefinition object.

    steps : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Odb.OdbStep.OdbStep`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L56-L57)[¶](#abaqus.Odb.OdbBase.OdbBase.steps "Permalink to this definition")
    :   A repository of OdbStep objects.

    update()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L155-L167)[¶](#abaqus.Odb.OdbBase.OdbBase.update "Permalink to this definition")
    :   This method is used to update an Odb object in memory while an Abaqus analysis writes data to the
        associated output database. update checks if additional steps have been written to the output database
        since it was opened or last updated. If additional steps have been written to the output database,
        update adds them to the Odb object.

        Returns:[¶](#abaqus.Odb.OdbBase.OdbBase.update-returns "Permalink to this headline")
        :   A Boolean specifying whether additional steps or frames were added to the Odb object.

        Return type:[¶](#abaqus.Odb.OdbBase.OdbBase.update-return-type "Permalink to this headline")
        :   `Boolean`

    userData : --is-rst--:py:class:`~abaqus.Odb.UserData.UserData` = `<abaqus.Odb.UserData.UserData object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbBase.py#L68-L69)[¶](#abaqus.Odb.OdbBase.OdbBase.userData "Permalink to this definition")
    :   A UserData object.

*class* SectorDefinition[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/SectorDefinition.py#L6-L23)[¶](#abaqus.Odb.SectorDefinition.SectorDefinition "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The SectorDefinition object describes the number of symmetry sectors and axis of symmetry for a cyclic
    symmetry model.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].sectorDefinition
    ```

    Note

    Check [SectorDefinition on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectordefinitionpyc.htm?contextscope=all).

    Member Details:

    numSectors : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/SectorDefinition.py#L18-L19)[¶](#abaqus.Odb.SectorDefinition.SectorDefinition.numSectors "Permalink to this definition")
    :   An Int specifying the number of sectors in the cyclic symmetry model.

    symmetryAxis : --is-rst--:py:class:`tuple`\[:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`], :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/SectorDefinition.py#L6-L23)[¶](#abaqus.Odb.SectorDefinition.SectorDefinition.symmetryAxis "Permalink to this definition")
    :   A tuple of tuples of Floats specifying the coordinates of two points on the axis of
        symmetry.

*class* UserData[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/UserData.py#L6-L6)[¶](#abaqus.Odb.UserData.UserData "Permalink to this definition")
:   Bases: [`AnimationUserData`](mdb/annotation.html#abaqus.Annotation.AnimationUserData.AnimationUserData "abaqus.Annotation.AnimationUserData.AnimationUserData (Python class) — Bases: UserDataBase")

    Member Details:

AnalyticSurfaceProfile()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbCommands.py#L172-L184)[¶](#abaqus.Odb.OdbCommands.AnalyticSurfaceProfile "Permalink to this definition")
:   This method creates a OdbSequenceAnalyticSurfaceSegment object.

    Path:

    ```python
    odbAccess.AnalyticSurfaceProfile()
    ```

    Returns:[¶](#abaqus.Odb.OdbCommands.AnalyticSurfaceProfile-returns "Permalink to this headline")
    :   An OdbSequenceAnalyticSurfaceSegment object.

    Return type:[¶](#abaqus.Odb.OdbCommands.AnalyticSurfaceProfile-return-type "Permalink to this headline")
    :   `OdbSequenceAnalyticSurfaceSegment`

isUpgradeRequiredForOdb(*[upgradeRequiredOdbPath](#abaqus.Odb.OdbCommands.isUpgradeRequiredForOdb.upgradeRequiredOdbPath "abaqus.Odb.OdbCommands.isUpgradeRequiredForOdb.upgradeRequiredOdbPath (Python parameter) — An String specifying the path to an output database file to test.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbCommands.py#L25-L53)[¶](#abaqus.Odb.OdbCommands.isUpgradeRequiredForOdb "Permalink to this definition")
:   This method determines if an output database file needs to be upgraded to the current release. You can
    access this method using either of the following techniques:

    * From a script running outside Abaqus/CAE. For example:

      ```python
      import odbAccess
      needsUpgrade = odbAccess.isUpgradeRequiredForOdb(
          upgradeRequiredOdbPath='myOdb.odb')
      ```
    * From the Visualization module in Abaqus/CAE. For example:

      ```python
      import visualization
      needsUpgrade = session.isUpgradeRequiredForOdb(upgradeRequiredOdbPath='myOdb.odb')
      ```

    Note

    Check [OdbCommands.isUpgradeRequiredForOdb on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-functionodbcommandspyc.htm?contextscope=all#simaker-functionodbcommandsisupgraderequiredforodbpyc).

    Parameters:[¶](#abaqus.Odb.OdbCommands.isUpgradeRequiredForOdb-parameters "Permalink to this headline")
    :   upgradeRequiredOdbPath[¶](#abaqus.Odb.OdbCommands.isUpgradeRequiredForOdb.upgradeRequiredOdbPath "Permalink to this definition")
        :   An String specifying the path to an output database file to test. The test determines if
            the output database needs to be upgraded to the current release.

    Returns:[¶](#abaqus.Odb.OdbCommands.isUpgradeRequiredForOdb-returns "Permalink to this headline")
    :   A Boolean indicating the result of the test. A value of True indicates that the output
        database needs to be upgraded to the current release.

    Return type:[¶](#abaqus.Odb.OdbCommands.isUpgradeRequiredForOdb-return-type "Permalink to this headline")
    :   `Boolean`

maxEnvelope()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbCommands.py#L56-L74)[¶](#abaqus.Odb.OdbCommands.maxEnvelope "Permalink to this definition")
:   Retrieve the maximum value of an output variable over a number of fields.

    Returns:[¶](#abaqus.Odb.OdbCommands.maxEnvelope-returns "Permalink to this headline")
    :   A sequence of two fieldOutput objects. The first fieldOutput object contains the maximum
        value. The second fieldOutput object contains the index of the field containing the
        maximum value. The index follows the order in which fields are positioned in the list of
        fieldOutput objects provided as the argument to the function.

    Return type:[¶](#abaqus.Odb.OdbCommands.maxEnvelope-return-type "Permalink to this headline")
    :   `Sequence[FieldOutput]`

    Raises:[¶](#abaqus.Odb.OdbCommands.maxEnvelope-raises "Permalink to this headline")
    :   * **OdbError** –
        * [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.13)") – This function takes no keyword arguments.

minEnvelope()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbCommands.py#L77-L95)[¶](#abaqus.Odb.OdbCommands.minEnvelope "Permalink to this definition")
:   Retrieve the minimum value of an output variable over a number of fields.

    Returns:[¶](#abaqus.Odb.OdbCommands.minEnvelope-returns "Permalink to this headline")
    :   A sequence of two fieldOutput objects. The first fieldOutput object contains the minimum
        value. The second fieldOutput object contains the index of the field containing the
        minimum value. The index follows the order in which fields are positioned in the list of
        fieldOutput objects provided as the argument to the function.

    Return type:[¶](#abaqus.Odb.OdbCommands.minEnvelope-return-type "Permalink to this headline")
    :   `Sequence[tuple[FieldOutput`, `FieldOutput]]`

    Raises:[¶](#abaqus.Odb.OdbCommands.minEnvelope-raises "Permalink to this headline")
    :   * **OdbError** –
        * [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.13)") – This function takes no keyword arguments.

openOdb(*[path](#abaqus.Odb.OdbCommands.openOdb.path "abaqus.Odb.OdbCommands.openOdb.path (Python parameter) — A String specifying the path to an existing output database (.odb) file.")*, *[readOnly](#abaqus.Odb.OdbCommands.openOdb.readOnly "abaqus.Odb.OdbCommands.openOdb.readOnly (Python parameter) — A Boolean specifying whether the file will permit only read access or both read and write access.")=`0`*, *[readInternalSets](#abaqus.Odb.OdbCommands.openOdb.readInternalSets "abaqus.Odb.OdbCommands.openOdb.readInternalSets (Python parameter) — A Boolean specifying whether the file will permit access to sets specified as Internal on the database.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbCommands.py#L98-L135)[¶](#abaqus.Odb.OdbCommands.openOdb "Permalink to this definition")
:   This method opens an existing output database (.odb) file and creates a new Odb object. You typically
    execute this method outside of Abaqus/CAE when, in most cases, only one output database is open at any time.
    For example:

    ```python
    import odbAccess
    shockLoadOdb = odbAccess.openOdb(path='myOdb.odb')
    ```

    Note

    Check [OdbCommands.openOdb on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-functionodbcommandspyc.htm?contextscope=all#simaker-functionodbcommandsopenodbpyc).

    Parameters:[¶](#abaqus.Odb.OdbCommands.openOdb-parameters "Permalink to this headline")
    :   path[¶](#abaqus.Odb.OdbCommands.openOdb.path "Permalink to this definition")
        :   A String specifying the path to an existing output database (.odb) file.

        readOnly=`0`[¶](#abaqus.Odb.OdbCommands.openOdb.readOnly "Permalink to this definition")
        :   A Boolean specifying whether the file will permit only read access or both read and
            write access. The initial value is `False`, indicating that both read and write access
            will be permitted.

        readInternalSets=`0`[¶](#abaqus.Odb.OdbCommands.openOdb.readInternalSets "Permalink to this definition")
        :   A Boolean specifying whether the file will permit access to sets specified as Internal
            on the database. The initial value is `False`, indicating that internal sets will not be
            read.

    Returns:[¶](#abaqus.Odb.OdbCommands.openOdb-returns "Permalink to this headline")
    :   An Odb object.

    Return type:[¶](#abaqus.Odb.OdbCommands.openOdb-return-type "Permalink to this headline")
    :   `Odb`

    Raises:[¶](#abaqus.Odb.OdbCommands.openOdb-raises "Permalink to this headline")
    :   * **OdbError** – If the output database was generated by a previous release of Abaqus and needs
          upgrading. Run abaqus upgrade -job <newFilename> -odb <oldFileName> to upgrade it.
        * **OdbError** –
        * **opened.** – If the output database was generated by a newer release of Abaqus, and the
          installation of Abaqus needs upgrading.

upgradeOdb(*[existingOdbPath](#abaqus.Odb.OdbCommands.upgradeOdb.existingOdbPath "abaqus.Odb.OdbCommands.upgradeOdb.existingOdbPath (Python parameter) — An String specifying the path to the file containing the output database to be upgraded.")*, *[upgradedOdbPath](#abaqus.Odb.OdbCommands.upgradeOdb.upgradedOdbPath "abaqus.Odb.OdbCommands.upgradeOdb.upgradedOdbPath (Python parameter) — An String specifying the path to the file that will contain the upgraded output database.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbCommands.py#L138-L167)[¶](#abaqus.Odb.OdbCommands.upgradeOdb "Permalink to this definition")
:   This method upgrades an existing Odb object to the current release and writes the upgraded version of the
    Odb object to a file. In addition, Abaqus/CAE writes information about the status of the upgrade to a log
    (.log) file. You can access this method using either of the following techniques:

    * From a script running outside Abaqus/CAE. For example:

      ```python
      import odbAccess
      odbAccess.upgradeOdb(existingOdbPath='oldOdb', upgradedOdbPath='upgradedOdb')
      ```
    * From the session object in Abaqus/CAE. For example:

      ```python
      import visualization
      session.upgradeOdb(existingOdbPath='oldOdb', upgradedOdbPath='upgradedOdb')
      ```

    Note

    Check [OdbCommands.upgradeOdb on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-functionodbcommandspyc.htm?contextscope=all#simaker-functionodbcommandsupgradeodbpyc).

    Parameters:[¶](#abaqus.Odb.OdbCommands.upgradeOdb-parameters "Permalink to this headline")
    :   existingOdbPath[¶](#abaqus.Odb.OdbCommands.upgradeOdb.existingOdbPath "Permalink to this definition")
        :   An String specifying the path to the file containing the output database to be upgraded.

        upgradedOdbPath[¶](#abaqus.Odb.OdbCommands.upgradeOdb.upgradedOdbPath "Permalink to this definition")
        :   An String specifying the path to the file that will contain the upgraded output
            database.

    Raises:[¶](#abaqus.Odb.OdbCommands.upgradeOdb-raises "Permalink to this headline")
    :   **OdbError** – If the output database upgrade fails.

*class* OdbFrame(*[incrementNumber](#abaqus.Odb.OdbStepBase.OdbFrame "abaqus.Odb.OdbStepBase.OdbFrame.__init__.incrementNumber (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[frameValue](#abaqus.Odb.OdbStepBase.OdbFrame "abaqus.Odb.OdbStepBase.OdbFrame.__init__.frameValue (Python parameter)"): [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*, *[description](#abaqus.Odb.OdbStepBase.OdbFrame "abaqus.Odb.OdbStepBase.OdbFrame.__init__.description (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = `''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L12-L244)[¶](#abaqus.Odb.OdbStepBase.OdbFrame "Permalink to this definition")

*class* OdbFrame(*[mode](#abaqus.Odb.OdbStepBase.OdbFrame "abaqus.Odb.OdbStepBase.OdbFrame.__init__.mode (Python parameter)"): [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)")*, *[frequency](#abaqus.Odb.OdbStepBase.OdbFrame "abaqus.Odb.OdbStepBase.OdbFrame.__init__.frequency (Python parameter)"): [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")*, *[description](#abaqus.Odb.OdbStepBase.OdbFrame "abaqus.Odb.OdbStepBase.OdbFrame.__init__.description (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = `''`*)

*class* OdbFrame(*[loadCase](#abaqus.Odb.OdbStepBase.OdbFrame "abaqus.Odb.OdbStepBase.OdbFrame.__init__.loadCase (Python parameter)"): [OdbLoadCase](#abaqus.Odb.OdbStepBase.OdbLoadCase "abaqus.Odb.OdbLoadCase.OdbLoadCase (Python class)")*, *[description](#abaqus.Odb.OdbStepBase.OdbFrame "abaqus.Odb.OdbStepBase.OdbFrame.__init__.description (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = `''`*, *[frequency](#abaqus.Odb.OdbStepBase.OdbFrame "abaqus.Odb.OdbStepBase.OdbFrame.__init__.frequency (Python parameter)"): [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") = `0`*)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The domain of the OdbFrame object is taken from the parent step.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].steps[name].frames[i]
    ```

    Note

    Check [OdbFrame on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbframepyc.htm?contextscope=all).

    Member Details:

    FieldOutput(*[name](#abaqus.Odb.OdbStepBase.OdbFrame.FieldOutput "abaqus.Odb.OdbStepBase.OdbFrame.FieldOutput.name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[description](#abaqus.Odb.OdbStepBase.OdbFrame.FieldOutput "abaqus.Odb.OdbStepBase.OdbFrame.FieldOutput.description (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[type](#abaqus.Odb.OdbStepBase.OdbFrame.FieldOutput "abaqus.Odb.OdbStepBase.OdbFrame.FieldOutput.type (Python parameter)"): [SymbolicConstant](kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.SymbolicConstant "abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant (Python class)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L235-L244)[¶](#abaqus.Odb.OdbStepBase.OdbFrame.FieldOutput "Permalink to this definition")

    FieldOutput(*[field](#abaqus.Odb.OdbStepBase.OdbFrame.FieldOutput "abaqus.Odb.OdbStepBase.OdbFrame.FieldOutput.field (Python parameter)"): [FieldOutput](#abaqus.Odb.OdbStepBase.FieldOutput "abaqus.Odb.FieldOutput.FieldOutput (Python class)")*, *[name](#abaqus.Odb.OdbStepBase.OdbFrame.FieldOutput "abaqus.Odb.OdbStepBase.OdbFrame.FieldOutput.name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = `''`*, *[description](#abaqus.Odb.OdbStepBase.OdbFrame.FieldOutput "abaqus.Odb.OdbStepBase.OdbFrame.FieldOutput.description (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") = `''`*)

    FieldOutput(*\*[args](#abaqus.Odb.OdbStepBase.OdbFrame.FieldOutput "abaqus.Odb.OdbStepBase.OdbFrame.FieldOutput.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Odb.OdbStepBase.OdbFrame.FieldOutput "abaqus.Odb.OdbStepBase.OdbFrame.FieldOutput.kwargs (Python parameter)")*)

    Frame(*\*[args](#abaqus.Odb.OdbStepBase.OdbFrame.Frame "abaqus.Odb.OdbStepBase.OdbFrame.Frame.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Odb.OdbStepBase.OdbFrame.Frame "abaqus.Odb.OdbStepBase.OdbFrame.Frame.kwargs (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L151-L152)[¶](#abaqus.Odb.OdbStepBase.OdbFrame.Frame "Permalink to this definition")

    associatedFrame : --is-rst--:py:data:`~typing.Optional`\[:py:class:`~abaqus.Odb.OdbFrame.OdbFrame`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L38-L40)[¶](#abaqus.Odb.OdbStepBase.OdbFrame.associatedFrame "Permalink to this definition")
    :   An OdbFrame object specifying the real or imaginary portion of the data corresponding to
        this cyclic symmetry mode.

    cyclicModeNumber : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L23-L25)[¶](#abaqus.Odb.OdbStepBase.OdbFrame.cyclicModeNumber "Permalink to this definition")
    :   An Int specifying the cyclic mode number associated with the data stored on this frame.
        Only frequency analyses of cyclic symmetry models possess cyclic mode numbers.

    description : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L59-L60)[¶](#abaqus.Odb.OdbStepBase.OdbFrame.description "Permalink to this definition")
    :   A String specifying the contents of the frame. The default value is an empty string.

    domain : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py)[¶](#abaqus.Odb.OdbStepBase.OdbFrame.domain "Permalink to this definition")
    :   A SymbolicConstant specifying the domain of the step of which the frame is a member.
        Possible values are TIME, FREQUENCY, and MODAL.

    fieldOutputs : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Odb.FieldOutput.FieldOutput`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L42-L44)[¶](#abaqus.Odb.OdbStepBase.OdbFrame.fieldOutputs "Permalink to this definition")
    :   A repository of FieldOutput objects specifying the key to the **fieldOutputs** repository
        is a String representing an output variable.

    frameValue : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py)[¶](#abaqus.Odb.OdbStepBase.OdbFrame.frameValue "Permalink to this definition")
    :   A Float specifying the value in units determined by the **domain** member of the Step
        object. The equivalent in the time domain is **stepTime**; in the frequency domain the
        equivalent is **frequency**; and in the modal domain the equivalent is **mode**.

    frequency : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L31-L33)[¶](#abaqus.Odb.OdbStepBase.OdbFrame.frequency "Permalink to this definition")
    :   A Float specifying the frequency. This member is valid only if **domain** = FREQUENCY or if
        the **procedureType** member of the Step object=FREQUENCY. The default value is 0.0.

    incrementNumber : --is-rst--:py:class:`int`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py)[¶](#abaqus.Odb.OdbStepBase.OdbFrame.incrementNumber "Permalink to this definition")
    :   An Int specifying the frame increment number within the step. The base frame has
        normally increment number 0, and the results run from 1. In case of multiple load cases,
        the same increment number is duplicated for each loadcase.

    loadCase : --is-rst--:py:class:`~abaqus.Odb.OdbLoadCase.OdbLoadCase` = `<abaqus.Odb.OdbLoadCase.OdbLoadCase object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L46-L47)[¶](#abaqus.Odb.OdbStepBase.OdbFrame.loadCase "Permalink to this definition")
    :   An OdbLoadCase object specifying the load case for the frame.

    mode : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L35-L36)[¶](#abaqus.Odb.OdbStepBase.OdbFrame.mode "Permalink to this definition")
    :   An Int specifying the eigenmode. This member is valid only if **domain** = MODAL.

*class* OdbLoadCase(*[name](#abaqus.Odb.OdbStepBase.OdbLoadCase "abaqus.Odb.OdbStepBase.OdbLoadCase.__init__.name (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L6-L41)[¶](#abaqus.Odb.OdbStepBase.OdbLoadCase "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The OdbLoadCase object describes a load case.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].steps[name].frames[i].loadCase
    session.odbs[name].steps[name].historyRegions[name].loadCase
    session.odbs[name].steps[name].loadCases[name]
    ```

    Note

    Check [OdbLoadCase on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbloadcasepyc.htm?contextscope=all).

    Member Details:

    name : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py)[¶](#abaqus.Odb.OdbStepBase.OdbLoadCase.name "Permalink to this definition")
    :   A String specifying the name of the OdbLoadCase object.

*class* OdbInstanceBase(*[name](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.__init__.name (Python parameter)")*, *[object](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.__init__.object (Python parameter)")*, *[localCoordSystem](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.__init__.localCoordSystem (Python parameter)")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py#L34-L395)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    A part instance is the usage of a part within an assembly.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].rootAssembly.instances[name]
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance
    ```

    Note

    Check [OdbInstanceBase on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbinstancepyc.htm?contextscope=all).

    Member Details:

    AnalyticRigidSurf2DPlanar(*[name](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurf2DPlanar.name "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurf2DPlanar.name (Python parameter) — The name of the analytic surface.")*, *[profile](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurf2DPlanar.profile "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurf2DPlanar.profile (Python parameter) — A sequence of AnalyticSurfaceSegment objects or an OdbSequenceAnalyticSurfaceSegment object.")*, *[filletRadius](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurf2DPlanar.filletRadius "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurf2DPlanar.filletRadius (Python parameter) — A Double specifying the radius of curvature to smooth discontinuities between adjoining segments.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py#L270-L292)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurf2DPlanar "Permalink to this definition")
    :   This method is used to define a two-dimensional AnalyticSurface object on the instance.

        Note

        Check [AnalyticRigidSurf2DPlanar on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticrigidsurf2dplanarpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurf2DPlanar-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurf2DPlanar.name "Permalink to this definition")
            :   The name of the analytic surface.

            profile[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurf2DPlanar.profile "Permalink to this definition")
            :   A sequence of AnalyticSurfaceSegment objects or an OdbSequenceAnalyticSurfaceSegment
                object.

            filletRadius=`0`[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurf2DPlanar.filletRadius "Permalink to this definition")
            :   A Double specifying the radius of curvature to smooth discontinuities between adjoining
                segments. The default value is 0.0.

        Raises:[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurf2DPlanar-raises "Permalink to this headline")
        :   **OdbError** – 2D-Planar Analytic Rigid Surface can be defined only if the instance is of
            type TWO\_D\_PLANAR or AXISYMMETRIC.
            If OdbPart associated with the part instance is of type THREE\_D.

    AnalyticRigidSurfExtrude(*[name](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfExtrude.name "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfExtrude.name (Python parameter) — The name of the analytic surface.")*, *[profile](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfExtrude.profile "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfExtrude.profile (Python parameter) — A sequence of AnalyticSurfaceSegment objects or an OdbSequenceAnalyticSurfaceSegment object.")*, *[filletRadius](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfExtrude.filletRadius "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfExtrude.filletRadius (Python parameter) — A Double specifying the radius of curvature to smooth discontinuities between adjoining segments.")=`0`*, *[localCoordData](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfExtrude.localCoordData "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfExtrude.localCoordData (Python parameter) — A sequence of sequences of Floats specifying the global coordinates of points used to define the local coordinate system.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py#L294-L324)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfExtrude "Permalink to this definition")
    :   This method is used to define a three-dimensional cylindrical AnalyticSurface on the instance.

        Note

        Check [AnalyticRigidSurfExtrude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticrigidsurfextrudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfExtrude-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfExtrude.name "Permalink to this definition")
            :   The name of the analytic surface.

            profile[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfExtrude.profile "Permalink to this definition")
            :   A sequence of AnalyticSurfaceSegment objects or an OdbSequenceAnalyticSurfaceSegment
                object.

            filletRadius=`0`[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfExtrude.filletRadius "Permalink to this definition")
            :   A Double specifying the radius of curvature to smooth discontinuities between adjoining
                segments. The default value is 0.0.

            localCoordData=`()`[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfExtrude.localCoordData "Permalink to this definition")
            :   A sequence of sequences of Floats specifying the global coordinates of points used to
                define the local coordinate system.

        Raises:[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfExtrude-raises "Permalink to this headline")
        :   **OdbError** – Analytic Rigid Surface of type CYLINDER can be defined only if the instance is
            of type THREE\_D, If OdbPart associated with the part instance is not of type THREE\_D.

    AnalyticRigidSurfRevolve(*[name](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfRevolve.name "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfRevolve.name (Python parameter) — The name of the analytic surface.")*, *[profile](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfRevolve.profile "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfRevolve.profile (Python parameter) — A sequence of AnalyticSurfaceSegment objects or an OdbSequenceAnalyticSurfaceSegment object.")*, *[filletRadius](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfRevolve.filletRadius "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfRevolve.filletRadius (Python parameter) — A Double specifying the radius of curvature to smooth discontinuities between adjoining segments.")=`0`*, *[localCoordData](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfRevolve.localCoordData "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfRevolve.localCoordData (Python parameter) — A sequence of sequences of Floats specifying the global coordinates of points used to define the local coordinate system.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py#L326-L356)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfRevolve "Permalink to this definition")
    :   This method is used to define a three-dimensional AnalyticSurface of revolution on the instance.

        Note

        Check [AnalyticRigidSurfRevolve on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticrigidsurfrevolvepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfRevolve-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfRevolve.name "Permalink to this definition")
            :   The name of the analytic surface.

            profile[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfRevolve.profile "Permalink to this definition")
            :   A sequence of AnalyticSurfaceSegment objects or an OdbSequenceAnalyticSurfaceSegment
                object.

            filletRadius=`0`[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfRevolve.filletRadius "Permalink to this definition")
            :   A Double specifying the radius of curvature to smooth discontinuities between adjoining
                segments. The default value is 0.0.

            localCoordData=`()`[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfRevolve.localCoordData "Permalink to this definition")
            :   A sequence of sequences of Floats specifying the global coordinates of points used to
                define the local coordinate system.

        Raises:[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.AnalyticRigidSurfRevolve-raises "Permalink to this headline")
        :   **OdbError** – Analytic Rigid Surface of type REVOLUTION can be defined only if the
            instance is of type THREE\_D, If OdbPart associated with the part instance is not of type THREE\_D.

    RigidBody(*[referenceNode](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.RigidBody.referenceNode "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.RigidBody.referenceNode (Python parameter) — An OdbSet specifying the reference node assigned to the rigid body.")*, *[position](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.RigidBody.position "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.RigidBody.position (Python parameter) — A symbolic constant specify if the location of the reference node is to be defined by the user.")=`abaqusConstants.INPUT`*, *[isothermal](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.RigidBody.isothermal "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.RigidBody.isothermal (Python parameter) — A Boolean specifying an isothermal rigid body.")=`0`*, *[elset](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.RigidBody.elset "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.RigidBody.elset (Python parameter) — An OdbSet specifying an element set assigned to the rigid body.")=`''`*, *[pinNodes](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.RigidBody.pinNodes "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.RigidBody.pinNodes (Python parameter) — An OdbSet specifying pin-type nodes assigned to the rigid body.")=`''`*, *[tieNodes](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.RigidBody.tieNodes "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.RigidBody.tieNodes (Python parameter) — An OdbSet specifying tie-type nodes assigned to the rigid body.")=`''`*, *[analyticSurface](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.RigidBody.analyticSurface "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.RigidBody.analyticSurface (Python parameter) — An AnalyticSurface specifying the Analytic Rigid Surface assigned to the rigid body.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py#L358-L395)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.RigidBody "Permalink to this definition")
    :   This method defines an OdbRigidBody on the instance.

        Note

        Check [RigidBody on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rigidbodypyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.RigidBody-parameters "Permalink to this headline")
        :   referenceNode[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.RigidBody.referenceNode "Permalink to this definition")
            :   An OdbSet specifying the reference node assigned to the rigid body.

            position=`abaqusConstants.INPUT`[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.RigidBody.position "Permalink to this definition")
            :   A symbolic constant specify if the location of the reference node is to be defined by
                the user. Possible values are INPUT, and CENTER\_OF\_MASS. The default value is INPUT.

            isothermal=`0`[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.RigidBody.isothermal "Permalink to this definition")
            :   A Boolean specifying an isothermal rigid body. The default value is OFF. This parameter
                is used only for a fully-coupled thermal stress analysis.

            elset=`''`[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.RigidBody.elset "Permalink to this definition")
            :   An OdbSet specifying an element set assigned to the rigid body.

            pinNodes=`''`[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.RigidBody.pinNodes "Permalink to this definition")
            :   An OdbSet specifying pin-type nodes assigned to the rigid body.

            tieNodes=`''`[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.RigidBody.tieNodes "Permalink to this definition")
            :   An OdbSet specifying tie-type nodes assigned to the rigid body.

            analyticSurface=`''`[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.RigidBody.analyticSurface "Permalink to this definition")
            :   An AnalyticSurface specifying the Analytic Rigid Surface assigned to the rigid body.

        Raises:[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.RigidBody-raises "Permalink to this headline")
        :   **OdbError** – Rigid body definition requires a node set, If **referenceNode** is not a node set.

    analyticSurface : --is-rst--:py:class:`~abaqus.Odb.AnalyticSurface.AnalyticSurface` = `<abaqus.Odb.AnalyticSurface.AnalyticSurface object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py#L94-L95)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.analyticSurface "Permalink to this definition")
    :   An AnalyticSurface object specifying analytic Surface defined on the instance.

    assignBeamOrientation(*[region](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignBeamOrientation.region "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignBeamOrientation.region (Python parameter) — An OdbSet specifying a region on an instance.")*, *[method](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignBeamOrientation.method "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignBeamOrientation.method (Python parameter) — A SymbolicConstant specifying the assignment method.")*, *[vector](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignBeamOrientation.vector "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignBeamOrientation.vector (Python parameter) — A sequence of three Floats specifying the approximate local n1n1-direction of the beam cross-section.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py#L132-L147)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignBeamOrientation "Permalink to this definition")
    :   This method assigns a beam section orientation to a region of a part instance.

        Note

        Check [OdbInstanceBase.assignBeamOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbinstancepyc.htm?contextscope=all#simaker-odbinstanceassignbeamorientationpyc).

        Parameters:[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignBeamOrientation-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignBeamOrientation.region "Permalink to this definition")
            :   An OdbSet specifying a region on an instance.

            method[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignBeamOrientation.method "Permalink to this definition")
            :   A SymbolicConstant specifying the assignment method. Only a value of N1\_COSINES is
                currently supported.

            vector[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignBeamOrientation.vector "Permalink to this definition")
            :   A sequence of three Floats specifying the approximate local n1n1-direction of the beam
                cross-section.

    assignMaterialOrientation(*[region](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignMaterialOrientation.region "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignMaterialOrientation.region (Python parameter) — An OdbSet specifying a region on an instance.")*, *[localCsys](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignMaterialOrientation.localCsys "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignMaterialOrientation.localCsys (Python parameter) — An OdbDatumCsys object specifying the local coordinate system or None, indicating the global coordinate system.")*, *[axis](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignMaterialOrientation.axis "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignMaterialOrientation.axis (Python parameter) — A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate system about which an additional rotation is applied.")=`abaqusConstants.AXIS_1`*, *[angle](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignMaterialOrientation.angle "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignMaterialOrientation.angle (Python parameter) — A Float specifying the angle of the additional rotation.")=`0`*, *[stackDirection](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignMaterialOrientation.stackDirection "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignMaterialOrientation.stackDirection (Python parameter) — A SymbolicConstant specifying the stack or thickness direction of the material.")=`abaqusConstants.STACK_3`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py#L149-L179)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignMaterialOrientation "Permalink to this definition")
    :   This method assigns a material orientation to a region of a part instance.

        Note

        Check [OdbInstanceBase.assignMaterialOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbinstancepyc.htm?contextscope=all#simaker-odbinstanceassignmaterialorientationpyc).

        Parameters:[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignMaterialOrientation-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignMaterialOrientation.region "Permalink to this definition")
            :   An OdbSet specifying a region on an instance.

            localCsys[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignMaterialOrientation.localCsys "Permalink to this definition")
            :   An OdbDatumCsys object specifying the local coordinate system or None, indicating the
                global coordinate system.

            axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignMaterialOrientation.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate
                system about which an additional rotation is applied. For shells this axis is also the
                shell normal. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default value is
                AXIS\_1.

            angle=`0`[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignMaterialOrientation.angle "Permalink to this definition")
            :   A Float specifying the angle of the additional rotation. The default value is 0.0.

            stackDirection=`abaqusConstants.STACK_3`[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignMaterialOrientation.stackDirection "Permalink to this definition")
            :   A SymbolicConstant specifying the stack or thickness direction of the material. Possible
                values are STACK\_1, STACK\_2, STACK\_3, and STACK\_ORIENTATION. The default value is
                STACK\_3.

    assignRebarOrientation(*[region](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignRebarOrientation.region "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignRebarOrientation.region (Python parameter) — An OdbSet specifying a region on an instance.")*, *[localCsys](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignRebarOrientation.localCsys "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignRebarOrientation.localCsys (Python parameter) — An OdbDatumCsys object specifying the local coordinate system or None, indicating the global coordinate system.")*, *[axis](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignRebarOrientation.axis "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignRebarOrientation.axis (Python parameter) — A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate system about which an additional rotation is applied.")=`abaqusConstants.AXIS_1`*, *[angle](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignRebarOrientation.angle "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignRebarOrientation.angle (Python parameter) — A Float specifying the angle of the additional rotation.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py#L181-L206)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignRebarOrientation "Permalink to this definition")
    :   This method assigns a rebar reference orientation to a region of a part instance.

        Note

        Check [OdbInstanceBase.assignRebarOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbinstancepyc.htm?contextscope=all#simaker-odbinstanceassignrebarorientationpyc).

        Parameters:[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignRebarOrientation-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignRebarOrientation.region "Permalink to this definition")
            :   An OdbSet specifying a region on an instance.

            localCsys[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignRebarOrientation.localCsys "Permalink to this definition")
            :   An OdbDatumCsys object specifying the local coordinate system or None, indicating the
                global coordinate system.

            axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignRebarOrientation.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate
                system about which an additional rotation is applied. For shells this axis is also the
                shell normal. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default value is
                AXIS\_1.

            angle=`0`[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignRebarOrientation.angle "Permalink to this definition")
            :   A Float specifying the angle of the additional rotation. The default value is 0.0.

    assignSection(*[region](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignSection.region "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignSection.region (Python parameter) — An OdbSet specifying a region on an instance.")*, *[section](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignSection.section "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignSection.section (Python parameter) — A Section object.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py#L250-L268)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignSection "Permalink to this definition")
    :   This method is used to assign a section to a region on an instance.

        Note

        Check [OdbInstanceBase.assignSection on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbinstancepyc.htm?contextscope=all#simaker-odbinstanceassignsectionpyc).

        Parameters:[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignSection-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignSection.region "Permalink to this definition")
            :   An OdbSet specifying a region on an instance.

            section[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignSection.section "Permalink to this definition")
            :   A Section object.

        Raises:[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.assignSection-raises "Permalink to this headline")
        :   * **OdbError** – Section assignment requires element set, If **region** is not an element set.
            * **OdbError** – Section assignment requires element set from this part instance, If the element set is not from the current instance.

    beamOrientations : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Odb.BeamOrientation.BeamOrientation`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py#L85-L86)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.beamOrientations "Permalink to this definition")
    :   A BeamOrientationArray object.

    elementSets : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Odb.OdbSet.OdbSet`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py#L73-L74)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.elementSets "Permalink to this definition")
    :   A repository of OdbSet objects specifying element sets.

    elements : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Odb.OdbMeshElement.OdbMeshElement`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py#L67-L68)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.elements "Permalink to this definition")
    :   An OdbMeshElementArray object.

    embeddedSpace : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.embeddedSpace "Permalink to this definition")
    :   A SymbolicConstant specifying the dimensionality of the Part object. Possible values are
        THREE\_D, TWO\_D\_PLANAR, AXISYMMETRIC, and UNKNOWN\_DIMENSION.

    getElementFromLabel(*[label](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.getElementFromLabel.label "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.getElementFromLabel.label (Python parameter) — An Int specifying the element label.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py#L208-L227)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.getElementFromLabel "Permalink to this definition")
    :   This method is used to retrieved an element with a specific label from an instance object.

        Note

        Check [OdbInstanceBase.getElementFromLabel on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbinstancepyc.htm?contextscope=all#simaker-odbinstancegetelementfromlabelpyc).

        Parameters:[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.getElementFromLabel-parameters "Permalink to this headline")
        :   label[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.getElementFromLabel.label "Permalink to this definition")
            :   An Int specifying the element label.

        Returns:[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.getElementFromLabel-returns "Permalink to this headline")
        :   An OdbMeshElement object.

        Return type:[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.getElementFromLabel-return-type "Permalink to this headline")
        :   `OdbMeshElement`

        Raises:[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.getElementFromLabel-raises "Permalink to this headline")
        :   **OdbError** – Invalid element label, If no element with the specified label exists.

    getNodeFromLabel(*[label](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.getNodeFromLabel.label "abaqus.Odb.OdbInstanceBase.OdbInstanceBase.getNodeFromLabel.label (Python parameter) — An Int specifying the node label.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py#L229-L248)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.getNodeFromLabel "Permalink to this definition")
    :   This method is used to retrieved a node with a specific label from an instance object.

        Note

        Check [OdbInstanceBase.getNodeFromLabel on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbinstancepyc.htm?contextscope=all#simaker-odbinstancegetnodefromlabelpyc).

        Parameters:[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.getNodeFromLabel-parameters "Permalink to this headline")
        :   label[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.getNodeFromLabel.label "Permalink to this definition")
            :   An Int specifying the node label.

        Returns:[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.getNodeFromLabel-returns "Permalink to this headline")
        :   An OdbMeshNode object.

        Return type:[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.getNodeFromLabel-return-type "Permalink to this headline")
        :   `OdbMeshNode`

        Raises:[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.getNodeFromLabel-raises "Permalink to this headline")
        :   **OdbError** – Invalid node label, If no node with the specified label exists.

    materialOrientations : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Property.MaterialOrientation.MaterialOrientation`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py#L88-L89)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.materialOrientations "Permalink to this definition")
    :   A MaterialOrientationArray object.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py#L46-L47)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.name "Permalink to this definition")
    :   A String specifying the instance name.

    nodeSets : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Odb.OdbSet.OdbSet`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py#L70-L71)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.nodeSets "Permalink to this definition")
    :   A repository of OdbSet objects specifying node sets.

    nodes : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Odb.OdbMeshNode.OdbMeshNode`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py#L64-L65)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.nodes "Permalink to this definition")
    :   An OdbMeshNodeArray object.

    rebarOrientations : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Odb.RebarOrientation.RebarOrientation`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py#L91-L92)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.rebarOrientations "Permalink to this definition")
    :   A RebarOrientationArray object.

    resultState : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'PROPAGATED'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py#L57-L62)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.resultState "Permalink to this definition")
    :   A SymbolicConstant specifying the state of the Instance as modified by the analysis.
        This member is only present if the Instance is part of the RootAssemblyState tree.
        Possible values are:PROPAGATED, specifying that the value is the same as the previous
        frame or the original rootAssembly.MODIFIED, specifying that the geometry of the
        instance has been changed at this frame.The default value is PROPAGATED.

    rigidBodies : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Odb.OdbRigidBody.OdbRigidBody`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py#L82-L83)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.rigidBodies "Permalink to this definition")
    :   An OdbRigidBodyArray object.

    sectionAssignments : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Property.SectionAssignment.SectionAssignment`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py#L79-L80)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.sectionAssignments "Permalink to this definition")
    :   A SectionAssignmentArray object.

    surfaces : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Odb.OdbSet.OdbSet`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py#L76-L77)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.surfaces "Permalink to this definition")
    :   A repository of OdbSet objects specifying surfaces.

    type : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbInstanceBase.py)[¶](#abaqus.Odb.OdbInstanceBase.OdbInstanceBase.type "Permalink to this definition")
    :   A SymbolicConstant specifying the type of the Part object. Only a value of
        DEFORMABLE\_BODY is currently supported.

*class* OdbPartBase(*[name](#abaqus.Odb.OdbPartBase.OdbPartBase "abaqus.Odb.OdbPartBase.OdbPartBase.__init__.name (Python parameter)")*, *[embeddedSpace](#abaqus.Odb.OdbPartBase.OdbPartBase "abaqus.Odb.OdbPartBase.OdbPartBase.__init__.embeddedSpace (Python parameter)")*, *[type](#abaqus.Odb.OdbPartBase.OdbPartBase "abaqus.Odb.OdbPartBase.OdbPartBase.__init__.type (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py#L25-L381)[¶](#abaqus.Odb.OdbPartBase.OdbPartBase "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The OdbPart object is similar to the kernel Part object and contains nodes and elements, but not
    geometry.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].parts[name]
    ```

    Note

    Check [OdbPartBase on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all).

    Member Details:

    AnalyticRigidSurf2DPlanar(*[name](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurf2DPlanar.name "abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurf2DPlanar.name (Python parameter) — The name of the analytic surface.")*, *[profile](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurf2DPlanar.profile "abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurf2DPlanar.profile (Python parameter) — A sequence of AnalyticSurfaceSegment objects or an OdbSequenceAnalyticSurfaceSegment object.")*, *[filletRadius](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurf2DPlanar.filletRadius "abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurf2DPlanar.filletRadius (Python parameter) — A Double specifying the radius of curvature to smooth discontinuities between adjoining segments.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py#L314-L335)[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurf2DPlanar "Permalink to this definition")
    :   This method is used to define a two-dimensional AnalyticSurface object on the part object.

        Note

        Check [AnalyticRigidSurf2DPlanar on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticrigidsurf2dplanarpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurf2DPlanar-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurf2DPlanar.name "Permalink to this definition")
            :   The name of the analytic surface.

            profile[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurf2DPlanar.profile "Permalink to this definition")
            :   A sequence of AnalyticSurfaceSegment objects or an OdbSequenceAnalyticSurfaceSegment
                object.

            filletRadius=`0`[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurf2DPlanar.filletRadius "Permalink to this definition")
            :   A Double specifying the radius of curvature to smooth discontinuities between adjoining
                segments. The default value is 0.0.

        Raises:[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurf2DPlanar-raises "Permalink to this headline")
        :   * **OdbError** –
            * **TWO\_D\_PLANAR** – If OdbPart is of type THREE\_D.

    AnalyticRigidSurfExtrude(*[name](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurfExtrude.name "abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurfExtrude.name (Python parameter) — The name of the analytic surface.")*, *[profile](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurfExtrude.profile "abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurfExtrude.profile (Python parameter) — A sequence of AnalyticSurfaceSegment objects or an OdbSequenceAnalyticSurfaceSegment object.")*, *[filletRadius](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurfExtrude.filletRadius "abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurfExtrude.filletRadius (Python parameter) — A Double specifying the radius of curvature to smooth discontinuities between adjoining segments.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py#L337-L358)[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurfExtrude "Permalink to this definition")
    :   This method is used to define a three-dimensional cylindrical AnalyticSurface on the part object.

        Note

        Check [AnalyticRigidSurfExtrude on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticrigidsurfextrudepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurfExtrude-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurfExtrude.name "Permalink to this definition")
            :   The name of the analytic surface.

            profile[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurfExtrude.profile "Permalink to this definition")
            :   A sequence of AnalyticSurfaceSegment objects or an OdbSequenceAnalyticSurfaceSegment
                object.

            filletRadius=`0`[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurfExtrude.filletRadius "Permalink to this definition")
            :   A Double specifying the radius of curvature to smooth discontinuities between adjoining
                segments. The default value is 0.0.

        Raises:[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurfExtrude-raises "Permalink to this headline")
        :   * **OdbError** –
            * **of type THREE\_D** – If OdbPart is not of type THREE\_D.

    AnalyticRigidSurfRevolve(*[name](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurfRevolve.name "abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurfRevolve.name (Python parameter) — The name of the analytic surface.")*, *[profile](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurfRevolve.profile "abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurfRevolve.profile (Python parameter) — A sequence of AnalyticSurfaceSegment objects or an OdbSequenceAnalyticSurfaceSegment object.")*, *[filletRadius](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurfRevolve.filletRadius "abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurfRevolve.filletRadius (Python parameter) — A Double specifying the radius of curvature to smooth discontinuities between adjoining segments.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py#L360-L381)[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurfRevolve "Permalink to this definition")
    :   This method is used to define a three-dimensional AnalyticSurface of revolution on the part object.

        Note

        Check [AnalyticRigidSurfRevolve on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-analyticrigidsurfrevolvepyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurfRevolve-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurfRevolve.name "Permalink to this definition")
            :   The name of the analytic surface.

            profile[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurfRevolve.profile "Permalink to this definition")
            :   A sequence of AnalyticSurfaceSegment objects or an OdbSequenceAnalyticSurfaceSegment
                object.

            filletRadius=`0`[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurfRevolve.filletRadius "Permalink to this definition")
            :   A Double specifying the radius of curvature to smooth discontinuities between adjoining
                segments. The default value is 0.0.

        Raises:[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.AnalyticRigidSurfRevolve-raises "Permalink to this headline")
        :   * **OdbError** –
            * **of type THREE\_D** – If OdbPart is not of type THREE\_D.

    addElements(*[labels](#abaqus.Odb.OdbPartBase.OdbPartBase.addElements "abaqus.Odb.OdbPartBase.OdbPartBase.addElements.labels (Python parameter)"): [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")*, *[connectivity](#abaqus.Odb.OdbPartBase.OdbPartBase.addElements "abaqus.Odb.OdbPartBase.OdbPartBase.addElements.connectivity (Python parameter)"): [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")*, *[type](#abaqus.Odb.OdbPartBase.OdbPartBase.addElements "abaqus.Odb.OdbPartBase.OdbPartBase.addElements.type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py#L158-L159)[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.addElements "Permalink to this definition")

    addElements(*[elementData](#abaqus.Odb.OdbPartBase.OdbPartBase.addElements "abaqus.Odb.OdbPartBase.OdbPartBase.addElements.elementData (Python parameter)"): [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")*, *[type](#abaqus.Odb.OdbPartBase.OdbPartBase.addElements "abaqus.Odb.OdbPartBase.OdbPartBase.addElements.type (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[elementSetName](#abaqus.Odb.OdbPartBase.OdbPartBase.addElements "abaqus.Odb.OdbPartBase.OdbPartBase.addElements.elementSetName (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)

    addElements(*\*[args](#abaqus.Odb.OdbPartBase.OdbPartBase.addElements "abaqus.Odb.OdbPartBase.OdbPartBase.addElements.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Odb.OdbPartBase.OdbPartBase.addElements "abaqus.Odb.OdbPartBase.OdbPartBase.addElements.kwargs (Python parameter)")*)

    addNodes(*[labels](#abaqus.Odb.OdbPartBase.OdbPartBase.addNodes "abaqus.Odb.OdbPartBase.OdbPartBase.addNodes.labels (Python parameter)"): [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")*, *[coordinates](#abaqus.Odb.OdbPartBase.OdbPartBase.addNodes "abaqus.Odb.OdbPartBase.OdbPartBase.addNodes.coordinates (Python parameter)"): [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")*, *[nodeSetName](#abaqus.Odb.OdbPartBase.OdbPartBase.addNodes "abaqus.Odb.OdbPartBase.OdbPartBase.addNodes.nodeSetName (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py#L194-L195)[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.addNodes "Permalink to this definition")

    addNodes(*[nodeData](#abaqus.Odb.OdbPartBase.OdbPartBase.addNodes "abaqus.Odb.OdbPartBase.OdbPartBase.addNodes.nodeData (Python parameter)"): [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.13)")*, *[nodeSetName](#abaqus.Odb.OdbPartBase.OdbPartBase.addNodes "abaqus.Odb.OdbPartBase.OdbPartBase.addNodes.nodeSetName (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.13)") = `None`*)

    addNodes(*\*[args](#abaqus.Odb.OdbPartBase.OdbPartBase.addNodes "abaqus.Odb.OdbPartBase.OdbPartBase.addNodes.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Odb.OdbPartBase.OdbPartBase.addNodes "abaqus.Odb.OdbPartBase.OdbPartBase.addNodes.kwargs (Python parameter)")*)

    analyticSurface : --is-rst--:py:class:`~abaqus.Odb.AnalyticSurface.AnalyticSurface` = `<abaqus.Odb.AnalyticSurface.AnalyticSurface object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py#L67-L68)[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.analyticSurface "Permalink to this definition")
    :   An AnalyticSurface object specifying analytic Surface defined on the instance.

    assignBeamOrientation(*[region](#abaqus.Odb.OdbPartBase.OdbPartBase.assignBeamOrientation.region "abaqus.Odb.OdbPartBase.OdbPartBase.assignBeamOrientation.region (Python parameter) — An OdbSet specifying a region on an instance.")*, *[method](#abaqus.Odb.OdbPartBase.OdbPartBase.assignBeamOrientation.method "abaqus.Odb.OdbPartBase.OdbPartBase.assignBeamOrientation.method (Python parameter) — A SymbolicConstant specifying the assignment method.")*, *[vector](#abaqus.Odb.OdbPartBase.OdbPartBase.assignBeamOrientation.vector "abaqus.Odb.OdbPartBase.OdbPartBase.assignBeamOrientation.vector (Python parameter) — A sequence of three Floats specifying the approximate local n1n1 -direction of the beam cross-section.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py#L197-L211)[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.assignBeamOrientation "Permalink to this definition")
    :   This method assigns a beam section orientation to a region of a part instance.

        Parameters:[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.assignBeamOrientation-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.assignBeamOrientation.region "Permalink to this definition")
            :   An OdbSet specifying a region on an instance.

            method[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.assignBeamOrientation.method "Permalink to this definition")
            :   A SymbolicConstant specifying the assignment method. Only a value of N1\_COSINES is
                currently supported.

            vector[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.assignBeamOrientation.vector "Permalink to this definition")
            :   A sequence of three Floats specifying the approximate local n1n1 -direction of the beam
                cross-section.

    assignMaterialOrientation(*[region](#abaqus.Odb.OdbPartBase.OdbPartBase.assignMaterialOrientation.region "abaqus.Odb.OdbPartBase.OdbPartBase.assignMaterialOrientation.region (Python parameter) — An OdbSet specifying a region on an instance.")*, *[localCSys](#abaqus.Odb.OdbPartBase.OdbPartBase.assignMaterialOrientation.localCSys "abaqus.Odb.OdbPartBase.OdbPartBase.assignMaterialOrientation.localCSys (Python parameter) — An OdbDatumCsys object specifying the local coordinate system or None, indicating the global coordinate system.")*, *[axis](#abaqus.Odb.OdbPartBase.OdbPartBase.assignMaterialOrientation.axis "abaqus.Odb.OdbPartBase.OdbPartBase.assignMaterialOrientation.axis (Python parameter) — A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate system about which an additional rotation is applied.")=`abaqusConstants.AXIS_1`*, *[angle](#abaqus.Odb.OdbPartBase.OdbPartBase.assignMaterialOrientation.angle "abaqus.Odb.OdbPartBase.OdbPartBase.assignMaterialOrientation.angle (Python parameter) — A Float specifying the angle of the additional rotation.")=`0`*, *[stackDirection](#abaqus.Odb.OdbPartBase.OdbPartBase.assignMaterialOrientation.stackDirection "abaqus.Odb.OdbPartBase.OdbPartBase.assignMaterialOrientation.stackDirection (Python parameter) — A SymbolicConstant specifying the stack or thickness direction of the material.")=`abaqusConstants.STACK_3`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py#L213-L243)[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.assignMaterialOrientation "Permalink to this definition")
    :   This method assigns a material orientation to a region of a part instance.

        Note

        Check [OdbPartBase.assignMaterialOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partassignmaterialorientationpyc).

        Parameters:[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.assignMaterialOrientation-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.assignMaterialOrientation.region "Permalink to this definition")
            :   An OdbSet specifying a region on an instance.

            localCSys[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.assignMaterialOrientation.localCSys "Permalink to this definition")
            :   An OdbDatumCsys object specifying the local coordinate system or None, indicating the
                global coordinate system.

            axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.assignMaterialOrientation.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate
                system about which an additional rotation is applied. For shells this axis is also the
                shell normal. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default value is
                AXIS\_1.

            angle=`0`[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.assignMaterialOrientation.angle "Permalink to this definition")
            :   A Float specifying the angle of the additional rotation. The default value is 0.0.

            stackDirection=`abaqusConstants.STACK_3`[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.assignMaterialOrientation.stackDirection "Permalink to this definition")
            :   A SymbolicConstant specifying the stack or thickness direction of the material. Possible
                values are STACK\_1, STACK\_2, STACK\_3, and STACK\_ORIENTATION. The default value is
                STACK\_3.

    assignRebarOrientation(*[region](#abaqus.Odb.OdbPartBase.OdbPartBase.assignRebarOrientation.region "abaqus.Odb.OdbPartBase.OdbPartBase.assignRebarOrientation.region (Python parameter) — An OdbSet specifying a region on an instance.")*, *[localCsys](#abaqus.Odb.OdbPartBase.OdbPartBase.assignRebarOrientation.localCsys "abaqus.Odb.OdbPartBase.OdbPartBase.assignRebarOrientation.localCsys (Python parameter) — An OdbDatumCsys object specifying the local coordinate system or None, indicating the global coordinate system.")*, *[axis](#abaqus.Odb.OdbPartBase.OdbPartBase.assignRebarOrientation.axis "abaqus.Odb.OdbPartBase.OdbPartBase.assignRebarOrientation.axis (Python parameter) — A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate system about which an additional rotation is applied.")=`abaqusConstants.AXIS_1`*, *[angle](#abaqus.Odb.OdbPartBase.OdbPartBase.assignRebarOrientation.angle "abaqus.Odb.OdbPartBase.OdbPartBase.assignRebarOrientation.angle (Python parameter) — A Float specifying the angle of the additional rotation.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py#L245-L270)[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.assignRebarOrientation "Permalink to this definition")
    :   This method assigns a rebar reference orientation to a region of a part instance.

        Note

        Check [OdbPartBase.assignRebarOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partassignrebarorientationpyc).

        Parameters:[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.assignRebarOrientation-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.assignRebarOrientation.region "Permalink to this definition")
            :   An OdbSet specifying a region on an instance.

            localCsys[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.assignRebarOrientation.localCsys "Permalink to this definition")
            :   An OdbDatumCsys object specifying the local coordinate system or None, indicating the
                global coordinate system.

            axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.assignRebarOrientation.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate
                system about which an additional rotation is applied. For shells this axis is also the
                shell normal. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default value is
                AXIS\_1.

            angle=`0`[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.assignRebarOrientation.angle "Permalink to this definition")
            :   A Float specifying the angle of the additional rotation. The default value is 0.0.

    beamOrientations : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Odb.BeamOrientation.BeamOrientation`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py#L55-L56)[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.beamOrientations "Permalink to this definition")
    :   A BeamOrientationArray object.

    elementSets : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Odb.OdbSet.OdbSet`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py#L46-L47)[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.elementSets "Permalink to this definition")
    :   A repository of OdbSet objects specifying element sets.

    elements : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Odb.OdbMeshElement.OdbMeshElement`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py#L40-L41)[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.elements "Permalink to this definition")
    :   An OdbMeshElementArray object.

    getElementFromLabel(*[label](#abaqus.Odb.OdbPartBase.OdbPartBase.getElementFromLabel.label "abaqus.Odb.OdbPartBase.OdbPartBase.getElementFromLabel.label (Python parameter) — An Int specifying the element label.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py#L272-L291)[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.getElementFromLabel "Permalink to this definition")
    :   This method is used to retrieved an element with a specific label from a part object.

        Note

        Check [OdbPartBase.getElementFromLabel on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partgetelementfromlabelpyc).

        Parameters:[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.getElementFromLabel-parameters "Permalink to this headline")
        :   label[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.getElementFromLabel.label "Permalink to this definition")
            :   An Int specifying the element label.

        Returns:[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.getElementFromLabel-returns "Permalink to this headline")
        :   An OdbMeshElement object.

        Return type:[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.getElementFromLabel-return-type "Permalink to this headline")
        :   `OdbMeshElement`

        Raises:[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.getElementFromLabel-raises "Permalink to this headline")
        :   **OdbError** – Invalid element label, If no element with the specified label exists.

    getNodeFromLabel(*[label](#abaqus.Odb.OdbPartBase.OdbPartBase.getNodeFromLabel.label "abaqus.Odb.OdbPartBase.OdbPartBase.getNodeFromLabel.label (Python parameter) — An Int specifying the node label.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py#L293-L312)[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.getNodeFromLabel "Permalink to this definition")
    :   This method is used to retrieved a node with a specific label from a part object.

        Note

        Check [OdbPartBase.getNodeFromLabel on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partgetnodefromlabelpyc).

        Parameters:[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.getNodeFromLabel-parameters "Permalink to this headline")
        :   label[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.getNodeFromLabel.label "Permalink to this definition")
            :   An Int specifying the node label.

        Returns:[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.getNodeFromLabel-returns "Permalink to this headline")
        :   An OdbMeshNode object.

        Return type:[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.getNodeFromLabel-return-type "Permalink to this headline")
        :   `OdbMeshNode`

        Raises:[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.getNodeFromLabel-raises "Permalink to this headline")
        :   **OdbError** – Invalid node label, If no node with the specified label exists.

    materialOrientations : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Property.MaterialOrientation.MaterialOrientation`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py#L58-L59)[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.materialOrientations "Permalink to this definition")
    :   A MaterialOrientationArray object.

    nodeSets : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Odb.OdbSet.OdbSet`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py#L43-L44)[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.nodeSets "Permalink to this definition")
    :   A repository of OdbSet objects specifying node sets.

    nodes : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Odb.OdbMeshNode.OdbMeshNode`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py#L37-L38)[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.nodes "Permalink to this definition")
    :   An OdbMeshNodeArray object.

    rebarOrientations : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Odb.RebarOrientation.RebarOrientation`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py#L61-L62)[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.rebarOrientations "Permalink to this definition")
    :   A RebarOrientationArray object.

    rigidBodies : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Odb.OdbRigidBody.OdbRigidBody`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py#L64-L65)[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.rigidBodies "Permalink to this definition")
    :   An OdbRigidBodyArray object.

    sectionAssignments : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Property.SectionAssignment.SectionAssignment`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py#L52-L53)[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.sectionAssignments "Permalink to this definition")
    :   A SectionAssignmentArray object.

    surfaces : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Odb.OdbSet.OdbSet`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPartBase.py#L49-L50)[¶](#abaqus.Odb.OdbPartBase.OdbPartBase.surfaces "Permalink to this definition")
    :   A repository of OdbSet objects specifying surfaces.

*class* OdbPretensionSection[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPretensionSectionArray.py#L8-L30)[¶](#abaqus.Odb.OdbPretensionSectionArray.OdbPretensionSection "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The pretension section object is used to define an assembly load. It associates a pretension node with a
    pretension section.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].rootAssembly.pretensionSections[i]
    ```

    Note

    Check [OdbPretensionSection on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbpretensionsectionpyc.htm?contextscope=all).

    Member Details:

    element : --is-rst--:py:class:`~abaqus.Odb.OdbSet.OdbSet` = `<abaqus.Odb.OdbSet.OdbSet object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPretensionSectionArray.py#L23-L24)[¶](#abaqus.Odb.OdbPretensionSectionArray.OdbPretensionSection.element "Permalink to this definition")
    :   An OdbSet object specifying the element set that defines the pretension section.

    node : --is-rst--:py:class:`~abaqus.Odb.OdbSet.OdbSet` = `<abaqus.Odb.OdbSet.OdbSet object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPretensionSectionArray.py#L20-L21)[¶](#abaqus.Odb.OdbPretensionSectionArray.OdbPretensionSection.node "Permalink to this definition")
    :   An OdbSet object specifying the node set containing the pretension node.

    normal : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPretensionSectionArray.py#L8-L30)[¶](#abaqus.Odb.OdbPretensionSectionArray.OdbPretensionSection.normal "Permalink to this definition")
    :   A tuple of Floats specifying the components of the normal to the pretension section.

    surface : --is-rst--:py:class:`~abaqus.Odb.OdbSet.OdbSet` = `<abaqus.Odb.OdbSet.OdbSet object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbPretensionSectionArray.py#L26-L27)[¶](#abaqus.Odb.OdbPretensionSectionArray.OdbPretensionSection.surface "Permalink to this definition")
    :   An OdbSet object specifying the surface set that defines the pretension section.

*class* OdbSession[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbSession.py#L11-L109)[¶](#abaqus.Odb.OdbSession.OdbSession "Permalink to this definition")
:   Bases: [`SessionBase`](session/index.html#abaqus.Session.SessionBase.SessionBase "abaqus.Session.SessionBase.SessionBase (Python class) — Bases: object")

    Member Details:

    ScratchOdb(*[odb](#abaqus.Odb.OdbSession.OdbSession.ScratchOdb.odb "abaqus.Odb.OdbSession.OdbSession.ScratchOdb.odb (Python parameter) — An Odb object specifying the output database with which to associate.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbSession.py#L13-L33)[¶](#abaqus.Odb.OdbSession.OdbSession.ScratchOdb "Permalink to this definition")
    :   This method creates a new ScratchOdb object.

        Note

        This function can be accessed by:

        ```python
        session.ScratchOdb
        ```

        Note

        Check [ScratchOdb on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-scratchodbpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.OdbSession.OdbSession.ScratchOdb-parameters "Permalink to this headline")
        :   odb[¶](#abaqus.Odb.OdbSession.OdbSession.ScratchOdb.odb "Permalink to this definition")
            :   An Odb object specifying the output database with which to associate.

        Returns:[¶](#abaqus.Odb.OdbSession.OdbSession.ScratchOdb-returns "Permalink to this headline")
        :   A ScratchOdb object.

        Return type:[¶](#abaqus.Odb.OdbSession.OdbSession.ScratchOdb-return-type "Permalink to this headline")
        :   [`ScratchOdb`](#abaqus.Odb.OdbSession.OdbSession.ScratchOdb "abaqus.Odb.OdbSession.OdbSession.ScratchOdb (Python method) — This method creates a new ScratchOdb object.")

    openOdb(*[name](#abaqus.Odb.OdbSession.OdbSession.openOdb.name "abaqus.Odb.OdbSession.OdbSession.openOdb.name (Python parameter) — A String specifying the repository key.")*, *[path](#abaqus.Odb.OdbSession.OdbSession.openOdb.path "abaqus.Odb.OdbSession.OdbSession.openOdb.path (Python parameter) — A String specifying the path to an existing output database (.odb) file.")=`''`*, *[readOnly](#abaqus.Odb.OdbSession.OdbSession.openOdb.readOnly "abaqus.Odb.OdbSession.OdbSession.openOdb.readOnly (Python parameter) — A Boolean specifying whether the file will permit only read access or both read and write access.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbSession.py#L37-L78)[¶](#abaqus.Odb.OdbSession.OdbSession.openOdb "Permalink to this definition")
    :   This method opens an existing output database (.odb) file and creates a new Odb object. This method
        is accessed only via the session object inside Abaqus/CAE and adds the new Odb object to the
        session.odbs repository. This method allows you to open multiple output databases at the same time and
        to use the repository key to specify a particular output database. For example:

        ```python
        import visualization
        session.openOdb(name='myOdb', path='stress.odb', readOnly=True)
        ```

        Note

        Check [OdbSession.openOdb on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsessionpyc.htm?contextscope=all#simaker-odbsessionopenodbpyc).

        Parameters:[¶](#abaqus.Odb.OdbSession.OdbSession.openOdb-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.OdbSession.OdbSession.openOdb.name "Permalink to this definition")
            :   A String specifying the repository key. If the `name` is not the same as the `path` to the
                output database (.odb) file, the `path` must be specified as well. Additionally, to
                support backwards compatibility of the interface, if the `name` parameter is omitted,
                the `path` and `name` will be presumed to be the same.

            path=`''`[¶](#abaqus.Odb.OdbSession.OdbSession.openOdb.path "Permalink to this definition")
            :   A String specifying the path to an existing output database (.odb) file.

            readOnly=`0`[¶](#abaqus.Odb.OdbSession.OdbSession.openOdb.readOnly "Permalink to this definition")
            :   A Boolean specifying whether the file will permit only read access or both read and
                write access. The initial value is TRUE when the output database file is opened from
                Abaqus/CAE, indicating that only read access will be permitted.

        Returns:[¶](#abaqus.Odb.OdbSession.OdbSession.openOdb-returns "Permalink to this headline")
        :   An Odb object.

        Return type:[¶](#abaqus.Odb.OdbSession.OdbSession.openOdb-return-type "Permalink to this headline")
        :   `Odb`

        Raises:[¶](#abaqus.Odb.OdbSession.OdbSession.openOdb-raises "Permalink to this headline")
        :   * **OdbError** – The database is from a previous release of Abaqus, If the output database was generated by a previous release of Abaqus and needs
              upgrading, Run abaqus upgrade -job <newFilename> -odb <oldFileName> to upgrade it.
            * **OdbError** – Abaqus installation must be upgraded before this output database can be opened, If the output database was generated by a newer release of Abaqus, and the
              installation of Abaqus needs upgrading.
            * [**AbaqusError**](../autoapi/abqpy/run/index.html#abqpy.run.AbaqusError "abqpy.run.AbaqusError (Python exception) — Bases: Exception") – If the file is not a valid database.

    upgradeOdb(*[existingOdbPath](#abaqus.Odb.OdbSession.OdbSession.upgradeOdb.existingOdbPath "abaqus.Odb.OdbSession.OdbSession.upgradeOdb.existingOdbPath (Python parameter) — An String specifying the path to the file containing the output database to be upgraded.")*, *[upgradedOdbPath](#abaqus.Odb.OdbSession.OdbSession.upgradeOdb.upgradedOdbPath "abaqus.Odb.OdbSession.OdbSession.upgradeOdb.upgradedOdbPath (Python parameter) — An String specifying the path to the file that will contain the upgraded output database.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbSession.py#L80-L109)[¶](#abaqus.Odb.OdbSession.OdbSession.upgradeOdb "Permalink to this definition")
    :   This method upgrades an existing Odb object to the current release and writes the upgraded version of the
        Odb object to a file. In addition, Abaqus/CAE writes information about the status of the upgrade to a log
        (.log) file. You can access this method using either of the following techniques:

        * From a script running outside Abaqus/CAE. For example:

          ```python
          import odbAccess
          odbAccess.upgradeOdb(existingOdbPath='oldOdb', upgradedOdbPath='upgradedOdb')
          ```
        * From the session object in Abaqus/CAE. For example:

          ```python
          import visualization
          session.upgradeOdb(existingOdbPath='oldOdb', upgradedOdbPath='upgradedOdb')
          ```

        Note

        Check [OdbSession.upgradeOdb on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbsessionpyc.htm?contextscope=all#simaker-odbsessionupgradeodbpyc).

        Parameters:[¶](#abaqus.Odb.OdbSession.OdbSession.upgradeOdb-parameters "Permalink to this headline")
        :   existingOdbPath[¶](#abaqus.Odb.OdbSession.OdbSession.upgradeOdb.existingOdbPath "Permalink to this definition")
            :   An String specifying the path to the file containing the output database to be upgraded.

            upgradedOdbPath[¶](#abaqus.Odb.OdbSession.OdbSession.upgradeOdb.upgradedOdbPath "Permalink to this definition")
            :   An String specifying the path to the file that will contain the upgraded output
                database.

        Raises:[¶](#abaqus.Odb.OdbSession.OdbSession.upgradeOdb-raises "Permalink to this headline")
        :   **OdbError** – If the output database upgrade fails.

*class* ScratchOdb(*[odb](#abaqus.Odb.ScratchOdb.ScratchOdb "abaqus.Odb.ScratchOdb.ScratchOdb.__init__.odb (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/ScratchOdb.py#L8-L41)[¶](#abaqus.Odb.ScratchOdb.ScratchOdb "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    A scratch output database is associated with an open output database and is used to store session-
    related, non-persistent objects, such as Step, Frame and FieldOutput objects. Abaqus creates a scratch
    output database when needed for these non-persistent objects during an Abaqus/CAE session. Abaqus deletes
    the scratch output database when the associated output database is closed.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.scratchOdbs[name]
    ```

    Note

    Check [ScratchOdb on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbpyc.htm?contextscope=all).

    Member Details:

*class* OdbStepBase(*[name](#abaqus.Odb.OdbStepBase.OdbStepBase "abaqus.Odb.OdbStepBase.OdbStepBase.__init__.name (Python parameter)")*, *[description](#abaqus.Odb.OdbStepBase.OdbStepBase "abaqus.Odb.OdbStepBase.OdbStepBase.__init__.description (Python parameter)")*, *[domain](#abaqus.Odb.OdbStepBase.OdbStepBase "abaqus.Odb.OdbStepBase.OdbStepBase.__init__.domain (Python parameter)")*, *[timePeriod](#abaqus.Odb.OdbStepBase.OdbStepBase "abaqus.Odb.OdbStepBase.OdbStepBase.__init__.timePeriod (Python parameter)")=`0`*, *[previousStepName](#abaqus.Odb.OdbStepBase.OdbStepBase "abaqus.Odb.OdbStepBase.OdbStepBase.__init__.previousStepName (Python parameter)")=`''`*, *[procedure](#abaqus.Odb.OdbStepBase.OdbStepBase "abaqus.Odb.OdbStepBase.OdbStepBase.__init__.procedure (Python parameter)")=`''`*, *[totalTime](#abaqus.Odb.OdbStepBase.OdbStepBase "abaqus.Odb.OdbStepBase.OdbStepBase.__init__.totalTime (Python parameter)")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L19-L309)[¶](#abaqus.Odb.OdbStepBase.OdbStepBase "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    An output database contains the same steps of the model database that originated it.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].steps[name]
    ```

    Note

    Check [OdbStepBase on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-steppyc.htm?contextscope=all).

    Member Details:

    acousticMass : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L40-L41)[¶](#abaqus.Odb.OdbStepBase.OdbStepBase.acousticMass "Permalink to this definition")
    :   A Float specifying the current value of the mass of the acoustic media of the model.

    acousticMassCenter : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L67-L69)[¶](#abaqus.Odb.OdbStepBase.OdbStepBase.acousticMassCenter "Permalink to this definition")
    :   A tuple of Floats specifying the coordinates of the center of mass of the acoustic
        media.

    frames : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Odb.OdbFrame.OdbFrame`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L43-L44)[¶](#abaqus.Odb.OdbStepBase.OdbStepBase.frames "Permalink to this definition")
    :   An OdbFrameArray object.

    getFrame(*[frameValue](#abaqus.Odb.OdbStepBase.OdbStepBase.getFrame "abaqus.Odb.OdbStepBase.OdbStepBase.getFrame.frameValue (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[match](#abaqus.Odb.OdbStepBase.OdbStepBase.getFrame "abaqus.Odb.OdbStepBase.OdbStepBase.getFrame.match (Python parameter)"): [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")[CLOSEST] | [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")[BEFORE] | [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")[AFTER] | [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")[EXACT] = `CLOSEST`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L263-L265)[¶](#abaqus.Odb.OdbStepBase.OdbStepBase.getFrame "Permalink to this definition")

    getFrame(*[loadCase](#abaqus.Odb.OdbStepBase.OdbStepBase.getFrame "abaqus.Odb.OdbStepBase.OdbStepBase.getFrame.loadCase (Python parameter)"): [OdbLoadCase](#abaqus.Odb.OdbStepBase.OdbLoadCase "abaqus.Odb.OdbLoadCase.OdbLoadCase (Python class)")*)

    getFrame(*[loadCase](#abaqus.Odb.OdbStepBase.OdbStepBase.getFrame "abaqus.Odb.OdbStepBase.OdbStepBase.getFrame.loadCase (Python parameter)"): [OdbLoadCase](#abaqus.Odb.OdbStepBase.OdbLoadCase "abaqus.Odb.OdbLoadCase.OdbLoadCase (Python class)")*, *[frameValue](#abaqus.Odb.OdbStepBase.OdbStepBase.getFrame "abaqus.Odb.OdbStepBase.OdbStepBase.getFrame.frameValue (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[match](#abaqus.Odb.OdbStepBase.OdbStepBase.getFrame "abaqus.Odb.OdbStepBase.OdbStepBase.getFrame.match (Python parameter)"): [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")[CLOSEST] | [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")[BEFORE] | [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")[AFTER] | [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.13)")[EXACT] = `CLOSEST`*)

    getFrame(*\*[args](#abaqus.Odb.OdbStepBase.OdbStepBase.getFrame "abaqus.Odb.OdbStepBase.OdbStepBase.getFrame.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Odb.OdbStepBase.OdbStepBase.getFrame "abaqus.Odb.OdbStepBase.OdbStepBase.getFrame.kwargs (Python parameter)")*)

    getHistoryRegion(*[point](#abaqus.Odb.OdbStepBase.OdbStepBase.getHistoryRegion.point "abaqus.Odb.OdbStepBase.OdbStepBase.getHistoryRegion.point (Python parameter) — A HistoryPoint object specifying the point in the model.")*, *[loadCase=<abaqus.Odb.OdbLoadCase.OdbLoadCase object>](#abaqus.Odb.OdbStepBase.OdbStepBase.getHistoryRegion "abaqus.Odb.OdbStepBase.OdbStepBase.getHistoryRegion.loadCase=<abaqus.Odb.OdbLoadCase.OdbLoadCase object> (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L267-L287)[¶](#abaqus.Odb.OdbStepBase.OdbStepBase.getHistoryRegion "Permalink to this definition")
    :   This method retrieves a HistoryRegion object associated with a HistoryPoint in the model.

        Parameters:[¶](#abaqus.Odb.OdbStepBase.OdbStepBase.getHistoryRegion-parameters "Permalink to this headline")
        :   point[¶](#abaqus.Odb.OdbStepBase.OdbStepBase.getHistoryRegion.point "Permalink to this definition")
            :   A HistoryPoint object specifying the point in the model.

            loadCase : [`OdbLoadCase`](#abaqus.Odb.OdbStepBase.OdbLoadCase "abaqus.Odb.OdbLoadCase.OdbLoadCase (Python class)"), default: `<abaqus.Odb.OdbLoadCase.OdbLoadCase object at 0x7f850c72c650>`
            :   An OdbLoadCase object specifying a load case in the step.

        Returns:[¶](#abaqus.Odb.OdbStepBase.OdbStepBase.getHistoryRegion-returns "Permalink to this headline")
        :   A HistoryRegion object.

        Return type:[¶](#abaqus.Odb.OdbStepBase.OdbStepBase.getHistoryRegion-return-type "Permalink to this headline")
        :   [`HistoryRegion`](#abaqus.Odb.OdbStepBase.HistoryRegion "abaqus.Odb.OdbStepBase.HistoryRegion (Python class) — Bases: object")

        Raises:[¶](#abaqus.Odb.OdbStepBase.OdbStepBase.getHistoryRegion-raises "Permalink to this headline")
        :   **OdbError** – HistoryRegion not found, If a HistoryRegion object is not found.

    historyRegions : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Odb.HistoryRegion.HistoryRegion`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L46-L47)[¶](#abaqus.Odb.OdbStepBase.OdbStepBase.historyRegions "Permalink to this definition")
    :   A repository of HistoryRegion objects.

    inertiaAboutCenter : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L55-L59)[¶](#abaqus.Odb.OdbStepBase.OdbStepBase.inertiaAboutCenter "Permalink to this definition")
    :   A tuple of Floats specifying the moments and products of inertia about the center of
        mass. For 3-D models inertia quantities are written in the following order: I(XX),
        I(YY), I(ZZ), I(XY), I(XZ), and I(YZ). For 2-D models only I(ZZ) and I(XY) are
        outputted.

    inertiaAboutOrigin : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L61-L65)[¶](#abaqus.Odb.OdbStepBase.OdbStepBase.inertiaAboutOrigin "Permalink to this definition")
    :   A tuple of Floats specifying the moments and products of inertia about the origin of the
        global coordinate system. For 3-D models inertia quantities are written in the following
        order: I(XX), I(YY), I(ZZ), I(XY), I(XZ), and I(YZ). For 2-D models only I(ZZ) and I(XY)
        are outputted.

    loadCases : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Odb.OdbLoadCase.OdbLoadCase`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L49-L50)[¶](#abaqus.Odb.OdbStepBase.OdbStepBase.loadCases "Permalink to this definition")
    :   A repository of OdbLoadCase objects.

    mass : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L36-L38)[¶](#abaqus.Odb.OdbStepBase.OdbStepBase.mass "Permalink to this definition")
    :   A Float specifying the current value of the mass of the model. This does not include the
        mass of the acoustic media if any present.

    massCenter : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L52-L53)[¶](#abaqus.Odb.OdbStepBase.OdbStepBase.massCenter "Permalink to this definition")
    :   A tuple of Floats specifying the coordinates of the center of mass.

    nlgeom : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L33-L34)[¶](#abaqus.Odb.OdbStepBase.OdbStepBase.nlgeom "Permalink to this definition")
    :   A Boolean specifying whether geometric nonlinearity can occur in this step.

    number : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L30-L31)[¶](#abaqus.Odb.OdbStepBase.OdbStepBase.number "Permalink to this definition")
    :   An Int specifying the step number.

    setDefaultDeformedField(*[field](#abaqus.Odb.OdbStepBase.OdbStepBase.setDefaultDeformedField.field "abaqus.Odb.OdbStepBase.OdbStepBase.setDefaultDeformedField.field (Python parameter) — A FieldOutput object specifying the default deformed field variable for visualization.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L289-L298)[¶](#abaqus.Odb.OdbStepBase.OdbStepBase.setDefaultDeformedField "Permalink to this definition")
    :   This method sets the default deformed field variable in a step.

        Note

        Check [OdbStepBase.setDefaultDeformedField on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-steppyc.htm?contextscope=all#simaker-stepsetdefaultdeformedfieldpyc).

        Parameters:[¶](#abaqus.Odb.OdbStepBase.OdbStepBase.setDefaultDeformedField-parameters "Permalink to this headline")
        :   field[¶](#abaqus.Odb.OdbStepBase.OdbStepBase.setDefaultDeformedField.field "Permalink to this definition")
            :   A FieldOutput object specifying the default deformed field variable for visualization.

    setDefaultField(*[field](#abaqus.Odb.OdbStepBase.OdbStepBase.setDefaultField.field "abaqus.Odb.OdbStepBase.OdbStepBase.setDefaultField.field (Python parameter) — A FieldOutput object specifying the default field variable for visualization.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/OdbStepBase.py#L300-L309)[¶](#abaqus.Odb.OdbStepBase.OdbStepBase.setDefaultField "Permalink to this definition")
    :   This method sets the default field variable in a step.

        Note

        Check [OdbStepBase.setDefaultField on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-steppyc.htm?contextscope=all#simaker-stepsetdefaultfieldpyc).

        Parameters:[¶](#abaqus.Odb.OdbStepBase.OdbStepBase.setDefaultField-parameters "Permalink to this headline")
        :   field[¶](#abaqus.Odb.OdbStepBase.OdbStepBase.setDefaultField.field "Permalink to this definition")
            :   A FieldOutput object specifying the default field variable for visualization.

*class* RebarOrientation[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientationArray.py#L10-L35)[¶](#abaqus.Odb.RebarOrientationArray.RebarOrientation "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The RebarOrientation object represents the orientation of the rebar reference.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].parts[name].rebarOrientations[i]
    session.odbs[name].rootAssembly.instances[name].rebarOrientations[i]
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.rebarOrientations[i]
    ```

    Note

    Check [RebarOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-rebarorientationpyc.htm?contextscope=all).

    Member Details:

    angle : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientationArray.py#L28-L29)[¶](#abaqus.Odb.RebarOrientationArray.RebarOrientation.angle "Permalink to this definition")
    :   A Float specifying the angle of the additional rotation.

    axis : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientationArray.py)[¶](#abaqus.Odb.RebarOrientationArray.RebarOrientation.axis "Permalink to this definition")
    :   A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate
        system about which an additional rotation is applied. Possible values are AXIS\_1,
        AXIS\_2, and AXIS\_3.

    csys : --is-rst--:py:class:`~abaqus.Odb.OdbDatumCsys.OdbDatumCsys` = `<abaqus.Odb.OdbDatumCsys.OdbDatumCsys object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientationArray.py#L10-L35)[¶](#abaqus.Odb.RebarOrientationArray.RebarOrientation.csys "Permalink to this definition")
    :   An OdbDatumCsys object specifying a datum coordinates system.

    region : --is-rst--:py:class:`~abaqus.Odb.OdbSet.OdbSet` = `<abaqus.Odb.OdbSet.OdbSet object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/RebarOrientationArray.py#L31-L32)[¶](#abaqus.Odb.RebarOrientationArray.RebarOrientation.region "Permalink to this definition")
    :   An OdbSet object specifying a region for which the rebar orientation is defined.

*class* UserDataBase[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/UserDataBase.py#L10-L123)[¶](#abaqus.Odb.UserDataBase.UserDataBase "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The UserData object contains user-defined XY data. The UserData object has no constructor; it is created
    automatically when an Odb object is created.

    Note

    This object can be accessed by:

    ```python
    import odbAccess
    session.odbs[name].userData
    ```

    Note

    Check [UserDataBase on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-userdatapyc.htm?contextscope=all).

    Member Details:

    XYData(*[name](#abaqus.Odb.UserDataBase.UserDataBase.XYData.name "abaqus.Odb.UserDataBase.UserDataBase.XYData.name (Python parameter) — A String specifying the repository key.")*, *[data](#abaqus.Odb.UserDataBase.UserDataBase.XYData.data "abaqus.Odb.UserDataBase.UserDataBase.XYData.data (Python parameter) — A sequence of pairs of Floats specifying the X - Y data pairs.")*, *[sourceDescription](#abaqus.Odb.UserDataBase.UserDataBase.XYData.sourceDescription "abaqus.Odb.UserDataBase.UserDataBase.XYData.sourceDescription (Python parameter) — A String specifying the source of the X - Y data (e.g., “Entered from keyboard”, “Taken from ASCII file”, “Read from an ODB”, etc.).")=`''`*, *[contentDescription](#abaqus.Odb.UserDataBase.UserDataBase.XYData.contentDescription "abaqus.Odb.UserDataBase.UserDataBase.XYData.contentDescription (Python parameter) — A String specifying the content of the X - Y data (e.g., “field 1 vs.")=`''`*, *[positionDescription](#abaqus.Odb.UserDataBase.UserDataBase.XYData.positionDescription "abaqus.Odb.UserDataBase.UserDataBase.XYData.positionDescription (Python parameter) — A String specifying additional information about the X - Y data (e.g., “for whole model”).")=`''`*, *[legendLabel](#abaqus.Odb.UserDataBase.UserDataBase.XYData.legendLabel "abaqus.Odb.UserDataBase.UserDataBase.XYData.legendLabel (Python parameter) — A String specifying the label to be used in the legend.")=`''`*, *[xValuesLabel](#abaqus.Odb.UserDataBase.UserDataBase.XYData.xValuesLabel "abaqus.Odb.UserDataBase.UserDataBase.XYData.xValuesLabel (Python parameter) — A String specifying the label for the X-values.")=`''`*, *[yValuesLabel](#abaqus.Odb.UserDataBase.UserDataBase.XYData.yValuesLabel "abaqus.Odb.UserDataBase.UserDataBase.XYData.yValuesLabel (Python parameter) — A String specifying the label for the Y-values.")=`''`*, *[axis1QuantityType](#abaqus.Odb.UserDataBase.UserDataBase.XYData.axis1QuantityType "abaqus.Odb.UserDataBase.UserDataBase.XYData.axis1QuantityType (Python parameter) — A QuantityType object specifying the QuantityType object associated to the X -axis1- values.")=`None`*, *[axis2QuantityType](#abaqus.Odb.UserDataBase.UserDataBase.XYData.axis2QuantityType "abaqus.Odb.UserDataBase.UserDataBase.XYData.axis2QuantityType (Python parameter) — A QuantityType object specifying the QuantityType object associated to the Y -axis2- values.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/UserDataBase.py#L66-L123)[¶](#abaqus.Odb.UserDataBase.UserDataBase.XYData "Permalink to this definition")
    :   This method creates an XYData object from a sequence of **X - Y** data pairs.

        Note

        This function can be accessed by:

        ```python
        session.odbs[name].userData.XYData
        ```

        Note

        Check [XYData on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-xydatapyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Odb.UserDataBase.UserDataBase.XYData-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Odb.UserDataBase.UserDataBase.XYData.name "Permalink to this definition")
            :   A String specifying the repository key.

            data[¶](#abaqus.Odb.UserDataBase.UserDataBase.XYData.data "Permalink to this definition")
            :   A sequence of pairs of Floats specifying the **X - Y** data pairs.

            sourceDescription=`''`[¶](#abaqus.Odb.UserDataBase.UserDataBase.XYData.sourceDescription "Permalink to this definition")
            :   A String specifying the source of the **X - Y** data (e.g., “Entered from keyboard”, “Taken
                from ASCII file”, “Read from an ODB”, etc.). The default value is an empty string.

            contentDescription=`''`[¶](#abaqus.Odb.UserDataBase.UserDataBase.XYData.contentDescription "Permalink to this definition")
            :   A String specifying the content of the **X - Y** data (e.g., “field 1 vs. field 2”). The
                default value is an empty string.

            positionDescription=`''`[¶](#abaqus.Odb.UserDataBase.UserDataBase.XYData.positionDescription "Permalink to this definition")
            :   A String specifying additional information about the **X - Y** data (e.g., “for whole
                model”). The default value is an empty string.

            legendLabel=`''`[¶](#abaqus.Odb.UserDataBase.UserDataBase.XYData.legendLabel "Permalink to this definition")
            :   A String specifying the label to be used in the legend. The default value is the name of
                the XYData object.

            xValuesLabel=`''`[¶](#abaqus.Odb.UserDataBase.UserDataBase.XYData.xValuesLabel "Permalink to this definition")
            :   A String specifying the label for the X-values. This value may be overridden if the
                **X - Y** data are combined with other **X - Y** data. The default value is an empty string.

            yValuesLabel=`''`[¶](#abaqus.Odb.UserDataBase.UserDataBase.XYData.yValuesLabel "Permalink to this definition")
            :   A String specifying the label for the Y-values. This value may be overridden if the
                **X - Y** data are combined with other **X - Y** data. The default value is an empty string.

            axis1QuantityType=`None`[¶](#abaqus.Odb.UserDataBase.UserDataBase.XYData.axis1QuantityType "Permalink to this definition")
            :   A QuantityType object specifying the QuantityType object associated to the X -axis1-
                values.

            axis2QuantityType=`None`[¶](#abaqus.Odb.UserDataBase.UserDataBase.XYData.axis2QuantityType "Permalink to this definition")
            :   A QuantityType object specifying the QuantityType object associated to the Y -axis2-
                values.

        Returns:[¶](#abaqus.Odb.UserDataBase.UserDataBase.XYData-returns "Permalink to this headline")
        :   An XYData object.

        Return type:[¶](#abaqus.Odb.UserDataBase.UserDataBase.XYData-return-type "Permalink to this headline")
        :   [`XYData`](#abaqus.Odb.UserDataBase.UserDataBase.XYData "abaqus.Odb.UserDataBase.UserDataBase.XYData (Python method) — This method creates an XYData object from a sequence of X - Y data pairs.")

    annotations : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.Annotation.Annotation.Annotation`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/UserDataBase.py#L60-L61)[¶](#abaqus.Odb.UserDataBase.UserDataBase.annotations "Permalink to this definition")
    :   A repository of Annotation objects.

    axis1QuantityType : --is-rst--:py:class:`~abaqus.XY.QuantityType.QuantityType` = `<abaqus.XY.QuantityType.QuantityType object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/UserDataBase.py#L45-L47)[¶](#abaqus.Odb.UserDataBase.UserDataBase.axis1QuantityType "Permalink to this definition")
    :   A QuantityType object specifying the QuantityType object associated to the X -axis1-
        values.

    axis2QuantityType : --is-rst--:py:class:`~abaqus.XY.QuantityType.QuantityType` = `<abaqus.XY.QuantityType.QuantityType object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/UserDataBase.py#L49-L51)[¶](#abaqus.Odb.UserDataBase.UserDataBase.axis2QuantityType "Permalink to this definition")
    :   A QuantityType object specifying the QuantityType object associated to the Y -axis2-
        values.

    contentDescription : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/UserDataBase.py#L29-L31)[¶](#abaqus.Odb.UserDataBase.UserDataBase.contentDescription "Permalink to this definition")
    :   A String specifying the content of the **X - Y** data (e.g., “field 1 vs. field 2”). The
        default value is an empty string.

    data : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/UserDataBase.py#L63-L64)[¶](#abaqus.Odb.UserDataBase.UserDataBase.data "Permalink to this definition")
    :   A tuple of pairs of Floats specifying the **X - Y** data pairs.

    legendLabel : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/UserDataBase.py#L53-L55)[¶](#abaqus.Odb.UserDataBase.UserDataBase.legendLabel "Permalink to this definition")
    :   A String specifying the label to be used in the legend. The default value is the name of
        the XYData object.

    name : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/UserDataBase.py#L22-L23)[¶](#abaqus.Odb.UserDataBase.UserDataBase.name "Permalink to this definition")
    :   A String specifying the repository key.

    positionDescription : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/UserDataBase.py#L33-L35)[¶](#abaqus.Odb.UserDataBase.UserDataBase.positionDescription "Permalink to this definition")
    :   A String specifying additional information about the **X - Y** data (e.g., “for whole
        model”). The default value is an empty string.

    sourceDescription : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/UserDataBase.py#L25-L27)[¶](#abaqus.Odb.UserDataBase.UserDataBase.sourceDescription "Permalink to this definition")
    :   A String specifying the source of the **X - Y** data (e.g., “Entered from keyboard”, “Taken
        from ASCII file”, “Read from an ODB”, etc.). The default value is an empty string.

    xValuesLabel : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/UserDataBase.py#L37-L39)[¶](#abaqus.Odb.UserDataBase.UserDataBase.xValuesLabel "Permalink to this definition")
    :   A String specifying the label for the X-values. This value may be overridden if the
        **X - Y** data are combined with other **X - Y** data. The default value is an empty string.

    xyDataObjects : --is-rst--:py:class:`dict`\[:py:class:`str`, :py:class:`~abaqus.XY.XYData.XYData`] = `{}`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/UserDataBase.py#L57-L58)[¶](#abaqus.Odb.UserDataBase.UserDataBase.xyDataObjects "Permalink to this definition")
    :   A repository of XYData objects.

    yValuesLabel : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Odb/UserDataBase.py#L41-L43)[¶](#abaqus.Odb.UserDataBase.UserDataBase.yValuesLabel "Permalink to this definition")
    :   A String specifying the label for the Y-values. This value may be overridden if the
        **X - Y** data are combined with other **X - Y** data. The default value is an empty string.

[Back to top](#)