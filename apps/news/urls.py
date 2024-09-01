from django.urls import path
from apps.news.views import NewscontentListAPIView,NewsContentDetailAPIView

urlpatterns = [
        path("news/<slug:slug>/", NewsContentDetailAPIView.as_view()),
        path("news/", NewscontentListAPIView.as_view())
]
