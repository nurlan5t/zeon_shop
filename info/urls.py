from django.urls import path
from info.views import ListNews, AboutUsView, HelpQAView, OurAdvantagesView, \
    SliderMainPageView, PublicOfferView, CallBackViewSet, \
    FooterHeaderObjectsView, ImageHelpQAView

urlpatterns = [
    path('news/', ListNews.as_view()),
    path('about/', AboutUsView.as_view()),
    path('help/', HelpQAView.as_view()),
    path('help/image/', ImageHelpQAView.as_view()),
    path('our_advantages/', OurAdvantagesView.as_view()),
    path('slider/', SliderMainPageView.as_view()),
    path('public_offer/', PublicOfferView.as_view()),
    path('callback/', CallBackViewSet.as_view({'post': 'create'})),
    path('footer_header_objects/', FooterHeaderObjectsView.as_view()),
]
