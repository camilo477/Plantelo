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

# Importar los módulos necesarios
from django.shortcuts import render
import mysql.connector

def mostrar_plantas(request):
    # Obtener el ID de la solicitud GET
    id = request.GET.get('id', '')

    # Imprimir el ID en la consola para depuración
    print("ID recibido:", id)

    # Conexión a la base de datos
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="plantas"
    )

    # Cursor para ejecutar consultas SQL
    cursor = connection.cursor()

    # Consulta SQL para obtener los datos de las plantas
    query = "SELECT * FROM planta WHERE Id = %s;"
    cursor.execute(query, (id,))

    # Obtener el resultado
    planta = cursor.fetchone()

    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()

    # Si no se encontró ninguna planta con el ID proporcionado
    if not planta:
        return JsonResponse({'error': 'Planta con ID {} no encontrada'.format(id)})

    # Convertir los resultados en un diccionario
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

    # Devolver la información de la planta como una respuesta JSON
    return JsonResponse({'planta': planta_info})

def get_plant_name(request):
    try:
        # Obtener la planta con ID 3 desde la base de datos
        planta = Planta.objects.get(id=3)
        nombre_cientifico = planta.Nombre_cientifico
        # Devolver la información de la planta como una respuesta JSON
        return JsonResponse({'nombre_cientifico': nombre_cientifico})
    except Planta.DoesNotExist:
        # Si la planta con ID 3 no existe, devolver un mensaje de error
        return JsonResponse({'error': 'Planta con ID 3 no encontrada'})

def test_ajax_url(request):
    try:
        # Obtener la planta con ID 3 desde la base de datos
        planta = Planta.objects.get(id=3)
        nombre_cientifico = planta.Nombre_cientifico
        # Devolver la información de la planta como una respuesta JSON
        return JsonResponse({'nombre_cientifico': nombre_cientifico})
    except Planta.DoesNotExist:
        # Si la planta con ID 3 no existe, devolver un mensaje de error
        return JsonResponse({'error': 'Planta con ID 3 no encontrada'})

def buscar_planta(request):
    # Conexión a la base de datos
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="plantas"
    )

    # Cursor para ejecutar consultas SQL
    cursor = connection.cursor()

    # Obtener el ID de la planta proporcionado en la solicitud GET
    id = request.GET.get('id')

    # Consulta SQL para obtener los datos de la planta con el ID proporcionado
    query = f"SELECT * FROM planta WHERE Id = {id};"

    # Ejecutar la consulta
    cursor.execute(query)

    # Obtener todos los resultados como una lista de diccionarios
    column_names = [col[0] for col in cursor.description]
    planta = [dict(zip(column_names, row)) for row in cursor.fetchall()]

    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()

    # Renderizar la plantilla con los datos obtenidos
    return render(request, 'mostrar_plantas.html', {'planta': planta})

def mapa(request):
    return render(request, 'pages/index.html')