from django.urls import path
from .views import ApplicationAPIView,ApplicationStatusesListApiView
urlpatterns = [
    path("application/", ApplicationAPIView.as_view() ),
    path("application-statuses/", ApplicationStatusesListApiView.as_view() )
]