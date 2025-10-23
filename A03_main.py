# A03_main.py
from client.client import Client
from accounts.chequing_account import ChequingAccount
from accounts.investment_account import InvestmentAccount
from accounts.savings_account import SavingsAccount
from datetime import date

def main():
    # Create client observers
    client1 = Client("Johny Dee", "johny@example.com")
    client2 = Client("Alica Smi", "alica@example.com")

    # Create accounts
    chequing = ChequingAccount("CHK-001", 200.00, 50.00)
    investment = InvestmentAccount("INV-001", 15000.00, 10.00, date(2010, 5, 15))
    savings = SavingsAccount("SAV-001", 500.00, 300.00)

    # Attach clients as observers
    chequing.attach(client1)
    investment.attach(client1)
    savings.attach(client2)

    # Simulate transactions
    print("\n--- Transaction Simulation ---\n")
    chequing.update_balance(-250.00)   # should trigger low balance alert
    investment.update_balance(6000.00) # should trigger large transaction alert
    savings.update_balance(-300.00)    # should trigger low balance alert

    # Show service charges
    print("\n--- Service Charge Summary ---")
    print(f"Chequing Account: ${chequing.get_service_charges():.2f}")
    print(f"Investment Account: ${investment.get_service_charges():.2f}")
    print(f"Savings Account: ${savings.get_service_charges():.2f}")

if __name__ == "__main__":
    main()
