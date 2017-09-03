class Animal:
    def run(self):
        print('Animal is running...')


animal = Animal()
print(type(animal))
print(type(animal.run))


def fn():
    pass


print(type(fn))

print(type(abs))


class Dog(Animal):
    pass


class Husky(Dog):
    pass


husky = Husky()
dog = Dog()

print(type(husky))
print(isinstance(husky, Husky))
print(isinstance(husky, Dog))
print(isinstance(husky, Animal))
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(dog, Husky))

print(isinstance(dog, (Animal, Dog, Husky)))

for d in dir('ABC'):
    print(d)


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


myobject = MyObject()
print(hasattr(myobject, 'x'))
print(getattr(myobject, 'x'))
print(myobject.x)
print(getattr(myobject, 'y', 404))
print(hasattr(myobject, 'y'))
setattr(myobject, 'y', 19)
print(hasattr(myobject, 'y'))
print(getattr(myobject, 'y'))
print(hasattr(myobject, 'power'))
print(getattr(myobject, 'power'))
fn = getattr(myobject, 'power')
print(fn())
