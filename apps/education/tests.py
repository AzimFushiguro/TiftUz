from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Faculty


class FacultyAPITestCase(APITestCase):
    def setUp(self):
        self.item1 = Faculty.objects.create(
            title="test faculty",
            degree="Test faculty test "
        )
        self.item2 = Faculty.objects.create(
            title="test faculty",
            degree="test faculty test"
        )
        self.list_url = reverse('faculty-list')

    def test_faculty_content_list_api(self):
        response = self.client.get(self.list_url)
        r = response.json()
        data1 = r.get("results")[0]
        data2 = r.get("results")[1]
        count = r.get("count")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(2, count)
        self.assertEqual(self.item1.title, data1['title'])
        self.assertEqual(self.item1.degree, data1['degree'])
        self.assertEqual(self.item2.title, data2['title'])
        self.assertEqual(self.item2.degree, data2['degree'])

    def test_active_faculty_detail_api(self):
        response = self.client.get(reverse("faculty-detail", kwargs={"pk": self.item1.id}))
        r = response.json()
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.item1.title, r['title'])

        # self.assertEqual(self.item_active.degree, r['degree'])
        # self.assertEqual(self.item_active.id, r['id'])

    # Create your tests here.

