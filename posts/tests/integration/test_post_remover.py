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
    url_cadastrar = '/posts/new/'
    url_delete = '/posts/delete/'

    def set_user(self):
        User.objects.create_user('bruno', 'bruno@email.com', 'senha')
        Usuario.objects.create(nome="Bruno Silva", user=User.objects.get(username='bruno'))
        self.client.login(username="bruno", password="senha")

    @pytest.mark.django_db(transaction=True)
    def test_remove_post(self):
        self.set_user()
        Revista.objects.create(nome="RevistaTeste")
        posts.models.Post.objects.create(
            titulo="TituloTal",
            corpo='CorpoTal',
            revistaAssociada=Revista.objects.get(nome='RevistaTeste'))

        post = Post.objects.get(titulo='TituloTal')
        response = self.client.get(self.url_delete + str(post.id) + '/')
        assert response.status_code == 200

    @pytest.mark.django_db(transaction=True)
    def test_remove_post_correct_url(self):
        self.set_user()

        Revista.objects.create(nome="RevistaTeste")
        posts.models.Post.objects.create(
            titulo="TituloTal",
            corpo='CorpoTal',
            revistaAssociada=Revista.objects.get(nome='RevistaTeste'))

        post = Post.objects.get(titulo='TituloTal')
        assert resolve(self.url_delete + str(post.id) + '/').view_name == 'delete_post'

    def test_remove_correct_post_for_id(self):
        self.set_user()
        Revista.objects.create(nome="RevistaTeste")
        posts.models.Post.objects.create(
            titulo="TituloTal",
            corpo='CorpoTal',
            revistaAssociada=Revista.objects.get(nome='RevistaTeste'))

        postagem = Post.objects.get(titulo="TituloTal")
        self.client.post(self.url_delete + str(postagem.id) + '/',{
        })
        postagens = Post.objects.all()
        assert postagens.exists() == False