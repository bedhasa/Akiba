number = int(input("Enter a number: "))

# Work with the positive value so negative numbers also work
if number < 0:
    number = -number

total = 0

while number > 0:
    digit = number % 10      # the last digit
    total = total + digit    # add it to the running total
    number = number // 10    # remove the last digit

print("Sum of digits is", total)