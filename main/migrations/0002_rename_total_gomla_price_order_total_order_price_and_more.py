# Generated by Django 5.0.1 on 2024-01-03 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_gomla_price',
            new_name='total_order_price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_market_price',
        ),
        migrations.AddField(
            model_name='order',
            name='is_gomla',
            field=models.BooleanField(default=False),
        ),
    ]
