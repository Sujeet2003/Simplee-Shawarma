from django.contrib import admin
from Base.models import Starter, Shawarma, ShawarmaPlate, LoadedShawarma, CombosForOne, CombosForTwo, HealthyShawarma, OnlyForCheeseLovers, AddOn

# Define a custom admin form with a dropdown
class ItemAdmin(admin.ModelAdmin):
    list_display = ('items_name', 'sub_items_name', 'half_price', 'full_price')
    list_filter = ('items_name',)
    search_fields = ('items_name', 'sub_items_name')

# Register all models with the custom admin form
admin.site.register(Starter, ItemAdmin)
admin.site.register(Shawarma, ItemAdmin)
admin.site.register(ShawarmaPlate, ItemAdmin)
admin.site.register(LoadedShawarma, ItemAdmin)
admin.site.register(CombosForOne, ItemAdmin)
admin.site.register(CombosForTwo, ItemAdmin)
admin.site.register(HealthyShawarma, ItemAdmin)
admin.site.register(OnlyForCheeseLovers, ItemAdmin)
admin.site.register(AddOn, ItemAdmin)