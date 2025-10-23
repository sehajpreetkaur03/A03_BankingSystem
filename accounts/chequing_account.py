# accounts/chequing_account.py
from .bank_account import BankAccount
from patterns.strategy.overdraft_strategy import OverdraftStrategy

class ChequingAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_penalty):
        super().__init__(account_number, balance)
        self.__service_charge_strategy = OverdraftStrategy(overdraft_penalty)

    def get_service_charges(self):
        return self.__service_charge_strategy.calculate_service_charges(self)
