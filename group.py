from student import Student

class Group:
    def __init__(self, name):
        self.name = name
        self.students = set()

    def add_student(self, student):
        if len(self.students) >= 10:
            raise ValueError('The group cannot have more than 10 students.')
        self.students.add(student)

    def delete_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                self.students.remove(student)
                return
        raise ValueError(f'Student with last name "{last_name}" not found.')

    def find_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        return f"Group {self.name}:\n" + "\n".join([str(student) for student in self.students])