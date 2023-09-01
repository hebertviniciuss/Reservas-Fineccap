"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from finecap.views import criar_reserva, reserva_editar, reserva_remover, reserva_detalhar, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('criar_reserva', criar_reserva, name='criar_reserva'),
    path('reserva_remover/<int:id>/', reserva_remover, name='reserva_remover'),
    path('reserva_editar/<int:id>/', reserva_editar, name='reserva_editar'),
    path('reserva_detalhar/<int:id>/', reserva_detalhar, name='reserva_detalhar'),
]
