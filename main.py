# main.py
# Main program: collects purchases and connects the modules

from products import items, display_items
from billing import calculate_bill
from receipt import generate_bill

def main():
    name = input("Enter your name: ").strip()
    if not name:
        name = "Customer"

    option = input("To see the list of items, press 1: ").strip()

    if option != "1":
        print("You entered a wrong number.")
        return

    display_items()
    cart = {}

    while True:
        choice = input("\nPress 1 to buy or 2 to exit: ").strip()

        if choice == "2":
            break
        elif choice != "1":
            print("You entered a wrong number. Please press 1 or 2.")
            continue

        item = input("Enter your item: ").lower().strip()

        if item not in items:
            print("Sorry, this item is not available.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        cart[item] = cart.get(item, 0) + quantity
        print(f"{quantity} x {item.capitalize()} added to cart.")

    totalprice, gst, finalamount = calculate_bill(cart)

    if finalamount <= 0:
        print("No items were purchased. No bill generated.")
        return

    answer = input("Can I bill the items? (yes/no): ").lower().strip()

    if answer == "yes":
        generate_bill(name, cart, totalprice, gst, finalamount)
    else:
        print("Bill generation cancelled.")

if __name__ == "__main__":
    main()
