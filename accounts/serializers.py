from  django.contrib.auth.models import User
from rest_framework import serializers
from pedidos.serializers import OrdenClienteSerializer



class UserSerializer(serializers.ModelSerializer):
    orden=OrdenClienteSerializer(many=True, read_only=True)
    password=serializers.CharField(write_only=True)
    class Meta:
        model= User
        fields=['username', 'email', 'password', 'id', 'orden']

    def create(self, validated_data):
        password=validated_data.pop('password')
        user=User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        return  user
