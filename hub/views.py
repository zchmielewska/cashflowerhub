from django.shortcuts import render, redirect, get_object_or_404
from .models import CashFlowModel, Document, Run
from .forms import CashFlowModelForm


def model_view(request):
    cashflow_models = CashFlowModel.objects.all().order_by('-id')
    return render(request, 'model.html', {'cashflow_models': cashflow_models})


def run_view(request):
    runs = Run.objects.all().order_by('-id')
    return render(request, 'run.html', {'runs': runs})


def document_view(request):
    documents = Document.objects.all().order_by('-id')
    return render(request, 'document.html', {'documents': documents})


def model_add(request):
    if request.method == 'POST':
        form = CashFlowModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('model')
    else:
        form = CashFlowModelForm()
    return render(request, 'model_add.html', {'form': form})


def model_delete(request, model_id):
    model = get_object_or_404(CashFlowModel, pk=model_id)
    if request.method == 'POST':
        model.delete()
        return redirect('model')
    return render(request, 'model_delete.html', {'model': model})
