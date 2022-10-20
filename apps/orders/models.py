from django.db import models

from apps.core.models import Color, CarBrand, Model


class Order(models.Model):
    color_id = models.ForeignKey(
        to=Color,
        on_delete=models.CASCADE,
        related_name='colors'
    )
    brand_id = models.ForeignKey(
        to=CarBrand,
        on_delete=models.CASCADE,
        related_name='brands'
    )
    model_id = models.ForeignKey(
        to=Model,
        on_delete=models.CASCADE,
        related_name='models'
    )
    amount = models.IntegerField()
    date = models.DateTimeField(
        auto_now_add=True,

    )

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ('amount', )
