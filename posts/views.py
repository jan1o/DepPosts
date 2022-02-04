from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from .models import Post
from .forms import PostForm

#import primeiro o login
class ListPosts(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Post
    template_name = "posts.html"

    def get_queryset(self):
        self.object_list = Post.objects.filter(usuario=self.request.user)
        return self.object_list


class CreatePost(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    template_name = "posts-form.html"
    form_class = PostForm
    success_url = reverse_lazy('list_posts')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

class UpdatePost(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Post
    fields = ['titulo', 'corpo', 'revistaAssociada']
    template_name = "posts-form.html"
    success_url = reverse_lazy('list_posts')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Post, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

class DeletePost(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Post
    template_name = "post-delete-confirm.html"
    success_url = reverse_lazy('list_posts')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Post, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object

