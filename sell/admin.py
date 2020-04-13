from django.contrib import admin
from .models import *

class SellAdmin(admin.ModelAdmin):
    list_display = ['converter']
    list_per_page = 10
admin.site.register(Sell,SellAdmin)

class SellItemAdmin(admin.ModelAdmin):
    list_display = ['sell','product','quantity','enduser','description','discontinued']
    list_per_page = 10
admin.site.register(SellItem,SellItemAdmin)
