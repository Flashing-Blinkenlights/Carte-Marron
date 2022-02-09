# Generated by Django 4.0 on 2021-12-22 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuisine', '0004_alter_productstereotype_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_name',
        ),
        migrations.RemoveField(
            model_name='vessel',
            name='vessel_name',
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vessel',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='productstereotype',
            name='category',
            field=models.CharField(choices=[('F-VEG', 'Fresh fuits, vegetables and legumes'), ('DAIRY', 'Dairy Products'), ('F-FSH', 'Fresh animal products'), ('P-VEG', 'Preserved fuits, vegetables and legumes'), ('P-FSH', 'Preserved animal products'), ('GRAIN', 'Grains and Cerals'), ('NUTS', 'Nuts and Seeds'), ('INGNT', 'Ingredients'), ('SEASN', 'Herbs and Spices'), ('EAT', 'Ready Meals'), ('BREAD', 'Breads, Pastries and Pasta'), ('SAUCE', 'Sauces and Condiments'), ('SNACK', 'Snacks, Confections and Desserts'), ('DRINK', 'Drinks')], default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='productstereotype',
            name='name',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='vessel',
            name='heat_resistance',
            field=models.CharField(choices=[(1, 'Heatproof'), (2, 'Ovenproof'), (3, 'Flameproof')], default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='vessel',
            name='shape',
            field=models.CharField(blank=True, choices=[('RECT', 'Square or rectangular'), ('CIRC', 'Circular'), ('OVAL', 'Oval or elliptical'), ('SPEC', 'Decorative mould')], default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='vessel',
            name='size',
            field=models.CharField(choices=[('S', 'small'), ('M', 'medium'), ('L', 'large')], default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='vessel',
            name='type',
            field=models.CharField(blank=True, choices=[('STOR', 'Storage container or tupperware'), ('MEAS', 'Measuring jug'), ('SAUC', 'Saucepan or pot'), ('FRY', 'Frying pan, grill pan or wok'), ('DISH', 'Casserole or oven pan'), ('BAKE', 'Baking tray, oven pan or springform'), ('BOWL', 'Mixing bowls')], default='', max_length=4),
        ),
    ]
