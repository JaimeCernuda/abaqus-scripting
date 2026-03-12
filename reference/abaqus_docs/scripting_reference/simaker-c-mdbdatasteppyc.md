# MdbDataStep object

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | MdbDataStep object | | |  | | | |  | | --- | | The MdbDataStep object.It corresponds to same named step in the cae model.  This page discusses:   * [Access](#simaker-c-mdbdatasteppyc__simaker-c-mdbdatasteppyc-s-pyaccess1) * [Members](#simaker-c-mdbdatasteppyc-t-pymembersect1) | | |   Access  ``` import visualization session.mdbData[name].steps[i] ```  Members The MdbDataStep object has the following member:  frames  A [MdbDataFrameArray](simaker-c-mdbdataframepyc.md) object specifying the list of frames. The list is read-only. There is only one frame in a step. |