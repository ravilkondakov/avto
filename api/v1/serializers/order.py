from rest_framework import serializers

from api.v1.serializers.brand import CarBrandSerializer
from api.v1.serializers.color import ColorSerializer
from api.v1.serializers.model import ModelSerializer

from apps.orders.models import Order
from apps.core.models import Color
from apps.core.models import CarBrand


class OrderSerializer(serializers.ModelSerializer):
    color_id = ColorSerializer()
    brand_id = CarBrandSerializer()
    model_id = ModelSerializer()

    class Meta:
        model = Order
        fields = (
            'date', 'color_id', 'brand_id',
            'model_id', 'amount',
        )


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'date', 'color_id', 'brand_id',
            'model_id', 'amount',
        )


class OrderAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('amount',)


class ColorAmountSerializer(serializers.ModelSerializer):
    amount = serializers.SerializerMethodField()

    class Meta:
        model = Color
        fields = (
            'name', 'amount',
        )

    def get_amount(self, obj):
        queryset = Order.objects.filter(color_id__name=obj).all()
        return OrderAmountSerializer(queryset, many=True).data


class BrandAmountSerializer(serializers.ModelSerializer):
    amount = serializers.SerializerMethodField()

    class Meta:
        model = CarBrand
        fields = (
            'brand', 'amount',
        )

    def get_amount(self, obj):
        queryset = Order.objects.filter(brand_id__brand=obj).all()
        return OrderAmountSerializer(queryset, many=True).data
