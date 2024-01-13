from django.contrib import admin
# Import model
from .models import Pasta, Dish

# Register your models here.
admin.site.register(Pasta)
admin.site.register(Dish)