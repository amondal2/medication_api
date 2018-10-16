from django.db import models

# Create your models here.

class Medication(models.Model):
    name = models.CharField(
        max_length=155,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.name

