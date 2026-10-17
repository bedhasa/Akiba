"""A simple interactive bank account for the Week 2 mini project."""

correct_pin = "1234"
attempts_remaining = 3

# Give the user at most three chances to enter the PIN.
while attempts_remaining > 0:
    entered_pin = input("Enter your PIN: ")

    if entered_pin == correct_pin:
        print("PIN correct!")
        print("Welcome to Akiba Bank.")
        break
    else:
        attempts_remaining -= 1
        print("Incorrect PIN.")

        if attempts_remaining > 0:
            print("Attempts remaining:", attempts_remaining)

if attempts_remaining == 0:
    print("Too many incorrect attempts.")
    print("Your account is locked.")
else:
    balance = 1000
    transactions = 0
    running = True

    while running:
        print("\n===== AKIBA BANK =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            print(f"Your current balance is: {balance:.2f} Birr")
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: "))
                if amount <= 0:
                    print("Deposit amount must be greater than zero.")
                else:
                    balance += amount
                    transactions += 1
                    print("Deposit successful!")
                    print(f"Your new balance is: {balance:.2f} Birr")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: "))
                if amount <= 0:
                    print("Withdrawal amount must be greater than zero.")
                elif amount > balance:
                    print("Insufficient balance!")
                else:
                    balance -= amount
                    transactions += 1
                    print("Withdrawal successful!")
                    print(f"Your new balance is: {balance:.2f} Birr")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == "4":
            print("Thank you for using Akiba Bank!")
            print("Goodbye!")
            print("Transactions made:", transactions)
            running = False
        else:
            print("Invalid option.")
            print("Please choose a valid option.")
