from types import MethodType

class Student(object):
    name = 'Student'

    def __init__(self, name):
        self.name = name


s = Student('Bob')
s.score = 90

print(Student.name)
print(s.name)
print(s.score)
delattr(s, 'name')
print(s.name)
