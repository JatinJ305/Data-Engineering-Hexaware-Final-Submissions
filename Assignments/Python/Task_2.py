def atm_transaction():
    try:
        # Get the user's current balance
        balance = float(input("Enter your current balance: "))
        # Display transaction options
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        # Get the user's choice
        choice = input("\nEnter the number corresponding to your choice: ")
        # Nested conditional statements for each option
        if choice == "1":
            # Option 1: Check Balance
            print(f"\nYour current balance is: ${balance:.2f}")
        elif choice == "2":
            # Option 2: Withdraw
            withdraw_amount = float(input("\nEnter the amount you want to withdraw: "))
            # Check if the withdrawal amount is valid
            if withdraw_amount > balance:
                print("Insufficient balance. Withdrawal failed.")
            elif withdraw_amount <= 0:
                print("Invalid withdrawal amount. Please enter a positive value.")
            elif withdraw_amount % 100 != 0:
                print("Withdrawal amount must be in multiples of 100.")
            else:
                balance -= withdraw_amount
                print(f"Withdrawal successful. Your new balance is: ${balance:.2f}")
        elif choice == "3":
            # Option 3: Deposit
            deposit_amount = float(input("\nEnter the amount you want to deposit: "))
            # Check if the deposit amount is valid
            if deposit_amount <= 0:
                print("Invalid deposit amount. Please enter a positive value.")
            else:
                balance += deposit_amount
                print(f"Deposit successful. Your new balance is: ${balance:.2f}")
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
    except ValueError:
        print("Invalid input. Please enter numeric values for balance and amounts.")
# Run the function
atm_transaction()
