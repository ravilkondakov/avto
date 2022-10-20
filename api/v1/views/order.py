from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend

from api.v1.serializers.order import OrderSerializer, OrderCreateSerializer
from apps.orders.models import Order


class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.AllowAny,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['model_id',]


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = (permissions.AllowAny,)


# class ColorAmountView(generics.ListAPIView):
#     queryset = Order.objects.all()
#     serializer_class = ColorAmountSerializer
#     permission_classes = (permissions.AllowAny,)
