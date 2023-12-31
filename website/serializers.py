from rest_framework import serializers
from .models import Roles, Predmet, Mugalim, Class, Okuuchular, Raspisanie, Posishenie, Janylyktar
from .models import CustomUser



class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'

class PredmetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predmet
        fields = '__all__'


class MugalimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mugalim
        fields = '__all__'

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'
class OkuuchularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Okuuchular
        fields = '__all__'
class RaspisanieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raspisanie
        fields = '__all__'
class PosishenieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posishenie
        fields = '__all__'
class JanylyktarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Janylyktar
        fields = '__all__'



#register
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password')  # Укажите поля, которые нужно сериализовать
        extra_kwargs = {'password': {'write_only': True}}