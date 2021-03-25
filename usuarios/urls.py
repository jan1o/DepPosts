from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from .views import UsuarioCreate, UsuarioUpdate

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signin/', UsuarioCreate.as_view(), name='signin'),
    path('atualizar-usuario/', UsuarioUpdate.as_view(), name='update')
]
