# Generated by Django 5.0 on 2024-01-09 19:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0002_remove_truck_brand_remove_truck_city_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='sell_truck',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sell_truck', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
