from rest_framework import serializers

from apps.core.models import Model


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = (
            'country', 'model', 'body',
            'engine_volume', 'year',
        )
