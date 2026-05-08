# test cell
from unittest.mock import patch


def test_solution_5() -> None:
    try:
        import solution_5
    except:
        raise ValueError("You did not execute your solution cell!")
    try:
        from solution_5 import CourseRegister
        from solution_4 import Student
        from solution_2 import Person
    except:
        raise ValueError("Your solution does not contain the right function!")
        
    assert 'CourseRegister' in dir(), 'Class CourseRegister does not exist!'
    assert 'register' in dir(CourseRegister), \
        'Class CourseRegister does not have method `register`'
    assert 'remove' in dir(CourseRegister), \
        'Class CourseRegister does not have method `remove`'

    c = CourseRegister('Applied object-oriented programming', 'EEN060')
    assert hasattr(c, 'name'), 'Class CourseRegister does not have property `name`.'
    assert hasattr(c, 'code'), 'Class CourseRegister does not have property `code`.'
    assert hasattr(c, 'list_registered_students'), \
        'Class CourseRegister does not have property `list_registered_students`.'
    assert isinstance(c.list_registered_students, list), \
        'The attribute list_enrolled_students is not a list'

    s1 = Student('John Doe', '201414202014', 'TIDSL')
    c.register(s1)
    assert len(c.list_registered_students) == 1

    p1 = Person('John Doe', '201414202014', 'Manager')
    c.register(p1)
    assert len(c.list_registered_students) == 1

    s2 = Student('Jane Doe', '201212202012', 'TKDES', 'Gibraltargatan')
    c.register(s2)
    assert len(c.list_registered_students) == 2

    c.remove(s1)
    assert len(c.list_registered_students) == 1

    c.remove(s1)
    assert len(c.list_registered_students) == 1

    c.remove(p1)
    assert len(c.list_registered_students) == 1

    c.register(s2)
    assert len(c.list_registered_students) == 1

    c = CourseRegister('Applied object-oriented programming', 'EEN060')
    assert isinstance(c.list_registered_students, list), \
        'The attribute list_enrolled_students is not a list'

    s1 = Student('John Doe', '201414202014_d', 'TIDSL')
    c.register(s1)
    assert len(c.list_registered_students) == 1

    p1 = Person('John Doe', '201414202014_d', 'Manager')
    c.register(p1)
    assert len(c.list_registered_students) == 1

    s2 = Student('Jane Doe', '201212202012_d', 'TKDES', 'Gibraltargatan')
    c.register(s2)
    assert len(c.list_registered_students) == 2

    c.remove(s1)
    assert len(c.list_registered_students) == 1

    c.remove(s1)
    assert len(c.list_registered_students) == 1

    c.remove(p1)
    assert len(c.list_registered_students) == 1
