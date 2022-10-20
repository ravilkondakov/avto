from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from api.v1.views.color import ColorViewSet, ColorAmountView
from api.v1.views.brand import CarBrandViewSet, CarBrandAmountViewSet
from api.v1.views.model import AvtoModelViewSet
from api.v1.views.order import OrderListView, OrderCreateView

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

"""DOCS"""
urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

router = DefaultRouter()
"""COLOR"""

router.register(r'color', ColorViewSet)
router.register(r'brand', CarBrandViewSet)
router.register(r'model', AvtoModelViewSet)

urlpatterns += [
    path('', include(router.urls)),
    path('orders/', OrderListView.as_view(),  name='orders_list_view'),
    path('create_order/', OrderCreateView.as_view(),  name='create_order_view'),
    path('color_amount/', ColorAmountView.as_view(),  name='color_amount_view'),
    path('brand_amount/', CarBrandAmountViewSet.as_view(),  name='color_amount_view'),

]
