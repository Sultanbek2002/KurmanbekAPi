from rest_framework import viewsets
from .models import Roles, Predmet, Mugalim, Class, Okuuchular, Raspisanie, Posishenie, Janylyktar
from .serializers import RolesSerializer, PredmetSerializer, MugalimSerializer, ClassSerializer, OkuuchularSerializer, RaspisanieSerializer, PosishenieSerializer, JanylyktarSerializer

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

