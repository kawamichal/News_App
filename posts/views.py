from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from posts.models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'posts/home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'