from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from apps.education.serializers import FacultyListSerializer, FacultyDetailSerializers
from .models import Faculty


class FacultyListApiView(ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultyListSerializer


class FacultyDetailAPIView(RetrieveAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultyDetailSerializers
# Create your views here.
