class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print('eating')


# animal: Parent, Base
# Mammal/fish: Child, Sub
class Mammal(Animal):
    def __init__(self):
        # method overriding this uses the animal init first then then mammal init
        # if you dont called super Mammal will not get the age
        super().__init__()
        self.weight = 2

    def walk(self):
        print('walking')


class Fish(Animal):
    def swim(self):
        print('swimming')


m = Mammal()
m.eat()
m.walk()
print(m.age)
print(m.weight)

f = Fish()
f.eat()
f.swim()
print(f.age)

# python supports multi-level inheritance


class Flyer:
    def fly(self):
        print("flies")


class Swimmer:
    def swim(self):
        print('swimming')


# python supports multipe inheritance
# try to make sure that the classes you inherite from using multiple inheritance does not methods and properties that have the same name
class FlyingFish(Flyer, Swimmer):
    pass


fish1 = FlyingFish()
