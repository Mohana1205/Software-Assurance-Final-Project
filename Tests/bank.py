class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited {amount}. Balance: {self.balance}")
            return f"Deposited {amount}. Current balance: {self.balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}. Balance: {self.balance}")
            return f"Withdrew {amount}. Current balance: {self.balance}"
        elif amount > self.balance:
            return "Insufficient funds."
        else:
            return "Withdrawal amount must be positive."

    def check_balance(self):
        return f"Current balance: {self.balance}"

    def transfer(self, amount, recipient):
        if isinstance(recipient, BankAccount):
            if amount > 0 and self.balance >= amount:
                self.balance -= amount
                recipient.balance += amount
                self.transaction_history.append(f"Transferred {amount} to {recipient.account_holder}. Balance: {self.balance}")
                recipient.transaction_history.append(f"Received {amount} from {self.account_holder}. Balance: {recipient.balance}")
                return f"Transferred {amount} to {recipient.account_holder}. Current balance: {self.balance}"
            else:
                return "Transfer failed. Check the amount or balance."
        else:
            return "Invalid recipient."

    def transaction_summary(self):
        if self.transaction_history:
            return "\n".join(self.transaction_history)
        return "No transactions yet."

    def apply_interest(self, rate):
        if rate > 0:
            interest = self.balance * (rate / 100)
            self.balance += interest
            self.transaction_history.append(f"Interest applied at {rate}%. Balance: {self.balance}")
            return f"Interest of {interest} applied. New balance: {self.balance}"
        else:
            return "Interest rate must be positive."

    def close_account(self):
        if self.balance > 0:
            return f"Account cannot be closed. Withdraw remaining balance: {self.balance}"
        self.transaction_history.append("Account closed.")
        return f"Account for {self.account_holder} is closed."


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, account_holder, initial_balance=0):
        if initial_balance < 0:
            return "Initial balance cannot be negative."
        new_account = BankAccount(account_holder, initial_balance)
        self.accounts.append(new_account)
        return f"Account created for {account_holder} with balance {initial_balance}."

    def find_account(self, account_holder):
        for account in self.accounts:
            if account.account_holder == account_holder:
                return account
        return None

    def list_accounts(self):
        if self.accounts:
            return [f"{account.account_holder}: {account.balance}" for account in self.accounts]
        else:
            return "No accounts found."

    def delete_account(self, account_holder):
        account = self.find_account(account_holder)
        if account:
            if account.balance > 0:
                return "Account cannot be deleted. Withdraw remaining balance first."
            self.accounts.remove(account)
            return f"Account for {account_holder} has been deleted."
        return "Account not found."

    def transfer_between_accounts(self, sender_name, recipient_name, amount):
        sender = self.find_account(sender_name)
        recipient = self.find_account(recipient_name)
        if sender and recipient:
            return sender.transfer(amount, recipient)
        return "Transfer failed. One or both accounts not found."

    def total_bank_balance(self):
        return sum(account.balance for account in self.accounts)

    def account_with_highest_balance(self):
        if not self.accounts:
            return "No accounts found."
        highest_balance_account = max(self.accounts, key=lambda account: account.balance)
        return f"{highest_balance_account.account_holder} has the highest balance: {highest_balance_account.balance}"
