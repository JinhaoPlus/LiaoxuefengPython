print('包含中文的str')

print(ord('A'))

print(ord('中'))

print(chr(66))

print(chr(25991))

print('\u4e2d\u6587')

print('A'.encode('utf-8'))

print('中文'.encode('utf-8'))

print(b'ABC'.decode('ascii'))

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print(len('ABC'))

print(len(b'ABC'))

print(len('中文'))

print(len('中文'.encode('utf-8')))

print('Hello, %s' % 'world')

print('Hi, %s, you have $%d.' % ('Michael', 1000000))

print('%2d-%02d' % (3, 1))

print('%.2f' % 3.1415926)
