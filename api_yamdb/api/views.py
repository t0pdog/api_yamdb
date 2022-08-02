from django.shortcuts import render
from reviews.models import Title, Genre, Category
from rest_framework import filters, permissions, status, viewsets, mixins
from .permissions import IsAdminOrReadOnly, IsOwnerOrHigherOrReadOnly
from rest_framework.pagination import LimitOffsetPagination

from .serializers import (
    TitleSerializer, GenreSerializer,
    CategorySerializer,
)

class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = LimitOffsetPagination


class CreateRetrieveDestroyViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin,
    mixins.DestroyModelMixin, viewsets.GenericViewSet
):
    pass


class GenreViewSet(CreateRetrieveDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = "slug"


class CategoryViewSet(CreateRetrieveDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = "slug"
