# test cell
from unittest.mock import patch
from io import StringIO

def test_solution_3() -> None:
    try:
        import solution_3
    except:
        raise ValueError("You did not execute your solution cell!")
    try:
        from solution_3 import age_counter
    except:
        raise ValueError("The module does not have the necessary function!")

    test_cases = [("Alice = 25, Bob = 31, Charlie = 22, David = 22, Emma = 28, \
        Frank = 35, Grace = 25, Harry = 25, Isabella = 22, Jack = 27", \
            {25: 3, 31: 1, 22: 3, 28: 1, 35: 1, 27: 1}, "8"), \
        ("Sophia = 24, Olivia = 28, Liam = 32, Noah = 24, \
            Emily = 28, Ava = 24, Benjamin = 35, Mia = 31, Elijah = 28, Harper = 28", \
                {24: 3, 28: 4, 32: 1, 35: 1, 31: 1}, "7")]
    for _in, _out, _print in test_cases:
        with patch("sys.stdout", new=StringIO()) as fakeOutput:
            _res = age_counter(_in)
            assert _res == _out, f"The function received input\n`{_in}`\
                and should return the value `{_out}` of type \
    `{type(_out)}`\n but returned the value `{_res}` of type `{type(_res)}`."
            assert fakeOutput.getvalue().strip() == _print, f"For the received input \
    received input\n`{_in}`\nthe function should print \
    the value `{_print}` but printed the value `{fakeOutput.getvalue().strip()}`."
