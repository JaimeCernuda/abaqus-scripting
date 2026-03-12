# Toolbar and toolbox buttons

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Toolbar and toolbox buttons | | |  | | | |  | | --- | | The  AFXToolButton widget displays no text in its button, but the button generally has a tool tip. | | |   You group the buttons created by AFXToolButton into toolbars using AFXToolbarGroups or into toolboxes using  AFXToolboxGroups. AFXToolbarGroups and  AFXToolboxGroups provide visual grouping between buttons in the toolbar or toolbox. For example,  ``` # Create toolbar icons  # group = AFXToolbarGroup(self) AFXToolButton(group, '\tMy Module\nToolbar Button',     icon, sel)  # Create toolbox icons # group = AFXToolboxGroup(self)  AFXToolButton(group, '\tMy Module\nToolbox Button',     icon, sel) ``` |