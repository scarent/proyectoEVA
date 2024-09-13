from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,'appEVA/index.html')

def auto(request,nombre,descripcion,valoracion):
    datos = {"nombre":nombre,
            "descripcion":descripcion,
            "valoracion":valoracion}
    return render(request,'appEVA/interfaz.html',datos)

def yaris(request):
    datos={"nombre":"Toyota yaris",
            "descripcion":"Vehiculo de ciudad",
            "valoracion":"5",
            "img1":"yaris.png"}
    return render(request,'appEVA/interfaz.html',datos)