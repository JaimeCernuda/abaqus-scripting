# getFirstStep

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | getFirstStep | | |  | | | |  | | --- | | You must always write the getFirstStep method for your mode. The getFirstStep method should return the first step of the mode. | | |   In [Procedure example](simacus-c-modprocedureexample.md) a pointer to the procedure is passed into the dialog box constructor. The dialog box will use this pointer to access the mode's keywords.  If you want the same default values to appear every time you post the dialog box, you must call the setKeywordValuesToDefaults() method before returning the dialog box, as shown in [Procedure example](simacus-c-modprocedureexample.md). |