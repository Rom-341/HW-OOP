class Student:  # определяем класс студента
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades_student = {}
        self.students_lst = []

    # определяем метод для расчета оценки за лекцию, которая
    # выставляется студентом лектору и хранится
    # в словаре класса Lecturer

    def rate_lecturer(self, lecturer, course, grade):
        if (
                isinstance(lecturer, Lecturer)
                and course in self.courses_in_progress
                and course in lecturer.courses_attached
                and grade >= 0
        ):
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'

    # находим среднюю оценку за домашние задания
    def avg_grade(self):
        if self.grades_student:
            grades_lst = sum(self.grades_student.values(), start=[])
            return round(sum(grades_lst) / len(grades_lst), 1)
        else:
            return "Нет оценок"

    # определяем метод для печати студента
    def __str__(self):
        return (
                f"Имя: {self.name}" + "\n"
                f"Фамилия: {self.surname}" + "\n"
                f"Средняя оценка за домашние задания: {self.avg_grade()}" + "\n"
                f"Курсы в процессе изучения: {self.courses_in_progress}" + "\n"
                f"Завершенные курсы: {self.finished_courses}" + "\n"
        )

# сравнение студентов по средней оценке за домашние задания
    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()


# определяем класс ментора
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# определяем дочерний класс лектор
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lecturer = {}

# средняя оценка за лекции
    def avg_grade(self):
        if self.grades_lecturer:
            grades_lst = sum(self.grades_lecturer.values(), start=[])
            return round(sum(grades_lst) / len(grades_lst), 1)
        else:
            return "Нет оценок"

    # определяем метод для печати лекторов
    def __str__(self):
        return (
                f"Имя: {self.name}" + "\n"
                f"Фамилия: {self.surname}" + "\n"
                f"Средняя оценка за лекции: {self.avg_grade()}" + "\n"
        )

# сравнение студентов по средней оценке за домашние задания
    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()


# определяем дочерний класс экспертов
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    # определяем метод для печати экспертов
    def __str__(self):
        return (
                f"Имя: {self.name}" + "\n"
                f"Фамилия: {self.surname} " + "\n"
        )

    # определяем метод для расчета оценки за домашние задания,
    # которая выставляется экспертом и хранится в словаре
    # класса Student
    def rate_hw(self, student, course, grade):
        if (
                isinstance(student, Student)
                and course in self.courses_attached
                and course in student.courses_in_progress
        ):
            if course in student.grades_student:
                student.grades_student[course] += [grade]
            else:
                student.grades_student[course] = [grade]
        else:
            return 'Ошибка'


some_student1 = Student("Roy", "Eman", "male")
some_student1.courses_in_progress += ["Python"]
some_student1.courses_in_progress += ["Git"]
some_student1.finished_courses += ["Введение в программирование"]

some_student2 = Student("Jon", "Pyman", "male")
some_student2.courses_in_progress += ["Python"]
some_student2.courses_in_progress += ["Git"]
some_student2.finished_courses += ["Введение в программирование"]

some_reviewer = Reviewer("Some", "Buddy")
some_reviewer.courses_attached += ["Python"]
some_reviewer.courses_attached += ["Git"]
some_reviewer.rate_hw(some_student1, "Python", 5)
some_reviewer.rate_hw(some_student1, "Git", 4)
some_reviewer.rate_hw(some_student2, "Python", 3)
some_reviewer.rate_hw(some_student2, "Git", 3)

some_lecturer1 = Lecturer("Jack", "Gog")
some_lecturer1.courses_attached += ["Python"]
some_lecturer1.courses_attached += ["Git"]

some_lecturer2 = Lecturer("Иван", "Иванов")
some_lecturer2.courses_attached += ["Python"]
some_lecturer2.courses_attached += ["Git"]

some_student1.rate_lecturer(some_lecturer1, "Python", 2)
some_student1.rate_lecturer(some_lecturer2, "Python", 6)
some_student1.rate_lecturer(some_lecturer1, "Git", 5)

some_student2.rate_lecturer(some_lecturer1, "Python", 1)
some_student2.rate_lecturer(some_lecturer2, "Python", 5)
some_student2.rate_lecturer(some_lecturer1, "Git", 4)

print(some_reviewer)
print(some_lecturer1)
print(some_lecturer2)
print(some_student1)
print(some_student2)
print(some_student1.avg_grade() < some_student2.avg_grade())
print(some_lecturer1.avg_grade() < some_lecturer2.avg_grade())

# расчет средней оценки за всех студентов
students_lst = [some_student1, some_student2]


def average_rating_for_all_students(students_lst, course):
    all_grade = []
    if students_lst:
        for student in students_lst:
            for key, grade in student.grades_student.items():
                if key == course:
                    all_grade += grade
                    # print(all_grade)
        return round(sum(all_grade) / len(all_grade), 1)


print(average_rating_for_all_students(students_lst, "Python"))
print(average_rating_for_all_students(students_lst, "Git"))


lecturer_lst = [some_lecturer1, some_lecturer2]


def average_rating_for_all_lecturer(lecturer_lst, course):
    all_grade_1 = []
    if lecturer_lst:
        for lecturer in lecturer_lst:
            for key, grade in lecturer.grades_lecturer.items():
                if key == course:
                    all_grade_1 += grade
                    # print(all_grade_1)
        return round(sum(all_grade_1) / len(all_grade_1), 1)


print(average_rating_for_all_lecturer(lecturer_lst, "Python"))
print(average_rating_for_all_lecturer(lecturer_lst, "Git"))
