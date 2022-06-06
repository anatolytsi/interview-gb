from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
from django.db import models
from django.db.models import Manager
from django.utils.translation import gettext_lazy as _


class ProductCategory(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False, verbose_name=_('название'))
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    objects = Manager()
    on_site = CurrentSiteManager('site')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False, verbose_name=_('название'))
    delivery_date = models.DateField(verbose_name=_('дата поставки'))
    price = models.PositiveIntegerField(verbose_name=_('цена'))
    units = models.CharField(max_length=5, blank=False, verbose_name=_('единица измерения'))
    provider = models.CharField(max_length=50, verbose_name=_('поставщик'))
    categories = models.ManyToManyField(ProductCategory, related_name='product_categories', blank=True, default=None)
    site = models.ManyToManyField(Site, related_name='product_site', null=True)
    objects = Manager()
    on_site = CurrentSiteManager('site')

    def __str__(self):
        return self.name
