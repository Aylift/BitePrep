from django import forms
from django.forms import inlineformset_factory, formset_factory
from .models import Food, DiaryEntry, FoodNutrient, FoodCategory, Nutrient

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
        fields = ['amount_100g']
    
    def __init__(self, *args, **kwargs):
        self.nutrient = kwargs.pop('nutrient', None)
        super().__init__(*args, **kwargs)
        if self.nutrient:
            self.fields['amount_100g'].label = f"Amount of {self.nutrient.name} per 100g"

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.nutrient:
            instance.nutrient = self.nutrient
        if commit:
            instance.save()
        return instance

def get_fixed_nutrient_formset(data=None):
    nutrients = Nutrient.objects.filter(name__in=['carb', 'fat', 'protein'])
    print(f"Nutrients fetched: {nutrients}")  # Debugging line

    FormSet = formset_factory(FoodNutrientForm, extra=len(nutrients), max_num=len(nutrients))
    formset = FormSet(data)

    for form, nutrient in zip(formset.forms, nutrients):
        form.nutrient = nutrient
        form.fields['amount_100g'].label = f"Amount of {nutrient.name} per 100g"
        print(f"Form label set for {nutrient.name}")  # Debugging line

    return formset

class FoodCategoryForm(forms.ModelForm):
    class Meta:
        model = FoodCategory
        fields = ['name']