from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import News, AboutUs, HelpQA, OurAdvantages, SliderMainPage
from info.serializers import NewsSerializer, AboutUsSerializer, \
    HelpQASeralizer, OurAdvantagesSeralizer, SliderMainPageSeralizer


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


class OurAdvantagesView(generics.ListAPIView):
    """
    View to get list of Our Advantages
    """
    queryset = OurAdvantages.objects.all()
    serializer_class = OurAdvantagesSeralizer


class SliderMainPageView(generics.ListAPIView):
    """
    View to get list of Slider links-images to Main Page
    """
    queryset = SliderMainPage.objects.all()
    serializer_class = SliderMainPageSeralizer
