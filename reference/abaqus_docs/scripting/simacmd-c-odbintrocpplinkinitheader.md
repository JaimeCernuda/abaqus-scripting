# Header file location

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Header file location | | |  | | | |  | | --- | | The header files required to compile a program that accesses the C++ interface are located in the following directories: | | |   Linux  abaqus\_dir/code/include  Windows  abaqus\_dir\code\include  where abaqus\_dir is the name of the directory in which Abaqus is installed. To determine the location of abaqus\_dir at your site, type `abaqus whereami` at an operating system prompt.  Only odb\_API.h must be included to access the C++ interface, but the path to the header files must be provided during compilation. |