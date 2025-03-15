from faker import Faker
import random
from model import Database, Order, MenuItem, OrderMenuItem

fake = Faker()
db = Database()


menu_items = []
for _ in range(10):
    item_name = fake.word().capitalize()
    price = round(random.uniform(5, 50), 2)
    print(f"Creating MenuItem: {item_name}, ${price}") 
    item = MenuItem(db, item_name, price)
    item.save()
    menu_items.append(item)

print("Menu Items Created")


orders = []
for _ in range(5):
    customer_name = fake.name()
    order_date = fake.date()
    total_amount = round(random.uniform(20, 200), 2)
    print(f"Creating Order: {customer_name}, {order_date}, ${total_amount}")
    order = Order(db, customer_name, order_date, total_amount)
    order.save()
    orders.append(order)

print("Orders Created")

for order in orders:
    num_items = random.randint(1, 3)
    selected_items = random.sample(menu_items, num_items)
    for item in selected_items:
        quantity = random.randint(1, 5)
        print(f"Linking Order {order.order_id} with MenuItem {item.item_id}, Quantity: {quantity}")
        OrderMenuItem.add_menu_item_to_order(db, order_id=order.order_id, item_id=item.item_id, quantity=quantity)


db.close()
