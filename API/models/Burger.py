from django.db import models


class Ingrediente(models.Model):
    TIPO_CHOICES = [
        ("pao", "Pão"),
        ("carne", "Carne"),
        ("opcional", "Opcional"),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    nome = models.CharField(max_length=100)


class Status(models.Model):
    nome = models.CharField(max_length=50)


class Burger(models.Model):
    nome = models.CharField(max_length=100)
    carne = models.CharField(max_length=100)
    pao = models.CharField(max_length=100)
    opcionais = models.JSONField()
    status = models.CharField(max_length=50)
