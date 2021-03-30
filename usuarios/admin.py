from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    model = Usuario
    list_display = ('user', 'nome',)
