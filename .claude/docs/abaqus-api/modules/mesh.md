# Abaqus MESH Module API Reference

> Source: [https://hailin.wang/abqpy/en/2025/reference/mdb/model/mesh.html](https://hailin.wang/abqpy/en/2025/reference/mdb/model/mesh.html)
> Downloaded for offline use by Claude Code skills.

---

# Mesh[¶](#mesh "Permalink to this heading")

Mesh commands are used to mesh part instances and regions. Mesh commands are also used to assign element sizes, element types, and mesh control parameters.

## Other Classes[¶](#other-classes "Permalink to this heading")

*class* ElemType(*[elemCode](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.elemCode (Python parameter)")*, *[elemLibrary](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.elemLibrary (Python parameter)")=`abaqusConstants.STANDARD`*, *[hourglassStiffness](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.hourglassStiffness (Python parameter)")=`0`*, *[bendingHourglass](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.bendingHourglass (Python parameter)")=`0`*, *[drillingHourglass](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.drillingHourglass (Python parameter)")=`0`*, *[kinematicSplit](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.kinematicSplit (Python parameter)")=`abaqusConstants.AVERAGE_STRAIN`*, *[distortionControl](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.distortionControl (Python parameter)")=`0`*, *[lengthRatio](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.lengthRatio (Python parameter)")=`1`*, *[secondOrderAccuracy](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.secondOrderAccuracy (Python parameter)")=`0`*, *[hourglassControl](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.hourglassControl (Python parameter)")=`abaqusConstants.ENHANCED`*, *[weightFactor](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.weightFactor (Python parameter)")=`0`*, *[displacementHourglass](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.displacementHourglass (Python parameter)")=`1`*, *[rotationalHourglass](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.rotationalHourglass (Python parameter)")=`1`*, *[outOfPlaneDisplacementHourglass](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.outOfPlaneDisplacementHourglass (Python parameter)")=`1`*, *[elemDeletion](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.elemDeletion (Python parameter)")=`abaqusConstants.DEFAULT`*, *[particleConversion](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.particleConversion (Python parameter)")=`abaqusConstants.DEFAULT`*, *[particleConversionThreshold](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.particleConversionThreshold (Python parameter)")=`0`*, *[particleConversionPPD](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.particleConversionPPD (Python parameter)")=`1`*, *[particleConversionKernel](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.particleConversionKernel (Python parameter)")=`abaqusConstants.CUBIC`*, *[maxDegradation](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.maxDegradation (Python parameter)")=`None`*, *[viscosity](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.viscosity (Python parameter)")=`0`*, *[linearBulkViscosity](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.linearBulkViscosity (Python parameter)")=`1`*, *[quadraticBulkViscosity](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.quadraticBulkViscosity (Python parameter)")=`1`*, *[numFourierModes](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.numFourierModes (Python parameter)")=`1`*, *[nodeOffset](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.nodeOffset (Python parameter)")=`None`*, *[linearKinematicCtrl](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.linearKinematicCtrl (Python parameter)")=`None`*, *[initialGapOpening](#abaqus.Mesh.MeshPart.ElemType "abaqus.Mesh.MeshPart.ElemType.__init__.initialGapOpening (Python parameter)")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L24-L353)[¶](#abaqus.Mesh.MeshPart.ElemType "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The ElemType object is an argument object used as an argument in the setElementType command.

    Note

    This object can be accessed by:

    ```python
    import mesh
    ```

    Note

    Check [ElemType on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-elemtypepyc.htm?contextscope=all).

    Member Details:

    bendingHourglass : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L57-L60)[¶](#abaqus.Mesh.MeshPart.ElemType.bendingHourglass "Permalink to this definition")
    :   A Float specifying the bending hourglass stiffness. A value of zero indicates the
        default value should be used. The default value will be used where appropriate. The
        default value is 0.0.This argument is applicable only to some Abaqus/Standard elements.

    displacementHourglass : --is-rst--:py:class:`float` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L95-L98)[¶](#abaqus.Mesh.MeshPart.ElemType.displacementHourglass "Permalink to this definition")
    :   A Float specifying the displacement hourglass scaling factor. The default value will be
        used where appropriate. The default value is 1.0.This argument is applicable only to
        some Abaqus/Explicit elements.

    distortionControl : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L72-L75)[¶](#abaqus.Mesh.MeshPart.ElemType.distortionControl "Permalink to this definition")
    :   A Boolean specifying whether to prevent negative element volumes or other excessive
        distortions in crushable materials. The default value is OFF.This argument is applicable
        only to some Abaqus/Explicit elements.

    drillingHourglass : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L62-L65)[¶](#abaqus.Mesh.MeshPart.ElemType.drillingHourglass "Permalink to this definition")
    :   A Float specifying the drilling hourglass scaling factor. A value of zero indicates the
        default value should be used. The default value will be used where appropriate. The
        default value is 0.0.This argument is applicable only to some Abaqus/Standard elements.

    elemCode : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py)[¶](#abaqus.Mesh.MeshPart.ElemType.elemCode "Permalink to this definition")
    :   A SymbolicConstant specifying the Abaqus element code or just the element shape.
        Possible values are:

        * C3D8R, specifying a 8-node linear brick, reduced integration with hourglass control.
        * CODE, specifying add more codes.
        * UNKNOWN\_TRI, specifying an unknown element type associated with a triangular shape.
        * UNKNOWN\_QUAD, specifying an unknown element type associated with a quadrilateral
          shape.
        * UNKNOWN\_HEX, specifying an unknown element type associated with a hexahedral shape.
        * UNKNOWN\_WEDGE, specifying an unknown element type associated with a wedge shape.
        * UNKNOWN\_TET, specifying an unknown element type associated with a tetrahedral shape.

    elemDeletion : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'DEFAULT'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L110-L112)[¶](#abaqus.Mesh.MeshPart.ElemType.elemDeletion "Permalink to this definition")
    :   A SymbolicConstant specifying the element deletion option. Possible values are DEFAULT,
        ON, and OFF. The default value is DEFAULT.

    elemLibrary : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'STANDARD'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L47-L49)[¶](#abaqus.Mesh.MeshPart.ElemType.elemLibrary "Permalink to this definition")
    :   A SymbolicConstant specifying the Abaqus element library to use. Possible values are
        STANDARD and EXPLICIT. The default value is STANDARD.

    hourglassControl : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'ENHANCED'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L86-L89)[¶](#abaqus.Mesh.MeshPart.ElemType.hourglassControl "Permalink to this definition")
    :   A SymbolicConstant specifying the hourglass control. Possible values are
        RELAX\_STIFFNESS, STIFFNESS, VISCOUS, ENHANCED, and COMBINED. The default value is
        ENHANCED.This argument is applicable only to some Abaqus/Explicit elements.

    hourglassStiffness : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L51-L55)[¶](#abaqus.Mesh.MeshPart.ElemType.hourglassStiffness "Permalink to this definition")
    :   A Float specifying the hourglass stiffness. (For shell elements this is the membrane
        hourglass stiffness.) A value of zero indicates the default value should be used. The
        default value will be used where appropriate. The default value is 0.0.This argument is
        applicable only to some Abaqus/Standard elements.

    initialGapOpening : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L172-L174)[¶](#abaqus.Mesh.MeshPart.ElemType.initialGapOpening "Permalink to this definition")
    :   A Float specifying the initial gap opening.This parameter is applicable only to some
        Abaqus/Standard elements.

        New in version 2022: The `initialGapOpening` attribute was added.

    kinematicSplit : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'AVERAGE_STRAIN'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L67-L70)[¶](#abaqus.Mesh.MeshPart.ElemType.kinematicSplit "Permalink to this definition")
    :   A SymbolicConstant specifying the kinematic split control. Possible values are
        AVERAGE\_STRAIN, ORTHOGONAL, and CENTROID. The default value is AVERAGE\_STRAIN.This
        argument is applicable only to some Abaqus/Explicit elements.

    lengthRatio : --is-rst--:py:class:`float` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L77-L80)[¶](#abaqus.Mesh.MeshPart.ElemType.lengthRatio "Permalink to this definition")
    :   A Float specifying the length ratio for distortion control in crushable materials.
        Possible values are 0.0 ≤ **lengthRatio** ≤ 1.0. The default value is
        **lengthRatio** = 0.10.1This argument is applicable only when **distortionControl** is ON.

    linearBulkViscosity : --is-rst--:py:class:`float` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L145-L147)[¶](#abaqus.Mesh.MeshPart.ElemType.linearBulkViscosity "Permalink to this definition")
    :   A Float specifying the linear bulk viscosity scaling factor option for Abaqus/Explicit.
        The default value is 1.0.

    linearKinematicCtrl : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L172-L174)[¶](#abaqus.Mesh.MeshPart.ElemType.linearKinematicCtrl "Permalink to this definition")
    :   A Float specifying the linear kinematic conversion value.This argument is applicable
        only to some Abaqus/Explicit elements.

        New in version 2022: The `linearKinematicCtrl` attribute was added.

    maxDegradation : --is-rst--:py:data:`~typing.Optional`\[:py:class:`float`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L137-L139)[¶](#abaqus.Mesh.MeshPart.ElemType.maxDegradation "Permalink to this definition")
    :   A Float specifying the maximum degradation option for damage control. The default value
        is −1.0.

    nodeOffset : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L157-L159)[¶](#abaqus.Mesh.MeshPart.ElemType.nodeOffset "Permalink to this definition")
    :   An Int specifying the positive offset number for specifying the additional nodes needed
        in the connectivity.This argument is applicable only for axisymmetric elements with
        nonlinear asymmetric deformation.

        New in version 2019: The `nodeOffset` attribute was added.

    numFourierModes : --is-rst--:py:class:`int` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L157-L159)[¶](#abaqus.Mesh.MeshPart.ElemType.numFourierModes "Permalink to this definition")
    :   An Int specifying the number of Fourier modes. Possible values are 1, 2, 3, and 4. The
        default value is 1.This argument is applicable only for axisymmetric elements with
        nonlinear asymmetric deformation.

        New in version 2019: The `numFourierModes` attribute was added.

    outOfPlaneDisplacementHourglass : --is-rst--:py:class:`float` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L105-L108)[¶](#abaqus.Mesh.MeshPart.ElemType.outOfPlaneDisplacementHourglass "Permalink to this definition")
    :   A Float specifying the out-of-plane displacement hourglass scaling factor. The default
        value will be used where appropriate. The default value is 1.0.This argument is
        applicable only to some Abaqus/Explicit elements.

    particleConversion : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'DEFAULT'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L114-L119)[¶](#abaqus.Mesh.MeshPart.ElemType.particleConversion "Permalink to this definition")
    :   A SymbolicConstant specifying the particle conversion option for smoothed particle
        hydrodynamics. When not OFF or DEFAULT this argument refers to the criterion used for
        conversion of elements to particles. Possible values are DEFAULT, OFF, TIME, STRAIN, and
        STRESS. The default value is DEFAULT.This argument is applicable only to some
        Abaqus/Explicit elements.

    particleConversionKernel : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'CUBIC'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L131-L135)[¶](#abaqus.Mesh.MeshPart.ElemType.particleConversionKernel "Permalink to this definition")
    :   A SymbolicConstant specifying the interpolation function for particle conversion when
        **particleConversion** is specified. Possible values are CUBIC, QUADRATIC, and QUINTIC.
        The default value is CUBIC.This argument is applicable only to some Abaqus/Explicit
        elements.

    particleConversionPPD : --is-rst--:py:class:`int` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L126-L129)[¶](#abaqus.Mesh.MeshPart.ElemType.particleConversionPPD "Permalink to this definition")
    :   An Int specifying the number of particles per direction for element conversion when
        **particleConversion** is specified. The default value is 1.This argument is applicable
        only to some Abaqus/Explicit elements.

    particleConversionThreshold : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L121-L124)[¶](#abaqus.Mesh.MeshPart.ElemType.particleConversionThreshold "Permalink to this definition")
    :   A Float specifying the threshold value for the particle conversion criterion specified
        by **particleConversion**. The default value is 0.0.This argument is applicable only to
        some Abaqus/Explicit elements.

    quadraticBulkViscosity : --is-rst--:py:class:`float` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L149-L151)[¶](#abaqus.Mesh.MeshPart.ElemType.quadraticBulkViscosity "Permalink to this definition")
    :   A Float specifying the quadratic bulk viscosity scaling factor option for
        Abaqus/Explicit. The default value is 1.0.

    rotationalHourglass : --is-rst--:py:class:`float` = `1`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L100-L103)[¶](#abaqus.Mesh.MeshPart.ElemType.rotationalHourglass "Permalink to this definition")
    :   A Float specifying the rotational hourglass scaling factor. The default value will be
        used where appropriate. The default value is 1.0.This argument is applicable only to
        some Abaqus/Explicit elements.

    secondOrderAccuracy : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L82-L84)[¶](#abaqus.Mesh.MeshPart.ElemType.secondOrderAccuracy "Permalink to this definition")
    :   A Boolean specifying the second-order accuracy option. The default value is OFF.This
        argument is applicable only to some Abaqus/Explicit elements.

    viscosity : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L141-L143)[¶](#abaqus.Mesh.MeshPart.ElemType.viscosity "Permalink to this definition")
    :   A Float specifying the viscosity option. The default value is 0.0.This argument is
        applicable only to some Abaqus/Standard elements.

    weightFactor : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L91-L93)[¶](#abaqus.Mesh.MeshPart.ElemType.weightFactor "Permalink to this definition")
    :   A Float specifying a weight factor when **hourglassControl** = COMBINED. The default value
        is 0.5.This argument is applicable only to some Abaqus/Explicit elements.

*class* MeshAssembly[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L24-L1168)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly "Permalink to this definition")
:   Bases: [`AssemblyBase`](part_assembly/assembly.html#abaqus.Assembly.AssemblyBase.AssemblyBase "abaqus.Assembly.AssemblyBase.AssemblyBase (Python class) — Bases: AssemblyFeature")

    An Assembly object is a container for instances of parts. The Assembly object has no constructor command.
    Abaqus creates the **rootAssembly** member when a Model object is created.

    Note

    This object can be accessed by:

    ```python
    import assembly
    mdb.models[name].rootAssembly
    ```

    Note

    Check [MeshAssembly on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all).

    Member Details:

    assignStackDirection(*[cells](#abaqus.Mesh.MeshAssembly.MeshAssembly.assignStackDirection.cells "abaqus.Mesh.MeshAssembly.MeshAssembly.assignStackDirection.cells (Python parameter) — A sequence of Cell objects specifying regions where to assign the stack direction.")*, *[referenceRegion](#abaqus.Mesh.MeshAssembly.MeshAssembly.assignStackDirection.referenceRegion "abaqus.Mesh.MeshAssembly.MeshAssembly.assignStackDirection.referenceRegion (Python parameter) — A Face object specifying the top side of the stack direction.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L36-L48)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.assignStackDirection "Permalink to this definition")
    :   This method assigns a stack direction to geometric cells. The stack direction will be used to orient
        the elements during mesh generation.

        Note

        Check [MeshAssembly.assignStackDirection on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblyassignstackdirectionpyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.assignStackDirection-parameters "Permalink to this headline")
        :   cells[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.assignStackDirection.cells "Permalink to this definition")
            :   A sequence of Cell objects specifying regions where to assign the stack direction.

            referenceRegion[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.assignStackDirection.referenceRegion "Permalink to this definition")
            :   A Face object specifying the top side of the stack direction.

    associateMeshWithGeometry(*[geometricEntity](#abaqus.Mesh.MeshAssembly.MeshAssembly.associateMeshWithGeometry.geometricEntity "abaqus.Mesh.MeshAssembly.MeshAssembly.associateMeshWithGeometry.geometricEntity (Python parameter) — A Cell , a Face, an Edge, or a ConstrainedSketchVertex object specifying geometric entity to be associated with one or more mesh entities.If the geometric entity is a Cell object then the argument elements must be specified.If the geometric entity is a Face object then the argument elemFaces must be specified.If the geometric entity is an Edge object then the argument elemEdges must be specified.If the geometric entity is a ConstrainedSketchVertex object then the argument node must be specified.")*, *elements=()*, *elemFaces=()*, *elemEdges=()*, *[node=<abaqus.Mesh.MeshNode.MeshNode object>](#abaqus.Mesh.MeshAssembly.MeshAssembly.associateMeshWithGeometry "abaqus.Mesh.MeshAssembly.MeshAssembly.associateMeshWithGeometry.node=<abaqus.Mesh.MeshNode.MeshNode object> (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L50-L83)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.associateMeshWithGeometry "Permalink to this definition")
    :   This method associates a geometric entity with mesh entities that are either orphan elements, bounds
        orphan elements, or were created using the bottom-up meshing technique.

        Note

        Check [MeshAssembly.associateMeshWithGeometry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblyassociatemeshwithgeometrypyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.associateMeshWithGeometry-parameters "Permalink to this headline")
        :   geometricEntity[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.associateMeshWithGeometry.geometricEntity "Permalink to this definition")
            :   A Cell , a Face, an Edge, or a ConstrainedSketchVertex object specifying geometric entity to be
                associated with one or more mesh entities.If the geometric entity is a Cell object then
                the argument **elements** must be specified.If the geometric entity is a Face object then
                the argument **elemFaces** must be specified.If the geometric entity is an Edge object
                then the argument **elemEdges** must be specified.If the geometric entity is a ConstrainedSketchVertex
                object then the argument **node** must be specified.

            elements : [`Sequence`](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.13)")[[`MeshElement`](#abaqus.Mesh.MeshPart.MeshElement "abaqus.Mesh.MeshElement.MeshElement (Python class)")], default: `()`
            :   A sequence of MeshElement objects specifying the elements to be associated with the
                geometric cell.

            elemFaces : [`Sequence`](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.13)")[[`MeshFace`](#abaqus.Mesh.MeshPart.MeshFace "abaqus.Mesh.MeshFace.MeshFace (Python class)")], default: `()`
            :   A sequence of MeshFace objects specifying the element faces to be associated with the
                geometric face.

            elemEdges : [`Sequence`](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.13)")[[`MeshEdge`](#abaqus.Mesh.MeshPart.MeshEdge "abaqus.Mesh.MeshEdge.MeshEdge (Python class)")], default: `()`
            :   A sequence of MeshEdge objects specifying the element edges to be associated with the
                geometric edge.

            node : [`MeshNode`](#abaqus.Mesh.MeshPart.MeshNode "abaqus.Mesh.MeshNode.MeshNode (Python class)"), default: `<abaqus.Mesh.MeshNode.MeshNode object at 0x7f850c68f250>`
            :   A MeshNode object specifying the mesh node to be associated with the geometric vertex.

    createVirtualTopology(*[regions](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.regions "abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.regions (Python parameter) — A sequence of Face objects or PartInstance objects specifying the domain to search for geometric entities that need to be merged.")*, *[mergeShortEdges](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.mergeShortEdges "abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.mergeShortEdges (Python parameter) — A Boolean specifying whether to merge short edges.")=`False`*, *[shortEdgeThreshold](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.shortEdgeThreshold "abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.shortEdgeThreshold (Python parameter) — A Float specifying a threshold that determines which edges are considered to be short. These edges are the candidate entities to be merged.")=`None`*, *[mergeSmallFaces](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.mergeSmallFaces "abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.mergeSmallFaces (Python parameter) — A Boolean specifying whether to merge faces with small area.")=`False`*, *[smallFaceAreaThreshold](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.smallFaceAreaThreshold "abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.smallFaceAreaThreshold (Python parameter) — A Float specifying a threshold that determines which faces are considered to have a small area.")=`None`*, *[mergeSliverFaces](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.mergeSliverFaces "abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.mergeSliverFaces (Python parameter) — A Boolean specifying whether to merge faces with high aspect ratio.")=`False`*, *[faceAspectRatioThreshold](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.faceAspectRatioThreshold "abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.faceAspectRatioThreshold (Python parameter) — A Float specifying a threshold that determines which faces are considered to have high aspect ratio.")=`None`*, *[mergeSmallAngleFaces](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.mergeSmallAngleFaces "abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.mergeSmallAngleFaces (Python parameter) — A Boolean specifying whether to merge faces that have a sharp corner angle.")=`False`*, *[smallFaceCornerAngleThreshold](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.smallFaceCornerAngleThreshold "abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.smallFaceCornerAngleThreshold (Python parameter) — A Float specifying a threshold that determines which face corner angles are considered to be small.")=`None`*, *[mergeThinStairFaces](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.mergeThinStairFaces "abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.mergeThinStairFaces (Python parameter) — A Boolean specifying whether to merge faces that represent a thin stair-like feature. The default value is False.")=`False`*, *[thinStairFaceThreshold](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.thinStairFaceThreshold "abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.thinStairFaceThreshold (Python parameter) — A Float specifying a threshold that determines which faces representing small stair-like features are considered thin.")=`None`*, *[ignoreRedundantEntities](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.ignoreRedundantEntities "abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.ignoreRedundantEntities (Python parameter) — A Boolean specifying whether to abstract away redundant edges and vertices.")=`False`*, *[cornerAngleTolerance](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.cornerAngleTolerance "abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.cornerAngleTolerance (Python parameter) — A Float specifying the angle deviation from 180 degrees at a vertex or at an edge such that the two edges radiating from the vertex or the two faces bounded by the edge can be merged.")=`30`*, *[applyBlendControls](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.applyBlendControls "abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.applyBlendControls (Python parameter) — A Boolean specifying whether to verify that blend faces can be merged with neighboring faces.")=`False`*, *[blendSubtendedAngleTolerance](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.blendSubtendedAngleTolerance "abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.blendSubtendedAngleTolerance (Python parameter) — A Float specifying the largest subtended angle of blend faces that can be merged with neighboring faces.")=`None`*, *[blendRadiusTolerance](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.blendRadiusTolerance "abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.blendRadiusTolerance (Python parameter) — A Float specifying the smallest radius of curvature of blend faces that can be merged with neighboring faces.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L85-L182)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology "Permalink to this definition")
    :   This method creates a virtual topology feature by automatically merging faces and edges based on a
        set of geometric parameters. The edges and vertices that are being merged will be ignored during mesh
        generation.

        Note

        Check [MeshAssembly.createVirtualTopology on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblycreatevirtualtopologypyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology-parameters "Permalink to this headline")
        :   regions[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.regions "Permalink to this definition")
            :   A sequence of Face objects or PartInstance objects specifying the domain to search for
                geometric entities that need to be merged. Entities identified as candidates to be
                merged may be merged with entities from outside the specified region.

            mergeShortEdges=`False`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.mergeShortEdges "Permalink to this definition")
            :   A Boolean specifying whether to merge short edges. The default value is False.

            shortEdgeThreshold=`None`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.shortEdgeThreshold "Permalink to this definition")
            :   A Float specifying a threshold that determines which edges are considered to be short.
                These edges are the candidate entities to be merged. This argument is a required
                argument if the argument **mergeShortEdges** equals True and it is ignored if the argument
                **mergeShortEdges** equals False.

            mergeSmallFaces=`False`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.mergeSmallFaces "Permalink to this definition")
            :   A Boolean specifying whether to merge faces with small area. The default value is False.

            smallFaceAreaThreshold=`None`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.smallFaceAreaThreshold "Permalink to this definition")
            :   A Float specifying a threshold that determines which faces are considered to have a
                small area. These faces are the candidate entities to be merged. This argument is a
                required argument if the argument **mergeSmallFaces** equals True and it is ignored if the
                argument **mergeSmallFaces** equals False.

            mergeSliverFaces=`False`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.mergeSliverFaces "Permalink to this definition")
            :   A Boolean specifying whether to merge faces with high aspect ratio. The default value is
                False.

            faceAspectRatioThreshold=`None`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.faceAspectRatioThreshold "Permalink to this definition")
            :   A Float specifying a threshold that determines which faces are considered to have high
                aspect ratio. These faces are candidate entities to be merged. This argument is a
                required argument if the argument **mergeSliverFaces** equals True and it is ignored if
                the argument **mergeSliverFaces** equals False.

            mergeSmallAngleFaces=`False`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.mergeSmallAngleFaces "Permalink to this definition")
            :   A Boolean specifying whether to merge faces that have a sharp corner angle. The default
                value is False.

            smallFaceCornerAngleThreshold=`None`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.smallFaceCornerAngleThreshold "Permalink to this definition")
            :   A Float specifying a threshold that determines which face corner angles are considered
                to be small. These faces will be candidate entities to be merged. This argument is a
                required argument if the argument **mergeSmallAngleFaces** equals True and it is ignored
                if the argument **mergeSmallAngleFaces** equals False.

            mergeThinStairFaces=`False`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.mergeThinStairFaces "Permalink to this definition")
            :   A Boolean specifying whether to merge faces that represent a thin stair-like feature.
                The default value is False.

            thinStairFaceThreshold=`None`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.thinStairFaceThreshold "Permalink to this definition")
            :   A Float specifying a threshold that determines which faces representing small stair-like
                features are considered thin. These faces will be candidate entities to be merged. This
                argument is required if the argument **mergeThinStairFaces** is True and it is ignored if
                **mergeThinStairFaces** is False.

            ignoreRedundantEntities=`False`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.ignoreRedundantEntities "Permalink to this definition")
            :   A Boolean specifying whether to abstract away redundant edges and vertices. The default
                value is False.

            cornerAngleTolerance=`30`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.cornerAngleTolerance "Permalink to this definition")
            :   A Float specifying the angle deviation from 180 degrees at a vertex or at an edge such
                that the two edges radiating from the vertex or the two faces bounded by the edge can be
                merged. The default value is 30.0 degrees.

            applyBlendControls=`False`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.applyBlendControls "Permalink to this definition")
            :   A Boolean specifying whether to verify that blend faces can be merged with neighboring
                faces. If **applyBlendControls** is True then all faces that have angle larger than
                **blendSubtendedAngleTolerance** and a radius smaller than **blendRadiusTolerance** will not
                be merged with neighboring faces unless the neighboring faces are also blend faces with
                similar geometric characteristics. The default value is False.

            blendSubtendedAngleTolerance=`None`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.blendSubtendedAngleTolerance "Permalink to this definition")
            :   A Float specifying the largest subtended angle of blend faces that can be merged with
                neighboring faces. This argument is a required argument if the argument
                **applyBlendControls** equals True and it is ignored if the argument **applyBlendControls**
                equals False.

            blendRadiusTolerance=`None`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology.blendRadiusTolerance "Permalink to this definition")
            :   A Float specifying the smallest radius of curvature of blend faces that can be merged
                with neighboring faces. This argument is a required argument if the argument
                **applyBlendControls** equals True and it is ignored if the argument **applyBlendControls**
                equals False.

        Returns:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.createVirtualTopology-return-type "Permalink to this headline")
        :   `Feature`

    deleteBoundaryLayerControls(*[regions](#abaqus.Mesh.MeshAssembly.MeshAssembly.deleteBoundaryLayerControls.regions "abaqus.Mesh.MeshAssembly.MeshAssembly.deleteBoundaryLayerControls.regions (Python parameter) — A sequence of Cell objects specifying the regions for which to set the boundary layer mesh control parameters.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L184-L194)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.deleteBoundaryLayerControls "Permalink to this definition")
    :   This method deletes the control parameters for boundary layer mesh for all the specified regions.

        Note

        Check [MeshAssembly.deleteBoundaryLayerControls on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblydeleteboundarylayercontrolspyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.deleteBoundaryLayerControls-parameters "Permalink to this headline")
        :   regions[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.deleteBoundaryLayerControls.regions "Permalink to this definition")
            :   A sequence of Cell objects specifying the regions for which to set the boundary layer
                mesh control parameters.

    deleteMesh(*[regions](#abaqus.Mesh.MeshAssembly.MeshAssembly.deleteMesh.regions "abaqus.Mesh.MeshAssembly.MeshAssembly.deleteMesh.regions (Python parameter) — A sequence of PartInstance objects or Region objects specifying the part instances or regions from where the native mesh is to be deleted.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L196-L207)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.deleteMesh "Permalink to this definition")
    :   This method deletes a subset of the mesh that contains the native elements from the given part
        instances or regions.

        Note

        Check [MeshAssembly.deleteMesh on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblydeletemeshpyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.deleteMesh-parameters "Permalink to this headline")
        :   regions[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.deleteMesh.regions "Permalink to this definition")
            :   A sequence of PartInstance objects or Region objects specifying the part instances or
                regions from where the native mesh is to be deleted.

    deleteMeshAssociationWithGeometry(*[geometricEntities](#abaqus.Mesh.MeshAssembly.MeshAssembly.deleteMeshAssociationWithGeometry.geometricEntities "abaqus.Mesh.MeshAssembly.MeshAssembly.deleteMeshAssociationWithGeometry.geometricEntities (Python parameter) — A sequence of Cell objects, Face objects, Edge objects, or ConstrainedSketchVertex objects specifying the geometric entities that will be disassociated from the mesh.")*, *[addBoundingEntities](#abaqus.Mesh.MeshAssembly.MeshAssembly.deleteMeshAssociationWithGeometry.addBoundingEntities "abaqus.Mesh.MeshAssembly.MeshAssembly.deleteMeshAssociationWithGeometry.addBoundingEntities (Python parameter) — A Boolean specifying whether the mesh will also be disassociated from the geometric entities that bounds the given geometricEntities.")=`False`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L209-L227)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.deleteMeshAssociationWithGeometry "Permalink to this definition")
    :   This method deletes the association of geometric entities with mesh entities.

        Note

        Check [MeshAssembly.deleteMeshAssociationWithGeometry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblydeletemeshassociationwithgeometrypyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.deleteMeshAssociationWithGeometry-parameters "Permalink to this headline")
        :   geometricEntities[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.deleteMeshAssociationWithGeometry.geometricEntities "Permalink to this definition")
            :   A sequence of Cell objects, Face objects, Edge objects, or ConstrainedSketchVertex objects specifying the
                geometric entities that will be disassociated from the mesh.

            addBoundingEntities=`False`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.deleteMeshAssociationWithGeometry.addBoundingEntities "Permalink to this definition")
            :   A Boolean specifying whether the mesh will also be disassociated from the geometric
                entities that bounds the given **geometricEntities**. For example, if the argument
                **geometricEntities** contains a face, this boolean indicates whether the edges and
                vertices that bound the face will also be disassociated from the mesh. The default value
                is False.

    deletePreviewMesh()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L229-L236)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.deletePreviewMesh "Permalink to this definition")
    :   This method deletes all boundary meshes in the assembly.

        See the **boundaryPreview** argument of generateMesh for information about generating boundary
        meshes.

    deleteSeeds(*[regions](#abaqus.Mesh.MeshAssembly.MeshAssembly.deleteSeeds.regions "abaqus.Mesh.MeshAssembly.MeshAssembly.deleteSeeds.regions (Python parameter) — A sequence of PartInstance objects or Edge objects specifying the part instances or edges from which the seeds are to be deleted.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L238-L249)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.deleteSeeds "Permalink to this definition")
    :   This method deletes the global edge seeds from the given part instances or deletes the local edge
        seeds from the given edges.

        Note

        Check [MeshAssembly.deleteSeeds on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblydeleteseedspyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.deleteSeeds-parameters "Permalink to this headline")
        :   regions[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.deleteSeeds.regions "Permalink to this definition")
            :   A sequence of PartInstance objects or Edge objects specifying the part instances or
                edges from which the seeds are to be deleted.

    generateBottomUpExtrudedMesh(*[cell](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.cell "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.cell (Python parameter) — A Cell object specifying the geometric region where the mesh is to be generated.")*, *[numberOfLayers](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.numberOfLayers "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.numberOfLayers (Python parameter) — An Int specifying the number of layers to be generated along the extrusion vector.")*, *[extrudeVector](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.extrudeVector "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.extrudeVector (Python parameter) — A sequence of sequences of Floats specifying the start point and end point of a vector. Each point is defined by a tuple of three coordinates indicating its position.")*, *[geometrySourceSide](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.geometrySourceSide "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.geometrySourceSide (Python parameter) — A Region of Face objects specifying the geometric domain to be used as the source for the extrude meshing operation.")=`''`*, *[elemFacesSourceSide](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.elemFacesSourceSide "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.elemFacesSourceSide (Python parameter) — A sequence of MeshFace objects specifying the faces of 3D elements to be used as the source for the extrude meshing operation.")=`()`*, *[elemSourceSide](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.elemSourceSide "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.elemSourceSide (Python parameter) — A sequence of 2D MeshElement objects specifying the elements to be used as the source for the extrude meshing operation.")=`()`*, *[depth](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.depth "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.depth (Python parameter) — A Float specifying the distance of the mesh extrusion.")=`None`*, *[targetSide](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.targetSide "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.targetSide (Python parameter) — A datum plane, a sequence of Face objects, a sequence of MeshFace objects, or a sequence of 2D MeshElement objects specifying the target of the extrude meshing operation.")=`''`*, *[biasRatio](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.biasRatio "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.biasRatio (Python parameter) — A Float specifying a ratio of the element size in the extrusion direction between the source and the target sides of the extrusion.")=`1`*, *[extendElementSets](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.extendElementSets "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.extendElementSets (Python parameter) — A Boolean specifying whether existing element sets that include source elements will be extended to also include extruded elements.")=`False`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L251-L304)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh "Permalink to this definition")
    :   This method generates solid elements by extruding a 2D mesh along a vector, either on an orphan mesh
        or within a cell region using a bottom-up technique.

        Note

        Check [MeshAssembly.generateBottomUpExtrudedMesh on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblygeneratebottomupextrudedmeshpyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh-parameters "Permalink to this headline")
        :   cell[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.cell "Permalink to this definition")
            :   A Cell object specifying the geometric region where the mesh is to be generated. This
                argument is valid only for native part instances.

            numberOfLayers[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.numberOfLayers "Permalink to this definition")
            :   An Int specifying the number of layers to be generated along the extrusion vector.

            extrudeVector[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.extrudeVector "Permalink to this definition")
            :   A sequence of sequences of Floats specifying the start point and end point of a vector.
                Each point is defined by a tuple of three coordinates indicating its position. The
                direction of the mesh extrusion operation is from the first point to the second point.

            geometrySourceSide=`''`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.geometrySourceSide "Permalink to this definition")
            :   A Region of Face objects specifying the geometric domain to be used as the source for
                the extrude meshing operation.

            elemFacesSourceSide=`()`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.elemFacesSourceSide "Permalink to this definition")
            :   A sequence of MeshFace objects specifying the faces of 3D elements to be used as the
                source for the extrude meshing operation.

            elemSourceSide=`()`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.elemSourceSide "Permalink to this definition")
            :   A sequence of 2D MeshElement objects specifying the elements to be used as the source
                for the extrude meshing operation.

            depth=`None`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.depth "Permalink to this definition")
            :   A Float specifying the distance of the mesh extrusion. If unspecified, the vector length
                of the **extrudeVector** argument is assumed.

            targetSide=`''`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.targetSide "Permalink to this definition")
            :   A datum plane, a sequence of Face objects, a sequence of MeshFace objects, or a sequence
                of 2D MeshElement objects specifying the target of the extrude meshing operation. If
                specified, this argument overrides the **depth** argument, and all points on the source
                will be extruded in the direction of the extrusion vector until meeting the target.

            biasRatio=`1`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.biasRatio "Permalink to this definition")
            :   A Float specifying a ratio of the element size in the extrusion direction between the
                source and the target sides of the extrusion. The default is 1.0, meaning no bias.

            extendElementSets=`False`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpExtrudedMesh.extendElementSets "Permalink to this definition")
            :   A Boolean specifying whether existing element sets that include source elements will be
                extended to also include extruded elements. This argument is ignored for native part
                instances. The default value is False.

    generateBottomUpRevolvedMesh(*[cell](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh.cell "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh.cell (Python parameter) — A Cell object specifying the geometric region where the mesh is to be generated.")*, *[numberOfLayers](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh.numberOfLayers "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh.numberOfLayers (Python parameter) — An Int specifying the number of layers of elements to be generated around the axis of revolution.")*, *[axisOfRevolution](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh.axisOfRevolution "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh.axisOfRevolution (Python parameter) — A sequence of sequences of Floats specifying the two points of the vector that describes the axis of revolution.")*, *[angleOfRevolution](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh.angleOfRevolution "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh.angleOfRevolution (Python parameter) — A Float specifying the angle of revolution.")*, *[geometrySourceSide](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh.geometrySourceSide "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh.geometrySourceSide (Python parameter) — A Region of Face objects specifying the geometric domain to be used as the source for the revolve meshing operation.")=`''`*, *[elemFacesSourceSide](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh.elemFacesSourceSide "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh.elemFacesSourceSide (Python parameter) — A sequence of MeshFace objects specifying the faces of 3D elements to be used as the source for the revolve meshing operation.")=`()`*, *[elemSourceSide](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh.elemSourceSide "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh.elemSourceSide (Python parameter) — A sequence of 2D MeshElement objects specifying the elements to be used as the source for the revolve meshing operation.")=`()`*, *[extendElementSets](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh.extendElementSets "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh.extendElementSets (Python parameter) — A Boolean specifying whether existing element sets that include source elements will be extended to also include extruded elements.")=`False`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L356-L401)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh "Permalink to this definition")
    :   This method generates solid elements by revolving a 2D mesh around an axis, either on an orphan mesh
        or within a cell region using a bottom-up technique.

        Note

        Check [MeshAssembly.generateBottomUpRevolvedMesh on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblygeneratebottomuprevolvedmeshpyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh-parameters "Permalink to this headline")
        :   cell[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh.cell "Permalink to this definition")
            :   A Cell object specifying the geometric region where the mesh is to be generated. This
                argument is valid only for native part instances.

            numberOfLayers[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh.numberOfLayers "Permalink to this definition")
            :   An Int specifying the number of layers of elements to be generated around the axis of
                revolution.

            axisOfRevolution[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh.axisOfRevolution "Permalink to this definition")
            :   A sequence of sequences of Floats specifying the two points of the vector that describes
                the axis of revolution. Each point is defined by a tuple of three coordinates indicating
                its position. The direction of the axis of revolution is from the first point to the
                second point. The orientation of the revolution operation follows the right-hand-rule
                about the axis of revolution.

            angleOfRevolution[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh.angleOfRevolution "Permalink to this definition")
            :   A Float specifying the angle of revolution.

            geometrySourceSide=`''`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh.geometrySourceSide "Permalink to this definition")
            :   A Region of Face objects specifying the geometric domain to be used as the source for
                the revolve meshing operation.

            elemFacesSourceSide=`()`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh.elemFacesSourceSide "Permalink to this definition")
            :   A sequence of MeshFace objects specifying the faces of 3D elements to be used as the
                source for the revolve meshing operation.

            elemSourceSide=`()`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh.elemSourceSide "Permalink to this definition")
            :   A sequence of 2D MeshElement objects specifying the elements to be used as the source
                for the revolve meshing operation.

            extendElementSets=`False`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpRevolvedMesh.extendElementSets "Permalink to this definition")
            :   A Boolean specifying whether existing element sets that include source elements will be
                extended to also include extruded elements. This argument is ignored for native part
                instances. The default value is False.

    generateBottomUpSweptMesh(*[cell](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.cell "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.cell (Python parameter) — A Cell object specifying the geometric region where the mesh is to be generated.")*, *[geometrySourceSide](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.geometrySourceSide "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.geometrySourceSide (Python parameter) — A Region of Face objects specifying the geometric domain to be used as the source for the sweep meshing operation.")=`''`*, *[elemFacesSourceSide](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.elemFacesSourceSide "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.elemFacesSourceSide (Python parameter) — A sequence of MeshFace objects specifying the faces of 3D elements to be used as the source for the sweep meshing operation.")=`()`*, *[elemSourceSide](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.elemSourceSide "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.elemSourceSide (Python parameter) — A sequence of 2D MeshElement objects specifying the elements to be used as the source for the sweep meshing operation.")=`()`*, *[geometryConnectingSides](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.geometryConnectingSides "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.geometryConnectingSides (Python parameter) — A Region of Face objects specifying the connecting sides of the sweep meshing operation.")=`''`*, *[elemFacesConnectingSides](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.elemFacesConnectingSides "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.elemFacesConnectingSides (Python parameter) — A sequence of MeshFace objects specifying connecting sides of the sweep meshing operation.")=`()`*, *[elemConnectingSides](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.elemConnectingSides "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.elemConnectingSides (Python parameter) — A sequence of 2D MeshElement objects specifying connecting sides of the sweep meshing operation.")=`()`*, *[targetSide](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.targetSide "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.targetSide (Python parameter) — A Face object specifying the target side of the sweep meshing operation.")=`None`*, *[numberOfLayers](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.numberOfLayers "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.numberOfLayers (Python parameter) — An Int specifying the number of layers to be generated along the sweep direction.")=`None`*, *[extendElementSets](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.extendElementSets "abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.extendElementSets (Python parameter) — A Boolean specifying whether existing element sets that include source elements will be extended to also include swept elements.")=`False`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L306-L354)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh "Permalink to this definition")
    :   This method generates solid elements by sweeping a 2D mesh, either on an orphan mesh or within a cell
        region using a bottom-up technique.

        Note

        Check [MeshAssembly.generateBottomUpSweptMesh on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblygeneratebottomupsweptmeshpyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh-parameters "Permalink to this headline")
        :   cell[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.cell "Permalink to this definition")
            :   A Cell object specifying the geometric region where the mesh is to be generated. This
                argument is valid only for native part instances.

            geometrySourceSide=`''`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.geometrySourceSide "Permalink to this definition")
            :   A Region of Face objects specifying the geometric domain to be used as the source for
                the sweep meshing operation.

            elemFacesSourceSide=`()`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.elemFacesSourceSide "Permalink to this definition")
            :   A sequence of MeshFace objects specifying the faces of 3D elements to be used as the
                source for the sweep meshing operation.

            elemSourceSide=`()`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.elemSourceSide "Permalink to this definition")
            :   A sequence of 2D MeshElement objects specifying the elements to be used as the source
                for the sweep meshing operation.

            geometryConnectingSides=`''`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.geometryConnectingSides "Permalink to this definition")
            :   A Region of Face objects specifying the connecting sides of the sweep meshing operation.

            elemFacesConnectingSides=`()`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.elemFacesConnectingSides "Permalink to this definition")
            :   A sequence of MeshFace objects specifying connecting sides of the sweep meshing
                operation.

            elemConnectingSides=`()`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.elemConnectingSides "Permalink to this definition")
            :   A sequence of 2D MeshElement objects specifying connecting sides of the sweep meshing
                operation.

            targetSide=`None`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.targetSide "Permalink to this definition")
            :   A Face object specifying the target side of the sweep meshing operation.

            numberOfLayers=`None`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.numberOfLayers "Permalink to this definition")
            :   An Int specifying the number of layers to be generated along the sweep direction.

            extendElementSets=`False`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateBottomUpSweptMesh.extendElementSets "Permalink to this definition")
            :   A Boolean specifying whether existing element sets that include source elements will be
                extended to also include swept elements. This argument is ignored for native part
                instances. The default value is False.

    generateMesh(*[regions](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateMesh.regions "abaqus.Mesh.MeshAssembly.MeshAssembly.generateMesh.regions (Python parameter) — A sequence of PartInstance objects or Region objects specifying the part instances or regions where the mesh is to be generated.")=`()`*, *[seedConstraintOverride](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateMesh.seedConstraintOverride "abaqus.Mesh.MeshAssembly.MeshAssembly.generateMesh.seedConstraintOverride (Python parameter) — A Boolean specifying whether mesh generation is allowed to modify seed constraints.")=`0`*, *[meshTechniqueOverride](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateMesh.meshTechniqueOverride "abaqus.Mesh.MeshAssembly.MeshAssembly.generateMesh.meshTechniqueOverride (Python parameter) — A Boolean specifying whether mesh generation is allowed to modify the existing mesh techniques so that a compatible mesh can be generated.")=`0`*, *[boundaryPreview](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateMesh.boundaryPreview "abaqus.Mesh.MeshAssembly.MeshAssembly.generateMesh.boundaryPreview (Python parameter) — A Boolean specifying whether the generated mesh should be a boundary mesh.")=`0`*, *[boundaryMeshOverride](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateMesh.boundaryMeshOverride "abaqus.Mesh.MeshAssembly.MeshAssembly.generateMesh.boundaryMeshOverride (Python parameter) — A Boolean specifying whether mesh generation is allowed to modify an existing boundary preview mesh.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L403-L436)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateMesh "Permalink to this definition")
    :   This method generates a mesh in the given part instances or regions.

        Note

        Check [MeshAssembly.generateMesh on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblygeneratemeshpyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateMesh-parameters "Permalink to this headline")
        :   regions=`()`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateMesh.regions "Permalink to this definition")
            :   A sequence of PartInstance objects or Region objects specifying the part instances or
                regions where the mesh is to be generated.

            seedConstraintOverride=`0`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateMesh.seedConstraintOverride "Permalink to this definition")
            :   A Boolean specifying whether mesh generation is allowed to modify seed constraints. The
                default value is OFF.

            meshTechniqueOverride=`0`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateMesh.meshTechniqueOverride "Permalink to this definition")
            :   A Boolean specifying whether mesh generation is allowed to modify the existing mesh
                techniques so that a compatible mesh can be generated. The default value is OFF.

            boundaryPreview=`0`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateMesh.boundaryPreview "Permalink to this definition")
            :   A Boolean specifying whether the generated mesh should be a boundary mesh. This option
                will only have an effect if any of the specified regions are to be meshed with
                tetrahedral elements or using the bottom-up technique with hexahedral or wedge elements.
                The default value is OFF.

            boundaryMeshOverride=`0`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.generateMesh.boundaryMeshOverride "Permalink to this definition")
            :   A Boolean specifying whether mesh generation is allowed to modify an existing boundary
                preview mesh. This option will only have an effect if any of the specified regions are
                to be meshed with tetrahedral elements and a boundary preview mesh already exists. The
                default value is OFF.

    getEdgeSeeds(*[edge](#abaqus.Mesh.MeshAssembly.MeshAssembly.getEdgeSeeds.edge "abaqus.Mesh.MeshAssembly.MeshAssembly.getEdgeSeeds.edge (Python parameter) — An Edge object specifying the edge to be queried.")*, *[attribute](#abaqus.Mesh.MeshAssembly.MeshAssembly.getEdgeSeeds.attribute "abaqus.Mesh.MeshAssembly.MeshAssembly.getEdgeSeeds.attribute (Python parameter) — A SymbolicConstant specifying the type of edge seed attribute to return.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L438-L526)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getEdgeSeeds "Permalink to this definition")
    :   This method returns an edge seed parameter for a specified edge of an assembly.

        Note

        Check [MeshAssembly.getEdgeSeeds on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblygetedgeseedspyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getEdgeSeeds-parameters "Permalink to this headline")
        :   edge[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getEdgeSeeds.edge "Permalink to this definition")
            :   An Edge object specifying the edge to be queried.

            attribute[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getEdgeSeeds.attribute "Permalink to this definition")
            :   A SymbolicConstant specifying the type of edge seed attribute to return. Possible values
                are:

                * EDGE\_SEEDING\_METHOD
                * BIAS\_METHOD
                * NUMBER
                * AVERAGE\_SIZE
                * DEVIATION\_FACTOR
                * MIN\_SIZE\_FACTOR
                * BIAS\_RATIO
                * BIAS\_MIN\_SIZE
                * BIAS\_MAX\_SIZE
                * VERTEX\_ADJ\_TO\_SMALLEST\_ELEM
                * SMALLEST\_ELEM\_LOCATION
                * CONSTRAINT

        Returns:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getEdgeSeeds-returns "Permalink to this headline")
        :   The return value is a Float, an Int, or a SymbolicConstant depending on the value of the
            **attribute** argument.

            The return value is dependent on the **attribute** argument.

            * If **attribute** = EDGE\_SEEDING\_METHOD, the return value is a SymbolicConstant specifying
              the edge seeding method used to create the seeds along the edge. Possible values are:
              UNIFORM\_BY\_NUMBER, UNIFORM\_BY\_SIZE, CURVATURE\_BASED\_BY\_SIZE, BIASED, NONE
            * If **attribute** = BIAS\_METHOD, the return value is a SymbolicConstant specifying the bias
              type used to create the seeds along the edge. Possible values are: SINGLE, DOUBLE, NONE
            * If **attribute** = NUMBER, the return value is an Int specifying the number of element
              seeds along the edge.
            * If **attribute** = AVERAGE\_SIZE, the return value is a Float specifying the average
              element size along the edge.
            * If **attribute** = DEVIATION\_FACTOR, the return value is a Float specifying the deviation
              factor h/Lh/L, where hh is the chordal deviation and LL is the element length. If edge
              seeds are not defined, the return value is zero.
            * If **attribute** = MIN\_SIZE\_FACTOR, the return value is a Float specifying the size of the
              smallest allowable element as a fraction of the specified global element size. If edge
              seeds are not defined, the return value is zero.
            * If **attribute** = BIAS\_RATIO, the return value is a Float specifying the length ratio of
              the largest element to the smallest element.
            * If **attribute** = BIAS\_MIN\_SIZE, the return value is a Float specifying the length of the
              largest element; only applicable if the EDGE\_SEEDING\_METHOD is BIASED and seeds were
              specified by minimum and maximum sizes.
            * If **attribute** = BIAS\_MAX\_SIZE, the return value is a Float specifying the length of the
              largest element; only applicable if the EDGE\_SEEDING\_METHOD is BIASED and seeds were
              specified by minimum and maximum sizes.
            * If **attribute** = VERTEX\_ADJ\_TO\_SMALLEST\_ELEM, the return value is an Int specifying the
              ID of the vertex next to the smallest element; only applicable if the
              EDGE\_SEEDING\_METHOD is BIASED.
            * If **attribute** = SMALLEST\_ELEM\_LOCATION, the return value is a SymbolicConstant
              specifying the location of smallest elements for double bias seeds; only applicable if
              the EDGE\_SEEDING\_METHOD is BIASED and BIAS\_METHOD is DOUBLE. Possible values are:
              SMALLEST\_ELEM\_AT\_CENTER, SMALLEST\_ELEM\_AT\_ENDS, NONE
            * If **attribute** = CONSTRAINT, the return value is a SymbolicConstant specifying how close
              the seeds must be matched by the mesh. Possible values are: FREE, FINER, FIXED, NONE

            A value of NONE indicates that the edge is not seeded.

        Return type:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getEdgeSeeds-return-type "Permalink to this headline")
        :   `Union[float`, [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), `SymbolicConstant]`

    getElementType(*[region](#abaqus.Mesh.MeshAssembly.MeshAssembly.getElementType.region "abaqus.Mesh.MeshAssembly.MeshAssembly.getElementType.region (Python parameter) — A Cell, a Face, or an Edge object specifying the region to be queried.")*, *[elemShape](#abaqus.Mesh.MeshAssembly.MeshAssembly.getElementType.elemShape "abaqus.Mesh.MeshAssembly.MeshAssembly.getElementType.elemShape (Python parameter) — A SymbolicConstant specifying the shape of the element for which to return the element type.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L528-L552)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getElementType "Permalink to this definition")
    :   This method returns the ElemType object of a given element shape assigned to a region of the
        assembly.

        Note

        Check [MeshAssembly.getElementType on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblygetelementtypepyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getElementType-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getElementType.region "Permalink to this definition")
            :   A Cell, a Face, or an Edge object specifying the region to be queried.

            elemShape[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getElementType.elemShape "Permalink to this definition")
            :   A SymbolicConstant specifying the shape of the element for which to return the element
                type. Possible values are:LINEQUADTRIHEXWEDGETET

        Returns:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getElementType-returns "Permalink to this headline")
        :   An ElemType object.

        Return type:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getElementType-return-type "Permalink to this headline")
        :   `ElementType`

        Raises:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getElementType-raises "Permalink to this headline")
        :   [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.13)") – If the region cannot be associated with element types or if the **elemShape** is not
            consistent with the dimension of the **region**.

    getIncompatibleMeshInterfaces(*[cells](#abaqus.Mesh.MeshAssembly.MeshAssembly.getIncompatibleMeshInterfaces.cells "abaqus.Mesh.MeshAssembly.MeshAssembly.getIncompatibleMeshInterfaces.cells (Python parameter) — A sequence of Cell objects which will be used to search the incompatible faces.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L554-L568)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getIncompatibleMeshInterfaces "Permalink to this definition")
    :   This method returns a sequence of face objects that are meshed with incompatible elements.

        Note

        Check [MeshAssembly.getIncompatibleMeshInterfaces on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblygetincompatiblemeshinterfacespyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getIncompatibleMeshInterfaces-parameters "Permalink to this headline")
        :   cells=`()`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getIncompatibleMeshInterfaces.cells "Permalink to this definition")
            :   A sequence of Cell objects which will be used to search the incompatible faces.

        Returns:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getIncompatibleMeshInterfaces-returns "Permalink to this headline")
        :   A sequence of Face objects.

        Return type:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getIncompatibleMeshInterfaces-return-type "Permalink to this headline")
        :   `Sequence[Face]`

    getMeshControl(*[region](#abaqus.Mesh.MeshAssembly.MeshAssembly.getMeshControl.region "abaqus.Mesh.MeshAssembly.MeshAssembly.getMeshControl.region (Python parameter) — A Cell, a Face, or an Edge object specifying the region to be queried.")*, *[attribute](#abaqus.Mesh.MeshAssembly.MeshAssembly.getMeshControl.attribute "abaqus.Mesh.MeshAssembly.MeshAssembly.getMeshControl.attribute (Python parameter) — A SymbolicConstant specifying the mesh control attribute to return.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L570-L635)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getMeshControl "Permalink to this definition")
    :   This method returns a mesh control parameter for the specified region of the assembly.

        Note

        Check [MeshAssembly.getMeshControl on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblygetmeshcontrolpyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getMeshControl-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getMeshControl.region "Permalink to this definition")
            :   A Cell, a Face, or an Edge object specifying the region to be queried.

            attribute[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getMeshControl.attribute "Permalink to this definition")
            :   A SymbolicConstant specifying the mesh control attribute to return. Possible values are:

                * ELEM\_SHAPE
                * TECHNIQUE
                * ALGORITHM
                * MIN\_TRANSITION

                The return value is dependent on the **attribute** argument.

                * If **attribute** = ELEM\_SHAPE, the return value is a SymbolicConstant specifying the
                  element shape used during meshing. Possible values are: LINE, QUAD, TRI, QUAD\_DOMINATED, HEX, TET, WEDGE, HEX\_DOMINATED
                * If **attribute** = TECHNIQUE, the return value is a SymbolicConstant specifying the
                  meshing technique to be used during meshing. Possible values are: FREE, STRUCTURED, SWEEP, UNMESHABLE, Where UNMESHABLE indicates that no meshing technique is applicable with the currently assigned element shape.
                * If **attribute** = ALGORITHM, the return value is a SymbolicConstant specifying the
                  meshing algorithm to be used during meshing. Possible values are: MEDIAL\_AXIS, ADVANCING\_FRONT, DEFAULT, NON\_DEFAULT, NONE, Where NONE indicates that no algorithm is applicable.
                * If **attribute** = MIN\_TRANSITION, the return value is a Boolean indicating whether
                  minimum transition will be used during meshing. This option is applicable only to the
                  following: Free quadrilateral meshing or sweep hexahedral meshing with **algorithm** = MEDIAL\_AXIS, Structured quadrilateral meshing.

        Returns:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getMeshControl-returns "Permalink to this headline")
        :   The return value is a SymbolicConstant or a Boolean depending on the value of the
            **attribute** argument.

        Return type:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getMeshControl-return-type "Permalink to this headline")
        :   `Union[bool`, `SymbolicConstant]`

        Raises:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getMeshControl-raises "Permalink to this headline")
        :   [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.13)") – The region cannot carry mesh controls.

    getMeshStats(*[regions](#abaqus.Mesh.MeshAssembly.MeshAssembly.getMeshStats.regions "abaqus.Mesh.MeshAssembly.MeshAssembly.getMeshStats.regions (Python parameter) — A sequence or tuple of PartInstance objects or ConstrainedSketchGeometry regions for which mesh statistics should be returned.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L637-L652)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getMeshStats "Permalink to this definition")
    :   This method returns the mesh statistics for the given part instances or regions.

        Note

        Check [MeshAssembly.getMeshStats on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblygetmeshstatspyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getMeshStats-parameters "Permalink to this headline")
        :   regions[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getMeshStats.regions "Permalink to this definition")
            :   A sequence or tuple of PartInstance objects or ConstrainedSketchGeometry regions for which mesh
                statistics should be returned.

        Returns:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getMeshStats-returns "Permalink to this headline")
        :   A MeshStats object.

        Return type:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getMeshStats-return-type "Permalink to this headline")
        :   `MeshStats`

    getPartSeeds(*[region](#abaqus.Mesh.MeshAssembly.MeshAssembly.getPartSeeds.region "abaqus.Mesh.MeshAssembly.MeshAssembly.getPartSeeds.region (Python parameter) — A PartInstance object specifying the part instance to be queried.")*, *[attribute](#abaqus.Mesh.MeshAssembly.MeshAssembly.getPartSeeds.attribute "abaqus.Mesh.MeshAssembly.MeshAssembly.getPartSeeds.attribute (Python parameter) — A SymbolicConstant specifying the type of part seed attribute to return.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L654-L698)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getPartSeeds "Permalink to this definition")
    :   This method returns a part seed parameter for the specified instance.

        Note

        Check [MeshAssembly.getPartSeeds on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblygetpartseedspyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getPartSeeds-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getPartSeeds.region "Permalink to this definition")
            :   A PartInstance object specifying the part instance to be queried.

            attribute[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getPartSeeds.attribute "Permalink to this definition")
            :   A SymbolicConstant specifying the type of part seed attribute to return. Possible values
                are:

                * SIZE
                * DEFAULT\_SIZE
                * DEVIATION\_FACTOR
                * MIN\_SIZE\_FACTOR

                The return value is dependent on the value of the **attribute** argument.

                * If **attribute** = SIZE, the return value is a Float specifying the assigned global
                  element size. If part seeds are not defined, the return value is zero.
                * If **attribute** = DEFAULT\_SIZE, the return value is a Float specifying a suggested
                  default global element size based upon the part geometry.
                * If **attribute** = DEVIATION\_FACTOR, the return value is a Float specifying the deviation
                  factor h/Lh/L, where hh is the chordal deviation and LL is the element length. If part
                  seeds are not defined, the return value is zero.
                * If **attribute** = MIN\_SIZE\_FACTOR, the return value is a Float specifying the size of the
                  smallest allowable element as a fraction of the specified global element size. If part
                  seeds are not defined, the return value is zero.

        Returns:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getPartSeeds-returns "Permalink to this headline")
        :   The return value is a Float, and its value is dependent on the **attribute** argument.

        Return type:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getPartSeeds-return-type "Permalink to this headline")
        :   [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")

        Raises:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getPartSeeds-raises "Permalink to this headline")
        :   **Error** – Part instance does not contain native geometry, An exception occurs if the part instance does not contain native geometry.

    getUnmeshedRegions()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L700-L710)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getUnmeshedRegions "Permalink to this definition")
    :   This method returns all geometric regions in the assembly that require a mesh for submitting an
        analysis but are either unmeshed or are meshed incompletely.

        Returns:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getUnmeshedRegions-returns "Permalink to this headline")
        :   A Region object, or None.

        Return type:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.getUnmeshedRegions-return-type "Permalink to this headline")
        :   `Region`

    ignoreEntity(*[entities](#abaqus.Mesh.MeshAssembly.MeshAssembly.ignoreEntity.entities "abaqus.Mesh.MeshAssembly.MeshAssembly.ignoreEntity.entities (Python parameter) — A sequence of vertices and edges specifying the entities to be ignored during meshing.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L712-L728)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.ignoreEntity "Permalink to this definition")
    :   This method creates a virtual topology feature. Virtual topology allows unimportant entities to be
        ignored during mesh generation. You can combine two adjacent faces by specifying a common edge to
        ignore. Similarly, you can combine two adjacent edges by specifying a common vertex to ignore.

        Note

        Check [MeshAssembly.ignoreEntity on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblyignoreentitypyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.ignoreEntity-parameters "Permalink to this headline")
        :   entities[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.ignoreEntity.entities "Permalink to this definition")
            :   A sequence of vertices and edges specifying the entities to be ignored during meshing.

        Returns:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.ignoreEntity-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.ignoreEntity-return-type "Permalink to this headline")
        :   `Feature`

    restoreIgnoredEntity(*[entities](#abaqus.Mesh.MeshAssembly.MeshAssembly.restoreIgnoredEntity.entities "abaqus.Mesh.MeshAssembly.MeshAssembly.restoreIgnoredEntity.entities (Python parameter) — A sequence of IgnoredVertex objects and IgnoredEdge objects specifying the entities to be restored.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L730-L745)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.restoreIgnoredEntity "Permalink to this definition")
    :   This method restores vertices and edges that have been merged using a virtual topology feature.

        Note

        Check [MeshAssembly.restoreIgnoredEntity on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblyrestoreignoredentitypyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.restoreIgnoredEntity-parameters "Permalink to this headline")
        :   entities[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.restoreIgnoredEntity.entities "Permalink to this definition")
            :   A sequence of IgnoredVertex objects and IgnoredEdge objects specifying the entities to
                be restored.

        Returns:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.restoreIgnoredEntity-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.restoreIgnoredEntity-return-type "Permalink to this headline")
        :   `Feature`

    seedEdgeByBias(*[biasMethod](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.biasMethod "abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.biasMethod (Python parameter) — A SymbolicConstant specifying whether single- or double-biased seed distribution will be applied.")*, *[end1Edges](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.end1Edges "abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.end1Edges (Python parameter) — A sequence of Edge objects specifying the edges to seed.")*, *[end2Edges](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.end2Edges "abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.end2Edges (Python parameter) — A sequence of Edge objects specifying the edges to seed.")*, *[centerEdges](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.centerEdges "abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.centerEdges (Python parameter) — A sequence of Edge objects specifying the edges to seed.")*, *[endEdges](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.endEdges "abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.endEdges (Python parameter) — A sequence of Edge objects specifying the edges to seed.")*, *[ratio](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.ratio "abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.ratio (Python parameter) — A Float specifying the ratio of the largest element to the smallest element.")*, *[number](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.number "abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.number (Python parameter) — An Int specifying the number of elements along each edge.")*, *[minSize](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.minSize "abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.minSize (Python parameter) — A Float specifying the desired smallest element size.")*, *[maxSize](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.maxSize "abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.maxSize (Python parameter) — A Float specifying the desired largest element size.")*, *[constraint](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.constraint "abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.constraint (Python parameter) — A SymbolicConstant specifying how closely the seeds must be matched by the mesh.")=`abaqusConstants.FREE`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L747-L812)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias "Permalink to this definition")
    :   This method seeds the given edges nonuniformly using the specified number of elements and bias ratio
        or the specified minimum and maximum element sizes.

        Note

        Check [MeshAssembly.seedEdgeByBias on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblyseededgebybiaspyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias-parameters "Permalink to this headline")
        :   biasMethod[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.biasMethod "Permalink to this definition")
            :   A SymbolicConstant specifying whether single- or double-biased seed distribution will be
                applied. If unspecified, single-biased seed distribution will be applied. Possible
                values are:

                * SINGLE: Single-biased seed distribution will be applied.
                * DOUBLE: Double-biased seed distribution will be applied.

            end1Edges[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.end1Edges "Permalink to this definition")
            :   A sequence of Edge objects specifying the edges to seed. The smallest elements will be
                positioned near the end where the normalized curve parameter=0.0. You must provide
                either the **end1Edges** or the **end2Edges** argument or both when **biasMethod** = SINGLE and
                omit both of them when **biasMethod** = DOUBLE. Note: You can determine which end is which by
                the order of the vertex indices returned by getVertices().

            end2Edges[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.end2Edges "Permalink to this definition")
            :   A sequence of Edge objects specifying the edges to seed. The smallest elements will be
                positioned near the end where the normalized curve parameter=1.0.

            centerEdges[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.centerEdges "Permalink to this definition")
            :   A sequence of Edge objects specifying the edges to seed. The smallest elements will be
                positioned near edge center. You must provide either the **centerEdges** or the **endEdges**
                argument or both when **biasMethod** = DOUBLE and omit both of them when
                **biasMethod** = SINGLE.

            endEdges[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.endEdges "Permalink to this definition")
            :   A sequence of Edge objects specifying the edges to seed. The smallest elements will be
                positioned near edge ends.

            ratio[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.ratio "Permalink to this definition")
            :   A Float specifying the ratio of the largest element to the smallest element. Possible
                values are 1.0 ≤ **ratio** ≤ 10⁶.

            number[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.number "Permalink to this definition")
            :   An Int specifying the number of elements along each edge. Possible values are 1 ≤
                **number** ≤ 10⁴.

            minSize[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.minSize "Permalink to this definition")
            :   A Float specifying the desired smallest element size.

            maxSize[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.maxSize "Permalink to this definition")
            :   A Float specifying the desired largest element size. Note: You must specify either the
                **ratio** and **number** or **minSize** and **maxSize** pair of arguments.

            constraint=`abaqusConstants.FREE`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByBias.constraint "Permalink to this definition")
            :   A SymbolicConstant specifying how closely the seeds must be matched by the mesh. The
                default value is FREE. If unspecified, the existing constraint will remain unchanged.
                Possible values are:

                * FREE: The resulting mesh can be finer or coarser than the specified seeds.
                * FINER: The resulting mesh can be finer than the specified seeds.
                * FIXED: The seeds must be exactly matched by the mesh (only with respect to the number
                  of elements, not to the nodal positioning).

    seedEdgeByNumber(*[edges](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByNumber.edges "abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByNumber.edges (Python parameter) — A sequence of Edge objects specifying the edges to seed.")*, *[number](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByNumber.number "abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByNumber.number (Python parameter) — An Int specifying the number of elements along each edge.")*, *[constraint](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByNumber.constraint "abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByNumber.constraint (Python parameter) — A SymbolicConstant specifying how closely the seeds must be matched by the mesh.")=`abaqusConstants.FREE`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L814-L833)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByNumber "Permalink to this definition")
    :   This method seeds the given edges uniformly based on the number of elements along the edges.

        Note

        Check [MeshAssembly.seedEdgeByNumber on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblyseededgebynumberpyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByNumber-parameters "Permalink to this headline")
        :   edges[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByNumber.edges "Permalink to this definition")
            :   A sequence of Edge objects specifying the edges to seed.

            number[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByNumber.number "Permalink to this definition")
            :   An Int specifying the number of elements along each edge. Possible values are 1 ≤
                **number** ≤ 10⁴.

            constraint=`abaqusConstants.FREE`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeByNumber.constraint "Permalink to this definition")
            :   A SymbolicConstant specifying how closely the seeds must be matched by the mesh. The
                default value is FREE. If unspecified, the existing constraint will remain unchanged.
                Possible values are:FREE: The resulting mesh can be finer or coarser than the specified
                seeds.FINER: The resulting mesh can be finer than the specified seeds.FIXED: The seeds
                must be exactly matched by the mesh (only with respect to the number of elements, not to
                the nodal positioning).

    seedEdgeBySize(*[edges](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeBySize.edges "abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeBySize.edges (Python parameter) — A sequence of Edge objects specifying the edges to seed.")*, *[size](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeBySize.size "abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeBySize.size (Python parameter) — A Float specifying the desired element size.")*, *[deviationFactor](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeBySize.deviationFactor "abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeBySize.deviationFactor (Python parameter) — A Float specifying the deviation factor h/Lh/L, where hh is the chordal deviation and LL is the element length.")=`None`*, *[minSizeFactor](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeBySize.minSizeFactor "abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeBySize.minSizeFactor (Python parameter) — A Float specifying the size of the smallest allowable element as a fraction of the specified global element size.")=`None`*, *[constraint](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeBySize.constraint "abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeBySize.constraint (Python parameter) — A SymbolicConstant specifying how closely the seeds must be matched by the mesh.")=`abaqusConstants.FREE`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L835-L867)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeBySize "Permalink to this definition")
    :   This method seeds the given edges either uniformly or following edge curvature distribution, based on
        the desired element size.

        Note

        Check [MeshAssembly.seedEdgeBySize on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblyseededgebysizepyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeBySize-parameters "Permalink to this headline")
        :   edges[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeBySize.edges "Permalink to this definition")
            :   A sequence of Edge objects specifying the edges to seed.

            size[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeBySize.size "Permalink to this definition")
            :   A Float specifying the desired element size.

            deviationFactor=`None`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeBySize.deviationFactor "Permalink to this definition")
            :   A Float specifying the deviation factor h/Lh/L, where hh is the chordal deviation and LL
                is the element length.

            minSizeFactor=`None`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeBySize.minSizeFactor "Permalink to this definition")
            :   A Float specifying the size of the smallest allowable element as a fraction of the
                specified global element size.

            constraint=`abaqusConstants.FREE`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedEdgeBySize.constraint "Permalink to this definition")
            :   A SymbolicConstant specifying how closely the seeds must be matched by the mesh. The
                default value is FREE. If unspecified, the existing constraint will remain unchanged.
                Possible values are:FREE: The resulting mesh can be finer or coarser than the specified
                seeds.FINER: The resulting mesh can be finer than the specified seeds.FIXED: The seeds
                must be exactly matched by the mesh (only with respect to the number of elements, not to
                the nodal positioning).

    seedPartInstance(*[regions](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedPartInstance.regions "abaqus.Mesh.MeshAssembly.MeshAssembly.seedPartInstance.regions (Python parameter) — A sequence of PartInstance objects specifying the part instances to seed.")*, *[size](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedPartInstance.size "abaqus.Mesh.MeshAssembly.MeshAssembly.seedPartInstance.size (Python parameter) — A Float specifying the desired global element size for the edges.")*, *[deviationFactor](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedPartInstance.deviationFactor "abaqus.Mesh.MeshAssembly.MeshAssembly.seedPartInstance.deviationFactor (Python parameter) — A Float specifying the deviation factor h/Lh/L, where hh is the chordal deviation and LL is the element length.")=`None`*, *[minSizeFactor](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedPartInstance.minSizeFactor "abaqus.Mesh.MeshAssembly.MeshAssembly.seedPartInstance.minSizeFactor (Python parameter) — A Float specifying the size of the smallest allowable element as a fraction of the specified global element size.")=`None`*, *[constraint](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedPartInstance.constraint "abaqus.Mesh.MeshAssembly.MeshAssembly.seedPartInstance.constraint (Python parameter) — A SymbolicConstant specifying how closely the seeds must be matched by the mesh.")=`abaqusConstants.FREE`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L869-L898)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedPartInstance "Permalink to this definition")
    :   This method assigns global edge seeds to the given part instances.

        Note

        Check [MeshAssembly.seedPartInstance on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblyseedpartinstancepyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedPartInstance-parameters "Permalink to this headline")
        :   regions[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedPartInstance.regions "Permalink to this definition")
            :   A sequence of PartInstance objects specifying the part instances to seed.

            size[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedPartInstance.size "Permalink to this definition")
            :   A Float specifying the desired global element size for the edges.

            deviationFactor=`None`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedPartInstance.deviationFactor "Permalink to this definition")
            :   A Float specifying the deviation factor h/Lh/L, where hh is the chordal deviation and LL
                is the element length.

            minSizeFactor=`None`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedPartInstance.minSizeFactor "Permalink to this definition")
            :   A Float specifying the size of the smallest allowable element as a fraction of the
                specified global element size.

            constraint=`abaqusConstants.FREE`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.seedPartInstance.constraint "Permalink to this definition")
            :   A SymbolicConstant specifying how closely the seeds must be matched by the mesh. The
                default value is FREE. If unspecified, the existing constraint will remain unchanged.
                Possible values are:FREE: The resulting mesh can be finer or coarser than the specified
                seeds.FINER: The resulting mesh can be finer than the specified seeds.

    setBoundaryLayerControls(*[regions](#abaqus.Mesh.MeshAssembly.MeshAssembly.setBoundaryLayerControls.regions "abaqus.Mesh.MeshAssembly.MeshAssembly.setBoundaryLayerControls.regions (Python parameter) — A sequence of Cell objects specifying the regions for which to set the boundary layer mesh control parameters.")*, *[firstElemSize](#abaqus.Mesh.MeshAssembly.MeshAssembly.setBoundaryLayerControls.firstElemSize "abaqus.Mesh.MeshAssembly.MeshAssembly.setBoundaryLayerControls.firstElemSize (Python parameter) — A Float specifying the height of the first element layer off boundary.")*, *[growthFactor](#abaqus.Mesh.MeshAssembly.MeshAssembly.setBoundaryLayerControls.growthFactor "abaqus.Mesh.MeshAssembly.MeshAssembly.setBoundaryLayerControls.growthFactor (Python parameter) — A Float specifying the ratio of heights of any two consecutive element layers.")*, *[numLayers](#abaqus.Mesh.MeshAssembly.MeshAssembly.setBoundaryLayerControls.numLayers "abaqus.Mesh.MeshAssembly.MeshAssembly.setBoundaryLayerControls.numLayers (Python parameter) — An Int specifying the number of element layers to be generated.")*, *[inactiveFaces](#abaqus.Mesh.MeshAssembly.MeshAssembly.setBoundaryLayerControls.inactiveFaces "abaqus.Mesh.MeshAssembly.MeshAssembly.setBoundaryLayerControls.inactiveFaces (Python parameter) — A sequence of Face objects specifying the faces where boundary layer should not be generated.")=`()`*, *[setName](#abaqus.Mesh.MeshAssembly.MeshAssembly.setBoundaryLayerControls.setName "abaqus.Mesh.MeshAssembly.MeshAssembly.setBoundaryLayerControls.setName (Python parameter) — A String specifying a unique name for a set that will contain boundary layer elements.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L900-L933)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setBoundaryLayerControls "Permalink to this definition")
    :   This method sets the control parameters for boundary layer mesh for the specified regions.

        Note

        Check [MeshAssembly.setBoundaryLayerControls on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblysetboundarylayercontrolspyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setBoundaryLayerControls-parameters "Permalink to this headline")
        :   regions[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setBoundaryLayerControls.regions "Permalink to this definition")
            :   A sequence of Cell objects specifying the regions for which to set the boundary layer
                mesh control parameters.

            firstElemSize[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setBoundaryLayerControls.firstElemSize "Permalink to this definition")
            :   A Float specifying the height of the first element layer off boundary. Possible values
                are 0.0 < **firstElemSize** ≤ 10⁶.

            growthFactor[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setBoundaryLayerControls.growthFactor "Permalink to this definition")
            :   A Float specifying the ratio of heights of any two consecutive element layers. Possible
                values are 1.0 ≤ **growthFactor** ≤ 10.0.

            numLayers[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setBoundaryLayerControls.numLayers "Permalink to this definition")
            :   An Int specifying the number of element layers to be generated. Possible values are 1 ≤
                **numLayers** ≤ 10⁴.

            inactiveFaces=`()`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setBoundaryLayerControls.inactiveFaces "Permalink to this definition")
            :   A sequence of Face objects specifying the faces where boundary layer should not be
                generated. By default, boundary layer mesh will be generated on all faces of the
                selected regions.

            setName=`''`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setBoundaryLayerControls.setName "Permalink to this definition")
            :   A String specifying a unique name for a set that will contain boundary layer elements.

    setElementType(*[regions](#abaqus.Mesh.MeshAssembly.MeshAssembly.setElementType.regions "abaqus.Mesh.MeshAssembly.MeshAssembly.setElementType.regions (Python parameter) — A sequence of ConstrainedSketchGeometry regions or MeshElement objects, or a Set object containing either geometry regions or elements, specifying the regions to which element types are to be assigned.")*, *[elemTypes](#abaqus.Mesh.MeshAssembly.MeshAssembly.setElementType.elemTypes "abaqus.Mesh.MeshAssembly.MeshAssembly.setElementType.elemTypes (Python parameter) — A sequence of ElemType objects, one for each element shape applicable to the regions.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L935-L963)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setElementType "Permalink to this definition")
    :   This method assigns element types to the specified regions.

        Note

        Check [MeshAssembly.setElementType on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblysetelementtypepyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setElementType-parameters "Permalink to this headline")
        :   regions[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setElementType.regions "Permalink to this definition")
            :   A sequence of ConstrainedSketchGeometry regions or MeshElement objects, or a Set object containing either
                geometry regions or elements, specifying the regions to which element types are to be
                assigned.

            elemTypes[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setElementType.elemTypes "Permalink to this definition")
            :   A sequence of ElemType objects, one for each element shape applicable to the
                regions. Note: If an ElemType object has an UNKNOWN\_\*xxx\* value for **elemCode**, its order
                will be deduced from the order of other valid ElemType objects within the same
                setElementType command. If no valid ElemType objects can be found, the order will remain
                unchanged.

        Raises:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setElementType-raises "Permalink to this headline")
        :   [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.13)") – As a result of the element assignment, a region must have the same library, family, and
            order for all its assigned element types. Otherwise, an exception will be thrown.
            For example, suppose the Hex, Wedge, and Tet elements previously assigned to a cell are
            all linear. The user now constructs an ElemType object with a quadratic Hex element and
            includes only this object in the setElementType command. An exception will be thrown
            because the Wedge and Tet elements will remain linear (i.e., As Is) and become
            incompatible with the newly assigned quadratic Hex element.

    setLogicalCorners(*[region](#abaqus.Mesh.MeshAssembly.MeshAssembly.setLogicalCorners.region "abaqus.Mesh.MeshAssembly.MeshAssembly.setLogicalCorners.region (Python parameter) — A Face region.")*, *[corners](#abaqus.Mesh.MeshAssembly.MeshAssembly.setLogicalCorners.corners "abaqus.Mesh.MeshAssembly.MeshAssembly.setLogicalCorners.corners (Python parameter) — Three, four, or five ConstrainedSketchVertex objects defining the logical corners for a given mappable face region.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L965-L977)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setLogicalCorners "Permalink to this definition")
    :   This method sets the logical corners for a mappable face region.

        Note

        Check [MeshAssembly.setLogicalCorners on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblysetlogicalcornerspyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setLogicalCorners-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setLogicalCorners.region "Permalink to this definition")
            :   A Face region.

            corners[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setLogicalCorners.corners "Permalink to this definition")
            :   Three, four, or five ConstrainedSketchVertex objects defining the logical corners for a given mappable
                face region.

    setMeshControls(*[regions](#abaqus.Mesh.MeshAssembly.MeshAssembly.setMeshControls.regions "abaqus.Mesh.MeshAssembly.MeshAssembly.setMeshControls.regions (Python parameter) — A sequence of Face or Cell regions specifying the regions for which to set the mesh control parameters.")*, *[elemShape](#abaqus.Mesh.MeshAssembly.MeshAssembly.setMeshControls.elemShape "abaqus.Mesh.MeshAssembly.MeshAssembly.setMeshControls.elemShape (Python parameter) — A SymbolicConstant specifying the element shape to be used for meshing.")=`None`*, *[technique](#abaqus.Mesh.MeshAssembly.MeshAssembly.setMeshControls.technique "abaqus.Mesh.MeshAssembly.MeshAssembly.setMeshControls.technique (Python parameter) — A SymbolicConstant specifying the mesh technique to be used.")=`None`*, *[algorithm](#abaqus.Mesh.MeshAssembly.MeshAssembly.setMeshControls.algorithm "abaqus.Mesh.MeshAssembly.MeshAssembly.setMeshControls.algorithm (Python parameter) — A SymbolicConstant specifying the algorithm used to generate the mesh for the specified regions.")=`None`*, *[minTransition](#abaqus.Mesh.MeshAssembly.MeshAssembly.setMeshControls.minTransition "abaqus.Mesh.MeshAssembly.MeshAssembly.setMeshControls.minTransition (Python parameter) — A Boolean specifying whether minimum transition is to be applied.")=`1`*, *[sizeGrowth](#abaqus.Mesh.MeshAssembly.MeshAssembly.setMeshControls.sizeGrowth "abaqus.Mesh.MeshAssembly.MeshAssembly.setMeshControls.sizeGrowth (Python parameter) — A SymbolicConstant specifying element size growth to be applied when generating the interior of a tetrahedral mesh.")=`None`*, *[allowMapped](#abaqus.Mesh.MeshAssembly.MeshAssembly.setMeshControls.allowMapped "abaqus.Mesh.MeshAssembly.MeshAssembly.setMeshControls.allowMapped (Python parameter) — A Boolean specifying whether mapped meshing can be used to replace the selected mesh technique.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L979-L1058)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setMeshControls "Permalink to this definition")
    :   This method sets the mesh control parameters for the specified regions.

        Note

        Check [MeshAssembly.setMeshControls on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblysetmeshcontrolspyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setMeshControls-parameters "Permalink to this headline")
        :   regions[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setMeshControls.regions "Permalink to this definition")
            :   A sequence of Face or Cell regions specifying the regions for which to set the mesh
                control parameters.

            elemShape=`None`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setMeshControls.elemShape "Permalink to this definition")
            :   A SymbolicConstant specifying the element shape to be used for meshing. The default
                value is QUAD for Face regions and HEX for Cell regions. If unspecified, the existing
                element shape will remain unchanged. Possible values are:

                * QUAD: Quadrilateral mesh.
                * QUAD\_DOMINATED: Quadrilateral-dominated mesh.
                * TRI: Triangular mesh.
                * HEX: Hexahedral mesh.
                * HEX\_DOMINATED: Hex-dominated mesh.
                * TET: Tetrahedral mesh.
                * WEDGE: Wedge mesh.

            technique=`None`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setMeshControls.technique "Permalink to this definition")
            :   A SymbolicConstant specifying the mesh technique to be used. The default value is FREE
                for Face regions. For Cell regions the initial value depends on the geometry of the
                regions and can be STRUCTURED, SWEEP, or unmeshable. If unspecified, the existing mesh
                technique(s) will remain unchanged. Possible values are:

                * FREE: Free mesh technique.
                * STRUCTURED: Structured mesh technique.
                * SWEEP: Sweep mesh technique.
                * BOTTOM\_UP: Bottom-up mesh technique. Only applicable for cell regions.
                * SYSTEM\_ASSIGN: Allow the system to assign a suitable technique. The actual technique
                  assigned can be STRUCTURED, SWEEP, or “unmeshable”.

            algorithm=`None`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setMeshControls.algorithm "Permalink to this definition")
            :   A SymbolicConstant specifying the algorithm used to generate the mesh for the specified
                regions. Possible values are MEDIAL\_AXIS, ADVANCING\_FRONT, and NON\_DEFAULT. If
                unspecified, the existing value will remain unchanged. This option is applicable only to
                the following:

                * Free quadrilateral or quadrilateral-dominated meshing. In this case the possible
                  values are MEDIAL\_AXIS and ADVANCING\_FRONT.
                * Sweep hexahedral or hexahedral-dominated meshing. In this case the possible values are
                  MEDIAL\_AXIS and ADVANCING\_FRONT.
                * Free tetrahedral meshing. In this case the only possible value is NON\_DEFAULT, and it
                  indicates that the free tetrahedral-meshing technique available in Abaqus 6.4 or earlier
                  will be used. If algorithm is not specified, the default tetrahedral-meshing technique
                  will be used.

            minTransition=`1`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setMeshControls.minTransition "Permalink to this definition")
            :   A Boolean specifying whether minimum transition is to be applied. The default value is
                ON. If unspecified, the existing value will remain unchanged. This option is applicable
                only in the following cases:

                * Free quadrilateral meshing or hexahedral sweep meshing with **algorithm** = MEDIAL\_AXIS.
                * Structured quadrilateral meshing.

            sizeGrowth=`None`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setMeshControls.sizeGrowth "Permalink to this definition")
            :   A SymbolicConstant specifying element size growth to be applied when generating the
                interior of a tetrahedral mesh. Possible values are MODERATE and MAXIMUM. If
                unspecified, the existing value will remain unchanged. This option only applies to the
                default tetrahedral mesher.

            allowMapped=`0`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setMeshControls.allowMapped "Permalink to this definition")
            :   A Boolean specifying whether mapped meshing can be used to replace the selected mesh
                technique. The **allowMapped** argument is applicable only in the following cases:

                * Free triangular meshing.
                * Free quadrilateral or quadrilateral-dominated meshing with
                  **algorithm** = ADVANCING\_FRONT.
                * Hexahedral or hexahedral-dominated sweep meshing with **algorithm** = ADVANCING\_FRONT.
                * Free tetrahedral meshing. **allowMapped** = True implies that mapped triangular meshing
                  can be used on faces that bound three-dimensional **regions**.

    setSweepPath(*[region](#abaqus.Mesh.MeshAssembly.MeshAssembly.setSweepPath.region "abaqus.Mesh.MeshAssembly.MeshAssembly.setSweepPath.region (Python parameter) — A sweepable region.")*, *[edge](#abaqus.Mesh.MeshAssembly.MeshAssembly.setSweepPath.edge "abaqus.Mesh.MeshAssembly.MeshAssembly.setSweepPath.edge (Python parameter) — An Edge object specifying the sweep or revolve path.")*, *[sense](#abaqus.Mesh.MeshAssembly.MeshAssembly.setSweepPath.sense "abaqus.Mesh.MeshAssembly.MeshAssembly.setSweepPath.sense (Python parameter) — A SymbolicConstant specifying the sweep sense.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L1060-L1076)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setSweepPath "Permalink to this definition")
    :   This method sets the sweep path for a sweepable region or the revolve path for a revolvable region.

        Note

        Check [MeshAssembly.setSweepPath on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblysetsweeppathpyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setSweepPath-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setSweepPath.region "Permalink to this definition")
            :   A sweepable region.

            edge[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setSweepPath.edge "Permalink to this definition")
            :   An Edge object specifying the sweep or revolve path.

            sense[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.setSweepPath.sense "Permalink to this definition")
            :   A SymbolicConstant specifying the sweep sense. The sense will affect only how gasket
                elements will be created; it will have no effect if gasket elements are not used.
                Possible values are FORWARD or REVERSE.If **sense** = FORWARD, the sense of the given edge’s
                underlying curve will be used.

    verifyMeshQuality(*[criterion](#abaqus.Mesh.MeshAssembly.MeshAssembly.verifyMeshQuality.criterion "abaqus.Mesh.MeshAssembly.MeshAssembly.verifyMeshQuality.criterion (Python parameter) — A SymbolicConstant specifying the criterion used for the quality check.")*, *[threshold](#abaqus.Mesh.MeshAssembly.MeshAssembly.verifyMeshQuality.threshold "abaqus.Mesh.MeshAssembly.MeshAssembly.verifyMeshQuality.threshold (Python parameter) — A Float value used to determine low quality elements according to the specified criterion.")=`None`*, *[elemShape](#abaqus.Mesh.MeshAssembly.MeshAssembly.verifyMeshQuality.elemShape "abaqus.Mesh.MeshAssembly.MeshAssembly.verifyMeshQuality.elemShape (Python parameter) — A SymbolicConstant specifying an element shape for limiting the query.")=`None`*, *[regions](#abaqus.Mesh.MeshAssembly.MeshAssembly.verifyMeshQuality.regions "abaqus.Mesh.MeshAssembly.MeshAssembly.verifyMeshQuality.regions (Python parameter) — A sequence of Region or MeshElement objects.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshAssembly.py#L1078-L1168)[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.verifyMeshQuality "Permalink to this definition")
    :   This method tests the quality of part instance meshes and returns poor-quality elements.

        Note

        Check [MeshAssembly.verifyMeshQuality on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblymgnpyc.htm?contextscope=all#simaker-assemblyverifymeshqualitypyc).

        Parameters:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.verifyMeshQuality-parameters "Permalink to this headline")
        :   criterion[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.verifyMeshQuality.criterion "Permalink to this definition")
            :   A SymbolicConstant specifying the criterion used for the quality check. Possible values
                are:

                * ANALYSIS\_CHECKS
                  When this criterion is specified Abaqus/CAE will invoke the element quality checks
                  included with the input file processor for Abaqus/Standard and Abaqus/Explicit.
                * ANGULAR\_DEVIATION
                  The maximum amount (in degrees) that an element’s face corner angles deviate from the
                  ideal angle. The ideal angle is 90° for quadrilateral element faces and 60° for
                  triangular element faces. Elements with an angular deviation larger than the specified
                  threshold will fail this test.
                * ASPECT\_RATIO
                  The ratio between the lengths of the longest and shortest edges of an element. Elements
                  with an aspect ratio larger than the specified threshold will fail this test.
                * GEOM\_DEVIATION\_FACTOR
                  The largest geometric deviation factor evaluated along any of the element edges
                  associated with geometric edges or faces. The geometric deviation factor along an
                  element edge is calculated by dividing the maximum gap between the element edge and its
                  associated geometry by the length of the element edge. Elements with a geometric
                  deviation factor larger than the specified threshold will fail this test.
                * LARGE\_ANGLE
                  The largest corner angle on any of an element’s faces. Elements with face angles larger
                  than the specified threshold (in degrees) will fail this test.
                * LONGEST\_EDGE
                  The length of an element’s longest edge. Elements with an edge longer than the specified
                  threshold will fail this test.
                * MAX\_FREQUENCY
                  An estimate of an element’s contribution to the initial maximum allowable frequency for
                  Abaqus/Standard analyses. This calculation requires appropriate section assignments and
                  material definitions. Elements whose maximum allowable frequency is smaller than the
                  given value will fail this test.
                * SHAPE\_FACTOR
                  The shape factor for triangular and tetrahedral elements. This is the ratio between the
                  element area or volume and the optimal element area or volume. Elements with a shape
                  factor smaller than the specified threshold will fail this test.
                * SHORTEST\_EDGE
                  The length of an element’s shortest edge. Elements with an edge shorter than the
                  specified threshold will fail this test.
                * SMALL\_ANGLE
                  The smallest corner angle on any of an element’s faces. Elements with face angles
                  smaller than the given value (in degrees) will fail this test.
                * STABLE\_TIME\_INCREMENT
                  An estimate of an element’s contribution to the initial maximum stable time increment
                  for Abaqus/Explicit analyses. This calculation requires appropriate section assignments
                  and material definitions. Elements that require a time increment smaller than the given
                  value will fail this test.

            threshold=`None`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.verifyMeshQuality.threshold "Permalink to this definition")
            :   A Float value used to determine low quality elements according to the specified
                criterion. This argument is ignored when the ANALYSIS\_CHECKS criterion is used. For
                other criterion, if this argument is unspecified then no list of failed elements will be
                returned.

            elemShape=`None`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.verifyMeshQuality.elemShape "Permalink to this definition")
            :   A SymbolicConstant specifying an element shape for limiting the query. Possible values
                are LINE, QUAD, TRI, HEX, WEDGE, and TET.

            regions=`()`[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.verifyMeshQuality.regions "Permalink to this definition")
            :   A sequence of Region or MeshElement objects. If you do not specify the **regions**
                argument, all meshes in the assembly are considered.

        Returns:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.verifyMeshQuality-returns "Permalink to this headline")
        :   A Dictionary object containing values for some number of the following keys:
            failedElements, warningElements, naElements (sequences of MeshElement objects);
            numElements (Int); average, worst (Float); worstElement (MeshElement object) .

        Return type:[¶](#abaqus.Mesh.MeshAssembly.MeshAssembly.verifyMeshQuality-return-type "Permalink to this headline")
        :   `dict[str`, `int | float | MeshElement]`

*class* MeshEdge[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L8-L93)[¶](#abaqus.Mesh.MeshPart.MeshEdge "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The MeshEdge object refers to an element edge. It has no constructor or members. A MeshEdge object can be
    accessed via a MeshEdgeArray or a repository on a part or part instance.

    Note

    This object can be accessed by:

    ```python
    import part
    mdb.models[name].parts[name].elemEdges[i]
    mdb.models[name].parts[name].elementEdges[i]
    import assembly
    mdb.models[name].rootAssembly.allInstances[name].elemEdges[i]
    mdb.models[name].rootAssembly.allInstances[name].elementEdges[i]
    mdb.models[name].rootAssembly.instances[name].elemEdges[i]
    mdb.models[name].rootAssembly.instances[name].elementEdges[i]
    ```

    Note

    Check [MeshEdge on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgepyc.htm?contextscope=all).

    Member Details:

    getElemFaces()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L73-L82)[¶](#abaqus.Mesh.MeshPart.MeshEdge.getElemFaces "Permalink to this definition")
    :   This method returns a tuple of unique MeshFace objects that share the element edge.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshEdge.getElemFaces-returns "Permalink to this headline")
        :   A tuple of MeshFace objects.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshEdge.getElemFaces-return-type "Permalink to this headline")
        :   `Sequence[MeshFace]`

    getElements()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L26-L35)[¶](#abaqus.Mesh.MeshPart.MeshEdge.getElements "Permalink to this definition")
    :   This method returns a tuple of elements that share the element edge.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshEdge.getElements-returns "Permalink to this headline")
        :   A tuple of MeshElement objects.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshEdge.getElements-return-type "Permalink to this headline")
        :   `Sequence[MeshElement]`

    getElementsViaTopology(*[domain](#abaqus.Mesh.MeshPart.MeshEdge.getElementsViaTopology.domain "abaqus.Mesh.MeshPart.MeshEdge.getElementsViaTopology.domain (Python parameter) — A MeshElementArray object specifying the domain to include in the search.")=`[]`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L37-L53)[¶](#abaqus.Mesh.MeshPart.MeshEdge.getElementsViaTopology "Permalink to this definition")
    :   This method returns an array of MeshElement objects that are obtained by recursively finding adjacent
        elements via topology.

        Note

        Check [MeshEdge.getElementsViaTopology on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgepyc.htm?contextscope=all#simaker-meshedgegetelementsviatopologypyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshEdge.getElementsViaTopology-parameters "Permalink to this headline")
        :   domain=`[]`[¶](#abaqus.Mesh.MeshPart.MeshEdge.getElementsViaTopology.domain "Permalink to this definition")
            :   A MeshElementArray object specifying the domain to include in the search. By default,
                all elements in the mesh are included.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshEdge.getElementsViaTopology-returns "Permalink to this headline")
        :   A MeshElementArray object, which is a sequence of MeshElement objects.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshEdge.getElementsViaTopology-return-type "Permalink to this headline")
        :   `MeshElementArray`

    getNodes()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L84-L93)[¶](#abaqus.Mesh.MeshPart.MeshEdge.getNodes "Permalink to this definition")
    :   This method returns a tuple of nodes on the element edge.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshEdge.getNodes-returns "Permalink to this headline")
        :   A tuple of MeshNode objects.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshEdge.getNodes-return-type "Permalink to this headline")
        :   `Sequence[MeshNode]`

    getNodesViaTopology(*[domain](#abaqus.Mesh.MeshPart.MeshEdge.getNodesViaTopology.domain "abaqus.Mesh.MeshPart.MeshEdge.getNodesViaTopology.domain (Python parameter) — A MeshElementArray object specifying the domain to include in the search.")=`[]`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L55-L71)[¶](#abaqus.Mesh.MeshPart.MeshEdge.getNodesViaTopology "Permalink to this definition")
    :   This method returns an array of MeshNode objects that lie along element edges topologically in line
        with the element edge.

        Note

        Check [MeshEdge.getNodesViaTopology on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgepyc.htm?contextscope=all#simaker-meshedgegetnodesviatopologypyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshEdge.getNodesViaTopology-parameters "Permalink to this headline")
        :   domain=`[]`[¶](#abaqus.Mesh.MeshPart.MeshEdge.getNodesViaTopology.domain "Permalink to this definition")
            :   A MeshElementArray object specifying the domain to include in the search. By default,
                all elements in the mesh are included.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshEdge.getNodesViaTopology-returns "Permalink to this headline")
        :   A MeshNodeArray object, which is a sequence of MeshNode objects.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshEdge.getNodesViaTopology-return-type "Permalink to this headline")
        :   `MeshNodeArray`

*class* MeshElement[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L19-L193)[¶](#abaqus.Mesh.MeshPart.MeshElement "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The MeshElement object refers to an element of a native mesh or an orphan mesh. A MeshElement object can
    be accessed via a part or part instance using an index that refers to the internal numbering of the element
    repository. The index does not refer to the element label.

    Note

    This object can be accessed by:

    ```python
    import part
    mdb.models[name].parts[name].allInternalSets[name].elements[i]
    mdb.models[name].parts[name].allInternalSurfaces[name].elements[i]
    mdb.models[name].parts[name].allSets[name].elements[i]
    mdb.models[name].parts[name].allSurfaces[name].elements[i]
    mdb.models[name].parts[name].elements[i]
    mdb.models[name].parts[name].sets[name].elements[i]
    mdb.models[name].parts[name].surfaces[name].elements[i]
    import assembly
    mdb.models[name].rootAssembly.allInstances[name].elements[i]
    mdb.models[name].rootAssembly.allInstances[name].sets[name].elements[i]
    mdb.models[name].rootAssembly.allInstances[name].surfaces[name].elements[i]
    mdb.models[name].rootAssembly.allInternalSets[name].elements[i]
    mdb.models[name].rootAssembly.allInternalSurfaces[name].elements[i]
    mdb.models[name].rootAssembly.allSets[name].elements[i]
    mdb.models[name].rootAssembly.allSurfaces[name].elements[i]
    mdb.models[name].rootAssembly.elements[i]
    mdb.models[name].rootAssembly.instances[name].elements[i]
    mdb.models[name].rootAssembly.instances[name].sets[name].elements[i]
    mdb.models[name].rootAssembly.instances[name].surfaces[name].elements[i]
    mdb.models[name].rootAssembly.modelInstances[i].elements[i]
    mdb.models[name].rootAssembly.modelInstances[i].sets[name].elements[i]
    mdb.models[name].rootAssembly.modelInstances[i].surfaces[name].elements[i]
    mdb.models[name].rootAssembly.sets[name].elements[i]
    mdb.models[name].rootAssembly.surfaces[name].elements[i]
    ```

    Note

    Check [MeshElement on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?contextscope=all).

    Member Details:

    Element(*[nodes](#abaqus.Mesh.MeshPart.MeshElement.Element.nodes "abaqus.Mesh.MeshPart.MeshElement.Element.nodes (Python parameter) — A sequence of MeshNode objects.")*, *[elemShape](#abaqus.Mesh.MeshPart.MeshElement.Element.elemShape "abaqus.Mesh.MeshPart.MeshElement.Element.elemShape (Python parameter) — A SymbolicConstant specifying the shape of the new element.")*, *[label](#abaqus.Mesh.MeshPart.MeshElement.Element.label "abaqus.Mesh.MeshPart.MeshElement.Element.label (Python parameter) — An Int specifying the element label.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L69-L111)[¶](#abaqus.Mesh.MeshPart.MeshElement.Element "Permalink to this definition")
    :   This method creates an element on an orphan mesh part from a sequence of nodes.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].Element
        ```

        Note

        Check [Element on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-elementpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshElement.Element-parameters "Permalink to this headline")
        :   nodes[¶](#abaqus.Mesh.MeshPart.MeshElement.Element.nodes "Permalink to this definition")
            :   A sequence of MeshNode objects.

            elemShape[¶](#abaqus.Mesh.MeshPart.MeshElement.Element.elemShape "Permalink to this definition")
            :   A SymbolicConstant specifying the shape of the new element. Possible values are LINE2,
                LINE3, TRI3, TRI6, QUAD4, QUAD8, TET4, TET10, WEDGE6, WEDGE15, HEX8, and HEX20.

            label=`0`[¶](#abaqus.Mesh.MeshPart.MeshElement.Element.label "Permalink to this definition")
            :   An Int specifying the element label.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshElement.Element-returns "Permalink to this headline")
        :   **element** – A MeshElement object.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshElement.Element-return-type "Permalink to this headline")
        :   [`MeshElement`](#abaqus.Mesh.MeshPart.MeshElement "abaqus.Mesh.MeshPart.MeshElement (Python class) — Bases: object")

    connectivity : --is-rst--:py:class:`tuple`\[:py:class:`int`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L64-L67)[¶](#abaqus.Mesh.MeshPart.MeshElement.connectivity "Permalink to this definition")
    :   A tuple of Ints specifying the internal node indices that define the nodal connectivity.
        It is important to note the difference with OdbMeshElement object of ODB where the
        connectivity is node labels instead of node indices.

    getAdjacentElements()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L154-L163)[¶](#abaqus.Mesh.MeshPart.MeshElement.getAdjacentElements "Permalink to this definition")
    :   This method returns an array of element objects adjacent to the mesh element.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshElement.getAdjacentElements-returns "Permalink to this headline")
        :   A MeshElementArray object which is a sequence of MeshElement objects.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshElement.getAdjacentElements-return-type "Permalink to this headline")
        :   `MeshElementArray`

    getElemEdges()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L132-L141)[¶](#abaqus.Mesh.MeshPart.MeshElement.getElemEdges "Permalink to this definition")
    :   This method returns a tuple of unique element edge objects on the element.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshElement.getElemEdges-returns "Permalink to this headline")
        :   A tuple of MeshEdge objects.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshElement.getElemEdges-return-type "Permalink to this headline")
        :   `tuple[MeshEdge]`

    getElemFaces()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L143-L152)[¶](#abaqus.Mesh.MeshPart.MeshElement.getElemFaces "Permalink to this definition")
    :   This method returns a tuple of unique element face objects on the element.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshElement.getElemFaces-returns "Permalink to this headline")
        :   A tuple of MeshFace objects.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshElement.getElemFaces-return-type "Permalink to this headline")
        :   `tuple[MeshFace]`

    getElementsByFeatureEdge(*[angle](#abaqus.Mesh.MeshPart.MeshElement.getElementsByFeatureEdge.angle "abaqus.Mesh.MeshPart.MeshElement.getElementsByFeatureEdge.angle (Python parameter) — A float specifying the value of the face angle in degrees.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L165-L180)[¶](#abaqus.Mesh.MeshPart.MeshElement.getElementsByFeatureEdge "Permalink to this definition")
    :   This method returns an array of mesh element objects that are obtained by recursively finding
        adjacent elements along a feature edge with a face angle of less than or equal to the specified angle.

        Note

        Check [MeshElement.getElementsByFeatureEdge on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?contextscope=all#simaker-meshelementgetelementsbyfeatureedgepyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshElement.getElementsByFeatureEdge-parameters "Permalink to this headline")
        :   angle[¶](#abaqus.Mesh.MeshPart.MeshElement.getElementsByFeatureEdge.angle "Permalink to this definition")
            :   A float specifying the value of the face angle in degrees.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshElement.getElementsByFeatureEdge-returns "Permalink to this headline")
        :   A MeshElementArray object, which is a sequence of MeshElement objects.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshElement.getElementsByFeatureEdge-return-type "Permalink to this headline")
        :   `MeshElementArray`

    getNodes()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L113-L130)[¶](#abaqus.Mesh.MeshPart.MeshElement.getNodes "Permalink to this definition")
    :   This method returns a tuple of node objects of the element.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshElement.getNodes-returns "Permalink to this headline")
        :   A tuple of MeshNode objects.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshElement.getNodes-return-type "Permalink to this headline")
        :   `tuple[MeshNode]`

    instanceName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L61-L62)[¶](#abaqus.Mesh.MeshPart.MeshElement.instanceName "Permalink to this definition")
    :   A String specifying the name of the part instance that owns this element.

    label : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L55-L56)[¶](#abaqus.Mesh.MeshPart.MeshElement.label "Permalink to this definition")
    :   An Int specifying the element label.

    setValues(*[label](#abaqus.Mesh.MeshPart.MeshElement.setValues.label "abaqus.Mesh.MeshPart.MeshElement.setValues.label (Python parameter) — An Int specifying the element label.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L182-L193)[¶](#abaqus.Mesh.MeshPart.MeshElement.setValues "Permalink to this definition")
    :   This method modifies the MeshElement object.

        Note

        Check [MeshElement.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementpyc.htm?contextscope=all#simaker-meshelementsetvaluespyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshElement.setValues-parameters "Permalink to this headline")
        :   label=`None`[¶](#abaqus.Mesh.MeshPart.MeshElement.setValues.label "Permalink to this definition")
            :   An Int specifying the element label. This member may only be edited if the element
                belongs to an orphan mesh part. The specified label must be non-negative and must not be
                in use by any other element of the same part.

    type : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py)[¶](#abaqus.Mesh.MeshPart.MeshElement.type "Permalink to this definition")
    :   A SymbolicConstant specifying the Abaqus element code.

*class* MeshFace[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L6-L188)[¶](#abaqus.Mesh.MeshPart.MeshFace "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The MeshFace object refers to an element face. It has no constructor or members. A MeshFace object can be
    accessed via a MeshFaceArray or a repository on a part or part instance.

    Note

    This object can be accessed by:

    ```python
    import part
    mdb.models[name].parts[name].elementFaces[i]
    mdb.models[name].parts[name].elemFaces[i]
    import assembly
    mdb.models[name].rootAssembly.allInstances[name].elementFaces[i]
    mdb.models[name].rootAssembly.allInstances[name].elemFaces[i]
    mdb.models[name].rootAssembly.instances[name].elementFaces[i]
    mdb.models[name].rootAssembly.instances[name].elemFaces[i]
    ```

    Note

    Check [MeshFace on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?contextscope=all).

    Member Details:

    face : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L27-L28)[¶](#abaqus.Mesh.MeshPart.MeshFace.face "Permalink to this definition")
    :   An Int specifying a symbolic constant specifying the side of the element.

    getElemEdges()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L30-L39)[¶](#abaqus.Mesh.MeshPart.MeshFace.getElemEdges "Permalink to this definition")
    :   This method returns a tuple of unique element edges on the element face.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshFace.getElemEdges-returns "Permalink to this headline")
        :   **edges** – A tuple of MeshEdge objects

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshFace.getElemEdges-return-type "Permalink to this headline")
        :   `Sequence[MeshEdge]`

    getElemEdgesByFaceAngle(*[angle](#abaqus.Mesh.MeshPart.MeshFace.getElemEdgesByFaceAngle.angle "abaqus.Mesh.MeshPart.MeshFace.getElemEdgesByFaceAngle.angle (Python parameter) — A float specifying the value of the face angle in degrees.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L109-L124)[¶](#abaqus.Mesh.MeshPart.MeshFace.getElemEdgesByFaceAngle "Permalink to this definition")
    :   This method returns an array of element edge objects that are obtained by recursively finding
        adjacent element edges that are at an angle of less than or equal to the specified face angle.

        Note

        Check [MeshFace.getElemEdgesByFaceAngle on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?contextscope=all#simaker-meshfacegetelemedgesbyfaceanglepyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshFace.getElemEdgesByFaceAngle-parameters "Permalink to this headline")
        :   angle[¶](#abaqus.Mesh.MeshPart.MeshFace.getElemEdgesByFaceAngle.angle "Permalink to this definition")
            :   A float specifying the value of the face angle in degrees.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshFace.getElemEdgesByFaceAngle-returns "Permalink to this headline")
        :   **edges** – A MeshEdgeArray object, which is a sequence of MeshEdge objects.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshFace.getElemEdgesByFaceAngle-return-type "Permalink to this headline")
        :   `MeshEdgeArray`

    getElemFacesByFaceAngle(*[angle](#abaqus.Mesh.MeshPart.MeshFace.getElemFacesByFaceAngle.angle "abaqus.Mesh.MeshPart.MeshFace.getElemFacesByFaceAngle.angle (Python parameter) — A float specifying the value of the face angle.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L92-L107)[¶](#abaqus.Mesh.MeshPart.MeshFace.getElemFacesByFaceAngle "Permalink to this definition")
    :   This method returns an array of element face objects that are obtained by recursively finding
        adjacent element faces that are at an angle of less than or equal to the specified angle.

        Note

        Check [MeshFace.getElemFacesByFaceAngle on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?contextscope=all#simaker-meshfacegetelemfacesbyfaceanglepyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshFace.getElemFacesByFaceAngle-parameters "Permalink to this headline")
        :   angle[¶](#abaqus.Mesh.MeshPart.MeshFace.getElemFacesByFaceAngle.angle "Permalink to this definition")
            :   A float specifying the value of the face angle.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshFace.getElemFacesByFaceAngle-returns "Permalink to this headline")
        :   **faces** – A MeshFaceArray object, which is a sequence of MeshFace objects.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshFace.getElemFacesByFaceAngle-return-type "Permalink to this headline")
        :   `MeshFaceArray`

    getElemFacesByLayer(*[numLayers](#abaqus.Mesh.MeshPart.MeshFace.getElemFacesByLayer.numLayers "abaqus.Mesh.MeshPart.MeshFace.getElemFacesByLayer.numLayers (Python parameter) — A int specifying the value of the number of layers.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L173-L188)[¶](#abaqus.Mesh.MeshPart.MeshFace.getElemFacesByLayer "Permalink to this definition")
    :   This method returns an array of element face objects, obtained by traversing shell elements or the
        exterior of a solid mesh, and recursively finding adjacent element faces by layer.

        Note

        Check [MeshFace.getElemFacesByLayer on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?contextscope=all#simaker-meshfacegetelemfacesbylayerpyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshFace.getElemFacesByLayer-parameters "Permalink to this headline")
        :   numLayers[¶](#abaqus.Mesh.MeshPart.MeshFace.getElemFacesByLayer.numLayers "Permalink to this definition")
            :   A int specifying the value of the number of layers.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshFace.getElemFacesByLayer-returns "Permalink to this headline")
        :   **faces** – A MeshFaceArray object, which is a sequence of MeshFace objects.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshFace.getElemFacesByLayer-return-type "Permalink to this headline")
        :   `MeshFaceArray`

    getElemFacesByLimitingAngle(*[angle](#abaqus.Mesh.MeshPart.MeshFace.getElemFacesByLimitingAngle.angle "abaqus.Mesh.MeshPart.MeshFace.getElemFacesByLimitingAngle.angle (Python parameter) — A float specifying the value of the face angle in degrees.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L143-L159)[¶](#abaqus.Mesh.MeshPart.MeshFace.getElemFacesByLimitingAngle "Permalink to this definition")
    :   This method returns an array of element edge objects that are obtained by recursively finding
        adjacent element faces that are at an angle of less than or equal to the specified face angle with the
        seed face.

        Note

        Check [MeshFace.getElemFacesByLimitingAngle on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?contextscope=all#simaker-meshfacegetelemfacesbylimitinganglepyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshFace.getElemFacesByLimitingAngle-parameters "Permalink to this headline")
        :   angle[¶](#abaqus.Mesh.MeshPart.MeshFace.getElemFacesByLimitingAngle.angle "Permalink to this definition")
            :   A float specifying the value of the face angle in degrees.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshFace.getElemFacesByLimitingAngle-returns "Permalink to this headline")
        :   **faces** – A MeshFaceArray object, which is a sequence of MeshFace objects.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshFace.getElemFacesByLimitingAngle-return-type "Permalink to this headline")
        :   `MeshFaceArray`

    getElements()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L41-L50)[¶](#abaqus.Mesh.MeshPart.MeshFace.getElements "Permalink to this definition")
    :   This method returns a tuple of elements that share the element face.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshFace.getElements-returns "Permalink to this headline")
        :   **elements** – A tuple of MeshElement objects

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshFace.getElements-return-type "Permalink to this headline")
        :   `Sequence[MeshElement]`

    getElementsByFaceAngle(*[angle](#abaqus.Mesh.MeshPart.MeshFace.getElementsByFaceAngle.angle "abaqus.Mesh.MeshPart.MeshFace.getElementsByFaceAngle.angle (Python parameter) — A float specifying the value of the face angle.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L126-L141)[¶](#abaqus.Mesh.MeshPart.MeshFace.getElementsByFaceAngle "Permalink to this definition")
    :   This method returns an array of mesh Element objects that are obtained by recursively finding
        adjacent element faces that are at an angle of less than or equal to the specified angle.

        Note

        Check [MeshFace.getElementsByFaceAngle on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?contextscope=all#simaker-meshfacegetelementsbyfaceanglepyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshFace.getElementsByFaceAngle-parameters "Permalink to this headline")
        :   angle[¶](#abaqus.Mesh.MeshPart.MeshFace.getElementsByFaceAngle.angle "Permalink to this definition")
            :   A float specifying the value of the face angle.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshFace.getElementsByFaceAngle-returns "Permalink to this headline")
        :   **elements** – A MeshElementArray object, which is a sequence of MeshElement objects.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshFace.getElementsByFaceAngle-return-type "Permalink to this headline")
        :   `MeshElementArray`

    getElementsViaTopology()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L161-L171)[¶](#abaqus.Mesh.MeshPart.MeshFace.getElementsViaTopology "Permalink to this definition")
    :   This method returns an array of mesh Element objects that are obtained by recursively finding
        adjacent elements via topology.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshFace.getElementsViaTopology-returns "Permalink to this headline")
        :   **elements** – A MeshElementArray object, which is a sequence of MeshElement objects.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshFace.getElementsViaTopology-return-type "Permalink to this headline")
        :   `MeshElementArray`

    getNodes()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L52-L61)[¶](#abaqus.Mesh.MeshPart.MeshFace.getNodes "Permalink to this definition")
    :   This method returns a tuple of nodes on the element face.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshFace.getNodes-returns "Permalink to this headline")
        :   **nodes** – A tuple of MeshNode objects

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshFace.getNodes-return-type "Permalink to this headline")
        :   `Sequence[MeshNode]`

    getNodesByFaceAngle(*[angle](#abaqus.Mesh.MeshPart.MeshFace.getNodesByFaceAngle.angle "abaqus.Mesh.MeshPart.MeshFace.getNodesByFaceAngle.angle (Python parameter) — A float specifying the value of the face angle.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L63-L78)[¶](#abaqus.Mesh.MeshPart.MeshFace.getNodesByFaceAngle "Permalink to this definition")
    :   This method returns an array of mesh node objects that are obtained by recursively finding adjacent
        element faces that are at an angle of less than or equal to the specified angle.

        Note

        Check [MeshFace.getNodesByFaceAngle on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacepyc.htm?contextscope=all#simaker-meshfacegetnodesbyfaceanglepyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshFace.getNodesByFaceAngle-parameters "Permalink to this headline")
        :   angle[¶](#abaqus.Mesh.MeshPart.MeshFace.getNodesByFaceAngle.angle "Permalink to this definition")
            :   A float specifying the value of the face angle.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshFace.getNodesByFaceAngle-returns "Permalink to this headline")
        :   **nodes** – A MeshNodeArray object, which is a sequence of MeshNode objects

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshFace.getNodesByFaceAngle-return-type "Permalink to this headline")
        :   `MeshNodeArray`

    getNormal()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L80-L90)[¶](#abaqus.Mesh.MeshPart.MeshFace.getNormal "Permalink to this definition")
    :   This method returns the normal direction for the element face.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshFace.getNormal-returns "Permalink to this headline")
        :   **normal** – A tuple of 3 floats representing the unit normal vector. If the element face is
            collapsed such that a normal cannot be computed, a zero-length vector is returned.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshFace.getNormal-return-type "Permalink to this headline")
        :   `Sequence[float]`

    label : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L24-L25)[¶](#abaqus.Mesh.MeshPart.MeshFace.label "Permalink to this definition")
    :   An Int specifying an Int specifying the element label.

*class* MeshNode(*[coordinates](#abaqus.Mesh.MeshPart.MeshNode "abaqus.Mesh.MeshPart.MeshNode.__init__.coordinates (Python parameter)")*, *[localCsys](#abaqus.Mesh.MeshPart.MeshNode "abaqus.Mesh.MeshPart.MeshNode.__init__.localCsys (Python parameter)")=`None`*, *[label](#abaqus.Mesh.MeshPart.MeshNode "abaqus.Mesh.MeshPart.MeshNode.__init__.label (Python parameter)")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L16-L158)[¶](#abaqus.Mesh.MeshPart.MeshNode "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The MeshNode object refers to a node of a native mesh or an orphan mesh. A MeshNode object can be
    accessed via a part or part instance using an index that refers to the internal numbering of the node
    repository. The index does not refer to the node label.

    Note

    This object can be accessed by:

    ```python
    import part
    mdb.models[name].parts[name].allInternalSets[name].nodes[i]
    mdb.models[name].parts[name].allInternalSurfaces[name].nodes[i]
    mdb.models[name].parts[name].allSets[name].nodes[i]
    mdb.models[name].parts[name].allSurfaces[name].nodes[i]
    mdb.models[name].parts[name].nodes[i]
    mdb.models[name].parts[name].retainedNodes[i]
    mdb.models[name].parts[name].sets[name].nodes[i]
    mdb.models[name].parts[name].surfaces[name].nodes[i]
    import assembly
    mdb.models[name].rootAssembly.allInstances[name].nodes[i]
    mdb.models[name].rootAssembly.allInstances[name].sets[name].nodes[i]
    mdb.models[name].rootAssembly.allInstances[name].surfaces[name].nodes[i]
    mdb.models[name].rootAssembly.allInternalSets[name].nodes[i]
    mdb.models[name].rootAssembly.allInternalSurfaces[name].nodes[i]
    mdb.models[name].rootAssembly.allSets[name].nodes[i]
    mdb.models[name].rootAssembly.allSurfaces[name].nodes[i]
    mdb.models[name].rootAssembly.instances[name].nodes[i]
    mdb.models[name].rootAssembly.instances[name].sets[name].nodes[i]
    mdb.models[name].rootAssembly.instances[name].surfaces[name].nodes[i]
    mdb.models[name].rootAssembly.modelInstances[i].nodes[i]
    mdb.models[name].rootAssembly.modelInstances[i].sets[name].nodes[i]
    mdb.models[name].rootAssembly.modelInstances[i].surfaces[name].nodes[i]
    mdb.models[name].rootAssembly.nodes[i]
    mdb.models[name].rootAssembly.sets[name].nodes[i]
    mdb.models[name].rootAssembly.surfaces[name].nodes[i]
    ```

    Note

    Check [MeshNode on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?contextscope=all).

    Member Details:

    coordinates : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:class:`float`, :py:class:`float`][[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py)[¶](#abaqus.Mesh.MeshPart.MeshNode.coordinates "Permalink to this definition")
    :   A tuple of three Floats specifying the coordinates of the new node.

    getElemEdges()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L93-L102)[¶](#abaqus.Mesh.MeshPart.MeshNode.getElemEdges "Permalink to this definition")
    :   This method returns a tuple of element edge objects that share the node.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshNode.getElemEdges-returns "Permalink to this headline")
        :   **edges** – A tuple of MeshEdge objects

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshNode.getElemEdges-return-type "Permalink to this headline")
        :   `Sequence[MeshEdge]`

    getElemFaces()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L104-L113)[¶](#abaqus.Mesh.MeshPart.MeshNode.getElemFaces "Permalink to this definition")
    :   This method returns a tuple of element face objects that share the node.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshNode.getElemFaces-returns "Permalink to this headline")
        :   **faces** – A tuple of MeshFace objects

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshNode.getElemFaces-return-type "Permalink to this headline")
        :   `Sequence[MeshFace]`

    getElements()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L115-L124)[¶](#abaqus.Mesh.MeshPart.MeshNode.getElements "Permalink to this definition")
    :   This method returns a tuple of element objects that share the node.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshNode.getElements-returns "Permalink to this headline")
        :   **elements** – A tuple of MeshElement objects

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshNode.getElements-return-type "Permalink to this headline")
        :   `Sequence[MeshElement]`

    getNodesByFeatureEdge(*[angle](#abaqus.Mesh.MeshPart.MeshNode.getNodesByFeatureEdge.angle "abaqus.Mesh.MeshPart.MeshNode.getNodesByFeatureEdge.angle (Python parameter) — A float specifying the value of the face angle in degrees.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L126-L141)[¶](#abaqus.Mesh.MeshPart.MeshNode.getNodesByFeatureEdge "Permalink to this definition")
    :   This method returns an array of mesh node objects that are obtained by recursively finding adjacent
        nodes along a feature edge that are at an angle of less than or equal to the specified face angle.

        Note

        Check [MeshNode.getNodesByFeatureEdge on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?contextscope=all#simaker-meshnodegetnodesbyfeatureedgepyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshNode.getNodesByFeatureEdge-parameters "Permalink to this headline")
        :   angle[¶](#abaqus.Mesh.MeshPart.MeshNode.getNodesByFeatureEdge.angle "Permalink to this definition")
            :   A float specifying the value of the face angle in degrees.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshNode.getNodesByFeatureEdge-returns "Permalink to this headline")
        :   **nodes** – A MeshNodeArray object, which is a sequence of MeshNode objects

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshNode.getNodesByFeatureEdge-return-type "Permalink to this headline")
        :   `MeshNodeArray`

    instanceName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L56-L57)[¶](#abaqus.Mesh.MeshPart.MeshNode.instanceName "Permalink to this definition")
    :   A String specifying the name of the part instance that owns this node.

    label : --is-rst--:py:class:`int`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py)[¶](#abaqus.Mesh.MeshPart.MeshNode.label "Permalink to this definition")
    :   An Int specifying the node label.

    setValues(*[label](#abaqus.Mesh.MeshPart.MeshNode.setValues.label "abaqus.Mesh.MeshPart.MeshNode.setValues.label (Python parameter) — An Int specifying the node label.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L143-L158)[¶](#abaqus.Mesh.MeshPart.MeshNode.setValues "Permalink to this definition")
    :   This method modifies the MeshNode object.

        Note

        Check [MeshNode.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodepyc.htm?contextscope=all#simaker-meshnodesetvaluespyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshNode.setValues-parameters "Permalink to this headline")
        :   label=`None`[¶](#abaqus.Mesh.MeshPart.MeshNode.setValues.label "Permalink to this definition")
            :   An Int specifying the node label. This member may only be edited if the node belongs to
                an orphan mesh part. The specified label must be non-negative and must not be in use by
                any other node of the same part.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshNode.setValues-returns "Permalink to this headline")
        :   None

*class* MeshElementArray(*[elements](#abaqus.Mesh.MeshElementArray.MeshElementArray "abaqus.Mesh.MeshElementArray.MeshElementArray.__init__.elements (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshElementArray.py#L16-L255)[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray "Permalink to this definition")
:   Bases: [`List`](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")[[`MeshElement`](#abaqus.Mesh.MeshPart.MeshElement "abaqus.Mesh.MeshElement.MeshElement (Python class)")]

    The MeshElementArray is a sequence of MeshElement objects.

    Note

    This object can be accessed by:

    ```python
    import part
    mdb.models[name].parts[name].allInternalSets[name].elements
    mdb.models[name].parts[name].allInternalSurfaces[name].elements
    mdb.models[name].parts[name].allSets[name].elements
    mdb.models[name].parts[name].allSurfaces[name].elements
    mdb.models[name].parts[name].elements
    mdb.models[name].parts[name].sets[name].elements
    mdb.models[name].parts[name].surfaces[name].elements
    import assembly
    mdb.models[name].rootAssembly.allInstances[name].elements
    mdb.models[name].rootAssembly.allInstances[name].sets[name].elements
    mdb.models[name].rootAssembly.allInstances[name].surfaces[name].elements
    mdb.models[name].rootAssembly.allInternalSets[name].elements
    mdb.models[name].rootAssembly.allInternalSurfaces[name].elements
    mdb.models[name].rootAssembly.allSets[name].elements
    mdb.models[name].rootAssembly.allSurfaces[name].elements
    mdb.models[name].rootAssembly.elements
    mdb.models[name].rootAssembly.instances[name].elements
    mdb.models[name].rootAssembly.instances[name].sets[name].elements
    mdb.models[name].rootAssembly.instances[name].surfaces[name].elements
    mdb.models[name].rootAssembly.modelInstances[i].elements
    mdb.models[name].rootAssembly.modelInstances[i].sets[name].elements
    mdb.models[name].rootAssembly.modelInstances[i].surfaces[name].elements
    mdb.models[name].rootAssembly.sets[name].elements
    mdb.models[name].rootAssembly.surfaces[name].elements
    ```

    Note

    Check [MeshElementArray on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementarraypyc.htm?contextscope=all).

    Member Details:

    getBoundingBox()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshElementArray.py#L189-L204)[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getBoundingBox "Permalink to this definition")
    :   This method returns a dictionary of two tuples representing minimum and maximum boundary values of
        the bounding box of the minimum size containing the element sequence.

        Returns:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getBoundingBox-returns "Permalink to this headline")
        :   A Dictionary object with the following items:

            * **low**: a tuple of three floats representing the minimum x, y, and z boundary values of
              the bounding box.
            * **high**: a tuple of three floats representing the maximum x, y, and z boundary values of
              the bounding box.

        Return type:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getBoundingBox-return-type "Permalink to this headline")
        :   `dict[str`, `tuple[float`, [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"), `float]]`

    getByBoundingBox(*[xMin](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingBox.xMin "abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingBox.xMin (Python parameter) — A float specifying the minimum X boundary of the bounding box.")=`0`*, *[yMin](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingBox.yMin "abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingBox.yMin (Python parameter) — A float specifying the minimum Y boundary of the bounding box.")=`0`*, *[zMin](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingBox.zMin "abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingBox.zMin (Python parameter) — A float specifying the minimum Z boundary of the bounding box.")=`0`*, *[xMax](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingBox.xMax "abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingBox.xMax (Python parameter) — A float specifying the maximum X boundary of the bounding box.")=`0`*, *[yMax](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingBox.yMax "abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingBox.yMax (Python parameter) — A float specifying the maximum Y boundary of the bounding box.")=`0`*, *[zMax](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingBox.zMax "abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingBox.zMax (Python parameter) — A float specifying the maximum Z boundary of the bounding box.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshElementArray.py#L116-L148)[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingBox "Permalink to this definition")
    :   This method returns an array of element objects that lie within the specified bounding box.

        Note

        Check [MeshElementArray.getByBoundingBox on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementarraypyc.htm?contextscope=all#simaker-meshelementarraygetbyboundingboxpyc).

        Parameters:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingBox-parameters "Permalink to this headline")
        :   xMin=`0`[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingBox.xMin "Permalink to this definition")
            :   A float specifying the minimum X boundary of the bounding box.

            yMin=`0`[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingBox.yMin "Permalink to this definition")
            :   A float specifying the minimum Y boundary of the bounding box.

            zMin=`0`[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingBox.zMin "Permalink to this definition")
            :   A float specifying the minimum Z boundary of the bounding box.

            xMax=`0`[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingBox.xMax "Permalink to this definition")
            :   A float specifying the maximum X boundary of the bounding box.

            yMax=`0`[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingBox.yMax "Permalink to this definition")
            :   A float specifying the maximum Y boundary of the bounding box.

            zMax=`0`[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingBox.zMax "Permalink to this definition")
            :   A float specifying the maximum Z boundary of the bounding box.

        Returns:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingBox-returns "Permalink to this headline")
        :   A MeshElementArray object, which is a sequence of MeshElement objects.

        Return type:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingBox-return-type "Permalink to this headline")
        :   [`MeshElementArray`](#abaqus.Mesh.MeshElementArray.MeshElementArray "abaqus.Mesh.MeshElementArray.MeshElementArray (Python class) — Bases: List[MeshElement]")

    getByBoundingCylinder(*[center1](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingCylinder.center1 "abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingCylinder.center1 (Python parameter) — A tuple of the X-, Y-, and Z-coordinates of the center of the first end of the cylinder.")*, *[center2](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingCylinder.center2 "abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingCylinder.center2 (Python parameter) — A tuple of the X-, Y-, and Z-coordinates of the center of the second end of the cylinder.")*, *[radius](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingCylinder.radius "abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingCylinder.radius (Python parameter) — A float specifying the radius of the cylinder.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshElementArray.py#L150-L169)[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingCylinder "Permalink to this definition")
    :   This method returns an array of element objects that lie within the specified bounding cylinder.

        Note

        Check [MeshElementArray.getByBoundingCylinder on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementarraypyc.htm?contextscope=all#simaker-meshelementarraygetbyboundingcylinderpyc).

        Parameters:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingCylinder-parameters "Permalink to this headline")
        :   center1[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingCylinder.center1 "Permalink to this definition")
            :   A tuple of the X-, Y-, and Z-coordinates of the center of the first end of the cylinder.

            center2[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingCylinder.center2 "Permalink to this definition")
            :   A tuple of the X-, Y-, and Z-coordinates of the center of the second end of the
                cylinder.

            radius[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingCylinder.radius "Permalink to this definition")
            :   A float specifying the radius of the cylinder.

        Returns:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingCylinder-returns "Permalink to this headline")
        :   A MeshElementArray object, which is a sequence of MeshElement objects.

        Return type:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingCylinder-return-type "Permalink to this headline")
        :   [`MeshElementArray`](#abaqus.Mesh.MeshElementArray.MeshElementArray "abaqus.Mesh.MeshElementArray.MeshElementArray (Python class) — Bases: List[MeshElement]")

    getByBoundingSphere(*[center](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingSphere.center "abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingSphere.center (Python parameter) — A tuple of the X-, Y-, and Z-coordinates of the center of the sphere.")*, *[radius](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingSphere.radius "abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingSphere.radius (Python parameter) — A float specifying the radius of the sphere.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshElementArray.py#L171-L187)[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingSphere "Permalink to this definition")
    :   This method returns an array of element objects that lie within the specified bounding sphere.

        Note

        Check [MeshElementArray.getByBoundingSphere on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementarraypyc.htm?contextscope=all#simaker-meshelementarraygetbyboundingspherepyc).

        Parameters:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingSphere-parameters "Permalink to this headline")
        :   center[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingSphere.center "Permalink to this definition")
            :   A tuple of the X-, Y-, and Z-coordinates of the center of the sphere.

            radius[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingSphere.radius "Permalink to this definition")
            :   A float specifying the radius of the sphere.

        Returns:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingSphere-returns "Permalink to this headline")
        :   A MeshElementArray object, which is a sequence of MeshElement objects.

        Return type:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getByBoundingSphere-return-type "Permalink to this headline")
        :   [`MeshElementArray`](#abaqus.Mesh.MeshElementArray.MeshElementArray "abaqus.Mesh.MeshElementArray.MeshElementArray (Python class) — Bases: List[MeshElement]")

    getExteriorEdges()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshElementArray.py#L227-L240)[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getExteriorEdges "Permalink to this definition")
    :   This method returns the edges on the exterior of the faces in the FaceArray. That is, it returns the
        edges that are referenced by exactly one of the faces in the sequence.

        New in version 2018: The `getExteriorEdges` method was added.

        Returns:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getExteriorEdges-returns "Permalink to this headline")
        :   An EdgeArray object specifying the exterior edges.

        Return type:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getExteriorEdges-return-type "Permalink to this headline")
        :   `EdgeArray`

    getExteriorFaces()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshElementArray.py#L242-L255)[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getExteriorFaces "Permalink to this definition")
    :   This method returns the cell faces on the exterior of the CellArray. That is, it returns the faces
        that are referenced by exactly one of the cells in the sequence.

        New in version 2018: The `getExteriorFaces` method was added.

        Returns:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getExteriorFaces-returns "Permalink to this headline")
        :   A FaceArray object representing the faces on the exterior of the cells.

        Return type:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getExteriorFaces-return-type "Permalink to this headline")
        :   `FaceArray`

    getFromLabel(*[label](#abaqus.Mesh.MeshElementArray.MeshElementArray.getFromLabel.label "abaqus.Mesh.MeshElementArray.MeshElementArray.getFromLabel.label (Python parameter) — An Int specifying the label of the object.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshElementArray.py#L71-L85)[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getFromLabel "Permalink to this definition")
    :   This method returns the object in the MeshElementArray with the given label.

        Note

        Check [MeshElementArray.getFromLabel on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementarraypyc.htm?contextscope=all#simaker-meshelementarraygetfromlabelpyc).

        Parameters:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getFromLabel-parameters "Permalink to this headline")
        :   label[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getFromLabel.label "Permalink to this definition")
            :   An Int specifying the label of the object.

        Returns:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getFromLabel-returns "Permalink to this headline")
        :   A MeshElement object.

        Return type:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getFromLabel-return-type "Permalink to this headline")
        :   `MeshElement`

    getMask()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshElementArray.py#L105-L114)[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getMask "Permalink to this definition")
    :   This method returns a string specifying the object or objects.

        Returns:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getMask-returns "Permalink to this headline")
        :   A String specifying the object or objects.

        Return type:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getMask-return-type "Permalink to this headline")
        :   [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    getSequenceFromMask(*[mask](#abaqus.Mesh.MeshElementArray.MeshElementArray.getSequenceFromMask.mask "abaqus.Mesh.MeshElementArray.MeshElementArray.getSequenceFromMask.mask (Python parameter) — A String specifying the object or objects.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshElementArray.py#L87-L103)[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getSequenceFromMask "Permalink to this definition")
    :   This method returns the objects in the MeshElementArray identified using the specified
        **mask**. This command is generated when the JournalOptions are set to COMPRESSEDINDEX.
        When a large number of objects are involved, this method is highly efficient.

        Note

        Check [MeshElementArray.getSequenceFromMask on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementarraypyc.htm?contextscope=all#simaker-meshelementarraygetsequencefrommaskpyc).

        Parameters:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getSequenceFromMask-parameters "Permalink to this headline")
        :   mask[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getSequenceFromMask.mask "Permalink to this definition")
            :   A String specifying the object or objects.

        Returns:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getSequenceFromMask-returns "Permalink to this headline")
        :   A MeshElementArray object.

        Return type:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.getSequenceFromMask-return-type "Permalink to this headline")
        :   [`MeshElementArray`](#abaqus.Mesh.MeshElementArray.MeshElementArray "abaqus.Mesh.MeshElementArray.MeshElementArray (Python class) — Bases: List[MeshElement]")

    sequenceFromLabels(*[labels](#abaqus.Mesh.MeshElementArray.MeshElementArray.sequenceFromLabels.labels "abaqus.Mesh.MeshElementArray.MeshElementArray.sequenceFromLabels.labels (Python parameter) — A sequence of Ints specifying the labels.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshElementArray.py#L206-L225)[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.sequenceFromLabels "Permalink to this definition")
    :   This method returns the objects in the MeshElementArray identified using the specified labels.

        Note

        Check [MeshElementArray.sequenceFromLabels on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshelementarraypyc.htm?contextscope=all#simaker-meshelementarraysequencefromlabelspyc).

        Parameters:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.sequenceFromLabels-parameters "Permalink to this headline")
        :   labels[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.sequenceFromLabels.labels "Permalink to this definition")
            :   A sequence of Ints specifying the labels.

        Returns:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.sequenceFromLabels-returns "Permalink to this headline")
        :   A MeshElementArray object.

        Return type:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.sequenceFromLabels-return-type "Permalink to this headline")
        :   [`MeshElementArray`](#abaqus.Mesh.MeshElementArray.MeshElementArray "abaqus.Mesh.MeshElementArray.MeshElementArray (Python class) — Bases: List[MeshElement]")

        Raises:[¶](#abaqus.Mesh.MeshElementArray.MeshElementArray.sequenceFromLabels-raises "Permalink to this headline")
        :   **Error** – The mask results in an empty sequence, An exception occurs if the resulting sequence is empty.

*class* MeshEdgeArray(*[elemEdges](#abaqus.Mesh.MeshEdgeArray.MeshEdgeArray "abaqus.Mesh.MeshEdgeArray.MeshEdgeArray.__init__.elemEdges (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshEdgeArray.py#L10-L79)[¶](#abaqus.Mesh.MeshEdgeArray.MeshEdgeArray "Permalink to this definition")
:   Bases: [`List`](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")[[`MeshEdge`](#abaqus.Mesh.MeshPart.MeshEdge "abaqus.Mesh.MeshEdge.MeshEdge (Python class)")]

    The MeshEdgeArray is a sequence of MeshEdge objects.

    Note

    This object can be accessed by:

    ```python
    import part
    mdb.models[name].parts[name].elementEdges
    import assembly
    mdb.models[name].rootAssembly.allInstances[name].elementEdges
    mdb.models[name].rootAssembly.instances[name].elementEdges
    ```

    Note

    Check [MeshEdgeArray on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgearraypyc.htm?contextscope=all).

    Member Details:

    getMask()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshEdgeArray.py#L70-L79)[¶](#abaqus.Mesh.MeshEdgeArray.MeshEdgeArray.getMask "Permalink to this definition")
    :   This method returns a string specifying the object or objects.

        Returns:[¶](#abaqus.Mesh.MeshEdgeArray.MeshEdgeArray.getMask-returns "Permalink to this headline")
        :   A String specifying the object or objects.

        Return type:[¶](#abaqus.Mesh.MeshEdgeArray.MeshEdgeArray.getMask-return-type "Permalink to this headline")
        :   [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    getSequenceFromMask(*[mask](#abaqus.Mesh.MeshEdgeArray.MeshEdgeArray.getSequenceFromMask.mask "abaqus.Mesh.MeshEdgeArray.MeshEdgeArray.getSequenceFromMask.mask (Python parameter) — A String specifying the object or objects.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshEdgeArray.py#L48-L68)[¶](#abaqus.Mesh.MeshEdgeArray.MeshEdgeArray.getSequenceFromMask "Permalink to this definition")
    :   This method returns the objects in the MeshEdgeArray identified using the specified
        **mask**. When large number of objects are involved, this method is highly efficient.

        Note

        Check [MeshEdgeArray.getSequenceFromMask on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshedgearraypyc.htm?contextscope=all#simaker-meshedgearraygetsequencefrommaskpyc).

        Parameters:[¶](#abaqus.Mesh.MeshEdgeArray.MeshEdgeArray.getSequenceFromMask-parameters "Permalink to this headline")
        :   mask[¶](#abaqus.Mesh.MeshEdgeArray.MeshEdgeArray.getSequenceFromMask.mask "Permalink to this definition")
            :   A String specifying the object or objects.

        Returns:[¶](#abaqus.Mesh.MeshEdgeArray.MeshEdgeArray.getSequenceFromMask-returns "Permalink to this headline")
        :   A MeshEdgeArray object.

        Return type:[¶](#abaqus.Mesh.MeshEdgeArray.MeshEdgeArray.getSequenceFromMask-return-type "Permalink to this headline")
        :   [`MeshEdgeArray`](#abaqus.Mesh.MeshEdgeArray.MeshEdgeArray "abaqus.Mesh.MeshEdgeArray.MeshEdgeArray (Python class) — Bases: List[MeshEdge]")

        Raises:[¶](#abaqus.Mesh.MeshEdgeArray.MeshEdgeArray.getSequenceFromMask-raises "Permalink to this headline")
        :   **Error** – The mask results in an empty sequence, An exception occurs if the resulting sequence is empty.

*class* MeshFaceArray(*[elemFaces](#abaqus.Mesh.MeshFaceArray.MeshFaceArray "abaqus.Mesh.MeshFaceArray.MeshFaceArray.__init__.elemFaces (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshFaceArray.py#L10-L79)[¶](#abaqus.Mesh.MeshFaceArray.MeshFaceArray "Permalink to this definition")
:   Bases: [`List`](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")[[`MeshFace`](#abaqus.Mesh.MeshPart.MeshFace "abaqus.Mesh.MeshFace.MeshFace (Python class)")]

    The MeshFaceArray is a sequence of MeshFace objects.

    Note

    This object can be accessed by:

    ```python
    import part
    mdb.models[name].parts[name].elementFaces
    import assembly
    mdb.models[name].rootAssembly.allInstances[name].elementFaces
    mdb.models[name].rootAssembly.instances[name].elementFaces
    ```

    Note

    Check [MeshFaceArray on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacearraypyc.htm?contextscope=all).

    Member Details:

    getMask()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshFaceArray.py#L70-L79)[¶](#abaqus.Mesh.MeshFaceArray.MeshFaceArray.getMask "Permalink to this definition")
    :   This method returns a string specifying the object or objects.

        Returns:[¶](#abaqus.Mesh.MeshFaceArray.MeshFaceArray.getMask-returns "Permalink to this headline")
        :   A String specifying the object or objects.

        Return type:[¶](#abaqus.Mesh.MeshFaceArray.MeshFaceArray.getMask-return-type "Permalink to this headline")
        :   [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    getSequenceFromMask(*[mask](#abaqus.Mesh.MeshFaceArray.MeshFaceArray.getSequenceFromMask.mask "abaqus.Mesh.MeshFaceArray.MeshFaceArray.getSequenceFromMask.mask (Python parameter) — A String specifying the object or objects.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshFaceArray.py#L48-L68)[¶](#abaqus.Mesh.MeshFaceArray.MeshFaceArray.getSequenceFromMask "Permalink to this definition")
    :   This method returns the objects in the MeshFaceArray identified using the specified
        **mask**. When large number of objects are involved, this method is highly efficient.

        Note

        Check [MeshFaceArray.getSequenceFromMask on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshfacearraypyc.htm?contextscope=all#simaker-meshfacearraygetsequencefrommaskpyc).

        Parameters:[¶](#abaqus.Mesh.MeshFaceArray.MeshFaceArray.getSequenceFromMask-parameters "Permalink to this headline")
        :   mask[¶](#abaqus.Mesh.MeshFaceArray.MeshFaceArray.getSequenceFromMask.mask "Permalink to this definition")
            :   A String specifying the object or objects.

        Returns:[¶](#abaqus.Mesh.MeshFaceArray.MeshFaceArray.getSequenceFromMask-returns "Permalink to this headline")
        :   A MeshFaceArray object.

        Return type:[¶](#abaqus.Mesh.MeshFaceArray.MeshFaceArray.getSequenceFromMask-return-type "Permalink to this headline")
        :   [`MeshFaceArray`](#abaqus.Mesh.MeshFaceArray.MeshFaceArray "abaqus.Mesh.MeshFaceArray.MeshFaceArray (Python class) — Bases: List[MeshFace]")

        Raises:[¶](#abaqus.Mesh.MeshFaceArray.MeshFaceArray.getSequenceFromMask-raises "Permalink to this headline")
        :   **Error** – The mask results in an empty sequence, An exception occurs if the resulting sequence is empty.

*class* MeshNodeArray(*[nodes](#abaqus.Mesh.MeshNodeArray.MeshNodeArray "abaqus.Mesh.MeshNodeArray.MeshNodeArray.__init__.nodes (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshNodeArray.py#L10-L254)[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray "Permalink to this definition")
:   Bases: [`List`](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.13)")[[`MeshNode`](#abaqus.Mesh.MeshPart.MeshNode "abaqus.Mesh.MeshNode.MeshNode (Python class)")]

    The MeshNodeArray is a sequence of MeshNode objects.

    Note

    This object can be accessed by:

    ```python
    import part
    mdb.models[name].parts[name].allInternalSets[name].nodes
    mdb.models[name].parts[name].allInternalSurfaces[name].nodes
    mdb.models[name].parts[name].allSets[name].nodes
    mdb.models[name].parts[name].allSurfaces[name].nodes
    mdb.models[name].parts[name].nodes
    mdb.models[name].parts[name].retainedNodes
    mdb.models[name].parts[name].sets[name].nodes
    mdb.models[name].parts[name].surfaces[name].nodes
    import assembly
    mdb.models[name].rootAssembly.allInstances[name].nodes
    mdb.models[name].rootAssembly.allInstances[name].sets[name].nodes
    mdb.models[name].rootAssembly.allInstances[name].surfaces[name].nodes
    mdb.models[name].rootAssembly.allInternalSets[name].nodes
    mdb.models[name].rootAssembly.allInternalSurfaces[name].nodes
    mdb.models[name].rootAssembly.allSets[name].nodes
    mdb.models[name].rootAssembly.allSurfaces[name].nodes
    mdb.models[name].rootAssembly.instances[name].nodes
    mdb.models[name].rootAssembly.instances[name].sets[name].nodes
    mdb.models[name].rootAssembly.instances[name].surfaces[name].nodes
    mdb.models[name].rootAssembly.modelInstances[i].nodes
    mdb.models[name].rootAssembly.modelInstances[i].sets[name].nodes
    mdb.models[name].rootAssembly.modelInstances[i].surfaces[name].nodes
    mdb.models[name].rootAssembly.nodes
    mdb.models[name].rootAssembly.sets[name].nodes
    mdb.models[name].rootAssembly.surfaces[name].nodes
    ```

    Note

    Check [MeshNodeArray on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodearraypyc.htm?contextscope=all).

    Member Details:

    getBoundingBox()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshNodeArray.py#L189-L207)[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getBoundingBox "Permalink to this definition")
    :   This method returns a dictionary of two tuples representing minimum and maximum boundary values of
        the bounding box of the minimum size containing the node sequence.

        Returns:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getBoundingBox-returns "Permalink to this headline")
        :   A Dictionary object with the following items:

            * **low**: a tuple of three floats representing the minimum x, y and z boundary values of
              the bounding box.
            * **high**: a tuple of three floats representing the maximum x, y and z boundary values of
              the bounding box.

        Return type:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getBoundingBox-return-type "Permalink to this headline")
        :   `dict[str`, `tuple[float`, [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)"), `float]]`

    getByBoundingBox(*[xMin](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingBox.xMin "abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingBox.xMin (Python parameter) — A float specifying the minimum X boundary of the bounding box.")=`0`*, *[yMin](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingBox.yMin "abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingBox.yMin (Python parameter) — A float specifying the minimum Y boundary of the bounding box.")=`0`*, *[zMin](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingBox.zMin "abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingBox.zMin (Python parameter) — A float specifying the minimum Z boundary of the bounding box.")=`0`*, *[xMax](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingBox.xMax "abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingBox.xMax (Python parameter) — A float specifying the maximum X boundary of the bounding box.")=`0`*, *[yMax](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingBox.yMax "abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingBox.yMax (Python parameter) — A float specifying the maximum Y boundary of the bounding box.")=`0`*, *[zMax](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingBox.zMax "abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingBox.zMax (Python parameter) — A float specifying the maximum Z boundary of the bounding box.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshNodeArray.py#L111-L143)[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingBox "Permalink to this definition")
    :   This method returns an array of nodes that lie within the specified bounding box.

        Note

        Check [MeshNodeArray.getByBoundingBox on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodearraypyc.htm?contextscope=all#simaker-meshnodearraygetbyboundingboxpyc).

        Parameters:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingBox-parameters "Permalink to this headline")
        :   xMin=`0`[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingBox.xMin "Permalink to this definition")
            :   A float specifying the minimum X boundary of the bounding box.

            yMin=`0`[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingBox.yMin "Permalink to this definition")
            :   A float specifying the minimum Y boundary of the bounding box.

            zMin=`0`[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingBox.zMin "Permalink to this definition")
            :   A float specifying the minimum Z boundary of the bounding box.

            xMax=`0`[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingBox.xMax "Permalink to this definition")
            :   A float specifying the maximum X boundary of the bounding box.

            yMax=`0`[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingBox.yMax "Permalink to this definition")
            :   A float specifying the maximum Y boundary of the bounding box.

            zMax=`0`[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingBox.zMax "Permalink to this definition")
            :   A float specifying the maximum Z boundary of the bounding box.

        Returns:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingBox-returns "Permalink to this headline")
        :   A MeshNodeArray object, which is a sequence of MeshNode objects.

        Return type:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingBox-return-type "Permalink to this headline")
        :   [`MeshNodeArray`](#abaqus.Mesh.MeshNodeArray.MeshNodeArray "abaqus.Mesh.MeshNodeArray.MeshNodeArray (Python class) — Bases: List[MeshNode]")

    getByBoundingCylinder(*[center1](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingCylinder.center1 "abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingCylinder.center1 (Python parameter) — A tuple of the X-, Y-, and Z-coordinates of the center of the first end of the cylinder.")*, *[center2](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingCylinder.center2 "abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingCylinder.center2 (Python parameter) — A tuple of the X-, Y-, and Z-coordinates of the center of the second end of the cylinder.")*, *[radius](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingCylinder.radius "abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingCylinder.radius (Python parameter) — A float specifying the radius of the cylinder.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshNodeArray.py#L145-L169)[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingCylinder "Permalink to this definition")
    :   This method returns an array of node objects that lie within the specified bounding cylinder.

        Note

        Check [MeshNodeArray.getByBoundingCylinder on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodearraypyc.htm?contextscope=all#simaker-meshnodearraygetbyboundingcylinderpyc).

        Parameters:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingCylinder-parameters "Permalink to this headline")
        :   center1[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingCylinder.center1 "Permalink to this definition")
            :   A tuple of the X-, Y-, and Z-coordinates of the center of the first end of the cylinder.

            center2[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingCylinder.center2 "Permalink to this definition")
            :   A tuple of the X-, Y-, and Z-coordinates of the center of the second end of the
                cylinder.

            radius[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingCylinder.radius "Permalink to this definition")
            :   A float specifying the radius of the cylinder.

        Returns:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingCylinder-returns "Permalink to this headline")
        :   A MeshNodeArray object, which is a sequence of MeshNode objects.

        Return type:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingCylinder-return-type "Permalink to this headline")
        :   [`MeshNodeArray`](#abaqus.Mesh.MeshNodeArray.MeshNodeArray "abaqus.Mesh.MeshNodeArray.MeshNodeArray (Python class) — Bases: List[MeshNode]")

    getByBoundingSphere(*[center](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingSphere.center "abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingSphere.center (Python parameter) — A tuple of the X-, Y-, and Z-coordinates of the center of the sphere.")*, *[radius](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingSphere.radius "abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingSphere.radius (Python parameter) — A float specifying the radius of the sphere.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshNodeArray.py#L171-L187)[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingSphere "Permalink to this definition")
    :   This method returns an array of node objects that lie within the specified bounding sphere.

        Note

        Check [MeshNodeArray.getByBoundingSphere on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodearraypyc.htm?contextscope=all#simaker-meshnodearraygetbyboundingspherepyc).

        Parameters:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingSphere-parameters "Permalink to this headline")
        :   center[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingSphere.center "Permalink to this definition")
            :   A tuple of the X-, Y-, and Z-coordinates of the center of the sphere.

            radius[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingSphere.radius "Permalink to this definition")
            :   A float specifying the radius of the sphere.

        Returns:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingSphere-returns "Permalink to this headline")
        :   A MeshNodeArray object, which is a sequence of MeshNode objects.

        Return type:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getByBoundingSphere-return-type "Permalink to this headline")
        :   [`MeshNodeArray`](#abaqus.Mesh.MeshNodeArray.MeshNodeArray "abaqus.Mesh.MeshNodeArray.MeshNodeArray (Python class) — Bases: List[MeshNode]")

    getClosest(*[coordinates](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getClosest.coordinates "abaqus.Mesh.MeshNodeArray.MeshNodeArray.getClosest.coordinates (Python parameter) — A point defined by x, y, and z values or a list of such points.")*, *[numToFind](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getClosest.numToFind "abaqus.Mesh.MeshNodeArray.MeshNodeArray.getClosest.numToFind (Python parameter) — The number of nodes to find for each given point.")=`1`*, *[searchTolerance](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getClosest.searchTolerance "abaqus.Mesh.MeshNodeArray.MeshNodeArray.getClosest.searchTolerance (Python parameter) — A float specifying a search radius for each point.")=`0.0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshNodeArray.py#L209-L233)[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getClosest "Permalink to this definition")
    :   This method returns the node or nodes closest to the given point or set of points.

        Note

        Check [MeshNodeArray.getClosest on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodearraypyc.htm?contextscope=all#simaker-meshnodearraygetclosestpyc).

        Parameters:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getClosest-parameters "Permalink to this headline")
        :   coordinates[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getClosest.coordinates "Permalink to this definition")
            :   A point defined by x, y, and z values or a list of such points.

            numToFind=`1`[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getClosest.numToFind "Permalink to this definition")
            :   The number of nodes to find for each given point. For example, if **numToFind** is 2, then
                the 2 closest points, if available and within **searchTolerance**, will be returned in
                order of proximity for each input point. The default is 1.

            searchTolerance=`0.0`[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getClosest.searchTolerance "Permalink to this definition")
            :   A float specifying a search radius for each point. By default, no search radius is
                defined, and all nodes in the sequence will be searched.

        Returns:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getClosest-returns "Permalink to this headline")
        :   A MeshNode, or a list of MeshNode objects, or a list of lists of MeshNode objects,
            depending on the number of points given and the number of nodes requested.

        Return type:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getClosest-return-type "Permalink to this headline")
        :   `MeshNode | list[MeshNode]`

    getFromLabel(*[label](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getFromLabel.label "abaqus.Mesh.MeshNodeArray.MeshNodeArray.getFromLabel.label (Python parameter) — An Int specifying the label of the object.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshNodeArray.py#L66-L80)[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getFromLabel "Permalink to this definition")
    :   This method returns the object in the MeshNodeArray with the given label.

        Note

        Check [MeshNodeArray.getFromLabel on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodearraypyc.htm?contextscope=all#simaker-meshnodearraygetfromlabelpyc).

        Parameters:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getFromLabel-parameters "Permalink to this headline")
        :   label[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getFromLabel.label "Permalink to this definition")
            :   An Int specifying the label of the object.

        Returns:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getFromLabel-returns "Permalink to this headline")
        :   A MeshNode object.

        Return type:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getFromLabel-return-type "Permalink to this headline")
        :   `MeshNode`

    getMask()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshNodeArray.py#L100-L109)[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getMask "Permalink to this definition")
    :   This method returns a string specifying the object or objects.

        Returns:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getMask-returns "Permalink to this headline")
        :   A String specifying the object or objects.

        Return type:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getMask-return-type "Permalink to this headline")
        :   [`str`](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")

    getSequenceFromMask(*[mask](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getSequenceFromMask.mask "abaqus.Mesh.MeshNodeArray.MeshNodeArray.getSequenceFromMask.mask (Python parameter) — A String specifying the object or objects.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshNodeArray.py#L82-L98)[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getSequenceFromMask "Permalink to this definition")
    :   This method returns the objects in the MeshNodeArray identified using the specified
        **mask**. This command is generated when the JournalOptions are set to COMPRESSEDINDEX.
        When a large number of objects are involved, this method is highly efficient.

        Note

        Check [MeshNodeArray.getSequenceFromMask on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodearraypyc.htm?contextscope=all#simaker-meshnodearraygetsequencefrommaskpyc).

        Parameters:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getSequenceFromMask-parameters "Permalink to this headline")
        :   mask[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getSequenceFromMask.mask "Permalink to this definition")
            :   A String specifying the object or objects.

        Returns:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getSequenceFromMask-returns "Permalink to this headline")
        :   A MeshNodeArray object.

        Return type:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.getSequenceFromMask-return-type "Permalink to this headline")
        :   [`MeshNodeArray`](#abaqus.Mesh.MeshNodeArray.MeshNodeArray "abaqus.Mesh.MeshNodeArray.MeshNodeArray (Python class) — Bases: List[MeshNode]")

    sequenceFromLabels(*[labels](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.sequenceFromLabels.labels "abaqus.Mesh.MeshNodeArray.MeshNodeArray.sequenceFromLabels.labels (Python parameter) — A sequence of Ints specifying the labels.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshNodeArray.py#L235-L254)[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.sequenceFromLabels "Permalink to this definition")
    :   This method returns the objects in the MeshNodeArray identified using the specified labels.

        Note

        Check [MeshNodeArray.sequenceFromLabels on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshnodearraypyc.htm?contextscope=all#simaker-meshnodearraysequencefromlabelspyc).

        Parameters:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.sequenceFromLabels-parameters "Permalink to this headline")
        :   labels[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.sequenceFromLabels.labels "Permalink to this definition")
            :   A sequence of Ints specifying the labels.

        Returns:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.sequenceFromLabels-returns "Permalink to this headline")
        :   A MeshNodeArray object.

        Return type:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.sequenceFromLabels-return-type "Permalink to this headline")
        :   [`MeshNodeArray`](#abaqus.Mesh.MeshNodeArray.MeshNodeArray "abaqus.Mesh.MeshNodeArray.MeshNodeArray (Python class) — Bases: List[MeshNode]")

        Raises:[¶](#abaqus.Mesh.MeshNodeArray.MeshNodeArray.sequenceFromLabels-raises "Permalink to this headline")
        :   **Error** – The mask results in an empty sequence, An exception occurs if the resulting sequence is empty.

*class* MeshPart(*[name](#abaqus.Mesh.MeshPart.MeshPart "abaqus.Mesh.MeshPart.MeshPart.__init__.name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[dimensionality](#abaqus.Mesh.MeshPart.MeshPart "abaqus.Mesh.MeshPart.MeshPart.__init__.dimensionality (Python parameter)"): [SymbolicConstant](../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.SymbolicConstant "abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant (Python class)")*, *[type](#abaqus.Mesh.MeshPart.MeshPart "abaqus.Mesh.MeshPart.MeshPart.__init__.type (Python parameter)"): [SymbolicConstant](../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.SymbolicConstant "abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant (Python class)")*, *[twist](#abaqus.Mesh.MeshPart.MeshPart "abaqus.Mesh.MeshPart.MeshPart.__init__.twist (Python parameter)"): [AbaqusBoolean](../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.AbaqusBoolean "abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean (Python class)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `OFF`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L31-L1237)[¶](#abaqus.Mesh.MeshPart.MeshPart "Permalink to this definition")

*class* MeshPart(*[name](#abaqus.Mesh.MeshPart.MeshPart "abaqus.Mesh.MeshPart.MeshPart.__init__.name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[objectToCopy](#abaqus.Mesh.MeshPart.MeshPart "abaqus.Mesh.MeshPart.MeshPart.__init__.objectToCopy (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[scale](#abaqus.Mesh.MeshPart.MeshPart "abaqus.Mesh.MeshPart.MeshPart.__init__.scale (Python parameter)"): [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") = `1`*, *[mirrorPlane](#abaqus.Mesh.MeshPart.MeshPart "abaqus.Mesh.MeshPart.MeshPart.__init__.mirrorPlane (Python parameter)"): [SymbolicConstant](../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.SymbolicConstant "abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant (Python class)") = `NONE`*, *[compressFeatureList](#abaqus.Mesh.MeshPart.MeshPart "abaqus.Mesh.MeshPart.MeshPart.__init__.compressFeatureList (Python parameter)"): [AbaqusBoolean](../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.AbaqusBoolean "abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean (Python class)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `OFF`*, *[separate](#abaqus.Mesh.MeshPart.MeshPart "abaqus.Mesh.MeshPart.MeshPart.__init__.separate (Python parameter)"): [AbaqusBoolean](../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.AbaqusBoolean "abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean (Python class)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `OFF`*)
:   Bases: [`PartBase`](part_assembly/part.html#abaqus.Part.PartBase.PartBase "abaqus.Part.PartBase.PartBase (Python class) — Bases: PartFeature")

    The following commands operate on Part objects. For more information about the Part object, see Part
    object.

    Note

    This object can be accessed by:

    ```python
    import mesh
    ```

    Note

    Check [MeshPart on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all).

    Member Details:

    Node(*[coordinates](#abaqus.Mesh.MeshPart.MeshPart.Node.coordinates "abaqus.Mesh.MeshPart.MeshPart.Node.coordinates (Python parameter) — A sequence of three Floats specifying the coordinates of the new node.")*, *[localCsys](#abaqus.Mesh.MeshPart.MeshPart.Node.localCsys "abaqus.Mesh.MeshPart.MeshPart.Node.localCsys (Python parameter) — A DatumCsys object specifying the local coordinate system.")=`None`*, *[label](#abaqus.Mesh.MeshPart.MeshPart.Node.label "abaqus.Mesh.MeshPart.MeshPart.Node.label (Python parameter) — An Int specifying the node label.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L1206-L1237)[¶](#abaqus.Mesh.MeshPart.MeshPart.Node "Permalink to this definition")
    :   This method creates a node on an orphan mesh part.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].Node
        ```

        Note

        Check [Node on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-nodemgnpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.Node-parameters "Permalink to this headline")
        :   coordinates[¶](#abaqus.Mesh.MeshPart.MeshPart.Node.coordinates "Permalink to this definition")
            :   A sequence of three Floats specifying the coordinates of the new node.

            localCsys=`None`[¶](#abaqus.Mesh.MeshPart.MeshPart.Node.localCsys "Permalink to this definition")
            :   A DatumCsys object specifying the local coordinate system. If unspecified, the global
                coordinate system will be used.

            label=`None`[¶](#abaqus.Mesh.MeshPart.MeshPart.Node.label "Permalink to this definition")
            :   An Int specifying the node label.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshPart.Node-returns "Permalink to this headline")
        :   A MeshNode object.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshPart.Node-return-type "Permalink to this headline")
        :   [`MeshNode`](#abaqus.Mesh.MeshPart.MeshNode "abaqus.Mesh.MeshPart.MeshNode (Python class) — Bases: object")

    assignStackDirection(*[cells](#abaqus.Mesh.MeshPart.MeshPart.assignStackDirection.cells "abaqus.Mesh.MeshPart.MeshPart.assignStackDirection.cells (Python parameter) — A sequence of Cell objects specifying regions where to assign the stack direction.")*, *[referenceRegion](#abaqus.Mesh.MeshPart.MeshPart.assignStackDirection.referenceRegion "abaqus.Mesh.MeshPart.MeshPart.assignStackDirection.referenceRegion (Python parameter) — A Face object specifying the top side of the stack direction.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L42-L54)[¶](#abaqus.Mesh.MeshPart.MeshPart.assignStackDirection "Permalink to this definition")
    :   This method assigns a stack direction to geometric cells. The stack direction will be used to orient
        the elements during mesh generation.

        Note

        Check [MeshPart.assignStackDirection on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partassignstackdirectionpyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.assignStackDirection-parameters "Permalink to this headline")
        :   cells[¶](#abaqus.Mesh.MeshPart.MeshPart.assignStackDirection.cells "Permalink to this definition")
            :   A sequence of Cell objects specifying regions where to assign the stack direction.

            referenceRegion[¶](#abaqus.Mesh.MeshPart.MeshPart.assignStackDirection.referenceRegion "Permalink to this definition")
            :   A Face object specifying the top side of the stack direction.

    associateMeshWithGeometry(*[geometricEntity](#abaqus.Mesh.MeshPart.MeshPart.associateMeshWithGeometry.geometricEntity "abaqus.Mesh.MeshPart.MeshPart.associateMeshWithGeometry.geometricEntity (Python parameter) — A Cell, a Face, an Edge, or a ConstrainedSketchVertex object specifying geometric entity to be associated with one or more mesh entities.If the geometric entity is a Cell object then the argument elements must be specified.If the geometric entity is a Face object then the argument elemFaces must be specified.If the geometric entity is an Edge object then the argument elemEdges must be specified.If the geometric entity is a ConstrainedSketchVertex object then the argument node must be specified.")*, *elements=()*, *elemFaces=()*, *elemEdges=()*, *[node=<abaqus.Mesh.MeshNode.MeshNode object>](#abaqus.Mesh.MeshPart.MeshPart.associateMeshWithGeometry "abaqus.Mesh.MeshPart.MeshPart.associateMeshWithGeometry.node=<abaqus.Mesh.MeshNode.MeshNode object> (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L56-L89)[¶](#abaqus.Mesh.MeshPart.MeshPart.associateMeshWithGeometry "Permalink to this definition")
    :   This method associates a geometric entity with mesh entities that are either orphan elements, bounds
        orphan elements, or were created using the bottom-up meshing technique.

        Note

        Check [MeshPart.associateMeshWithGeometry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partassociatemeshwithgeometrypyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.associateMeshWithGeometry-parameters "Permalink to this headline")
        :   geometricEntity[¶](#abaqus.Mesh.MeshPart.MeshPart.associateMeshWithGeometry.geometricEntity "Permalink to this definition")
            :   A Cell, a Face, an Edge, or a ConstrainedSketchVertex object specifying geometric entity to be associated
                with one or more mesh entities.If the geometric entity is a Cell object then the
                argument **elements** must be specified.If the geometric entity is a Face object then the
                argument **elemFaces** must be specified.If the geometric entity is an Edge object then
                the argument **elemEdges** must be specified.If the geometric entity is a ConstrainedSketchVertex object
                then the argument **node** must be specified.

            elements : [`Sequence`](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.13)")[[`MeshElement`](#abaqus.Mesh.MeshPart.MeshElement "abaqus.Mesh.MeshElement.MeshElement (Python class)")], default: `()`
            :   A sequence of MeshElement objects specifying the elements to be associated with the
                geometric cell.

            elemFaces : [`Sequence`](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.13)")[[`MeshFace`](#abaqus.Mesh.MeshPart.MeshFace "abaqus.Mesh.MeshFace.MeshFace (Python class)")], default: `()`
            :   A sequence of MeshFace objects specifying the element faces to be associated with the
                geometric face.

            elemEdges : [`Sequence`](https://docs.python.org/3/library/typing.html#typing.Sequence "(in Python v3.13)")[[`MeshEdge`](#abaqus.Mesh.MeshPart.MeshEdge "abaqus.Mesh.MeshEdge.MeshEdge (Python class)")], default: `()`
            :   A sequence of MeshEdge objects specifying the element edges to be associated with the
                geometric edge.

            node : [`MeshNode`](#abaqus.Mesh.MeshPart.MeshNode "abaqus.Mesh.MeshNode.MeshNode (Python class)"), default: `<abaqus.Mesh.MeshNode.MeshNode object at 0x7f850cd54510>`
            :   A MeshNode object specifying the mesh node to be associated with the geometric vertex.

    createVirtualTopology(*[regions](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.regions "abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.regions (Python parameter) — A sequence of Face objects specifying the domain to search for geometric entities that need to be merged.")=`()`*, *[mergeShortEdges](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.mergeShortEdges "abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.mergeShortEdges (Python parameter) — A Boolean specifying whether to merge short edges.")=`False`*, *[shortEdgeThreshold](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.shortEdgeThreshold "abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.shortEdgeThreshold (Python parameter) — A Float specifying a threshold that determines which edges are considered to be short. These edges are the candidate entities to be merged.")=`None`*, *[mergeSmallFaces](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.mergeSmallFaces "abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.mergeSmallFaces (Python parameter) — A Boolean specifying whether to merge faces with small area.")=`False`*, *[smallFaceAreaThreshold](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.smallFaceAreaThreshold "abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.smallFaceAreaThreshold (Python parameter) — A Float specifying a threshold that determines which faces are considered to have a small area.")=`None`*, *[mergeSliverFaces](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.mergeSliverFaces "abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.mergeSliverFaces (Python parameter) — A Boolean specifying whether to merge faces with high aspect ratio.")=`False`*, *[faceAspectRatioThreshold](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.faceAspectRatioThreshold "abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.faceAspectRatioThreshold (Python parameter) — A Float specifying a threshold that determines which faces are considered to have high aspect ratio.")=`None`*, *[mergeSmallAngleFaces](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.mergeSmallAngleFaces "abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.mergeSmallAngleFaces (Python parameter) — A Boolean specifying whether to merge faces that have a sharp corner angle.")=`False`*, *[smallFaceCornerAngleThreshold](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.smallFaceCornerAngleThreshold "abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.smallFaceCornerAngleThreshold (Python parameter) — A Float specifying a threshold that determines which face corner angles are considered to be small.")=`None`*, *[mergeThinStairFaces](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.mergeThinStairFaces "abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.mergeThinStairFaces (Python parameter) — A Boolean specifying whether to merge faces that represent a thin stair-like feature. The default value is False.")=`False`*, *[thinStairFaceThreshold](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.thinStairFaceThreshold "abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.thinStairFaceThreshold (Python parameter) — A Float specifying a threshold that determines which faces representing small stair-like features are considered thin.")=`None`*, *[ignoreRedundantEntities](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.ignoreRedundantEntities "abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.ignoreRedundantEntities (Python parameter) — A Boolean specifying whether to abstract away redundant edges and vertices.")=`False`*, *[cornerAngleTolerance](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.cornerAngleTolerance "abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.cornerAngleTolerance (Python parameter) — A Float specifying the angle deviation from 180 degrees at a vertex or at an edge such that the two edges radiating from the vertex or the two faces bounded by the edge can be merged.")=`30`*, *[applyBlendControls](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.applyBlendControls "abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.applyBlendControls (Python parameter) — A Boolean specifying whether to verify that blend faces can be merged with neighboring faces.")=`False`*, *[blendSubtendedAngleTolerance](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.blendSubtendedAngleTolerance "abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.blendSubtendedAngleTolerance (Python parameter) — A Float specifying the largest subtended angle of blend faces that can be merged with neighboring faces.")=`None`*, *[blendRadiusTolerance](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.blendRadiusTolerance "abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.blendRadiusTolerance (Python parameter) — A Float specifying the smallest radius of curvature of blend faces that can be merged with neighboring faces.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L91-L189)[¶](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology "Permalink to this definition")
    :   This method creates a virtual topology feature by automatically merging faces and edges based on a
        set of geometric parameters. The edges and vertices that are being merged will be ignored during mesh
        generation.

        Note

        Check [MeshPart.createVirtualTopology on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partcreatevirtualtopologypyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology-parameters "Permalink to this headline")
        :   regions=`()`[¶](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.regions "Permalink to this definition")
            :   A sequence of Face objects specifying the domain to search for geometric entities that
                need to be merged. Entities identified as candidates to be merged may be merged with
                entities from outside the specified region. If **regions** is not specified then the
                entire part is the domain for searching geometric entities that need to be merged.

            mergeShortEdges=`False`[¶](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.mergeShortEdges "Permalink to this definition")
            :   A Boolean specifying whether to merge short edges. The default value is False.

            shortEdgeThreshold=`None`[¶](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.shortEdgeThreshold "Permalink to this definition")
            :   A Float specifying a threshold that determines which edges are considered to be short.
                These edges are the candidate entities to be merged. This argument is a required
                argument if the argument\*mergeShortEdges\* equals True and it is ignored if the argument
                **mergeShortEdges** equals False.

            mergeSmallFaces=`False`[¶](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.mergeSmallFaces "Permalink to this definition")
            :   A Boolean specifying whether to merge faces with small area. The default value is False.

            smallFaceAreaThreshold=`None`[¶](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.smallFaceAreaThreshold "Permalink to this definition")
            :   A Float specifying a threshold that determines which faces are considered to have a
                small area. These faces are the candidate entities to be merged. This argument is a
                required argument if the argument\*mergeSmallFaces\* equals True and it is ignored if the
                argument **mergeSmallFaces** equals False.

            mergeSliverFaces=`False`[¶](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.mergeSliverFaces "Permalink to this definition")
            :   A Boolean specifying whether to merge faces with high aspect ratio. The default value is
                False.

            faceAspectRatioThreshold=`None`[¶](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.faceAspectRatioThreshold "Permalink to this definition")
            :   A Float specifying a threshold that determines which faces are considered to have high
                aspect ratio. These faces are the candidate entities to be merged. This argument is a
                required argument if the argument\*mergeSliverFaces\* equals True and it is ignored if the
                argument **mergeSliverFaces** equals False.

            mergeSmallAngleFaces=`False`[¶](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.mergeSmallAngleFaces "Permalink to this definition")
            :   A Boolean specifying whether to merge faces that have a sharp corner angle. The default
                value is False.

            smallFaceCornerAngleThreshold=`None`[¶](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.smallFaceCornerAngleThreshold "Permalink to this definition")
            :   A Float specifying a threshold that determines which face corner angles are considered
                to be small. These faces will be candidate entities to be merged. This argument is a
                required argument if the argument\*mergeSmallAngleFaces\* equals True and it is ignored if
                the argument **mergeSmallAngleFaces** equals False.

            mergeThinStairFaces=`False`[¶](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.mergeThinStairFaces "Permalink to this definition")
            :   A Boolean specifying whether to merge faces that represent a thin stair-like feature.
                The default value is False.

            thinStairFaceThreshold=`None`[¶](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.thinStairFaceThreshold "Permalink to this definition")
            :   A Float specifying a threshold that determines which faces representing small stair-like
                features are considered thin. These faces will be candidate entities to be merged. This
                argument is required if the argument **mergeThinStairFaces** is True and it is ignored if
                **mergeThinStairFaces** is False.

            ignoreRedundantEntities=`False`[¶](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.ignoreRedundantEntities "Permalink to this definition")
            :   A Boolean specifying whether to abstract away redundant edges and vertices. The default
                value is False.

            cornerAngleTolerance=`30`[¶](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.cornerAngleTolerance "Permalink to this definition")
            :   A Float specifying the angle deviation from 180 degrees at a vertex or at an edge such
                that the two edges radiating from the vertex or the two faces bounded by the edge can be
                merged. The default value is 30.0 degrees.

            applyBlendControls=`False`[¶](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.applyBlendControls "Permalink to this definition")
            :   A Boolean specifying whether to verify that blend faces can be merged with neighboring
                faces. If **applyBlendControls** is true then all faces that have angle larger than
                **blendSubtendedAngleTolerance** and a radius smaller than **blendRadiusTolerance** will not
                be merged with neighboring faces unless the neighboring faces are also blend faces with
                similar geometric characteristics. The default value is False.

            blendSubtendedAngleTolerance=`None`[¶](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.blendSubtendedAngleTolerance "Permalink to this definition")
            :   A Float specifying the largest subtended angle of blend faces that can be merged with
                neighboring faces. This argument is a required argument if the argument
                **applyBlendControls** equals True and it is ignored if the argument **applyBlendControls**
                equals False.

            blendRadiusTolerance=`None`[¶](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology.blendRadiusTolerance "Permalink to this definition")
            :   A Float specifying the smallest radius of curvature of blend faces that can be merged
                with neighboring faces. This argument is a required argument if the argument
                **applyBlendControls** equals True and it is ignored if the argument **applyBlendControls**
                equals False.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshPart.createVirtualTopology-return-type "Permalink to this headline")
        :   `Feature`

    deleteBoundaryLayerControls(*[regions](#abaqus.Mesh.MeshPart.MeshPart.deleteBoundaryLayerControls.regions "abaqus.Mesh.MeshPart.MeshPart.deleteBoundaryLayerControls.regions (Python parameter) — A sequence of Cell objects specifying the regions for which to set the boundary layer mesh control parameters.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L191-L201)[¶](#abaqus.Mesh.MeshPart.MeshPart.deleteBoundaryLayerControls "Permalink to this definition")
    :   This method deletes the control parameters for boundary layer mesh for all the specified regions.

        Note

        Check [MeshPart.deleteBoundaryLayerControls on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partdeleteboundarylayercontrolspyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.deleteBoundaryLayerControls-parameters "Permalink to this headline")
        :   regions[¶](#abaqus.Mesh.MeshPart.MeshPart.deleteBoundaryLayerControls.regions "Permalink to this definition")
            :   A sequence of Cell objects specifying the regions for which to set the boundary layer
                mesh control parameters.

    deleteMesh(*[regions](#abaqus.Mesh.MeshPart.MeshPart.deleteMesh.regions "abaqus.Mesh.MeshPart.MeshPart.deleteMesh.regions (Python parameter) — A sequence of Part objects or Region objects specifying the parts or regions from which the native mesh is to be deleted.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L203-L214)[¶](#abaqus.Mesh.MeshPart.MeshPart.deleteMesh "Permalink to this definition")
    :   This method deletes a subset of the mesh that contains the native elements from the given parts or
        regions.

        Note

        Check [MeshPart.deleteMesh on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partdeletemeshpyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.deleteMesh-parameters "Permalink to this headline")
        :   regions[¶](#abaqus.Mesh.MeshPart.MeshPart.deleteMesh.regions "Permalink to this definition")
            :   A sequence of Part objects or Region objects specifying the parts or regions from which
                the native mesh is to be deleted.

    deleteMeshAssociationWithGeometry(*[geometricEntities](#abaqus.Mesh.MeshPart.MeshPart.deleteMeshAssociationWithGeometry.geometricEntities "abaqus.Mesh.MeshPart.MeshPart.deleteMeshAssociationWithGeometry.geometricEntities (Python parameter) — A sequence of Cell objects, Face objects, Edge objects, or ConstrainedSketchVertex objects specifying the geometric entities that will be disassociated from the mesh.")*, *[addBoundingEntities](#abaqus.Mesh.MeshPart.MeshPart.deleteMeshAssociationWithGeometry.addBoundingEntities "abaqus.Mesh.MeshPart.MeshPart.deleteMeshAssociationWithGeometry.addBoundingEntities (Python parameter) — A Boolean specifying whether the mesh will also be disassociated from the geometric entities that bounds the given geometricEntities.")=`False`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L216-L234)[¶](#abaqus.Mesh.MeshPart.MeshPart.deleteMeshAssociationWithGeometry "Permalink to this definition")
    :   This method deletes the association of geometric entities with mesh entities.

        Note

        Check [MeshPart.deleteMeshAssociationWithGeometry on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partdeletemeshassociationwithgeometrypyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.deleteMeshAssociationWithGeometry-parameters "Permalink to this headline")
        :   geometricEntities[¶](#abaqus.Mesh.MeshPart.MeshPart.deleteMeshAssociationWithGeometry.geometricEntities "Permalink to this definition")
            :   A sequence of Cell objects, Face objects, Edge objects, or ConstrainedSketchVertex objects specifying the
                geometric entities that will be disassociated from the mesh.

            addBoundingEntities=`False`[¶](#abaqus.Mesh.MeshPart.MeshPart.deleteMeshAssociationWithGeometry.addBoundingEntities "Permalink to this definition")
            :   A Boolean specifying whether the mesh will also be disassociated from the geometric
                entities that bounds the given **geometricEntities**. For example, if the argument
                **geometricEntities** contains a face, this boolean indicates whether the edges and
                vertices that bound the face will also be disassociated from the mesh. The default value
                is False.

    deletePreviewMesh()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L236-L243)[¶](#abaqus.Mesh.MeshPart.MeshPart.deletePreviewMesh "Permalink to this definition")
    :   This method deletes all boundary meshes in the parts.

        See the **boundaryPreview** argument of generateMesh for information about generating boundary
        meshes.

    deleteSeeds(*[regions](#abaqus.Mesh.MeshPart.MeshPart.deleteSeeds.regions "abaqus.Mesh.MeshPart.MeshPart.deleteSeeds.regions (Python parameter) — A sequence of Part objects or Edge objects specifying the parts or edges from which the seeds are to be deleted.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L245-L256)[¶](#abaqus.Mesh.MeshPart.MeshPart.deleteSeeds "Permalink to this definition")
    :   This method deletes the global edge seeds from the given parts or deletes the local edge seeds from
        the given edges.

        Note

        Check [MeshPart.deleteSeeds on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partdeleteseedspyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.deleteSeeds-parameters "Permalink to this headline")
        :   regions[¶](#abaqus.Mesh.MeshPart.MeshPart.deleteSeeds.regions "Permalink to this definition")
            :   A sequence of Part objects or Edge objects specifying the parts or edges from which the
                seeds are to be deleted.

    generateBottomUpExtrudedMesh(*[cell](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.cell "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.cell (Python parameter) — A Cell object specifying the geometric region where the mesh is to be generated.")*, *[numberOfLayers](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.numberOfLayers "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.numberOfLayers (Python parameter) — An Int specifying the number of layers to be generated along the extrusion vector.")*, *[extrudeVector](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.extrudeVector "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.extrudeVector (Python parameter) — A sequence of sequences of Floats specifying the start point and end point of a vector. Each point is defined by a tuple of three coordinates indicating its position.")*, *[geometrySourceSide](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.geometrySourceSide "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.geometrySourceSide (Python parameter) — A Region of Face objects specifying the geometric domain to be used as the source for the extrude meshing operation.")=`''`*, *[elemFacesSourceSide](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.elemFacesSourceSide "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.elemFacesSourceSide (Python parameter) — A sequence of MeshFace objects specifying the faces of 3D elements to be used as the source for the extrude meshing operation.")=`()`*, *[elemSourceSide](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.elemSourceSide "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.elemSourceSide (Python parameter) — A sequence of 2D MeshElement objects specifying the elements to be used as the source for the extrude meshing operation.")=`()`*, *[depth](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.depth "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.depth (Python parameter) — A Float specifying the distance of the mesh extrusion.")=`None`*, *[targetSide](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.targetSide "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.targetSide (Python parameter) — A datum plane, a sequence of Face objects, a sequence of MeshFace objects, or a sequence of 2D MeshElement objects specifying the target of the extrude meshing operation.")=`''`*, *[biasRatio](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.biasRatio "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.biasRatio (Python parameter) — A Float specifying a ratio of the element size in the extrusion direction between the source and the target sides of the extrusion.")=`1`*, *[extendElementSets](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.extendElementSets "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.extendElementSets (Python parameter) — A Boolean specifying whether existing element sets that include source elements will be extended to also include extruded elements.")=`False`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L293-L346)[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh "Permalink to this definition")
    :   This method generates solid elements by extruding a 2D mesh along a vector, either on an orphan mesh
        or within a cell region using a bottom-up technique.

        Note

        Check [MeshPart.generateBottomUpExtrudedMesh on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partgeneratebottomupextrudedmeshpyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh-parameters "Permalink to this headline")
        :   cell[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.cell "Permalink to this definition")
            :   A Cell object specifying the geometric region where the mesh is to be generated. This
                argument is valid only for native parts.

            numberOfLayers[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.numberOfLayers "Permalink to this definition")
            :   An Int specifying the number of layers to be generated along the extrusion vector.

            extrudeVector[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.extrudeVector "Permalink to this definition")
            :   A sequence of sequences of Floats specifying the start point and end point of a vector.
                Each point is defined by a tuple of three coordinates indicating its position. The
                direction of the mesh extrusion operation is from the first point to the second point.

            geometrySourceSide=`''`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.geometrySourceSide "Permalink to this definition")
            :   A Region of Face objects specifying the geometric domain to be used as the source for
                the extrude meshing operation.

            elemFacesSourceSide=`()`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.elemFacesSourceSide "Permalink to this definition")
            :   A sequence of MeshFace objects specifying the faces of 3D elements to be used as the
                source for the extrude meshing operation.

            elemSourceSide=`()`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.elemSourceSide "Permalink to this definition")
            :   A sequence of 2D MeshElement objects specifying the elements to be used as the source
                for the extrude meshing operation.

            depth=`None`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.depth "Permalink to this definition")
            :   A Float specifying the distance of the mesh extrusion. If unspecified, the vector length
                of the **extrudeVector** argument is assumed.

            targetSide=`''`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.targetSide "Permalink to this definition")
            :   A datum plane, a sequence of Face objects, a sequence of MeshFace objects, or a sequence
                of 2D MeshElement objects specifying the target of the extrude meshing operation. If
                specified, this argument overrides the **depth** argument, and all points on the source
                will be extruded in the direction of the extrusion vector until meeting the target.

            biasRatio=`1`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.biasRatio "Permalink to this definition")
            :   A Float specifying a ratio of the element size in the extrusion direction between the
                source and the target sides of the extrusion. The default is 1.0, meaning no bias.

            extendElementSets=`False`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpExtrudedMesh.extendElementSets "Permalink to this definition")
            :   A Boolean specifying whether existing element sets that include source elements will be
                extended to also include extruded elements. This argument is ignored for native parts.
                The default value is False.

    generateBottomUpRevolvedMesh(*[cell](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh.cell "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh.cell (Python parameter) — A Cell object specifying the geometric region where the mesh is to be generated.")*, *[numberOfLayers](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh.numberOfLayers "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh.numberOfLayers (Python parameter) — An Int specifying the number of layers of elements to be generated around the axis of revolution.")*, *[axisOfRevolution](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh.axisOfRevolution "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh.axisOfRevolution (Python parameter) — A sequence of sequences of Floats specifying the two points of the vector that describes the axis of revolution.")*, *[angleOfRevolution](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh.angleOfRevolution "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh.angleOfRevolution (Python parameter) — A Float specifying the angle of revolution.")*, *[geometrySourceSide](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh.geometrySourceSide "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh.geometrySourceSide (Python parameter) — A Region of Face objects specifying the geometric domain to be used as the source for the revolve meshing operation.")=`''`*, *[elemFacesSourceSide](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh.elemFacesSourceSide "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh.elemFacesSourceSide (Python parameter) — A sequence of MeshFace objects specifying the faces of 3D elements to be used as the source for the revolve meshing operation.")=`()`*, *[elemSourceSide](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh.elemSourceSide "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh.elemSourceSide (Python parameter) — A sequence of 2D MeshElement objects specifying the elements to be used as the source for the revolve meshing operation.")=`()`*, *[extendElementSets](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh.extendElementSets "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh.extendElementSets (Python parameter) — A Boolean specifying whether existing element sets that include source elements will be extended to also include extruded elements.")=`False`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L398-L443)[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh "Permalink to this definition")
    :   This method generates solid elements by revolving a 2D mesh around an axis, either on an orphan mesh
        or within a cell region using a bottom-up technique.

        Note

        Check [MeshPart.generateBottomUpRevolvedMesh on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partgeneratebottomuprevolvedmeshpyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh-parameters "Permalink to this headline")
        :   cell[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh.cell "Permalink to this definition")
            :   A Cell object specifying the geometric region where the mesh is to be generated. This
                argument is valid only for native parts.

            numberOfLayers[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh.numberOfLayers "Permalink to this definition")
            :   An Int specifying the number of layers of elements to be generated around the axis of
                revolution.

            axisOfRevolution[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh.axisOfRevolution "Permalink to this definition")
            :   A sequence of sequences of Floats specifying the two points of the vector that describes
                the axis of revolution. Each point is defined by a tuple of three coordinates indicating
                its position. The direction of the axis of revolution is from the first point to the
                second point. The orientation of the revolution operation follows the right-hand-rule
                about the axis of revolution.

            angleOfRevolution[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh.angleOfRevolution "Permalink to this definition")
            :   A Float specifying the angle of revolution.

            geometrySourceSide=`''`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh.geometrySourceSide "Permalink to this definition")
            :   A Region of Face objects specifying the geometric domain to be used as the source for
                the revolve meshing operation.

            elemFacesSourceSide=`()`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh.elemFacesSourceSide "Permalink to this definition")
            :   A sequence of MeshFace objects specifying the faces of 3D elements to be used as the
                source for the revolve meshing operation.

            elemSourceSide=`()`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh.elemSourceSide "Permalink to this definition")
            :   A sequence of 2D MeshElement objects specifying the elements to be used as the source
                for the revolve meshing operation.

            extendElementSets=`False`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpRevolvedMesh.extendElementSets "Permalink to this definition")
            :   A Boolean specifying whether existing element sets that include source elements will be
                extended to also include extruded elements. This argument is ignored for native parts.
                The default value is False.

    generateBottomUpSweptMesh(*[cell](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.cell "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.cell (Python parameter) — A Cell object specifying the geometric region where the mesh is to be generated.")*, *[geometrySourceSide](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.geometrySourceSide "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.geometrySourceSide (Python parameter) — A Region of Face objects specifying the geometric domain to be used as the source for the sweep meshing operation.")=`''`*, *[elemFacesSourceSide](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.elemFacesSourceSide "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.elemFacesSourceSide (Python parameter) — A sequence of MeshFace objects specifying the faces of 3D elements to be used as the source for the sweep meshing operation.")=`()`*, *[elemSourceSide](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.elemSourceSide "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.elemSourceSide (Python parameter) — A sequence of 2D MeshElement objects specifying the elements to be used as the source for the sweep meshing operation.")=`()`*, *[geometryConnectingSides](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.geometryConnectingSides "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.geometryConnectingSides (Python parameter) — A Region of Face objects specifying connecting sides of the sweep meshing operation.")=`''`*, *[elemFacesConnectingSides](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.elemFacesConnectingSides "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.elemFacesConnectingSides (Python parameter) — A sequence of MeshFace objects specifying connecting sides of the sweep meshing operation.")=`()`*, *[elemConnectingSides](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.elemConnectingSides "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.elemConnectingSides (Python parameter) — A sequence of 2D MeshElement objects specifying connecting sides of the sweep meshing operation.")=`()`*, *[targetSide](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.targetSide "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.targetSide (Python parameter) — A Face object specifying the target side of the sweep meshing operation.")=`None`*, *[numberOfLayers](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.numberOfLayers "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.numberOfLayers (Python parameter) — An Int specifying the number of layers to be generated along the sweep direction.")=`None`*, *[extendElementSets](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.extendElementSets "abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.extendElementSets (Python parameter) — A Boolean specifying whether existing element sets that include source elements will be extended to also include swept elements.")=`False`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L348-L396)[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh "Permalink to this definition")
    :   This method generates solid elements by sweeping a 2D mesh, either on an orphan mesh or within a cell
        region using a bottom-up technique.

        Note

        Check [MeshPart.generateBottomUpSweptMesh on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partgeneratebottomupsweptmeshpyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh-parameters "Permalink to this headline")
        :   cell[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.cell "Permalink to this definition")
            :   A Cell object specifying the geometric region where the mesh is to be generated. This
                argument is valid only for native parts.

            geometrySourceSide=`''`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.geometrySourceSide "Permalink to this definition")
            :   A Region of Face objects specifying the geometric domain to be used as the source for
                the sweep meshing operation.

            elemFacesSourceSide=`()`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.elemFacesSourceSide "Permalink to this definition")
            :   A sequence of MeshFace objects specifying the faces of 3D elements to be used as the
                source for the sweep meshing operation.

            elemSourceSide=`()`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.elemSourceSide "Permalink to this definition")
            :   A sequence of 2D MeshElement objects specifying the elements to be used as the source
                for the sweep meshing operation.

            geometryConnectingSides=`''`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.geometryConnectingSides "Permalink to this definition")
            :   A Region of Face objects specifying connecting sides of the sweep meshing operation.

            elemFacesConnectingSides=`()`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.elemFacesConnectingSides "Permalink to this definition")
            :   A sequence of MeshFace objects specifying connecting sides of the sweep meshing
                operation.

            elemConnectingSides=`()`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.elemConnectingSides "Permalink to this definition")
            :   A sequence of 2D MeshElement objects specifying connecting sides of the sweep meshing
                operation.

            targetSide=`None`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.targetSide "Permalink to this definition")
            :   A Face object specifying the target side of the sweep meshing operation.

            numberOfLayers=`None`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.numberOfLayers "Permalink to this definition")
            :   An Int specifying the number of layers to be generated along the sweep direction.

            extendElementSets=`False`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateBottomUpSweptMesh.extendElementSets "Permalink to this definition")
            :   A Boolean specifying whether existing element sets that include source elements will be
                extended to also include swept elements. This argument is ignored for native parts. The
                default value is False.

    generateMesh(*[regions](#abaqus.Mesh.MeshPart.MeshPart.generateMesh.regions "abaqus.Mesh.MeshPart.MeshPart.generateMesh.regions (Python parameter) — A sequence of Part objects or Region objects specifying the parts or regions where the mesh is to be generated.")=`()`*, *[seedConstraintOverride](#abaqus.Mesh.MeshPart.MeshPart.generateMesh.seedConstraintOverride "abaqus.Mesh.MeshPart.MeshPart.generateMesh.seedConstraintOverride (Python parameter) — A Boolean specifying whether mesh generation is allowed to modify seed constraints.")=`0`*, *[meshTechniqueOverride](#abaqus.Mesh.MeshPart.MeshPart.generateMesh.meshTechniqueOverride "abaqus.Mesh.MeshPart.MeshPart.generateMesh.meshTechniqueOverride (Python parameter) — A Boolean specifying whether mesh generation is allowed to modify the existing mesh techniques so that a compatible mesh can be generated.")=`0`*, *[boundaryPreview](#abaqus.Mesh.MeshPart.MeshPart.generateMesh.boundaryPreview "abaqus.Mesh.MeshPart.MeshPart.generateMesh.boundaryPreview (Python parameter) — A Boolean specifying whether the generated mesh should be a boundary preview mesh.")=`0`*, *[boundaryMeshOverride](#abaqus.Mesh.MeshPart.MeshPart.generateMesh.boundaryMeshOverride "abaqus.Mesh.MeshPart.MeshPart.generateMesh.boundaryMeshOverride (Python parameter) — A Boolean specifying whether mesh generation is allowed to modify an existing boundary preview mesh.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L258-L291)[¶](#abaqus.Mesh.MeshPart.MeshPart.generateMesh "Permalink to this definition")
    :   This method generates a mesh in the given parts or regions.

        Note

        Check [MeshPart.generateMesh on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partgeneratemeshpyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.generateMesh-parameters "Permalink to this headline")
        :   regions=`()`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateMesh.regions "Permalink to this definition")
            :   A sequence of Part objects or Region objects specifying the parts or regions where the
                mesh is to be generated.

            seedConstraintOverride=`0`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateMesh.seedConstraintOverride "Permalink to this definition")
            :   A Boolean specifying whether mesh generation is allowed to modify seed constraints. The
                default value is OFF.

            meshTechniqueOverride=`0`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateMesh.meshTechniqueOverride "Permalink to this definition")
            :   A Boolean specifying whether mesh generation is allowed to modify the existing mesh
                techniques so that a compatible mesh can be generated. The default value is OFF.

            boundaryPreview=`0`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateMesh.boundaryPreview "Permalink to this definition")
            :   A Boolean specifying whether the generated mesh should be a boundary preview mesh. This
                option will only have an effect if any of the specified regions are to be meshed with
                tetrahedral elements or using the bottom-up technique with hexahedral or wedge elements.
                The default value is OFF.

            boundaryMeshOverride=`0`[¶](#abaqus.Mesh.MeshPart.MeshPart.generateMesh.boundaryMeshOverride "Permalink to this definition")
            :   A Boolean specifying whether mesh generation is allowed to modify an existing boundary
                preview mesh. This option will only have an effect if any of the specified regions are
                to be meshed with tetrahedral elements and a boundary preview mesh already exists. The
                default value is OFF.

    getEdgeSeeds(*[edge](#abaqus.Mesh.MeshPart.MeshPart.getEdgeSeeds.edge "abaqus.Mesh.MeshPart.MeshPart.getEdgeSeeds.edge (Python parameter) — An Edge object specifying the edge to be queried.")*, *[attribute](#abaqus.Mesh.MeshPart.MeshPart.getEdgeSeeds.attribute "abaqus.Mesh.MeshPart.MeshPart.getEdgeSeeds.attribute (Python parameter) — A SymbolicConstant specifying the type of edge seed attribute to return.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L445-L531)[¶](#abaqus.Mesh.MeshPart.MeshPart.getEdgeSeeds "Permalink to this definition")
    :   This method returns an edge seed parameter for a specified edge of a part.

        Note

        Check [MeshPart.getEdgeSeeds on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partgetedgeseedspyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.getEdgeSeeds-parameters "Permalink to this headline")
        :   edge[¶](#abaqus.Mesh.MeshPart.MeshPart.getEdgeSeeds.edge "Permalink to this definition")
            :   An Edge object specifying the edge to be queried.

            attribute[¶](#abaqus.Mesh.MeshPart.MeshPart.getEdgeSeeds.attribute "Permalink to this definition")
            :   A SymbolicConstant specifying the type of edge seed attribute to return. Possible values
                are:

                * EDGE\_SEEDING\_METHOD
                * BIAS\_METHOD
                * NUMBER
                * AVERAGE\_SIZE
                * DEVIATION\_FACTOR
                * MIN\_SIZE\_FACTOR
                * BIAS\_RATIO
                * BIAS\_MIN\_SIZE
                * BIAS\_MAX\_SIZE
                * VERTEX\_ADJ\_TO\_SMALLEST\_ELEM
                * SMALLEST\_ELEM\_LOCATION
                * CONSTRAINT

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshPart.getEdgeSeeds-returns "Permalink to this headline")
        :   The return value is a Float, an Int, or a SymbolicConstant depending on the value of the
            **attribute** argument.

            The return value is dependent on the **attribute** argument.

            * If **attribute** = EDGE\_SEEDING\_METHOD, the return value is a SymbolicConstant specifying
              the edge seeding method used to create the seeds along the edge. Possible values are: UNIFORM\_BY\_NUMBER, UNIFORM\_BY\_SIZE, CURVATURE\_BASED\_BY\_SIZE, BIASED, NONE
            * If **attribute** = BIAS\_METHOD, the return value is a SymbolicConstant specifying the bias
              type used to create the seeds along the edge. Possible values are: SINGLE, DOUBLE, NONE
            * If **attribute** = NUMBER, the return value is an Int specifying the number of element
              seeds along the edge.
            * If **attribute** = AVERAGE\_SIZE, the return value is a Float specifying the average
              element size along the edge.
            * If **attribute** = DEVIATION\_FACTOR, the return value is a Float specifying the deviation
              factor h/Lh/L, where hh is the chordal deviation and LL is the element length. If edge
              seeds are not defined, the return value is zero.
            * If **attribute** = MIN\_SIZE\_FACTOR, the return value is a Float specifying the size of the
              smallest allowable element as a fraction of the specified global element size. If edge
              seeds are not defined, the return value is zero.
            * If **attribute** = BIAS\_RATIO, the return value is a Float specifying the length ratio of
              the largest element to the smallest element.
            * If **attribute** = BIAS\_MIN\_SIZE, the return value is a Float specifying the length of the
              largest element; only applicable if the EDGE\_SEEDING\_METHOD is BIASED and seeds were
              specified by minimum and maximum sizes.
            * If **attribute** = BIAS\_MAX\_SIZE, the return value is a Float specifying the length of the
              largest element; only applicable if the EDGE\_SEEDING\_METHOD is BIASED and seeds were
              specified by minimum and maximum sizes.
            * If **attribute** = VERTEX\_ADJ\_TO\_SMALLEST\_ELEM, the return value is an Int specifying the
              ID of the vertex next to the smallest element; only applicable if the
              EDGE\_SEEDING\_METHOD is BIASED.
            * If **attribute** = SMALLEST\_ELEM\_LOCATION, the return value is a SymbolicConstant
              specifying the location of smallest elements for double bias seeds; only applicable if
              the EDGE\_SEEDING\_METHOD is BIASED and BIAS\_METHOD is DOUBLE. Possible values are: SMALLEST\_ELEM\_AT\_CENTER, SMALLEST\_ELEM\_AT\_ENDS, NONE
            * If **attribute** = CONSTRAINT, the return value is a SymbolicConstant specifying how close
              the seeds must be matched by the mesh. Possible values are: FREE, FINER, FIXED, NONE

            A value of NONE indicates that the edge is not seeded.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshPart.getEdgeSeeds-return-type "Permalink to this headline")
        :   `Union[float`, [`int`](https://docs.python.org/3/library/functions.html#int "(in Python v3.13)"), `SymbolicConstant]`

    getElementType(*[region](#abaqus.Mesh.MeshPart.MeshPart.getElementType.region "abaqus.Mesh.MeshPart.MeshPart.getElementType.region (Python parameter) — A Cell, a Face, or an Edge object specifying the region to be queried.")*, *[elemShape](#abaqus.Mesh.MeshPart.MeshPart.getElementType.elemShape "abaqus.Mesh.MeshPart.MeshPart.getElementType.elemShape (Python parameter) — A SymbolicConstant specifying the shape of the element for which to return the element type.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L533-L574)[¶](#abaqus.Mesh.MeshPart.MeshPart.getElementType "Permalink to this definition")
    :   This method returns the ElemType object of a given element shape assigned to a region of a part.

        Note

        Check [MeshPart.getElementType on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partgetelementtypepyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.getElementType-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Mesh.MeshPart.MeshPart.getElementType.region "Permalink to this definition")
            :   A Cell, a Face, or an Edge object specifying the region to be queried.

            elemShape[¶](#abaqus.Mesh.MeshPart.MeshPart.getElementType.elemShape "Permalink to this definition")
            :   A SymbolicConstant specifying the shape of the element for which to return the element
                type. Possible values are:

                * LINE
                * QUAD
                * TRI
                * HEX
                * WEDGE
                * TET

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshPart.getElementType-returns "Permalink to this headline")
        :   An ElemType object.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshPart.getElementType-return-type "Permalink to this headline")
        :   `ElementType`

        Raises:[¶](#abaqus.Mesh.MeshPart.MeshPart.getElementType-raises "Permalink to this headline")
        :   [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.13)") – The region cannot be associated with element types or the **elemShape** is not
            consistent with the dimension of the **region**.

    getIncompatibleMeshInterfaces(*[cells](#abaqus.Mesh.MeshPart.MeshPart.getIncompatibleMeshInterfaces.cells "abaqus.Mesh.MeshPart.MeshPart.getIncompatibleMeshInterfaces.cells (Python parameter) — A sequence of cell objects which will be used to search the incompatible faces.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L576-L590)[¶](#abaqus.Mesh.MeshPart.MeshPart.getIncompatibleMeshInterfaces "Permalink to this definition")
    :   This method returns a sequence of Face objects that are meshed with incompatible elements.

        Note

        Check [MeshPart.getIncompatibleMeshInterfaces on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partgetincompatiblemeshinterfacespyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.getIncompatibleMeshInterfaces-parameters "Permalink to this headline")
        :   cells=`()`[¶](#abaqus.Mesh.MeshPart.MeshPart.getIncompatibleMeshInterfaces.cells "Permalink to this definition")
            :   A sequence of cell objects which will be used to search the incompatible faces.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshPart.getIncompatibleMeshInterfaces-returns "Permalink to this headline")
        :   A sequence of Face objects.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshPart.getIncompatibleMeshInterfaces-return-type "Permalink to this headline")
        :   `Sequence[Face]`

    getMeshControl(*[region](#abaqus.Mesh.MeshPart.MeshPart.getMeshControl.region "abaqus.Mesh.MeshPart.MeshPart.getMeshControl.region (Python parameter) — A Cell, a Face, or an Edge object specifying the region to be queried.")*, *[attribute](#abaqus.Mesh.MeshPart.MeshPart.getMeshControl.attribute "abaqus.Mesh.MeshPart.MeshPart.getMeshControl.attribute (Python parameter) — A SymbolicConstant specifying the mesh control attribute to return.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L592-L658)[¶](#abaqus.Mesh.MeshPart.MeshPart.getMeshControl "Permalink to this definition")
    :   This method returns a mesh control parameter for the specified region of a part.

        Note

        Check [MeshPart.getMeshControl on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partgetmeshcontrolpyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.getMeshControl-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Mesh.MeshPart.MeshPart.getMeshControl.region "Permalink to this definition")
            :   A Cell, a Face, or an Edge object specifying the region to be queried.

            attribute[¶](#abaqus.Mesh.MeshPart.MeshPart.getMeshControl.attribute "Permalink to this definition")
            :   A SymbolicConstant specifying the mesh control attribute to return. Possible values are:

                * ELEM\_SHAPE
                * TECHNIQUE
                * ALGORITHM
                * MIN\_TRANSITION

                The return value is dependent on the **attribute** argument.

                * If **attribute** = ELEM\_SHAPE, the return value is a SymbolicConstant specifying the
                  element shape used during meshing. Possible values are: LINE, QUAD, TRI, QUAD\_DOMINATED, HEX, TET, WEDGE, HEX\_DOMINATED
                * If **attribute** = TECHNIQUE, the return value is a SymbolicConstant specifying the
                  meshing technique to be used during meshing. Possible values are: FREE, STRUCTURED, SWEEP, UNMESHABLE, Where UNMESHABLE indicates that no meshing technique is applicable with the currently assigned element shape.
                * If **attribute** = ALGORITHM, the return value is a SymbolicConstant specifying the
                  meshing algorithm to be used during meshing. Possible values are: MEDIAL\_AXIS, ADVANCING\_FRONT, DEFAULT, NON\_DEFAULT, NONE, Where NONE indicates that no algorithm is applicable.
                * If **attribute** = MIN\_TRANSITION, the return value is a Boolean indicating whether
                  minimum transition will be used during meshing. This option is applicable only to the
                  following: Free quadrilateral meshing or sweep hexahedral meshing with **algorithm** = MEDIAL\_AXIS, Structured quadrilateral meshing.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshPart.getMeshControl-returns "Permalink to this headline")
        :   The return value is a SymbolicConstant or a Boolean depending on the value of the
            **attribute** argument.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshPart.getMeshControl-return-type "Permalink to this headline")
        :   `Union[bool`, `SymbolicConstant]`

        Raises:[¶](#abaqus.Mesh.MeshPart.MeshPart.getMeshControl-raises "Permalink to this headline")
        :   [**TypeError**](https://docs.python.org/3/library/exceptions.html#TypeError "(in Python v3.13)") – The region cannot carry mesh controls.

    getMeshStats(*[regions](#abaqus.Mesh.MeshPart.MeshPart.getMeshStats.regions "abaqus.Mesh.MeshPart.MeshPart.getMeshStats.regions (Python parameter) — A sequence or tuple of ConstrainedSketchGeometry regions for which mesh statistics should be returned.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L660-L674)[¶](#abaqus.Mesh.MeshPart.MeshPart.getMeshStats "Permalink to this definition")
    :   This method returns the mesh statistics for the given regions.

        Note

        Check [MeshPart.getMeshStats on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partgetmeshstatspyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.getMeshStats-parameters "Permalink to this headline")
        :   regions[¶](#abaqus.Mesh.MeshPart.MeshPart.getMeshStats.regions "Permalink to this definition")
            :   A sequence or tuple of ConstrainedSketchGeometry regions for which mesh statistics should be returned.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshPart.getMeshStats-returns "Permalink to this headline")
        :   A MeshStats object.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshPart.getMeshStats-return-type "Permalink to this headline")
        :   `MeshStats`

    getPartSeeds(*[attribute](#abaqus.Mesh.MeshPart.MeshPart.getPartSeeds.attribute "abaqus.Mesh.MeshPart.MeshPart.getPartSeeds.attribute (Python parameter) — A SymbolicConstant specifying the type of part seed attribute to return.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L676-L722)[¶](#abaqus.Mesh.MeshPart.MeshPart.getPartSeeds "Permalink to this definition")
    :   This method returns a part seed parameter for the part.

        Note

        Check [MeshPart.getPartSeeds on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partgetpartseedspyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.getPartSeeds-parameters "Permalink to this headline")
        :   attribute[¶](#abaqus.Mesh.MeshPart.MeshPart.getPartSeeds.attribute "Permalink to this definition")
            :   A SymbolicConstant specifying the type of part seed attribute to return. Possible values
                are:

                * SIZE
                * DEFAULT\_SIZE
                * DEVIATION\_FACTOR
                * MIN\_SIZE\_FACTOR

                The return value depends on the value of the **attribute** argument.

                * If **attribute** = SIZE, the return value is a Float specifying the assigned global
                  element size. If part seeds are not defined, the return value is zero.
                * If **attribute** = DEFAULT\_SIZE, the return value is a Float specifying a suggested
                  default global element size based upon the part geometry.
                * If **attribute** = DEVIATION\_FACTOR, the return value is a Float specifying the deviation
                  factor h/Lh/L, where hh is the chordal deviation and LL is the element length. If part
                  seeds are not defined, the return value is zero.
                * If **attribute** = MIN\_SIZE\_FACTOR, the return value is a Float specifying the size of the
                  smallest allowable element as a fraction of the specified global element size. If part
                  seeds are not defined, the return value is zero.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshPart.getPartSeeds-returns "Permalink to this headline")
        :   The return value is a Float that depends on the value of the **attribute** argument.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshPart.getPartSeeds-return-type "Permalink to this headline")
        :   [`float`](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)")

        Raises:[¶](#abaqus.Mesh.MeshPart.MeshPart.getPartSeeds-raises "Permalink to this headline")
        :   **Error** – Part does not contain native geometry, An exception occurs if the part does not contain native geometry.

    getUnmeshedRegions()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L724-L734)[¶](#abaqus.Mesh.MeshPart.MeshPart.getUnmeshedRegions "Permalink to this definition")
    :   This method returns all geometric regions in the part that require a mesh for submitting an analysis
        but are either unmeshed or are meshed incompletely.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshPart.getUnmeshedRegions-returns "Permalink to this headline")
        :   A Region object, or None.

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshPart.getUnmeshedRegions-return-type "Permalink to this headline")
        :   `Region`

    ignoreEntity(*[entities](#abaqus.Mesh.MeshPart.MeshPart.ignoreEntity.entities "abaqus.Mesh.MeshPart.MeshPart.ignoreEntity.entities (Python parameter) — A sequence of vertices and edges specifying the entities to be ignored during meshing.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L736-L752)[¶](#abaqus.Mesh.MeshPart.MeshPart.ignoreEntity "Permalink to this definition")
    :   This method creates a virtual topology feature. Virtual topology allows unimportant entities to be
        ignored during mesh generation. You can combine two adjacent faces by specifying a common edge to
        ignore. Similarly, you can combine two adjacent edges by specifying a common vertex to ignore.

        Note

        Check [MeshPart.ignoreEntity on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partignoreentitypyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.ignoreEntity-parameters "Permalink to this headline")
        :   entities[¶](#abaqus.Mesh.MeshPart.MeshPart.ignoreEntity.entities "Permalink to this definition")
            :   A sequence of vertices and edges specifying the entities to be ignored during meshing.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshPart.ignoreEntity-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshPart.ignoreEntity-return-type "Permalink to this headline")
        :   `Feature`

    restoreIgnoredEntity(*[entities](#abaqus.Mesh.MeshPart.MeshPart.restoreIgnoredEntity.entities "abaqus.Mesh.MeshPart.MeshPart.restoreIgnoredEntity.entities (Python parameter) — A sequence of IgnoredVertex objects and IgnoredEdge objects specifying the entities to be restored.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L754-L769)[¶](#abaqus.Mesh.MeshPart.MeshPart.restoreIgnoredEntity "Permalink to this definition")
    :   This method restores vertices and edges that have been merged using a virtual topology feature.

        Note

        Check [MeshPart.restoreIgnoredEntity on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partrestoreignoredentitypyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.restoreIgnoredEntity-parameters "Permalink to this headline")
        :   entities[¶](#abaqus.Mesh.MeshPart.MeshPart.restoreIgnoredEntity.entities "Permalink to this definition")
            :   A sequence of IgnoredVertex objects and IgnoredEdge objects specifying the entities to
                be restored.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshPart.restoreIgnoredEntity-returns "Permalink to this headline")
        :   **feature** – A Feature object

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshPart.restoreIgnoredEntity-return-type "Permalink to this headline")
        :   `Feature`

    seedEdgeByBias(*[biasMethod](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.biasMethod "abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.biasMethod (Python parameter) — A SymbolicConstant specifying whether single- or double-biased seed distribution will be applied.")=`abaqusConstants.SINGLE`*, *[end1Edges](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.end1Edges "abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.end1Edges (Python parameter) — A sequence of Edge objects specifying the edges to seed.")=`Ellipsis`*, *[end2Edges](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.end2Edges "abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.end2Edges (Python parameter) — A sequence of Edge objects specifying the edges to seed.")=`Ellipsis`*, *[centerEdges](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.centerEdges "abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.centerEdges (Python parameter) — A sequence of Edge objects specifying the edges to seed.")=`Ellipsis`*, *[endEdges](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.endEdges "abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.endEdges (Python parameter) — A sequence of Edge objects specifying the edges to seed.")=`Ellipsis`*, *[ratio](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.ratio "abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.ratio (Python parameter) — A Float specifying the ratio of the largest element to the smallest element.")=`0`*, *[number](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.number "abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.number (Python parameter) — An Int specifying the number of elements along each edge.")=`Ellipsis`*, *[minSize](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.minSize "abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.minSize (Python parameter) — A Float specifying the desired smallest element size.")=`0`*, *[maxSize](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.maxSize "abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.maxSize (Python parameter) — A Float specifying the desired largest element size.")=`0`*, *[constraint](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.constraint "abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.constraint (Python parameter) — A SymbolicConstant specifying how closely the seeds must be matched by the mesh.")=`Ellipsis`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L771-L836)[¶](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias "Permalink to this definition")
    :   This method seeds the given edges nonuniformly using the specified number of elements and bias ratio
        or the specified minimum and maximum element sizes.

        Note

        Check [MeshPart.seedEdgeByBias on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partseededgebybiaspyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias-parameters "Permalink to this headline")
        :   biasMethod=`abaqusConstants.SINGLE`[¶](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.biasMethod "Permalink to this definition")
            :   A SymbolicConstant specifying whether single- or double-biased seed distribution will be
                applied. If unspecified, single-biased seed distribution will be applied. Possible
                values are:

                * SINGLE: Single-biased seed distribution will be applied.
                * DOUBLE: Double-biased seed distribution will be applied.

            end1Edges=`Ellipsis`[¶](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.end1Edges "Permalink to this definition")
            :   A sequence of Edge objects specifying the edges to seed. The smallest elements will be
                positioned near the end where the normalized curve parameter=0.0. You must provide
                either the **end1Edges** or the **end2Edges** argument or both when **biasMethod** = SINGLE and
                omit both of them when **biasMethod** = DOUBLE. Note: You can determine which end is which by
                the order of the vertex indices returned by getVertices().

            end2Edges=`Ellipsis`[¶](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.end2Edges "Permalink to this definition")
            :   A sequence of Edge objects specifying the edges to seed. The smallest elements will be
                positioned near the end where the normalized curve parameter=1.0.

            centerEdges=`Ellipsis`[¶](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.centerEdges "Permalink to this definition")
            :   A sequence of Edge objects specifying the edges to seed. The smallest elements will be
                positioned near edge center. You must provide either the **centerEdges** or the **endEdges**
                argument or both when **biasMethod** = DOUBLE and omit both of them when
                **biasMethod** = SINGLE.

            endEdges=`Ellipsis`[¶](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.endEdges "Permalink to this definition")
            :   A sequence of Edge objects specifying the edges to seed. The smallest elements will be
                positioned near edge ends.

            ratio=`0`[¶](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.ratio "Permalink to this definition")
            :   A Float specifying the ratio of the largest element to the smallest element. Possible
                values are 1.0 ≤ **ratio** ≤ 10⁶.

            number=`Ellipsis`[¶](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.number "Permalink to this definition")
            :   An Int specifying the number of elements along each edge. Possible values are 1 ≤
                **number** ≤ 10⁴.

            minSize=`0`[¶](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.minSize "Permalink to this definition")
            :   A Float specifying the desired smallest element size.

            maxSize=`0`[¶](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.maxSize "Permalink to this definition")
            :   A Float specifying the desired largest element size. Note: You must specify either the
                **ratio** and **number** or **minSize** and **maxSize** pair of arguments.

            constraint=`Ellipsis`[¶](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByBias.constraint "Permalink to this definition")
            :   A SymbolicConstant specifying how closely the seeds must be matched by the mesh. The
                default value is FREE. If unspecified, the existing constraint will remain unchanged.
                Possible values are:

                * FREE: The resulting mesh can be finer or coarser than the specified seeds.
                * FINER: The resulting mesh can be finer than the specified seeds.
                * FIXED: The seeds must be exactly matched by the mesh (only with respect to the number
                  of elements, not to the nodal positioning).

    seedEdgeByNumber(*[edges](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByNumber.edges "abaqus.Mesh.MeshPart.MeshPart.seedEdgeByNumber.edges (Python parameter) — A sequence of Edge objects specifying the edges to seed.")*, *[number](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByNumber.number "abaqus.Mesh.MeshPart.MeshPart.seedEdgeByNumber.number (Python parameter) — An Int specifying the number of elements along each edge.")*, *[constraint](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByNumber.constraint "abaqus.Mesh.MeshPart.MeshPart.seedEdgeByNumber.constraint (Python parameter) — A SymbolicConstant specifying how closely the seeds must be matched by the mesh.")=`Ellipsis`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L838-L864)[¶](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByNumber "Permalink to this definition")
    :   This method seeds the given edges uniformly based on the number of elements along the edges.

        Note

        Check [MeshPart.seedEdgeByNumber on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partseededgebynumberpyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByNumber-parameters "Permalink to this headline")
        :   edges[¶](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByNumber.edges "Permalink to this definition")
            :   A sequence of Edge objects specifying the edges to seed.

            number[¶](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByNumber.number "Permalink to this definition")
            :   An Int specifying the number of elements along each edge. Possible values are 1 ≤
                **number** ≤ 10⁴.

            constraint=`Ellipsis`[¶](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeByNumber.constraint "Permalink to this definition")
            :   A SymbolicConstant specifying how closely the seeds must be matched by the mesh. The
                default value is FREE. If unspecified, the existing constraint will remain unchanged.
                Possible values are:

                * FREE: The resulting mesh can be finer or coarser than the specified seeds.
                * FINER: The resulting mesh can be finer than the specified seeds.
                * FIXED: The seeds must be exactly matched by the mesh (only with respect to the number
                  of elements, not to the nodal positioning).

    seedEdgeBySize(*[edges](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeBySize.edges "abaqus.Mesh.MeshPart.MeshPart.seedEdgeBySize.edges (Python parameter) — A sequence of Edge objects specifying the edges to seed.")*, *[size](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeBySize.size "abaqus.Mesh.MeshPart.MeshPart.seedEdgeBySize.size (Python parameter) — A Float specifying the desired element size.")*, *[deviationFactor](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeBySize.deviationFactor "abaqus.Mesh.MeshPart.MeshPart.seedEdgeBySize.deviationFactor (Python parameter) — A Float specifying the deviation factor h/Lh/L, where hh is the chordal deviation and LL is the element length.")=`None`*, *[minSizeFactor](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeBySize.minSizeFactor "abaqus.Mesh.MeshPart.MeshPart.seedEdgeBySize.minSizeFactor (Python parameter) — A Float specifying the size of the smallest allowable element as a fraction of the specified global element size.")=`None`*, *[constraint](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeBySize.constraint "abaqus.Mesh.MeshPart.MeshPart.seedEdgeBySize.constraint (Python parameter) — A SymbolicConstant specifying how closely the seeds must be matched by the mesh.")=`Ellipsis`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L866-L900)[¶](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeBySize "Permalink to this definition")
    :   This method seeds the given edges either uniformly or following edge curvature distribution, based on
        the desired element size.

        Note

        Check [MeshPart.seedEdgeBySize on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partseededgebysizepyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeBySize-parameters "Permalink to this headline")
        :   edges[¶](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeBySize.edges "Permalink to this definition")
            :   A sequence of Edge objects specifying the edges to seed.

            size[¶](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeBySize.size "Permalink to this definition")
            :   A Float specifying the desired element size.

            deviationFactor=`None`[¶](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeBySize.deviationFactor "Permalink to this definition")
            :   A Float specifying the deviation factor h/Lh/L, where hh is the chordal deviation and LL
                is the element length.

            minSizeFactor=`None`[¶](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeBySize.minSizeFactor "Permalink to this definition")
            :   A Float specifying the size of the smallest allowable element as a fraction of the
                specified global element size.

            constraint=`Ellipsis`[¶](#abaqus.Mesh.MeshPart.MeshPart.seedEdgeBySize.constraint "Permalink to this definition")
            :   A SymbolicConstant specifying how closely the seeds must be matched by the mesh. The
                default value is FREE. If unspecified, the existing constraint will remain unchanged.
                Possible values are:

                * FREE: The resulting mesh can be finer or coarser than the specified seeds.
                * FINER: The resulting mesh can be finer than the specified seeds.
                * FIXED: The seeds must be exactly matched by the mesh (only with respect to the number
                  of elements, not to the nodal positioning).

    seedPart(*[size](#abaqus.Mesh.MeshPart.MeshPart.seedPart.size "abaqus.Mesh.MeshPart.MeshPart.seedPart.size (Python parameter) — A Float specifying the desired global element size for the edges.")*, *[deviationFactor](#abaqus.Mesh.MeshPart.MeshPart.seedPart.deviationFactor "abaqus.Mesh.MeshPart.MeshPart.seedPart.deviationFactor (Python parameter) — A Float specifying the deviation factor h/Lh/L, where hh is the chordal deviation and LL is the element length.")=`None`*, *[minSizeFactor](#abaqus.Mesh.MeshPart.MeshPart.seedPart.minSizeFactor "abaqus.Mesh.MeshPart.MeshPart.seedPart.minSizeFactor (Python parameter) — A Float specifying the size of the smallest allowable element as a fraction of the specified global element size.")=`None`*, *[constraint](#abaqus.Mesh.MeshPart.MeshPart.seedPart.constraint "abaqus.Mesh.MeshPart.MeshPart.seedPart.constraint (Python parameter) — A SymbolicConstant specifying how closely the seeds must be matched by the mesh.")=`Ellipsis`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L902-L930)[¶](#abaqus.Mesh.MeshPart.MeshPart.seedPart "Permalink to this definition")
    :   This method assigns global edge seeds to the given parts.

        Note

        Check [MeshPart.seedPart on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partseedpartpyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.seedPart-parameters "Permalink to this headline")
        :   size[¶](#abaqus.Mesh.MeshPart.MeshPart.seedPart.size "Permalink to this definition")
            :   A Float specifying the desired global element size for the edges.

            deviationFactor=`None`[¶](#abaqus.Mesh.MeshPart.MeshPart.seedPart.deviationFactor "Permalink to this definition")
            :   A Float specifying the deviation factor h/Lh/L, where hh is the chordal deviation and LL
                is the element length.

            minSizeFactor=`None`[¶](#abaqus.Mesh.MeshPart.MeshPart.seedPart.minSizeFactor "Permalink to this definition")
            :   A Float specifying the size of the smallest allowable element as a fraction of the
                specified global element size.

            constraint=`Ellipsis`[¶](#abaqus.Mesh.MeshPart.MeshPart.seedPart.constraint "Permalink to this definition")
            :   A SymbolicConstant specifying how closely the seeds must be matched by the mesh. The
                default value is FREE. If unspecified, the existing constraint will remain unchanged.
                Possible values are:

                * FREE: The resulting mesh can be finer or coarser than the specified seeds.
                * FINER: The resulting mesh can be finer than the specified seeds.

    setBoundaryLayerControls(*[regions](#abaqus.Mesh.MeshPart.MeshPart.setBoundaryLayerControls.regions "abaqus.Mesh.MeshPart.MeshPart.setBoundaryLayerControls.regions (Python parameter) — A sequence of Cell objects specifying the regions for which to set the boundary layer mesh control parameters.")*, *[firstElemSize](#abaqus.Mesh.MeshPart.MeshPart.setBoundaryLayerControls.firstElemSize "abaqus.Mesh.MeshPart.MeshPart.setBoundaryLayerControls.firstElemSize (Python parameter) — A Float specifying the height of the first element layer off boundary.")*, *[growthFactor](#abaqus.Mesh.MeshPart.MeshPart.setBoundaryLayerControls.growthFactor "abaqus.Mesh.MeshPart.MeshPart.setBoundaryLayerControls.growthFactor (Python parameter) — A Float specifying the ratio of heights of any two consecutive element layers.")*, *[numLayers](#abaqus.Mesh.MeshPart.MeshPart.setBoundaryLayerControls.numLayers "abaqus.Mesh.MeshPart.MeshPart.setBoundaryLayerControls.numLayers (Python parameter) — An Int specifying the number of element layers to be generated.")*, *[inactiveFaces](#abaqus.Mesh.MeshPart.MeshPart.setBoundaryLayerControls.inactiveFaces "abaqus.Mesh.MeshPart.MeshPart.setBoundaryLayerControls.inactiveFaces (Python parameter) — A sequence of Face objects specifying the faces where boundary layer should not be generated.")=`()`*, *[setName](#abaqus.Mesh.MeshPart.MeshPart.setBoundaryLayerControls.setName "abaqus.Mesh.MeshPart.MeshPart.setBoundaryLayerControls.setName (Python parameter) — A String specifying a unique name for a set that will contain boundary layer elements.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L932-L965)[¶](#abaqus.Mesh.MeshPart.MeshPart.setBoundaryLayerControls "Permalink to this definition")
    :   This method sets the control parameters for boundary layer mesh for the specified regions.

        Note

        Check [MeshPart.setBoundaryLayerControls on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partsetboundarylayercontrolspyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.setBoundaryLayerControls-parameters "Permalink to this headline")
        :   regions[¶](#abaqus.Mesh.MeshPart.MeshPart.setBoundaryLayerControls.regions "Permalink to this definition")
            :   A sequence of Cell objects specifying the regions for which to set the boundary layer
                mesh control parameters.

            firstElemSize[¶](#abaqus.Mesh.MeshPart.MeshPart.setBoundaryLayerControls.firstElemSize "Permalink to this definition")
            :   A Float specifying the height of the first element layer off boundary. Possible values
                are 0.0 < **firstElemSize** ≤ 10⁶.

            growthFactor[¶](#abaqus.Mesh.MeshPart.MeshPart.setBoundaryLayerControls.growthFactor "Permalink to this definition")
            :   A Float specifying the ratio of heights of any two consecutive element layers. Possible
                values are 1.0 ≤ **growthFactor** ≤ 10.0.

            numLayers[¶](#abaqus.Mesh.MeshPart.MeshPart.setBoundaryLayerControls.numLayers "Permalink to this definition")
            :   An Int specifying the number of element layers to be generated. Possible values are 1 ≤
                **numLayers** ≤ 10⁴.

            inactiveFaces=`()`[¶](#abaqus.Mesh.MeshPart.MeshPart.setBoundaryLayerControls.inactiveFaces "Permalink to this definition")
            :   A sequence of Face objects specifying the faces where boundary layer should not be
                generated. By default, boundary layer mesh will be generated on all faces of the
                selected regions.

            setName=`''`[¶](#abaqus.Mesh.MeshPart.MeshPart.setBoundaryLayerControls.setName "Permalink to this definition")
            :   A String specifying a unique name for a set that will contain boundary layer elements.

    setElementType(*[regions](#abaqus.Mesh.MeshPart.MeshPart.setElementType.regions "abaqus.Mesh.MeshPart.MeshPart.setElementType.regions (Python parameter) — A sequence of ConstrainedSketchGeometry regions or MeshElement objects, or a Set object containing either geometry regions or elements, specifying the regions to which element types are to be assigned.")*, *[elemTypes](#abaqus.Mesh.MeshPart.MeshPart.setElementType.elemTypes "abaqus.Mesh.MeshPart.MeshPart.setElementType.elemTypes (Python parameter) — A sequence of ElemType objects, one for each element shape applicable to the regions.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L967-L999)[¶](#abaqus.Mesh.MeshPart.MeshPart.setElementType "Permalink to this definition")
    :   This method assigns element types to the specified regions.

        Note

        Check [MeshPart.setElementType on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partsetelementtypepyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.setElementType-parameters "Permalink to this headline")
        :   regions[¶](#abaqus.Mesh.MeshPart.MeshPart.setElementType.regions "Permalink to this definition")
            :   A sequence of ConstrainedSketchGeometry regions or MeshElement objects, or a Set object containing either
                geometry regions or elements, specifying the regions to which element types are to be
                assigned.

            elemTypes[¶](#abaqus.Mesh.MeshPart.MeshPart.setElementType.elemTypes "Permalink to this definition")
            :   A sequence of ElemType objects, one for each element shape applicable to the
                regions. Note: If an ElemType object has an UNKNOWN\_\*xxx\* value for **elemCode**, its order
                will be deduced from the order of other valid ElemType objects within the same
                setElementType command. If no valid ElemType objects can be found, the order will remain
                unchanged.

        Raises:[¶](#abaqus.Mesh.MeshPart.MeshPart.setElementType-raises "Permalink to this headline")
        :   [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.13)") – As a result of the element assignment, a region must have the same library, family, and
            order for all its assigned element types. Otherwise, an exception will be thrown.
            For example, suppose the Hex, Wedge, and Tet elements previously assigned to a cell are
            all linear. The user now constructs an ElemType object with a quadratic Hex element and
            includes only this object in the setElementType command. An exception will be thrown
            because the Wedge and Tet elements will remain linear (i.e., As Is) and become
            incompatible with the newly assigned quadratic Hex element.

    setLogicalCorners(*[region](#abaqus.Mesh.MeshPart.MeshPart.setLogicalCorners.region "abaqus.Mesh.MeshPart.MeshPart.setLogicalCorners.region (Python parameter) — A Face region.")*, *[corners](#abaqus.Mesh.MeshPart.MeshPart.setLogicalCorners.corners "abaqus.Mesh.MeshPart.MeshPart.setLogicalCorners.corners (Python parameter) — Three, four, or five ConstrainedSketchVertex objects defining the logical corners for a given mappable face region.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L1001-L1013)[¶](#abaqus.Mesh.MeshPart.MeshPart.setLogicalCorners "Permalink to this definition")
    :   This method sets the logical corners for a mappable face region.

        Note

        Check [MeshPart.setLogicalCorners on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partsetlogicalcornerspyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.setLogicalCorners-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Mesh.MeshPart.MeshPart.setLogicalCorners.region "Permalink to this definition")
            :   A Face region.

            corners[¶](#abaqus.Mesh.MeshPart.MeshPart.setLogicalCorners.corners "Permalink to this definition")
            :   Three, four, or five ConstrainedSketchVertex objects defining the logical corners for a given mappable
                face region.

    setMeshControls(*[regions](#abaqus.Mesh.MeshPart.MeshPart.setMeshControls.regions "abaqus.Mesh.MeshPart.MeshPart.setMeshControls.regions (Python parameter) — A sequence of Face or Cell regions specifying the regions for which to set the mesh control parameters.")*, *[elemShape](#abaqus.Mesh.MeshPart.MeshPart.setMeshControls.elemShape "abaqus.Mesh.MeshPart.MeshPart.setMeshControls.elemShape (Python parameter) — A SymbolicConstant specifying the element shape to be used for meshing.")=`None`*, *[technique](#abaqus.Mesh.MeshPart.MeshPart.setMeshControls.technique "abaqus.Mesh.MeshPart.MeshPart.setMeshControls.technique (Python parameter) — A SymbolicConstant specifying the mesh technique to be used.")=`None`*, *[algorithm](#abaqus.Mesh.MeshPart.MeshPart.setMeshControls.algorithm "abaqus.Mesh.MeshPart.MeshPart.setMeshControls.algorithm (Python parameter) — A SymbolicConstant specifying the algorithm used to generate the mesh for the specified regions.")=`None`*, *[minTransition](#abaqus.Mesh.MeshPart.MeshPart.setMeshControls.minTransition "abaqus.Mesh.MeshPart.MeshPart.setMeshControls.minTransition (Python parameter) — A Boolean specifying whether minimum transition is to be applied.")=`1`*, *[sizeGrowth](#abaqus.Mesh.MeshPart.MeshPart.setMeshControls.sizeGrowth "abaqus.Mesh.MeshPart.MeshPart.setMeshControls.sizeGrowth (Python parameter) — A SymbolicConstant specifying element size growth to be applied when generating the interior of a tetrahedral mesh.")=`None`*, *[allowMapped](#abaqus.Mesh.MeshPart.MeshPart.setMeshControls.allowMapped "abaqus.Mesh.MeshPart.MeshPart.setMeshControls.allowMapped (Python parameter) — A Boolean specifying whether mapped meshing can be used to replace the selected mesh technique.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L1015-L1093)[¶](#abaqus.Mesh.MeshPart.MeshPart.setMeshControls "Permalink to this definition")
    :   This method sets the mesh control parameters for the specified regions.

        Note

        Check [MeshPart.setMeshControls on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partsetmeshcontrolspyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.setMeshControls-parameters "Permalink to this headline")
        :   regions[¶](#abaqus.Mesh.MeshPart.MeshPart.setMeshControls.regions "Permalink to this definition")
            :   A sequence of Face or Cell regions specifying the regions for which to set the mesh
                control parameters.

            elemShape=`None`[¶](#abaqus.Mesh.MeshPart.MeshPart.setMeshControls.elemShape "Permalink to this definition")
            :   A SymbolicConstant specifying the element shape to be used for meshing. The default
                value is QUAD for Face regions and HEX for Cell regions. If unspecified, the existing
                element shape will remain unchanged. Possible values are:

                * QUAD: Quadrilateral mesh.
                * QUAD\_DOMINATED: Quadrilateral-dominated mesh.
                * TRI: Triangular mesh.
                * HEX: Hexahedral mesh.
                * HEX\_DOMINATED: Hex-dominated mesh.
                * TET: Tetrahedral mesh.
                * WEDGE: Wedge mesh.

            technique=`None`[¶](#abaqus.Mesh.MeshPart.MeshPart.setMeshControls.technique "Permalink to this definition")
            :   A SymbolicConstant specifying the mesh technique to be used. The default value is FREE
                for Face regions. For Cell regions the initial value depends on the geometry of the
                regions and can be STRUCTURED, SWEEP, or unmeshable. If unspecified, the existing mesh
                technique(s) will remain unchanged. Possible values are:

                * FREE: Free mesh technique.
                * STRUCTURED: Structured mesh technique.
                * SWEEP: Sweep mesh technique.
                * BOTTOM\_UP: Bottom-up mesh technique. Only applicable for cell regions.
                * SYSTEM\_ASSIGN: Allow the system to assign a suitable technique. The actual technique
                  assigned can be STRUCTURED, SWEEP, or unmeshable.

            algorithm=`None`[¶](#abaqus.Mesh.MeshPart.MeshPart.setMeshControls.algorithm "Permalink to this definition")
            :   A SymbolicConstant specifying the algorithm used to generate the mesh for the specified
                regions. Possible values are MEDIAL\_AXIS, ADVANCING\_FRONT, and NON\_DEFAULT. If
                unspecified, the existing value will remain unchanged. This option is applicable only to
                the following:

                * Free quadrilateral or quadrilateral-dominated meshing. In this case the possible
                  values are MEDIAL\_AXIS and ADVANCING\_FRONT.
                * Sweep hexahedral or hexahedral-dominated meshing. In this case the possible values are
                  MEDIAL\_AXIS and ADVANCING\_FRONT.
                * Free tetrahedral meshing. In this case the only possible value is NON\_DEFAULT, and it
                  indicates that the free tetrahedral-meshing technique available in Abaqus 6.4 or earlier
                  will be used. If algorithm is not specified, the default

            minTransition=`1`[¶](#abaqus.Mesh.MeshPart.MeshPart.setMeshControls.minTransition "Permalink to this definition")
            :   A Boolean specifying whether minimum transition is to be applied. The default value is
                ON. If unspecified, the existing value will remain unchanged. This option is applicable
                only in the following cases:

                * Free quadrilateral meshing or hexahedral sweep meshing with **algorithm** = MEDIAL\_AXIS.
                * Structured quadrilateral meshing.

            sizeGrowth=`None`[¶](#abaqus.Mesh.MeshPart.MeshPart.setMeshControls.sizeGrowth "Permalink to this definition")
            :   A SymbolicConstant specifying element size growth to be applied when generating the
                interior of a tetrahedral mesh. Possible values are MODERATE and MAXIMUM. If
                unspecified, the existing value will remain unchanged. This option only applies to the
                default tetrahedral mesher.

            allowMapped=`0`[¶](#abaqus.Mesh.MeshPart.MeshPart.setMeshControls.allowMapped "Permalink to this definition")
            :   A Boolean specifying whether mapped meshing can be used to replace the selected mesh
                technique. The **allowMapped** argument is applicable only in the following cases:

                * Free triangular meshing.
                * Free quadrilateral or quadrilateral-dominated meshing with
                  **algorithm** = ADVANCING\_FRONT.
                * Hexahedral or hexahedral-dominated sweep meshing with **algorithm** = ADVANCING\_FRONT.
                * Free tetrahedral meshing. **allowMapped** = True implies that mapped triangular meshing
                  can be used on faces that bound three-dimensional **regions**.

    setSweepPath(*[region](#abaqus.Mesh.MeshPart.MeshPart.setSweepPath.region "abaqus.Mesh.MeshPart.MeshPart.setSweepPath.region (Python parameter) — A sweepable region.")*, *[edge](#abaqus.Mesh.MeshPart.MeshPart.setSweepPath.edge "abaqus.Mesh.MeshPart.MeshPart.setSweepPath.edge (Python parameter) — An Edge object specifying the sweep or revolve path.")*, *[sense](#abaqus.Mesh.MeshPart.MeshPart.setSweepPath.sense "abaqus.Mesh.MeshPart.MeshPart.setSweepPath.sense (Python parameter) — A SymbolicConstant specifying the sweep sense.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L1095-L1111)[¶](#abaqus.Mesh.MeshPart.MeshPart.setSweepPath "Permalink to this definition")
    :   This method sets the sweep path for a sweepable region or the revolve path for a revolvable region.

        Note

        Check [MeshPart.setSweepPath on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partsetsweeppathpyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.setSweepPath-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Mesh.MeshPart.MeshPart.setSweepPath.region "Permalink to this definition")
            :   A sweepable region.

            edge[¶](#abaqus.Mesh.MeshPart.MeshPart.setSweepPath.edge "Permalink to this definition")
            :   An Edge object specifying the sweep or revolve path.

            sense[¶](#abaqus.Mesh.MeshPart.MeshPart.setSweepPath.sense "Permalink to this definition")
            :   A SymbolicConstant specifying the sweep sense. The sense will affect only how gasket
                elements will be created; it will have no effect if gasket elements are not used.
                Possible values are FORWARD or REVERSE.If **sense** = FORWARD, the sense of the given edge’s
                underlying curve will be used.

    verifyMeshQuality(*[criterion](#abaqus.Mesh.MeshPart.MeshPart.verifyMeshQuality.criterion "abaqus.Mesh.MeshPart.MeshPart.verifyMeshQuality.criterion (Python parameter) — A SymbolicConstant specifying the criterion used for the quality check.")*, *[threshold](#abaqus.Mesh.MeshPart.MeshPart.verifyMeshQuality.threshold "abaqus.Mesh.MeshPart.MeshPart.verifyMeshQuality.threshold (Python parameter) — A Float value used to determine low quality elements according to the specified criterion.")=`None`*, *[elemShape](#abaqus.Mesh.MeshPart.MeshPart.verifyMeshQuality.elemShape "abaqus.Mesh.MeshPart.MeshPart.verifyMeshQuality.elemShape (Python parameter) — A SymbolicConstant specifying an element shape for limiting the query.")=`None`*, *[regions](#abaqus.Mesh.MeshPart.MeshPart.verifyMeshQuality.regions "abaqus.Mesh.MeshPart.MeshPart.verifyMeshQuality.regions (Python parameter) — A sequence of Region or MeshElement objects.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshPart.py#L1113-L1204)[¶](#abaqus.Mesh.MeshPart.MeshPart.verifyMeshQuality "Permalink to this definition")
    :   This method tests the mesh quality of a part and returns poor-quality elements.

        Note

        Check [MeshPart.verifyMeshQuality on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partmgnpyc.htm?contextscope=all#simaker-partverifymeshqualitypyc).

        Parameters:[¶](#abaqus.Mesh.MeshPart.MeshPart.verifyMeshQuality-parameters "Permalink to this headline")
        :   criterion[¶](#abaqus.Mesh.MeshPart.MeshPart.verifyMeshQuality.criterion "Permalink to this definition")
            :   A SymbolicConstant specifying the criterion used for the quality check. Possible values
                are:

                * ANALYSIS\_CHECKS
                  When this criterion is specified Abaqus/CAE will invoke the element quality checks
                  included with the input file processor for Abaqus/Standard and Abaqus/Explicit.
                * ANGULAR\_DEVIATION
                  The maximum amount (in degrees) that an element’s face corner angles deviate from the
                  ideal angle. The ideal angle is 90° for quadrilateral element faces and 60° for
                  triangular element faces. Elements with an angular deviation larger than the specified
                  threshold will fail this test.
                * ASPECT\_RATIO
                  The ratio between the lengths of the longest and shortest edges of an element. Elements
                  with an aspect ratio larger than the specified threshold will fail this test.
                * GEOM\_DEVIATION\_FACTOR
                  The largest geometric deviation factor evaluated along any of the element edges
                  associated with geometric edges or faces. The geometric deviation factor along an
                  element edge is calculated by dividing the maximum gap between the element edge and its
                  associated geometry by the length of the element edge. Elements with a geometric
                  deviation factor larger than the specified threshold will fail this test.
                * LARGE\_ANGLE
                  The largest corner angle on any of an element’s faces. Elements with face angles larger
                  than the specified threshold (in degrees) will fail this test.
                * LONGEST\_EDGE
                  The length of an element’s longest edge. Elements with an edge longer than the specified
                  threshold will fail this test.
                * MAX\_FREQUENCY
                  An estimate of an element’s contribution to the initial maximum allowable frequency for
                  Abaqus/Standard analyses. This calculation requires appropriate section assignments and
                  material definitions. Elements whose maximum allowable frequency is smaller than the
                  given value will fail this test.
                * SHAPE\_FACTOR
                  The shape factor for triangular and tetrahedral elements. This is the ratio between the
                  element area or volume and the optimal element area or volume. Elements with a shape
                  factor smaller than the specified threshold will fail this test.
                * SHORTEST\_EDGE
                  The length of an element’s shortest edge. Elements with an edge shorter than the
                  specified threshold will fail this test.
                * SMALL\_ANGLE
                  The smallest corner angle on any of an element’s faces. Elements with face angles
                  smaller than the given value (in degrees) will fail this test.
                * STABLE\_TIME\_INCREMENT
                  An estimate of an element’s contribution to the initial maximum stable time increment
                  for Abaqus/Explicit analyses. This calculation requires appropriate section assignments
                  and material definitions. Elements that require a time increment smaller than the given
                  value will fail this test.

            threshold=`None`[¶](#abaqus.Mesh.MeshPart.MeshPart.verifyMeshQuality.threshold "Permalink to this definition")
            :   A Float value used to determine low quality elements according to the specified
                criterion. This argument is ignored when the ANALYSIS\_CHECKS criterion is used. For
                other criterion, if this argument is unspecified then no list of failed elements will be
                returned.

            elemShape=`None`[¶](#abaqus.Mesh.MeshPart.MeshPart.verifyMeshQuality.elemShape "Permalink to this definition")
            :   A SymbolicConstant specifying an element shape for limiting the query. Possible values
                are LINE, QUAD, TRI, HEX, WEDGE, and TET.

            regions=`()`[¶](#abaqus.Mesh.MeshPart.MeshPart.verifyMeshQuality.regions "Permalink to this definition")
            :   A sequence of Region or MeshElement objects. If you do not specify the **regions**
                argument, the entire part mesh is considered.

        Returns:[¶](#abaqus.Mesh.MeshPart.MeshPart.verifyMeshQuality-returns "Permalink to this headline")
        :   A Dictionary object containing values for some number of the following keys:
            failedElements, warningElements, naElements (sequences of MeshElement objects);
            numElements (Int); average, worst (Float); worstElement
            (MeshElement object) .

        Return type:[¶](#abaqus.Mesh.MeshPart.MeshPart.verifyMeshQuality-return-type "Permalink to this headline")
        :   `dict[str`, `int | float`, `MeshElement]`

*class* MeshStats[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshStats.py#L6-L45)[¶](#abaqus.Mesh.MeshStats.MeshStats "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The MeshStats object is a query object for holding mesh statistics and is returned by the getMeshStats
    command. The object does not have any methods.

    Note

    This object can be accessed by:

    ```python
    import mesh
    ```

    Note

    Check [MeshStats on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-meshstatspyc.htm?contextscope=all).

    Member Details:

    numHexElems : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshStats.py#L29-L30)[¶](#abaqus.Mesh.MeshStats.MeshStats.numHexElems "Permalink to this definition")
    :   An Int specifying the number of hexahedral elements.

    numLineElems : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshStats.py#L20-L21)[¶](#abaqus.Mesh.MeshStats.MeshStats.numLineElems "Permalink to this definition")
    :   An Int specifying the number of line elements.

    numMeshedRegions : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshStats.py#L6-L45)[¶](#abaqus.Mesh.MeshStats.MeshStats.numMeshedRegions "Permalink to this definition")
    :   An Int specifying the number of regions that contain a mesh.

    numNodes : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshStats.py#L41-L42)[¶](#abaqus.Mesh.MeshStats.MeshStats.numNodes "Permalink to this definition")
    :   An Int specifying the number of nodes.

    numPointElems : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshStats.py#L17-L18)[¶](#abaqus.Mesh.MeshStats.MeshStats.numPointElems "Permalink to this definition")
    :   An Int specifying the number of point elements.

    numPyramidElems : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshStats.py#L38-L39)[¶](#abaqus.Mesh.MeshStats.MeshStats.numPyramidElems "Permalink to this definition")
    :   An Int specifying the number of pyramid elements.

    numQuadElems : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshStats.py#L23-L24)[¶](#abaqus.Mesh.MeshStats.MeshStats.numQuadElems "Permalink to this definition")
    :   An Int specifying the number of quadrilateral elements.

    numTetElems : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshStats.py#L35-L36)[¶](#abaqus.Mesh.MeshStats.MeshStats.numTetElems "Permalink to this definition")
    :   An Int specifying the number of tetrahedral elements.

    numTriElems : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshStats.py#L26-L27)[¶](#abaqus.Mesh.MeshStats.MeshStats.numTriElems "Permalink to this definition")
    :   An Int specifying the number of triangular elements.

    numWedgeElems : --is-rst--:py:data:`~typing.Optional`\[:py:class:`int`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MeshStats.py#L32-L33)[¶](#abaqus.Mesh.MeshStats.MeshStats.numWedgeElems "Permalink to this definition")
    :   An Int specifying the number of wedge elements.

*class* MesherOptions[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MesherOptions.py#L19-L80)[¶](#abaqus.Mesh.MesherOptions.MesherOptions "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The MesherOptions object controls the default settings that Abaqus uses for all meshing methods. The
    MesherOptions object has no constructor. Abaqus creates the **MesherOptions** member when a session is
    started. MesherOptions commands are intended for use at the beginning of scripts and in the abaqus\_v6.env
    file only; they should not be used during an Abaqus/CAE session.

    Note

    This object can be accessed by:

    ```python
    session.defaultMesherOptions
    ```

    Note

    Check [MesherOptions on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mesheroptionspyc.htm?contextscope=all).

    Member Details:

    setValues(*[elemShape2D](#abaqus.Mesh.MesherOptions.MesherOptions.setValues.elemShape2D "abaqus.Mesh.MesherOptions.MesherOptions.setValues.elemShape2D (Python parameter) — A SymbolicConstant specifying the default element shape for meshing two-dimensional objects.")=`abaqusConstants.QUAD_DOMINATED`*, *[elemShape3D](#abaqus.Mesh.MesherOptions.MesherOptions.setValues.elemShape3D "abaqus.Mesh.MesherOptions.MesherOptions.setValues.elemShape3D (Python parameter) — A SymbolicConstant specifying the default element shape for meshing three-dimensional objects.")=`abaqusConstants.HEX`*, *[quadAlgorithm](#abaqus.Mesh.MesherOptions.MesherOptions.setValues.quadAlgorithm "abaqus.Mesh.MesherOptions.MesherOptions.setValues.quadAlgorithm (Python parameter) — A SymbolicConstant specifying the default algorithm for meshing an object with quad- or quad-dominated elements.")=`abaqusConstants.ADVANCING_FRONT`*, *[allowMapped](#abaqus.Mesh.MesherOptions.MesherOptions.setValues.allowMapped "abaqus.Mesh.MesherOptions.MesherOptions.setValues.allowMapped (Python parameter) — A Boolean specifying whether Abaqus/CAE should allow mapped meshing, where appropriate. The default value is OFF.")=`0`*, *[minTransition](#abaqus.Mesh.MesherOptions.MesherOptions.setValues.minTransition "abaqus.Mesh.MesherOptions.MesherOptions.setValues.minTransition (Python parameter) — A Boolean specifying whether Abaqus/CAE should attempt to minimize the mesh transition when it moves from a coarse mesh to a fine mesh.")=`1`*, *[guiPreferredElements](#abaqus.Mesh.MesherOptions.MesherOptions.setValues.guiPreferredElements "abaqus.Mesh.MesherOptions.MesherOptions.setValues.guiPreferredElements (Python parameter) — A list of SymbolicConstants specifying preferred Abaqus element types.")=`None`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Mesh/MesherOptions.py#L32-L80)[¶](#abaqus.Mesh.MesherOptions.MesherOptions.setValues "Permalink to this definition")
    :   This method modifies the MesherOptions object.

        Note

        Check [MesherOptions.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mesheroptionspyc.htm?contextscope=all#simaker-mesheroptionssetvaluespyc).

        Parameters:[¶](#abaqus.Mesh.MesherOptions.MesherOptions.setValues-parameters "Permalink to this headline")
        :   elemShape2D=`abaqusConstants.QUAD_DOMINATED`[¶](#abaqus.Mesh.MesherOptions.MesherOptions.setValues.elemShape2D "Permalink to this definition")
            :   A SymbolicConstant specifying the default element shape for meshing two-dimensional
                objects. Possible values are QUAD, QUAD\_DOMINATED, and TRI. The default value is
                QUAD\_DOMINATED.

            elemShape3D=`abaqusConstants.HEX`[¶](#abaqus.Mesh.MesherOptions.MesherOptions.setValues.elemShape3D "Permalink to this definition")
            :   A SymbolicConstant specifying the default element shape for meshing three-dimensional
                objects. Possible values are HEX, HEX\_DOMINATED, WEDGE, and TET. The default value is
                HEX.

            quadAlgorithm=`abaqusConstants.ADVANCING_FRONT`[¶](#abaqus.Mesh.MesherOptions.MesherOptions.setValues.quadAlgorithm "Permalink to this definition")
            :   A SymbolicConstant specifying the default algorithm for meshing an object with quad- or
                quad-dominated elements. Possible values are ADVANCING\_FRONT and MEDIAL\_AXIS. The
                default value is ADVANCING\_FRONT.

            allowMapped=`0`[¶](#abaqus.Mesh.MesherOptions.MesherOptions.setValues.allowMapped "Permalink to this definition")
            :   A Boolean specifying whether Abaqus/CAE should allow mapped meshing, where appropriate.
                The default value is OFF.

            minTransition=`1`[¶](#abaqus.Mesh.MesherOptions.MesherOptions.setValues.minTransition "Permalink to this definition")
            :   A Boolean specifying whether Abaqus/CAE should attempt to minimize the mesh transition
                when it moves from a coarse mesh to a fine mesh. The default value is ON.

            guiPreferredElements=`None`[¶](#abaqus.Mesh.MesherOptions.MesherOptions.setValues.guiPreferredElements "Permalink to this definition")
            :   A list of SymbolicConstants specifying preferred Abaqus element types. This setting is
                relevant only when Abaqus/CAE is run interactively. When a part or part instance that
                has never been assigned an element type is meshed, this list is consulted. If an element
                type appropriate to the geometry is found in the list, it is assigned to the geometry.
                Multiple element types representing different shapes (for example, triangles and
                quadrilaterals) can be assigned in combination, but only element types that are
                compatible with each other are used. When more than one appropriate element type is
                found in the list, the first element type encountered takes precedence. This list is
                also consulted when populating the element type dialog; preferred types are selected by
                default for a region not previously assigned any element types. The default value is an
                empty list.

                New in version 2018: The `guiPreferredElements` argument was added.

[Back to top](#)