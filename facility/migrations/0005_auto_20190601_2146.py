# Generated by Django 2.0 on 2019-06-01 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('facility', '0004_auto_20190528_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baoxiu',
            name='baoxiu_staff_name',
        ),
        migrations.RemoveField(
            model_name='baoxiu',
            name='facility_id',
        ),
        migrations.AddField(
            model_name='repair',
            name='baoxiu_complementary',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='保修描述'),
        ),
        migrations.AddField(
            model_name='repair',
            name='baoxiu_place',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='详细地点'),
        ),
        migrations.AddField(
            model_name='repair',
            name='baoxiu_staff_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='aaa', to=settings.AUTH_USER_MODEL, verbose_name='报修人'),
        ),
        migrations.AddField(
            model_name='repair',
            name='baoxiu_time',
            field=models.DateField(auto_now=True, null=True, verbose_name='保修时间'),
        ),
        migrations.AlterField(
            model_name='repair',
            name='facility_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.Facility', verbose_name='设备'),
        ),
        migrations.AlterField(
            model_name='repair',
            name='repair_complementary',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='维修补充'),
        ),
        migrations.AlterField(
            model_name='repair',
            name='repair_staff_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='bbb', to=settings.AUTH_USER_MODEL, verbose_name='维修人'),
        ),
        migrations.AlterField(
            model_name='repair',
            name='repair_time',
            field=models.DateField(auto_now=True, null=True, verbose_name='维修时间'),
        ),
        migrations.DeleteModel(
            name='Baoxiu',
        ),
    ]
