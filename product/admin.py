from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'group', 'family', 'producer']
    list_editable = ['group', 'producer',]
    list_per_page = 10
admin.site.register(Product,ProductAdmin)
