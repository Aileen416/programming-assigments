# test cell
from unittest.mock import patch


def test_solution_5() -> None:
    try:
        import solution_5
    except:
        raise ValueError("You did not execute your solution cell!")
    try:
        from solution_5 import lists_intersection
    except:
        raise ValueError("The module does not have the necessary function!")

    test_cases = [((('test_1', 'test_2'), ('test_3', 'test_4')), None), \
        ((('test_1', 'test_2'), ['test_3', 'test_4']), None), \
            ((['a', 'b'], ['b', 'c']), ['b']), \
        ((['a', 'b'], ['a', 'b']), ['a', 'b']), ((['a', 'b'], ['c', 'd']), [])]

    for _in, _out in test_cases:
        _res = lists_intersection(*_in)
        if _out:
            assert set(_res) == set(_out), f"The function received the input\n`{_in}` \
            and should return the value `{_out}`\n but returned the value `{_res}`."
        elif _out == []:
            assert _out == _res, f"The function received the input\n`{_in}` \
            and should return the value `{_out}`\n but returned the value `{_res}`."            
        else:
            assert _res == None, f"The function received the input\n`{_in}` \
            and should return the value `{_out}`\n but returned the value `{_res}`."

    with patch('builtins.set') as mock_set:
        lists_intersection(['a', 'b'], ['c', 'd'])
    mock_set.assert_not_called()
