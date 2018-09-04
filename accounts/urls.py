from django.urls import path
from django.contrib.auth import views as logViews
from .viewsdos import(
HomeAdminView,
LogView,
#RegistroVendedor,
UsuarioVendedorCreate,
UsuarioCajeroCreate,
UsuarioSurtidorCreate,
VendedoresListView,
BienbenidaView,
ContadorView,
UsuarioValidadorCreate,
)


#si vamos a  agregar include especifiquemos el nombre de la app
app_name='accounts'

urlpatterns = [
    #path('', include(catalogo_urls, namespace='productos')),
    path('',LogView.as_view(),name='sesion'),
    path('login/', LogView.as_view(), name='login'),
	path('logout/', logViews.logout, name='logout'),
    path('profile/', HomeAdminView.as_view(), name='profile'),
    path('addvendedor/',UsuarioVendedorCreate.as_view(),name='registrarvendedor'),
    path('addcajero/',UsuarioCajeroCreate.as_view(),name='registrarcajero'),
    path('addsurtidor/',UsuarioSurtidorCreate.as_view(),name='registrasurtidor'),
    path('listavendedor/',VendedoresListView.as_view(),name='listavendedores'),
    path('bienvenida/',BienbenidaView.as_view(),name='bienvenida'),
    path('dashboard/',ContadorView.as_view(),name='dashboard'),
    path('addvalidador/',UsuarioValidadorCreate.as_view(),name='registravalidador'),

]
