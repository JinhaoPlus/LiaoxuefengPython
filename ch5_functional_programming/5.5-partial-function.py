import functools

print(int('1001'))

print(int('1001', base=2))
print(int('1010', base=2))
print(int('1111', base=2))


def int2(str, base=2):
    return int(str, base)


print(int2('1001'))
print(int2('1010'))
print(int2('1111'))

int2 = functools.partial(int, base=2)
print(int2('1001'))
print(int2('1010'))
print(int2('1111'))
