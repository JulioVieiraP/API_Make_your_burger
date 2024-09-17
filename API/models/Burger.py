import random
import string
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
    id = models.CharField(
        primary_key=True, max_length=10, editable=False
    )  # Campo personalizado para ID
    nome = models.CharField(max_length=100)
    carne = models.CharField(max_length=100)
    pao = models.CharField(max_length=100)
    opcionais = models.JSONField()
    status = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.id:  # Gera o ID apenas se não existir
            self.id = self.generate_custom_id()
        super().save(*args, **kwargs)

    def generate_custom_id(self):
        # Função para gerar um ID aleatório
        return "".join(random.choices(string.ascii_lowercase + string.digits, k=4))
