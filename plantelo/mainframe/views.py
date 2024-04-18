from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from .models import Planta
from django.shortcuts import render
from .models import Planta

from django.shortcuts import render
import mysql.connector
from django.http import JsonResponse
from .models import Planta

def buscar_plantas(request):
    nombre_cientifico = request.GET.get('nombre_cientifico', '').lower() 

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="plantas"
        )
        cursor = connection.cursor()

        query = "SELECT Nombre_cientifico FROM planta WHERE Nombre_cientifico LIKE %s;"
        cursor.execute(query, (nombre_cientifico + '%',))

        plantas = cursor.fetchall()

        cursor.close()
        connection.close()

        nombres_plantas = [planta[0] for planta in plantas]

        return JsonResponse({'plant_names': nombres_plantas})
    except mysql.connector.Error as e:
        return JsonResponse({'error': str(e)})


def mostrar_nombres_plantas(request):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="plantas"
        )

        cursor = connection.cursor()

        query = "SELECT Nombre_cientifico FROM planta;"
        cursor.execute(query)

        plantas = cursor.fetchall()

        cursor.close()
        connection.close()

        nombres_plantas = [planta[0] for planta in plantas]

        return JsonResponse({'plant_names': nombres_plantas})
    except Exception as e:
        return JsonResponse({'error': str(e)})

def mostrar_plantas(request):
    nombre_cientifico = request.GET.get('nombre_cientifico', '').lower() 

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="plantas"
        )

        cursor = connection.cursor()

        query = "SELECT * FROM planta WHERE Nombre_cientifico = %s;"
        cursor.execute(query, (nombre_cientifico,))

        planta = cursor.fetchone()

        if not planta:
            return JsonResponse({'error': 'Planta con nombre científico "{}" no encontrada'.format(nombre_cientifico)})

        planta_info = {
            'Id': planta[0],
            'Codigo_institucion': planta[1],
            'Codigo_coleccion': planta[2],
            'Grabado_por': planta[3],
            'Pais': planta[4],
            'Provincia_estado': planta[5],
            'Ciudad': planta[6],
            'Localidad': planta[7],
            'Latitud': float(planta[8]),
            'Longitud': float(planta[9]),
            'Identificado_por': planta[10],
            'Nombre_cientifico': planta[11],
            'Reino': planta[12],
            'Filo': planta[13],
            'Clase': planta[14],
            'Orden': planta[15],
            'Familia': planta[16],
            'Genero': planta[17],
            'Epiteto_especifico': planta[18],
            'Taxon_rango': planta[19],
            'Ubicacion': planta[20]
        }

        return JsonResponse({'planta': planta_info})
    except Exception as e:
        return JsonResponse({'error': str(e)})
    finally:
        if cursor:
            cursor.fetchall()  
            cursor.close()
        if connection:
            connection.close()


def test_ajax_url(request):
    try:
        planta = Planta.objects.get(id=3)
        nombre_cientifico = planta.Nombre_cientifico
        return JsonResponse({'nombre_cientifico': nombre_cientifico})
    except Planta.DoesNotExist:
        return JsonResponse({'error': 'Planta con ID 3 no encontrada'})



def mapa(request):
    return render(request, 'pages/index.html')