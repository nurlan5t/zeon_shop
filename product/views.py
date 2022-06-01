from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from product.models import Collection, Product
from product.serializers import CollectionsSerializer, ProductsSerializer,\
    ProductsInCollectionSerializer

"""
COLLECTIONS VIEWS.
"""


class ListCollectionsPagination(PageNumberPagination):
    """Set specific pagination for Collections list."""

    page_size = 8


class CollectionsListView(generics.ListAPIView):
    """View to list all Collections."""

    queryset = Collection.objects.all()
    serializer_class = CollectionsSerializer
    pagination_class = ListCollectionsPagination


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


class ProductsNoveltiesPagination(PageNumberPagination):
    """Set specific pagination for Product list in definite Collection."""

    page_size = 5


class ProductNoveltiesView(generics.ListAPIView):
    """List all 'Novelties' of Products ."""
    queryset = Product.objects.filter(novelty=True)
    serializer_class = ProductsSerializer
    pagination_class = ProductsNoveltiesPagination


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
