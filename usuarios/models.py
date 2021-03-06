from django.db import models
from django.contrib.auth.models import User
from revistas.models import Revista

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    nome = models.CharField(max_length=100)
    revista = models.ForeignKey(Revista, on_delete=models.CASCADE, null=True)
