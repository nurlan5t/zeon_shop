from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import News
from info.serializers import NewsSerializer


class ListNewsPagination(PageNumberPagination):
    """
    Set specific pagination for list News Api.
    """
    page_size = 8


class ListNews(generics.ListAPIView):
    """
    View to list all news in the system.
    """
    queryset = News.objects.all().order_by('-publish')
    serializer_class = NewsSerializer
    pagination_class = ListNewsPagination
