from rest_framework import serializers
from product.models import Collection, Product, ProductObjects, Cart


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
        exclude = ['bestseller', 'novelty']


class ProductsInCollectionSerializer(serializers.ModelSerializer):
    """Serializing Products in definite Collection"""

    product_objects = ProductObjectsSerializer(many=True)
    collection = CollectionsSerializer()

    class Meta:
        model = Product
        fields = ['collection', 'id', 'product_objects', 'title',
                  'actual_price', 'old_price', 'discount',
                  'size_line', 'favorite']


class ProductFavoriteSerializer(serializers.ModelSerializer):
    """Serializer for validation Like/Unlike the Poduct"""

    class Meta:
        model = Product
        fields = ['id', 'title', 'favorite']
        read_only_fields = ('id', 'collection', 'title', 'article',
                            'actual_price', 'old_price', 'discount',
                            'description', 'size_line', 'tissue_composition',
                            'quantity_in_line', 'material', 'bestseller',
                            'novelty')


class ProductsForCart(serializers.ModelSerializer):
    """Serializing Products in definite Collection"""

    class Meta:
        model = Product
        fields = ['id', 'title', 'size_line',
                  'actual_price', 'old_price']


class ProductsInCartSerializer(serializers.ModelSerializer):
    """Serializing Products in Cart"""
    product = ProductsForCart()

    class Meta:
        model = ProductObjects
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    """Serializing Products in Cart"""
    product = ProductsInCartSerializer()

    class Meta:
        model = Cart
        fields = ['id', 'product', 'quantity']


class CartUpdateSerializer(serializers.ModelSerializer):
    """Serializing Product in Cart"""
    product = ProductsInCartSerializer(read_only=True)
    quantity = serializers.IntegerField(min_value=1)

    class Meta:
        model = Cart
        fields = ['product', 'quantity']
        read_only_fields = ('id', 'product')
