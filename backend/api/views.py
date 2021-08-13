
# , RetrieveDestroyAPIView, RetrieveAPIView, DestroyAPIView,  ListAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import ArticleSerializers, UserSerializers

from rest_framework.permissions import IsAuthenticated  # IsAdminUser
from .permissions import IsAuthorOrReadOnly, IsStaffOrReadOnly, IsSuperUserOrStaffReadOnly   # , IsSuperUser


from blog.models import Article
from django.contrib.auth import get_user_model  # get User model!

# from rest_framework.authentication import SessionAuthentication # for authentication_classes

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


class RevokeToken(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request):
        request.auth.delete()
        # return Response({"msg": "Token revoked!"}) # This is not standard but it works
        return Response(status=204)

    # def get(self, request):
    #     return Response({"method": "get"})

    # def post(self, request):
    #     return Response({"method": "post"})

    # def put(self, request):
    #     return Response({"method": "put"})
