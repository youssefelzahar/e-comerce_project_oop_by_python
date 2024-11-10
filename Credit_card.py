from payment import payment

class Credit_card(payment):
   def __init__(self, card_number, card_holder, expiration_date):
       self.card_number = card_number
       self.card_holder = card_holder
       self.expiration_date = expiration_date
   def pay(self,amount):
        print(f"Processing credit card payment of ${amount} for {self.card_holder}")
        return True
