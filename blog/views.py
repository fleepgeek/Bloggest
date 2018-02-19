from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post

class Home(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering =  '-pub_date'
    paginate_by = 3


class Dashboard(View):
    def get(self, request, *args, **kwargs):
        view = Home.as_view(
            template_name = 'blog/admin_page.html',
            paginate_by = 4
        )
        return view(request, *args, **kwargs)


class PostDetail(DetailView):
    model = Post
    def get_object(self):
        object = super(PostDetail, self).get_object()
        object.view_count += 1
        object.save()
        return object

    


class PostCreate(CreateView):
    model = Post
    fields = ('title', 'category', 'content')

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super(PostCreate, self).form_valid(form)


class PostUpdate(UpdateView):
    model = Post
    fields = ('title', 'category', 'content')


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('dashboard')