# accounts/bank_account.py
from abc import ABC, abstractmethod
from patterns.observer.subject import Subject

class BankAccount(Subject, ABC):
    LOW_BALANCE_LEVEL = 100.00
    LARGE_TRANSACTION_THRESHOLD = 5000.00

    def __init__(self, account_number, balance):
        super().__init__()
        self._account_number = account_number
        self._balance = balance

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self._account_number

    def update_balance(self, amount):
        self._balance += amount

        # Trigger observer notifications
        if self._balance < self.LOW_BALANCE_LEVEL:
            self.notify(f"Low balance warning ${self._balance:.2f}: on account {self._account_number}.")
        if abs(amount) > self.LARGE_TRANSACTION_THRESHOLD:
            self.notify(f"Large transaction ${amount:.2f}: on account {self._account_number}.")

    @abstractmethod
    def get_service_charges(self):
        pass
