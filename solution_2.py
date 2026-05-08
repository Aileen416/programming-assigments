# solution cell

class Person:
    def __init__(
        self,
        name: str,
        role: str,
        person_number: str,
        address: str | None = None
    ) -> None:
        self.name = name
        self.role = role
        self.person_number = person_number
        self.address = address

    def __repr__(self) -> str:
        values = [
            self.name,
            self.role,
            self.person_number,
            self.address
        ]

        return "\t".join(
            str(value) for value in values if value is not None
        )
