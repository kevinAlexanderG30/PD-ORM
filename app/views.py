from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Book
from .forms import AutorForm, BookForm


# Create your views here.
def index(request):
    autor = Autor.objects.all()
    """Select * From Autor"""

    context = {
        "autor": autor,
        "form": AutorForm()
    }
    return render(request, 'index.html', context)

#Crear Autor
def create_autor(request):
    if request.method == "POST": 
        # p = Autor(name="Marcela")
        # p.save()
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()

    return redirect("index")

def eliminar_autor(request, pk):
    # autor = Autor.objects.get(pk=pk)
    # print(f"Hola mundo {autor}")
    autor = get_object_or_404(Autor, pk=pk)
    print(f"Hola mundo, {autor}")
    autor.delete()
    return redirect("index")

"""Select * From Autor Where name like %name% """
def buscar(request): 
    if request.method == "POST":
        name = request.POST['buscar']
        print(f"Hola {name}" )
        # Con contains es como si usaramos el like %paramentro%
        #Con startswith es como si usaramos like %parametro
        autor = Autor.objects.filter(name__contains=name)
        print("Hola", autor)
        context = {
            "autor": autor,
        }
        return render(request,"buscar.html",context)
    else: 
        return redirect('index')
    
def crear_libros(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        
        redirect('crearLibros')

# " Select * FROM" Book es como estar 
#haciendo un Book.objects.all()
    context = {
        'form': BookForm(),
        'book': Book.objects.all(),

    }
    return render(request, 'crearbooks.html', context)