# Create your views here.
from django.shortcuts import render_to_response

def home(request):
    posts = []
    return render_to_response("blog/home.html", {'posts': posts})


def posts(request):
    posts = []
    return render_to_response("blog/posts.html", {'posts': posts})


def create_post(request):
    form = None
    return render_to_response("blog/create_post.html", {'form': form})

def comment_post(request):
    form = None
    return render_to_response("blog/comment_post.html", {'form': form})