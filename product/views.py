from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from random import sample, choice
from product.models import Collection, Product
from product.serializers import CollectionsSerializer, ProductsSerializer, \
    ProductsInCollectionSerializer, ProductFavoriteSerializer


"""
COLLECTIONS VIEWS.
"""


class ListCollectionsPagination8(PageNumberPagination):
    """Set specific pagination for Collections list."""

    page_size = 8


class CollectionsListView(generics.ListAPIView):
    """View to list all Collections."""

    queryset = Collection.objects.all()
    serializer_class = CollectionsSerializer
    pagination_class = ListCollectionsPagination8


class ProductsInCollectionPagination12(PageNumberPagination):
    """Set specific pagination for Product list in definite Collection."""

    page_size = 12


class CollectionDetailView(generics.ListAPIView):
    """Get list of Products by chosen Collection."""
    queryset = Product.objects.all()
    serializer_class = ProductsInCollectionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['collection']
    pagination_class = ProductsInCollectionPagination12


"""
PRODUCTS VIEWS.
"""


class ProductsNoveltiesPagination5(PageNumberPagination):
    """Set specific pagination for Product list in definite Collection."""

    page_size = 5


class ProductsNoveltiesView(generics.ListAPIView):
    """List all 'Novelties' of Products ."""
    queryset = Product.objects.filter(novelty=True)
    serializer_class = ProductsSerializer
    pagination_class = ProductsNoveltiesPagination5


class ProductsInCollectionPagination5(PageNumberPagination):
    """Set specific pagination for Products list in definite Collection."""

    page_size = 5


class ProductsListView(generics.ListAPIView):
    """Get list of Products by chosen Collection."""
    queryset = Product.objects.all()
    serializer_class = ProductsInCollectionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['collection']
    pagination_class = ProductsInCollectionPagination5


class ProductDetailView(generics.RetrieveAPIView):
    """Detail View of Product object by id/pk."""
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


class ProductLikeView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFavoriteSerializer
    lookup_field = 'pk'


class ProductsFavoritesView(generics.ListAPIView):
    """List all 'Favorites' of Products."""
    queryset = Product.objects.filter(favorite=True)
    serializer_class = ProductsSerializer
    pagination_class = ProductsInCollectionPagination12

    """Returns random 5 products if Favorites Products doesn't exists."""
    if queryset.count() == 0:
        try:
            data = []
            collection_id = 1
            while len(data) != 5:
                collect = Product.objects.filter(
                    collection_id=collection_id
                )
                data.append(choice(collect))
                collection_id += 1
            queryset = data
            serializer_class = ProductsSerializer
        except IndexError:
            queryset = sample(tuple(Product.objects.all()), 5)
            serializer_class = ProductsSerializer
