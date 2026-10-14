numbers = []
count = 0

while count < 3:
    num = float(input("Enter number " + str(count + 1) + ": "))
    numbers.append(num)
    count = count + 1

# take the three numbers out of the list
a = numbers[0]
b = numbers[1]
c = numbers[2]


if a == b and b == c:
    print("All three numbers are equal")
elif a > b and a > c:
    print(a, "is the largest")
elif b > a and b > c:
    print(b, "is the largest")
elif c > a and c > b:
    print(c, "is the largest")
elif a == b:
    print(a, "and", b, "are equal and the largest")
elif a == c:
    print(a, "and", c, "are equal and the largest")
else:
    print(b, "and", c, "are equal and the largest")