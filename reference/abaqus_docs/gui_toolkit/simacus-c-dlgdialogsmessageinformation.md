# Information dialog boxes

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Information dialog boxes | | |  | | | |  | | --- | | You post information dialog boxes to provide an explanatory message. | | |   Information dialog boxes have the following characteristics:   * The application name is displayed in their title bar. * An information symbol is displayed on the left side of the dialog box. * The action area contains only a Dismiss button. * They are modal.   For example,   ``` mainWindow = getAFXApp().getAFXMainWindow() showAFXInformationDialog(mainWindow,      'This is an information dialog.') ```  Figure 1. An example of an information dialog box from showAFXInformationDialog. |