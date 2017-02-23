from test.base_test import BaseTest

signup_url = "/auth/register"
login_url = "/auth/login"


class AuthenticationTestCase(BaseTest):

    def test_login(self):
        payload = {"email": "an@asas.co", "password": "password123A"}
        response = self.app.post(login_url, data=payload)
        assert "access_token" in response.data.decode()
        assert response.status, 200

    def test_invalid_credentials_login(self):
        payload = {"email": "an@asas.co", "password": "wrong_password"}
        response = self.app.post(login_url, data=payload)
        assert "error" in response.data.decode()
        assert response.status, 200

    def test_signup_email_validation(self):
        name = "ian"
        email = "an@asas.co"
        payload = {"name": name, "email": email, "password": "password123A"}
        response = self.app.post(signup_url, data=payload)
        assert "error" in response.data.decode()

    def test_signup_unique_email_validation(self):
        name = "ian"
        email = "anasas.co"
        payload = {"name": name, "email": email, "password": "password123A"}
        response = self.app.post(signup_url, data=payload)
        assert "error" in response.data.decode()

    def test_signup_password_validation(self):
        name = "ian"
        email = "atest@email.com"
        payload = {"name": name, "email": email, "password": "short"}
        response = self.app.post(signup_url, data=payload)
        assert "error" in response.data.decode()
