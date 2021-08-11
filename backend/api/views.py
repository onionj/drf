
# , RetrieveDestroyAPIView, RetrieveAPIView, DestroyAPIView,  ListAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import ArticleSerializers, UserSerializers
# from rest_framework.permissions import IsAdminUser # default drf premissions
from .permissions import IsAuthorOrReadOnly, IsStaffOrReadOnly, IsSuperUserOrStaffReadOnly  # , IsSuperUser

# from rest_framework.authentication import SessionAuthentication

from blog.models import Article
from django.contrib.auth import get_user_model  # get User model!


# Create your views here.


class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    # authentication_classes = (SessionAuthentication,)


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)


class UserList(ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsSuperUserOrStaffReadOnly,)


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsSuperUserOrStaffReadOnly,)
