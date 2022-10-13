from django.urls import path
from . import views

urlpatterns = [path('', views.AuthorsView.as_view(), name='authors')]