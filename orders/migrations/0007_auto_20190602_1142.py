# Generated by Django 2.0 on 2019-06-02 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_orders_order_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'ordering': ['-order_time']},
        ),
    ]
