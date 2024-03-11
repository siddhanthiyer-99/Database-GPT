from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import po_line, product, purchase_order, supplier, supplies

@admin.register(supplier)
class AdminSupplier(admin.ModelAdmin):
    list_display = ('supnr', 'supname', 'supaddress', 'supcity', 'supstatus')

@admin.register(po_line)
class AdminPoLine(admin.ModelAdmin):
    list_display = ('id', 'ponr', 'prodnr', 'quantity')

@admin.register(product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('prodnr', 'prodname', 'prodtype', 'available_quantity')

@admin.register(purchase_order)
class AdminPurchaseOrder(admin.ModelAdmin):
    list_display = ('ponr', 'podate', 'supnr')

@admin.register(supplies)
class AdminSupplies(admin.ModelAdmin):
    list_display = ('id', 'supnr', 'purchase_price', 'deliv_period')

# admin.site.register(po_line)
# admin.site.register(product)
# admin.site.register(purchase_order)
# admin.site.register(supplier)
# admin.site.register(supplies)