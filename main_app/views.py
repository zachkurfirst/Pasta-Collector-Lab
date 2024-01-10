from django.shortcuts import render

# Import Model
from .models import Pasta

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
    return render(request, 'pastas/detail.html', {
        'pasta': pasta
    })