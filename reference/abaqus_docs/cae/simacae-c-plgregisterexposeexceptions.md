# Displaying exceptions for imported plug-ins at startup

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Displaying exceptions for imported plug-ins at startup | | |  | | | |  | | --- | | By default, Abaqus/CAE does not display the exceptions associated with the import of plug-ins when you start the application. If you want to expose these exceptions for debugging purposes, set the environment variable ABQ\_PLUGIN\_DEBUG to 1 at a command prompt before launching Abaqus/CAE. When this environment variable is set, Abaqus/CAE provides more trackback information about plug-ins upon startup, including the location and nature of any failures that occur. | | | |