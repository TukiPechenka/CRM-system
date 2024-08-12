from django.db import models


class Lead(models.Model):
    """
    Модель Потенциального Клиента
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    email = models.EmailField()
    ad = models.ForeignKey("advertisements.Advertisement", on_delete=models.CASCADE)

    is_customer = models.BooleanField(default=False)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super().save(force_insert, force_update, using, update_fields)
        self.ad.save()

    def __str__(self):
        return self.last_name + " " + self.first_name
