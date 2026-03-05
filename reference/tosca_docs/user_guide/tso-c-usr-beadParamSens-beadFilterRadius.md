# Filtering (BEAD_FILTER_RADIUS)

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Filtering (BEAD\_FILTER\_RADIUS) | | |  | | | |  | | --- | | To avoid known problems of fluctuations in sensitivity values you should define a filter radius. | | |   ``` OPT_PARAM  ...  BEAD_FILTER_RADIUS = <filter_radius> , <unit_type> END_ ```   Default value is `4.0, REL`. The first item is the filter radius. Second option is whether the radius is relative to the medium edge length of elements in the design area (`REL`). The radius might also be set to an absolute value (`ABS`), for example:   ``` BEAD_FILTER_RADIUS = 5.0, ABS ``` |