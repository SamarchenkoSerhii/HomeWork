# Пользовательское исключение
class GroupLimitError(Exception):
    def __init__(self, message="В группе не может быть больше 10 студентов"):
        self.message = message
        super().__init__(self.message)

# Классы Human, Student и Group
class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} лет"

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Залікова книжка: {self.record_book}"

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError(f"Группа {self.number} уже содержит 10 студентов!")
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f"Група: {self.number}\nСтуденти:\n{all_students}"

# Пример использования
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')

try:
    gr.add_student(st1)
    gr.add_student(st2)
    # Добавляем студентов, чтобы достичь лимита
    for i in range(3, 12):
        gr.add_student(Student('Male', 20, f'Student{i}', f'Lastname{i}', f'RB{i}'))
    print(gr)
except GroupLimitError as e:
    print(f"Ошибка: {e}")