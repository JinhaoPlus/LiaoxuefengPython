class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    pass


dog = Dog()
cat = Cat()

dog.run()
cat.run()

a = list()  # a是list类型
b = Animal()  # b是Animal类型
c = Dog()  # c是Dog类型

print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))
print(isinstance(c, Animal))


def run_twice(animal):
    animal.run()
    animal.run()


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


run_twice(Tortoise())


class Timer(object):
    def run(self):
        print('Start...')


timer = Timer()
run_twice(timer)
