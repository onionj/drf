from rest_framework import serializers
from blog.models import Article
from django.contrib.auth import get_user_model


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
        ]


class ArticleSerializers(serializers.ModelSerializer):
    author = AuthorSerializers()

    # author = serializers.HyperlinkedIdentityField(view_name='api:authors-detail', lookup_field='pk') #! bug: author id = post id! why?

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


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
