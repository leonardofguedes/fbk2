from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.token import Token
from resources.user import User
from resources.admin import Admin, HealthCheck

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "your-secret-key"

api = Api(app)
jwt = JWTManager(app)

# Rotas
api.add_resource(Token, "/token")
api.add_resource(User, "/user")
api.add_resource(Admin, "/admin")
api.add_resource(HealthCheck, "/health")

if __name__ == "__main__":
    app.run(debug=True)
