from django.urls import path

from info.views import ListNews, AboutUsView, HelpQAView, OurAdvantagesView, \
    SliderMainPageView

urlpatterns = [
    path('news/', ListNews.as_view()),
    path('about/', AboutUsView.as_view()),
    path('help/', HelpQAView.as_view()),
    path('our_advantages/', OurAdvantagesView.as_view()),
    path('slider/', SliderMainPageView.as_view()),
]
