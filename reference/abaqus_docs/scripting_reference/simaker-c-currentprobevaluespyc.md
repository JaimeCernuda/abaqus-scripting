# CurrentProbeValues object

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | CurrentProbeValues object | | |  | | | |  | | --- | | The CurrentProbeValues object has no constructor. The CurrentProbeValues object is created when you import the Visualization module.  This page discusses:   * [Access](#simaker-c-currentprobevaluespyc__simaker-c-currentprobevaluespyc-s-pyaccess1) * [Members](#simaker-c-currentprobevaluespyc-t-pymembersect1) | | |   Access  ``` import visualization session.currentProbeValues ```  Members The CurrentProbeValues object has the following member:  values  A tuple of Floats specifying the values obtained while probing. These values are updated constantly as the user moves the mouse over the object being probed. |