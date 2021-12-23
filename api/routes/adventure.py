from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from flask_restful import reqparse

from models.adventure import Adventure


adventure_blueprint = Blueprint('adventure', __name__)

class AdventureParser:
    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True, type=str)

@adventure_blueprint.route('/list', methods=['GET'])
@jwt_required()
def list_adventures():
    adventures = Adventure.list_adventures()
    if not adventures:
        return jsonify(message='Nenhum aventura encontrada!'), 404
    return jsonify(adventures=[adventure.name for adventure in adventures])

@adventure_blueprint.route('/create', methods=['POST'])
@jwt_required()
def create_adventure():
    data = AdventureParser.parser.parse_args()
    if Adventure.get_adventure(data['name']):
        return jsonify(message='Aventura já existente!'), 400
    try:
        adventure = Adventure.create_adventure(data['name'])
        return jsonify(name=adventure.name)
    except Exception as e:
        return jsonify(message=e), 500
