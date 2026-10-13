# Ask for the student's information.
student_name = input("Student name: ")
student_id = input("Student ID: ")
department = input("Department: ")
year = int(input("Year: "))
university = input("University: ")
phone = input("Phone number: ")

# Show the information in a simple card.
print("\n" + "+" + "-" * 34 + "+")
print("|" + "AKIBA STUDENT CARD".center(34) + "|")
print("+" + "-" * 34 + "+")
print(f"| Name:       {student_name:<21}|")
print(f"| ID:         {student_id:<21}|")
print(f"| Department: {department:<21}|")
print(f"| Year:       {year:<21}|")
print(f"| University: {university:<21}|")
print(f"| Phone:      {phone:<21}|")
print("+" + "-" * 34 + "+")
