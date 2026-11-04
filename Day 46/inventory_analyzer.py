
products = []


def add_product():
    print("\n===== ADD PRODUCT =====")

    name = input("Enter product name: ").strip()

    if not name:
        print("Product name cannot be empty!")
        return

    quantity = get_number("Enter quantity: ", 0)
    price = get_number("Enter price per item: ₹", 0)

    # Prevent duplicate product names
    for product in products:
        if product["name"].lower() == name.lower():
            print("Product already exists!")
            return

    product = {
        "name": name,
        "quantity": quantity,
        "price": price
    }

    products.append(product)
    print("Product added successfully!")


def get_number(message, minimum):
    while True:
        try:
            number = float(input(message))

            if number < minimum:
                print(f"Enter a value of at least {minimum}.")
                continue

            return number

        except ValueError:
            print("Invalid input! Enter a valid number.")


def display_products():
    if not products:
        print("\nNo products available.")
        return

    print("\n===== INVENTORY DETAILS =====")

    for product in products:
        total_value = product["quantity"] * product["price"]

        print(f"\nProduct: {product['name']}")
        print(f"Quantity: {product['quantity']:g}")
        print(f"Price: ₹{product['price']:.2f}")
        print(f"Total Value: ₹{total_value:.2f}")


def calculate_inventory_value():
    total = 0

    for product in products:
        total += product["quantity"] * product["price"]

    print(f"\nTotal Inventory Value: ₹{total:.2f}")


def show_low_stock():
    print("\n===== LOW STOCK PRODUCTS =====")

    low_stock = [
        product for product in products
        if product["quantity"] <= 5
    ]

    if not low_stock:
        print("No low-stock products.")
        return

    for product in low_stock:
        print(
            f"{product['name']} - "
            f"{product['quantity']:g} units remaining"
        )


def show_top_products():
    if not products:
        print("\nNo products available.")
        return

    sorted_products = sorted(
        products,
        key=lambda product: (
            product["quantity"] * product["price"]
        ),
        reverse=True
    )

    print("\n===== PRODUCTS BY TOTAL VALUE =====")

    for product in sorted_products:
        value = product["quantity"] * product["price"]

        print(f"{product['name']} - ₹{value:.2f}")


def main():
    while True:
        print("\n===== INVENTORY ANALYZER =====")
        print("1. Add Product")
        print("2. Display All Products")
        print("3. Calculate Total Inventory Value")
        print("4. Show Low Stock Products")
        print("5. Sort Products by Total Value")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_product()

        elif choice == "2":
            display_products()

        elif choice == "3":
            calculate_inventory_value()

        elif choice == "4":
            show_low_stock()

        elif choice == "5":
            show_top_products()

        elif choice == "6":
            print("Thank you for using Inventory Analyzer!")
            break

        else:
            print("Invalid choice! Select from 1 to 6.")


if __name__ == "__main__":
    main()
