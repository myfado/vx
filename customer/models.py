from django.db import models
from django.urls import reverse

class Customer(models.Model):
    name = models.CharField(max_length=20)
    STATUS = (
        ('C', 'Converter'),
        ('E', 'Enduser'),
        ('D', 'Distributor'),
        ('A', 'Agent')
        )
    status = models.CharField(max_length=1,choices=STATUS,default='C')
    country = models.CharField(max_length=2,default='HR')
    CATEGORY = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4)
        )
    category = models.PositiveSmallIntegerField(choices=CATEGORY,default=2)
    issue = models.CharField(max_length=50, blank=True)


    class Meta:
        db_table = 'customer'
        ordering = ('country','name','status','category','issue')

    def __str__(self):
        return self.name
