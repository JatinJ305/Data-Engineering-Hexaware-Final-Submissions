def calculate_compound_interest():
    try:
        # Get the number of customers to process
        num_customers = int(input("Enter the number of customers: "))
        # Loop through each customer to calculate their future balance
        for i in range(1, num_customers + 1):
            print(f"\nCustomer {i}:")
            # Prompt user to enter initial balance, interest rate, and years
            initial_balance = float(input("Enter the initial balance: "))
            annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
            years = int(input("Enter the number of years: "))
            # Calculate the future balance using the formula
            future_balance = initial_balance * (1 + annual_interest_rate / 100) ** years
            # Display the future balance for the customer
            print(f"The future balance for Customer {i} after {years} years is: ${future_balance:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for balances, interest rates, and years.")
# Run the function
calculate_compound_interest()
