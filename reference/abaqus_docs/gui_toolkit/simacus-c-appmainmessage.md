# The message area

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | The message area | | |  | | | |  | | --- | | The application uses the message area to display informational and warning messages. | | |   You can send messages to the message area using the following method:  ``` mainWindow = getAFXApp().getAFXMainWindow() mainWindow.writeToMessageArea('Warning: Some items failed!') ``` |