"""Defines the app models."""

from django import forms
from django.db import models

NUTRIENTS = (
    'total_calories',
    'total_fat',
    'saturated_fat',
    'monounsaturated_fat',
    'polyunsaturated_fat',
    'total_carbohydrate',
    'sugar_carbohydrate',
    'polyol_carbohydrate',
    'starch_carbohydrate',
    'total_fibre',
    'total_salt',
    'total_protein',
    'vitamin_a',
    'vitamin_d',
    'vitamin_e',
    'vitamin_k',
    'vitamin_c',
    'thiamin',
    'riboflavin',
    'niacin',
    'vitamin_b6',
    'folic_acid',
    'vitamin_b12',
    'biotin',
    'pantothenic_acid',
    'potassium',
    'chloride',
    'calcium',
    'phosphorus',
    'magnesium',
    'iron',
    'zinc',
    'copper',
    'manganese',
    'fluoride',
    'selenium',
    'chromium',
    'molybdenum',
    'iodine',
)


# General
class Tag(models.Model):
    """Define a tag."""

    tag = models.CharField(max_length=10, default='')
    favorite = models.BooleanField(default=False)
    product_tag = models.BooleanField(default=True)
    recipe_tag = models.BooleanField(default=True)

    def __str__(self):
        """Return tag as string."""
        return f"{'🖤 ' if self.favorite else ''}{self.tag}"

    class Meta:
        """Defines metadata options."""

        ordering = ['-favorite', 'tag']

# Products


class Brand(models.Model):
    """Define a brand and its addresses."""

    brand = models.CharField(max_length=30, default='')
    favorite = models.BooleanField(default=False)
    partner = models.BooleanField(default=False)
    website = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        """Return brand as string."""
        return f"{'🖤 ' if self.favorite else ''}{self.brand}" \
            f"{' ✓' if self.partner else ''}"

    class Meta:
        """Defines metadata options."""

        ordering = ['-favorite', '-partner', 'brand']


class ProductStereotype(models.Model):
    """Define a product stereotype which may be used as an ingredient."""

    # Constants in ProductStereotype class
    FRESH_FRUIT_OR_VEG = 'F-VEG'
    DAIRY_OR_EGG = 'DAIRY'
    PRESERVED_FRUIT_OR_VEG = 'P-VEG'
    FRESH_MEAT_POULTRY_OR_FISH = 'F-MPF'
    PRESERVED_MEAT_POULTRY_OR_FISH = 'P-MPF'
    GRAIN_OR_CEREAL = 'GRAIN'
    NUT_OR_SEED = 'NUTS'
    INGREDIENT = 'INGNT'
    SEASONING = 'SEASN'
    BREAD_OR_PASTRY = 'BREAD'
    SAUCE = 'SAUCE'
    READY_TO_EAT = 'EAT'
    SNACK_OR_SWEET = 'SNACK'
    READY_TO_DRINK = 'DRINK'
    PRODUCT_CATEGORY_CHOICES = (
        # Fresh
        (FRESH_FRUIT_OR_VEG, 'Fresh fuits, vegetables and legumes'),
        (DAIRY_OR_EGG, 'Dairy and egg products'),
        (FRESH_MEAT_POULTRY_OR_FISH, 'Fresh meat, poultry and fish'),
        # Semi-/Non-Perishable
        (PRESERVED_FRUIT_OR_VEG, 'Preserved fuits, vegetables and legumes'),
        (PRESERVED_MEAT_POULTRY_OR_FISH, 'Preserved meat, poultry and fish'),
        (GRAIN_OR_CEREAL, 'Grains and Cerals'),
        (NUT_OR_SEED, 'Nuts and Seeds'),
        # Inedible
        (INGREDIENT, 'Ingredients'),
        (SEASONING, 'Herbs and Spices'),
        # Finished
        (BREAD_OR_PASTRY, 'Breads, Pastries and Pasta'),
        (SAUCE, 'Sauces and Condiments'),
        # Quick bites
        (READY_TO_EAT, 'Ready Meals'),
        (SNACK_OR_SWEET, 'Snacks, Confections and Desserts'),
        (READY_TO_DRINK, 'Drinks'),
    )

    name = models.CharField(max_length=20, default='')
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True)
    category = models.CharField(
        max_length=6, choices=PRODUCT_CATEGORY_CHOICES, default='')
    # in g/ml or kg/l at room temperature
    density = models.DecimalField(max_digits=9, decimal_places=3, default='1')

    allergen = models.BooleanField(default=False)

    hierarchy = models.CharField(max_length=100,
                                 default=f"{f'{parent} > ' if parent else ''}"
                                 f"{name}",
                                 blank=True)

    for n in NUTRIENTS:
        eval(f"{n}= models.DecimalField(max_digits=9, decimal_places=3, "
             "null=True, blank=True)")

    def __str__(self):
        """Return name as string."""
        return f"{'! ' if self.allergen else ''}{self.hierarchy}"

    def save(self, *args, **kwargs):
        """Update self.hierarchy and inherited values upon save."""
        self.hierarchy = \
            f"{f'{self.parent.hierarchy} > ' if self.parent else ''}" \
            + f"{self.name}"
        if self.parent:
            if self.parent.allergen:
                self.allergen = True
            self.category = self.parent.category
        super().save(*args, **kwargs)

    class Meta:
        """Defines metadata options."""

        ordering = ['category', '-allergen', 'hierarchy']


class Product(models.Model):
    """Define a product and its various attributes."""

    DAYS = ''
    WEEKS = '7*'
    MONTHS = '30*'
    TIMESCALE = ((DAYS, 'days'), (WEEKS, 'weeks'), (MONTHS, 'months'))

    VOLUME = 'v'
    WEIGHT = 'm'
    UNIT_TYPE = ((WEIGHT, 'grams'), (VOLUME, 'Millilitres'))

    name = models.CharField(max_length=100, default='')
    brand = models.ForeignKey(
        Brand, on_delete=models.RESTRICT, null=True, blank=True)
    preferred = models.BooleanField(default=False)
    purchase_link = models.URLField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    unit = models.CharField(
        max_length=1, choices=UNIT_TYPE, default=UNIT_TYPE[0][0])
    amount = models.DecimalField(
        max_digits=9, decimal_places=3, default='100')
    price = models.DecimalField(
        max_digits=9, decimal_places=3, null=True, blank=True)
    shelf_life = models.DecimalField(
        max_digits=9, decimal_places=0, null=True, blank=True)
    self_unit = models.CharField(
        max_length=3, choices=TIMESCALE, default=TIMESCALE[0][0], blank=True)
    fridge_life = models.DecimalField(
        max_digits=9, decimal_places=0, null=True, blank=True)
    fridge_unit = models.CharField(
        max_length=3, choices=TIMESCALE, default=TIMESCALE[0][0], blank=True)
    freezable = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)

    stereotype = models.ForeignKey(
        ProductStereotype, on_delete=models.SET_NULL, null=True)
    allergens = models.ManyToManyField(
        ProductStereotype, related_name='product_allergens', blank=True)
    trace_allergens = models.ManyToManyField(
        ProductStereotype, related_name='product_allergen_traces', blank=True)
    product_ingredients = models.ManyToManyField(
        ProductStereotype, related_name='product_ingredients', blank=True)
    density = models.DecimalField(
        max_digits=9, decimal_places=3, null=True, blank=True)

    for n in NUTRIENTS:
        eval(f"{n}= models.DecimalField(max_digits=9, decimal_places=3, "
             "null=True, blank=True)")

    def __str__(self):
        """Return name as string."""
        return f"{self.name} {f'by {self.brand}' if self.brand else ''} " \
            f"({self.stereotype})"

    def save(self, *args, **kwargs):
        """Update default values from stereotype upon save."""
        for n in NUTRIENTS:
            pass  # TODO implement nutrient updating
        super().save(*args, **kwargs)

    class Meta:
        """Defines metadata options."""

        ordering = ['-preferred', 'stereotype__category',
                    'stereotype', 'name', 'price']


# Recipes


class Author(models.Model):
    """Define the author of a recipe."""

    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    verified = models.BooleanField(default=False)
    biography = models.TextField(null=True, blank=True)
    profile = models.ImageField(null=True, blank=True)

    def __str__(self):
        """Return author as string."""
        return f"{self.last_name}, {self.first_name}" \
            f"{' ✓' if self.verified else ''}"

    class Meta:
        """Defines metadata options."""

        ordering = ['-verified', 'last_name', 'first_name']


class Recipe(models.Model):
    """Define a recipe."""

    title = models.CharField(max_length=30, default='')
    author = models.ForeignKey(
        Author, on_delete=models.RESTRICT, null=True, blank=True)
    favorite = models.BooleanField(default=False)
    difficulty = models.DecimalField(max_digits=1, decimal_places=0, default=0)
    score = models.DecimalField(max_digits=1, decimal_places=0, default=0)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    description = models.CharField(max_length=100, default='')
    portion_size = models.DecimalField(
        max_digits=3, decimal_places=0, null=True, blank=True)
    min_portions = models.DecimalField(max_digits=2, decimal_places=1)
    comment = models.TextField(default='', blank=True)
    ingredients = models.ManyToManyField(
        ProductStereotype, through='Ingredients')
    products = models.ManyToManyField(
        ProductStereotype, through='Products')
    method = models.TextField(default='', blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """Return recipe title as string."""
        return f"{'🖤 ' if self.favorite else ''}{self.title}"

    class Meta:
        """Defines metadata options."""

        ordering = ['-favorite', 'title', '-author__verified']


# Equipment
class Vessel(models.Model):
    """Define a cooking vessel and its various attributes."""

    # Constants in Vessel class
    STORAGE = 'STOR'
    MEASURING_JUG = 'MEAS'
    SAUCEPAN = 'SAUC'
    FRYING_PAN = 'FRY'
    DISH = 'DISH'
    BAKEWARE = 'BAKE'
    BOWL = 'BOWL'
    VESSEL_TYPE = (
        (STORAGE, 'Storage container or tupperware'),
        (MEASURING_JUG, 'Measuring jug'),
        (SAUCEPAN, 'Saucepan or pot'),
        (FRYING_PAN, 'Frying pan, grill pan or wok'),
        (DISH, 'Casserole or oven pan'),
        (BAKEWARE, 'Baking tray, oven pan or springform'),
        (BOWL, 'Mixing bowls'),
    )

    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    SIZE = ((SMALL, 'small'), (MEDIUM, 'medium'), (LARGE, 'large'))

    NO = '0'
    HEATPROOF = '1'
    OVENPROOF = '2'
    FLAMEPROOF = '3'
    HEAT_RESISTANCE = (
        (NO, 'Not heat resistant'),
        (HEATPROOF, 'Heatproof'),
        (OVENPROOF, 'Ovenproof'),
        (FLAMEPROOF, 'Flameproof'),
    )

    RECTANGLE = 'RECT'
    CIRCLE = 'CIRC'
    ELLIPSE = 'OVAL'
    SPECIAL = 'SPEC'
    SHAPES = (
        (RECTANGLE, 'Square or rectangular'),
        (CIRCLE, 'Circular'),
        (ELLIPSE, 'Oval or elliptical'),
        (SPECIAL, 'Decorative mould'),
    )

    name = models.CharField(max_length=30, default='')
    amount = models.DecimalField(max_digits=3, decimal_places=0, default='1')
    price = models.DecimalField(
        max_digits=9, decimal_places=3, null=True, blank=True)
    type = models.CharField(
        max_length=4, choices=VESSEL_TYPE, default=VESSEL_TYPE[1][0])
    shape = models.CharField(
        max_length=4, choices=SHAPES, default='')
    size = models.CharField(max_length=1, choices=SIZE, default='')
    depth = models.DecimalField(
        max_digits=3, decimal_places=0, null=True, blank=True)
    width = models.DecimalField(
        max_digits=3, decimal_places=0, null=True, blank=True)
    length = models.DecimalField(
        max_digits=3, decimal_places=0, null=True, blank=True)
    volume = models.DecimalField(
        max_digits=3, decimal_places=0, null=True, blank=True)
    heat_resistance = models.CharField(
        max_length=4, choices=HEAT_RESISTANCE, default='')
    airtight = models.BooleanField(default=False)
    dishwasher_safe = models.BooleanField(default=False)
    microwavable = models.BooleanField(default=False)
    freezer_safe = models.BooleanField(default=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """Return name as string."""
        return f"{self.name} ({self.size} {self.type})"

    class Meta:
        """Defines metadata options."""

        ordering = ['name', 'type', 'size', 'amount', 'price']


# Connections
class Ingredients(models.Model):
    """Connects products with recipes as ingredients."""

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductStereotype, on_delete=models.CASCADE)
    amount = models.DecimalField(
        max_digits=9, decimal_places=3, null=True, blank=True)
    optional = models.BooleanField(default=False)

    def __str__(self):
        """Return ingredients as string."""
        return f"Product '{self.product}' is " \
            + f"ingredient of Recipe '{self.recipe}'"


class Products(models.Model):
    """Connects products with recipes as products and by-products."""

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=9, decimal_places=3)

    def __str__(self):
        """Return products as string."""
        return f"Product '{self.product}' is " \
            + f"product of Recipe '{self.recipe}'"
