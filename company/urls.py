"""
URL configuration for company project.

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
from gestion_employes import views

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path('adminlogin/', views.admin_logins, name='admin_logins'),
    path('adminsignup/', views.admin_signup, name='admin_signup'),
    path('adminlogout/', views.admin_logout, name='admin_logout'),
    path('admindashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('adminsecurity/', views.admin_security, name='admin_security'),
    path('adminusermanage/', views.admin_usermanage, name='admin_usermanage'),
    path('adminsetting/', views.admin_setting, name='admin_setting'),
    path('adminnotif/', views.admin_notif, name='admin_notif'),
    path('adminnotifmessageread/', views.admin_notif_message_read, name='admin_notif_message_read'),
    path('adminnotifmessage/', views.admin_notif_message, name='admin_notif_message'),
    path('adminsecurityblocked/', views.admin_security_blocked, name='admin_security_blocked'),
    path('adminsecurity/offline/', views.admin_security_offline, name='admin_security_offline'),
    path('adminusermanageedit/', views.admin_usermanage_edit, name='admin_usermanage_edit'),
    path('adminusermanageinput/', views.admin_usermanage_input, name='admin_usermanage_input'),
    path('adminusermanage/', views.admin_usermanage, name='admin_usermanage'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('doctor/', views.doctor, name='doctor'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('treatment/', views.treatment, name='treatment'),
]
