from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Client

@receiver(post_migrate)
def create_default_superuser(sender, **kwargs):
    username = "admin"
    password = "admin123"
    email = "admin@example.com"

    if not User.objects.filter(username=username).exists():
        print("Criando superusuário padrão...")
        User.objects.create_superuser(username=username, password=password, email=email)

@receiver(post_migrate)
def create_default_clients(sender, **kwargs):
    clientes = [
        {"name": "João Silva", "email": "joao.silva@example.com"},
        {"name": "Maria Oliveira", "email": "maria.oliveira@example.com"},
    ]

    for cliente in clientes:
        if not Client.objects.filter(email=cliente["email"]).exists():
            Client.objects.create(name=cliente["name"], email=cliente["email"])
            print(f"Cliente {cliente['name']} criado com sucesso.")