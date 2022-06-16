from rest_framework import serializers
from .models import Products, ProductImages, ProductOptions


class ProductsSerializer(serializers.ModelSerializer):
    basic_price = serializers.IntegerField()
    image = serializers.CharField(source='image.image')
    image_caption = serializers.CharField(source='image.caption')
    image_sort_order = serializers.IntegerField(source='image.sort_order')
    option_name = serializers.CharField(source='option.option_name')
    option_value = serializers.CharField(source='option.value')
    option_price = serializers.IntegerField(source='option.price')
    option_sort_order = serializers.CharField(source='option.sort_order')
    class Meta:
        model = Products
        fields = ('id', 'name', 'description', 'basic_price', 'sort_order', 'basic_price', 'image', 'image_caption', 'image_sort_order', 'option_name', 'option_value', 'option_price', 'option_sort_order')


