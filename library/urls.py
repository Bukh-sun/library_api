from django.urls import path, include
from rest_framework import routers
from library.views import BookViewSet, AuthorViewSet, GenreViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet, basename='book')
router.register('authors', AuthorViewSet, basename='author')
router.register('genres', GenreViewSet, basename='genre')
urlpatterns = [path('', include(router.urls)),

]