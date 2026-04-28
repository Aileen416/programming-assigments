# test cell
def test_solution_2() -> None:
    try:
        import solution_2
    except:
        raise ValueError("You did not execute your solution cell!")
    try:
        from solution_2 import reverse_lower_and_upper_case
    except:
        raise ValueError("The module does not have the necessary function!")

    test_cases = [(['test', 'PRACTICE'], ['TEST', 'practice']), \
        (['TEST', 'practice'], ['test', 'PRACTICE']), \
        (['TEST', 'PRACTICE'], ['test', 'practice']), \
        (['resource granted', 'RESOURCE NOT GRANTED', 'grattis'], \
        ['RESOURCE GRANTED', 'resource not granted', 'GRATTIS'])]

    for _in, _out in test_cases:
        _res = reverse_lower_and_upper_case(_in)
        assert _res == _out, f"The function received the input\n`{_in}` \
        and should return the value `{_out}`\n but returned the value `{_res}`."
