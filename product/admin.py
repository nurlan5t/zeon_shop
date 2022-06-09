from django.contrib import admin
from product.models import Collection, ProductObjects, Product, Cart, Order


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    """Representation of a model 'Collection' in the admin interface."""
    list_display = ('title',)


class ProductObjectsAdmin(admin.StackedInline):
    """Allow to admin add images and colors for product (maximum 8)."""
    model = ProductObjects
    max_num = 8


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Representation of a model 'Product' in the admin interface."""
    inlines = [ProductObjectsAdmin]
    list_display = ('title', 'article', 'size_line', 'quantity_in_line',
                    'collection')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('status', 'created', 'discount', 'total_price', 'actual_price')


admin.site.register(ProductObjects)
