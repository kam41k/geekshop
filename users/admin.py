from django.contrib import admin
from users.models import User
from basket.admin import BasketAdminInline


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (BasketAdminInline,)
    list_display = ('first_name', 'last_name', 'username', 'email', 'city')
    fields = ('image', 'first_name', 'last_name', 'username', 'email', 'city')
    search_fields = ('username',)
    ordering = ('username',)