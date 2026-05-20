
from django.db.models import Q

from django.shortcuts import render, redirect
from .models import Mascota
from django.contrib.auth.decorators import login_required

@login_required
def lista_mascotas(request):
    query = request.GET.get('q')  # lo que escribe el usuario

    mascotas = Mascota.objects.all()

    if query:
        mascotas = Mascota.objects.filter(
        Q(nombre__icontains=query) |
        Q(codigo__icontains=query)
    )

    return render(request, 'mascotas/lista.html', {
        'mascotas': mascotas,
        'query': query
    })

@login_required
def crear_mascota(request):
    error = None
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        if codigo and Mascota.objects.filter(codigo=codigo).exists():
            error = "⚠️ El código ya existe. Por favor, ingrese otro."
        else:
            Mascota.objects.create(
            codigo=codigo,
            nombre=nombre,
            edad_anios=request.POST['edad_anios'],
            edad_meses=request.POST['edad_meses'],
            edad_dias=request.POST['edad_dias'],
            tipo=request.POST['tipo']
        )
            return redirect('lista')

    return render(request, 'mascotas/crear.html', {'error': error})

@login_required
def editar_mascota(request, id):
    mascota = Mascota.objects.get(id=id)

    if request.method == 'POST':
        mascota.nombre = request.POST['nombre']
        mascota.edad_anios = request.POST['edad_anios']
        mascota.edad_meses = request.POST['edad_meses']
        mascota.edad_dias = request.POST['edad_dias']
        mascota.tipo = request.POST['tipo']
        mascota.save()

        return redirect('lista')

    return render(request, 'mascotas/editar.html', {'mascota': mascota})

@login_required
def eliminar_mascota(request, id):
    mascota = Mascota.objects.get(id=id)
    mascota.delete()
    return redirect('lista')