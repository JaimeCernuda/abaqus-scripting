# getFirstDialog

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | getFirstDialog | | |  | | | |  | | --- | | You must write the getFirstDialog method for your mode. | | |   The getFirstDialog method should return the first dialog box of the mode. In [Form example](simacus-c-modmodesformexample.md) a pointer to the form is passed into the dialog box constructor. The dialog box will use this pointer to access the mode's keywords.  If you want the same default values to appear every time you post the dialog box, you must call the setKeywordValuesToDefaults() method before returning the dialog box, as shown in [Form example](simacus-c-modmodesformexample.md). |