from django.db import models
from ckeditor.fields import RichTextField


class EducationDegreeChoices(models.TextChoices):
    MASTER = "master", "Magistratura"
    BACHELORS = "bachelors", "Bakalavr"


class LanguageChoices(models.TextChoices):
    UZ = "uz", "O'zbek tili"
    RU = "ru", "Rus tili"
    EN = "en", "English tili"


class EducationTypeChoices(models.TextChoices):
    DAYTIME = "daytime", "Kunduzgi"
    PART_TIME = "part_time", "Sirtqi"
    EVENING = "Evening", "Kechki"


class Director(models.Model):
    full_name = models.CharField(max_length=255)
    bio = RichTextField()
    phone_number = models.CharField(max_length=255)
    picture = models.ImageField(upload_to="images")

    def __str__(self):
        return self.full_name


class Faculty(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    degree = models.CharField(max_length=255, choices=EducationDegreeChoices.choices)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Direction(models.Model):
    title = models.CharField(max_length=255)
    language = models.CharField(choices=LanguageChoices.choices,max_length=255)
    body = RichTextField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name= "directions")
    education_type = models.CharField(choices=EducationTypeChoices.choices, max_length=255)

    def __str__(self):
        return self.title

