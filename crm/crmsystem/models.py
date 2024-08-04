from datetime import date

from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    cost = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])


class Ad(models.Model):
    name = models.CharField(max_length=250)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    promotion_channel = models.CharField(max_length=250, name="promotionChannel")
    budget = models.PositiveIntegerField()

    profit = models.IntegerField(default=0)
    leads_count = models.PositiveIntegerField(default=0)
    customers_count = models.PositiveIntegerField(default=0)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.leads_count = Lead.objects.filter(ad=self, is_customer=False).count()
        self.customers_count = Customer.objects.filter(lead__ad=self).count()
        contracts_cost = Customer.objects.filter(lead__ad=self).aggregate(models.Sum('contract__cost'))['contract__cost__sum'] or 0
        self.profit = contracts_cost - self.budget
        super().save(force_insert, force_update, using, update_fields)

class Lead(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    email = models.EmailField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)

    is_customer = models.BooleanField(default=False)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        super().save(force_insert, force_update, using, update_fields)
        self.ad.save()


class Contract(models.Model):
    def upload_document(self, filename):
        extension = filename.split('.')[-1]
        if not self.pk:
            pk = Contract.objects.order_by('-id').first()
            self.pk = self.id = pk + 1 if pk else 1
        return 'documents/{pk}.{extension}'.format(
            pk=self.pk, extension=extension,
        )

    name = models.CharField(max_length=250)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    document = models.FileField(upload_to=upload_document)
    start_date = models.DateField()
    end_date = models.DateField()
    cost = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(0)])

    def clean(self):
        errors = {}
        if (self.end_date - self.start_date).total_seconds() < 0:
            errors['start_date'] = 'start date must be less than or equal to end date'
            errors['end_date'] = 'end date must be greate than or equal to start date'
        if (date.today() - self.start_date).total_seconds() < 0:
            errors['start_date'] = "start date must be greater than or equeal to today's day"
        if errors:
            raise ValidationError(errors)


class Customer(models.Model):
    lead = models.OneToOneField(Lead, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.lead.ad.save()
        self.lead.is_customer = True
        super().save(force_insert, force_update, using, update_fields)
