from django.urls import path
from apps.education.views import FacultyListApiView,FacultyDetailAPIView
urlpatterns = [
        path("faculties/",FacultyListApiView.as_view(),name = "faculty-list"),
        path("faculties/<int:pk>",FacultyDetailAPIView.as_view() , name = "faculty-detail")
]