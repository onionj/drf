# from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView  # ,  ListAPIView
from .serializer import ArticleSerializers
from blog.models import Article


# Create your views here.


class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
