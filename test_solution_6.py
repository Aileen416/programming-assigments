# test cell
def test_solution_6() -> None:
    try:
        import solution_6
    except:
        raise ValueError("You did not execute your solution cell!")
    try:
        from solution_6 import Word
    except:
        raise ValueError("The module does not have the necessary function!")

    w = Word("ha")
    assert hasattr(w, "text"), "Word must have an attribute `text`."
    assert w.text == "ha", "`text` must store the given input string."

    assert Word("ha") == Word("HA"), "Equality must ignore case."
    assert Word("ha") != Word("eh"), "Different words must not be equal."

    assert (Word("ha") == Word("ha")) is True
