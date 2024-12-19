class Account:
    def __init__(self, account_number=None, account_type=None, account_balance=0.0):
        self.account_number = account_number
        self.account_type = account_type
        self.account_balance = account_balance
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.account_balance:.2f}.")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.account_balance:
            print("Insufficient balance.")
        else:
            self.account_balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance is ${self.account_balance:.2f}.")
    def print_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Account Balance: ${self.account_balance:.2f}")
class SavingsAccount(Account):
    def __init__(self, account_number, account_balance=0.0, interest_rate=4.5):
        super().__init__(account_number, "Savings", account_balance)
        self.interest_rate = interest_rate
    def calculate_interest(self):
        interest = self.account_balance * (self.interest_rate / 100)
        self.account_balance += interest
        print(f"Interest of ${interest:.2f} added. New balance is ${self.account_balance:.2f}.")
class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 500.0
    def __init__(self, account_number, account_balance=0.0):
        super().__init__(account_number, "Current", account_balance)
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > (self.account_balance + CurrentAccount.OVERDRAFT_LIMIT):
            print("Withdrawal exceeds the overdraft limit.")
        else:
            self.account_balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance is ${self.account_balance:.2f}.")
class Bank:
    def main(self):
        print("\n--- Welcome to the Banking System ---")
        print("1. Create a Savings Account")
        print("2. Create a Current Account")
        choice = input("Choose an option (1/2): ")
        account = None
        if choice == '1':
            account_number = input("Enter Account Number: ")
            initial_balance = float(input("Enter Initial Balance: "))
            account = SavingsAccount(account_number, initial_balance)
        elif choice == '2':
            account_number = input("Enter Account Number: ")
            initial_balance = float(input("Enter Initial Balance: "))
            account = CurrentAccount(account_number, initial_balance)
        else:
            print("Invalid option selected.")
            return
        while True:
            print("\n--- Banking Operations ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Calculate Interest (Savings Accounts only)")
            print("4. Display Account Info")
            print("5. Exit")
            operation = input("Choose an operation (1-5): ")
            if operation == '1':
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            elif operation == '2':
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            elif operation == '3':
                if isinstance(account, SavingsAccount):
                    account.calculate_interest()
                else:
                    print("Interest calculation is not applicable for Current Accounts.")
            elif operation == '4':
                account.print_account_info()
            elif operation == '5':
                print("Exiting the Banking System.")
                break
            else:
                print("Invalid operation selected. Please try again.")
# Run the program
if __name__ == "__main__":
    bank = Bank()
    bank.main()
