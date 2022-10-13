from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from articles.models import Article


def get_articles(request):
    articles = Article.objects.all
    return render(request, 'home/home.html', {'articles' : articles})


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)