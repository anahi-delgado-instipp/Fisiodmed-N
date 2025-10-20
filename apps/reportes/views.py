from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def tabla_reportes(request):
    return render(request, 'reportes/tabla_reportes.html')

@login_required
def editar_reporte(request):
    return render(request, 'reportes/editar_reporte.html')