# The drawing area and canvas

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | The drawing area and canvas | | |  | | | |  | | --- | | The canvas provides an infinite space upon which you can create and manipulate viewports. The drawing area is a window into the visible part of the canvas. | | |   You can access the canvas area using the following statement:  ``` canvas = getAFXApp().getAFXMainWindow().i_getCanvas() ```  The “i\_” in the method name indicates that this is an internal method that you should not normally use—it is expected that only the GUI infrastructure needs to access this method. |