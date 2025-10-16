import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ads_factory_method.settings')
django.setup()

from core.models import Sale

sales = [
    {"product_name": "Notebook Dell Inspiron", "amount": 4500, "transaction_date": date(2025, 10, 1)},
    {"product_name": "Mouse Logitech", "amount": 150, "transaction_date": date(2025, 10, 2)},
    {"product_name": "Teclado Mecânico Redragon", "amount": 350, "transaction_date": date(2025, 10, 3)},
]

for s in sales:
    Sale.objects.create(**s)

print("Dados de vendas inseridos com sucesso!")

