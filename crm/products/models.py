from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    """
    Модель Услуги
    """

    name = models.CharField(max_length=250)
    description = models.TextField()
    cost = models.DecimalField(
        max_digits=12, decimal_places=2, validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return str(self.name)
