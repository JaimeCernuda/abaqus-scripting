# Creating a new output database

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Creating a new output database | | |  | | | |  | | --- | | You use the Odb constructor to create a new, empty Odb object.  ``` odb = Odb(name='myData',     analysisTitle='derived data',     description='test problem',     path='testWrite.odb') ```  For a full description of the Odb command, see [Odb object](.._SIMACAEKERRefMap_simaker-c-odbpyc.md). Abaqus creates the RootAssembly object when you create or open an output database. | | |   You use the save method to save the output database.   ``` odb.save() ```   For a full description of the save command, see [save()](.._SIMACAEKERRefMap_simaker-c-odbpyc.md#simaker-odbsavepyc). |