# test cell
from unittest.mock import patch
import math

def test_solution_3() -> None:
    try:
        import assignment_5.solution_3 as solution_3
    except:
        raise ValueError("You did not execute your solution cell!")
    try:
        from assignment_5.solution_3 import gm_median
    except:
        raise ValueError("The module does not have the necessary function!")

    test_cases = [
        ([], None),                       # empty list
        ([0, -1, -2.5, "x"], None),       # all numeric <= 0
        (["x", 0, -3, "7"], None),        # strings ignored, <=0 ignored → nothing left

        ([2, "x", 0, 8, -3, "5"], (4.0, 5.0)),      # valid numbers [2, 8]
        (["x", 7, 0, -1], (7.0, 7.0)),              # single valid number
        ([0.5, "ignore", 2.0], (1.0, 1.25)),        # float handling
    ]

    for _in, _out in test_cases:
        _res = gm_median(_in)
        
        if _out == None:
            assert _res is None, f"The function with input `{_in}` should return None, \
        but returned `{_res}`."
            continue

        assert _res is not None, f"The function with input `{_in}` returned None unexpectedly."

        cond1 = math.isclose(_res[0], _out[0], abs_tol=1e-1)
        cond2 = math.isclose(_res[1], _out[1], abs_tol=1e-1)

        assert cond1 and cond2, f"The function with input `{_in}` should return the value \
    `{_out}` of type `{type(_out)}`\n but returned the value `{_res}` of type `{type(_res)}`."

    with patch("solution_3.geometric_mean") as mock_gm, \
        patch("solution_3.median") as mock_med:

        mock_gm.return_value = 123.0
        mock_med.return_value = 456.0
        assert gm_median([1, 2, 3]) == (123.0, 456.0)
        mock_gm.assert_called_once()
        mock_med.assert_called_once()
        assert (
            mock_gm.called and mock_med.called
        ), "Do not use `import statistics`. Import the specific functions from the module."
