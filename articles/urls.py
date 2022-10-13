from django.urls import path
from . import views

urlpatterns = [path('newarticle', views.NewArticle.as_view(), name='new'),
               path('editarticle/<str:pagename>', views.EditArticle.as_view(), name='edit'),
               path('<str:pagename>', views.ViewArticle.as_view(), name='get'),
               path('section/bible', views.getSection.as_view(), {'section' : 'bible'}, name='section'),
               path('section/travel', views.getSection.as_view(), {'section' : 'travel'}, name='section'),
               path('section/coding', views.getSection.as_view(), {'section' : 'coding'}, name='section'),]
