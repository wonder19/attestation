import datetime
import random

from faker import Faker


class PaymentData:
    def __init__(self, date=None, amount=None, comment=None):
        self.date = date
        self.amount = amount
        self.comment = comment

    def random(self):
        date = "20.11.2020"
        amount = random.randint(1, 50000)
        comment = Faker().text()
        return PaymentData(date, amount, comment)
