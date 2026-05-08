# test cell
import dataclasses
from datetime import date
from unittest.mock import patch

def test_solution_3() -> None:
    try:
        import solution_3
    except:
        raise ValueError("You did not execute your solution cell!")
    try:
        from solution_3 import PersonAge
    except:
        raise ValueError("The class does not exist. Did you execute your solution cell?")

    assert dataclasses.is_dataclass(PersonAge), "The class is not a dataclass!"
    assert any(f.name == "age" and f.init is False for f in dataclasses.fields(PersonAge))
    
    p = PersonAge('John Doe', 'Manager', date(1990, 11, 15))
    assert hasattr(p, 'name'), 'Class PersonAge does not have property `name`.'
    assert hasattr(p, 'job'), 'Class PersonAge does not have property `job`.'
    assert hasattr(p, 'age') == False, 'Class PersonAge should not have property `age`.'
    p.compute_age()
    assert hasattr(p, 'age'), 'Class PersonAge does not have property `age`.'
    assert p.age == 35, f"The computed age `{p.age}` is incorrect!"

    with patch('__main__.print') as mock_print:
        s = str(p)
    mock_print.assert_not_called()

    person1 = PersonAge('John Doe', 'Manager', date(1990, 11, 15))
    person1.compute_age()
    person2 = PersonAge('Jane Doe', 'Manager', date(1980, 11, 15))
    person2.compute_age()
    assert person1.age < person2.age, "The age computation seems incorrect!"
