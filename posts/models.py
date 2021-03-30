from django.db import models
from django.contrib.auth.models import User
from revistas.models import Revista


class Post(models.Model):
    titulo = models.CharField(max_length=100)
    corpo = models.CharField(max_length=1000)
    dataPublicacao = models.DateTimeField(auto_now_add=True)
    revistaAssociada = models.OneToOneField(Revista, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.titulo
