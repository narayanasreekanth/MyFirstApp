from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

# Dummy data
products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 499.99},
    {"id": 3, "name": "Headphones", "price": 199.99}
]

cart = []

@app.route('/')
def home():
    return render_template('index_1.html', products=products, cart=cart)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        cart.append(product)
    return render_template('index_1.html', products=products, cart=cart)

if __name__ == '__main__':
    app.run(host="0.0.0.0" , port=5000 ,debug=True)
