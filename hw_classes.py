class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
            progress=", ".join(self.courses_in_progress)
            finished=", ".join(self.finished_courses)
            result =f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {str(self.grade_avg)}
Курсы в процессе изучения: {progress}
Завершенные курсы: {finished}"""
            return result

    def rate_lecturer(self, lecturer, course, grade):
        """
        Метод выставления оценок лекторам. По заданию № 2.
        """
        if grade>10 or grade<1:
            return 'Ошибка. Оценка должна быть от 1 до 10'
            
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка добавления оценки'

    @property
    def grade_avg(self):
        """
        Подсчет средней оценки среди всех предметов для студента
        """        
        grade_total=0
        grade_count=0

        for keys,vals in self.grades.items():
            grade_total +=sum(vals)
            grade_count +=len(vals)

        if grade_count>0:

            return grade_total/grade_count
        else:
            return 0

    def check_instance(self, other):
        if not isinstance(other, Student):
            raise TypeError("Операнд справа должен иметь тип Student")
        return True

    def __eq__(self, other):
        if self.check_instance(other):
            return self.grade_avg == other.grade_avg

    def __ne__(self, other):
        if self.check_instance(other):
            return self.grade_avg != other.grade_avg

    def __lt__(self, other):
        if self.check_instance(other):
            return self.grade_avg < other.grade_avg        

    def __le__(self, other):
        if self.check_instance(other):
            return self.grade_avg <= other.grade_avg

    def __gt__(self, other):
        if self.check_instance(other):
            return self.grade_avg > other.grade_avg
    
    def __ge__(self, other):
        if self.check_instance(other):
            return self.grade_avg >= other.grade_avg

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __str__(self):
        result =f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {str(self.grade_avg)}"
        return result
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached =[]
        self.grades = {}

    @property
    def grade_avg(self):
        """
        Подсчет средней оценки среди всех предметов
        К этому методу можно обращаться как к свойству
        """        
        grade_total=0
        grade_count=0

        for keys,vals in self.grades.items():
            grade_total +=sum(vals)
            grade_count +=len(vals)

        if grade_count>0:
            return grade_total/grade_count
        else:
            return 0

    def check_instance(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Операнд справа должен иметь тип Lecturer")
        return True

    def __eq__(self, other):
        if self.check_instance(other):
            return self.grade_avg == other.grade_avg

    def __ne__(self, other):
        if self.check_instance(other):
            return self.grade_avg != other.grade_avg

    def __lt__(self, other):
        if self.check_instance(other):
            return self.grade_avg < other.grade_avg        

    def __le__(self, other):
        if self.check_instance(other):
            return self.grade_avg <= other.grade_avg

    def __gt__(self, other):
        if self.check_instance(other):
            return self.grade_avg > other.grade_avg
    
    def __ge__(self, other):
        if self.check_instance(other):
            return self.grade_avg >= other.grade_avg
    
class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        """
        Метод выставления оценок студентам. По заданию он только у проверяющих.
        """
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка добавления оценки'

def avg_students_rating(students,course):
    """
    Задание 4.
    Подсчет средней оценки по студентам в рамках конкретного курса
    В качестве аргументов принимаем список студентов и название курса
    """
    total_grade = 0
    total_len = 0
    for student in students:
        total_grade += sum(student.grades[course])
        total_len += len(student.grades[course])
    
    if total_len!=0:
        return total_grade/total_len
    else:
        return 0

def avg_lecturers_rating(lecturers,course):
    """
    Задание 4.
    Подсчет средней оценки по лекторам в рамках конкретного курса
    В качестве аргументов принимаем список лекторов и название курса
    """
    total_grade = 0
    total_len = 0
    for lecturer in lecturers:
        total_grade += sum(lecturer.grades[course])
        total_len += len(lecturer.grades[course])
    
    if total_len!=0:
        return total_grade/total_len
    else:
        return 0

student_1 = Student('Steve', 'Davis', 'male')
student_1.courses_in_progress += ['Python','Git']
student_1.finished_courses += ['Tutorial']

student_2 = Student('Jessica', 'Flatcher', 'female')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ['Tutorial']

reviewer_1 = Reviewer('Harry', 'Walker')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Freddy', 'Moore')
reviewer_2.courses_attached += ['Python']

lecturer_1 = Lecturer("John", "Smith")
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer("Morty", "Addams")
lecturer_2.courses_attached += ['Python']

reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 4)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 9)

reviewer_2.rate_hw(student_1, 'Python', 8)
reviewer_2.rate_hw(student_1, 'Python', 6)
reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Python', 10)

student_1.rate_lecturer(lecturer_1,'Python',7)
student_1.rate_lecturer(lecturer_1,'Python',3)
student_1.rate_lecturer(lecturer_1,'Python',4)
student_1.rate_lecturer(lecturer_1,'Python',7)

student_2.rate_lecturer(lecturer_2,'Python',10)
student_2.rate_lecturer(lecturer_2,'Python',6)
student_2.rate_lecturer(lecturer_2,'Python',6)
student_2.rate_lecturer(lecturer_2,'Python',4)

print (student_1,'\n')

print (reviewer_1,'\n')

print (lecturer_1,'\n')

print ("Средние оценки первого лектора: ",lecturer_1.grade_avg,'\n')

print ("Средние оценки второго лектора:",lecturer_2.grade_avg,'\n')

print ("Проверка методов сравнения класов: ", lecturer_1<lecturer_2,'\n')

print ("Словарь оценок студента:", student_1.grades,'\n')

print ("Словарь оценок лектора:", lecturer_1.grades,'\n')

# проверка отдельных функций по 4 заданию:
rating = avg_students_rating([student_1,student_2],"Python")
print ("Задание 4. Средняя оценка студентов: ", rating, "\n")

rating = avg_lecturers_rating([lecturer_1,lecturer_2],"Python")
print ("Задание 4. Средняя оценка лекторов: ", rating, "\n")