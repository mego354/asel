# Generated by Django 5.0.1 on 2024-01-24 13:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_orderitem_profit'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-100), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='number',
            field=models.PositiveIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1000000001), django.core.validators.MaxValueValidator(1599999999)]),
        ),
    ]
