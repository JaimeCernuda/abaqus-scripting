# Refining what the user can select

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Refining what the user can select | | |  | | | |  | | --- | | A refinement qualifies the types of pickable entities specified in the AFXPickStep constructor. | | |   The following example shows how to select only straight edges:  ``` step = AFXPickStep(self, self.edgeKw, 'Select a straight edge',      AFXPickStep.EDGES) step.setEdgeRefinements(AFXPickStep.STRAIGHT) ```  By default, no refinements are set. For a complete list of refinements, see the [Abaqus GUI Toolkit Reference Guide](.._SIMACAEGUIRefHtml_simagui-c-ov.md). |