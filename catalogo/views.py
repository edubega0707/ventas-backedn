from django.views.generic import ListView,TemplateView,DetailView,CreateView,UpdateView,View
from django.shortcuts import render, redirect
from .models import Producto,Categoria
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

#from .forms import FormProductos

class ProductoListView(ListView):
    model = Producto

class DescargaView(LoginRequiredMixin,TemplateView):
    template_name='pedidos/catalogo/descarga.html'

class MnualView(LoginRequiredMixin,TemplateView):
    template_name='pedidos/catalogo/capacitacion.html'


class RecursosView(LoginRequiredMixin,TemplateView):
    template_name="pedidos/catalogo/recursos.html"

##Views para el backend

class Productoback(LoginRequiredMixin,View):
    def get(self, request):
        template_name = 'pedidos/catalogo/catologo_list.html'
        query=Producto.objects.all()
        context={
            'object_list':query
        }
        return render(request,template_name,context)


class Productodetail(LoginRequiredMixin,DetailView):
    model = Producto
    template_name = 'pedidos/catalogo/catalogo_detail.html'

class Productoadd(LoginRequiredMixin,CreateView):
    model = Producto
    template_name = 'pedidos/catalogo/catalogo_create.html'
    fields = '__all__'




class Productomodificar(LoginRequiredMixin,UpdateView):
    model = Producto
    template_name = 'pedidos/catalogo/catalogo_create.html'
    fields = '__all__'

class Categoriaadd(LoginRequiredMixin,CreateView):
    model = Categoria
    template_name = 'pedidos/catalogo/catalogo_create.html'
    fields = '__all__'