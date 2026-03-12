# OdbDataMaterial object

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | OdbDataMaterial object | | |  | | | |  | | --- | | The OdbDataMaterial object stores material data.  This page discusses:   * [Access](#simaker-c-odbdatamaterialpyc__simaker-c-odbdatamaterialpyc-s-pyaccess1) * [Members](#simaker-c-odbdatamaterialpyc-t-pymembersect1) | | |   Access  ``` import visualization session.odbData[name].materials[i] ```  Members The OdbDataMaterial object has the following members:  name  A String specifying the set name. This attribute is read-only.  elements  A String-to-tuple-of-Ints Dictionary specifying the elements in the set. This attribute is read-only. |