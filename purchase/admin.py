from django.contrib import admin

from .models import Stage, Purchase, PurchaseItem

class StageAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Stage,StageAdmin)

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['application','front_partner','product','quantity','back_partner','structure','replacing','price','deadline','discontinued','RND','completed']
    list_per_page = 10
admin.site.register(Purchase,PurchaseAdmin)

class PurchaseItemAdmin(admin.ModelAdmin):
    list_display = ['purchase','stage','comment']
    list_per_page = 10
admin.site.register(PurchaseItem,PurchaseItemAdmin)
