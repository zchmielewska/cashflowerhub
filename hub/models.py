from django.core.validators import FileExtensionValidator
from django.db import models


class CashFlowModel(models.Model):
    name = models.CharField(max_length=100)
    repository_url = models.URLField()
    short_description = models.TextField()

    def __str__(self):
        return self.name


class Run(models.Model):
    cash_flow_model = models.ForeignKey(CashFlowModel, on_delete=models.CASCADE)
    version = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('running', 'Running'),
        ('error', 'Error'),
        ('completed', 'Completed'),
    ))

    def __str__(self):
        return f"{self.cash_flow_model.name} - Version: {self.version}, Status: {self.status}"


class Document(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='documents/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    cash_flow_models = models.ManyToManyField(CashFlowModel, blank=True)

    def __str__(self):
        return self.name
