print(abs(-10))

print(abs)

f = abs
print(f)
print(f(-10))


def add(x, y, f):
    return f(x) + f(y)


print(add(1, 2, abs))
