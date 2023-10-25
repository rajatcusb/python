from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class Cow(Animal):
    def sound(self):
        return "Moo!"

# Create instances of the subclasses
dog = Dog()
cat = Cat()
cow = Cow()

# Call the sound method for each animal
print("Dog says:", dog.sound())
print("Cat says:", cat.sound())
print("Cow says:", cow.sound())
