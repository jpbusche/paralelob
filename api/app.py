from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from settings import SECRET_KEY, EXPIRATION_TIME
from services.mongo_database import start_mongo
from routes.user import user_blueprint
from routes.adventure import adventure_blueprint


def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = SECRET_KEY
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = EXPIRATION_TIME
    app.register_blueprint(user_blueprint)
    app.register_blueprint(adventure_blueprint, url_prefix='/adventure')
    CORS(app)
    JWTManager(app)
    app.run(port=5000)

if __name__ == '__main__':
    start_mongo()
    create_app()