# test cell
def test_solution_1() -> None:
    try:
        import solution_1
    except:
        raise ValueError("You did not execute your solution cell!")
    try:
        from solution_1 import VolumeCalculator
    except:
        raise ValueError("The class does not exist. \
            Did you execute your solution cell?")

    assert 'volume' in dir(VolumeCalculator), 'Method volume() does not exist!'

    test_cases = [(None, None), (0, None), (-1, None), (1, 4.1887902047863905), \
        (2, 33.510321638291124)]
    for _in, _out in test_cases:
        _res = VolumeCalculator(_in)
        assert _res.volume() == _out, f"The volume function with input `{_in}` should \
            return the value `{_out}` of type `{type(_out)}`\n \
                but returned the value `{_res}` of type `{type(_res)}`."
