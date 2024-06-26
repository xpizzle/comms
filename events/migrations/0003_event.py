# Generated by Django 5.0.4 on 2024-06-10 18:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0002_rename_location_events_street_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("filmname", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="event_images")),
            ],
        ),
    ]
