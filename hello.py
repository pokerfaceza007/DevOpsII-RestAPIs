from flask import Flask, request, jsonify, abort

app = Flask(__name__)

Cars = [
    {"name": "Tesla Model Y", "category": 1, "price": 2500000, "instock": 200},
    {"name": "Tesla Model 3", "category": 2, "price": 3000000, "instock": 250},
    {"name": "Porsche Taycan", "category": 3, "price": 6190000, "instock": 100},
    {"name": "porsche 911", "category": 4, "price": 10000000, "instock": 50},
    {"name": "BMW iX", "category": 5, "price": 5000000, "instock": 400},
]


def find_car_by_name(name):
    for car in Cars:
        if car["name"] == name:
            return car
    return None


@app.route("/Cars", methods=["GET"])
def get_cars():
    return jsonify(Cars)


@app.route("/Cars/<name>", methods=["GET"])
def get_car_by_name(name):
    car = find_car_by_name(name)
    if car is None:
        abort(404, description="Car not found")
    return jsonify(car)


@app.route("/Cars", methods=["POST"])
def add_car():
    name = request.form.get("name")
    category = request.form.get("category")
    price = request.form.get("price")
    instock = request.form.get("instock")

    if find_car_by_name(name):
        abort(400, description="Car already exists")

    new_car = {"name": name, "category": category, "price": price, "instock": instock}
    Cars.append(new_car)
    return jsonify(new_car)


@app.route("/Cars/<name>", methods=["PUT"])
def update_car(name):
    car = find_car_by_name(name)
    if car is None:
        abort(404, description="Car not found")

    car["category"] = request.form.get("category", car["category"])
    car["price"] = request.form.get("price", car["price"])
    car["instock"] = request.form.get("instock", car["instock"])

    return jsonify(car)


@app.route("/Cars/<name>", methods=["DELETE"])
def delete_car(name):
    car = find_car_by_name(name)
    if car is None:
        abort(404, description="Car not found")
    Cars.remove(car)
    return "Car deleted successfully", 200


if __name__ == "__main__":
    app.run(debug=True)
