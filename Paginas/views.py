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
def Login(request):

    return render(request,'Paginas/Login.html')
def Registro(request):

    return render(request,'Paginas/Registro.html')