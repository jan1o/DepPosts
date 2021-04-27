from django.test import Client, TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from usuarios.models import Usuario
from revistas.models import Revista
import pytest


class TestCaseRevista(TestCase):
    client = Client()
    url_cadastrar = '/revista/adicionar/'
    url = '/revista/editar/'

    def set_user(self):
        User.objects.create_user('janio', 'meuemail@email.com', 'minhasenha123')
        Usuario.objects.create(nome="janio Fernandes", user=User.objects.get(username='janio'))
        user_login = self.client.login(username="janio", password="minhasenha123")

    @pytest.mark.django_db(transaction=True)
    def test_edit_revista(self):
        self.set_user()
        response = self.client.post(self.url_cadastrar,{
            'nome': 'revista1',
        })
        revista = Revista.objects.get(nome='revista1')
        response = self.client.get(self.url + str(revista.id) + '/')
        assert response.status_code == 200

    @pytest.mark.django_db(transaction=True)
    def test_edit_revista_correct_url(self):
        self.set_user()
        response = self.client.post(self.url_cadastrar,{
            'nome': 'revista1',
        })
        revista = Revista.objects.get(nome='revista1')
        assert resolve(self.url + str(revista.id) + '/').view_name == 'editarRevista'

    @pytest.mark.django_db(transaction=True)
    def test_edit_revista_incorrect_url(self):
        self.set_user()
        response = self.client.get(self.url + str(999999) + '/')
        assert response.status_code == 404

    @pytest.mark.django_db(transaction=True)
    def test_edit_correct_revista_for_id(self):
        self.set_user()
        response = self.client.post(self.url_cadastrar,{
            'nome': 'revista1',
        })
        revista = Revista.objects.get(nome='revista1')
        response = self.client.post(self.url + str(revista.id) + '/',{
            'nome': 'revista2',
        })
        revista = Revista.objects.get(nome='revista2')
        assert revista != False