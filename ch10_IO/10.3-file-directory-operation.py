import os

print(os.name)
print(os.uname())
for (envk, envv) in os.environ.items():
    print(envk + ":" + envv)

print("********************************************************")

for envk in os.environ:
    print(envk + ":" + os.environ.get(envk))

print("********************************************************")

print(os.path.abspath('.'))

path = os.path.join('/Users/jinhaoplus/Desktop', 'testdir')
print(path)
os.mkdir(path)
os.rmdir(path)

print(os.path.split('/Users/jinhaoplus/Desktop/test.txt'))
print(os.path.splitext('/Users/jinhaoplus/Desktop/test.txt'))

# os.rename('/Users/jinhaoplus/Desktop/test.txt', '/Users/jinhaoplus/Desktop/test.py')
# os.remove('/Users/jinhaoplus/Desktop/test.py')

print("********************************************************")

print(os.path.isdir('/Users/jinhaoplus/Music'))

files = [x for x in os.listdir('/Users/jinhaoplus/')]
print(files)

print("********************************************************")


def findfile(thepath, filename):
    for x in os.listdir(thepath):
        if os.path.isfile(os.path.join(thepath, x)) and filename in x:
            print(os.path.join(thepath, x))
        elif os.path.isdir(os.path.join(thepath, x)):
            y = os.path.join(thepath, x)
            findfile(y, filename)


print(r'请输入需要看的目录，例如：/Users/jinhaoplus/Desktop')
a = input()
print(r'请输入关键字')
b = input()
findfile(a, b)
