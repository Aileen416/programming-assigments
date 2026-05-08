# test cell
from unittest.mock import patch


def test_solution_4() -> None:
    try:
        import solution_4
    except:
        raise ValueError("You did not execute your solution cell!")
    try:
        from solution_4 import Student
        from solution_2 import Person
    except:
        raise ValueError("Your solution does not contain the right function!")

    assert 'print' in dir(Student), 'Class Student does not have a method `print`.'

    s = Student('John Doe', '201414202014', 'TIDSL')
    assert isinstance(s, Person), 'The class Student is not a child class of the class Person'
    with patch('solution_4.print') as mock_print:
        s.print()
    mock_print.assert_called_once_with('John Doe\tStudent\t201414202014\tTIDSL')

    s = Student('John Doe', '201414202014', 'TKDES', 'Gibraltargatan')
    with patch('solution_4.print') as mock_print:
        s.print()
    mock_print.assert_called_once_with('John Doe\tStudent\t201414202014\tGibraltargatan\tTKDES')
    assert hasattr(s, 'program'), 'The object does not seem to have the property `program`'
