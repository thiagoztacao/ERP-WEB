# Generated by Django 4.2 on 2023-04-21 17:06

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="XMLFile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("xml_file", models.FileField(upload_to="xml_files/")),
            ],
        ),
    ]
