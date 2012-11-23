from django.forms import ModelForm
from apps.blog.models import Post
from django.forms.widgets import Textarea
from django import forms
from django.core.exceptions import ValidationError

def without_asterix(value):
    if "*" in value:
        raise ValidationError("Value can't contain an asterix char")
    
class PostForm_0(forms.Form):
    
    title = forms.CharField(required=True, help_text="Help text here")
    content = Textarea(attrs={'cols': 60, 'rows': 15})
    
# Using ModelFroms
class PostForm(ModelForm):
    title = forms.CharField(required=True, help_text="Aqui va el titulo del post", label="Titulo", validators=[without_asterix])
    
    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {
            'content': Textarea(attrs={'cols': 60, 'rows': 15}),
        }