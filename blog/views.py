from django.shortcuts import render, redirect
from django.views import View

from .models import Post
from .forms import PostForm

class Home(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/home.html', {'posts': posts})


class PostDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})


class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_form.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'blog/post_form.html', {'form': form})