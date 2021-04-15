from django.urls import reverse, resolve
from django.test import TestCase, Client
from django.contrib.auth.models import User
import pytest


class TestSignIn:
    client = Client()
    url = reverse('signin')

    def test_signin_call(self):
        response = self.client.get(self.url)
        assert response.status_code == 200


    def test_signin_correct_page_content(self):
        response = self.client.get(self.url)
        content = "<h3>Sign In</h3>"
        assert content in str(response.content)

    def test_signin_no_incorrect_page_content(self):
        response = self.client.get(self.url)
        content = "<h3>cid cidoso</h3>"
        assert content not in str(response.content)

    def test_signin_correct_url(self):
        assert resolve(self.url).view_name == 'signin'

    @pytest.mark.django_db(transaction=True)
    def test_signin_correct_user_create(self):
        response = self.client.post(self.url,{
            'username': 'usuario1',
            'password1': 'minhasenha123',
            'password2': 'minhasenha123'
        })
        user = User.objects.get(username='usuario1')
        assert user != None
