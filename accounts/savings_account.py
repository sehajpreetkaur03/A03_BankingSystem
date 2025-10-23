# accounts/savings_account.py
from .bank_account import BankAccount
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, minimum_balance):
        super().__init__(account_number, balance)
        self.__service_charge_strategy = MinimumBalanceStrategy(minimum_balance)

    def get_service_charges(self):
        return self.__service_charge_strategy.calculate_service_charges(self)
