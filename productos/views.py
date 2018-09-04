from django.shortcuts import render
from .models import Tarifa
from .serializers import Tarifaserializer,CreditoTarifaserializer,AnticipadoTarifaserializer
from rest_framework import viewsets,permissions
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class TarifaView(viewsets.ModelViewSet):
    queryset         = Tarifa.objects.all()
    serializer_class = Tarifaserializer
    permissions_class=(permissions.IsAuthenticated,)

class CreditoTarifaView(viewsets.ModelViewSet):
    queryset         = Tarifa.objects.all()
    serializer_class = CreditoTarifaserializer

class AnticipadoTarifaView(viewsets.ModelViewSet):
    queryset = Tarifa.objects.all()
    serializer_class = AnticipadoTarifaserializer

class Tarifalistview(LoginRequiredMixin,ListView):
    model = Tarifa
    template_name = "pedidos/tarifas/tarifa_list.html"