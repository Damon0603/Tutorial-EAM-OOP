# Class Definition in Python:
## Understanding Financial Instrument


```python
class FinancialInstrument:
    symbol: str
    price: float

    def __new__(cls, *args, **kwargs):
        """
        __new__ is a static method (implicitly) and is the first step in the instance creation process.
        It is responsible for actually creating a new instance of the class.
        It takes the class itself as its first argument and returns a new instance of that class.
        __new__ is rarely used or overridden, except in cases where you need to control the way objects are created.
        If you override __new__, it's important to remember to call the superclass’s __new__ method with super().__new__(cls, ...),
        to ensure proper object creation.

        Is very rarely modified but for example when doing singleton Pattern.
        """
        # print("Creating Object")
        instance = super().__new__(cls)
        return instance

    def __init__(self, symbol, price):
        """
        __init__ is an instance method and is the second step in the instance creation process.
        It's called after __new__ and is responsible for initializing the new instance, not for creating it.
        __init__ doesn't return anything; it modifies the instance in place.
        This method takes the instance (self) as its first argument and is where you typically set up instance attributes and
        perform any required setup tasks.
        __init__ is the constructor method that is most commonly overridden and customized in Python classes.
        """
        # print("Initializing Values")
        self.symbol = symbol
        self.price = price

    def get_market_value(self):
        return self.price

```
## Automatic Passing of Self

**When you call a method on an instance, Python automatically passes the instance as the first argument to the method.** 
**Therefore**, you don't need to provide the self argument explicitly; Python does it for you.

### So How do we create an Instance of the Class ? 

```
# Instantiating Object 
apple = FinancialInstrument("AAPL", 170)

print(apple) # What happens if I do this? -> What Value is printed ? Is there any Value ? 
```
    <__main__.FinancialInstrument object at 0x000001246DE33110>

### Understanding the Output

    main: Indicates the FinancialInstrument class is defined in the main module.
    FinancialInstrument: The name of the class to which the object belongs.
    object at 0x000001246DE33110: Shows the memory address where the object is stored.