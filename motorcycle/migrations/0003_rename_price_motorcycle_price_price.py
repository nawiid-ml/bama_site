# Generated by Django 5.0 on 2024-01-02 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('motorcycle', '0002_remove_motorcycle_brand_remove_motorcycle_city_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='motorcycle_price',
            old_name='Price',
            new_name='price',
        ),
    ]