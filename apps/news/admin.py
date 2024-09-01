from django.contrib import admin


from apps.news.models import NewsContent


@admin.register(NewsContent)
class NewsContentAdmin(admin.ModelAdmin):
    list_display = ("id", "title","slug", "is_published", "published_time")
    list_editable = ("is_published", "published_time")
    list_filter = ("is_published",)
    search_fields = ("title", "body")
    exclude = ("slug", )
# Register your models here.
