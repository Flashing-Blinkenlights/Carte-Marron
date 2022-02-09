from django.contrib import admin

from .models import (Author, Brand, Product, ProductStereotype, Recipe, Tag,
                     Vessel)

admin.site.register(Author)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(ProductStereotype)
admin.site.register(Vessel)
admin.site.register(Recipe)
admin.site.register(Tag)
