# patterns/strategy/management_fee_strategy.py
from datetime import date, timedelta
from .service_charge_strategy import ServiceChargeStrategy

class ManagementFeeStrategy(ServiceChargeStrategy):
    TEN_YEARS_AGO = date.today() - timedelta(days=10 * 365.25)

    def __init__(self, management_fee, creation_date):
        self._management_fee = management_fee
        self._creation_date = creation_date

    def calculate_service_charges(self, account):
        fee = self.BASE_SERVICE_CHARGE
        if self._creation_date < self.TEN_YEARS_AGO:
            fee = 0  # waive fee for loyal clients
        else:
            fee += self._management_fee
        return fee
