from django.shortcuts import render

def pop(request):
    return render(request, 'pages/introduccion.html')