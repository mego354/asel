# Generated by Django 5.0.1 on 2024-01-24 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='profit',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
