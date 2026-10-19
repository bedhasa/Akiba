
def calculate_subtotal(items):
    """Calculate the total price before discounts and tax."""
    subtotal = 0

    for item in items:
        price = item["price"]
        quantity = item["quantity"]

        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        subtotal += price * quantity

    return subtotal


def calculate_discount(subtotal):
    """Calculate discount based on the subtotal."""
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative.")

    if subtotal >= 3000:
        return subtotal * 0.10
    elif subtotal >= 1000:
        return subtotal * 0.05
    else:
        return 0


def calculate_tax(amount, tax_rate):
    """Calculate tax using a percentage tax rate."""
    if amount < 0:
        raise ValueError("Amount cannot be negative.")

    if not 0 <= tax_rate <= 100:
        raise ValueError("Tax rate must be between 0 and 100.")

    return amount * tax_rate / 100


def generate_receipt(items, tax_rate=15):
    """Generate and return a formatted shopping receipt."""
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)
    discounted_total = subtotal - discount
    tax = calculate_tax(discounted_total, tax_rate)
    final_amount = discounted_total + tax

    lines = [
        "=" * 38,
        "       AKIBA SHOPPING RECEIPT",
        "=" * 38,
    ]

    for item in items:
        item_total = item["price"] * item["quantity"]
        lines.append(
            f'{item["name"]}: {item["quantity"]} x '
            f'{item["price"]:.2f} = {item_total:.2f} Birr'
        )

    lines.extend([
        "-" * 38,
        f"Subtotal:       {subtotal:.2f} Birr",
        f"Discount:      -{discount:.2f} Birr",
        f"Tax ({tax_rate}%):      {tax:.2f} Birr",
        "-" * 38,
        f"FINAL TOTAL:    {final_amount:.2f} Birr",
        "=" * 38,
    ])

    return "\n".join(lines)


if __name__ == "__main__":
    products = [
        {"name": "Notebook", "price": 80, "quantity": 3},
        {"name": "Pen", "price": 15, "quantity": 5},
    ]

    try:
        receipt = generate_receipt(products, tax_rate=15)
        print(receipt)
    except (ValueError, KeyError, TypeError) as error:
        print(f"Error: {error}")
