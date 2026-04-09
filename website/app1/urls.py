from django.urls import path
from . import views

urlpatterns = [
    path("", views.article_list, name='articles list'),
    # path("article/<str:slug>", views.article_list, name='list'),

]