from django.urls import path
from rest_framework import views
from .views import ArticleList
app_name = 'api'

urlpatterns = [
    path('', ArticleList.as_view(), name='list')
]
