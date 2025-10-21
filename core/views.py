from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Sum, F, FloatField
from .factories import ReportFactory
from .forms import ClientForm, SaleForm, TransactionForm
from .models import Sale, Transaction
import calendar

# Página inicial
def home(request):
    return render(request, 'home.html')

# Geração de relatórios dinâmicos
def generate_report(request, report_type):
    factory = ReportFactory()
    report = factory.create_report(report_type)
    data = report.generate()

    total = sum(data['values']) if data['values'] else 0
    meses_registrados = len(data['labels']) if data['labels'] else 0
    media_mensal = total / meses_registrados if meses_registrados > 0 else 0

    total_key = 'total_clients' if report_type == "clients" else 'total_vendas'

    context = {
        'content': data,
        'report_type': report_type,
        'last_updated': timezone.now(),
        total_key: total,
        'meses_registrados': meses_registrados,
        'media_mensal': media_mensal,
        'zipped_data': list(zip(data['labels'], data['values'])),
    }

    template_name = f'{report_type}.html'
    return render(request, template_name, context)

# Dashboard de vendas
def sales_dashboard_view(request):
    ano_atual = timezone.now().year
    vendas_ano = Sale.objects.filter(date__year=ano_atual)

    meses = range(1, 13)
    labels = []
    values = []

    for mes in meses:
        total_mes = vendas_ano.filter(date__month=mes).aggregate(
            total=Sum(F('price') * F('quantity'), output_field=FloatField())
        )['total'] or 0
        labels.append(calendar.month_name[mes])
        values.append(float(total_mes))

    total_vendas = sum(values)
    meses_registrados = sum(1 for v in values if v > 0)
    media_mensal = total_vendas / meses_registrados if meses_registrados else 0
    zipped_data = zip(labels, values)

    context = {
        'content': {
            'labels': labels,
            'values': values
        },
        'total_vendas': total_vendas,
        'meses_registrados': meses_registrados,
        'media_mensal': media_mensal,
        'zipped_data': zipped_data,
        'last_updated': timezone.now()
    }

    return render(request, 'sales.html', context)


def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClientForm()
    return render(request, 'create_form.html', {'form': form, 'titulo': 'Cadastrar Cliente'})

def add_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SaleForm()
    return render(request, 'create_form.html', {'form': form, 'titulo': 'Cadastrar Venda'})

def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TransactionForm()
    return render(request, 'create_form.html', {'form': form, 'titulo': 'Cadastrar Transação'})
