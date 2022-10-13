from http.client import HTTPResponse
from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from datetime import datetime
from authors.models import Author
from django.views import View

class getSection(View):
    def get(self, request, section):
        chosen_section = Section.objects.get(section_name = section)
        articles = Article.objects.filter(section=chosen_section, published=True)
        return render(request, 'articles/articles.html', {'articles' : articles, 'section':chosen_section})

class EditArticle(View):
    
    def get(self, request, pagename):
        pagename = '/' + pagename
        article = Article.objects.get(permalink = pagename)
        article_form = ArticleForm(instance=article)
        if article.author.userid == self.request.user:
            return render(request, 'articles/editarticle.html', {'article' : article_form})
        else:
            return render(request, 'articles/message.html', {'message' : "You are not the author of this article. Go away."})
    
    def post(self, request, pagename):
        pagename = '/' + pagename
        article = Article.objects.get(permalink = pagename)
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article.last_edited = datetime.now()
            article_form.save()
            return HttpResponseRedirect(self.request.path_info)
        else:
            return render(request, 'articles/message.html', {'message' : "something went wrong."})


class NewArticle(View):

    def get(self, request):
        try:
            if Author.objects.filter(userid = self.request.user).exists():
                article_form = ArticleForm(request.GET)
                return render(request, 'articles/newarticle.html', {'articleform' : article_form})
            else:
                return render(request, 'articles/message.html', {'message':'You are not an author. Go away.'})
        except TypeError:
            return render(request, 'articles/message.html', {'message' : 'You are not logged in.'})

    
    def post(self, request):
        current_author = Author.objects.get(userid = self.request.user)
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            Article.objects.create(title=article_form.cleaned_data['title'],
                                    summary = article_form.cleaned_data['summary'],
                                    permalink = article_form.cleaned_data['permalink'],
                                    author = current_author,
                                    text = article_form.cleaned_data['text'],
                                    section = article_form.cleaned_data['section'],
                                    published = article_form.cleaned_data['published'],
                                    last_edited = datetime.now(),
                                    image = article_form.cleaned_data['image'],)
            return render(request, 'articles/message.html', {'message' : 'Article added successfully.'})

class ViewArticle(View):
    def get(self, request, pagename):
        pagename = '/' + pagename
        article = Article.objects.get(permalink=pagename)
        cform = CommentForm()
        comments = Comment.objects.filter(article=article)
        content = {'article' : article, 'comments' : comments, 'form' : cform}
        return render(request, 'articles/singlearticle.html', content)
    
    def post(self, request, pagename):
        pagename = '/' + pagename
        cform = CommentForm(request.POST)
        article = Article.objects.get(permalink=pagename)
        if cform.is_valid():
            Comment.objects.create(comment = cform.cleaned_data['comment'], user = self.request.user, 
                                    article=article, timepublished = datetime.now())
            return HttpResponseRedirect(self.request.path_info)


    


