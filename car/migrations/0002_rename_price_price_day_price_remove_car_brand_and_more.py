# Generated by Django 5.0 on 2024-01-02 19:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price_day',
            old_name='Price',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='car',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='car',
            name='city',
        ),
        migrations.AlterField(
            model_name='car',
            name='search',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.sell_car'),
        ),
    ]
