from rest_framework import serializers
from blog.models import Article
from django.contrib.auth.models import User


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article

        # select all fields:
        fields = '__all__'

        # # select this fields:
        # fields = ('title', 'slug', 'author', 'content', 'publish', 'status',)

        # # deny this fields:
        # exclude = ('created', 'updated',)


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
