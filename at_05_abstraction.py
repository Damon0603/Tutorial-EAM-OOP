from abc import ABC, abstractmethod
from typing import override


# Why are abstract classes used
# 1. Define a Template: Abstract classes provide a template or blueprint for other classes to follow.
#     They establish a common structure or set of behaviors that subclasses should implement.

# 2. Enforce Contracts: Abstract classes can enforce contracts by declaring abstract methods that must be implemented by subclasses.
#   This helps ensure that subclasses provide necessary functionality.

# 3. Encourage Code Reuse: By defining common methods or properties in an abstract class, you can promote code reuse among subclasses.
# Subclasses inherit these common functionalities, reducing redundancy and promoting maintainability.

# 4. Polymorphism: Abstract classes facilitate polymorphism, allowing objects of different subclasses to be treated uniformly through a common interface.
#   This enables more flexible and modular code.

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):

    @override
    def make_sound(self):
        return "Woof!"

class Cat(Animal):

    @override
    def make_sound(self):
        return "Meow!"


dog = Dog("Merci")
cat = Cat("Tiger")

print(dog.make_sound())  # Outputs: Woof!
print(cat.make_sound())  # Outputs: Meow!

# croco = Animal("croci")
