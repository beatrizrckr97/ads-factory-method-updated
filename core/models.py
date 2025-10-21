from django.db import models

class Transaction(models.Model):
    client_name = models.CharField("Nome do Cliente", max_length=100)
    amount = models.DecimalField("Valor", max_digits=10, decimal_places=2)
    transaction_date = models.DateField("Data da Transação", null=True, blank=True)
    created_at = models.DateTimeField("Data de Criação", auto_now_add=True)


class Sale(models.Model):
    product_name = models.CharField("Nome do Produto", max_length=255)
    quantity = models.IntegerField("Quantidade")
    price = models.FloatField("Preço")
    date = models.DateField("Data da Venda")

    def __str__(self):
        return f"{self.product_name} - {self.date}"
    


class Client(models.Model):
    nome = models.CharField("Nome", max_length=255, default="  ")
    email = models.EmailField("E-mail")
    created_at = models.DateTimeField("Data de Cadastro", auto_now_add=True)

    def __str__(self):
        return self.nome
