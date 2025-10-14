from django.shortcuts import render
from .factories import ReportFactory

def home(request):
    return render(request, 'home.html')

def generate_report(request, report_type):
    factory = ReportFactory()
    report = factory.create_report(report_type)
    data = report.generate()

    template_name = f'{report_type}.html'

    return render(request, template_name, {'content': data, 'report_type': report_type})

