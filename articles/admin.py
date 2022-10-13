from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title', 'author', 'section')
    list_display = ('title', 'author', 'published', 'last_edited')
    ordering = ('title', 'author', 'section', 'last_edited')

class CommentAdmin(admin.ModelAdmin):
    search_fields = ('user',)
    list_display = ('user', 'comment', 'article')
    ordering = ('user', 'article')

class SectionAdmin(admin.ModelAdmin):
    search_fields = list_display = ordering = ('section_name',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Section, SectionAdmin)