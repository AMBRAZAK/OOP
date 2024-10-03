class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = ["Введение в программирование"]
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
                and self.courses_in_progress
                and course in lecturer.courses_attached):
            if 0 <= grade <= 10:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return "Ошибка"

    def average_grade(self):
        total_grades = []
        for grades in self.grades.values():
            total_grades.extend(grades)
        return sum(total_grades) / len(total_grades) if total_grades else 0

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {self.average_grade():.1f}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.average_grade() < other.average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other,Student):
            return self.average_grade() <= other.average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_grade() == other.average_grade()
        return NotImplemented

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        total_grades = []
        for grades in self.grades.values():
            total_grades.extend(grades)
        return sum(total_grades) / len(total_grades) if total_grades else 0
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {self.average_grade():.1f}")

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() < other.average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() <= other.average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_grade() == other.average_grade()
        return NotImplemented

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

def average_student_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0

def average_lecturer_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0

# Примеры использования:
student_1 = Student('Ruoy', 'Eman', 'male')
student_1.courses_in_progress += ['Python', 'Git']

student_2 = Student('John', 'Doe', 'male')
student_2.courses_in_progress += ['Python', 'Git']

lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Another', 'Buddy')
lecturer_2.courses_attached += ['Python', 'Git']

reviewer = Reviewer('Some', 'Buddy')
reviewer.courses_attached += ['Python']

# Оценки студентам
reviewer.rate_hw(student_1, 'Python', 10)
reviewer.rate_hw(student_1, 'Python', 9.9)
reviewer.rate_hw(student_2, 'Python', 9.8)

# Оценки лекторам
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_2, 'Python', 9.9)
student_2.rate_lecturer(lecturer_2, 'Python', 9.8)

# Вывод информации
print(reviewer, "\n")
print(lecturer_1, "\n")
print(lecturer_2, "\n")
print(student_1, "\n")
print(student_2, "\n")

# Подсчет средней оценки
print("Средняя оценка за домашние задания у студентов по курсу Python:", average_student_grade([student_1, student_2], 'Python'))
print("Средняя оценка за лекции у лекторов по курсу Python:", average_lecturer_grade([lecturer_1, lecturer_2], 'Python'))