from django.test import Client, TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

import posts
from revistas.models import Revista
from posts.models import Post
from usuarios.models import Usuario
import pytest

class TestCasePost(TestCase):
    client = Client()
    url = '/posts/new/'

    def set_user(self):
        User.objects.create_user('bruno', 'bruno@email.com', 'senha')
        Usuario.objects.create(nome="Bruno Silva", user=User.objects.get(username='bruno'))
        user_login = self.client.login(username="bruno", password="senha")

    @pytest.mark.django_db(transaction=True)
    def test_add_post(self):
        self.set_user()
        response = self.client.get(self.url)
        assert response.status_code == 200

    @pytest.mark.django_db(transaction=True)
    def test_add_update_post_correct_page_content(self):
        self.set_user()
        response = self.client.get(self.url)
        content = "<h1>Novo/Atualizar Post</h1>"
        assert content in str(response.content)

    @pytest.mark.django_db(transaction=True)
    def test_add_post_correct_url(self):
        self.set_user()
        assert resolve(self.url).view_name == 'create_post'

    '''
    @pytest.mark.django_db(transaction=True)
    def test_add_correct_post(self):
        User.objects.create_user('bruno', 'bruno@email.com', 'minhasenha123')
        Usuario.objects.create(nome="Bruno Silva", user=User.objects.get(username='bruno'))
        user_login = self.client.login(username="bruno", password="minhasenha123")

        Revista.objects.create(nome="RevistaTeste")
        posts.models.Post.objects.create(titulo="a", corpo='a', revistaAssociada=Revista.objects.get(nome='RevistaTeste'))

        print(Revista.objects.get(nome='RevistaTeste'))
        print(posts.models.Post.objects.get(titulo='a'))

        response = self.client.post(self.url, {
            'titulo': 'Titulo do Post',
            'corpo': 'Regna terrae, cantate deo, Tribuite virtutem deo.',
            'RevistaAssociada': Revista.objects.get(nome='RevistaTeste')
        })
        post = posts.models.Post.objects.get(titulo='Titulo do Post')
        print(post)
        assert post != None
    '''