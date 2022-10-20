from rest_framework import permissions

from api.v1.serializers.model import ModelSerializer
from apps.core.models import Model
from rest_framework.viewsets import ModelViewSet


class AvtoModelViewSet(ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer
    permission_classes = (permissions.AllowAny,)
