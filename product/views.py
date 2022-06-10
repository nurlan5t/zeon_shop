from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from random import choice
from rest_framework.decorators import api_view

from product.models import Collection, Product, Cart, calculate_order_info, \
    Order
from product.serializers import CollectionsSerializer, ProductsSerializer, \
    ProductsInCollectionSerializer, ProductFavoriteSerializer, \
    CartSerializer, CartUpdateSerializer, CartCreateSerializer, \
    OrderCreateSerializer

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
def order_info_view(request):
    """Returns all information about Order."""

    return Response({
        "Количество линеек": calculate_order_info()[0],
        "Количество товаров": calculate_order_info()[1],
        "Стоимость": calculate_order_info()[2],
        "Скидка": calculate_order_info()[4],
        "Итого к оплате": calculate_order_info()[3]
        })


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()
