from django.shortcuts import render
from .models import Author
from django.views import View

class AuthorsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'authors/authors.html', {'authors' : Author.objects.all})
    
