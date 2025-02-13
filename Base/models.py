from django.db import models

# Create your models here.

# Starter
class Starter(models.Model):
    serial_number = models.PositiveIntegerField(editable=False, unique=True)
    items_name = models.CharField(max_length=500)
    sub_items_name = models.CharField(max_length=2000)
    half_price = models.FloatField(null=True, blank=True)
    full_price = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.serial_number = Starter.objects.count() + 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        serial_to_delete = self.serial_number
        super().delete(*args, **kwargs)
        
        for index, obj in enumerate(Starter.objects.order_by('serial_number'), start=1):
            obj.serial_number = index
            obj.save()

    def __str__(self):
        return self.items_name

# Shawarma


# Shawarma Plate


# Loaded Shawarma


# Combos for One


# Combos for Two


# Healthy Shawarma


# Only for Cheese Lovers


# Add-On