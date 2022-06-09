from django.urls import path
from product.views import CollectionsListView, ProductDetailView,\
    CollectionDetailView, ProductsNoveltiesView, ProductsListView,\
    ProductLikeView, ProductsFavoritesView, FiveRandomProducts,\
    ProductsCartView, ProductCartView, CartCreateView, order_info_view


urlpatterns = [
    path('collections/', CollectionsListView.as_view(), name='collections'),
    path('collections/detail/', CollectionDetailView.as_view()),
    path('products/', ProductsListView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('products/novelties/', ProductsNoveltiesView.as_view(),
         name='products_novelties'),
    path('products/<int:pk>/favorite/', ProductLikeView.as_view()),
    path('products/favorites/', ProductsFavoritesView.as_view(),
         name='products_favorites'),
    path('products/5random/', FiveRandomProducts.as_view(),
         name='random_products'),
    path('cart/', ProductsCartView.as_view(), name='cart_list'),
    path('cart/<int:pk>/', ProductCartView.as_view(), name='cart_detail'),
    path('products/add_to_cart/', CartCreateView.as_view()),
    path('order/info/', order_info_view),
]
