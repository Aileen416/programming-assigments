# test cell
def test_solution_1() -> None:
    try:
        import assignment_5.solution_1 as solution_1
    except:
        raise ValueError("You did not execute your solution cell!")
    try:
        from assignment_5.solution_1 import assignment_points
    except:
        raise ValueError("The module does not have the necessary function!")

    test_cases = [(["Not Approved","Not Approved","Not Approved","Not Approved", \
        "Not Approved","Not Approved","Not Approved"], 0.0), \
        (["Approved","Not Approved","Not Approved","Not Approved", "Not Approved", \
            "Not Approved","Not Approved"], 1.0), \
        (["Approved","Approved","Not Approved","Not Approved", "Not Approved", \
            "Not Approved","Not Approved"], 2.0), \
        (["Approved","Approved","Approved","Not Approved", "Not Approved", \
            "Not Approved","Not Approved"], 4.0), \
        (["Approved","Approved","Approved","Approved", "Not Approved", "Not Approved", \
            "Not Approved"], 6.0), \
        (["Approved","Approved","Approved","Approved", "Approved","Not Approved", \
            "Not Approved"], 9.0), \
        (["Approved","Approved","Approved","Approved", "Approved","Approved", \
            "Not Approved"], 12.0), \
        (["Approved","Approved","Approved","Approved", "Approved","Approved", \
            "Approved"], 15.0), \
        (["Approved","Approved","Approved","Approved", "Approved","Approved", \
            "Approved", "Not Approved"], 0.0), \
        (["Approved","Approved","Approved","Approved", "Approved","Approved", \
            "Approved", "Approved"], 0.0)]

    for _in, _out in test_cases:
        _res = assignment_points(_in)
        assert _res == _out, f"The function received the input\n`{_in}` \
        and should return the value `{_out}`\n but returned the value `{_res}`."
