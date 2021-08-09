# from django.shortcuts import render

# , RetrieveDestroyAPIView, RetrieveAPIView, DestroyAPIView,  ListAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import ArticleSerializers
from blog.models import Article


# Create your views here.


class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
