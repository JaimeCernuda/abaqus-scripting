# Color buttons

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Color buttons | | |  | | | |  | | --- | | The AFXColorButton widget displays a push button that shows a color. | | |   Clicking the button posts the color selection dialog box, which the user can use to change the value of the color for the button. For example,  ```  AFXColorButton(parent, 'Color:') ``` Figure 1. An example of an AFXColorButton.     When connected to an AFXStringKeyword, this widget will assign the value of the button's current color to the keyword in hex format; for example, "#FF0000". |