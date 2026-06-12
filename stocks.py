class Stock:
    market="NSE"
    def __init__(self,name,price):
        self.name = name
        self.price = price
      
    @classmethod
    def from_string(cls, stock_string):
        name, price = stock_string.split("-")
        return cls(name, float(price))
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
    

    def __str__(self):
        return f"Stock: {self.name} | Price: ₹{self._price}"
    
    def __repr__(self):
        return f"Stock('{self.name}', {self._price})"    
    @staticmethod
    def is_market_open(hour):
        return 9 <= hour <= 15
class IndexStock(Stock):
    def __init__(self, name, price, index_name):
        super().__init__(name, price)
        self.index_name = index_name
    
    def display(self):
        print(f"{self.name} belongs to {self.index_name}")
    
    def __str__(self):
        return f"{super().__str__()} | Index: {self.index_name}"

i1 = IndexStock("HDFC Bank", 1600, "Nifty 50")
i1.display()
s1 = Stock("Reliance", 2500)
s2 = Stock("Infosys", 1400)
s3 = Stock.from_string("TCS-3500")
print(Stock.is_market_open(10))
