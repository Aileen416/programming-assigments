# test cell
def test_solution_4() -> None:
    try:
        import assignment_5.solution_4 as solution_4
    except:
        raise ValueError("You did not execute your solution cell!")
    try:
        from assignment_5.solution_4 import numbers_and_bools
    except:
        raise ValueError("The module does not have the necessary function!")

    test_cases = [([True, 10., False, 90., True, 45., True, 12, -1.2, 44.9], \
        ([True, False, True, True], [10.0, 90.0, 45.0, 12, -1.2, 44.9])), \
            (['this', 10., 'is', 90., 'another', 45., 'case', 12, 'test', 44.9], \
        ([], [10.0, 90.0, 45.0, 12, 44.9]))]
    for _in, _out in test_cases:
        _res = numbers_and_bools(_in)
        assert _res == _out, f"The function received the input\n`{_in}` \
        and should return the value `{_out}`\n but returned the value `{_res}`."
