from django.db import models


class CashFlowModel(models.Model):
    name = models.CharField(max_length=100)
    repository_url = models.URLField()
    short_description = models.TextField()

    def __str__(self):
        return self.name
