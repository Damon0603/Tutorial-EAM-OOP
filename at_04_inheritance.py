from at_02_oop import FinancialInstrument

# Inheritance
class Stock(FinancialInstrument):
    def __init__(self,symbol,price,volume):
        super().__init__(symbol,price)

        self.volume = volume

    def __str__(self):
        return f"{super().__str__()}, Volume: {self.volume}"



class Fund(FinancialInstrument): # Lets assume this fund contains stocks only
    def __init__(self, symbol, price, holdings):
        super().__init__(symbol, price)
        self.holdings = holdings  # List of stocks

    def get_holdings_value(self):
        return sum(stock.get_market_value() for stock in self.holdings)

    def __str__(self):
        holdings_str = ', '.join(str(stock) for stock in self.holdings)
        return f"{super().__str__()}, Holdings: [{holdings_str}]"



apple = Stock('AAPL', 150, 5000000)
google = Stock('GOOGL', 2800, 3000000)

tech_fund = Fund('TECHX', 500, [apple, google])

print(apple)
print(google)
print(tech_fund)

print(tech_fund.get_holdings_value())