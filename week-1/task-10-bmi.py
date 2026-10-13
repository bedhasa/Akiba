# Ask for the information needed to calculate BMI.
name = input("Name: ")
weight = float(input("Weight in kilograms: "))
height = float(input("Height in meters: "))

bmi = weight / (height * height)

print("\n" + "=" * 32)
print("BMI REPORT".center(32))
print("=" * 32)
print(f"Name:   {name}")
print(f"Weight: {weight:g} kg")
print(f"Height: {height:.2f} m")
print(f"\nBMI: {bmi:.2f}")
print("=" * 32)
