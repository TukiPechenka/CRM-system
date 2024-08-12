from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from products.models import Product


class Contract(models.Model):
    """
    Модель Контракта
    """

    def upload_document(self, filename):
        """
        Определение пути для файла документа по id Контракта
        """
        extension = filename.split(".")[-1]
        pk = self.pk - 1 if self.pk is not None else self.pk
        if not pk:
            obj = Contract.objects.order_by("-id").first()
            pk = obj.id if obj is not None else 0
        return f"documents/{pk + 1}.{extension}"

    name = models.CharField(max_length=250)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    document = models.FileField(upload_to=upload_document)
    start_date = models.DateField()
    end_date = models.DateField()
    cost = models.DecimalField(
        decimal_places=2, max_digits=12, validators=[MinValueValidator(0)]
    )

    def clean(self):
        errors = {}
        if (self.end_date - self.start_date).total_seconds() < 0:
            errors["start_date"] = "start date must be less than or equal to end date"
            errors["end_date"] = "end date must be greate than or equal to start date"
        if (date.today() - self.start_date).total_seconds() < 0:
            errors["start_date"] = (
                "start date must be greater than or equeal to today's day"
            )
        if errors:
            raise ValidationError(errors)

    def __str__(self):
        return self.name + " - " + self.product.name
