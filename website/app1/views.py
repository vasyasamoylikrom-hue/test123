from django.shortcuts import render
from django.views.generic import ListView

from .models import Article


def article_list(request):
    articles = Article.objects.all() # Все записи из таблицы
    return render(request, 'articles.html', {
        'articles' : articles
    })


# class ArticleListView(ListView):
#     model = Article
#     template_name = 'articles.html'
#     context_object_name = 'articles'
