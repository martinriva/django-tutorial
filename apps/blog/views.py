import logging

# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from apps.blog.forms import PostForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from apps.blog.models import Post


def home(request):
    posts = Post.objects.all()[:2]
    return render_to_response("blog/home.html", {'posts': posts}, RequestContext(request))


def posts(request):
    posts = Post.objects.all().order_by("-datetime")
    return render_to_response("blog/posts.html", {'posts': posts}, RequestContext(request))


def create_post(request):
    
    if request.method == 'POST':
        if request.POST:
            form = PostForm(request.POST) # A form bound to the POST data
            if form.is_valid(): # All validation rules pass
                # Process the data in form.cleaned_data
                # ...
                user = User.objects.all()[1]
                post = form.save(commit=False)
                post.author = user
                post.save()
                return HttpResponseRedirect(reverse("blog_posts")) # Redirect after POST
    else:
        form = PostForm()
        
    return render_to_response("blog/create_post.html", {'form': form}, RequestContext(request))

def comment_post(request):
    form = None
    return render_to_response("blog/comment_post.html", {'form': form}, RequestContext(request))
