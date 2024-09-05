from django.urls import path
from apps.news.views import NewscontentListAPIView,NewsContentDetailAPIView

urlpatterns = [
        path("news/<slug:slug>/", NewsContentDetailAPIView.as_view(), name = "news-detail"),
        path("news/", NewscontentListAPIView.as_view(), name = "news-list")
]
