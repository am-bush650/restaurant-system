# CLI RESTAURANT SYSTEM


This is a CLI-based restaurant management system built using Python, SQLite, and SQLAlchemy ORM. It allows users to:


📌 Manage Orders (Create, View, Delete)

📌 Manage Menu Items (Create, View, Delete)

📌 Link Orders to Menu Items (Many-to-Many Relationship)

📌 Seed the Database with Fake Data using Faker

📌 Perform CRUD operations with an Interactive CLI


## Relationships

        ### one-to-many relationship

        -orders - Each order is associated with one customer(customer_name).
        -orders contain multiple items - handled via OrderMenuItem in the many to many setup


        ### many-to-many relationship

        -an order can have multiple menu items
        -a menu item can appear in multiple orders
        the order_menu_items table acts as a join table that links orders and menu_items with an additional quantity column

## Database Schema


The system has the following tables:


📌 orders → Stores customer orders. 

    order_id(primary key), customer_name, order_date, total_amount

📌 menu_items → Stores restaurant menu items. 

    item_id,(primary key), item_name, price

📌 order_menu_items → Links orders and menu items. 

    order_id(foreign key), item_id(foreign key), quantity



## Features


### Orders Management

Add a new order

View all orders

Find an order by ID

Delete an order

### Menu Items Management

Add a menu item

View all menu items

Find a menu item by ID

Delete a menu item


### Database Seeding

Automatically populates the database with random orders and menu items.

Uses Faker for fake customer names and order dates.


## Technologies Used


📌 Python (CLI & ORM)

📌 SQLite (Database)

📌 SQLAlchemy (ORM for Database Operations)

📌 Faker (Generates Fake Data)

📌 IPDB (Debugging)




#################################################################

CLI COMMANDS - python cli.py
source phase3project/bin/activate
