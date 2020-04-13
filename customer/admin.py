from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','country', 'status', 'category', 'issue']
    list_editable = ['category','issue',]
admin.site.register(Customer, CustomerAdmin)
