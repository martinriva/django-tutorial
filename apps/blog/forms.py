from django.forms import ModelForm
from apps.blog.models import Post
from django.forms.widgets import Textarea

# Create the form class.
class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content')
        #widgets = {
        #    'content': Textarea(attrs={'cols': 80, 'rows': 20}),
        #}