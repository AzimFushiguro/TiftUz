from rest_framework import serializers
from .models import Faculty, Director, Direction


class FacultyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ("id", "title", "degree")


class DirectorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ("full_name", "bio", "phone_number", "picture")


class DirectionModelSerializer(serializers.ModelSerializer):
    language = serializers.SerializerMethodField()
    education_type = serializers.SerializerMethodField()

    class Meta:
        model = Direction
        fields = ("title", "language", "body", "education_type")

    def get_language(self, obj):
        return obj.get_language_display()

    def get_education_type(self, obj):
        return obj.get_education_type_display()


class FacultyDetailSerializers(serializers.ModelSerializer):
    new_field = serializers.SerializerMethodField()
    degree = serializers.SerializerMethodField()
    director = DirectorModelSerializer()
    directions = DirectionModelSerializer(many=True)
    def get_degree(self,obj):
        return  obj.get_degree_display()
    class Meta:
        model = Faculty
        fields = ("title", "body", "degree", "director", "directions")

    def get_new_field(self,obj):
        return obj.get_new_field_display()
