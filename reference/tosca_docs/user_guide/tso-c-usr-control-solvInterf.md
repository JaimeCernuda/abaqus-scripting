# Solver Interface

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Solver Interface | | |  | | | |  | | --- | | Solver interface related topics are discussed within this section. | | |   Entering the type of solver to be used (`--solver <solvername>`) automatically activates the interface according to the type of solver. If no solver interface is specified in the command-line, the default solver is used which is already set in the SIMULIA Tosca Structure configuration. The typical SIMULIA Tosca Structure call with a specific solver interface is:   ``` ToscaStructure.[bat|sh] -j <jobname> --solver <solvername> ```   Note, that only licensed interfaces can be activated. |