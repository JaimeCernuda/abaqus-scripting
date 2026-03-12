# getLoopStep

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | getLoopStep | | |  | | | |  | | --- | | If you want your procedure to loop, you must write the getLoopStep method. | | |   The getLoopStep method is defined in the base class to return None, indicating that the mode will be run through a single time. You can redefine the getLoopStep method and return a step to which the procedure should loop back. The following example shows how you can make the procedure shown in the previous section loop back to the first step after it has completed the last step:  ``` def getLoopStep(self):     return self.step1 ``` |