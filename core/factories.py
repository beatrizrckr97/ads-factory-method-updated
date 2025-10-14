from .reports.transactions_report import TransactionsReport

class ReportFactory:
    def create_report(self, report_type):
        if report_type == "transactions":
            return TransactionsReport()
        else:
            raise ValueError("Tipo de relatório inválido")