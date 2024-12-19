from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self, account_number=None, customer_name=None, balance=0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
    @abstractmethod
    def deposit(self, amount: float):
        pass
    @abstractmethod
    def withdraw(self, amount: float):
        pass
    @abstractmethod
    def calculate_interest(self):
        pass
    def print_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Balance: ${self.balance:.2f}")
class SavingsAccount(BankAccount):
    def __init__(self, account_number, customer_name, balance=0.0, interest_rate=4.5):
        super().__init__(account_number, customer_name, balance)
        self.interest_rate = interest_rate
    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount: float):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")
    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        print(f"Interest of ${interest:.2f} added. New balance is ${self.balance:.2f}.")
class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = 500.0
    def __init__(self, account_number, customer_name, balance=0.0):
        super().__init__(account_number, customer_name, balance)
    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount: float):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > (self.balance + CurrentAccount.OVERDRAFT_LIMIT):
            print("Withdrawal exceeds the overdraft limit.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")
    def calculate_interest(self):
        print("Current accounts do not earn interest.")
class Bank:
    def main(self):
        print("\n--- Welcome to the Banking System ---")
        print("1. Create a Savings Account")
        print("2. Create a Current Account")
        choice = input("Choose an option (1/2): ")
        account = None
        if choice == '1':
            account_number = input("Enter Account Number: ")
            customer_name = input("Enter Customer Name: ")
            initial_balance = float(input("Enter Initial Balance: "))
            account = SavingsAccount(account_number, customer_name, initial_balance)
        elif choice == '2':
            account_number = input("Enter Account Number: ")
            customer_name = input("Enter Customer Name: ")
            initial_balance = float(input("Enter Initial Balance: "))
            account = CurrentAccount(account_number, customer_name, initial_balance)
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
                account.calculate_interest()
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
