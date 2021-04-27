from django.test import Client, TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from usuarios.models import Usuario
from revistas.models import Revista
import pytest

class TestCaseRevista(TestCase):
    client = Client()
    url = '/revista/adicionar/'

    def set_user(self):
        User.objects.create_user('janio', 'meuemail@email.com', 'minhasenha123')
        Usuario.objects.create(nome="janio Fernandes", user=User.objects.get(username='janio'))
        user_login = self.client.login(username="janio", password="minhasenha123")

    @pytest.mark.django_db(transaction=True)
    def test_add_revista(self):
        self.set_user()
        response = self.client.get(self.url)
        assert response.status_code == 200

    @pytest.mark.django_db(transaction=True)
    def test_add_revista_correct_page_content(self):
        self.set_user()
        response = self.client.get(self.url)
        content = "<h1>Adicionar Revista</h1>"
        assert content in str(response.content)

    @pytest.mark.django_db(transaction=True)
    def test_add_revista_no_incorrect_page_content(self):
        self.set_user()
        response = self.client.get(self.url)
        content = "<h1>cid cidoso</h1>"
        assert content not in str(response.content)

    @pytest.mark.django_db(transaction=True)
    def test_add_revista_correct_url(self):
        self.set_user()
        assert resolve(self.url).view_name == 'adicionarRevista'

    @pytest.mark.django_db(transaction=True)
    def test_add_correct_revista(self):
        self.set_user()
        response = self.client.post(self.url,{
            'nome': 'revista1',
        })
        revista = Revista.objects.get(nome='revista1')
        assert revista != None