from django.urls import reverse, resolve
from django.test import TestCase, Client
import pytest

class TestLogin:
    client = Client()
    url = reverse('login')


    def test_login_call(self):
        response = self.client.get(self.url)
        assert response.status_code == 200


    def test_login_correct_page_content(self):
        response = self.client.get(self.url)
        content = "<h3>Login</h3>"
        assert content in str(response.content)

    def test_login_no_incorrect_page_content(self):
        response = self.client.get(self.url)
        content = "<h3>cid cidoso</h3>"
        assert content not in str(response.content)

    def test_login_correct_url(self):
        assert resolve(self.url).view_name == 'login'




