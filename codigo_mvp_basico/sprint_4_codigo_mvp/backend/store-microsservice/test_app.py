import json
import unittest
from app import app, conn


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        cur = conn.cursor()
        cur.execute("DELETE FROM User")
        cur.execute("DELETE FROM Product")
        conn.commit()
        cur.close()

    def test_get_users(self):
        # Add a user to the database
        cur = conn.cursor()
        cur.execute("INSERT INTO User (email, password) VALUES ('test@example.com', 'password')")
        conn.commit()
        cur.close()

        # Make a GET request to /users
        response = self.app.get('/users')

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the added user
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['email'], 'test@example.com')

    def test_get_user(self):
        # Add a user to the database
        cur = conn.cursor()
        cur.execute("INSERT INTO User (email, password) VALUES ('test@example.com', 'password')")
        conn.commit()
        cur.close()

        # Make a GET request to /users/1
        response = self.app.get('/users/1')

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the added user
        data = json.loads(response.data)
        self.assertEqual(data['email'], 'test@example.com')

    def test_add_user(self):
        # Make a POST request to /users with a new user
        response = self.app.post('/users', json={'email': 'test@example.com', 'password': 'password'})

        # Check that the response is successful
        self.assertEqual(response.status_code, 204)

        # Check that the user was added to the database
        cur = conn.cursor()
        cur.execute("SELECT * FROM User")
        data = cur.fetchall()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0][1], 'test@example.com')
        cur.close()

    def test_update_user(self):
        # Add a user to the database
        cur = conn.cursor()
        cur.execute("INSERT INTO User (email, password) VALUES ('test@example.com', 'password')")
        conn.commit()
        cur.close()

        # Make a PUT request to /users/1 with updated user data
        response = self.app.put('/users/1', json={'email': 'new@example.com', 'password': 'newpassword'})

        # Check that the response is successful
        self.assertEqual(response.status_code, 204)

        # Check that the user was updated in the database
        cur = conn.cursor()
        cur.execute("SELECT * FROM User")
        data = cur.fetchall()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0][1], 'new@example.com')
        cur.close()

    def test_delete_user(self):
        # Add a user to the database
        cur = conn.cursor()
        cur.execute("INSERT INTO User (email, password) VALUES ('test@example.com', 'password')")
        conn.commit()
        cur.close()

        # Make a DELETE request to /users/1
        response = self.app.delete('/users/1')

        # Check that the response is successful
        self.assertEqual(response.status_code, 204)

        # Check that the user was deleted from the database
        cur = conn.cursor()
        cur.execute("SELECT * FROM User")
        data = cur.fetchall()
        self.assertEqual(len(data), 0)
        cur.close()

    def test_get_products(self):
        # Add a product to the database
        cur = conn.cursor()
        cur.execute("INSERT INTO Product (name, price, description, image) VALUES ('Test Product', 9.99, 'A test product', 'test.jpg')")
        conn.commit()
        cur.close()

        # Make a GET request to /products
        response = self.app.get('/products')

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the added product
        data = json.loads(response.data)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'Test Product')

    def test_get_product(self):
        # Add a product to the database
        cur = conn.cursor()
        cur.execute("INSERT INTO Product (name, price, description, image) VALUES ('Test Product', 9.99, 'A test product', 'test.jpg')")
        conn.commit()
        cur.close()

        # Make a GET request to /products/1
        response = self.app.get('/products/1')

        # Check that the response is successful
        self.assertEqual(response.status_code, 200)

        # Check that the response contains the added product
        data = json.loads(response.data)
        self.assertEqual(data['name'], 'Test Product')

    def test_add_product(self):
        # Make a POST request to /products with a new product
        response = self.app.post('/products', json={'name': 'Test Product', 'price': 9.99, 'description': 'A test product', 'image': 'test.jpg'})

        # Check that the response is successful
        self.assertEqual(response.status_code, 204)

        # Check that the product was added to the database
        cur = conn.cursor()
        cur.execute("SELECT * FROM Product")
        data = cur.fetchall()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0][1], 'Test Product')
        cur.close()

    def test_update_product(self):
        # Add a product to the database
        cur = conn.cursor()
        cur.execute("INSERT INTO Product (name, price, description, image) VALUES ('Test Product', 9.99, 'A test product', 'test.jpg')")
        conn.commit()
        cur.close()

        # Make a PUT request to /products/1 with updated product data
        response = self.app.put('/products/1', json={'name': 'New Product', 'price': 19.99, 'description': 'A new product', 'image': 'new.jpg'})

        # Check that the response is successful
        self.assertEqual(response.status_code, 204)

        # Check that the product was updated in the database
        cur = conn.cursor()
        cur.execute("SELECT * FROM Product")
        data = cur.fetchall()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0][1], 'New Product')
        cur.close()


if __name__ == '__main__':
    unittest.main()
