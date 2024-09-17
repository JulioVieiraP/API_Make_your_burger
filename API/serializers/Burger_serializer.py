from rest_framework import serializers
from API.models import Burger, Ingrediente, Status


class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = "__all__"


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"


class BurgerSerializer(serializers.ModelSerializer):
    opcionais = serializers.JSONField()

    class Meta:
        model = Burger
        fields = ["id", "nome", "carne", "pao", "opcionais", "status"]
