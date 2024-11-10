class Customer():
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.orders=[]

    def __str__(self):
        return f"{self.name} {self.email}"
    def add_order(self,order):
        self.orders.append(order)
    def get_order_history(self):
        return self.orders    