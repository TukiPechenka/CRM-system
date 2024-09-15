from django.db import models

from contracts.models import Contract
from leads.models import Lead


class Customer(models.Model):
    """
    Модель Клиента
    """

    lead = models.OneToOneField(
        Lead, on_delete=models.CASCADE, limit_choices_to={"is_customer": False}
    )
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super().save(force_insert, force_update, using, update_fields)
        self.lead.is_customer = True
        self.lead.save()  # pylint: disable=no-member

    def __str__(self):
        return (
            self.lead.last_name  # pylint: disable=no-member
            + " "
            + self.lead.first_name  # pylint: disable=no-member
        )
