import math

from ch3_function.abstest import their_abs

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(1))
print(my_abs(-1))

print(their_abs(1))
print(their_abs(-1))


def nop():
    pass


nop()


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
print(move(100, 100, 60, math.pi / 6))

