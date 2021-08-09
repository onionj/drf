# from django.shortcuts import render

# , RetrieveDestroyAPIView, RetrieveAPIView, DestroyAPIView,  ListAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import ArticleSerializers, UserSerializers
from blog.models import Article
from django.contrib.auth.models import User


# Create your views here.


class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
