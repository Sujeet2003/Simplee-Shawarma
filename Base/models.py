from django.db import models

# Create your models here.

from django.db import models

# Base model to avoid repetition
class BaseItem(models.Model):
    items_name = models.CharField(max_length=500)
    sub_items_name = models.CharField(max_length=2000)
    half_price = models.FloatField(null=True, blank=True)
    full_price = models.FloatField(null=True, blank=True)

    class Meta:
        abstract = True  # This prevents Django from creating a table for BaseItem

    def __str__(self):
        return self.items_name

# Categories inheriting from BaseItem
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