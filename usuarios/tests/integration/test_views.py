from django.urls import reverse, resolve
from django.test import TestCase, Client
from django.contrib.auth.models import User
import pytest

from usuarios.views import *
from usuarios.models import *


class TestViews:
    client = Client()

    @pytest.mark.django_db(transaction=True)
    def test_UsuarioCreate_username_correct(self):
        url = reverse('signin')
        response = self.client.post(url, {
            'username': 'usuario1',
            'password1': 'minhasenha123',
            'password2': 'minhasenha123'
        })

        user = User.objects.get(username='usuario1')
        assert user.username == 'usuario1'

    @pytest.mark.django_db(transaction=True)
    def test_UsuarioCreate_id_correct(self):
        url = reverse('signin')
        response = self.client.post(url, {
            'username': 'usuario1',
            'password1': 'minhasenha123',
            'password2': 'minhasenha123'
        })

        user = User.objects.get(username='usuario1')
        assert user.id == 2



