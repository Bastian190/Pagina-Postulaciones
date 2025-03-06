from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model 

class UsuarioManager(BaseUserManager):
    def create_user(self, correo, password=None, **extra_fields):
        if not correo:
            raise ValueError('El correo debe ser proporcionado')
        correo = self.normalize_email(correo)
        user = self.model(correo=correo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, correo, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(correo, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    es_funcionario = models.BooleanField(default=False)

    USERNAME_FIELD = 'correo'  
    REQUIRED_FIELDS = ['nombre', 'apellido']

    objects = UsuarioManager()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    def get_full_name(self):
        return f"{self.nombre} {self.apellido}"

    def get_short_name(self):
        return self.nombre



from django.db import models

class Postulacion(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('en_revision', 'En revisión'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
    ]
    
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="postulaciones")
    tipo_postulacion = models.CharField(max_length=100)
    formulario = models.FileField(upload_to='formularios/')
    rut_organizacion = models.FileField(upload_to='ruts/')
    ci_representante = models.FileField(upload_to='cis/')
    certificado_personalidad = models.FileField(upload_to='certificados_personalidad/')
    certificado_fondos = models.FileField(upload_to='certificados_fondos/')
    cuenta_corriente = models.FileField(upload_to='cuentas_corrientes/')
    acreditacion_propiedad = models.FileField(upload_to='acreditaciones/', blank=True, null=True)
    aportes_propios = models.FileField(upload_to='aportes_propios/', blank=True, null=True)
    aportes_terceros = models.FileField(upload_to='postulaciones/', blank=True, null=True)
    cotizaciones = models.JSONField(default=list)
    otros_documentos = models.JSONField(default=list)
    fecha_postulacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    comentarios = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Postulación {self.tipo_postulacion} - {self.estado}"