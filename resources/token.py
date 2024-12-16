from flask import request
from flask_restful import Resource
from utils.auth import get_fake_token

class Token(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        # Obter token do serviço FAKE
        fake_token = get_fake_token(username, password)
        if not fake_token:
            return {"msg": "Falha ao autenticar no serviço FAKE"}, 401

        # Retorna o token do serviço FAKE e o token JWT local
        return {"fake_token": fake_token}, 200
