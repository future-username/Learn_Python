def normalize(value: str) -> str:
    """Normalize input string by removing extra spaces and replacing comma with dot."""
    return value.strip().replace(',', '.')


def check(value: str) -> bool:
    """Check if the value is a valid positive number."""
    try:
        num = float(value)
        return num > 0
    except ValueError:
        return False


def get_price(price: float, weight: float) -> float:
    """Calculate total price based on unit price and weight."""
    return price * weight


def main():
    """Main function to calculate total price."""
    # Input price
    price_input = input("Enter price per unit: ")

    # Input weight
    weight_input = input("Enter weight: ")

    # Normalize inputs
    price_normalized = normalize(price_input)
    weight_normalized = normalize(weight_input)

    # Check inputs
    price_valid = check(price_normalized)
    weight_valid = check(weight_normalized)

    # Calculate or show error
    if price_valid and weight_valid:
        price = float(price_normalized)
        weight = float(weight_normalized)
        total_price = get_price(price, weight)
        print(f"Total price: {total_price:.2f}")
    else:
        print("Error: Invalid input. Please enter valid positive numbers.")


if __name__ == "__main__":
    main()