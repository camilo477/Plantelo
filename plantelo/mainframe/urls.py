from django.urls import path
from . import views
from .views import mostrar_plantas, complaint_view
from django.urls import path
from .views import mostrar_plantas, complaint_view, success_view
from django.views.generic import TemplateView

urlpatterns = [
    path('ajax/get_plant_name/', views.test_ajax_url, name='test_ajax_url'),
    path('plantas/', views.mostrar_plantas, name='mostrar_plantas'),
    path('mostrar_plantas/', views.mostrar_plantas, name='mostrar_plantas'),
    path('mostrar_nombres_plantas/', views.mostrar_nombres_plantas, name='mostrar_nombres_plantas'),
    path('buscar_plantas/', views.buscar_plantas, name='buscar_plantas'),
    path('mostrar_plantas_por_estado/', views.mostrar_plantas_por_estado, name='mostrar_plantas_por_estado'),
    path('obtener_departamento/', views.obtener_departamento, name='obtener_departamento'),
    path('reclamo/', complaint_view, name='complaint'),
    path('formulario/', complaint_view, name='complaint'),
    path('success/', success_view, name='success'),
    path('buscar_plantas_por_letras/', views.buscar_plantas_por_letras, name='buscar_plantas_por_letras'),
]