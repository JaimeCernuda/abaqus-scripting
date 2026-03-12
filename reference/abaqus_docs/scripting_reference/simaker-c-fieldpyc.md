# Field object

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Field object | | |  | | | |  | | --- | | The Field object is the abstract base type for other Field objects. The Field object has no explicit constructor. The methods and members of the Field object are common to all objects derived from the Field.  This page discusses:   * [Access](#simaker-c-fieldpyc__simaker-c-fieldpyc-s-pyaccess1) * [Members](#simaker-c-fieldpyc-t-pymembersect1) | | |   Access  ``` import fields ```  Members The Field object can have the following members:  name  A String specifying the repository key.  description  A String specifying the description of the field. The default value is an empty string. |