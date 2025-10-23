# patterns/strategy/service_charge_strategy.py
from abc import ABC, abstractmethod

class ServiceChargeStrategy(ABC):
    BASE_SERVICE_CHARGE = 4.00

    @abstractmethod
    def calculate_service_charges(self, account):
        pass
