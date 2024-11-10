class order():
    order_counter=0
    def __init__(self,customer):
        self.order_id=order.order_counter+1
        order.order_counter+=1
        self.customer=customer
        self.products=[]
        self.status="pending"
        self.total=0
    def __str__(self):
        return f"{self.order_id} {self.customer} {self.products} {self.status} {self.total}"
    def add_item(self,product,quantity):
          if product.update_stock(quantity):
              
            self.products.append((product,quantity))
            self.total+=product.price*quantity
            return True

          return False
    def complete_order(self):
        self.status="complete"
            