from django.db import models
from ckeditor.fields import RichTextField
from authors.models import Author
from django.contrib.auth.models import User
from datetime import datetime

class Section(models.Model):
    section_name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.section_name

class Article(models.Model):
    title = models.CharField(max_length=40)
    permalink = models.CharField(max_length=80, unique=True, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = RichTextField(blank=True, null=True)
    section  = models.ForeignKey(Section, on_delete=models.CASCADE, blank=False)
    published = models.BooleanField(default=False, blank=False)
    last_edited = models.DateTimeField(default=datetime.now())
    image = models.URLField(default='https://i.imgur.com/PdEQAt6.jpg', blank=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-last_edited']

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.TextField('comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timepublished = models.DateTimeField()

    def __str__(self):
        return ("{0} commented on {1}").format(self.user, self.comment)





    
