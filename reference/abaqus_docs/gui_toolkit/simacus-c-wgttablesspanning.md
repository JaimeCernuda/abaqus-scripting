# Spanning

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Spanning | | |  | | | |  | | --- | | You can make an item in a header row or column span more than one row or column. | | |   ``` vf = FXVerticalFrame(parent, FRAME_SUNKEN|FRAME_THICK,      0,0,0,0, 0,0,0,0) table = AFXTable(vf, 4, 3, 4, 3) table.setLeadingColumns(1) table.setLeadingRows(2)  # Corner item table.setItemSpan(0, 0, 2, 1)  # Span top row item over 2 columns table.setItemSpan(0, 1, 1, 2) table.setLeadingRowLabels('Coordinates') table.setLeadingRowLabels('X\tY', 1)  table.showHorizontalGrid(True) table.showVerticalGrid(True)  table.setColumnWidth(0, 30) ```  Figure 1. An example of spanning two header columns. |