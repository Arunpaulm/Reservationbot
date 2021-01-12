from django.db import models


class Document(models.Model):
    invalid_trigger = models.CharField(max_length=20)
    key = models.CharField(max_length=11)
    name = models.CharField(max_length=10)
    reuse = models.BooleanField(default=False)
    support_multiple = models.BooleanField(default=False)
    pick_first = models.BooleanField(default=False)
    validation_parser = models.CharField(max_length=30)
