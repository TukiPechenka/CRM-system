from django.db import models

from customers.models import Customer
from leads.models import Lead
from products.models import Product


class Advertisement(models.Model):
    """
    Модель Рекламной компании
    """

    name = models.CharField(max_length=250)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    promotion_channel = models.CharField(max_length=250, name="promotionChannel")
    budget = models.PositiveIntegerField()

    profit = models.IntegerField(default=0)
    leads_count = models.PositiveIntegerField(default=0)
    customers_count = models.PositiveIntegerField(default=0)

    class Meta:  # pylint: disable=too-few-public-methods
        """
        Мета информация о модели Рекламной компании.
        (Дополнительные параметры)
        """

        permissions = (("view_statistics", "Can view ads statistics"),)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.pk:
            self.leads_count = Lead.objects.filter(  # pylint: disable=no-member
                ad=self, is_customer=False
            ).count()
            self.customers_count = Customer.objects.filter(  # pylint: disable=no-member
                lead__ad=self
            ).count()
            contracts_cost = (
                Customer.objects.filter(  # pylint: disable=no-member
                    lead__ad=self
                ).aggregate(models.Sum("contract__cost"))["contract__cost__sum"]
                or 0
            )
            self.profit = contracts_cost - self.budget
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.name + " - " + self.product.name
