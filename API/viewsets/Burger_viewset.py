from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from API.models import Burger, Ingrediente, Status
from API.serializers import BurgerSerializer, IngredienteSerializer, StatusSerializer


class BurgerViewSet(viewsets.ModelViewSet):
    queryset = Burger.objects.all()
    serializer_class = BurgerSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        burgers = {"burgers": serializer.data}
        return Response(burgers)

    @action(detail=False, methods=["get"])
    def ingredientes(self, request):
        paes = Ingrediente.objects.filter(tipo="pao")
        carnes = Ingrediente.objects.filter(tipo="carne")
        opcionais = Ingrediente.objects.filter(tipo="opcional")
        status = Status.objects.all()

        paes_serializer = IngredienteSerializer(paes, many=True)
        carnes_serializer = IngredienteSerializer(carnes, many=True)
        opcionais_serializer = IngredienteSerializer(opcionais, many=True)
        status_serializer = StatusSerializer(status, many=True)

        ingredientes = {
            "paes": paes_serializer.data,
            "carnes": carnes_serializer.data,
            "opcionais": opcionais_serializer.data,
            "status": status_serializer.data,
        }
        return Response(ingredientes)
