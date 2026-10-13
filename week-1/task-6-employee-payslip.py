# Ask for the employee's salary details.
employee_name = input("Employee name: ")
basic_salary = float(input("Basic salary in ETB: "))
transport_allowance = float(input("Transport allowance in ETB: "))
food_allowance = float(input("Food allowance in ETB: "))

gross_salary = basic_salary + transport_allowance + food_allowance

print("\n" + "=" * 40)
print("EMPLOYEE PAYSLIP".center(40))
print("=" * 40)
print(f"Employee:             {employee_name}")
print(f"Basic salary:         {basic_salary:,.2f} ETB")
print(f"Transport allowance:  {transport_allowance:,.2f} ETB")
print(f"Food allowance:       {food_allowance:,.2f} ETB")
print("-" * 40)
print(f"Gross salary:         {gross_salary:,.2f} ETB")
print("=" * 40)
