from django.shortcuts import render
from django.views.generic import ListView, DetailView

from post.models import Post


# Create your views here.


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'

