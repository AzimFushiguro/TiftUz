from django.shortcuts import render
from .serializer import ApplicationCreateSerializer,ApplicationDetailSerializer
from rest_framework.generics import CreateAPIView,ListAPIView
from .models import Application
from rest_framework.permissions import IsAuthenticated
class ApplicationAPIView(CreateAPIView):
    serializer_class = ApplicationCreateSerializer
    queryset = Application.objects.all()
    permission_classes = (IsAuthenticated,)
# Create your views here.
class ApplicationStatusesListApiView(ListAPIView):
    serializer_class = ApplicationDetailSerializer
    queryset = Application.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs =super().get_queryset()
        return qs.filter(user=self.request.user)