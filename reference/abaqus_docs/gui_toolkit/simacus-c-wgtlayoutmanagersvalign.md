# Vertical alignment for composite children

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Vertical alignment for composite children | | |  | | | |  | | --- | | The AFXVerticalAligner widget is designed to align children that contain multiple children. | | |   AFXVerticalAligner does the following:   1. Finds the maximum width of the first child of each of its children. 2. Sets the width of all the first children to the maximum width.   For example,   ``` va = AFXVerticalAligner(parent) AFXTextField(va, 16, 'Name:') AFXTextField(va, 16, 'Address:') AFXTextField(va, 16, 'Phone Number:') ```  Figure 1. An example of vertical alignment from AFXVerticalAligner. |