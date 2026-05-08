# test cell
from unittest.mock import patch


def test_solution_2() -> None:
    try:
        import solution_2
    except:
        raise ValueError("You did not execute your solution cell!")
    try:
        from solution_2 import Person
    except:
        raise ValueError("The class does not exist. \
            Did you execute your solution cell?")

    p = Person('John Doe', 'Manager', '201414202014')

    with patch('builtins.print') as mock_print:
        s = str(p)
    mock_print.assert_not_called()

    test_cases = [(('John Doe', 'Manager', '201414202014'), \
        'John Doe\tManager\t201414202014'), \
        (('Jane Doe', 'Supervisor', '201212202012', 'Gibraltargatan'), \
            'Jane Doe\tSupervisor\t201212202012\tGibraltargatan'), \
        (('Jane Doe', 'Supervisor', '201212202012', 'Gibraltargatan'), \
        'Jane Doe\tSupervisor\t201212202012\tGibraltargatan')]
    for _in, _out in test_cases:
        _res = Person(*_in)
        assert repr(_res) == _out, f"The Person class with input `{_in}` should be \
            displayed as the value `{_out}` of type `{type(_out)}`\n \
                but returned the value `{_res}` of type `{type(_res)}`."
