from django.shortcuts import render, redirect,  get_object_or_404
from django.core.exceptions import ValidationError
from .models import Usuario, Postulacion
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User 
from django.contrib.auth import logout
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponse
def home(request):

    return render(request,'Paginas/index.html')

def procesar_postulacion(request):
    if request.method == 'POST':
        tipo_postulacion = request.POST.get('tipo_postulacion', 'desconocido')

        # Validar cotizaciones (mínimo 2)
        cotizaciones = request.FILES.getlist('cotizaciones[]')
        if len(cotizaciones) < 2:
            messages.error(request, 'Debes adjuntar al menos dos cotizaciones.')
            return redirect(request.path)

        # Capturar archivos
        campos_archivos = [
            'formulario', 'rut_organizacion', 'ci_representante',
            'certificado_personalidad', 'certificado_fondos', 'cuenta_corriente',
            'acreditacion_propiedad', 'aportes_propios', 'aportes_terceros'
        ]

        archivos = {campo: request.FILES.get(campo) for campo in campos_archivos}

        # Guardar la postulación en la base de datos, incluyendo el usuario actual
        postulacion = Postulacion.objects.create(
            usuario=request.user,  # Asegúrate de incluir al usuario aquí
            tipo_postulacion=tipo_postulacion,
            cotizaciones=[archivo.name for archivo in cotizaciones],
            otros_documentos=[archivo.name for archivo in request.FILES.getlist('otros_documentos[]')],
            **archivos
        )

        messages.success(request, '¡Postulación enviada con éxito!')
        return redirect('home')

    return render(request, 'formulario_postulacion.html')


def vista_postulacion(request, template_name):
    if request.method == 'POST':
        return procesar_postulacion(request)
    return render(request, template_name)

def Aporte(request):
    return vista_postulacion(request, 'Paginas/Aporte.html')

def Fondeporte(request):
    return vista_postulacion(request, 'Paginas/Fondeporte.html')

def fondeve(request):
    return vista_postulacion(request, 'Paginas/fondeve.html')

def subvencion(request):
    return vista_postulacion(request, 'Paginas/subvencion.html')






def Login(request):
    if request.method == 'POST':
        email = request.POST.get('usuario')  
        password = request.POST.get('password')

  
        try:
            user = Usuario.objects.get(correo=email) 
        except Usuario.DoesNotExist:
            user = None


        if user is not None and check_password(password, user.contraseña):
            login(request, user) 
            messages.success(request, '¡Inicio de sesión exitoso!')
            return redirect('home')  
        else:
            messages.error(request, 'Correo o contraseña incorrectos.')

    return render(request, 'Paginas/Login.html')

def Registro(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')

        # Validar que las contraseñas coinciden
        if password != password1:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'Paginas/Registro.html', {'nombre': nombre, 'apellido': apellido, 'correo': correo})

        try:
            # Intentar crear y guardar el usuario
            usuario = Usuario(
                nombre=nombre,
                apellido=apellido,
                correo=correo,
                contraseña=make_password(password)
            )
            usuario.save()
            messages.success(request, '¡Registro exitoso! Ahora puedes iniciar sesión.')
            return redirect('Login')  # Redirigir a la página de login
        except IntegrityError:
            messages.error(request, 'El correo ya está registrado. Usa otro.')
            return render(request, 'Paginas/Registro.html', {'nombre': nombre, 'apellido': apellido, 'correo': correo})  

    return render(request, 'Paginas/Registro.html')


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
def Logout(request):
    logout(request)
    return redirect('home')  

def lista_postulaciones(request):
    postulaciones = Postulacion.objects.all()
    print("Postulaciones:", postulaciones)  # Verifica qué datos se están pasando
    return render(request, 'Paginas/Postulacion.html', {'postulaciones': postulaciones})


def cambiar_estado(request, postulacion_id):
    postulacion = get_object_or_404(Postulacion, id=postulacion_id)
    
    if request.method == 'POST':
        nuevo_estado = request.POST.get('estado')
        comentarios = request.POST.get('comentarios')
        
        postulacion.estado = nuevo_estado
        postulacion.comentarios = comentarios
        postulacion.save()
        messages.success(request, f"El estado de la postulación '{postulacion.tipo_postulacion}' ha sido cambiado a {postulacion.get_estado_display()} correctamente.")
        return redirect('postulacion')  # Redirige a la página de postulaciones
    
    return render(request, 'Paginas/Postulacion.html', {'postulacion': postulacion})


def estado(request):
    postulaciones = Postulacion.objects.filter(usuario=request.user).order_by('-fecha_postulacion')

    return render(request, 'Paginas/estado.html', {'postulaciones': postulaciones})

def eliminar_postulacion(request, postulacion_id):
    # Obtener la postulación que el usuario quiere eliminar
    postulacion = get_object_or_404(Postulacion, id=postulacion_id, usuario=request.user)

    # Eliminar la postulación
    postulacion.delete()

    # Mensaje de éxito
    messages.success(request, '¡Postulación eliminada con éxito!')
    return redirect('estado')
