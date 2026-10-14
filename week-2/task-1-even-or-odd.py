number= input("Enter a number: ")
number = int(number)

if number == 0 or number < 0:
    print(f"{number} is neither even nor odd.")
else:
 if number % 2 == 0:
    print(f"{number} is an even number.")
 else:
    print(f"{number} is an odd number.")