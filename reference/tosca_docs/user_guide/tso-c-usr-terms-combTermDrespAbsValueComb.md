# About Combining Absolute Values of Responses

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | About Combining Absolute Values of Responses | | |  | | | |  | | --- | | This chapter shows how to combine absolute values of responses. | | |   Combining absolute values of response is done by operator type `VAR_OPER = SUB_ABS`. To get the absolute value of the difference of two terms (`DRESP_1` and `DRESP_2`) the design response definition is as follows:   ``` DRESP  ID_NAME  = .....  DEF_TYPE = OPER  VAR_OPER = SUB_ABS  VAR_A    = DRESP_1  VAR_B    = DRESP_2 END_ ``` |