from django.shortcuts import render, redirect

# Import for Class-based Views
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Import Model
from .models import Pasta

# Import ModelForm
from .forms import DishForm

# pastas = [
#     {
#         'name': 'Bucatini',
#         'type': 'Ribbon-Cut',
#         'cook_time': 9
#     },
#     {
#         'name': 'Agnolotti',
#         'type': 'Stuffed',
#         'cook_time': 6
#     },
#     {
#         'name': 'Rigatoni',
#         'type': 'Tube-Shaped',
#         'cook_time': 8
#     }
# ]

# Create your views here.

# HOME VIEW
def home(request):
    return render(request, 'home.html')

# ABOUT VIEW
def about(request):
    return render(request, 'about.html')

# PASTAS INDEX VIEW
def pastas_index(request):
    pastas = Pasta.objects.all() # retrieve all Pastas
    return render(request, 'pastas/index.html', {
        'pastas': pastas,
    })

# PASTAS DETAIL VIEW - GET
def pastas_detail(request, pasta_id):
    pasta = Pasta.objects.get(id=pasta_id) # retreive pasta by id
    dish_form = DishForm() # invoke ModelForm
    return render(request, 'pastas/detail.html', {
        'pasta': pasta,
        'dish_form': dish_form
    })

# PASTAS CREATE CLASS-BASED VIEW
class PastaCreate(CreateView):
    model = Pasta
    fields = '__all__'

# PASTAS UPDATE CLASS-BASED VIEW
class PastaUpdate(UpdateView):
    model = Pasta
    fields = ['type', 'cook_time']

# PASTAS DELETE CLASS-BASED VIEW
class PastaDelete(DeleteView):
    model = Pasta
    success_url = reverse_lazy('index')

# PASTA - CREATE DISH
def add_dish(request, pasta_id):
    form = DishForm(request.POST)
    if form.is_valid():
        new_dish = form.save(commit=False)
        new_dish.pasta_id = pasta_id
        new_dish.save()
    return redirect('detail', pasta_id=pasta_id)

