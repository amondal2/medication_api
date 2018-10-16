from django.db import models
from medications.models import Medication

class Patient(models.Model):
    name = models.CharField(
        max_length=155,
        null=False,
        blank=False
    )
    age = models.IntegerField(
        default=1,
        null=True,
        blank=True
    )

    medications = models.ManyToManyField(
        Medication
    )

    def __str__(self):
        return self.name
