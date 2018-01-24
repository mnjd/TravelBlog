from django.forms import ModelForm

from .models import Articles

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'author', 'body']
