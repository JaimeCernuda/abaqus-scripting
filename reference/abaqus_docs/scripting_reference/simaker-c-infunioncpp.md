# Union object

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Union object | | |  | | | |  | | --- | | An odb\_Union object is used to determine the type of variable used when an object allows multiple variable types. The odb\_Union object can have a value that is either a SymbolicConstant, Int, Float, Double, Boolean, or String.   * [type(...)](#simaker-infunionuniontypecpp) | | |     type(...) This method returns the current type of the odb\_Union object.  Prototype  ``` odb_UnionType type(); ```  Arguments None.  Return value The type of the odb\_Union object. Possible values are odb\_UNION\_INT, odb\_UNION\_FLOAT, odb\_UNION\_DOUBLE, odb\_UNION\_BOOL, and odb\_UNION\_STRING.  Exceptions odbException |