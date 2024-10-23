from django import forms
from .models import CashFlowModel


class CashFlowModelForm(forms.ModelForm):
    class Meta:
        model = CashFlowModel
        fields = '__all__'
