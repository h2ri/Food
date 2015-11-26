from django.contrib import admin

from .models import Items
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name','item_image','item_price','item_description','item_quantity')

admin.site.register(Items, ItemAdmin)