import unittest
from bank import Bank  # Import Bank class from bank.py


class TestBankAccount(unittest.TestCase):
    def test_create_account(self):
        bank = Bank()
        
        # Test creating accounts
        result = bank.create_account("Alice", 1000)
        self.assertEqual(result, "Account created for Alice with balance 1000.")
        
        result = bank.create_account("Bob", 500)
        self.assertEqual(result, "Account created for Bob with balance 500.")
        
        # Verify accounts were created
        alice = bank.find_account("Alice")
        bob = bank.find_account("Bob")
        
        self.assertIsNotNone(alice)
        self.assertIsNotNone(bob)
        self.assertEqual(alice.balance, 1000)
        self.assertEqual(bob.balance, 500)

    def test_transfer(self):
        bank = Bank()
        
        # Create accounts
        bank.create_account("Alice", 1000)
        bank.create_account("Bob", 500)
        
        # Retrieve accounts
        alice = bank.find_account("Alice")
        bob = bank.find_account("Bob")
        
        # Perform transfer
        transfer_result = alice.transfer(200, bob)
        self.assertEqual(transfer_result, "Transferred 200 to Bob. Current balance: 800")
        
        # Verify balances after transfer
        self.assertEqual(alice.balance, 800)
        self.assertEqual(bob.balance, 700)

    def test_withdrawal(self):
        bank = Bank()
        
        # Create an account
        bank.create_account("Alice", 1000)
        
        # Retrieve account
        alice = bank.find_account("Alice")
        
        # Perform withdrawal
        withdrawal_result = alice.withdraw(200)
        self.assertEqual(withdrawal_result, "Withdrew 200. Current balance: 800")
        
        # Attempt to withdraw more than balance
        withdrawal_result = alice.withdraw(1000)
        self.assertEqual(withdrawal_result, "Insufficient funds.")
        
        # Verify balance after withdrawals
        self.assertEqual(alice.balance, 800)

    def test_delete_account_after_transfer(self):
        bank = Bank()
        
        # Create accounts for Alice and Bob
        bank.create_account("Alice", 1000)
        bank.create_account("Bob", 500)
        
        # Retrieve Alice and Bob's accounts
        alice = bank.find_account("Alice")
        bob = bank.find_account("Bob")
        
        # Perform transfer
        transfer_result = alice.transfer(200, bob)
        self.assertEqual(transfer_result, "Transferred 200 to Bob. Current balance: 800")
        
        # Assert balances after transfer
        self.assertEqual(alice.balance, 800)
        self.assertEqual(bob.balance, 700)
        
        # Withdraw the remaining balance from Alice's account
        withdrawal_result = alice.withdraw(800)
        self.assertEqual(withdrawal_result, "Withdrew 800. Current balance: 0")
        
        # Now delete Alice's account
        result = bank.delete_account("Alice")
        self.assertEqual(result, "Account for Alice has been deleted.")
        
        # Assert that Alice's account no longer exists
        self.assertIsNone(bank.find_account("Alice"))
        
        # Assert that the bank has the correct number of accounts
        self.assertEqual(len(bank.accounts), 1)  # Only Bob's account should exist
        
        # Ensure Bob’s account is still intact after Alice’s deletion
        bob_account = bank.find_account("Bob")
        self.assertIsNotNone(bob_account)
        self.assertEqual(bob_account.balance, 700)

    def test_delete_account_with_balance(self):
        bank = Bank()
        
        # Create account with balance
        bank.create_account("Alice", 1000)
        
        # Attempt to delete account with balance
        result = bank.delete_account("Alice")
        self.assertEqual(result, "Account cannot be deleted. Withdraw remaining balance first.")
        
        # Ensure the account still exists
        self.assertIsNotNone(bank.find_account("Alice"))

    def test_find_non_existent_account(self):
        bank = Bank()
        
        # Attempt to find a non-existent account
        result = bank.find_account("NonExistent")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
