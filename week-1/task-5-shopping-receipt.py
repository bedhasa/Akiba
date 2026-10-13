# Ask for the customer's purchase details.
customer_name = input("Customer name: ")
product_name = input("Product name: ")
price = float(input("Price per item in ETB: "))
quantity = int(input("Quantity: "))

total = price * quantity

print("\n" + "=" * 40)
print("SHOPPING RECEIPT".center(40))
print("=" * 40)
print(f"Customer: {customer_name}")
print(f"Product:  {product_name}")
print(f"Price:    {price:,.2f} ETB")
print(f"Quantity: {quantity}")
print("-" * 40)
print(f"Total:    {total:,.2f} ETB")
print("\nThank you for shopping!")
