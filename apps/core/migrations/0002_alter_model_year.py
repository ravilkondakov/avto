# Generated by Django 4.1.2 on 2022-10-19 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='year',
            field=models.DateField(),
        ),
    ]
