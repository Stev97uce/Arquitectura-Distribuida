from flask import Flask, render_template
import requests

app = Flask(__name__)

API_GATEWAY_URL = "http://api_gateway:8000"  # Nombre del servicio en Docker

@app.route("/")
def home():
    # Obtener productos y órdenes desde el API Gateway
    products = requests.get(f"{API_GATEWAY_URL}/products").json()
    orders = requests.get(f"{API_GATEWAY_URL}/orders").json()
    return render_template("index.html", products=products, orders=orders)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)