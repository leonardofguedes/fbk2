from flask_restful import Resource
from flask import request
from utils.auth import access_fake_user

class User(Resource):
    def get(self):
        # Obtém o token do cabeçalho Authorization
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return {"msg": "Token não fornecido ou inválido"}, 401

        # Extrai o token do cabeçalho
        fake_token = auth_header.split(" ")[1]

        # Acessa os dados protegidos de /fake/user
        user_data = access_fake_user(fake_token)
        if "error" in user_data:
            return {"msg": "Falha ao acessar /fake/user", "details": user_data}, 401

        # Retorna os dados do usuário obtidos do serviço FAKE
        return {"fake_user_data": user_data}, 200
