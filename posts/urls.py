from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import CreatePost, ListPosts, UpdatePost, DeletePost

# from .views import list_products, create_product, update_product, delete_product

urlpatterns = [
    path('', ListPosts.as_view(), name='list_posts'),
    path('new/', CreatePost.as_view(), name='create_post'),
    path('update/<int:pk>/', UpdatePost.as_view(), name='update_post'),
    path('delete/<int:pk>/', DeletePost.as_view(), name='delete_post'),
]
