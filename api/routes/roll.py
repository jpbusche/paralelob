from types import MethodDescriptorType
from flask import Blueprint, jsonify, request
from flask_restful import reqparse
from flask_jwt_extended import jwt_required
from random import randint

from models.roll import Result, Roll


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

def roll_dices(_type, _qtd, _attribute):
    results = []
    for i in range(0, _qtd):
        result = randint(1, 6)
        results.append(Result.create_result(result, get_success(result, _type, _attribute)))
    return results

def get_success(_result, _type, _attribute):
    if _type == 'fisico':
        return 'critico' if _result == _attribute else 'sucesso' if _result < _attribute else 'falha'
    elif _type == 'mental':
        return 'critico' if _result == _attribute else 'sucesso' if _result > _attribute else 'falha'

def mount_rolls(_results):
    results = []
    for result in _results:
        results.append({'name': result.char_name, 'results': [res.to_mongo().to_dict() for res in result.results]})
    return results
