from types import MethodType


class Student(object):
    pass


s = Student()

s.name = 'Michael'
print(s.name)


def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


s.set_age = MethodType(set_age, s)
s.set_age(20)
print(s.age)

s2 = Student()


# s2.set_age(25)


def set_score(self, score):
    self.score = score


Student.set_score = set_score
s.set_score(100)
print(s.score)

s2.set_score(80)
print(s2.score)


class Student(object):
    __slots__ = ('name', 'age')


s = Student()
s.name = 'Michael'
s.age = 25


# s.score = 99

class GraduateStudent(Student):
    pass


gs = GraduateStudent()
gs.score = 100
print(gs.score)
