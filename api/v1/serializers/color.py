from rest_framework import serializers

from apps.core.models import Color


class ColorSerializer(serializers.ModelSerializer):
    color_url = serializers.ImageField(
        use_url=True,
        source='color',
    )

    class Meta:
        model = Color
        fields = (
            'name', 'color_url',
        )

