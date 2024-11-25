from flask import Blueprint, jsonify

example_blueprint = Blueprint("example", __name__)

@example_blueprint.route("/hello-world", methods=["GET"])
def hello_world():
    return jsonify({"message": "Hello, World!"}), 200
