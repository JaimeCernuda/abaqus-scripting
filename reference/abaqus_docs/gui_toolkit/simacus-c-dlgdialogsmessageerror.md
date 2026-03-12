# Error dialog boxes

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Error dialog boxes | | |  | | | |  | | --- | | You post error dialog boxes in response to a failure condition that the application cannot resolve. | | |   Error dialog boxes have the following characteristics:   * The application name is displayed in their title bar. * An error symbol is displayed on the left side of the dialog box. * The action area contains only a Dismiss button. * They are modal.   For example:   ``` mainWindow = getAFXApp().getAFXMainWindow() showAFXErrorDialog(mainWindow, 'An invalid value was supplied.') ```  Figure 1. An example of an error dialog box from showAFXErrorDialog. |