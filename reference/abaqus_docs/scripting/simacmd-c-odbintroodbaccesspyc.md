# Making the Odb commands available

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Making the Odb commands available | | |  | | | |  | | --- | | To make the Odb commands available to your script, you first need to import the odbAccess module using the following statements:  ``` from odbAccess import * from abaqusConstants import * ```  To make the material and section Odb commands available to your script, you also need to import the relevant module using the following statements:  ``` from odbMaterial import * from odbSection import * ``` | | | |