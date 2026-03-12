# Creating a mid-plane shell mesh from a thin solid model

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Creating a mid-plane shell mesh from a thin solid model | | |  | | | |  | | --- | | You can use the following procedure to create a mid-plane shell mesh from a thin solid model using the offset meshing tool: | | |   1. Convert the solid part to a shell using the From solid shell tool in the Part module. 2. Isolate a collection of faces on the upper or lower surface of the part using the Remove faces tool in the Geometry Edit toolset. 3. Mesh the simplified model with shell elements, and create a mesh part. 4. Create an offset shell mesh, and specify an Initial Offset corresponding to half the model thickness. |