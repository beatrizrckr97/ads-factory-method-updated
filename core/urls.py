from django.urls import path
from .views import (
    home,
    generate_report,
    sales_dashboard_view,
    add_client,
    add_sale,
    add_transaction,
)

urlpatterns = [
    path('', home, name='home'),
    path('report/<str:report_type>/', generate_report, name='generate_report'),
    

    # Formulários
    path('add-client/', add_client, name='add_client'),
    path('add-sale/', add_sale, name='add_sale'),
    path('add-transaction/', add_transaction, name='add_transaction'),
]