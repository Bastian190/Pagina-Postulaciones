from django.urls import path
from .views import home,subvencion,Aporte,Fondeporte,fondeve,Login,Registro,formulario_subvencion

urlpatterns = [
    path('',home,name="home"),
    path('subvencion',subvencion,name="subvencion"),
    path('Aporte',Aporte,name="Aporte"),
    path('Fondeporte',Fondeporte,name="Fondeporte"),
    path('fondeve',fondeve,name="fondeve"),
    path('Login',Login,name="Login"),
    path('Registro',Registro,name="Registro"),
    path('formulario_subvencion/',formulario_subvencion, name='formulario_subvencion'), 
]
