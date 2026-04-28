# test cell
from unittest.mock import patch


def test_solution_5() -> None:
    try:
        import assignment_5.solution_5 as solution_5
    except:
        raise ValueError("You did not execute your solution cell!")
    try:
        from assignment_5.solution_5 import lottery_numbers
    except:
        raise ValueError("The module does not have the necessary function!")

    invalid_inputs = [
        (5, 50, -1),     # lower < 0
        (5, 0, 0),       # upper < 1
        (0, 10, 0),      # number < 1
        (5, 3, 0),       # not enough unique values
        (30, -1, 0),     # upper < 1 (also negative)
    ]
    for _in in invalid_inputs:
        _res = lottery_numbers(*_in)
        assert _res is None, \
            f"The function received the input `{_in}` and should return None, " \
            f"but returned `{_res}`."

    valid_inputs = [
        (5, 50, 10),
        (30, 100, 0),
        (2, 1, 0),       # edge case: population size == number
    ]
    for _in in valid_inputs:
        _res = lottery_numbers(*_in)
        assert _res is not None, f"The function returned None for valid input `{_in}`."
        assert len(_res) == _in[0], f"Wrong length for input `{_in}`. Output: `{_res}`."
        assert len(_res) == len(set(_res)), \
            f"Repeated elements for input `{_in}`. Output: `{_res}`."
        assert min(_res) >= _in[2], \
            f"Element below lower bound for input `{_in}`. Output: `{_res}`."
        assert max(_res) <= _in[1], \
            f"Element above upper bound for input `{_in}`. Output: `{_res}`."
