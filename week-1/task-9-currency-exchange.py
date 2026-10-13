# The exchange rate is stored once so it is easy to update.
exchange_rate = 150
usd_amount = float(input("Enter the amount in USD: "))
etb_amount = usd_amount * exchange_rate

print(f"\nExchange rate: 1 USD = {exchange_rate} ETB")
print(f"ETB amount: {etb_amount:,.2f} ETB")
