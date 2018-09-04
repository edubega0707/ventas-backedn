from django.urls import path
from .views import ClienteListView,TarifaListView, OrdenListView, ClienteCreateView,OrdendesDetail,Pdf,OrdenAprobar,AprobarListOrdenView,OrdenValidar, OrdenSurtir,ClienteUpdate,ClienteDetail

app_name = 'pedidos'
urlpatterns = [
    path('nuevo/',ClienteCreateView.as_view(),name='addcliente'),
    path('clientes/',ClienteListView.as_view(),name='clientes'),
    path('tarifas',TarifaListView.as_view(),name='tarifas'),
    path('ordenes/', OrdenListView.as_view(), name='ordenlist' ),
    path('verdetalle/<int:id>/',OrdendesDetail.as_view(),name='verdetalle'),
    path('pdf/<int:id>/', Pdf.as_view(),name='detalle'),
    path('aprobar/<int:id>', OrdenAprobar.as_view(), name="aprobar"),
    path('validar/<int:id>', OrdenValidar.as_view(), name="validar"),
    path('surtir/<int:id>', OrdenSurtir.as_view(), name="surtir"),
    path('listageneradas/', AprobarListOrdenView.as_view(), name='vergenerada'),
    path('detalle/<int:pk>/',ClienteDetail.as_view(),name='detallecliente'),
    path('update/<int:pk>/',ClienteUpdate.as_view(),name='editarcliente'),
]


