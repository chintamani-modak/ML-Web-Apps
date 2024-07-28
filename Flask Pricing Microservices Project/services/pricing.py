import requests
import pandas as pd
from flask import Flask, jsonify, request
from sklearn.linear_model import LinearRegression
import pickle
import os

app = Flask(__name__)

model = None
products = []  # List to store product data

@app.route("/")
def home():
    return "Hello, this is a Flask Pricing Microservice with ML"

@app.route('/external-products', methods=['GET'])
def get_external_products():
    response = requests.get('https://dummyjson.com/products')
    if response.status_code == 200:
        items = response.json()['products']
        return jsonify({'products': items}), 200
    return jsonify({'error': 'Failed to fetch data from external API'}), response.status_code

@app.route('/train-model', methods=['POST'])
def train_model():
    global model
    data = request.json
    df = pd.DataFrame(data)
    X = df[['discountPercentage', 'rating', 'stock']]  # Replace with actual feature names
    y = df['price']
    model = LinearRegression()
    model.fit(X, y)
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)
    return jsonify({'message': 'Model trained successfully'}), 200

@app.route('/predict', methods=['POST'])
def predict():
    global model
    if model is None:
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
    data = request.json
    df = pd.DataFrame([data])
    X = df[['discountPercentage', 'rating', 'stock']]  # Replace with actual feature names
    prediction = model.predict(X)[0]
    return jsonify({'predicted_price': prediction}), 200

@app.route('/products', methods=['POST'])
def create_product():
    product = request.json
    product['id'] = len(products) + 1
    products.append(product)
    return jsonify(product), 201

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({'products': products}), 200

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((product for product in products if product['id'] == product_id), None)
    if product:
        return jsonify(product), 200
    return jsonify({'error': 'Product not found'}), 404

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = next((product for product in products if product['id'] == product_id), None)
    if product:
        updated_data = request.json
        product.update(updated_data)
        return jsonify(product), 200
    return jsonify({'error': 'Product not found'}), 404

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [product for product in products if product['id'] != product_id]
    return jsonify({'message': 'Product deleted'}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)