from django.urls.conf import include
from rest_framework import routers
from .views import UserViewSet, ArticleViewSet
from django.urls import path

app_name = 'api'


router = routers.SimpleRouter()
router.register('', ArticleViewSet)
router.register('users', UserViewSet)
urlpatterns = [
    path("", include(router.urls))
]
