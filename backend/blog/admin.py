from django.contrib import admin
from .models import Article

# Register your models here.

# admin.site.register(Article)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'publish')
    search_fields = ('title', 'author', 'status', 'publish')
    list_editable = ('status', 'author', 'publish')
