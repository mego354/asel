# Generated by Django 5.0.1 on 2024-01-30 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_order_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='store_orderitem',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
