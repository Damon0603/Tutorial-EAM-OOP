class Person:
    def __init__(self, name, age):
        self.__name = name # __ denotes a private attribute
        self.__age = age

    # Getter method for age
    @property
    def age(self):
        return self.__age

    # Setter method for age
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age must be a non-negative value")
        self.__age = value

    # Getter method for name (no setter provided, so it's read-only)
    @property
    def name(self):
        return self.__name

# Creating an instance of Person
person = Person("Alice", 30)

# Accessing and modifying age using properties
print(person.age)  # Output: 30
person.age = 35
print(person.age)  # Output: 35

# Attempting to set age to a negative value will raise an error
try:
    person.age = -5
except ValueError as e:
    print(e)  # Output: Age must be a non-negative value

# Accessing name (which has no setter)
print(person.name)  # Output: Alice

# Attempting to modify name directly will not work
# person.name = "Bob"  # This would raise an AttributeError because there's no setter for name


class MyClass:
    def __init__(self):
        self.__private_attribute = 42

obj = MyClass()
print(obj.__private_attribute)  # This would raise an AttributeError because of name mangling


class MyClass:
    def __init__(self):
        self.__private_attribute = 42

    def get_private_attribute(self):
        return self.__private_attribute

obj = MyClass()
print(obj.get_private_attribute())  # Output: 42

