# test cell
from unittest.mock import patch


def test_solution_1() -> None:
    try:
        import solution_1
    except:
        raise ValueError("You did not execute your solution cell!")
    try:
        from solution_1 import group_by_first_letter
    except:
        raise ValueError("The module does not have the necessary function!")

    words = ["apple", "banana", "apricot", "Berry", "", "blue"]

    result = group_by_first_letter(words)

    expected = {
        "a": ["apple", "apricot"],
        "b": ["banana", "blue"],
        "B": ["Berry"],
    }

    assert result == expected, \
        f"Expected {expected}, but got {result}."

    assert group_by_first_letter([]) == {}

    with patch("solution_1.defaultdict") as mock_defaultdict:
        mock_instance = mock_defaultdict.return_value
        mock_instance.__getitem__.side_effect = lambda key: []
        mock_instance.items.return_value = []

        group_by_first_letter(["x"])

        mock_defaultdict.assert_called_once()
        assert mock_defaultdict.called, \
            "Do not manually implement dictionary initialization logic. Use `defaultdict`."
