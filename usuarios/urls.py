
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('registrar', cadastrar_usuario, name="registrar_usuario"),
]
