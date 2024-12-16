from flask_restful import Resource
from flask import request
from utils.auth import access_fake_admin
from utils.auth import get_fake_health

class Admin(Resource):
    def get(self):
        # Obtém o token do cabeçalho Authorization
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return {"msg": "Token não fornecido ou inválido"}, 401

        # Extrai o token do cabeçalho
        fake_token = auth_header.split(" ")[1]

        # Acessa os dados protegidos de /fake/admin
        admin_data = access_fake_admin(fake_token)
        if "error" in admin_data:
            return {"msg": "Falha ao acessar /fake/admin", "details": admin_data}, 401

        # Retorna os dados do administrador obtidos do serviço FAKE
        return {"fake_admin_data": admin_data}, 200


class HealthCheck(Resource):
    def get(self):
        return get_fake_health()