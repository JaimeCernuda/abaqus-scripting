# Optimizing the Hub Model

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Optimizing the Hub Model | | |  | | | |  | | --- | | This example illustrates the shape optimization of a hub of a wind turbine system. | | |   Define a link condition (LINK\_SHAPE) for the SURF\_CYCLIC\_PLANE-symmetry: ``` LINK_SHAPE  ID_NAME          = LINK_SHAPE_1_SYMMETRY_CONTROL_3  MAIN           = MAX  CLIENT           = SURF_CYCLIC_PLANE_SYM  CYCLIC_SYM_START = 0., 0. , 1.  CLIENT_DIR       = 1.,0.,0.  CS               = CS_0  TOL              = 0.1  ANGLE            = 120. END_ ```  The result looks as follows:   The front of the hub looks as follows: |