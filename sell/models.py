from django.db import models
from product.models import Product
from customer.models import Customer
from django.db.models import Q

class Sell(models.Model):
    converter = models.ForeignKey(Customer, null=True, related_name="converter_sales",on_delete=models.SET_NULL, limit_choices_to=Q(status='C') | Q(status='D'))
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        db_table = 'sell'
        ordering = ('converter','-updated_at')
        verbose_name_plural = 'sales'
    def __str__(self):
        return str(self.converter)

class SellItem(models.Model):
    sell = models.ForeignKey(Sell, related_name="has_items",on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, related_name="product_sells",on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField(blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    enduser = models.ForeignKey(Customer, blank=True, null=True, related_name="enduser_sales",on_delete=models.SET_NULL, limit_choices_to={'status': 'E'},)
    description = models.CharField(max_length=50, blank=True)
    discontinued = models.BooleanField(default=False)

    class Meta:
        db_table = 'sellitem'
        ordering = ('-quantity',)
        verbose_name_plural = "SellItems"

    def __str__(self):
        return str(self.product)+ '  ' + ' discontinued ' + str(self.discontinued)
