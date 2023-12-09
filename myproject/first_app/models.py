from django.db import models

# Create your models here.
from django.db import models

class Bill(models.Model):
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    tipPercentage = models.DecimalField(max_digits=5, decimal_places=2)