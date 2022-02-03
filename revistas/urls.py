from django.urls import path
#from .views import adicionarRevista, editarRevista, excluirRevista
from .views import *

urlpatterns = [
    path('', ListRevistas.as_view(), name='list_revistas'),
    path('adicionar/', CreateRevista.as_view(), name='create_revista'),
    path('editar/<int:pk>/', UpdateRevista.as_view(), name='update_revista'),
    path('excluir/<int:pk>/', DeleteRevista.as_view(), name='delete_revista'),
]

