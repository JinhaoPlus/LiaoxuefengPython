names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

summary = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    summary = summary + x
print(summary)

summary = 0
for x in range(101):
    summary = summary + x
print(summary)

summary = 0
n = 99
while n > 0:
    summary = summary + n
    n = n - 2
print(summary)

n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
