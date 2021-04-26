from django.test import Client, TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from usuarios.models import Usuario
from revistas.models import Revista
import pytest


class TestCaseRevista(TestCase):
    client = Client()
    url_cadastrar = '/revista/adicionar/'
    url = '/revista/excluir/'

    @pytest.mark.django_db(transaction=True)
    def test_remove_revista(self):
        User.objects.create_user('janio', 'meuemail@email.com', 'minhasenha123')
        Usuario.objects.create(nome="janio Fernandes", user=User.objects.get(username='janio'))
        user_login = self.client.login(username="janio", password="minhasenha123")
        response = self.client.post(self.url_cadastrar,{
            'nome': 'revista1',
        })
        revista = Revista.objects.get(nome='revista1')
        response = self.client.get(self.url + str(revista.id) + '/')
        assert response.status_code == 200

    @pytest.mark.django_db(transaction=True)
    def test_remove_revista_correct_url(self):
        User.objects.create_user('janio', 'meuemail@email.com', 'minhasenha123')
        Usuario.objects.create(nome="janio Fernandes", user=User.objects.get(username='janio'))
        user_login = self.client.login(username="janio", password="minhasenha123")
        response = self.client.post(self.url_cadastrar,{
            'nome': 'revista1',
        })
        revista = Revista.objects.get(nome='revista1')
        assert resolve(self.url + str(revista.id) + '/').view_name == 'excluirRevista'

    @pytest.mark.django_db(transaction=True)
    def test_remove_correct_revista_for_id(self):
        User.objects.create_user('janio', 'meuemail@email.com', 'minhasenha123')
        Usuario.objects.create(nome="janio Fernandes", user=User.objects.get(username='janio'))
        user_login = self.client.login(username="janio", password="minhasenha123")
        response = self.client.post(self.url_cadastrar,{
            'nome': 'revista1',
        })
        revista = Revista.objects.get(nome='revista1')
        response = self.client.post(self.url + str(revista.id) + '/',{
        })
        revistas = Revista.objects.all()
        assert revistas.exists() == False