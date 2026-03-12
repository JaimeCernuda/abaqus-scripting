# BaseException object

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | BaseException object | | |  | | | |  | | --- | | The odb\_BaseException object catches all exceptions thrown in the output database  This page discusses:   * [Access](#simaker-c-infbaseexceptioncpp__simaker-c-infbaseexceptioncpp-s-cppaccess1) * [UserReport()](#simaker-exceptexceptuserreportpyccpp) | | |   Access  ``` catch(odb_BaseException& exc) ```  UserReport() This method returns a description of the error condition that generated the exception.  Prototype  ``` odb_String UserReport() const; ```  Arguments None.  Return value None.  Exceptions None. |