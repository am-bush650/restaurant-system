import sqlite3

class Database:
    """Handles database connection and initialization"""
    def __init__(self, db_name="restaurant.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Creates necessary tables if they do not exist"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders(
                order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_name TEXT NOT NULL,
                order_date TEXT NOT NULL,
                total_amount REAL NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS menu_items(
                item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS order_menu_items (
                order_id INTEGER,
                item_id INTEGER,
                quantity INTEGER,
                FOREIGN KEY(order_id) REFERENCES orders(order_id),
                FOREIGN KEY(item_id) REFERENCES menu_items(item_id),
                PRIMARY KEY (order_id, item_id)
            )
        ''')
        self.conn.commit()

    def close(self):
        """Closes database connection"""
        self.conn.close()


class Order:
    def __init__(self, db, customer_name, order_date, total_amount):
        self.db = db
        self.customer_name = customer_name
        self.order_date = order_date
        self.total_amount = total_amount

    def save(self):
        """Inserts a new order into the database"""
        cursor = self.db.cursor
        cursor.execute(
            "INSERT INTO orders (customer_name, order_date, total_amount) VALUES (?, ?, ?)",
            (self.customer_name, self.order_date, self.total_amount)
        )
        self.db.conn.commit()
        self.order_id = cursor.lastrowid


    @classmethod
    def get_all(cls, db):
        """Fetches all orders"""
        db.cursor.execute("SELECT * FROM orders")
        return db.cursor.fetchall()

    @classmethod
    def find_by_id(cls, db, order_id):
        """Finds an order by ID"""
        db.cursor.execute("SELECT * FROM orders WHERE order_id = ?", (order_id,))
        return db.cursor.fetchone()

    @classmethod
    def delete(cls, db, order_id):
        """Deletes an order by ID"""
        db.cursor.execute("DELETE FROM orders WHERE order_id = ?", (order_id,))
        db.conn.commit()


class MenuItem:
    def __init__(self, db, item_name, price):
        self.db = db
        self.item_name = item_name
        self.price = price
        self.item_id = None

    def save(self):
        cursor = self.db.cursor
        cursor.execute("INSERT INTO menu_items (item_name, price) VALUES (?, ?)", (self.item_name, self.price))
        self.db.conn.commit()
        self.item_id = cursor.lastrowid

    @classmethod
    def get_all(cls, db):
        """Fetches all menu items"""
        db.cursor.execute("SELECT * FROM menu_items")
        return db.cursor.fetchall()

    @classmethod
    def find_by_id(cls, db, item_id):
        """Finds a menu item by ID"""
        db.cursor.execute("SELECT * FROM menu_items WHERE item_id = ?", (item_id,))
        return db.cursor.fetchone()

    @classmethod
    def delete(cls, db, item_id):
        """Deletes a menu item by ID"""
        db.cursor.execute("DELETE FROM menu_items WHERE item_id = ?", (item_id,))
        db.conn.commit()

class OrderMenuItem:
    """Manages Many-to-Many relationships"""
    @classmethod
    def add_menu_item_to_order(cls, db, order_id, item_id, quantity):
        db.cursor.execute(
            "INSERT INTO order_menu_items (order_id, item_id, quantity) VALUES (?, ?, ?)",
            (order_id, item_id, quantity)
        )
        db.conn.commit()

    @classmethod
    def get_menu_items_for_order(cls, db, order_id):
        db.cursor.execute(
            """SELECT menu_items.item_name, order_menu_items.quantity 
               FROM order_menu_items 
               JOIN menu_items ON order_menu_items.item_id = menu_items.item_id 
               WHERE order_menu_items.order_id = ?""",
            (order_id,)
        )
        return db.cursor.fetchall()
