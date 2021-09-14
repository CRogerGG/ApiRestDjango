from django.shortcuts import render,redirect
from .models import *
from .forms import LibroForm
# Create your views here.

def home(request):
    return render(request,'index.html')

def crearLibro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = LibroForm()
    return render(request,'libros/crear_libro.html',{'form':form})

def listarLibro(request):
    libro = Libro.objects.all()
    context = {'libro':libro}
    return render(request,'libros/listar_libro.html',context)

def editarLibro(request, id):
    libro = Libro.objects.get(id = id)
    if request.method == 'GET':
        form = LibroForm(instance=libro)
    else:
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request,'libros/crear_libro.html',{'form':form})

def eliminarLibro(request,id):
    libro = Libro.objects.get(id=id)
    if request.method == 'POST':
        libro.delete()
        return redirect('index')
    return render(request,'libros/eliminar_libro.html',{'libro':libro})

