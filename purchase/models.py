from django.db import models
import datetime
from django.utils import timezone
from datetime import timedelta
from product.models import Product
from customer.models import Customer

def six_month_from_today():
    return timezone.now() + timedelta(weeks=25)

class Purchase(models.Model):
    application = models.CharField(max_length=50, blank=True)
    front_partner = models.ForeignKey(Customer, null=True, related_name="front_partner_projects",on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, related_name="product_projects",on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(default=20)
    back_partner = models.ForeignKey(Customer, null=True, related_name="back_partner_projects",on_delete=models.SET_NULL)
    structure = models.CharField(max_length=50, blank=True)
    replacing = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    deadline = models.DateField(default=six_month_from_today)
    discontinued = models.BooleanField(default=False)
    RND = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = 'purchase'
        ordering = ('front_partner','-quantity', 'product')
        verbose_name_plural = 'purchases'
    def __str__(self):
        return str(self.front_partner)

class Stage(models.Model):
    name = models.CharField(max_length=30,unique=True,default='FOC ordered')

    class Meta:
        db_table = 'stage'
    def __str__(self):
        return str(self.name)

class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, related_name="what_is_going",on_delete=models.CASCADE)
    stage = models.ForeignKey(Stage, related_name="projs_on_stage", on_delete=models.SET_NULL, null=True)
    comment = models.CharField(max_length=50, blank=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'purchaseitem'
        ordering = ('stage',)
        verbose_name_plural = "PurchaseItems"

    def __str__(self):
        return str(self.purchase)+ '  ' +  str(self.stage)
