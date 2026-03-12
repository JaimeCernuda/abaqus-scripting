# Section object

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| |  |  | | --- | --- | | Section object | | |  | | | |  | | --- | | The Section object defines the properties of a section. The Section object is the abstract base type for other Section objects. The Section object has no explicit constructor. The methods and members of the Section object are common to all objects derived from the Section.  This page discusses:   * [Access](#simaker-c-sectioncpp__simaker-c-sectioncpp-s-cppaccess1) * [Members](#simaker-c-sectioncpp-t-pymembersect1) | | |   Access  ``` sectionApi.sections()[name] ```  Members The Section object has the following member:  Prototype  ``` odb_String name() const; ```  name  An odb\_String specifying the repository key. |