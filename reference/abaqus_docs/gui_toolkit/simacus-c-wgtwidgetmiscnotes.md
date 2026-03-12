# Notes and warnings

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Notes and warnings | | |  | | | |  | | --- | | The AFXNote widget provides a convenient way to display notes or warnings in a dialog box. | | |   AFXNote displays either the word Note or the word Warning in a bold font. AFXNote also aligns messages that contain more than one line. For example,  ``` AFXNote(parent, 'This is an AFXNote information note\n'     'that wraps on two lines.') AFXNote(parent, 'This is an AFXNote warning note!', NOTE_WARNING) ``` Figure 1. An example of a note and a warning from AFXNote. |