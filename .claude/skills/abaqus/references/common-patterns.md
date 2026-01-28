# Common Abaqus Scripting Patterns

## Model Setup Template

```python
from abaqus import *
from abaqusConstants import *
from caeModules import *

# Create model
model = mdb.Model(name='MyModel')
if 'Model-1' in mdb.models:
    del mdb.models['Model-1']
```

## Geometry Creation

### Extruded Box
```python
part = model.Part(name='Box', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch = model.ConstrainedSketch(name='BoxSketch', sheetSize=200.0)
sketch.rectangle(point1=(0.0, 0.0), point2=(LENGTH, WIDTH))
part.BaseSolidExtrude(sketch=sketch, depth=HEIGHT)
```

### Revolved Cylinder
```python
part = model.Part(name='Cylinder', dimensionality=THREE_D, type=DEFORMABLE_BODY)
sketch = model.ConstrainedSketch(name='CylSketch', sheetSize=200.0)
sketch.rectangle(point1=(0.0, 0.0), point2=(RADIUS, HEIGHT))
part.BaseSolidRevolve(sketch=sketch, angle=360.0, flipRevolveDirection=OFF)
```

### Import CAD
```python
step = mdb.openStep('path/to/file.step', scaleFromFile=OFF)
part = mdb.models['MyModel'].PartFromGeometryFile(
    name='ImportedPart',
    geometryFile=step,
    dimensionality=THREE_D,
    type=DEFORMABLE_BODY
)
```

## Material Definition

### Elastic Material
```python
material = model.Material(name='Steel')
material.Elastic(table=((210000.0, 0.3),))  # E, nu
material.Density(table=((7.85e-9,),))        # tonne/mm³
```

### With Plasticity
```python
material = model.Material(name='Steel')
material.Elastic(table=((210000.0, 0.3),))
material.Plastic(table=(
    (250.0, 0.0),    # yield stress, plastic strain
    (400.0, 0.2),
    (500.0, 0.4),
))
material.Density(table=((7.85e-9,),))
```

### Thermal Properties
```python
material.Conductivity(table=((50.0,),))              # W/(m·K) → W/(mm·K) = 0.05
material.SpecificHeat(table=((500e6,),))             # J/(kg·K) → J/(tonne·K)
material.Expansion(table=((12e-6,),))                # 1/K
```

## Section Assignment

```python
model.HomogeneousSolidSection(name='SolidSection', material='Steel', thickness=None)

cells = part.cells
region = part.Set(cells=cells, name='AllCells')
part.SectionAssignment(region=region, sectionName='SolidSection')
```

## Assembly

```python
assembly = model.rootAssembly
assembly.DatumCsysByDefault(CARTESIAN)
instance = assembly.Instance(name='Part-1', part=part, dependent=ON)
```

## Locating Faces/Edges

### By Coordinates (findAt)
```python
# Find face at a point
face = instance.faces.findAt(((x, y, z),))

# Find edge at a point
edge = instance.edges.findAt(((x, y, z),))

# Find vertex at a point
vertex = instance.vertices.findAt(((x, y, z),))
```

### By Bounding Box (getByBoundingBox)
```python
faces = instance.faces.getByBoundingBox(
    xMin=0, yMin=0, zMin=0,
    xMax=10, yMax=100, zMax=50
)
```

### Create Sets and Surfaces
```python
# Create node/element set
fixed_face = instance.faces.findAt(((0.0, HEIGHT/2, WIDTH/2),))
fixed_region = assembly.Set(faces=fixed_face, name='FixedEnd')

# Create surface
load_face = instance.faces.findAt(((LENGTH, HEIGHT/2, WIDTH/2),))
load_surface = assembly.Surface(side1Faces=load_face, name='LoadSurface')
```

## Boundary Conditions

### Encastre (Fixed)
```python
model.EncastreBC(name='Fixed', createStepName='Initial', region=fixed_region)
```

### Displacement BC
```python
model.DisplacementBC(
    name='Pinned',
    createStepName='Initial',
    region=region,
    u1=0.0, u2=0.0, u3=0.0,          # Displacements
    ur1=UNSET, ur2=UNSET, ur3=UNSET  # Rotations free
)
```

### Symmetry
```python
model.XssymmBC(name='SymX', createStepName='Initial', region=region)  # X-symmetry
model.YsymmBC(name='SymY', createStepName='Initial', region=region)   # Y-symmetry
model.ZsymmBC(name='SymZ', createStepName='Initial', region=region)   # Z-symmetry
```

## Loads

### Concentrated Force
```python
model.ConcentratedForce(
    name='PointLoad',
    createStepName='LoadStep',
    region=region,
    cf1=0.0, cf2=-1000.0, cf3=0.0  # Force components
)
```

### Surface Traction
```python
model.SurfaceTraction(
    name='Traction',
    createStepName='LoadStep',
    region=surface,
    magnitude=10.0,  # MPa
    directionVector=((0, 0, 0), (0, -1, 0)),  # Direction
    distributionType=UNIFORM,
    traction=GENERAL
)
```

### Pressure
```python
model.Pressure(
    name='Pressure',
    createStepName='LoadStep',
    region=surface,
    magnitude=10.0  # MPa (positive = compression)
)
```

## Analysis Steps

### Static Step
```python
model.StaticStep(
    name='LoadStep',
    previous='Initial',
    timePeriod=1.0,
    initialInc=1.0,
    minInc=1e-6,
    maxInc=1.0,
    nlgeom=OFF  # ON for large deformation
)
```

### Frequency Step
```python
model.FrequencyStep(
    name='FreqStep',
    previous='Initial',
    numEigen=10,  # Number of modes
    eigensolver=LANCZOS
)
```

### Dynamic Explicit
```python
model.ExplicitDynamicsStep(
    name='Impact',
    previous='Initial',
    timePeriod=0.01  # seconds
)
```

## Meshing

### Seed and Generate
```python
part.seedPart(size=MESH_SIZE, deviationFactor=0.1, minSizeFactor=0.1)

elemType1 = mesh.ElemType(elemCode=C3D8R, elemLibrary=STANDARD)
elemType2 = mesh.ElemType(elemCode=C3D6, elemLibrary=STANDARD)
elemType3 = mesh.ElemType(elemCode=C3D4, elemLibrary=STANDARD)
part.setElementType(regions=(part.cells,), elemTypes=(elemType1, elemType2, elemType3))

part.generateMesh()

print(f"Nodes: {len(part.nodes)}, Elements: {len(part.elements)}")
```

### Local Seeding
```python
# Seed specific edges
edges = part.edges.findAt(((x, y, z),))
part.seedEdgeBySize(edges=edges, size=1.0)
```

## Output Requests

```python
model.FieldOutputRequest(
    name='F-Output-1',
    createStepName='LoadStep',
    variables=('S', 'U', 'RF', 'E', 'ENER')
)

model.HistoryOutputRequest(
    name='H-Output-1',
    createStepName='LoadStep',
    variables=('ALLSE', 'ALLKE', 'ALLWK')
)
```

## Job Submission

```python
mdb.saveAs(pathName='MyModel.cae')

job = mdb.Job(name='MyJob', model='MyModel', type=ANALYSIS)
job.writeInput(consistencyChecking=OFF)
job.submit(consistencyChecking=OFF)
job.waitForCompletion()
```

## ODB Post-Processing

```python
from odbAccess import openOdb

odb = openOdb(path='MyJob.odb', readOnly=True)

step = odb.steps['LoadStep']
frame = step.frames[-1]  # Last frame

# Get displacement field
disp = frame.fieldOutputs['U']
for value in disp.values:
    print(f"Node {value.nodeLabel}: {value.data}")

# Get stress field
stress = frame.fieldOutputs['S']
for value in stress.values:
    print(f"Element {value.elementLabel}: Mises = {value.mises}")

odb.close()
```

## Topology Optimization

```python
# Create optimization task
model.TopologyTask(
    name='TopoTask',
    region=MODEL,
    materialInterpolationTechnique=SIMP,
    materialInterpolationPenalty=3.0,
    freezeBoundaryConditionRegions=ON,
    freezeLoadRegions=ON
)

# Design responses
model.optimizationTasks['TopoTask'].SingleTermDesignResponse(
    name='volume', region=MODEL, identifier=VOLUME
)
model.optimizationTasks['TopoTask'].SingleTermDesignResponse(
    name='strain_energy', region=MODEL, identifier=STRAIN_ENERGY, stepOptions=LAST_STEP
)

# Objective: minimize strain energy (maximize stiffness)
model.optimizationTasks['TopoTask'].ObjectiveFunction(
    name='MinEnergy',
    objectives=((model.optimizationTasks['TopoTask'].designResponses['strain_energy'],
                 MINIMIZE_MAXIMUM, 1.0, 0.0),)
)

# Constraint: volume <= 30%
model.optimizationTasks['TopoTask'].OptimizationConstraint(
    name='VolConstraint',
    designResponse='volume',
    restrictionMethod=RELATIVE_LESS_THAN_EQUAL,
    restrictionValue=0.3
)

# Create and run optimization process
opt = mdb.OptimizationProcess(
    name='Optimization',
    model='MyModel',
    task='TopoTask',
    maxDesignCycle=50
)
# opt.submit()
```
