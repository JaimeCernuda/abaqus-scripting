# Nonpickable entities

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Nonpickable entities | | |  | | | |  | | --- | | By default, the procedure mode prevents previously selected geometric entities from being selected twice in the same procedure. If you do not want this behavior, you can call the allowRepeatedSelections method. | | |   The following example shows how to allow repeated selections:  ``` step = AFXPickStep(self, self.edgeKw, 'Select a straight edge',      AFXPickStep.EDGES) step.allowRepeatedSelections(True) ```  Disallowing repeated picks works only for geometry items such as vertices, edges, and faces; it does not work for nodes and elements. |