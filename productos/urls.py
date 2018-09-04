from django.urls import path
from .views import Tarifalistview

app_name = 'productos'
urlpatterns = [
    path('lista/',Tarifalistview.as_view(),name='tarifa'),
]