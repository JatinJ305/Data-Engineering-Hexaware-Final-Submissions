def bank_account_simulation():
    # Sample data: Dictionary with account numbers as keys and balances as values
    accounts = {
        "1001": 1500.00,
        "1002": 2500.50,
        "1003": 1750.75,
        "1004": 3000.00,
        "1005": 500.25
    }
    print("Welcome to the bank! You can check your account balance.")
    # Loop until the user enters a valid account number
    while True:
        # Prompt the user for their account number
        account_number = input("Please enter your account number: ")
        # Validate if the entered account number exists in the accounts dictionary
        if account_number in accounts:
            # If valid, display the account balance
            balance = accounts[account_number]
            print(f"Account Number: {account_number}")
            print(f"Your balance is: ${balance:.2f}")
            break
        else:
            # If not valid, ask the user to try again
            print("Invalid account number. Please try again.")
# Run the function
bank_account_simulation()
