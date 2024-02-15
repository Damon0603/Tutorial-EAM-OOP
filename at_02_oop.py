# We define Classes with the Keyword Class -> Blueprint

class FinancialInstrument:
    symbol: str
    price: float

    def __new__(cls, *args, **kwargs):

        """
    __new__ is a static method (implicitly) and is the first step in the instance creation process.
    It is responsible for actually creating a new instance of the class.
    It takes the class itself as its first argument and returns a new instance of that class.
    __new__ is rarely used or overridden, except in cases where you need to control the way objects are created
    If you override __new__, it's important to remember to call the superclass’s __new__ method with super().__new__(cls, ...),
    to ensure proper object creation.

    Is very rarely modified but for example when doing singleton Pattern
        """
        # print("Creating Object")
        instance = super().__new__(cls)
        return instance

    def __init__(self, symbol, price):

        # print("Initializing Values")
        self.symbol = symbol
        self.price = price

        """
     __init__ is an instance method and is the second step in the instance creation process.
    It's called after __new__ and is responsible for initializing the new instance, not for creating it.
    __init__ doesn't return anything; it modifies the instance in place.
    This method takes the instance (self) as its first argument and is where you typically set up instance attributes and
    perform any required setup tasks.
    __init__ is the constructor method that is most commonly overridden and customized in Python classes.
    
        """

    def get_market_value(self):
        return self.price


# Automatic Passing of Self: When you call a method on an instance,
# Python automatically passes the instance as the first argument to the method.
# Therefore, you don't need to provide the self argument explicitly; Python does it for you.

# Creating an Instance of the Class
apple = FinancialInstrument("AAPL", 170)

print(apple) # What happens if I do this ?

# <__main__.FinancialInstrument object at 0x000001246DE33110>

# __main__: This indicates that the FinancialInstrument class is defined in the main module,
    #   which is the script you are currently running. In Python, __main__ is the name of the environment where
    #   the top-level script is executed.

# FinancialInstrument: This is the name of the class to which the object belongs.
    # It tells you that the object is an instance of the FinancialInstrument class.

# object at 0x000001246DE33110: This part shows that the particular instance of FinancialInstrument is
# located in memory at the address 0x000001246DE33110.
# This is a hexadecimal memory address where the object is stored.
# Each object in Python gets its own unique memory address,
# which can be useful for certain low-level operations or for understanding that two variables might reference the same object in memory.


# Where is this Object stored in Memory ?
#Heap: Der Heap ist ein Bereich, in dem dynamisch zur Laufzeit Speicher für Objekte und Datenstrukturen allokiert wird.
# Wenn du in deinem Programm ein Objekt erstellst, das mehr Speicher benötigt oder dessen Größe sich zur Laufzeit ändern kann, wird es oft im Heap gespeichert.
# Objekte im Heap bleiben so lange erhalten, bis sie nicht mehr benötigt werden und vom Garbage Collector (in Sprachen wie Java) bereinigt werden,
# oder bis der Speicher explizit freigegeben wird (in Sprachen wie C++).

# Stack: Der Stack wird für die Verwaltung von Funktionen und Methoden verwendet. Wenn eine Funktion aufgerufen wird,
#         wird ein Block im Stack für sie reserviert,
#       der lokale Variablen und andere Funktionsspezifika enthält. Nachdem die Funktion abgearbeitet ist, wird dieser Block freigegeben.


# Ram also includes ->     Code-Segment: Hier wird der ausführbare Code des Programms gespeichert.
#                           Daten-Segment: Dieser Bereich speichert globale und statische Variablen.
#                       BSS-Segment (Block Started by Symbol): Ein Teil des Daten-Segments, der uninitialisierte globale und statische Variablen enthält.

#
# In Python, wenn du ein Objekt an eine Funktion übergibst, wird die Referenz auf dieses Objekt übergeben,
#   nicht das Objekt selbst. Das bedeutet, die Funktion arbeitet mit der gleichen Instanz des Objekts,
#   die außerhalb der Funktion existiert.
#   Dieses Verhalten wird oft als "Pass-by-Reference" beschrieben,
#   obwohl in Python genauer gesagt "Pass-by-Object-Reference" zutrifft.
#
# Was bedeutet das konkret?
#
#     Wenn du ein veränderbares Objekt wie eine Liste oder ein Dictionary an eine Funktion übergibst und die Funktion dieses Objekt modifiziert,
#     werden die Änderungen auch außerhalb der Funktion sichtbar sein.
#     Bei unveränderlichen Objekten wie Zahlen, Strings oder Tuples führt jede Modifikation zu einem neuen Objekt, und das ursprüngliche Objekt bleibt unverändert.
#
#       Benefit  ? Dieser Mechanismus ermöglicht es, dass Funktionen effizient mit großen Datenstrukturen arbeiten können,
#       ohne dass diese komplett kopiert werden müssen.


