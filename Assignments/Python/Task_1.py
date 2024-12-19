def check_loan_eligibility():
    # Take input from the user
    try:
        credit_score = int(input("Enter your credit score: "))
        annual_income = float(input("Enter your annual income: "))
        # Check eligibility
        if credit_score > 700 and annual_income >= 50000:
            print("Congratulations! You are eligible for a loan.")
        else:
            print("Unfortunately, you are not eligible for a loan.")
    except ValueError:
        print("Invalid input. Please enter numeric values for credit score and annual income.")
# Run the function
check_loan_eligibility()
