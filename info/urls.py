from django.urls import path

from info.views import ListNews, AboutUsView

urlpatterns = [
    path('news/', ListNews.as_view()),
    path('about/', AboutUsView.as_view()),
]
