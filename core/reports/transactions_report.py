from .base_report import BaseReport
from core.models import Transaction
from django.db.models.functions import TruncMonth
from django.db.models import Sum
import calendar

class TransactionsReport(BaseReport):
    def generate(self):
        # Agrupa por mês e soma os valores
        data = (
            Transaction.objects
            .annotate(month=TruncMonth('transaction_date'))
            .values('month')
            .annotate(total_amount=Sum('amount'))
            .order_by('month')
        )

        labels = [calendar.month_name[d['month'].month] for d in data]
        values = [float(d['total_amount']) for d in data]

        return {'labels': labels, 'values': values}