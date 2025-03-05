import math


def round_up(amount, round_val):
    """Rounds amount to desired whole number"""
    return int(math.ceil(amount / round_val)) * round_val


# main

while 1:
    quantity_made = int(input("# of items: "))
    total_expenses = float(input("Total Expenses: "))
    target = float(input("Profit Goal: "))
    round_to = int(input("Round To:"))

    selling_price = (total_expenses + target) / quantity_made
    suggested_price = round_up(selling_price, round_to)

    print(f"Minimum Price: ${selling_price:.2f}")
    print(f"Suggested Price: ${suggested_price:.2f}")
    print()
