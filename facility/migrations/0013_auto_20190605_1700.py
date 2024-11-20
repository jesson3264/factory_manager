# Generated by Django 2.0 on 2019-06-05 09:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0012_auto_20190602_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='购买人'),
        ),
        migrations.AlterField(
            model_name='maintain',
            name='staff_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='保养员'),
        ),
    ]
