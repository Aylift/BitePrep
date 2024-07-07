from django.shortcuts import render

from .models import FoodCategory, Food, Nutrient, FoodNutrient


def index(request):
    portion_size = request.GET.get('portion_size,', 100)
    portion_size = float(portion_size)

    foods_list = Food.objects.all().prefetch_related('food_nutrients', 'category')

    for food in foods_list:
        food.calories = food.calories_100g * portion_size / 100
        for food_nutrient in food.food_nutrients.all():
            food_nutrient.amount = food_nutrient.amount_100g * portion_size / 100

    context= {
        'foods_list': foods_list,
        'portion_size': portion_size,
    }
    return render(request, 'Foods/index.html', context)

def home(request):
    return render(request, 'base.html')