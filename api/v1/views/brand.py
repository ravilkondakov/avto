from rest_framework import permissions, generics

from api.v1.serializers.brand import CarBrandSerializer
from apps.core.models import CarBrand
from rest_framework.viewsets import ModelViewSet

from api.v1.serializers.order import BrandAmountSerializer


class CarBrandViewSet(ModelViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = (permissions.AllowAny,)


class CarBrandAmountViewSet(generics.ListAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = BrandAmountSerializer
    permission_classes = (permissions.AllowAny,)
