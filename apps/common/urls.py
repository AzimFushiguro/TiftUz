from django.urls import path
from apps.common.views import RegionListApiView, DestrictListByRegionApiView, SocialListApiView,GenderChoicesAPIView

urlpatterns = [
    path("regions/", RegionListApiView.as_view()),
    path("<int:pk>/districts/", DestrictListByRegionApiView.as_view()),
    path("socials/", SocialListApiView.as_view()),
    path("genders/",GenderChoicesAPIView.as_view())
]
