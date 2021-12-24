from flask import Blueprint, jsonify, request
from flask_restful import reqparse
from flask_jwt_extended import jwt_required

from models.roll import Roll
from services.utils import roll_dices, mount_rolls


roll_blueprint = Blueprint('roll', __name__)

class RollParser:
    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True, type=str)
    parser.add_argument('type', required=True, type=str, choices=('mental', 'fisico'))
    parser.add_argument('adventure', required=True, type=str)
    parser.add_argument('attribute', required=True, type=int, choices=(2, 3, 4, 5))
    parser.add_argument('qtd', default=2, type=int)

@roll_blueprint.route('', methods=['POST'])
@jwt_required()
def roll_dice():
    data = RollParser.parser.parse_args()
    results = roll_dices(data['type'], data['qtd'], data['attribute'])
    try:
        roll = Roll.create_roll(results, data['adventure'], data['name'])
        return jsonify(results=[result.to_mongo().to_dict() for result in results])
    except Exception as e:
        return jsonify(message=e), 500

@roll_blueprint.route('/list', methods=['GET'])
def list_rolls_by_adventure():
    data = request.args
    results = Roll.list_rolls_adventure(data['adventure'])
    if results:
        return jsonify(results=mount_rolls(results))
    return jsonify(message='Sem rolagens para essa aventura'), 404
