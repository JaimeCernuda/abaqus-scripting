# Creating a new output database

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Creating a new output database | | |  | | | |  | | --- | | You use the Odb constructor to create a new, empty Odb object.  ```   odb_Odb& odb = Odb("myData","derived data",      "test problem", "testWrite.odb"); ```  For a full description of the Odb command, see [Odb object](.._SIMACAEKERRefMap_simaker-c-odbcpp.md). Abaqus creates the RootAssembly object when you create or open an output database. | | |   You use the save method to save the output database.   ```   odb.save(); ```   For a full description of the save command, see [save()](.._SIMACAEKERRefMap_simaker-c-odbcpp.md#simaker-odbsavecpp). |