# Action button handling

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Action button handling | | |  | | | |  | | --- | | AFXDialog and AFXDataDialog provide some automatic handling of the messages that are sent when a button in the action area is clicked. If you want to perform some actions other than those provided by the dialog box, you must catch the messages sent by the action area buttons and write your own message handler. | | |   For example, if you want to take an action when the user clicks the Apply button in the dialog box, you must catch the (ID\_CLICKED\_APPLY | SEL\_COMMAND) message and map it to a message handler in your dialog box. For more information, see [Targets and messages](simacus-c-comcommandstargets.md). |