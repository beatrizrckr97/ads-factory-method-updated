from core.models import Sale
from django.db.models import Sum, F, FloatField
import calendar
from django.utils import timezone

class SalesReport:
    def generate(self):
        ano_atual = timezone.now().year
        vendas_ano = Sale.objects.filter(date__year=ano_atual)

        labels = []
        values = []

        for mes in range(1, 13):
            total_mes = vendas_ano.filter(date__month=mes).aggregate(
                total=Sum(F('price') * F('quantity'), output_field=FloatField())
            )['total'] or 0
            labels.append(calendar.month_name[mes])
            values.append(float(total_mes))

        return {
            'labels': labels,
            'values': values
        }

