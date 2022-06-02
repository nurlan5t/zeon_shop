from django.urls import path
from product.views import CollectionsListView, ProductDetailView,\
    CollectionDetailView, ProductsNoveltiesView, ProductsListView,\
    ProductLikeView, ProductsFavoritesView

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
]
