# test cell
from unittest.mock import patch


def test_solution_7() -> None:
    try:
        import solution_7
    except:
        raise ValueError("You did not execute your solution cell!")
    try:
        from solution_7 import validating_sum_of_squares
    except:
        raise ValueError("The module does not have the necessary function!")

    test_cases = [(['2', 'x', -10, 3.3, 'asd', None, 'b', 4.0], \
        [True, False, False, False, False, False, False, True]), \
        ([9, 'x', -9, None], [True, False, False, False])]

    for _in, _out in test_cases:
        _res = validating_sum_of_squares(_in)
        assert _res == _out, f"The function received the input\n`{_in}` \
        and should return the value `{_out}`\n but returned the value `{_res}`."
