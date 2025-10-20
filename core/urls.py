from django.urls import path
from .views import home, generate_report, sales_dashboard_view

urlpatterns = [
    path('', home, name='home'),
    path('report/<str:report_type>/', generate_report, name='generate_report'),   
]
