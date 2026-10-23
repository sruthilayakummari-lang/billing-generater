# receipt.py
# Prints the final supermarket bill

from datetime import datetime
from products import items

def generate_bill(name, cart, totalprice, gst, finalamount):
    if finalamount <= 0:
        print("No items were purchased. No bill generated.")
        return

    print("\n" + "=" * 45)
    print("          KIRAN SUPERMARKET")
    print("              WANAPARTHY")
    print("=" * 45)
    print("Customer Name:", name)
    print("Date:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
    print("-" * 45)
    print(f"{'S.No':<6}{'Item':<12}{'Qty':<8}{'Price':>12}")
    print("-" * 45)

    for i, (item, quantity) in enumerate(cart.items(), start=1):
        price = items[item] * quantity
        print(f"{i:<6}{item.capitalize():<12}{quantity:<8}{price:>12.2f}")

    print("-" * 45)
    print(f"Total Amount: Rs {totalprice:.2f}")
    print(f"GST (5%):     Rs {gst:.2f}")
    print("-" * 45)
    print(f"Final Amount: Rs {finalamount:.2f}")
    print("=" * 45)
    print("       Thanks for visiting!")
    print("=" * 45)
