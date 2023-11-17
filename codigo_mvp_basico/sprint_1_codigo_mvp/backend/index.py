from flask import Flask, jsonify, request
import pymysql
from flask_cors import CORS

# Connect to the MySQL AWS RDS instance
conn = pymysql.connect(
    host="<HOST_NAME>",
    port="<PORT_NUMBER>",
    user="<USER_NAME>",
    password="<PASSWORD>",
    db="<DATABASE_NAME>",
)

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app
app.config["CORS_HEADERS"] = "Content-Type"

# Enable debugging
app.debug = True


def create_pets_table():
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Pets (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            animal VARCHAR(50) NOT NULL,
            gender VARCHAR(10) NOT NULL,
            age INT NOT NULL,
            description TEXT,
            image VARCHAR(255)
        )
    """
    )
    conn.commit()
    cur.close()


@app.route("/pets", methods=["GET"])
@app.route("/pets/<int:pet_id>", methods=["GET"])
def get_pets(pet_id=None):
    cur = conn.cursor()

    if pet_id is None:
        cur.execute("SELECT * FROM Pets")
    else:
        cur.execute("SELECT * FROM Pets WHERE id = %s", (pet_id,))

    rows = cur.fetchall()
    cur.close()

    # Convert the list of tuples to a list of dictionaries
    pets = []
    for row in rows:
        pet = {
            "id": row[0],
            "name": row[1],
            "animal": row[2],
            "gender": row[3],
            "age": row[4],
            "description": row[5],
            "image": row[6],
        }
        pets.append(pet)

    return jsonify(pets)


@app.route("/pets", methods=["POST"])
def add_pet():
    pet_data = request.get_json()
    name = pet_data.get("name")
    animal = pet_data.get("animal")
    gender = pet_data.get("gender")
    age = pet_data.get("age")
    description = pet_data.get("description")
    image = pet_data.get("image")

    cur = conn.cursor()
    cur.execute(
        "INSERT INTO Pets (name, animal, gender, age, description, image) VALUES (%s, %s, %s, %s, %s, %s)",
        (name, animal, gender, age, description, image),
    )
    conn.commit()
    cur.close()

    return "", 204


@app.route("/pets/<int:index>", methods=["PUT"])
def update_pet(index):
    pet_data = request.get_json()
    name = pet_data.get("name")
    animal = pet_data.get("animal")
    gender = pet_data.get("gender")
    age = pet_data.get("age")
    description = pet_data.get("description")
    image = pet_data.get("image")

    cur = conn.cursor()
    cur.execute(
        "UPDATE Pets SET name=%s, animal=%s, gender=%s, age=%s, description=%s, image=%s WHERE id=%s",
        (name, animal, gender, age, description, image, index),
    )
    conn.commit()
    cur.close()

    return "", 204


@app.route("/pets/<int:index>", methods=["DELETE"])
def delete_pet(index):
    cur = conn.cursor()
    cur.execute("DELETE FROM Pets WHERE id=%s", (index,))
    conn.commit()
    cur.close()

    return "", 204


if __name__ == "__main__":
    create_pets_table()  # Call the function to create the Pets table
    app.run()
