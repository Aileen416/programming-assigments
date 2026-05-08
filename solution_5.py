# solution cell

from dataclasses import dataclass, field

from solution_4 import Student


@dataclass
class CourseRegister:
    name: str
    code: str
    list_registered_students: list[Student] = field(
        default_factory=list
    )

    def register(self, student: Student) -> None:
        if (
            isinstance(student, Student)
            and student not in self.list_registered_students
        ):
            self.list_registered_students.append(student)

    def remove(self, student: Student) -> None:
        if student in self.list_registered_students:
            self.list_registered_students.remove(student)
