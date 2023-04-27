
class Student: #Класс студент
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lecture(self, lecturer, course, grade): #Студент оценивает лектора
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _round_rate(self): #Считает среднее значение по оценкам студента
        sum_ = 0
        counter = 0
        for i in self.grades.values():
            for j in i:
                sum_ += j
                counter += 1
        res = sum_ / counter
        return res

    def __str__(self): #меняем принт для студента
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._round_rate()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other): #Делаем возможность сравнивать студентов по среднему баллу
        if not isinstance(other, Student):
            print('Это не студент!')
            return
        return self._round_rate() < other._round_rate()

class Mentor: #Класс ментор, родительский
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []




class Lecturer(Mentor): #Дочерний класс Лектор
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _round_rate(self): #Считает среднее значение по оценкам лектора
        sum_ = 0
        counter = 0
        for i in self.grades.values():
            for j in i:
                sum_ += j
                counter += 1
        res = sum_ / counter
        return res

    def __str__(self): #Меняем принт для лектора
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._round_rate()}'
        return res

    def __lt__(self, other): #Делаем возможность сравнивать лекторов по среднему баллу
        if not isinstance(other, Lecturer):
            print('Это не лектор!')
            return
        return self._round_rate() < other._round_rate()

class Reviewer(Mentor): #класс проверяющего
    pass

    def rate_hw(self, student, course, grade): #Проверяющий оценивает студентов
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):#Меняем принт для проверяющего
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

#Объявляем все подклассы
best_student = Student('Ruoy', 'Eman', 'your_gender')
student2 = Student('Vasya', 'Pupkin', 'man')
cool_reviewer = Reviewer('Some', 'Buddy')
reviewer2 = Reviewer('Name2', 'Lastname2')
lecturer1 = Lecturer('Name1', 'Lastname1')
lecturer2 = Lecturer('Name3', 'Lastname3')

#Проводим различные мероприятия, добавляем курсы, ставим оценки и т.д.
lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['Python']
lecturer1.courses_attached += ['Java']
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
student2.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']
best_student.rate_lecture(lecturer1, 'Python', 8)
best_student.rate_lecture(lecturer2, 'Python', 3)
best_student.rate_lecture(lecturer1, 'Python', 10)
best_student.rate_lecture(lecturer1, 'Java', 9)
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Java']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Java', 9)
cool_reviewer.rate_hw(student2, 'Python', 7)
cool_reviewer.rate_hw(student2, 'Java', 6)
students_list = [best_student, student2]
lecturers_list = [lecturer1, lecturer2]
def round_course(students, course): #Считаем средний балл по курсу у студентов
    counter = 0
    sum_ = 0
    for student in students:
        for key, value in student.grades.items():
            if key == course:
                counter += len(value)
                sum_ += sum(value)
    return sum_/counter

def round_rates(lecturers, course): #Считаем средний балл по курсу у лекторов
    counter = 0
    sum_ = 0
    for lecturer in lecturers:
        for key, value in lecturer.grades.items():
            if key == course:
                counter += len(value)
                sum_ += sum(value)
    return sum_/counter

#блок принтов
print(cool_reviewer)
print(reviewer2)
print(lecturer1)
print(lecturer2)
print(best_student)
print(student2)
print(lecturer1 > lecturer2)
print(best_student > student2)
print(best_student.grades)
print(round_course(students_list, 'Python'))
print(round_rates(lecturers_list, 'Python'))