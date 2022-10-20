from rest_framework import serializers

from apps.core.models import CarBrand


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = (
            'brand',
        )
