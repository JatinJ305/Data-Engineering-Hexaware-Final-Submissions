def bank_transactions():
    print("Welcome to your bank transaction manager!")
    print("You can add deposits or withdrawals. Type 'exit' to finish and see your transaction history.")
    # List to store transactions
    transactions = []
    # Loop to allow adding transactions
    while True:
        # Prompt user to input a transaction type
        transaction_type = input("Enter 'deposit' or 'withdrawal' to add a transaction, or 'exit' to finish: ").strip().lower()
        if transaction_type == 'exit':
            break  # Exit the loop if the user types 'exit'
        # Validate the transaction type
        if transaction_type not in ['deposit', 'withdrawal']:
            print("Invalid input. Please enter 'deposit' or 'withdrawal'.")
            continue
        # Prompt user for the transaction amount
        try:
            amount = float(input(f"Enter the amount for the {transaction_type}: "))
            # Ensure the amount is positive
            if amount <= 0:
                print("Amount must be positive. Please try again.")
                continue
            # Add the transaction as a tuple (type, amount) to the list
            transactions.append((transaction_type, amount))
            print(f"{transaction_type.capitalize()} of ${amount:.2f} added successfully.")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
    # Display the transaction history
    print("\nTransaction History:")
    if not transactions:
        print("No transactions recorded.")
    else:
        for idx, (t_type, t_amount) in enumerate(transactions, start=1):
            print(f"{idx}. {t_type.capitalize()}: ${t_amount:.2f}")
# Run the function
bank_transactions()
