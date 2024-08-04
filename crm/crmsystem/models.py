from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    cost = models.DecimalField(max_digits=12, decimal_places=2)


class Ad(models.Model):
    name = models.CharField(max_length=250)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    promotion_channel = models.CharField(max_length=250, name='promotionChannel')
    budget = models.PositiveIntegerField()


class Lead(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    email = models.EmailField()


def upload_document(instance: 'Contract', filename):
    extension = filename.split('.')[-1]
    return "documents/{pk}.{extension}".format(
        pk=instance.pk, extension=extension
    )


class Contract(models.Model):
    name = models.CharField(max_length=250)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    document = models.FileField(upload_to=upload_document)
    start_date = models.DateField()
    end_date = models.DateField()
    cost = models.DecimalField(decimal_places=2, max_digits=12)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        print(dir(self.end_date - self.start_date))
        super().save(force_insert, force_update, using, update_fields)


class Customer(models.Model):
    lead = models.OneToOneField(Lead, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
