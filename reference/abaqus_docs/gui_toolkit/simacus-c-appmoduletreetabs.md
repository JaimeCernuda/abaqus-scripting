# Tree tabs

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Tree tabs | | |  | | | |  | | --- | | By default, the tabs in the TreeToolsetGui are not visible when the user switches into a custom module. To specify that a tab should be visible or applicable to a module, use the appendApplicableModuleForTreeTab and appendVisibleModuleForTreeTab methods. | | |   The example in [GUI module example](simacus-c-appmoduleoverview.md#simacus-c-appmoduleoverview) specifies that the Model tab will be applicable and visible in My Module. If the user is in the Part module and switches to My Module, the Results tab will be hidden, and the Model tab will be made current if it was not already current. |