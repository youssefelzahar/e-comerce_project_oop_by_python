class Report:
 instace=None
 def __new__(cls):
  if cls.instace is None:
   cls.instace=super().__new__(cls)
  return cls.instace
 def generate_customer_report(self,orders):
    print("Customer Report")
    for order in orders:
            print(f"{order} - Items: {[item[0].name for item in order.products]} - Total: ${order.total}")
    