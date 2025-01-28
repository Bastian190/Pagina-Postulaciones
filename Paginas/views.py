from django.shortcuts import render
from django.shortcuts import render
from django.core.exceptions import ValidationError
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



def validar_archivo(archivo, extensiones_permitidas):
    if not archivo.name.split('.')[-1].lower() in extensiones_permitidas:
        raise ValidationError(
            f"El archivo '{archivo.name}' no tiene un formato válido. Permitidos: {', '.join(extensiones_permitidas)}"
        )

# Vista para manejar el formulario
def formulario_subvencion(request):
    if request.method == 'POST':
        errores = {}
        # Campos requeridos y extensiones permitidas
        campos_requeridos = [
            ('formulario', ['pdf', 'docx']),
            ('rut_organizacion', ['pdf', 'jpg', 'png']),
            ('cotizacion1', ['pdf', 'jpg', 'png']),
            ('cotizacion2', ['pdf', 'jpg', 'png']),
        ]

        # Validar cada campo
        for campo, extensiones in campos_requeridos:
            archivo = request.FILES.get(campo)
            if not archivo:
                errores[campo] = f"El campo '{campo}' es obligatorio."
            else:
                try:
                    validar_archivo(archivo, extensiones)
                except ValidationError as e:
                    errores[campo] = str(e)

        # Si hay errores, devolverlos al template
        if errores:
            return render(request, 'Paginas/Fondeporte.html', {'errores': errores})

        # Si todo está correcto, redirigir a la página principal
        return render(request, 'Paginas/index.html')

    # En caso de GET, renderizar la página sin errores
    return render(request, 'Paginas/Fondeporte.html')