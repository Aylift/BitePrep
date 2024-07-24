from django import forms
from .models import Food, DiaryEntry

class FoodSearchForm(forms.Form):
    query = forms.CharField(label='Search for food', max_length=100)

class DiaryEntryForm(forms.ModelForm):
    class Meta:
        model = DiaryEntry
        fields = ['food', 'portion_size']
        widgets = {
            'food': forms.HiddenInput()
        }