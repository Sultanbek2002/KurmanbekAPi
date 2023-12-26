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
from website.views import RolesViewSet, PredmetViewSet, MugalimViewSet, ClassViewSet, OkuuchularViewSet, RaspisanieViewSet, PosishenieViewSet, JanylyktarViewSet,LoginTeacher,LoginStudent
from rest_framework_simplejwt.views import (
    
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
router.register(r'roles', RolesViewSet)
router.register(r'add/predmet/', PredmetViewSet)
router.register(r'auth/v1/mu/register', MugalimViewSet)
router.register(r'add/klass/', ClassViewSet)
router.register(r'auth/v1/ok/register', OkuuchularViewSet)
router.register(r'add/raspisanie/', RaspisanieViewSet)
router.register(r'add/poshishenie/', PosishenieViewSet)
router.register(r'add/news/', JanylyktarViewSet)


urlpatterns = [
    # path('api/register/', RegisterUserView.as_view(), name='register_user'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
    path('auth/v1/mu/login',LoginTeacher,name='login'),
    path('auth/v1/ok/login',LoginStudent,name="loginstudent")
    # path('auth/v1/mu/register',registerTeacher,name='teachregister')   
]
