
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
from django.urls import path
from django.views.generic import TemplateView
from .import views
from .views import *

app_name = 'landing'

urlpatterns = [
    #path('', include('django.contrib.auth.urls')),
    path('', views.landing, name='landing'),
    path('test', views.test, name='test'),
    #path('listaciudades', views.listaciudades, name='listaciudades'),
    path('test_slider', views.test_slider, name='test_slider'),
    path('ajax/get_ciudades/', views.get_ciudades, name='get_ciudades'),


]
