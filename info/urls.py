from django.urls import path

from info.views import ListNews

urlpatterns = [
    path('news/', ListNews.as_view()),
]
