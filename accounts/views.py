from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from pedidos.models import Orden
from pedidos.serializers import OrdenClienteSerializer
from rest_framework.permissions import  IsAuthenticated
from datetime import *
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse


def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request, '404.html', data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [IsAuthenticated]

class Vendedor(APIView):
    def get(self, request, format=None):
        my_user = User.objects.all().get(id=request.user.id)
        serializer = UserSerializer(my_user)
        return Response(serializer.data)



class MyUser(ListAPIView):
    serializer_class=OrdenClienteSerializer
    #permission_classes = [IsAuthenticated]
    def get_queryset(self, *args, **kwargs):
        queryset_list = Orden.objects.all().filter(vendedor=self.request.user.id)
        #queryset_list = super(MyUser, self).get_queryset(*args, **kwargs)
        #queryset        =Orden.objects.all() esta sentencia es lo mismo que la a terior
        search = self.request.GET.get('s')
        if search:
            queryset_list = queryset_list.filter(
                Q(numerodeorden__icontains=search)|
               Q(cliente__NOMBRE__icontains=search)
        )
        return queryset_list



class Myorders(ListAPIView):
    ##queryset = Orden.objects.all()
    serializer_class=OrdenClienteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        año=datetime.now().year
        print(año)
        queryset_list = Orden.objects.all().filter(Q(vendedor=self.request.user),Q(fechageneracion__year=año))
        #queryset_list = super(MyUser, self).get_queryset(*args, **kwargs)
        #queryset        =Orden.objects.all() esta sentencia es lo mismo que la a terior
        status = self.request.GET.get('s')
        if status:
            queryset_list = queryset_list.filter(
                Q(status__icontains=status)
            )
            return queryset_list




