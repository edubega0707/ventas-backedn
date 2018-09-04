from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from catalogo import urls as catalogo_urls
from django.views.static import serve


from accounts import urls as accounts_urls
from pedidos import urls as pedidos_urls


urlpatterns = [
    path('', include(catalogo_urls, namespace='productos')),
    path('admin/', admin.site.urls),
    path('accounts/', include(accounts_urls, namespace='accounts')),
    path('pedidos/', include(pedidos_urls, namespace='pedidos')),

    url('^searchableselect/', include('searchableselect.urls')),
    url(
        regex=r'^exp/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root': settings.MEDIA_ROOT},
    ),

]
