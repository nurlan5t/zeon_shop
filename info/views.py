from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from .models import News, AboutUs, HelpQA, OurAdvantages, SliderMainPage,\
    PublicOffer, CallBack, FooterHeaderObjects
from info.serializers import NewsSerializer, AboutUsSerializer, \
    HelpQASeralizer, OurAdvantagesSeralizer, SliderMainPageSeralizer, \
    PublicOfferSeralizer, CallBackSerializer, FooterHeaderObjectsSerializer


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


class PublicOfferView(generics.ListAPIView):
    """
    View to get Public Offer
    """
    queryset = PublicOffer.objects.all()
    serializer_class = PublicOfferSeralizer


class CallBackViewSet(viewsets.ModelViewSet):
    """
    View to create Callback
    """
    queryset = CallBack.objects.all()
    serializer_class = CallBackSerializer
    permission_classes = [AllowAny, ]


class FooterHeaderObjectsView(generics.ListAPIView):
    """
    View to get Footer and Header objects
    """
    queryset = FooterHeaderObjects.objects.all()
    serializer_class = FooterHeaderObjectsSerializer
