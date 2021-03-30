from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def list_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


def create_post(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_posts')

    return render(request, 'posts-form.html', {'form': form})


def update_post(request, identifier):
    post = Post.objects.get(id=identifier)
    form = PostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect('list_posts')

    return render(request, 'posts-form.html', {'form': form, 'post': post})


def delete_post(request, identifier):
    post = Post.objects.get(id=identifier)

    if request.method == 'POST':
        post.delete()
        return redirect('list_posts')

    return render(request, 'post-delete-confirm.html', {'post': post})
