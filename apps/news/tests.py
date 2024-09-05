from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import NewsContent
from datetime import datetime
from django.utils import timezone


class NewsContentAPITestCase(APITestCase):
    def setUp(self):
        self.item_active = NewsContent.objects.create(
            title="test news",
            body="test news test",
            is_published=True,
            published_time=timezone.make_aware(datetime(2024, 8, 29, 12, 30, 30)),
        )
        self.item_inactive = NewsContent.objects.create(
            title="test news",
            body="test news test",
            is_published=False,
            published_time=timezone.make_aware(datetime(2024, 8, 31, 12, 30, 30)),
        )
        self.list_url = reverse('news-list')

    def test_news_content_list_api(self):
        response = self.client.get(self.list_url)
        r = response.json()
        data = r.get("results")[0]
        count = r.get("count")
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, count)
        self.assertEqual(self.item_active.title, data['title'])
        self.assertEqual("2024-08-29T12:30:30Z", data['published_time'])
        self.assertEqual(self.item_active.slug, data['slug'])

    def test_active_news_content_detail_api(self):
        response = self.client.get(reverse("news-detail", kwargs={"slug" : self.item_active.slug}))
        r = response.json()
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.item_active.title,r['title'])
        self.assertEqual(self.item_active.body,r['body'])
        self.assertEqual(self.item_active.slug,r['slug'])
    def test_inactive_news_content_detail_api(self):
        response = self.client.get(reverse("news-detail",kwargs={"slug": self.item_inactive.slug}))
        r  = response.json()
        self.assertEqual(404, response.status_code)
