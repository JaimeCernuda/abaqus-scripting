# OdbDataSection object

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | OdbDataSection object | | |  | | | |  | | --- | | The OdbDataSection object stores section data.  This page discusses:   * [Access](#simaker-c-odbdatasectionpyc__simaker-c-odbdatasectionpyc-s-pyaccess1) * [Members](#simaker-c-odbdatasectionpyc-t-pymembersect1) | | |   Access  ``` import visualization session.odbData[name].sections[i] ```  Members The OdbDataSection object has the following members:  name  A String specifying the set name. This attribute is read-only.  elements  A String-to-tuple-of-Ints Dictionary specifying the elements in the set. This attribute is read-only. |