from flask import Flask, jsonify, request
import pymysql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app

# Connect to the MySQL AWS RDS instance
conn = pymysql.connect(
    host="petdatabase.c6yxltpk0xpz.us-east-1.rds.amazonaws.com",
    port=3306,
    user="petadmin",
    password="intelibancosecreto",
    db="store",
)

# Enable debugging
app.debug = True


def create_tables():
    print("Creating tables...")
    cur = conn.cursor()

    create_user_table_query = """
        CREATE TABLE IF NOT EXISTS User (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            UNIQUE (email)
        )
    """

    create_basket_table_query = """
        CREATE TABLE IF NOT EXISTS Basket (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            FOREIGN KEY (user_id) REFERENCES User(id)
        )
    """

    create_product_table_query = """
        CREATE TABLE IF NOT EXISTS Product (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            price INT NOT NULL,
            description TEXT,
            image VARCHAR(255) NOT NULL
        )
    """

    create_basket_product_table_query = """
        CREATE TABLE IF NOT EXISTS BasketProduct (
            id INT AUTO_INCREMENT PRIMARY KEY,
            basket_id INT,
            product_id INT,
            quantity INT,
            FOREIGN KEY (basket_id) REFERENCES Basket(id),
            FOREIGN KEY (product_id) REFERENCES Product(id)
        )
    """

    create_bought_product_table_query = """
        CREATE TABLE IF NOT EXISTS BoughtProduct (
            user_id INT,
            product_id INT,
            quantity INT,
            FOREIGN KEY (user_id) REFERENCES User(id),
            FOREIGN KEY (product_id) REFERENCES Product(id)
        )
    """

    create_table_queries = [
        create_user_table_query,
        create_basket_table_query,
        create_product_table_query,
        create_basket_product_table_query,
        create_bought_product_table_query,
    ]

    for query in create_table_queries:
        print("SQL Query:", query)
        cur.execute(query)

    conn.commit()
    cur.close()
    print("Tables created successfully!")


# CRUD endpoints for User
@app.route("/users", methods=["GET"])
@app.route("/users/<int:user_id>", methods=["GET"])
def get_users(user_id=None):
    cur = conn.cursor()

    if user_id is None:
        cur.execute("SELECT * FROM User")
    else:
        cur.execute("SELECT * FROM User WHERE id = %s", (user_id,))

    rows = cur.fetchall()
    cur.close()

    users = []
    for row in rows:
        user = {
            "id": row[0],
            "email": row[1],
            "password": row[2],
        }
        users.append(user)

    return jsonify(users)


@app.route("/users", methods=["POST"])
def add_user():
    try:
        user_data = request.get_json()
        email = user_data.get("email")
        password = user_data.get("password")

        cur = conn.cursor()

        # Check if the email already exists in the database
        cur.execute("SELECT id FROM User WHERE email = %s", (email,))
        existing_user = cur.fetchone()

        if existing_user:
            cur.close()
            return "An account with this email already exists.", 409

        # Email doesn't exist, proceed with registration
        cur.execute(
            "INSERT INTO User (email, password) VALUES (%s, %s)",
            (email, password),
        )
        conn.commit()

        # Get the ID of the newly inserted user
        user_id = cur.lastrowid

        # Create a basket for the user
        cur.execute(
            "INSERT INTO Basket (user_id) VALUES (%s)",
            (user_id,),
        )
        conn.commit()

        cur.close()

        return "", 204
    except Exception as e:
        print("Error:", e)
        return "An error occurred while registering the user.", 500


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user_data = request.get_json()
    email = user_data.get("email")
    password = user_data.get("password")

    cur = conn.cursor()
    cur.execute(
        "UPDATE User SET email=%s, password=%s WHERE id=%s",
        (email, password, user_id),
    )
    conn.commit()
    cur.close()

    return "", 204


@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    cur = conn.cursor()
    cur.execute("DELETE FROM User WHERE id=%s", (user_id,))
    conn.commit()
    cur.close()

    return "", 204


# CRUD endpoints for Product
@app.route("/products", methods=["GET"])
@app.route("/products/<int:product_id>", methods=["GET"])
def get_products(product_id=None):
    cur = conn.cursor()

    if product_id is None:
        cur.execute("SELECT * FROM Product")
    else:
        cur.execute("SELECT * FROM Product WHERE id = %s", (product_id,))

    rows = cur.fetchall()
    cur.close()

    products = []
    for row in rows:
        product = {
            "id": row[0],
            "name": row[1],
            "price": row[2],
            "description": row[3],
            "image": row[4],
        }
        products.append(product)

    return jsonify(products)


@app.route("/products", methods=["POST"])
def add_product():
    product_data = request.get_json()
    name = product_data.get("name")
    price = product_data.get("price")
    description = product_data.get("description")
    image = product_data.get("image")

    cur = conn.cursor()
    cur.execute(
        "INSERT INTO Product (name, price, description, image) VALUES (%s, %s, %s, %s)",
        (name, price, description, image),
    )
    conn.commit()
    cur.close()

    return "", 204


@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product_data = request.get_json()
    name = product_data.get("name")
    price = product_data.get("price")
    description = product_data.get("description")
    image = product_data.get("image")

    cur = conn.cursor()
    cur.execute(
        "UPDATE Product SET name=%s, price=%s, description=%s, image=%s WHERE id=%s",
        (name, price, description, image, product_id),
    )
    conn.commit()
    cur.close()

    return "", 204


@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    cur = conn.cursor()
    cur.execute("DELETE FROM Product WHERE id=%s", (product_id,))
    conn.commit()
    cur.close()

    return "", 204


# CRUD endpoints for Basket Products
@app.route("/baskets/<int:basket_id>/products", methods=["POST"])
def add_product_to_basket(basket_id):
    product_data = request.get_json()
    product_id = product_data.get("product_id")
    quantity = product_data.get("quantity")

    cur = conn.cursor()
    cur.execute(
        "INSERT INTO BasketProduct (basket_id, product_id, quantity) VALUES (%s, %s, %s)",
        (basket_id, product_id, quantity),
    )
    conn.commit()
    cur.close()

    return "", 204


@app.route("/users/<int:user_id>/basket/products", methods=["GET"])
def get_products_in_basket(user_id):
    cur = conn.cursor()

    # Retrieve all products in the user's basket
    cur.execute(
        "SELECT p.id, p.name, p.price, p.description, p.image, bp.quantity "
        "FROM Product p "
        "JOIN BasketProduct bp ON p.id = bp.product_id "
        "JOIN Basket b ON bp.basket_id = b.id "
        "WHERE b.user_id = %s",
        (user_id,),
    )

    rows = cur.fetchall()
    cur.close()

    products_in_basket = []
    for row in rows:
        product = {
            "id": row[0],
            "name": row[1],
            "price": row[2],
            "description": row[3],
            "image": row[4],
            "quantity": row[5],
        }
        products_in_basket.append(product)

    return jsonify(products_in_basket)


@app.route("/baskets/<int:basket_id>/products/<int:product_id>", methods=["DELETE"])
def remove_product_from_basket(basket_id, product_id):
    cur = conn.cursor()
    cur.execute(
        "DELETE FROM BasketProduct WHERE basket_id=%s AND product_id=%s",
        (basket_id, product_id),
    )
    conn.commit()
    cur.close()

    return "", 204


# Endpoint to process payment and move items to BoughtProduct table
@app.route("/baskets/<int:basket_id>/checkout", methods=["POST"])
def checkout_basket(basket_id):
    cur = conn.cursor()

    # Get the items in the user's basket
    cur.execute(
        "SELECT product_id, quantity FROM BasketProduct WHERE basket_id = %s",
        (basket_id,),
    )
    basket_items = cur.fetchall()

    # Move items to BoughtProduct table
    for product_id, quantity in basket_items:
        cur.execute(
            "INSERT INTO BoughtProduct (user_id, product_id, quantity) VALUES (%s, %s, %s)",
            (basket_id, product_id, quantity),
        )

    # Clear the basket by deleting items from BasketProduct
    cur.execute("DELETE FROM BasketProduct WHERE basket_id = %s", (basket_id,))

    conn.commit()
    cur.close()

    return "Payment processed successfully. Items moved to BoughtProduct table.", 200


@app.route("/create_tables", methods=["GET"])
def create_tables_route():
    try:
        create_tables()
        return "Tables created successfully!", 200
    except Exception as e:
        return f"An error occurred while creating the tables: {e}", 500


if __name__ == "__main__":
    app.run()
