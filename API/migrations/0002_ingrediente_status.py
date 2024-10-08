# Generated by Django 5.1.1 on 2024-09-09 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("API", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ingrediente",
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
                (
                    "tipo",
                    models.CharField(
                        choices=[
                            ("pao", "Pão"),
                            ("carne", "Carne"),
                            ("opcional", "Opcional"),
                        ],
                        max_length=10,
                    ),
                ),
                ("nome", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Status",
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
                ("nome", models.CharField(max_length=50)),
            ],
        ),
    ]
