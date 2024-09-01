from django.db import models


class Region(models.Model):
    title = models.CharField(max_length=255)
    order_id = models.IntegerField(unique=True)

    class Meta:
        ordering = ["order_id", "id"]

    def __str__(self):
        return self.title


class District(models.Model):
    title = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    order_id = models.IntegerField(unique=True)

    class Meta:
        ordering = ["order_id", "id"]

    def __str__(self):
        return self.title


class Social(models.Model):
    class SocialMediaChoices(models.TextChoices):
        TELEGRAM = "telegram", "Telegram"
        INSTAGRAM = "instagram,", "Instagram"
        FACEBOOK = "facebook", "Facebook"
        YOUTUBE = "youtube", "Youtube"
    social = models.CharField(choices=SocialMediaChoices.choices,max_length=16)
    title = models.CharField(max_length=255)
    link = models.URLField()


# Create your models here.
