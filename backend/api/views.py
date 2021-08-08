# from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializer import ArticleSerializers
from blog.models import Article


# Create your views here.


class ArticleList(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
