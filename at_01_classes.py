# I will make a bold Claim, by saying that basically everything in Python is an Object

# String , Int , Boolean

name = "Nico"

# So we said everything is an object ,  what do you guys think this will throw  ?
print(isinstance(name,str))

# what about this ?
print(isinstance(name,object))

liste = ["Sebastian",29,True]

for element in liste:
    print(isinstance(element,object))

# So If everything is Python is an Object , does that mean we automatically do Object Oriented Programming ?

# Creating Classes and Objects does not necessarily have much to do with Object Oriented Programming.
# OOP is paradigm that uses object and classes to design software.

# We now have to find a definition for the following key concepts -> Classes, Objects, Attributes, Methods


## Classes: Blueprints for creating objects. A class defines a set of attributes and methods that its objects will have.

## Objects: Instances of classes.
# An object is a self-contained component that contains properties and methods needed to make a certain type of data useful.


## Methods : Functions defined inside a class. They describe the behaviors of an object.

## Attributes: Variables that hold data which belongs to a class or instance.



# Benefits of OOP in Python:
#
#     Abstraction: Encourages the division of a program into distinct parts. -> Breaking down complexity
#     Reusability: Code can be reused through inheritance, leading to a reduction in redundancy.
#     Encapsulation: Keeps the internal representation of an object hidden from the outside.
#     Polymorphism: Allows entities to be treated in multiple forms, enhancing flexibility.

# Lets say you
# Imagine a kitchen in a home or a restaurant. It's designed with various modules,
# each serving a specific purpose: there's a refrigerator for preserving food, an oven for baking,
# a stove for cooking, cabinets for storage, and so on. Each of these modules (or appliances) is self-contained,
# with a specific function, and they work independently of each other. Yet, when combined,
# they make the overall task of preparing and cooking meals much more efficient.
#
# In this analogy:
#
#     Modular Design: Just like a kitchen is divided into different areas or appliances with specific functions,
#     OOP splits a program into distinct modules (or classes and objects).
#     Each class/object in OOP is designed to perform a specific task or represent a specific concept.


#     Encapsulation: Each module (like an oven or a refrigerator) encapsulates its functionality.
#     You don’t need to know how the refrigerator’s cooling mechanism works internally to use it,
#     similar to how you use methods of a class without knowing the internal implementation.

#     Reusability: Just as you can use the same kitchen appliances to prepare different kinds of meals,
#     in OOP, you can reuse classes and objects in different parts of your program or even in different programs.
#     Maintenance: If something goes wrong with the oven, you can troubleshoot or replace just the oven without having to remodel
#     the entire kitchen. Similarly, if a bug is found in a module of an OOP-based program,
#     it can often be fixed without the need for major changes to the rest of the program.


#     Upgradability/Extensibility: You can replace an old model of a microwave with a newer one without changing other appliances.
#       In OOP, you can upgrade or extend a class without affecting other parts of the program.