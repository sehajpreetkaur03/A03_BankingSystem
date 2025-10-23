# patterns/strategy/minimum_balance_strategy.py
from .service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    SERVICE_CHARGE_PREMIUM = 2.00

    def __init__(self, minimum_balance):
        self._minimum_balance = minimum_balance

    def calculate_service_charges(self, account):
        if account.get_balance() < self._minimum_balance:
            return self.BASE_SERVICE_CHARGE + self.SERVICE_CHARGE_PREMIUM
        return self.BASE_SERVICE_CHARGE
