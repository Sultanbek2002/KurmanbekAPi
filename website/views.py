from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Roles, Predmet, Mugalim, Class, Okuuchular, Raspisanie, Posishenie, Janylyktar
from .serializers import RolesSerializer, PredmetSerializer, MugalimSerializer, ClassSerializer, OkuuchularSerializer, RaspisanieSerializer, PosishenieSerializer, JanylyktarSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer
from .models import *
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

@csrf_exempt
def LoginTeacher(request):
    print(request.POST)
    if request.method == "POST":
        login = request.POST["login"]
        password = request.POST["password"]
        print(login,"-",password)
        try:
            mugalim = Mugalim.objects.get(login=login)
            if mugalim.password == password:
                print("success!!!")
                return HttpResponse(status=200)
            else:
                return HttpResponse("Неверный пароль", status=401)
        except ObjectDoesNotExist:
            return HttpResponse("Пользователь с таким логином не найден", status=404)
    return HttpResponse("Авторизация")



        
@csrf_exempt
def LoginStudent(request):
    if request.method == "POST":
        login = request.POST.get("login")
        password = request.POST.get("password")
        try:
            mugalim = Okuuchular.objects.get(login=login)
            if mugalim.password == password:
                print("success!!!")
                return HttpResponse(status=200)
            else:
                return HttpResponse("Неверный пароль", status=401)
        except ObjectDoesNotExist:
            return HttpResponse("Пользователь с таким логином не найден", status=404)
    return HttpResponse("Авторизация")



class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    

class PredmetViewSet(viewsets.ModelViewSet):
    queryset = Predmet.objects.all()
    serializer_class = PredmetSerializer

class MugalimViewSet(viewsets.ModelViewSet):
    queryset = Mugalim.objects.all()
    serializer_class = MugalimSerializer
class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
class OkuuchularViewSet(viewsets.ModelViewSet):
    queryset = Okuuchular.objects.all()
    serializer_class = OkuuchularSerializer
class RaspisanieViewSet(viewsets.ModelViewSet):
    queryset = Raspisanie.objects.all()
    serializer_class = RaspisanieSerializer
class PosishenieViewSet(viewsets.ModelViewSet):
    queryset = Posishenie.objects.all()
    serializer_class = PosishenieSerializer
class JanylyktarViewSet(viewsets.ModelViewSet):
    queryset = Janylyktar.objects.all()
    serializer_class = JanylyktarSerializer

    # permission_classes = [IsAuthenticated] 


##token register
# class RegisterUserView(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = self.perform_create(serializer)
#         refresh = RefreshToken.for_user(user)
#         response_data = {
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         }
#         return Response(response_data, status=status.HTTP_201_CREATED)

#     def perform_create(self, serializer):
#         return serializer.save()