"""DepPosts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *
from usuarios import urls as usuario_urls
from revistas import urls as revista_urls
from posts import urls as post_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include(post_urls)),
    path('', hello, name='hello'),
    path('', include(usuario_urls)),
    path('revistas/', include(revista_urls)),
]
