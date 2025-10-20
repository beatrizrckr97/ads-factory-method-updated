from .base_report import BaseReport
from core.models import Client
from django.db.models import Count
from django.db.models.functions import TruncMonth
import calendar

class ClientsReport(BaseReport):
    def generate(self):
        
        data = (
            Client.objects
            .annotate(month=TruncMonth('created_at'))  
            .values('month')
            .annotate(total_clients=Count('id'))
            .order_by('month')
        )

        labels = [calendar.month_name[d['month'].month] for d in data]
        values = [d['total_clients'] for d in data]

        return {'labels': labels, 'values': values}