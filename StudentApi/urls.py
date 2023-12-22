"""
URL configuration for StudentApi project.

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
from website.views import *
from django.urls import path, include
from rest_framework import routers
from website.views import RolesViewSet, PredmetViewSet, MugalimViewSet, ClassViewSet, OkuuchularViewSet, RaspisanieViewSet, PosishenieViewSet, JanylyktarViewSet

router = routers.DefaultRouter()
router.register(r'roles', RolesViewSet)
router.register(r'predmets', PredmetViewSet)
router.register(r'mugalims', MugalimViewSet)
router.register(r'classes', ClassViewSet)
router.register(r'okuuchulars', OkuuchularViewSet)
router.register(r'raspisanies', RaspisanieViewSet)
router.register(r'posishenies', PosishenieViewSet)
router.register(r'janylyktars', JanylyktarViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),    
]
