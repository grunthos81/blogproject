from http.client import HTTPResponse
from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from datetime import datetime
from authors.models import Author
from django.views import View
from django.urls import reverse_lazy
from re import sub

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


class NewArticleView(View):

    def get(self, request):
        try:
            if Author.objects.filter(userid = self.request.user).exists():
                aform  = ArticleForm(request.GET)
                return render(request, 'articles/newarticle.html', {'aform' : aform})
            else:
                messages.warning(request, 'You are not an author, bugger off.')
                return HttpResponseRedirect(reverse_lazy('home'))
        except TypeError:
            messages.warning(request, 'You are not logged in.')
            return HttpResponseRedirect(reverse_lazy('home'))
    
    def post(self, request):
        author = Author.objects.get(userid = self.request.user)
        aform = ArticleForm(request.POST)
        if aform.is_valid():
            title = aform.cleaned_data['title']
            permalink = re.sub(r'[^a-zA-Z\d]', '', str(title))
            Article.objects.create(title = title, permalink = permalink, 
            section = aform.cleaned_data['section'], text = aform.cleaned_data['text'], 
            author = author, last_edited = datetime.now(), 
            published = aform.cleaned_data['published'], image = aform.cleaned_data['image'])
            messages.warning(request, 'Article created successfully.')
            return HttpResponseRedirect(reverse_lazy('home'))
        else:
            messages.warning(request, aform.errors)
            return HttpResponseRedirect(reverse_lazy('home'))

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


    


