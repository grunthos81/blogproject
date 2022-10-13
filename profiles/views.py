
from authors.models import Author
from articles.models import Article, Comment
from django.views import View
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist



class get_profile(View):

    def get(self, request):
        content = {}
        try:
            current_author = Author.objects.get(userid = self.request.user)
            articles = Article.objects.filter(author=current_author)
            content['articles'] = articles
        except ObjectDoesNotExist:
            content['articles'] = "No articles"
        content['comments'] = Comment.objects.filter(user = self.request.user)
        return render(request, 'profiles/profile.html', content)

        
