# The menu bar

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | The menu bar | | |  | | | |  | | --- | | The menu bar consists of the following three areas: persistent toolset menus, module menus, and the help menu. | | |   The persistent toolset menus and the help menu are shown when the application is first started, and they remain visible throughout the user’s session. The module menus reflect the current module and are swapped in and out as the user visits the various modules. You can access the menu bar using the following statement:   ``` menubar = getAFXApp().getAFXMainWindow().getMenubar() ``` |