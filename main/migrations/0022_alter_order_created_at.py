# Generated by Django 5.0.1 on 2024-01-30 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_store_orderitem_change_gomla_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]