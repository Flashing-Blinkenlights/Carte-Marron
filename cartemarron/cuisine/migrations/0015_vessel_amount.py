# Generated by Django 4.0 on 2021-12-22 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuisine', '0014_alter_vessel_heat_resistance_alter_vessel_shape_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vessel',
            name='amount',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3),
        ),
    ]
