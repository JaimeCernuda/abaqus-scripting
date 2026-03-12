# Spinners

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Spinners | | |  | | | |  | | --- | | The AFXSpinner widget combines a text field and two arrow buttons. | | |   The arrows increment the integer value shown in the text field. AFXSpinner extends the capability of the FXSpinner widget by providing an optional label. For example,  ``` spinner = AFXSpinner(p, 4, 'AFXSpinner:') spinner.setRange(20, 80) spinner.setValue(50) ``` Figure 1. An example of a spinner from AFXSpinner.     The AFXFloatSpinner widget is similar to the AFXSpinner widget, but it allows floating point values. |