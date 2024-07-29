from django import forms
from django.forms import inlineformset_factory
from .models import Food, DiaryEntry, FoodNutrient, FoodCategory

class FoodSearchForm(forms.Form):
    query = forms.CharField(label='Search for food', max_length=100)

class DiaryEntryForm(forms.ModelForm):
    class Meta:
        model = DiaryEntry
        fields = ['food', 'portion_size']
        widgets = {
            'food': forms.HiddenInput()
        }

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'category', 'description', 'calories_100g']

class FoodNutrientForm(forms.ModelForm):
    class Meta:
        model = FoodNutrient
        fields = ['nutrient', 'amount_100g']

FoodNutrientFormSet = inlineformset_factory(Food, FoodNutrient, form=FoodNutrientForm, extra=1)

class FoodCategoryForm(forms.ModelForm):
    class Meta:
        model = FoodCategory
        fields = ['name']