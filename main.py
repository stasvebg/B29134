class Student:
    # Атрибуты уровня класа
    group = 'B29234'
    education = 'ITStep'
    teacher= 'Evganiy'

    def __init__(self):
        print(id(self))

st1 = Student()
print(id(st1))

print(Student.group)
print(Student.teacher)
print(Student.education)