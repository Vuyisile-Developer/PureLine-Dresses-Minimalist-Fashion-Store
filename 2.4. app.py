from flask import Flask, jsonify, request
from flask_cors import CORS
from database import Base, engine, SessionLocal
from models import Product

app = Flask(__name__)
CORS(app)

Base.metadata.create_all(bind=engine)

@app.route("/products", methods=["GET"])
def get_products():

    db = SessionLocal()
    products = db.query(Product).all()

    result = []

    for p in products:
        result.append({
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "description": p.description,
            "image": p.image
        })

    return jsonify(result)

@app.route("/products", methods=["POST"])
def add_product():

    data = request.json

    db = SessionLocal()

    product = Product(
        name=data["name"],
        price=data["price"],
        description=data["description"],
        image=data["image"]
    )

    db.add(product)
    db.commit()

    return {"message": "Product added"}

if __name__ == "__main__":
    app.run(debug=True)