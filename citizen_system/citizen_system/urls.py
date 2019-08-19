"""citizen_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include

from main_system.views import add_citizen_group, update_citizen, get_imports_citizens, get_presents_amount, \
    get_towns_stat

urlpatterns = [
    path('admin/', admin.site.urls),
    path('imports', add_citizen_group),
    path('imports/<int:import_id>/citizens/<int:citizen_id>', update_citizen),
    path('imports/<int:import_id>/citizens', get_imports_citizens),
    path('imports/<int:import_id>/citizens/birthdays', get_presents_amount),
    path('imports/<int:import_id>/towns/stat/percentile/age', get_towns_stat),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
