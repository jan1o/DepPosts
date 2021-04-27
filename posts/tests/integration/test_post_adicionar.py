from django.test import Client, TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User

import posts
from usuarios.models import Usuario
from revistas.models import Revista
from posts.models import Post
import pytest

class TestCasePost(TestCase):
    client = Client()
    url = '/posts/new/'

    #anotação para acessar o bd
    @pytest.mark.django_db(transaction=True)
    def test_add_post(self):
        User.objects.create_user('bruno', 'bruno@email.com', 'minhasenha123')
        Usuario.objects.create(nome="Bruno Silva", user=User.objects.get(username='bruno'))
        user_login = self.client.login(username="bruno", password="minhasenha123")
        response = self.client.get(self.url)
        assert response.status_code == 200

    @pytest.mark.django_db(transaction=True)
    def test_add_update_post_correct_page_content(self):
        User.objects.create_user('bruno', 'bruno@email.com', 'minhasenha123')
        Usuario.objects.create(nome="Bruno Silva", user=User.objects.get(username='bruno'))
        user_login = self.client.login(username="bruno", password="minhasenha123")
        response = self.client.get(self.url)
        content = "<h1>Novo/Atualizar Post</h1>"
        assert content in str(response.content)

    @pytest.mark.django_db(transaction=True)
    def test_add_post_correct_url(self):
        User.objects.create_user('bruno', 'bruno@email.com', 'minhasenha123')
        Usuario.objects.create(nome="Bruno Silva", user=User.objects.get(username='bruno'))
        user_login = self.client.login(username="bruno", password="minhasenha123")
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