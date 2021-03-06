# Generated by Django 4.0 on 2021-12-22 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuisine', '0022_alter_productstereotype_hierarchy'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productstereotype',
            options={'ordering': ['category', '-allergen', 'hierarchy']},
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='biotin',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='calcium',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='chloride',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='chromium',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='copper',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='fluoride',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='folic_acid',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='iodine',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='iron',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='magnesium',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='manganese',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='molybdenum',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='monounsaturated_fat',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='niacin',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='pantothenic_acid',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='phosphorus',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='polyol_carbohydrate',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='polyunsaturated_fat',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='potassium',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='riboflavin',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='saturated_fat',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='selenium',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='starch_carbohydrate',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='sugar_carbohydrate',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='thiamin',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='total_calories',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='total_carbohydrate',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='total_fat',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='total_fibre',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='total_protein',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='total_salt',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='vitamin_a',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='vitamin_b12',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='vitamin_b6',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='vitamin_c',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='vitamin_d',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='vitamin_e',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='vitamin_k',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='productstereotype',
            name='zinc',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='productstereotype',
            name='category',
            field=models.CharField(choices=[('F-VEG', 'Fresh fuits, vegetables and legumes'), ('DAIRY', 'Dairy and egg products'), ('F-MPF', 'Fresh meat, poultry and fish'), ('P-VEG', 'Preserved fuits, vegetables and legumes'), ('P-MPF', 'Preserved meat, poultry and fish'), ('GRAIN', 'Grains and Cerals'), ('NUTS', 'Nuts and Seeds'), ('INGNT', 'Ingredients'), ('SEASN', 'Herbs and Spices'), ('BREAD', 'Breads, Pastries and Pasta'), ('SAUCE', 'Sauces and Condiments'), ('EAT', 'Ready Meals'), ('SNACK', 'Snacks, Confections and Desserts'), ('DRINK', 'Drinks')], default='', max_length=6),
        ),
    ]
