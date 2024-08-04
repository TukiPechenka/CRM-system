from django.contrib import admin

from .models import Product, Ad, Lead, Contract, Customer


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name', 'description', 'cost'


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name', 'product', 'promotionChannel', 'budget', 'profit', 'leads_count', 'customers_count'
    readonly_fields = 'profit', 'leads_count', 'customers_count'


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = 'pk', 'first_name', 'last_name', 'phone', 'email', 'ad', 'is_customer'


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name', 'product', 'document', 'start_date', 'end_date', 'cost'


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = 'pk', 'lead', 'contract'



