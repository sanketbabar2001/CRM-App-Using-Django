# Generated by Django 4.2.6 on 2023-10-28 15:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="record",
            name="phone",
            field=models.CharField(blank=True, default="", max_length=10),
        ),
    ]
