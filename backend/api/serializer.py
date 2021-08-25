from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model
from drf_dynamic_fields import DynamicFieldsMixin


class ArticleSerializers(DynamicFieldsMixin, serializers.ModelSerializer):

    def get_author(self, obj):
        return {
            "username": obj.author.username,
            "first_name": obj.author.first_name,
            "last_name": obj.author.last_name,
        }

    author = serializers.SerializerMethodField("get_author")

    class Meta:
        model = Article

        # select all fields:
        fields = '__all__'

        # # select this fields:
        # fields = ('title', 'slug', 'author', 'content', 'publish', 'status',)

        # # deny this fields:
        # exclude = ('created', 'updated',)

    def validate_title(self, value):
        filter_list = ['fuck', 'javascript']
        for i in filter_list:
            if i in value:
                raise serializers.ValidationError(
                    f"don't use bad words!: {i}")


class UserSerializers(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ('password', 'email',)
