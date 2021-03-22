from django.db import models

class Revista(models.Model):
    login = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)

class Usuario(models.Model):
    login = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    revista =  models.ForeignKey(Revista, on_delete=models.CASCADE)

