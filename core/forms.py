from django import forms
from .models import Client, Sale, Transaction
from datetime import date

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nome', 'email']
        labels = {
            'nome': 'Nome',
            'email': 'E-mail',
        }

class SaleForm(forms.ModelForm):
    date = forms.DateField(
        label="Data da Venda",
        initial=date.today,
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Sale
        fields = ['product_name', 'quantity', 'price', 'date']
        labels = {
            'product_name': 'Nome do Produto',
            'quantity': 'Quantidade',
            'price': 'Preço',
           
        }

class TransactionForm(forms.ModelForm):
    transaction_date = forms.DateField(
        label="Data da Transação",
        initial=date.today,
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Transaction
        fields = ['client_name', 'amount', 'transaction_date']
        labels = {
            'client_name': 'Nome do Cliente',
            'amount': 'Valor',
           
        }