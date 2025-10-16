from django.db import models

class Transaction(models.Model):
    client_name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Sale(models.Model):
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.FloatField()
    date = models.DateField()

    def __str__(self):
        return f"{self.product_name} - {self.date}"

