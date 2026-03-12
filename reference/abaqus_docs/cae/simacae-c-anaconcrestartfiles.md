# Files required to restart an analysis

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Files required to restart an analysis | | |  | | | |  | | --- | | To restart an analysis, various files that were created by the previous analysis must be available in the directory from which you started the Abaqus/CAE session. | | |   Abaqus/Standard  * Output database (.odb) * Restart file (.res) * Model file (.mdl) * Part file (.prt) * State file (.stt)  Abaqus/Explicit  * Output database (.odb) * Restart file (.res) * Model file (.mdl) * Package file (.pac) * Part file (.prt) * State files (.abq and .stt) * Selected results file (.sel)  The restart analysis generates an error if any of these files are not available in the current directory. |