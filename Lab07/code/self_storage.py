"""Input parsing and rental calculations for the Self Storage fuzz-testing lab."""

import math


def _require_text(value, field_name):
    """Return text input or raise a consistent ValueError."""
    if not isinstance(value, str):
        raise ValueError(f"{field_name} must be text")
    return value


def parse_rental(text):
    """Parse a rental string formatted as ``unit:months``."""
    text = _require_text(text, "rental")
    if text.count(":") != 1:
        raise ValueError("rental must contain exactly one ':' separator")
    unit_text, months_text = text.split(":")
    unit = unit_text.strip().title()
    if not unit:
        raise ValueError("unit must not be empty")
    try:
        months = float(months_text.strip())
    except ValueError as exc:
        raise ValueError("months must be a number") from exc
    if not math.isfinite(months) or months < 0:
        raise ValueError("months must be a finite non-negative number")
    return unit, months


def duration_average(months_csv):
    """Return the integer average of a non-empty comma-separated month list."""
    months_csv = _require_text(months_csv, "months_csv")
    fields = months_csv.split(",")
    if not fields or any(not field.strip() for field in fields):
        raise ValueError("months_csv must contain non-empty integer values")
    try:
        values = [int(field.strip()) for field in fields]
    except ValueError as exc:
        raise ValueError("months_csv must contain only integers") from exc
    if any(value < 0 for value in values):
        raise ValueError("months must be non-negative")
    return sum(values) // len(values)


def payable_rent(text):
    """Calculate rent including 18% tax, less discount, floored at zero."""
    text = _require_text(text, "payment")
    if text.count("|") != 1:
        raise ValueError("payment must contain exactly one '|' separator")
    rent_text, discount_text = text.split("|")
    try:
        rent = float(rent_text.strip())
        discount = float(discount_text.strip())
    except ValueError as exc:
        raise ValueError("rent and discount must be numbers") from exc
    if not math.isfinite(rent) or not math.isfinite(discount):
        raise ValueError("rent and discount must be finite numbers")
    if rent < 0 or discount < 0:
        raise ValueError("rent and discount must be non-negative")
    total = rent * 1.18 - discount
    return max(total, 0)


def main():
    """Run the interactive demonstration."""
    print("==== Running parse_rental ====")
    user_input = input("Enter unit:months (e.g. medium:6): ")
    try:
        result = parse_rental(user_input)
        print("Unit and Months:", result)
    except ValueError as error:
        print("Invalid rental:", error)

    print("\n==== Running duration_average ====")
    user_input = input("Enter rental months as CSV (e.g. 3,6,12): ")
    try:
        result = duration_average(user_input)
        print("Average Duration:", result)
    except ValueError as error:
        print("Invalid durations:", error)

    print("\n==== Running payable_rent ====")
    user_input = input("Enter rent|discount (e.g. 2400|200): ")
    try:
        result = payable_rent(user_input)
        print("Payable Rent:", result)
    except ValueError as error:
        print("Invalid payment:", error)


if __name__ == "__main__":
    main()
