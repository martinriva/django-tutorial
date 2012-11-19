import logging

from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from apps.blog.models import Post
from apps.blog.forms import PostForm

def home(request):
    posts = Post.objects.all()[:2]
    return render(request, "blog/home.html", {'posts': posts})


def posts(request):
    
    posts = Post.objects.all().order_by("-datetime")
    result = {}
    for p in posts:
        result[p] = p.comment_set.all()
    #posts = Post.objects.filter(title__startswith="C")
    return render(request, "blog/posts.html", {'posts': result})

def create_post(request):
    
    form = PostForm(request.POST or None)
    if form.is_valid(): # All validation rules pass
        user = User.objects.all()[0]
        post = form.save(commit=False)
        post.author = user
        post.save()
        return redirect(reverse("blog_posts"))
        
    return render(request, "blog/create_post.html", {'form': form})


def edit_post(request, post_id):
    
    a_post_instance = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance=a_post_instance)
    if form.is_valid(): # All validation rules pass
        post = form.save()
        # do something
        post.save()
        return redirect(reverse("blog_posts"))
        
    return render(request, "blog/edit_post.html", {'form': form})


# ---------------------------------------------------
# FORMS EXAMPLES
# ---------------------------------------------------


def create_post_first_aproach(request):
    
    if request.method == "POST":
        form = PostForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            user = User.objects.all()[0]
            post = form.save(commit=False)
            post.author = user
            post.save()
            return redirect(reverse("blog_posts")) # Redirect after POST
    else:
        form = PostForm()
        
    return render(request, "blog/create_post.html", {'form': form})


def comment_post(request):
    form = None
    return render(request, "blog/comment_post.html", {'form': form})

    
