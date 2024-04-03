from django.contrib import admin
from django.urls import path, include
from mainframe.views import mapa
from popup.views import pop

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', pop),
    path('home/', mapa),
    path('', include('mainframe.urls')),
]