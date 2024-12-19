class Customer:
    # Constructor to initialize customer attributes
    def __init__(self, customer_id=None, first_name=None, last_name=None, email=None, phone_number=None, address=None):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone_number = phone_number
        self.__address = address
    # Getter and Setter methods for each attribute
    def get_customer_id(self):
        return self.__customer_id
    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id
    def get_first_name(self):
        return self.__first_name
    def set_first_name(self, first_name):
        self.__first_name = first_name
    def get_last_name(self):
        return self.__last_name
    def set_last_name(self, last_name):
        self.__last_name = last_name
    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email
    def get_phone_number(self):
        return self.__phone_number
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
    def get_address(self):
        return self.__address
    def set_address(self, address):
        self.__address = address
    # Method to print all information of the customer
    def print_customer_info(self):
        print(f"Customer ID: {self.__customer_id}")
        print(f"Name: {self.__first_name} {self.__last_name}")
        print(f"Email: {self.__email}")
        print(f"Phone Number: {self.__phone_number}")
        print(f"Address: {self.__address}")
class Account:
    # Constructor to initialize account attributes
    def __init__(self, account_number=None, account_type=None, account_balance=0.0):
        self.__account_number = account_number
        self.__account_type = account_type
        self.__account_balance = account_balance
    # Getter and Setter methods for each attribute
    def get_account_number(self):
        return self.__account_number
    def set_account_number(self, account_number):
        self.__account_number = account_number
    def get_account_type(self):
        return self.__account_type
    def set_account_type(self, account_type):
        self.__account_type = account_type
    def get_account_balance(self):
        return self.__account_balance
    def set_account_balance(self, account_balance):
        self.__account_balance = account_balance
    # Method to print account information
    def print_account_info(self):
        print(f"Account Number: {self.__account_number}")
        print(f"Account Type: {self.__account_type}")
        print(f"Account Balance: ${self.__account_balance:.2f}")
    # Method to deposit an amount into the account
    def deposit(self, amount: float):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.__account_balance:.2f}.")
        else:
            print("Deposit amount must be positive.")
    # Method to withdraw an amount from the account
    def withdraw(self, amount: float):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__account_balance:
            print("Insufficient balance.")
        else:
            self.__account_balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance is ${self.__account_balance:.2f}.")
    # Method to calculate interest and add it to the account balance
    def calculate_interest(self):
        interest_rate = 4.5 / 100
        interest = self.__account_balance * interest_rate
        self.__account_balance += interest
        print(f"Interest of ${interest:.2f} added. New balance is ${self.__account_balance:.2f}.")
class Bank:
    def main(self):
        # Create an account using the parameterized constructor
        account = Account(account_number="123456789", account_type="Savings", account_balance=1000.0)
        # Print account details
        print("\n--- Account Information ---")
        account.print_account_info()
        # Perform a deposit
        print("\n--- Deposit Operation ---")
        account.deposit(500.0)
        # Perform a withdrawal
        print("\n--- Withdrawal Operation ---")
        account.withdraw(300.0)
        # Calculate interest for a savings account
        print("\n--- Interest Calculation ---")
        account.calculate_interest()
        # Print final account details
        print("\n--- Final Account Information ---")
        account.print_account_info()
# Run the program
if __name__ == "__main__":
    bank = Bank()
    bank.main()
