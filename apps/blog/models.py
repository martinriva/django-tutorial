from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, blank=True, null=True)
    title = models.CharField(blank=False, max_length=100)
    content = models.TextField(blank=False, max_length=40)
    datetime = models.DateTimeField(blank=True, auto_now_add=True)
    visits = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User)
    post = models.ForeignKey(Post)
    content = models.CharField(blank=False, max_length=100)
    


