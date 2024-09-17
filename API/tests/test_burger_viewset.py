from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from API.models import Burger, Ingrediente, Status


class BurgerViewSetTest(APITestCase):

    def setUp(self):
        # Criando dados de exemplo
        Ingrediente.objects.create(tipo="pao", nome="3 Queijos")
        Ingrediente.objects.create(tipo="carne", nome="Maminha")
        Ingrediente.objects.create(tipo="opcional", nome="Bacon")
        Status.objects.create(nome="Finalizado")

        self.burger_data = {
            "nome": "Júlio",
            "carne": "Maminha",
            "pao": "3 Queijos",
            "opcionais": ["Bacon", "Pepino", "Tomate"],
            "status": "Finalizado",
        }

    def test_get_ingredientes(self):
        url = reverse("burgers-ingredientes")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("paes", response.data)
        self.assertIn("carnes", response.data)
        self.assertIn("opcionais", response.data)
        self.assertIn("status", response.data)

    def test_create_burger(self):
        url = reverse("burgers-list")
        response = self.client.post(url, self.burger_data, format="json")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["nome"], self.burger_data["nome"])
        self.assertEqual(response.data["carne"], self.burger_data["carne"])
        self.assertEqual(response.data["pao"], self.burger_data["pao"])
        self.assertEqual(response.data["opcionais"], self.burger_data["opcionais"])
        self.assertEqual(response.data["status"], self.burger_data["status"])
