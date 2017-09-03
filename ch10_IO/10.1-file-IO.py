f = open('/Users/jinhaoplus/Desktop/test.txt', 'r')
print(f.read())

try:
    f = open('/Users/jinhaoplus/Desktop/test.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

with open('/Users/jinhaoplus/Desktop/test.txt', 'r') as f:
    print(f.read())

with open('/Users/jinhaoplus/Desktop/test.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())

with open('/Users/jinhaoplus/Desktop/pic.png', 'rb') as f:
    print(f.read())

with open('/Users/jinhaoplus/Desktop/ch.txt', 'r', encoding="utf-8") as f:
    print(f.read())

with open('/Users/jinhaoplus/Desktop/ch.txt', 'w', encoding="utf-8") as f:
    f.write('Hello, world!')
