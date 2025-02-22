"""homebanking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from login import views as login_views
from clientes import views
from django.conf import settings
from django.conf.urls.static import static
from tarjetas import views as tarjetas_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_views.login, name="login"),
    path('clientes/', login_views.login, name="clientes"),
    path('tarjetas/', tarjetas_views.Tarjeta, name="tarjetas")
    

    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
