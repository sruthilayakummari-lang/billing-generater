# products.py
# Stores supermarket product names and prices

items = {
    "rice": 20,
    "sugar": 30,
    "salt": 20,
    "oil": 80,
    "paneer": 110,
    "maggi": 50,
    "boost": 90,
    "colgate": 85
}

def display_items():
    print("\nAvailable Items:")
    print("-" * 35)
    print(f"{'Item':<12}{'Price':<12}{'Unit'}")
    print("-" * 35)
    print("Rice        Rs 200        per kg")
    print("Sugar       Rs 80        per kg")
    print("Salt        Rs 90        per kg")
    print("Oil         Rs 180        per liter")
    print("Paneer      Rs 110       per kg")
    print("Maggi       Rs 50        each")
    print("Boost       Rs 290        each")
    print("Colgate     Rs 85        each")
    print("-" * 35)
