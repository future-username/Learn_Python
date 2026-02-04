# def normalize(value: str) -> str:
#     """Normalize input string by removing extra spaces and replacing comma with dot."""
#     return value.strip().replace(',', '.')
#
#
# def check(value: str) -> bool:
#     """Check if the value is a valid positive number."""
#     try:
#         num = float(value)
#         return num > 0
#     except ValueError:
#         return False
#
#
# def get_price(price: float, weight: float) -> float:
#     """Calculate total price based on unit price and weight."""
#     return price * weight
#
#
# def main():
#     """Main function to calculate total price."""
#     # Input price
#     price_input = input("Enter price per unit: ")
#
#     # Input weight
#     weight_input = input("Enter weight: ")
#
#     # Normalize inputs
#     price_normalized = normalize(price_input)
#     weight_normalized = normalize(weight_input)
#
#     # Check inputs
#     price_valid = check(price_normalized)
#     weight_valid = check(weight_normalized)
#
#     # Calculate or show error
#     if price_valid and weight_valid:
#         price = float(price_normalized)
#         weight = float(weight_normalized)
#         total_price = get_price(price, weight)
#         print(f"Total price: {total_price:.2f}")
#     else:
#         print("Error: Invalid input. Please enter valid positive numbers.")
#
#
# if __name__ == "__main__":
#     main()


def normalize(value: str) -> str:
    """
    Participant: Normalize
    Логика: убираем пробелы, меняем запятые на точки (как пример нормализации).
    """
    return value.strip().replace(',', '.')


def get_price(price: float, weight: float) -> float:
    """
    Participant: GetPrice
    Логика: price * weight
    """
    return price * weight


def main():
    # 1. Main -> Input: Input price
    price_input = input("Enter price: ")

    # 2. Main -> Input: Input weight
    weight_input = input("Enter weight: ")

    # 3. Main -> Normalize: Normalize price
    price_norm = normalize(price_input)

    # 4. Main -> Normalize: Normalize weight
    weight_norm = normalize(weight_input)

    # 5. Alt block: Проверка валидности (строго по диаграмме)
    # replace('.', '', 1) позволяет проверить дробное число через isdigit
    is_price_valid = price_norm.replace('.', '', 1).isdigit()
    is_weight_valid = weight_norm.replace('.', '', 1).isdigit()

    if is_price_valid and is_weight_valid:
        # Main -> GetPrice: Get FULL price
        # Примечание: Диаграмма требует float на входе get_price, поэтому конвертируем здесь
        final_price = get_price(float(price_norm), float(weight_norm))
        print(f"Total price: {final_price}")
    else:
        # Error message
        print("Error: Invalid input. Please enter numbers.")


if __name__ == "__main__":
    main()