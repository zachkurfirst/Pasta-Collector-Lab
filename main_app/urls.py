from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pastas/', views.pastas_index, name='index'),
    path('pastas/<int:pasta_id>/', views.pastas_detail, name='detail'),
    path('pastas/create', views.PastaCreate.as_view(), name='pastas_create'),
    path('pastas/<int:pk>/update', views.PastaUpdate.as_view(), name='pastas_update'),
    path('pastas/<int:pk>/delete', views.PastaDelete.as_view(), name='pastas_delete'),
]
