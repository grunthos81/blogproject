from django.contrib import admin
from .models import Author

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ordering = list_display = ('name',)

admin.site.register(Author, AuthorAdmin)
