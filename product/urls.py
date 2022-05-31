from django.urls import path
from product.views import CollectionsListView, ProductDetailView
# CollectionDetailView

urlpatterns = [
    path('collections/', CollectionsListView.as_view(), name='collections'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product'),
    # path('collections/<int:pk>/', CollectionDetailView.as_view(),
    #      name='collection'),
]
