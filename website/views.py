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




class RolesViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    permission_classes = [IsAuthenticated] 

class PredmetViewSet(viewsets.ModelViewSet):
    queryset = Predmet.objects.all()
    serializer_class = PredmetSerializer
    permission_classes = [IsAuthenticated]     

class MugalimViewSet(viewsets.ModelViewSet):
    queryset = Mugalim.objects.all()
    serializer_class = MugalimSerializer
    permission_classes = [IsAuthenticated] 
class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticated] 
class OkuuchularViewSet(viewsets.ModelViewSet):
    queryset = Okuuchular.objects.all()
    serializer_class = OkuuchularSerializer
    permission_classes = [IsAuthenticated] 
class RaspisanieViewSet(viewsets.ModelViewSet):
    queryset = Raspisanie.objects.all()
    serializer_class = RaspisanieSerializer
    permission_classes = [IsAuthenticated] 
class PosishenieViewSet(viewsets.ModelViewSet):
    queryset = Posishenie.objects.all()
    serializer_class = PosishenieSerializer
    permission_classes = [IsAuthenticated] 
class JanylyktarViewSet(viewsets.ModelViewSet):
    queryset = Janylyktar.objects.all()
    serializer_class = JanylyktarSerializer
    permission_classes = [IsAuthenticated] 


##token register
class RegisterUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        refresh = RefreshToken.for_user(user)
        response_data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
        return Response(response_data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        return serializer.save()