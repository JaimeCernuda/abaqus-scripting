# About Defining Restrictions with Tosca Structure.gui

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | About Defining Restrictions with Tosca Structure.gui | | |  | | | |  | | --- | | For the definition of restrictions in Tosca Structure.gui consider the following remarks. | | |  | | --- | | See Also |  |  | | --- | |  | | In Other Guides | | DVCON\_TOPO | |   The `DVCON_TOPO` `ID_NAME` must be referenced in the `OPTIMIZE` command to activate the restriction.   ``` OPTIMIZE  ...   DVCON = name_of_dvcon_entry   ... END_ ```   Note:  The element group for a certain restriction should be a subset of the design element group. If this is not the case, SIMULIA Tosca Structure stops the optimization. |