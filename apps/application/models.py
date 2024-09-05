from datetime import datetime
from django.db import models
from apps.common.models import District
from apps.education.models import Direction
from django.contrib.auth import get_user_model
from django.urls import reverse
User = get_user_model()


class ApplicationChoices(models.TextChoices):
    ACCEPTED = "accepted", "Qabul qilindi"
    REJECTED = "rejected", "Rad etildi"
    PENDING = "pending", "Kutilmoqda"


class Application(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = "male", "Erkak"
        FEMALE = "female", "Ayol"


    user = models.ForeignKey(User, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    passport = models.CharField(max_length=9)  # Corrected field type
    pinfl = models.CharField(max_length=14)
    gender = models.CharField(choices=GenderChoices.choices, max_length=6)
    birth_date = models.DateField()
    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=16, choices=ApplicationChoices.choices, default=ApplicationChoices.PENDING)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    accepted_at = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    contract_url = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        from weasyprint import HTML
        from django.conf import settings
        import os
        if (self.status == ApplicationChoices.ACCEPTED or self.status == ApplicationChoices.REJECTED) and not self.accepted_at:
            if self.status == ApplicationChoices.ACCEPTED:
                if not os.path.exists("contracts"):
                    os.makedirs("contrast")
                file_name = f"contracts/{self.first_name}-{self.last_name}.pdf"
                HTML(f"{settings.HOST_NAME}{reverse('application-generator')}?application_id={self.pk}").write_pdf(file_name)
                self.contract_url = file_name
            self.accepted_at = datetime.now()
        return  super().save(*args, **kwargs)
