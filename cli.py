from model import Database, Order, MenuItem, OrderMenuItem

# Initialize database
db = Database()

def main():
    while True:
        print("\nMain Menu:")
        print("1. Manage Orders")
        print("2. Manage Menu Items")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            manage_orders()
        elif choice == "2":
            manage_menu_items()
        elif choice == "3":
            db.close()  # Close DB connection before exiting
            break
        else:
            print("Invalid option. Please try again.")

def manage_orders():
    while True:
        print("\nOrder Management:")
        print("1. Create Order")
        print("2. View All Orders")
        print("3. Find Order by ID")
        print("4. Delete Order")
        print("5. Add Menu Item to Order")  # Fixed option name
        print("6. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            create_order()
        elif choice == "2":
            view_orders()
        elif choice == "3":
            find_order()
        elif choice == "4":
            delete_order()
        elif choice == "5":
            add_menu_item_to_order()  # Correct function call
        elif choice == "6":
            break
        else:
            print("Invalid option. Please try again.")

def manage_menu_items():
    while True:
        print("\nMenu Item Management: ")
        print("1. Create Menu Item")
        print("2. View All Menu Items")
        print("3. Find Menu Item by ID")
        print("4. Delete Menu Item")
        print("5. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            create_menu_item()
        elif choice == "2":
            view_menu_items()
        elif choice == "3":
            find_menu_item()
        elif choice == "4":
            delete_menu_item()
        elif choice == "5":
            break
        else:
            print("Invalid option. Please try again.")

# --- Order Functions ---
def create_order():
    name = input("Enter customer name: ")
    date = input("Enter order date (YYYY-MM-DD): ")
    amount = float(input("Enter total amount: "))
    order = Order(db, name, date, amount)
    order.save()
    print("Order created successfully.")

def view_orders():
    orders = Order.get_all(db)
    if orders:
        for order in orders:
            print(order)
    else:
        print("No orders found.")

def find_order():
    order_id = int(input("Enter Order ID: "))
    order = Order.find_by_id(db, order_id)
    print(order if order else "Order not found.")

def delete_order():
    order_id = int(input("Enter Order ID to delete: "))
    Order.delete(db, order_id)
    print("Order deleted successfully.")

def add_menu_item_to_order():
    ipdb.set_trace()  # Debugging
    order_id = int(input("Enter Order ID: "))
    item_id = int(input("Enter Menu Item ID: "))
    quantity = int(input("Enter quantity: "))

    order = Order.find_by_id(db, order_id)
    item = MenuItem.find_by_id(db, item_id)

    if order and item:
        OrderMenuItem.add_menu_item_to_order(db, order_id, item_id, quantity)
        print("Menu item added to order successfully.")
    else:
        print("Invalid Order ID or Menu Item ID.")

# --- Menu Item Functions ---
def create_menu_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    menu_item = MenuItem(db, name, price)
    menu_item.save()
    print("Menu item created successfully.")

def view_menu_items():
    items = MenuItem.get_all(db)
    if items:
        for item in items:
            print(item)
    else:
        print("No menu items found.")

def find_menu_item():
    item_id = int(input("Enter Menu Item ID: "))
    item = MenuItem.find_by_id(db, item_id)
    print(item if item else "Menu item not found.")

def delete_menu_item():
    item_id = int(input("Enter Menu Item ID to delete: "))
    MenuItem.delete(db, item_id)
    print("Menu item deleted successfully.")

if __name__ == "__main__":
    main()
