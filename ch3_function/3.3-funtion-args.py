def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5, 3))
print(power(5))


def add_end_e(L=[]):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end_e())
print(add_end_e())


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())
print(add_end())


def calc1(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc1([1, 2, 3]))


def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc2(1, 2, 3))
nums = (1, 2, 3)
print(calc2(*nums))


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')


def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')


def person(name, age, *args, city, job):
    print(name, age, args, city, job)


person('Jack', 24, 1, 2, city='Beijing', job='Engineer')
