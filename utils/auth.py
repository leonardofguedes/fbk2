from utils.services import FakeService

def get_fake_token(username, password):
    """
    Obtém um token JWT do serviço FAKE usando query parameters.
    """
    params = {"username": username, "password": password}
    result = FakeService.post("token", params=params)
    if "access_token" in result:
        return result["access_token"]
    return {"error": result.get("error", "Falha ao obter token")}

def access_fake_user(token):
    """
    Acessa a rota protegida de usuário no serviço FAKE.
    """
    result = FakeService.get("user", token=token)
    if "error" in result:
        return {"error": f"Erro ao acessar /fake/user: {result['error']}"}
    return result

def access_fake_admin(token):
    """
    Acessa a rota protegida de administrador no serviço FAKE.
    """
    result = FakeService.get("admin", token=token)
    if "error" in result:
        return {"error": f"Erro ao acessar /fake/admin: {result['error']}"}
    return result

def get_fake_health():
    """
    Verifica o estado de saúde do serviço FAKE.
    """
    return FakeService.health_check()
