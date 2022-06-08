from rest_framework import generics, permissions, serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from random import choice
from rest_framework.decorators import api_view
from django.db.models import Sum

from product.models import Collection, Product, Cart, ProductObjects
from product.serializers import CollectionsSerializer, ProductsSerializer, \
    ProductsInCollectionSerializer, ProductFavoriteSerializer,\
    CartSerializer, CartUpdateSerializer, CartCreateSerializer


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
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['collection']
    search_fields = ['title']
    pagination_class = ListCollectionsPagination8


class ProductDetailView(generics.RetrieveAPIView):
    """Detail View of Product object by id/pk."""
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


class ProductLikeView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFavoriteSerializer
    lookup_field = 'pk'


class ProductsFavoritesView(generics.ListAPIView):
    """List all 'Favorites' of Products."""
    queryset = Product.objects.filter(favorite=True)
    serializer_class = ProductsSerializer
    pagination_class = ProductsInCollectionPagination12


class FiveRandomProducts(generics.ListAPIView):
    """Returns five random products from each existing Category.

    Apply if Favorites Products or Search results doesn't exists.
    """
    queryset = Product.objects.all()
    serializer_class = ProductsInCollectionSerializer

    def list(self, request, *args, **kwargs):
        lst_ids = list(Collection.objects.all().values_list(
            'id', flat=True))[:5]
        queryset = list(choice(Product.objects.filter(
            collection_id=idc)) for idc in lst_ids)
        serializer_class = ProductsInCollectionSerializer(queryset, many=True)
        return Response(serializer_class.data)


"""
CART VIEWS.
"""


class ProductsCartView(generics.ListAPIView):
    """List all Products in Cart."""
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class ProductCartView(generics.RetrieveUpdateDestroyAPIView):
    """View to Update, Delete Product in Cart."""
    queryset = Cart.objects.all()
    serializer_class = CartUpdateSerializer


class CartCreateView(generics.CreateAPIView):
    """View to add a Product to Cart"""
    serializer_class = CartCreateSerializer
    permission_classes = [permissions.AllowAny]


@api_view()
def get_order_info(request):
    """Calculate Cart objects and returns all information about Order."""
    lines_amount = Cart.objects.all().count()
    products_amount = sum(
        i.product.product.quantity_in_line *
        i.quantity for i in Cart.objects.all())
    total_price = sum(
        i.product.product.old_price * i.quantity for i in Cart.objects.all())
    actual_price = sum(
        i.product.product.actual_price * i.quantity for i in Cart.objects.all())
    discount = total_price - actual_price
    return Response({
        "Количество линеек": lines_amount,
        "Количество товаров": products_amount,
        "Стоимость": total_price,
        "Скидка": discount,
        "Итого к оплате": actual_price
        })
