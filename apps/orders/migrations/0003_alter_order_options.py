# Generated by Django 4.1.2 on 2022-10-20 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_rename_model_order_model_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('amount',), 'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
    ]