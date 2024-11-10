class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} {self.price} {self.stock}"

    
    def update_stock(self, quantity):
        if quantity<=self.stock:
            self.stock -= quantity
            return True
        return False   
        
        
        

