from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Permission, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.contrib.auth import views as auth_views
from django.views.generic import (
    ListView,
    View,
    TemplateView,
)

from pedidos.models import Tarifa, Orden


from .forms import FormUsuario



########################### INICIO DE SESION###########################
class LogView(auth_views.LoginView):
    template_name="pedidos/registration/login.html"

class HomeAdminView(View):
    @method_decorator(login_required)
    #@method_decorator(permission_required('accounts.administrador'))
    def get(self, request):
        usuario=get_object_or_404(User, username=request.user)

        if usuario.is_superuser==False:
            if usuario.has_perm('pedidos.vendedor'):
                template_name = 'pedidos/vendedor.html'
                context = {

                }
                return render(request, template_name, context)


            elif usuario.has_perm('pedidos.cajero'):
                return redirect('pedidos:clientes')


            elif usuario.has_perm('pedidos.surtidor'):
                template_name = 'pedidos/surtidor.html'
                ordenes = Orden.objects.filter(
                    Q(tipoorden="CONTADO") | Q(tipoorden="CREDITO"),
                    Q(status="a")
                )
                ordenesdos=Orden.objects.filter(Q(status="v"), Q(tipoorden='ANTICIPADO'))
                ordenes_surtidas=Orden.objects.all().filter(Q(status="s")| Q(status='i'))
                context = {
                    'ordenes': ordenes,
                    'ordenesdos' : ordenesdos,
                    'ordenes_surtidas':ordenes_surtidas
                }

                return render(request, template_name, context)


            elif usuario.has_perm('pedidos.validador'):
                template_name = 'pedidos/validador.html'
                #ordenes             =Orden.objects.all().filter(status='g')
                ordenes_validadas   =Orden.objects.all().filter(status="v")
                ordenes_surtidas    =Orden.objects.all().filter(Q(tipoorden='ANTICIPADO'), (Q(status="s")|Q(status="i")))
                ordenes = Orden.objects.filter(Q(status="a"), Q(tipoorden='ANTICIPADO'))
                context = {
                        'ordenes':ordenes,
                        'ordenes_validadas':ordenes_validadas,
                        'ordenes_surtidas':ordenes_surtidas
                }
                return render(request, template_name, context)


        else:
            return redirect('pedidos:vergenerada')


############################AGREGAR VENDEDOR#############################
class UsuarioVendedorCreate(LoginRequiredMixin, View):
    template_name = 'pedidos/registration/add_vendedor.html'

    def get(self, request):
        permiso = Permission.objects.get(codename='vendedor')
        usuarios = permiso.user_set.all()
        form = FormUsuario
        context = {
            'form': form,
            'usuarios':usuarios
        }
        return render(request, self.template_name, context)


    def post(self, request):
        form = FormUsuario(request.POST)
        resetform = FormUsuario
        permiso = Permission.objects.get(codename='vendedor')
        usuarios = permiso.user_set.all()

        if form.is_valid():
            user = form.cleaned_data['username']
            form.save()

            usuario = get_object_or_404(User, username=user)
            permission = Permission.objects.get(codename='vendedor')
            usuario.user_permissions.add(permission)


            return render(request, self.template_name, {'form':resetform, 'usuarios':usuarios} )
        else:
            return render(request, self.template_name, {'form':form, 'usuarios':usuarios})


########################### Registro de Cajeros###########################
class UsuarioCajeroCreate(LoginRequiredMixin, View):
    template_name = 'pedidos/registration/add_cajero.html'

    def get(self, request):
        permiso = Permission.objects.get(codename="cajero")
        usuarios = permiso.user_set.all()
        form = FormUsuario
        context = {
            'form': form,
            'usuarios': usuarios
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = FormUsuario(request.POST)
        resetform = FormUsuario
        permiso = Permission.objects.get(codename="cajero")
        usuarios = permiso.user_set.all()

        if form.is_valid():
            user = form.cleaned_data['username']
            form.save()

            usuario = get_object_or_404(User, username=user)
            permission = Permission.objects.get(codename='cajero')
            usuario.user_permissions.add(permission)

            return render(request, self.template_name, {'form':resetform,'usuarios':usuarios})
        else:
            return render(request, self.template_name, {'form': form, 'usuarios':usuarios})


########################### Registro de Surtidor###########################
class UsuarioSurtidorCreate(LoginRequiredMixin, View):
    template_name = 'pedidos/registration/add_surtidor.html'

    def get(self, request):
        permiso = Permission.objects.get(codename="surtidor")
        usuarios = permiso.user_set.all()
        form = FormUsuario
        context = {
            'form': form,
            'usuarios': usuarios
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = FormUsuario(request.POST)
        resetform = FormUsuario
        permiso = Permission.objects.get(codename="surtidor")
        usuarios = permiso.user_set.all()

        if form.is_valid():
            user = form.cleaned_data['username']
            form.save()

            usuario = get_object_or_404(User, username=user)
            permission = Permission.objects.get(codename='surtidor')
            usuario.user_permissions.add(permission)

            return render(request, self.template_name, {'form':resetform,'usuarios':usuarios})
        else:
            return render(request, self.template_name, {'form': form, 'usuarios':usuarios})

######################################Crear validador#########################################
class UsuarioValidadorCreate(LoginRequiredMixin, View):
    template_name = 'pedidos/registration/add_validador.html'

    def get(self, request):
        permiso = Permission.objects.get(codename='validador')
        usuarios = permiso.user_set.all()
        form = FormUsuario
        context = {
            'form': form,
            'usuarios': usuarios
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = FormUsuario(request.POST)
        resetform = FormUsuario
        permiso = Permission.objects.get(codename='validador')
        usuarios = permiso.user_set.all()

        if form.is_valid():
            user = form.cleaned_data['username']
            form.save()

            usuario = get_object_or_404(User, username=user)
            permission = Permission.objects.get(codename='validador')
            usuario.user_permissions.add(permission)

            return render(request, self.template_name, {'form':resetform,'usuarios':usuarios})
        else:
            return render(request, self.template_name, {'form': form, 'usuarios':usuarios})

######################################List #################
class VendedoresListView(ListView):
    model = User
    template_name = "pedidos/registration/vendedores_list.html"

class BienbenidaView(TemplateView):
    template_name="pedidos/dashboard/bienvenida.html"

class ContadorView(TemplateView):
    template_name="pedidos/dashboard/contador_list.html"


