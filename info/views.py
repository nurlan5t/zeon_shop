from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import News, AboutUs, HelpQA
from info.serializers import NewsSerializer, AboutUsSerializer, HelpQASeralizer


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


class AboutUsView(generics.ListAPIView):
    """
    View to get info About us
    """
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class HelpQAView(generics.ListAPIView):
    """
    View to get answer for frequently questions
    """
    queryset = HelpQA.objects.all()
    serializer_class = HelpQASeralizer
