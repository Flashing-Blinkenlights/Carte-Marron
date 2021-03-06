# Generated by Django 4.0 on 2021-12-22 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuisine', '0005_remove_product_product_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='biography',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='profile',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='purchase_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='comment',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='method',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='vessel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
