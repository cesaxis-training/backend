from flask import Blueprint, request
import controllers
import logging

# Create a logger for this module
logger = logging.getLogger(__name__)

# Create a Blueprint for the quote routes
quote_bp = Blueprint("quote_bp", __name__)

# Route to create a new quote (POST)
@quote_bp.route("/quotes", methods=["POST"])
def create_quote():
    logger.info("POST /quotes called")
    return controllers.create_quote(request.get_json())

# Route to list all quotes (GET)
@quote_bp.route("/quotes", methods=["GET"])
def get_all_quotes():
    logger.info("GET /quotes called")
    return controllers.get_all_quotes()

# Route to get a specific quote (GET)
@quote_bp.route("/quotes/<int:id>", methods=["GET"])
def get_quote(id):
    logger.info(f"GET /quotes/{id} called")
    return controllers.get_quote(id)

# Route to update a quote (PUT)
@quote_bp.route("/quotes/<int:id>", methods=["PUT"])
def update_quote(id):
    logger.info(f"PUT /quotes/{id} called")
    return controllers.update_quote(id, request.get_json())

# Route to delete a quote (DELETE)
@quote_bp.route("/quotes/<int:id>", methods=["DELETE"])
def delete_quote(id):
    logger.info(f"DELETE /quotes/{id} called")
    return controllers.delete_quote(id)
