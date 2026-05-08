# test cell
from datetime import datetime as dt
from unittest.mock import patch


def test_solution_6() -> None:
    try:
        import solution_6
    except:
        raise ValueError("You did not execute your solution cell!")
    try:
        from solution_6 import datetime_validator
    except:
        raise ValueError("The module does not have the necessary function!")

    valid_cases = [
        ("January 15, 2022, 12:30:45", dt(2022, 1, 15, 12, 30, 45)),
        ("Jan 15, 2022, 12:30:45", dt(2022, 1, 15, 12, 30, 45)),
        ("  January 15, 2022, 12:30:45  ", dt(2022, 1, 15, 12, 30, 45)),
        ("Feb 29, 2024, 00:00:00", dt(2024, 2, 29, 0, 0, 0)),  # leap year check
    ]

    for _in, _out in valid_cases:
        _res = datetime_validator(_in)
        assert _res == _out, \
            f"Input `{_in}` should return `{_out}`, but returned `{_res}`."

    invalid_cases = [
        "2021-01-01 12:30:45",          # wrong format entirely
        "September 31, 2021, 14:45:15", # invalid date
        "Jan 15 2022 12:30:45",         # missing commas
        "",                             # empty string
    ]

    for bad in invalid_cases:
        _res = datetime_validator(bad)
        assert _res is None, \
            f"Input `{bad}` should return None, but returned `{_res}`."

    with patch("solution_6.datetime") as mock_datetime:
        mock_datetime.strptime.return_value = dt(2000, 1, 1, 0, 0, 0)
        result = datetime_validator("January 15, 2022, 12:30:45")
        assert result == dt(2000, 1, 1, 0, 0, 0)
        mock_datetime.strptime.assert_called()
        assert mock_datetime.strptime.called, \
            "You must use `datetime.strptime()` to parse the string."
