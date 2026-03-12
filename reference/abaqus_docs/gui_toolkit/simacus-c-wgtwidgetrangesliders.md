# Sliders

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Sliders | | |  | | | |  | | --- | | The AFXSlider widget provides a handle that the user can drag to set a value using only the mouse. | | |   AFXSlider extends the capability of the FXSlider widget by providing the following:   * An optional title. * Minimum and maximum range labels. * The ability to display the current value above the drag handle.   For example,   ``` slider = AFXSlider(p, None, 0,     AFXSLIDER_INSIDE_BAR|AFXSLIDER_SHOW_VALUE|LAYOUT_FILL_X) slider.setMinLabelText('Min') slider.setMaxLabelText('Max')  slider.setDecimalPlaces(1) slider.setRange(20, 80)  slider.setValue(50) ```  Figure 1. An example of a slider from  AFXSlider. |