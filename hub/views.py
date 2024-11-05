from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy

from .models import CashFlowModel, Document, Run
from .forms import CashFlowModelForm, DocumentForm


class ModelListView(ListView):
    model = CashFlowModel
    template_name = 'model_list.html'
    context_object_name = 'models'
    ordering = ['-id']


class ModelDetailView(DetailView):
    model = CashFlowModel
    template_name = 'model_detail.html'
    context_object_name = 'model'


class ModelCreateView(CreateView):
    model = CashFlowModel
    form_class = CashFlowModelForm
    template_name = 'model_add.html'
    success_url = reverse_lazy('model_list')


class ModelUpdateView(UpdateView):
    model = CashFlowModel
    form_class = CashFlowModelForm
    template_name = 'model_edit.html'
    success_url = reverse_lazy('model_list')


class ModelDeleteView(DeleteView):
    model = CashFlowModel
    template_name = 'model_delete.html'
    success_url = reverse_lazy('model_list')


def run_view(request):
    runs = Run.objects.all().order_by('-id')
    return render(request, 'run.html', {'runs': runs})


class DocumentListView(ListView):
    model = Document
    template_name = 'document_list.html'
    context_object_name = 'documents'


class DocumentCreateView(CreateView):
    model = Document
    form_class = DocumentForm
    template_name = 'document_add.html'
    success_url = reverse_lazy('document_list')


class DocumentDetailView(DetailView):
    model = Document
    template_name = 'document_detail.html'
    context_object_name = 'document'


class DocumentUpdateView(UpdateView):
    model = Document
    template_name = 'document_edit.html'
    fields = ['name', 'file', 'cash_flow_models']
    success_url = reverse_lazy('document_list')


class DocumentDeleteView(DeleteView):
    model = Document
    template_name = 'document_delete.html'
    success_url = reverse_lazy('document_list')
