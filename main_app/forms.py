from django.forms import ModelForm
from .models import Dish

class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'is_vegetarian', 'recipe_link', 'difficulty']
