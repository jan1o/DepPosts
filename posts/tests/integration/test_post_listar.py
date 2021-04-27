from django.test import Client, TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from usuarios.models import Usuario
import pytest

class TestCasePost(TestCase):
    client = Client()
    url = '/posts/'

    def set_user(self):
        User.objects.create_user('bruno', 'bruno@email.com', 'senha')
        Usuario.objects.create(nome="Bruno Silva", user=User.objects.get(username='bruno'))
        user_login = self.client.login(username="bruno", password="senha")

    @pytest.mark.django_db(transaction=True)
    def test_list_post(self):
        self.set_user()
        response = self.client.get(self.url)
        assert response.status_code == 200

    @pytest.mark.django_db(transaction=True)
    def test_list_post_correct_page_content(self):
        self.set_user()
        response = self.client.get(self.url)
        content = "<h1>Lista de Posts</h1>"
        assert content in str(response.content)

    @pytest.mark.django_db(transaction=True)
    def test_list_post_correct_url(self):
        self.set_user()
        assert resolve(self.url).view_name == 'list_posts'