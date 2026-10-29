"""A simple command-line banking system demonstrating Python OOP."""

from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Transaction:
    transaction_type: str
    amount: float
    balance_after: float
    timestamp: str

    def __str__(self) -> str:
        return (
            f"{self.timestamp} | {self.transaction_type:<10} | "
            f"Amount: ₹{self.amount:.2f} | Balance: ₹{self.balance_after:.2f}"
        )


class BankAccount:
    """Represents one bank account."""

    def __init__(self, account_holder: str, opening_balance: float = 0.0):
        if not account_holder.strip():
            raise ValueError("Account holder name cannot be empty.")
        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative.")

        self.account_holder = account_holder.strip()
        self.__balance = float(opening_balance)  # Encapsulation
        self.transaction_history: List[Transaction] = []
        if opening_balance > 0:
            self._record_transaction("Opening deposit", float(opening_balance))

    @property
    def balance(self) -> float:
        """Read-only access to the current balance."""
        return self.__balance

    def _record_transaction(self, transaction_type: str, amount: float) -> None:
        self.transaction_history.append(
            Transaction(
                transaction_type=transaction_type,
                amount=amount,
                balance_after=self.__balance,
                timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            )
        )

    def deposit(self, amount: float) -> bool:
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return False
        self.__balance += amount
        self._record_transaction("Deposit", amount)
        print(f"Deposit successful. Current balance: ₹{self.__balance:.2f}")
        return True

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return False
        if amount > self.__balance:
            print("Insufficient balance. Withdrawal cancelled.")
            return False
        self.__balance -= amount
        self._record_transaction("Withdrawal", amount)
        print(f"Withdrawal successful. Current balance: ₹{self.__balance:.2f}")
        return True

    def show_transactions(self) -> None:
        print(f"\nTransaction history for {self.account_holder}:")
        if not self.transaction_history:
            print("No transactions yet.")
            return
        for transaction in self.transaction_history:
            print(transaction)


class SavingsAccount(BankAccount):
    """Example subclass demonstrating inheritance."""

    def __init__(self, account_holder: str, opening_balance: float = 0.0,
                 minimum_balance: float = 500.0):
        super().__init__(account_holder, opening_balance)
        self.minimum_balance = minimum_balance

    def account_type(self) -> str:
        return "Savings Account"


class BankingSystem:
    """Manages account creation and account lookup."""

    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number: str, name: str,
                       opening_balance: float = 0.0) -> bool:
        account_number = account_number.strip()
        if not account_number:
            print("Account number cannot be empty.")
            return False
        if account_number in self.accounts:
            print("That account number already exists.")
            return False
        try:
            self.accounts[account_number] = SavingsAccount(name, opening_balance)
        except ValueError as error:
            print(f"Could not create account: {error}")
            return False
        print(f"Account created successfully for {name}. Account number: {account_number}")
        return True

    def get_account(self, account_number: str):
        account = self.accounts.get(account_number.strip())
        if account is None:
            print("Account not found.")
        return account

    def run(self) -> None:
        while True:
            print("\n===== PYTHON BANKING SYSTEM =====")
            print("1. Create account")
            print("2. Check balance")
            print("3. Deposit money")
            print("4. Withdraw money")
            print("5. View transaction history")
            print("6. Exit")
            choice = input("Choose an option (1-6): ").strip()

            if choice == "1":
                number = input("Enter a new account number: ")
                name = input("Enter account holder name: ")
                try:
                    opening = float(input("Enter opening balance (₹): "))
                    self.create_account(number, name, opening)
                except ValueError:
                    print("Please enter a valid numeric balance.")
            elif choice in {"2", "3", "4", "5"}:
                number = input("Enter account number: ")
                account = self.get_account(number)
                if account is None:
                    continue
                if choice == "2":
                    print(f"Current balance: ₹{account.balance:.2f}")
                elif choice in {"3", "4"}:
                    try:
                        amount = float(input("Enter amount (₹): "))
                        if choice == "3":
                            account.deposit(amount)
                        else:
                            account.withdraw(amount)
                    except ValueError:
                        print("Please enter a valid numeric amount.")
                else:
                    account.show_transactions()
            elif choice == "6":
                print("Thank you for using the Python Banking System.")
                break
            else:
                print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    BankingSystem().run()
