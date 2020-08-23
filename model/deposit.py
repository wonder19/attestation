import random

from common.constants import DepositPageConstants


class DepositData:
    def __init__(self, currency=None, end_date=None, deposit_type=None):
        self.currency = currency
        self.end_date = end_date
        self.deposit_type = deposit_type

    @staticmethod
    def random():
        currency = random.choice(DepositPageConstants.currency_list)
        end_date = random.choice(DepositPageConstants.end_date_list)
        deposit_type = random.choice(DepositPageConstants.deposit_type)
        return DepositData(currency, end_date, deposit_type)
