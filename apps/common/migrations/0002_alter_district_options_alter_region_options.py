# Generated by Django 5.1 on 2024-08-17 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='district',
            options={'ordering': ['order_id', 'id']},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ['order_id', 'id']},
        ),
    ]
