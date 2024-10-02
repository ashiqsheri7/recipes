from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'difficulty_level', 'preparation_time', 'vegetarian', 'description', 'image']
