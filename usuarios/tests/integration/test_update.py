from django.urls import reverse, resolve
from django.test import TestCase, Client
from django.contrib.auth.models import User
from usuarios.models import Usuario
import pytest

class TestUpdate:
    client = Client()
    url = reverse('update')

    def set_user(self):
        User.objects.create_user('janio', 'meuemail@email.com', 'minhasenha123')
        Usuario.objects.create(nome="janio Fernandes", user=User.objects.get(username='janio'))
        user_login = self.client.login(username="janio", password="minhasenha123")

    def set_i_user(self):
        User.objects.create_user('janio', 'meuemail@email.com', 'minhasenha123')
        user_login = self.client.login(username="janio", password="minhasenha123")

    @pytest.mark.django_db(transaction=True)
    def test_update_correct_call(self):
        self.set_user()
        response = self.client.get(self.url)
        assert response.status_code == 200

    @pytest.mark.django_db(transaction=True)
    def test_update_incorrect_call_no_usuario(self):
        self.set_i_user()
        response = self.client.get(self.url)
        assert response.status_code == 404

    @pytest.mark.django_db(transaction=True)
    def test_update_correct_page_content(self):
        self.set_user()
        response = self.client.get(self.url)
        content = "<h3>Update Usuario</h3>"
        assert content in str(response.content)

    @pytest.mark.django_db(transaction=True)
    def test_update_no_incorrect_page_content(self):
        self.set_user()
        response = self.client.get(self.url)
        content = "<h3>cid cidoso</h3>"
        assert content not in str(response.content)

    @pytest.mark.django_db(transaction=True)
    def test_update_correct_url(self):
        self.set_user()
        assert resolve(self.url).view_name == 'update'