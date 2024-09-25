from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import FoodCategory, Food, Nutrient, FoodNutrient, DiaryEntry
from .forms import FoodSearchForm, DiaryEntryForm, FoodForm, FoodCategoryForm, get_fixed_nutrient_formset


def foods_db(request):
    portion_size = float(request.GET.get('portion_size', 100))
    foods_list = Food.objects.all().prefetch_related('food_nutrients', 'category')

    for food in foods_list:
        food.calories = food.calories_100g * portion_size / 100
        for food_nutrient in food.food_nutrients.all():
            food_nutrient.amount = food_nutrient.amount_100g * portion_size / 100

    if request.method == 'POST':
        if 'add_food' in request.POST:
            form = FoodForm(request.POST)
            formset = get_fixed_nutrient_formset(request.POST)
            if form.is_valid() and formset.is_valid():
                food = form.save()
                for form in formset:
                    if form.cleaned_data:  # Ensure the form is filled out
                        food_nutrient = form.save(commit=False)
                        food_nutrient.food = food
                        food_nutrient.save()
                return redirect('foods_db')

        elif 'add_category' in request.POST:
            category_form = FoodCategoryForm(request.POST)
            if category_form.is_valid():
                category_form.save()
                return redirect('foods_db')
    else:
        form = FoodForm()
        formset = get_fixed_nutrient_formset()  # Initialize empty formset
        category_form = FoodCategoryForm()

    context = {
        'foods_list': foods_list,
        'portion_size': portion_size,
        'form': form,
        'formset': formset,
        'category_form': category_form,
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
                           'foods': foods,
                           'diary_entries': DiaryEntry.objects.all()
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

def delete_diary_record(request, pk):
    record = get_object_or_404(DiaryEntry, pk=pk)

    if request.method == 'POST':
        record.delete()
        return redirect('diary')
    
    return render(request, 'Foods/diary.html', {'record': record})

def delete_food_record(request, pk):
    record = get_object_or_404(Food, pk=pk)

    if request.method == 'POST':
        record.delete()
        return redirect('foods_db')

    return render(request, 'Foods/food_diary.html', {'record': record})