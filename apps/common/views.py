from django.shortcuts import render
from rest_framework import generics,response
from apps.common.models import Region,District,Social
from  apps.common.serializers import RegionListSerializer,DisrritSerializer,SocialSerializer
from rest_framework.views import APIView


class RegionListApiView(generics.ListAPIView):
    serializer_class =RegionListSerializer
    queryset = Region.objects.all()


class DestrictListByRegionApiView(generics.ListAPIView):
    serializer_class = DisrritSerializer
    queryset = District.objects.all()
    def get_queryset(self):
        region_id =self.request.parser_context['kwargs'].get('pk',None)
        qs = super().get_queryset()
        return qs.filter(region_id=region_id)
class SocialListApiView(generics.ListAPIView):
    serializer_class = SocialSerializer
    queryset = Social.objects.all()

class GenderChoicesAPIView(APIView):


    def get(self,request,*args,**kwargs):
        data = [
            {
                "key":"male",
                "value":"Erkak"
            },
            {
                "key":"female",
                "value":"Ayol"
            }
        ]
        return response.Response(data,status=200)
# Create your views here.
