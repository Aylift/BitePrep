from django.template import loader
from django.http import HttpResponse

from .models import FoodCategory, Food, Nutrient, FoodNutrient


def index(request):
    foods = Food.name
    template = loader.get_template('foods/index.html')
    context = {
        'foods': foods,
    }
    return HttpResponse(template.render(context, request))
