
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _round_rate(self):
        sum_ = 0
        counter = 0
        for i in self.grades.values():
            for j in i:
                sum_ += j
                counter += 1
        res = sum_ / counter
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._round_rate()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Это не студент!')
            return
        return self._round_rate() < other._round_rate()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}



class Lecturer(Mentor):
    def __int__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _round_rate(self):
        sum_ = 0
        counter = 0
        for i in self.grades.values():
            for j in i:
                sum_ += j
                counter += 1
        res = sum_ / counter
        return res

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._round_rate()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Это не лектор!')
            return
        return self._round_rate() < other._round_rate()

class Reviewer(Mentor):
    pass

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
student2 = Student('Vasya', 'Pupkin', 'man')
cool_reviewer = Reviewer('Some', 'Buddy')
reviewer2 = Reviewer('Name2', 'Lastname2')
lecturer1 = Lecturer('Name1', 'Lastname1')
lecturer2 = Lecturer('Name3', 'Lastname3')


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
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(student2, 'Python', 7)




print(cool_reviewer)
print(reviewer2)
print(lecturer1)
print(lecturer2)
print(best_student)
print(student2)
print(lecturer1 > lecturer2)
print(best_student > student2)