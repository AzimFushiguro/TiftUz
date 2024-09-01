from django.contrib import admin
from apps.common import models


@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "order_id")
    list_editable = ("order_id",)


@admin.register(models.District)
class DisreictAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "region", "order_id")
    list_editable = ("order_id",)


@admin.register(models.Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "social", "link")
    list_editable = ("title", "social", "link")


