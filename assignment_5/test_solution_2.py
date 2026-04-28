# test cell
from unittest.mock import patch


def test_solution_2() -> None:
    try:
        import assignment_5.solution_2 as solution_2
    except:
        raise ValueError("You did not execute your solution cell!")
    try:
        from assignment_5.solution_2 import flatten_sequences
    except:
        raise ValueError("The module does not have the necessary function!")

    assert flatten_sequences([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert flatten_sequences([], []) == []
    assert flatten_sequences([1], []) == [1]
    assert flatten_sequences([], [5]) == [5]

    # Ensure new list is returned (no aliasing)
    a = [1, 2]
    b = [3, 4]
    result = flatten_sequences(a, b)
    assert result is not a
    assert result is not b

    with patch("solution_2.chain") as mock_chain:
        mock_chain.return_value = [9, 8]

        result = flatten_sequences([1], [2])
        assert result == [9, 8]

        mock_chain.assert_called_once()
        assert mock_chain.called, \
            "Do not manually concatenate lists. Use `itertools.chain`."
