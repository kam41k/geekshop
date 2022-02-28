from django.contrib import admin
from basket.models import Basket


# Register your models here.
class BasketAdminInline(admin.TabularInline):
    model = Basket
    fields = readonly_fields = ('product', 'quantity', 'created_timestamp')
    extra = 0
