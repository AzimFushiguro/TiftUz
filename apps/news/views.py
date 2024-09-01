from django.shortcuts import render
from apps.news.Serializer import NewsContentListSerializer, NewsContentDetailSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from apps.news.models import NewsContent
from django.utils import timezone


from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from apps.news.models import NewsContent
from  apps.news.Serializer import NewsContentListSerializer,NewsContentDetailSerializer
from django.utils import timezone


class NewscontentListAPIView(ListAPIView):
    serializer_class = NewsContentListSerializer
    queryset = NewsContent.objects.filter(
        is_published=True,
        published_time__lte=timezone.now()
    ).order_by("-id")


class NewsContentDetailAPIView(RetrieveAPIView):
    serializer_class = NewsContentDetailSerializer  # Corrected field name
    queryset = NewsContent.objects.filter(
        is_published=True,
        published_time__lte=timezone.now()
    ).order_by("-id")
    lookup_field = 'slug'
