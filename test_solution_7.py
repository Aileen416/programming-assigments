# test cell
from unittest.mock import patch


def test_solution_7() -> None:
    try:
        import solution_7
    except:
        raise ValueError("You did not execute your solution cell!")
    try:
        from solution_7 import most_common_words
    except:
        raise ValueError("The module does not have the necessary function!")

    assert most_common_words([], 3) is None
    assert most_common_words(["a", "b"], 0) is None

    words = ["apple", "banana", "apple", "orange", "banana", "apple"]

    result = most_common_words(words, 2)
    expected = [("apple", 3), ("banana", 2)]

    assert result == expected, \
        f"Expected {expected}, but got {result}."

    # n larger than unique words
    result = most_common_words(words, 10)
    assert len(result) == 3

    with patch("solution_7.Counter") as mock_counter:
        mock_instance = mock_counter.return_value
        mock_instance.most_common.return_value = [("x", 5)]

        result = most_common_words(["x", "x"], 1)
        assert result == [("x", 5)]

        mock_counter.assert_called_once()
        mock_instance.most_common.assert_called_once()

        assert mock_counter.called, \
        "Do not use `import collections`. Import the specific functions from the module."
