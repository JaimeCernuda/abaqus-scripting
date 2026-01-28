# Geometry Verification Report
## Experiment 4 - Pin Hole Orientation

**Date:** January 27, 2026
**Model:** Experiment4_TO_Specimen_v19.cae

---

## Verification Method

Three independent verification methods were used:

### 1. Circular Edge Coordinate Analysis (verify_holes.py)

Analyzed all circular edges with radius 6.35mm (pin radius):

| Hole | Edge 1 X | Edge 2 X | X Span | Z Span | Direction |
|------|----------|----------|--------|--------|-----------|
| Upper | -9.0 | 9.0 | **18.0 mm** | 0.0 mm | **X-direction** |
| Lower Left | -32.3 | -14.3 | **18.0 mm** | 0.0 mm | **X-direction** |
| Lower Right | 14.3 | 32.3 | **18.0 mm** | 0.0 mm | **X-direction** |

**Interpretation:**
- X-direction holes have large X-span (front-to-back of block) and zero Z-span
- Z-direction holes would have zero X-span and large Z-span
- **All holes are confirmed X-direction**

### 2. Input File Node Coordinates (Job_100kN.inp)

Examined nodes on circular hole boundaries:

**Upper hole circle nodes:**
- Node at X=-9.0: Forms circle on inner face (UB_LEFT)
- Node at X=+9.0: Forms circle on outer face (UB_RIGHT)
- Circle centers at Y≈132.17 (UPPER_PIN_Y)

**Lower right hole circle nodes:**
- Nodes 39-45 at X=14.3: Circle on inner face
- Nodes 46-52 at X=32.3: Circle on outer face
- Circle centers at Y≈14.0 (LOWER_PIN_Y)

**Lower left hole circle nodes:**
- Nodes 60-66 at X=-14.3: Circle on inner face
- Nodes 53-59 at X=-32.3: Circle on outer face

### 3. Geometry Creation Script Analysis (create_geometry_v19.py)

The script uses faces with X-normals as sketch planes:
- `upper_face = part.faces.findAt(((-9.0, 127.5, 16.7),))` - Face at X=-9
- CutExtrude with `depth=BLOCK_WIDTH_X` (18mm) cuts through X-direction

---

## Visual Confirmation

The isometric view shows:
1. Upper block with through-hole (circular opening visible)
2. Lower left block with through-hole
3. Lower right block with through-hole

From the viewing angle:
- X-direction holes appear as ellipses (viewed at angle to axis)
- The holes connect left and right faces of each block

---

## Conclusion

**ALL THREE PIN HOLES ARE CORRECTLY ORIENTED IN THE X-DIRECTION**

This allows proper specimen mounting in the MTS 370.02 load frame with:
- Horizontal pins inserted through the specimen thickness
- Upper pin connected to load cell
- Lower pins connected to fixed grips

---

## Analysis Results Summary

With correctly oriented X-direction holes, the analysis produced:

| Load | Max Stress | Status |
|------|------------|--------|
| 20 kN | 380.72 MPa | Elastic (below 980 MPa yield) |
| 60 kN | 982.39 MPa | Yield onset (PEEQ = 0.001) |
| 100 kN | 1148.03 MPa | Plastic (PEEQ = 0.067) |

These results are physically consistent with the IN718 material properties and demonstrate
the expected elastic-to-plastic transition.
