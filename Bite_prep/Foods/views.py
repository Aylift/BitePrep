from django.shortcuts import render, redirect
from django.db.models import Q
from .models import FoodCategory, Food, Nutrient, FoodNutrient, DiaryEntry
from .forms import FoodSearchForm, DiaryEntryForm, FoodForm, FoodNutrientFormSet


def foods_db(request):
    portion_size = request.GET.get('portion_size', 100)
    portion_size = float(portion_size)

    foods_list = Food.objects.all().prefetch_related('food_nutrients', 'category')

    for food in foods_list:
        food.calories = food.calories_100g * portion_size / 100
        for food_nutrient in food.food_nutrients.all():
            food_nutrient.amount = food_nutrient.amount_100g * portion_size / 100
    
    if request.method == 'POST':
        form = FoodForm(request.POST)
        formset = FoodNutrientFormSet(request.POST, instance=Food())
        if form.is_valid():
            formset.instance = food
            formset.save()
            form.save()
            return redirect('foods_db')
    else:
        form = FoodForm()
        formset = FoodNutrientFormSet(instance=Food())

    context= {
        'foods_list': foods_list,
        'portion_size': portion_size,
        'form': form,
        'formset': formset,
    }
    return render(request, 'Foods/foods_db.html', context)

def home(request):
    return render(request, 'base.html')

def diary(request):
    if request.method == 'POST':
        search_form = FoodSearchForm(request.POST)
        entry_form = DiaryEntryForm(request.POST)
        if 'search' in request.POST and search_form.is_valid():
            query = search_form.cleaned_data['query']
            foods = Food.objects.filter(
                Q(name__icontains=query) | Q(category__name__icontains=query)
            )
            return render(request, 'Foods/diary.html', 
                          {'search_form': search_form, 
                           'entry_form': entry_form, 
                           'foods': foods
                        })
        elif 'add' in request.POST and entry_form.is_valid():
            entry_form.save()
            return redirect('diary')
    else:
        search_form = FoodSearchForm()
        entry_form = DiaryEntryForm()

    diary_entries = DiaryEntry.objects.all()
    return render(request, 'Foods/diary.html', {
        'search_form': search_form,
        'entry_form': entry_form,
        'diary_entries': diary_entries
    })