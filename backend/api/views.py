
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView

from .serializer import ArticleSerializers, UserSerializers, AuthorSerializers
from .permissions import IsAuthorOrReadOnly, IsStaffOrReadOnly, IsSuperUserOrStaffReadOnly

from blog.models import Article


# Create your views here.

class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()

    filterset_fields = ['status', 'author__username']
    search_fields = [
        'title',
        'content',
        'author__username',
        'author__first_name',
        'author__last_name',
    ]
    ordering_fields = ['id', 'publish', 'status', ]
    ordering = ['-publish']  # ! default = new to old

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsSuperUserOrStaffReadOnly,)
    filterset_fields = ['id', 'username', 'is_staff', 'is_active', 'email']
    ordering_fields = ['id', 'last_login', 'is_staff', 'date_joined']


class AuthorRetrieve(RetrieveAPIView):
    '''Author detail'''
    queryset = get_user_model().objects.filter(is_staff=True)
    serializer_class = AuthorSerializers
    filterset_fields = ['id', 'username', 'is_active', 'email']
    ordering_fields = ['id', 'last_login', 'is_staff', 'date_joined']
