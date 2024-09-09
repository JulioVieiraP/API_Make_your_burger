import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from API.models import Ingrediente, Status

# Dados de exemplo
paes = [
    {"tipo": "pao", "nome": "Italiano Branco"},
    {"tipo": "pao", "nome": "3 Queijos"},
    {"tipo": "pao", "nome": "Parmesão e Orégano"},
    {"tipo": "pao", "nome": "Integral"},
]

carnes = [
    {"tipo": "carne", "nome": "Maminha"},
    {"tipo": "carne", "nome": "Alcatra"},
    {"tipo": "carne", "nome": "Picanha"},
    {"tipo": "carne", "nome": "Veggie burger"},
]

opcionais = [
    {"tipo": "opcional", "nome": "Bacon"},
    {"tipo": "opcional", "nome": "Cheddar"},
    {"tipo": "opcional", "nome": "Salame"},
    {"tipo": "opcional", "nome": "Tomate"},
    {"tipo": "opcional", "nome": "Cebola roxa"},
    {"tipo": "opcional", "nome": "Pepino"},
]

status_list = [{"nome": "Solicitado"}, {"nome": "Em produção"}, {"nome": "Finalizado"}]

# Populando o banco de dados
for item in paes + carnes + opcionais:
    Ingrediente.objects.get_or_create(tipo=item["tipo"], nome=item["nome"])

for item in status_list:
    Status.objects.get_or_create(nome=item["nome"])

print("Dados populados com sucesso!")
