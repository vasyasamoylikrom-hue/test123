from django.contrib import admin
from .models import Article

admin.site.register(Article)

# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ['title', 'text']
#     list_filter = ['created']
#     search_fields = ['title', 'text']
#     ordering = ['-created']