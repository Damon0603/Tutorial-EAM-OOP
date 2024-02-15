# Memory Storage of Objects in Python

### Heap

The heap is an area where memory for objects and data structures is dynamically allocated at runtime. 
If you create an object in your program that requires more memory or whose size can change during runtime,
it is often stored in the heap. Objects in the heap remain there until they are no longer needed and are cleaned up by the garbage collector (in languages like Java)
, or until the memory is explicitly released (in languages like C++).

### Stack

The stack is used for managing functions and methods. When a function is called, a block in the stack is reserved for it, containing local variables and other function specifics. After the function has been processed, this block is released.
RAM Segments

    Code Segment: This is where the executable code of the program is stored.
    Data Segment: This area stores global and static variables.
    BSS Segment (Block Started by Symbol): A part of the data segment that contains uninitialized global and static variables.


```python
def funktion():
    # Lokale Variable: auf dem Stack gespeichert
    nummer = 10

    # Referenz auf ein Objekt: Referenz auf dem Stack, Objekt selbst auf dem Heap
    liste = [1, 2, 3]

    # Weiteres komplexes Objekt: Referenz auf dem Stack, Objekt selbst auf dem Heap
    worterbuch = {'a': 1, 'b': 2, 'c': 3}

    # Objekt einer Klasse: Referenz auf dem Stack, Objekt selbst auf dem Heap
    objekt = MyClass()

class MyClass:
    def __init__(self):
        self.attribut = 123
```


## Reference on the Stack

In Python, when a variable for a complex object (like a list, a dictionary, or a custom object) is declared within a function,
a reference to this object is stored on the stack.
<br>
###  This means:

    The variable itself (the name that refers to the object) is placed in stack memory.
    The stack memory is used for the execution of functions and stores information such as function calls, local variables, and their values.

#### In Python,

###### variable names are merely identifiers that refer to objects in memory.

When you write `meine_liste = [1, 2, 3],` you create a new list object in memory and meine_liste becomes a reference to this object. 
The name meine_liste is thus the key with which you can access the list, 
and the reference is the mechanism that enables this access.


Stack Overflow

A stack overflow is an error that occurs when a program's call stack exceeds its allocated memory limit. It mostly happens through deep or infinite recursion, which is basically nothing else than a function that repeatedly calls itself without a base case.

**Note: Python has a limit to the depth of recursion to prevent a stack overflow.**
<br>

The default limit is usually high enough for most typical use cases, but not infinite. 
You can check the recursion limit in Python with sys.getrecursionlimit() and even set it with sys.setrecursionlimit(limit), 
but it's generally not recommended to increase it significantly.
```
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        less = [x for x in arr if x < pivot]
        greater = [x for x in arr if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# Example of a call that might cause stack overflow on large, sorted arrays
sorted_array = list(range(10000))  # Large sorted array
quicksort(sorted_array)
```


### Passing Objects to Function

In Python, when you pass an object to a function, the reference to this object is passed, not the object itself. 
This means the function works with the same instance of the object that exists outside the function. 
This behavior is often described as "Pass-by-Reference", although in Python it is more accurately "Pass-by-Object-Reference".
What does this mean in practice?

If you pass a mutable object like a list or dictionary to a function and the function modifies this object, 
the changes will also be **visible outside of the function.** 
With immutable objects like numbers, strings, or tuples, any modification leads to a new object,
and the original object remains unchanged.


### Benefit

This mechanism allows functions to efficiently work with large data structures, without needing to copy them entirely.


```
class MeinObjekt:
    def __init__(self, wert):
        self.wert = wert

def aendere_attribut(obj):
    print("In der Funktion, Adresse von obj:", id(obj))
    obj.wert = "Neuer Wert"

# Objekt der Klasse MeinObjekt erstellen
mein_objekt = MeinObjekt("Alter Wert")

print("Vor der Funktion, Adresse von mein_objekt:", id(mein_objekt))
print("Vor der Funktion, Wert von mein_objekt:", mein_objekt.wert)

# Übergebe das Objekt der Funktion
aendere_attribut(mein_objekt)

print("Nach der Funktion, Adresse von mein_objekt:", id(mein_objekt))
print("Nach der Funktion, Wert von mein_objekt:", mein_objekt.wert)
```


**Immutable objects in Python include:**
* integers
* Floats
* Strings
* Tuples
* FrozenSets
* Booleans
* Bytes

```
# String erstellen
mein_string = "Alter Wert"

print("Vor der Funktion, Adresse von mein_string:", id(mein_string))
print("Vor der Funktion, Wert von mein_string:", mein_string)

def modify_string(s):
    print("In der Funktion, Adresse von s:", id(s))
    s = "Neuer Wert"
    print("In der Funktion nach Änderung, Adresse von s:", id(s))

modify_string(mein_string)

print("Nach der Funktion, Adresse von mein_string:", id(mein_string))
print("Nach der Funktion, Wert von mein_string:", mein_string)

```