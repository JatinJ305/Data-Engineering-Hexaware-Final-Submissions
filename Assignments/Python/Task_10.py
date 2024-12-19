import re
class Customer:
    def __init__(self, customer_id=None, first_name=None, last_name=None, email=None, phone=None, address=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
    def set_email(self, email):
        if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            self.email = email
        else:
            raise ValueError("Invalid email address")
    def set_phone(self, phone):
        if re.match(r'^\d{10}$', phone):
            self.phone = phone
        else:
            raise ValueError("Invalid phone number. Must be 10 digits.")
    def print_info(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Address: {self.address}")
class Account:
    account_counter = 1000
    def __init__(self, account_type=None, balance=0.0, customer=None):
        Account.account_counter += 1
        self.account_number = Account.account_counter
        self.account_type = account_type
        self.balance = balance
        self.customer = customer
    def print_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: ${self.balance:.2f}")
        self.customer.print_info()
class Bank:
    def __init__(self):
        self.accounts = {}
    def create_account(self, customer, acc_type, balance):
        account = Account(acc_type, balance, customer)
        self.accounts[account.account_number] = account
        print(f"Account created successfully. Account Number: {account.account_number}")
    def get_account_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account.balance
        else:
            print("Account not found.")
            return None
    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if amount > 0:
                account.balance += amount
                print(f"Deposited ${amount:.2f}. New balance: ${account.balance:.2f}")
                return account.balance
            else:
                print("Deposit amount must be positive.")
        else:
            print("Account not found.")
        return None
    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if 0 < amount <= account.balance:
                account.balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${account.balance:.2f}")
                return account.balance
            else:
                print("Insufficient balance or invalid withdrawal amount.")
        else:
            print("Account not found.")
        return None
    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.accounts.get(from_account_number)
        to_account = self.accounts.get(to_account_number)
        if from_account and to_account:
            if 0 < amount <= from_account.balance:
                from_account.balance -= amount
                to_account.balance += amount
                print(f"Transferred ${amount:.2f} from {from_account_number} to {to_account_number}.")
                print(f"New balance of {from_account_number}: ${from_account.balance:.2f}")
                print(f"New balance of {to_account_number}: ${to_account.balance:.2f}")
            else:
                print("Insufficient funds or invalid transfer amount.")
        else:
            print("One or both accounts not found.")
    def get_account_details(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            account.print_info()
        else:
            print("Account not found.")
class BankApp:
    def main(self):
        bank = Bank()
        while True:
            print("\n--- Banking System Menu ---")
            print("1. Create Account")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Get Account Balance")
            print("6. Get Account Details")
            print("7. Exit")
            choice = input("Choose an option (1-7): ")
            if choice == '1':
                customer_id = input("Enter Customer ID: ")
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                email = input("Enter Email: ")
                phone = input("Enter Phone (10 digits): ")
                address = input("Enter Address: ")
                try:
                    customer = Customer(customer_id, first_name, last_name)
                    customer.set_email(email)
                    customer.set_phone(phone)
                    customer.address = address
                    print("\nSelect Account Type:")
                    print("1. Savings")
                    print("2. Current")
                    acc_type = input("Enter choice (1/2): ")
                    acc_type = "Savings" if acc_type == '1' else "Current"
                    initial_balance = float(input("Enter Initial Balance: "))
                    bank.create_account(customer, acc_type, initial_balance)
                except ValueError as e:
                    print(e)
            elif choice == '2':
                account_number = int(input("Enter Account Number: "))
                amount = float(input("Enter deposit amount: "))
                bank.deposit(account_number, amount)
            elif choice == '3':
                account_number = int(input("Enter Account Number: "))
                amount = float(input("Enter withdrawal amount: "))
                bank.withdraw(account_number, amount)
            elif choice == '4':
                from_account = int(input("Enter your Account Number: "))
                to_account = int(input("Enter recipient's Account Number: "))
                amount = float(input("Enter transfer amount: "))
                bank.transfer(from_account, to_account, amount)
            elif choice == '5':
                account_number = int(input("Enter Account Number: "))
                balance = bank.get_account_balance(account_number)
                if balance is not None:
                    print(f"Account Balance: ${balance:.2f}")
            elif choice == '6':
                account_number = int(input("Enter Account Number: "))
                bank.get_account_details(account_number)
            elif choice == '7':
                print("Exiting the Banking System.")
                break
            else:
                print("Invalid choice. Please select a valid option.")
# Run the banking app
if __name__ == "__main__":
    app = BankApp()
    app.main()
