from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm

class ListPosts(ListView):
    model = Post
    template_name = "posts.html"


class CreatePost(CreateView):
    template_name = "posts-form.html"
    form_class = PostForm
    success_url = reverse_lazy('list_posts')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url

class UpdatePost(UpdateView):
    model = Post
    fields = ['titulo', 'corpo', 'revistaAssociada']
    template_name = "posts-form.html"
    success_url = reverse_lazy('list_posts')

class DeletePost(DeleteView):
    model = Post
    template_name = "post-delete-confirm.html"
    success_url = reverse_lazy('list_posts')

