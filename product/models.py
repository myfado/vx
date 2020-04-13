from django.db import models
from django.urls import reverse


class Product(models.Model):
    PRODUCER = (
        ('TE', 'Treofan'),
        ('JE', 'Jindal Europe'),
        ('JI', 'Jindal India'),
        ('JA', 'Jindal America')
    )
    producer = models.CharField(max_length=2,choices=PRODUCER, default='JE')
    name = models.CharField(max_length=20, unique=True)
    GROUP = (
        ('NPD', 'NPD'),
        ('SPP', 'Specialty Packaging'),
        ('SPL', 'Specialty Labeling'),
        ('IML', 'IML'),
        ('COM', 'Commodity')
    )
    group = models.CharField(max_length=3,choices=GROUP, default='NPD')
    FAMILY = (
        ('UW', 'Uncoated White'),
        ('CW', 'Coated White'),
        ('UT', 'Uncoated Transparent'),
        ('CT', 'Coated transparent'),
        ('MT', 'Metallised'),
        ('ST', 'SealTough'),
        ('AL', 'Alox'),
        ('HD', 'EthyLyte')
    )
    family = models.CharField(max_length=2,choices=FAMILY, default='UW')
    link = models.URLField(blank=True)

    class Meta:
        db_table = 'product'
        ordering = ('name','family',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:product-detail', {'id':self.id})
