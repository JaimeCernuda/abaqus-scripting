# Abaqus PROPERTY Module API Reference

> Source: [https://hailin.wang/abqpy/en/2025/reference/mdb/model/property.html](https://hailin.wang/abqpy/en/2025/reference/mdb/model/property.html)
> Downloaded for offline use by Claude Code skills.

---

# Property[¶](#property "Permalink to this heading")

The Property commands are used to create and manage reinforcements and to assign properties to a part.
(See also Material commands and Section commands.) The Property commands are methods of a Part object.

## Create properties for Part[¶](#create-properties-for-part "Permalink to this heading")

*class* PropertyPart(*[name](#abaqus.Property.PropertyPart.PropertyPart "abaqus.Property.PropertyPart.PropertyPart.__init__.name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[dimensionality](#abaqus.Property.PropertyPart.PropertyPart "abaqus.Property.PropertyPart.PropertyPart.__init__.dimensionality (Python parameter)"): [SymbolicConstant](../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.SymbolicConstant "abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant (Python class)")*, *[type](#abaqus.Property.PropertyPart.PropertyPart "abaqus.Property.PropertyPart.PropertyPart.__init__.type (Python parameter)"): [SymbolicConstant](../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.SymbolicConstant "abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant (Python class)")*, *[twist](#abaqus.Property.PropertyPart.PropertyPart "abaqus.Property.PropertyPart.PropertyPart.__init__.twist (Python parameter)"): [AbaqusBoolean](../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.AbaqusBoolean "abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean (Python class)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `OFF`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L33-L446)[¶](#abaqus.Property.PropertyPart.PropertyPart "Permalink to this definition")

*class* PropertyPart(*[name](#abaqus.Property.PropertyPart.PropertyPart "abaqus.Property.PropertyPart.PropertyPart.__init__.name (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[objectToCopy](#abaqus.Property.PropertyPart.PropertyPart "abaqus.Property.PropertyPart.PropertyPart.__init__.objectToCopy (Python parameter)"): [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.13)")*, *[scale](#abaqus.Property.PropertyPart.PropertyPart "abaqus.Property.PropertyPart.PropertyPart.__init__.scale (Python parameter)"): [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.13)") = `1`*, *[mirrorPlane](#abaqus.Property.PropertyPart.PropertyPart "abaqus.Property.PropertyPart.PropertyPart.__init__.mirrorPlane (Python parameter)"): [SymbolicConstant](../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.SymbolicConstant "abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant (Python class)") = `NONE`*, *[compressFeatureList](#abaqus.Property.PropertyPart.PropertyPart "abaqus.Property.PropertyPart.PropertyPart.__init__.compressFeatureList (Python parameter)"): [AbaqusBoolean](../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.AbaqusBoolean "abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean (Python class)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `OFF`*, *[separate](#abaqus.Property.PropertyPart.PropertyPart "abaqus.Property.PropertyPart.PropertyPart.__init__.separate (Python parameter)"): [AbaqusBoolean](../../kernel/utility.html#abaqus.UtilityAndView.abaqusConstants.AbaqusBoolean "abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean (Python class)") | [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.13)") = `OFF`*)
:   Bases: [`PartBase`](part_assembly/part.html#abaqus.Part.PartBase.PartBase "abaqus.Part.PartBase.PartBase (Python class) — Bases: PartFeature")

    Public Data Attributes:

    Inherited from [`PartBase`](part_assembly/part.html#abaqus.Part.PartBase.PartBase "abaqus.Part.PartBase.PartBase (Python class) — Bases: PartFeature")

    |  |  |
    | --- | --- |
    | [`geometryValidity`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.geometryValidity "abaqus.Part.PartBase.PartBase.geometryValidity (Python attribute) — A Boolean specifying the validity of the geometry of the part. The value is computed, but it can be set to ON to perform feature and mesh operations on an invalid part. There is no guarantee that such operations will work if the part was originally invalid.") | A Boolean specifying the validity of the geometry of the part. |
    | [`isOutOfDate`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.isOutOfDate "abaqus.Part.PartBase.PartBase.isOutOfDate (Python attribute) — An Int specifying that feature parameters have been modified but that the part has not been regenerated. Possible values are 0 and 1.") | An Int specifying that feature parameters have been modified but that the part has not been regenerated. |
    | [`timeStamp`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.timeStamp "abaqus.Part.PartBase.PartBase.timeStamp (Python attribute) — A Float specifying when the part was last modified.") | A Float specifying when the part was last modified. |
    | [`vertices`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.vertices "abaqus.Part.PartBase.PartBase.vertices (Python attribute) — A VertexArray object specifying all the vertices in the part.") | A VertexArray object specifying all the vertices in the part. |
    | [`ignoredVertices`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.ignoredVertices "abaqus.Part.PartBase.PartBase.ignoredVertices (Python attribute) — An IgnoredVertexArray object specifying all the ignored vertices in the part.") | An IgnoredVertexArray object specifying all the ignored vertices in the part. |
    | [`edges`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.edges "abaqus.Part.PartBase.PartBase.edges (Python attribute) — An EdgeArray object specifying all the edges in the part.") | An EdgeArray object specifying all the edges in the part. |
    | [`ignoredEdges`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.ignoredEdges "abaqus.Part.PartBase.PartBase.ignoredEdges (Python attribute) — An IgnoredEdgeArray object specifying all the ignored edges in the part.") | An IgnoredEdgeArray object specifying all the ignored edges in the part. |
    | [`faces`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.faces "abaqus.Part.PartBase.PartBase.faces (Python attribute) — A FaceArray object specifying all the faces in the part.") | A FaceArray object specifying all the faces in the part. |
    | [`cells`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.cells "abaqus.Part.PartBase.PartBase.cells (Python attribute) — A CellArray object specifying all the cells in the part.") | A CellArray object specifying all the cells in the part. |
    | [`features`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.features "abaqus.Part.PartBase.PartBase.features (Python attribute) — A repository of Feature objects specifying all the features in the part.") | A repository of Feature objects specifying all the features in the part. |
    | [`featuresById`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.featuresById "abaqus.Part.PartBase.PartBase.featuresById (Python attribute) — A repository of Feature objects specifying all Feature objects in the part. The Feature objects in the featuresById repository are the same as the Feature objects in the features' repository. However, the key to the objects in the featuresById repository is an integer specifying the ID, whereas the key to the objects in the features repository is a string specifying the name.") | A repository of Feature objects specifying all Feature objects in the part. |
    | [`datums`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.datums "abaqus.Part.PartBase.PartBase.datums (Python attribute) — A repository of Datum objects specifying all the datums in the part.") | A repository of Datum objects specifying all the datums in the part. |
    | [`elements`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.elements "abaqus.Part.PartBase.PartBase.elements (Python attribute) — A MeshElementArray object specifying all the elements in the part.") | A MeshElementArray object specifying all the elements in the part. |
    | [`elemFaces`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.elemFaces "abaqus.Part.PartBase.PartBase.elemFaces (Python attribute) — A repository of MeshFace objects specifying all the element faces in the part. For a given element and a given face index within that element, the corresponding MeshFace object can be retrieved from the repository by using the key calculated as (i*8 + j), where i and j are zero-based element and face indices, respectively.") | A repository of MeshFace objects specifying all the element faces in the part. |
    | [`elementFaces`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.elementFaces "abaqus.Part.PartBase.PartBase.elementFaces (Python attribute) — A MeshFaceArray object specifying all the unique element faces in the part.") | A MeshFaceArray object specifying all the unique element faces in the part. |
    | [`nodes`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.nodes "abaqus.Part.PartBase.PartBase.nodes (Python attribute) — A MeshNodeArray object specifying all the nodes in the part.") | A MeshNodeArray object specifying all the nodes in the part. |
    | [`retainedNodes`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.retainedNodes "abaqus.Part.PartBase.PartBase.retainedNodes (Python attribute) — A MeshNodeArray object specifying all the retained nodes in the substructure part.") | A MeshNodeArray object specifying all the retained nodes in the substructure part. |
    | [`sets`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.sets "abaqus.Part.PartBase.PartBase.sets (Python attribute) — A repository of Set objects specifying for more information, see Set.") | A repository of Set objects specifying for more information, see Set. |
    | [`allSets`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.allSets "abaqus.Part.PartBase.PartBase.allSets (Python attribute) — A repository of Set objects specifying the contents of the allSets repository is the same as the contents of the sets repository.") | A repository of Set objects specifying the contents of the **allSets** repository is the same as the contents of the **sets** repository. |
    | [`allInternalSets`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.allInternalSets "abaqus.Part.PartBase.PartBase.allInternalSets (Python attribute) — A repository of Set objects specifying picked regions.") | A repository of Set objects specifying picked regions. |
    | [`surfaces`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.surfaces "abaqus.Part.PartBase.PartBase.surfaces (Python attribute) — A repository of Surface objects specifying for more information, see Surface.") | A repository of Surface objects specifying for more information, see Surface. |
    | [`allSurfaces`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.allSurfaces "abaqus.Part.PartBase.PartBase.allSurfaces (Python attribute) — A repository of Surface objects specifying the contents of the allSurfaces repository is the same as the contents of the surfaces repository.") | A repository of Surface objects specifying the contents of the **allSurfaces** repository is the same as the contents of the **surfaces** repository. |
    | [`allInternalSurfaces`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.allInternalSurfaces "abaqus.Part.PartBase.PartBase.allInternalSurfaces (Python attribute) — A repository of Surface objects specifying picked regions.") | A repository of Surface objects specifying picked regions. |
    | [`skins`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.skins "abaqus.Part.PartBase.PartBase.skins (Python attribute) — A repository of Skin objects specifying the skins created on the part.") | A repository of Skin objects specifying the skins created on the part. |
    | [`stringers`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.stringers "abaqus.Part.PartBase.PartBase.stringers (Python attribute) — A repository of Stringer objects specifying the stringers created on the part.") | A repository of Stringer objects specifying the stringers created on the part. |
    | [`referencePoints`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.referencePoints "abaqus.Part.PartBase.PartBase.referencePoints (Python attribute) — A repository of ReferencePoint objects.") | A repository of ReferencePoint objects. |
    | [`engineeringFeatures`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.engineeringFeatures "abaqus.Part.PartBase.PartBase.engineeringFeatures (Python attribute) — An EngineeringFeature object.") | An EngineeringFeature object. |
    | [`sectionAssignments`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.sectionAssignments "abaqus.Part.PartBase.PartBase.sectionAssignments (Python attribute) — A SectionAssignmentArray object.") | A SectionAssignmentArray object. |
    | [`materialOrientations`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.materialOrientations "abaqus.Part.PartBase.PartBase.materialOrientations (Python attribute) — A MaterialOrientationArray object.") | A MaterialOrientationArray object. |
    | [`compositeLayups`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.compositeLayups "abaqus.Part.PartBase.PartBase.compositeLayups (Python attribute) — A repository of CompositeLayup objects.") | A repository of CompositeLayup objects. |
    | [`elemEdges`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.elemEdges "abaqus.Part.PartBase.PartBase.elemEdges (Python attribute) — A repository of MeshEdge objects specifying all the element edges in the part. For a given element and a given edge index on a given face within that element, the corresponding MeshEdge object can be retrieved from the repository by using the key calculated as (i*32 + j*4 + k), where i, j, and k are zero-based element, face, and edge indices, respectively.") | A repository of MeshEdge objects specifying all the element edges in the part. |
    | [`elementEdges`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.elementEdges "abaqus.Part.PartBase.PartBase.elementEdges (Python attribute) — A MeshEdgeArray object specifying all the unique element edges in the part.") | A MeshEdgeArray object specifying all the unique element edges in the part. |
    | `name` | A String specifying the repository key. |
    | `id` | An Int specifying the ID of the feature. |

    Inherited from [`Feature`](part_assembly/feature.html#abaqus.Feature.Feature.Feature "abaqus.Feature.Feature.Feature (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | [`name`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.name "abaqus.Feature.Feature.Feature.name (Python attribute) — A String specifying the repository key.") | A String specifying the repository key. |
    | [`id`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.id "abaqus.Feature.Feature.Feature.id (Python attribute) — An Int specifying the ID of the feature.") | An Int specifying the ID of the feature. |

    Public Methods:

    |  |  |
    | --- | --- |
    | [`CompositeLayup`](#abaqus.Property.PropertyPart.PropertyPart.CompositeLayup "abaqus.Property.PropertyPart.PropertyPart.CompositeLayup (Python method) — This method creates a CompositeLayup object.")(name[, description, ...]) | This method creates a CompositeLayup object. |
    | [`SectionAssignment`](#abaqus.Property.PropertyPart.PropertyPart.SectionAssignment "abaqus.Property.PropertyPart.PropertyPart.SectionAssignment (Python method) — This method creates a SectionAssignment object.")(region, sectionName[, ...]) | This method creates a SectionAssignment object. |
    | [`MaterialOrientation`](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation "abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation (Python method) — This method creates a MaterialOrientation object.")([region, localCsys, ...]) | This method creates a MaterialOrientation object. |
    | [`assignBeamSectionOrientation`](#abaqus.Property.PropertyPart.PropertyPart.assignBeamSectionOrientation "abaqus.Property.PropertyPart.PropertyPart.assignBeamSectionOrientation (Python method) — This method assigns a beam section orientation to a region of a part.")(region, method, n1) | This method assigns a beam section orientation to a region of a part. |
    | [`assignMaterialOrientation`](#abaqus.Property.PropertyPart.PropertyPart.assignMaterialOrientation "abaqus.Property.PropertyPart.PropertyPart.assignMaterialOrientation (Python method) — This method assigns a material orientation to a region.")(region, localCsys) | This method assigns a material orientation to a region. |
    | [`assignRebarOrientation`](#abaqus.Property.PropertyPart.PropertyPart.assignRebarOrientation "abaqus.Property.PropertyPart.PropertyPart.assignRebarOrientation (Python method) — This method assigns a rebar reference orientation to a region.")(region, localCsys[, ...]) | This method assigns a rebar reference orientation to a region. |
    | [`flipNormal`](#abaqus.Property.PropertyPart.PropertyPart.flipNormal "abaqus.Property.PropertyPart.PropertyPart.flipNormal (Python method) — This method flips the normals of shell or membrane elements of an orphan mesh or of two-dimensional geometric regions.")(regions[, referenceRegion]) | This method flips the normals of shell or membrane elements of an orphan mesh or of two-dimensional geometric regions. |
    | [`flipTangent`](#abaqus.Property.PropertyPart.PropertyPart.flipTangent "abaqus.Property.PropertyPart.PropertyPart.flipTangent (Python method) — This method flips the tangents of beam or truss elements of an orphan mesh or of one-dimensional geometric regions.")(regions) | This method flips the tangents of beam or truss elements of an orphan mesh or of one-dimensional geometric regions. |
    | [`unassignBeamSectionOrientation`](#abaqus.Property.PropertyPart.PropertyPart.unassignBeamSectionOrientation "abaqus.Property.PropertyPart.PropertyPart.unassignBeamSectionOrientation (Python method) — This method deletes a beam section orientation assignment.")(index) | This method deletes a beam section orientation assignment. |
    | [`unassignMaterialOrientation`](#abaqus.Property.PropertyPart.PropertyPart.unassignMaterialOrientation "abaqus.Property.PropertyPart.PropertyPart.unassignMaterialOrientation (Python method) — This method deletes a material orientation assignment.")(index) | This method deletes a material orientation assignment. |
    | [`unassignRebarOrientation`](#abaqus.Property.PropertyPart.PropertyPart.unassignRebarOrientation "abaqus.Property.PropertyPart.PropertyPart.unassignRebarOrientation (Python method) — This method deletes a rebar orientation assignment.")(index) | This method deletes a rebar orientation assignment. |

    Inherited from [`PartBase`](part_assembly/part.html#abaqus.Part.PartBase.PartBase "abaqus.Part.PartBase.PartBase (Python class) — Bases: PartFeature")

    |  |  |
    | --- | --- |
    | `__init__`() |  |
    | [`PartFromBooleanCut`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.PartFromBooleanCut "abaqus.Part.PartBase.PartBase.PartFromBooleanCut (Python method) — This method creates a Part in the parts repository after subtracting or cutting the geometries of a group of part instances from that of a base part instance.")(name, instanceToBeCut, ...) | This method creates a Part in the parts repository after subtracting or cutting the geometries of a group of part instances from that of a base part instance. |
    | [`PartFromBooleanMerge`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.PartFromBooleanMerge "abaqus.Part.PartBase.PartBase.PartFromBooleanMerge (Python method) — This method creates a Part in the parts repository after merging two or more part instances. The part instances can be either Abaqus native parts or orphan mesh parts, but they cannot be a combination of both.")(name, instances[, ...]) | This method creates a Part in the parts repository after merging two or more part instances. |
    | [`PartFromExtrude2DMesh`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.PartFromExtrude2DMesh "abaqus.Part.PartBase.PartBase.PartFromExtrude2DMesh (Python method) — This method creates a Part object by extruding an existing two-dimensional orphan mesh Part object in the positive Z direction and places it in the parts repository.")(name, part, depth, ...) | This method creates a Part object by extruding an existing two-dimensional orphan mesh Part object in the positive **Z** direction and places it in the parts repository. |
    | [`PartFromGeometryFile`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.PartFromGeometryFile "abaqus.Part.PartBase.PartBase.PartFromGeometryFile (Python method) — This method creates a Part object and places it in the parts repository.")(name, geometryFile, ...) | This method creates a Part object and places it in the parts repository. |
    | [`PartFromInstanceMesh`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.PartFromInstanceMesh "abaqus.Part.PartBase.PartBase.PartFromInstanceMesh (Python method) — This method creates a Part object containing the mesh found in the supplied PartInstance objects and places the new Part object in the parts repository.")(name[, partInstances, ...]) | This method creates a Part object containing the mesh found in the supplied PartInstance objects and places the new Part object in the parts repository. |
    | [`PartFromMesh`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.PartFromMesh "abaqus.Part.PartBase.PartBase.PartFromMesh (Python method) — This method creates a Part object containing the mesh found in the part and places the new Part object in the parts repository.")(name[, copySets]) | This method creates a Part object containing the mesh found in the part and places the new Part object in the parts repository. |
    | [`PartFromMeshMirror`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.PartFromMeshMirror "abaqus.Part.PartBase.PartBase.PartFromMeshMirror (Python method) — This method creates a Part object by mirroring an existing orphan mesh Part object about a specified plane and places it in the parts repository. The result is a union of the original and the mirrored copy. Contrast the PartFromMeshMirror method with the mirrorPlane argument of the Part copy constructor. The mirrorPlane argument creates only the second half of the part but does not unite the two halves.")(name, part, point1, point2) | This method creates a Part object by mirroring an existing orphan mesh Part object about a specified plane and places it in the parts repository. |
    | [`PartFromNodesAndElements`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.PartFromNodesAndElements "abaqus.Part.PartBase.PartBase.PartFromNodesAndElements (Python method) — This method creates a Part object from nodes and elements and places it in the parts repository.")(name, ...[, twist]) | This method creates a Part object from nodes and elements and places it in the parts repository. |
    | [`PartFromOdb`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.PartFromOdb "abaqus.Part.PartBase.PartBase.PartFromOdb (Python method) — This method creates an orphan mesh Part object by reading an output database. The new part is placed in the parts repository.")(name, odb[, fileName, instance, ...]) | This method creates an orphan mesh Part object by reading an output database. |
    | [`PartFromSection3DMeshByPlane`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane "abaqus.Part.PartBase.PartBase.PartFromSection3DMeshByPlane (Python method) — This method creates a Part object by cutting an existing three-dimensional orphan mesh Part object by a plane and places it in the parts repository. This method is valid only for orphan mesh parts composed of 8-node brick elements.")(name, part, ...) | This method creates a Part object by cutting an existing three-dimensional orphan mesh Part object by a plane and places it in the parts repository. |
    | [`PartFromSubstructure`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.PartFromSubstructure "abaqus.Part.PartBase.PartBase.PartFromSubstructure (Python method) — This method creates a substructure Part object by reading a substructure sim file and places it in the parts repository.")(name, substructureFile, ...) | This method creates a substructure Part object by reading a substructure sim file and places it in the parts repository. |
    | [`Part2DGeomFrom2DMesh`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.Part2DGeomFrom2DMesh "abaqus.Part.PartBase.PartBase.Part2DGeomFrom2DMesh (Python method) — This method creates a geometric Part object from the outline of an existing two-dimensional orphan mesh Part object and places it in the parts repository. If the Part2DGeomFrom2DMesh method cannot create a valid two-dimensional shell section from the two-dimensional mesh, the method fails and creates an empty geometry part with a failed base shell feature.")(name, part, featureAngle) | This method creates a geometric Part object from the outline of an existing two-dimensional orphan mesh Part object and places it in the parts repository. |
    | [`setValues`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.setValues "abaqus.Part.PartBase.PartBase.setValues (Python method) — This method modifies the Part object.")(\*args, \*\*kwargs) | This method modifies the Part object. |
    | [`addGeomToSketch`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.addGeomToSketch "abaqus.Part.PartBase.PartBase.addGeomToSketch (Python method) — This method converts a part into a sketch by projecting all of the edges of the part onto the X-Y plane of the sketch. You can use addGeomToSketch with a part of any modeling space.")(sketch) | This method converts a part into a sketch by projecting all of the edges of the part onto the X-Y plane of the sketch. |
    | [`assignThickness`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.assignThickness "abaqus.Part.PartBase.PartBase.assignThickness (Python method) — This method assigns thickness data to shell faces. The thickness can be used while assigning shell and membrane sections to faces.")(faces[, thickness, ...]) | This method assigns thickness data to shell faces. |
    | [`backup`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.backup "abaqus.Part.PartBase.PartBase.backup (Python method) — This method makes a backup copy of the features in the part.")() | This method makes a backup copy of the features in the part. |
    | [`checkGeometry`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.checkGeometry "abaqus.Part.PartBase.PartBase.checkGeometry (Python method) — This method checks the validity of the geometry of the part and prints a count of all topological entities on the part (faces, edges, vertices, etc.).")([detailed, reportFacetErrors, ...]) | This method checks the validity of the geometry of the part and prints a count of all topological entities on the part (faces, edges, vertices, etc.). |
    | [`clearGeometryCache`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.clearGeometryCache "abaqus.Part.PartBase.PartBase.clearGeometryCache (Python method) — This method clears the geometry cache.")() | This method clears the geometry cache. |
    | [`deleteAllFeatures`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.deleteAllFeatures "abaqus.Part.PartBase.PartBase.deleteAllFeatures (Python method) — This method deletes all the features in the part.")() | This method deletes all the features in the part. |
    | [`deleteFeatures`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.deleteFeatures "abaqus.Part.PartBase.PartBase.deleteFeatures (Python method) — This method deletes the given features.")(featureNames) | This method deletes the given features. |
    | [`getAngle`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.getAngle "abaqus.Part.PartBase.PartBase.getAngle (Python method) — This method returns the angle between the specified entities.")(plane1, plane2, line1, line2[, ...]) | This method returns the angle between the specified entities. |
    | [`getArea`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.getArea "abaqus.Part.PartBase.PartBase.getArea (Python method) — This method returns the total surface area of a given face or group of faces.")(faces[, relativeAccuracy]) | This method returns the total surface area of a given face or group of faces. |
    | [`getAssociatedCADPaths`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.getAssociatedCADPaths "abaqus.Part.PartBase.PartBase.getAssociatedCADPaths (Python method) — This method returns the paths to the associated CAD part and root file. These are only available if the part was imported from one of the supported CAD softwares using the Associative Import capability. The root file can be the assembly file or the part file, depending on what which one was imported.")() | This method returns the paths to the associated CAD part and root file. |
    | [`getCADParameters`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.getCADParameters "abaqus.Part.PartBase.PartBase.getCADParameters (Python method) — This method returns the names and values of the CAD parameters associated with the part. These are only available if the part was imported from one of the supported CAD softwares using the Associative Import capability, and if the parameter names defined in that CAD software are prefixed with the string ABQ.")() | This method returns the names and values of the CAD parameters associated with the part. |
    | [`getCentroid`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.getCentroid "abaqus.Part.PartBase.PartBase.getCentroid (Python method) — Location of the centroid of a given face/cell or group of faces/cells.")(faces, cells[, relativeAccuracy]) | Location of the centroid of a given face/cell or group of faces/cells. |
    | [`getCoordinates`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.getCoordinates "abaqus.Part.PartBase.PartBase.getCoordinates (Python method) — This method returns the coordinates of specified point.")(entity, csys) | This method returns the coordinates of specified point. |
    | [`getCurvature`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.getCurvature "abaqus.Part.PartBase.PartBase.getCurvature (Python method) — This method returns the maximum curvature of a given edge or group of edges. For an arc, the curvature is constant over the entire edge, and equal to the inverse of the radius. For a straight line, the curvature is constant and equal to 0. For a spline edge, the curvature varies over a range, and this methods computes the maximum.")(edges[, samplePoints]) | This method returns the maximum curvature of a given edge or group of edges. |
    | [`getDistance`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.getDistance "abaqus.Part.PartBase.PartBase.getDistance (Python method) — Depending on the arguments provided, this method returns one of the following:")(entity1, entity2) | Depending on the arguments provided, this method returns one of the following: |
    | [`getLength`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.getLength "abaqus.Part.PartBase.PartBase.getLength (Python method) — This method returns the length of a given edge or group of edges.")(edges) | This method returns the length of a given edge or group of edges. |
    | [`getPerimeter`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.getPerimeter "abaqus.Part.PartBase.PartBase.getPerimeter (Python method) — This method returns the total perimeter of a given face or group of faces. All faces need to be on the same part. If the specified faces have shared edges, these edges are excluded from the computation, thus providing the length of the outer perimeter of the specified faces.")(faces) | This method returns the total perimeter of a given face or group of faces. |
    | [`getVolume`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.getVolume "abaqus.Part.PartBase.PartBase.getVolume (Python method) — This method returns the volume area of a given cell or group of cells.")(cells[, relativeAccuracy]) | This method returns the volume area of a given cell or group of cells. |
    | [`getMassProperties`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.getMassProperties "abaqus.Part.PartBase.PartBase.getMassProperties (Python method) — This method returns the mass properties of a part or region. Only beams, trusses, shells, solids, point, nonstructural mass, and rotary inertia elements are supported.")([regions, ...]) | This method returns the mass properties of a part or region. |
    | [`getFeatureFaces`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.getFeatureFaces "abaqus.Part.PartBase.PartBase.getFeatureFaces (Python method) — This method returns a sequence of Face objects that are created by the given feature.")(name) | This method returns a sequence of Face objects that are created by the given feature. |
    | [`getFeatureEdges`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.getFeatureEdges "abaqus.Part.PartBase.PartBase.getFeatureEdges (Python method) — This method returns a sequence of Edge objects that are created by the given feature.")(name) | This method returns a sequence of Edge objects that are created by the given feature. |
    | [`getFeatureCells`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.getFeatureCells "abaqus.Part.PartBase.PartBase.getFeatureCells (Python method) — This method returns a sequence of Cell objects that are created by the given feature.")(name) | This method returns a sequence of Cell objects that are created by the given feature. |
    | [`getFeatureVertices`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.getFeatureVertices "abaqus.Part.PartBase.PartBase.getFeatureVertices (Python method) — This method returns a sequence of ConstrainedSketchVertex objects that are created by the given feature.")(name) | This method returns a sequence of ConstrainedSketchVertex objects that are created by the given feature. |
    | [`isAlignedWithSketch`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.isAlignedWithSketch "abaqus.Part.PartBase.PartBase.isAlignedWithSketch (Python method) — This method checks if the normal of an analytical rigid surface part is aligned with that of its sketch.")() | This method checks if the normal of an analytical rigid surface part is aligned with that of its sketch. |
    | [`printAssignedSections`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.printAssignedSections "abaqus.Part.PartBase.PartBase.printAssignedSections (Python method) — This method prints information on each section that has been assigned to a region of the part.")() | This method prints information on each section that has been assigned to a region of the part. |
    | [`projectEdgesOntoSketch`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.projectEdgesOntoSketch "abaqus.Part.PartBase.PartBase.projectEdgesOntoSketch (Python method) — This method projects the selected edges of a part onto the specified ConstrainedSketch object. The edges appear as sketch geometry after projection. If the plane of projection is not parallel to the specified edge, the resultant sketch geometry may be of a different type. For example, a circular edge can be projected as an ellipse or a line depending on the angle of the plane of projection. By default, the projected edge will be constrained to the background geometry. You can remove this constraint by setting constrainToBackground to False.")(sketch, edges[, ...]) | This method projects the selected edges of a part onto the specified ConstrainedSketch object. |
    | [`projectReferencesOntoSketch`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.projectReferencesOntoSketch "abaqus.Part.PartBase.PartBase.projectReferencesOntoSketch (Python method) — This method projects the vertices of specified edges, and datum points from the part onto the specified ConstrainedSketch object. The vertices and datum points appear on the sketch as reference geometry.")(sketch[, ...]) | This method projects the vertices of specified edges, and datum points from the part onto the specified ConstrainedSketch object. |
    | [`queryAttributes`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.queryAttributes "abaqus.Part.PartBase.PartBase.queryAttributes (Python method) — This method prints the following information about a part:")([printResults]) | This method prints the following information about a part: |
    | [`queryCachedStates`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.queryCachedStates "abaqus.Part.PartBase.PartBase.queryCachedStates (Python method) — This method displays the position of geometric states relative to the sequence of features in the part cache.")() | This method displays the position of geometric states relative to the sequence of features in the part cache. |
    | [`queryGeometry`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.queryGeometry "abaqus.Part.PartBase.PartBase.queryGeometry (Python method) — This method prints the following information about a part:")([relativeAccuracy, printResults]) | This method prints the following information about a part: |
    | [`queryRegionsMissingSections`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.queryRegionsMissingSections "abaqus.Part.PartBase.PartBase.queryRegionsMissingSections (Python method) — This method returns all regions in the part that do not have a section assignment but require one for analysis.")() | This method returns all regions in the part that do not have a section assignment but require one for analysis. |
    | [`queryDisjointPlyRegions`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.queryDisjointPlyRegions "abaqus.Part.PartBase.PartBase.queryDisjointPlyRegions (Python method) — This method provides a list of all composite plys in the current part which have disjoint regions.")() | This method provides a list of all composite plys in the current part which have disjoint regions. |
    | [`regenerate`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.regenerate "abaqus.Part.PartBase.PartBase.regenerate (Python method) — This method regenerates a part.")() | This method regenerates a part. |
    | [`regenerationWarnings`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.regenerationWarnings "abaqus.Part.PartBase.PartBase.regenerationWarnings (Python method) — This method prints any regeneration warnings associated with the features.")() | This method prints any regeneration warnings associated with the features. |
    | [`removeInvalidGeometry`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.removeInvalidGeometry "abaqus.Part.PartBase.PartBase.removeInvalidGeometry (Python method) — Removes all invalid entities from the part, leaving a valid part.")() | Removes all invalid entities from the part, leaving a valid part. |
    | [`restore`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.restore "abaqus.Part.PartBase.PartBase.restore (Python method) — This method restores the parameters of all features in the assembly to the value they had before a failed regeneration.")() | This method restores the parameters of all features in the assembly to the value they had before a failed regeneration. |
    | [`resumeAllFeatures`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.resumeAllFeatures "abaqus.Part.PartBase.PartBase.resumeAllFeatures (Python method) — This method resumes all the suppressed features in the part.")() | This method resumes all the suppressed features in the part. |
    | [`resumeFeatures`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.resumeFeatures "abaqus.Part.PartBase.PartBase.resumeFeatures (Python method) — This method resumes the specified suppressed features in the part.")(featureNames) | This method resumes the specified suppressed features in the part. |
    | [`resumeLastSetFeatures`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.resumeLastSetFeatures "abaqus.Part.PartBase.PartBase.resumeLastSetFeatures (Python method) — This method resumes the last set of features to be suppressed in the part.")() | This method resumes the last set of features to be suppressed in the part. |
    | [`saveGeometryCache`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.saveGeometryCache "abaqus.Part.PartBase.PartBase.saveGeometryCache (Python method) — This method caches the current geometry.")() | This method caches the current geometry. |
    | [`setAssociatedCADPaths`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.setAssociatedCADPaths "abaqus.Part.PartBase.PartBase.setAssociatedCADPaths (Python method) — This method sets the paths to the associated CAD part and root file. This method is only available if the part was imported from one of the supported CAD softwares using the Associative Import capability. The root file can be the assembly file or the part file, depending on the one that was imported. This method can be used to specify the new paths when the CAD data is moved to a different directory.")([partFile, rootFile]) | This method sets the paths to the associated CAD part and root file. |
    | [`suppressFeatures`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.suppressFeatures "abaqus.Part.PartBase.PartBase.suppressFeatures (Python method) — This method suppresses the given features.")(featureNames) | This method suppresses the given features. |
    | [`writeAcisFile`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.writeAcisFile "abaqus.Part.PartBase.PartBase.writeAcisFile (Python method) — This method exports the geometry of the part to a named file in ACIS format.")(fileName[, version]) | This method exports the geometry of the part to a named file in ACIS format. |
    | [`writeCADParameters`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.writeCADParameters "abaqus.Part.PartBase.PartBase.writeCADParameters (Python method) — This method writes the parameters that were imported from the CAD system to a parameter file.")(paramFile[, ...]) | This method writes the parameters that were imported from the CAD system to a parameter file. |
    | [`writeIgesFile`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.writeIgesFile "abaqus.Part.PartBase.PartBase.writeIgesFile (Python method) — This method exports the geometry of the part to a named file in IGES format.")(fileName, flavor) | This method exports the geometry of the part to a named file in IGES format. |
    | [`writeStepFile`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.writeStepFile "abaqus.Part.PartBase.PartBase.writeStepFile (Python method) — This method exports the geometry of the part to a named file in STEP format.")(fileName) | This method exports the geometry of the part to a named file in STEP format. |
    | [`writeVdaFile`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.writeVdaFile "abaqus.Part.PartBase.PartBase.writeVdaFile (Python method) — This method exports the geometry of the part to a named file in VDA-FS format.")(fileName) | This method exports the geometry of the part to a named file in VDA-FS format. |
    | [`copyMeshPattern`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.copyMeshPattern "abaqus.Part.PartBase.PartBase.copyMeshPattern (Python method) — This method copies a mesh pattern from a source region consisting of a set of shell elements or element faces onto a target face, mapping nodes and elements in a one-one correspondence between source and target.")(elements, faces, elemFaces, ...) | This method copies a mesh pattern from a source region consisting of a set of shell elements or element faces onto a target face, mapping nodes and elements in a one-one correspondence between source and target. |
    | [`smoothNodes`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.smoothNodes "abaqus.Part.PartBase.PartBase.smoothNodes (Python method) — This method smooths the given nodes of a native mesh, moving them locally to a more optimal location that improves the quality of the mesh.")(nodes) | This method smooths the given nodes of a native mesh, moving them locally to a more optimal location that improves the quality of the mesh. |
    | [`Lock`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.Lock "abaqus.Part.PartBase.PartBase.Lock (Python method) — This method locks the part.")() | This method locks the part. |
    | [`Unlock`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.Unlock "abaqus.Part.PartBase.PartBase.Unlock (Python method) — This method unlocks the part.")() | This method unlocks the part. |
    | [`LockForUpgrade`](part_assembly/part.html#abaqus.Part.PartBase.PartBase.LockForUpgrade "abaqus.Part.PartBase.PartBase.LockForUpgrade (Python method) — This method locks the part for upgrade.")() | This method locks the part for upgrade. |

    Inherited from [`PartFeature`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature "abaqus.Part.PartFeature.PartFeature (Python class) — Bases: Feature")

    |  |  |
    | --- | --- |
    | [`AutoRepair`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.AutoRepair "abaqus.Part.PartFeature.PartFeature.AutoRepair (Python method) — This method carries out a sequence of geometry repair operations if it contains invalid entities. It is expected to improve the geometry, but it does not guarantee that the number of invalid entities will decrease. In some cases, it can also increase the number of invalid entities. Since a number of geometry repair operations and validity checks are performed, it could be a slow operation depending on the complexity of the geometry.")() | This method carries out a sequence of geometry repair operations if it contains invalid entities. |
    | [`AddCells`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.AddCells "abaqus.Part.PartFeature.PartFeature.AddCells (Python method) — This method tries to convert a shell entity to a solid entity. The conversion is not always successful.")(faceList[, flipped]) | This method tries to convert a shell entity to a solid entity. |
    | [`AnalyticRigidSurf2DPlanar`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurf2DPlanar "abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurf2DPlanar (Python method) — This method creates a first Feature object for an analytical rigid surface by creating a planar wire from the given ConstrainedSketch object.")(sketch) | This method creates a first Feature object for an analytical rigid surface by creating a planar wire from the given ConstrainedSketch object. |
    | [`AnalyticRigidSurfExtrude`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfExtrude "abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfExtrude (Python method) — This method creates a first Feature object for an analytical rigid surface by extruding the given ConstrainedSketch object by the given depth, creating a surface.")(sketch[, depth]) | This method creates a first Feature object for an analytical rigid surface by extruding the given ConstrainedSketch object by the given depth, creating a surface. |
    | [`AnalyticRigidSurfRevolve`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfRevolve "abaqus.Part.PartFeature.PartFeature.AnalyticRigidSurfRevolve (Python method) — This method creates a first Feature object for an analytical rigid surface by revolving the given ConstrainedSketch object by 360° about the Y axis.")(sketch) | This method creates a first Feature object for an analytical rigid surface by revolving the given ConstrainedSketch object by 360° about the **Y** axis. |
    | [`AssignMidsurfaceRegion`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.AssignMidsurfaceRegion "abaqus.Part.PartFeature.PartFeature.AssignMidsurfaceRegion (Python method) — This method assign a mid-surface property to sequence of Cell objects. If a reference representation of the part does not exist, it creates one. It also copies the cells to the reference representation and deletes the cells from the active representation of the part.")(cellList) | This method assign a mid-surface property to sequence of Cell objects. |
    | [`BaseSolidExtrude`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.BaseSolidExtrude "abaqus.Part.PartFeature.PartFeature.BaseSolidExtrude (Python method) — This method creates a first Feature object by extruding the given ConstrainedSketch object by the given depth, creating a solid. The ConstrainedSketch object must define a closed profile.")(sketch, depth[, ...]) | This method creates a first Feature object by extruding the given ConstrainedSketch object by the given depth, creating a solid. |
    | [`BaseSolidRevolve`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve "abaqus.Part.PartFeature.PartFeature.BaseSolidRevolve (Python method) — This method creates a first Feature object by revolving the given ConstrainedSketch object by the given angle, creating a solid. The ConstrainedSketch object must define a closed profile and an axis of revolution. The axis is defined by a single construction line.")(sketch, angle[, pitch, ...]) | This method creates a first Feature object by revolving the given ConstrainedSketch object by the given angle, creating a solid. |
    | [`BaseSolidSweep`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.BaseSolidSweep "abaqus.Part.PartFeature.PartFeature.BaseSolidSweep (Python method) — This method creates a first Feature object by sweeping the given profile ConstrainedSketch object along the path defined by the path ConstrainedSketch object, creating a solid. The profile ConstrainedSketch object must define a closed profile. The origin of the profile sketch is positioned at the start of the sweep path and swept perpendicular to the path. No checks are made for self- intersection.")(sketch, path) | This method creates a first Feature object by sweeping the given profile ConstrainedSketch object along the path defined by the path ConstrainedSketch object, creating a solid. |
    | [`BaseShell`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.BaseShell "abaqus.Part.PartFeature.PartFeature.BaseShell (Python method) — This method creates a first Feature object by creating a planar shell from the given ConstrainedSketch object. The ConstrainedSketch object must define a closed profile.")(sketch) | This method creates a first Feature object by creating a planar shell from the given ConstrainedSketch object. |
    | [`BaseShellExtrude`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.BaseShellExtrude "abaqus.Part.PartFeature.PartFeature.BaseShellExtrude (Python method) — This method creates a first Feature object by extruding the given ConstrainedSketch object by the given depth, creating a shell. The ConstrainedSketch object can define either an open or closed profile.")(sketch, depth[, ...]) | This method creates a first Feature object by extruding the given ConstrainedSketch object by the given depth, creating a shell. |
    | [`BaseShellRevolve`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.BaseShellRevolve "abaqus.Part.PartFeature.PartFeature.BaseShellRevolve (Python method) — This method creates a first Feature object by revolving the given ConstrainedSketch object by the given angle, creating a shell. The ConstrainedSketch object can define either an open or closed profile and an axis of revolution. The axis is defined by a single construction line.")(sketch, angle[, pitch, ...]) | This method creates a first Feature object by revolving the given ConstrainedSketch object by the given angle, creating a shell. |
    | [`BaseShellSweep`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.BaseShellSweep "abaqus.Part.PartFeature.PartFeature.BaseShellSweep (Python method) — This method creates a first Feature object by sweeping the given section ConstrainedSketch object along the path defined by the path ConstrainedSketch object, creating a shell. The ConstrainedSketch object can define either an open or closed profile. The origin of the profile sketch is positioned at the start of the sweep path and swept perpendicular to the path. No checks are made for self- intersection.")(sketch, path) | This method creates a first Feature object by sweeping the given section ConstrainedSketch object along the path defined by the path ConstrainedSketch object, creating a shell. |
    | [`BaseWire`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.BaseWire "abaqus.Part.PartFeature.PartFeature.BaseWire (Python method) — This method creates a first Feature object by creating a planar wire from the given ConstrainedSketch object.")(sketch) | This method creates a first Feature object by creating a planar wire from the given ConstrainedSketch object. |
    | [`BlendFaces`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.BlendFaces "abaqus.Part.PartFeature.PartFeature.BlendFaces (Python method) — This method creates a Feature object by creating new faces that blends two sets of faces.")(side1, side2[, method, path]) | This method creates a Feature object by creating new faces that blends two sets of faces. |
    | [`Chamfer`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.Chamfer "abaqus.Part.PartFeature.PartFeature.Chamfer (Python method) — This method creates an additional Feature object by chamfering the given list of edges with a given length.")(length, edgeList) | This method creates an additional Feature object by chamfering the given list of edges with a given length. |
    | [`Mirror`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.Mirror "abaqus.Part.PartFeature.PartFeature.Mirror (Python method) — This method mirrors existing part geometry across a plane to create new geometry.")(mirrorPlane, keepOriginal[, ...]) | This method mirrors existing part geometry across a plane to create new geometry. |
    | [`ConvertToAnalytical`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.ConvertToAnalytical "abaqus.Part.PartFeature.PartFeature.ConvertToAnalytical (Python method) — This method attempts to change entities into a simpler form that will speed up processing and make entities available during feature operations.")() | This method attempts to change entities into a simpler form that will speed up processing and make entities available during feature operations. |
    | [`ConvertToPrecise`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.ConvertToPrecise "abaqus.Part.PartFeature.PartFeature.ConvertToPrecise (Python method) — This method attempts to change imprecise entities so that the geometry becomes precise.")([method]) | This method attempts to change imprecise entities so that the geometry becomes precise. |
    | [`CoverEdges`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.CoverEdges "abaqus.Part.PartFeature.PartFeature.CoverEdges (Python method) — This method generates a face using the given edges as the face's boundaries. The CoverEdges method generates a face by creating the geometry consisting of the underlying surface, associated edges, and vertices.")(edgeList[, tryAnalytical]) | This method generates a face using the given edges as the face's boundaries. |
    | [`Cut`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.Cut "abaqus.Part.PartFeature.PartFeature.Cut (Python method) — This method creates an additional Feature object by cutting a hole using the given ConstrainedSketch object.")(sketchPlane, sketchPlaneSide, ...[, ...]) | This method creates an additional Feature object by cutting a hole using the given ConstrainedSketch object. |
    | [`CutExtrude`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.CutExtrude "abaqus.Part.PartFeature.PartFeature.CutExtrude (Python method) — This method creates an additional Feature object by extruding the given ConstrainedSketch object by the given depth and cutting away material in the solid and shell regions of the part. The ConstrainedSketch object must define a closed profile. The CutExtrude method creates a blind cut (using depth), an up-to-face cut (using upToFace), or a through-all cut (if depth and upToFace are not specified).")(sketchPlane, sketchPlaneSide, ...) | This method creates an additional Feature object by extruding the given ConstrainedSketch object by the given depth and cutting away material in the solid and shell regions of the part. |
    | [`CutLoft`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.CutLoft "abaqus.Part.PartFeature.PartFeature.CutLoft (Python method) — This method creates an additional Feature object by lofting between the given sections and cutting away material from the part. You define the sections using a sequence of edges from the part or an EdgeArray.")(loftsections[, startCondition, ...]) | This method creates an additional Feature object by lofting between the given sections and cutting away material from the part. |
    | [`CutRevolve`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.CutRevolve "abaqus.Part.PartFeature.PartFeature.CutRevolve (Python method) — This method creates an additional Feature object by revolving the given ConstrainedSketch object by the given angle and cutting away material from the part. The ConstrainedSketch object must define a closed profile and an axis of revolution.")(sketchPlane, sketchPlaneSide, ...) | This method creates an additional Feature object by revolving the given ConstrainedSketch object by the given angle and cutting away material from the part. |
    | [`CutSweep`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.CutSweep "abaqus.Part.PartFeature.PartFeature.CutSweep (Python method) — This method creates an additional Feature object by sweeping the given ConstrainedSketch object along a path which may be a ConstrainedSketch or a sequence of Edge objects and cutting away material from the part. If the profile section is a ConstrainedSketch object, it must define a closed profile. The section sketch can be created at the normal plane at the start of the sweep path or it may be created on a Datum plane or a planar Face. No checks are made for self-intersection.")(path, profile[, pathPlane, ...]) | This method creates an additional Feature object by sweeping the given ConstrainedSketch object along a path which may be a ConstrainedSketch or a sequence of Edge objects and cutting away material from the part. |
    | [`ExtendFaces`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.ExtendFaces "abaqus.Part.PartFeature.PartFeature.ExtendFaces (Python method) — This method extends faces along its free edges by offsetting the external edges along the surfaces. One of distance, upToReferenceRep, or upToFaces must be used to specify how far the faces need to be extended.")([faces, extendAlong, distance, ...]) | This method extends faces along its free edges by offsetting the external edges along the surfaces. |
    | [`FaceFromElementFaces`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.FaceFromElementFaces "abaqus.Part.PartFeature.PartFeature.FaceFromElementFaces (Python method) — This method creates a geometry face from a collection of orphan element faces.")(elementFaces[, stitch, ...]) | This method creates a geometry face from a collection of orphan element faces. |
    | [`HoleBlindFromEdges`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges "abaqus.Part.PartFeature.PartFeature.HoleBlindFromEdges (Python method) — This method creates an additional Feature object by creating a circular blind hole of the given diameter and depth and cutting away material in the solid and shell regions of the part. The center of the hole is offset from two non-parallel straight edges by the given distances.")(plane, planeSide, ...) | This method creates an additional Feature object by creating a circular blind hole of the given diameter and depth and cutting away material in the solid and shell regions of the part. |
    | [`HoleFromEdges`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.HoleFromEdges "abaqus.Part.PartFeature.PartFeature.HoleFromEdges (Python method) — This method creates an additional Feature object by creating a circular hole of the given diameter in a 2D planar part and cutting away material in the shell and wire regions of the part. The center of the hole is offset from two non-parallel straight edges by the given distances.")(diameter, edge1, distance1, ...) | This method creates an additional Feature object by creating a circular hole of the given diameter in a 2D planar part and cutting away material in the shell and wire regions of the part. |
    | [`HoleThruAllFromEdges`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges "abaqus.Part.PartFeature.PartFeature.HoleThruAllFromEdges (Python method) — This method creates an additional Feature object by creating a circular through hole of the given diameter and cutting away material in the solid and shell regions of the part. The center of the hole is offset from two non-parallel straight edges by the given distances.")(plane, planeSide, ...) | This method creates an additional Feature object by creating a circular through hole of the given diameter and cutting away material in the solid and shell regions of the part. |
    | [`MergeEdges`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.MergeEdges "abaqus.Part.PartFeature.PartFeature.MergeEdges (Python method) — This method merges edges either by extending the user selection or using only the selected edges.")([edgeList, extendSelection]) | This method merges edges either by extending the user selection or using only the selected edges. |
    | [`OffsetFaces`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.OffsetFaces "abaqus.Part.PartFeature.PartFeature.OffsetFaces (Python method) — This method creates new faces by offsetting existing faces.")(faceList[, distance, ...]) | This method creates new faces by offsetting existing faces. |
    | [`RemoveCells`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.RemoveCells "abaqus.Part.PartFeature.PartFeature.RemoveCells (Python method) — This method converts a solid entity to a shell entity.")(cellList) | This method converts a solid entity to a shell entity. |
    | [`RemoveFaces`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.RemoveFaces "abaqus.Part.PartFeature.PartFeature.RemoveFaces (Python method) — This method removes faces from a solid entity or from a shell entity.")(faceList[, deleteCells]) | This method removes faces from a solid entity or from a shell entity. |
    | [`RemoveFacesAndStitch`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.RemoveFacesAndStitch "abaqus.Part.PartFeature.PartFeature.RemoveFacesAndStitch (Python method) — This method removes faces from a solid entity and attempts to close the resulting gap by extending the neighboring faces of the solid.")(faceList) | This method removes faces from a solid entity and attempts to close the resulting gap by extending the neighboring faces of the solid. |
    | [`RemoveRedundantEntities`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.RemoveRedundantEntities "abaqus.Part.PartFeature.PartFeature.RemoveRedundantEntities (Python method) — This method removes redundant edges and vertices from a solid or a shell entity. One of the two arguments is required.")([vertexList, ...]) | This method removes redundant edges and vertices from a solid or a shell entity. |
    | [`RepairFaceNormals`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.RepairFaceNormals "abaqus.Part.PartFeature.PartFeature.RepairFaceNormals (Python method) — This method works on the entire part or a sequence of shell faces. When the entire part is selected, it aligns all the shell face normals, and inverts all of the solid faces' normals if the solid was originally inside out. When a few shell faces are selected, it inverts the normals of the selected faces.")([faceList]) | This method works on the entire part or a sequence of shell faces. |
    | [`RepairInvalidEdges`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.RepairInvalidEdges "abaqus.Part.PartFeature.PartFeature.RepairInvalidEdges (Python method) — This method repairs invalid edges. It will always attempt to improve edges even if none of selected edges are initially invalid and may leave behind invalid edges that could not be repaired.")(edgeList) | This method repairs invalid edges. |
    | [`RepairSliver`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.RepairSliver "abaqus.Part.PartFeature.PartFeature.RepairSliver (Python method) — This method repairs the selected sliver from the selected face. The sliver area is specified using two points. A face partition is carried out at the specified points and the smaller of the two faces is removed.")(face, point1, point2[, ...]) | This method repairs the selected sliver from the selected face. |
    | [`RepairSmallEdges`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.RepairSmallEdges "abaqus.Part.PartFeature.PartFeature.RepairSmallEdges (Python method) — This method repairs small edges. This method will attempt to replace selected small edges with vertices and extend the adjacent faces and edges. This method might leave behind some small edges that cannot be removed.")(edgeList[, toleranceChecks]) | This method repairs small edges. |
    | [`RepairSmallFaces`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.RepairSmallFaces "abaqus.Part.PartFeature.PartFeature.RepairSmallFaces (Python method) — This method repairs small faces. It will attempt to replace the selected small faces with edges or vertices and extend the adjacent faces. This method might leave behind some small faces that cannot be removed.")(faceList[, toleranceChecks]) | This method repairs small faces. |
    | [`ReplaceFaces`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.ReplaceFaces "abaqus.Part.PartFeature.PartFeature.ReplaceFaces (Python method) — This method replaces the selected faces with a single face. If one single face is selected, that alone is replaced with a new face.")(faceList[, stitch]) | This method replaces the selected faces with a single face. |
    | [`Round`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.Round "abaqus.Part.PartFeature.PartFeature.Round (Python method) — This method creates an additional Feature object by rounding (filleting) the given list of entities with the given radius.")(radius[, edgeList, vertexList]) | This method creates an additional Feature object by rounding (filleting) the given list of entities with the given radius. |
    | [`Shell`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.Shell "abaqus.Part.PartFeature.PartFeature.Shell (Python method) — This method creates an additional Feature object by creating a planar shell from the given ConstrainedSketch object. The ConstrainedSketch object must define a closed profile.")(sketchPlane, sketchPlaneSide, ...[, ...]) | This method creates an additional Feature object by creating a planar shell from the given ConstrainedSketch object. |
    | [`ShellExtrude`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.ShellExtrude "abaqus.Part.PartFeature.PartFeature.ShellExtrude (Python method) — This method creates an additional Feature object by extruding the given ConstrainedSketch object by the given depth, creating a shell protrusion. The ConstrainedSketch object can define either an open or closed profile.")(sketchPlane, sketchPlaneSide, ...) | This method creates an additional Feature object by extruding the given ConstrainedSketch object by the given depth, creating a shell protrusion. |
    | [`ShellLoft`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.ShellLoft "abaqus.Part.PartFeature.PartFeature.ShellLoft (Python method) — This method creates an additional Feature object by lofting between the given sections and adding shell faces to the part. You define the sections using a sequence of edges from the part or an EdgeArray.")(loftsections[, startCondition, ...]) | This method creates an additional Feature object by lofting between the given sections and adding shell faces to the part. |
    | [`ShellRevolve`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.ShellRevolve "abaqus.Part.PartFeature.PartFeature.ShellRevolve (Python method) — This method creates an additional Feature object by revolving the given ConstrainedSketch object by the given angle, creating a shell protrusion. The ConstrainedSketch object can define either an open or closed profile and an axis of revolution. The axis is defined by a single construction line. For a description of the plane positioning arguments, see SolidExtrude.")(sketchPlane, sketchPlaneSide, ...) | This method creates an additional Feature object by revolving the given ConstrainedSketch object by the given angle, creating a shell protrusion. |
    | [`ShellSweep`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.ShellSweep "abaqus.Part.PartFeature.PartFeature.ShellSweep (Python method) — This method creates an additional Feature object by sweeping the given ConstrainedSketch object or a sequence of Edge objects along a path which may be a ConstrainedSketch or a sequence of Edge objects, creating a shell swept protrusion. The section can be an open or a closed profile. The section sketch can be created at the normal plane at the start of the sweep path or it may be created on a Datum plane or a planar Face. No checks are made for self-intersection.")(path, profile[, pathPlane, ...]) | This method creates an additional Feature object by sweeping the given ConstrainedSketch object or a sequence of Edge objects along a path which may be a ConstrainedSketch or a sequence of Edge objects, creating a shell swept protrusion. |
    | [`SolidExtrude`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.SolidExtrude "abaqus.Part.PartFeature.PartFeature.SolidExtrude (Python method) — This method creates an additional Feature object by extruding the given ConstrainedSketch object by the given depth, creating a solid protrusion. The ConstrainedSketch object must define a closed profile.")(sketchPlane, sketchPlaneSide, ...) | This method creates an additional Feature object by extruding the given ConstrainedSketch object by the given depth, creating a solid protrusion. |
    | [`SolidLoft`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.SolidLoft "abaqus.Part.PartFeature.PartFeature.SolidLoft (Python method) — This method creates an additional Feature object by lofting between the given sections and adding material to the part. You define the sections using a sequence of edges from the part or an EdgeArray.")(loftsections[, startCondition, ...]) | This method creates an additional Feature object by lofting between the given sections and adding material to the part. |
    | [`SolidRevolve`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.SolidRevolve "abaqus.Part.PartFeature.PartFeature.SolidRevolve (Python method) — This method creates an additional Feature object by revolving the given ConstrainedSketch object by the given angle, creating a solid protrusion. The ConstrainedSketch object must define a closed profile and an axis of revolution. The axis is defined by a single construction line.")(sketchPlane, sketchPlaneSide, ...) | This method creates an additional Feature object by revolving the given ConstrainedSketch object by the given angle, creating a solid protrusion. |
    | [`SolidSweep`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.SolidSweep "abaqus.Part.PartFeature.PartFeature.SolidSweep (Python method) — This method creates an additional Feature object by sweeping the given ConstrainedSketch object or a Face object along a path which may be a ConstrainedSketch or a sequence of Edge objects, creating a solid swept protrusion. If the profile section is a ConstrainedSketch object, it must define a closed profile. The section sketch can be created at the normal plane at the start of the sweep path or it may be created on a Datum plane or a planar Face. No checks are made for self-intersection.")(path, profile[, pathPlane, ...]) | This method creates an additional Feature object by sweeping the given ConstrainedSketch object or a Face object along a path which may be a ConstrainedSketch or a sequence of Edge objects, creating a solid swept protrusion. |
    | [`Stitch`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.Stitch "abaqus.Part.PartFeature.PartFeature.Stitch (Python method) — This method attempts to create a valid part by binding together free and imprecise edges of all the faces of a part. If edgeList is not given, a global stitch will be performed. If stitchTolerance is not specified, a value of 1.0 will be used.")([edgeList, stitchTolerance]) | This method attempts to create a valid part by binding together free and imprecise edges of all the faces of a part. |
    | [`Wire`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.Wire "abaqus.Part.PartFeature.PartFeature.Wire (Python method) — This method creates an additional Feature object by creating a planar wire from the given ConstrainedSketch object. The ConstrainedSketch object must define a closed profile.")(sketchPlane, sketchPlaneSide, ...[, ...]) | This method creates an additional Feature object by creating a planar wire from the given ConstrainedSketch object. |
    | [`WireSpline`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.WireSpline "abaqus.Part.PartFeature.PartFeature.WireSpline (Python method) — This method creates an additional Feature object by creating a spline wire that passes through a sequence of given points. Each point can be a datum point, a vertex, an interesting point, or a tuple.")(points[, mergeType, ...]) | This method creates an additional Feature object by creating a spline wire that passes through a sequence of given points. |
    | [`WirePolyLine`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.WirePolyLine "abaqus.Part.PartFeature.PartFeature.WirePolyLine (Python method) — This method creates an additional Feature object by creating a polyline wire that passes through a sequence of given points. Each point can be a datum point, a vertex, an interesting point, or a tuple.")(points[, mergeType, meshable]) | This method creates an additional Feature object by creating a polyline wire that passes through a sequence of given points. |
    | [`WireFromEdge`](part_assembly/part.html#abaqus.Part.PartFeature.PartFeature.WireFromEdge "abaqus.Part.PartFeature.PartFeature.WireFromEdge (Python method) — This method creates an additional Feature object by creating a Wire by selecting one or more Edge objects of a Solid or Shell part.")(edgeList) | This method creates an additional Feature object by creating a Wire by selecting one or more Edge objects of a Solid or Shell part. |

    Inherited from [`Feature`](part_assembly/feature.html#abaqus.Feature.Feature.Feature "abaqus.Feature.Feature.Feature (Python class) — Bases: object")

    |  |  |
    | --- | --- |
    | [`AttachmentPoints`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.AttachmentPoints "abaqus.Feature.Feature.Feature.AttachmentPoints (Python method) — This method creates an attachment points Feature. Attachment points may be created using datum points, vertices, reference points, attachment points, interesting points, orphan mesh nodes or coordinates. Optionally, the attachment points can be projected on geometric faces or element faces.")(name, points[, ...]) | This method creates an attachment points Feature. |
    | [`AttachmentPointsAlongDirection`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.AttachmentPointsAlongDirection "abaqus.Feature.Feature.Feature.AttachmentPointsAlongDirection (Python method) — This method creates a Feature object by creating attachment points along a direction or between two points. A Datum point, a ConstrainedSketchVertex, a Reference point, an Attachment point, an Interesting point, or an orphan mesh Node can be specified as the start or end point. The direction can be specified using a straight edge or a datum axis.")(name, ...[, ...]) | This method creates a Feature object by creating attachment points along a direction or between two points. |
    | [`AttachmentPointsOffsetFromEdges`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.AttachmentPointsOffsetFromEdges "abaqus.Feature.Feature.Feature.AttachmentPointsOffsetFromEdges (Python method) — This method creates a Feature object by creating attachment points along or offset from one or more connected edges.")(name, edges) | This method creates a Feature object by creating attachment points along or offset from one or more connected edges. |
    | [`DatumAxisByCylFace`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumAxisByCylFace "abaqus.Feature.Feature.Feature.DatumAxisByCylFace (Python method) — This method creates a Feature object and a DatumAxis object along the axis of a cylinder or cone.")(face) | This method creates a Feature object and a DatumAxis object along the axis of a cylinder or cone. |
    | [`DatumAxisByNormalToPlane`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumAxisByNormalToPlane "abaqus.Feature.Feature.Feature.DatumAxisByNormalToPlane (Python method) — This method creates a Feature object and a DatumAxis object normal to the specified plane and passing through the specified point.")(plane, point) | This method creates a Feature object and a DatumAxis object normal to the specified plane and passing through the specified point. |
    | [`DatumAxisByParToEdge`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumAxisByParToEdge "abaqus.Feature.Feature.Feature.DatumAxisByParToEdge (Python method) — This method creates a Feature object and a DatumAxis object parallel to the specified edge and passing through the specified point.")(edge, point) | This method creates a Feature object and a DatumAxis object parallel to the specified edge and passing through the specified point. |
    | [`DatumAxisByPrincipalAxis`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumAxisByPrincipalAxis "abaqus.Feature.Feature.Feature.DatumAxisByPrincipalAxis (Python method) — This method creates a Feature object and a DatumAxis object along one of the three principal axes.")(principalAxis) | This method creates a Feature object and a DatumAxis object along one of the three principal axes. |
    | [`DatumAxisByRotation`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumAxisByRotation "abaqus.Feature.Feature.Feature.DatumAxisByRotation (Python method)")() |  |
    | [`DatumAxisByThreePoint`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumAxisByThreePoint "abaqus.Feature.Feature.Feature.DatumAxisByThreePoint (Python method) — This method creates a Feature object and a DatumAxis object normal to the circle described by three points and through its center.")(point1, point2, point3) | This method creates a Feature object and a DatumAxis object normal to the circle described by three points and through its center. |
    | [`DatumAxisByThruEdge`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumAxisByThruEdge "abaqus.Feature.Feature.Feature.DatumAxisByThruEdge (Python method) — This method creates a Feature object and a DatumAxis object along the specified edge.")(edge) | This method creates a Feature object and a DatumAxis object along the specified edge. |
    | [`DatumAxisByTwoPlane`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumAxisByTwoPlane "abaqus.Feature.Feature.Feature.DatumAxisByTwoPlane (Python method) — This method creates a Feature object and a DatumAxis object at the intersection of two planes.")(plane1, plane2) | This method creates a Feature object and a DatumAxis object at the intersection of two planes. |
    | [`DatumAxisByTwoPoint`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumAxisByTwoPoint "abaqus.Feature.Feature.Feature.DatumAxisByTwoPoint (Python method) — This method creates a Feature object and a DatumAxis object along the line joining two points.")(point1, point2) | This method creates a Feature object and a DatumAxis object along the line joining two points. |
    | [`DatumCsysByDefault`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumCsysByDefault "abaqus.Feature.Feature.Feature.DatumCsysByDefault (Python method) — This method creates a Feature object and a DatumCsys object from the specified default coordinate system at the origin.")(coordSysType[, name]) | This method creates a Feature object and a DatumCsys object from the specified default coordinate system at the origin. |
    | [`DatumCsysByOffset`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumCsysByOffset "abaqus.Feature.Feature.Feature.DatumCsysByOffset (Python method) — This method creates a Feature object and a DatumCsys object by offsetting the origin of an existing datum coordinate system to a specified point.")(coordSysType, ...[, name]) | This method creates a Feature object and a DatumCsys object by offsetting the origin of an existing datum coordinate system to a specified point. |
    | [`DatumCsysByThreePoints`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumCsysByThreePoints "abaqus.Feature.Feature.Feature.DatumCsysByThreePoints (Python method) — This method creates a Feature object and a DatumCsys object from three points.")(coordSysType, origin, ...) | This method creates a Feature object and a DatumCsys object from three points. |
    | [`DatumCsysByTwoLines`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumCsysByTwoLines "abaqus.Feature.Feature.Feature.DatumCsysByTwoLines (Python method) — This method creates a Feature object and a DatumCsys object from two orthogonal lines. The origin of the new datum coordinate system is placed at the intersection of the two lines.")(coordSysType, line1, line2) | This method creates a Feature object and a DatumCsys object from two orthogonal lines. |
    | [`DatumPlaneByPrincipalPlane`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumPlaneByPrincipalPlane "abaqus.Feature.Feature.Feature.DatumPlaneByPrincipalPlane (Python method) — This method creates a Feature object and a DatumPlane object through the origin along one of the three principal planes.")(principalPlane, ...) | This method creates a Feature object and a DatumPlane object through the origin along one of the three principal planes. |
    | [`DatumPlaneByOffset`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumPlaneByOffset "abaqus.Feature.Feature.Feature.DatumPlaneByOffset (Python method)")() |  |
    | [`DatumPlaneByRotation`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumPlaneByRotation "abaqus.Feature.Feature.Feature.DatumPlaneByRotation (Python method) — This method creates a Feature object and a DatumPlane object by rotating a plane about the specified axis through the specified angle.")(plane, axis, angle) | This method creates a Feature object and a DatumPlane object by rotating a plane about the specified axis through the specified angle. |
    | [`DatumPlaneByThreePoints`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumPlaneByThreePoints "abaqus.Feature.Feature.Feature.DatumPlaneByThreePoints (Python method) — This method creates a Feature object and a DatumPlane object defined by passing through three points.")(point1, point2, point3) | This method creates a Feature object and a DatumPlane object defined by passing through three points. |
    | [`DatumPlaneByLinePoint`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumPlaneByLinePoint "abaqus.Feature.Feature.Feature.DatumPlaneByLinePoint (Python method) — This method creates a Feature object and a DatumPlane object that pass through the specified line and through the specified point that does not lie on the line.")(line, point) | This method creates a Feature object and a DatumPlane object that pass through the specified line and through the specified point that does not lie on the line. |
    | [`DatumPlaneByPointNormal`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumPlaneByPointNormal "abaqus.Feature.Feature.Feature.DatumPlaneByPointNormal (Python method) — This method creates a Feature object and a DatumPlane object normal to the specified line and running through the specified point.")(point, normal) | This method creates a Feature object and a DatumPlane object normal to the specified line and running through the specified point. |
    | [`DatumPlaneByTwoPoint`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumPlaneByTwoPoint "abaqus.Feature.Feature.Feature.DatumPlaneByTwoPoint (Python method) — This method creates a Feature object and a DatumPlane object midway between two points and normal to the line connecting the points.")(point1, point2) | This method creates a Feature object and a DatumPlane object midway between two points and normal to the line connecting the points. |
    | [`DatumPointByCoordinate`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumPointByCoordinate "abaqus.Feature.Feature.Feature.DatumPointByCoordinate (Python method) — This method creates a Feature object and a DatumPoint object at the point defined by the specified coordinates.")(coords) | This method creates a Feature object and a DatumPoint object at the point defined by the specified coordinates. |
    | [`DatumPointByOffset`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumPointByOffset "abaqus.Feature.Feature.Feature.DatumPointByOffset (Python method) — This method creates a Feature object and a DatumPoint object offset from an existing point by a vector.")(point, vector) | This method creates a Feature object and a DatumPoint object offset from an existing point by a vector. |
    | [`DatumPointByMidPoint`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumPointByMidPoint "abaqus.Feature.Feature.Feature.DatumPointByMidPoint (Python method) — This method creates a Feature object and a DatumPoint object midway between two points.")(point1, point2) | This method creates a Feature object and a DatumPoint object midway between two points. |
    | [`DatumPointByOnFace`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumPointByOnFace "abaqus.Feature.Feature.Feature.DatumPointByOnFace (Python method) — This method creates a Feature object and a DatumPoint object on the specified face, offset from two edges.")(face, edge1, offset1, ...) | This method creates a Feature object and a DatumPoint object on the specified face, offset from two edges. |
    | [`DatumPointByEdgeParam`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumPointByEdgeParam "abaqus.Feature.Feature.Feature.DatumPointByEdgeParam (Python method) — This method creates a Feature object and a DatumPoint object along an edge at a selected distance from one end of the edge.")(edge, parameter) | This method creates a Feature object and a DatumPoint object along an edge at a selected distance from one end of the edge. |
    | [`DatumPointByProjOnEdge`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumPointByProjOnEdge "abaqus.Feature.Feature.Feature.DatumPointByProjOnEdge (Python method) — This method creates a Feature object and a DatumPoint object along an edge by projecting an existing point along the normal to the edge.")(point, edge) | This method creates a Feature object and a DatumPoint object along an edge by projecting an existing point along the normal to the edge. |
    | [`DatumPointByProjOnFace`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.DatumPointByProjOnFace "abaqus.Feature.Feature.Feature.DatumPointByProjOnFace (Python method) — This method creates a Feature object and a DatumPoint object on a specified face by projecting an existing point onto the face.")(point, face) | This method creates a Feature object and a DatumPoint object on a specified face by projecting an existing point onto the face. |
    | [`MakeSketchTransform`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.MakeSketchTransform "abaqus.Feature.Feature.Feature.MakeSketchTransform (Python method) — This method creates a Transform object. A Transform object is a 4x3 matrix of Floats that represents the transformation from sketch coordinates to part coordinates.")(sketchPlane[, origin, ...]) | This method creates a Transform object. |
    | [`PartitionCellByDatumPlane`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.PartitionCellByDatumPlane "abaqus.Feature.Feature.Feature.PartitionCellByDatumPlane (Python method) — This method partitions one or more cells using the given datum plane.")(cells, datumPlane) | This method partitions one or more cells using the given datum plane. |
    | [`PartitionCellByExtendFace`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.PartitionCellByExtendFace "abaqus.Feature.Feature.Feature.PartitionCellByExtendFace (Python method) — This method partitions one or more cells by extending the underlying geometry of a given face to partition the target cells.")(cells, extendFace) | This method partitions one or more cells by extending the underlying geometry of a given face to partition the target cells. |
    | [`PartitionCellByExtrudeEdge`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.PartitionCellByExtrudeEdge "abaqus.Feature.Feature.Feature.PartitionCellByExtrudeEdge (Python method) — This method partitions one or more cells by extruding selected edges in the given direction.")(cells, edges, ...) | This method partitions one or more cells by extruding selected edges in the given direction. |
    | [`PartitionCellByPatchNCorners`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.PartitionCellByPatchNCorners "abaqus.Feature.Feature.Feature.PartitionCellByPatchNCorners (Python method) — This method partitions a cell using an N-sided cutting patch defined by the given corner points.")(cell, cornerPoints) | This method partitions a cell using an N-sided cutting patch defined by the given corner points. |
    | [`PartitionCellByPatchNEdges`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.PartitionCellByPatchNEdges "abaqus.Feature.Feature.Feature.PartitionCellByPatchNEdges (Python method) — This method partitions a cell using an N-sided cutting patch defined by the given edges.")(cell, edges) | This method partitions a cell using an N-sided cutting patch defined by the given edges. |
    | [`PartitionCellByPlaneNormalToEdge`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.PartitionCellByPlaneNormalToEdge "abaqus.Feature.Feature.Feature.PartitionCellByPlaneNormalToEdge (Python method) — This method partitions one or more cells using a plane normal to an edge at the given edge point.")(cells, ...) | This method partitions one or more cells using a plane normal to an edge at the given edge point. |
    | [`PartitionCellByPlanePointNormal`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.PartitionCellByPlanePointNormal "abaqus.Feature.Feature.Feature.PartitionCellByPlanePointNormal (Python method) — This method partitions one or more cells using a plane defined by a point and a normal direction.")(cells, ...) | This method partitions one or more cells using a plane defined by a point and a normal direction. |
    | [`PartitionCellByPlaneThreePoints`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.PartitionCellByPlaneThreePoints "abaqus.Feature.Feature.Feature.PartitionCellByPlaneThreePoints (Python method) — This method partitions one or more cells using a plane defined by three points.")(cells, ...) | This method partitions one or more cells using a plane defined by three points. |
    | [`PartitionCellBySweepEdge`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.PartitionCellBySweepEdge "abaqus.Feature.Feature.Feature.PartitionCellBySweepEdge (Python method) — This method partitions one or more cells by sweeping selected edges along the given sweep path.")(cells, edges, sweepPath) | This method partitions one or more cells by sweeping selected edges along the given sweep path. |
    | [`PartitionEdgeByDatumPlane`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.PartitionEdgeByDatumPlane "abaqus.Feature.Feature.Feature.PartitionEdgeByDatumPlane (Python method) — This method partitions an edge where it intersects with a datum plane.")(edges, datumPlane) | This method partitions an edge where it intersects with a datum plane. |
    | [`PartitionEdgeByParam`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.PartitionEdgeByParam "abaqus.Feature.Feature.Feature.PartitionEdgeByParam (Python method) — This method partitions one or more edges at the given normalized edge parameter.")(edges, parameter) | This method partitions one or more edges at the given normalized edge parameter. |
    | [`PartitionEdgeByPoint`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.PartitionEdgeByPoint "abaqus.Feature.Feature.Feature.PartitionEdgeByPoint (Python method) — This method partitions an edge at the given point.")(edge, point) | This method partitions an edge at the given point. |
    | [`PartitionFaceByAuto`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.PartitionFaceByAuto "abaqus.Feature.Feature.Feature.PartitionFaceByAuto (Python method) — This method automatically partitions a target face into simple regions that can be meshed using a structured meshing technique.")(face) | This method automatically partitions a target face into simple regions that can be meshed using a structured meshing technique. |
    | [`PartitionFaceByCurvedPathEdgeParams`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.PartitionFaceByCurvedPathEdgeParams "abaqus.Feature.Feature.Feature.PartitionFaceByCurvedPathEdgeParams (Python method) — This method partitions a face normal to two edges, using a curved path between the two given edge points defined by the normalized edge parameters.")(face, ...) | This method partitions a face normal to two edges, using a curved path between the two given edge points defined by the normalized edge parameters. |
    | [`PartitionFaceByCurvedPathEdgePoints`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.PartitionFaceByCurvedPathEdgePoints "abaqus.Feature.Feature.Feature.PartitionFaceByCurvedPathEdgePoints (Python method) — This method partitions a face normal to two edges, using a curved path between the two given edge points.")(face, ...) | This method partitions a face normal to two edges, using a curved path between the two given edge points. |
    | [`PartitionFaceByDatumPlane`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.PartitionFaceByDatumPlane "abaqus.Feature.Feature.Feature.PartitionFaceByDatumPlane (Python method) — This method partitions one or more faces using the given datum plane.")(faces, datumPlane) | This method partitions one or more faces using the given datum plane. |
    | [`PartitionFaceByExtendFace`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.PartitionFaceByExtendFace "abaqus.Feature.Feature.Feature.PartitionFaceByExtendFace (Python method) — This method partitions one or more faces by extending the underlying geometry of another given face to partition the target faces.")(faces, extendFace) | This method partitions one or more faces by extending the underlying geometry of another given face to partition the target faces. |
    | [`PartitionFaceByIntersectFace`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.PartitionFaceByIntersectFace "abaqus.Feature.Feature.Feature.PartitionFaceByIntersectFace (Python method) — This method partitions one or more faces using the given cutting faces to partition the target faces.")(faces, cuttingFaces) | This method partitions one or more faces using the given cutting faces to partition the target faces. |
    | [`PartitionFaceByProjectingEdges`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.PartitionFaceByProjectingEdges "abaqus.Feature.Feature.Feature.PartitionFaceByProjectingEdges (Python method) — This method partitions one or more faces by projecting the given edges on the target faces.")(faces, edges) | This method partitions one or more faces by projecting the given edges on the target faces. |
    | [`PartitionFaceByShortestPath`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.PartitionFaceByShortestPath "abaqus.Feature.Feature.Feature.PartitionFaceByShortestPath (Python method) — This method partitions one or more faces using a minimum distance path between the two given points.")(faces, point1, ...) | This method partitions one or more faces using a minimum distance path between the two given points. |
    | [`PartitionFaceBySketch`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.PartitionFaceBySketch "abaqus.Feature.Feature.Feature.PartitionFaceBySketch (Python method) — This method partitions one or more planar faces by sketching on them.")(faces, sketch[, ...]) | This method partitions one or more planar faces by sketching on them. |
    | [`PartitionFaceBySketchDistance`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.PartitionFaceBySketchDistance "abaqus.Feature.Feature.Feature.PartitionFaceBySketchDistance (Python method) — This method partitions one or more faces by sketching on a sketch plane and then projecting the sketch toward the target faces through the given distance.")(faces, ...[, ...]) | This method partitions one or more faces by sketching on a sketch plane and then projecting the sketch toward the target faces through the given distance. |
    | [`PartitionFaceBySketchRefPoint`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.PartitionFaceBySketchRefPoint "abaqus.Feature.Feature.Feature.PartitionFaceBySketchRefPoint (Python method) — This method partitions one or more faces by sketching on a sketch plane and then projecting the sketch toward the target faces through a distance governed by the reference point.")(faces, ...[, ...]) | This method partitions one or more faces by sketching on a sketch plane and then projecting the sketch toward the target faces through a distance governed by the reference point. |
    | [`PartitionFaceBySketchThruAll`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.PartitionFaceBySketchThruAll "abaqus.Feature.Feature.Feature.PartitionFaceBySketchThruAll (Python method) — This method partitions one or more faces by sketching on a sketch plane and then projecting toward the target faces through an infinite distance.")(faces, ...[, ...]) | This method partitions one or more faces by sketching on a sketch plane and then projecting toward the target faces through an infinite distance. |
    | [`ReferencePoint`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.ReferencePoint "abaqus.Feature.Feature.Feature.ReferencePoint (Python method) — This method creates a Feature object and a ReferencePoint object at the specified location.")(point[, instanceName]) | This method creates a Feature object and a ReferencePoint object at the specified location. |
    | [`RemoveWireEdges`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.RemoveWireEdges "abaqus.Feature.Feature.Feature.RemoveWireEdges (Python method) — This method removes wire edges.")(wireEdgeList) | This method removes wire edges. |
    | [`WirePolyLine`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.WirePolyLine "abaqus.Feature.Feature.Feature.WirePolyLine (Python method) — This method creates an additional Feature object by creating a series of wires joining points in pairs. When such a feature is created at the Part level, then each point can be either a datum point, a vertex, a reference point, an interesting point, an orphan mesh node, or the coordinates of a point. When such a feature is created at the Assembly level, then each point can only be a vertex, a reference point, or an orphan mesh node.")(points[, mergeType, meshable]) | This method creates an additional Feature object by creating a series of wires joining points in pairs. |
    | [`isSuppressed`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.isSuppressed "abaqus.Feature.Feature.Feature.isSuppressed (Python method) — This method queries the suppressed state of the feature.")() | This method queries the suppressed state of the feature. |
    | [`restore`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.restore "abaqus.Feature.Feature.Feature.restore (Python method) — This method restores the parameters of a feature to the value they had when the backup method was invoked on the part or assembly.")() | This method restores the parameters of a feature to the value they had when the backup method was invoked on the part or assembly. |
    | [`resume`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.resume "abaqus.Feature.Feature.Feature.resume (Python method) — This method resumes suppressed features.")() | This method resumes suppressed features. |
    | [`setValues`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.setValues "abaqus.Feature.Feature.Feature.setValues (Python method) — This method modifies the Feature object.")([parameter, parameter1, ...]) | This method modifies the Feature object. |
    | [`suppress`](part_assembly/feature.html#abaqus.Feature.Feature.Feature.suppress "abaqus.Feature.Feature.Feature.suppress (Python method) — This method suppresses features.")() | This method suppresses features. |

    ---

    Member Details:

    CompositeLayup(*[name](#abaqus.Property.PropertyPart.PropertyPart.CompositeLayup.name "abaqus.Property.PropertyPart.PropertyPart.CompositeLayup.name (Python parameter) — A String specifying the repository key.")*, *[description](#abaqus.Property.PropertyPart.PropertyPart.CompositeLayup.description "abaqus.Property.PropertyPart.PropertyPart.CompositeLayup.description (Python parameter) — A String specifying a description of the composite layup.")=`''`*, *[offsetType](#abaqus.Property.PropertyPart.PropertyPart.CompositeLayup.offsetType "abaqus.Property.PropertyPart.PropertyPart.CompositeLayup.offsetType (Python parameter) — A SymbolicConstant specifying the method used to define the shell offset.")=`abaqusConstants.GLOBAL`*, *[offsetField](#abaqus.Property.PropertyPart.PropertyPart.CompositeLayup.offsetField "abaqus.Property.PropertyPart.PropertyPart.CompositeLayup.offsetField (Python parameter) — A String specifying The name of the field specifying the offset.")=`''`*, *[offsetValues](#abaqus.Property.PropertyPart.PropertyPart.CompositeLayup.offsetValues "abaqus.Property.PropertyPart.PropertyPart.CompositeLayup.offsetValues (Python parameter) — A Float specifying The offset of the shell section.")=`0`*, *[elementType](#abaqus.Property.PropertyPart.PropertyPart.CompositeLayup.elementType "abaqus.Property.PropertyPart.PropertyPart.CompositeLayup.elementType (Python parameter) — A SymbolicConstant specifying the type of element in the composite layup.")=`abaqusConstants.SHELL`*, *[symmetric](#abaqus.Property.PropertyPart.PropertyPart.CompositeLayup.symmetric "abaqus.Property.PropertyPart.PropertyPart.CompositeLayup.symmetric (Python parameter) — A Boolean specifying whether or not the layup should be made symmetric by the analysis. The default value is OFF.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L35-L97)[¶](#abaqus.Property.PropertyPart.PropertyPart.CompositeLayup "Permalink to this definition")
    :   This method creates a CompositeLayup object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].CompositeLayup
        ```

        Note

        Check [CompositeLayup on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-compositelayuppyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Property.PropertyPart.PropertyPart.CompositeLayup-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Property.PropertyPart.PropertyPart.CompositeLayup.name "Permalink to this definition")
            :   A String specifying the repository key.

            description=`''`[¶](#abaqus.Property.PropertyPart.PropertyPart.CompositeLayup.description "Permalink to this definition")
            :   A String specifying a description of the composite layup.

            offsetType=`abaqusConstants.GLOBAL`[¶](#abaqus.Property.PropertyPart.PropertyPart.CompositeLayup.offsetType "Permalink to this definition")
            :   A SymbolicConstant specifying the method used to define the shell offset. If
                **offsetType** = OFFSET\_FIELD the **offsetField** argument is required. This member is valid
                only if **elementType** = SHELL. Possible values are SINGLE\_VALUE, MIDDLE\_SURFACE,
                TOP\_SURFACE, BOTTOM\_SURFACE, OFFSET\_FIELD, and GLOBAL. The default value is GLOBAL.

            offsetField=`''`[¶](#abaqus.Property.PropertyPart.PropertyPart.CompositeLayup.offsetField "Permalink to this definition")
            :   A String specifying The name of the field specifying the offset. This member is valid
                only if **elementType** = SHELL. The default value is an empty string.

            offsetValues=`0`[¶](#abaqus.Property.PropertyPart.PropertyPart.CompositeLayup.offsetValues "Permalink to this definition")
            :   A Float specifying The offset of the shell section. This member is valid only if
                **elementType** = SHELL. The default value is 0.0.

            elementType=`abaqusConstants.SHELL`[¶](#abaqus.Property.PropertyPart.PropertyPart.CompositeLayup.elementType "Permalink to this definition")
            :   A SymbolicConstant specifying the type of element in the composite layup. Possible
                values are SHELL, CONTINUUM\_SHELL, and SOLID. The default value is SHELL.

            symmetric=`0`[¶](#abaqus.Property.PropertyPart.PropertyPart.CompositeLayup.symmetric "Permalink to this definition")
            :   A Boolean specifying whether or not the layup should be made symmetric by the analysis.
                The default value is OFF.

        Returns:[¶](#abaqus.Property.PropertyPart.PropertyPart.CompositeLayup-returns "Permalink to this headline")
        :   **layup** – A CompositeLayup object.

        Return type:[¶](#abaqus.Property.PropertyPart.PropertyPart.CompositeLayup-return-type "Permalink to this headline")
        :   [`CompositeLayup`](#abaqus.Property.PropertyPart.CompositeLayup "abaqus.Property.PropertyPart.CompositeLayup (Python class) — Bases: object")

        Raises:[¶](#abaqus.Property.PropertyPart.PropertyPart.CompositeLayup-raises "Permalink to this headline")
        :   [**AbaqusException**](../../kernel/utility.html#abaqus.UtilityAndView.AbaqusException.AbaqusException "abaqus.UtilityAndView.AbaqusException.AbaqusException (Python class) — Bases: Exception") –

    MaterialOrientation(*[region](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.region "abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.region (Python parameter) — A Set object specifying a region for which the material orientation is defined.")=`None`*, *[localCsys](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.localCsys "abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.localCsys (Python parameter) — A DatumCsys object specifying the local coordinate system or None, describing the material orientation for the given region.")=`None`*, *[axis](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.axis "abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.axis (Python parameter) — A SymbolicConstant specifying the axis of a datum coordinate system about which an additional rotation is applied.")=`abaqusConstants.AXIS_1`*, *[angle](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.angle "abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.angle (Python parameter) — A Float specifying the angle of the additional rotation (if accessed from the ODB instead of the MDB, it will be a string instead of a float).")=`0`*, *[stackDirection](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.stackDirection "abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.stackDirection (Python parameter) — A SymbolicConstant specifying the stack or thickness direction.")=`abaqusConstants.STACK_3`*, *[fieldName](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.fieldName "abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.fieldName (Python parameter) — A String specifying the name of the DiscreteField object specifying the orientation.")=`''`*, *[orientationType](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.orientationType "abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.orientationType (Python parameter) — A SymbolicConstant specifying the method used to define the material orientation.")=`abaqusConstants.GLOBAL`*, *[normalAxisDirection](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.normalAxisDirection "abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.normalAxisDirection (Python parameter) — A SymbolicConstant specifying the axis that is defined by the normal axis direction for a discrete orientation.")=`abaqusConstants.AXIS_3`*, *[normalAxisDefinition](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.normalAxisDefinition "abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.normalAxisDefinition (Python parameter) — A SymbolicConstant specifying the method used to define the normal axis direction for a discrete orientation.")=`abaqusConstants.NORMAL_VECTOR`*, *[normalAxisRegion](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.normalAxisRegion "abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.normalAxisRegion (Python parameter) — A Surface object specifying a region whose geometric normals define the normal axis for the discrete orientation.")=`None`*, *[normalAxisDatum](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.normalAxisDatum "abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.normalAxisDatum (Python parameter) — A DatumAxis object specifying the Datum Axis or None, describing the normal axis direction for the discrete orientation.")=`None`*, *[flipNormalDirection](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.flipNormalDirection "abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.flipNormalDirection (Python parameter) — A Boolean specifying the flag to reverse the direction of the defined normal axis direction.")=`0`*, *[normalAxisVector](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.normalAxisVector "abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.normalAxisVector (Python parameter) — A sequence of Floats specifying the vector that defines the direction of the normal axis of the discrete orientation.")=`()`*, *[primaryAxisDirection](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.primaryAxisDirection "abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.primaryAxisDirection (Python parameter) — A SymbolicConstant specifying the axis that is defined by the primary axis direction for a discrete orientation.")=`abaqusConstants.AXIS_1`*, *[primaryAxisDefinition](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.primaryAxisDefinition "abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.primaryAxisDefinition (Python parameter) — A SymbolicConstant specifying the method used to define the primary axis direction for a discrete orientation.")=`abaqusConstants.PRIMARY_VECTOR`*, *[primaryAxisRegion](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.primaryAxisRegion "abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.primaryAxisRegion (Python parameter) — A Set object specifying a region whose geometric tangents define the primary axis for the discrete orientation.")=`None`*, *[primaryAxisDatum](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.primaryAxisDatum "abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.primaryAxisDatum (Python parameter) — A DatumAxis object specifying the Datum Axis or None, describing the primary axis direction for the discrete orientation.")=`None`*, *[flipPrimaryDirection](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.flipPrimaryDirection "abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.flipPrimaryDirection (Python parameter) — A Boolean specifying the flag to reverse the direction of the defined primary axis direction.")=`0`*, *[primaryAxisVector](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.primaryAxisVector "abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.primaryAxisVector (Python parameter) — A sequence of Floats specifying the vector that defines the direction of the primary axis of the discrete orientation.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L148-L273)[¶](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation "Permalink to this definition")
    :   This method creates a MaterialOrientation object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].MaterialOrientation
        ```

        Note

        Check [MaterialOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-materialorientationpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation-parameters "Permalink to this headline")
        :   region=`None`[¶](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.region "Permalink to this definition")
            :   A Set object specifying a region for which the material orientation is defined.

            localCsys=`None`[¶](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.localCsys "Permalink to this definition")
            :   A DatumCsys object specifying the local coordinate system or None, describing the
                material orientation for the given region. In the ODB, this member was previously
                accessible using “csys,” but support has now been added for localCsys and the csys
                member will be deprecated.

            axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the axis of a datum coordinate system about which an
                additional rotation is applied. For shells this axis is also the shell normal. Possible
                values are AXIS\_1, AXIS\_2, and AXIS\_3. The default value is AXIS\_1.

            angle=`0`[¶](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.angle "Permalink to this definition")
            :   A Float specifying the angle of the additional rotation (if accessed from the ODB
                instead of the MDB, it will be a string instead of a float). The default value is 0.0.

            stackDirection=`abaqusConstants.STACK_3`[¶](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.stackDirection "Permalink to this definition")
            :   A SymbolicConstant specifying the stack or thickness direction. Possible values are
                STACK\_1, STACK\_2, STACK\_3, and STACK\_ORIENTATION. The default value is STACK\_3.

            fieldName=`''`[¶](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.fieldName "Permalink to this definition")
            :   A String specifying the name of the DiscreteField object specifying the orientation. The
                default value is an empty string.

            orientationType=`abaqusConstants.GLOBAL`[¶](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.orientationType "Permalink to this definition")
            :   A SymbolicConstant specifying the method used to define the material orientation. If
                **orientationType** = SYSTEM, the **region** and **localCsys** arguments are required. If
                **orientationType** = FIELD, the **fieldName** argument is required. Possible values are
                GLOBAL, SYSTEM, FIELD, DISCRETE, and USER. The default value is GLOBAL.

            normalAxisDirection=`abaqusConstants.AXIS_3`[¶](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.normalAxisDirection "Permalink to this definition")
            :   A SymbolicConstant specifying the axis that is defined by the normal axis direction for
                a discrete orientation. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default
                value is AXIS\_3.

            normalAxisDefinition=`abaqusConstants.NORMAL_VECTOR`[¶](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.normalAxisDefinition "Permalink to this definition")
            :   A SymbolicConstant specifying the method used to define the normal axis direction for a
                discrete orientation. Possible values are SURFACE, NORMAL\_DATUM, and NORMAL\_VECTOR. The
                default value is NORMAL\_VECTOR.

            normalAxisRegion=`None`[¶](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.normalAxisRegion "Permalink to this definition")
            :   A Surface object specifying a region whose geometric normals define the normal axis for
                the discrete orientation.

            normalAxisDatum=`None`[¶](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.normalAxisDatum "Permalink to this definition")
            :   A DatumAxis object specifying the Datum Axis or None, describing the normal axis
                direction for the discrete orientation.

            flipNormalDirection=`0`[¶](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.flipNormalDirection "Permalink to this definition")
            :   A Boolean specifying the flag to reverse the direction of the defined normal axis
                direction. The default value is OFF.

            normalAxisVector=`()`[¶](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.normalAxisVector "Permalink to this definition")
            :   A sequence of Floats specifying the vector that defines the direction of the normal axis
                of the discrete orientation.

            primaryAxisDirection=`abaqusConstants.AXIS_1`[¶](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.primaryAxisDirection "Permalink to this definition")
            :   A SymbolicConstant specifying the axis that is defined by the primary axis direction for
                a discrete orientation. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default
                value is AXIS\_1.

            primaryAxisDefinition=`abaqusConstants.PRIMARY_VECTOR`[¶](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.primaryAxisDefinition "Permalink to this definition")
            :   A SymbolicConstant specifying the method used to define the primary axis direction for a
                discrete orientation. Possible values are SURFACE, PRIMARY\_DATUM, and PRIMARY\_VECTOR.
                The default value is PRIMARY\_VECTOR.

            primaryAxisRegion=`None`[¶](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.primaryAxisRegion "Permalink to this definition")
            :   A Set object specifying a region whose geometric tangents define the primary axis for
                the discrete orientation.

            primaryAxisDatum=`None`[¶](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.primaryAxisDatum "Permalink to this definition")
            :   A DatumAxis object specifying the Datum Axis or None, describing the primary axis
                direction for the discrete orientation.

            flipPrimaryDirection=`0`[¶](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.flipPrimaryDirection "Permalink to this definition")
            :   A Boolean specifying the flag to reverse the direction of the defined primary axis
                direction. The default value is OFF.

            primaryAxisVector=`()`[¶](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation.primaryAxisVector "Permalink to this definition")
            :   A sequence of Floats specifying the vector that defines the direction of the primary
                axis of the discrete orientation.

        Returns:[¶](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation-returns "Permalink to this headline")
        :   **orientation** – A MaterialOrientation object.

        Return type:[¶](#abaqus.Property.PropertyPart.PropertyPart.MaterialOrientation-return-type "Permalink to this headline")
        :   [`MaterialOrientation`](#abaqus.Property.PropertyPart.MaterialOrientation "abaqus.Property.PropertyPart.MaterialOrientation (Python class) — Bases: object")

    SectionAssignment(*[region](#abaqus.Property.PropertyPart.PropertyPart.SectionAssignment.region "abaqus.Property.PropertyPart.PropertyPart.SectionAssignment.region (Python parameter) — A Set object specifying the region to which the section is assigned.")*, *[sectionName](#abaqus.Property.PropertyPart.PropertyPart.SectionAssignment.sectionName "abaqus.Property.PropertyPart.PropertyPart.SectionAssignment.sectionName (Python parameter) — A String specifying the name of the section.")*, *[thicknessAssignment](#abaqus.Property.PropertyPart.PropertyPart.SectionAssignment.thicknessAssignment "abaqus.Property.PropertyPart.PropertyPart.SectionAssignment.thicknessAssignment (Python parameter) — A SymbolicConstant specifying section thickness assignment method.")=`abaqusConstants.FROM_SECTION`*, *[offset](#abaqus.Property.PropertyPart.PropertyPart.SectionAssignment.offset "abaqus.Property.PropertyPart.PropertyPart.SectionAssignment.offset (Python parameter) — A Float specifying the offset of the shell section.")=`0`*, *[offsetType](#abaqus.Property.PropertyPart.PropertyPart.SectionAssignment.offsetType "abaqus.Property.PropertyPart.PropertyPart.SectionAssignment.offsetType (Python parameter) — A SymbolicConstant specifying the method used to define the shell offset.")=`abaqusConstants.SINGLE_VALUE`*, *[offsetField](#abaqus.Property.PropertyPart.PropertyPart.SectionAssignment.offsetField "abaqus.Property.PropertyPart.PropertyPart.SectionAssignment.offsetField (Python parameter) — A String specifying the name of the field specifying the offset.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L99-L146)[¶](#abaqus.Property.PropertyPart.PropertyPart.SectionAssignment "Permalink to this definition")
    :   This method creates a SectionAssignment object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].SectionAssignment
        mdb.models[name].rootAssembly.SectionAssignment
        ```

        Note

        Check [SectionAssignment on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionassignmentpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Property.PropertyPart.PropertyPart.SectionAssignment-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Property.PropertyPart.PropertyPart.SectionAssignment.region "Permalink to this definition")
            :   A Set object specifying the region to which the section is assigned.

            sectionName[¶](#abaqus.Property.PropertyPart.PropertyPart.SectionAssignment.sectionName "Permalink to this definition")
            :   A String specifying the name of the section.

            thicknessAssignment=`abaqusConstants.FROM_SECTION`[¶](#abaqus.Property.PropertyPart.PropertyPart.SectionAssignment.thicknessAssignment "Permalink to this definition")
            :   A SymbolicConstant specifying section thickness assignment method. Possible values are
                FROM\_SECTION and FROM\_GEOMETRY. The default value is FROM\_SECTION.

            offset=`0`[¶](#abaqus.Property.PropertyPart.PropertyPart.SectionAssignment.offset "Permalink to this definition")
            :   A Float specifying the offset of the shell section. The default value is 0.0.

            offsetType=`abaqusConstants.SINGLE_VALUE`[¶](#abaqus.Property.PropertyPart.PropertyPart.SectionAssignment.offsetType "Permalink to this definition")
            :   A SymbolicConstant specifying the method used to define the shell offset. If
                **offsetType** is set to OFFSET\_FIELD the **offsetField** must have a value. Possible values
                are SINGLE\_VALUE, MIDDLE\_SURFACE, TOP\_SURFACE, BOTTOM\_SURFACE, FROM\_GEOMETRY, and
                OFFSET\_FIELD. The default value is SINGLE\_VALUE.

            offsetField=`''`[¶](#abaqus.Property.PropertyPart.PropertyPart.SectionAssignment.offsetField "Permalink to this definition")
            :   A String specifying the name of the field specifying the offset. The default value is
                “”.

        Returns:[¶](#abaqus.Property.PropertyPart.PropertyPart.SectionAssignment-returns "Permalink to this headline")
        :   **assignment** – A SectionAssignment object

        Return type:[¶](#abaqus.Property.PropertyPart.PropertyPart.SectionAssignment-return-type "Permalink to this headline")
        :   [`SectionAssignment`](#abaqus.Property.PropertyPart.PropertyPart.SectionAssignment "abaqus.Property.PropertyPart.PropertyPart.SectionAssignment (Python method) — This method creates a SectionAssignment object.")

    assignBeamSectionOrientation(*[region](#abaqus.Property.PropertyPart.PropertyPart.assignBeamSectionOrientation.region "abaqus.Property.PropertyPart.PropertyPart.assignBeamSectionOrientation.region (Python parameter) — A sequence of geomSequences of Edge objects or a sequence of sequences of one-dimensional elements.")*, *[method](#abaqus.Property.PropertyPart.PropertyPart.assignBeamSectionOrientation.method "abaqus.Property.PropertyPart.PropertyPart.assignBeamSectionOrientation.method (Python parameter) — A SymbolicConstant specifying the assignment method.")*, *[n1](#abaqus.Property.PropertyPart.PropertyPart.assignBeamSectionOrientation.n1 "abaqus.Property.PropertyPart.PropertyPart.assignBeamSectionOrientation.n1 (Python parameter) — A sequence of three Floats specifying the approximate local n1n1-direction of the beam cross-section.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L275-L296)[¶](#abaqus.Property.PropertyPart.PropertyPart.assignBeamSectionOrientation "Permalink to this definition")
    :   This method assigns a beam section orientation to a region of a part.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].assignBeamSectionOrientation
        ```

        Note

        Check [PropertyPart.assignBeamSectionOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partassignbeamsectionorientationpyc).

        Parameters:[¶](#abaqus.Property.PropertyPart.PropertyPart.assignBeamSectionOrientation-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Property.PropertyPart.PropertyPart.assignBeamSectionOrientation.region "Permalink to this definition")
            :   A sequence of geomSequences of Edge objects or a sequence of sequences of
                one-dimensional elements.

            method[¶](#abaqus.Property.PropertyPart.PropertyPart.assignBeamSectionOrientation.method "Permalink to this definition")
            :   A SymbolicConstant specifying the assignment method. Only a value of N1\_COSINES is
                currently supported.

            n1[¶](#abaqus.Property.PropertyPart.PropertyPart.assignBeamSectionOrientation.n1 "Permalink to this definition")
            :   A sequence of three Floats specifying the approximate local n1n1-direction of the beam
                cross-section.

    assignMaterialOrientation(*[region](#abaqus.Property.PropertyPart.PropertyPart.assignMaterialOrientation.region "abaqus.Property.PropertyPart.PropertyPart.assignMaterialOrientation.region (Python parameter) — A sequence of geomSequences of ConstrainedSketchVertex, Edge, Face, and Cell objects or a sequence of sequences of elements.")*, *[localCsys](#abaqus.Property.PropertyPart.PropertyPart.assignMaterialOrientation.localCsys "abaqus.Property.PropertyPart.PropertyPart.assignMaterialOrientation.localCsys (Python parameter) — A Datum object specifying the local coordinate system or None, indicating the global coordinate system.")*, *[axis](#abaqus.Property.PropertyPart.PropertyPart.assignMaterialOrientation.axis "abaqus.Property.PropertyPart.PropertyPart.assignMaterialOrientation.axis (Python parameter) — A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate system about which an additional rotation is applied.")=`abaqusConstants.AXIS_1`*, *[angle](#abaqus.Property.PropertyPart.PropertyPart.assignMaterialOrientation.angle "abaqus.Property.PropertyPart.PropertyPart.assignMaterialOrientation.angle (Python parameter) — A Float specifying the angle of the additional rotation.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L298-L325)[¶](#abaqus.Property.PropertyPart.PropertyPart.assignMaterialOrientation "Permalink to this definition")
    :   This method assigns a material orientation to a region.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].assignMaterialOrientation
        ```

        Note

        Check [PropertyPart.assignMaterialOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partassignmaterialorientationpyc).

        Parameters:[¶](#abaqus.Property.PropertyPart.PropertyPart.assignMaterialOrientation-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Property.PropertyPart.PropertyPart.assignMaterialOrientation.region "Permalink to this definition")
            :   A sequence of geomSequences of ConstrainedSketchVertex, Edge, Face, and Cell objects or a sequence of
                sequences of elements.

            localCsys[¶](#abaqus.Property.PropertyPart.PropertyPart.assignMaterialOrientation.localCsys "Permalink to this definition")
            :   A Datum object specifying the local coordinate system or None, indicating the global
                coordinate system.

            axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Property.PropertyPart.PropertyPart.assignMaterialOrientation.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate
                system about which an additional rotation is applied. For shells this axis is also the
                shell normal. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default value is
                AXIS\_1.

            angle=`0`[¶](#abaqus.Property.PropertyPart.PropertyPart.assignMaterialOrientation.angle "Permalink to this definition")
            :   A Float specifying the angle of the additional rotation. The default value is 0.0.

    assignRebarOrientation(*[region](#abaqus.Property.PropertyPart.PropertyPart.assignRebarOrientation.region "abaqus.Property.PropertyPart.PropertyPart.assignRebarOrientation.region (Python parameter) — A sequence of geomSequences of ConstrainedSketchVertex, Edge, Face, and Cell objects or a sequence of sequences of elements.")*, *[localCsys](#abaqus.Property.PropertyPart.PropertyPart.assignRebarOrientation.localCsys "abaqus.Property.PropertyPart.PropertyPart.assignRebarOrientation.localCsys (Python parameter) — A Datum object specifying the local coordinate system or None, indicating the global coordinate system.")*, *[axis](#abaqus.Property.PropertyPart.PropertyPart.assignRebarOrientation.axis "abaqus.Property.PropertyPart.PropertyPart.assignRebarOrientation.axis (Python parameter) — A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate system about which an additional rotation is applied.")=`abaqusConstants.AXIS_1`*, *[angle](#abaqus.Property.PropertyPart.PropertyPart.assignRebarOrientation.angle "abaqus.Property.PropertyPart.PropertyPart.assignRebarOrientation.angle (Python parameter) — A Float specifying the angle of the additional rotation.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L327-L354)[¶](#abaqus.Property.PropertyPart.PropertyPart.assignRebarOrientation "Permalink to this definition")
    :   This method assigns a rebar reference orientation to a region.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].assignRebarOrientation
        ```

        Note

        Check [PropertyPart.assignRebarOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partassignrebarorientationpyc).

        Parameters:[¶](#abaqus.Property.PropertyPart.PropertyPart.assignRebarOrientation-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Property.PropertyPart.PropertyPart.assignRebarOrientation.region "Permalink to this definition")
            :   A sequence of geomSequences of ConstrainedSketchVertex, Edge, Face, and Cell objects or a sequence of
                sequences of elements.

            localCsys[¶](#abaqus.Property.PropertyPart.PropertyPart.assignRebarOrientation.localCsys "Permalink to this definition")
            :   A Datum object specifying the local coordinate system or None, indicating the global
                coordinate system.

            axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Property.PropertyPart.PropertyPart.assignRebarOrientation.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate
                system about which an additional rotation is applied. For shells this axis is also the
                shell normal. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default value is
                AXIS\_1.

            angle=`0`[¶](#abaqus.Property.PropertyPart.PropertyPart.assignRebarOrientation.angle "Permalink to this definition")
            :   A Float specifying the angle of the additional rotation. The default value is 0.0.

    flipNormal(*[regions](#abaqus.Property.PropertyPart.PropertyPart.flipNormal.regions "abaqus.Property.PropertyPart.PropertyPart.flipNormal.regions (Python parameter) — A Region object specifying the region on which normals are flipped.")*, *[referenceRegion](#abaqus.Property.PropertyPart.PropertyPart.flipNormal.referenceRegion "abaqus.Property.PropertyPart.PropertyPart.flipNormal.referenceRegion (Python parameter) — A two-dimensional element object whose normal is to be matched.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L356-L379)[¶](#abaqus.Property.PropertyPart.PropertyPart.flipNormal "Permalink to this definition")
    :   This method flips the normals of shell or membrane elements of an orphan mesh or of two-dimensional
        geometric regions.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].flipNormal
        ```

        Note

        Check [PropertyPart.flipNormal on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partflipnormalpyc).

        Parameters:[¶](#abaqus.Property.PropertyPart.PropertyPart.flipNormal-parameters "Permalink to this headline")
        :   regions[¶](#abaqus.Property.PropertyPart.PropertyPart.flipNormal.regions "Permalink to this definition")
            :   A Region object specifying the region on which normals are flipped. For 3D parts, the
                region contains Face objects or two-dimensional triangle or quadrilateral Element
                objects. For axisymmetric parts, the region contains Edge objects or line Elements
                objects.

            referenceRegion=`''`[¶](#abaqus.Property.PropertyPart.PropertyPart.flipNormal.referenceRegion "Permalink to this definition")
            :   A two-dimensional element object whose normal is to be matched. If unspecified, all the
                normals associated with the given regions will be flipped. The **referenceRegion**
                argument is applicable only if the argument regions contain a sequence of quadrilateral
                or triangular elements.

    flipTangent(*[regions](#abaqus.Property.PropertyPart.PropertyPart.flipTangent.regions "abaqus.Property.PropertyPart.PropertyPart.flipTangent.regions (Python parameter) — A Region object specifying the region on which normals are flipped.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L381-L397)[¶](#abaqus.Property.PropertyPart.PropertyPart.flipTangent "Permalink to this definition")
    :   This method flips the tangents of beam or truss elements of an orphan mesh or of one-dimensional
        geometric regions.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].flipTangent
        ```

        Note

        Check [PropertyPart.flipTangent on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partfliptangentpyc).

        Parameters:[¶](#abaqus.Property.PropertyPart.PropertyPart.flipTangent-parameters "Permalink to this headline")
        :   regions[¶](#abaqus.Property.PropertyPart.PropertyPart.flipTangent.regions "Permalink to this definition")
            :   A Region object specifying the region on which normals are flipped. The region contains
                Edge objects or one-dimensional Element objects.

    unassignBeamSectionOrientation(*[index](#abaqus.Property.PropertyPart.PropertyPart.unassignBeamSectionOrientation.index "abaqus.Property.PropertyPart.PropertyPart.unassignBeamSectionOrientation.index (Python parameter) — An Int specifying the number of the beam section orientation assignment to be deleted.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L399-L413)[¶](#abaqus.Property.PropertyPart.PropertyPart.unassignBeamSectionOrientation "Permalink to this definition")
    :   This method deletes a beam section orientation assignment.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].unassignBeamSectionOrientation
        ```

        Note

        Check [PropertyPart.unassignBeamSectionOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partunassignbeamsectionorientationpyc).

        Parameters:[¶](#abaqus.Property.PropertyPart.PropertyPart.unassignBeamSectionOrientation-parameters "Permalink to this headline")
        :   index[¶](#abaqus.Property.PropertyPart.PropertyPart.unassignBeamSectionOrientation.index "Permalink to this definition")
            :   An Int specifying the number of the beam section orientation assignment to be deleted.

    unassignMaterialOrientation(*[index](#abaqus.Property.PropertyPart.PropertyPart.unassignMaterialOrientation.index "abaqus.Property.PropertyPart.PropertyPart.unassignMaterialOrientation.index (Python parameter) — An Int specifying the number of the material assignment to be deleted.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L415-L429)[¶](#abaqus.Property.PropertyPart.PropertyPart.unassignMaterialOrientation "Permalink to this definition")
    :   This method deletes a material orientation assignment.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].unassignMaterialOrientation
        ```

        Note

        Check [PropertyPart.unassignMaterialOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partunassignmaterialorientationpyc).

        Parameters:[¶](#abaqus.Property.PropertyPart.PropertyPart.unassignMaterialOrientation-parameters "Permalink to this headline")
        :   index[¶](#abaqus.Property.PropertyPart.PropertyPart.unassignMaterialOrientation.index "Permalink to this definition")
            :   An Int specifying the number of the material assignment to be deleted.

    unassignRebarOrientation(*[index](#abaqus.Property.PropertyPart.PropertyPart.unassignRebarOrientation.index "abaqus.Property.PropertyPart.PropertyPart.unassignRebarOrientation.index (Python parameter) — An Int specifying the number of the rebar reference orientation assignment to be deleted.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L431-L446)[¶](#abaqus.Property.PropertyPart.PropertyPart.unassignRebarOrientation "Permalink to this definition")
    :   This method deletes a rebar orientation assignment.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].unassignRebarOrientation
        ```

        Note

        Check [PropertyPart.unassignRebarOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-partpyc.htm?contextscope=all#simaker-partunassignrebarorientationpyc).

        Parameters:[¶](#abaqus.Property.PropertyPart.PropertyPart.unassignRebarOrientation-parameters "Permalink to this headline")
        :   index[¶](#abaqus.Property.PropertyPart.PropertyPart.unassignRebarOrientation.index "Permalink to this definition")
            :   An Int specifying the number of the rebar reference orientation assignment to be
                deleted.

## Other Classes[¶](#other-classes "Permalink to this heading")

*class* CompositeLayup(*[name](#abaqus.Property.PropertyPart.CompositeLayup "abaqus.Property.PropertyPart.CompositeLayup.__init__.name (Python parameter)")*, *[description](#abaqus.Property.PropertyPart.CompositeLayup "abaqus.Property.PropertyPart.CompositeLayup.__init__.description (Python parameter)")=`''`*, *[offsetType](#abaqus.Property.PropertyPart.CompositeLayup "abaqus.Property.PropertyPart.CompositeLayup.__init__.offsetType (Python parameter)")=`abaqusConstants.GLOBAL`*, *[offsetField](#abaqus.Property.PropertyPart.CompositeLayup "abaqus.Property.PropertyPart.CompositeLayup.__init__.offsetField (Python parameter)")=`''`*, *[offsetValues](#abaqus.Property.PropertyPart.CompositeLayup "abaqus.Property.PropertyPart.CompositeLayup.__init__.offsetValues (Python parameter)")=`0`*, *[elementType](#abaqus.Property.PropertyPart.CompositeLayup "abaqus.Property.PropertyPart.CompositeLayup.__init__.elementType (Python parameter)")=`abaqusConstants.SHELL`*, *[symmetric](#abaqus.Property.PropertyPart.CompositeLayup "abaqus.Property.PropertyPart.CompositeLayup.__init__.symmetric (Python parameter)")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L33-L643)[¶](#abaqus.Property.PropertyPart.CompositeLayup "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The CompositeLayup object is used to specify a composite layup on a part.

    Note

    This object can be accessed by:

    ```python
    import part
    mdb.models[name].parts[name].compositeLayups[i]
    ```

    The corresponding analysis keywords are:

    * SHELL SECTION
    * SHELL GENERAL SECTION
    * SOLID SECTION

    Note

    Check [CompositeLayup on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-compositelayuppyc.htm?contextscope=all).

    Member Details:

    CompositePly(*[thickness](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.thickness "abaqus.Property.PropertyPart.CompositeLayup.CompositePly.thickness (Python parameter) — A Float specifying the thickness of the section layer.")*, *[region](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.region "abaqus.Property.PropertyPart.CompositeLayup.CompositePly.region (Python parameter) — A Region object specifying the region to which the composite ply applies.")*, *[material](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.material "abaqus.Property.PropertyPart.CompositeLayup.CompositePly.material (Python parameter) — A String specifying the name of the material for the ply.")*, *[plyName](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.plyName "abaqus.Property.PropertyPart.CompositeLayup.CompositePly.plyName (Python parameter) — A String specifying the ply identifier for this section layer.")*, *[orientationType](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.orientationType "abaqus.Property.PropertyPart.CompositeLayup.CompositePly.orientationType (Python parameter) — A SymbolicConstant specifying the method used to define the relative orientation.")*, *[thicknessType](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.thicknessType "abaqus.Property.PropertyPart.CompositeLayup.CompositePly.thicknessType (Python parameter) — A SymbolicConstant specifying the method used to define the thickness.")*, *[orientationValue](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.orientationValue "abaqus.Property.PropertyPart.CompositeLayup.CompositePly.orientationValue (Python parameter) — A Float specifying the relative orientation of the section layer.")=`0`*, *[thicknessField](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.thicknessField "abaqus.Property.PropertyPart.CompositeLayup.CompositePly.thicknessField (Python parameter) — A String specifying the name of the AnalyticalField or DiscreteField object used to define the thickness of the shell elements and composite ply.")=`''`*, *[numIntPts](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.numIntPts "abaqus.Property.PropertyPart.CompositeLayup.CompositePly.numIntPts (Python parameter) — An Int specifying the number of integration points to be used through the section layer. This argument is valid only if preIntegrate = OFF.")=`3`*, *[axis](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.axis "abaqus.Property.PropertyPart.CompositeLayup.CompositePly.axis (Python parameter) — A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate system about which an additional rotation is applied.")=`abaqusConstants.AXIS_1`*, *[angle](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.angle "abaqus.Property.PropertyPart.CompositeLayup.CompositePly.angle (Python parameter) — A Float specifying the angle of the additional rotation.")=`0`*, *[additionalRotationType](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.additionalRotationType "abaqus.Property.PropertyPart.CompositeLayup.CompositePly.additionalRotationType (Python parameter) — A SymbolicConstant specifying the method used to describe the additional rotation when a valid orientation is specified.")=`abaqusConstants.ROTATION_NONE`*, *[orientation](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.orientation "abaqus.Property.PropertyPart.CompositeLayup.CompositePly.orientation (Python parameter) — The SymbolicConstant None or a DatumCsys object specifying a coordinate system reference for the relative orientation of this layer.")=`None`*, *[additionalRotationField](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.additionalRotationField "abaqus.Property.PropertyPart.CompositeLayup.CompositePly.additionalRotationField (Python parameter) — A String specifying the name of the field specifying the additional rotation.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L195-L303)[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly "Permalink to this definition")
    :   This method creates a CompositePly object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].CompositeLayup
        ```

        Note

        Check [CompositePly on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-compositeplypyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly-parameters "Permalink to this headline")
        :   thickness[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.thickness "Permalink to this definition")
            :   A Float specifying the thickness of the section layer.

            region[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.region "Permalink to this definition")
            :   A Region object specifying the region to which the composite ply applies.

            material[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.material "Permalink to this definition")
            :   A String specifying the name of the material for the ply.

            plyName[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.plyName "Permalink to this definition")
            :   A String specifying the ply identifier for this section layer. The default value is an
                empty string.

            orientationType[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.orientationType "Permalink to this definition")
            :   A SymbolicConstant specifying the method used to define the relative orientation. If
                **orientationType** = SPECIFY\_ORIENT the **orientationValue** argument is required. If
                **orientationType** = CSYS the **orientation** argument is required. Possible values are CSYS,
                SPECIFY\_ORIENT, ANGLE\_0, ANGLE\_45, ANGLE\_90, and ANGLE\_NEG45. The default value is
                ANGLE\_0.

            thicknessType[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.thicknessType "Permalink to this definition")
            :   A SymbolicConstant specifying the method used to define the thickness. If
                **thicknessType** = SPECIFY\_THICKNESS, the **thickness** argument is required. Possible values
                are SPECIFY\_THICKNESS, FIELD\_THICKNESS, and ANALYTICAL\_FIELD\_THICKNESS. The default
                value is SPECIFY\_THICKNESS.

            orientationValue=`0`[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.orientationValue "Permalink to this definition")
            :   A Float specifying the relative orientation of the section layer. The default value is
                0.0.

            thicknessField=`''`[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.thicknessField "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField or DiscreteField object used to
                define the thickness of the shell elements and composite ply. The **thicknessField**
                argument applies when **thicknessType** = ANALYTICAL\_FIELD or **thicknessType** = DISCRETE\_FIELD
                for shell elements and **thicknessType** = FIELD\_THICKNESS or
                **thicknessType** = ANALYTICAL\_FIELD\_THICKNESS for composite ply. The default value is an
                empty string.

            numIntPts=`3`[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.numIntPts "Permalink to this definition")
            :   An Int specifying the number of integration points to be used through the section layer.
                This argument is valid only if **preIntegrate** = OFF. The default value is 3.

            axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate
                system about which an additional rotation is applied. For shells this axis is also the
                shell normal. The **axis** argument applies only if a valid reference is provided for the
                **orientation**. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default value is
                AXIS\_1.

            angle=`0`[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.angle "Permalink to this definition")
            :   A Float specifying the angle of the additional rotation. The **angle** argument applies
                only if a valid reference is provided for the **orientation**. The default value is 0.0.

            additionalRotationType=`abaqusConstants.ROTATION_NONE`[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.additionalRotationType "Permalink to this definition")
            :   A SymbolicConstant specifying the method used to describe the additional rotation when a
                valid orientation is specified. Use **orientationType** = ANGLE\_0 and
                **additionalRotationType** = ROTATION\_FIELD to specify a discrete field of rotations for
                this CompositePly. Possible values are ROTATION\_NONE, ROTATION\_ANGLE, and
                ROTATION\_FIELD. The default value is ROTATION\_NONE.

            orientation=`None`[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.orientation "Permalink to this definition")
            :   The SymbolicConstant None or a DatumCsys object specifying a coordinate system reference
                for the relative orientation of this layer. The default value is None.

            additionalRotationField=`''`[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly.additionalRotationField "Permalink to this definition")
            :   A String specifying the name of the field specifying the additional rotation. The
                default value is an empty string.

        Returns:[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly-returns "Permalink to this headline")
        :   A CompositePly object.

        Return type:[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly-return-type "Permalink to this headline")
        :   [`CompositePly`](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly "abaqus.Property.PropertyPart.CompositeLayup.CompositePly (Python method) — This method creates a CompositePly object.")

        Raises:[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositePly-raises "Permalink to this headline")
        :   [**AbaqusException**](../../kernel/utility.html#abaqus.UtilityAndView.AbaqusException.AbaqusException "abaqus.UtilityAndView.AbaqusException.AbaqusException (Python class) — Bases: Exception") –

    CompositeShellSection(*[name](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.name "abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.name (Python parameter) — A String specifying the repository key.")*, *[layup](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.layup "abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.layup (Python parameter) — A SectionLayerArray object specifying the shell cross-section.")*, *[symmetric](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.symmetric "abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.symmetric (Python parameter) — A Boolean specifying whether or not the layup should be made symmetric by the analysis. The default value is OFF.")=`0`*, *[thicknessType](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.thicknessType "abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.thicknessType (Python parameter) — A SymbolicConstant specifying the distribution used for defining the thickness of the elements.")=`abaqusConstants.UNIFORM`*, *[preIntegrate](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.preIntegrate "abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.preIntegrate (Python parameter) — A Boolean specifying whether the shell section properties are specified by the user prior to the analysis (ON) or integrated during the analysis (OFF).")=`0`*, *[poissonDefinition](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.poissonDefinition "abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.poissonDefinition (Python parameter) — A SymbolicConstant specifying whether to use the default value for the Poisson's ratio. Possible values are:DEFAULT, specifying that the default value for the Poisson's ratio is 0.5 in an Abaqus/Standard analysis and is obtained from the material definition in an Abaqus/Explicit analysis.VALUE, specifying that the Poisson's ratio used in the analysis is the value provided in poisson.The default value is DEFAULT.")=`abaqusConstants.DEFAULT`*, *[poisson](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.poisson "abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.poisson (Python parameter) — A Float specifying the Poisson's ratio.")=`0`*, *[integrationRule](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.integrationRule "abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.integrationRule (Python parameter) — A SymbolicConstant specifying the shell section integration rule.")=`abaqusConstants.SIMPSON`*, *[temperature](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.temperature "abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.temperature (Python parameter) — A SymbolicConstant specifying the mode used for temperature and field variable input across the section thickness.")=`abaqusConstants.GRADIENT`*, *[idealization](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.idealization "abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.idealization (Python parameter) — A SymbolicConstant specifying the mechanical idealization used for the section calculations.")=`abaqusConstants.NO_IDEALIZATION`*, *[nTemp](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.nTemp "abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.nTemp (Python parameter) — None or an Int specifying the number of temperature points to be input.")=`None`*, *[thicknessModulus](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.thicknessModulus "abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.thicknessModulus (Python parameter) — None or a Float specifying the effective thickness modulus.")=`None`*, *[useDensity](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.useDensity "abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.useDensity (Python parameter) — A Boolean specifying whether or not to use the value of density.")=`0`*, *[density](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.density "abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.density (Python parameter) — A Float specifying the value of density to apply to this section.")=`0`*, *[layupName](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.layupName "abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.layupName (Python parameter) — A String specifying the layup name for this section.")=`''`*, *[thicknessField](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.thicknessField "abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.thicknessField (Python parameter) — A String specifying the name of the AnalyticalField or DiscreteField object used to define the thickness of the shell elements.")=`''`*, *[nodalThicknessField](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.nodalThicknessField "abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.nodalThicknessField (Python parameter) — A String specifying the name of the AnalyticalField or DiscreteField object used to define the thickness of the shell elements at each node.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L305-L424)[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection "Permalink to this definition")
    :   This method creates a CompositeShellSection object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].CompositeLayup
        ```

        Note

        Check [CompositeShellSection on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-compositeshellsectionpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.name "Permalink to this definition")
            :   A String specifying the repository key.

            layup[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.layup "Permalink to this definition")
            :   A SectionLayerArray object specifying the shell cross-section.

            symmetric=`0`[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.symmetric "Permalink to this definition")
            :   A Boolean specifying whether or not the layup should be made symmetric by the analysis.
                The default value is OFF.

            thicknessType=`abaqusConstants.UNIFORM`[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.thicknessType "Permalink to this definition")
            :   A SymbolicConstant specifying the distribution used for defining the thickness of the
                elements. Possible values are UNIFORM, ANALYTICAL\_FIELD, DISCRETE\_FIELD,
                NODAL\_ANALYTICAL\_FIELD, and NODAL\_DISCRETE\_FIELD. The default value is UNIFORM.

            preIntegrate=`0`[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.preIntegrate "Permalink to this definition")
            :   A Boolean specifying whether the shell section properties are specified by the user
                prior to the analysis (ON) or integrated during the analysis (OFF). The default value is
                OFF.

            poissonDefinition=`abaqusConstants.DEFAULT`[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.poissonDefinition "Permalink to this definition")
            :   A SymbolicConstant specifying whether to use the default value for the Poisson’s ratio.
                Possible values are:DEFAULT, specifying that the default value for the Poisson’s ratio
                is 0.5 in an Abaqus/Standard analysis and is obtained from the material definition in an
                Abaqus/Explicit analysis.VALUE, specifying that the Poisson’s ratio used in the analysis
                is the value provided in **poisson**.The default value is DEFAULT.

            poisson=`0`[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.poisson "Permalink to this definition")
            :   A Float specifying the Poisson’s ratio. Possible values are −1.0 ≤ **poisson** ≤ 0.5.
                This argument is valid only when **poissonDefinition** = VALUE. The default value is 0.5.

            integrationRule=`abaqusConstants.SIMPSON`[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.integrationRule "Permalink to this definition")
            :   A SymbolicConstant specifying the shell section integration rule. Possible values are
                SIMPSON and GAUSS. The default value is SIMPSON.

            temperature=`abaqusConstants.GRADIENT`[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.temperature "Permalink to this definition")
            :   A SymbolicConstant specifying the mode used for temperature and field variable input
                across the section thickness. Possible values are GRADIENT and POINTWISE. The default
                value is GRADIENT.

            idealization=`abaqusConstants.NO_IDEALIZATION`[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.idealization "Permalink to this definition")
            :   A SymbolicConstant specifying the mechanical idealization used for the section
                calculations. This member is only applicable when **preIntegrate** is set to ON. Possible
                values are NO\_IDEALIZATION, SMEAR\_ALL\_LAYERS, MEMBRANE, and BENDING. The default value
                is NO\_IDEALIZATION.

            nTemp=`None`[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.nTemp "Permalink to this definition")
            :   None or an Int specifying the number of temperature points to be input. This argument is
                valid only when **temperature** = POINTWISE. The default value is None.

            thicknessModulus=`None`[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.thicknessModulus "Permalink to this definition")
            :   None or a Float specifying the effective thickness modulus. This argument is relevant
                only for continuum shells and must be used in conjunction with the argument **poisson**.
                The default value is None.

            useDensity=`0`[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.useDensity "Permalink to this definition")
            :   A Boolean specifying whether or not to use the value of **density**. The default value is
                OFF.

            density=`0`[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.density "Permalink to this definition")
            :   A Float specifying the value of density to apply to this section. The default value is
                0.0.

            layupName=`''`[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.layupName "Permalink to this definition")
            :   A String specifying the layup name for this section. The default value is an empty
                string.

            thicknessField=`''`[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.thicknessField "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField or DiscreteField object used to
                define the thickness of the shell elements. The **thicknessField** argument applies only
                when **thicknessType** = ANALYTICAL\_FIELD or **thicknessType** = DISCRETE\_FIELD. The default
                value is an empty string.

            nodalThicknessField=`''`[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection.nodalThicknessField "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField or DiscreteField object used to
                define the thickness of the shell elements at each node. The **nodalThicknessField**
                argument applies only when **thicknessType** = NODAL\_ANALYTICAL\_FIELD or
                **thicknessType** = NODAL\_DISCRETE\_FIELD. The default value is an empty string.

        Returns:[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection-returns "Permalink to this headline")
        :   A CompositeShellSection object.

        Return type:[¶](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection-return-type "Permalink to this headline")
        :   [`CompositeShellSection`](#abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection "abaqus.Property.PropertyPart.CompositeLayup.CompositeShellSection (Python method) — This method creates a CompositeShellSection object.")

    GeometryShellSection(*[nodalThicknessField](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.nodalThicknessField "abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.nodalThicknessField (Python parameter) — A String specifying the name of the AnalyticalField or DiscreteField object used to define the thickness of the shell elements at each node.")=`''`*, *[thicknessField](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.thicknessField "abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.thicknessField (Python parameter) — A String specifying the name of the AnalyticalField or DiscreteField object used to define the thickness of the shell elements.")=`''`*, *[thicknessType](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.thicknessType "abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.thicknessType (Python parameter) — A SymbolicConstant specifying the distribution used for defining the thickness of the elements.")=`abaqusConstants.UNIFORM`*, *[preIntegrate](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.preIntegrate "abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.preIntegrate (Python parameter) — A Boolean specifying whether the shell section properties are specified by the user prior to the analysis (ON) or integrated during the analysis (OFF).")=`0`*, *[poissonDefinition](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.poissonDefinition "abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.poissonDefinition (Python parameter) — A SymbolicConstant specifying whether to use the default value for the Poisson's ratio. Possible values are:DEFAULT, specifying that the default value for the Poisson's ratio is 0.5 in an Abaqus/Standard analysis and is obtained from the material definition in an Abaqus/Explicit analysis.VALUE, specifying that the Poisson's ratio used in the analysis is the value provided in poisson.The default value is DEFAULT.")=`abaqusConstants.DEFAULT`*, *[poisson](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.poisson "abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.poisson (Python parameter) — A Float specifying the Poisson's ratio.")=`0`*, *[integrationRule](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.integrationRule "abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.integrationRule (Python parameter) — A SymbolicConstant specifying the shell section integration rule.")=`abaqusConstants.SIMPSON`*, *[temperature](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.temperature "abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.temperature (Python parameter) — A SymbolicConstant specifying the mode used for temperature and field variable input across the section thickness.")=`abaqusConstants.GRADIENT`*, *[nTemp](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.nTemp "abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.nTemp (Python parameter) — None or an Int specifying the number of temperature points to be input.")=`None`*, *[thicknessModulus](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.thicknessModulus "abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.thicknessModulus (Python parameter) — None or a Float specifying the effective thickness modulus.")=`None`*, *[useDensity](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.useDensity "abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.useDensity (Python parameter) — A Boolean specifying whether or not to use the value of density.")=`0`*, *[density](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.density "abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.density (Python parameter) — A Float specifying the value of density to apply to this section.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L426-L520)[¶](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection "Permalink to this definition")
    :   This method creates a GeometryShellSection object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].CompositeLayup
        ```

        Note

        Check [GeometryShellSection on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-geometryshellsectionpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection-parameters "Permalink to this headline")
        :   nodalThicknessField=`''`[¶](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.nodalThicknessField "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField or DiscreteField object used to
                define the thickness of the shell elements at each node. The **nodalThicknessField**
                argument applies only when **thicknessType** = NODAL\_ANALYTICAL\_FIELD or
                **thicknessType** = NODAL\_DISCRETE\_FIELD. The default value is an empty string.

            thicknessField=`''`[¶](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.thicknessField "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField or DiscreteField object used to
                define the thickness of the shell elements. The **thicknessField** argument applies only
                when **thicknessType** = ANALYTICAL\_FIELD or **thicknessType** = DISCRETE\_FIELD. The default
                value is an empty string.

            thicknessType=`abaqusConstants.UNIFORM`[¶](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.thicknessType "Permalink to this definition")
            :   A SymbolicConstant specifying the distribution used for defining the thickness of the
                elements. Possible values are UNIFORM, ANALYTICAL\_FIELD, DISCRETE\_FIELD,
                NODAL\_ANALYTICAL\_FIELD, and NODAL\_DISCRETE\_FIELD. The default value is UNIFORM.

            preIntegrate=`0`[¶](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.preIntegrate "Permalink to this definition")
            :   A Boolean specifying whether the shell section properties are specified by the user
                prior to the analysis (ON) or integrated during the analysis (OFF). The default value is
                OFF.

            poissonDefinition=`abaqusConstants.DEFAULT`[¶](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.poissonDefinition "Permalink to this definition")
            :   A SymbolicConstant specifying whether to use the default value for the Poisson’s ratio.
                Possible values are:DEFAULT, specifying that the default value for the Poisson’s ratio
                is 0.5 in an Abaqus/Standard analysis and is obtained from the material definition in an
                Abaqus/Explicit analysis.VALUE, specifying that the Poisson’s ratio used in the analysis
                is the value provided in **poisson**.The default value is DEFAULT.

            poisson=`0`[¶](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.poisson "Permalink to this definition")
            :   A Float specifying the Poisson’s ratio. Possible values are −1.0 ≤ **poisson** ≤ 0.5.
                This argument is valid only when **poissonDefinition** = VALUE. The default value is 0.5.

            integrationRule=`abaqusConstants.SIMPSON`[¶](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.integrationRule "Permalink to this definition")
            :   A SymbolicConstant specifying the shell section integration rule. Possible values are
                SIMPSON and GAUSS. The default value is SIMPSON.

            temperature=`abaqusConstants.GRADIENT`[¶](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.temperature "Permalink to this definition")
            :   A SymbolicConstant specifying the mode used for temperature and field variable input
                across the section thickness. Possible values are GRADIENT and POINTWISE. The default
                value is GRADIENT.

            nTemp=`None`[¶](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.nTemp "Permalink to this definition")
            :   None or an Int specifying the number of temperature points to be input. This argument is
                valid only when **temperature** = POINTWISE. The default value is None.

            thicknessModulus=`None`[¶](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.thicknessModulus "Permalink to this definition")
            :   None or a Float specifying the effective thickness modulus. This argument is relevant
                only for continuum shells and must be used in conjunction with the argument **poisson**.
                The default value is None.

            useDensity=`0`[¶](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.useDensity "Permalink to this definition")
            :   A Boolean specifying whether or not to use the value of **density**. The default value is
                OFF.

            density=`0`[¶](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection.density "Permalink to this definition")
            :   A Float specifying the value of density to apply to this section. The default value is
                0.0.

        Returns:[¶](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection-returns "Permalink to this headline")
        :   A GeometryShellSection object.

        Return type:[¶](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection-return-type "Permalink to this headline")
        :   [`GeometryShellSection`](#abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection "abaqus.Property.PropertyPart.CompositeLayup.GeometryShellSection (Python method) — This method creates a GeometryShellSection object.")

    HomogeneousShellSection(*[name](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.name "abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.name (Python parameter) — A String specifying the repository key.")*, *[material](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.material "abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.material (Python parameter) — A String specifying the name of the section material.")*, *[thickness](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.thickness "abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.thickness (Python parameter) — A Float specifying the thickness of the section.")=`0`*, *[numIntPts](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.numIntPts "abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.numIntPts (Python parameter) — An Int specifying the number of integration points to be used through the section. Possible values are numIntPts > 0.")=`5`*, *[thicknessType](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.thicknessType "abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.thicknessType (Python parameter) — A SymbolicConstant specifying the distribution used for defining the thickness of the elements.")=`abaqusConstants.UNIFORM`*, *[preIntegrate](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.preIntegrate "abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.preIntegrate (Python parameter) — A Boolean specifying whether the shell section properties are specified by the user prior to the analysis (ON) or integrated during the analysis (OFF).")=`0`*, *[poissonDefinition](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.poissonDefinition "abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.poissonDefinition (Python parameter) — A SymbolicConstant specifying whether to use the default value for the Poisson's ratio. Possible values are:DEFAULT, specifying that the default value for the Poisson's ratio is 0.5 in an Abaqus/Standard analysis and is obtained from the material definition in an Abaqus/Explicit analysis.VALUE, specifying that the Poisson's ratio used in the analysis is the value provided in poisson.The default value is DEFAULT.")=`abaqusConstants.DEFAULT`*, *[poisson](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.poisson "abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.poisson (Python parameter) — A Float specifying the Poisson's ratio.")=`0`*, *[integrationRule](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.integrationRule "abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.integrationRule (Python parameter) — A SymbolicConstant specifying the shell section integration rule.")=`abaqusConstants.SIMPSON`*, *[temperature](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.temperature "abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.temperature (Python parameter) — A SymbolicConstant specifying the mode used for temperature and field variable input across the section thickness.")=`abaqusConstants.GRADIENT`*, *[idealization](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.idealization "abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.idealization (Python parameter) — A SymbolicConstant specifying the mechanical idealization used for the section calculations.")=`abaqusConstants.NO_IDEALIZATION`*, *[nTemp](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.nTemp "abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.nTemp (Python parameter) — None or an Int specifying the number of temperature points to be input.")=`None`*, *[thicknessModulus](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.thicknessModulus "abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.thicknessModulus (Python parameter) — None or a Float specifying the effective thickness modulus.")=`None`*, *[useDensity](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.useDensity "abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.useDensity (Python parameter) — A Boolean specifying whether or not to use the value of density.")=`0`*, *[density](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.density "abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.density (Python parameter) — A Float specifying the value of density to apply to this section.")=`0`*, *[thicknessField](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.thicknessField "abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.thicknessField (Python parameter) — A String specifying the name of the AnalyticalField or DiscreteField object used to define the thickness of the shell elements.")=`''`*, *[nodalThicknessField](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.nodalThicknessField "abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.nodalThicknessField (Python parameter) — A String specifying the name of the AnalyticalField or DiscreteField object used to define the thickness of the shell elements at each node.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L522-L643)[¶](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection "Permalink to this definition")
    :   This method creates a HomogeneousShellSection object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].CompositeLayup
        ```

        Note

        Check [HomogeneousShellSection on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-homogeneousshellsectionpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection-parameters "Permalink to this headline")
        :   name[¶](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.name "Permalink to this definition")
            :   A String specifying the repository key.

            material[¶](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.material "Permalink to this definition")
            :   A String specifying the name of the section material.

            thickness=`0`[¶](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.thickness "Permalink to this definition")
            :   A Float specifying the thickness of the section. The **thickness** argument applies only
                when **thicknessType** = UNIFORM. The default value is 0.0.

            numIntPts=`5`[¶](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.numIntPts "Permalink to this definition")
            :   An Int specifying the number of integration points to be used through the section.
                Possible values are **numIntPts** > 0. The default value is 5.To use the default settings
                of the analysis products, set **numIntPts** to 5 if **integrationRule** = SIMPSON or set
                **numIntPts** to 7 if **integrationRule** = GAUSS.

            thicknessType=`abaqusConstants.UNIFORM`[¶](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.thicknessType "Permalink to this definition")
            :   A SymbolicConstant specifying the distribution used for defining the thickness of the
                elements. Possible values are UNIFORM, ANALYTICAL\_FIELD, DISCRETE\_FIELD,
                NODAL\_ANALYTICAL\_FIELD, and NODAL\_DISCRETE\_FIELD. The default value is UNIFORM.

            preIntegrate=`0`[¶](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.preIntegrate "Permalink to this definition")
            :   A Boolean specifying whether the shell section properties are specified by the user
                prior to the analysis (ON) or integrated during the analysis (OFF). The default value is
                OFF.

            poissonDefinition=`abaqusConstants.DEFAULT`[¶](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.poissonDefinition "Permalink to this definition")
            :   A SymbolicConstant specifying whether to use the default value for the Poisson’s ratio.
                Possible values are:DEFAULT, specifying that the default value for the Poisson’s ratio
                is 0.5 in an Abaqus/Standard analysis and is obtained from the material definition in an
                Abaqus/Explicit analysis.VALUE, specifying that the Poisson’s ratio used in the analysis
                is the value provided in **poisson**.The default value is DEFAULT.

            poisson=`0`[¶](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.poisson "Permalink to this definition")
            :   A Float specifying the Poisson’s ratio. Possible values are −1.0 ≤ **poisson** ≤ 0.5.
                This argument is valid only when **poissonDefinition** = VALUE. The default value is 0.5.

            integrationRule=`abaqusConstants.SIMPSON`[¶](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.integrationRule "Permalink to this definition")
            :   A SymbolicConstant specifying the shell section integration rule. Possible values are
                SIMPSON and GAUSS. The default value is SIMPSON.

            temperature=`abaqusConstants.GRADIENT`[¶](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.temperature "Permalink to this definition")
            :   A SymbolicConstant specifying the mode used for temperature and field variable input
                across the section thickness. Possible values are GRADIENT and POINTWISE. The default
                value is GRADIENT.

            idealization=`abaqusConstants.NO_IDEALIZATION`[¶](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.idealization "Permalink to this definition")
            :   A SymbolicConstant specifying the mechanical idealization used for the section
                calculations. This member is only applicable when **preIntegrate** is set to ON. Possible
                values are NO\_IDEALIZATION, SMEAR\_ALL\_LAYERS, MEMBRANE, and BENDING. The default value
                is NO\_IDEALIZATION.

            nTemp=`None`[¶](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.nTemp "Permalink to this definition")
            :   None or an Int specifying the number of temperature points to be input. This argument is
                valid only when **temperature** = POINTWISE. The default value is None.

            thicknessModulus=`None`[¶](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.thicknessModulus "Permalink to this definition")
            :   None or a Float specifying the effective thickness modulus. This argument is relevant
                only for continuum shells and must be used in conjunction with the argument **poisson**.
                The default value is None.

            useDensity=`0`[¶](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.useDensity "Permalink to this definition")
            :   A Boolean specifying whether or not to use the value of **density**. The default value is
                OFF.

            density=`0`[¶](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.density "Permalink to this definition")
            :   A Float specifying the value of density to apply to this section. The default value is
                0.0.

            thicknessField=`''`[¶](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.thicknessField "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField or DiscreteField object used to
                define the thickness of the shell elements. The **thicknessField** argument applies only
                when **thicknessType** = ANALYTICAL\_FIELD or **thicknessType** = DISCRETE\_FIELD. The default
                value is an empty string.

            nodalThicknessField=`''`[¶](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection.nodalThicknessField "Permalink to this definition")
            :   A String specifying the name of the AnalyticalField or DiscreteField object used to
                define the thickness of the shell elements at each node. The **nodalThicknessField**
                argument applies only when **thicknessType** = NODAL\_ANALYTICAL\_FIELD or
                **thicknessType** = NODAL\_DISCRETE\_FIELD. The default value is an empty string.

        Returns:[¶](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection-returns "Permalink to this headline")
        :   A HomogeneousShellSection object.

        Return type:[¶](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection-return-type "Permalink to this headline")
        :   [`HomogeneousShellSection`](#abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection "abaqus.Property.PropertyPart.CompositeLayup.HomogeneousShellSection (Python method) — This method creates a HomogeneousShellSection object.")

    deletePlies()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L152-L155)[¶](#abaqus.Property.PropertyPart.CompositeLayup.deletePlies "Permalink to this definition")
    :   This method deletes all of the plies from a composite layup.

    description : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L62-L63)[¶](#abaqus.Property.PropertyPart.CompositeLayup.description "Permalink to this definition")
    :   A String specifying a description of the composite layup.

    elementType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'SHELL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L79-L81)[¶](#abaqus.Property.PropertyPart.CompositeLayup.elementType "Permalink to this definition")
    :   A SymbolicConstant specifying the type of element in the composite layup. Possible
        values are SHELL, CONTINUUM\_SHELL, and SOLID. The default value is SHELL.

    name : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py)[¶](#abaqus.Property.PropertyPart.CompositeLayup.name "Permalink to this definition")
    :   A String specifying the repository key.

    offsetField : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L71-L73)[¶](#abaqus.Property.PropertyPart.CompositeLayup.offsetField "Permalink to this definition")
    :   A String specifying The name of the field specifying the offset. This member is valid
        only if **elementType** = SHELL. The default value is an empty string.

    offsetType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'GLOBAL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L65-L69)[¶](#abaqus.Property.PropertyPart.CompositeLayup.offsetType "Permalink to this definition")
    :   A SymbolicConstant specifying the method used to define the shell offset. If
        **offsetType** = OFFSET\_FIELD the **offsetField** argument is required. This member is valid
        only if **elementType** = SHELL. Possible values are SINGLE\_VALUE, MIDDLE\_SURFACE,
        TOP\_SURFACE, BOTTOM\_SURFACE, OFFSET\_FIELD, and GLOBAL. The default value is GLOBAL.

    offsetValues : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L75-L77)[¶](#abaqus.Property.PropertyPart.CompositeLayup.offsetValues "Permalink to this definition")
    :   A Float specifying The offset of the shell section. This member is valid only if
        **elementType** = SHELL. The default value is 0.0.

    orientation : --is-rst--:py:class:`~abaqus.Property.MaterialOrientation.MaterialOrientation` = `<abaqus.Property.MaterialOrientation.MaterialOrientation object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L53-L54)[¶](#abaqus.Property.PropertyPart.CompositeLayup.orientation "Permalink to this definition")
    :   A MaterialOrientation object.

    plies : --is-rst--:py:class:`~typing.List`\[:py:class:`~abaqus.Property.CompositePly.CompositePly`] = `[]`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L56-L57)[¶](#abaqus.Property.PropertyPart.CompositeLayup.plies "Permalink to this definition")
    :   A CompositePlyArray object specifying the plies that make up this composite layup.

    resume()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L147-L150)[¶](#abaqus.Property.PropertyPart.CompositeLayup.resume "Permalink to this definition")
    :   This method resumes a composite layup that was previously suppressed.

    section : --is-rst--:py:class:`~abaqus.Section.GeometryShellSection.GeometryShellSection` = `<abaqus.Section.GeometryShellSection.GeometryShellSection object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L50-L51)[¶](#abaqus.Property.PropertyPart.CompositeLayup.section "Permalink to this definition")
    :   A GeometryShellSection object.

    setValues(*[description](#abaqus.Property.PropertyPart.CompositeLayup.setValues.description "abaqus.Property.PropertyPart.CompositeLayup.setValues.description (Python parameter) — A String specifying a description of the composite layup.")=`''`*, *[offsetType](#abaqus.Property.PropertyPart.CompositeLayup.setValues.offsetType "abaqus.Property.PropertyPart.CompositeLayup.setValues.offsetType (Python parameter) — A SymbolicConstant specifying the method used to define the shell offset.")=`abaqusConstants.GLOBAL`*, *[offsetField](#abaqus.Property.PropertyPart.CompositeLayup.setValues.offsetField "abaqus.Property.PropertyPart.CompositeLayup.setValues.offsetField (Python parameter) — A String specifying The name of the field specifying the offset.")=`''`*, *[offsetValues](#abaqus.Property.PropertyPart.CompositeLayup.setValues.offsetValues "abaqus.Property.PropertyPart.CompositeLayup.setValues.offsetValues (Python parameter) — A Float specifying The offset of the shell section.")=`0`*, *[elementType](#abaqus.Property.PropertyPart.CompositeLayup.setValues.elementType "abaqus.Property.PropertyPart.CompositeLayup.setValues.elementType (Python parameter) — A SymbolicConstant specifying the type of element in the composite layup.")=`abaqusConstants.SHELL`*, *[symmetric](#abaqus.Property.PropertyPart.CompositeLayup.setValues.symmetric "abaqus.Property.PropertyPart.CompositeLayup.setValues.symmetric (Python parameter) — A Boolean specifying whether or not the layup should be made symmetric by the analysis. The default value is OFF.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L157-L193)[¶](#abaqus.Property.PropertyPart.CompositeLayup.setValues "Permalink to this definition")
    :   This method modifies the CompositeLayup object.

        Note

        Check [CompositeLayup.setValues on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-compositelayuppyc.htm?contextscope=all#simaker-compositelayupsetvaluespyc).

        Parameters:[¶](#abaqus.Property.PropertyPart.CompositeLayup.setValues-parameters "Permalink to this headline")
        :   description=`''`[¶](#abaqus.Property.PropertyPart.CompositeLayup.setValues.description "Permalink to this definition")
            :   A String specifying a description of the composite layup.

            offsetType=`abaqusConstants.GLOBAL`[¶](#abaqus.Property.PropertyPart.CompositeLayup.setValues.offsetType "Permalink to this definition")
            :   A SymbolicConstant specifying the method used to define the shell offset. If
                **offsetType** = OFFSET\_FIELD the **offsetField** argument is required. This member is valid
                only if **elementType** = SHELL. Possible values are SINGLE\_VALUE, MIDDLE\_SURFACE,
                TOP\_SURFACE, BOTTOM\_SURFACE, OFFSET\_FIELD, and GLOBAL. The default value is GLOBAL.

            offsetField=`''`[¶](#abaqus.Property.PropertyPart.CompositeLayup.setValues.offsetField "Permalink to this definition")
            :   A String specifying The name of the field specifying the offset. This member is valid
                only if **elementType** = SHELL. The default value is an empty string.

            offsetValues=`0`[¶](#abaqus.Property.PropertyPart.CompositeLayup.setValues.offsetValues "Permalink to this definition")
            :   A Float specifying The offset of the shell section. This member is valid only if
                **elementType** = SHELL. The default value is 0.0.

            elementType=`abaqusConstants.SHELL`[¶](#abaqus.Property.PropertyPart.CompositeLayup.setValues.elementType "Permalink to this definition")
            :   A SymbolicConstant specifying the type of element in the composite layup. Possible
                values are SHELL, CONTINUUM\_SHELL, and SOLID. The default value is SHELL.

            symmetric=`0`[¶](#abaqus.Property.PropertyPart.CompositeLayup.setValues.symmetric "Permalink to this definition")
            :   A Boolean specifying whether or not the layup should be made symmetric by the analysis.
                The default value is OFF.

    suppress()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L142-L145)[¶](#abaqus.Property.PropertyPart.CompositeLayup.suppress "Permalink to this definition")
    :   This method suppresses a composite layup.

    symmetric : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L83-L85)[¶](#abaqus.Property.PropertyPart.CompositeLayup.symmetric "Permalink to this definition")
    :   A Boolean specifying whether or not the layup should be made symmetric by the analysis.
        The default value is OFF.

*class* CompositePly(*[thickness](#abaqus.Property.CompositePlyArray.CompositePly "abaqus.Property.CompositePlyArray.CompositePly.__init__.thickness (Python parameter)")*, *[region](#abaqus.Property.CompositePlyArray.CompositePly "abaqus.Property.CompositePlyArray.CompositePly.__init__.region (Python parameter)")*, *[material](#abaqus.Property.CompositePlyArray.CompositePly "abaqus.Property.CompositePlyArray.CompositePly.__init__.material (Python parameter)")*, *[plyName](#abaqus.Property.CompositePlyArray.CompositePly "abaqus.Property.CompositePlyArray.CompositePly.__init__.plyName (Python parameter)")*, *[orientationType](#abaqus.Property.CompositePlyArray.CompositePly "abaqus.Property.CompositePlyArray.CompositePly.__init__.orientationType (Python parameter)")*, *[thicknessType](#abaqus.Property.CompositePlyArray.CompositePly "abaqus.Property.CompositePlyArray.CompositePly.__init__.thicknessType (Python parameter)")*, *[orientationValue](#abaqus.Property.CompositePlyArray.CompositePly "abaqus.Property.CompositePlyArray.CompositePly.__init__.orientationValue (Python parameter)")=`0`*, *[thicknessField](#abaqus.Property.CompositePlyArray.CompositePly "abaqus.Property.CompositePlyArray.CompositePly.__init__.thicknessField (Python parameter)")=`''`*, *[numIntPts](#abaqus.Property.CompositePlyArray.CompositePly "abaqus.Property.CompositePlyArray.CompositePly.__init__.numIntPts (Python parameter)")=`3`*, *[axis](#abaqus.Property.CompositePlyArray.CompositePly "abaqus.Property.CompositePlyArray.CompositePly.__init__.axis (Python parameter)")=`abaqusConstants.AXIS_1`*, *[angle](#abaqus.Property.CompositePlyArray.CompositePly "abaqus.Property.CompositePlyArray.CompositePly.__init__.angle (Python parameter)")=`0`*, *[additionalRotationType](#abaqus.Property.CompositePlyArray.CompositePly "abaqus.Property.CompositePlyArray.CompositePly.__init__.additionalRotationType (Python parameter)")=`abaqusConstants.ROTATION_NONE`*, *[orientation](#abaqus.Property.CompositePlyArray.CompositePly "abaqus.Property.CompositePlyArray.CompositePly.__init__.orientation (Python parameter)")=`None`*, *[additionalRotationField](#abaqus.Property.CompositePlyArray.CompositePly "abaqus.Property.CompositePlyArray.CompositePly.__init__.additionalRotationField (Python parameter)")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/CompositePlyArray.py#L12-L192)[¶](#abaqus.Property.CompositePlyArray.CompositePly "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The CompositePly object defines the material layers in a composite layup.

    Note

    This object can be accessed by:

    ```python
    import section
    mdb.models[name].parts[name].compositeLayups[i].plies[i]
    ```

    Note

    Check [CompositePly on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-compositeplypyc.htm?contextscope=all).

    Member Details:

    additionalRotationField : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/CompositePlyArray.py#L91-L93)[¶](#abaqus.Property.CompositePlyArray.CompositePly.additionalRotationField "Permalink to this definition")
    :   A String specifying the name of the field specifying the additional rotation. The
        default value is an empty string.

    additionalRotationType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'ROTATION_NONE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/CompositePlyArray.py#L80-L85)[¶](#abaqus.Property.CompositePlyArray.CompositePly.additionalRotationType "Permalink to this definition")
    :   A SymbolicConstant specifying the method used to describe the additional rotation when a
        valid orientation is specified. Use **orientationType** = ANGLE\_0 and
        **additionalRotationType** = ROTATION\_FIELD to specify a discrete field of rotations for
        this CompositePly. Possible values are ROTATION\_NONE, ROTATION\_ANGLE, and
        ROTATION\_FIELD. The default value is ROTATION\_NONE.

    angle : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/CompositePlyArray.py#L76-L78)[¶](#abaqus.Property.CompositePlyArray.CompositePly.angle "Permalink to this definition")
    :   A Float specifying the angle of the additional rotation. The **angle** argument applies
        only if a valid reference is provided for the **orientation**. The default value is 0.0.

    axis : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'AXIS_1'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/CompositePlyArray.py#L69-L74)[¶](#abaqus.Property.CompositePlyArray.CompositePly.axis "Permalink to this definition")
    :   A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate
        system about which an additional rotation is applied. For shells this axis is also the
        shell normal. The **axis** argument applies only if a valid reference is provided for the
        **orientation**. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default value is
        AXIS\_1.

    material : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/CompositePlyArray.py)[¶](#abaqus.Property.CompositePlyArray.CompositePly.material "Permalink to this definition")
    :   A String specifying the name of the material for the ply.

    numIntPts : --is-rst--:py:class:`int` = `3`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/CompositePlyArray.py#L65-L67)[¶](#abaqus.Property.CompositePlyArray.CompositePly.numIntPts "Permalink to this definition")
    :   An Int specifying the number of integration points to be used through the section layer.
        This argument is valid only if **preIntegrate** = OFF. The default value is 3.

    orientation : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/CompositePlyArray.py)[¶](#abaqus.Property.CompositePlyArray.CompositePly.orientation "Permalink to this definition")
    :   The SymbolicConstant None or a DatumCsys object specifying a coordinate system reference
        for the relative orientation of this layer. The default value is None.

    orientationType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/CompositePlyArray.py)[¶](#abaqus.Property.CompositePlyArray.CompositePly.orientationType "Permalink to this definition")
    :   A SymbolicConstant specifying the method used to define the relative orientation. If
        **orientationType** = SPECIFY\_ORIENT the **orientationValue** argument is required. If
        **orientationType** = CSYS the **orientation** argument is required. Possible values are CSYS,
        SPECIFY\_ORIENT, ANGLE\_0, ANGLE\_45, ANGLE\_90, and ANGLE\_NEG45. The default value is
        ANGLE\_0.

    orientationValue : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/CompositePlyArray.py#L52-L54)[¶](#abaqus.Property.CompositePlyArray.CompositePly.orientationValue "Permalink to this definition")
    :   A Float specifying the relative orientation of the section layer. The default value is
        0.0.

    plyName : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/CompositePlyArray.py)[¶](#abaqus.Property.CompositePlyArray.CompositePly.plyName "Permalink to this definition")
    :   A String specifying the ply identifier for this section layer. The default value is an
        empty string.

    region : --is-rst--:py:class:`~abaqus.Region.Region.Region`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/CompositePlyArray.py)[¶](#abaqus.Property.CompositePlyArray.CompositePly.region "Permalink to this definition")
    :   A Region object specifying the region to which the composite ply applies.

    thickness : --is-rst--:py:class:`float`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/CompositePlyArray.py)[¶](#abaqus.Property.CompositePlyArray.CompositePly.thickness "Permalink to this definition")
    :   A Float specifying the thickness of the section layer.

    thicknessField : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/CompositePlyArray.py#L48-L50)[¶](#abaqus.Property.CompositePlyArray.CompositePly.thicknessField "Permalink to this definition")
    :   A String specifying the name of the AnalyticalField or DiscreteField object used to
        define the thickness of the shell elements. The thicknessField argument applies only
        when thicknessType=ANALYTICAL\_FIELD or thicknessType=DISCRETE\_FIELD. The default
        value is an empty string.

        ..versionchanged:: 2021
        :   Update docs for ANALYTICAL\_FIELD\_THICKNESS

    thicknessType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/CompositePlyArray.py)[¶](#abaqus.Property.CompositePlyArray.CompositePly.thicknessType "Permalink to this definition")
    :   A SymbolicConstant specifying the method used to define the thickness. If
        thicknessType=SPECIFY\_THICKNESS, the thickness argument is required.
        Possible values are SPECIFY\_THICKNESS and FIELD\_THICKNESS. The default
        value is SPECIFY\_THICKNESS.

        ..versionchanged:: 2021
        :   Add possible value ANALYTICAL\_FIELD\_THICKNESS.

*class* MaterialOrientation(*[region](#abaqus.Property.PropertyPart.MaterialOrientation "abaqus.Property.PropertyPart.MaterialOrientation.__init__.region (Python parameter)")*, *[localCsys](#abaqus.Property.PropertyPart.MaterialOrientation "abaqus.Property.PropertyPart.MaterialOrientation.__init__.localCsys (Python parameter)")=`None`*, *[axis](#abaqus.Property.PropertyPart.MaterialOrientation "abaqus.Property.PropertyPart.MaterialOrientation.__init__.axis (Python parameter)")=`abaqusConstants.AXIS_1`*, *[angle](#abaqus.Property.PropertyPart.MaterialOrientation "abaqus.Property.PropertyPart.MaterialOrientation.__init__.angle (Python parameter)")=`0`*, *[stackDirection](#abaqus.Property.PropertyPart.MaterialOrientation "abaqus.Property.PropertyPart.MaterialOrientation.__init__.stackDirection (Python parameter)")=`abaqusConstants.STACK_3`*, *[fieldName](#abaqus.Property.PropertyPart.MaterialOrientation "abaqus.Property.PropertyPart.MaterialOrientation.__init__.fieldName (Python parameter)")=`''`*, *[orientationType](#abaqus.Property.PropertyPart.MaterialOrientation "abaqus.Property.PropertyPart.MaterialOrientation.__init__.orientationType (Python parameter)")=`abaqusConstants.GLOBAL`*, *[normalAxisDirection](#abaqus.Property.PropertyPart.MaterialOrientation "abaqus.Property.PropertyPart.MaterialOrientation.__init__.normalAxisDirection (Python parameter)")=`abaqusConstants.AXIS_3`*, *[normalAxisDefinition](#abaqus.Property.PropertyPart.MaterialOrientation "abaqus.Property.PropertyPart.MaterialOrientation.__init__.normalAxisDefinition (Python parameter)")=`abaqusConstants.NORMAL_VECTOR`*, *[normalAxisRegion](#abaqus.Property.PropertyPart.MaterialOrientation "abaqus.Property.PropertyPart.MaterialOrientation.__init__.normalAxisRegion (Python parameter)")=`None`*, *[normalAxisDatum](#abaqus.Property.PropertyPart.MaterialOrientation "abaqus.Property.PropertyPart.MaterialOrientation.__init__.normalAxisDatum (Python parameter)")=`None`*, *[flipNormalDirection](#abaqus.Property.PropertyPart.MaterialOrientation "abaqus.Property.PropertyPart.MaterialOrientation.__init__.flipNormalDirection (Python parameter)")=`0`*, *[normalAxisVector](#abaqus.Property.PropertyPart.MaterialOrientation "abaqus.Property.PropertyPart.MaterialOrientation.__init__.normalAxisVector (Python parameter)")=`()`*, *[primaryAxisDirection](#abaqus.Property.PropertyPart.MaterialOrientation "abaqus.Property.PropertyPart.MaterialOrientation.__init__.primaryAxisDirection (Python parameter)")=`abaqusConstants.AXIS_1`*, *[primaryAxisDefinition](#abaqus.Property.PropertyPart.MaterialOrientation "abaqus.Property.PropertyPart.MaterialOrientation.__init__.primaryAxisDefinition (Python parameter)")=`abaqusConstants.PRIMARY_VECTOR`*, *[primaryAxisRegion](#abaqus.Property.PropertyPart.MaterialOrientation "abaqus.Property.PropertyPart.MaterialOrientation.__init__.primaryAxisRegion (Python parameter)")=`None`*, *[primaryAxisDatum](#abaqus.Property.PropertyPart.MaterialOrientation "abaqus.Property.PropertyPart.MaterialOrientation.__init__.primaryAxisDatum (Python parameter)")=`None`*, *[flipPrimaryDirection](#abaqus.Property.PropertyPart.MaterialOrientation "abaqus.Property.PropertyPart.MaterialOrientation.__init__.flipPrimaryDirection (Python parameter)")=`0`*, *[primaryAxisVector](#abaqus.Property.PropertyPart.MaterialOrientation "abaqus.Property.PropertyPart.MaterialOrientation.__init__.primaryAxisVector (Python parameter)")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L27-L356)[¶](#abaqus.Property.PropertyPart.MaterialOrientation "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The MaterialOrientation object represents the orientation of the material properties and composite
    layups.

    Note

    This object can be accessed by:

    ```python
    import section
    mdb.models[name].parts[name].compositeLayups[i].orientation
    mdb.models[name].parts[name].materialOrientations[i]
    import odbAccess
    session.odbs[name].parts[name].materialOrientations[i]
    session.odbs[name].rootAssembly.instances[name].materialOrientations[i]
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.materialOrientations[i]
    ```

    Note

    Check [MaterialOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-materialorientationpyc.htm?contextscope=all).

    Member Details:

    ReferenceOrientation(*[localCsys](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.localCsys "abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.localCsys (Python parameter) — A DatumCsys object specifying the local coordinate system or None, describing the material orientation for the given region.")=`None`*, *[axis](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.axis "abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.axis (Python parameter) — A SymbolicConstant specifying the axis of a datum coordinate system about which an additional rotation is applied.")=`abaqusConstants.AXIS_1`*, *[angle](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.angle "abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.angle (Python parameter) — A Float specifying the angle of the additional rotation (if accessed from the ODB instead of the MDB, it will be a string instead of a float).")=`0`*, *[stackDirection](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.stackDirection "abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.stackDirection (Python parameter) — A SymbolicConstant specifying the stack or thickness direction.")=`abaqusConstants.STACK_3`*, *[fieldName](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.fieldName "abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.fieldName (Python parameter) — A String specifying the name of the DiscreteField object specifying the orientation.")=`''`*, *[orientationType](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.orientationType "abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.orientationType (Python parameter) — A SymbolicConstant specifying the method used to define the material orientation.")=`abaqusConstants.GLOBAL`*, *[additionalRotationField](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.additionalRotationField "abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.additionalRotationField (Python parameter) — A String specifying the name of the DiscreteField object specifying the additional rotation.")=`''`*, *[additionalRotationType](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.additionalRotationType "abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.additionalRotationType (Python parameter) — A SymbolicConstant specifying the method used to describe the additional rotation when a valid orientation is specified.")=`abaqusConstants.ROTATION_NONE`*, *[normalAxisDirection](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.normalAxisDirection "abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.normalAxisDirection (Python parameter) — A SymbolicConstant specifying the axis that is defined by the normal axis direction for a discrete orientation.")=`abaqusConstants.AXIS_3`*, *[normalAxisDefinition](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.normalAxisDefinition "abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.normalAxisDefinition (Python parameter) — A SymbolicConstant specifying the method used to define the normal axis direction for a discrete orientation.")=`abaqusConstants.VECTOR`*, *[normalAxisRegion](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.normalAxisRegion "abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.normalAxisRegion (Python parameter) — A Surface object specifying a region whose geometric normals define the normal axis for the discrete orientation.")=`None`*, *[normalAxisDatum](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.normalAxisDatum "abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.normalAxisDatum (Python parameter) — A DatumAxis object specifying the Datum Axis or None, describing the normal axis direction for the discrete orientation.")=`None`*, *[flipNormalDirection](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.flipNormalDirection "abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.flipNormalDirection (Python parameter) — A Boolean specifying the flag to reverse the direction of the defined normal axis direction.")=`0`*, *[normalAxisVector](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.normalAxisVector "abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.normalAxisVector (Python parameter) — A sequence of Floats specifying the vector that defines the direction of the normal axis of the discrete orientation.")=`()`*, *[primaryAxisDirection](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.primaryAxisDirection "abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.primaryAxisDirection (Python parameter) — A SymbolicConstant specifying the axis that is defined by the primary axis direction for a discrete orientation.")=`abaqusConstants.AXIS_1`*, *[primaryAxisDefinition](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.primaryAxisDefinition "abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.primaryAxisDefinition (Python parameter) — A SymbolicConstant specifying the method used to define the primary axis direction for a discrete orientation.")=`abaqusConstants.VECTOR`*, *[primaryAxisRegion](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.primaryAxisRegion "abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.primaryAxisRegion (Python parameter) — A Set object specifying a region whose geometric tangents define the primary axis for the discrete orientation.")=`None`*, *[primaryAxisDatum](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.primaryAxisDatum "abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.primaryAxisDatum (Python parameter) — A DatumAxis object specifying the Datum Axis or None, describing the primary axis direction for the discrete orientation.")=`None`*, *[flipPrimaryDirection](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.flipPrimaryDirection "abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.flipPrimaryDirection (Python parameter) — A Boolean specifying the flag to reverse the direction of the defined primary axis direction.")=`0`*, *[primaryAxisVector](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.primaryAxisVector "abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.primaryAxisVector (Python parameter) — A sequence of Floats specifying the vector that defines the direction of the primary axis of the discrete orientation.")=`()`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L242-L351)[¶](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation "Permalink to this definition")
    :   This method creates a MaterialOrientation object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].MaterialOrientation
        ```

        Note

        Check [ReferenceOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-referenceorientationpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation-parameters "Permalink to this headline")
        :   localCsys=`None`[¶](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.localCsys "Permalink to this definition")
            :   A DatumCsys object specifying the local coordinate system or None, describing the
                material orientation for the given region. In the ODB, this member was previously
                accessible using “csys,” but support has now been added for localCsys and the csys
                member will be deprecated.

            axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.axis "Permalink to this definition")
            :   A SymbolicConstant specifying the axis of a datum coordinate system about which an
                additional rotation is applied. For shells this axis is also the shell normal. Possible
                values are AXIS\_1, AXIS\_2, and AXIS\_3. The default value is AXIS\_1.

            angle=`0`[¶](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.angle "Permalink to this definition")
            :   A Float specifying the angle of the additional rotation (if accessed from the ODB
                instead of the MDB, it will be a string instead of a float). The default value is 0.0.

            stackDirection=`abaqusConstants.STACK_3`[¶](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.stackDirection "Permalink to this definition")
            :   A SymbolicConstant specifying the stack or thickness direction. Possible values are
                STACK\_1, STACK\_2, STACK\_3, and STACK\_ORIENTATION. The default value is STACK\_3.

            fieldName=`''`[¶](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.fieldName "Permalink to this definition")
            :   A String specifying the name of the DiscreteField object specifying the orientation. The
                default value is an empty string.

            orientationType=`abaqusConstants.GLOBAL`[¶](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.orientationType "Permalink to this definition")
            :   A SymbolicConstant specifying the method used to define the material orientation. If
                **orientationType** = SYSTEM, the **region** and **localCsys** arguments are required. If
                **orientationType** = FIELD, the **fieldName** argument is required. Possible values are
                GLOBAL, SYSTEM, FIELD, DISCRETE, and USER. The default value is GLOBAL.

            additionalRotationField=`''`[¶](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.additionalRotationField "Permalink to this definition")
            :   A String specifying the name of the DiscreteField object specifying the additional
                rotation. The default value is an empty string.

            additionalRotationType=`abaqusConstants.ROTATION_NONE`[¶](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.additionalRotationType "Permalink to this definition")
            :   A SymbolicConstant specifying the method used to describe the additional rotation when a
                valid orientation is specified. Possible values are ROTATION\_NONE, ROTATION\_ANGLE, and
                ROTATION\_FIELD. The default value is ROTATION\_NONE.

            normalAxisDirection=`abaqusConstants.AXIS_3`[¶](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.normalAxisDirection "Permalink to this definition")
            :   A SymbolicConstant specifying the axis that is defined by the normal axis direction for
                a discrete orientation. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default
                value is AXIS\_3.

            normalAxisDefinition=`abaqusConstants.VECTOR`[¶](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.normalAxisDefinition "Permalink to this definition")
            :   A SymbolicConstant specifying the method used to define the normal axis direction for a
                discrete orientation. Possible values are SURFACE, DATUM, and VECTOR. The default value
                is VECTOR.

            normalAxisRegion=`None`[¶](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.normalAxisRegion "Permalink to this definition")
            :   A Surface object specifying a region whose geometric normals define the normal axis for
                the discrete orientation.

            normalAxisDatum=`None`[¶](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.normalAxisDatum "Permalink to this definition")
            :   A DatumAxis object specifying the Datum Axis or None, describing the normal axis
                direction for the discrete orientation.

            flipNormalDirection=`0`[¶](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.flipNormalDirection "Permalink to this definition")
            :   A Boolean specifying the flag to reverse the direction of the defined normal axis
                direction. The default value is OFF.

            normalAxisVector=`()`[¶](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.normalAxisVector "Permalink to this definition")
            :   A sequence of Floats specifying the vector that defines the direction of the normal axis
                of the discrete orientation.

            primaryAxisDirection=`abaqusConstants.AXIS_1`[¶](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.primaryAxisDirection "Permalink to this definition")
            :   A SymbolicConstant specifying the axis that is defined by the primary axis direction for
                a discrete orientation. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default
                value is AXIS\_1.

            primaryAxisDefinition=`abaqusConstants.VECTOR`[¶](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.primaryAxisDefinition "Permalink to this definition")
            :   A SymbolicConstant specifying the method used to define the primary axis direction for a
                discrete orientation. Possible values are EDGE, DATUM, and VECTOR. The default value is
                VECTOR.

            primaryAxisRegion=`None`[¶](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.primaryAxisRegion "Permalink to this definition")
            :   A Set object specifying a region whose geometric tangents define the primary axis for
                the discrete orientation.

            primaryAxisDatum=`None`[¶](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.primaryAxisDatum "Permalink to this definition")
            :   A DatumAxis object specifying the Datum Axis or None, describing the primary axis
                direction for the discrete orientation.

            flipPrimaryDirection=`0`[¶](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.flipPrimaryDirection "Permalink to this definition")
            :   A Boolean specifying the flag to reverse the direction of the defined primary axis
                direction. The default value is OFF.

            primaryAxisVector=`()`[¶](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation.primaryAxisVector "Permalink to this definition")
            :   A sequence of Floats specifying the vector that defines the direction of the primary
                axis of the discrete orientation.

        Returns:[¶](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation-returns "Permalink to this headline")
        :   A MaterialOrientation object.

        Return type:[¶](#abaqus.Property.PropertyPart.MaterialOrientation.ReferenceOrientation-return-type "Permalink to this headline")
        :   [`MaterialOrientation`](#abaqus.Property.PropertyPart.MaterialOrientation "abaqus.Property.PropertyPart.MaterialOrientation (Python class) — Bases: object")

    additionalRotationField : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L49-L51)[¶](#abaqus.Property.PropertyPart.MaterialOrientation.additionalRotationField "Permalink to this definition")
    :   A String specifying the name of the DiscreteField object specifying the additional
        rotation. The default value is an empty string.

    additionalRotationType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'ROTATION_NONE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L44-L47)[¶](#abaqus.Property.PropertyPart.MaterialOrientation.additionalRotationType "Permalink to this definition")
    :   A SymbolicConstant specifying the method used to describe the additional rotation when a
        valid orientation is specified. Possible values are ROTATION\_NONE, ROTATION\_ANGLE, and
        ROTATION\_FIELD. The default value is ROTATION\_NONE.

    angle : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L67-L69)[¶](#abaqus.Property.PropertyPart.MaterialOrientation.angle "Permalink to this definition")
    :   A Float specifying the angle of the additional rotation (if accessed from the ODB
        instead of the MDB, it will be a string instead of a float). The default value is 0.0.

    axis : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'AXIS_1'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L62-L65)[¶](#abaqus.Property.PropertyPart.MaterialOrientation.axis "Permalink to this definition")
    :   A SymbolicConstant specifying the axis of a datum coordinate system about which an
        additional rotation is applied. For shells this axis is also the shell normal. Possible
        values are AXIS\_1, AXIS\_2, and AXIS\_3. The default value is AXIS\_1.

    fieldName : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L75-L77)[¶](#abaqus.Property.PropertyPart.MaterialOrientation.fieldName "Permalink to this definition")
    :   A String specifying the name of the DiscreteField object specifying the orientation. The
        default value is an empty string.

    flipNormalDirection : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L103-L105)[¶](#abaqus.Property.PropertyPart.MaterialOrientation.flipNormalDirection "Permalink to this definition")
    :   A Boolean specifying the flag to reverse the direction of the defined normal axis
        direction. The default value is OFF.

    flipPrimaryDirection : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L129-L131)[¶](#abaqus.Property.PropertyPart.MaterialOrientation.flipPrimaryDirection "Permalink to this definition")
    :   A Boolean specifying the flag to reverse the direction of the defined primary axis
        direction. The default value is OFF.

    localCsys : --is-rst--:py:data:`~typing.Optional`\[:py:class:`~abaqus.Datum.DatumCsys.DatumCsys`] = `<abaqus.Datum.DatumCsys.DatumCsys object>`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L56-L60)[¶](#abaqus.Property.PropertyPart.MaterialOrientation.localCsys "Permalink to this definition")
    :   A DatumCsys object specifying the local coordinate system or None, describing the
        material orientation for the given region. In the ODB, this member was previously
        accessible using “csys,” but support has now been added for localCsys and the csys
        member will be deprecated.

    normalAxisDatum : --is-rst--:py:data:`~typing.Optional`\[:py:class:`~abaqus.Datum.DatumAxis.DatumAxis`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L99-L101)[¶](#abaqus.Property.PropertyPart.MaterialOrientation.normalAxisDatum "Permalink to this definition")
    :   A DatumAxis object specifying the Datum Axis or None, describing the normal axis
        direction for the discrete orientation.

    normalAxisDefinition : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'NORMAL_VECTOR'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L90-L93)[¶](#abaqus.Property.PropertyPart.MaterialOrientation.normalAxisDefinition "Permalink to this definition")
    :   A SymbolicConstant specifying the method used to define the normal axis direction for a
        discrete orientation. Possible values are SURFACE, NORMAL\_DATUM, and NORMAL\_VECTOR. The
        default value is NORMAL\_VECTOR.

    normalAxisDirection : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'AXIS_3'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L85-L88)[¶](#abaqus.Property.PropertyPart.MaterialOrientation.normalAxisDirection "Permalink to this definition")
    :   A SymbolicConstant specifying the axis that is defined by the normal axis direction for
        a discrete orientation. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default
        value is AXIS\_3.

    normalAxisRegion : --is-rst--:py:data:`~typing.Optional`\[:py:class:`~abaqus.Region.Surface.Surface`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L95-L97)[¶](#abaqus.Property.PropertyPart.MaterialOrientation.normalAxisRegion "Permalink to this definition")
    :   A Surface object specifying a region whose geometric normals define the normal axis for
        the discrete orientation.

    normalAxisVector : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L107-L109)[¶](#abaqus.Property.PropertyPart.MaterialOrientation.normalAxisVector "Permalink to this definition")
    :   A sequence of Floats specifying the vector that defines the direction of the normal axis
        of the discrete orientation.

    orientationType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'GLOBAL'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L79-L83)[¶](#abaqus.Property.PropertyPart.MaterialOrientation.orientationType "Permalink to this definition")
    :   A SymbolicConstant specifying the method used to define the material orientation. If
        **orientationType** = SYSTEM, the **region** and **localCsys** arguments are required. If
        **orientationType** = FIELD, the **fieldName** argument is required. Possible values are
        GLOBAL, SYSTEM, FIELD, DISCRETE, and USER. The default value is GLOBAL.

    primaryAxisDatum : --is-rst--:py:data:`~typing.Optional`\[:py:class:`~abaqus.Datum.DatumAxis.DatumAxis`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L125-L127)[¶](#abaqus.Property.PropertyPart.MaterialOrientation.primaryAxisDatum "Permalink to this definition")
    :   A DatumAxis object specifying the Datum Axis or None, describing the primary axis
        direction for the discrete orientation.

    primaryAxisDefinition : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'PRIMARY_VECTOR'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L116-L119)[¶](#abaqus.Property.PropertyPart.MaterialOrientation.primaryAxisDefinition "Permalink to this definition")
    :   A SymbolicConstant specifying the method used to define the primary axis direction for a
        discrete orientation. Possible values are SURFACE, PRIMARY\_DATUM, and PRIMARY\_VECTOR.
        The default value is PRIMARY\_VECTOR.

    primaryAxisDirection : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'AXIS_1'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L111-L114)[¶](#abaqus.Property.PropertyPart.MaterialOrientation.primaryAxisDirection "Permalink to this definition")
    :   A SymbolicConstant specifying the axis that is defined by the primary axis direction for
        a discrete orientation. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default
        value is AXIS\_1.

    primaryAxisRegion : --is-rst--:py:data:`~typing.Optional`\[:py:class:`~abaqus.Region.Set.Set`] = `None`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L121-L123)[¶](#abaqus.Property.PropertyPart.MaterialOrientation.primaryAxisRegion "Permalink to this definition")
    :   A Set object specifying a region whose geometric tangents define the primary axis for
        the discrete orientation.

    primaryAxisVector : --is-rst--:py:class:`tuple`\[:py:class:`float`, :py:data:`...<Ellipsis>`] = `()`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L133-L135)[¶](#abaqus.Property.PropertyPart.MaterialOrientation.primaryAxisVector "Permalink to this definition")
    :   A sequence of Floats specifying the vector that defines the direction of the primary
        axis of the discrete orientation.

    region : --is-rst--:py:class:`~abaqus.Region.Set.Set`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py)[¶](#abaqus.Property.PropertyPart.MaterialOrientation.region "Permalink to this definition")
    :   A Set object specifying a region for which the material orientation is defined.

    setValues(*\*[args](#abaqus.Property.PropertyPart.MaterialOrientation.setValues "abaqus.Property.PropertyPart.MaterialOrientation.setValues.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Property.PropertyPart.MaterialOrientation.setValues "abaqus.Property.PropertyPart.MaterialOrientation.setValues.kwargs (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L353-L356)[¶](#abaqus.Property.PropertyPart.MaterialOrientation.setValues "Permalink to this definition")
    :   This method modifies the MaterialOrientation object.

    stackDirection : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'STACK_3'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyPart.py#L71-L73)[¶](#abaqus.Property.PropertyPart.MaterialOrientation.stackDirection "Permalink to this definition")
    :   A SymbolicConstant specifying the stack or thickness direction. Possible values are
        STACK\_1, STACK\_2, STACK\_3, and STACK\_ORIENTATION. The default value is STACK\_3.

*class* PlyStackPlot[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PlyStackPlot.py#L10-L20)[¶](#abaqus.Property.PlyStackPlot.PlyStackPlot "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The PlyStackPlot object is used to plot the stacking of plies in a composite layup or in a composite
    shell section.

    Note

    This object can be accessed by:

    ```python
    import section
    import visualization
    ```

    Note

    Check [PlyStackPlot on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-plystackplotpyc.htm?contextscope=all).

    Member Details:

MdbPlyStackPlot(*[part](#abaqus.Property.PlyStackPlot.MdbPlyStackPlot.part "abaqus.Property.PlyStackPlot.MdbPlyStackPlot.part (Python parameter) — A Part object.")*, *[region](#abaqus.Property.PlyStackPlot.MdbPlyStackPlot.region "abaqus.Property.PlyStackPlot.MdbPlyStackPlot.region (Python parameter) — A Region object which contains a composite shell layup.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PlyStackPlot.py#L23-L48)[¶](#abaqus.Property.PlyStackPlot.MdbPlyStackPlot "Permalink to this definition")
:   This method creates a PlyStackPlot object from a region of a part that contains a composite shell layup.

    Note

    This function can be accessed by:

    ```python
    section.MdbPlyStackPlot
    ```

    Note

    Check [MdbPlyStackPlot on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-mdbplystackplotpyc.htm?contextscope=all).

    Parameters:[¶](#abaqus.Property.PlyStackPlot.MdbPlyStackPlot-parameters "Permalink to this headline")
    :   part[¶](#abaqus.Property.PlyStackPlot.MdbPlyStackPlot.part "Permalink to this definition")
        :   A Part object.

        region[¶](#abaqus.Property.PlyStackPlot.MdbPlyStackPlot.region "Permalink to this definition")
        :   A Region object which contains a composite shell layup.

    Returns:[¶](#abaqus.Property.PlyStackPlot.MdbPlyStackPlot-returns "Permalink to this headline")
    :   A PlyStackPlot object.

    Return type:[¶](#abaqus.Property.PlyStackPlot.MdbPlyStackPlot-return-type "Permalink to this headline")
    :   [`PlyStackPlot`](#abaqus.Property.PlyStackPlot.PlyStackPlot "abaqus.Property.PlyStackPlot.PlyStackPlot (Python class) — Bases: object")

    Raises:[¶](#abaqus.Property.PlyStackPlot.MdbPlyStackPlot-raises "Permalink to this headline")
    :   **None.** –

OdbPlyStackPlot(*[odb](#abaqus.Property.PlyStackPlot.OdbPlyStackPlot.odb "abaqus.Property.PlyStackPlot.OdbPlyStackPlot.odb (Python parameter) — An Odb object.")*, *[sectionName](#abaqus.Property.PlyStackPlot.OdbPlyStackPlot.sectionName "abaqus.Property.PlyStackPlot.OdbPlyStackPlot.sectionName (Python parameter) — A String specifying the section name that contains a composite shell section.")*, *[offset](#abaqus.Property.PlyStackPlot.OdbPlyStackPlot.offset "abaqus.Property.PlyStackPlot.OdbPlyStackPlot.offset (Python parameter) — A Float specifying the shell offset.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PlyStackPlot.py#L51-L77)[¶](#abaqus.Property.PlyStackPlot.OdbPlyStackPlot "Permalink to this definition")
:   This method creates a PlyStackPlot object from a composite shell section of an Odb object.

    Note

    This function can be accessed by:

    ```python
    visualization.OdbPlyStackPlot
    ```

    Note

    Check [OdbPlyStackPlot on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-odbplystackplotpyc.htm?contextscope=all).

    Parameters:[¶](#abaqus.Property.PlyStackPlot.OdbPlyStackPlot-parameters "Permalink to this headline")
    :   odb[¶](#abaqus.Property.PlyStackPlot.OdbPlyStackPlot.odb "Permalink to this definition")
        :   An Odb object.

        sectionName[¶](#abaqus.Property.PlyStackPlot.OdbPlyStackPlot.sectionName "Permalink to this definition")
        :   A String specifying the section name that contains a composite shell section.

        offset=`0`[¶](#abaqus.Property.PlyStackPlot.OdbPlyStackPlot.offset "Permalink to this definition")
        :   A Float specifying the shell offset. The default value is 0.0.

    Returns:[¶](#abaqus.Property.PlyStackPlot.OdbPlyStackPlot-returns "Permalink to this headline")
    :   A PlyStackPlot object.

    Raises:[¶](#abaqus.Property.PlyStackPlot.OdbPlyStackPlot-raises "Permalink to this headline")
    :   **None.** –

assignBeamSectionOrientation(*[region](#abaqus.Property.Property.assignBeamSectionOrientation.region "abaqus.Property.Property.assignBeamSectionOrientation.region (Python parameter) — A sequence of geomSequences of Edge objects or a sequence of sequences of one-dimensional elements.")*, *[method](#abaqus.Property.Property.assignBeamSectionOrientation.method "abaqus.Property.Property.assignBeamSectionOrientation.method (Python parameter) — A SymbolicConstant specifying the assignment method.")*, *[n1](#abaqus.Property.Property.assignBeamSectionOrientation.n1 "abaqus.Property.Property.assignBeamSectionOrientation.n1 (Python parameter) — A sequence of three Floats specifying the approximate local n1n1-direction of the beam cross-section.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/Property.py#L20-L41)[¶](#abaqus.Property.Property.assignBeamSectionOrientation "Permalink to this definition")
:   This method assigns a beam section orientation to a region of a part.

    Note

    This function can be accessed by:

    ```python
    mdb.models[name].parts[name].assignBeamSectionOrientation
    ```

    Note

    Check [Property.assignBeamSectionOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-functionpropertypyc.htm?contextscope=all#simaker-functionpropertyassignbeamsectionorientationpyc).

    Parameters:[¶](#abaqus.Property.Property.assignBeamSectionOrientation-parameters "Permalink to this headline")
    :   region[¶](#abaqus.Property.Property.assignBeamSectionOrientation.region "Permalink to this definition")
        :   A sequence of geomSequences of Edge objects or a sequence of sequences of
            one-dimensional elements.

        method[¶](#abaqus.Property.Property.assignBeamSectionOrientation.method "Permalink to this definition")
        :   A SymbolicConstant specifying the assignment method. Only a value of N1\_COSINES is
            currently supported.

        n1[¶](#abaqus.Property.Property.assignBeamSectionOrientation.n1 "Permalink to this definition")
        :   A sequence of three Floats specifying the approximate local n1n1-direction of the beam
            cross-section.

assignMaterialOrientation(*[region](#abaqus.Property.Property.assignMaterialOrientation.region "abaqus.Property.Property.assignMaterialOrientation.region (Python parameter) — A sequence of geomSequences of ConstrainedSketchVertex, Edge, Face, and Cell objects or a sequence of sequences of elements.")*, *[localCsys](#abaqus.Property.Property.assignMaterialOrientation.localCsys "abaqus.Property.Property.assignMaterialOrientation.localCsys (Python parameter) — A Datum object specifying the local coordinate system or None, indicating the global coordinate system.")*, *[axis](#abaqus.Property.Property.assignMaterialOrientation.axis "abaqus.Property.Property.assignMaterialOrientation.axis (Python parameter) — A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate system about which an additional rotation is applied.")=`abaqusConstants.AXIS_1`*, *[angle](#abaqus.Property.Property.assignMaterialOrientation.angle "abaqus.Property.Property.assignMaterialOrientation.angle (Python parameter) — A Float specifying the angle of the additional rotation.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/Property.py#L44-L69)[¶](#abaqus.Property.Property.assignMaterialOrientation "Permalink to this definition")
:   This method assigns a material orientation to a region.

    Note

    This function can be accessed by:

    ```python
    mdb.models[name].parts[name].assignMaterialOrientation
    ```

    Note

    Check [Property.assignMaterialOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-functionpropertypyc.htm?contextscope=all#simaker-functionpropertyassignmaterialorientationpyc).

    Parameters:[¶](#abaqus.Property.Property.assignMaterialOrientation-parameters "Permalink to this headline")
    :   region[¶](#abaqus.Property.Property.assignMaterialOrientation.region "Permalink to this definition")
        :   A sequence of geomSequences of ConstrainedSketchVertex, Edge, Face, and Cell objects or a sequence of
            sequences of elements.

        localCsys[¶](#abaqus.Property.Property.assignMaterialOrientation.localCsys "Permalink to this definition")
        :   A Datum object specifying the local coordinate system or None, indicating the global
            coordinate system.

        axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Property.Property.assignMaterialOrientation.axis "Permalink to this definition")
        :   A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate
            system about which an additional rotation is applied. For shells this axis is also the
            shell normal. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default value is
            AXIS\_1.

        angle=`0`[¶](#abaqus.Property.Property.assignMaterialOrientation.angle "Permalink to this definition")
        :   A Float specifying the angle of the additional rotation. The default value is 0.0.

assignRebarOrientation(*[region](#abaqus.Property.Property.assignRebarOrientation.region "abaqus.Property.Property.assignRebarOrientation.region (Python parameter) — A sequence of geomSequences of ConstrainedSketchVertex, Edge, Face, and Cell objects or a sequence of sequences of elements.")*, *[localCsys](#abaqus.Property.Property.assignRebarOrientation.localCsys "abaqus.Property.Property.assignRebarOrientation.localCsys (Python parameter) — A Datum object specifying the local coordinate system or None, indicating the global coordinate system.")*, *[axis](#abaqus.Property.Property.assignRebarOrientation.axis "abaqus.Property.Property.assignRebarOrientation.axis (Python parameter) — A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate system about which an additional rotation is applied.")=`abaqusConstants.AXIS_1`*, *[angle](#abaqus.Property.Property.assignRebarOrientation.angle "abaqus.Property.Property.assignRebarOrientation.angle (Python parameter) — A Float specifying the angle of the additional rotation.")=`0`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/Property.py#L72-L97)[¶](#abaqus.Property.Property.assignRebarOrientation "Permalink to this definition")
:   This method assigns a rebar reference orientation to a region.

    Note

    This function can be accessed by:

    ```python
    mdb.models[name].parts[name].assignRebarOrientation
    ```

    Note

    Check [Property.assignRebarOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-functionpropertypyc.htm?contextscope=all#simaker-functionpropertyassignrebarorientationpyc).

    Parameters:[¶](#abaqus.Property.Property.assignRebarOrientation-parameters "Permalink to this headline")
    :   region[¶](#abaqus.Property.Property.assignRebarOrientation.region "Permalink to this definition")
        :   A sequence of geomSequences of ConstrainedSketchVertex, Edge, Face, and Cell objects or a sequence of
            sequences of elements.

        localCsys[¶](#abaqus.Property.Property.assignRebarOrientation.localCsys "Permalink to this definition")
        :   A Datum object specifying the local coordinate system or None, indicating the global
            coordinate system.

        axis=`abaqusConstants.AXIS_1`[¶](#abaqus.Property.Property.assignRebarOrientation.axis "Permalink to this definition")
        :   A SymbolicConstant specifying the axis of a cylindrical or spherical datum coordinate
            system about which an additional rotation is applied. For shells this axis is also the
            shell normal. Possible values are AXIS\_1, AXIS\_2, and AXIS\_3. The default value is
            AXIS\_1.

        angle=`0`[¶](#abaqus.Property.Property.assignRebarOrientation.angle "Permalink to this definition")
        :   A Float specifying the angle of the additional rotation. The default value is 0.0.

flipNormal(*[regions](#abaqus.Property.Property.flipNormal.regions "abaqus.Property.Property.flipNormal.regions (Python parameter) — A Region object specifying the region on which normals are flipped.")*, *[referenceRegion](#abaqus.Property.Property.flipNormal.referenceRegion "abaqus.Property.Property.flipNormal.referenceRegion (Python parameter) — A two-dimensional element object whose normal is to be matched.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/Property.py#L100-L123)[¶](#abaqus.Property.Property.flipNormal "Permalink to this definition")
:   This method flips the normals of shell or membrane elements of an orphan mesh or of two-dimensional
    geometric regions.

    Note

    This function can be accessed by:

    ```python
    mdb.models[name].parts[name].flipNormal
    ```

    Note

    Check [Property.flipNormal on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-functionpropertypyc.htm?contextscope=all#simaker-functionpropertyflipnormalpyc).

    Parameters:[¶](#abaqus.Property.Property.flipNormal-parameters "Permalink to this headline")
    :   regions[¶](#abaqus.Property.Property.flipNormal.regions "Permalink to this definition")
        :   A Region object specifying the region on which normals are flipped. For 3D parts, the
            region contains Face objects or two-dimensional triangle or quadrilateral Element
            objects. For axisymmetric parts, the region contains Edge objects or line Elements
            objects.

        referenceRegion=`''`[¶](#abaqus.Property.Property.flipNormal.referenceRegion "Permalink to this definition")
        :   A two-dimensional element object whose normal is to be matched. If unspecified, all the
            normals associated with the given regions will be flipped. The **referenceRegion**
            argument is applicable only if the argument regions contain a sequence of quadrilateral
            or triangular elements.

flipTangent(*[regions](#abaqus.Property.Property.flipTangent.regions "abaqus.Property.Property.flipTangent.regions (Python parameter) — A Region object specifying the region on which normals are flipped.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/Property.py#L126-L142)[¶](#abaqus.Property.Property.flipTangent "Permalink to this definition")
:   This method flips the tangents of beam or truss elements of an orphan mesh or of one-dimensional
    geometric regions.

    Note

    This function can be accessed by:

    ```python
    mdb.models[name].parts[name].flipTangent
    ```

    Note

    Check [Property.flipTangent on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-functionpropertypyc.htm?contextscope=all#simaker-functionpropertyfliptangentpyc).

    Parameters:[¶](#abaqus.Property.Property.flipTangent-parameters "Permalink to this headline")
    :   regions[¶](#abaqus.Property.Property.flipTangent.regions "Permalink to this definition")
        :   A Region object specifying the region on which normals are flipped. The region contains
            Edge objects or one-dimensional Element objects.

unassignBeamSectionOrientation(*[index](#abaqus.Property.Property.unassignBeamSectionOrientation.index "abaqus.Property.Property.unassignBeamSectionOrientation.index (Python parameter) — An Int specifying the number of the beam section orientation assignment to be deleted.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/Property.py#L145-L159)[¶](#abaqus.Property.Property.unassignBeamSectionOrientation "Permalink to this definition")
:   This method deletes a beam section orientation assignment.

    Note

    This function can be accessed by:

    ```python
    mdb.models[name].parts[name].unassignBeamSectionOrientation
    ```

    Note

    Check [Property.unassignBeamSectionOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-functionpropertypyc.htm?contextscope=all#simaker-functionpropertyunassignbeamsectionorientationpyc).

    Parameters:[¶](#abaqus.Property.Property.unassignBeamSectionOrientation-parameters "Permalink to this headline")
    :   index[¶](#abaqus.Property.Property.unassignBeamSectionOrientation.index "Permalink to this definition")
        :   An Int specifying the number of the beam section orientation assignment to be deleted.

unassignMaterialOrientation(*[index](#abaqus.Property.Property.unassignMaterialOrientation.index "abaqus.Property.Property.unassignMaterialOrientation.index (Python parameter) — An Int specifying the number of the material assignment to be deleted.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/Property.py#L162-L176)[¶](#abaqus.Property.Property.unassignMaterialOrientation "Permalink to this definition")
:   This method deletes a material orientation assignment.

    Note

    This function can be accessed by:

    ```python
    mdb.models[name].parts[name].unassignMaterialOrientation
    ```

    Note

    Check [Property.unassignMaterialOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-functionpropertypyc.htm?contextscope=all#simaker-functionpropertyunassignmaterialorientationpyc).

    Parameters:[¶](#abaqus.Property.Property.unassignMaterialOrientation-parameters "Permalink to this headline")
    :   index[¶](#abaqus.Property.Property.unassignMaterialOrientation.index "Permalink to this definition")
        :   An Int specifying the number of the material assignment to be deleted.

unassignRebarOrientation(*[index](#abaqus.Property.Property.unassignRebarOrientation.index "abaqus.Property.Property.unassignRebarOrientation.index (Python parameter) — An Int specifying the number of the rebar reference orientation assignment to be deleted.")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/Property.py#L179-L194)[¶](#abaqus.Property.Property.unassignRebarOrientation "Permalink to this definition")
:   This method deletes a rebar orientation assignment.

    Note

    This function can be accessed by:

    ```python
    mdb.models[name].parts[name].unassignRebarOrientation
    ```

    Note

    Check [Property.unassignRebarOrientation on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-functionpropertypyc.htm?contextscope=all#simaker-functionpropertyunassignrebarorientationpyc).

    Parameters:[¶](#abaqus.Property.Property.unassignRebarOrientation-parameters "Permalink to this headline")
    :   index[¶](#abaqus.Property.Property.unassignRebarOrientation.index "Permalink to this definition")
        :   An Int specifying the number of the rebar reference orientation assignment to be
            deleted.

*class* PropertyAssembly[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyAssembly.py#L14-L73)[¶](#abaqus.Property.PropertyAssembly.PropertyAssembly "Permalink to this definition")
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

    Check [PropertyAssembly on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-assemblypyc.htm?contextscope=all).

    Member Details:

    SectionAssignment(*[region](#abaqus.Property.PropertyAssembly.PropertyAssembly.SectionAssignment.region "abaqus.Property.PropertyAssembly.PropertyAssembly.SectionAssignment.region (Python parameter) — A Set object specifying the region to which the section is assigned.")*, *[sectionName](#abaqus.Property.PropertyAssembly.PropertyAssembly.SectionAssignment.sectionName "abaqus.Property.PropertyAssembly.PropertyAssembly.SectionAssignment.sectionName (Python parameter) — A String specifying the name of the section.")*, *[thicknessAssignment](#abaqus.Property.PropertyAssembly.PropertyAssembly.SectionAssignment.thicknessAssignment "abaqus.Property.PropertyAssembly.PropertyAssembly.SectionAssignment.thicknessAssignment (Python parameter) — A SymbolicConstant specifying section thickness assignment method.")=`abaqusConstants.FROM_SECTION`*, *[offset](#abaqus.Property.PropertyAssembly.PropertyAssembly.SectionAssignment.offset "abaqus.Property.PropertyAssembly.PropertyAssembly.SectionAssignment.offset (Python parameter) — A Float specifying the offset of the shell section.")=`0`*, *[offsetType](#abaqus.Property.PropertyAssembly.PropertyAssembly.SectionAssignment.offsetType "abaqus.Property.PropertyAssembly.PropertyAssembly.SectionAssignment.offsetType (Python parameter) — A SymbolicConstant specifying the method used to define the shell offset.")=`abaqusConstants.SINGLE_VALUE`*, *[offsetField](#abaqus.Property.PropertyAssembly.PropertyAssembly.SectionAssignment.offsetField "abaqus.Property.PropertyAssembly.PropertyAssembly.SectionAssignment.offsetField (Python parameter) — A String specifying the name of the field specifying the offset.")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/PropertyAssembly.py#L26-L73)[¶](#abaqus.Property.PropertyAssembly.PropertyAssembly.SectionAssignment "Permalink to this definition")
    :   This method creates a SectionAssignment object.

        Note

        This function can be accessed by:

        ```python
        mdb.models[name].parts[name].SectionAssignment
        mdb.models[name].rootAssembly.SectionAssignment
        ```

        Note

        Check [SectionAssignment on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionassignmentpyc.htm?contextscope=all).

        Parameters:[¶](#abaqus.Property.PropertyAssembly.PropertyAssembly.SectionAssignment-parameters "Permalink to this headline")
        :   region[¶](#abaqus.Property.PropertyAssembly.PropertyAssembly.SectionAssignment.region "Permalink to this definition")
            :   A Set object specifying the region to which the section is assigned.

            sectionName[¶](#abaqus.Property.PropertyAssembly.PropertyAssembly.SectionAssignment.sectionName "Permalink to this definition")
            :   A String specifying the name of the section.

            thicknessAssignment=`abaqusConstants.FROM_SECTION`[¶](#abaqus.Property.PropertyAssembly.PropertyAssembly.SectionAssignment.thicknessAssignment "Permalink to this definition")
            :   A SymbolicConstant specifying section thickness assignment method. Possible values are
                FROM\_SECTION and FROM\_GEOMETRY. The default value is FROM\_SECTION.

            offset=`0`[¶](#abaqus.Property.PropertyAssembly.PropertyAssembly.SectionAssignment.offset "Permalink to this definition")
            :   A Float specifying the offset of the shell section. The default value is 0.0.

            offsetType=`abaqusConstants.SINGLE_VALUE`[¶](#abaqus.Property.PropertyAssembly.PropertyAssembly.SectionAssignment.offsetType "Permalink to this definition")
            :   A SymbolicConstant specifying the method used to define the shell offset. If
                **offsetType** is set to OFFSET\_FIELD the **offsetField** must have a value. Possible values
                are SINGLE\_VALUE, MIDDLE\_SURFACE, TOP\_SURFACE, BOTTOM\_SURFACE, FROM\_GEOMETRY, and
                OFFSET\_FIELD. The default value is SINGLE\_VALUE.

            offsetField=`''`[¶](#abaqus.Property.PropertyAssembly.PropertyAssembly.SectionAssignment.offsetField "Permalink to this definition")
            :   A String specifying the name of the field specifying the offset. The default value is
                “”.

        Returns:[¶](#abaqus.Property.PropertyAssembly.PropertyAssembly.SectionAssignment-returns "Permalink to this headline")
        :   A SectionAssignment object.

        Return type:[¶](#abaqus.Property.PropertyAssembly.PropertyAssembly.SectionAssignment-return-type "Permalink to this headline")
        :   [`SectionAssignment`](#abaqus.Property.PropertyAssembly.PropertyAssembly.SectionAssignment "abaqus.Property.PropertyAssembly.PropertyAssembly.SectionAssignment (Python method) — This method creates a SectionAssignment object.")

*class* SectionAssignment(*[region](#abaqus.Property.SectionAssignmentArray.SectionAssignment "abaqus.Property.SectionAssignmentArray.SectionAssignment.__init__.region (Python parameter)")*, *[sectionName](#abaqus.Property.SectionAssignmentArray.SectionAssignment "abaqus.Property.SectionAssignmentArray.SectionAssignment.__init__.sectionName (Python parameter)")*, *[thicknessAssignment](#abaqus.Property.SectionAssignmentArray.SectionAssignment "abaqus.Property.SectionAssignmentArray.SectionAssignment.__init__.thicknessAssignment (Python parameter)")=`abaqusConstants.FROM_SECTION`*, *[offset](#abaqus.Property.SectionAssignmentArray.SectionAssignment "abaqus.Property.SectionAssignmentArray.SectionAssignment.__init__.offset (Python parameter)")=`0`*, *[offsetType](#abaqus.Property.SectionAssignmentArray.SectionAssignment "abaqus.Property.SectionAssignmentArray.SectionAssignment.__init__.offsetType (Python parameter)")=`abaqusConstants.SINGLE_VALUE`*, *[offsetField](#abaqus.Property.SectionAssignmentArray.SectionAssignment "abaqus.Property.SectionAssignmentArray.SectionAssignment.__init__.offsetField (Python parameter)")=`''`*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/SectionAssignmentArray.py#L18-L142)[¶](#abaqus.Property.SectionAssignmentArray.SectionAssignment "Permalink to this definition")
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.13)")

    The SectionAssignment object is used to specify a section assignment on an assembly or part. Section
    assignments on the assembly are limited to connector elements only.

    Note

    This object can be accessed by:

    ```python
    import section
    mdb.models[name].parts[name].sectionAssignments[i]
    import assembly
    mdb.models[name].rootAssembly.sectionAssignments[i]
    import odbAccess
    session.odbs[name].parts[name].sectionAssignments[i]
    session.odbs[name].rootAssembly.instances[name].sectionAssignments[i]
    session.odbs[name].rootAssembly.sectionAssignments[i]
    session.odbs[name].steps[name].frames[i].fieldOutputs[name].values[i].instance.sectionAssignments[i]
    ```

    Note

    Check [SectionAssignment on help.3ds.com/2025](https://help.3ds.com/2025/English/DSSIMULIA_Established/SIMACAEKERRefMap/simaker-c-sectionassignmentpyc.htm?contextscope=all).

    Member Details:

    getVertices()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/SectionAssignmentArray.py#L121-L137)[¶](#abaqus.Property.SectionAssignmentArray.SectionAssignment.getVertices "Permalink to this definition")
    :   This method is only valid for connector section assignments. This method returns a sequence
        consisting of tuples of coordinates of the connector’s endpoints.

        Returns:[¶](#abaqus.Property.SectionAssignmentArray.SectionAssignment.getVertices-returns "Permalink to this headline")
        :   A sequence of tuples of floats.

        Return type:[¶](#abaqus.Property.SectionAssignmentArray.SectionAssignment.getVertices-return-type "Permalink to this headline")
        :   `Sequence[tuple[float`, `]]`

        Raises:[¶](#abaqus.Property.SectionAssignmentArray.SectionAssignment.getVertices-raises "Permalink to this headline")
        :   [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.13)") – An exception is thrown if getVertices() is called on any section assignment except
            connector section assignment. This method is valid only for connector section assignments.

    offset : --is-rst--:py:class:`float` = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/SectionAssignmentArray.py#L51-L52)[¶](#abaqus.Property.SectionAssignmentArray.SectionAssignment.offset "Permalink to this definition")
    :   A Float specifying the offset of the shell section. The default value is 0.0.

    offsetField : --is-rst--:py:class:`str` = `''`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/SectionAssignmentArray.py#L60-L62)[¶](#abaqus.Property.SectionAssignmentArray.SectionAssignment.offsetField "Permalink to this definition")
    :   A String specifying the name of the field specifying the offset. The default value is
        “”.

    offsetType : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'SINGLE_VALUE'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/SectionAssignmentArray.py#L54-L58)[¶](#abaqus.Property.SectionAssignmentArray.SectionAssignment.offsetType "Permalink to this definition")
    :   A SymbolicConstant specifying the method used to define the shell offset. If
        **offsetType** is set to OFFSET\_FIELD the **offsetField** must have a value. Possible values
        are SINGLE\_VALUE, MIDDLE\_SURFACE, TOP\_SURFACE, BOTTOM\_SURFACE, FROM\_GEOMETRY, and
        OFFSET\_FIELD. The default value is SINGLE\_VALUE.

    region : --is-rst--:py:class:`~abaqus.Region.Set.Set`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/SectionAssignmentArray.py)[¶](#abaqus.Property.SectionAssignmentArray.SectionAssignment.region "Permalink to this definition")
    :   A Set object specifying the region to which the section is assigned.

    resume()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/SectionAssignmentArray.py#L111-L114)[¶](#abaqus.Property.SectionAssignmentArray.SectionAssignment.resume "Permalink to this definition")
    :   This method resumes the section assignment that was previously suppressed.

    sectionName : --is-rst--:py:class:`str`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/SectionAssignmentArray.py)[¶](#abaqus.Property.SectionAssignmentArray.SectionAssignment.sectionName "Permalink to this definition")
    :   A String specifying the name of the section.

    setValues(*\*[args](#abaqus.Property.SectionAssignmentArray.SectionAssignment.setValues "abaqus.Property.SectionAssignmentArray.SectionAssignment.setValues.args (Python parameter)")*, *\*\*[kwargs](#abaqus.Property.SectionAssignmentArray.SectionAssignment.setValues "abaqus.Property.SectionAssignmentArray.SectionAssignment.setValues.kwargs (Python parameter)")*)[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/SectionAssignmentArray.py#L139-L142)[¶](#abaqus.Property.SectionAssignmentArray.SectionAssignment.setValues "Permalink to this definition")
    :   This method modifies the SectionAssignment object.

    suppress()[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/SectionAssignmentArray.py#L116-L119)[¶](#abaqus.Property.SectionAssignmentArray.SectionAssignment.suppress "Permalink to this definition")
    :   This method suppresses the section assignment.

    suppressed : --is-rst--:py:data:`~typing.Union`\[:py:class:`~abaqus.UtilityAndView.AbaqusBoolean.AbaqusBoolean`, :py:class:`bool`] = `0`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/SectionAssignmentArray.py#L37-L39)[¶](#abaqus.Property.SectionAssignmentArray.SectionAssignment.suppressed "Permalink to this definition")
    :   A Boolean specifying whether the section assignment is suppressed or not. The default
        value is OFF.

    thicknessAssignment : --is-rst--:py:class:`~abaqus.UtilityAndView.SymbolicConstant.SymbolicConstant` = `'FROM_SECTION'`[[source]](https://github.com/haiiliin/abqpy/blob/2025/src/abaqus/Property/SectionAssignmentArray.py#L47-L49)[¶](#abaqus.Property.SectionAssignmentArray.SectionAssignment.thicknessAssignment "Permalink to this definition")
    :   A SymbolicConstant specifying section thickness assignment method. Possible values are
        FROM\_SECTION and FROM\_GEOMETRY. The default value is FROM\_SECTION.

[Back to top](#)