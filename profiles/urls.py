from django.urls import path
from . import views

urlpatterns = [path('', views.get_profile.as_view(), name='getprofile')]