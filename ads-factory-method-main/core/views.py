from django.shortcuts import render
from django.utils import timezone
from django.db.models import Sum, F, FloatField
from .factories import ReportFactory
from .models import Sale  # certifique-se de que o modelo Sale existe
import calendar

def home(request):
    return render(request, 'home.html')


def generate_report(request, report_type):
    factory = ReportFactory()
    report = factory.create_report(report_type)
    data = report.generate()

    total_vendas = sum(data['values']) if data['values'] else 0
    meses_registrados = len(data['labels']) if data['labels'] else 0
    media_mensal = total_vendas / meses_registrados if meses_registrados > 0 else 0

    context = {
        'content': data,
        'report_type': report_type,
        'last_updated': timezone.now(),
        'total_vendas': total_vendas,
        'meses_registrados': meses_registrados,
        'media_mensal': media_mensal,
        'zipped_data': list(zip(data['labels'], data['values'])),
    }

    template_name = f'{report_type}.html'
    return render(request, template_name, context)


def sales_dashboard_view(request):
    # Pega todas as vendas do ano atual
    ano_atual = timezone.now().year
    vendas_ano = Sale.objects.filter(date__year=ano_atual)

    # Agrupa por mês e soma o total de cada mês
    meses = range(1, 13)
    labels = []
    values = []

    for mes in meses:
        total_mes = vendas_ano.filter(date__month=mes).aggregate(
            total=Sum(F('price') * F('quantity'), output_field=FloatField())
        )['total'] or 0
        labels.append(calendar.month_name[mes])  # Nome do mês
        values.append(float(total_mes))

    # Estatísticas
    total_vendas = sum(values)
    meses_registrados = sum(1 for v in values if v > 0)
    media_mensal = total_vendas / meses_registrados if meses_registrados else 0

    # Zip para tabela
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

    return render(request, 'sales_dashboard.html', context)
