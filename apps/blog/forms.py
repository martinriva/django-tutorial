from django.forms import ModelForm
from apps.blog.models import Post
from django.forms.widgets import Textarea
from django import forms

class PostForm_0(forms.Form):
    
    title = forms.CharField()
    content = Textarea(attrs={'cols': 60, 'rows': 15})
    
# Using ModelFroms
class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {
            'content': Textarea(attrs={'cols': 60, 'rows': 15}),
        }
        
        
        