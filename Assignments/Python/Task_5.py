def validate_password():
    print("Welcome to the bank account setup!")
    print("Please create a password following these rules:")
    print("1. The password must be at least 8 characters long.")
    print("2. It must contain at least one uppercase letter.")
    print("3. It must contain at least one digit.")
    # Loop until a valid password is entered
    while True:
        password = input("Enter your password: ")
        # Check if the password meets the criteria
        if len(password) < 8:
            print("Password must be at least 8 characters long. Please try again.")
        elif not any(char.isupper() for char in password):
            print("Password must contain at least one uppercase letter. Please try again.")
        elif not any(char.isdigit() for char in password):
            print("Password must contain at least one digit. Please try again.")
        else:
            print("Password is valid. Your account setup is complete!")
            break
# Run the function
validate_password()
