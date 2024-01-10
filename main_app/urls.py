from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pastas/', views.pastas_index, name='index'),
    path('pastas/<int:pasta_id>/', views.pastas_detail, name='detail'),
]
