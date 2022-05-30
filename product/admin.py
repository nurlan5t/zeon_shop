from django.contrib import admin
from product.models import Collection


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    """Representation of a model 'Collection' in the admin interface."""
    list_display = ('title',)
