# main-0.py (Updated)
import sys
from bank_account import BankAccount

def main():
    # BankAccount will now load the balance from the file, or use 100 
    # if it's the very first time running and the file doesn't exist.
    account = BankAccount(100) 

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_arg = sys.argv[1]
    
    # ... (Rest of the command parsing logic is the same)
    # ...
    # (The command parsing code from your original main-0.py goes here)
    # ...
    
    parts = command_arg.split(':')
    command = parts[0].lower()
    amount = None
    if len(parts) > 1 and parts[1]:
        try:
            amount = float(parts[1])
        except ValueError:
            print(f"Invalid amount provided: {parts[1]}")
            sys.exit(1)

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    
    elif command == "display" and amount is None:
        account.display_balance()
    
    else:
        print("Invalid command or missing amount for the operation.")


if __name__ == "__main__":
    main()