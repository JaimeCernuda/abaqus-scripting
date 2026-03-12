# Making the Odb commands available

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Making the Odb commands available | | |  | | | |  | | --- | | To make the Odb commands available to your program, you first need to include the output database interface classes using the following statement:  ``` #include <odb_API.h> ```  To make the material and section Odb commands available to your program, you also need to include their output database classes:  ``` #include <odb_MaterialTypes.h> #include <odb_SectionTypes.h> ``` | | | |