from rest_framework import serializers
from product.models import Collection, Product, ProductObjects


class CollectionsSerializer(serializers.ModelSerializer):
    """Allow complex data of Collection model to be rendered into JSON."""

    class Meta:
        model = Collection
        fields = '__all__'


class ProductObjectsSerializer(serializers.ModelSerializer):
    """Allow complex data of Collection model to be rendered into JSON."""

    class Meta:
        model = ProductObjects
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    """Serializing Product objects into JSON content-type."""

    product_objects = ProductObjectsSerializer(many=True)
    collection = CollectionsSerializer()

    class Meta:
        model = Product
        fields = '__all__'
