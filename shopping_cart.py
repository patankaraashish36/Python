class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []  # Instance variable to store items in this cart

    def total(self):
        return sum(item.price for item in self.items)

    def add(self, item):
        self.items.append(item)

    def __len__(self):  # Overriding len() to get the length of items
        return len(self.items)

if __name__ == '__main__':
    # Test the implementation
    items = []
    n = int(input("Enter number of items: "))
    for _ in range(n):
        name, price = input("Enter name and price (separated by space): ").split()
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = int(input("Enter number of commands: "))
    for _ in range(q):
        line = input("Enter command (add, total, or len): ").split()
        command, params = line[0], line[1:]
        if command == "len":
            print(len(cart))
        elif command == "total":
            print(cart.total())
        elif command == "add":
            name = params[0]
            item = next((item for item in items if item.name == name), None)
            if item:
                cart.add(item)
                print(f"Added {item.name} to the cart.")
            else:
                print("Item not found.")
        else:
            raise ValueError("Unknown command %s" % command)
