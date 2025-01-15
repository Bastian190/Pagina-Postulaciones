from django.shortcuts import render

def home(request):

    return render(request,'Paginas/index.html')

def Aporte(request):

    return render(request,'Paginas/Aporte.html')

def Fondeporte(request):

    return render(request,'Paginas/Fondeporte.html')

def fondeve(request):

    return render(request,'Paginas/fondeve.html')

def subvencion(request):

    return render(request,'Paginas/subvencion.html')