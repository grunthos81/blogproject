
from django.contrib import admin
from django.urls import path, include
#from django.conf.urls.static import static
#from django.conf import settings
from django.views.generic.base import TemplateView
from home.views import Register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('authors/', include('authors.urls')),
    path('register/success/', TemplateView.as_view(template_name='registration/success.html'), 
    name='register-success'),
    path('register/', Register.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
    path('articles/', include('articles.urls')),
    path('profile/', include('profiles.urls'))
]