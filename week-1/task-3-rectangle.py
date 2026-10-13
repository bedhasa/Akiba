# Ask for the rectangle's measurements.
length = float(input("Enter the length in meters: "))
width = float(input("Enter the width in meters: "))

# Calculate area and perimeter.
area = length * width
perimeter = 2 * (length + width)

print(f"\nArea: {area:g} m²")
print(f"Perimeter: {perimeter:g} m")
