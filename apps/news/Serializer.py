from rest_framework import serializers
from apps.news.models import NewsContent


class NewsContentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsContent
        fields = ("title", "slug", "published_time",)


class NewsContentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsContent
        fields = ("title", "body", "slug", "published_time",)
