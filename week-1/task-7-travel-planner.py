# Estimate travel time from distance and average speed.
destination = input("Destination: ")
distance = float(input("Distance in kilometers: "))
average_speed = float(input("Average speed in km/h: "))

travel_hours = distance / average_speed
whole_hours = int(travel_hours)
minutes = round((travel_hours - whole_hours) * 60)

print(f"\nDestination: {destination}")
print(f"Estimated travel time: {whole_hours} hours and {minutes} minutes")
