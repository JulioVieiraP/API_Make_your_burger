# Generated by Django 5.1.1 on 2024-09-09 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Burger",
            fields=[
                (
                    "id",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
                ("nome", models.CharField(max_length=100)),
                ("carne", models.CharField(max_length=100)),
                ("pao", models.CharField(max_length=100)),
                ("opcionais", models.JSONField()),
                ("status", models.CharField(max_length=50)),
            ],
        ),
    ]
