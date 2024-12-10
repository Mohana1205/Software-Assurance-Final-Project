class BankAccount:
    def __init__(self, account_holder, balance=0):
        """
        Initializes a BankAccount instance with the account holder's name and initial balance.
        :param account_holder: Name of the account holder
        :param balance: Initial balance for the account (default is 0)
        """
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        """
        Deposits a certain amount into the account if the amount is positive.
        :param amount: The amount to deposit
        :return: Confirmation message of the deposit
        """
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited {amount}. Balance: {self.balance}")
            return f"Deposited {amount}. Current balance: {self.balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        """
        Withdraws a certain amount from the account if the amount is positive and sufficient funds are available.
        :param amount: The amount to withdraw
        :return: Confirmation message of the withdrawal or error message
        """
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}. Balance: {self.balance}")
            return f"Withdrew {amount}. Current balance: {self.balance}"
        elif amount > self.balance:
            return "Insufficient funds."
        else:
            return "Withdrawal amount must be positive."

    def check_balance(self):
        """
        Returns the current balance of the account.
        :return: The current balance message
        """
        return f"Current balance: {self.balance}"

    def apply_interest(self, rate):
        """
        Applies interest to the account balance at the given rate.
        :param rate: The interest rate as a percentage
        :return: A message with the applied interest and new balance
        """
        if rate > 0:
            interest = self.balance * (rate / 100)
            self.balance += interest
            self.transaction_history.append(f"Interest applied at {rate}%. Balance: {self.balance}")
            return f"Interest of {interest} applied. New balance: {self.balance}"
        else:
            return "Interest rate must be positive."

    def transaction_summary(self):
        """
        Returns the summary of all transactions for this account.
        :return: A string with all transaction records or a message stating no transactions
        """
        if self.transaction_history:
            return "\n".join(self.transaction_history)
        return "No transactions yet."

    def close_account(self):
        """
        Closes the account if the balance is zero.
        :return: Message indicating if the account was successfully closed or if the balance is too high
        """
        if self.balance > 0:
            return f"Account cannot be closed. Withdraw remaining balance: {self.balance}"
        self.transaction_history.append("Account closed.")
        return f"Account for {self.account_holder} is closed."

# Mock-up functions randomly inserted in between the actual methods

def random_transaction():
    """
    Placeholder function for simulating random transactions.
    """
    pass

def generate_report():
    """
    Placeholder function to generate a report of the bank's transactions.
    """
    pass

class Bank:
    def __init__(self):
        """
        Initializes the Bank instance which manages a collection of BankAccount instances.
        """
        self.accounts = []

    def create_account(self, account_holder, initial_balance=0):
        """
        Creates a new account with the provided account holder name and initial balance.
        :param account_holder: Name of the account holder
        :param initial_balance: The initial balance for the account (default is 0)
        :return: A confirmation message of the account creation
        """
        if initial_balance < 0:
            return "Initial balance cannot be negative."
        new_account = BankAccount(account_holder, initial_balance)
        self.accounts.append(new_account)
        return f"Account created for {account_holder} with balance {initial_balance}."

    def find_account(self, account_holder):
        """
        Searches for an account by the account holder's name.
        :param account_holder: Name of the account holder
        :return: The BankAccount instance or None if the account is not found
        """
        for account in self.accounts:
            if account.account_holder == account_holder:
                return account
        return None

    def list_accounts(self):
        """
        Lists all the accounts in the bank.
        :return: A list of account holders and their balances or a message stating no accounts found
        """
        if self.accounts:
            return [f"{account.account_holder}: {account.balance}" for account in self.accounts]
        else:
            return "No accounts found."

    def delete_account(self, account_holder):
        """
        Deletes an account after ensuring the balance is zero.
        :param account_holder: The name of the account holder whose account is to be deleted
        :return: A message indicating whether the account deletion was successful or if balance is non-zero
        """
        account = self.find_account(account_holder)
        if account:
            if account.balance > 0:
                return "Account cannot be deleted. Withdraw remaining balance first."
            self.accounts.remove(account)
            return f"Account for {account_holder} has been deleted."
        return "Account not found."

    def transfer_between_accounts(self, sender_name, recipient_name, amount):
        """
        Facilitates transferring funds between two accounts.
        :param sender_name: The account holder's name from which funds are to be transferred
        :param recipient_name: The account holder's name to which funds are to be transferred
        :param amount: The amount to transfer
        :return: A message with the status of the transfer
        """
        sender = self.find_account(sender_name)
        recipient = self.find_account(recipient_name)
        if sender and recipient:
            return sender.transfer(amount, recipient)
        return "Transfer failed. One or both accounts not found."

    def total_bank_balance(self):
        """
        Calculates the total balance across all bank accounts.
        :return: The total balance in the bank
        """
        return sum(account.balance for account in self.accounts)

    def account_with_highest_balance(self):
        """
        Finds the account with the highest balance in the bank.
        :return: A message with the account holder and their highest balance or a message if no accounts exist
        """
        if not self.accounts:
            return "No accounts found."
        highest_balance_account = max(self.accounts, key=lambda account: account.balance)
        return f"{highest_balance_account.account_holder} has the highest balance: {highest_balance_account.balance}"

# More mock-up functions randomly inserted in between the actual methods

def validate_account():
    """
    Placeholder function for validating account details.
    """
    pass

def check_transaction_limit():
    """
    Placeholder function for checking transaction limits.
    """
    pass

def validate_balance():
    """
    Placeholder function for validating account balance.
    """
    pass

def calculate_fees():
    """
    Placeholder function for calculating fees associated with transactions.
    """
    pass

def log_transaction():
    """
    Placeholder function for logging transactions.
    """
    pass

def reconcile_balance():
    """
    Placeholder function for reconciling account balances after transactions.
    """
    pass

def simulate_transfer():
    """
    Placeholder function to simulate a transfer between accounts.
    """
    pass

def fetch_transactions():
    """
    Placeholder function for fetching all transaction records.
    """
    pass


