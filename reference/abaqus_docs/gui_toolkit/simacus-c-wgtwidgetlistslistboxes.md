# List boxes

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | List boxes | | |  | | | |  | | --- | | The AFXListBox widget provides a one-of-many selection from its items. | | |   AFXListBox differs from AFXComboBox in that the items displayed by  AFXListBox can include icons. For example,  ``` listBox = AFXListBox(parent, 3, 'AFXListBox:', keyword) listBox.appendItem('Item 1', thinIcon) listBox.appendItem('Item 2', mediumIcon) listBox.appendItem('Item 3', thickIcon) ``` Figure 1. An example of a list box from AFXListBox. |