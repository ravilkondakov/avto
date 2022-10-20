from django.db import models


class Color(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name='name'
    )
    color = models.ImageField(
        upload_to='images/color',
        max_length=100
    )

    @property
    def color_url(self):
        if self.color and hasattr(self.color, 'url'):
            return self.color.url

    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"

    def __str__(self):
        return self.name


class CarBrand(models.Model):
    brand = models.CharField(
        max_length=250,
        verbose_name='brand'
    )

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

    def __str__(self):
        return self.brand


class Model(models.Model):
    country = models.CharField(
        max_length=250,
        verbose_name='country'
    )
    model = models.CharField(
        max_length=250,
        verbose_name='model'
    )
    body = models.CharField(
        max_length=250,
        verbose_name='body'
    )

    engine_volume = models.CharField(
        max_length=250,
        verbose_name='engine_volume'
    )
    year = models.DateField()

    class Meta:
        verbose_name = "Model"
        verbose_name_plural = "Models"

    def __str__(self):
        return self.model
