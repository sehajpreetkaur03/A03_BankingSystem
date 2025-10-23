# patterns/strategy/overdraft_strategy.py
from .service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    def __init__(self, overdraft_penalty):
        self._overdraft_penalty = overdraft_penalty

    def calculate_service_charges(self, account):
        charges = self.BASE_SERVICE_CHARGE
        if account.get_balance() < 0:
            charges += self._overdraft_penalty
        return charges
