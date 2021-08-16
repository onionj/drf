
from django.contrib.auth import get_user_model  # get User model!
from rest_framework.viewsets import ModelViewSet

from .serializer import ArticleSerializers, UserSerializers
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
