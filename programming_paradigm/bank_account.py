# bank_account.py (Updated with Persistence)
import json
import os

class BankAccount:
    FILE_PATH = "account_data.json" # File where the balance is saved

    def __init__(self, initial_balance=0):
        # We start by trying to load the existing balance
        self._account_balance = self._load_balance(initial_balance)
    
    def _load_balance(self, default_balance):
        """Loads balance from file, or returns default if file doesn't exist."""
        if os.path.exists(self.FILE_PATH):
            try:
                with open(self.FILE_PATH, 'r') as f:
                    data = json.load(f)
                    return data.get('balance', default_balance)
            except (json.JSONDecodeError, KeyError):
                # Handle corrupted or incomplete file
                return default_balance
        return default_balance

    def _save_balance(self):
        """Saves the current balance to the file."""
        data = {'balance': self._account_balance}
        with open(self.FILE_PATH, 'w') as f:
            json.dump(data, f)

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            self._save_balance() # Save after change
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        
        if self._account_balance >= amount:
            self._account_balance -= amount
            self._save_balance() # Save after change
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")