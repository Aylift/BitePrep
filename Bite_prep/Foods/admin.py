from django.contrib import admin
from .models import FoodCategory, Food, Nutrient, FoodNutrient

admin.site.register(FoodCategory)
admin.site.register(Food)
admin.site.register(Nutrient)
admin.site.register(FoodNutrient)
