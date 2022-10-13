from django.forms import ModelForm
from .models import Article, Comment

class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'permalink', 'text', 'section', 'published', 'image']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
