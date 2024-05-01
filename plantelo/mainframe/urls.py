from django.urls import path
from . import views
from .views import mostrar_plantas

urlpatterns = [
    path('ajax/get_plant_name/', views.test_ajax_url, name='test_ajax_url'),
    path('plantas/', views.mostrar_plantas, name='mostrar_plantas'),
    path('mostrar_plantas/', views.mostrar_plantas, name='mostrar_plantas'),
    path('mostrar_nombres_plantas/', views.mostrar_nombres_plantas, name='mostrar_nombres_plantas'),
    path('buscar_plantas/', views.buscar_plantas, name='buscar_plantas'),
    path('mostrar_plantas_por_estado/', views.mostrar_plantas_por_estado, name='mostrar_plantas_por_estado'),
   path('obtener_departamento/', views.obtener_departamento, name='obtener_departamento'),
]