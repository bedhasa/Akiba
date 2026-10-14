number = int(input("Enter a number: "))

# Prime numbers must be greater than 1,
# so 0, 1 and negative numbers are not prime
if number <= 1:
    print(number, "is Not Prime")
else:
    is_prime = True
    divisor = 2

    # WHY we do not check every number up to the input:
    # Divisors come in pairs. For example, 36 = 2 x 18, 3 x 12, 4 x 9, 6 x 6.
    # In every pair, one number is small and the other is big.
    # The small one is never bigger than the square root of the number.
    # So if a number has any divisor at all, we will find one
    # at or below its square root. Checking further is a waste of time.
    # Example: for 97 we only check 2 to 9 (since 10 x 10 = 100 > 97),
    # not 2 to 96.
    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            break  # found a divisor, no need to keep checking
        divisor = divisor + 1

    if is_prime:
        print(number, "is Prime")
    else:
        print(number, "is Not Prime")