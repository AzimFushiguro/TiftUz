from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Social, District, Region


class CommonAPITestCase(APITestCase):
    def setUp(self):
        self.item = Social.objects.create(
            title="test Social",
            social = "texsdelegram"
        )
        self.list_url = reverse('social-list')

    def test_Social_List_API(self):
        response = self.client.get(self.list_url)
        r = response.json()
        data1 = r.get("results")[0]
        count = r.get("count")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, count)
        self.assertEqual(self.item.title, data1['title'])

# Create your tests here.
