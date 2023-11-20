from faker import Faker

fake = Faker()


class Account:
    def __init__(self, owner: str, address: str):
        self.account_owner = owner
        self.owner_address = address
        self.balance = 0
        self.card = fake.credit_card_full()

    def add_money(self, summa: float):
        self.balance += summa
