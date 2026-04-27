class Account:

    def __init__(self):
        self.customer = None
        self.balance = 0
        self.interest_rate = 0.05

    def get_customer(self):
        return self.customer

    def set_customer(self, customer):
        self.customer = customer

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    def get_interest_rate(self):
        return self.interest_rate

    def set_interest_rate(self, rate):
        self.interest_rate = rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance = self.balance + interest

    def add_amount(self, amount):
        self.balance = self.balance + amount

    def close(self):
        self.customer = None
        self.balance = 0