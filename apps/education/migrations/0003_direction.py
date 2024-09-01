# Generated by Django 5.1 on 2024-08-19 06:44

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_director_faculty_delete_direktor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('language', models.CharField(choices=[('uz', "O'zbek tili"), ('ru', 'Rus tili'), ('en', 'English tili')], max_length=255)),
                ('body', ckeditor.fields.RichTextField()),
                ('education_type', models.CharField(choices=[('daytime', 'Kunduzgi'), ('part_time', 'Sirtqi'), ('Evening', 'Kechki')], max_length=255)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.faculty')),
            ],
        ),
    ]
