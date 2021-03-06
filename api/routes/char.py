from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import reqparse

from models.adventure import Adventure
from models.char import Char
from models.user import User
from services.utils import mount_chars


char_blueprint = Blueprint('char', __name__)

class CharParser:
    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True, type=str)
    parser.add_argument('adventure', required=True, type=str)
    parser.add_argument('attribute', required=True, type=int, choices=(2, 3, 4, 5))
    parser.add_argument('is_npc', type=bool)
    parser.add_argument('color', required=True, type=str)

@char_blueprint.route('/create', methods=['POST'])
@jwt_required()
def create_char():
    data = CharParser.parser.parse_args()
    print(data)
    adventure = Adventure.get_adventure(data['adventure'])
    user = User.get_user_by_id(get_jwt_identity())
    if Char.get_char(data['name'], adventure.name):
        return jsonify(message='Personagem já existente!'), 400
    if adventure:
        try:
            char = Char.create_char(data, user, adventure.name)
            return jsonify(name=char.name, attribute=char.attribute, user=char.user.username, adventure=char.adventure), 201
        except Exception as e:
            return jsonify(message=e), 500
    return jsonify(message='Aventura escolhida não existe!'), 400

@char_blueprint.route('', methods=['GET'])
def get_char():
    data = request.args
    adventure = Adventure.get_adventure(data['adventure'])
    print(adventure)
    char = Char.get_char(data['name'], adventure.name)
    if char:
        return jsonify(name=char.name, attribute=char.attribute)
    return jsonify(message='Não existe esse personagem!'), 404

@char_blueprint.route('/list', methods=['GET'])
@jwt_required()
def list_chars():
    user = User.get_user_by_id(get_jwt_identity())
    chars = Char.list_char_user(user)
    if not chars:
        return jsonify(message='Não existe personagens para esse usuário!'), 404
    return jsonify(chars=mount_chars(chars))
