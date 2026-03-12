# Header files

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Header files | | |  | | | |  | | --- | | To use a class in a C++ program, the relevant header files must be included. The naming convention followed is that the file name is the same as the name of the class declared in the header file. For example, the odb\_FieldValue object is declared in the file odb\_FieldValue.h. The file odb\_API.h includes all the header files required to use the API. Other header files must be included to use some classes: | | |   * To access material objects you must include the file odb\_MaterialTypes.h. * To access section objects you must include the file odb\_SectionTypes.h. |