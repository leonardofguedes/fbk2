import unittest
from unittest.mock import patch
from utils.auth import get_fake_health, get_fake_token, access_fake_user, access_fake_admin

class TestFakeService(unittest.TestCase):
    @patch("utils.services.FakeService.health_check")
    def test_health_status(self, mock_health_check):
        """Testa a verificação do status do serviço FAKE."""
        mock_health_check.return_value = {"status": "healthy"}
        health_status = get_fake_health()
        self.assertIn("status", health_status)
        self.assertEqual(health_status["status"], "healthy")

    @patch("utils.services.FakeService.post")
    def test_fake_token(self, mock_post):
        """Testa a obtenção de token do serviço FAKE."""
        mock_post.return_value = {"access_token": "fake_token"}
        token = get_fake_token("user", "fake-password")
        self.assertIsInstance(token, str)

    @patch("utils.services.FakeService.get")
    def test_fake_user_access(self, mock_get):
        """Testa o acesso à rota protegida de usuário no serviço FAKE."""
        mock_get.return_value = {"user_data": "dados_do_usuario"}
        token = "fake_token"
        user_data = access_fake_user(token)
        self.assertIn("user_data", user_data)

    @patch("utils.services.FakeService.get")
    def test_fake_admin_access(self, mock_get):
        """Testa o acesso à rota protegida de administrador no serviço FAKE."""
        mock_get.return_value = {"admin_data": "dados_do_admin"}
        token = "fake_token"
        admin_data = access_fake_admin(token)
        self.assertIn("admin_data", admin_data)

if __name__ == "__main__":
    unittest.main()
