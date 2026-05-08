# solution cell

from solution_2 import Person


class Student(Person):
    def __init__(
        self,
        name: str,
        person_number: str,
        program: str,
        address: str | None = None
    ) -> None:
        super().__init__(
            name,
            "Student",
            person_number,
            address
        )

        self.program = program

    def print(self) -> None:
        result = super().__repr__() + "\t" + self.program
        print(result)
