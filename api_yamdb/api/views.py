from django.shortcuts import render
from reviews.models import Title, Genre, Category
from rest_framework import filters, permissions, status, viewsets, mixins

from .serializers import (
    TitleSerializer, GenreSerializer,
    CategorySerializer,
)

class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class CreateRetrieveDestroyViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin,
    mixins.DestroyModelMixin, viewsets.GenericViewSet
):
    pass


class GenreViewSet(viewsets.CreateRetrieveDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # permission_classes = [IsAdminOrReadOnly]
    lookup_field = "slug"


class CategoryViewSet(viewsets.CreateRetrieveDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [IsAdminOrReadOnly]
    lookup_field = "slug"
