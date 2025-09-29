class BankAccount:
    """A simple BankAccount class with basic operations."""

    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        Returns True if successful, False if insufficient funds.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance."""
        print(f"Current Balance: ${self.account_balance}")
