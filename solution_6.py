# solution cell

class Word:
    def __init__(self, text: str) -> None:
        self.text = text

    def __eq__(self, other: "Word") -> bool:
        return self.text.lower() == other.text.lower()
