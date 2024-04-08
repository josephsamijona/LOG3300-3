"""
URL configuration for gestion_employes project.

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
from employees import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),
    path('gestion/', views.gestion, name='gestion'),
    path('employee/', views.employee, name='employee'),
    path('ajouter-departement/', views.ajouter_departement, name='ajouter_departement'),
    path('ajouter-employee/', views.ajouter_employee, name='ajouter_employee'),
    path('update_department/<int:pk>/', views.update_department, name='update_department'),
    path('delete_department/<int:pk>/', views.delete_department, name='delete_department'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)