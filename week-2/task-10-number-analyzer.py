
total = 0
even = 0
odd = 0

for i in range(10):
    num = int(input("Enter a number: "))

    total = total + num

    if i == 0:
        largest = num
        smallest = num
    else:
        if num > largest:
            largest = num

        if num < smallest:
            smallest = num

    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

average = total / 10

print("Largest number:", largest)
print("Smallest number:", smallest)
print("Total sum:", total)
print("Average:", average)
print("Even numbers:", even)
print("Odd numbers:", odd)
