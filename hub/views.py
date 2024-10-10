from django.shortcuts import render
from .models import CashFlowModel


def models_view(request):
    cashflow_models = CashFlowModel.objects.all()
    return render(request, 'models.html', {'cashflow_models': cashflow_models})


def runs_view(request):
    return render(request, 'runs.html')


def documentation_view(request):
    return render(request, 'documentation.html')
