# Coordinate Systems

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Coordinate Systems | | |  | | | |  | | --- | | Some remarks concerning coordinate systems are summarized within this section. | | |   SIMULIA Tosca Structure reads the coordinate systems that are defined with the ANSYS® command `LOCAL`:   ``` LOCAL, R5.0, Type, NSCY, CSTYP, VAL1, VAL2, VAL3 ```   The coordinate systems can be referenced in SIMULIA Tosca Structure as `CS_*` where `*` is the id number `NSCY` of the coordinate system. |