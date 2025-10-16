from .reports.transactions_report import TransactionsReport
from .reports.sales_report import SalesReport

class ReportFactory:
    def create_report(self, report_type):
        if report_type == "transactions":
            return TransactionsReport()
        elif report_type == "sales":
            return SalesReport()
