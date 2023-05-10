class Customer:
    def __init__(self, id, name, email, phone):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone

customers = []

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/customers', methods=['GET'])
def get_customers():
    return jsonify({'customers': [customer.__dict__ for customer in customers]})

@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    customer = Customer(data['id'], data['name'], data['email'], data['phone'])
    customers.append(customer)
    return jsonify({'customer': customer.__dict__})

@app.route('/customers/<id>', methods=['GET'])
def get_customer(id):
    customer = next((customer for customer in customers if customer.id == id), None)
    if customer:
        return jsonify({'customer': customer.__dict__})
    return jsonify({'message': 'Customer not found'})

@app.route('/customers/<id>', methods=['PUT'])
def update_customer(id):
    data = request.get_json()
    customer = next((customer for customer in customers if customer.id == id), None)
    if customer:
        customer.name = data['name']
        customer.email = data['email']
        customer.phone = data['phone']
        return jsonify({'customer': customer.__dict__})
    return jsonify({'message': 'Customer not found'})

@app.route('/customers/<id>', methods=['DELETE'])
def delete_customer(id):
    global customers
    customers = [customer for customer in customers if customer.id != id]
    return jsonify({'message': 'Customer deleted'})

class Product:
    def __init__(self, id, name, description, price, is_active):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.is_active = is_active

products = []

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({'products': [product.__dict__ for product in products]})

@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product = Product(data['id'], data['name'], data['description'], data['price'], data['is_active'])
    products.append(product)
    return jsonify({'product': product.__dict__})

@app.route('/products/<id>', methods=['GET'])
def get_product(id):
    product = next((product for product in products if product.id == id), None)
    if product:
        return jsonify({'product': product.__dict__})
    return jsonify({'message': 'Product not found'})

@app.route('/products/<id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    product = next((product for product in products if product.id == id), None)
    if product:
        product.name = data['name']
        product.description = data['description']
        product.price = data['price']
        product.is_active = data['is_active']
        return jsonify({'product': product.__dict__})
    return jsonify({'message': 'Product not found'})

@app.route('/products/<id>', methods=['DELETE'])
def delete_product(id):
    global products
    products = [product for product in products if product.id != id]
    return jsonify({'message': 'Product deleted'})

class Customer:
    def __init__(self, id, name, email, phone, products=[]):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.products = products

@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    product_ids = data.pop('product_ids', [])
    products = [product for product in products if product.id in product_ids]
    customer = Customer(data['id'], data['name'], data['email'], data['phone'], products)
    customers.append(customer)
    return jsonify({'customer': customer.__dict__})

from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)


products = [
    {"id": 1, "name": "Product A", "description": "This is a product description.", "price": 9.99, "is_active": True, "customer_id": 1, "registration_date": datetime.date(2022, 3, 15)},
    {"id": 2, "name": "Product B", "description": "This is another product description.", "price": 19.99, "is_active": True, "customer_id": 1, "registration_date": datetime.date(2022, 4, 1)},
    {"id": 3, "name": "Product C", "description": "This is a third product description.", "price": 29.99, "is_active": True, "customer_id": 2, "registration_date": datetime.date(2022, 5, 1)},
]


customers = [
    {"id": 1, "name": "Customer A", "email": "customer_a@example.com", "phone": "123-456-7890", "product_ids": [1, 2]},
    {"id": 2, "name": "Customer B", "email": "customer_b@example.com", "phone": "234-567-8901", "product_ids": [3]},
]

@app.route('/products/<int:product_id>/toggle_active', methods=['PUT'])
def toggle_product_active(product_id):
    # find the product by id
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({'error': 'Product not found'}), 404

    # check if the product was registered more than 2 months ago
    registration_date = product.get('registration_date')
    if registration_date and (datetime.date.today() - registration_date).days < 60:
        return jsonify({'error': 'Cannot make the product inactive yet'}), 400

    # toggle the is_active status of the product
    product['is_active'] = not product['is_active']

    # return the updated product
    return jsonify(product), 200

if __name__ == '__main__':
    app.run(debug=True)
