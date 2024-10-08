# Generated by Django 3.2.7 on 2021-09-21 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("results", "0003_alter_ytresult_title"),
    ]

    operations = [
        migrations.CreateModel(
            name="YoutubeAPIKeys",
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
                ("api_key", models.CharField(max_length=200, unique=True)),
                ("name", models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
