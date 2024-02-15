class Person:
    def __init__(self, name, age):
        self._name = name
        # if not isinstance(age,int):
        #     raise TypeError(f"Expected int got {type(age)}")
        # else:
        #     self._age = age
        self._age = age



    # Getter method for age
    @property
    def age(self):
        return self._age #+ "Miau" -> Is possible

    # Setter method for age
    @age.setter
    def age(self, value):
        # if value < 0:
        #     raise ValueError("Age must be a non-negative value")
        # self._age = value
        if not isinstance(value,int):
            raise TypeError(f"Expected str got {type(value).__name__}")

    # Getter method for name (no setter provided, so it's read-only)
    @property
    def name(self):
        return self._name


daniel = Person("Daniel","30")
# daniel.age = "30" # Wont work


print(daniel.age)

# daniel.name = "Miguele" # Wont work






