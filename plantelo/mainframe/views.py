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
            'Filo': planta[1],
            'Clase': planta[2],
            'Orden': planta[3],
            'Familia': planta[4],
            'Genero': planta[5],
            'Nombre_cientifico': planta[6],
            'Localidad': planta[7],
            'Provincia_estado': planta[8],
            'Latitud': float(planta[9]),
            'Longitud': float(planta[10]),
            'Codigo_institucion': planta[11],
            
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

def mostrar_plantas_por_estado(request):
    nombre_estado = request.GET.get('nombre_estado', '')

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="plantas"
        )

        cursor = connection.cursor()

        if nombre_estado: 
            query = "SELECT * FROM planta WHERE Provincia_estado = %s;"
            
            cursor.execute(query, (nombre_estado,))

        plantas = cursor.fetchall()

        plantas_info = []
        for planta in plantas:
            planta_info = {
                'Id': planta[0],
                'Filo': planta[1],
                'Clase': planta[2],
                'Orden': planta[3],
                'Familia': planta[4],
                'Genero': planta[5],
                'Nombre_cientifico': planta[6],
                'Localidad': planta[7],
                'Provincia_estado': planta[8],
                'Latitud': float(planta[9]),
                'Longitud': float(planta[10]),
                'Codigo_institucion': planta[11],
            }
            plantas_info.append(planta_info)

        return JsonResponse({'plantas': plantas_info})
    except Exception as e:
        return JsonResponse({'error': str(e)})
    finally:
        if cursor:
            cursor.fetchall()  
            cursor.close()
        if connection:
            connection.close()


def obtener_departamento(request):
    if request.method == 'GET':
        nombre_cientifico = request.GET.get('nombre_cientifico', None)
        if nombre_cientifico:
            try:
                with connection.cursor() as cursor:
                    query = "SELECT Provincia_estado FROM planta WHERE Nombre_cientifico = %s;"
                    cursor.execute(query, [nombre_cientifico])
                    departamento = cursor.fetchone()

                if departamento:
                    return JsonResponse({'departamento': departamento[0]})
                else:
                    return JsonResponse({'error': 'Departamento no encontrado para la planta'}, status=404)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Parámetro nombre_cientifico no proporcionado'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)