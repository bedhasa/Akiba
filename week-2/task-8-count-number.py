n = int(input("Enter a positive number: "))

even_count = 0
odd_count = 0
total_sum = 0

for number in range(1, n + 1):
    if number % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

    total_sum = total_sum + number

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
print("Sum of all numbers:", total_sum)