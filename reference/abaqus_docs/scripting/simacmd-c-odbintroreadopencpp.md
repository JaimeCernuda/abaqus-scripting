# Opening an output database

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Opening an output database | | |  | | | |  | | --- | | You use the openOdb method to open an existing output database. For example, the following statement opens the output database used by the Abaqus/CAE Visualization module tutorial:  ```     odb_Odb& odb = openOdb("viewer_tutorial.odb"); ```  After you open the output database, you can access its contents using the methods and members of the Odb object returned by the openOdb method. In the above example the Odb object is referred to by the variable `odb`. For a full description of the openOdb command, see [openOdb](.._SIMACAEKERRefMap_simaker-c-odbopenodbcommandcpp.md#simaker-odbodbsesopenodbcpp). | | | |