from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from rest_framework import routers
from rest_framework.authtoken import views
from accounts.views import UserViewSet, MyUser,Myorders, Vendedor
from productos.views import TarifaView,CreditoTarifaView,AnticipadoTarifaView
from pedidos.views import (
ClienteViewSet,
OrdenViewSet,
PedidoViewSet,
ContadoTarifaView,
OrdenesVendedorView,
MisOrdenesView,
OrdenDetail,
DomiciliosViewSet,
UploadedImagesViewSet,
UploadedImagesdosViewSet
)
from productos import urls as productos_urls
from catalogo import urls as catalogo_urls
from accounts import urls as accounts_urls
from pedidos import urls as pedidos_urls

router = routers.DefaultRouter()
router.register('productos', TarifaView)
router.register('users', UserViewSet)
router.register('clientes',ClienteViewSet)
router.register('ordenes', OrdenViewSet)
router.register('pedidos',PedidoViewSet)
router.register('misordenes',OrdenesVendedorView)
router.register('domicilios', DomiciliosViewSet)
router.register('images', UploadedImagesViewSet, 'images')
router.register('imagesdos', UploadedImagesdosViewSet, 'imagesdos')
#serializers que no sirven

#router.register('credito',CreditoTarifaView)
#router.register('contado',ContadoTarifaView)
#router.register('anticipado',AnticipadoTarifaView)
#router.register('categories', CategoryViewSet)
#router.register('pedidotestnousar',PedidoViewSet)



urlpatterns = [
    path('', include(catalogo_urls, namespace='index')),
    path('accounts/', include(accounts_urls, namespace='accounts')),
    path('pedidos/', include(pedidos_urls, namespace='pedidos')),
    path('nfh/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('vendedor/', Vendedor.as_view()),
    path('my_user/', MyUser.as_view()),
    path('my_orders/', Myorders.as_view()),
    url(r'^ordenes/(?P<pk>[0-9]+)/$', OrdenDetail.as_view()),
    path('sellers/', include(router.urls)),
    path('producs/',include(productos_urls, namespace='productos')),
    url(
        regex=r'^exp/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root': settings.MEDIA_ROOT}
    ),
]