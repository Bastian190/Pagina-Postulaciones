from django.urls import path
from .views import home,subvencion,Aporte,Fondeporte,fondeve,Login,Registro,formulario_subvencion, lista_postulaciones, estado
from . import views

urlpatterns = [
    path('',home,name="home"),
    path('subvencion',subvencion,name="subvencion"),
    path('Aporte',Aporte,name="Aporte"),
    path('Fondeporte',Fondeporte,name="Fondeporte"),
    path('fondeve',fondeve,name="fondeve"),
    path('postulacion/', views.lista_postulaciones, name="postulacion"),
    path('Login',Login,name="Login"),
    path('Registro/',Registro,name="Registro"),
    path('formulario_subvencion/',formulario_subvencion, name='formulario_subvencion'),
    path('logout/', views.Logout, name='Logout'),
    path('postulacion/revisar/<int:postulacion_id>/', views.cambiar_estado, name='cambiar_estado'),
    path('estado/', estado, name='estado'),
    path('eliminar_postulacion/<int:postulacion_id>/', views.eliminar_postulacion, name='eliminar_postulacion'),
    
]
