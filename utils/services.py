import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do .env
load_dotenv()

FAKE_BASE_URL = os.getenv("FAKE_BASE_URL")
if not FAKE_BASE_URL:
    raise ValueError("FAKE_BASE_URL não configurado. Verifique o arquivo env.example para que passe a ser .env")

class FakeService:
    @staticmethod
    def get(endpoint, token=None):
        """
        Executa uma requisição GET para o serviço FAKE.
        """
        url = f"{FAKE_BASE_URL}/{endpoint}"
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        try:
            response = requests.get(url, headers=headers, verify=False)  # Ignora SSL
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"Erro na requisição GET para {endpoint}: {str(e)}"}

    @staticmethod
    def post(endpoint, params=None):
        """
        Executa uma requisição POST para o serviço FAKE.
        """
        url = f"{FAKE_BASE_URL}/{endpoint}"
        try:
            response = requests.post(url, params=params, verify=False)  # Ignora SSL
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"Erro na requisição POST para {endpoint}: {str(e)}"}
    
    @staticmethod
    def health_check():
        """
        Verifica o estado de saúde do serviço FAKE.
        """
        url = f"{FAKE_BASE_URL}/health"
        try:
            response = requests.get(url, verify=False)  # Ignora SSL
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"Erro ao verificar o estado de saúde: {str(e)}"}
