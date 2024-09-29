grocery_items = [
    ("Apples", 0.50, "Fresh red apples"),
    ("Bananas", 0.30, "Ripe yellow bananas"),
    ("Bread", 2.00, "Whole wheat bread loaf"),
    ("Milk", 2.50, "1 gallon of whole milk"),
    ("Eggs", 3.00, "A dozen large eggs"),
    ("Cheese", 4.00, "Sharp cheddar cheese block"),
    ("Cereal", 3.50, "Whole grain cereal box"),
    ("Pasta", 1.50, "Dry spaghetti pasta"),
    ("Tomatoes", 1.00, "Fresh vine tomatoes"),
    ("Onions", 0.75, "Yellow onions"),
    ("Potatoes", 1.25, "Russet potatoes"),
    ("Chicken", 5.00, "Boneless chicken breast"),
    ("Beef", 6.00, "Ground beef"),
    ("Fish", 7.00, "Fresh salmon fillet"),
    ("Rice", 2.00, "Long-grain white rice"),
    ("Beans", 1.00, "Canned black beans"),
    ("Carrots", 0.75, "Fresh carrots"),
    ("Lettuce", 1.50, "Crisp romaine lettuce"),
    ("Yogurt", 2.00, "Greek yogurt"),
    ("Ice Cream", 4.50, "Vanilla ice cream"),
    ("Coffee", 5.00, "Ground coffee"),
    ("Tea", 3.00, "Herbal tea"),
    ("Juice", 2.50, "Orange juice"),
    ("Soda", 1.50, "Carbonated soft drink"),
    ("Chips", 2.00, "Potato chips"),
    ("Cookies", 2.50, "Chocolate chip cookies"),
    ("Candy", 1.00, "Mixed candy pack"),
    ("Chocolate", 2.00, "Dark chocolate bar"),
    ("Soap", 1.50, "Bar of soap"),
    ("Shampoo", 3.50, "Bottle of shampoo")
]

TAX_RATE = 0.09
BAG_COST = 0.08
ITEMS_PER_BAG = 5

# ItemToPurchase class definition
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name}: {self.item_quantity} @ ${self.item_price:.2f} = ${total:.2f}")

def print_store_menu():
    print("\n" + "="*40)
    print("Welcome to the Simple Grocery Store!")
    print("="*40)
    for i, (item, price, description) in enumerate(grocery_items, 1):
        print(f"{i:2}. {item:<15} ${price:.2f}")
        if i % 6 == 0:
            print()

def get_user_selection():
    while True:
        try:
            selection = input("Enter the numbers of the items you want (comma-separated): ")
            return [int(x.strip()) for x in selection.split(",") if 1 <= int(x.strip()) <= len(grocery_items)]
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")

def calculate_bags_needed(total_items):
    return max(1, (total_items + ITEMS_PER_BAG - 1) // ITEMS_PER_BAG)

global_cart = []

def main():
    print_store_menu()
    selected_items = get_user_selection()

    total_items = 0
    for item_num in selected_items:
        # Retrieve item details from grocery_items
        item_name, item_price, item_description = grocery_items[item_num - 1]
        quantity = int(input(f"How many {item_name} do you want? "))
        # Add item with description to global_cart
        global_cart.append(ItemToPurchase(item_name, item_price, quantity, item_description))
        total_items += quantity

    print("\n" + "="*40)
    print("Your Receipt")
    print("="*40)
    subtotal = 0
    for item in global_cart:
        item.print_item_cost()
        subtotal += item.item_price * item.item_quantity

    bags_needed = calculate_bags_needed(total_items)
    bag_charge = bags_needed * BAG_COST
    tax = subtotal * TAX_RATE
    total_cost = subtotal + bag_charge + tax

    print("-"*40)
    print(f"Subtotal:     ${subtotal:>6.2f}")
    print(f"Bag Charge:   ${bag_charge:>6.2f} ({bags_needed} bag{'s' if bags_needed > 1 else ''} @ ${BAG_COST:.2f} each)")
    print(f"Tax (9%):     ${tax:>6.2f}")
    print(f"Total:        ${total_cost:>6.2f}")
    print("="*40)
    print("Thank you for shopping with us!")

if __name__ == "__main__":
    main()

#cell #2

import datetime

# ItemToPurchase class definition
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name}: {self.item_quantity} @ ${self.item_price:.2f} = ${total:.2f}")

# ShoppingCart class
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        """Adds an ItemToPurchase to the cart."""
        self.cart_items.append(item)

    def remove_item(self, item_name):
        """Removes an item from the cart by name (case-insensitive)."""
        item_found = False
        for item in self.cart_items:
            if item.item_name.lower() == item_name.lower():  # Case-insensitive comparison
                self.cart_items.remove(item)
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_update):
        """Modifies the quantity, description, or price of an item in the cart."""
        item_found = False
        for cart_item in self.cart_items:
            if cart_item.item_name.lower() == item_to_update.item_name.lower():  # Case-insensitive comparison
                item_found = True
                # Update item details if new values are provided
                if item_to_update.item_description != "none":
                    cart_item.item_description = item_to_update.item_description
                if item_to_update.item_price != 0.0:
                    cart_item.item_price = item_to_update.item_price
                if item_to_update.item_quantity != 0:
                    cart_item.item_quantity = item_to_update.item_quantity
                break
        if not item_found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        """Returns the total number of items in the cart."""
        total_quantity = sum(item.item_quantity for item in self.cart_items)
        return total_quantity

    def get_cost_of_cart(self):
        """Returns the total cost of the items in the cart."""
        total_cost = sum(item.item_price * item.item_quantity for item in self.cart_items)
        return total_cost

    def print_total(self):
        """Prints the total cost of the cart."""
        if len(self.cart_items) == 0:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                total_item_cost = item.item_price * item.item_quantity
                print(f"{item.item_name} {item.item_quantity} @ ${item.item_price:.2f} = ${total_item_cost:.2f}")
            print(f"Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        """Prints the descriptions of each item in the cart."""
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")

def print_menu(cart):
    menu = '''
MENU
a - Add item to cart
r - Remove item from cart
c - Change item quantity
i - Output items' descriptions
o - Output shopping cart
q - Quit
'''
    while True:
        print(menu)
        choice = input("Choose an option: ").lower().strip()  # Remove leading/trailing whitespace

        if choice == 'a':
            # Add an item from grocery_items to the cart
            print("\nAvailable Items:")
            for i, (item_name, item_price, item_description) in enumerate(grocery_items, 1):
                print(f"{i}. {item_name}: ${item_price:.2f} - {item_description}")

            while True:
                try:
                    item_index = int(input("Enter the number of the item to add: ")) - 1
                    if 0 <= item_index < len(grocery_items):
                        item_name, item_price, item_description = grocery_items[item_index]
                        while True:
                            try:
                                item_quantity = int(input(f"Enter quantity of {item_name}: "))
                                if item_quantity <= 0:
                                    print("Quantity must be a positive integer.")
                                else:
                                    break
                            except ValueError:
                                print("Invalid input. Please enter a valid number.")
                        new_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
                        cart.add_item(new_item)
                        break
                    else:
                        print("Invalid item selection.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        elif choice == 'r':
            # Remove an item from the cart (case-insensitive)
            while True:
                item_name = input("Enter the name of the item to remove: ").strip()
                if item_name:
                    cart.remove_item(item_name)
                    break
                else:
                    print("Please enter a valid item name.")

        elif choice == 'c':
            # Modify an existing item in the cart (case-insensitive)
            while True:
                item_name = input("Enter the item name to modify: ").strip()
                if item_name:
                    break
                else:
                    print("Please enter a valid item name.")

            while True:
                item_description = input("Enter the new item description (or 'none' to skip): ").strip()
                if item_description.lower() == 'none':
                    item_description = None
                    break
                elif item_description:
                    break
                else:
                    print("Please enter a valid description or 'none' to skip.")

            while True:
                try:
                    item_price = float(input("Enter the new item price (or 0 to skip): "))
                    if item_price < 0:
                        print("Price cannot be negative.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            while True:
                try:
                    item_quantity = int(input("Enter the new item quantity (or 0 to skip): "))
                    if item_quantity < 0:
                        print("Quantity cannot be negative.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

            updated_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            cart.modify_item(updated_item)

        elif choice == 'i':
            # Output items' descriptions
            cart.print_descriptions()

        elif choice == 'o':
            # Output shopping cart
            cart.print_total()

        elif choice == 'q':
            # Quit the menu
            break

        else:
            print("Invalid option. Please choose again.")

# Main function to transfer global_cart data from the first cell
def main():
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date (leave blank for today's date): ")
    if not current_date:
        current_date = datetime.date.today().strftime("%B %d, %Y")

    # Create the new cart
    cart = ShoppingCart(customer_name, current_date)

    # Transfer items from the global_cart (from first cell) to the new ShoppingCart
    for item in global_cart:  # Use the global_cart from the first cell
        cart.add_item(item)

    print(f"\nCustomer name: {cart.customer_name}")
    print(f"Today's date: {cart.current_date}")

    print_menu(cart)

if __name__ == "__main__":
    main()
