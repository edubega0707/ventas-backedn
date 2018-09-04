from .models import Cliente,Tarifa,Orden,Pedido,DomCliente, Archivo,Archivodos
from .serializers import ClienteSerializer,OrdenSerializer,PedidoArticulosSerializer,ContadoTarifaserializer,OrdenClienteSerializer, DomicilioSerializer, ArchivoSerializer,ArchivodosSerializer

from rest_framework import viewsets,permissions
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Permission, User
from django.urls import reverse_lazy
from rest_framework.response import Response
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    UpdateView,
    DetailView,
    View
)
from django.db.models import Q
from .forms import FormAprobar, FormValidar, FormSurtir, FormCliente
from django.shortcuts import render
from nfh.utileria import Render
from django.http import Http404

app_name='pedidos'

################################################### PDF  #############

class Pdf(LoginRequiredMixin, DetailView):
    def get(self,request,id):
        queryorden =Orden.objects.get(id=id)
        query=Pedido.objects.select_related().filter(orden_id=id)
        template_name = 'pedidos/orden/pdf.html'
        contexto={
            'pedido':query,
            'object':queryorden,
            'request':request
        }
        return Render.render(template_name,contexto)

#############################Views genericas para los paneles######

class TarifaListView(LoginRequiredMixin, ListView):
    template_name = 'pedidos/tarifas/tarifa_list.html'
    model = Tarifa


class ClienteListView(LoginRequiredMixin, ListView):
    template_name = 'pedidos/clientes/cliente_list.html'
    model = Cliente


class OrdenListView(LoginRequiredMixin, ListView):
    template_name = 'pedidos/orden/orden_list.html'
    model = Orden

#class ClienteCreateView(LoginRequiredMixin, CreateView):
 #   template_name = 'pedidos/clientes/cliente_form.html'
  #  model = Cliente
   # fields = '__all__'
    #success_url = reverse_lazy('pedidos:clientes')



#########################CREAR  USUARIO#############################
class ClienteCreateView(LoginRequiredMixin, View):
    template_name = 'pedidos/clientes/cliente_form.html'

    def get(self, request):
        form = FormCliente
        context = {
            'form': form,
        }
        return render(request, self.template_name, context)


    def post(self, request):
        form = FormCliente(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedidos:clientes')
        else:
            return render(request, self.template_name, {'form': form} )




class OrdendesDetail(LoginRequiredMixin, DetailView):
    def get(self,request,id):
        query=Orden.objects.get(id=id)
        pedido= Pedido.objects.select_related().filter(orden_id=id)
        archivos=Archivo.objects.all().filter(orden_id=id)
        archivodos=Archivodos.objects.all().filter(orden_id=id)
        template_name='pedidos/orden/orden_detail.html'
        context={
            'object':query,
            'pedido':pedido,
            'archivos':archivos,
            'archivodos':archivodos
        }
        return render(request,template_name,context)

#######################Vistas para validar, aprovar, surtir y modificar##########
class OrdenAprobar(LoginRequiredMixin,View):
    def get(self, request, id):
        template_name="pedidos/orden/orden_aprobar.html"
        query=Orden.objects.get(id=id)
        setquery = Orden.objects.get(id=id)
        archivos = Archivo.objects.all().filter(orden_id=id)
        archivodos = Archivodos.objects.all().filter(orden_id=id)
        form=FormAprobar(instance=query)
        context={
            'form':form,
            'setquery':setquery,
            'archivos': archivos,
            'archivodos': archivodos
        }
        return render(request,template_name,context)
    def post(self,request,id):
        query=Orden.objects.get(id=id)
        form=FormAprobar(request.POST, instance=query)
        if form.is_valid:
            form.save()
            return redirect('pedidos:vergenerada')
        else:
            return render(request, 'pedidos/orden/orden_aprobar.html', {'form':form})

class ClienteUpdate(LoginRequiredMixin,UpdateView):
    model = Cliente
    fields = ['NOMBRE','DIRECCIÓN','COLONIA','POBLACIÓN','MUNICIPIO','CP','RFC','TELÉFONO','CORREO']
    template_name = 'pedidos/clientes/cliente_form.html'

class ClienteDetail(DetailView):
    model = Cliente
    template_name = 'pedidos/clientes/cliente_detail.html'

#######################Vistas para validar##########
class OrdenValidar(LoginRequiredMixin,View):
    def get(self, request, id):
        template_name="pedidos/orden/orden_validar.html"
        query=Orden.objects.get(id=id)
        setquery = Orden.objects.get(id=id)
        archivos = Archivo.objects.all().filter(orden_id=id)
        archivodos=Archivodos.objects.all().filter(orden_id=id)
        form=FormValidar(instance=query)
        context={
            'form':form,
            'setquery':setquery,
            'archivos':archivos,
            'archivodos':archivodos
        }
        return render(request,template_name,context)

    def post(self,request,id):
        query=Orden.objects.get(id=id)
        form=FormValidar(request.POST, instance=query)
        if form.is_valid:
            form.save()
        return redirect('accounts:profile')


#######################Vistas para surtir##########
class OrdenSurtir(LoginRequiredMixin,View):
    def get(self, request, id):
        template_name="pedidos/orden/orden_surtir.html"
        query=Orden.objects.get(id=id)
        setquery = Orden.objects.get(id=id)
        form=FormSurtir(instance=query)
        context={
            'form':form,
            'setquery':setquery
        }
        return render(request,template_name,context)

    def post(self,request,id):
        query=Orden.objects.get(id=id)
        form=FormSurtir(request.POST, instance=query)
        if form.is_valid:
            form.save()
        return redirect('accounts:profile')





class AprobarListOrdenView(LoginRequiredMixin, View):
    def get(self,request):
        template_name = 'pedidos/orden/orden_list_aprobar.html'
        object_list=Orden.objects.all().filter(status='g')
        context={
            'object_list':object_list
        }
        return render(request,template_name,context)
#######################serializadores################################



class ClienteViewSet(viewsets.ModelViewSet):
    queryset        =Cliente.objects.all()
    serializer_class=ClienteSerializer
    def get_queryset(self, *args, **kwargs):
        search = self.request.GET.get('s')
        queryset_list = super(ClienteViewSet, self).get_queryset()
        if search:
            queryset_list = queryset_list.filter(
                Q(NOMBRE__icontains=search)
            ).distinct()

        return queryset_list



class OrdenViewSet(ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer


class OrdenDetail(APIView):
    """
     Obtenemos, el detalle de la orden
    """
    def get_object(self, pk):
        try:
            return Orden.objects.get(pk=pk)
        except Orden.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        orden=self.get_object(pk)
        serializer=OrdenClienteSerializer(orden)
        return Response(serializer.data)




class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoArticulosSerializer



############Serializer para lalo#######

class ContadoTarifaView(viewsets.ModelViewSet):
    queryset = Tarifa.objects.all()
    serializer_class = ContadoTarifaserializer




############Serializador ORDENES DE CADA VENDEDOR#####
class OrdenesVendedorView(viewsets.ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenClienteSerializer





class MisOrdenesView(APIView):
    def get(self,request, format=None):
        mis_ordenes=Orden.objects.all().filter(vendedor=request.user.id)
        serializer=OrdenClienteSerializer

    def get_queryset(self, *args, **kwargs):
        search = self.request.GET.get('s')
        queryset_list = super(MisOrdenesView, self).get_queryset()
        if search:
            queryset_list = queryset_list.filter(
                Q(numerodeorden__icontains=search)
            ).distinct()
        return queryset_list




class DomiciliosViewSet(viewsets.ModelViewSet):
    queryset = DomCliente.objects.all()
    serializer_class =DomicilioSerializer

    def get_queryset(self, *args, **kwargs):
        cliente = self.request.GET.get('cli')
        queryset_list = super(DomiciliosViewSet, self).get_queryset()
        if cliente:
            queryset_list = queryset_list.filter(cliente=cliente)

        return queryset_list


class UploadedImagesViewSet(viewsets.ModelViewSet):
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer

class UploadedImagesdosViewSet(viewsets.ModelViewSet):
    queryset = Archivodos.objects.all()
    serializer_class = ArchivodosSerializer