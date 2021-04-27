from django.urls import path
from .views import list_posts, create_post, update_post, delete_post

# from .views import list_products, create_product, update_product, delete_product

urlpatterns = [
    path('', list_posts, name='list_posts'),
    path('new/', create_post, name='create_post'),
    path('update/<int:identifier>/', update_post, name='update_post'),
    path('delete/<int:identifier>/', delete_post, name='delete_post'),
]
