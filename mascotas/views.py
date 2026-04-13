from django.shortcuts import render, redirect
from .models import Mascota


def lista_mascotas(request):
    query = request.GET.get('q')  # lo que escribe el usuario

    mascotas = Mascota.objects.all()

    if query:
        mascotas = Mascota.objects.filter(nombre__icontains=query)

    return render(request, 'mascotas/lista.html', {
        'mascotas': mascotas,
        'query': query
    })


def crear_mascota(request):
    if request.method == 'POST':
        Mascota.objects.create(
            nombre=request.POST['nombre'],
            edad_anios=request.POST['edad_anios'],
            edad_meses=request.POST['edad_meses'],
            edad_dias=request.POST['edad_dias'],
            tipo=request.POST['tipo']
        )
        return redirect('lista')

    return render(request, 'mascotas/crear.html')


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


def eliminar_mascota(request, id):
    mascota = Mascota.objects.get(id=id)
    mascota.delete()
    return redirect('lista')