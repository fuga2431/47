class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        marital_status = "женат" if self.is_married else "неженат"
        print(f"Я {self.fullname}, мне {self.age} лет, я {marital_status}.")

class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average_marks(self):
        if not self.marks:
            return 0
        return sum(self.marks.values()) / len(self.marks)

class Teacher(Person):
    base_salary = 30000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        bonus = 0
        if self.experience > 3:
            bonus = (self.experience - 3) * 0.05 * Teacher.base_salary
        return Teacher.base_salary + bonus

teacher = Teacher("Бфгдатова Челпонвй", 35, True, 5)
teacher.introduce_myself()
print(f"Зарплата учителя: {teacher.calculate_salary()}")

def create_students():
    students = [
        Student("Алыьбекова бегаим", 16, False, {"математика": 2, "русский язык": 3}),
        Student("райымкулова арууке", 17, False, {"математика": 4, "история": 5}),
        Student("бекханов ыйьан", 15, False, {"математика": 3, "физика": 4}),
    ]
    return students
students = create_students()
for student in students:
    student.introduce_myself()
    print(f"Оценки: {student.marks}")
    print(f"Средняя оценка: {student.average_marks():.2f}\n")















