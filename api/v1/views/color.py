from rest_framework import generics, permissions

from api.v1.serializers.color import ColorSerializer
from apps.core.models import Color
from rest_framework.viewsets import ModelViewSet

from api.v1.serializers.order import ColorAmountSerializer


class ColorViewSet(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = (permissions.AllowAny,)


class ColorAmountView(generics.ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorAmountSerializer
