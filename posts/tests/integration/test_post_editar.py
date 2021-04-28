from django.test import Client, TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from usuarios.models import Usuario
from revistas.models import Revista
from posts.models import Post
import posts
import pytest


class TestCaseRevista(TestCase):
    client = Client()
    url_cadastrar = '/posts/new/'
    url = '/posts/update/'

    def set_user(self):
        User.objects.create_user('janio', 'meuemail@email.com', 'minhasenha123')
        Usuario.objects.create(nome="janio Fernandes", user=User.objects.get(username='janio'))
        self.client.login(username="janio", password="minhasenha123")

    @pytest.mark.django_db(transaction=True)
    def test_edit_post(self):
        self.set_user()
        Revista.objects.create(nome="RevistaTeste")
        posts.models.Post.objects.create(
            titulo="TituloTal",
            corpo='CorpoTal',
            revistaAssociada=Revista.objects.get(nome='RevistaTeste'))

        post = Post.objects.get(titulo='TituloTal')
        response = self.client.get(self.url + str(post.id) + '/')
        assert response.status_code == 200

    @pytest.mark.django_db(transaction=True)
    def test_edit_post_correct_url(self):
        self.set_user()
        Revista.objects.create(nome="RevistaTeste")
        posts.models.Post.objects.create(
            titulo="TituloTal",
            corpo='CorpoTal',
            revistaAssociada=Revista.objects.get(nome='RevistaTeste'))

        post = Post.objects.get(titulo='TituloTal')
        assert resolve(self.url + str(post.id) + '/').view_name == 'update_post'

    @pytest.mark.django_db(transaction=True)
    def test_edit_post_incorrect_url(self):
        self.set_user()
        response = self.client.get(self.url + str(999999) + '/')
        assert response.status_code == 404

    @pytest.mark.django_db(transaction=True)
    def test_edit_correct_post_for_id(self):
        self.set_user()
        Revista.objects.create(nome="RevistaTeste")
        posts.models.Post.objects.create(
            titulo="TituloTal",
            corpo='CorpoTal',
            revistaAssociada=Revista.objects.get(nome='RevistaTeste'))

        post = Post.objects.get(titulo='TituloTal')
        self.client.post(self.url + str(post.id) + '/',{
            'titulo': 'Novo Título',
            'corpo': 'Novo Corpo',
            'revistaAssociada': Revista.objects.get(nome='RevistaTeste').pk,
        })
        post = Post.objects.get(titulo='Novo Título')
        assert post != False