from django.urls import path
from .views import ProductoListView,DescargaView,MnualView,RecursosView,Productoback,Productodetail,Productoadd,Categoriaadd,Productomodificar


app_name="catalogo"
urlpatterns=[
    path('', ProductoListView.as_view(),name='lista'),
    path('descarga/',DescargaView.as_view(),name='app'),
    path('manuales/',MnualView.as_view(),name='manual'),
    path('recursos/', RecursosView.as_view(), name='recursos'),
    path('catalogo/', Productoback.as_view(), name='catalogogeneral'),
    path('catproducto/<int:pk>/',Productodetail.as_view(),name='detalle'),
    path('addproducto/',Productoadd.as_view(),name='nuevo'),
    path('addcategoria/',Categoriaadd.as_view(),name='nueva'),
    path('editar/<int:pk>/',Productomodificar.as_view(),name='modificar'),
]