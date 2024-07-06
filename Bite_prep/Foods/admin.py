from django.contrib import admin
from .models import Category, GroceryList, Item

admin.site.register(Category)
admin.site.register(GroceryList)
admin.site.register(Item)
