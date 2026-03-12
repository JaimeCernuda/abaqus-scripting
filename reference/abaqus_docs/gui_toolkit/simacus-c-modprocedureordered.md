# AFXOrderedPickStep

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | AFXOrderedPickStep | | |  | | | |  | | --- | | The AFXOrderedPickStep is a special pick step that preserves the order in which the user picks entities. | | |   For example, when picking four nodes to create a quad element, the order in which the user picks the nodes is important and must be preserved during picking. The user must pick the entities one at a time and cannot drag select them. In addition, because this is a single step that treats the picked entities as a single pick, the user cannot backup any of the individual picks. The step continues to loop until the user clicks the mouse button two. |