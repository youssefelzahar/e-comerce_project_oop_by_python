# Create products
from product import Product
from customer import Customer
from order import order
import Credit_card
from Report import Report


product1 = Product("Laptop", 1200.0, 10)
product2 = Product("Headphones", 150.0, 20)

# Create a customer
customer1 = Customer("Alice", "alice@example.com")

# Create an order
order1 = order(customer1)
if order1.add_item(product1, 1):
    print(f"Added {product1.name} to order.")
if order1.add_item(product2, 2):
    print(f"Added {product2.name} to order.")

# Add the order to the customer’s history
customer1.add_order(order1)

# Process payment
payment_method = Credit_card.Credit_card("1234-5678-9876-5432", "Alice", "12/25")
if payment_method.pay(order1.total):
    order1.complete_order()

# Generate a report (Singleton pattern)
report = Report()
report.generate_customer_report(customer1.get_order_history())
print("1",report)

# Create a new customer
customer2 = Customer("Bob", "bob@example.com")
order2 = order(customer2)
if order2.add_item(product1, 1):    
    print(f"Added {product1.name} to order.")
if order2.add_item(product2, 2):
    print(f"Added {product2.name} to order.")

# Add the order to the customer’s history    
customer2.add_order(order2) 

# Process payment
payment_method = Credit_card.Credit_card("1234-5678-9876-5432", "Bob", "12/25")
if payment_method.pay(order2.total):
    order2.complete_order()

# Generate a report (Singleton pattern)
report = Report()
report.generate_customer_report(customer2.get_order_history())
print("2",report)