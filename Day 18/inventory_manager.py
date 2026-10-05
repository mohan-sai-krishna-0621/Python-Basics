print("===== INVENTORY MANAGER =====")

inventory = []


def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    inventory.append(product)
    print("Product added successfully!")


def view_inventory():
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        print("\n===== INVENTORY =====")

        for i, product in enumerate(inventory, start=1):
            print(f"{i}. {product['name']}")
            print(f"   Price: ₹{product['price']}")
            print(f"   Quantity: {product['quantity']}")


def search_product():
    search = input("Enter product name to search: ")

    found = False

    for product in inventory:
        if product["name"].lower() == search.lower():
            print("\nProduct Found!")
            print("Name:", product["name"])
            print("Price: ₹", product["price"])
            print("Quantity:", product["quantity"])
            found = True
            break

    if not found:
        print("Product not found.")


def delete_product():
    name = input("Enter product name to delete: ")

    for product in inventory:
        if product["name"].lower() == name.lower():
            inventory.remove(product)
            print("Product deleted successfully!")
            return

    print("Product not found.")


while True:
    print("\n===== MENU =====")
    print("1. Add Product")
    print("2. View Inventory")
    print("3. Search Product")
    print("4. Delete Product")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_inventory()

    elif choice == "3":
        search_product()

    elif choice == "4":
        delete_product()

    elif choice == "5":
        print("Thank you for using Inventory Manager!")
        break

    else:
        print("Invalid choice. Please try again.")