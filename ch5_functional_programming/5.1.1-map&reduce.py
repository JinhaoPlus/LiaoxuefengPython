from functools import reduce


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print(list(r))


def add(x, y):
    return x + y


print(reduce(add, list(range(1, 101))))


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(fn, map(char2num, s))


print(str2int('100'))


def normalize(name):
    return name[0:1].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(L):
    return reduce(lambda x, y: x * y, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def str2float(s):
    s = s.split('.')
    s1 = reduce(lambda x, y: x * 10 + y, map(char2num, s[0]))
    s2 = reduce(lambda x, y: x * 10 + y, map(char2num, s[1])) / 10 ** len(s[1])
    return s1 + s2


print('str2float(\'123.456\') =', str2float('123.456'))
