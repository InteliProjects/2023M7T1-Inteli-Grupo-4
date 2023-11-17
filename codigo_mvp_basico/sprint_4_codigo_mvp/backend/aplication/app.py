from flask import Flask, jsonify, request, render_template
import pymysql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app
app.config["CORS_HEADERS"] = "Content-Type"

# Connect to the MySQL AWS RDS instance
conn = pymysql.connect(
    host="petdatabase.c6yxltpk0xpz.us-east-1.rds.amazonaws.com",
    port=3306,
    user="petadmin",
    password="intelibancosecreto",
    db="store" ,
)

# Enable debugging
app.debug = True

# router ////////////////////////////////////////////////
@app.route("/", methods=["GET"])
def dashboard():
    return render_template("index.html")

@app.route("/resumo-de-pedidos", methods=["GET"])
def sumaryOrder():
    return render_template("sumaryOrder.html")

@app.route("/entrar", methods=["GET"])
def entrar():
    return render_template("login.html")

@app.route("/produtos", methods=["GET"])
def produtos():
    return render_template("produtos.html")

@app.route("/cadastro", methods=["GET"])
def cadUser():
    return render_template("signUp.html")

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
            "full_name": row[3],
            "celphone": row[4]
        }
        users.append(user)

    return jsonify(users)

# Rota de login
@app.route('/login', methods=['POST'])
def login():
    # Obtenha as credenciais do usuário do corpo da solicitação JSON
    user_data = request.json
    email = user_data.get('email')
    password = user_data.get('password')

    cur = conn.cursor()
    cur.execute(
        "SELECT id, password FROM User WHERE email = %s",
        (email,),
    )
    user = cur.fetchone()
    cur.close()

    if user is None:
        # Usuário não encontrado
        return jsonify({"message": "Usuário não encontrado"}), 401

    user_id, stored_password = user

    if password != stored_password:
        # Senha incorreta
        return jsonify({"message": "Senha incorreta"}), 401

    # Autenticação bem-sucedida, retorne o ID do usuário na resposta JSON
    return jsonify({"user_id": user_id, "message": "Autenticação bem-sucedida"})



@app.route("/users", methods=["POST"])
def add_user():
    user_data = request.get_json()
    email = user_data.get("email")
    password = user_data.get("password")
    full_name = user_data.get( "full_name")
    celphone = user_data.get("celphone")

    cur = conn.cursor()
    cur.execute(
        "INSERT INTO User (email, password, full_name, celphone) VALUES (%s, %s)",
        (email, password, full_name, celphone),
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

# render
@app.route("/productmachines", methods=["GET"])
def get_product_machines():
    cur = conn.cursor()

    cur.execute("SELECT * FROM productMachine")

    rows = cur.fetchall()
    cur.close()

    product_machines = []
    for row in rows:
        product_machine = {
            "id": row[0],
            "name": row[1],
            "price_divided": row[2],
            "price": row[3],
            "image": row[4],
            "description": row[5]
        }
        product_machines.append(product_machine)

    return jsonify(product_machines)


# CRUD endpoints for ProductPlan
@app.route("/productplans", methods=["GET"])
def get_product_plans():
    cur = conn.cursor()

    cur.execute("SELECT id, name, tax_deb, tax_cred, description FROM productPlan")

    rows = cur.fetchall()
    cur.close()

    product_plans = []
    for row in rows:
        product_plan = {
            "id": row[0],
            "name": row[1],
            "tax_deb": row[2],
            "tax_cred": row[3],
            "description": row[4]
        }
        product_plans.append(product_plan)

    return jsonify(product_plans)


@app.route("/baskets/<int:basket_id>", methods=["GET"])
def get_basket(basket_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Basket WHERE id = %s", (basket_id,))
    basket = cur.fetchone()
    cur.close()

    if basket:
        basket_dict = {
            "id": basket[0],
            "user_id": basket[1],
            "productMachine_ID": basket[2],
            "productPlan": basket[3],
            "quantity": basket[4]
        }
        return jsonify(basket_dict), 200
    else:
        return "Basket not found", 404

@app.route("/baskets/<int:basket_id>", methods=["PUT"])
def update_basket(basket_id):
    basket_data = request.get_json()
    user_id = basket_data.get("user_id")
    productMachine_ID = basket_data.get("productMachine_ID")
    productPlan = basket_data.get("productPlan")
    quantity = basket_data.get("quantity")

    cur = conn.cursor()
    cur.execute(
        "UPDATE Basket SET user_id=%s, productMachine_ID=%s, productPlan=%s, quantity=%s WHERE id=%s",
        (user_id, productMachine_ID, productPlan, quantity, basket_id),
    )
    conn.commit()
    cur.close()

    return "", 204

@app.route("/baskets/<int:basket_id>", methods=["DELETE"])
def delete_basket(basket_id):
    cur = conn.cursor()
    cur.execute("DELETE FROM Basket WHERE id=%s", (basket_id,))
    conn.commit()   
    cur.close()

    return "", 204

@app.route("/userbasket/<user_id>", methods=["GET"])
def get_user_basket(user_id):
    try:
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM Basket WHERE user_id = %s", (user_id,))
        basket_items = cur.fetchall()
        
        if not basket_items:
            return jsonify({"message": "No items found in the basket."}), 204

        detailed_basket = []
        
        for item in basket_items:
            product_machine_id = item[2]  
            product_plan_id = item[3]
            quantity = item[4]
            
            if product_machine_id:
                cur.execute("SELECT * FROM productMachine WHERE id = %s", (product_machine_id,))
                product_machine = cur.fetchone()
            else:
                product_machine = None
            
            if product_plan_id:
                cur.execute("SELECT * FROM productPlan WHERE id = %s", (product_plan_id,))
                product_plan = cur.fetchone()
            else:
                product_plan = None
            
            detailed_item = {
                "id": item[0],  
                "user_id": item[1],
                "quantity": quantity,
                "product_machine": {
                    "id": product_machine[0] if product_machine else None,
                    "name": product_machine[1] if product_machine else None,
                    "price_divided"	: product_machine[2] if product_machine else None,
                    "price"	: product_machine[3] if product_machine else None,
                    "image"	: product_machine[4] if product_machine else None,
                    "description": product_machine[5] if product_machine else None,
                },
                "product_plan": {
                    "tax_cred"	: product_plan[0] if product_plan else None,
                    "tax_cred_divided"	: product_plan[1] if product_plan else None,
                    "id"	: product_plan[2] if product_plan else None,
                    "tax_deb"	: product_plan[3] if product_plan else None,
                    "description"	: product_plan[4] if product_plan else None,
                    "name": product_plan[5] if product_plan else None,
                    # ... outros campos
                }
            }
            
            detailed_basket.append(detailed_item)

        return jsonify(detailed_basket), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/baskets-plans", methods=["POST"])
def create_or_update_basket():
    try:
        basket_data = request.get_json()
        user_id = basket_data.get("user_id")
        productPlan = basket_data.get("productPlan")
        quantity = basket_data.get("quantity")
        cur = conn.cursor()
        
        # Verifique se já existe um registro com o mesmo user_id e productPlan
        cur.execute("SELECT id, quantity FROM Basket WHERE user_id = %s AND productPlan = %s", (user_id, productPlan))
        existing_basket_data = cur.fetchone()
        
        if existing_basket_data:
            # Se o registro já existe, aumente a quantidade em quantity
            existing_id, existing_quantity = existing_basket_data
            new_quantity = existing_quantity + quantity
            cur.execute("UPDATE Basket SET quantity = %s WHERE id = %s", (new_quantity, existing_id))
        else:
            # Se o registro não existe, insira um novo
            cur.execute("INSERT INTO Basket (user_id, productPlan, quantity) VALUES (%s, %s, %s)", (user_id, productPlan, quantity))
        
        conn.commit()
        # cur.close()
        
        return jsonify({"message": "Operação concluída com sucesso"}), 201
    except Exception as e:
        # Lida com erros e retorna uma resposta de erro apropriada
        conn.rollback()  # Desfaz quaisquer alterações no banco de dados
        return jsonify({"error": str(e)}), 500

@app.route("/baskets-machine", methods=["POST"])
def create_or_update_basket_machine():
    try:
        basket_data = request.get_json()
        user_id = basket_data.get("user_id")
        productMachine_ID = basket_data.get("productMachine_ID")
        quantity = basket_data.get("quantity")
        cur = conn.cursor()
        
        # Verifique se já existe um registro com o mesmo user_id e productMachine_ID
        cur.execute("SELECT id, quantity FROM Basket WHERE user_id = %s AND productMachine_ID = %s", (user_id, productMachine_ID))
        existing_basket_data = cur.fetchone()
        
        if existing_basket_data:
            # Se o registro já existe, aumente a quantidade em quantity
            existing_id, existing_quantity = existing_basket_data
            new_quantity = existing_quantity + quantity
            cur.execute("UPDATE Basket SET quantity = %s WHERE id = %s", (new_quantity, existing_id))
        else:
            # Se o registro não existe, insira um novo
            cur.execute("INSERT INTO Basket (user_id, productMachine_ID, quantity) VALUES (%s, %s, %s)", (user_id, productMachine_ID, quantity))
        
        conn.commit()
        # cur.close()
        
        return jsonify({"message": "Operação concluída com sucesso"}), 201
    except Exception as e:
        # Lida com erros e retorna uma resposta de erro apropriada
        conn.rollback()  # Desfaz quaisquer alterações no banco de dados
        return jsonify({"error": str(e)}), 500
    

# CRUD endpoints for BoughtProduct
@app.route("/boughtproducts", methods=["POST"])
def create_bought_product():
    product_data = request.get_json()
    user_id = product_data.get("user_id")
    basket_id = product_data.get("basket_ID")

    cur = conn.cursor()
    cur.execute(
        "INSERT INTO BoughtProduct (user_id, basket_ID) VALUES (%s, %s) RETURNING id",
        (user_id, basket_id),
    )
    bought_product_id = cur.fetchone()[0]
    conn.commit()
    cur.close()

    return jsonify({"id": bought_product_id}), 201

@app.route("/boughtproducts/<int:bought_product_id>", methods=["GET"])
def get_bought_product(bought_product_id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM BoughtProduct WHERE id = %s", (bought_product_id,))
    bought_product = cur.fetchone()
    cur.close()

    if bought_product:
        bought_product_dict = {
            "id": bought_product[0],
            "user_id": bought_product[1],
            "basket_ID": bought_product[2]
        }
        return jsonify(bought_product_dict), 200
    else:
        return "BoughtProduct not found", 404
    
if __name__ == "__main__":
    app.run(debug=True)