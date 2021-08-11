from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model


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
        model = get_user_model()
        fields = '__all__'
