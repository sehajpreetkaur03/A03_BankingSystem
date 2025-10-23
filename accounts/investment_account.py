# accounts/investment_account.py
from .bank_account import BankAccount
from patterns.strategy.management_fee_strategy import ManagementFeeStrategy

class InvestmentAccount(BankAccount):
    def __init__(self, account_number, balance, management_fee, creation_date):
        super().__init__(account_number, balance)
        self.__service_charge_strategy = ManagementFeeStrategy(management_fee, creation_date)

    def get_service_charges(self):
        return self.__service_charge_strategy.calculate_service_charges(self)
