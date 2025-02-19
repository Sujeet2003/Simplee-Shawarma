from django.db import models
from Simplee.settings import logger

# Create your models here.

from django.db import models

# Base model to avoid repetition
logger.info("Creating databases for the given models...")
class BaseItem(models.Model):
    items_name = models.CharField(max_length=500)
    sub_items_name = models.CharField(max_length=2000)
    half_price = models.FloatField(null=True, blank=True)
    full_price = models.FloatField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.items_name

class Starter(BaseItem):
    pass

class Shawarma(BaseItem):
    pass

class ShawarmaPlate(BaseItem):
    pass

class LoadedShawarma(BaseItem):
    pass

class CombosForOne(BaseItem):
    pass

class CombosForTwo(BaseItem):
    pass

class HealthyShawarma(BaseItem):
    pass

class OnlyForCheeseLovers(BaseItem):
    pass

class AddOn(BaseItem):
    pass

logger.info('Databases created for the mentined models successfully.')