classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])

classmates.append('Adam')
print(classmates)

classmates.insert(1, 'Jack')
print(classmates)

classmates.pop()
print(classmates)

classmates.pop(1)
print(classmates)

classmates[0] = 'Sarah'
print(classmates)

L = ['Apple', 123, True]
print(L)

L = []
print(len(L))

s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))

classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
print(len(classmates))
print(classmates[0])

s = ()
print(len(s))

t = (1,)
print(t)

t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

a = ['c', 'b', 'a']
print(a)
a.sort()
print(a)
