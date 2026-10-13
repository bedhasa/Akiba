# Ask for the student's name and three scores.
student_name = input("Student name: ")
python_score = float(input("Python score: "))
english_score = float(input("English score: "))
mathematics_score = float(input("Mathematics score: "))

average = (python_score + english_score + mathematics_score) / 3

print("\n" + "=" * 36)
print("STUDENT RESULT".center(36))
print("=" * 36)
print(f"Student:      {student_name}")
print(f"Python:       {python_score:g}")
print(f"English:      {english_score:g}")
print(f"Mathematics:  {mathematics_score:g}")
print("-" * 36)
print(f"Average:      {average:.2f}")
print("=" * 36)
