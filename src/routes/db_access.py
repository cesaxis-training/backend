from flask import Blueprint, jsonify, request
import mysql.connector
import os
from models import models

# Create the Blueprint object
db_test_blueprint = Blueprint("db_test", __name__)


# Define the routes inside the blueprint
@db_test_blueprint.route("/hello-world", methods=["GET"])
def hello_world():
    return "Hello, World!", 200


@db_test_blueprint.route("/db-test", methods=["GET"])
def db_test():
    try:
        conn = mysql.connector.connect(
            host=os.environ.get("MYSQL_HOST"),
            user=os.environ.get("MYSQL_USER"),
            password=os.environ.get("MYSQL_PASSWORD"),
            database=os.environ.get("MYSQL_DATABASE"),
            port=3308,
        )
        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE()")
        result = cursor.fetchone()
        conn.close()
        return f"Connected to database: {result[0]}", 200
    except mysql.connector.Error as err:
        return f"Error: {err}", 500


# Rota para listar todas as citações (GET)
@db_test_blueprint.route("/quotes", methods=["GET"])
def get_all_quotes():
    try:
        # Obtém todas as citações do banco de dados
        quotes = models.Quotes.query.all()
        # Converte as citações para um formato de lista de dicionários
        quotes_list = [{"id": q.id, "text": q.text, "author": q.author} for q in quotes]
        return jsonify(quotes_list), 200
    except Exception as e:
        return jsonify({"message": "Erro ao listar citações", "error": str(e)}), 500


# Rota para criar uma nova citação (POST)
@db_test_blueprint.route("/quotes/create", methods=["POST"])
def create_quote():
    data = request.get_json()

    # Verifica se o corpo da requisição contém os campos necessários
    if not data or not data.get("text") or not data.get("author"):
        return jsonify({"message": "Texto e autor são obrigatórios"}), 400

    # Cria uma nova citação a partir dos dados fornecidos
    new_quote = models.Quotes(text=data["text"], author=data["author"])

    try:
        # Adiciona a nova citação à sessão do banco de dados e faz o commit
        models.db.session.add(new_quote)
        models.db.session.commit()
        # Retorna a citação criada com status 201 (Criado)
        return (
            jsonify(
                {"id": new_quote.id, "text": new_quote.text, "author": new_quote.author}
            ),
            201,
        )
    except Exception as e:
        models.db.session.rollback()
        return jsonify({"message": "Erro ao criar citação", "error": str(e)}), 500


# Rota para atualizar uma citação existente (PUT)
@db_test_blueprint.route("/quotes/update/<int:id>", methods=["PUT"])
def update_quote(id):
    data = request.get_json()

    # Busca a citação no banco de dados com o ID fornecido
    quote = models.Quotes.query.get(id)
    if not quote:
        return jsonify({"message": "Citação não encontrada"}), 404

    # Atualiza os campos da citação com os dados fornecidos
    if "text" in data:
        quote.text = data["text"]
    if "author" in data:
        quote.author = data["author"]

    try:
        # Commit das alterações no banco de dados
        models.db.session.commit()
        return (
            jsonify({"id": quote.id, "text": quote.text, "author": quote.author}),
            200,
        )
    except Exception as e:
        models.db.session.rollback()
        return jsonify({"message": "Erro ao atualizar citação", "error": str(e)}), 500


# Rota para deletar uma citação (DELETE)
@db_test_blueprint.route("/quotes/delete/<int:id>", methods=["DELETE"])
def delete_quote(id):
    # Busca a citação no banco de dados com o ID fornecido
    quote = models.Quotes.query.get(id)
    if not quote:
        return jsonify({"message": "Citação não encontrada"}), 404

    try:
        # Deleta a citação do banco de dados
        models.db.session.delete(quote)
        models.db.session.commit()
        return jsonify({"message": f"Citação com id {id} deletada com sucesso"}), 200
    except Exception as e:
        models.db.session.rollback()
        return jsonify({"message": "Erro ao deletar citação", "error": str(e)}), 500
