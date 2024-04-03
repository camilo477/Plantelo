from django.urls import path
from . import views
from .views import mostrar_plantas

urlpatterns = [
    # Otras rutas aquí...
    path('ajax/get_plant_name/', views.test_ajax_url, name='test_ajax_url'),
    path('plantas/', views.mostrar_plantas, name='mostrar_plantas'),
    path('mostrar_plantas/', views.mostrar_plantas, name='mostrar_plantas'),
]