# Generated by Django 3.0.8 on 2020-10-18 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_auto_20201017_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='sd_volume_max',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Максимальный объем встраиваемой памяти'),
        ),
    ]