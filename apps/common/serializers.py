from rest_framework import serializers
from apps.common.models import Region, Social, District


class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ("id", "title")


class DisrritSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ("id", "title")


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ("id", "title", "social", "link")


