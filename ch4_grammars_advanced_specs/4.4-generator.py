L = [x * x for x in range(10)]
print(L)

G = (x * x for x in range(10))
for n in G:
    print(n)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


fib(20)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


for n in fib(6):
    print(n)


def triangles():
    n = [1]
    a = [1, 1]
    yield n
    yield a
    start = 1
    end = 1
    while True:
        L = []
        L.append(start)
        left = 0
        right = 0
        for i in range(len(a) - 1):
            left = a[i]
            right = a[i + 1]
            ele = left + right
            L.append(ele)
        L.append(end)
        a = L
        yield a

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
