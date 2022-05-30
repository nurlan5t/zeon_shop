from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from product.models import Collection
from product.serializers import CollectionsSerializer


class ListCollectionsPagination(PageNumberPagination):
    """Set specific pagination for Collection list."""

    page_size = 8


class CollectionsListView(generics.ListAPIView):
    """View to list all Collections."""

    queryset = Collection.objects.all()
    serializer_class = CollectionsSerializer
    pagination_class = ListCollectionsPagination
