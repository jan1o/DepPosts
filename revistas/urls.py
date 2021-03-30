from django.urls import path
from .views import listarRevistaAdministrador, adicionarRevista, editarRevista, excluirRevista

urlpatterns = [
    path('listar/', listarRevistaAdministrador, name='listarRevista'),
    path('adicionar/', adicionarRevista, name='adicionarRevista'),
    path('editar/<int:id>/', editarRevista, name='editarRevista'),
    path('excluir/<int:id>/', excluirRevista, name='excluirRevista'),
]

