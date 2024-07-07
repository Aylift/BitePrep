from django.shortcuts import render

from .models import FoodCategory, Food, Nutrient, FoodNutrient


def index(request):
    foods_list = Food.objects.all()
    context = {
        'foods_list': foods_list,
    }
    return render(request, 'Foods/index.html', context)
