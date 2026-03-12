# Initializing the C++ interface

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Initializing the C++ interface | | |  | | | |  | | --- | | Before any calls are made to the C++ interface, the following call must be made to initialize the interface:  ``` odb_initializeAPI(); ```  This call is generated automatically when the abaqus make utility is run but must be included in any application that is not compiled and linked using the abaqus make utility. After all calls to the C++ interface have been completed, the interface may be deactivated by including a call to  ``` odb_finalizeAPI(); ```  If the finalization call is not made explicitly, the finalize routine will be called automatically when the application exits. | | | |