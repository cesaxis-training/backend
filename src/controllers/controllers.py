from flask import Blueprint, request, jsonify
from models import models
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

# Criar um Blueprint para o controller de Citações
quote_bp = Blueprint('quote_bp', __name__)

# Rota para criar uma nova citação (POST)
@quote_bp.route('/quotes', methods=['POST'])
def create_quote():
    data = request.get_json()
    
    if not data or not data.get('text') or not data.get('author'):
        return jsonify({'message': 'Texto e autor são obrigatórios'}), 400

    text = data['text'].strip()
    author = data['author'].strip()

    if not text or not author:
        return jsonify({'message': 'Texto e autor não podem ser vazios'}), 400

    # Criar uma nova citação
    new_quote = models(text=text, author=author)
    
    try:
        models.db.session.add(new_quote)
        models.db.session.commit()
        return jsonify({'id': new_quote.id, 'text': new_quote.text, 'author': new_quote.author}), 201
    except IntegrityError as e:
        models.db.session.rollback()
        return jsonify({'message': 'Erro de integridade ao criar citação', 'error': str(e)}), 400
    except SQLAlchemyError as e:
        models.db.session.rollback()
        return jsonify({'message': 'Erro ao criar citação', 'error': str(e)}), 500


# Rota para listar todas as citações (GET)
@quote_bp.route('/quotes', methods=['GET'])
def get_all_quotes():
    quotes = models.Quotes.query.all()
    quotes_list = [{'id': q.id, 'text': q.text, 'author': q.author} for q in quotes]
    return jsonify(quotes_list)


# Rota para obter uma citação específica (GET)
@quote_bp.route('/quotes/<int:id>', methods=['GET'])
def get_quote(id):
    quote = models.Quotes.query.get(id)
    if quote:
        return jsonify({'id': quote.id, 'text': quote.text, 'author': quote.author})
    return jsonify({'message': 'Citação não encontrada'}), 404


# Rota para atualizar uma citação (PUT)
@quote_bp.route('/quotes/<int:id>', methods=['PUT'])
def update_quote(id):
    data = request.get_json()
    
    quote = models.Quotes.query.get(id)
    if not quote:
        return jsonify({'message': 'Citação não encontrada'}), 404

    if 'text' in data:
        quote.text = data['text'].strip()
    if 'author' in data:
        quote.author = data['author'].strip()
    
    try:
        models.db.session.commit()
        return jsonify({'id': quote.id, 'text': quote.text, 'author': quote.author})
    except IntegrityError as e:
        models.db.session.rollback()
        return jsonify({'message': 'Erro de integridade ao atualizar citação', 'error': str(e)}), 400
    except SQLAlchemyError as e:
        models.db.session.rollback()
        return jsonify({'message': 'Erro ao atualizar citação', 'error': str(e)}), 500


# Rota para deletar uma citação (DELETE)
@quote_bp.route('/quotes/<int:id>', methods=['DELETE'])
def delete_quote(id):
    quote = models.Quotes.query.get(id)
    if not quote:
        return jsonify({'message': 'Citação não encontrada'}), 404

    try:
        models.db.session.delete(quote)
        models.db.session.commit()
        return jsonify({'message': f'Citação com id {id} deletada com sucesso'})
    except SQLAlchemyError as e:
        models.db.session.rollback()
        return jsonify({'message': 'Erro ao deletar citação', 'error': str(e)}), 500