"""Personal Information and Calculator - crash-proof, beginner version."""


# ---------- Validation helpers ----------
def get_text(prompt):
    """Keep asking until the user types a real name (letters, not empty)."""
    while True:
        value = input(prompt).strip()
        if value == "":
            print("  Oops, that was empty. Please type something.")
        elif not any(ch.isalpha() for ch in value):
            print("  Please include some letters in your answer.")
        else:
            return value


def get_number(prompt, minimum=None, whole=False):
    """Keep asking until the user types a valid number."""
    while True:
        value = input(prompt).strip()
        if value == "":
            print("  Oops, that was empty. Please type a number.")
            continue
        try:
            number = int(value) if whole else float(value)
        except ValueError:
            print(f"  '{value}' is not a valid number. Try again (e.g. 12 or 3.5).")
            continue
        if minimum is not None and number < minimum:
            print(f"  Please enter a number that is at least {minimum}.")
            continue
        return number


# ---------- Part 1: Info collector ----------
def collect_info():
    print("\n--- Personal Information ---")
    name = get_text("Your name: ")
    age = get_number("Your age: ", minimum=1, whole=True)
    if age > 120:
        print("  Wow, that's a long life! Using it anyway.")
    return name, age


# ---------- Part 2: Calculator ----------
def calculator():
    print("\n--- Calculator ---")
    a = get_number("First number: ")
    b = get_number("Second number: ")

    print(f"\n{a} + {b}  = {a + b:.2f}")
    print(f"{a} - {b}  = {a - b:.2f}")
    print(f"{a} * {b}  = {a * b:.2f}")
    if b == 0:
        print(f"{a} / {b}  = cannot divide by zero")
        print(f"{a} // {b} = cannot divide by zero")
        print(f"{a} % {b}  = cannot divide by zero")
    else:
        print(f"{a} / {b}  = {a / b:.2f}")
        print(f"{a} // {b} = {a // b:.2f}")
        print(f"{a} % {b}  = {a % b:.2f}")
    print(f"{a} ** {b} = {a ** b:.2f}")


# ---------- Part 3: Totals, average and receipt ----------
def receipt(name, age):
    print("\n--- Shopping Receipt ---")
    count = get_number("How many items did you buy? ", minimum=1, whole=True)

    items = []
    for i in range(1, count + 1):
        item = get_text(f"Item {i} name: ")
        price = get_number(f"  Price of {item}: ", minimum=0)
        qty = get_number(f"  Quantity of {item}: ", minimum=1, whole=True)
        items.append((item, price, qty))

    subtotal = 0
    for item, price, qty in items:
        subtotal += price * qty
    tax = subtotal * 0.16
    total = subtotal + tax
    average = subtotal / count

    # Formatted, aligned report (bonus)
    print("\n" + "=" * 42)
    print(f"{'RECEIPT':^42}")
    print("=" * 42)
    print(f"Customer: {name} (age {age})")
    print("-" * 42)
    print(f"{'Item':<16}{'Price':>8}{'Qty':>5}{'Total':>11}")
    print("-" * 42)
    for item, price, qty in items:
        print(f"{item[:15]:<16}{price:>8.2f}{qty:>5}{price * qty:>11.2f}")
    print("-" * 42)
    print(f"{'Subtotal:':<29}{subtotal:>13.2f}")
    print(f"{'Tax (16%):':<29}{tax:>13.2f}")
    print(f"{'TOTAL:':<29}{total:>13.2f}")
    print(f"{'Average per item line:':<29}{average:>13.2f}")
    print("=" * 42)


# ---------- Main ----------
def main():
    try:
        name, age = collect_info()
        print(f"\nHello {name}! Next year you will be {age + 1}.")
        calculator()
        receipt(name, age)
        print("\nThank you, goodbye!")
    except (KeyboardInterrupt, EOFError):
        print("\n\nProgram stopped. Goodbye!")


main()
