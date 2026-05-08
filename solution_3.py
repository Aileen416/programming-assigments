# solution cell

import datetime
from dataclasses import dataclass, field


@dataclass
class PersonAge:
    name: str
    job: str
    birthdate: datetime.date
    age: int = field(init=False)

    def compute_age(self) -> int:
        today = datetime.date.today()

        self.age = (
            today.year
            - self.birthdate.year
            - (
                (today.month, today.day)
                < (self.birthdate.month, self.birthdate.day)
            )
        )

        return self.age
