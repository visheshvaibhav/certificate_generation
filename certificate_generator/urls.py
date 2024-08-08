"""
URL configuration for certificate_generator project.

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
from django.urls import path, include
from certificate_app import views  # Import the views module from your app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.generate_certificate, name='generate_certificate'),  # Add this line for the root path
    path('generate_certificate/', views.generate_certificate, name='generate_certificate'),
    path('', include('certificate_app.urls')),
    # Add other URL patterns here if needed
]
