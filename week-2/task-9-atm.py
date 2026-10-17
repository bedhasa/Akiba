
correct_pin = "1234"
attempts = 3

while attempts > 0:
    pin = input("Enter your PIN: ")

    if pin == correct_pin:
        print("Correct PIN. Welcome!")
        break
    else:
        attempts = attempts - 1
        print("Incorrect PIN.")
        
        if attempts > 0:
            print("Attempts remaining:", attempts)
        else:
            print("Your ATM card is locked.")
