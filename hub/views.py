from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy

from .models import CashFlowModel, Document, Run
from .forms import CashFlowModelForm, DocumentForm


def model_view(request):
    cashflow_models = CashFlowModel.objects.all().order_by('-id')
    return render(request, 'model.html', {'cashflow_models': cashflow_models})


class ModelDetailView(DetailView):
    model = CashFlowModel
    template_name = 'model_detail.html'
    context_object_name = 'model'


def model_add(request):
    if request.method == 'POST':
        form = CashFlowModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('model')
    else:
        form = CashFlowModelForm()
    return render(request, 'model_add.html', {'form': form})


def model_edit(request, model_id):
    model = get_object_or_404(CashFlowModel, pk=model_id)
    if request.method == 'POST':
        form = CashFlowModelForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
            return redirect('model')
    else:
        form = CashFlowModelForm(instance=model)

    return render(request, 'model_edit.html', {'form': form, 'model': model})


def model_delete(request, model_id):
    model = get_object_or_404(CashFlowModel, pk=model_id)
    if request.method == 'POST':
        model.delete()
        return redirect('model')
    return render(request, 'model_delete.html', {'model': model})


def run_view(request):
    runs = Run.objects.all().order_by('-id')
    return render(request, 'run.html', {'runs': runs})


def document_view(request):
    documents = Document.objects.all().order_by('-id')
    return render(request, 'document.html', {'documents': documents})


def document_add(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('document')
    else:
        form = DocumentForm()
    return render(request, 'document_add.html', {'form': form})


class DocumentDetailView(DetailView):
    model = Document
    template_name = 'document_detail.html'
    context_object_name = 'document'


class DocumentEditView(UpdateView):
    model = Document
    template_name = 'document_edit.html'
    fields = ['name', 'file', 'cash_flow_models']
    success_url = reverse_lazy('document')


class DocumentDeleteView(DeleteView):
    model = Document
    template_name = 'document_delete.html'
    success_url = reverse_lazy('document')

# You also need a ListView for a list of documents
class DocumentListView(ListView):
    model = Document
    template_name = 'document_list.html'
    context_object_name = 'documents'