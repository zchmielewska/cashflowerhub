from django import forms
from .models import CashFlowModel, Document


class CashFlowModelForm(forms.ModelForm):
    class Meta:
        model = CashFlowModel
        fields = '__all__'


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
