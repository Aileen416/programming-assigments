# test cell
from datetime import datetime


def test_solution_6() -> None:
    try:
        import assignment_5.solution_6 as solution_6
    except:
        raise ValueError("You did not execute your solution cell!")
    try:
        from assignment_5.solution_6 import person_number_validate
    except:
        raise ValueError("The module does not have the necessary function!")

    test_cases = [
        # Valid
        ('8112289874', True),
        ('3101057853', True),

        # Invalid checksum
        ('3101057851', False),

        # Invalid month
        ('9913211234', False),   # month 13
        ('1200301234', False),   # month 00

        # Invalid day for 30-day month
        ('1211310123', False),   # Nov 31

        # Invalid February dates
        ('1202301212', False),   # Feb 30
        ('0002301234', False),   # Feb 30

        # Clearly invalid day
        ('1200321234', False),   # day 32
    ]

    for _in, _out in test_cases:
        _res = person_number_validate(_in)
        assert _res == _out, f"The function received the input\n`{_in}` \
        and should return the value `{_out}`\n but returned the value `{_res}`."
