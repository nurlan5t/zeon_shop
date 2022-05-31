import requests
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from product.models import Collection, Product
from product.serializers import CollectionsSerializer, ProductsSerializer


class ListCollectionsPagination(PageNumberPagination):
    """Set specific pagination for Collections list."""

    page_size = 8


class CollectionsListView(generics.ListAPIView):
    """View to list all Collections."""

    queryset = Collection.objects.all()
    serializer_class = CollectionsSerializer
    pagination_class = ListCollectionsPagination


class ProductDetailView(generics.RetrieveAPIView):
    """Detail View of Product object by id/pk."""
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer

# class CollectionDetailView(generics.ListAPIView):
#     """Detail view the Collection and list it's products."""
#
#     queryset = Product.objects.filter(collection_id=3)
#           # вместо числа 3 нужно получить первичный ключ из url,
#            # для получения всех товаров из указанной коллекции
#     serializer_class = ProductsSerializer
