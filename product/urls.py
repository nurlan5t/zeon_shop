from django.urls import path
from product.views import CollectionsListView

urlpatterns = [
    path('collections/', CollectionsListView.as_view(), name='index'),
]
