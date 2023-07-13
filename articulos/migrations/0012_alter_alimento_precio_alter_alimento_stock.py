# Generated by Django 4.2.1 on 2023-07-12 05:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0011_alter_alimento_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimento',
            name='precio',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='alimento',
            name='stock',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Stock'),
        ),
    ]
