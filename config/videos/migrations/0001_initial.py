# Generated by Django 5.0.6 on 2024-05-24 08:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Video",
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
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("published_at", models.DateTimeField()),
                ("thumbnail_url", models.URLField()),
            ],
            options={
                "indexes": [
                    models.Index(
                        fields=["published_at"], name="videos_vide_publish_dd5f2e_idx"
                    ),
                    models.Index(fields=["title"], name="videos_vide_title_8a2e81_idx"),
                    models.Index(
                        fields=["description"], name="videos_vide_descrip_334af6_idx"
                    ),
                ],
            },
        ),
    ]
